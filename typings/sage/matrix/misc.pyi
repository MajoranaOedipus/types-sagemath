import _cython_3_2_1
from sage.arith.misc import CRT_basis as CRT_basis, previous_prime as previous_prime
from sage.matrix.misc_flint import matrix_integer_dense_rational_reconstruction as matrix_integer_dense_rational_reconstruction
from sage.matrix.misc_mpfr import hadamard_row_bound_mpfr as hadamard_row_bound_mpfr
from sage.misc.lazy_import import LazyImport as LazyImport
from sage.misc.verbose import verbose as verbose
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

cmp_pivots: _cython_3_2_1.cython_function_or_method
matrix_integer_sparse_rational_reconstruction: _cython_3_2_1.cython_function_or_method
matrix_rational_echelon_form_multimodular: _cython_3_2_1.cython_function_or_method
