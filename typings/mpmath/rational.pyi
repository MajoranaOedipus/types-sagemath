from __future__ import annotations
import gmpy2
from gmpy2.gmpy2 import _mpmath_create as from_man_exp
from gmpy2.gmpy2 import bit_length as bitcount
from mpmath.libmp.libmpf import mpf_hash
import numbers as numbers
import operator as operator
import sys as sys
import typing
__all__: list[str] = ['HASH_MODULUS', 'bitcount', 'create_reduced', 'from_man_exp', 'int_types', 'mpf_hash', 'mpq', 'mpq_0', 'mpq_1', 'mpq_1_16', 'mpq_1_2', 'mpq_1_4', 'mpq_3_16', 'mpq_3_2', 'mpq_3_4', 'mpq_5_2', 'mpq_5_4', 'mpq_7_4', 'numbers', 'operator', 'sys']
class mpq:
    """
    
    Exact rational type, currently only intended for internal use.
    """
    __slots__: typing.ClassVar[list] = ['_mpq_']
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
    def __hash__(s):
        ...
    @staticmethod
    def __int__(s):
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
    def __rsub__(s, t):
        ...
    @staticmethod
    def __str__(s):
        ...
    @staticmethod
    def __sub__(s, t):
        ...
    @staticmethod
    def _cmp(s, t, op):
        ...
    @classmethod
    def __new__(cls, p, q = 1):
        ...
def create_reduced(p, q, _cache = ...):
    ...
HASH_MODULUS: int = 2305843009213693951
int_types: tuple = (int, gmpy2.mpz)
mpq_0: mpq  # value = mpq(0,1)
mpq_1: mpq  # value = mpq(1,1)
mpq_1_16: mpq  # value = mpq(1,16)
mpq_1_2: mpq  # value = mpq(1,2)
mpq_1_4: mpq  # value = mpq(1,4)
mpq_3_16: mpq  # value = mpq(3,16)
mpq_3_2: mpq  # value = mpq(3,2)
mpq_3_4: mpq  # value = mpq(3,4)
mpq_5_2: mpq  # value = mpq(5,2)
mpq_5_4: mpq  # value = mpq(5,4)
mpq_7_4: mpq  # value = mpq(7,4)
