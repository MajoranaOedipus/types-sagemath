import _cython_3_2_1
import sage as sage
import sage.libs.ntl.all as ntl
from sage.arith.misc import is_prime as is_prime, primitive_root as primitive_root
from sage.rings.bernmm import bernmm_bern_modp as bernmm_bern_modp
from sage.structure.element import have_same_parent as have_same_parent, parent as parent

bernoulli_mod_p: _cython_3_2_1.cython_function_or_method
bernoulli_mod_p_single: _cython_3_2_1.cython_function_or_method
verify_bernoulli_mod_p: _cython_3_2_1.cython_function_or_method
