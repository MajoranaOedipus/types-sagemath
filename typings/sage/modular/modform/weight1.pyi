from sage.misc.cachefunc import cached_function as cached_function
from sage.misc.verbose import verbose as verbose
from sage.modular.arithgroup.arithgroup_generic import ArithmeticSubgroup as ArithmeticSubgroup
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.structure.sequence import Sequence as Sequence

@cached_function
def modular_ratio_space(chi):
    """
    Compute the space of 'modular ratios', i.e. meromorphic modular forms f
    level N and character chi such that f * E is a holomorphic cusp form for
    every Eisenstein series E of weight 1 and character 1/chi.

    Elements are returned as `q`-expansions up to precision R, where R is one
    greater than the weight 3 Sturm bound.

    EXAMPLES::

        sage: chi = DirichletGroup(31,QQ).0
        sage: sage.modular.modform.weight1.modular_ratio_space(chi)
        [q - 8/3*q^3 + 13/9*q^4 + 43/27*q^5 - 620/81*q^6 + 1615/243*q^7 + 3481/729*q^8 + O(q^9),
         q^2 - 8/3*q^3 + 13/9*q^4 + 70/27*q^5 - 620/81*q^6 + 1858/243*q^7 + 2752/729*q^8 + O(q^9)]
    """
def modular_ratio_to_prec(chi, qexp, prec):
    """
    Given a `q`-expansion of a modular ratio up to sufficient precision to
    determine it uniquely, compute it to greater precision.

    EXAMPLES::

        sage: from sage.modular.modform.weight1 import modular_ratio_to_prec
        sage: R.<q> = QQ[[]]
        sage: modular_ratio_to_prec(DirichletGroup(31,QQ).0, q-q^2-q^5-q^7+q^8+O(q^9), 20)
        q - q^2 - q^5 - q^7 + q^8 + q^9 + q^10 + q^14 - q^16 - q^18 - q^19 + O(q^20)
    """
@cached_function
def hecke_stable_subspace(chi, aux_prime=...):
    """
    Compute a `q`-expansion basis for `S_1(\\chi)`.

    Results are returned as `q`-expansions to a certain fixed (and fairly high)
    precision. If more precision is required this can be obtained with
    :func:`modular_ratio_to_prec`.

    EXAMPLES::

        sage: from sage.modular.modform.weight1 import hecke_stable_subspace
        sage: hecke_stable_subspace(DirichletGroup(59, QQ).0)
        [q - q^3 + q^4 - q^5 - q^7 - q^12 + q^15 + q^16 + 2*q^17 - q^19 - q^20 + q^21 + q^27 - q^28 - q^29 + q^35 + O(q^40)]
    """
@cached_function
def dimension_wt1_cusp_forms(chi):
    """
    Return the dimension of the space of cusp forms of weight 1 and character chi.

    EXAMPLES::

        sage: chi = DirichletGroup(59, QQ).0
        sage: sage.modular.modform.weight1.dimension_wt1_cusp_forms(chi)
        1
    """
@cached_function
def dimension_wt1_cusp_forms_gH(group):
    """
    Return the dimension of the space of cusp forms of weight 1 for the given
    group (which should be of GammaH type). Computed by summing over Galois
    orbits of characters modulo H.

    EXAMPLES::

        sage: sage.modular.modform.weight1.dimension_wt1_cusp_forms_gH(GammaH(31, [7]))
        1
    """
