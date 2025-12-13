import _cython_3_2_1
import sage.libs.ntl.all as ntl
from sage.arith.misc import prime_divisors as prime_divisors
from sage.categories.category import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring import polygen as polygen
from sage.rings.polynomial.real_roots import real_roots as real_roots
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

test_els: _cython_3_2_1.cython_function_or_method
test_padic_square: _cython_3_2_1.cython_function_or_method
test_qpls: _cython_3_2_1.cython_function_or_method
test_valuation: _cython_3_2_1.cython_function_or_method
two_descent_by_two_isogeny: _cython_3_2_1.cython_function_or_method
two_descent_by_two_isogeny_work: _cython_3_2_1.cython_function_or_method
