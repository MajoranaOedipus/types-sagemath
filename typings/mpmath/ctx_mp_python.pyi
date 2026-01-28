from __future__ import annotations
from builtins import exec as exec_
from builtins import str as basestring
import gmpy2
from gmpy2.gmpy2 import _mpmath_create as from_man_exp
from gmpy2.gmpy2 import _mpmath_normalize as normalize
from gmpy2.gmpy2 import bit_length as bitcount
from gmpy2 import mpz as MPZ
import mpmath.ctx_mp
from mpmath import function_docs
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
from mpmath.libmp.libmpf import from_Decimal
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
import numbers as numbers
import typing
__all__: list[str] = ['ComplexResult', 'MPZ', 'MPZ_ONE', 'MPZ_ZERO', 'PythonMPContext', 'basestring', 'binary_op', 'bitcount', 'complex_types', 'dps_to_prec', 'exec_', 'finf', 'fnan', 'fninf', 'fone', 'from_Decimal', 'from_float', 'from_int', 'from_man_exp', 'from_npfloat', 'from_pickable', 'from_rational', 'from_str', 'function_docs', 'fzero', 'int_types', 'mpc', 'mpc_abs', 'mpc_add', 'mpc_add_mpf', 'mpc_conjugate', 'mpc_div', 'mpc_div_mpf', 'mpc_hash', 'mpc_is_nonzero', 'mpc_mpf_div', 'mpc_mul', 'mpc_mul_int', 'mpc_mul_mpf', 'mpc_neg', 'mpc_pos', 'mpc_pow', 'mpc_pow_int', 'mpc_pow_mpf', 'mpc_sub', 'mpc_sub_mpf', 'mpc_to_complex', 'mpc_to_str', 'mpf', 'mpf_abs', 'mpf_add', 'mpf_binary_op', 'mpf_cmp', 'mpf_div', 'mpf_eq', 'mpf_ge', 'mpf_gt', 'mpf_hash', 'mpf_le', 'mpf_lt', 'mpf_mod', 'mpf_mul', 'mpf_mul_int', 'mpf_neg', 'mpf_pos', 'mpf_pow', 'mpf_pow_int', 'mpf_pow_same', 'mpf_rand', 'mpf_rdiv_int', 'mpf_sub', 'mpf_sum', 'mpnumeric', 'normalize', 'numbers', 'prec_to_dps', 'rational', 'repr_dps', 'return_mpc', 'return_mpf', 'round_ceiling', 'round_floor', 'round_nearest', 'to_fixed', 'to_float', 'to_int', 'to_pickable', 'to_str']
class PythonMPContext:
    dps = ...
    prec = ...
    @staticmethod
    def __init__(ctx):
        ...
    @staticmethod
    def _convert_param(ctx, x):
        ...
    @staticmethod
    def _mpf_mag(ctx, x):
        ...
    @staticmethod
    def _set_dps(ctx, n):
        ...
    @staticmethod
    def _set_prec(ctx, n):
        ...
    @staticmethod
    def _wrap_libmp_function(ctx, mpf_f, mpc_f = None, mpi_f = None, doc = '<no doc>'):
        """
        
        Given a low-level mpf_ function, and optionally similar functions
        for mpc_ and mpi_, defines the function as a context method.
        
        It is assumed that the return type is the same as that of
        the input; the exception is that propagation from mpf to mpc is possible
        by raising ComplexResult.
        
        """
    @staticmethod
    def convert(ctx, x, strings = True):
        """
        
        Converts *x* to an ``mpf`` or ``mpc``. If *x* is of type ``mpf``,
        ``mpc``, ``int``, ``float``, ``complex``, the conversion
        will be performed losslessly.
        
        If *x* is a string, the result will be rounded to the present
        working precision. Strings representing fractions or complex
        numbers are permitted.
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> mpmathify(3.5)
            mpf('3.5')
            >>> mpmathify('2.1')
            mpf('2.1000000000000001')
            >>> mpmathify('3/4')
            mpf('0.75')
            >>> mpmathify('2+3j')
            mpc(real='2.0', imag='3.0')
        
        """
    @staticmethod
    def default(ctx):
        ...
    @staticmethod
    def fdot(ctx, A, B = None, conjugate = False):
        """
        
        Computes the dot product of the iterables `A` and `B`,
        
        .. math ::
        
            \\sum_{k=0} A_k B_k.
        
        Alternatively, :func:`~mpmath.fdot` accepts a single iterable of pairs.
        In other words, ``fdot(A,B)`` and ``fdot(zip(A,B))`` are equivalent.
        The elements are automatically converted to mpmath numbers.
        
        With ``conjugate=True``, the elements in the second vector
        will be conjugated:
        
        .. math ::
        
            \\sum_{k=0} A_k \\overline{B_k}
        
        **Examples**
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> A = [2, 1.5, 3]
            >>> B = [1, -1, 2]
            >>> fdot(A, B)
            mpf('6.5')
            >>> list(zip(A, B))
            [(2, 1), (1.5, -1), (3, 2)]
            >>> fdot(_)
            mpf('6.5')
            >>> A = [2, 1.5, 3j]
            >>> B = [1+j, 3, -1-j]
            >>> fdot(A, B)
            mpc(real='9.5', imag='-1.0')
            >>> fdot(A, B, conjugate=True)
            mpc(real='3.5', imag='-5.0')
        
        """
    @staticmethod
    def fsum(ctx, terms, absolute = False, squared = False):
        """
        
        Calculates a sum containing a finite number of terms (for infinite
        series, see :func:`~mpmath.nsum`). The terms will be converted to
        mpmath numbers. For len(terms) > 2, this function is generally
        faster and produces more accurate results than the builtin
        Python function :func:`sum`.
        
            >>> from mpmath import *
            >>> mp.dps = 15; mp.pretty = False
            >>> fsum([1, 2, 0.5, 7])
            mpf('10.5')
        
        With squared=True each term is squared, and with absolute=True
        the absolute value of each term is used.
        """
    @staticmethod
    def isinf(ctx, x):
        """
        
        Return *True* if the absolute value of *x* is infinite;
        otherwise return *False*::
        
            >>> from mpmath import *
            >>> isinf(inf)
            True
            >>> isinf(-inf)
            True
            >>> isinf(3)
            False
            >>> isinf(3+4j)
            False
            >>> isinf(mpc(3,inf))
            True
            >>> isinf(mpc(inf,3))
            True
        
        """
    @staticmethod
    def isint(ctx, x, gaussian = False):
        """
        
        Return *True* if *x* is integer-valued; otherwise return
        *False*::
        
            >>> from mpmath import *
            >>> isint(3)
            True
            >>> isint(mpf(3))
            True
            >>> isint(3.2)
            False
            >>> isint(inf)
            False
        
        Optionally, Gaussian integers can be checked for::
        
            >>> isint(3+0j)
            True
            >>> isint(3+2j)
            False
            >>> isint(3+2j, gaussian=True)
            True
        
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
    def isnormal(ctx, x):
        """
        
        Determine whether *x* is "normal" in the sense of floating-point
        representation; that is, return *False* if *x* is zero, an
        infinity or NaN; otherwise return *True*. By extension, a
        complex number *x* is considered "normal" if its magnitude is
        normal::
        
            >>> from mpmath import *
            >>> isnormal(3)
            True
            >>> isnormal(0)
            False
            >>> isnormal(inf); isnormal(-inf); isnormal(nan)
            False
            False
            False
            >>> isnormal(0+0j)
            False
            >>> isnormal(0+3j)
            True
            >>> isnormal(mpc(2,nan))
            False
        """
    @staticmethod
    def mag(ctx, x):
        """
        
        Quick logarithmic magnitude estimate of a number. Returns an
        integer or infinity `m` such that `|x| <= 2^m`. It is not
        guaranteed that `m` is an optimal bound, but it will never
        be too large by more than 2 (and probably not more than 1).
        
        **Examples**
        
            >>> from mpmath import *
            >>> mp.pretty = True
            >>> mag(10), mag(10.0), mag(mpf(10)), int(ceil(log(10,2)))
            (4, 4, 4, 4)
            >>> mag(10j), mag(10+10j)
            (4, 5)
            >>> mag(0.01), int(ceil(log(0.01,2)))
            (-6, -6)
            >>> mag(0), mag(inf), mag(-inf), mag(nan)
            (-inf, +inf, +inf, nan)
        
        """
    @staticmethod
    def make_mpc(ctx, v):
        ...
    @staticmethod
    def make_mpf(ctx, v):
        ...
    @staticmethod
    def npconvert(ctx, x):
        """
        
        Converts *x* to an ``mpf`` or ``mpc``. *x* should be a numpy
        scalar.
        """
    @classmethod
    def _wrap_specfun(cls, name, f, wrap):
        ...
class _constant(_mpf):
    """
    Represents a mathematical constant with dynamic precision.
    When printed or used in an arithmetic operation, a constant
    is converted to a regular mpf at the working precision. A
    regular mpf can also be obtained using the operation +x.
    """
    @classmethod
    def __new__(cls, func, name, docname = ''):
        ...
    def __call__(self, prec = None, dps = None, rounding = None):
        ...
    def __repr__(self):
        ...
    @property
    def _mpf_(self):
        ...
class _mpc(mpnumeric):
    """
    
    An mpc represents a complex number using a pair of mpf:s (one
    for the real part and another for the imaginary part.) The mpc
    class behaves fairly similarly to Python's complex type.
    """
    __slots__: typing.ClassVar[list] = ['_mpc_']
    @staticmethod
    def __abs__(s):
        ...
    @staticmethod
    def __add__(s, t):
        ...
    @staticmethod
    def __bool__(s):
        ...
    @staticmethod
    def __complex__(s):
        ...
    @staticmethod
    def __div__(s, t):
        ...
    @staticmethod
    def __eq__(s, t):
        ...
    @staticmethod
    def __ge__(*args):
        ...
    @staticmethod
    def __gt__(*args):
        ...
    @staticmethod
    def __hash__(s):
        ...
    @staticmethod
    def __le__(*args):
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
    def __nonzero__(s):
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
    def _compare(*args):
        ...
    @staticmethod
    def ae(s, t, rel_eps = None, abs_eps = None):
        ...
    @staticmethod
    def conjugate(s):
        ...
    @classmethod
    def __new__(cls, real = 0, imag = 0):
        ...
    @classmethod
    def mpc_convert_lhs(cls, x):
        ...
    def __getstate__(self):
        ...
    def __setstate__(self, val):
        ...
    @property
    def imag(self):
        ...
    @property
    def real(self):
        ...
class _mpf(mpnumeric):
    """
    
    An mpf instance holds a real-valued floating-point number. mpf:s
    work analogously to Python floats, but support arbitrary-precision
    arithmetic.
    """
    __slots__: typing.ClassVar[list] = ['_mpf_']
    @staticmethod
    def __abs__(s):
        ...
    @staticmethod
    def __bool__(s):
        ...
    @staticmethod
    def __cmp__(s, t):
        ...
    @staticmethod
    def __complex__(s):
        ...
    @staticmethod
    def __float__(s):
        ...
    @staticmethod
    def __ge__(s, t):
        ...
    @staticmethod
    def __gt__(s, t):
        ...
    @staticmethod
    def __hash__(s):
        ...
    @staticmethod
    def __int__(s):
        ...
    @staticmethod
    def __le__(s, t):
        ...
    @staticmethod
    def __long__(s):
        ...
    @staticmethod
    def __lt__(s, t):
        ...
    @staticmethod
    def __ne__(s, t):
        ...
    @staticmethod
    def __neg__(s):
        ...
    @staticmethod
    def __nonzero__(s):
        ...
    @staticmethod
    def __pos__(s):
        ...
    @staticmethod
    def __rdiv__(s, t):
        ...
    @staticmethod
    def __repr__(s):
        ...
    @staticmethod
    def __rmod__(s, t):
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
    def _cmp(s, t, func):
        ...
    @staticmethod
    def ae(s, t, rel_eps = None, abs_eps = None):
        ...
    @staticmethod
    def sqrt(s):
        ...
    @classmethod
    def __new__(cls, val = ..., **kwargs):
        """
        A new mpf can be created from a Python float, an int, a
        or a decimal string representing a number in floating-point
        format.
        """
    @classmethod
    def mpf_convert_arg(cls, x, prec, rounding):
        ...
    @classmethod
    def mpf_convert_lhs(cls, x):
        ...
    @classmethod
    def mpf_convert_rhs(cls, x):
        ...
    def __add__(self, other):
        ...
    def __div__(self, other):
        ...
    def __eq__(self, other):
        ...
    def __getstate__(self):
        ...
    def __mod__(self, other):
        ...
    def __mul__(self, other):
        ...
    def __pow__(self, other):
        ...
    def __radd__(self, other):
        ...
    def __rmul__(self, other):
        ...
    def __round__(self, *args):
        ...
    def __setstate__(self, val):
        ...
    def __sub__(self, other):
        ...
    def __truediv__(self, other):
        ...
    def conjugate(self):
        ...
    def to_fixed(self, prec):
        ...
    @property
    def bc(self):
        ...
    @property
    def exp(self):
        ...
    @property
    def imag(self):
        ...
    @property
    def man(self):
        ...
    @property
    def man_exp(self):
        ...
    @property
    def real(self):
        ...
class mpc(_mpc):
    _ctxdata: typing.ClassVar[list]  # value = [mpc, <built-in method __new__ of type object at 0x7a0f2331d600>, [53, 'n']]
    context: typing.ClassVar[mpmath.ctx_mp.MPContext]  # value = <mpmath.ctx_mp.MPContext object>
class mpf(_mpf):
    _ctxdata: typing.ClassVar[list]  # value = [mpf, <built-in method __new__ of type object at 0x7a0f2331d600>, [53, 'n']]
    context: typing.ClassVar[mpmath.ctx_mp.MPContext]  # value = <mpmath.ctx_mp.MPContext object>
class mpnumeric:
    """
    Base class for mpf and mpc.
    """
    __slots__: typing.ClassVar[list] = list()
    @classmethod
    def __new__(cls, val):
        ...
def binary_op(name, with_mpf = '', with_int = '', with_mpc = ''):
    ...
MPZ_ONE: gmpy2.mpz  # value = mpz(1)
MPZ_ZERO: gmpy2.mpz  # value = mpz(0)
complex_types: tuple = (complex, _mpc)
finf: tuple  # value = (0, mpz(0), -456, -2)
fnan: tuple  # value = (0, mpz(0), -123, -1)
fninf: tuple  # value = (1, mpz(0), -789, -3)
fone: tuple  # value = (0, mpz(1), 0, 1)
fzero: tuple  # value = (0, mpz(0), 0, 0)
int_types: tuple = (int, gmpy2.mpz)
mpf_binary_op: str = "\ndef %NAME%(self, other):\n    mpf, new, (prec, rounding) = self._ctxdata\n    sval = self._mpf_\n    if hasattr(other, '_mpf_'):\n        tval = other._mpf_\n        %WITH_MPF%\n    ttype = type(other)\n    if ttype in int_types:\n        %WITH_INT%\n    elif ttype is float:\n        tval = from_float(other)\n        %WITH_MPF%\n    elif hasattr(other, '_mpc_'):\n        tval = other._mpc_\n        mpc = type(other)\n        %WITH_MPC%\n    elif ttype is complex:\n        tval = from_float(other.real), from_float(other.imag)\n        mpc = self.context.mpc\n        %WITH_MPC%\n    if isinstance(other, mpnumeric):\n        return NotImplemented\n    try:\n        other = mpf.context.convert(other, strings=False)\n    except TypeError:\n        return NotImplemented\n    return self.%NAME%(other)\n"
mpf_pow_same: str = '\n        try:\n            val = mpf_pow(sval, tval, prec, rounding) ; obj = new(mpf); obj._mpf_ = val; return obj\n        except ComplexResult:\n            if mpf.context.trap_complex:\n                raise\n            mpc = mpf.context.mpc\n            val = mpc_pow((sval, fzero), (tval, fzero), prec, rounding) ; obj = new(mpc); obj._mpc_ = val; return obj\n'
return_mpc: str = '; obj = new(mpc); obj._mpc_ = val; return obj'
return_mpf: str = '; obj = new(mpf); obj._mpf_ = val; return obj'
round_ceiling: str = 'c'
round_floor: str = 'f'
round_nearest: str = 'n'
