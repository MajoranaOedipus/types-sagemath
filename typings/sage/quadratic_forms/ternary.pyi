import _cython_3_2_1
from sage.arith.misc import gcd as gcd, inverse_mod as inverse_mod, xgcd as xgcd
from sage.categories.category import ZZ as ZZ
from sage.matrix.constructor import matrix as matrix
from sage.misc.prandom import randint as randint
from sage.rings.finite_rings.integer_mod import mod as mod

evaluate: _cython_3_2_1.cython_function_or_method
extend: _cython_3_2_1.cython_function_or_method
primitivize: _cython_3_2_1.cython_function_or_method
pseudorandom_primitive_zero_mod_p: _cython_3_2_1.cython_function_or_method
red_mfact: _cython_3_2_1.cython_function_or_method
