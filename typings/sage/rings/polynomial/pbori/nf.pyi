from _typeshed import Incomplete
from sage.rings.polynomial.pbori.PyPolyBoRi import BoolePolynomialVector as BoolePolynomialVector
from sage.rings.polynomial.pbori.pbori import BooleSet as BooleSet, GroebnerStrategy as GroebnerStrategy, Monomial as Monomial, Polynomial as Polynomial, ReductionStrategy as ReductionStrategy, Variable as Variable, easy_linear_factors as easy_linear_factors, mod_mon_set as mod_mon_set, parallel_reduce as parallel_reduce
from sage.rings.polynomial.pbori.statistics import used_vars_set as used_vars_set

class GeneratorLimitExceeded(Exception):
    """
    Docstring for GeneratorLimitExceeded
    """
    strat: Incomplete
    def __init__(self, strat) -> None: ...

def pkey(p): ...

mat_counter: int

def build_and_print_matrices(v, strat) -> None:
    """
    Old solution using PIL, the currently used implementation is done in C++
    and plots the same matrices, as being calculated
    """
def multiply_polynomials(l, ring):
    """

    TESTS::

        sage: from sage.rings.polynomial.pbori import *
        sage: r = Ring(1000)
        sage: x = r.variable
        sage: from sage.rings.polynomial.pbori.nf import multiply_polynomials
        sage: multiply_polynomials([x(3), x(2)+x(5)*x(6), x(0), x(0)+1], r)
        0
    """
def build_and_print_matrices_deg_colored(v, strat) -> None:
    """
    old PIL solution using a different color for each degree
    """
def high_probability_polynomials_trick(p, strat) -> None: ...
def symmGB_F2_python(G, deg_bound: int = 1000000000000, over_deg_bound: int = 0, use_faugere: bool = False, use_noro: bool = False, opt_lazy: bool = True, opt_red_tail: bool = True, max_growth: float = 2.0, step_factor: float = 1.0, implications: bool = False, prot: bool = False, full_prot: bool = False, selection_size: int = 1000, opt_exchange: bool = True, opt_allow_recursion: bool = False, ll: bool = False, opt_linear_algebra_in_last_block: bool = True, max_generators=None, red_tail_deg_growth: bool = True, matrix_prefix: str = 'mat', modified_linear_algebra: bool = True, draw_matrices: bool = False, easy_linear_polynomials: bool = True): ...
def GPS(G, vars_start, vars_end) -> None: ...
def GPS_with_proof_path(G, proof_path, deg_bound, over_deg_bound) -> None: ...
def GPS_with_suggestions(G, deg_bound, over_deg_bound, opt_lazy: bool = True, opt_red_tail: bool = True, initial_bb: bool = True): ...
def GPS_with_non_binary_proof_path(G, proof_path, deg_bound, over_deg_bound) -> None: ...
def symmGB_F2_C(G, opt_exchange: bool = True, deg_bound: int = 1000000000000, opt_lazy: bool = False, over_deg_bound: int = 0, opt_red_tail: bool = True, max_growth: float = 2.0, step_factor: float = 1.0, implications: bool = False, prot: bool = False, full_prot: bool = False, selection_size: int = 1000, opt_allow_recursion: bool = False, use_noro: bool = False, use_faugere: bool = False, ll: bool = False, opt_linear_algebra_in_last_block: bool = True, max_generators=None, red_tail_deg_growth: bool = True, modified_linear_algebra: bool = True, matrix_prefix: str = '', draw_matrices: bool = False): ...
def normal_form(poly, ideal, reduced: bool = True):
    """
    Simple normal form computation of a polynomial  against an ideal.

    TESTS::

        sage: from sage.rings.polynomial.pbori import declare_ring, normal_form
        sage: r=declare_ring(['x','y'], globals())
        sage: normal_form(x+y, [y],reduced=True)
        x
        sage: normal_form(x+y,[x,y])
        0
    """
