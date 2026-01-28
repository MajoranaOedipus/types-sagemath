"""

This module implements computation of hypergeometric and related
functions. In particular, it provides code for generic summation
of hypergeometric series. Optimized versions for various special
cases are also provided.
"""
from __future__ import annotations
from builtins import exec as exec_
from builtins import range as xrange
import gmpy2
from gmpy2.gmpy2 import _mpmath_create as from_man_exp
from gmpy2.gmpy2 import bit_length as bitcount
from gmpy2.gmpy2 import fac as ifac
import math as math
from mpmath.libmp.gammazeta import mpf_gamma_int
from mpmath.libmp.libelefun import agm_fixed
from mpmath.libmp.libelefun import mpf_cos
from mpmath.libmp.libelefun import mpf_cos_sin
from mpmath.libmp.libelefun import mpf_exp
from mpmath.libmp.libelefun import mpf_log
from mpmath.libmp.libelefun import mpf_sin
from mpmath.libmp.libintmath import gcd
from mpmath.libmp.libintmath import sqrt_fixed
from mpmath.libmp.libmpc import complex_int_pow
from mpmath.libmp.libmpc import mpc_abs
from mpmath.libmp.libmpc import mpc_add
from mpmath.libmp.libmpc import mpc_add_mpf
from mpmath.libmp.libmpc import mpc_div
from mpmath.libmp.libmpc import mpc_exp
from mpmath.libmp.libmpc import mpc_is_infnan
from mpmath.libmp.libmpc import mpc_log
from mpmath.libmp.libmpc import mpc_mpf_div
from mpmath.libmp.libmpc import mpc_mul
from mpmath.libmp.libmpc import mpc_mul_mpf
from mpmath.libmp.libmpc import mpc_neg
from mpmath.libmp.libmpc import mpc_pos
from mpmath.libmp.libmpc import mpc_shift
from mpmath.libmp.libmpc import mpc_sqrt
from mpmath.libmp.libmpc import mpc_square
from mpmath.libmp.libmpc import mpc_sub
from mpmath.libmp.libmpc import mpc_sub_mpf
from mpmath.libmp.libmpf import ComplexResult
from mpmath.libmp.libmpf import from_int
from mpmath.libmp.libmpf import from_rational
from mpmath.libmp.libmpf import gmpy_mpf_mul as mpf_mul
from mpmath.libmp.libmpf import mpf_abs
from mpmath.libmp.libmpf import mpf_add
from mpmath.libmp.libmpf import mpf_cmp
from mpmath.libmp.libmpf import mpf_div
from mpmath.libmp.libmpf import mpf_gt
from mpmath.libmp.libmpf import mpf_le
from mpmath.libmp.libmpf import mpf_lt
from mpmath.libmp.libmpf import mpf_min_max
from mpmath.libmp.libmpf import mpf_neg
from mpmath.libmp.libmpf import mpf_perturb
from mpmath.libmp.libmpf import mpf_pos
from mpmath.libmp.libmpf import mpf_pow_int
from mpmath.libmp.libmpf import mpf_rdiv_int
from mpmath.libmp.libmpf import mpf_shift
from mpmath.libmp.libmpf import mpf_sign
from mpmath.libmp.libmpf import mpf_sqrt
from mpmath.libmp.libmpf import mpf_sub
from mpmath.libmp.libmpf import to_fixed
from mpmath.libmp.libmpf import to_int
from mpmath.libmp.libmpf import to_rational
import operator as operator
__all__: list[str] = ['BACKEND', 'ComplexResult', 'MPZ_ONE', 'MPZ_ZERO', 'NoConvergence', 'agm_fixed', 'bitcount', 'complex_ei_asymptotic', 'complex_ei_taylor', 'complex_int_pow', 'ei_asymptotic', 'ei_taylor', 'erfc_check_series', 'exec_', 'finf', 'fnan', 'fninf', 'fnone', 'fone', 'from_int', 'from_man_exp', 'from_rational', 'ftwo', 'fzero', 'gcd', 'ifac', 'make_hyp_summator', 'math', 'mpc_abs', 'mpc_add', 'mpc_add_mpf', 'mpc_agm', 'mpc_agm1', 'mpc_besseljn', 'mpc_ci', 'mpc_ci_si_taylor', 'mpc_div', 'mpc_e1', 'mpc_ei', 'mpc_ellipe', 'mpc_ellipk', 'mpc_exp', 'mpc_is_infnan', 'mpc_log', 'mpc_mpf_div', 'mpc_mul', 'mpc_mul_mpf', 'mpc_neg', 'mpc_one', 'mpc_pos', 'mpc_shift', 'mpc_si', 'mpc_sqrt', 'mpc_square', 'mpc_sub', 'mpc_sub_mpf', 'mpc_zero', 'mpf_abs', 'mpf_add', 'mpf_agm', 'mpf_agm1', 'mpf_besseljn', 'mpf_ci', 'mpf_ci_si', 'mpf_ci_si_taylor', 'mpf_cmp', 'mpf_cos', 'mpf_cos_sin', 'mpf_div', 'mpf_e1', 'mpf_ei', 'mpf_ellipe', 'mpf_ellipk', 'mpf_erf', 'mpf_erfc', 'mpf_exp', 'mpf_expint', 'mpf_gamma_int', 'mpf_gt', 'mpf_le', 'mpf_log', 'mpf_lt', 'mpf_min_max', 'mpf_mul', 'mpf_neg', 'mpf_perturb', 'mpf_pos', 'mpf_pow_int', 'mpf_rdiv_int', 'mpf_shift', 'mpf_si', 'mpf_sign', 'mpf_sin', 'mpf_sqrt', 'mpf_sub', 'negative_rnd', 'operator', 'round_fast', 'round_nearest', 'sqrt_fixed', 'to_fixed', 'to_int', 'to_rational', 'xrange']
class NoConvergence(Exception):
    pass
def complex_ei_asymptotic(zre, zim, prec):
    ...
def complex_ei_taylor(zre, zim, prec):
    ...
def ei_asymptotic(x, prec):
    ...
def ei_taylor(x, prec):
    ...
def erfc_check_series(x, prec):
    ...
def make_hyp_summator(key):
    """
    
    Returns a function that sums a generalized hypergeometric series,
    for given parameter types (integer, rational, real, complex).
    
    """
def mpc_agm(a, b, prec, rnd = 'd'):
    """
    
    Complex AGM.
    
    TODO:
    * check that convergence works as intended
    * optimize
    * select a nonarbitrary branch
    """
def mpc_agm1(a, prec, rnd = 'd'):
    ...
def mpc_besseljn(n, z, prec, rounding = 'd'):
    ...
def mpc_ci(z, prec, rnd = 'd'):
    ...
def mpc_ci_si_taylor(re, im, wp, which = 0):
    ...
def mpc_e1(x, prec, rnd = 'd'):
    ...
def mpc_ei(z, prec, rnd = 'd', e1 = False):
    ...
def mpc_ellipe(z, prec, rnd = 'd'):
    ...
def mpc_ellipk(z, prec, rnd = 'd'):
    ...
def mpc_si(z, prec, rnd = 'd'):
    ...
def mpf_agm(a, b, prec, rnd = 'd'):
    """
    
    Computes the arithmetic-geometric mean agm(a,b) for
    nonnegative mpf values a, b.
    """
def mpf_agm1(a, prec, rnd = 'd'):
    """
    
    Computes the arithmetic-geometric mean agm(1,a) for a nonnegative
    mpf value a.
    """
def mpf_besseljn(n, x, prec, rounding = 'd'):
    ...
def mpf_ci(x, prec, rnd = 'd'):
    ...
def mpf_ci_si(x, prec, rnd = 'd', which = 2):
    """
    
    Calculation of Ci(x), Si(x) for real x.
    
    which = 0 -- returns (Ci(x), -)
    which = 1 -- returns (Si(x), -)
    which = 2 -- returns (Ci(x), Si(x))
    
    Note: if x < 0, Ci(x) needs an additional imaginary term, pi*i.
    """
def mpf_ci_si_taylor(x, wp, which = 0):
    """
    
    0 - Ci(x) - (euler+log(x))
    1 - Si(x)
    """
def mpf_e1(x, prec, rnd = 'd'):
    ...
def mpf_ei(x, prec, rnd = 'd', e1 = False):
    ...
def mpf_ellipe(x, prec, rnd = 'd'):
    ...
def mpf_ellipk(x, prec, rnd = 'd'):
    ...
def mpf_erf(x, prec, rnd = 'd'):
    ...
def mpf_erfc(x, prec, rnd = 'd'):
    ...
def mpf_expint(n, x, prec, rnd = 'd', gamma = False):
    """
    
    E_n(x), n an integer, x real
    
    With gamma=True, computes Gamma(n,x)   (upper incomplete gamma function)
    
    Returns (real, None) if real, otherwise (real, imag)
    The imaginary part is an optional branch cut term
    
    """
def mpf_si(x, prec, rnd = 'd'):
    ...
BACKEND: str = 'gmpy'
MPZ_ONE: gmpy2.mpz  # value = mpz(1)
MPZ_ZERO: gmpy2.mpz  # value = mpz(0)
finf: tuple  # value = (0, mpz(0), -456, -2)
fnan: tuple  # value = (0, mpz(0), -123, -1)
fninf: tuple  # value = (1, mpz(0), -789, -3)
fnone: tuple  # value = (1, mpz(1), 0, 1)
fone: tuple  # value = (0, mpz(1), 0, 1)
ftwo: tuple  # value = (0, mpz(1), 1, 1)
fzero: tuple  # value = (0, mpz(0), 0, 0)
mpc_one: tuple  # value = ((0, mpz(1), 0, 1), (0, mpz(0), 0, 0))
mpc_zero: tuple  # value = ((0, mpz(0), 0, 0), (0, mpz(0), 0, 0))
negative_rnd: dict = {'d': 'd', 'u': 'u', 'f': 'c', 'c': 'f', 'n': 'n'}
round_fast: str = 'd'
round_nearest: str = 'n'
