from __future__ import annotations
from builtins import str as basestring
import gmpy2
import mpmath.ctx_base
from mpmath.ctx_base import StandardBaseContext
from mpmath import libmp
from mpmath.libmp.libmpc import mpc_hash
from mpmath.libmp.libmpf import ComplexResult
from mpmath.libmp.libmpf import dps_to_prec
from mpmath.libmp.libmpf import from_float
from mpmath.libmp.libmpf import from_int
from mpmath.libmp.libmpf import from_rational
from mpmath.libmp.libmpf import from_str
from mpmath.libmp.libmpf import mpf_hash
from mpmath.libmp.libmpf import mpf_le
from mpmath.libmp.libmpf import mpf_neg
from mpmath.libmp.libmpf import prec_to_dps
from mpmath.libmp.libmpf import repr_dps
from mpmath.libmp.libmpi import mpci_abs
from mpmath.libmp.libmpi import mpci_add
from mpmath.libmp.libmpi import mpci_div
from mpmath.libmp.libmpi import mpci_exp
from mpmath.libmp.libmpi import mpci_log
from mpmath.libmp.libmpi import mpci_mul
from mpmath.libmp.libmpi import mpci_neg
from mpmath.libmp.libmpi import mpci_pos
from mpmath.libmp.libmpi import mpci_pow
from mpmath.libmp.libmpi import mpci_sub
from mpmath.libmp.libmpi import mpi_abs
from mpmath.libmp.libmpi import mpi_add
from mpmath.libmp.libmpi import mpi_delta
from mpmath.libmp.libmpi import mpi_div
from mpmath.libmp.libmpi import mpi_from_str
from mpmath.libmp.libmpi import mpi_mid
from mpmath.libmp.libmpi import mpi_mul
from mpmath.libmp.libmpi import mpi_neg
from mpmath.libmp.libmpi import mpi_pos
from mpmath.libmp.libmpi import mpi_pow
from mpmath.libmp.libmpi import mpi_pow_int
from mpmath.libmp.libmpi import mpi_str
from mpmath.libmp.libmpi import mpi_sub
from mpmath.matrices.matrices import _matrix
import numbers as numbers
import operator as operator
__all__: list[str] = ['ComplexResult', 'MPIntervalContext', 'MPZ_ONE', 'StandardBaseContext', 'basestring', 'convert_mpf_', 'dps_to_prec', 'finf', 'fnan', 'fninf', 'from_float', 'from_int', 'from_rational', 'from_str', 'fzero', 'int_types', 'ivmpc', 'ivmpf', 'ivmpf_constant', 'libmp', 'mpc_hash', 'mpci_abs', 'mpci_add', 'mpci_div', 'mpci_exp', 'mpci_log', 'mpci_mul', 'mpci_neg', 'mpci_pos', 'mpci_pow', 'mpci_sub', 'mpf_hash', 'mpf_le', 'mpf_neg', 'mpi_abs', 'mpi_add', 'mpi_delta', 'mpi_div', 'mpi_from_str', 'mpi_mid', 'mpi_mul', 'mpi_neg', 'mpi_pos', 'mpi_pow', 'mpi_pow_int', 'mpi_str', 'mpi_sub', 'mpi_zero', 'numbers', 'operator', 'prec_to_dps', 'repr_dps', 'round_ceiling', 'round_floor']
class MPIntervalContext(mpmath.ctx_base.StandardBaseContext):
    dps = ...
    prec = ...
    @staticmethod
    def __init__(ctx):
        ...
    @staticmethod
    def _altzeta_generic(ctx, *args, **kwargs):
        ...
    @staticmethod
    def _ci_generic(ctx, *args, **kwargs):
        ...
    @staticmethod
    def _convert_param(ctx, x):
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
    def _gamma3(ctx, z, a, b, regularized = False):
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
    def _init_builtins(ctx):
        ...
    @staticmethod
    def _is_complex_type(ctx, z):
        ...
    @staticmethod
    def _is_real_type(ctx, z):
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
    def _mpi(ctx, a, b = None):
        ...
    @staticmethod
    def _mpq(ctx, pq):
        ...
    @staticmethod
    def _rootof1(ctx, k, n):
        ...
    @staticmethod
    def _set_dps(ctx, n):
        ...
    @staticmethod
    def _set_prec(ctx, n):
        ...
    @staticmethod
    def _si_generic(ctx, *args, **kwargs):
        ...
    @staticmethod
    def _upper_gamma(ctx, z, a, regularized = False):
        ...
    @staticmethod
    def _wrap_mpi_function(ctx, f_real, f_complex = None):
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
    def absmax(ctx, x):
        ...
    @staticmethod
    def absmin(ctx, x):
        ...
    @staticmethod
    def acot(ctx, *args, **kwargs):
        ...
    @staticmethod
    def acoth(ctx, *args, **kwargs):
        ...
    @staticmethod
    def acsc(ctx, *args, **kwargs):
        ...
    @staticmethod
    def acsch(ctx, *args, **kwargs):
        ...
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
        ...
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
        ...
    @staticmethod
    def asech(ctx, *args, **kwargs):
        ...
    @staticmethod
    def atan2(ctx, y, x):
        ...
    @staticmethod
    def backlunds(ctx, *args, **kwargs):
        ...
    @staticmethod
    def barnesg(ctx, *args, **kwargs):
        ...
    @staticmethod
    def bei(ctx, n, z, **kwargs):
        """
        
        Computes the Kelvin function bei, which for real arguments gives the
        imaginary part of the Bessel J function of a rotated argument.
        See :func:`~mpmath.ber`.
        """
    @staticmethod
    def bell(ctx, *args, **kwargs):
        ...
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
    def bernpoly(ctx, *args, **kwargs):
        ...
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
        ...
    @staticmethod
    def bessely(ctx, *args, **kwargs):
        ...
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
        ...
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
        ...
    @staticmethod
    def chebyu(ctx, *args, **kwargs):
        ...
    @staticmethod
    def chi(ctx, *args, **kwargs):
        ...
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
        ...
    @staticmethod
    def clsin(ctx, *args, **kwargs):
        ...
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
    def convert(ctx, x):
        ...
    @staticmethod
    def cot(ctx, *args, **kwargs):
        ...
    @staticmethod
    def coth(ctx, *args, **kwargs):
        ...
    @staticmethod
    def coulombc(ctx, *args, **kwargs):
        ...
    @staticmethod
    def coulombf(ctx, *args, **kwargs):
        ...
    @staticmethod
    def coulombg(ctx, *args, **kwargs):
        ...
    @staticmethod
    def csc(ctx, *args, **kwargs):
        ...
    @staticmethod
    def csch(ctx, *args, **kwargs):
        ...
    @staticmethod
    def cyclotomic(ctx, *args, **kwargs):
        ...
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
        ...
    @staticmethod
    def ellipf(ctx, *args, **kwargs):
        ...
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
        ...
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
        ...
    @staticmethod
    def erfinv(ctx, *args, **kwargs):
        ...
    @staticmethod
    def eta(ctx, *args, **kwargs):
        ...
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
        ...
    @staticmethod
    def expint(ctx, *args, **kwargs):
        ...
    @staticmethod
    def expm1(ctx, *args, **kwargs):
        ...
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
        ...
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
    def fresnelc(ctx, *args, **kwargs):
        ...
    @staticmethod
    def fresnels(ctx, *args, **kwargs):
        ...
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
        ...
    @staticmethod
    def grampoint(ctx, *args, **kwargs):
        ...
    @staticmethod
    def hankel1(ctx, *args, **kwargs):
        ...
    @staticmethod
    def hankel2(ctx, *args, **kwargs):
        ...
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
        ...
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
    def hypsum(ctx, p, q, types, coeffs, z, maxterms = 6000, **kwargs):
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
    def isinf(ctx, x):
        ...
    @staticmethod
    def isint(ctx, x):
        ...
    @staticmethod
    def isnan(ctx, x):
        ...
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
        ...
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
        ...
    @staticmethod
    def kleinj(ctx, *args, **kwargs):
        ...
    @staticmethod
    def laguerre(ctx, *args, **kwargs):
        ...
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
        ...
    @staticmethod
    def legendre(ctx, *args, **kwargs):
        ...
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
        ...
    @staticmethod
    def li(ctx, *args, **kwargs):
        ...
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
        ...
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
    def mag(ctx, x):
        ...
    @staticmethod
    def make_mpc(ctx, v):
        ...
    @staticmethod
    def make_mpf(ctx, v):
        ...
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
        ...
    @staticmethod
    def ncdf(ctx, *args, **kwargs):
        ...
    @staticmethod
    def npdf(ctx, *args, **kwargs):
        ...
    @staticmethod
    def nstr(ctx, x, n = 5, **kwargs):
        ...
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
        ...
    @staticmethod
    def polylog(ctx, *args, **kwargs):
        ...
    @staticmethod
    def powm1(ctx, *args, **kwargs):
        ...
    @staticmethod
    def primepi2(ctx, *args, **kwargs):
        ...
    @staticmethod
    def primezeta(ctx, *args, **kwargs):
        ...
    @staticmethod
    def qbarfrom(ctx, *args, **kwargs):
        ...
    @staticmethod
    def qfac(ctx, *args, **kwargs):
        ...
    @staticmethod
    def qfrom(ctx, *args, **kwargs):
        ...
    @staticmethod
    def qgamma(ctx, *args, **kwargs):
        ...
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
        ...
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
        ...
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
        ...
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
        ...
    @staticmethod
    def sech(ctx, *args, **kwargs):
        ...
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
        ...
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
        ...
    @staticmethod
    def siegelz(ctx, *args, **kwargs):
        ...
    @staticmethod
    def sigmoid(ctx, *args, **kwargs):
        ...
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
        ...
    @staticmethod
    def sincpi(ctx, *args, **kwargs):
        ...
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
        ...
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
        ...
    @staticmethod
    def trianglew(ctx, *args, **kwargs):
        ...
    @staticmethod
    def unit_triangle(ctx, *args, **kwargs):
        ...
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
        ...
    @staticmethod
    def whitw(ctx, *args, **kwargs):
        ...
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
    @classmethod
    def _wrap_specfun(cls, name, f, wrap):
        ...
class ivmpc:
    @staticmethod
    def __abs__(s):
        ...
    @staticmethod
    def __add__(s, t):
        ...
    @staticmethod
    def __contains__(s, t):
        ...
    @staticmethod
    def __div__(s, t):
        ...
    @staticmethod
    def __eq__(s, t):
        ...
    @staticmethod
    def __ge__(s, t):
        ...
    @staticmethod
    def __gt__(s, t):
        ...
    @staticmethod
    def __le__(s, t):
        ...
    @staticmethod
    def __lt__(s, t):
        ...
    @staticmethod
    def __mul__(s, t):
        ...
    @staticmethod
    def __ne__(s, t):
        ...
    @staticmethod
    def __neg__(s):
        ...
    @staticmethod
    def __pos__(s):
        ...
    @staticmethod
    def __pow__(s, t):
        ...
    @staticmethod
    def __radd__(s, t):
        ...
    @staticmethod
    def __rdiv__(s, t):
        ...
    @staticmethod
    def __repr__(s):
        ...
    @staticmethod
    def __rmul__(s, t):
        ...
    @staticmethod
    def __rpow__(s, t):
        ...
    @staticmethod
    def __rsub__(s, t):
        ...
    @staticmethod
    def __rtruediv__(s, t):
        ...
    @staticmethod
    def __str__(s):
        ...
    @staticmethod
    def __sub__(s, t):
        ...
    @staticmethod
    def __truediv__(s, t):
        ...
    @staticmethod
    def _compare(s, t, ne = False):
        ...
    @staticmethod
    def ae(s, t, rel_eps = None, abs_eps = None):
        ...
    @staticmethod
    def conjugate(s):
        ...
    @staticmethod
    def overlap(s, t):
        ...
    @classmethod
    def __new__(cls, re = 0, im = 0):
        ...
    def __hash__(self):
        ...
    @property
    def a(self):
        ...
    @property
    def b(self):
        ...
    @property
    def c(self):
        ...
    @property
    def d(self):
        ...
    @property
    def imag(self):
        ...
    @property
    def real(self):
        ...
class ivmpf:
    """
    
    Interval arithmetic class. Precision is controlled by iv.prec.
    """
    @staticmethod
    def __add__(s, t):
        ...
    @staticmethod
    def __div__(s, t):
        ...
    @staticmethod
    def __eq__(s, t):
        ...
    @staticmethod
    def __ge__(s, t):
        ...
    @staticmethod
    def __gt__(s, t):
        ...
    @staticmethod
    def __le__(s, t):
        ...
    @staticmethod
    def __lt__(s, t):
        ...
    @staticmethod
    def __mul__(s, t):
        ...
    @staticmethod
    def __ne__(s, t):
        ...
    @staticmethod
    def __pow__(s, t):
        ...
    @staticmethod
    def __radd__(s, t):
        ...
    @staticmethod
    def __rdiv__(s, t):
        ...
    @staticmethod
    def __rmul__(s, t):
        ...
    @staticmethod
    def __rpow__(s, t):
        ...
    @staticmethod
    def __rsub__(s, t):
        ...
    @staticmethod
    def __rtruediv__(s, t):
        ...
    @staticmethod
    def __sub__(s, t):
        ...
    @staticmethod
    def __truediv__(s, t):
        ...
    @staticmethod
    def _compare(s, t, cmpfun):
        ...
    @staticmethod
    def ae(s, t, rel_eps = None, abs_eps = None):
        ...
    @classmethod
    def __new__(cls, x = 0):
        ...
    def __abs__(self):
        ...
    def __complex__(self):
        ...
    def __contains__(self, t):
        ...
    def __float__(self):
        ...
    def __hash__(self):
        ...
    def __int__(self):
        ...
    def __neg__(self):
        ...
    def __pos__(self):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def cast(self, cls, f_convert):
        ...
    def conjugate(self):
        ...
    @property
    def _mpci_(self):
        ...
    @property
    def a(self):
        ...
    @property
    def b(self):
        ...
    @property
    def delta(self):
        ...
    @property
    def imag(self):
        ...
    @property
    def mid(self):
        ...
    @property
    def real(self):
        ...
class ivmpf_constant(ivmpf):
    @classmethod
    def __new__(cls, f):
        ...
    def _get_mpi_(self):
        ...
    @property
    def _mpi_(self):
        ...
def _binary_op(f_real, f_complex):
    ...
def convert_mpf_(x, prec, rounding):
    ...
MPZ_ONE: gmpy2.mpz  # value = mpz(1)
finf: tuple  # value = (0, mpz(0), -456, -2)
fnan: tuple  # value = (0, mpz(0), -123, -1)
fninf: tuple  # value = (1, mpz(0), -789, -3)
fzero: tuple  # value = (0, mpz(0), 0, 0)
int_types: tuple = (int, gmpy2.mpz)
mpi_zero: tuple  # value = ((0, mpz(0), 0, 0), (0, mpz(0), 0, 0))
round_ceiling: str = 'c'
round_floor: str = 'f'
