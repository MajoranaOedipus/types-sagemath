from __future__ import annotations
import builtins as builtins
from builtins import exec as exec_
from builtins import range as xrange
from builtins import str as basestring
import gmpy2
import gmpy2 as gmpy
from gmpy2 import mpz as MPZ_TYPE
from gmpy2 import mpz as MPZ
import os as os
import sys as sys
__all__: list[str] = ['BACKEND', 'HASH_BITS', 'HASH_MODULUS', 'MPZ', 'MPZ_FIVE', 'MPZ_ONE', 'MPZ_THREE', 'MPZ_TWO', 'MPZ_TYPE', 'MPZ_ZERO', 'STRICT', 'basestring', 'builtins', 'exec_', 'gmpy', 'int_types', 'os', 'python3', 'sage', 'sage_utils', 'sys', 'xrange']
BACKEND: str = 'gmpy'
HASH_BITS: int = 61
HASH_MODULUS: int = 2305843009213693951
MPZ_FIVE: gmpy2.mpz  # value = mpz(5)
MPZ_ONE: gmpy2.mpz  # value = mpz(1)
MPZ_THREE: gmpy2.mpz  # value = mpz(3)
MPZ_TWO: gmpy2.mpz  # value = mpz(2)
MPZ_ZERO: gmpy2.mpz  # value = mpz(0)
STRICT: bool = False
int_types: tuple = (int, gmpy2.mpz)
python3: bool = True
sage = None
sage_utils = None
