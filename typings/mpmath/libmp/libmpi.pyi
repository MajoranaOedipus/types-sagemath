"""

Computational functions for interval arithmetic.

"""
from __future__ import annotations
from builtins import range as xrange
import gmpy2
from gmpy2.gmpy2 import _mpmath_create as from_man_exp
from gmpy2.gmpy2 import bit_length as bitcount
from mpmath.libmp.gammazeta import mpc_loggamma
from mpmath.libmp.gammazeta import mpf_gamma
from mpmath.libmp.gammazeta import mpf_loggamma
from mpmath.libmp.gammazeta import mpf_rgamma
from mpmath.libmp.libelefun import mod_pi2
from mpmath.libmp.libelefun import mpf_atan
from mpmath.libmp.libelefun import mpf_atan2
from mpmath.libmp.libelefun import mpf_cos_sin
from mpmath.libmp.libelefun import mpf_exp
from mpmath.libmp.libelefun import mpf_log
from mpmath.libmp.libmpf import ComplexResult
from mpmath.libmp.libmpf import dps_to_prec
from mpmath.libmp.libmpf import from_float
from mpmath.libmp.libmpf import from_int
from mpmath.libmp.libmpf import from_str
from mpmath.libmp.libmpf import gmpy_mpf_mul as mpf_mul
from mpmath.libmp.libmpf import gmpy_mpf_mul_int as mpf_mul_int
from mpmath.libmp.libmpf import mpf_abs
from mpmath.libmp.libmpf import mpf_add
from mpmath.libmp.libmpf import mpf_cmp
from mpmath.libmp.libmpf import mpf_div
from mpmath.libmp.libmpf import mpf_eq
from mpmath.libmp.libmpf import mpf_floor
from mpmath.libmp.libmpf import mpf_ge
from mpmath.libmp.libmpf import mpf_gt
from mpmath.libmp.libmpf import mpf_le
from mpmath.libmp.libmpf import mpf_lt
from mpmath.libmp.libmpf import mpf_min_max
from mpmath.libmp.libmpf import mpf_neg
from mpmath.libmp.libmpf import mpf_pos
from mpmath.libmp.libmpf import mpf_pow_int
from mpmath.libmp.libmpf import mpf_shift
from mpmath.libmp.libmpf import mpf_sign
from mpmath.libmp.libmpf import mpf_sqrt
from mpmath.libmp.libmpf import mpf_sub
from mpmath.libmp.libmpf import prec_to_dps
from mpmath.libmp.libmpf import repr_dps
from mpmath.libmp.libmpf import to_int
from mpmath.libmp.libmpf import to_str
__all__: list[str] = ['ComplexResult', 'MAX', 'MIN', 'MPZ_ONE', 'bitcount', 'cos_sin_quadrant', 'dps_to_prec', 'fhalf', 'finf', 'fnan', 'fninf', 'fnone', 'fone', 'from_float', 'from_int', 'from_man_exp', 'from_str', 'fzero', 'gamma_min', 'gamma_min_a', 'gamma_min_b', 'gamma_mono_imag_a', 'gamma_mono_imag_b', 'mod_pi2', 'mpc_loggamma', 'mpci_abs', 'mpci_add', 'mpci_arg', 'mpci_cos', 'mpci_div', 'mpci_exp', 'mpci_factorial', 'mpci_gamma', 'mpci_log', 'mpci_loggamma', 'mpci_mul', 'mpci_neg', 'mpci_pos', 'mpci_pow', 'mpci_pow_int', 'mpci_rgamma', 'mpci_sin', 'mpci_square', 'mpci_sub', 'mpf_abs', 'mpf_add', 'mpf_atan', 'mpf_atan2', 'mpf_cmp', 'mpf_cos_sin', 'mpf_div', 'mpf_eq', 'mpf_exp', 'mpf_floor', 'mpf_gamma', 'mpf_ge', 'mpf_gt', 'mpf_le', 'mpf_log', 'mpf_loggamma', 'mpf_lt', 'mpf_min_max', 'mpf_mul', 'mpf_mul_int', 'mpf_neg', 'mpf_pos', 'mpf_pow_int', 'mpf_rgamma', 'mpf_shift', 'mpf_sign', 'mpf_sqrt', 'mpf_sub', 'mpi_abs', 'mpi_add', 'mpi_atan', 'mpi_atan2', 'mpi_cos', 'mpi_cos_sin', 'mpi_cosh_sinh', 'mpi_cot', 'mpi_delta', 'mpi_div', 'mpi_div_mpf', 'mpi_eq', 'mpi_exp', 'mpi_factorial', 'mpi_from_str', 'mpi_from_str_a_b', 'mpi_gamma', 'mpi_ge', 'mpi_gt', 'mpi_le', 'mpi_log', 'mpi_loggamma', 'mpi_lt', 'mpi_mid', 'mpi_mul', 'mpi_mul_mpf', 'mpi_ne', 'mpi_neg', 'mpi_one', 'mpi_overlap', 'mpi_pi', 'mpi_pos', 'mpi_pow', 'mpi_pow_int', 'mpi_rgamma', 'mpi_shift', 'mpi_sin', 'mpi_sqrt', 'mpi_square', 'mpi_str', 'mpi_sub', 'mpi_tan', 'mpi_to_str', 'mpi_zero', 'prec_to_dps', 'repr_dps', 'round_ceiling', 'round_down', 'round_floor', 'round_nearest', 'round_up', 'to_int', 'to_str', 'xrange']
def MAX(x, y):
    ...
def MIN(x, y):
    ...
def cos_sin_quadrant(x, wp):
    ...
def mpci_abs(x, prec):
    ...
def mpci_add(x, y, prec):
    ...
def mpci_arg(z, prec):
    ...
def mpci_cos(x, prec):
    ...
def mpci_div(x, y, prec):
    ...
def mpci_exp(x, prec):
    ...
def mpci_factorial(z, prec):
    ...
def mpci_gamma(z, prec, type = 0):
    ...
def mpci_log(z, prec):
    ...
def mpci_loggamma(z, prec):
    ...
def mpci_mul(x, y, prec):
    ...
def mpci_neg(x, prec = 0):
    ...
def mpci_pos(x, prec):
    ...
def mpci_pow(x, y, prec):
    ...
def mpci_pow_int(x, n, prec):
    ...
def mpci_rgamma(z, prec):
    ...
def mpci_sin(x, prec):
    ...
def mpci_square(x, prec):
    ...
def mpci_sub(x, y, prec):
    ...
def mpi_abs(s, prec = 0):
    ...
def mpi_add(s, t, prec = 0):
    ...
def mpi_atan(s, prec):
    ...
def mpi_atan2(y, x, prec):
    ...
def mpi_cos(x, prec):
    ...
def mpi_cos_sin(x, prec):
    ...
def mpi_cosh_sinh(x, prec):
    ...
def mpi_cot(x, prec):
    ...
def mpi_delta(s, prec):
    ...
def mpi_div(s, t, prec):
    ...
def mpi_div_mpf(s, t, prec):
    ...
def mpi_eq(s, t):
    ...
def mpi_exp(s, prec):
    ...
def mpi_factorial(z, prec):
    ...
def mpi_from_str(s, prec):
    """
    
    Parse an interval number given as a string.
    
    Allowed forms are
    
    "-1.23e-27"
        Any single decimal floating-point literal.
    "a +- b"  or  "a (b)"
        a is the midpoint of the interval and b is the half-width
    "a +- b%"  or  "a (b%)"
        a is the midpoint of the interval and the half-width
        is b percent of a (`a   imes b / 100`).
    "[a, b]"
        The interval indicated directly.
    "x[y,z]e"
        x are shared digits, y and z are unequal digits, e is the exponent.
    
    """
def mpi_from_str_a_b(x, y, percent, prec):
    ...
def mpi_gamma(z, prec, type = 0):
    ...
def mpi_ge(s, t):
    ...
def mpi_gt(s, t):
    ...
def mpi_le(s, t):
    ...
def mpi_log(s, prec):
    ...
def mpi_loggamma(z, prec):
    ...
def mpi_lt(s, t):
    ...
def mpi_mid(s, prec):
    ...
def mpi_mul(s, t, prec = 0):
    ...
def mpi_mul_mpf(s, t, prec):
    ...
def mpi_ne(s, t):
    ...
def mpi_neg(s, prec = 0):
    ...
def mpi_overlap(x, y):
    ...
def mpi_pi(prec):
    ...
def mpi_pos(s, prec):
    ...
def mpi_pow(s, t, prec):
    ...
def mpi_pow_int(s, n, prec):
    ...
def mpi_rgamma(z, prec):
    ...
def mpi_shift(x, n):
    ...
def mpi_sin(x, prec):
    ...
def mpi_sqrt(s, prec):
    ...
def mpi_square(s, prec = 0):
    ...
def mpi_str(s, prec):
    ...
def mpi_sub(s, t, prec = 0):
    ...
def mpi_tan(x, prec):
    ...
def mpi_to_str(x, dps, use_spaces = True, brackets = '[]', mode = 'brackets', error_dps = 4, **kwargs):
    """
    
    Convert a mpi interval to a string.
    
    **Arguments**
    
    *dps*
        decimal places to use for printing
    *use_spaces*
        use spaces for more readable output, defaults to true
    *brackets*
        pair of strings (or two-character string) giving left and right brackets
    *mode*
        mode of display: 'plusminus', 'percent', 'brackets' (default) or 'diff'
    *error_dps*
        limit the error to *error_dps* digits (mode 'plusminus and 'percent')
    
    Additional keyword arguments are forwarded to the mpf-to-string conversion
    for the components of the output.
    
    **Examples**
    
        >>> from mpmath import mpi, mp
        >>> mp.dps = 30
        >>> x = mpi(1, 2)._mpi_
        >>> mpi_to_str(x, 2, mode='plusminus')
        '1.5 +- 0.5'
        >>> mpi_to_str(x, 2, mode='percent')
        '1.5 (33.33%)'
        >>> mpi_to_str(x, 2, mode='brackets')
        '[1.0, 2.0]'
        >>> mpi_to_str(x, 2, mode='brackets' , brackets=('<', '>'))
        '<1.0, 2.0>'
        >>> x = mpi('5.2582327113062393041', '5.2582327113062749951')._mpi_
        >>> mpi_to_str(x, 15, mode='diff')
        '5.2582327113062[4, 7]'
        >>> mpi_to_str(mpi(0)._mpi_, 2, mode='percent')
        '0.0 (0.0%)'
    
    """
MPZ_ONE: gmpy2.mpz  # value = mpz(1)
fhalf: tuple  # value = (0, mpz(1), -1, 1)
finf: tuple  # value = (0, mpz(0), -456, -2)
fnan: tuple  # value = (0, mpz(0), -123, -1)
fninf: tuple  # value = (1, mpz(0), -789, -3)
fnone: tuple  # value = (1, mpz(1), 0, 1)
fone: tuple  # value = (0, mpz(1), 0, 1)
fzero: tuple  # value = (0, mpz(0), 0, 0)
gamma_min: tuple  # value = ((0, mpz(6582605983394595), -52, 53), (0, mpz(6582605983439631), -52, 53))
gamma_min_a: tuple  # value = (0, mpz(6582605983394595), -52, 53)
gamma_min_b: tuple  # value = (0, mpz(6582605983439631), -52, 53)
gamma_mono_imag_a: tuple  # value = (1, mpz(2476979795053773), -51, 52)
gamma_mono_imag_b: tuple  # value = (0, mpz(2476979795053773), -51, 52)
mpi_one: tuple  # value = ((0, mpz(1), 0, 1), (0, mpz(1), 0, 1))
mpi_zero: tuple  # value = ((0, mpz(0), 0, 0), (0, mpz(0), 0, 0))
round_ceiling: str = 'c'
round_down: str = 'd'
round_floor: str = 'f'
round_nearest: str = 'n'
round_up: str = 'u'
