"""

This module defines the mpf, mpc classes, and standard functions for
operating with them.
"""
from __future__ import annotations
from builtins import str as basestring
import functools as functools
import gmpy2
from gmpy2.gmpy2 import _mpmath_create as from_man_exp
from gmpy2.gmpy2 import _mpmath_normalize as normalize
from gmpy2.gmpy2 import bit_length as bitcount
from gmpy2 import mpz as MPZ
import mpmath.ctx_base
from mpmath.ctx_base import StandardBaseContext
import mpmath.ctx_mp_python
from mpmath import ctx_mp_python as _mpf_module
from mpmath.ctx_mp_python import PythonMPContext as BaseMPContext
from mpmath.ctx_mp_python import _mpc
from mpmath.ctx_mp_python import _mpf
from mpmath.ctx_mp_python import mpnumeric
from mpmath import function_docs
from mpmath import libmp
from mpmath.libmp.libelefun import mpf_pow
from mpmath.libmp.libmpc import mpc_abs
from mpmath.libmp.libmpc import mpc_add
from mpmath.libmp.libmpc import mpc_add_mpf
from mpmath.libmp.libmpc import mpc_conjugate
from mpmath.libmp.libmpc import mpc_div
from mpmath.libmp.libmpc import mpc_div_mpf
from mpmath.libmp.libmpc import mpc_hash
from mpmath.libmp.libmpc import mpc_is_nonzero
from mpmath.libmp.libmpc import mpc_mpf_div
from mpmath.libmp.libmpc import mpc_mul
from mpmath.libmp.libmpc import mpc_mul_int
from mpmath.libmp.libmpc import mpc_mul_mpf
from mpmath.libmp.libmpc import mpc_neg
from mpmath.libmp.libmpc import mpc_pos
from mpmath.libmp.libmpc import mpc_pow
from mpmath.libmp.libmpc import mpc_pow_int
from mpmath.libmp.libmpc import mpc_pow_mpf
from mpmath.libmp.libmpc import mpc_sub
from mpmath.libmp.libmpc import mpc_sub_mpf
from mpmath.libmp.libmpc import mpc_to_complex
from mpmath.libmp.libmpc import mpc_to_str
from mpmath.libmp.libmpf import ComplexResult
from mpmath.libmp.libmpf import dps_to_prec
from mpmath.libmp.libmpf import from_float
from mpmath.libmp.libmpf import from_int
from mpmath.libmp.libmpf import from_pickable
from mpmath.libmp.libmpf import from_rational
from mpmath.libmp.libmpf import from_str
from mpmath.libmp.libmpf import gmpy_mpf_mul as mpf_mul
from mpmath.libmp.libmpf import gmpy_mpf_mul_int as mpf_mul_int
from mpmath.libmp.libmpf import mpf_abs
from mpmath.libmp.libmpf import mpf_add
from mpmath.libmp.libmpf import mpf_cmp
from mpmath.libmp.libmpf import mpf_div
from mpmath.libmp.libmpf import mpf_eq
from mpmath.libmp.libmpf import mpf_ge
from mpmath.libmp.libmpf import mpf_gt
from mpmath.libmp.libmpf import mpf_hash
from mpmath.libmp.libmpf import mpf_le
from mpmath.libmp.libmpf import mpf_lt
from mpmath.libmp.libmpf import mpf_mod
from mpmath.libmp.libmpf import mpf_neg
from mpmath.libmp.libmpf import mpf_pos
from mpmath.libmp.libmpf import mpf_pow_int
from mpmath.libmp.libmpf import mpf_rand
from mpmath.libmp.libmpf import mpf_rdiv_int
from mpmath.libmp.libmpf import mpf_sub
from mpmath.libmp.libmpf import mpf_sum
from mpmath.libmp.libmpf import prec_to_dps
from mpmath.libmp.libmpf import repr_dps
from mpmath.libmp.libmpf import to_fixed
from mpmath.libmp.libmpf import to_float
from mpmath.libmp.libmpf import to_int
from mpmath.libmp.libmpf import to_pickable
from mpmath.libmp.libmpf import to_str
from mpmath import rational
import re as re
import typing
__all__: list[str] = ['BACKEND', 'BaseMPContext', 'ComplexResult', 'MPContext', 'MPZ', 'MPZ_ONE', 'MPZ_ZERO', 'PrecisionManager', 'StandardBaseContext', 'basestring', 'bitcount', 'dps_to_prec', 'finf', 'fnan', 'fninf', 'fone', 'from_float', 'from_int', 'from_man_exp', 'from_pickable', 'from_rational', 'from_str', 'function_docs', 'functools', 'fzero', 'get_complex', 'int_types', 'libmp', 'mpc_abs', 'mpc_add', 'mpc_add_mpf', 'mpc_conjugate', 'mpc_div', 'mpc_div_mpf', 'mpc_hash', 'mpc_is_nonzero', 'mpc_mpf_div', 'mpc_mul', 'mpc_mul_int', 'mpc_mul_mpf', 'mpc_neg', 'mpc_pos', 'mpc_pow', 'mpc_pow_int', 'mpc_pow_mpf', 'mpc_sub', 'mpc_sub_mpf', 'mpc_to_complex', 'mpc_to_str', 'mpf_abs', 'mpf_add', 'mpf_cmp', 'mpf_div', 'mpf_eq', 'mpf_ge', 'mpf_gt', 'mpf_hash', 'mpf_le', 'mpf_lt', 'mpf_mod', 'mpf_mul', 'mpf_mul_int', 'mpf_neg', 'mpf_pos', 'mpf_pow', 'mpf_pow_int', 'mpf_rand', 'mpf_rdiv_int', 'mpf_sub', 'mpf_sum', 'mpnumeric', 'normalize', 'prec_to_dps', 'rational', 're', 'repr_dps', 'round_ceiling', 'round_floor', 'round_nearest', 'to_fixed', 'to_float', 'to_int', 'to_pickable', 'to_str']
class MPContext(mpmath.ctx_mp_python.PythonMPContext, mpmath.ctx_base.StandardBaseContext):
    """
    
    Context for multiprecision arithmetic with a global precision.
    """
    _exact_overflow_msg: typing.ClassVar[str] = 'the exact result does not fit in memory'
    _hypsum_msg: typing.ClassVar[str] = 'hypsum() failed to converge to the requested %i bits of accuracy\nusing a working precision of %i bits. Try with a higher maxprec,\nmaxterms, or set zeroprec.'
    @staticmethod
    def __init__(ctx):
        ...
    @staticmethod
    def __str__(ctx):
        ...
    @staticmethod
    def _agm(ctx, a, b = 1):
        ...
    @staticmethod
    def _altzeta_generic(ctx, *args, **kwargs):
        ...
    @staticmethod
    def _as_points(ctx, x):
        ...
    @staticmethod
    def _besselj(ctx, n, z):
        ...
    @staticmethod
    def _ci_generic(ctx, *args, **kwargs):
        ...
    @staticmethod
    def _convert_fallback(ctx, x, strings):
        ...
    @staticmethod
    def _coulomb_chi(ctx, *args, **kwargs):
        ...
    @staticmethod
    def _djacobi_theta2(ctx, z, q, nd):
        ...
    @staticmethod
    def _djacobi_theta2a(ctx, z, q, nd):
        """
        
        case ctx._im(z) != 0
        dtheta(2, z, q, nd) =
        j* q**1/4 * Sum(q**(n*n + n) * (2*n+1)*exp(j*(2*n + 1)*z), n=-inf, inf)
        max term for (2*n0+1)*log(q).real - 2* ctx._im(z) ~= 0
        n0 = int(ctx._im(z)/log(q).real - 1/2)
        """
    @staticmethod
    def _djacobi_theta3(ctx, z, q, nd):
        """
        nd=1,2,3 order of the derivative with respect to z
        """
    @staticmethod
    def _djacobi_theta3a(ctx, z, q, nd):
        """
        
        case ctx._im(z) != 0
        djtheta3(z, q, nd) = (2*j)**nd *
          Sum(q**(n*n) * n**nd * exp(j*2*n*z), n, -inf, inf)
        max term for minimum n*abs(log(q).real) + ctx._im(z)
        """
    @staticmethod
    def _djtheta(ctx, n, z, q, derivative = 1):
        ...
    @staticmethod
    def _ei_generic(ctx, *args, **kwargs):
        ...
    @staticmethod
    def _erf_complex(ctx, *args, **kwargs):
        ...
    @staticmethod
    def _erfc_complex(ctx, *args, **kwargs):
        ...
    @staticmethod
    def _expint_int(ctx, n, z):
        ...
    @staticmethod
    def _gamma3(ctx, z, a, b, regularized = False):
        ...
    @staticmethod
    def _gamma_upper_int(ctx, n, z):
        ...
    @staticmethod
    def _hurwitz(ctx, s, a = 1, d = 0, **kwargs):
        ...
    @staticmethod
    def _hyp0f1(ctx, b_s, z, **kwargs):
        ...
    @staticmethod
    def _hyp1f0(ctx, *args, **kwargs):
        ...
    @staticmethod
    def _hyp1f1(ctx, a_s, b_s, z, **kwargs):
        ...
    @staticmethod
    def _hyp1f2(ctx, a_s, b_s, z, **kwargs):
        ...
    @staticmethod
    def _hyp2f0(ctx, a_s, b_s, z, **kwargs):
        ...
    @staticmethod
    def _hyp2f1(ctx, a_s, b_s, z, **kwargs):
        ...
    @staticmethod
    def _hyp2f2(ctx, a_s, b_s, z, **kwargs):
        ...
    @staticmethod
    def _hyp2f3(ctx, a_s, b_s, z, **kwargs):
        ...
    @staticmethod
    def _hyp_borel(ctx, p, q, a_s, b_s, z, **kwargs):
        ...
    @staticmethod
    def _hypq1fq(ctx, p, q, a_s, b_s, z, **kwargs):
        """
        
        Evaluates 3F2, 4F3, 5F4, ...
        """
    @staticmethod
    def _is_complex_type(ctx, x):
        ...
    @staticmethod
    def _is_real_type(ctx, x):
        ...
    @staticmethod
    def _jacobi_theta2(ctx, z, q):
        ...
    @staticmethod
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
    @staticmethod
    def _jacobi_theta3(ctx, z, q):
        ...
    @staticmethod
    def _jacobi_theta3a(ctx, z, q):
        """
        
        case ctx._im(z) != 0
        theta3(z, q) = Sum(q**(n*n) * exp(j*2*n*z), n, -inf, inf)
        max term for n*abs(log(q).real) + ctx._im(z) ~= 0
        n0 = int(- ctx._im(z)/abs(log(q).real))
        """
    @staticmethod
    def _lower_gamma(ctx, z, b, regularized = False):
        ...
    @staticmethod
    def _nthroot(ctx, x, n):
        ...
    @staticmethod
    def _parse_prec(ctx, kwargs):
        ...
    @staticmethod
    def _rootof1(ctx, k, n):
        ...
    @staticmethod
    def _si_generic(ctx, *args, **kwargs):
        ...
    @staticmethod
    def _upper_gamma(ctx, z, a, regularized = False):
        ...
    @staticmethod
    def _zeta_int(ctx, n):
        ...
    @staticmethod
    def _zetasum(ctx, s, a, n, derivatives = [0], reflect = False):
        """
        
        Returns [xd0,xd1,...,xdr], [yd0,yd1,...ydr] where
        
        xdk = D^k     ( 1/a^s     +  1/(a+1)^s      +  ...  +  1/(a+n)^s     )
        ydk = D^k conj( 1/a^(1-s) +  1/(a+1)^(1-s)  +  ...  +  1/(a+n)^(1-s) )
        
        D^k = kth derivative with respect to s, k ranges over the given list of
        derivatives (which should consist of either a single element
        or a range 0,1,...r). If reflect=False, the ydks are not computed.
        """
    @staticmethod
    def _zetasum_fast(ctx, s, a, n, derivatives = [0], reflect = False):
        ...
    @staticmethod
    def absmax(ctx, x):
        ...
    @staticmethod
    def absmin(ctx, x):
        ...
    @staticmethod
    def acot(ctx, *args, **kwargs):
        """
        Computes the inverse cotangent of `x`,
        `\\mathrm{cot}^{-1}(x) = \\tan^{-1}(1/x)`.
        """
    @staticmethod
    def acoth(ctx, *args, **kwargs):
        """
        Computes the inverse hyperbolic cotangent of `x`,
        `\\mathrm{coth}^{-1}(x) = \\tanh^{-1}(1/x)`.
        """
    @staticmethod
    def acsc(ctx, *args, **kwargs):
        """
        Computes the inverse cosecant of `x`,
        `\\mathrm{csc}^{-1}(x) = \\sin^{-1}(1/x)`.
        """
    @staticmethod
    def acsch(ctx, *args, **kwargs):
        """
        Computes the inverse hyperbolic cosecant of `x`,
        `\\mathrm{csch}^{-1}(x) = \\sinh^{-1}(1/x)`.
        """
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def appellf1(ctx, *args, **kwargs):
        """
        
        Gives the Appell F1 hypergeometric function of two variables,
        
        .. math ::
        
            F_1(a,b_1,b_2,c,x,y) = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
                \\frac{(a)_{m+n} (b_1)_m (b_2)_n}{(c)_{m+n}}
                \\frac{x^m y^n}{m! n!}.
        
        This series is only generally convergent when `|x| < 1` and `|y| < 1`,
        although :func:`~mpmath.appellf1` can evaluate an analytic continuation
        with respecto to either variable, and sometimes both.
        
        **Examples**
        
        Evaluation is supported for real and complex parameters::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> appellf1(1,0,0.5,1,0.5,0.25)
            1.154700538379251529018298
            >>> appellf1(1,1+j,0.5,1,0.5,0.5j)
            (1.138403860350148085179415 + 1.510544741058517621110615j)
        
        For some integer parameters, the F1 series reduces to a polynomial::
        
            >>> appellf1(2,-4,-3,1,2,5)
            -816.0
            >>> appellf1(-5,1,2,1,4,5)
            -20528.0
        
        The analytic continuation with respect to either `x` or `y`,
        and sometimes with respect to both, can be evaluated::
        
            >>> appellf1(2,3,4,5,100,0.5)
            (0.0006231042714165329279738662 + 0.0000005769149277148425774499857j)
            >>> appellf1('1.1', '0.3', '0.2+2j', '0.4', '0.2', 1.5+3j)
            (-0.1782604566893954897128702 + 0.002472407104546216117161499j)
            >>> appellf1(1,2,3,4,10,12)
            -0.07122993830066776374929313
        
        For certain arguments, F1 reduces to an ordinary hypergeometric function::
        
            >>> appellf1(1,2,3,5,0.5,0.25)
            1.547902270302684019335555
            >>> 4*hyp2f1(1,2,5,'1/3')/3
            1.547902270302684019335555
            >>> appellf1(1,2,3,4,0,1.5)
            (-1.717202506168937502740238 - 2.792526803190927323077905j)
            >>> hyp2f1(1,3,4,1.5)
            (-1.717202506168937502740238 - 2.792526803190927323077905j)
        
        The F1 function satisfies a system of partial differential equations::
        
            >>> a,b1,b2,c,x,y = map(mpf, [1,0.5,0.25,1.125,0.25,-0.25])
            >>> F = lambda x,y: appellf1(a,b1,b2,c,x,y)
            >>> chop(x*(1-x)*diff(F,(x,y),(2,0)) +
            ...      y*(1-x)*diff(F,(x,y),(1,1)) +
            ...      (c-(a+b1+1)*x)*diff(F,(x,y),(1,0)) -
            ...      b1*y*diff(F,(x,y),(0,1)) -
            ...      a*b1*F(x,y))
            0.0
            >>>
            >>> chop(y*(1-y)*diff(F,(x,y),(0,2)) +
            ...      x*(1-y)*diff(F,(x,y),(1,1)) +
            ...      (c-(a+b2+1)*y)*diff(F,(x,y),(0,1)) -
            ...      b2*x*diff(F,(x,y),(1,0)) -
            ...      a*b2*F(x,y))
            0.0
        
        The Appell F1 function allows for closed-form evaluation of various
        integrals, such as any integral of the form
        `\\int x^r (x+a)^p (x+b)^q dx`::
        
            >>> def integral(a,b,p,q,r,x1,x2):
            ...     a,b,p,q,r,x1,x2 = map(mpmathify, [a,b,p,q,r,x1,x2])
            ...     f = lambda x: x**r * (x+a)**p * (x+b)**q
            ...     def F(x):
            ...         v = x**(r+1)/(r+1) * (a+x)**p * (b+x)**q
            ...         v *= (1+x/a)**(-p)
            ...         v *= (1+x/b)**(-q)
            ...         v *= appellf1(r+1,-p,-q,2+r,-x/a,-x/b)
            ...         return v
            ...     print("Num. quad: %s" % quad(f, [x1,x2]))
            ...     print("Appell F1: %s" % (F(x2)-F(x1)))
            ...
            >>> integral('1/5','4/3','-2','3','1/2',0,1)
            Num. quad: 9.073335358785776206576981
            Appell F1: 9.073335358785776206576981
            >>> integral('3/2','4/3','-2','3','1/2',0,1)
            Num. quad: 1.092829171999626454344678
            Appell F1: 1.092829171999626454344678
            >>> integral('3/2','4/3','-2','3','1/2',12,25)
            Num. quad: 1106.323225040235116498927
            Appell F1: 1106.323225040235116498927
        
        Also incomplete elliptic integrals fall into this category [1]::
        
            >>> def E(z, m):
            ...     if (pi/2).ae(z):
            ...         return ellipe(m)
            ...     return 2*round(re(z)/pi)*ellipe(m) + mpf(-1)**round(re(z)/pi)*\\
            ...         sin(z)*appellf1(0.5,0.5,-0.5,1.5,sin(z)**2,m*sin(z)**2)
            ...
            >>> z, m = 1, 0.5
            >>> E(z,m); quad(lambda t: sqrt(1-m*sin(t)**2), [0,pi/4,3*pi/4,z])
            0.9273298836244400669659042
            0.9273298836244400669659042
            >>> z, m = 3, 2
            >>> E(z,m); quad(lambda t: sqrt(1-m*sin(t)**2), [0,pi/4,3*pi/4,z])
            (1.057495752337234229715836 + 1.198140234735592207439922j)
            (1.057495752337234229715836 + 1.198140234735592207439922j)
        
        **References**
        
        1. [WolframFunctions]_ http://functions.wolfram.com/EllipticIntegrals/EllipticE2/26/01/
        2. [SrivastavaKarlsson]_
        3. [CabralRosetti]_
        4. [Vidunas]_
        5. [Slater]_
        
        """
    @staticmethod
    def appellf2(ctx, a, b1, b2, c1, c2, x, y, **kwargs):
        """
        
        Gives the Appell F2 hypergeometric function of two variables
        
        .. math ::
        
            F_2(a,b_1,b_2,c_1,c_2,x,y) = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
                \\frac{(a)_{m+n} (b_1)_m (b_2)_n}{(c_1)_m (c_2)_n}
                \\frac{x^m y^n}{m! n!}.
        
        The series is generally absolutely convergent for `|x| + |y| < 1`.
        
        **Examples**
        
        Evaluation for real and complex arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> appellf2(1,2,3,4,5,0.25,0.125)
            1.257417193533135344785602
            >>> appellf2(1,-3,-4,2,3,2,3)
            -42.8
            >>> appellf2(0.5,0.25,-0.25,2,3,0.25j,0.25)
            (0.9880539519421899867041719 + 0.01497616165031102661476978j)
            >>> chop(appellf2(1,1+j,1-j,3j,-3j,0.25,0.25))
            1.201311219287411337955192
            >>> appellf2(1,1,1,4,6,0.125,16)
            (-0.09455532250274744282125152 - 0.7647282253046207836769297j)
        
        A transformation formula::
        
            >>> a,b1,b2,c1,c2,x,y = map(mpf, [1,2,0.5,0.25,1.625,-0.125,0.125])
            >>> appellf2(a,b1,b2,c1,c2,x,y)
            0.2299211717841180783309688
            >>> (1-x)**(-a)*appellf2(a,c1-b1,b2,c1,c2,x/(x-1),y/(1-x))
            0.2299211717841180783309688
        
        A system of partial differential equations satisfied by F2::
        
            >>> a,b1,b2,c1,c2,x,y = map(mpf, [1,0.5,0.25,1.125,1.5,0.0625,-0.0625])
            >>> F = lambda x,y: appellf2(a,b1,b2,c1,c2,x,y)
            >>> chop(x*(1-x)*diff(F,(x,y),(2,0)) -
            ...      x*y*diff(F,(x,y),(1,1)) +
            ...      (c1-(a+b1+1)*x)*diff(F,(x,y),(1,0)) -
            ...      b1*y*diff(F,(x,y),(0,1)) -
            ...      a*b1*F(x,y))
            0.0
            >>> chop(y*(1-y)*diff(F,(x,y),(0,2)) -
            ...      x*y*diff(F,(x,y),(1,1)) +
            ...      (c2-(a+b2+1)*y)*diff(F,(x,y),(0,1)) -
            ...      b2*x*diff(F,(x,y),(1,0)) -
            ...      a*b2*F(x,y))
            0.0
        
        **References**
        
        See references for :func:`~mpmath.appellf1`.
        """
    @staticmethod
    def appellf3(ctx, a1, a2, b1, b2, c, x, y, **kwargs):
        """
        
        Gives the Appell F3 hypergeometric function of two variables
        
        .. math ::
        
            F_3(a_1,a_2,b_1,b_2,c,x,y) = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
                \\frac{(a_1)_m (a_2)_n (b_1)_m (b_2)_n}{(c)_{m+n}}
                \\frac{x^m y^n}{m! n!}.
        
        The series is generally absolutely convergent for `|x| < 1, |y| < 1`.
        
        **Examples**
        
        Evaluation for various parameters and variables::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> appellf3(1,2,3,4,5,0.5,0.25)
            2.221557778107438938158705
            >>> appellf3(1,2,3,4,5,6,0); hyp2f1(1,3,5,6)
            (-0.5189554589089861284537389 - 0.1454441043328607980769742j)
            (-0.5189554589089861284537389 - 0.1454441043328607980769742j)
            >>> appellf3(1,-2,-3,1,1,4,6)
            -17.4
            >>> appellf3(1,2,-3,1,1,4,6)
            (17.7876136773677356641825 + 19.54768762233649126154534j)
            >>> appellf3(1,2,-3,1,1,6,4)
            (85.02054175067929402953645 + 148.4402528821177305173599j)
            >>> chop(appellf3(1+j,2,1-j,2,3,0.25,0.25))
            1.719992169545200286696007
        
        Many transformations and evaluations for special combinations
        of the parameters are possible, e.g.:
        
            >>> a,b,c,x,y = map(mpf, [0.5,0.25,0.125,0.125,-0.125])
            >>> appellf3(a,c-a,b,c-b,c,x,y)
            1.093432340896087107444363
            >>> (1-y)**(a+b-c)*hyp2f1(a,b,c,x+y-x*y)
            1.093432340896087107444363
            >>> x**2*appellf3(1,1,1,1,3,x,-x)
            0.01568646277445385390945083
            >>> polylog(2,x**2)
            0.01568646277445385390945083
            >>> a1,a2,b1,b2,c,x = map(mpf, [0.5,0.25,0.125,0.5,4.25,0.125])
            >>> appellf3(a1,a2,b1,b2,c,x,1)
            1.03947361709111140096947
            >>> gammaprod([c,c-a2-b2],[c-a2,c-b2])*hyp3f2(a1,b1,c-a2-b2,c-a2,c-b2,x)
            1.03947361709111140096947
        
        The Appell F3 function satisfies a pair of partial
        differential equations::
        
            >>> a1,a2,b1,b2,c,x,y = map(mpf, [0.5,0.25,0.125,0.5,0.625,0.0625,-0.0625])
            >>> F = lambda x,y: appellf3(a1,a2,b1,b2,c,x,y)
            >>> chop(x*(1-x)*diff(F,(x,y),(2,0)) +
            ...      y*diff(F,(x,y),(1,1)) +
            ...     (c-(a1+b1+1)*x)*diff(F,(x,y),(1,0)) -
            ...     a1*b1*F(x,y))
            0.0
            >>> chop(y*(1-y)*diff(F,(x,y),(0,2)) +
            ...     x*diff(F,(x,y),(1,1)) +
            ...     (c-(a2+b2+1)*y)*diff(F,(x,y),(0,1)) -
            ...     a2*b2*F(x,y))
            0.0
        
        **References**
        
        See references for :func:`~mpmath.appellf1`.
        """
    @staticmethod
    def appellf4(ctx, a, b, c1, c2, x, y, **kwargs):
        """
        
        Gives the Appell F4 hypergeometric function of two variables
        
        .. math ::
        
            F_4(a,b,c_1,c_2,x,y) = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
                \\frac{(a)_{m+n} (b)_{m+n}}{(c_1)_m (c_2)_n}
                \\frac{x^m y^n}{m! n!}.
        
        The series is generally absolutely convergent for
        `\\sqrt{|x|} + \\sqrt{|y|} < 1`.
        
        **Examples**
        
        Evaluation for various parameters and arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> appellf4(1,1,2,2,0.25,0.125)
            1.286182069079718313546608
            >>> appellf4(-2,-3,4,5,4,5)
            34.8
            >>> appellf4(5,4,2,3,0.25j,-0.125j)
            (-0.2585967215437846642163352 + 2.436102233553582711818743j)
        
        Reduction to `\\,_2F_1` in a special case::
        
            >>> a,b,c,x,y = map(mpf, [0.5,0.25,0.125,0.125,-0.125])
            >>> appellf4(a,b,c,a+b-c+1,x*(1-y),y*(1-x))
            1.129143488466850868248364
            >>> hyp2f1(a,b,c,x)*hyp2f1(a,b,a+b-c+1,y)
            1.129143488466850868248364
        
        A system of partial differential equations satisfied by F4::
        
            >>> a,b,c1,c2,x,y = map(mpf, [1,0.5,0.25,1.125,0.0625,-0.0625])
            >>> F = lambda x,y: appellf4(a,b,c1,c2,x,y)
            >>> chop(x*(1-x)*diff(F,(x,y),(2,0)) -
            ...      y**2*diff(F,(x,y),(0,2)) -
            ...      2*x*y*diff(F,(x,y),(1,1)) +
            ...      (c1-(a+b+1)*x)*diff(F,(x,y),(1,0)) -
            ...      ((a+b+1)*y)*diff(F,(x,y),(0,1)) -
            ...      a*b*F(x,y))
            0.0
            >>> chop(y*(1-y)*diff(F,(x,y),(0,2)) -
            ...      x**2*diff(F,(x,y),(2,0)) -
            ...      2*x*y*diff(F,(x,y),(1,1)) +
            ...      (c2-(a+b+1)*y)*diff(F,(x,y),(0,1)) -
            ...      ((a+b+1)*x)*diff(F,(x,y),(1,0)) -
            ...      a*b*F(x,y))
            0.0
        
        **References**
        
        See references for :func:`~mpmath.appellf1`.
        """
    @staticmethod
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
    @staticmethod
    def asec(ctx, *args, **kwargs):
        """
        Computes the inverse secant of `x`,
        `\\mathrm{sec}^{-1}(x) = \\cos^{-1}(1/x)`.
        """
    @staticmethod
    def asech(ctx, *args, **kwargs):
        """
        Computes the inverse hyperbolic secant of `x`,
        `\\mathrm{sech}^{-1}(x) = \\cosh^{-1}(1/x)`.
        """
    @staticmethod
    def atan2(ctx, y, x):
        ...
    @staticmethod
    def autoprec(ctx, f, maxprec = None, catch = tuple(), verbose = False):
        """
        
        Return a wrapped copy of *f* that repeatedly evaluates *f*
        with increasing precision until the result converges to the
        full precision used at the point of the call.
        
        This heuristically protects against rounding errors, at the cost of
        roughly a 2x slowdown compared to manually setting the optimal
        precision. This method can, however, easily be fooled if the results
        from *f* depend "discontinuously" on the precision, for instance
        if catastrophic cancellation can occur. Therefore, :func:`~mpmath.autoprec`
        should be used judiciously.
        
        **Examples**
        
        Many functions are sensitive to perturbations of the input arguments.
        If the arguments are decimal numbers, they may have to be converted
        to binary at a much higher precision. If the amount of required
        extra precision is unknown, :func:`~mpmath.autoprec` is convenient::
        
            >>> from mpmath import *
            >>> mp.dps = 15
            >>> mp.pretty = True
            >>> besselj(5, 125 * 10**28)    # Exact input
            -8.03284785591801e-17
            >>> besselj(5, '1.25e30')   # Bad
            7.12954868316652e-16
            >>> autoprec(besselj)(5, '1.25e30')   # Good
            -8.03284785591801e-17
        
        The following fails to converge because `\\sin(\\pi) = 0` whereas all
        finite-precision approximations of `\\pi` give nonzero values::
        
            >>> autoprec(sin)(pi) # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
              ...
            NoConvergence: autoprec: prec increased to 2910 without convergence
        
        As the following example shows, :func:`~mpmath.autoprec` can protect against
        cancellation, but is fooled by too severe cancellation::
        
            >>> x = 1e-10
            >>> exp(x)-1; expm1(x); autoprec(lambda t: exp(t)-1)(x)
            1.00000008274037e-10
            1.00000000005e-10
            1.00000000005e-10
            >>> x = 1e-50
            >>> exp(x)-1; expm1(x); autoprec(lambda t: exp(t)-1)(x)
            0.0
            1.0e-50
            0.0
        
        With *catch*, an exception or list of exceptions to intercept
        may be specified. The raised exception is interpreted
        as signaling insufficient precision. This permits, for example,
        evaluating a function where a too low precision results in a
        division by zero::
        
            >>> f = lambda x: 1/(exp(x)-1)
            >>> f(1e-30)
            Traceback (most recent call last):
              ...
            ZeroDivisionError
            >>> autoprec(f, catch=ZeroDivisionError)(1e-30)
            1.0e+30
        
        
        """
    @staticmethod
    def backlunds(ctx, *args, **kwargs):
        """
        
        Computes the function
        `S(t) = \\operatorname{arg} \\zeta(\\frac{1}{2} + it) / \\pi`.
        
        See Titchmarsh Section 9.3 for details of the definition.
        
        **Examples**
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> backlunds(217.3)
            0.16302205431184
        
        Generally, the value is a small number. At Gram points it is an integer,
        frequently equal to 0::
        
            >>> chop(backlunds(grampoint(200)))
            0.0
            >>> backlunds(extraprec(10)(grampoint)(211))
            1.0
            >>> backlunds(extraprec(10)(grampoint)(232))
            -1.0
        
        The number of zeros of the Riemann zeta function up to height `t`
        satisfies `N(t) = \\theta(t)/\\pi + 1 + S(t)` (see :func:nzeros` and
        :func:`siegeltheta`)::
        
            >>> t = 1234.55
            >>> nzeros(t)
            842
            >>> siegeltheta(t)/pi+1+backlunds(t)
            842.0
        
        """
    @staticmethod
    def barnesg(ctx, *args, **kwargs):
        """
        
        Evaluates the Barnes G-function, which generalizes the
        superfactorial (:func:`~mpmath.superfac`) and by extension also the
        hyperfactorial (:func:`~mpmath.hyperfac`) to the complex numbers
        in an analogous way to how the gamma function generalizes
        the ordinary factorial.
        
        The Barnes G-function may be defined in terms of a Weierstrass
        product:
        
        .. math ::
        
            G(z+1) = (2\\pi)^{z/2} e^{-[z(z+1)+\\gamma z^2]/2}
            \\prod_{n=1}^\\infty
            \\left[\\left(1+\\frac{z}{n}\\right)^ne^{-z+z^2/(2n)}\\right]
        
        For positive integers `n`, we have have relation to superfactorials
        `G(n) = \\mathrm{sf}(n-2) = 0! \\cdot 1! \\cdots (n-2)!`.
        
        **Examples**
        
        Some elementary values and limits of the Barnes G-function::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> barnesg(1), barnesg(2), barnesg(3)
            (1.0, 1.0, 1.0)
            >>> barnesg(4)
            2.0
            >>> barnesg(5)
            12.0
            >>> barnesg(6)
            288.0
            >>> barnesg(7)
            34560.0
            >>> barnesg(8)
            24883200.0
            >>> barnesg(inf)
            +inf
            >>> barnesg(0), barnesg(-1), barnesg(-2)
            (0.0, 0.0, 0.0)
        
        Closed-form values are known for some rational arguments::
        
            >>> barnesg('1/2')
            0.603244281209446
            >>> sqrt(exp(0.25+log(2)/12)/sqrt(pi)/glaisher**3)
            0.603244281209446
            >>> barnesg('1/4')
            0.29375596533861
            >>> nthroot(exp('3/8')/exp(catalan/pi)/
            ...      gamma(0.25)**3/sqrt(glaisher)**9, 4)
            0.29375596533861
        
        The Barnes G-function satisfies the functional equation
        `G(z+1) = \\Gamma(z) G(z)`::
        
            >>> z = pi
            >>> barnesg(z+1)
            2.39292119327948
            >>> gamma(z)*barnesg(z)
            2.39292119327948
        
        The asymptotic growth rate of the Barnes G-function is related to
        the Glaisher-Kinkelin constant::
        
            >>> limit(lambda n: barnesg(n+1)/(n**(n**2/2-mpf(1)/12)*
            ...     (2*pi)**(n/2)*exp(-3*n**2/4)), inf)
            0.847536694177301
            >>> exp('1/12')/glaisher
            0.847536694177301
        
        The Barnes G-function can be differentiated in closed form::
        
            >>> z = 3
            >>> diff(barnesg, z)
            0.264507203401607
            >>> barnesg(z)*((z-1)*psi(0,z)-z+(log(2*pi)+1)/2)
            0.264507203401607
        
        Evaluation is supported for arbitrary arguments and at arbitrary
        precision::
        
            >>> barnesg(6.5)
            2548.7457695685
            >>> barnesg(-pi)
            0.00535976768353037
            >>> barnesg(3+4j)
            (-0.000676375932234244 - 4.42236140124728e-5j)
            >>> mp.dps = 50
            >>> barnesg(1/sqrt(2))
            0.81305501090451340843586085064413533788206204124732
            >>> q = barnesg(10j)
            >>> q.real
            0.000000000021852360840356557241543036724799812371995850552234
            >>> q.imag
            -0.00000000000070035335320062304849020654215545839053210041457588
            >>> mp.dps = 15
            >>> barnesg(100)
            3.10361006263698e+6626
            >>> barnesg(-101)
            0.0
            >>> barnesg(-10.5)
            5.94463017605008e+25
            >>> barnesg(-10000.5)
            -6.14322868174828e+167480422
            >>> barnesg(1000j)
            (5.21133054865546e-1173597 + 4.27461836811016e-1173597j)
            >>> barnesg(-1000+1000j)
            (2.43114569750291e+1026623 + 2.24851410674842e+1026623j)
        
        
        **References**
        
        1. Whittaker & Watson, *A Course of Modern Analysis*,
           Cambridge University Press, 4th edition (1927), p.264
        2. http://en.wikipedia.org/wiki/Barnes_G-function
        3. http://mathworld.wolfram.com/BarnesG-Function.html
        
        """
    @staticmethod
    def bei(ctx, n, z, **kwargs):
        """
        
        Computes the Kelvin function bei, which for real arguments gives the
        imaginary part of the Bessel J function of a rotated argument.
        See :func:`~mpmath.ber`.
        """
    @staticmethod
    def bell(ctx, *args, **kwargs):
        """
        
        For `n` a nonnegative integer, ``bell(n,x)`` evaluates the Bell
        polynomial `B_n(x)`, the first few of which are
        
        .. math ::
        
            B_0(x) = 1
        
            B_1(x) = x
        
            B_2(x) = x^2+x
        
            B_3(x) = x^3+3x^2+x
        
        If `x = 1` or :func:`~mpmath.bell` is called with only one argument, it
        gives the `n`-th Bell number `B_n`, which is the number of
        partitions of a set with `n` elements. By setting the precision to
        at least `\\log_{10} B_n` digits, :func:`~mpmath.bell` provides fast
        calculation of exact Bell numbers.
        
        In general, :func:`~mpmath.bell` computes
        
        .. math ::
        
            B_n(x) = e^{-x} \\left(\\mathrm{sinc}(\\pi n) + E_n(x)\\right)
        
        where `E_n(x)` is the generalized exponential function implemented
        by :func:`~mpmath.polyexp`. This is an extension of Dobinski's formula [1],
        where the modification is the sinc term ensuring that `B_n(x)` is
        continuous in `n`; :func:`~mpmath.bell` can thus be evaluated,
        differentiated, etc for arbitrary complex arguments.
        
        **Examples**
        
        Simple evaluations::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> bell(0, 2.5)
            1.0
            >>> bell(1, 2.5)
            2.5
            >>> bell(2, 2.5)
            8.75
        
        Evaluation for arbitrary complex arguments::
        
            >>> bell(5.75+1j, 2-3j)
            (-10767.71345136587098445143 - 15449.55065599872579097221j)
        
        The first few Bell polynomials::
        
            >>> for k in range(7):
            ...     nprint(taylor(lambda x: bell(k,x), 0, k))
            ...
            [1.0]
            [0.0, 1.0]
            [0.0, 1.0, 1.0]
            [0.0, 1.0, 3.0, 1.0]
            [0.0, 1.0, 7.0, 6.0, 1.0]
            [0.0, 1.0, 15.0, 25.0, 10.0, 1.0]
            [0.0, 1.0, 31.0, 90.0, 65.0, 15.0, 1.0]
        
        The first few Bell numbers and complementary Bell numbers::
        
            >>> [int(bell(k)) for k in range(10)]
            [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147]
            >>> [int(bell(k,-1)) for k in range(10)]
            [1, -1, 0, 1, 1, -2, -9, -9, 50, 267]
        
        Large Bell numbers::
        
            >>> mp.dps = 50
            >>> bell(50)
            185724268771078270438257767181908917499221852770.0
            >>> bell(50,-1)
            -29113173035759403920216141265491160286912.0
        
        Some even larger values::
        
            >>> mp.dps = 25
            >>> bell(1000,-1)
            -1.237132026969293954162816e+1869
            >>> bell(1000)
            2.989901335682408421480422e+1927
            >>> bell(1000,2)
            6.591553486811969380442171e+1987
            >>> bell(1000,100.5)
            9.101014101401543575679639e+2529
        
        A determinant identity satisfied by Bell numbers::
        
            >>> mp.dps = 15
            >>> N = 8
            >>> det([[bell(k+j) for j in range(N)] for k in range(N)])
            125411328000.0
            >>> superfac(N-1)
            125411328000.0
        
        **References**
        
        1. http://mathworld.wolfram.com/DobinskisFormula.html
        
        """
    @staticmethod
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
    @staticmethod
    def bernoulli(ctx, n):
        ...
    @staticmethod
    def bernpoly(ctx, *args, **kwargs):
        """
        
        Evaluates the Bernoulli polynomial `B_n(z)`.
        
        The first few Bernoulli polynomials are::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> for n in range(6):
            ...     nprint(chop(taylor(lambda x: bernpoly(n,x), 0, n)))
            ...
            [1.0]
            [-0.5, 1.0]
            [0.166667, -1.0, 1.0]
            [0.0, 0.5, -1.5, 1.0]
            [-0.0333333, 0.0, 1.0, -2.0, 1.0]
            [0.0, -0.166667, 0.0, 1.66667, -2.5, 1.0]
        
        At `z = 0`, the Bernoulli polynomial evaluates to a
        Bernoulli number (see :func:`~mpmath.bernoulli`)::
        
            >>> bernpoly(12, 0), bernoulli(12)
            (-0.253113553113553, -0.253113553113553)
            >>> bernpoly(13, 0), bernoulli(13)
            (0.0, 0.0)
        
        Evaluation is accurate for large `n` and small `z`::
        
            >>> mp.dps = 25
            >>> bernpoly(100, 0.5)
            2.838224957069370695926416e+78
            >>> bernpoly(1000, 10.5)
            5.318704469415522036482914e+1769
        
        """
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def besselk(ctx, *args, **kwargs):
        """
        
        ``besselk(n, x)`` gives the modified Bessel function of the
        second kind,
        
        .. math ::
        
            K_n(x) = \\frac{\\pi}{2} \\frac{I_{-n}(x)-I_{n}(x)}{\\sin(\\pi n)}
        
        For `n` an integer, this formula should be understood as a
        limit.
        
        **Plots**
        
        .. literalinclude :: /plots/besselk.py
        .. image :: /plots/besselk.png
        .. literalinclude :: /plots/besselk_c.py
        .. image :: /plots/besselk_c.png
        
        **Examples**
        
        Evaluation is supported for arbitrary complex arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> besselk(0,1)
            0.4210244382407083333356274
            >>> besselk(0, -1)
            (0.4210244382407083333356274 - 3.97746326050642263725661j)
            >>> besselk(3.5, 2+3j)
            (-0.02090732889633760668464128 + 0.2464022641351420167819697j)
            >>> besselk(2+3j, 0.5)
            (0.9615816021726349402626083 + 0.1918250181801757416908224j)
        
        Arguments may be large::
        
            >>> besselk(0, 100)
            4.656628229175902018939005e-45
            >>> besselk(1, 10**6)
            4.131967049321725588398296e-434298
            >>> besselk(1, 10**6*j)
            (0.001140348428252385844876706 - 0.0005200017201681152909000961j)
            >>> besselk(4.5, fmul(10**50, j, exact=True))
            (1.561034538142413947789221e-26 + 1.243554598118700063281496e-25j)
        
        The point `x = 0` is a singularity (logarithmic if `n = 0`)::
        
            >>> besselk(0,0)
            +inf
            >>> besselk(1,0)
            +inf
            >>> for n in range(-4, 5):
            ...     print(besselk(n, '1e-1000'))
            ...
            4.8e+4001
            8.0e+3000
            2.0e+2000
            1.0e+1000
            2302.701024509704096466802
            1.0e+1000
            2.0e+2000
            8.0e+3000
            4.8e+4001
        
        """
    @staticmethod
    def bessely(ctx, *args, **kwargs):
        """
        
        ``bessely(n, x, derivative=0)`` gives the Bessel function of the second kind,
        
        .. math ::
        
            Y_n(x) = \\frac{J_n(x) \\cos(\\pi n) - J_{-n}(x)}{\\sin(\\pi n)}.
        
        For `n` an integer, this formula should be understood as a
        limit. With *derivative* = `m \\ne 0`, the `m`-th derivative
        
        .. math ::
        
            \\frac{d^m}{dx^m} Y_n(x)
        
        is computed.
        
        **Plots**
        
        .. literalinclude :: /plots/bessely.py
        .. image :: /plots/bessely.png
        .. literalinclude :: /plots/bessely_c.py
        .. image :: /plots/bessely_c.png
        
        **Examples**
        
        Some values of `Y_n(x)`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> bessely(0,0), bessely(1,0), bessely(2,0)
            (-inf, -inf, -inf)
            >>> bessely(1, pi)
            0.3588729167767189594679827
            >>> bessely(0.5, 3+4j)
            (9.242861436961450520325216 - 3.085042824915332562522402j)
        
        Arguments may be large::
        
            >>> bessely(0, 10000)
            0.00364780555898660588668872
            >>> bessely(2.5, 10**50)
            -4.8952500412050989295774e-26
            >>> bessely(2.5, -10**50)
            (0.0 + 4.8952500412050989295774e-26j)
        
        Derivatives and antiderivatives of any order can be computed::
        
            >>> bessely(2, 3.5, 1)
            0.3842618820422660066089231
            >>> diff(lambda x: bessely(2, x), 3.5)
            0.3842618820422660066089231
            >>> bessely(0.5, 3.5, 1)
            -0.2066598304156764337900417
            >>> diff(lambda x: bessely(0.5, x), 3.5)
            -0.2066598304156764337900417
            >>> diff(lambda x: bessely(2, x), 0.5, 10)
            -208173867409.5547350101511
            >>> bessely(2, 0.5, 10)
            -208173867409.5547350101511
            >>> bessely(2, 100.5, 100)
            0.02668487547301372334849043
            >>> quad(lambda x: bessely(2,x), [1,3])
            -1.377046859093181969213262
            >>> bessely(2,3,-1) - bessely(2,1,-1)
            -1.377046859093181969213262
        
        """
    @staticmethod
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
    @staticmethod
    def beta(ctx, x, y):
        """
        
        Computes the beta function,
        `B(x,y) = \\Gamma(x) \\Gamma(y) / \\Gamma(x+y)`.
        The beta function is also commonly defined by the integral
        representation
        
        .. math ::
        
            B(x,y) = \\int_0^1 t^{x-1} (1-t)^{y-1} \\, dt
        
        **Examples**
        
        For integer and half-integer arguments where all three gamma
        functions are finite, the beta function becomes either rational
        number or a rational multiple of `\\pi`::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> beta(5, 2)
            0.0333333333333333
            >>> beta(1.5, 2)
            0.266666666666667
            >>> 16*beta(2.5, 1.5)
            3.14159265358979
        
        Where appropriate, :func:`~mpmath.beta` evaluates limits. A pole
        of the beta function is taken to result in ``+inf``::
        
            >>> beta(-0.5, 0.5)
            0.0
            >>> beta(-3, 3)
            -0.333333333333333
            >>> beta(-2, 3)
            +inf
            >>> beta(inf, 1)
            0.0
            >>> beta(inf, 0)
            nan
        
        :func:`~mpmath.beta` supports complex numbers and arbitrary precision
        evaluation::
        
            >>> beta(1, 2+j)
            (0.4 - 0.2j)
            >>> mp.dps = 25
            >>> beta(j,0.5)
            (1.079424249270925780135675 - 1.410032405664160838288752j)
            >>> mp.dps = 50
            >>> beta(pi, e)
            0.037890298781212201348153837138927165984170287886464
        
        Various integrals can be computed by means of the
        beta function::
        
            >>> mp.dps = 15
            >>> quad(lambda t: t**2.5*(1-t)**2, [0, 1])
            0.0230880230880231
            >>> beta(3.5, 3)
            0.0230880230880231
            >>> quad(lambda t: sin(t)**4 * sqrt(cos(t)), [0, pi/2])
            0.319504062596158
            >>> beta(2.5, 0.75)/2
            0.319504062596158
        
        """
    @staticmethod
    def betainc(ctx, *args, **kwargs):
        """
        
        ``betainc(a, b, x1=0, x2=1, regularized=False)`` gives the generalized
        incomplete beta function,
        
        .. math ::
        
            I_{x_1}^{x_2}(a,b) = \\int_{x_1}^{x_2} t^{a-1} (1-t)^{b-1} dt.
        
        When `x_1 = 0, x_2 = 1`, this reduces to the ordinary (complete)
        beta function `B(a,b)`; see :func:`~mpmath.beta`.
        
        With the keyword argument ``regularized=True``, :func:`~mpmath.betainc`
        computes the regularized incomplete beta function
        `I_{x_1}^{x_2}(a,b) / B(a,b)`. This is the cumulative distribution of the
        beta distribution with parameters `a`, `b`.
        
        .. note :
        
            Implementations of the incomplete beta function in some other
            software uses a different argument order. For example, Mathematica uses the
            reversed argument order ``Beta[x1,x2,a,b]``. For the equivalent of SciPy's
            three-argument incomplete beta integral (implicitly with `x1 = 0`), use
            ``betainc(a,b,0,x2,regularized=True)``.
        
        **Examples**
        
        Verifying that :func:`~mpmath.betainc` computes the integral in the
        definition::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> x,y,a,b = 3, 4, 0, 6
            >>> betainc(x, y, a, b)
            -4010.4
            >>> quad(lambda t: t**(x-1) * (1-t)**(y-1), [a, b])
            -4010.4
        
        The arguments may be arbitrary complex numbers::
        
            >>> betainc(0.75, 1-4j, 0, 2+3j)
            (0.2241657956955709603655887 + 0.3619619242700451992411724j)
        
        With regularization::
        
            >>> betainc(1, 2, 0, 0.25, regularized=True)
            0.4375
            >>> betainc(pi, e, 0, 1, regularized=True)   # Complete
            1.0
        
        The beta integral satisfies some simple argument transformation
        symmetries::
        
            >>> mp.dps = 15
            >>> betainc(2,3,4,5), -betainc(2,3,5,4), betainc(3,2,1-5,1-4)
            (56.0833333333333, 56.0833333333333, 56.0833333333333)
        
        The beta integral can often be evaluated analytically. For integer and
        rational arguments, the incomplete beta function typically reduces to a
        simple algebraic-logarithmic expression::
        
            >>> mp.dps = 25
            >>> identify(chop(betainc(0, 0, 3, 4)))
            '-(log((9/8)))'
            >>> identify(betainc(2, 3, 4, 5))
            '(673/12)'
            >>> identify(betainc(1.5, 1, 1, 2))
            '((-12+sqrt(1152))/18)'
        
        """
    @staticmethod
    def bihyper(ctx, a_s, b_s, z, **kwargs):
        """
        
        Evaluates the bilateral hypergeometric series
        
        .. math ::
        
            \\,_AH_B(a_1, \\ldots, a_k; b_1, \\ldots, b_B; z) =
                \\sum_{n=-\\infty}^{\\infty}
                \\frac{(a_1)_n \\ldots (a_A)_n}
                     {(b_1)_n \\ldots (b_B)_n} \\, z^n
        
        where, for direct convergence, `A = B` and `|z| = 1`, although a
        regularized sum exists more generally by considering the
        bilateral series as a sum of two ordinary hypergeometric
        functions. In order for the series to make sense, none of the
        parameters may be integers.
        
        **Examples**
        
        The value of `\\,_2H_2` at `z = 1` is given by Dougall's formula::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> a,b,c,d = 0.5, 1.5, 2.25, 3.25
            >>> bihyper([a,b],[c,d],1)
            -14.49118026212345786148847
            >>> gammaprod([c,d,1-a,1-b,c+d-a-b-1],[c-a,d-a,c-b,d-b])
            -14.49118026212345786148847
        
        The regularized function `\\,_1H_0` can be expressed as the
        sum of one `\\,_2F_0` function and one `\\,_1F_1` function::
        
            >>> a = mpf(0.25)
            >>> z = mpf(0.75)
            >>> bihyper([a], [], z)
            (0.2454393389657273841385582 + 0.2454393389657273841385582j)
            >>> hyper([a,1],[],z) + (hyper([1],[1-a],-1/z)-1)
            (0.2454393389657273841385582 + 0.2454393389657273841385582j)
            >>> hyper([a,1],[],z) + hyper([1],[2-a],-1/z)/z/(a-1)
            (0.2454393389657273841385582 + 0.2454393389657273841385582j)
        
        **References**
        
        1. [Slater]_ (chapter 6: "Bilateral Series", pp. 180-189)
        2. [Wikipedia]_ http://en.wikipedia.org/wiki/Bilateral_hypergeometric_series
        
        """
    @staticmethod
    def binomial(ctx, n, k):
        """
        
        Computes the binomial coefficient
        
        .. math ::
        
            {n \\choose k} = \\frac{n!}{k!(n-k)!}.
        
        The binomial coefficient gives the number of ways that `k` items
        can be chosen from a set of `n` items. More generally, the binomial
        coefficient is a well-defined function of arbitrary real or
        complex `n` and `k`, via the gamma function.
        
        **Examples**
        
        Generate Pascal's triangle::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> for n in range(5):
            ...     nprint([binomial(n,k) for k in range(n+1)])
            ...
            [1.0]
            [1.0, 1.0]
            [1.0, 2.0, 1.0]
            [1.0, 3.0, 3.0, 1.0]
            [1.0, 4.0, 6.0, 4.0, 1.0]
        
        There is 1 way to select 0 items from the empty set, and 0 ways to
        select 1 item from the empty set::
        
            >>> binomial(0, 0)
            1.0
            >>> binomial(0, 1)
            0.0
        
        :func:`~mpmath.binomial` supports large arguments::
        
            >>> binomial(10**20, 10**20-5)
            8.33333333333333e+97
            >>> binomial(10**20, 10**10)
            2.60784095465201e+104342944813
        
        Nonintegral binomial coefficients find use in series
        expansions::
        
            >>> nprint(taylor(lambda x: (1+x)**0.25, 0, 4))
            [1.0, 0.25, -0.09375, 0.0546875, -0.0375977]
            >>> nprint([binomial(0.25, k) for k in range(5)])
            [1.0, 0.25, -0.09375, 0.0546875, -0.0375977]
        
        An integral representation::
        
            >>> n, k = 5, 3
            >>> f = lambda t: exp(-j*k*t)*(1+exp(j*t))**n
            >>> chop(quad(f, [-pi,pi])/(2*pi))
            10.0
            >>> binomial(n,k)
            10.0
        
        """
    @staticmethod
    def chebyt(ctx, *args, **kwargs):
        """
        
        ``chebyt(n, x)`` evaluates the Chebyshev polynomial of the first
        kind `T_n(x)`, defined by the identity
        
        .. math ::
        
            T_n(\\cos x) = \\cos(n x).
        
        The Chebyshev polynomials of the first kind are a special
        case of the Jacobi polynomials, and by extension of the
        hypergeometric function `\\,_2F_1`. They can thus also be
        evaluated for nonintegral `n`.
        
        **Plots**
        
        .. literalinclude :: /plots/chebyt.py
        .. image :: /plots/chebyt.png
        
        **Basic evaluation**
        
        The coefficients of the `n`-th polynomial can be recovered
        using using degree-`n` Taylor expansion::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> for n in range(5):
            ...     nprint(chop(taylor(lambda x: chebyt(n, x), 0, n)))
            ...
            [1.0]
            [0.0, 1.0]
            [-1.0, 0.0, 2.0]
            [0.0, -3.0, 0.0, 4.0]
            [1.0, 0.0, -8.0, 0.0, 8.0]
        
        **Orthogonality**
        
        The Chebyshev polynomials of the first kind are orthogonal
        on the interval `[-1, 1]` with respect to the weight
        function `w(x) = 1/\\sqrt{1-x^2}`::
        
            >>> f = lambda x: chebyt(m,x)*chebyt(n,x)/sqrt(1-x**2)
            >>> m, n = 3, 4
            >>> nprint(quad(f, [-1, 1]),1)
            0.0
            >>> m, n = 4, 4
            >>> quad(f, [-1, 1])
            1.57079632596448
        
        """
    @staticmethod
    def chebyu(ctx, *args, **kwargs):
        """
        
        ``chebyu(n, x)`` evaluates the Chebyshev polynomial of the second
        kind `U_n(x)`, defined by the identity
        
        .. math ::
        
            U_n(\\cos x) = \\frac{\\sin((n+1)x)}{\\sin(x)}.
        
        The Chebyshev polynomials of the second kind are a special
        case of the Jacobi polynomials, and by extension of the
        hypergeometric function `\\,_2F_1`. They can thus also be
        evaluated for nonintegral `n`.
        
        **Plots**
        
        .. literalinclude :: /plots/chebyu.py
        .. image :: /plots/chebyu.png
        
        **Basic evaluation**
        
        The coefficients of the `n`-th polynomial can be recovered
        using using degree-`n` Taylor expansion::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> for n in range(5):
            ...     nprint(chop(taylor(lambda x: chebyu(n, x), 0, n)))
            ...
            [1.0]
            [0.0, 2.0]
            [-1.0, 0.0, 4.0]
            [0.0, -4.0, 0.0, 8.0]
            [1.0, 0.0, -12.0, 0.0, 16.0]
        
        **Orthogonality**
        
        The Chebyshev polynomials of the second kind are orthogonal
        on the interval `[-1, 1]` with respect to the weight
        function `w(x) = \\sqrt{1-x^2}`::
        
            >>> f = lambda x: chebyu(m,x)*chebyu(n,x)*sqrt(1-x**2)
            >>> m, n = 3, 4
            >>> quad(f, [-1, 1])
            0.0
            >>> m, n = 4, 4
            >>> quad(f, [-1, 1])
            1.5707963267949
        """
    @staticmethod
    def chi(ctx, *args, **kwargs):
        """
        
        Computes the hyperbolic cosine integral, defined
        in analogy with the cosine integral (see :func:`~mpmath.ci`) as
        
        .. math ::
        
            \\mathrm{Chi}(x) = -\\int_x^{\\infty} \\frac{\\cosh t}{t}\\,dt
            = \\gamma + \\log x + \\int_0^x \\frac{\\cosh t - 1}{t}\\,dt
        
        Some values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> chi(0)
            -inf
            >>> chi(1)
            0.8378669409802082408946786
            >>> chi(inf)
            +inf
            >>> findroot(chi, 0.5)
            0.5238225713898644064509583
            >>> chi(2+3j)
            (-0.1683628683277204662429321 + 2.625115880451325002151688j)
        
        Evaluation is supported for `z` anywhere in the complex plane::
        
            >>> chi(10**6*(1+j))
            (4.449410587611035724984376e+434287 - 9.75744874290013526417059e+434287j)
        
        """
    @staticmethod
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
    @staticmethod
    def clcos(ctx, *args, **kwargs):
        """
        
        Computes the Clausen cosine function, defined formally by the series
        
        .. math ::
        
            \\mathrm{\\widetilde{Cl}}_s(z) = \\sum_{k=1}^{\\infty} \\frac{\\cos(kz)}{k^s}.
        
        This function is complementary to the Clausen sine function
        :func:`~mpmath.clsin`. In terms of the polylogarithm,
        
        .. math ::
        
            \\mathrm{\\widetilde{Cl}}_s(z) =
                \\frac{1}{2}\\left(\\mathrm{Li}_s\\left(e^{iz}\\right) +
                \\mathrm{Li}_s\\left(e^{-iz}\\right)\\right)
        
            = \\mathrm{Re}\\left[\\mathrm{Li}_s(e^{iz})\\right] \\quad (s, z \\in \\mathbb{R}).
        
        **Examples**
        
        Evaluation for arbitrarily chosen `s` and `z`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> s, z = 3, 4
            >>> clcos(s, z); nsum(lambda k: cos(z*k)/k**s, [1,inf])
            -0.6518926267198991308332759
            -0.6518926267198991308332759
        
        Using `z + \\pi` instead of `z` gives an alternating series::
        
            >>> s, z = 3, 0.5
            >>> clcos(s, z+pi)
            -0.8155530586502260817855618
            >>> nsum(lambda k: (-1)**k*cos(z*k)/k**s, [1,inf])
            -0.8155530586502260817855618
        
        With `s = 1`, the sum can be expressed in closed form
        using elementary functions::
        
            >>> z = 1 + sqrt(3)
            >>> clcos(1, z)
            -0.6720334373369714849797918
            >>> chop(-0.5*(log(1-exp(j*z))+log(1-exp(-j*z))))
            -0.6720334373369714849797918
            >>> -log(abs(2*sin(0.5*z)))    # Equivalent to above when z is real
            -0.6720334373369714849797918
            >>> nsum(lambda k: cos(k*z)/k, [1,inf])
            -0.6720334373369714849797918
        
        It can also be expressed in closed form when `s` is an even integer.
        For example,
        
            >>> clcos(2,z)
            -0.7805359025135583118863007
            >>> pi**2/6 - pi*z/2 + z**2/4
            -0.7805359025135583118863007
        
        The case `s = 0` gives the renormalized sum of
        `\\cos(z) + \\cos(2z) + \\cos(3z) + \\ldots` (which happens to be the same for
        any value of `z`)::
        
            >>> clcos(0, z)
            -0.5
            >>> nsum(lambda k: cos(k*z), [1,inf])
            -0.5
        
        Also the sums
        
        .. math ::
        
            \\cos(z) + 2\\cos(2z) + 3\\cos(3z) + \\ldots
        
        and
        
        .. math ::
        
            \\cos(z) + 2^n \\cos(2z) + 3^n \\cos(3z) + \\ldots
        
        for higher integer powers `n = -s` can be done in closed form. They are zero
        when `n` is positive and even (`s` negative and even)::
        
            >>> clcos(-1, z); 1/(2*cos(z)-2)
            -0.2607829375240542480694126
            -0.2607829375240542480694126
            >>> clcos(-3, z); (2+cos(z))*csc(z/2)**4/8
            0.1472635054979944390848006
            0.1472635054979944390848006
            >>> clcos(-2, z); clcos(-4, z); clcos(-6, z)
            0.0
            0.0
            0.0
        
        With `z = \\pi`, the series reduces to that of the Riemann zeta function
        (more generally, if `z = p \\pi/q`, it is a finite sum over Hurwitz zeta
        function values)::
        
            >>> clcos(2.5, 0); zeta(2.5)
            1.34148725725091717975677
            1.34148725725091717975677
            >>> clcos(2.5, pi); -altzeta(2.5)
            -0.8671998890121841381913472
            -0.8671998890121841381913472
        
        Call with ``pi=True`` to multiply `z` by `\\pi` exactly::
        
            >>> clcos(-3, 2*pi)
            2.997921055881167659267063e+102
            >>> clcos(-3, 2, pi=True)
            0.008333333333333333333333333
        
        Evaluation for complex `s`, `z` in a nonconvergent case::
        
            >>> s, z = -1-j, 1+2j
            >>> clcos(s, z)
            (0.9407430121562251476136807 + 0.715826296033590204557054j)
            >>> extraprec(20)(nsum)(lambda k: cos(k*z)/k**s, [1,inf])
            (0.9407430121562251476136807 + 0.715826296033590204557054j)
        
        """
    @staticmethod
    def clone(ctx):
        """
        
        Create a copy of the context, with the same working precision.
        """
    @staticmethod
    def clsin(ctx, *args, **kwargs):
        """
        
        Computes the Clausen sine function, defined formally by the series
        
        .. math ::
        
            \\mathrm{Cl}_s(z) = \\sum_{k=1}^{\\infty} \\frac{\\sin(kz)}{k^s}.
        
        The special case `\\mathrm{Cl}_2(z)` (i.e. ``clsin(2,z)``) is the classical
        "Clausen function". More generally, the Clausen function is defined for
        complex `s` and `z`, even when the series does not converge. The
        Clausen function is related to the polylogarithm (:func:`~mpmath.polylog`) as
        
        .. math ::
        
            \\mathrm{Cl}_s(z) = \\frac{1}{2i}\\left(\\mathrm{Li}_s\\left(e^{iz}\\right) -
                               \\mathrm{Li}_s\\left(e^{-iz}\\right)\\right)
        
            = \\mathrm{Im}\\left[\\mathrm{Li}_s(e^{iz})\\right] \\quad (s, z \\in \\mathbb{R}),
        
        and this representation can be taken to provide the analytic continuation of the
        series. The complementary function :func:`~mpmath.clcos` gives the corresponding
        cosine sum.
        
        **Examples**
        
        Evaluation for arbitrarily chosen `s` and `z`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> s, z = 3, 4
            >>> clsin(s, z); nsum(lambda k: sin(z*k)/k**s, [1,inf])
            -0.6533010136329338746275795
            -0.6533010136329338746275795
        
        Using `z + \\pi` instead of `z` gives an alternating series::
        
            >>> clsin(s, z+pi)
            0.8860032351260589402871624
            >>> nsum(lambda k: (-1)**k*sin(z*k)/k**s, [1,inf])
            0.8860032351260589402871624
        
        With `s = 1`, the sum can be expressed in closed form
        using elementary functions::
        
            >>> z = 1 + sqrt(3)
            >>> clsin(1, z)
            0.2047709230104579724675985
            >>> chop((log(1-exp(-j*z)) - log(1-exp(j*z)))/(2*j))
            0.2047709230104579724675985
            >>> nsum(lambda k: sin(k*z)/k, [1,inf])
            0.2047709230104579724675985
        
        The classical Clausen function `\\mathrm{Cl}_2(\\theta)` gives the
        value of the integral `\\int_0^{\\theta} -\\ln(2\\sin(x/2)) dx` for
        `0 < \\theta < 2 \\pi`::
        
            >>> cl2 = lambda t: clsin(2, t)
            >>> cl2(3.5)
            -0.2465045302347694216534255
            >>> -quad(lambda x: ln(2*sin(0.5*x)), [0, 3.5])
            -0.2465045302347694216534255
        
        This function is symmetric about `\\theta = \\pi` with zeros and extreme
        points::
        
            >>> cl2(0); cl2(pi/3); chop(cl2(pi)); cl2(5*pi/3); chop(cl2(2*pi))
            0.0
            1.014941606409653625021203
            0.0
            -1.014941606409653625021203
            0.0
        
        Catalan's constant is a special value::
        
            >>> cl2(pi/2)
            0.9159655941772190150546035
            >>> +catalan
            0.9159655941772190150546035
        
        The Clausen sine function can be expressed in closed form when
        `s` is an odd integer (becoming zero when `s` < 0)::
        
            >>> z = 1 + sqrt(2)
            >>> clsin(1, z); (pi-z)/2
            0.3636895456083490948304773
            0.3636895456083490948304773
            >>> clsin(3, z); pi**2/6*z - pi*z**2/4 + z**3/12
            0.5661751584451144991707161
            0.5661751584451144991707161
            >>> clsin(-1, z)
            0.0
            >>> clsin(-3, z)
            0.0
        
        It can also be expressed in closed form for even integer `s \\le 0`,
        providing a finite sum for series such as
        `\\sin(z) + \\sin(2z) + \\sin(3z) + \\ldots`::
        
            >>> z = 1 + sqrt(2)
            >>> clsin(0, z)
            0.1903105029507513881275865
            >>> cot(z/2)/2
            0.1903105029507513881275865
            >>> clsin(-2, z)
            -0.1089406163841548817581392
            >>> -cot(z/2)*csc(z/2)**2/4
            -0.1089406163841548817581392
        
        Call with ``pi=True`` to multiply `z` by `\\pi` exactly::
        
            >>> clsin(3, 3*pi)
            -8.892316224968072424732898e-26
            >>> clsin(3, 3, pi=True)
            0.0
        
        Evaluation for complex `s`, `z` in a nonconvergent case::
        
            >>> s, z = -1-j, 1+2j
            >>> clsin(s, z)
            (-0.593079480117379002516034 + 0.9038644233367868273362446j)
            >>> extraprec(20)(nsum)(lambda k: sin(k*z)/k**s, [1,inf])
            (-0.593079480117379002516034 + 0.9038644233367868273362446j)
        
        """
    @staticmethod
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
    @staticmethod
    def cos_sin(ctx, x, **kwargs):
        ...
    @staticmethod
    def cospi_sinpi(ctx, x, **kwargs):
        ...
    @staticmethod
    def cot(ctx, *args, **kwargs):
        """
        
        Computes the cotangent of `x`,
        `\\mathrm{cot}(x) = \\frac{1}{\\tan(x)} = \\frac{\\cos(x)}{\\sin(x)}`.
        This cotangent function is singular at `x = n \\pi`, but with the
        exception of the point `x = 0`, ``cot(x)`` returns a finite result
        since `n \\pi` cannot be represented exactly using floating-point
        arithmetic.
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> cot(pi/3)
            0.5773502691896257645091488
            >>> cot(10000001)
            1.574131876209625656003562
            >>> cot(2+3j)
            (-0.003739710376336956660117409 - 0.9967577965693583104609688j)
            >>> cot(inf)
            nan
        
        Intervals are supported via :func:`mpmath.iv.cot`::
        
            >>> iv.dps = 25; iv.pretty = True
            >>> iv.cot([0,1])  # Interval includes a singularity
            [0.642092615934330703006419974862, +inf]
            >>> iv.cot([1,2])
            [-inf, +inf]
        """
    @staticmethod
    def coth(ctx, *args, **kwargs):
        """
        Computes the hyperbolic cotangent of `x`,
        `\\mathrm{coth}(x) = \\frac{\\cosh(x)}{\\sinh(x)}`.
        """
    @staticmethod
    def coulombc(ctx, *args, **kwargs):
        """
        
        Gives the normalizing Gamow constant for Coulomb wave functions,
        
        .. math ::
        
            C_l(\\eta) = 2^l \\exp\\left(-\\pi \\eta/2 + [\\ln \\Gamma(1+l+i\\eta) +
                \\ln \\Gamma(1+l-i\\eta)]/2 - \\ln \\Gamma(2l+2)\\right),
        
        where the log gamma function with continuous imaginary part
        away from the negative half axis (see :func:`~mpmath.loggamma`) is implied.
        
        This function is used internally for the calculation of
        Coulomb wave functions, and automatically cached to make multiple
        evaluations with fixed `l`, `\\eta` fast.
        """
    @staticmethod
    def coulombf(ctx, *args, **kwargs):
        """
        
        Calculates the regular Coulomb wave function
        
        .. math ::
        
            F_l(\\eta,z) = C_l(\\eta) z^{l+1} e^{-iz} \\,_1F_1(l+1-i\\eta, 2l+2, 2iz)
        
        where the normalization constant `C_l(\\eta)` is as calculated by
        :func:`~mpmath.coulombc`. This function solves the differential equation
        
        .. math ::
        
            f''(z) + \\left(1-\\frac{2\\eta}{z}-\\frac{l(l+1)}{z^2}\\right) f(z) = 0.
        
        A second linearly independent solution is given by the irregular
        Coulomb wave function `G_l(\\eta,z)` (see :func:`~mpmath.coulombg`)
        and thus the general solution is
        `f(z) = C_1 F_l(\\eta,z) + C_2 G_l(\\eta,z)` for arbitrary
        constants `C_1`, `C_2`.
        Physically, the Coulomb wave functions give the radial solution
        to the Schrodinger equation for a point particle in a `1/z` potential; `z` is
        then the radius and `l`, `\\eta` are quantum numbers.
        
        The Coulomb wave functions with real parameters are defined
        in Abramowitz & Stegun, section 14. However, all parameters are permitted
        to be complex in this implementation (see references).
        
        **Plots**
        
        .. literalinclude :: /plots/coulombf.py
        .. image :: /plots/coulombf.png
        .. literalinclude :: /plots/coulombf_c.py
        .. image :: /plots/coulombf_c.png
        
        **Examples**
        
        Evaluation is supported for arbitrary magnitudes of `z`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> coulombf(2, 1.5, 3.5)
            0.4080998961088761187426445
            >>> coulombf(-2, 1.5, 3.5)
            0.7103040849492536747533465
            >>> coulombf(2, 1.5, '1e-10')
            4.143324917492256448770769e-33
            >>> coulombf(2, 1.5, 1000)
            0.4482623140325567050716179
            >>> coulombf(2, 1.5, 10**10)
            -0.066804196437694360046619
        
        Verifying the differential equation::
        
            >>> l, eta, z = 2, 3, mpf(2.75)
            >>> A, B = 1, 2
            >>> f = lambda z: A*coulombf(l,eta,z) + B*coulombg(l,eta,z)
            >>> chop(diff(f,z,2) + (1-2*eta/z - l*(l+1)/z**2)*f(z))
            0.0
        
        A Wronskian relation satisfied by the Coulomb wave functions::
        
            >>> l = 2
            >>> eta = 1.5
            >>> F = lambda z: coulombf(l,eta,z)
            >>> G = lambda z: coulombg(l,eta,z)
            >>> for z in [3.5, -1, 2+3j]:
            ...     chop(diff(F,z)*G(z) - F(z)*diff(G,z))
            ...
            1.0
            1.0
            1.0
        
        Another Wronskian relation::
        
            >>> F = coulombf
            >>> G = coulombg
            >>> for z in [3.5, -1, 2+3j]:
            ...     chop(F(l-1,eta,z)*G(l,eta,z)-F(l,eta,z)*G(l-1,eta,z) - l/sqrt(l**2+eta**2))
            ...
            0.0
            0.0
            0.0
        
        An integral identity connecting the regular and irregular wave functions::
        
            >>> l, eta, z = 4+j, 2-j, 5+2j
            >>> coulombf(l,eta,z) + j*coulombg(l,eta,z)
            (0.7997977752284033239714479 + 0.9294486669502295512503127j)
            >>> g = lambda t: exp(-t)*t**(l-j*eta)*(t+2*j*z)**(l+j*eta)
            >>> j*exp(-j*z)*z**(-l)/fac(2*l+1)/coulombc(l,eta)*quad(g, [0,inf])
            (0.7997977752284033239714479 + 0.9294486669502295512503127j)
        
        Some test case with complex parameters, taken from Michel [2]::
        
            >>> mp.dps = 15
            >>> coulombf(1+0.1j, 50+50j, 100.156)
            (-1.02107292320897e+15 - 2.83675545731519e+15j)
            >>> coulombg(1+0.1j, 50+50j, 100.156)
            (2.83675545731519e+15 - 1.02107292320897e+15j)
            >>> coulombf(1e-5j, 10+1e-5j, 0.1+1e-6j)
            (4.30566371247811e-14 - 9.03347835361657e-19j)
            >>> coulombg(1e-5j, 10+1e-5j, 0.1+1e-6j)
            (778709182061.134 + 18418936.2660553j)
        
        The following reproduces a table in Abramowitz & Stegun, at twice
        the precision::
        
            >>> mp.dps = 10
            >>> eta = 2; z = 5
            >>> for l in [5, 4, 3, 2, 1, 0]:
            ...     print("%s %s %s" % (l, coulombf(l,eta,z),
            ...         diff(lambda z: coulombf(l,eta,z), z)))
            ...
            5 0.09079533488 0.1042553261
            4 0.2148205331 0.2029591779
            3 0.4313159311 0.320534053
            2 0.7212774133 0.3952408216
            1 0.9935056752 0.3708676452
            0 1.143337392 0.2937960375
        
        **References**
        
        1. I.J. Thompson & A.R. Barnett, "Coulomb and Bessel Functions of Complex
           Arguments and Order", J. Comp. Phys., vol 64, no. 2, June 1986.
        
        2. N. Michel, "Precise Coulomb wave functions for a wide range of
           complex `l`, `\\eta` and `z`", http://arxiv.org/abs/physics/0702051v1
        
        """
    @staticmethod
    def coulombg(ctx, *args, **kwargs):
        """
        
        Calculates the irregular Coulomb wave function
        
        .. math ::
        
            G_l(\\eta,z) = \\frac{F_l(\\eta,z) \\cos(\\chi) - F_{-l-1}(\\eta,z)}{\\sin(\\chi)}
        
        where `\\chi = \\sigma_l - \\sigma_{-l-1} - (l+1/2) \\pi`
        and `\\sigma_l(\\eta) = (\\ln \\Gamma(1+l+i\\eta)-\\ln \\Gamma(1+l-i\\eta))/(2i)`.
        
        See :func:`~mpmath.coulombf` for additional information.
        
        **Plots**
        
        .. literalinclude :: /plots/coulombg.py
        .. image :: /plots/coulombg.png
        .. literalinclude :: /plots/coulombg_c.py
        .. image :: /plots/coulombg_c.png
        
        **Examples**
        
        Evaluation is supported for arbitrary magnitudes of `z`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> coulombg(-2, 1.5, 3.5)
            1.380011900612186346255524
            >>> coulombg(2, 1.5, 3.5)
            1.919153700722748795245926
            >>> coulombg(-2, 1.5, '1e-10')
            201126715824.7329115106793
            >>> coulombg(-2, 1.5, 1000)
            0.1802071520691149410425512
            >>> coulombg(-2, 1.5, 10**10)
            0.652103020061678070929794
        
        The following reproduces a table in Abramowitz & Stegun,
        at twice the precision::
        
            >>> mp.dps = 10
            >>> eta = 2; z = 5
            >>> for l in [1, 2, 3, 4, 5]:
            ...     print("%s %s %s" % (l, coulombg(l,eta,z),
            ...         -diff(lambda z: coulombg(l,eta,z), z)))
            ...
            1 1.08148276 0.6028279961
            2 1.496877075 0.5661803178
            3 2.048694714 0.7959909551
            4 3.09408669 1.731802374
            5 5.629840456 4.549343289
        
        Evaluation close to the singularity at `z = 0`::
        
            >>> mp.dps = 15
            >>> coulombg(0,10,1)
            3088184933.67358
            >>> coulombg(0,10,'1e-10')
            5554866000719.8
            >>> coulombg(0,10,'1e-100')
            5554866221524.1
        
        Evaluation with a half-integer value for `l`::
        
            >>> coulombg(1.5, 1, 10)
            0.852320038297334
        """
    @staticmethod
    def csc(ctx, *args, **kwargs):
        """
        
        Computes the cosecant of `x`, `\\mathrm{csc}(x) = \\frac{1}{\\sin(x)}`.
        This cosecant function is singular at `x = n \\pi`, but with the
        exception of the point `x = 0`, ``csc(x)`` returns a finite result
        since `n \\pi` cannot be represented exactly using floating-point
        arithmetic.
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> csc(pi/3)
            1.154700538379251529018298
            >>> csc(10000001)
            -1.864910497503629858938891
            >>> csc(2+3j)
            (0.09047320975320743980579048 + 0.04120098628857412646300981j)
            >>> csc(inf)
            nan
        
        Intervals are supported via :func:`mpmath.iv.csc`::
        
            >>> iv.dps = 25; iv.pretty = True
            >>> iv.csc([0,1])  # Interval includes a singularity
            [1.18839510577812121626159943988, +inf]
            >>> iv.csc([0,2])
            [1.0, +inf]
        """
    @staticmethod
    def csch(ctx, *args, **kwargs):
        """
        Computes the hyperbolic cosecant of `x`,
        `\\mathrm{csch}(x) = \\frac{1}{\\sinh(x)}`.
        """
    @staticmethod
    def cyclotomic(ctx, *args, **kwargs):
        """
        
        Evaluates the cyclotomic polynomial `\\Phi_n(x)`, defined by
        
        .. math ::
        
            \\Phi_n(x) = \\prod_{\\zeta} (x - \\zeta)
        
        where `\\zeta` ranges over all primitive `n`-th roots of unity
        (see :func:`~mpmath.unitroots`). An equivalent representation, used
        for computation, is
        
        .. math ::
        
            \\Phi_n(x) = \\prod_{d\\mid n}(x^d-1)^{\\mu(n/d)} = \\Phi_n(x)
        
        where `\\mu(m)` denotes the Moebius function. The cyclotomic
        polynomials are integer polynomials, the first of which can be
        written explicitly as
        
        .. math ::
        
            \\Phi_0(x) = 1
        
            \\Phi_1(x) = x - 1
        
            \\Phi_2(x) = x + 1
        
            \\Phi_3(x) = x^3 + x^2 + 1
        
            \\Phi_4(x) = x^2 + 1
        
            \\Phi_5(x) = x^4 + x^3 + x^2 + x + 1
        
            \\Phi_6(x) = x^2 - x + 1
        
        **Examples**
        
        The coefficients of low-order cyclotomic polynomials can be recovered
        using Taylor expansion::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> for n in range(9):
            ...     p = chop(taylor(lambda x: cyclotomic(n,x), 0, 10))
            ...     print("%s %s" % (n, nstr(p[:10+1-p[::-1].index(1)])))
            ...
            0 [1.0]
            1 [-1.0, 1.0]
            2 [1.0, 1.0]
            3 [1.0, 1.0, 1.0]
            4 [1.0, 0.0, 1.0]
            5 [1.0, 1.0, 1.0, 1.0, 1.0]
            6 [1.0, -1.0, 1.0]
            7 [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            8 [1.0, 0.0, 0.0, 0.0, 1.0]
        
        The definition as a product over primitive roots may be checked
        by computing the product explicitly (for a real argument, this
        method will generally introduce numerical noise in the imaginary
        part)::
        
            >>> mp.dps = 25
            >>> z = 3+4j
            >>> cyclotomic(10, z)
            (-419.0 - 360.0j)
            >>> fprod(z-r for r in unitroots(10, primitive=True))
            (-419.0 - 360.0j)
            >>> z = 3
            >>> cyclotomic(10, z)
            61.0
            >>> fprod(z-r for r in unitroots(10, primitive=True))
            (61.0 - 3.146045605088568607055454e-25j)
        
        Up to permutation, the roots of a given cyclotomic polynomial
        can be checked to agree with the list of primitive roots::
        
            >>> p = taylor(lambda x: cyclotomic(6,x), 0, 6)[:3]
            >>> for r in polyroots(p[::-1]):
            ...     print(r)
            ...
            (0.5 - 0.8660254037844386467637232j)
            (0.5 + 0.8660254037844386467637232j)
            >>>
            >>> for r in unitroots(6, primitive=True):
            ...     print(r)
            ...
            (0.5 + 0.8660254037844386467637232j)
            (0.5 - 0.8660254037844386467637232j)
        
        """
    @staticmethod
    def degrees(ctx, x):
        """
        
        Converts the radian angle `x` to a degree angle::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> degrees(pi/3)
            60.0
        """
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def ellipe(ctx, *args, **kwargs):
        """
        
        Called with a single argument `m`, evaluates the Legendre complete
        elliptic integral of the second kind, `E(m)`, defined by
        
            .. math :: E(m) = \\int_0^{\\pi/2} \\sqrt{1-m \\sin^2 t} \\, dt \\,=\\,
                \\frac{\\pi}{2}
                \\,_2F_1\\left(\\frac{1}{2}, -\\frac{1}{2}, 1, m\\right).
        
        Called with two arguments `\\phi, m`, evaluates the incomplete elliptic
        integral of the second kind
        
         .. math ::
        
            E(\\phi,m) = \\int_0^{\\phi} \\sqrt{1-m \\sin^2 t} \\, dt =
                        \\int_0^{\\sin z}
                        \\frac{\\sqrt{1-mt^2}}{\\sqrt{1-t^2}} \\, dt.
        
        The incomplete integral reduces to a complete integral when
        `\\phi = \\frac{\\pi}{2}`; that is,
        
        .. math ::
        
            E\\left(\\frac{\\pi}{2}, m\\right) = E(m).
        
        In the defining integral, it is assumed that the principal branch
        of the square root is taken and that the path of integration avoids
        crossing any branch cuts. Outside `-\\pi/2 \\le \\Re(z) \\le \\pi/2`,
        the function extends quasi-periodically as
        
        .. math ::
        
            E(\\phi + n \\pi, m) = 2 n E(m) + E(\\phi,m), n \\in \\mathbb{Z}.
        
        **Plots**
        
        .. literalinclude :: /plots/ellipe.py
        .. image :: /plots/ellipe.png
        
        **Examples for the complete integral**
        
        Basic values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> ellipe(0)
            1.570796326794896619231322
            >>> ellipe(1)
            1.0
            >>> ellipe(-1)
            1.910098894513856008952381
            >>> ellipe(2)
            (0.5990701173677961037199612 + 0.5990701173677961037199612j)
            >>> ellipe(inf)
            (0.0 + +infj)
            >>> ellipe(-inf)
            +inf
        
        Verifying the defining integral and hypergeometric
        representation::
        
            >>> ellipe(0.5)
            1.350643881047675502520175
            >>> quad(lambda t: sqrt(1-0.5*sin(t)**2), [0, pi/2])
            1.350643881047675502520175
            >>> pi/2*hyp2f1(0.5,-0.5,1,0.5)
            1.350643881047675502520175
        
        Evaluation is supported for arbitrary complex `m`::
        
            >>> ellipe(0.5+0.25j)
            (1.360868682163129682716687 - 0.1238733442561786843557315j)
            >>> ellipe(3+4j)
            (1.499553520933346954333612 - 1.577879007912758274533309j)
        
        A definite integral::
        
            >>> quad(ellipe, [0,1])
            1.333333333333333333333333
        
        **Examples for the incomplete integral**
        
        Basic values and limits::
        
            >>> ellipe(0,1)
            0.0
            >>> ellipe(0,0)
            0.0
            >>> ellipe(1,0)
            1.0
            >>> ellipe(2+3j,0)
            (2.0 + 3.0j)
            >>> ellipe(1,1); sin(1)
            0.8414709848078965066525023
            0.8414709848078965066525023
            >>> ellipe(pi/2, -0.5); ellipe(-0.5)
            1.751771275694817862026502
            1.751771275694817862026502
            >>> ellipe(pi/2, 1); ellipe(-pi/2, 1)
            1.0
            -1.0
            >>> ellipe(1.5, 1)
            0.9974949866040544309417234
        
        Comparing with numerical integration::
        
            >>> z,m = 0.5, 1.25
            >>> ellipe(z,m)
            0.4740152182652628394264449
            >>> quad(lambda t: sqrt(1-m*sin(t)**2), [0,z])
            0.4740152182652628394264449
        
        The arguments may be complex numbers::
        
            >>> ellipe(3j, 0.5)
            (0.0 + 7.551991234890371873502105j)
            >>> ellipe(3+4j, 5-6j)
            (24.15299022574220502424466 + 75.2503670480325997418156j)
            >>> k = 35
            >>> z,m = 2+3j, 1.25
            >>> ellipe(z+pi*k,m); ellipe(z,m) + 2*k*ellipe(m)
            (48.30138799412005235090766 + 17.47255216721987688224357j)
            (48.30138799412005235090766 + 17.47255216721987688224357j)
        
        For `|\\Re(z)| < \\pi/2`, the function can be expressed as a
        hypergeometric series of two variables
        (see :func:`~mpmath.appellf1`)::
        
            >>> z,m = 0.5, 0.25
            >>> ellipe(z,m)
            0.4950017030164151928870375
            >>> sin(z)*appellf1(0.5,0.5,-0.5,1.5,sin(z)**2,m*sin(z)**2)
            0.4950017030164151928870376
        
        """
    @staticmethod
    def ellipf(ctx, *args, **kwargs):
        """
        
        Evaluates the Legendre incomplete elliptic integral of the first kind
        
         .. math ::
        
            F(\\phi,m) = \\int_0^{\\phi} \\frac{dt}{\\sqrt{1-m \\sin^2 t}}
        
        or equivalently
        
        .. math ::
        
            F(\\phi,m) = \\int_0^{\\sin \\phi}
            \\frac{dt}{\\left(\\sqrt{1-t^2}\\right)\\left(\\sqrt{1-mt^2}\\right)}.
        
        The function reduces to a complete elliptic integral of the first kind
        (see :func:`~mpmath.ellipk`) when `\\phi = \\frac{\\pi}{2}`; that is,
        
        .. math ::
        
            F\\left(\\frac{\\pi}{2}, m\\right) = K(m).
        
        In the defining integral, it is assumed that the principal branch
        of the square root is taken and that the path of integration avoids
        crossing any branch cuts. Outside `-\\pi/2 \\le \\Re(\\phi) \\le \\pi/2`,
        the function extends quasi-periodically as
        
        .. math ::
        
            F(\\phi + n \\pi, m) = 2 n K(m) + F(\\phi,m), n \\in \\mathbb{Z}.
        
        **Plots**
        
        .. literalinclude :: /plots/ellipf.py
        .. image :: /plots/ellipf.png
        
        **Examples**
        
        Basic values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> ellipf(0,1)
            0.0
            >>> ellipf(0,0)
            0.0
            >>> ellipf(1,0); ellipf(2+3j,0)
            1.0
            (2.0 + 3.0j)
            >>> ellipf(1,1); log(sec(1)+tan(1))
            1.226191170883517070813061
            1.226191170883517070813061
            >>> ellipf(pi/2, -0.5); ellipk(-0.5)
            1.415737208425956198892166
            1.415737208425956198892166
            >>> ellipf(pi/2+eps, 1); ellipf(-pi/2-eps, 1)
            +inf
            +inf
            >>> ellipf(1.5, 1)
            3.340677542798311003320813
        
        Comparing with numerical integration::
        
            >>> z,m = 0.5, 1.25
            >>> ellipf(z,m)
            0.5287219202206327872978255
            >>> quad(lambda t: (1-m*sin(t)**2)**(-0.5), [0,z])
            0.5287219202206327872978255
        
        The arguments may be complex numbers::
        
            >>> ellipf(3j, 0.5)
            (0.0 + 1.713602407841590234804143j)
            >>> ellipf(3+4j, 5-6j)
            (1.269131241950351323305741 - 0.3561052815014558335412538j)
            >>> z,m = 2+3j, 1.25
            >>> k = 1011
            >>> ellipf(z+pi*k,m); ellipf(z,m) + 2*k*ellipk(m)
            (4086.184383622179764082821 - 3003.003538923749396546871j)
            (4086.184383622179764082821 - 3003.003538923749396546871j)
        
        For `|\\Re(z)| < \\pi/2`, the function can be expressed as a
        hypergeometric series of two variables
        (see :func:`~mpmath.appellf1`)::
        
            >>> z,m = 0.5, 0.25
            >>> ellipf(z,m)
            0.5050887275786480788831083
            >>> sin(z)*appellf1(0.5,0.5,0.5,1.5,sin(z)**2,m*sin(z)**2)
            0.5050887275786480788831083
        
        """
    @staticmethod
    def ellipfun(ctx, kind, u = None, m = None, q = None, k = None, tau = None):
        """
        
        Computes any of the Jacobi elliptic functions, defined
        in terms of Jacobi theta functions as
        
        .. math ::
        
            \\mathrm{sn}(u,m) = \\frac{\\vartheta_3(0,q)}{\\vartheta_2(0,q)}
                \\frac{\\vartheta_1(t,q)}{\\vartheta_4(t,q)}
        
            \\mathrm{cn}(u,m) = \\frac{\\vartheta_4(0,q)}{\\vartheta_2(0,q)}
                \\frac{\\vartheta_2(t,q)}{\\vartheta_4(t,q)}
        
            \\mathrm{dn}(u,m) = \\frac{\\vartheta_4(0,q)}{\\vartheta_3(0,q)}
                \\frac{\\vartheta_3(t,q)}{\\vartheta_4(t,q)},
        
        or more generally computes a ratio of two such functions. Here
        `t = u/\\vartheta_3(0,q)^2`, and `q = q(m)` denotes the nome (see
        :func:`~mpmath.nome`). Optionally, you can specify the nome directly
        instead of `m` by passing ``q=<value>``, or you can directly
        specify the elliptic parameter `k` with ``k=<value>``.
        
        The first argument should be a two-character string specifying the
        function using any combination of ``'s'``, ``'c'``, ``'d'``, ``'n'``. These
        letters respectively denote the basic functions
        `\\mathrm{sn}(u,m)`, `\\mathrm{cn}(u,m)`, `\\mathrm{dn}(u,m)`, and `1`.
        The identifier specifies the ratio of two such functions.
        For example, ``'ns'`` identifies the function
        
        .. math ::
        
            \\mathrm{ns}(u,m) = \\frac{1}{\\mathrm{sn}(u,m)}
        
        and ``'cd'`` identifies the function
        
        .. math ::
        
            \\mathrm{cd}(u,m) = \\frac{\\mathrm{cn}(u,m)}{\\mathrm{dn}(u,m)}.
        
        If called with only the first argument, a function object
        evaluating the chosen function for given arguments is returned.
        
        **Examples**
        
        Basic evaluation::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> ellipfun('cd', 3.5, 0.5)
            -0.9891101840595543931308394
            >>> ellipfun('cd', 3.5, q=0.25)
            0.07111979240214668158441418
        
        The sn-function is doubly periodic in the complex plane with periods
        `4 K(m)` and `2 i K(1-m)` (see :func:`~mpmath.ellipk`)::
        
            >>> sn = ellipfun('sn')
            >>> sn(2, 0.25)
            0.9628981775982774425751399
            >>> sn(2+4*ellipk(0.25), 0.25)
            0.9628981775982774425751399
            >>> chop(sn(2+2*j*ellipk(1-0.25), 0.25))
            0.9628981775982774425751399
        
        The cn-function is doubly periodic with periods `4 K(m)` and `2 K(m) + 2 i K(1-m)`::
        
            >>> cn = ellipfun('cn')
            >>> cn(2, 0.25)
            -0.2698649654510865792581416
            >>> cn(2+4*ellipk(0.25), 0.25)
            -0.2698649654510865792581416
            >>> chop(cn(2+2*ellipk(0.25)+2*j*ellipk(1-0.25), 0.25))
            -0.2698649654510865792581416
        
        The dn-function is doubly periodic with periods `2 K(m)` and `4 i K(1-m)`::
        
            >>> dn = ellipfun('dn')
            >>> dn(2, 0.25)
            0.8764740583123262286931578
            >>> dn(2+2*ellipk(0.25), 0.25)
            0.8764740583123262286931578
            >>> chop(dn(2+4*j*ellipk(1-0.25), 0.25))
            0.8764740583123262286931578
        
        """
    @staticmethod
    def ellippi(ctx, *args, **kwargs):
        """
        
        Called with three arguments `n, \\phi, m`, evaluates the Legendre
        incomplete elliptic integral of the third kind
        
        .. math ::
        
            \\Pi(n; \\phi, m) = \\int_0^{\\phi}
                \\frac{dt}{(1-n \\sin^2 t) \\sqrt{1-m \\sin^2 t}} =
                \\int_0^{\\sin \\phi}
                \\frac{dt}{(1-nt^2) \\sqrt{1-t^2} \\sqrt{1-mt^2}}.
        
        Called with two arguments `n, m`, evaluates the complete
        elliptic integral of the third kind
        `\\Pi(n,m) = \\Pi(n; \\frac{\\pi}{2},m)`.
        
        In the defining integral, it is assumed that the principal branch
        of the square root is taken and that the path of integration avoids
        crossing any branch cuts. Outside `-\\pi/2 \\le \\Re(\\phi) \\le \\pi/2`,
        the function extends quasi-periodically as
        
        .. math ::
        
            \\Pi(n,\\phi+k\\pi,m) = 2k\\Pi(n,m) + \\Pi(n,\\phi,m), k \\in \\mathbb{Z}.
        
        **Plots**
        
        .. literalinclude :: /plots/ellippi.py
        .. image :: /plots/ellippi.png
        
        **Examples for the complete integral**
        
        Some basic values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> ellippi(0,-5); ellipk(-5)
            0.9555039270640439337379334
            0.9555039270640439337379334
            >>> ellippi(inf,2)
            0.0
            >>> ellippi(2,inf)
            0.0
            >>> abs(ellippi(1,5))
            +inf
            >>> abs(ellippi(0.25,1))
            +inf
        
        Evaluation in terms of simpler functions::
        
            >>> ellippi(0.25,0.25); ellipe(0.25)/(1-0.25)
            1.956616279119236207279727
            1.956616279119236207279727
            >>> ellippi(3,0); pi/(2*sqrt(-2))
            (0.0 - 1.11072073453959156175397j)
            (0.0 - 1.11072073453959156175397j)
            >>> ellippi(-3,0); pi/(2*sqrt(4))
            0.7853981633974483096156609
            0.7853981633974483096156609
        
        **Examples for the incomplete integral**
        
        Basic values and limits::
        
            >>> ellippi(0.25,-0.5); ellippi(0.25,pi/2,-0.5)
            1.622944760954741603710555
            1.622944760954741603710555
            >>> ellippi(1,0,1)
            0.0
            >>> ellippi(inf,0,1)
            0.0
            >>> ellippi(0,0.25,0.5); ellipf(0.25,0.5)
            0.2513040086544925794134591
            0.2513040086544925794134591
            >>> ellippi(1,1,1); (log(sec(1)+tan(1))+sec(1)*tan(1))/2
            2.054332933256248668692452
            2.054332933256248668692452
            >>> ellippi(0.25, 53*pi/2, 0.75); 53*ellippi(0.25,0.75)
            135.240868757890840755058
            135.240868757890840755058
            >>> ellippi(0.5,pi/4,0.5); 2*ellipe(pi/4,0.5)-1/sqrt(3)
            0.9190227391656969903987269
            0.9190227391656969903987269
        
        Complex arguments are supported::
        
            >>> ellippi(0.5, 5+6j-2*pi, -7-8j)
            (-0.3612856620076747660410167 + 0.5217735339984807829755815j)
        
        Some degenerate cases::
        
            >>> ellippi(1,1)
            +inf
            >>> ellippi(1,0)
            +inf
            >>> ellippi(1,2,0)
            +inf
            >>> ellippi(1,2,1)
            +inf
            >>> ellippi(1,0,1)
            0.0
        
        """
    @staticmethod
    def elliprc(ctx, x, y, pv = True):
        """
        
        Evaluates the degenerate Carlson symmetric elliptic integral
        of the first kind
        
        .. math ::
        
            R_C(x,y) = R_F(x,y,y) =
                \\frac{1}{2} \\int_0^{\\infty} \\frac{dt}{(t+y) \\sqrt{(t+x)}}.
        
        If `y \\in (-\\infty,0)`, either a value defined by continuity,
        or with *pv=True* the Cauchy principal value, can be computed.
        
        If `x \\ge 0, y > 0`, the value can be expressed in terms of
        elementary functions as
        
        .. math ::
        
            R_C(x,y) =
            \\begin{cases}
              \\dfrac{1}{\\sqrt{y-x}}
                \\cos^{-1}\\left(\\sqrt{\\dfrac{x}{y}}\\right),   & x < y \\\\
              \\dfrac{1}{\\sqrt{y}},                          & x = y \\\\
              \\dfrac{1}{\\sqrt{x-y}}
                \\cosh^{-1}\\left(\\sqrt{\\dfrac{x}{y}}\\right),  & x > y \\\\
            \\end{cases}.
        
        **Examples**
        
        Some special values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> elliprc(1,2)*4; elliprc(0,1)*2; +pi
            3.141592653589793238462643
            3.141592653589793238462643
            3.141592653589793238462643
            >>> elliprc(1,0)
            +inf
            >>> elliprc(5,5)**2
            0.2
            >>> elliprc(1,inf); elliprc(inf,1); elliprc(inf,inf)
            0.0
            0.0
            0.0
        
        Comparing with the elementary closed-form solution::
        
            >>> elliprc('1/3', '1/5'); sqrt(7.5)*acosh(sqrt('5/3'))
            2.041630778983498390751238
            2.041630778983498390751238
            >>> elliprc('1/5', '1/3'); sqrt(7.5)*acos(sqrt('3/5'))
            1.875180765206547065111085
            1.875180765206547065111085
        
        Comparing with numerical integration::
        
            >>> q = extradps(25)(quad)
            >>> elliprc(2, -3, pv=True)
            0.3333969101113672670749334
            >>> elliprc(2, -3, pv=False)
            (0.3333969101113672670749334 + 0.7024814731040726393156375j)
            >>> 0.5*q(lambda t: 1/(sqrt(t+2)*(t-3)), [0,3-j,6,inf])
            (0.3333969101113672670749334 + 0.7024814731040726393156375j)
        
        """
    @staticmethod
    def elliprd(ctx, x, y, z):
        """
        
        Evaluates the degenerate Carlson symmetric elliptic integral
        of the third kind or Carlson elliptic integral of the
        second kind `R_D(x,y,z) = R_J(x,y,z,z)`.
        
        See :func:`~mpmath.elliprj` for additional information.
        
        **Examples**
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> elliprd(1,2,3)
            0.2904602810289906442326534
            >>> elliprj(1,2,3,3)
            0.2904602810289906442326534
        
        The so-called *second lemniscate constant*, a transcendental number::
        
            >>> elliprd(0,2,1)/3
            0.5990701173677961037199612
            >>> extradps(25)(quad)(lambda t: t**2/sqrt(1-t**4), [0,1])
            0.5990701173677961037199612
            >>> gamma('3/4')**2/sqrt(2*pi)
            0.5990701173677961037199612
        
        """
    @staticmethod
    def elliprf(ctx, x, y, z):
        """
        
        Evaluates the Carlson symmetric elliptic integral of the first kind
        
        .. math ::
        
            R_F(x,y,z) = \\frac{1}{2}
                \\int_0^{\\infty} \\frac{dt}{\\sqrt{(t+x)(t+y)(t+z)}}
        
        which is defined for `x,y,z \\notin (-\\infty,0)`, and with
        at most one of `x,y,z` being zero.
        
        For real `x,y,z \\ge 0`, the principal square root is taken in the integrand.
        For complex `x,y,z`, the principal square root is taken as `t \\to \\infty`
        and as `t \\to 0` non-principal branches are chosen as necessary so as to
        make the integrand continuous.
        
        **Examples**
        
        Some basic values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> elliprf(0,1,1); pi/2
            1.570796326794896619231322
            1.570796326794896619231322
            >>> elliprf(0,1,inf)
            0.0
            >>> elliprf(1,1,1)
            1.0
            >>> elliprf(2,2,2)**2
            0.5
            >>> elliprf(1,0,0); elliprf(0,0,1); elliprf(0,1,0); elliprf(0,0,0)
            +inf
            +inf
            +inf
            +inf
        
        Representing complete elliptic integrals in terms of `R_F`::
        
            >>> m = mpf(0.75)
            >>> ellipk(m); elliprf(0,1-m,1)
            2.156515647499643235438675
            2.156515647499643235438675
            >>> ellipe(m); elliprf(0,1-m,1)-m*elliprd(0,1-m,1)/3
            1.211056027568459524803563
            1.211056027568459524803563
        
        Some symmetries and argument transformations::
        
            >>> x,y,z = 2,3,4
            >>> elliprf(x,y,z); elliprf(y,x,z); elliprf(z,y,x)
            0.5840828416771517066928492
            0.5840828416771517066928492
            0.5840828416771517066928492
            >>> k = mpf(100000)
            >>> elliprf(k*x,k*y,k*z); k**(-0.5) * elliprf(x,y,z)
            0.001847032121923321253219284
            0.001847032121923321253219284
            >>> l = sqrt(x*y) + sqrt(y*z) + sqrt(z*x)
            >>> elliprf(x,y,z); 2*elliprf(x+l,y+l,z+l)
            0.5840828416771517066928492
            0.5840828416771517066928492
            >>> elliprf((x+l)/4,(y+l)/4,(z+l)/4)
            0.5840828416771517066928492
        
        Comparing with numerical integration::
        
            >>> x,y,z = 2,3,4
            >>> elliprf(x,y,z)
            0.5840828416771517066928492
            >>> f = lambda t: 0.5*((t+x)*(t+y)*(t+z))**(-0.5)
            >>> q = extradps(25)(quad)
            >>> q(f, [0,inf])
            0.5840828416771517066928492
        
        With the following arguments, the square root in the integrand becomes
        discontinuous at `t = 1/2` if the principal branch is used. To obtain
        the right value, `-\\sqrt{r}` must be taken instead of `\\sqrt{r}`
        on `t \\in (0, 1/2)`::
        
            >>> x,y,z = j-1,j,0
            >>> elliprf(x,y,z)
            (0.7961258658423391329305694 - 1.213856669836495986430094j)
            >>> -q(f, [0,0.5]) + q(f, [0.5,inf])
            (0.7961258658423391329305694 - 1.213856669836495986430094j)
        
        The so-called *first lemniscate constant*, a transcendental number::
        
            >>> elliprf(0,1,2)
            1.31102877714605990523242
            >>> extradps(25)(quad)(lambda t: 1/sqrt(1-t**4), [0,1])
            1.31102877714605990523242
            >>> gamma('1/4')**2/(4*sqrt(2*pi))
            1.31102877714605990523242
        
        **References**
        
        1. [Carlson]_
        2. [DLMF]_ Chapter 19. Elliptic Integrals
        
        """
    @staticmethod
    def elliprg(ctx, x, y, z):
        """
        
        Evaluates the Carlson completely symmetric elliptic integral
        of the second kind
        
        .. math ::
        
            R_G(x,y,z) = \\frac{1}{4} \\int_0^{\\infty}
                \\frac{t}{\\sqrt{(t+x)(t+y)(t+z)}}
                \\left( \\frac{x}{t+x} + \\frac{y}{t+y} + \\frac{z}{t+z}\\right) dt.
        
        **Examples**
        
        Evaluation for real and complex arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> elliprg(0,1,1)*4; +pi
            3.141592653589793238462643
            3.141592653589793238462643
            >>> elliprg(0,0.5,1)
            0.6753219405238377512600874
            >>> chop(elliprg(1+j, 1-j, 2))
            1.172431327676416604532822
        
        A double integral that can be evaluated in terms of `R_G`::
        
            >>> x,y,z = 2,3,4
            >>> def f(t,u):
            ...     st = fp.sin(t); ct = fp.cos(t)
            ...     su = fp.sin(u); cu = fp.cos(u)
            ...     return (x*(st*cu)**2 + y*(st*su)**2 + z*ct**2)**0.5 * st
            ...
            >>> nprint(mpf(fp.quad(f, [0,fp.pi], [0,2*fp.pi])/(4*fp.pi)), 13)
            1.725503028069
            >>> nprint(elliprg(x,y,z), 13)
            1.725503028069
        
        """
    @staticmethod
    def elliprj(ctx, x, y, z, p, integration = 1):
        """
        
        Evaluates the Carlson symmetric elliptic integral of the third kind
        
        .. math ::
        
            R_J(x,y,z,p) = \\frac{3}{2}
                \\int_0^{\\infty} \\frac{dt}{(t+p)\\sqrt{(t+x)(t+y)(t+z)}}.
        
        Like :func:`~mpmath.elliprf`, the branch of the square root in the integrand
        is defined so as to be continuous along the path of integration for
        complex values of the arguments.
        
        **Examples**
        
        Some values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> elliprj(1,1,1,1)
            1.0
            >>> elliprj(2,2,2,2); 1/(2*sqrt(2))
            0.3535533905932737622004222
            0.3535533905932737622004222
            >>> elliprj(0,1,2,2)
            1.067937989667395702268688
            >>> 3*(2*gamma('5/4')**2-pi**2/gamma('1/4')**2)/(sqrt(2*pi))
            1.067937989667395702268688
            >>> elliprj(0,1,1,2); 3*pi*(2-sqrt(2))/4
            1.380226776765915172432054
            1.380226776765915172432054
            >>> elliprj(1,3,2,0); elliprj(0,1,1,0); elliprj(0,0,0,0)
            +inf
            +inf
            +inf
            >>> elliprj(1,inf,1,0); elliprj(1,1,1,inf)
            0.0
            0.0
            >>> chop(elliprj(1+j, 1-j, 1, 1))
            0.8505007163686739432927844
        
        Scale transformation::
        
            >>> x,y,z,p = 2,3,4,5
            >>> k = mpf(100000)
            >>> elliprj(k*x,k*y,k*z,k*p); k**(-1.5)*elliprj(x,y,z,p)
            4.521291677592745527851168e-9
            4.521291677592745527851168e-9
        
        Comparing with numerical integration::
        
            >>> elliprj(1,2,3,4)
            0.2398480997495677621758617
            >>> f = lambda t: 1/((t+4)*sqrt((t+1)*(t+2)*(t+3)))
            >>> 1.5*quad(f, [0,inf])
            0.2398480997495677621758617
            >>> elliprj(1,2+1j,3,4-2j)
            (0.216888906014633498739952 + 0.04081912627366673332369512j)
            >>> f = lambda t: 1/((t+4-2j)*sqrt((t+1)*(t+2+1j)*(t+3)))
            >>> 1.5*quad(f, [0,inf])
            (0.216888906014633498739952 + 0.04081912627366673332369511j)
        
        """
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def erfi(ctx, *args, **kwargs):
        """
        
        Computes the imaginary error function, `\\mathrm{erfi}(x)`.
        The imaginary error function is defined in analogy with the
        error function, but with a positive sign in the integrand:
        
        .. math ::
        
          \\mathrm{erfi}(x) = \\frac{2}{\\sqrt \\pi} \\int_0^x \\exp(t^2) \\,dt
        
        Whereas the error function rapidly converges to 1 as `x` grows,
        the imaginary error function rapidly diverges to infinity.
        The functions are related as
        `\\mathrm{erfi}(x) = -i\\,\\mathrm{erf}(ix)` for all complex
        numbers `x`.
        
        **Examples**
        
        Basic values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> erfi(0)
            0.0
            >>> erfi(1)
            1.65042575879754
            >>> erfi(-1)
            -1.65042575879754
            >>> erfi(inf)
            +inf
            >>> erfi(-inf)
            -inf
        
        Note the symmetry between erf and erfi::
        
            >>> erfi(3j)
            (0.0 + 0.999977909503001j)
            >>> erf(3)
            0.999977909503001
            >>> erf(1+2j)
            (-0.536643565778565 - 5.04914370344703j)
            >>> erfi(2+1j)
            (-5.04914370344703 - 0.536643565778565j)
        
        Large arguments are supported::
        
            >>> erfi(1000)
            1.71130938718796e+434291
            >>> erfi(10**10)
            7.3167287567024e+43429448190325182754
            >>> erfi(-10**10)
            -7.3167287567024e+43429448190325182754
            >>> erfi(1000-500j)
            (2.49895233563961e+325717 + 2.6846779342253e+325717j)
            >>> erfi(100000j)
            (0.0 + 1.0j)
            >>> erfi(-100000j)
            (0.0 - 1.0j)
        
        
        """
    @staticmethod
    def erfinv(ctx, *args, **kwargs):
        """
        
        Computes the inverse error function, satisfying
        
        .. math ::
        
            \\mathrm{erf}(\\mathrm{erfinv}(x)) =
            \\mathrm{erfinv}(\\mathrm{erf}(x)) = x.
        
        This function is defined only for `-1 \\le x \\le 1`.
        
        **Examples**
        
        Special values include::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> erfinv(0)
            0.0
            >>> erfinv(1)
            +inf
            >>> erfinv(-1)
            -inf
        
        The domain is limited to the standard interval::
        
            >>> erfinv(2)
            Traceback (most recent call last):
              ...
            ValueError: erfinv(x) is defined only for -1 <= x <= 1
        
        It is simple to check that :func:`~mpmath.erfinv` computes inverse values of
        :func:`~mpmath.erf` as promised::
        
            >>> erf(erfinv(0.75))
            0.75
            >>> erf(erfinv(-0.995))
            -0.995
        
        :func:`~mpmath.erfinv` supports arbitrary-precision evaluation::
        
            >>> mp.dps = 50
            >>> x = erf(2)
            >>> x
            0.99532226501895273416206925636725292861089179704006
            >>> erfinv(x)
            2.0
        
        A definite integral involving the inverse error function::
        
            >>> mp.dps = 15
            >>> quad(erfinv, [0, 1])
            0.564189583547756
            >>> 1/sqrt(pi)
            0.564189583547756
        
        The inverse error function can be used to generate random numbers
        with a Gaussian distribution (although this is a relatively
        inefficient algorithm)::
        
            >>> nprint([erfinv(2*rand()-1) for n in range(6)]) # doctest: +SKIP
            [-0.586747, 1.10233, -0.376796, 0.926037, -0.708142, -0.732012]
        
        """
    @staticmethod
    def eta(ctx, *args, **kwargs):
        """
        
        Returns the Dedekind eta function of tau in the upper half-plane.
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> eta(1j); gamma(0.25) / (2*pi**0.75)
            (0.7682254223260566590025942 + 0.0j)
            0.7682254223260566590025942
            >>> tau = sqrt(2) + sqrt(5)*1j
            >>> eta(-1/tau); sqrt(-1j*tau) * eta(tau)
            (0.9022859908439376463573294 + 0.07985093673948098408048575j)
            (0.9022859908439376463573295 + 0.07985093673948098408048575j)
            >>> eta(tau+1); exp(pi*1j/12) * eta(tau)
            (0.4493066139717553786223114 + 0.3290014793877986663915939j)
            (0.4493066139717553786223114 + 0.3290014793877986663915939j)
            >>> f = lambda z: diff(eta, z) / eta(z)
            >>> chop(36*diff(f,tau)**2 - 24*diff(f,tau,2)*f(tau) + diff(f,tau,3))
            0.0
        
        """
    @staticmethod
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
    @staticmethod
    def eulerpoly(ctx, *args, **kwargs):
        """
        
        Evaluates the Euler polynomial `E_n(z)`, defined by the generating function
        representation
        
        .. math ::
        
            \\frac{2e^{zt}}{e^t+1} = \\sum_{n=0}^\\infty E_n(z) \\frac{t^n}{n!}.
        
        The Euler polynomials may also be represented in terms of
        Bernoulli polynomials (see :func:`~mpmath.bernpoly`) using various formulas, for
        example
        
        .. math ::
        
            E_n(z) = \\frac{2}{n+1} \\left(
                B_n(z)-2^{n+1}B_n\\left(\\frac{z}{2}\\right)
            \\right).
        
        Special values include the Euler numbers `E_n = 2^n E_n(1/2)` (see
        :func:`~mpmath.eulernum`).
        
        **Examples**
        
        Computing the coefficients of the first few Euler polynomials::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> for n in range(6):
            ...     chop(taylor(lambda z: eulerpoly(n,z), 0, n))
            ...
            [1.0]
            [-0.5, 1.0]
            [0.0, -1.0, 1.0]
            [0.25, 0.0, -1.5, 1.0]
            [0.0, 1.0, 0.0, -2.0, 1.0]
            [-0.5, 0.0, 2.5, 0.0, -2.5, 1.0]
        
        Evaluation for arbitrary `z`::
        
            >>> eulerpoly(2,3)
            6.0
            >>> eulerpoly(5,4)
            423.5
            >>> eulerpoly(35, 11111111112)
            3.994957561486776072734601e+351
            >>> eulerpoly(4, 10+20j)
            (-47990.0 - 235980.0j)
            >>> eulerpoly(2, '-3.5e-5')
            0.000035001225
            >>> eulerpoly(3, 0.5)
            0.0
            >>> eulerpoly(55, -10**80)
            -1.0e+4400
            >>> eulerpoly(5, -inf)
            -inf
            >>> eulerpoly(6, -inf)
            +inf
        
        Computing Euler numbers::
        
            >>> 2**26 * eulerpoly(26,0.5)
            -4087072509293123892361.0
            >>> eulernum(26)
            -4087072509293123892361.0
        
        Evaluation is accurate for large `n` and small `z`::
        
            >>> eulerpoly(100, 0.5)
            2.29047999988194114177943e+108
            >>> eulerpoly(1000, 10.5)
            3.628120031122876847764566e+2070
            >>> eulerpoly(10000, 10.5)
            1.149364285543783412210773e+30688
        """
    @staticmethod
    def expint(ctx, *args, **kwargs):
        """
        
        :func:`~mpmath.expint(n,z)` gives the generalized exponential integral
        or En-function,
        
        .. math ::
        
            \\mathrm{E}_n(z) = \\int_1^{\\infty} \\frac{e^{-zt}}{t^n} dt,
        
        where `n` and `z` may both be complex numbers. The case with `n = 1` is
        also given by :func:`~mpmath.e1`.
        
        **Examples**
        
        Evaluation at real and complex arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> expint(1, 6.25)
            0.0002704758872637179088496194
            >>> expint(-3, 2+3j)
            (0.00299658467335472929656159 + 0.06100816202125885450319632j)
            >>> expint(2+3j, 4-5j)
            (0.001803529474663565056945248 - 0.002235061547756185403349091j)
        
        At negative integer values of `n`, `E_n(z)` reduces to a
        rational-exponential function::
        
            >>> f = lambda n, z: fac(n)*sum(z**k/fac(k-1) for k in range(1,n+2))/\\
            ...     exp(z)/z**(n+2)
            >>> n = 3
            >>> z = 1/pi
            >>> expint(-n,z)
            584.2604820613019908668219
            >>> f(n,z)
            584.2604820613019908668219
            >>> n = 5
            >>> expint(-n,z)
            115366.5762594725451811138
            >>> f(n,z)
            115366.5762594725451811138
        """
    @staticmethod
    def expm1(ctx, *args, **kwargs):
        """
        
        Computes `e^x - 1`, accurately for small `x`.
        
        Unlike the expression ``exp(x) - 1``, ``expm1(x)`` does not suffer from
        potentially catastrophic cancellation::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> exp(1e-10)-1; print(expm1(1e-10))
            1.00000008274037e-10
            1.00000000005e-10
            >>> exp(1e-20)-1; print(expm1(1e-20))
            0.0
            1.0e-20
            >>> 1/(exp(1e-20)-1)
            Traceback (most recent call last):
              ...
            ZeroDivisionError
            >>> 1/expm1(1e-20)
            1.0e+20
        
        Evaluation works for extremely tiny values::
        
            >>> expm1(0)
            0.0
            >>> expm1('1e-10000000')
            1.0e-10000000
        
        """
    @staticmethod
    def extradps(ctx, n, normalize_output = False):
        """
        
        This function is analogous to extraprec (see documentation)
        but changes the decimal precision instead of the number of bits.
        """
    @staticmethod
    def extraprec(ctx, n, normalize_output = False):
        """
        
        The block
        
            with extraprec(n):
                <code>
        
        increases the precision n bits, executes <code>, and then
        restores the precision.
        
        extraprec(n)(f) returns a decorated version of the function f
        that increases the working precision by n bits before execution,
        and restores the parent precision afterwards. With
        normalize_output=True, it rounds the return value to the parent
        precision.
        """
    @staticmethod
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
    @staticmethod
    def fac2(ctx, *args, **kwargs):
        """
        
        Computes the double factorial `x!!`, defined for integers
        `x > 0` by
        
        .. math ::
        
            x!! = \\begin{cases}
                1 \\cdot 3 \\cdots (x-2) \\cdot x & x \\;\\mathrm{odd} \\\\
                2 \\cdot 4 \\cdots (x-2) \\cdot x & x \\;\\mathrm{even}
            \\end{cases}
        
        and more generally by [1]
        
        .. math ::
        
            x!! = 2^{x/2} \\left(\\frac{\\pi}{2}\\right)^{(\\cos(\\pi x)-1)/4}
                  \\Gamma\\left(\\frac{x}{2}+1\\right).
        
        **Examples**
        
        The integer sequence of double factorials begins::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> nprint([fac2(n) for n in range(10)])
            [1.0, 1.0, 2.0, 3.0, 8.0, 15.0, 48.0, 105.0, 384.0, 945.0]
        
        For large `x`, double factorials follow a Stirling-like asymptotic
        approximation::
        
            >>> x = mpf(10000)
            >>> fac2(x)
            5.97272691416282e+17830
            >>> sqrt(pi)*x**((x+1)/2)*exp(-x/2)
            5.97262736954392e+17830
        
        The recurrence formula `x!! = x (x-2)!!` can be reversed to
        define the double factorial of negative odd integers (but
        not negative even integers)::
        
            >>> fac2(-1), fac2(-3), fac2(-5), fac2(-7)
            (1.0, -1.0, 0.333333333333333, -0.0666666666666667)
            >>> fac2(-2)
            Traceback (most recent call last):
              ...
            ValueError: gamma function pole
        
        With the exception of the poles at negative even integers,
        :func:`~mpmath.fac2` supports evaluation for arbitrary complex arguments.
        The recurrence formula is valid generally::
        
            >>> fac2(pi+2j)
            (-1.3697207890154e-12 + 3.93665300979176e-12j)
            >>> (pi+2j)*fac2(pi-2+2j)
            (-1.3697207890154e-12 + 3.93665300979176e-12j)
        
        Double factorials should not be confused with nested factorials,
        which are immensely larger::
        
            >>> fac(fac(20))
            5.13805976125208e+43675043585825292774
            >>> fac2(20)
            3715891200.0
        
        Double factorials appear, among other things, in series expansions
        of Gaussian functions and the error function. Infinite series
        include::
        
            >>> nsum(lambda k: 1/fac2(k), [0, inf])
            3.05940740534258
            >>> sqrt(e)*(1+sqrt(pi/2)*erf(sqrt(2)/2))
            3.05940740534258
            >>> nsum(lambda k: 2**k/fac2(2*k-1), [1, inf])
            4.06015693855741
            >>> e * erf(1) * sqrt(pi)
            4.06015693855741
        
        A beautiful Ramanujan sum::
        
            >>> nsum(lambda k: (-1)**k*(fac2(2*k-1)/fac2(2*k))**3, [0,inf])
            0.90917279454693
            >>> (gamma('9/8')/gamma('5/4')/gamma('7/8'))**2
            0.90917279454693
        
        **References**
        
        1. http://functions.wolfram.com/GammaBetaErf/Factorial2/27/01/0002/
        
        2. http://mathworld.wolfram.com/DoubleFactorial.html
        
        """
    @staticmethod
    def fadd(ctx, x, y, **kwargs):
        """
        
        Adds the numbers *x* and *y*, giving a floating-point result,
        optionally using a custom precision and rounding mode.
        
        The default precision is the working precision of the context.
        You can specify a custom precision in bits by passing the *prec* keyword
        argument, or by providing an equivalent decimal precision with the *dps*
        keyword argument. If the precision is set to ``+inf``, or if the flag
        *exact=True* is passed, an exact addition with no rounding is performed.
        
        When the precision is finite, the optional *rounding* keyword argument
        specifies the direction of rounding. Valid options are ``'n'`` for
        nearest (default), ``'f'`` for floor, ``'c'`` for ceiling, ``'d'``
        for down, ``'u'`` for up.
        
        **Examples**
        
        Using :func:`~mpmath.fadd` with precision and rounding control::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fadd(2, 1e-20)
            mpf('2.0')
            >>> fadd(2, 1e-20, rounding='u')
            mpf('2.0000000000000004')
            >>> nprint(fadd(2, 1e-20, prec=100), 25)
            2.00000000000000000001
            >>> nprint(fadd(2, 1e-20, dps=15), 25)
            2.0
            >>> nprint(fadd(2, 1e-20, dps=25), 25)
            2.00000000000000000001
            >>> nprint(fadd(2, 1e-20, exact=True), 25)
            2.00000000000000000001
        
        Exact addition avoids cancellation errors, enforcing familiar laws
        of numbers such as `x+y-x = y`, which don't hold in floating-point
        arithmetic with finite precision::
        
            >>> x, y = mpf(2), mpf('1e-1000')
            >>> print(x + y - x)
            0.0
            >>> print(fadd(x, y, prec=inf) - x)
            1.0e-1000
            >>> print(fadd(x, y, exact=True) - x)
            1.0e-1000
        
        Exact addition can be inefficient and may be impossible to perform
        with large magnitude differences::
        
            >>> fadd(1, '1e-100000000000000000000', prec=inf)
            Traceback (most recent call last):
              ...
            OverflowError: the exact result does not fit in memory
        
        """
    @staticmethod
    def fdiv(ctx, x, y, **kwargs):
        """
        
        Divides the numbers *x* and *y*, giving a floating-point result,
        optionally using a custom precision and rounding mode.
        
        See the documentation of :func:`~mpmath.fadd` for a detailed description
        of how to specify precision and rounding.
        
        **Examples**
        
        The result is an mpmath number::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fdiv(3, 2)
            mpf('1.5')
            >>> fdiv(2, 3)
            mpf('0.66666666666666663')
            >>> fdiv(2+4j, 0.5)
            mpc(real='4.0', imag='8.0')
        
        The rounding direction and precision can be controlled::
        
            >>> fdiv(2, 3, dps=3)    # Should be accurate to at least 3 digits
            mpf('0.6666259765625')
            >>> fdiv(2, 3, rounding='d')
            mpf('0.66666666666666663')
            >>> fdiv(2, 3, prec=60)
            mpf('0.66666666666666667')
            >>> fdiv(2, 3, rounding='u')
            mpf('0.66666666666666674')
        
        Checking the error of a division by performing it at higher precision::
        
            >>> fdiv(2, 3) - fdiv(2, 3, prec=100)
            mpf('-3.7007434154172148e-17')
        
        Unlike :func:`~mpmath.fadd`, :func:`~mpmath.fmul`, etc., exact division is not
        allowed since the quotient of two floating-point numbers generally
        does not have an exact floating-point representation. (In the
        future this might be changed to allow the case where the division
        is actually exact.)
        
            >>> fdiv(2, 3, exact=True)
            Traceback (most recent call last):
              ...
            ValueError: division is not an exact operation
        
        """
    @staticmethod
    def ff(ctx, x, n):
        """
        
        Computes the falling factorial,
        
        .. math ::
        
            (x)_n = x (x-1) \\cdots (x-n+1) = \\frac{\\Gamma(x+1)}{\\Gamma(x-n+1)}
        
        where the rightmost expression is valid for nonintegral `n`.
        
        **Examples**
        
        For integral `n`, the falling factorial is a polynomial::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> for n in range(5):
            ...     nprint(taylor(lambda x: ff(x,n), 0, n))
            ...
            [1.0]
            [0.0, 1.0]
            [0.0, -1.0, 1.0]
            [0.0, 2.0, -3.0, 1.0]
            [0.0, -6.0, 11.0, -6.0, 1.0]
        
        Evaluation is supported for arbitrary arguments::
        
            >>> ff(2+3j, 5.5)
            (-720.41085888203 + 316.101124983878j)
        """
    @staticmethod
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
    @staticmethod
    def fmul(ctx, x, y, **kwargs):
        """
        
        Multiplies the numbers *x* and *y*, giving a floating-point result,
        optionally using a custom precision and rounding mode.
        
        See the documentation of :func:`~mpmath.fadd` for a detailed description
        of how to specify precision and rounding.
        
        **Examples**
        
        The result is an mpmath number::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fmul(2, 5.0)
            mpf('10.0')
            >>> fmul(0.5j, 0.5)
            mpc(real='0.0', imag='0.25')
        
        Avoiding roundoff::
        
            >>> x, y = 10**10+1, 10**15+1
            >>> print(x*y)
            10000000001000010000000001
            >>> print(mpf(x) * mpf(y))
            1.0000000001e+25
            >>> print(int(mpf(x) * mpf(y)))
            10000000001000011026399232
            >>> print(int(fmul(x, y)))
            10000000001000011026399232
            >>> print(int(fmul(x, y, dps=25)))
            10000000001000010000000001
            >>> print(int(fmul(x, y, exact=True)))
            10000000001000010000000001
        
        Exact multiplication with complex numbers can be inefficient and may
        be impossible to perform with large magnitude differences between
        real and imaginary parts::
        
            >>> x = 1+2j
            >>> y = mpc(2, '1e-100000000000000000000')
            >>> fmul(x, y)
            mpc(real='2.0', imag='4.0')
            >>> fmul(x, y, rounding='u')
            mpc(real='2.0', imag='4.0000000000000009')
            >>> fmul(x, y, exact=True)
            Traceback (most recent call last):
              ...
            OverflowError: the exact result does not fit in memory
        
        """
    @staticmethod
    def fneg(ctx, x, **kwargs):
        """
        
        Negates the number *x*, giving a floating-point result, optionally
        using a custom precision and rounding mode.
        
        See the documentation of :func:`~mpmath.fadd` for a detailed description
        of how to specify precision and rounding.
        
        **Examples**
        
        An mpmath number is returned::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fneg(2.5)
            mpf('-2.5')
            >>> fneg(-5+2j)
            mpc(real='5.0', imag='-2.0')
        
        Precise control over rounding is possible::
        
            >>> x = fadd(2, 1e-100, exact=True)
            >>> fneg(x)
            mpf('-2.0')
            >>> fneg(x, rounding='f')
            mpf('-2.0000000000000004')
        
        Negating with and without roundoff::
        
            >>> n = 200000000000000000000001
            >>> print(int(-mpf(n)))
            -200000000000000016777216
            >>> print(int(fneg(n)))
            -200000000000000016777216
            >>> print(int(fneg(n, prec=log(n,2)+1)))
            -200000000000000000000001
            >>> print(int(fneg(n, dps=log(n,10)+1)))
            -200000000000000000000001
            >>> print(int(fneg(n, prec=inf)))
            -200000000000000000000001
            >>> print(int(fneg(n, dps=inf)))
            -200000000000000000000001
            >>> print(int(fneg(n, exact=True)))
            -200000000000000000000001
        
        """
    @staticmethod
    def fprod(ctx, factors):
        """
        
        Calculates a product containing a finite number of factors (for
        infinite products, see :func:`~mpmath.nprod`). The factors will be
        converted to mpmath numbers.
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fprod([1, 2, 0.5, 7])
            mpf('7.0')
        
        """
    @staticmethod
    def fraction(ctx, p, q):
        """
        
        Given Python integers `(p, q)`, returns a lazy ``mpf`` representing
        the fraction `p/q`. The value is updated with the precision.
        
            >>> from mpmath import *
            >>> mp.dps = 15
            >>> a = fraction(1,100)
            >>> b = mpf(1)/100
            >>> print(a); print(b)
            0.01
            0.01
            >>> mp.dps = 30
            >>> print(a); print(b)      # a will be accurate
            0.01
            0.0100000000000000002081668171172
            >>> mp.dps = 15
        """
    @staticmethod
    def fresnelc(ctx, *args, **kwargs):
        """
        
        Computes the Fresnel cosine integral
        
        .. math ::
        
            C(x) = \\int_0^x \\cos\\left(\\frac{\\pi t^2}{2}\\right) \\,dt
        
        Note that some sources define this function
        without the normalization factor `\\pi/2`.
        
        **Examples**
        
        Some basic values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> fresnelc(0)
            0.0
            >>> fresnelc(inf)
            0.5
            >>> fresnelc(-inf)
            -0.5
            >>> fresnelc(1)
            0.7798934003768228294742064
            >>> fresnelc(1+2j)
            (16.08787137412548041729489 - 36.22568799288165021578758j)
        
        Comparing with the definition::
        
            >>> fresnelc(3)
            0.6057207892976856295561611
            >>> quad(lambda t: cos(pi*t**2/2), [0,3])
            0.6057207892976856295561611
        """
    @staticmethod
    def fresnels(ctx, *args, **kwargs):
        """
        
        Computes the Fresnel sine integral
        
        .. math ::
        
            S(x) = \\int_0^x \\sin\\left(\\frac{\\pi t^2}{2}\\right) \\,dt
        
        Note that some sources define this function
        without the normalization factor `\\pi/2`.
        
        **Examples**
        
        Some basic values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> fresnels(0)
            0.0
            >>> fresnels(inf)
            0.5
            >>> fresnels(-inf)
            -0.5
            >>> fresnels(1)
            0.4382591473903547660767567
            >>> fresnels(1+2j)
            (36.72546488399143842838788 + 15.58775110440458732748279j)
        
        Comparing with the definition::
        
            >>> fresnels(3)
            0.4963129989673750360976123
            >>> quad(lambda t: sin(pi*t**2/2), [0,3])
            0.4963129989673750360976123
        """
    @staticmethod
    def frexp(ctx, x):
        """
        
        Given a real number `x`, returns `(y, n)` with `y \\in [0.5, 1)`,
        `n` a Python integer, and such that `x = y 2^n`. No rounding is
        performed.
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> frexp(7.5)
            (mpf('0.9375'), 3)
        
        """
    @staticmethod
    def fsub(ctx, x, y, **kwargs):
        """
        
        Subtracts the numbers *x* and *y*, giving a floating-point result,
        optionally using a custom precision and rounding mode.
        
        See the documentation of :func:`~mpmath.fadd` for a detailed description
        of how to specify precision and rounding.
        
        **Examples**
        
        Using :func:`~mpmath.fsub` with precision and rounding control::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fsub(2, 1e-20)
            mpf('2.0')
            >>> fsub(2, 1e-20, rounding='d')
            mpf('1.9999999999999998')
            >>> nprint(fsub(2, 1e-20, prec=100), 25)
            1.99999999999999999999
            >>> nprint(fsub(2, 1e-20, dps=15), 25)
            2.0
            >>> nprint(fsub(2, 1e-20, dps=25), 25)
            1.99999999999999999999
            >>> nprint(fsub(2, 1e-20, exact=True), 25)
            1.99999999999999999999
        
        Exact subtraction avoids cancellation errors, enforcing familiar laws
        of numbers such as `x-y+y = x`, which don't hold in floating-point
        arithmetic with finite precision::
        
            >>> x, y = mpf(2), mpf('1e1000')
            >>> print(x - y + y)
            0.0
            >>> print(fsub(x, y, prec=inf) + y)
            2.0
            >>> print(fsub(x, y, exact=True) + y)
            2.0
        
        Exact addition can be inefficient and may be impossible to perform
        with large magnitude differences::
        
            >>> fsub(1, '1e-100000000000000000000', prec=inf)
            Traceback (most recent call last):
              ...
            OverflowError: the exact result does not fit in memory
        
        """
    @staticmethod
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
    @staticmethod
    def gammaprod(ctx, a, b, _infsign = False):
        """
        
        Given iterables `a` and `b`, ``gammaprod(a, b)`` computes the
        product / quotient of gamma functions:
        
        .. math ::
        
            \\frac{\\Gamma(a_0) \\Gamma(a_1) \\cdots \\Gamma(a_p)}
                 {\\Gamma(b_0) \\Gamma(b_1) \\cdots \\Gamma(b_q)}
        
        Unlike direct calls to :func:`~mpmath.gamma`, :func:`~mpmath.gammaprod` considers
        the entire product as a limit and evaluates this limit properly if
        any of the numerator or denominator arguments are nonpositive
        integers such that poles of the gamma function are encountered.
        That is, :func:`~mpmath.gammaprod` evaluates
        
        .. math ::
        
            \\lim_{\\epsilon \\to 0}
            \\frac{\\Gamma(a_0+\\epsilon) \\Gamma(a_1+\\epsilon) \\cdots
                \\Gamma(a_p+\\epsilon)}
                 {\\Gamma(b_0+\\epsilon) \\Gamma(b_1+\\epsilon) \\cdots
                \\Gamma(b_q+\\epsilon)}
        
        In particular:
        
        * If there are equally many poles in the numerator and the
          denominator, the limit is a rational number times the remaining,
          regular part of the product.
        
        * If there are more poles in the numerator, :func:`~mpmath.gammaprod`
          returns ``+inf``.
        
        * If there are more poles in the denominator, :func:`~mpmath.gammaprod`
          returns 0.
        
        **Examples**
        
        The reciprocal gamma function `1/\\Gamma(x)` evaluated at `x = 0`::
        
            >>> from mpmath import *
            >>> mp.dps = 15
            >>> gammaprod([], [0])
            0.0
        
        A limit::
        
            >>> gammaprod([-4], [-3])
            -0.25
            >>> limit(lambda x: gamma(x-1)/gamma(x), -3, direction=1)
            -0.25
            >>> limit(lambda x: gamma(x-1)/gamma(x), -3, direction=-1)
            -0.25
        
        """
    @staticmethod
    def gegenbauer(ctx, *args, **kwargs):
        """
        
        Evaluates the Gegenbauer polynomial, or ultraspherical polynomial,
        
        .. math ::
        
            C_n^{(a)}(z) = {n+2a-1 \\choose n} \\,_2F_1\\left(-n, n+2a;
                a+\\frac{1}{2}; \\frac{1}{2}(1-z)\\right).
        
        When `n` is a nonnegative integer, this formula gives a polynomial
        in `z` of degree `n`, but all parameters are permitted to be
        complex numbers. With `a = 1/2`, the Gegenbauer polynomial
        reduces to a Legendre polynomial.
        
        **Examples**
        
        Evaluation for arbitrary arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> gegenbauer(3, 0.5, -10)
            -2485.0
            >>> gegenbauer(1000, 10, 100)
            3.012757178975667428359374e+2322
            >>> gegenbauer(2+3j, -0.75, -1000j)
            (-5038991.358609026523401901 + 9414549.285447104177860806j)
        
        Evaluation at negative integer orders::
        
            >>> gegenbauer(-4, 2, 1.75)
            -1.0
            >>> gegenbauer(-4, 3, 1.75)
            0.0
            >>> gegenbauer(-4, 2j, 1.75)
            0.0
            >>> gegenbauer(-7, 0.5, 3)
            8989.0
        
        The Gegenbauer polynomials solve the differential equation::
        
            >>> n, a = 4.5, 1+2j
            >>> f = lambda z: gegenbauer(n, a, z)
            >>> for z in [0, 0.75, -0.5j]:
            ...     chop((1-z**2)*diff(f,z,2) - (2*a+1)*z*diff(f,z) + n*(n+2*a)*f(z))
            ...
            0.0
            0.0
            0.0
        
        The Gegenbauer polynomials have generating function
        `(1-2zt+t^2)^{-a}`::
        
            >>> a, z = 2.5, 1
            >>> taylor(lambda t: (1-2*z*t+t**2)**(-a), 0, 3)
            [1.0, 5.0, 15.0, 35.0]
            >>> [gegenbauer(n,a,z) for n in range(4)]
            [1.0, 5.0, 15.0, 35.0]
        
        The Gegenbauer polynomials are orthogonal on `[-1, 1]` with respect
        to the weight `(1-z^2)^{a-\\frac{1}{2}}`::
        
            >>> a, n, m = 2.5, 4, 5
            >>> Cn = lambda z: gegenbauer(n, a, z, zeroprec=1000)
            >>> Cm = lambda z: gegenbauer(m, a, z, zeroprec=1000)
            >>> chop(quad(lambda z: Cn(z)*Cm(z)*(1-z**2)*(a-0.5), [-1, 1]))
            0.0
        """
    @staticmethod
    def grampoint(ctx, *args, **kwargs):
        """
        
        Gives the `n`-th Gram point `g_n`, defined as the solution
        to the equation `\\theta(g_n) = \\pi n` where `\\theta(t)`
        is the Riemann-Siegel theta function (:func:`~mpmath.siegeltheta`).
        
        The first few Gram points are::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> grampoint(0)
            17.84559954041086081682634
            >>> grampoint(1)
            23.17028270124630927899664
            >>> grampoint(2)
            27.67018221781633796093849
            >>> grampoint(3)
            31.71797995476405317955149
        
        Checking the definition::
        
            >>> siegeltheta(grampoint(3))
            9.42477796076937971538793
            >>> 3*pi
            9.42477796076937971538793
        
        A large Gram point::
        
            >>> grampoint(10**10)
            3293531632.728335454561153
        
        Gram points are useful when studying the Z-function
        (:func:`~mpmath.siegelz`). See the documentation of that function
        for additional examples.
        
        :func:`~mpmath.grampoint` can solve the defining equation for
        nonintegral `n`. There is a fixed point where `g(x) = x`::
        
            >>> findroot(lambda x: grampoint(x) - x, 10000)
            9146.698193171459265866198
        
        **References**
        
        1. http://mathworld.wolfram.com/GramPoint.html
        
        """
    @staticmethod
    def hankel1(ctx, *args, **kwargs):
        """
        
        ``hankel1(n,x)`` computes the Hankel function of the first kind,
        which is the complex combination of Bessel functions given by
        
        .. math ::
        
            H_n^{(1)}(x) = J_n(x) + i Y_n(x).
        
        **Plots**
        
        .. literalinclude :: /plots/hankel1.py
        .. image :: /plots/hankel1.png
        .. literalinclude :: /plots/hankel1_c.py
        .. image :: /plots/hankel1_c.png
        
        **Examples**
        
        The Hankel function is generally complex-valued::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> hankel1(2, pi)
            (0.4854339326315091097054957 - 0.0999007139290278787734903j)
            >>> hankel1(3.5, pi)
            (0.2340002029630507922628888 - 0.6419643823412927142424049j)
        """
    @staticmethod
    def hankel2(ctx, *args, **kwargs):
        """
        
        ``hankel2(n,x)`` computes the Hankel function of the second kind,
        which is the complex combination of Bessel functions given by
        
        .. math ::
        
            H_n^{(2)}(x) = J_n(x) - i Y_n(x).
        
        **Plots**
        
        .. literalinclude :: /plots/hankel2.py
        .. image :: /plots/hankel2.png
        .. literalinclude :: /plots/hankel2_c.py
        .. image :: /plots/hankel2_c.png
        
        **Examples**
        
        The Hankel function is generally complex-valued::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> hankel2(2, pi)
            (0.4854339326315091097054957 + 0.0999007139290278787734903j)
            >>> hankel2(3.5, pi)
            (0.2340002029630507922628888 + 0.6419643823412927142424049j)
        """
    @staticmethod
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
    @staticmethod
    def hyp0f1(ctx, b, z, **kwargs):
        """
        
        Gives the hypergeometric function `\\,_0F_1`, sometimes known as the
        confluent limit function, defined as
        
        .. math ::
        
            \\,_0F_1(a,z) = \\sum_{k=0}^{\\infty} \\frac{1}{(a)_k} \\frac{z^k}{k!}.
        
        This function satisfies the differential equation `z f''(z) + a f'(z) = f(z)`,
        and is related to the Bessel function of the first kind (see :func:`~mpmath.besselj`).
        
        ``hyp0f1(a,z)`` is equivalent to ``hyper([],[a],z)``; see documentation for
        :func:`~mpmath.hyper` for more information.
        
        **Examples**
        
        Evaluation for arbitrary arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> hyp0f1(2, 0.25)
            1.130318207984970054415392
            >>> hyp0f1((1,2), 1234567)
            6.27287187546220705604627e+964
            >>> hyp0f1(3+4j, 1000000j)
            (3.905169561300910030267132e+606 + 3.807708544441684513934213e+606j)
        
        Evaluation is supported for arbitrarily large values of `z`,
        using asymptotic expansions::
        
            >>> hyp0f1(1, 10**50)
            2.131705322874965310390701e+8685889638065036553022565
            >>> hyp0f1(1, -10**50)
            1.115945364792025420300208e-13
        
        Verifying the differential equation::
        
            >>> a = 2.5
            >>> f = lambda z: hyp0f1(a,z)
            >>> for z in [0, 10, 3+4j]:
            ...     chop(z*diff(f,z,2) + a*diff(f,z) - f(z))
            ...
            0.0
            0.0
            0.0
        
        """
    @staticmethod
    def hyp1f1(ctx, a, b, z, **kwargs):
        """
        
        Gives the confluent hypergeometric function of the first kind,
        
        .. math ::
        
            \\,_1F_1(a,b,z) = \\sum_{k=0}^{\\infty} \\frac{(a)_k}{(b)_k} \\frac{z^k}{k!},
        
        also known as Kummer's function and sometimes denoted by `M(a,b,z)`. This
        function gives one solution to the confluent (Kummer's) differential equation
        
        .. math ::
        
            z f''(z) + (b-z) f'(z) - af(z) = 0.
        
        A second solution is given by the `U` function; see :func:`~mpmath.hyperu`.
        Solutions are also given in an alternate form by the Whittaker
        functions (:func:`~mpmath.whitm`, :func:`~mpmath.whitw`).
        
        ``hyp1f1(a,b,z)`` is equivalent
        to ``hyper([a],[b],z)``; see documentation for :func:`~mpmath.hyper` for more
        information.
        
        **Examples**
        
        Evaluation for real and complex values of the argument `z`, with
        fixed parameters `a = 2, b = -1/3`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> hyp1f1(2, (-1,3), 3.25)
            -2815.956856924817275640248
            >>> hyp1f1(2, (-1,3), -3.25)
            -1.145036502407444445553107
            >>> hyp1f1(2, (-1,3), 1000)
            -8.021799872770764149793693e+441
            >>> hyp1f1(2, (-1,3), -1000)
            0.000003131987633006813594535331
            >>> hyp1f1(2, (-1,3), 100+100j)
            (-3.189190365227034385898282e+48 - 1.106169926814270418999315e+49j)
        
        Parameters may be complex::
        
            >>> hyp1f1(2+3j, -1+j, 10j)
            (261.8977905181045142673351 + 160.8930312845682213562172j)
        
        Arbitrarily large values of `z` are supported::
        
            >>> hyp1f1(3, 4, 10**20)
            3.890569218254486878220752e+43429448190325182745
            >>> hyp1f1(3, 4, -10**20)
            6.0e-60
            >>> hyp1f1(3, 4, 10**20*j)
            (-1.935753855797342532571597e-20 - 2.291911213325184901239155e-20j)
        
        Verifying the differential equation::
        
            >>> a, b = 1.5, 2
            >>> f = lambda z: hyp1f1(a,b,z)
            >>> for z in [0, -10, 3, 3+4j]:
            ...     chop(z*diff(f,z,2) + (b-z)*diff(f,z) - a*f(z))
            ...
            0.0
            0.0
            0.0
            0.0
        
        An integral representation::
        
            >>> a, b = 1.5, 3
            >>> z = 1.5
            >>> hyp1f1(a,b,z)
            2.269381460919952778587441
            >>> g = lambda t: exp(z*t)*t**(a-1)*(1-t)**(b-a-1)
            >>> gammaprod([b],[a,b-a])*quad(g, [0,1])
            2.269381460919952778587441
        
        
        """
    @staticmethod
    def hyp1f2(ctx, a1, b1, b2, z, **kwargs):
        """
        
        Gives the hypergeometric function `\\,_1F_2(a_1,a_2;b_1,b_2; z)`.
        The call ``hyp1f2(a1,b1,b2,z)`` is equivalent to
        ``hyper([a1],[b1,b2],z)``.
        
        Evaluation works for complex and arbitrarily large arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> a, b, c = 1.5, (-1,3), 2.25
            >>> hyp1f2(a, b, c, 10**20)
            -1.159388148811981535941434e+8685889639
            >>> hyp1f2(a, b, c, -10**20)
            -12.60262607892655945795907
            >>> hyp1f2(a, b, c, 10**20*j)
            (4.237220401382240876065501e+6141851464 - 2.950930337531768015892987e+6141851464j)
            >>> hyp1f2(2+3j, -2j, 0.5j, 10-20j)
            (135881.9905586966432662004 - 86681.95885418079535738828j)
        
        """
    @staticmethod
    def hyp2f0(ctx, a, b, z, **kwargs):
        """
        
        Gives the hypergeometric function `\\,_2F_0`, defined formally by the
        series
        
        .. math ::
        
            \\,_2F_0(a,b;;z) = \\sum_{n=0}^{\\infty} (a)_n (b)_n \\frac{z^n}{n!}.
        
        This series usually does not converge. For small enough `z`, it can be viewed
        as an asymptotic series that may be summed directly with an appropriate
        truncation. When this is not the case, :func:`~mpmath.hyp2f0` gives a regularized sum,
        or equivalently, it uses a representation in terms of the
        hypergeometric U function [1]. The series also converges when either `a` or `b`
        is a nonpositive integer, as it then terminates into a polynomial
        after `-a` or `-b` terms.
        
        **Examples**
        
        Evaluation is supported for arbitrary complex arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> hyp2f0((2,3), 1.25, -100)
            0.07095851870980052763312791
            >>> hyp2f0((2,3), 1.25, 100)
            (-0.03254379032170590665041131 + 0.07269254613282301012735797j)
            >>> hyp2f0(-0.75, 1-j, 4j)
            (-0.3579987031082732264862155 - 3.052951783922142735255881j)
        
        Even with real arguments, the regularized value of 2F0 is often complex-valued,
        but the imaginary part decreases exponentially as `z \\to 0`. In the following
        example, the first call uses complex evaluation while the second has a small
        enough `z` to evaluate using the direct series and thus the returned value
        is strictly real (this should be taken to indicate that the imaginary
        part is less than ``eps``)::
        
            >>> mp.dps = 15
            >>> hyp2f0(1.5, 0.5, 0.05)
            (1.04166637647907 + 8.34584913683906e-8j)
            >>> hyp2f0(1.5, 0.5, 0.0005)
            1.00037535207621
        
        The imaginary part can be retrieved by increasing the working precision::
        
            >>> mp.dps = 80
            >>> nprint(hyp2f0(1.5, 0.5, 0.009).imag)
            1.23828e-46
        
        In the polynomial case (the series terminating), 2F0 can evaluate exactly::
        
            >>> mp.dps = 15
            >>> hyp2f0(-6,-6,2)
            291793.0
            >>> identify(hyp2f0(-2,1,0.25))
            '(5/8)'
        
        The coefficients of the polynomials can be recovered using Taylor expansion::
        
            >>> nprint(taylor(lambda x: hyp2f0(-3,0.5,x), 0, 10))
            [1.0, -1.5, 2.25, -1.875, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            >>> nprint(taylor(lambda x: hyp2f0(-4,0.5,x), 0, 10))
            [1.0, -2.0, 4.5, -7.5, 6.5625, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        
        
        [1] http://people.math.sfu.ca/~cbm/aands/page_504.htm
        """
    @staticmethod
    def hyp2f1(ctx, a, b, c, z, **kwargs):
        """
        
        Gives the Gauss hypergeometric function `\\,_2F_1` (often simply referred to as
        *the* hypergeometric function), defined for `|z| < 1` as
        
        .. math ::
        
            \\,_2F_1(a,b,c,z) = \\sum_{k=0}^{\\infty}
                \\frac{(a)_k (b)_k}{(c)_k} \\frac{z^k}{k!}.
        
        and for `|z| \\ge 1` by analytic continuation, with a branch cut on `(1, \\infty)`
        when necessary.
        
        Special cases of this function include many of the orthogonal polynomials as
        well as the incomplete beta function and other functions. Properties of the
        Gauss hypergeometric function are documented comprehensively in many references,
        for example Abramowitz & Stegun, section 15.
        
        The implementation supports the analytic continuation as well as evaluation
        close to the unit circle where `|z| \\approx 1`. The syntax ``hyp2f1(a,b,c,z)``
        is equivalent to ``hyper([a,b],[c],z)``.
        
        **Examples**
        
        Evaluation with `z` inside, outside and on the unit circle, for
        fixed parameters::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> hyp2f1(2, (1,2), 4, 0.75)
            1.303703703703703703703704
            >>> hyp2f1(2, (1,2), 4, -1.75)
            0.7431290566046919177853916
            >>> hyp2f1(2, (1,2), 4, 1.75)
            (1.418075801749271137026239 - 1.114976146679907015775102j)
            >>> hyp2f1(2, (1,2), 4, 1)
            1.6
            >>> hyp2f1(2, (1,2), 4, -1)
            0.8235498012182875315037882
            >>> hyp2f1(2, (1,2), 4, j)
            (0.9144026291433065674259078 + 0.2050415770437884900574923j)
            >>> hyp2f1(2, (1,2), 4, 2+j)
            (0.9274013540258103029011549 + 0.7455257875808100868984496j)
            >>> hyp2f1(2, (1,2), 4, 0.25j)
            (0.9931169055799728251931672 + 0.06154836525312066938147793j)
        
        Evaluation with complex parameter values::
        
            >>> hyp2f1(1+j, 0.75, 10j, 1+5j)
            (0.8834833319713479923389638 + 0.7053886880648105068343509j)
        
        Evaluation with `z = 1`::
        
            >>> hyp2f1(-2.5, 3.5, 1.5, 1)
            0.0
            >>> hyp2f1(-2.5, 3, 4, 1)
            0.06926406926406926406926407
            >>> hyp2f1(2, 3, 4, 1)
            +inf
        
        Evaluation for huge arguments::
        
            >>> hyp2f1((-1,3), 1.75, 4, '1e100')
            (7.883714220959876246415651e+32 + 1.365499358305579597618785e+33j)
            >>> hyp2f1((-1,3), 1.75, 4, '1e1000000')
            (7.883714220959876246415651e+333332 + 1.365499358305579597618785e+333333j)
            >>> hyp2f1((-1,3), 1.75, 4, '1e1000000j')
            (1.365499358305579597618785e+333333 - 7.883714220959876246415651e+333332j)
        
        An integral representation::
        
            >>> a,b,c,z = -0.5, 1, 2.5, 0.25
            >>> g = lambda t: t**(b-1) * (1-t)**(c-b-1) * (1-t*z)**(-a)
            >>> gammaprod([c],[b,c-b]) * quad(g, [0,1])
            0.9480458814362824478852618
            >>> hyp2f1(a,b,c,z)
            0.9480458814362824478852618
        
        Verifying the hypergeometric differential equation::
        
            >>> f = lambda z: hyp2f1(a,b,c,z)
            >>> chop(z*(1-z)*diff(f,z,2) + (c-(a+b+1)*z)*diff(f,z) - a*b*f(z))
            0.0
        
        """
    @staticmethod
    def hyp2f2(ctx, a1, a2, b1, b2, z, **kwargs):
        """
        
        Gives the hypergeometric function `\\,_2F_2(a_1,a_2;b_1,b_2; z)`.
        The call ``hyp2f2(a1,a2,b1,b2,z)`` is equivalent to
        ``hyper([a1,a2],[b1,b2],z)``.
        
        Evaluation works for complex and arbitrarily large arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> a, b, c, d = 1.5, (-1,3), 2.25, 4
            >>> hyp2f2(a, b, c, d, 10**20)
            -5.275758229007902299823821e+43429448190325182663
            >>> hyp2f2(a, b, c, d, -10**20)
            2561445.079983207701073448
            >>> hyp2f2(a, b, c, d, 10**20*j)
            (2218276.509664121194836667 - 1280722.539991603850462856j)
            >>> hyp2f2(2+3j, -2j, 0.5j, 4j, 10-20j)
            (80500.68321405666957342788 - 20346.82752982813540993502j)
        
        """
    @staticmethod
    def hyp2f3(ctx, a1, a2, b1, b2, b3, z, **kwargs):
        """
        
        Gives the hypergeometric function `\\,_2F_3(a_1,a_2;b_1,b_2,b_3; z)`.
        The call ``hyp2f3(a1,a2,b1,b2,b3,z)`` is equivalent to
        ``hyper([a1,a2],[b1,b2,b3],z)``.
        
        Evaluation works for arbitrarily large arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> a1,a2,b1,b2,b3 = 1.5, (-1,3), 2.25, 4, (1,5)
            >>> hyp2f3(a1,a2,b1,b2,b3,10**20)
            -4.169178177065714963568963e+8685889590
            >>> hyp2f3(a1,a2,b1,b2,b3,-10**20)
            7064472.587757755088178629
            >>> hyp2f3(a1,a2,b1,b2,b3,10**20*j)
            (-5.163368465314934589818543e+6141851415 + 1.783578125755972803440364e+6141851416j)
            >>> hyp2f3(2+3j, -2j, 0.5j, 4j, -1-j, 10-20j)
            (-2280.938956687033150740228 + 13620.97336609573659199632j)
            >>> hyp2f3(2+3j, -2j, 0.5j, 4j, -1-j, 10000000-20000000j)
            (4.849835186175096516193e+3504 - 3.365981529122220091353633e+3504j)
        
        """
    @staticmethod
    def hyp3f2(ctx, a1, a2, a3, b1, b2, z, **kwargs):
        """
        
        Gives the generalized hypergeometric function `\\,_3F_2`, defined for `|z| < 1`
        as
        
        .. math ::
        
            \\,_3F_2(a_1,a_2,a_3,b_1,b_2,z) = \\sum_{k=0}^{\\infty}
                \\frac{(a_1)_k (a_2)_k (a_3)_k}{(b_1)_k (b_2)_k} \\frac{z^k}{k!}.
        
        and for `|z| \\ge 1` by analytic continuation. The analytic structure of this
        function is similar to that of `\\,_2F_1`, generally with a singularity at
        `z = 1` and a branch cut on `(1, \\infty)`.
        
        Evaluation is supported inside, on, and outside
        the circle of convergence `|z| = 1`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> hyp3f2(1,2,3,4,5,0.25)
            1.083533123380934241548707
            >>> hyp3f2(1,2+2j,3,4,5,-10+10j)
            (0.1574651066006004632914361 - 0.03194209021885226400892963j)
            >>> hyp3f2(1,2,3,4,5,-10)
            0.3071141169208772603266489
            >>> hyp3f2(1,2,3,4,5,10)
            (-0.4857045320523947050581423 - 0.5988311440454888436888028j)
            >>> hyp3f2(0.25,1,1,2,1.5,1)
            1.157370995096772047567631
            >>> (8-pi-2*ln2)/3
            1.157370995096772047567631
            >>> hyp3f2(1+j,0.5j,2,1,-2j,-1)
            (1.74518490615029486475959 + 0.1454701525056682297614029j)
            >>> hyp3f2(1+j,0.5j,2,1,-2j,sqrt(j))
            (0.9829816481834277511138055 - 0.4059040020276937085081127j)
            >>> hyp3f2(-3,2,1,-5,4,1)
            1.41
            >>> hyp3f2(-3,2,1,-5,4,2)
            2.12
        
        Evaluation very close to the unit circle::
        
            >>> hyp3f2(1,2,3,4,5,'1.0001')
            (1.564877796743282766872279 - 3.76821518787438186031973e-11j)
            >>> hyp3f2(1,2,3,4,5,'1+0.0001j')
            (1.564747153061671573212831 + 0.0001305757570366084557648482j)
            >>> hyp3f2(1,2,3,4,5,'0.9999')
            1.564616644881686134983664
            >>> hyp3f2(1,2,3,4,5,'-0.9999')
            0.7823896253461678060196207
        
        .. note ::
        
            Evaluation for `|z-1|` small can currently be inaccurate or slow
            for some parameter combinations.
        
        For various parameter combinations, `\\,_3F_2` admits representation in terms
        of hypergeometric functions of lower degree, or in terms of
        simpler functions::
        
            >>> for a, b, z in [(1,2,-1), (2,0.5,1)]:
            ...     hyp2f1(a,b,a+b+0.5,z)**2
            ...     hyp3f2(2*a,a+b,2*b,a+b+0.5,2*a+2*b,z)
            ...
            0.4246104461966439006086308
            0.4246104461966439006086308
            7.111111111111111111111111
            7.111111111111111111111111
        
            >>> z = 2+3j
            >>> hyp3f2(0.5,1,1.5,2,2,z)
            (0.7621440939243342419729144 + 0.4249117735058037649915723j)
            >>> 4*(pi-2*ellipe(z))/(pi*z)
            (0.7621440939243342419729144 + 0.4249117735058037649915723j)
        
        """
    @staticmethod
    def hyper(ctx, a_s, b_s, z, **kwargs):
        """
        
        Evaluates the generalized hypergeometric function
        
        .. math ::
        
            \\,_pF_q(a_1,\\ldots,a_p; b_1,\\ldots,b_q; z) =
            \\sum_{n=0}^\\infty \\frac{(a_1)_n (a_2)_n \\ldots (a_p)_n}
               {(b_1)_n(b_2)_n\\ldots(b_q)_n} \\frac{z^n}{n!}
        
        where `(x)_n` denotes the rising factorial (see :func:`~mpmath.rf`).
        
        The parameters lists ``a_s`` and ``b_s`` may contain integers,
        real numbers, complex numbers, as well as exact fractions given in
        the form of tuples `(p, q)`. :func:`~mpmath.hyper` is optimized to handle
        integers and fractions more efficiently than arbitrary
        floating-point parameters (since rational parameters are by
        far the most common).
        
        **Examples**
        
        Verifying that :func:`~mpmath.hyper` gives the sum in the definition, by
        comparison with :func:`~mpmath.nsum`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> a,b,c,d = 2,3,4,5
            >>> x = 0.25
            >>> hyper([a,b],[c,d],x)
            1.078903941164934876086237
            >>> fn = lambda n: rf(a,n)*rf(b,n)/rf(c,n)/rf(d,n)*x**n/fac(n)
            >>> nsum(fn, [0, inf])
            1.078903941164934876086237
        
        The parameters can be any combination of integers, fractions,
        floats and complex numbers::
        
            >>> a, b, c, d, e = 1, (-1,2), pi, 3+4j, (2,3)
            >>> x = 0.2j
            >>> hyper([a,b],[c,d,e],x)
            (0.9923571616434024810831887 - 0.005753848733883879742993122j)
            >>> b, e = -0.5, mpf(2)/3
            >>> fn = lambda n: rf(a,n)*rf(b,n)/rf(c,n)/rf(d,n)/rf(e,n)*x**n/fac(n)
            >>> nsum(fn, [0, inf])
            (0.9923571616434024810831887 - 0.005753848733883879742993122j)
        
        The `\\,_0F_0` and `\\,_1F_0` series are just elementary functions::
        
            >>> a, z = sqrt(2), +pi
            >>> hyper([],[],z)
            23.14069263277926900572909
            >>> exp(z)
            23.14069263277926900572909
            >>> hyper([a],[],z)
            (-0.09069132879922920160334114 + 0.3283224323946162083579656j)
            >>> (1-z)**(-a)
            (-0.09069132879922920160334114 + 0.3283224323946162083579656j)
        
        If any `a_k` coefficient is a nonpositive integer, the series terminates
        into a finite polynomial::
        
            >>> hyper([1,1,1,-3],[2,5],1)
            0.7904761904761904761904762
            >>> identify(_)
            '(83/105)'
        
        If any `b_k` is a nonpositive integer, the function is undefined (unless the
        series terminates before the division by zero occurs)::
        
            >>> hyper([1,1,1,-3],[-2,5],1)
            Traceback (most recent call last):
              ...
            ZeroDivisionError: pole in hypergeometric series
            >>> hyper([1,1,1,-1],[-2,5],1)
            1.1
        
        Except for polynomial cases, the radius of convergence `R` of the hypergeometric
        series is either `R = \\infty` (if `p \\le q`), `R = 1` (if `p = q+1`), or
        `R = 0` (if `p > q+1`).
        
        The analytic continuations of the functions with `p = q+1`, i.e. `\\,_2F_1`,
        `\\,_3F_2`,  `\\,_4F_3`, etc, are all implemented and therefore these functions
        can be evaluated for `|z| \\ge 1`. The shortcuts :func:`~mpmath.hyp2f1`, :func:`~mpmath.hyp3f2`
        are available to handle the most common cases (see their documentation),
        but functions of higher degree are also supported via :func:`~mpmath.hyper`::
        
            >>> hyper([1,2,3,4], [5,6,7], 1)   # 4F3 at finite-valued branch point
            1.141783505526870731311423
            >>> hyper([4,5,6,7], [1,2,3], 1)   # 4F3 at pole
            +inf
            >>> hyper([1,2,3,4,5], [6,7,8,9], 10)    # 5F4
            (1.543998916527972259717257 - 0.5876309929580408028816365j)
            >>> hyper([1,2,3,4,5,6], [7,8,9,10,11], 1j)   # 6F5
            (0.9996565821853579063502466 + 0.0129721075905630604445669j)
        
        Near `z = 1` with noninteger parameters::
        
            >>> hyper(['1/3',1,'3/2',2], ['1/5','11/6','41/8'], 1)
            2.219433352235586121250027
            >>> hyper(['1/3',1,'3/2',2], ['1/5','11/6','5/4'], 1)
            +inf
            >>> eps1 = extradps(6)(lambda: 1 - mpf('1e-6'))()
            >>> hyper(['1/3',1,'3/2',2], ['1/5','11/6','5/4'], eps1)
            2923978034.412973409330956
        
        Please note that, as currently implemented, evaluation of `\\,_pF_{p-1}`
        with `p \\ge 3` may be slow or inaccurate when `|z-1|` is small,
        for some parameter values.
        
        Evaluation may be aborted if convergence appears to be too slow.
        The optional ``maxterms`` (limiting the number of series terms) and ``maxprec``
        (limiting the internal precision) keyword arguments can be used
        to control evaluation::
        
            >>> hyper([1,2,3], [4,5,6], 10000)              # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
              ...
            NoConvergence: Hypergeometric series converges too slowly. Try increasing maxterms.
            >>> hyper([1,2,3], [4,5,6], 10000, maxterms=10**6)
            7.622806053177969474396918e+4310
        
        Additional options include ``force_series`` (which forces direct use of
        a hypergeometric series even if another evaluation method might work better)
        and ``asymp_tol`` which controls the target tolerance for using
        asymptotic series.
        
        When `p > q+1`, ``hyper`` computes the (iterated) Borel sum of the divergent
        series. For `\\,_2F_0` the Borel sum has an analytic solution and can be
        computed efficiently (see :func:`~mpmath.hyp2f0`). For higher degrees, the functions
        is evaluated first by attempting to sum it directly as an asymptotic
        series (this only works for tiny `|z|`), and then by evaluating the Borel
        regularized sum using numerical integration. Except for
        special parameter combinations, this can be extremely slow.
        
            >>> hyper([1,1], [], 0.5)          # regularization of 2F0
            (1.340965419580146562086448 + 0.8503366631752726568782447j)
            >>> hyper([1,1,1,1], [1], 0.5)     # regularization of 4F1
            (1.108287213689475145830699 + 0.5327107430640678181200491j)
        
        With the following magnitude of argument, the asymptotic series for `\\,_3F_1`
        gives only a few digits. Using Borel summation, ``hyper`` can produce
        a value with full accuracy::
        
            >>> mp.dps = 15
            >>> hyper([2,0.5,4], [5.25], '0.08', force_series=True)             # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
              ...
            NoConvergence: Hypergeometric series converges too slowly. Try increasing maxterms.
            >>> hyper([2,0.5,4], [5.25], '0.08', asymp_tol=1e-4)
            1.0725535790737
            >>> hyper([2,0.5,4], [5.25], '0.08')
            (1.07269542893559 + 5.54668863216891e-5j)
            >>> hyper([2,0.5,4], [5.25], '-0.08', asymp_tol=1e-4)
            0.946344925484879
            >>> hyper([2,0.5,4], [5.25], '-0.08')
            0.946312503737771
            >>> mp.dps = 25
            >>> hyper([2,0.5,4], [5.25], '-0.08')
            0.9463125037377662296700858
        
        Note that with the positive `z` value, there is a complex part in the
        correct result, which falls below the tolerance of the asymptotic series.
        
        By default, a parameter that appears in both ``a_s`` and ``b_s`` will be removed
        unless it is a nonpositive integer. This generally speeds up evaluation
        by producing a hypergeometric function of lower order.
        This optimization can be disabled by passing ``eliminate=False``.
        
            >>> hyper([1,2,3], [4,5,3], 10000)
            1.268943190440206905892212e+4321
            >>> hyper([1,2,3], [4,5,3], 10000, eliminate=False)             # doctest: +IGNORE_EXCEPTION_DETAIL
            Traceback (most recent call last):
              ...
            NoConvergence: Hypergeometric series converges too slowly. Try increasing maxterms.
            >>> hyper([1,2,3], [4,5,3], 10000, eliminate=False, maxterms=10**6)
            1.268943190440206905892212e+4321
        
        If a nonpositive integer `-n` appears in both ``a_s`` and ``b_s``, this parameter
        cannot be unambiguously removed since it creates a term 0 / 0.
        In this case the hypergeometric series is understood to terminate before
        the division by zero occurs. This convention is consistent with Mathematica.
        An alternative convention of eliminating the parameters can be toggled
        with ``eliminate_all=True``:
        
            >>> hyper([2,-1], [-1], 3)
            7.0
            >>> hyper([2,-1], [-1], 3, eliminate_all=True)
            0.25
            >>> hyper([2], [], 3)
            0.25
        
        """
    @staticmethod
    def hyper2d(ctx, a, b, x, y, **kwargs):
        """
        
        Sums the generalized 2D hypergeometric series
        
        .. math ::
        
            \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
                \\frac{P((a),m,n)}{Q((b),m,n)}
                \\frac{x^m y^n} {m! n!}
        
        where `(a) = (a_1,\\ldots,a_r)`, `(b) = (b_1,\\ldots,b_s)` and where
        `P` and `Q` are products of rising factorials such as `(a_j)_n` or
        `(a_j)_{m+n}`. `P` and `Q` are specified in the form of dicts, with
        the `m` and `n` dependence as keys and parameter lists as values.
        The supported rising factorials are given in the following table
        (note that only a few are supported in `Q`):
        
        +------------+-------------------+--------+
        | Key        |  Rising factorial | `Q`    |
        +============+===================+========+
        | ``'m'``    |   `(a_j)_m`       | Yes    |
        +------------+-------------------+--------+
        | ``'n'``    |   `(a_j)_n`       | Yes    |
        +------------+-------------------+--------+
        | ``'m+n'``  |   `(a_j)_{m+n}`   | Yes    |
        +------------+-------------------+--------+
        | ``'m-n'``  |   `(a_j)_{m-n}`   | No     |
        +------------+-------------------+--------+
        | ``'n-m'``  |   `(a_j)_{n-m}`   | No     |
        +------------+-------------------+--------+
        | ``'2m+n'`` |   `(a_j)_{2m+n}`  | No     |
        +------------+-------------------+--------+
        | ``'2m-n'`` |   `(a_j)_{2m-n}`  | No     |
        +------------+-------------------+--------+
        | ``'2n-m'`` |   `(a_j)_{2n-m}`  | No     |
        +------------+-------------------+--------+
        
        For example, the Appell F1 and F4 functions
        
        .. math ::
        
            F_1 = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
                  \\frac{(a)_{m+n} (b)_m (c)_n}{(d)_{m+n}}
                  \\frac{x^m y^n}{m! n!}
        
            F_4 = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
                  \\frac{(a)_{m+n} (b)_{m+n}}{(c)_m (d)_{n}}
                  \\frac{x^m y^n}{m! n!}
        
        can be represented respectively as
        
            ``hyper2d({'m+n':[a], 'm':[b], 'n':[c]}, {'m+n':[d]}, x, y)``
        
            ``hyper2d({'m+n':[a,b]}, {'m':[c], 'n':[d]}, x, y)``
        
        More generally, :func:`~mpmath.hyper2d` can evaluate any of the 34 distinct
        convergent second-order (generalized Gaussian) hypergeometric
        series enumerated by Horn, as well as the Kampe de Feriet
        function.
        
        The series is computed by rewriting it so that the inner
        series (i.e. the series containing `n` and `y`) has the form of an
        ordinary generalized hypergeometric series and thereby can be
        evaluated efficiently using :func:`~mpmath.hyper`. If possible,
        manually swapping `x` and `y` and the corresponding parameters
        can sometimes give better results.
        
        **Examples**
        
        Two separable cases: a product of two geometric series, and a
        product of two Gaussian hypergeometric functions::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> x, y = mpf(0.25), mpf(0.5)
            >>> hyper2d({'m':1,'n':1}, {}, x,y)
            2.666666666666666666666667
            >>> 1/(1-x)/(1-y)
            2.666666666666666666666667
            >>> hyper2d({'m':[1,2],'n':[3,4]}, {'m':[5],'n':[6]}, x,y)
            4.164358531238938319669856
            >>> hyp2f1(1,2,5,x)*hyp2f1(3,4,6,y)
            4.164358531238938319669856
        
        Some more series that can be done in closed form::
        
            >>> hyper2d({'m':1,'n':1},{'m+n':1},x,y)
            2.013417124712514809623881
            >>> (exp(x)*x-exp(y)*y)/(x-y)
            2.013417124712514809623881
        
        Six of the 34 Horn functions, G1-G3 and H1-H3::
        
            >>> from mpmath import *
            >>> mp.dps = 10; mp.pretty = True
            >>> x, y = 0.0625, 0.125
            >>> a1,a2,b1,b2,c1,c2,d = 1.1,-1.2,-1.3,-1.4,1.5,-1.6,1.7
            >>> hyper2d({'m+n':a1,'n-m':b1,'m-n':b2},{},x,y)  # G1
            1.139090746
            >>> nsum(lambda m,n: rf(a1,m+n)*rf(b1,n-m)*rf(b2,m-n)*\\
            ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
            1.139090746
            >>> hyper2d({'m':a1,'n':a2,'n-m':b1,'m-n':b2},{},x,y)  # G2
            0.9503682696
            >>> nsum(lambda m,n: rf(a1,m)*rf(a2,n)*rf(b1,n-m)*rf(b2,m-n)*\\
            ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
            0.9503682696
            >>> hyper2d({'2n-m':a1,'2m-n':a2},{},x,y)  # G3
            1.029372029
            >>> nsum(lambda m,n: rf(a1,2*n-m)*rf(a2,2*m-n)*\\
            ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
            1.029372029
            >>> hyper2d({'m-n':a1,'m+n':b1,'n':c1},{'m':d},x,y)  # H1
            -1.605331256
            >>> nsum(lambda m,n: rf(a1,m-n)*rf(b1,m+n)*rf(c1,n)/rf(d,m)*\\
            ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
            -1.605331256
            >>> hyper2d({'m-n':a1,'m':b1,'n':[c1,c2]},{'m':d},x,y)  # H2
            -2.35405404
            >>> nsum(lambda m,n: rf(a1,m-n)*rf(b1,m)*rf(c1,n)*rf(c2,n)/rf(d,m)*\\
            ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
            -2.35405404
            >>> hyper2d({'2m+n':a1,'n':b1},{'m+n':c1},x,y)  # H3
            0.974479074
            >>> nsum(lambda m,n: rf(a1,2*m+n)*rf(b1,n)/rf(c1,m+n)*\\
            ...     x**m*y**n/fac(m)/fac(n), [0,inf], [0,inf])
            0.974479074
        
        **References**
        
        1. [SrivastavaKarlsson]_
        2. [Weisstein]_ http://mathworld.wolfram.com/HornFunction.html
        3. [Weisstein]_ http://mathworld.wolfram.com/AppellHypergeometricFunction.html
        
        """
    @staticmethod
    def hypercomb(ctx, function, params = list(), discard_known_zeros = True, **kwargs):
        """
        
        Computes a weighted combination of hypergeometric functions
        
        .. math ::
        
            \\sum_{r=1}^N \\left[ \\prod_{k=1}^{l_r} {w_{r,k}}^{c_{r,k}}
            \\frac{\\prod_{k=1}^{m_r} \\Gamma(\\alpha_{r,k})}{\\prod_{k=1}^{n_r}
            \\Gamma(\\beta_{r,k})}
            \\,_{p_r}F_{q_r}(a_{r,1},\\ldots,a_{r,p}; b_{r,1},
            \\ldots, b_{r,q}; z_r)\\right].
        
        Typically the parameters are linear combinations of a small set of base
        parameters; :func:`~mpmath.hypercomb` permits computing a correct value in
        the case that some of the `\\alpha`, `\\beta`, `b` turn out to be
        nonpositive integers, or if division by zero occurs for some `w^c`,
        assuming that there are opposing singularities that cancel out.
        The limit is computed by evaluating the function with the base
        parameters perturbed, at a higher working precision.
        
        The first argument should be a function that takes the perturbable
        base parameters ``params`` as input and returns `N` tuples
        ``(w, c, alpha, beta, a, b, z)``, where the coefficients ``w``, ``c``,
        gamma factors ``alpha``, ``beta``, and hypergeometric coefficients
        ``a``, ``b`` each should be lists of numbers, and ``z`` should be a single
        number.
        
        **Examples**
        
        The following evaluates
        
        .. math ::
        
            (a-1) \\frac{\\Gamma(a-3)}{\\Gamma(a-4)} \\,_1F_1(a,a-1,z) = e^z(a-4)(a+z-1)
        
        with `a=1, z=3`. There is a zero factor, two gamma function poles, and
        the 1F1 function is singular; all singularities cancel out to give a finite
        value::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> hypercomb(lambda a: [([a-1],[1],[a-3],[a-4],[a],[a-1],3)], [1])
            -180.769832308689
            >>> -9*exp(3)
            -180.769832308689
        
        """
    @staticmethod
    def hyperfac(ctx, *args, **kwargs):
        """
        
        Computes the hyperfactorial, defined for integers as the product
        
        .. math ::
        
            H(n) = \\prod_{k=1}^n k^k.
        
        
        The hyperfactorial satisfies the recurrence formula `H(z) = z^z H(z-1)`.
        It can be defined more generally in terms of the Barnes G-function (see
        :func:`~mpmath.barnesg`) and the gamma function by the formula
        
        .. math ::
        
            H(z) = \\frac{\\Gamma(z+1)^z}{G(z)}.
        
        The extension to complex numbers can also be done via
        the integral representation
        
        .. math ::
        
            H(z) = (2\\pi)^{-z/2} \\exp \\left[
                {z+1 \\choose 2} + \\int_0^z \\log(t!)\\,dt
                \\right].
        
        **Examples**
        
        The rapidly-growing sequence of hyperfactorials begins
        (OEIS A002109)::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> for n in range(10):
            ...     print("%s %s" % (n, hyperfac(n)))
            ...
            0 1.0
            1 1.0
            2 4.0
            3 108.0
            4 27648.0
            5 86400000.0
            6 4031078400000.0
            7 3.3197663987712e+18
            8 5.56964379417266e+25
            9 2.15779412229419e+34
        
        Some even larger hyperfactorials are::
        
            >>> hyperfac(1000)
            5.46458120882585e+1392926
            >>> hyperfac(10**10)
            4.60408207642219e+489142638002418704309
        
        The hyperfactorial can be evaluated for arbitrary arguments::
        
            >>> hyperfac(0.5)
            0.880449235173423
            >>> diff(hyperfac, 1)
            0.581061466795327
            >>> hyperfac(pi)
            205.211134637462
            >>> hyperfac(-10+1j)
            (3.01144471378225e+46 - 2.45285242480185e+46j)
        
        The recurrence property of the hyperfactorial holds
        generally::
        
            >>> z = 3-4*j
            >>> hyperfac(z)
            (-4.49795891462086e-7 - 6.33262283196162e-7j)
            >>> z**z * hyperfac(z-1)
            (-4.49795891462086e-7 - 6.33262283196162e-7j)
            >>> z = mpf(-0.6)
            >>> chop(z**z * hyperfac(z-1))
            1.28170142849352
            >>> hyperfac(z)
            1.28170142849352
        
        The hyperfactorial may also be computed using the integral
        definition::
        
            >>> z = 2.5
            >>> hyperfac(z)
            15.9842119922237
            >>> (2*pi)**(-z/2)*exp(binomial(z+1,2) +
            ...     quad(lambda t: loggamma(t+1), [0, z]))
            15.9842119922237
        
        :func:`~mpmath.hyperfac` supports arbitrary-precision evaluation::
        
            >>> mp.dps = 50
            >>> hyperfac(10)
            215779412229418562091680268288000000000000000.0
            >>> hyperfac(1/sqrt(2))
            0.89404818005227001975423476035729076375705084390942
        
        **References**
        
        1. http://oeis.org/A002109
        2. http://mathworld.wolfram.com/Hyperfactorial.html
        
        """
    @staticmethod
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
    @staticmethod
    def hypot(ctx, x, y):
        """
        
        Computes the Euclidean norm of the vector `(x, y)`, equal
        to `\\sqrt{x^2 + y^2}`. Both `x` and `y` must be real.
        """
    @staticmethod
    def hypsum(ctx, p, q, flags, coeffs, z, accurate_small = True, **kwargs):
        ...
    @staticmethod
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
    @staticmethod
    def init_builtins(ctx):
        ...
    @staticmethod
    def isfinite(ctx, x):
        """
        
        Return *True* if *x* is a finite number, i.e. neither
        an infinity or a NaN.
        
            >>> from mpmath import *
            >>> isfinite(inf)
            False
            >>> isfinite(-inf)
            False
            >>> isfinite(3)
            True
            >>> isfinite(nan)
            False
            >>> isfinite(3+4j)
            True
            >>> isfinite(mpc(3,inf))
            False
            >>> isfinite(mpc(nan,3))
            False
        
        """
    @staticmethod
    def isnan(ctx, x):
        """
        
        Return *True* if *x* is a NaN (not-a-number), or for a complex
        number, whether either the real or complex part is NaN;
        otherwise return *False*::
        
            >>> from mpmath import *
            >>> isnan(3.14)
            False
            >>> isnan(nan)
            True
            >>> isnan(mpc(3.14,2.72))
            False
            >>> isnan(mpc(3.14,nan))
            True
        
        """
    @staticmethod
    def isnpint(ctx, x):
        """
        
        Determine if *x* is a nonpositive integer.
        """
    @staticmethod
    def j0(ctx, x):
        """
        Computes the Bessel function `J_0(x)`. See :func:`~mpmath.besselj`.
        """
    @staticmethod
    def j1(ctx, x):
        """
        Computes the Bessel function `J_1(x)`.  See :func:`~mpmath.besselj`.
        """
    @staticmethod
    def jacobi(ctx, *args, **kwargs):
        """
        
        ``jacobi(n, a, b, x)`` evaluates the Jacobi polynomial
        `P_n^{(a,b)}(x)`. The Jacobi polynomials are a special
        case of the hypergeometric function `\\,_2F_1` given by:
        
        .. math ::
        
            P_n^{(a,b)}(x) = {n+a \\choose n}
              \\,_2F_1\\left(-n,1+a+b+n,a+1,\\frac{1-x}{2}\\right).
        
        Note that this definition generalizes to nonintegral values
        of `n`. When `n` is an integer, the hypergeometric series
        terminates after a finite number of terms, giving
        a polynomial in `x`.
        
        **Evaluation of Jacobi polynomials**
        
        A special evaluation is `P_n^{(a,b)}(1) = {n+a \\choose n}`::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> jacobi(4, 0.5, 0.25, 1)
            2.4609375
            >>> binomial(4+0.5, 4)
            2.4609375
        
        A Jacobi polynomial of degree `n` is equal to its
        Taylor polynomial of degree `n`. The explicit
        coefficients of Jacobi polynomials can therefore
        be recovered easily using :func:`~mpmath.taylor`::
        
            >>> for n in range(5):
            ...     nprint(taylor(lambda x: jacobi(n,1,2,x), 0, n))
            ...
            [1.0]
            [-0.5, 2.5]
            [-0.75, -1.5, 5.25]
            [0.5, -3.5, -3.5, 10.5]
            [0.625, 2.5, -11.25, -7.5, 20.625]
        
        For nonintegral `n`, the Jacobi "polynomial" is no longer
        a polynomial::
        
            >>> nprint(taylor(lambda x: jacobi(0.5,1,2,x), 0, 4))
            [0.309983, 1.84119, -1.26933, 1.26699, -1.34808]
        
        **Orthogonality**
        
        The Jacobi polynomials are orthogonal on the interval
        `[-1, 1]` with respect to the weight function
        `w(x) = (1-x)^a (1+x)^b`. That is,
        `w(x) P_n^{(a,b)}(x) P_m^{(a,b)}(x)` integrates to
        zero if `m \\ne n` and to a nonzero number if `m = n`.
        
        The orthogonality is easy to verify using numerical
        quadrature::
        
            >>> P = jacobi
            >>> f = lambda x: (1-x)**a * (1+x)**b * P(m,a,b,x) * P(n,a,b,x)
            >>> a = 2
            >>> b = 3
            >>> m, n = 3, 4
            >>> chop(quad(f, [-1, 1]), 1)
            0.0
            >>> m, n = 4, 4
            >>> quad(f, [-1, 1])
            1.9047619047619
        
        **Differential equation**
        
        The Jacobi polynomials are solutions of the differential
        equation
        
        .. math ::
        
          (1-x^2) y'' + (b-a-(a+b+2)x) y' + n (n+a+b+1) y = 0.
        
        We can verify that :func:`~mpmath.jacobi` approximately satisfies
        this equation::
        
            >>> from mpmath import *
            >>> mp.dps = 15
            >>> a = 2.5
            >>> b = 4
            >>> n = 3
            >>> y = lambda x: jacobi(n,a,b,x)
            >>> x = pi
            >>> A0 = n*(n+a+b+1)*y(x)
            >>> A1 = (b-a-(a+b+2)*x)*diff(y,x)
            >>> A2 = (1-x**2)*diff(y,x,2)
            >>> nprint(A2 + A1 + A0, 1)
            4.0e-12
        
        The difference of order `10^{-12}` is as close to zero as
        it could be at 15-digit working precision, since the terms
        are large::
        
            >>> A0, A1, A2
            (26560.2328981879, -21503.7641037294, -5056.46879445852)
        
        """
    @staticmethod
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
    @staticmethod
    def kei(ctx, n, z, **kwargs):
        """
        
        Computes the Kelvin function kei, which for real arguments gives the
        imaginary part of the (rescaled) Bessel K function of a rotated argument.
        See :func:`~mpmath.ker`.
        """
    @staticmethod
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
    @staticmethod
    def kfrom(ctx, *args, **kwargs):
        """
        
        Returns the elliptic modulus `k`, given any of
        `q, m, k, \\tau, \\bar{q}`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> kfrom(k=0.25)
            0.25
            >>> kfrom(m=mfrom(k=0.25))
            0.25
            >>> kfrom(q=qfrom(k=0.25))
            0.25
            >>> kfrom(tau=taufrom(k=0.25))
            (0.25 + 0.0j)
            >>> kfrom(qbar=qbarfrom(k=0.25))
            0.25
        
        As `q \\to 1` and `q \\to -1`, `k` rapidly approaches
        `1` and `i \\infty` respectively::
        
            >>> kfrom(q=0.75)
            0.9999999999999899166471767
            >>> kfrom(q=-0.75)
            (0.0 + 7041781.096692038332790615j)
            >>> kfrom(q=1)
            1
            >>> kfrom(q=-1)
            (0.0 + +infj)
        """
    @staticmethod
    def kleinj(ctx, *args, **kwargs):
        """
        
        Evaluates the Klein j-invariant, which is a modular function defined for
        `\\tau` in the upper half-plane as
        
        .. math ::
        
            J(\\tau) = \\frac{g_2^3(\\tau)}{g_2^3(\\tau) - 27 g_3^2(\\tau)}
        
        where `g_2` and `g_3` are the modular invariants of the Weierstrass
        elliptic function,
        
        .. math ::
        
            g_2(\\tau) = 60 \\sum_{(m,n) \\in \\mathbb{Z}^2 \\setminus (0,0)} (m \\tau+n)^{-4}
        
            g_3(\\tau) = 140 \\sum_{(m,n) \\in \\mathbb{Z}^2 \\setminus (0,0)} (m \\tau+n)^{-6}.
        
        An alternative, common notation is that of the j-function
        `j(\\tau) = 1728 J(\\tau)`.
        
        **Plots**
        
        .. literalinclude :: /plots/kleinj.py
        .. image :: /plots/kleinj.png
        .. literalinclude :: /plots/kleinj2.py
        .. image :: /plots/kleinj2.png
        
        **Examples**
        
        Verifying the functional equation `J(\\tau) = J(\\tau+1) = J(-\\tau^{-1})`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> tau = 0.625+0.75*j
            >>> tau = 0.625+0.75*j
            >>> kleinj(tau)
            (-0.1507492166511182267125242 + 0.07595948379084571927228948j)
            >>> kleinj(tau+1)
            (-0.1507492166511182267125242 + 0.07595948379084571927228948j)
            >>> kleinj(-1/tau)
            (-0.1507492166511182267125242 + 0.07595948379084571927228946j)
        
        The j-function has a famous Laurent series expansion in terms of the nome
        `\\bar{q}`, `j(\\tau) = \\bar{q}^{-1} + 744 + 196884\\bar{q} + \\ldots`::
        
            >>> mp.dps = 15
            >>> taylor(lambda q: 1728*q*kleinj(qbar=q), 0, 5, singular=True)
            [1.0, 744.0, 196884.0, 21493760.0, 864299970.0, 20245856256.0]
        
        The j-function admits exact evaluation at special algebraic points
        related to the Heegner numbers 1, 2, 3, 7, 11, 19, 43, 67, 163::
        
            >>> @extraprec(10)
            ... def h(n):
            ...     v = (1+sqrt(n)*j)
            ...     if n > 2:
            ...         v *= 0.5
            ...     return v
            ...
            >>> mp.dps = 25
            >>> for n in [1,2,3,7,11,19,43,67,163]:
            ...     n, chop(1728*kleinj(h(n)))
            ...
            (1, 1728.0)
            (2, 8000.0)
            (3, 0.0)
            (7, -3375.0)
            (11, -32768.0)
            (19, -884736.0)
            (43, -884736000.0)
            (67, -147197952000.0)
            (163, -262537412640768000.0)
        
        Also at other special points, the j-function assumes explicit
        algebraic values, e.g.::
        
            >>> chop(1728*kleinj(j*sqrt(5)))
            1264538.909475140509320227
            >>> identify(cbrt(_))      # note: not simplified
            '((100+sqrt(13520))/2)'
            >>> (50+26*sqrt(5))**3
            1264538.909475140509320227
        
        """
    @staticmethod
    def laguerre(ctx, *args, **kwargs):
        """
        
        Gives the generalized (associated) Laguerre polynomial, defined by
        
        .. math ::
        
            L_n^a(z) = \\frac{\\Gamma(n+b+1)}{\\Gamma(b+1) \\Gamma(n+1)}
                \\,_1F_1(-n, a+1, z).
        
        With `a = 0` and `n` a nonnegative integer, this reduces to an ordinary
        Laguerre polynomial, the sequence of which begins
        `L_0(z) = 1, L_1(z) = 1-z, L_2(z) = z^2-2z+1, \\ldots`.
        
        The Laguerre polynomials are orthogonal with respect to the weight
        `z^a e^{-z}` on `[0, \\infty)`.
        
        **Plots**
        
        .. literalinclude :: /plots/laguerre.py
        .. image :: /plots/laguerre.png
        
        **Examples**
        
        Evaluation for arbitrary arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> laguerre(5, 0, 0.25)
            0.03726399739583333333333333
            >>> laguerre(1+j, 0.5, 2+3j)
            (4.474921610704496808379097 - 11.02058050372068958069241j)
            >>> laguerre(2, 0, 10000)
            49980001.0
            >>> laguerre(2.5, 0, 10000)
            -9.327764910194842158583189e+4328
        
        The first few Laguerre polynomials, normalized to have integer
        coefficients::
        
            >>> for n in range(7):
            ...     chop(taylor(lambda z: fac(n)*laguerre(n, 0, z), 0, n))
            ...
            [1.0]
            [1.0, -1.0]
            [2.0, -4.0, 1.0]
            [6.0, -18.0, 9.0, -1.0]
            [24.0, -96.0, 72.0, -16.0, 1.0]
            [120.0, -600.0, 600.0, -200.0, 25.0, -1.0]
            [720.0, -4320.0, 5400.0, -2400.0, 450.0, -36.0, 1.0]
        
        Verifying orthogonality::
        
            >>> Lm = lambda t: laguerre(m,a,t)
            >>> Ln = lambda t: laguerre(n,a,t)
            >>> a, n, m = 2.5, 2, 3
            >>> chop(quad(lambda t: exp(-t)*t**a*Lm(t)*Ln(t), [0,inf]))
            0.0
        
        
        """
    @staticmethod
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
    @staticmethod
    def ldexp(ctx, x, n):
        """
        
        Computes `x 2^n` efficiently. No rounding is performed.
        The argument `x` must be a real floating-point number (or
        possible to convert into one) and `n` must be a Python ``int``.
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> ldexp(1, 10)
            mpf('1024.0')
            >>> ldexp(1, -3)
            mpf('0.125')
        
        """
    @staticmethod
    def legendre(ctx, *args, **kwargs):
        """
        
        ``legendre(n, x)`` evaluates the Legendre polynomial `P_n(x)`.
        The Legendre polynomials are given by the formula
        
        .. math ::
        
            P_n(x) = \\frac{1}{2^n n!} \\frac{d^n}{dx^n} (x^2 -1)^n.
        
        Alternatively, they can be computed recursively using
        
        .. math ::
        
            P_0(x) = 1
        
            P_1(x) = x
        
            (n+1) P_{n+1}(x) = (2n+1) x P_n(x) - n P_{n-1}(x).
        
        A third definition is in terms of the hypergeometric function
        `\\,_2F_1`, whereby they can be generalized to arbitrary `n`:
        
        .. math ::
        
            P_n(x) = \\,_2F_1\\left(-n, n+1, 1, \\frac{1-x}{2}\\right)
        
        **Plots**
        
        .. literalinclude :: /plots/legendre.py
        .. image :: /plots/legendre.png
        
        **Basic evaluation**
        
        The Legendre polynomials assume fixed values at the points
        `x = -1` and `x = 1`::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> nprint([legendre(n, 1) for n in range(6)])
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            >>> nprint([legendre(n, -1) for n in range(6)])
            [1.0, -1.0, 1.0, -1.0, 1.0, -1.0]
        
        The coefficients of Legendre polynomials can be recovered
        using degree-`n` Taylor expansion::
        
            >>> for n in range(5):
            ...     nprint(chop(taylor(lambda x: legendre(n, x), 0, n)))
            ...
            [1.0]
            [0.0, 1.0]
            [-0.5, 0.0, 1.5]
            [0.0, -1.5, 0.0, 2.5]
            [0.375, 0.0, -3.75, 0.0, 4.375]
        
        The roots of Legendre polynomials are located symmetrically
        on the interval `[-1, 1]`::
        
            >>> for n in range(5):
            ...     nprint(polyroots(taylor(lambda x: legendre(n, x), 0, n)[::-1]))
            ...
            []
            [0.0]
            [-0.57735, 0.57735]
            [-0.774597, 0.0, 0.774597]
            [-0.861136, -0.339981, 0.339981, 0.861136]
        
        An example of an evaluation for arbitrary `n`::
        
            >>> legendre(0.75, 2+4j)
            (1.94952805264875 + 2.1071073099422j)
        
        **Orthogonality**
        
        The Legendre polynomials are orthogonal on `[-1, 1]` with respect
        to the trivial weight `w(x) = 1`. That is, `P_m(x) P_n(x)`
        integrates to zero if `m \\ne n` and to `2/(2n+1)` if `m = n`::
        
            >>> m, n = 3, 4
            >>> quad(lambda x: legendre(m,x)*legendre(n,x), [-1, 1])
            0.0
            >>> m, n = 4, 4
            >>> quad(lambda x: legendre(m,x)*legendre(n,x), [-1, 1])
            0.222222222222222
        
        **Differential equation**
        
        The Legendre polynomials satisfy the differential equation
        
        .. math ::
        
            ((1-x^2) y')' + n(n+1) y' = 0.
        
        We can verify this numerically::
        
            >>> n = 3.6
            >>> x = 0.73
            >>> P = legendre
            >>> A = diff(lambda t: (1-t**2)*diff(lambda u: P(n,u), t), x)
            >>> B = n*(n+1)*P(n,x)
            >>> nprint(A+B,1)
            9.0e-16
        
        """
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def lerchphi(ctx, *args, **kwargs):
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
    @staticmethod
    def li(ctx, *args, **kwargs):
        """
        
        Computes the logarithmic integral or li-function
        `\\mathrm{li}(x)`, defined by
        
        .. math ::
        
            \\mathrm{li}(x) = \\int_0^x \\frac{1}{\\log t} \\, dt
        
        The logarithmic integral has a singularity at `x = 1`.
        
        Alternatively, ``li(x, offset=True)`` computes the offset
        logarithmic integral (used in number theory)
        
        .. math ::
        
            \\mathrm{Li}(x) = \\int_2^x \\frac{1}{\\log t} \\, dt.
        
        These two functions are related via the simple identity
        `\\mathrm{Li}(x) = \\mathrm{li}(x) - \\mathrm{li}(2)`.
        
        The logarithmic integral should also not be confused with
        the polylogarithm (also denoted by Li), which is implemented
        as :func:`~mpmath.polylog`.
        
        **Examples**
        
        Some basic values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 30; mp.pretty = True
            >>> li(0)
            0.0
            >>> li(1)
            -inf
            >>> li(1)
            -inf
            >>> li(2)
            1.04516378011749278484458888919
            >>> findroot(li, 2)
            1.45136923488338105028396848589
            >>> li(inf)
            +inf
            >>> li(2, offset=True)
            0.0
            >>> li(1, offset=True)
            -inf
            >>> li(0, offset=True)
            -1.04516378011749278484458888919
            >>> li(10, offset=True)
            5.12043572466980515267839286347
        
        The logarithmic integral can be evaluated for arbitrary
        complex arguments::
        
            >>> mp.dps = 20
            >>> li(3+4j)
            (3.1343755504645775265 + 2.6769247817778742392j)
        
        The logarithmic integral is related to the exponential integral::
        
            >>> ei(log(3))
            2.1635885946671919729
            >>> li(3)
            2.1635885946671919729
        
        The logarithmic integral grows like `O(x/\\log(x))`::
        
            >>> mp.dps = 15
            >>> x = 10**100
            >>> x/log(x)
            4.34294481903252e+97
            >>> li(x)
            4.3619719871407e+97
        
        The prime number theorem states that the number of primes less
        than `x` is asymptotic to `\\mathrm{Li}(x)` (equivalently
        `\\mathrm{li}(x)`). For example, it is known that there are
        exactly 1,925,320,391,606,803,968,923 prime numbers less than
        `10^{23}` [1]. The logarithmic integral provides a very
        accurate estimate::
        
            >>> li(10**23, offset=True)
            1.92532039161405e+21
        
        A definite integral is::
        
            >>> quad(li, [0, 1])
            -0.693147180559945
            >>> -ln(2)
            -0.693147180559945
        
        **References**
        
        1. http://mathworld.wolfram.com/PrimeCountingFunction.html
        
        2. http://mathworld.wolfram.com/LogarithmicIntegral.html
        
        """
    @staticmethod
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
    @staticmethod
    def log10(ctx, x):
        """
        
        Computes the base-10 logarithm of `x`, `\\log_{10}(x)`. ``log10(x)``
        is equivalent to ``log(x, 10)``.
        """
    @staticmethod
    def log1p(ctx, *args, **kwargs):
        """
        
        Computes `\\log(1+x)`, accurately for small `x`.
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> log(1+1e-10); print(mp.log1p(1e-10))
            1.00000008269037e-10
            9.9999999995e-11
            >>> mp.log1p(1e-100j)
            (5.0e-201 + 1.0e-100j)
            >>> mp.log1p(0)
            0.0
        
        """
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def meijerg(ctx, a_s, b_s, z, r = 1, series = None, **kwargs):
        """
        
        Evaluates the Meijer G-function, defined as
        
        .. math ::
        
            G^{m,n}_{p,q} \\left( \\left. \\begin{matrix}
                 a_1, \\dots, a_n ; a_{n+1} \\dots a_p \\\\
                 b_1, \\dots, b_m ; b_{m+1} \\dots b_q
            \\end{matrix}\\; \\right| \\; z ; r \\right) =
            \\frac{1}{2 \\pi i} \\int_L
            \\frac{\\prod_{j=1}^m \\Gamma(b_j+s) \\prod_{j=1}^n\\Gamma(1-a_j-s)}
                 {\\prod_{j=n+1}^{p}\\Gamma(a_j+s) \\prod_{j=m+1}^q \\Gamma(1-b_j-s)}
                 z^{-s/r} ds
        
        for an appropriate choice of the contour `L` (see references).
        
        There are `p` elements `a_j`.
        The argument *a_s* should be a pair of lists, the first containing the
        `n` elements `a_1, \\ldots, a_n` and the second containing
        the `p-n` elements `a_{n+1}, \\ldots a_p`.
        
        There are `q` elements `b_j`.
        The argument *b_s* should be a pair of lists, the first containing the
        `m` elements `b_1, \\ldots, b_m` and the second containing
        the `q-m` elements `b_{m+1}, \\ldots b_q`.
        
        The implicit tuple `(m, n, p, q)` constitutes the order or degree of the
        Meijer G-function, and is determined by the lengths of the coefficient
        vectors. Confusingly, the indices in this tuple appear in a different order
        from the coefficients, but this notation is standard. The many examples
        given below should hopefully clear up any potential confusion.
        
        **Algorithm**
        
        The Meijer G-function is evaluated as a combination of hypergeometric series.
        There are two versions of the function, which can be selected with
        the optional *series* argument.
        
        *series=1* uses a sum of `m` `\\,_pF_{q-1}` functions of `z`
        
        *series=2* uses a sum of `n` `\\,_qF_{p-1}` functions of `1/z`
        
        The default series is chosen based on the degree and `|z|` in order
        to be consistent with Mathematica's. This definition of the Meijer G-function
        has a discontinuity at `|z| = 1` for some orders, which can
        be avoided by explicitly specifying a series.
        
        Keyword arguments are forwarded to :func:`~mpmath.hypercomb`.
        
        **Examples**
        
        Many standard functions are special cases of the Meijer G-function
        (possibly rescaled and/or with branch cut corrections). We define
        some test parameters::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> a = mpf(0.75)
            >>> b = mpf(1.5)
            >>> z = mpf(2.25)
        
        The exponential function:
        `e^z = G^{1,0}_{0,1} \\left( \\left. \\begin{matrix} - \\\\ 0 \\end{matrix} \\;
        \\right| \\; -z \\right)`
        
            >>> meijerg([[],[]], [[0],[]], -z)
            9.487735836358525720550369
            >>> exp(z)
            9.487735836358525720550369
        
        The natural logarithm:
        `\\log(1+z) = G^{1,2}_{2,2} \\left( \\left. \\begin{matrix} 1, 1 \\\\ 1, 0
        \\end{matrix} \\; \\right| \\; -z \\right)`
        
            >>> meijerg([[1,1],[]], [[1],[0]], z)
            1.178654996341646117219023
            >>> log(1+z)
            1.178654996341646117219023
        
        A rational function:
        `\\frac{z}{z+1} = G^{1,2}_{2,2} \\left( \\left. \\begin{matrix} 1, 1 \\\\ 1, 1
        \\end{matrix} \\; \\right| \\; z \\right)`
        
            >>> meijerg([[1,1],[]], [[1],[1]], z)
            0.6923076923076923076923077
            >>> z/(z+1)
            0.6923076923076923076923077
        
        The sine and cosine functions:
        
        `\\frac{1}{\\sqrt \\pi} \\sin(2 \\sqrt z) = G^{1,0}_{0,2} \\left( \\left. \\begin{matrix}
        - \\\\ \\frac{1}{2}, 0 \\end{matrix} \\; \\right| \\; z \\right)`
        
        `\\frac{1}{\\sqrt \\pi} \\cos(2 \\sqrt z) = G^{1,0}_{0,2} \\left( \\left. \\begin{matrix}
        - \\\\ 0, \\frac{1}{2} \\end{matrix} \\; \\right| \\; z \\right)`
        
            >>> meijerg([[],[]], [[0.5],[0]], (z/2)**2)
            0.4389807929218676682296453
            >>> sin(z)/sqrt(pi)
            0.4389807929218676682296453
            >>> meijerg([[],[]], [[0],[0.5]], (z/2)**2)
            -0.3544090145996275423331762
            >>> cos(z)/sqrt(pi)
            -0.3544090145996275423331762
        
        Bessel functions:
        
        `J_a(2 \\sqrt z) = G^{1,0}_{0,2} \\left( \\left.
        \\begin{matrix} - \\\\ \\frac{a}{2}, -\\frac{a}{2}
        \\end{matrix} \\; \\right| \\; z \\right)`
        
        `Y_a(2 \\sqrt z) = G^{2,0}_{1,3} \\left( \\left.
        \\begin{matrix} \\frac{-a-1}{2} \\\\ \\frac{a}{2}, -\\frac{a}{2}, \\frac{-a-1}{2}
        \\end{matrix} \\; \\right| \\; z \\right)`
        
        `(-z)^{a/2} z^{-a/2} I_a(2 \\sqrt z) = G^{1,0}_{0,2} \\left( \\left.
        \\begin{matrix} - \\\\ \\frac{a}{2}, -\\frac{a}{2}
        \\end{matrix} \\; \\right| \\; -z \\right)`
        
        `2 K_a(2 \\sqrt z) = G^{2,0}_{0,2} \\left( \\left.
        \\begin{matrix} - \\\\ \\frac{a}{2}, -\\frac{a}{2}
        \\end{matrix} \\; \\right| \\; z \\right)`
        
        As the example with the Bessel *I* function shows, a branch
        factor is required for some arguments when inverting the square root.
        
            >>> meijerg([[],[]], [[a/2],[-a/2]], (z/2)**2)
            0.5059425789597154858527264
            >>> besselj(a,z)
            0.5059425789597154858527264
            >>> meijerg([[],[(-a-1)/2]], [[a/2,-a/2],[(-a-1)/2]], (z/2)**2)
            0.1853868950066556941442559
            >>> bessely(a, z)
            0.1853868950066556941442559
            >>> meijerg([[],[]], [[a/2],[-a/2]], -(z/2)**2)
            (0.8685913322427653875717476 + 2.096964974460199200551738j)
            >>> (-z)**(a/2) / z**(a/2) * besseli(a, z)
            (0.8685913322427653875717476 + 2.096964974460199200551738j)
            >>> 0.5*meijerg([[],[]], [[a/2,-a/2],[]], (z/2)**2)
            0.09334163695597828403796071
            >>> besselk(a,z)
            0.09334163695597828403796071
        
        Error functions:
        
        `\\sqrt{\\pi} z^{2(a-1)} \\mathrm{erfc}(z) = G^{2,0}_{1,2} \\left( \\left.
        \\begin{matrix} a \\\\ a-1, a-\\frac{1}{2}
        \\end{matrix} \\; \\right| \\; z, \\frac{1}{2} \\right)`
        
            >>> meijerg([[],[a]], [[a-1,a-0.5],[]], z, 0.5)
            0.00172839843123091957468712
            >>> sqrt(pi) * z**(2*a-2) * erfc(z)
            0.00172839843123091957468712
        
        A Meijer G-function of higher degree, (1,1,2,3):
        
            >>> meijerg([[a],[b]], [[a],[b,a-1]], z)
            1.55984467443050210115617
            >>> sin((b-a)*pi)/pi*(exp(z)-1)*z**(a-1)
            1.55984467443050210115617
        
        A Meijer G-function of still higher degree, (4,1,2,4), that can
        be expanded as a messy combination of exponential integrals:
        
            >>> meijerg([[a],[2*b-a]], [[b,a,b-0.5,-1-a+2*b],[]], z)
            0.3323667133658557271898061
            >>> chop(4**(a-b+1)*sqrt(pi)*gamma(2*b-2*a)*z**a*\\
            ...     expint(2*b-2*a, -2*sqrt(-z))*expint(2*b-2*a, 2*sqrt(-z)))
            0.3323667133658557271898061
        
        In the following case, different series give different values::
        
            >>> chop(meijerg([[1],[0.25]],[[3],[0.5]],-2))
            -0.06417628097442437076207337
            >>> meijerg([[1],[0.25]],[[3],[0.5]],-2,series=1)
            0.1428699426155117511873047
            >>> chop(meijerg([[1],[0.25]],[[3],[0.5]],-2,series=2))
            -0.06417628097442437076207337
        
        **References**
        
        1. http://en.wikipedia.org/wiki/Meijer_G-function
        
        2. http://mathworld.wolfram.com/MeijerG-Function.html
        
        3. http://functions.wolfram.com/HypergeometricFunctions/MeijerG/
        
        4. http://functions.wolfram.com/HypergeometricFunctions/MeijerG1/
        
        """
    @staticmethod
    def mfrom(ctx, *args, **kwargs):
        """
        
        Returns the elliptic parameter `m`, given any of
        `q, m, k, \\tau, \\bar{q}`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> mfrom(m=0.25)
            0.25
            >>> mfrom(q=qfrom(m=0.25))
            0.25
            >>> mfrom(k=kfrom(m=0.25))
            0.25
            >>> mfrom(tau=taufrom(m=0.25))
            (0.25 + 0.0j)
            >>> mfrom(qbar=qbarfrom(m=0.25))
            0.25
        
        As `q \\to 1` and `q \\to -1`, `m` rapidly approaches
        `1` and `-\\infty` respectively::
        
            >>> mfrom(q=0.75)
            0.9999999999999798332943533
            >>> mfrom(q=-0.75)
            -49586681013729.32611558353
            >>> mfrom(q=1)
            1.0
            >>> mfrom(q=-1)
            -inf
        
        The inverse nome as a function of `q` has an integer
        Taylor series expansion::
        
            >>> taylor(lambda q: mfrom(q), 0, 7)
            [0.0, 16.0, -128.0, 704.0, -3072.0, 11488.0, -38400.0, 117632.0]
        
        """
    @staticmethod
    def mpmathify(ctx, *args, **kwargs):
        ...
    @staticmethod
    def ncdf(ctx, *args, **kwargs):
        """
        
        ``ncdf(x, mu=0, sigma=1)`` evaluates the cumulative distribution
        function of a normal distribution with mean value `\\mu`
        and variance `\\sigma^2`.
        
        See also :func:`~mpmath.npdf`, which gives the probability density.
        
        Elementary properties include::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> ncdf(pi, mu=pi)
            0.5
            >>> ncdf(-inf)
            0.0
            >>> ncdf(+inf)
            1.0
        
        The cumulative distribution is the integral of the density
        function having identical mu and sigma::
        
            >>> mp.dps = 15
            >>> diff(ncdf, 2)
            0.053990966513188
            >>> npdf(2)
            0.053990966513188
            >>> diff(lambda x: ncdf(x, 1, 0.5), 0)
            0.107981933026376
            >>> npdf(0, 1, 0.5)
            0.107981933026376
        """
    @staticmethod
    def nint_distance(ctx, x):
        """
        
        Return `(n,d)` where `n` is the nearest integer to `x` and `d` is
        an estimate of `\\log_2(|x-n|)`. If `d < 0`, `-d` gives the precision
        (measured in bits) lost to cancellation when computing `x-n`.
        
            >>> from mpmath import *
            >>> n, d = nint_distance(5)
            >>> print(n); print(d)
            5
            -inf
            >>> n, d = nint_distance(mpf(5))
            >>> print(n); print(d)
            5
            -inf
            >>> n, d = nint_distance(mpf(5.00000001))
            >>> print(n); print(d)
            5
            -26
            >>> n, d = nint_distance(mpf(4.99999999))
            >>> print(n); print(d)
            5
            -26
            >>> n, d = nint_distance(mpc(5,10))
            >>> print(n); print(d)
            5
            4
            >>> n, d = nint_distance(mpc(5,0.000001))
            >>> print(n); print(d)
            5
            -19
        
        """
    @staticmethod
    def npdf(ctx, *args, **kwargs):
        """
        
        ``npdf(x, mu=0, sigma=1)`` evaluates the probability density
        function of a normal distribution with mean value `\\mu`
        and variance `\\sigma^2`.
        
        Elementary properties of the probability distribution can
        be verified using numerical integration::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> quad(npdf, [-inf, inf])
            1.0
            >>> quad(lambda x: npdf(x, 3), [3, inf])
            0.5
            >>> quad(lambda x: npdf(x, 3, 2), [3, inf])
            0.5
        
        See also :func:`~mpmath.ncdf`, which gives the cumulative
        distribution.
        """
    @staticmethod
    def nstr(ctx, x, n = 6, **kwargs):
        """
        
        Convert an ``mpf`` or ``mpc`` to a decimal string literal with *n*
        significant digits. The small default value for *n* is chosen to
        make this function useful for printing collections of numbers
        (lists, matrices, etc).
        
        If *x* is a list or tuple, :func:`~mpmath.nstr` is applied recursively
        to each element. For unrecognized classes, :func:`~mpmath.nstr`
        simply returns ``str(x)``.
        
        The companion function :func:`~mpmath.nprint` prints the result
        instead of returning it.
        
        The keyword arguments *strip_zeros*, *min_fixed*, *max_fixed*
        and *show_zero_exponent* are forwarded to :func:`~mpmath.libmp.to_str`.
        
        The number will be printed in fixed-point format if the position
        of the leading digit is strictly between min_fixed
        (default = min(-dps/3,-5)) and max_fixed (default = dps).
        
        To force fixed-point format always, set min_fixed = -inf,
        max_fixed = +inf. To force floating-point format, set
        min_fixed >= max_fixed.
        
            >>> from mpmath import *
            >>> nstr([+pi, ldexp(1,-500)])
            '[3.14159, 3.05494e-151]'
            >>> nprint([+pi, ldexp(1,-500)])
            [3.14159, 3.05494e-151]
            >>> nstr(mpf("5e-10"), 5)
            '5.0e-10'
            >>> nstr(mpf("5e-10"), 5, strip_zeros=False)
            '5.0000e-10'
            >>> nstr(mpf("5e-10"), 5, strip_zeros=False, min_fixed=-11)
            '0.00000000050000'
            >>> nstr(mpf(0), 5, show_zero_exponent=True)
            '0.0e+0'
        
        """
    @staticmethod
    def nzeros(ctx, t):
        """
        
        Computes the number of zeros of the Riemann zeta function in
        `(0,1) \\times (0,t]`, usually denoted by `N(t)`.
        
        **Examples**
        
        The first zero has imaginary part between 14 and 15::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> nzeros(14)
            0
            >>> nzeros(15)
            1
            >>> zetazero(1)
            (0.5 + 14.1347251417347j)
        
        Some closely spaced zeros::
        
            >>> nzeros(10**7)
            21136125
            >>> zetazero(21136125)
            (0.5 + 9999999.32718175j)
            >>> zetazero(21136126)
            (0.5 + 10000000.2400236j)
            >>> nzeros(545439823.215)
            1500000001
            >>> zetazero(1500000001)
            (0.5 + 545439823.201985j)
            >>> zetazero(1500000002)
            (0.5 + 545439823.325697j)
        
        This confirms the data given by J. van de Lune,
        H. J. J. te Riele and D. T. Winter in 1986.
        """
    @staticmethod
    def oldzetazero(ctx, n, url = 'http://www.dtc.umn.edu/~odlyzko/zeta_tables/zeros1'):
        ...
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def polyexp(ctx, *args, **kwargs):
        """
        
        Evaluates the polyexponential function, defined for arbitrary
        complex `s`, `z` by the series
        
        .. math ::
        
            E_s(z) = \\sum_{k=1}^{\\infty} \\frac{k^s}{k!} z^k.
        
        `E_s(z)` is constructed from the exponential function analogously
        to how the polylogarithm is constructed from the ordinary
        logarithm; as a function of `s` (with `z` fixed), `E_s` is an L-series
        It is an entire function of both `s` and `z`.
        
        The polyexponential function provides a generalization of the
        Bell polynomials `B_n(x)` (see :func:`~mpmath.bell`) to noninteger orders `n`.
        In terms of the Bell polynomials,
        
        .. math ::
        
            E_s(z) = e^z B_s(z) - \\mathrm{sinc}(\\pi s).
        
        Note that `B_n(x)` and `e^{-x} E_n(x)` are identical if `n`
        is a nonzero integer, but not otherwise. In particular, they differ
        at `n = 0`.
        
        **Examples**
        
        Evaluating a series::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> nsum(lambda k: sqrt(k)/fac(k), [1,inf])
            2.101755547733791780315904
            >>> polyexp(0.5,1)
            2.101755547733791780315904
        
        Evaluation for arbitrary arguments::
        
            >>> polyexp(-3-4j, 2.5+2j)
            (2.351660261190434618268706 + 1.202966666673054671364215j)
        
        Evaluation is accurate for tiny function values::
        
            >>> polyexp(4, -100)
            3.499471750566824369520223e-36
        
        If `n` is a nonpositive integer, `E_n` reduces to a special
        instance of the hypergeometric function `\\,_pF_q`::
        
            >>> n = 3
            >>> x = pi
            >>> polyexp(-n,x)
            4.042192318847986561771779
            >>> x*hyper([1]*(n+1), [2]*(n+1), x)
            4.042192318847986561771779
        
        """
    @staticmethod
    def polylog(ctx, *args, **kwargs):
        """
        
        Computes the polylogarithm, defined by the sum
        
        .. math ::
        
            \\mathrm{Li}_s(z) = \\sum_{k=1}^{\\infty} \\frac{z^k}{k^s}.
        
        This series is convergent only for `|z| < 1`, so elsewhere
        the analytic continuation is implied.
        
        The polylogarithm should not be confused with the logarithmic
        integral (also denoted by Li or li), which is implemented
        as :func:`~mpmath.li`.
        
        **Examples**
        
        The polylogarithm satisfies a huge number of functional identities.
        A sample of polylogarithm evaluations is shown below::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> polylog(1,0.5), log(2)
            (0.693147180559945, 0.693147180559945)
            >>> polylog(2,0.5), (pi**2-6*log(2)**2)/12
            (0.582240526465012, 0.582240526465012)
            >>> polylog(2,-phi), -log(phi)**2-pi**2/10
            (-1.21852526068613, -1.21852526068613)
            >>> polylog(3,0.5), 7*zeta(3)/8-pi**2*log(2)/12+log(2)**3/6
            (0.53721319360804, 0.53721319360804)
        
        :func:`~mpmath.polylog` can evaluate the analytic continuation of the
        polylogarithm when `s` is an integer::
        
            >>> polylog(2, 10)
            (0.536301287357863 - 7.23378441241546j)
            >>> polylog(2, -10)
            -4.1982778868581
            >>> polylog(2, 10j)
            (-3.05968879432873 + 3.71678149306807j)
            >>> polylog(-2, 10)
            -0.150891632373114
            >>> polylog(-2, -10)
            0.067618332081142
            >>> polylog(-2, 10j)
            (0.0384353698579347 + 0.0912451798066779j)
        
        Some more examples, with arguments on the unit circle (note that
        the series definition cannot be used for computation here)::
        
            >>> polylog(2,j)
            (-0.205616758356028 + 0.915965594177219j)
            >>> j*catalan-pi**2/48
            (-0.205616758356028 + 0.915965594177219j)
            >>> polylog(3,exp(2*pi*j/3))
            (-0.534247512515375 + 0.765587078525922j)
            >>> -4*zeta(3)/9 + 2*j*pi**3/81
            (-0.534247512515375 + 0.765587078525921j)
        
        Polylogarithms of different order are related by integration
        and differentiation::
        
            >>> s, z = 3, 0.5
            >>> polylog(s+1, z)
            0.517479061673899
            >>> quad(lambda t: polylog(s,t)/t, [0, z])
            0.517479061673899
            >>> z*diff(lambda t: polylog(s+2,t), z)
            0.517479061673899
        
        Taylor series expansions around `z = 0` are::
        
            >>> for n in range(-3, 4):
            ...     nprint(taylor(lambda x: polylog(n,x), 0, 5))
            ...
            [0.0, 1.0, 8.0, 27.0, 64.0, 125.0]
            [0.0, 1.0, 4.0, 9.0, 16.0, 25.0]
            [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
            [0.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            [0.0, 1.0, 0.5, 0.333333, 0.25, 0.2]
            [0.0, 1.0, 0.25, 0.111111, 0.0625, 0.04]
            [0.0, 1.0, 0.125, 0.037037, 0.015625, 0.008]
        
        The series defining the polylogarithm is simultaneously
        a Taylor series and an L-series. For certain values of `z`, the
        polylogarithm reduces to a pure zeta function::
        
            >>> polylog(pi, 1), zeta(pi)
            (1.17624173838258, 1.17624173838258)
            >>> polylog(pi, -1), -altzeta(pi)
            (-0.909670702980385, -0.909670702980385)
        
        Evaluation for arbitrary, nonintegral `s` is supported
        for `z` within the unit circle:
        
            >>> polylog(3+4j, 0.25)
            (0.24258605789446 - 0.00222938275488344j)
            >>> nsum(lambda k: 0.25**k / k**(3+4j), [1,inf])
            (0.24258605789446 - 0.00222938275488344j)
        
        It is also supported outside of the unit circle::
        
            >>> polylog(1+j, 20+40j)
            (-7.1421172179728 - 3.92726697721369j)
            >>> polylog(1+j, 200+400j)
            (-5.41934747194626 - 9.94037752563927j)
        
        **References**
        
        1. Richard Crandall, "Note on fast polylogarithm computation"
           http://www.reed.edu/physics/faculty/crandall/papers/Polylog.pdf
        2. http://en.wikipedia.org/wiki/Polylogarithm
        3. http://mathworld.wolfram.com/Polylogarithm.html
        
        """
    @staticmethod
    def powm1(ctx, *args, **kwargs):
        """
        
        Computes `x^y - 1`, accurately when `x^y` is very close to 1.
        
        This avoids potentially catastrophic cancellation::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> power(0.99999995, 1e-10) - 1
            0.0
            >>> powm1(0.99999995, 1e-10)
            -5.00000012791934e-18
        
        Powers exactly equal to 1, and only those powers, yield 0 exactly::
        
            >>> powm1(-j, 4)
            (0.0 + 0.0j)
            >>> powm1(3, 0)
            0.0
            >>> powm1(fadd(-1, 1e-100, exact=True), 4)
            -4.0e-100
        
        Evaluation works for extremely tiny `y`::
        
            >>> powm1(2, '1e-100000')
            6.93147180559945e-100001
            >>> powm1(j, '1e-1000')
            (-1.23370055013617e-2000 + 1.5707963267949e-1000j)
        
        """
    @staticmethod
    def primepi2(ctx, *args, **kwargs):
        """
        
        Returns an interval (as an ``mpi`` instance) providing bounds
        for the value of the prime counting function `\\pi(x)`. For small
        `x`, :func:`~mpmath.primepi2` returns an exact interval based on
        the output of :func:`~mpmath.primepi`. For `x > 2656`, a loose interval
        based on Schoenfeld's inequality
        
        .. math ::
        
            |\\pi(x) - \\mathrm{li}(x)| < \\frac{\\sqrt x \\log x}{8 \\pi}
        
        is returned. This estimate is rigorous assuming the truth of
        the Riemann hypothesis, and can be computed very quickly.
        
        **Examples**
        
        Exact values of the prime counting function for small `x`::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> iv.dps = 15; iv.pretty = True
            >>> primepi2(10)
            [4.0, 4.0]
            >>> primepi2(100)
            [25.0, 25.0]
            >>> primepi2(1000)
            [168.0, 168.0]
        
        Loose intervals are generated for moderately large `x`:
        
            >>> primepi2(10000), primepi(10000)
            ([1209.0, 1283.0], 1229)
            >>> primepi2(50000), primepi(50000)
            ([5070.0, 5263.0], 5133)
        
        As `x` increases, the absolute error gets worse while the relative
        error improves. The exact value of `\\pi(10^{23})` is
        1925320391606803968923, and :func:`~mpmath.primepi2` gives 9 significant
        digits::
        
            >>> p = primepi2(10**23)
            >>> p
            [1.9253203909477020467e+21, 1.925320392280406229e+21]
            >>> mpf(p.delta) / mpf(p.a)
            6.9219865355293e-10
        
        A more precise, nonrigorous estimate for `\\pi(x)` can be
        obtained using the Riemann R function (:func:`~mpmath.riemannr`).
        For large enough `x`, the value returned by :func:`~mpmath.primepi2`
        essentially amounts to a small perturbation of the value returned by
        :func:`~mpmath.riemannr`::
        
            >>> primepi2(10**100)
            [4.3619719871407024816e+97, 4.3619719871407032404e+97]
            >>> riemannr(10**100)
            4.3619719871407e+97
        """
    @staticmethod
    def primezeta(ctx, *args, **kwargs):
        """
        
        Computes the prime zeta function, which is defined
        in analogy with the Riemann zeta function (:func:`~mpmath.zeta`)
        as
        
        .. math ::
        
            P(s) = \\sum_p \\frac{1}{p^s}
        
        where the sum is taken over all prime numbers `p`. Although
        this sum only converges for `\\mathrm{Re}(s) > 1`, the
        function is defined by analytic continuation in the
        half-plane `\\mathrm{Re}(s) > 0`.
        
        **Examples**
        
        Arbitrary-precision evaluation for real and complex arguments is
        supported::
        
            >>> from mpmath import *
            >>> mp.dps = 30; mp.pretty = True
            >>> primezeta(2)
            0.452247420041065498506543364832
            >>> primezeta(pi)
            0.15483752698840284272036497397
            >>> mp.dps = 50
            >>> primezeta(3)
            0.17476263929944353642311331466570670097541212192615
            >>> mp.dps = 20
            >>> primezeta(3+4j)
            (-0.12085382601645763295 - 0.013370403397787023602j)
        
        The prime zeta function has a logarithmic pole at `s = 1`,
        with residue equal to the difference of the Mertens and
        Euler constants::
        
            >>> primezeta(1)
            +inf
            >>> extradps(25)(lambda x: primezeta(1+x)+log(x))(+eps)
            -0.31571845205389007685
            >>> mertens-euler
            -0.31571845205389007685
        
        The analytic continuation to `0 < \\mathrm{Re}(s) \\le 1`
        is implemented. In this strip the function exhibits
        very complex behavior; on the unit interval, it has poles at
        `1/n` for every squarefree integer `n`::
        
            >>> primezeta(0.5)         # Pole at s = 1/2
            (-inf + 3.1415926535897932385j)
            >>> primezeta(0.25)
            (-1.0416106801757269036 + 0.52359877559829887308j)
            >>> primezeta(0.5+10j)
            (0.54892423556409790529 + 0.45626803423487934264j)
        
        Although evaluation works in principle for any `\\mathrm{Re}(s) > 0`,
        it should be noted that the evaluation time increases exponentially
        as `s` approaches the imaginary axis.
        
        For large `\\mathrm{Re}(s)`, `P(s)` is asymptotic to `2^{-s}`::
        
            >>> primezeta(inf)
            0.0
            >>> primezeta(10), mpf(2)**-10
            (0.00099360357443698021786, 0.0009765625)
            >>> primezeta(1000)
            9.3326361850321887899e-302
            >>> primezeta(1000+1000j)
            (-3.8565440833654995949e-302 - 8.4985390447553234305e-302j)
        
        **References**
        
        Carl-Erik Froberg, "On the prime zeta function",
        BIT 8 (1968), pp. 187-202.
        
        """
    @staticmethod
    def psi(ctx, m, z):
        ...
    @staticmethod
    def qbarfrom(ctx, *args, **kwargs):
        """
        
        Returns the number-theoretic nome `\\bar q`, given any of
        `q, m, k, \\tau, \\bar{q}`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> qbarfrom(qbar=0.25)
            0.25
            >>> qbarfrom(q=qfrom(qbar=0.25))
            0.25
            >>> qbarfrom(m=extraprec(20)(mfrom)(qbar=0.25))  # ill-conditioned
            0.25
            >>> qbarfrom(k=extraprec(20)(kfrom)(qbar=0.25))  # ill-conditioned
            0.25
            >>> qbarfrom(tau=taufrom(qbar=0.25))
            (0.25 + 0.0j)
        
        """
    @staticmethod
    def qfac(ctx, *args, **kwargs):
        """
        
        Evaluates the q-factorial,
        
        .. math ::
        
            [n]_q! = (1+q)(1+q+q^2)\\cdots(1+q+\\cdots+q^{n-1})
        
        or more generally
        
        .. math ::
        
            [z]_q! = \\frac{(q;q)_z}{(1-q)^z}.
        
        **Examples**
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> qfac(0,0)
            1.0
            >>> qfac(4,3)
            2080.0
            >>> qfac(5,6)
            121226245.0
            >>> qfac(1+1j, 2+1j)
            (0.4370556551322672478613695 + 0.2609739839216039203708921j)
        
        """
    @staticmethod
    def qfrom(ctx, *args, **kwargs):
        """
        
        Returns the elliptic nome `q`, given any of `q, m, k, \\tau, \\bar{q}`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> qfrom(q=0.25)
            0.25
            >>> qfrom(m=mfrom(q=0.25))
            0.25
            >>> qfrom(k=kfrom(q=0.25))
            0.25
            >>> qfrom(tau=taufrom(q=0.25))
            (0.25 + 0.0j)
            >>> qfrom(qbar=qbarfrom(q=0.25))
            0.25
        
        """
    @staticmethod
    def qgamma(ctx, *args, **kwargs):
        """
        
        Evaluates the q-gamma function
        
        .. math ::
        
            \\Gamma_q(z) = \\frac{(q; q)_{\\infty}}{(q^z; q)_{\\infty}} (1-q)^{1-z}.
        
        
        **Examples**
        
        Evaluation for real and complex arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> qgamma(4,0.75)
            4.046875
            >>> qgamma(6,6)
            121226245.0
            >>> qgamma(3+4j, 0.5j)
            (0.1663082382255199834630088 + 0.01952474576025952984418217j)
        
        The q-gamma function satisfies a functional equation similar
        to that of the ordinary gamma function::
        
            >>> q = mpf(0.25)
            >>> z = mpf(2.5)
            >>> qgamma(z+1,q)
            1.428277424823760954685912
            >>> (1-q**z)/(1-q)*qgamma(z,q)
            1.428277424823760954685912
        
        """
    @staticmethod
    def qhyper(ctx, a_s, b_s, q, z, **kwargs):
        """
        
        Evaluates the basic hypergeometric series or hypergeometric q-series
        
        .. math ::
        
            \\,_r\\phi_s \\left[\\begin{matrix}
                a_1 & a_2 & \\ldots & a_r \\\\
                b_1 & b_2 & \\ldots & b_s
            \\end{matrix} ; q,z \\right] =
            \\sum_{n=0}^\\infty
            \\frac{(a_1;q)_n, \\ldots, (a_r;q)_n}
                 {(b_1;q)_n, \\ldots, (b_s;q)_n}
            \\left((-1)^n q^{n\\choose 2}\\right)^{1+s-r}
            \\frac{z^n}{(q;q)_n}
        
        where `(a;q)_n` denotes the q-Pochhammer symbol (see :func:`~mpmath.qp`).
        
        **Examples**
        
        Evaluation works for real and complex arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> qhyper([0.5], [2.25], 0.25, 4)
            -0.1975849091263356009534385
            >>> qhyper([0.5], [2.25], 0.25-0.25j, 4)
            (2.806330244925716649839237 + 3.568997623337943121769938j)
            >>> qhyper([1+j], [2,3+0.5j], 0.25, 3+4j)
            (9.112885171773400017270226 - 1.272756997166375050700388j)
        
        Comparing with a summation of the defining series, using
        :func:`~mpmath.nsum`::
        
            >>> b, q, z = 3, 0.25, 0.5
            >>> qhyper([], [b], q, z)
            0.6221136748254495583228324
            >>> nsum(lambda n: z**n / qp(q,q,n)/qp(b,q,n) * q**(n*(n-1)), [0,inf])
            0.6221136748254495583228324
        
        """
    @staticmethod
    def qp(ctx, a, q = None, n = None, **kwargs):
        """
        
        Evaluates the q-Pochhammer symbol (or q-rising factorial)
        
        .. math ::
        
            (a; q)_n = \\prod_{k=0}^{n-1} (1-a q^k)
        
        where `n = \\infty` is permitted if `|q| < 1`. Called with two arguments,
        ``qp(a,q)`` computes `(a;q)_{\\infty}`; with a single argument, ``qp(q)``
        computes `(q;q)_{\\infty}`. The special case
        
        .. math ::
        
            \\phi(q) = (q; q)_{\\infty} = \\prod_{k=1}^{\\infty} (1-q^k) =
                \\sum_{k=-\\infty}^{\\infty} (-1)^k q^{(3k^2-k)/2}
        
        is also known as the Euler function, or (up to a factor `q^{-1/24}`)
        the Dedekind eta function.
        
        **Examples**
        
        If `n` is a positive integer, the function amounts to a finite product::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> qp(2,3,5)
            -725305.0
            >>> fprod(1-2*3**k for k in range(5))
            -725305.0
            >>> qp(2,3,0)
            1.0
        
        Complex arguments are allowed::
        
            >>> qp(2-1j, 0.75j)
            (0.4628842231660149089976379 + 4.481821753552703090628793j)
        
        The regular Pochhammer symbol `(a)_n` is obtained in the
        following limit as `q \\to 1`::
        
            >>> a, n = 4, 7
            >>> limit(lambda q: qp(q**a,q,n) / (1-q)**n, 1)
            604800.0
            >>> rf(a,n)
            604800.0
        
        The Taylor series of the reciprocal Euler function gives
        the partition function `P(n)`, i.e. the number of ways of writing
        `n` as a sum of positive integers::
        
            >>> taylor(lambda q: 1/qp(q), 0, 10)
            [1.0, 1.0, 2.0, 3.0, 5.0, 7.0, 11.0, 15.0, 22.0, 30.0, 42.0]
        
        Special values include::
        
            >>> qp(0)
            1.0
            >>> findroot(diffun(qp), -0.4)   # location of maximum
            -0.4112484791779547734440257
            >>> qp(_)
            1.228348867038575112586878
        
        The q-Pochhammer symbol is related to the Jacobi theta functions.
        For example, the following identity holds::
        
            >>> q = mpf(0.5)    # arbitrary
            >>> qp(q)
            0.2887880950866024212788997
            >>> root(3,-2)*root(q,-24)*jtheta(2,pi/6,root(q,6))
            0.2887880950866024212788997
        
        """
    @staticmethod
    def radians(ctx, x):
        """
        
        Converts the degree angle `x` to radians::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> radians(60)
            1.0471975511966
        """
    @staticmethod
    def rand(ctx):
        """
        
        Returns an ``mpf`` with value chosen randomly from `[0, 1)`.
        The number of randomly generated bits in the mantissa is equal
        to the working precision.
        """
    @staticmethod
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
    @staticmethod
    def rect(ctx, *args, **kwargs):
        """
        
        Returns the complex number represented by polar
        coordinates `(r, \\phi)`::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> chop(rect(2, pi))
            -2.0
            >>> rect(sqrt(2), -pi/4)
            (1.0 - 1.0j)
        """
    @staticmethod
    def rf(ctx, x, n):
        """
        
        Computes the rising factorial or Pochhammer symbol,
        
        .. math ::
        
            x^{(n)} = x (x+1) \\cdots (x+n-1) = \\frac{\\Gamma(x+n)}{\\Gamma(x)}
        
        where the rightmost expression is valid for nonintegral `n`.
        
        **Examples**
        
        For integral `n`, the rising factorial is a polynomial::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> for n in range(5):
            ...     nprint(taylor(lambda x: rf(x,n), 0, n))
            ...
            [1.0]
            [0.0, 1.0]
            [0.0, 1.0, 1.0]
            [0.0, 2.0, 3.0, 1.0]
            [0.0, 6.0, 11.0, 6.0, 1.0]
        
        Evaluation is supported for arbitrary arguments::
        
            >>> rf(2+3j, 5.5)
            (-7202.03920483347 - 3777.58810701527j)
        """
    @staticmethod
    def riemannr(ctx, *args, **kwargs):
        """
        
        Evaluates the Riemann R function, a smooth approximation of the
        prime counting function `\\pi(x)` (see :func:`~mpmath.primepi`). The Riemann
        R function gives a fast numerical approximation useful e.g. to
        roughly estimate the number of primes in a given interval.
        
        The Riemann R function is computed using the rapidly convergent Gram
        series,
        
        .. math ::
        
            R(x) = 1 + \\sum_{k=1}^{\\infty}
                \\frac{\\log^k x}{k k! \\zeta(k+1)}.
        
        From the Gram series, one sees that the Riemann R function is a
        well-defined analytic function (except for a branch cut along
        the negative real half-axis); it can be evaluated for arbitrary
        real or complex arguments.
        
        The Riemann R function gives a very accurate approximation
        of the prime counting function. For example, it is wrong by at
        most 2 for `x < 1000`, and for `x = 10^9` differs from the exact
        value of `\\pi(x)` by 79, or less than two parts in a million.
        It is about 10 times more accurate than the logarithmic integral
        estimate (see :func:`~mpmath.li`), which however is even faster to evaluate.
        It is orders of magnitude more accurate than the extremely
        fast `x/\\log x` estimate.
        
        **Examples**
        
        For small arguments, the Riemann R function almost exactly
        gives the prime counting function if rounded to the nearest
        integer::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> primepi(50), riemannr(50)
            (15, 14.9757023241462)
            >>> max(abs(primepi(n)-int(round(riemannr(n)))) for n in range(100))
            1
            >>> max(abs(primepi(n)-int(round(riemannr(n)))) for n in range(300))
            2
        
        The Riemann R function can be evaluated for arguments far too large
        for exact determination of `\\pi(x)` to be computationally
        feasible with any presently known algorithm::
        
            >>> riemannr(10**30)
            1.46923988977204e+28
            >>> riemannr(10**100)
            4.3619719871407e+97
            >>> riemannr(10**1000)
            4.3448325764012e+996
        
        A comparison of the Riemann R function and logarithmic integral estimates
        for `\\pi(x)` using exact values of `\\pi(10^n)` up to `n = 9`.
        The fractional error is shown in parentheses::
        
            >>> exact = [4,25,168,1229,9592,78498,664579,5761455,50847534]
            >>> for n, p in enumerate(exact):
            ...     n += 1
            ...     r, l = riemannr(10**n), li(10**n)
            ...     rerr, lerr = nstr((r-p)/p,3), nstr((l-p)/p,3)
            ...     print("%i %i %s(%s) %s(%s)" % (n, p, r, rerr, l, lerr))
            ...
            1 4 4.56458314100509(0.141) 6.1655995047873(0.541)
            2 25 25.6616332669242(0.0265) 30.1261415840796(0.205)
            3 168 168.359446281167(0.00214) 177.609657990152(0.0572)
            4 1229 1226.93121834343(-0.00168) 1246.13721589939(0.0139)
            5 9592 9587.43173884197(-0.000476) 9629.8090010508(0.00394)
            6 78498 78527.3994291277(0.000375) 78627.5491594622(0.00165)
            7 664579 664667.447564748(0.000133) 664918.405048569(0.000511)
            8 5761455 5761551.86732017(1.68e-5) 5762209.37544803(0.000131)
            9 50847534 50847455.4277214(-1.55e-6) 50849234.9570018(3.35e-5)
        
        The derivative of the Riemann R function gives the approximate
        probability for a number of magnitude `x` to be prime::
        
            >>> diff(riemannr, 1000)
            0.141903028110784
            >>> mpf(primepi(1050) - primepi(950)) / 100
            0.15
        
        Evaluation is supported for arbitrary arguments and at arbitrary
        precision::
        
            >>> mp.dps = 30
            >>> riemannr(7.5)
            3.72934743264966261918857135136
            >>> riemannr(-4+2j)
            (-0.551002208155486427591793957644 + 2.16966398138119450043195899746j)
        
        """
    @staticmethod
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
    @staticmethod
    def rs_z(ctx, w, derivative = 0):
        ...
    @staticmethod
    def rs_zeta(ctx, s, derivative = 0, **kwargs):
        ...
    @staticmethod
    def sawtoothw(ctx, *args, **kwargs):
        """
        
        Computes the sawtooth wave function using the definition:
        
        .. math::
            x(t) = A\\operatorname{frac}\\left(\\frac{t}{T}\\right)
        
        where :math:`\\operatorname{frac}\\left(\\frac{t}{T}\\right) = \\frac{t}{T}-\\left\\lfloor{\\frac{t}{T}}\\right\\rfloor`,
        `P` is the period of the wave, and `A` is the amplitude.
        
        **Examples**
        
        Sawtooth wave with period = 2, amplitude = 1 ::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> sawtoothw(0,1,2)
            0.0
            >>> sawtoothw(0.5,1,2)
            0.25
            >>> sawtoothw(1,1,2)
            0.5
            >>> sawtoothw(1.5,1,2)
            0.75
            >>> sawtoothw(2,1,2)
            0.0
        """
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def sec(ctx, *args, **kwargs):
        """
        
        Computes the secant of `x`, `\\mathrm{sec}(x) = \\frac{1}{\\cos(x)}`.
        The secant function is singular at `x = (n+1/2)\\pi`, but
        ``sec(x)`` always returns a finite result since `(n+1/2)\\pi`
        cannot be represented exactly using floating-point arithmetic.
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> sec(pi/3)
            2.0
            >>> sec(10000001)
            -1.184723164360392819100265
            >>> sec(2+3j)
            (-0.04167496441114427004834991 + 0.0906111371962375965296612j)
            >>> sec(inf)
            nan
            >>> nprint(chop(taylor(sec, 0, 6)))
            [1.0, 0.0, 0.5, 0.0, 0.208333, 0.0, 0.0847222]
        
        Intervals are supported via :func:`mpmath.iv.sec`::
        
            >>> iv.dps = 25; iv.pretty = True
            >>> iv.sec([0,1])
            [1.0, 1.85081571768092561791175326276]
            >>> iv.sec([0,2])  # Interval includes a singularity
            [-inf, +inf]
        """
    @staticmethod
    def sech(ctx, *args, **kwargs):
        """
        Computes the hyperbolic secant of `x`,
        `\\mathrm{sech}(x) = \\frac{1}{\\cosh(x)}`.
        """
    @staticmethod
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
    @staticmethod
    def shi(ctx, *args, **kwargs):
        """
        
        Computes the hyperbolic sine integral, defined
        in analogy with the sine integral (see :func:`~mpmath.si`) as
        
        .. math ::
        
            \\mathrm{Shi}(x) = \\int_0^x \\frac{\\sinh t}{t}\\,dt.
        
        Some values and limits::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> shi(0)
            0.0
            >>> shi(1)
            1.057250875375728514571842
            >>> shi(-1)
            -1.057250875375728514571842
            >>> shi(inf)
            +inf
            >>> shi(2+3j)
            (-0.1931890762719198291678095 + 2.645432555362369624818525j)
        
        Evaluation is supported for `z` anywhere in the complex plane::
        
            >>> shi(10**6*(1+j))
            (4.449410587611035724984376e+434287 - 9.75744874290013526417059e+434287j)
        
        """
    @staticmethod
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
    @staticmethod
    def siegeltheta(ctx, *args, **kwargs):
        """
        
        Computes the Riemann-Siegel theta function,
        
        .. math ::
        
            \\theta(t) = \\frac{
            \\log\\Gamma\\left(\\frac{1+2it}{4}\\right) -
            \\log\\Gamma\\left(\\frac{1-2it}{4}\\right)
            }{2i} - \\frac{\\log \\pi}{2} t.
        
        The Riemann-Siegel theta function is important in
        providing the phase factor for the Z-function
        (see :func:`~mpmath.siegelz`). Evaluation is supported for real and
        complex arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> siegeltheta(0)
            0.0
            >>> siegeltheta(inf)
            +inf
            >>> siegeltheta(-inf)
            -inf
            >>> siegeltheta(1)
            -1.767547952812290388302216
            >>> siegeltheta(10+0.25j)
            (-3.068638039426838572528867 + 0.05804937947429712998395177j)
        
        Arbitrary derivatives may be computed with derivative = k
        
            >>> siegeltheta(1234, derivative=2)
            0.0004051864079114053109473741
            >>> diff(siegeltheta, 1234, n=2)
            0.0004051864079114053109473741
        
        
        The Riemann-Siegel theta function has odd symmetry around `t = 0`,
        two local extreme points and three real roots including 0 (located
        symmetrically)::
        
            >>> nprint(chop(taylor(siegeltheta, 0, 5)))
            [0.0, -2.68609, 0.0, 2.69433, 0.0, -6.40218]
            >>> findroot(diffun(siegeltheta), 7)
            6.28983598883690277966509
            >>> findroot(siegeltheta, 20)
            17.84559954041086081682634
        
        For large `t`, there is a famous asymptotic formula
        for `\\theta(t)`, to first order given by::
        
            >>> t = mpf(10**6)
            >>> siegeltheta(t)
            5488816.353078403444882823
            >>> -t*log(2*pi/t)/2-t/2
            5488816.745777464310273645
        """
    @staticmethod
    def siegelz(ctx, *args, **kwargs):
        """
        
        Computes the Z-function, also known as the Riemann-Siegel Z function,
        
        .. math ::
        
            Z(t) = e^{i \\theta(t)} \\zeta(1/2+it)
        
        where `\\zeta(s)` is the Riemann zeta function (:func:`~mpmath.zeta`)
        and where `\\theta(t)` denotes the Riemann-Siegel theta function
        (see :func:`~mpmath.siegeltheta`).
        
        Evaluation is supported for real and complex arguments::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> siegelz(1)
            -0.7363054628673177346778998
            >>> siegelz(3+4j)
            (-0.1852895764366314976003936 - 0.2773099198055652246992479j)
        
        The first four derivatives are supported, using the
        optional *derivative* keyword argument::
        
            >>> siegelz(1234567, derivative=3)
            56.89689348495089294249178
            >>> diff(siegelz, 1234567, n=3)
            56.89689348495089294249178
        
        
        The Z-function has a Maclaurin expansion::
        
            >>> nprint(chop(taylor(siegelz, 0, 4)))
            [-1.46035, 0.0, 2.73588, 0.0, -8.39357]
        
        The Z-function `Z(t)` is equal to `\\pm |\\zeta(s)|` on the
        critical line `s = 1/2+it` (i.e. for real arguments `t`
        to `Z`).  Its zeros coincide with those of the Riemann zeta
        function::
        
            >>> findroot(siegelz, 14)
            14.13472514173469379045725
            >>> findroot(siegelz, 20)
            21.02203963877155499262848
            >>> findroot(zeta, 0.5+14j)
            (0.5 + 14.13472514173469379045725j)
            >>> findroot(zeta, 0.5+20j)
            (0.5 + 21.02203963877155499262848j)
        
        Since the Z-function is real-valued on the critical line
        (and unlike `|\\zeta(s)|` analytic), it is useful for
        investigating the zeros of the Riemann zeta function.
        For example, one can use a root-finding algorithm based
        on sign changes::
        
            >>> findroot(siegelz, [100, 200], solver='bisect')
            176.4414342977104188888926
        
        To locate roots, Gram points `g_n` which can be computed
        by :func:`~mpmath.grampoint` are useful. If `(-1)^n Z(g_n)` is
        positive for two consecutive `n`, then `Z(t)` must have
        a zero between those points::
        
            >>> g10 = grampoint(10)
            >>> g11 = grampoint(11)
            >>> (-1)**10 * siegelz(g10) > 0
            True
            >>> (-1)**11 * siegelz(g11) > 0
            True
            >>> findroot(siegelz, [g10, g11], solver='bisect')
            56.44624769706339480436776
            >>> g10, g11
            (54.67523744685325626632663, 57.54516517954725443703014)
        
        """
    @staticmethod
    def sigmoid(ctx, *args, **kwargs):
        """
        
        Computes the sigmoid function using the definition:
        
        .. math::
            x(t) = \\frac{A}{1 + e^{-t}}
        
        where `A` is the amplitude.
        
        **Examples**
        
        Sigmoid function with amplitude = 1 ::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> sigmoid(-1,1)
            0.2689414213699951207488408
            >>> sigmoid(-0.5,1)
            0.3775406687981454353610994
            >>> sigmoid(0,1)
            0.5
            >>> sigmoid(0.5,1)
            0.6224593312018545646389006
            >>> sigmoid(1,1)
            0.7310585786300048792511592
        
        """
    @staticmethod
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
    @staticmethod
    def sinc(ctx, *args, **kwargs):
        """
        
        ``sinc(x)`` computes the unnormalized sinc function, defined as
        
        .. math ::
        
            \\mathrm{sinc}(x) = \\begin{cases}
                \\sin(x)/x, & \\mbox{if } x \\ne 0 \\\\
                1,         & \\mbox{if } x = 0.
            \\end{cases}
        
        See :func:`~mpmath.sincpi` for the normalized sinc function.
        
        Simple values and limits include::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> sinc(0)
            1.0
            >>> sinc(1)
            0.841470984807897
            >>> sinc(inf)
            0.0
        
        The integral of the sinc function is the sine integral Si::
        
            >>> quad(sinc, [0, 1])
            0.946083070367183
            >>> si(1)
            0.946083070367183
        """
    @staticmethod
    def sincpi(ctx, *args, **kwargs):
        """
        
        ``sincpi(x)`` computes the normalized sinc function, defined as
        
        .. math ::
        
            \\mathrm{sinc}_{\\pi}(x) = \\begin{cases}
                \\sin(\\pi x)/(\\pi x), & \\mbox{if } x \\ne 0 \\\\
                1,                   & \\mbox{if } x = 0.
            \\end{cases}
        
        Equivalently, we have
        `\\mathrm{sinc}_{\\pi}(x) = \\mathrm{sinc}(\\pi x)`.
        
        The normalization entails that the function integrates
        to unity over the entire real line::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> quadosc(sincpi, [-inf, inf], period=2.0)
            1.0
        
        Like, :func:`~mpmath.sinpi`, :func:`~mpmath.sincpi` is evaluated accurately
        at its roots::
        
            >>> sincpi(10)
            0.0
        """
    @staticmethod
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
    @staticmethod
    def square_exp_arg(ctx, z, mult = 1, reciprocal = False):
        ...
    @staticmethod
    def squarew(ctx, *args, **kwargs):
        """
        
        Computes the square wave function using the definition:
        
        .. math::
            x(t) = A(-1)^{\\left\\lfloor{2t / P}\\right\\rfloor}
        
        where `P` is the period of the wave and `A` is the amplitude.
        
        **Examples**
        
        Square wave with period = 2, amplitude = 1 ::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> squarew(0,1,2)
            1.0
            >>> squarew(0.5,1,2)
            1.0
            >>> squarew(1,1,2)
            -1.0
            >>> squarew(1.5,1,2)
            -1.0
            >>> squarew(2,1,2)
            1.0
        """
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def superfac(ctx, z):
        """
        
        Computes the superfactorial, defined as the product of
        consecutive factorials
        
        .. math ::
        
            \\mathrm{sf}(n) = \\prod_{k=1}^n k!
        
        For general complex `z`, `\\mathrm{sf}(z)` is defined
        in terms of the Barnes G-function (see :func:`~mpmath.barnesg`).
        
        **Examples**
        
        The first few superfactorials are (OEIS A000178)::
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = True
            >>> for n in range(10):
            ...     print("%s %s" % (n, superfac(n)))
            ...
            0 1.0
            1 1.0
            2 2.0
            3 12.0
            4 288.0
            5 34560.0
            6 24883200.0
            7 125411328000.0
            8 5.05658474496e+15
            9 1.83493347225108e+21
        
        Superfactorials grow very rapidly::
        
            >>> superfac(1000)
            3.24570818422368e+1177245
            >>> superfac(10**10)
            2.61398543581249e+467427913956904067453
        
        Evaluation is supported for arbitrary arguments::
        
            >>> mp.dps = 25
            >>> superfac(pi)
            17.20051550121297985285333
            >>> superfac(2+3j)
            (-0.005915485633199789627466468 + 0.008156449464604044948738263j)
            >>> diff(superfac, 1)
            0.2645072034016070205673056
        
        **References**
        
        1. http://oeis.org/A000178
        
        """
    @staticmethod
    def taufrom(ctx, *args, **kwargs):
        """
        
        Returns the elliptic half-period ratio `\\tau`, given any of
        `q, m, k, \\tau, \\bar{q}`::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> taufrom(tau=0.5j)
            (0.0 + 0.5j)
            >>> taufrom(q=qfrom(tau=0.5j))
            (0.0 + 0.5j)
            >>> taufrom(m=mfrom(tau=0.5j))
            (0.0 + 0.5j)
            >>> taufrom(k=kfrom(tau=0.5j))
            (0.0 + 0.5j)
            >>> taufrom(qbar=qbarfrom(tau=0.5j))
            (0.0 + 0.5j)
        
        """
    @staticmethod
    def to_fixed(ctx, x, prec):
        ...
    @staticmethod
    def trianglew(ctx, *args, **kwargs):
        """
        
        Computes the triangle wave function using the definition:
        
        .. math::
            x(t) = 2A\\left(\\frac{1}{2}-\\left|1-2 \\operatorname{frac}\\left(\\frac{x}{P}+\\frac{1}{4}\\right)\\right|\\right)
        
        where :math:`\\operatorname{frac}\\left(\\frac{t}{T}\\right) = \\frac{t}{T}-\\left\\lfloor{\\frac{t}{T}}\\right\\rfloor`
        , `P` is the period of the wave, and `A` is the amplitude.
        
        **Examples**
        
        Triangle wave with period = 2, amplitude = 1 ::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> trianglew(0,1,2)
            0.0
            >>> trianglew(0.25,1,2)
            0.5
            >>> trianglew(0.5,1,2)
            1.0
            >>> trianglew(1,1,2)
            0.0
            >>> trianglew(1.5,1,2)
            -1.0
            >>> trianglew(2,1,2)
            0.0
        """
    @staticmethod
    def unit_triangle(ctx, *args, **kwargs):
        """
        
        Computes the unit triangle using the definition:
        
        .. math::
            x(t) = A(-\\left| t \\right| + 1)
        
        where `A` is the amplitude.
        
        **Examples**
        
        Unit triangle with amplitude = 1 ::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> unit_triangle(-1,1)
            0.0
            >>> unit_triangle(-0.5,1)
            0.5
            >>> unit_triangle(0,1)
            1.0
            >>> unit_triangle(0.5,1)
            0.5
            >>> unit_triangle(1,1)
            0.0
        """
    @staticmethod
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
    @staticmethod
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
    @staticmethod
    def whitm(ctx, *args, **kwargs):
        """
        
        Evaluates the Whittaker function `M(k,m,z)`, which gives a solution
        to the Whittaker differential equation
        
        .. math ::
        
            \\frac{d^2f}{dz^2} + \\left(-\\frac{1}{4}+\\frac{k}{z}+
              \\frac{(\\frac{1}{4}-m^2)}{z^2}\\right) f = 0.
        
        A second solution is given by :func:`~mpmath.whitw`.
        
        The Whittaker functions are defined in Abramowitz & Stegun, section 13.1.
        They are alternate forms of the confluent hypergeometric functions
        `\\,_1F_1` and `U`:
        
        .. math ::
        
            M(k,m,z) = e^{-\\frac{1}{2}z} z^{\\frac{1}{2}+m}
                \\,_1F_1(\\tfrac{1}{2}+m-k, 1+2m, z)
        
            W(k,m,z) = e^{-\\frac{1}{2}z} z^{\\frac{1}{2}+m}
                U(\\tfrac{1}{2}+m-k, 1+2m, z).
        
        **Examples**
        
        Evaluation for arbitrary real and complex arguments is supported::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> whitm(1, 1, 1)
            0.7302596799460411820509668
            >>> whitm(1, 1, -1)
            (0.0 - 1.417977827655098025684246j)
            >>> whitm(j, j/2, 2+3j)
            (3.245477713363581112736478 - 0.822879187542699127327782j)
            >>> whitm(2, 3, 100000)
            4.303985255686378497193063e+21707
        
        Evaluation at zero::
        
            >>> whitm(1,-1,0); whitm(1,-0.5,0); whitm(1,0,0)
            +inf
            nan
            0.0
        
        We can verify that :func:`~mpmath.whitm` numerically satisfies the
        differential equation for arbitrarily chosen values::
        
            >>> k = mpf(0.25)
            >>> m = mpf(1.5)
            >>> f = lambda z: whitm(k,m,z)
            >>> for z in [-1, 2.5, 3, 1+2j]:
            ...     chop(diff(f,z,2) + (-0.25 + k/z + (0.25-m**2)/z**2)*f(z))
            ...
            0.0
            0.0
            0.0
            0.0
        
        An integral involving both :func:`~mpmath.whitm` and :func:`~mpmath.whitw`,
        verifying evaluation along the real axis::
        
            >>> quad(lambda x: exp(-x)*whitm(3,2,x)*whitw(1,-2,x), [0,inf])
            3.438869842576800225207341
            >>> 128/(21*sqrt(pi))
            3.438869842576800225207341
        
        """
    @staticmethod
    def whitw(ctx, *args, **kwargs):
        """
        
        Evaluates the Whittaker function `W(k,m,z)`, which gives a second
        solution to the Whittaker differential equation. (See :func:`~mpmath.whitm`.)
        
        **Examples**
        
        Evaluation for arbitrary real and complex arguments is supported::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> whitw(1, 1, 1)
            1.19532063107581155661012
            >>> whitw(1, 1, -1)
            (-0.9424875979222187313924639 - 0.2607738054097702293308689j)
            >>> whitw(j, j/2, 2+3j)
            (0.1782899315111033879430369 - 0.01609578360403649340169406j)
            >>> whitw(2, 3, 100000)
            1.887705114889527446891274e-21705
            >>> whitw(-1, -1, 100)
            1.905250692824046162462058e-24
        
        Evaluation at zero::
        
            >>> for m in [-1, -0.5, 0, 0.5, 1]:
            ...     whitw(1, m, 0)
            ...
            +inf
            nan
            0.0
            nan
            +inf
        
        We can verify that :func:`~mpmath.whitw` numerically satisfies the
        differential equation for arbitrarily chosen values::
        
            >>> k = mpf(0.25)
            >>> m = mpf(1.5)
            >>> f = lambda z: whitw(k,m,z)
            >>> for z in [-1, 2.5, 3, 1+2j]:
            ...     chop(diff(f,z,2) + (-0.25 + k/z + (0.25-m**2)/z**2)*f(z))
            ...
            0.0
            0.0
            0.0
            0.0
        
        """
    @staticmethod
    def workdps(ctx, n, normalize_output = False):
        """
        
        This function is analogous to workprec (see documentation)
        but changes the decimal precision instead of the number of bits.
        """
    @staticmethod
    def workprec(ctx, n, normalize_output = False):
        """
        
        The block
        
            with workprec(n):
                <code>
        
        sets the precision to n bits, executes <code>, and then restores
        the precision.
        
        workprec(n)(f) returns a decorated version of the function f
        that sets the precision to n bits before execution,
        and restores the precision afterwards. With normalize_output=True,
        it rounds the return value to the parent precision.
        """
    @staticmethod
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
    @staticmethod
    def zetazero(ctx, n, info = False, round = True):
        """
        
        Computes the `n`-th nontrivial zero of `\\zeta(s)` on the critical line,
        i.e. returns an approximation of the `n`-th largest complex number
        `s = \\frac{1}{2} + ti` for which `\\zeta(s) = 0`. Equivalently, the
        imaginary part `t` is a zero of the Z-function (:func:`~mpmath.siegelz`).
        
        **Examples**
        
        The first few zeros::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> zetazero(1)
            (0.5 + 14.13472514173469379045725j)
            >>> zetazero(2)
            (0.5 + 21.02203963877155499262848j)
            >>> zetazero(20)
            (0.5 + 77.14484006887480537268266j)
        
        Verifying that the values are zeros::
        
            >>> for n in range(1,5):
            ...     s = zetazero(n)
            ...     chop(zeta(s)), chop(siegelz(s.imag))
            ...
            (0.0, 0.0)
            (0.0, 0.0)
            (0.0, 0.0)
            (0.0, 0.0)
        
        Negative indices give the conjugate zeros (`n = 0` is undefined)::
        
            >>> zetazero(-1)
            (0.5 - 14.13472514173469379045725j)
        
        :func:`~mpmath.zetazero` supports arbitrarily large `n` and arbitrary precision::
        
            >>> mp.dps = 15
            >>> zetazero(1234567)
            (0.5 + 727690.906948208j)
            >>> mp.dps = 50
            >>> zetazero(1234567)
            (0.5 + 727690.9069482075392389420041147142092708393819935j)
            >>> chop(zeta(_)/_)
            0.0
        
        with *info=True*, :func:`~mpmath.zetazero` gives additional information::
        
            >>> mp.dps = 15
            >>> zetazero(542964976,info=True)
            ((0.5 + 209039046.578535j), [542964969, 542964978], 6, '(013111110)')
        
        This means that the zero is between Gram points 542964969 and 542964978;
        it is the 6-th zero between them. Finally (01311110) is the pattern
        of zeros in this interval. The numbers indicate the number of zeros
        in each Gram interval (Rosser blocks between parenthesis). In this case
        there is only one Rosser block of length nine.
        """
    @property
    def _repr_digits(self):
        ...
    @property
    def _str_digits(self):
        ...
class PrecisionManager:
    def __call__(self, f):
        ...
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
    def __init__(self, ctx, precfun, dpsfun, normalize_output = False):
        ...
BACKEND: str = 'gmpy'
MPZ_ONE: gmpy2.mpz  # value = mpz(1)
MPZ_ZERO: gmpy2.mpz  # value = mpz(0)
__docformat__: str = 'plaintext'
finf: tuple  # value = (0, mpz(0), -456, -2)
fnan: tuple  # value = (0, mpz(0), -123, -1)
fninf: tuple  # value = (1, mpz(0), -789, -3)
fone: tuple  # value = (0, mpz(1), 0, 1)
fzero: tuple  # value = (0, mpz(0), 0, 0)
get_complex: re.Pattern  # value = re.compile('^\\(?(?P<re>[\\+\\-]?\\d*(\\.\\d*)?(e[\\+\\-]?\\d+)?)??(?P<im>[\\+\\-]?\\d*(\\.\\d*)?(e[\\+\\-]?\\d+)?j)?\\)?$')
int_types: tuple = (int, gmpy2.mpz)
round_ceiling: str = 'c'
round_floor: str = 'f'
round_nearest: str = 'n'
