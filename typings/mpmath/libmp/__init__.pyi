from __future__ import annotations
import gmpy2
import gmpy2 as gmpy
from gmpy2.gmpy2 import _mpmath_create as from_man_exp
from gmpy2.gmpy2 import _mpmath_normalize as normalize1
from gmpy2.gmpy2 import _mpmath_normalize as normalize
from gmpy2.gmpy2 import bit_length as bitcount
from gmpy2.gmpy2 import fac as ifac
from gmpy2.gmpy2 import isqrt as isqrt_fast
from gmpy2.gmpy2 import isqrt as isqrt_small
from gmpy2.gmpy2 import isqrt
from gmpy2.gmpy2 import isqrt_rem as sqrtrem
from gmpy2 import mpz as MPZ_TYPE
from gmpy2 import mpz as MPZ
from mpmath.libmp.gammazeta import bernfrac
from mpmath.libmp.gammazeta import mpc_altzeta
from mpmath.libmp.gammazeta import mpc_factorial
from mpmath.libmp.gammazeta import mpc_gamma
from mpmath.libmp.gammazeta import mpc_harmonic
from mpmath.libmp.gammazeta import mpc_loggamma
from mpmath.libmp.gammazeta import mpc_psi
from mpmath.libmp.gammazeta import mpc_psi0
from mpmath.libmp.gammazeta import mpc_rgamma
from mpmath.libmp.gammazeta import mpc_zeta
from mpmath.libmp.gammazeta import mpc_zetasum
from mpmath.libmp.gammazeta import mpf_altzeta
from mpmath.libmp.gammazeta import mpf_bernoulli
from mpmath.libmp.gammazeta import mpf_factorial
from mpmath.libmp.gammazeta import mpf_gamma
from mpmath.libmp.gammazeta import mpf_gamma_int
from mpmath.libmp.gammazeta import mpf_harmonic
from mpmath.libmp.gammazeta import mpf_loggamma
from mpmath.libmp.gammazeta import mpf_psi
from mpmath.libmp.gammazeta import mpf_psi0
from mpmath.libmp.gammazeta import mpf_rgamma
from mpmath.libmp.gammazeta import mpf_zeta
from mpmath.libmp.gammazeta import mpf_zeta_int
from mpmath.libmp.libelefun import agm_fixed
from mpmath.libmp.libelefun import degree_fixed
from mpmath.libmp.libelefun import log_int_fixed
from mpmath.libmp.libelefun import mpf_acos
from mpmath.libmp.libelefun import mpf_acosh
from mpmath.libmp.libelefun import mpf_asin
from mpmath.libmp.libelefun import mpf_asinh
from mpmath.libmp.libelefun import mpf_atan
from mpmath.libmp.libelefun import mpf_atan2
from mpmath.libmp.libelefun import mpf_atanh
from mpmath.libmp.libelefun import mpf_cbrt
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
from mpmath.libmp.libelefun import mpf_pow
from mpmath.libmp.libelefun import mpf_sin
from mpmath.libmp.libelefun import mpf_sin_pi
from mpmath.libmp.libelefun import mpf_sinh
from mpmath.libmp.libelefun import mpf_tan
from mpmath.libmp.libelefun import mpf_tanh
from mpmath.libmp.libhyper import NoConvergence
from mpmath.libmp.libhyper import make_hyp_summator
from mpmath.libmp.libhyper import mpc_agm
from mpmath.libmp.libhyper import mpc_agm1
from mpmath.libmp.libhyper import mpc_besseljn
from mpmath.libmp.libhyper import mpc_ci
from mpmath.libmp.libhyper import mpc_e1
from mpmath.libmp.libhyper import mpc_ei
from mpmath.libmp.libhyper import mpc_ellipe
from mpmath.libmp.libhyper import mpc_ellipk
from mpmath.libmp.libhyper import mpc_si
from mpmath.libmp.libhyper import mpf_agm
from mpmath.libmp.libhyper import mpf_agm1
from mpmath.libmp.libhyper import mpf_besseljn
from mpmath.libmp.libhyper import mpf_ci
from mpmath.libmp.libhyper import mpf_ci_si
from mpmath.libmp.libhyper import mpf_e1
from mpmath.libmp.libhyper import mpf_ei
from mpmath.libmp.libhyper import mpf_ellipe
from mpmath.libmp.libhyper import mpf_ellipk
from mpmath.libmp.libhyper import mpf_erf
from mpmath.libmp.libhyper import mpf_erfc
from mpmath.libmp.libhyper import mpf_expint
from mpmath.libmp.libhyper import mpf_si
from mpmath.libmp.libintmath import bin_to_radix
from mpmath.libmp.libintmath import eulernum
from mpmath.libmp.libintmath import gcd
from mpmath.libmp.libintmath import gmpy_trailing as trailing
from mpmath.libmp.libintmath import ifib
from mpmath.libmp.libintmath import isprime
from mpmath.libmp.libintmath import list_primes
from mpmath.libmp.libintmath import moebius
from mpmath.libmp.libintmath import numeral_gmpy as numeral
from mpmath.libmp.libintmath import sqrt_fixed
from mpmath.libmp.libintmath import stirling1
from mpmath.libmp.libintmath import stirling2
from mpmath.libmp.libmpc import complex_int_pow
from mpmath.libmp.libmpc import mpc_abs
from mpmath.libmp.libmpc import mpc_acos
from mpmath.libmp.libmpc import mpc_acosh
from mpmath.libmp.libmpc import mpc_add
from mpmath.libmp.libmpc import mpc_add_mpf
from mpmath.libmp.libmpc import mpc_arg
from mpmath.libmp.libmpc import mpc_asin
from mpmath.libmp.libmpc import mpc_asinh
from mpmath.libmp.libmpc import mpc_atan
from mpmath.libmp.libmpc import mpc_atanh
from mpmath.libmp.libmpc import mpc_cbrt
from mpmath.libmp.libmpc import mpc_ceil
from mpmath.libmp.libmpc import mpc_conjugate
from mpmath.libmp.libmpc import mpc_cos
from mpmath.libmp.libmpc import mpc_cos_pi
from mpmath.libmp.libmpc import mpc_cos_sin
from mpmath.libmp.libmpc import mpc_cos_sin_pi
from mpmath.libmp.libmpc import mpc_cosh
from mpmath.libmp.libmpc import mpc_div
from mpmath.libmp.libmpc import mpc_div_mpf
from mpmath.libmp.libmpc import mpc_exp
from mpmath.libmp.libmpc import mpc_expj
from mpmath.libmp.libmpc import mpc_expjpi
from mpmath.libmp.libmpc import mpc_fibonacci
from mpmath.libmp.libmpc import mpc_floor
from mpmath.libmp.libmpc import mpc_frac
from mpmath.libmp.libmpc import mpc_hash
from mpmath.libmp.libmpc import mpc_is_inf
from mpmath.libmp.libmpc import mpc_is_infnan
from mpmath.libmp.libmpc import mpc_is_nonzero
from mpmath.libmp.libmpc import mpc_log
from mpmath.libmp.libmpc import mpc_mpf_div
from mpmath.libmp.libmpc import mpc_mul
from mpmath.libmp.libmpc import mpc_mul_imag_mpf
from mpmath.libmp.libmpc import mpc_mul_int
from mpmath.libmp.libmpc import mpc_mul_mpf
from mpmath.libmp.libmpc import mpc_neg
from mpmath.libmp.libmpc import mpc_nint
from mpmath.libmp.libmpc import mpc_nthroot
from mpmath.libmp.libmpc import mpc_pos
from mpmath.libmp.libmpc import mpc_pow
from mpmath.libmp.libmpc import mpc_pow_int
from mpmath.libmp.libmpc import mpc_pow_mpf
from mpmath.libmp.libmpc import mpc_reciprocal
from mpmath.libmp.libmpc import mpc_shift
from mpmath.libmp.libmpc import mpc_sin
from mpmath.libmp.libmpc import mpc_sin_pi
from mpmath.libmp.libmpc import mpc_sinh
from mpmath.libmp.libmpc import mpc_sqrt
from mpmath.libmp.libmpc import mpc_square
from mpmath.libmp.libmpc import mpc_sub
from mpmath.libmp.libmpc import mpc_sub_mpf
from mpmath.libmp.libmpc import mpc_tan
from mpmath.libmp.libmpc import mpc_tanh
from mpmath.libmp.libmpc import mpc_to_complex
from mpmath.libmp.libmpc import mpc_to_str
from mpmath.libmp.libmpc import mpf_expj
from mpmath.libmp.libmpc import mpf_expjpi
from mpmath.libmp.libmpf import ComplexResult
from mpmath.libmp.libmpf import dps_to_prec
from mpmath.libmp.libmpf import from_Decimal
from mpmath.libmp.libmpf import from_bstr
from mpmath.libmp.libmpf import from_float
from mpmath.libmp.libmpf import from_int
from mpmath.libmp.libmpf import from_npfloat
from mpmath.libmp.libmpf import from_pickable
from mpmath.libmp.libmpf import from_rational
from mpmath.libmp.libmpf import from_str
from mpmath.libmp.libmpf import gmpy_mpf_mul as mpf_mul
from mpmath.libmp.libmpf import gmpy_mpf_mul_int as mpf_mul_int
from mpmath.libmp.libmpf import mpf_abs
from mpmath.libmp.libmpf import mpf_add
from mpmath.libmp.libmpf import mpf_ceil
from mpmath.libmp.libmpf import mpf_cmp
from mpmath.libmp.libmpf import mpf_div
from mpmath.libmp.libmpf import mpf_eq
from mpmath.libmp.libmpf import mpf_floor
from mpmath.libmp.libmpf import mpf_frac
from mpmath.libmp.libmpf import mpf_frexp
from mpmath.libmp.libmpf import mpf_ge
from mpmath.libmp.libmpf import mpf_gt
from mpmath.libmp.libmpf import mpf_hash
from mpmath.libmp.libmpf import mpf_hypot
from mpmath.libmp.libmpf import mpf_le
from mpmath.libmp.libmpf import mpf_lt
from mpmath.libmp.libmpf import mpf_mod
from mpmath.libmp.libmpf import mpf_neg
from mpmath.libmp.libmpf import mpf_nint
from mpmath.libmp.libmpf import mpf_perturb
from mpmath.libmp.libmpf import mpf_pos
from mpmath.libmp.libmpf import mpf_pow_int
from mpmath.libmp.libmpf import mpf_rand
from mpmath.libmp.libmpf import mpf_rdiv_int
from mpmath.libmp.libmpf import mpf_shift
from mpmath.libmp.libmpf import mpf_sign
from mpmath.libmp.libmpf import mpf_sqrt
from mpmath.libmp.libmpf import mpf_sub
from mpmath.libmp.libmpf import mpf_sum
from mpmath.libmp.libmpf import prec_to_dps
from mpmath.libmp.libmpf import repr_dps
from mpmath.libmp.libmpf import round_int
from mpmath.libmp.libmpf import str_to_man_exp
from mpmath.libmp.libmpf import to_bstr
from mpmath.libmp.libmpf import to_digits_exp
from mpmath.libmp.libmpf import to_fixed
from mpmath.libmp.libmpf import to_float
from mpmath.libmp.libmpf import to_int
from mpmath.libmp.libmpf import to_man_exp
from mpmath.libmp.libmpf import to_pickable
from mpmath.libmp.libmpf import to_rational
from mpmath.libmp.libmpf import to_str
from mpmath.libmp.libmpi import mpci_abs
from mpmath.libmp.libmpi import mpci_add
from mpmath.libmp.libmpi import mpci_cos
from mpmath.libmp.libmpi import mpci_div
from mpmath.libmp.libmpi import mpci_exp
from mpmath.libmp.libmpi import mpci_factorial
from mpmath.libmp.libmpi import mpci_gamma
from mpmath.libmp.libmpi import mpci_log
from mpmath.libmp.libmpi import mpci_loggamma
from mpmath.libmp.libmpi import mpci_mul
from mpmath.libmp.libmpi import mpci_neg
from mpmath.libmp.libmpi import mpci_pos
from mpmath.libmp.libmpi import mpci_pow
from mpmath.libmp.libmpi import mpci_rgamma
from mpmath.libmp.libmpi import mpci_sin
from mpmath.libmp.libmpi import mpci_sub
from mpmath.libmp.libmpi import mpi_abs
from mpmath.libmp.libmpi import mpi_add
from mpmath.libmp.libmpi import mpi_atan
from mpmath.libmp.libmpi import mpi_atan2
from mpmath.libmp.libmpi import mpi_cos
from mpmath.libmp.libmpi import mpi_cos_sin
from mpmath.libmp.libmpi import mpi_cot
from mpmath.libmp.libmpi import mpi_delta
from mpmath.libmp.libmpi import mpi_div
from mpmath.libmp.libmpi import mpi_eq
from mpmath.libmp.libmpi import mpi_exp
from mpmath.libmp.libmpi import mpi_factorial
from mpmath.libmp.libmpi import mpi_from_str
from mpmath.libmp.libmpi import mpi_gamma
from mpmath.libmp.libmpi import mpi_ge
from mpmath.libmp.libmpi import mpi_gt
from mpmath.libmp.libmpi import mpi_le
from mpmath.libmp.libmpi import mpi_log
from mpmath.libmp.libmpi import mpi_loggamma
from mpmath.libmp.libmpi import mpi_lt
from mpmath.libmp.libmpi import mpi_mid
from mpmath.libmp.libmpi import mpi_mul
from mpmath.libmp.libmpi import mpi_ne
from mpmath.libmp.libmpi import mpi_neg
from mpmath.libmp.libmpi import mpi_pos
from mpmath.libmp.libmpi import mpi_pow
from mpmath.libmp.libmpi import mpi_pow_int
from mpmath.libmp.libmpi import mpi_rgamma
from mpmath.libmp.libmpi import mpi_sin
from mpmath.libmp.libmpi import mpi_sqrt
from mpmath.libmp.libmpi import mpi_str
from mpmath.libmp.libmpi import mpi_sub
from mpmath.libmp.libmpi import mpi_tan
from mpmath.libmp.libmpi import mpi_to_str
from . import backend
from . import gammazeta
from . import libelefun
from . import libhyper
from . import libintmath
from . import libmpc
from . import libmpf
from . import libmpi
__all__: list[str] = ['BACKEND', 'ComplexResult', 'HASH_BITS', 'HASH_MODULUS', 'MPZ', 'MPZ_FIVE', 'MPZ_ONE', 'MPZ_THREE', 'MPZ_TWO', 'MPZ_TYPE', 'MPZ_ZERO', 'NoConvergence', 'STRICT', 'agm_fixed', 'backend', 'bernfrac', 'bin_to_radix', 'bitcount', 'complex_int_pow', 'degree_fixed', 'dps_to_prec', 'eulernum', 'fhalf', 'finf', 'fnan', 'fninf', 'fnone', 'fnzero', 'fone', 'from_Decimal', 'from_bstr', 'from_float', 'from_int', 'from_man_exp', 'from_npfloat', 'from_pickable', 'from_rational', 'from_str', 'ften', 'ftwo', 'fzero', 'gammazeta', 'gcd', 'gmpy', 'ifac', 'ifib', 'int_types', 'isprime', 'isqrt', 'isqrt_fast', 'isqrt_small', 'libelefun', 'libhyper', 'libintmath', 'libmpc', 'libmpf', 'libmpi', 'list_primes', 'log_int_fixed', 'make_hyp_summator', 'math_float_inf', 'moebius', 'mpc_abs', 'mpc_acos', 'mpc_acosh', 'mpc_add', 'mpc_add_mpf', 'mpc_agm', 'mpc_agm1', 'mpc_altzeta', 'mpc_arg', 'mpc_asin', 'mpc_asinh', 'mpc_atan', 'mpc_atanh', 'mpc_besseljn', 'mpc_cbrt', 'mpc_ceil', 'mpc_ci', 'mpc_conjugate', 'mpc_cos', 'mpc_cos_pi', 'mpc_cos_sin', 'mpc_cos_sin_pi', 'mpc_cosh', 'mpc_div', 'mpc_div_mpf', 'mpc_e1', 'mpc_ei', 'mpc_ellipe', 'mpc_ellipk', 'mpc_exp', 'mpc_expj', 'mpc_expjpi', 'mpc_factorial', 'mpc_fibonacci', 'mpc_floor', 'mpc_frac', 'mpc_gamma', 'mpc_half', 'mpc_harmonic', 'mpc_hash', 'mpc_is_inf', 'mpc_is_infnan', 'mpc_is_nonzero', 'mpc_log', 'mpc_loggamma', 'mpc_mpf_div', 'mpc_mul', 'mpc_mul_imag_mpf', 'mpc_mul_int', 'mpc_mul_mpf', 'mpc_neg', 'mpc_nint', 'mpc_nthroot', 'mpc_one', 'mpc_pos', 'mpc_pow', 'mpc_pow_int', 'mpc_pow_mpf', 'mpc_psi', 'mpc_psi0', 'mpc_reciprocal', 'mpc_rgamma', 'mpc_shift', 'mpc_si', 'mpc_sin', 'mpc_sin_pi', 'mpc_sinh', 'mpc_sqrt', 'mpc_square', 'mpc_sub', 'mpc_sub_mpf', 'mpc_tan', 'mpc_tanh', 'mpc_to_complex', 'mpc_to_str', 'mpc_two', 'mpc_zero', 'mpc_zeta', 'mpc_zetasum', 'mpci_abs', 'mpci_add', 'mpci_cos', 'mpci_div', 'mpci_exp', 'mpci_factorial', 'mpci_gamma', 'mpci_log', 'mpci_loggamma', 'mpci_mul', 'mpci_neg', 'mpci_pos', 'mpci_pow', 'mpci_rgamma', 'mpci_sin', 'mpci_sub', 'mpf_abs', 'mpf_acos', 'mpf_acosh', 'mpf_add', 'mpf_agm', 'mpf_agm1', 'mpf_altzeta', 'mpf_asin', 'mpf_asinh', 'mpf_atan', 'mpf_atan2', 'mpf_atanh', 'mpf_bernoulli', 'mpf_besseljn', 'mpf_cbrt', 'mpf_ceil', 'mpf_ci', 'mpf_ci_si', 'mpf_cmp', 'mpf_cos', 'mpf_cos_pi', 'mpf_cos_sin', 'mpf_cos_sin_pi', 'mpf_cosh', 'mpf_cosh_sinh', 'mpf_div', 'mpf_e1', 'mpf_ei', 'mpf_ellipe', 'mpf_ellipk', 'mpf_eq', 'mpf_erf', 'mpf_erfc', 'mpf_exp', 'mpf_expint', 'mpf_expj', 'mpf_expjpi', 'mpf_factorial', 'mpf_fibonacci', 'mpf_floor', 'mpf_frac', 'mpf_frexp', 'mpf_gamma', 'mpf_gamma_int', 'mpf_ge', 'mpf_gt', 'mpf_harmonic', 'mpf_hash', 'mpf_hypot', 'mpf_le', 'mpf_log', 'mpf_log_hypot', 'mpf_loggamma', 'mpf_lt', 'mpf_mod', 'mpf_mul', 'mpf_mul_int', 'mpf_neg', 'mpf_nint', 'mpf_nthroot', 'mpf_perturb', 'mpf_pos', 'mpf_pow', 'mpf_pow_int', 'mpf_psi', 'mpf_psi0', 'mpf_rand', 'mpf_rdiv_int', 'mpf_rgamma', 'mpf_shift', 'mpf_si', 'mpf_sign', 'mpf_sin', 'mpf_sin_pi', 'mpf_sinh', 'mpf_sqrt', 'mpf_sub', 'mpf_sum', 'mpf_tan', 'mpf_tanh', 'mpf_zeta', 'mpf_zeta_int', 'mpf_zetasum', 'mpi_abs', 'mpi_add', 'mpi_atan', 'mpi_atan2', 'mpi_cos', 'mpi_cos_sin', 'mpi_cot', 'mpi_delta', 'mpi_div', 'mpi_eq', 'mpi_exp', 'mpi_factorial', 'mpi_from_str', 'mpi_gamma', 'mpi_ge', 'mpi_gt', 'mpi_le', 'mpi_log', 'mpi_loggamma', 'mpi_lt', 'mpi_mid', 'mpi_mul', 'mpi_ne', 'mpi_neg', 'mpi_pos', 'mpi_pow', 'mpi_pow_int', 'mpi_rgamma', 'mpi_sin', 'mpi_sqrt', 'mpi_str', 'mpi_sub', 'mpi_tan', 'mpi_to_str', 'normalize', 'normalize1', 'numeral', 'prec_to_dps', 'repr_dps', 'round_ceiling', 'round_down', 'round_floor', 'round_int', 'round_nearest', 'round_up', 'sage', 'sqrt_fixed', 'sqrtrem', 'stirling1', 'stirling2', 'str_to_man_exp', 'to_bstr', 'to_digits_exp', 'to_fixed', 'to_float', 'to_int', 'to_man_exp', 'to_pickable', 'to_rational', 'to_str', 'trailing']
BACKEND: str = 'gmpy'
HASH_BITS: int = 61
HASH_MODULUS: int = 2305843009213693951
MPZ_FIVE: gmpy2.mpz  # value = mpz(5)
MPZ_ONE: gmpy2.mpz  # value = mpz(1)
MPZ_THREE: gmpy2.mpz  # value = mpz(3)
MPZ_TWO: gmpy2.mpz  # value = mpz(2)
MPZ_ZERO: gmpy2.mpz  # value = mpz(0)
STRICT: bool = False
fhalf: tuple  # value = (0, mpz(1), -1, 1)
finf: tuple  # value = (0, mpz(0), -456, -2)
fnan: tuple  # value = (0, mpz(0), -123, -1)
fninf: tuple  # value = (1, mpz(0), -789, -3)
fnone: tuple  # value = (1, mpz(1), 0, 1)
fnzero: tuple  # value = (1, mpz(0), 0, 0)
fone: tuple  # value = (0, mpz(1), 0, 1)
ften: tuple  # value = (0, mpz(5), 1, 3)
ftwo: tuple  # value = (0, mpz(1), 1, 1)
fzero: tuple  # value = (0, mpz(0), 0, 0)
int_types: tuple = (int, gmpy2.mpz)
math_float_inf: float  # value = inf
mpc_half: tuple  # value = ((0, mpz(1), -1, 1), (0, mpz(0), 0, 0))
mpc_one: tuple  # value = ((0, mpz(1), 0, 1), (0, mpz(0), 0, 0))
mpc_two: tuple  # value = ((0, mpz(1), 1, 1), (0, mpz(0), 0, 0))
mpc_zero: tuple  # value = ((0, mpz(0), 0, 0), (0, mpz(0), 0, 0))
mpf_zetasum = None
round_ceiling: str = 'c'
round_down: str = 'd'
round_floor: str = 'f'
round_nearest: str = 'n'
round_up: str = 'u'
sage = None
