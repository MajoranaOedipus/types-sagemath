"""

Low-level functions for complex arithmetic.
"""
from __future__ import annotations
import gmpy2
from gmpy2.gmpy2 import _mpmath_create as from_man_exp
from gmpy2.gmpy2 import _mpmath_normalize as normalize
from gmpy2.gmpy2 import _mpmath_normalize as normalize1
from gmpy2.gmpy2 import bit_length as bitcount
from gmpy2 import mpz as MPZ
from mpmath.libmp.libelefun import mpf_acos
from mpmath.libmp.libelefun import mpf_acosh
from mpmath.libmp.libelefun import mpf_asin
from mpmath.libmp.libelefun import mpf_atan
from mpmath.libmp.libelefun import mpf_atan2
from mpmath.libmp.libelefun import mpf_cos
from mpmath.libmp.libelefun import mpf_cos_pi
from mpmath.libmp.libelefun import mpf_cos_sin
from mpmath.libmp.libelefun import mpf_cos_sin_pi
from mpmath.libmp.libelefun import mpf_cosh
from mpmath.libmp.libelefun import mpf_cosh_sinh
from mpmath.libmp.libelefun import mpf_exp
from mpmath.libmp.libelefun import mpf_fibonacci
from mpmath.libmp.libelefun import mpf_log
from mpmath.libmp.libelefun import mpf_log_hypot
from mpmath.libmp.libelefun import mpf_nthroot
from mpmath.libmp.libelefun import mpf_sin
from mpmath.libmp.libelefun import mpf_sin_pi
from mpmath.libmp.libelefun import mpf_sinh
from mpmath.libmp.libelefun import mpf_tan
from mpmath.libmp.libelefun import mpf_tanh
from mpmath.libmp.libintmath import giant_steps
from mpmath.libmp.libintmath import lshift
from mpmath.libmp.libintmath import rshift
from mpmath.libmp.libmpf import ComplexResult
from mpmath.libmp.libmpf import from_float
from mpmath.libmp.libmpf import from_int
from mpmath.libmp.libmpf import gmpy_mpf_mul as mpf_mul
from mpmath.libmp.libmpf import gmpy_mpf_mul_int as mpf_mul_int
from mpmath.libmp.libmpf import mpf_abs
from mpmath.libmp.libmpf import mpf_add
from mpmath.libmp.libmpf import mpf_ceil
from mpmath.libmp.libmpf import mpf_div
from mpmath.libmp.libmpf import mpf_floor
from mpmath.libmp.libmpf import mpf_frac
from mpmath.libmp.libmpf import mpf_hash
from mpmath.libmp.libmpf import mpf_hypot
from mpmath.libmp.libmpf import mpf_neg
from mpmath.libmp.libmpf import mpf_nint
from mpmath.libmp.libmpf import mpf_pos
from mpmath.libmp.libmpf import mpf_pow_int
from mpmath.libmp.libmpf import mpf_rdiv_int
from mpmath.libmp.libmpf import mpf_shift
from mpmath.libmp.libmpf import mpf_sign
from mpmath.libmp.libmpf import mpf_sqrt
from mpmath.libmp.libmpf import mpf_sub
from mpmath.libmp.libmpf import to_fixed
from mpmath.libmp.libmpf import to_float
from mpmath.libmp.libmpf import to_int
from mpmath.libmp.libmpf import to_str
import sys as sys
__all__: list[str] = ['BACKEND', 'ComplexResult', 'MPZ', 'MPZ_ONE', 'MPZ_TWO', 'MPZ_ZERO', 'acos_asin', 'alpha_crossover', 'bctable', 'beta_crossover', 'bitcount', 'complex_int_pow', 'fhalf', 'finf', 'fnan', 'fninf', 'fnone', 'fone', 'from_float', 'from_int', 'from_man_exp', 'ftwo', 'fzero', 'giant_steps', 'lshift', 'mpc_abs', 'mpc_acos', 'mpc_acosh', 'mpc_add', 'mpc_add_mpf', 'mpc_arg', 'mpc_asin', 'mpc_asinh', 'mpc_atan', 'mpc_atanh', 'mpc_cbrt', 'mpc_ceil', 'mpc_conjugate', 'mpc_cos', 'mpc_cos_pi', 'mpc_cos_sin', 'mpc_cos_sin_pi', 'mpc_cosh', 'mpc_div', 'mpc_div_mpf', 'mpc_exp', 'mpc_expj', 'mpc_expjpi', 'mpc_fibonacci', 'mpc_floor', 'mpc_frac', 'mpc_half', 'mpc_hash', 'mpc_is_inf', 'mpc_is_infnan', 'mpc_is_nonzero', 'mpc_log', 'mpc_mpf_div', 'mpc_mul', 'mpc_mul_imag_mpf', 'mpc_mul_int', 'mpc_mul_mpf', 'mpc_neg', 'mpc_nint', 'mpc_nthroot', 'mpc_nthroot_fixed', 'mpc_one', 'mpc_pos', 'mpc_pow', 'mpc_pow_int', 'mpc_pow_mpf', 'mpc_reciprocal', 'mpc_shift', 'mpc_sin', 'mpc_sin_pi', 'mpc_sinh', 'mpc_sqrt', 'mpc_square', 'mpc_sub', 'mpc_sub_mpf', 'mpc_tan', 'mpc_tanh', 'mpc_to_complex', 'mpc_to_str', 'mpc_two', 'mpc_zero', 'mpf_abs', 'mpf_acos', 'mpf_acosh', 'mpf_add', 'mpf_asin', 'mpf_atan', 'mpf_atan2', 'mpf_ceil', 'mpf_cos', 'mpf_cos_pi', 'mpf_cos_sin', 'mpf_cos_sin_pi', 'mpf_cosh', 'mpf_cosh_sinh', 'mpf_div', 'mpf_exp', 'mpf_expj', 'mpf_expjpi', 'mpf_fibonacci', 'mpf_floor', 'mpf_frac', 'mpf_hash', 'mpf_hypot', 'mpf_log', 'mpf_log_hypot', 'mpf_mul', 'mpf_mul_int', 'mpf_neg', 'mpf_nint', 'mpf_nthroot', 'mpf_pos', 'mpf_pow_int', 'mpf_rdiv_int', 'mpf_shift', 'mpf_sign', 'mpf_sin', 'mpf_sin_pi', 'mpf_sinh', 'mpf_sqrt', 'mpf_sub', 'mpf_tan', 'mpf_tanh', 'negative_rnd', 'normalize', 'normalize1', 'reciprocal_rnd', 'round_ceiling', 'round_down', 'round_fast', 'round_floor', 'round_nearest', 'round_up', 'rshift', 'sys', 'to_fixed', 'to_float', 'to_int', 'to_str']
def acos_asin(z, prec, rnd, n):
    """
    complex acos for n = 0, asin for n = 1
    The algorithm is described in
    T.E. Hull, T.F. Fairgrieve and P.T.P. Tang
    'Implementing the Complex Arcsine and Arcosine Functions
    using Exception Handling',
    ACM Trans. on Math. Software Vol. 23 (1997), p299
    The complex acos and asin can be defined as
    acos(z) = acos(beta) - I*sign(a)* log(alpha + sqrt(alpha**2 -1))
    asin(z) = asin(beta) + I*sign(a)* log(alpha + sqrt(alpha**2 -1))
    where z = a + I*b
    alpha = (1/2)*(r + s); beta = (1/2)*(r - s) = a/alpha
    r = sqrt((a+1)**2 + y**2); s = sqrt((a-1)**2 + y**2)
    These expressions are rewritten in different ways in different
    regions, delimited by two crossovers alpha_crossover and beta_crossover,
    and by abs(a) <= 1, in order to improve the numerical accuracy.
    """
def complex_int_pow(a, b, n):
    """
    Complex integer power: computes (a+b*I)**n exactly for
    nonnegative n (a and b must be Python ints).
    """
def mpc_abs(z, prec, rnd = 'd'):
    """
    Absolute value of a complex number, |a+bi|.
    Returns an mpf value.
    """
def mpc_acos(z, prec, rnd = 'd'):
    ...
def mpc_acosh(z, prec, rnd = 'd'):
    ...
def mpc_add(z, w, prec, rnd = 'd'):
    ...
def mpc_add_mpf(z, x, prec, rnd = 'd'):
    ...
def mpc_arg(z, prec, rnd = 'd'):
    """
    Argument of a complex number. Returns an mpf value.
    """
def mpc_asin(z, prec, rnd = 'd'):
    ...
def mpc_asinh(z, prec, rnd = 'd'):
    ...
def mpc_atan(z, prec, rnd = 'd'):
    ...
def mpc_atanh(z, prec, rnd = 'd'):
    ...
def mpc_cbrt(z, prec, rnd = 'd'):
    """
    
    Complex cubic root.
    """
def mpc_ceil(z, prec, rnd = 'd'):
    ...
def mpc_conjugate(z, prec, rnd = 'd'):
    ...
def mpc_cos(z, prec, rnd = 'd'):
    """
    Complex cosine. The formula used is cos(a+bi) = cos(a)*cosh(b) -
    sin(a)*sinh(b)*i.
    
    The same comments apply as for the complex exp: only real
    multiplications are pewrormed, so no cancellation errors are
    possible. The formula is also efficient since we can compute both
    pairs (cos, sin) and (cosh, sinh) in single stwps.
    """
def mpc_cos_pi(z, prec, rnd = 'd'):
    ...
def mpc_cos_sin(z, prec, rnd = 'd'):
    ...
def mpc_cos_sin_pi(z, prec, rnd = 'd'):
    ...
def mpc_cosh(z, prec, rnd = 'd'):
    """
    Complex hyperbolic cosine. Computed as cosh(z) = cos(z*i).
    """
def mpc_div(z, w, prec, rnd = 'd'):
    ...
def mpc_div_mpf(z, p, prec, rnd = 'd'):
    """
    Calculate z/p where p is real
    """
def mpc_exp(z, prec, rnd = 'd'):
    """
    
    Complex exponential function.
    
    We use the direct formula exp(a+bi) = exp(a) * (cos(b) + sin(b)*i)
    for the computation. This formula is very nice because it is
    pefectly stable; since we just do real multiplications, the only
    numerical errors that can creep in are single-ulp rounding errors.
    
    The formula is efficient since mpmath's real exp is quite fast and
    since we can compute cos and sin simultaneously.
    
    It is no problem if a and b are large; if the implementations of
    exp/cos/sin are accurate and efficient for all real numbers, then
    so is this function for all complex numbers.
    """
def mpc_expj(z, prec, rnd = 'f'):
    ...
def mpc_expjpi(z, prec, rnd = 'f'):
    ...
def mpc_fibonacci(z, prec, rnd = 'd'):
    ...
def mpc_floor(z, prec, rnd = 'd'):
    ...
def mpc_frac(z, prec, rnd = 'd'):
    ...
def mpc_hash(z):
    ...
def mpc_is_inf(z):
    """
    Check if either real or imaginary part is infinite
    """
def mpc_is_infnan(z):
    """
    Check if either real or imaginary part is infinite or nan
    """
def mpc_is_nonzero(z):
    ...
def mpc_log(z, prec, rnd = 'd'):
    ...
def mpc_mpf_div(p, z, prec, rnd = 'd'):
    """
    Calculate p/z where p is real efficiently
    """
def mpc_mul(z, w, prec, rnd = 'd'):
    """
    
    Complex multiplication.
    
    Returns the real and imaginary part of (a+bi)*(c+di), rounded to
    the specified precision. The rounding mode applies to the real and
    imaginary parts separately.
    """
def mpc_mul_imag_mpf(z, x, prec, rnd = 'd'):
    """
    
    Multiply the mpc value z by I*x where x is an mpf value.
    """
def mpc_mul_int(z, n, prec, rnd = 'd'):
    ...
def mpc_mul_mpf(z, p, prec, rnd = 'd'):
    ...
def mpc_neg(z, prec = None, rnd = 'd'):
    ...
def mpc_nint(z, prec, rnd = 'd'):
    ...
def mpc_nthroot(z, n, prec, rnd = 'd'):
    """
    
    Complex n-th root.
    
    Use Newton method as in the real case when it is faster,
    otherwise use z**(1/n)
    """
def mpc_nthroot_fixed(a, b, n, prec):
    ...
def mpc_pos(z, prec, rnd = 'd'):
    ...
def mpc_pow(z, w, prec, rnd = 'd'):
    ...
def mpc_pow_int(z, n, prec, rnd = 'd'):
    ...
def mpc_pow_mpf(z, p, prec, rnd = 'd'):
    ...
def mpc_reciprocal(z, prec, rnd = 'd'):
    """
    Calculate 1/z efficiently
    """
def mpc_shift(z, n):
    ...
def mpc_sin(z, prec, rnd = 'd'):
    """
    Complex sine. We have sin(a+bi) = sin(a)*cosh(b) +
    cos(a)*sinh(b)*i. See the docstring for mpc_cos for additional
    comments.
    """
def mpc_sin_pi(z, prec, rnd = 'd'):
    ...
def mpc_sinh(z, prec, rnd = 'd'):
    """
    Complex hyperbolic sine. Computed as sinh(z) = -i*sin(z*i).
    """
def mpc_sqrt(z, prec, rnd = 'd'):
    """
    Complex square root (principal branch).
    
    We have sqrt(a+bi) = sqrt((r+a)/2) + b/sqrt(2*(r+a))*i where
    r = abs(a+bi), when a+bi is not a negative real number.
    """
def mpc_square(z, prec, rnd = 'd'):
    ...
def mpc_sub(z, w, prec = 0, rnd = 'd'):
    ...
def mpc_sub_mpf(z, p, prec = 0, rnd = 'd'):
    ...
def mpc_tan(z, prec, rnd = 'd'):
    """
    Complex tangent. Computed as tan(a+bi) = sin(2a)/M + sinh(2b)/M*i
    where M = cos(2a) + cosh(2b).
    """
def mpc_tanh(z, prec, rnd = 'd'):
    """
    Complex hyperbolic tangent. Computed as tanh(z) = -i*tan(z*i).
    """
def mpc_to_complex(z, strict = False, rnd = 'd'):
    ...
def mpc_to_str(z, dps, **kwargs):
    ...
def mpf_expj(x, prec, rnd = 'f'):
    ...
def mpf_expjpi(x, prec, rnd = 'f'):
    ...
BACKEND: str = 'gmpy'
MPZ_ONE: gmpy2.mpz  # value = mpz(1)
MPZ_TWO: gmpy2.mpz  # value = mpz(2)
MPZ_ZERO: gmpy2.mpz  # value = mpz(0)
_infs: tuple  # value = ((0, mpz(0), -456, -2), (1, mpz(0), -789, -3))
_infs_nan: tuple  # value = ((0, mpz(0), -456, -2), (1, mpz(0), -789, -3), (0, mpz(0), -123, -1))
alpha_crossover: tuple  # value = (0, mpz(3), -1, 2)
bctable: list = [0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
beta_crossover: tuple  # value = (0, mpz(5779919761767295), -53, 53)
fhalf: tuple  # value = (0, mpz(1), -1, 1)
finf: tuple  # value = (0, mpz(0), -456, -2)
fnan: tuple  # value = (0, mpz(0), -123, -1)
fninf: tuple  # value = (1, mpz(0), -789, -3)
fnone: tuple  # value = (1, mpz(1), 0, 1)
fone: tuple  # value = (0, mpz(1), 0, 1)
ftwo: tuple  # value = (0, mpz(1), 1, 1)
fzero: tuple  # value = (0, mpz(0), 0, 0)
mpc_half: tuple  # value = ((0, mpz(1), -1, 1), (0, mpz(0), 0, 0))
mpc_one: tuple  # value = ((0, mpz(1), 0, 1), (0, mpz(0), 0, 0))
mpc_two: tuple  # value = ((0, mpz(1), 1, 1), (0, mpz(0), 0, 0))
mpc_zero: tuple  # value = ((0, mpz(0), 0, 0), (0, mpz(0), 0, 0))
negative_rnd: dict = {'d': 'd', 'u': 'u', 'f': 'c', 'c': 'f', 'n': 'n'}
reciprocal_rnd: dict = {'d': 'u', 'u': 'd', 'f': 'c', 'c': 'f', 'n': 'n'}
round_ceiling: str = 'c'
round_down: str = 'd'
round_fast: str = 'd'
round_floor: str = 'f'
round_nearest: str = 'n'
round_up: str = 'u'
