from sage.arith.misc import factor as factor, is_prime as is_prime, valuation as valuation
from sage.misc.misc_c import prod as prod
from sage.modular import dirichlet as dirichlet
from sage.modular.arithgroup.congroup_gammaH import GammaH_class as GammaH_class
from sage.modular.arithgroup.congroup_generic import ArithmeticSubgroup as ArithmeticSubgroup
from sage.rings.finite_rings.integer_mod import Mod as Mod
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import frac as frac

def eisen(p):
    """
    Return the Eisenstein number `n` which is the numerator of `(p-1)/12`.

    INPUT:

    - ``p`` -- a prime

    OUTPUT: integer

    EXAMPLES::

        sage: [(p, sage.modular.dims.eisen(p)) for p in prime_range(24)]
        [(2, 1), (3, 1), (5, 1), (7, 1), (11, 5), (13, 1), (17, 4),
         (19, 3), (23, 11)]
    """
def CO_delta(r, p, N, eps):
    """
    This is used as an intermediate value in computations related to
    the paper of Cohen-Oesterlé.

    INPUT:

    - ``r`` -- positive integer

    - ``p`` -- a prime

    - ``N`` -- positive integer

    - ``eps`` -- character

    OUTPUT: element of the base ring of the character

    EXAMPLES::

        sage: G.<eps> = DirichletGroup(7)
        sage: sage.modular.dims.CO_delta(1,5,7,eps^3)
        2
    """
def CO_nu(r, p, N, eps):
    """
    This is used as an intermediate value in computations related to
    the paper of Cohen-Oesterlé.

    INPUT:

    - ``r`` -- positive integer

    - ``p`` -- a prime

    - ``N`` -- positive integer

    - ``eps`` -- character

    OUTPUT: element of the base ring of the character

    EXAMPLES::

        sage: G.<eps> = DirichletGroup(7)
        sage: G.<eps> = DirichletGroup(7)
        sage: sage.modular.dims.CO_nu(1,7,7,eps)
        -1
    """
def CohenOesterle(eps, k):
    """
    Compute the Cohen-Oesterlé function associate to eps, `k`.

    This is a summand in the formula for the dimension of the space of
    cusp forms of weight `2` with character `\\varepsilon`.

    INPUT:

    - ``eps`` -- Dirichlet character

    - ``k`` -- integer

    OUTPUT: element of the base ring of eps

    EXAMPLES::

        sage: G.<eps> = DirichletGroup(7)
        sage: sage.modular.dims.CohenOesterle(eps, 2)
        -2/3
        sage: sage.modular.dims.CohenOesterle(eps, 4)
        -1
    """
def dimension_new_cusp_forms(X, k: int = 2, p: int = 0):
    """
    Return the dimension of the new (or `p`-new) subspace of
    cusp forms for the character or group `X`.

    INPUT:

    - ``X`` -- integer, congruence subgroup or Dirichlet
      character

    - ``k`` -- weight (integer)

    - ``p`` -- 0 or a prime

    EXAMPLES::

        sage: from sage.modular.dims import dimension_new_cusp_forms
        sage: dimension_new_cusp_forms(100,2)
        1

        sage: dimension_new_cusp_forms(Gamma0(100),2)
        1
        sage: dimension_new_cusp_forms(Gamma0(100),4)
        5

        sage: dimension_new_cusp_forms(Gamma1(100),2)
        141
        sage: dimension_new_cusp_forms(Gamma1(100),4)
        463

        sage: dimension_new_cusp_forms(DirichletGroup(100).1^2,2)
        2
        sage: dimension_new_cusp_forms(DirichletGroup(100).1^2,4)
        8

        sage: sum(dimension_new_cusp_forms(e,3) for e in DirichletGroup(30))
        12
        sage: dimension_new_cusp_forms(Gamma1(30),3)
        12

    Check that :issue:`12640` is fixed::

        sage: dimension_new_cusp_forms(DirichletGroup(1)(1), 12)
        1
        sage: dimension_new_cusp_forms(DirichletGroup(2)(1), 24)
        1
    """
def dimension_cusp_forms(X, k: int = 2):
    """
    The dimension of the space of cusp forms for the given congruence
    subgroup or Dirichlet character.

    INPUT:

    - ``X`` -- congruence subgroup or Dirichlet character
      or integer

    - ``k`` -- weight (integer)

    EXAMPLES::

        sage: from sage.modular.dims import dimension_cusp_forms
        sage: dimension_cusp_forms(5,4)
        1

        sage: dimension_cusp_forms(Gamma0(11),2)
        1
        sage: dimension_cusp_forms(Gamma1(13),2)
        2

        sage: dimension_cusp_forms(DirichletGroup(13).0^2,2)
        1
        sage: dimension_cusp_forms(DirichletGroup(13).0,3)
        1

        sage: dimension_cusp_forms(Gamma0(11),2)
        1
        sage: dimension_cusp_forms(Gamma0(11),0)
        0
        sage: dimension_cusp_forms(Gamma0(1),12)
        1
        sage: dimension_cusp_forms(Gamma0(1),2)
        0
        sage: dimension_cusp_forms(Gamma0(1),4)
        0

        sage: dimension_cusp_forms(Gamma0(389),2)
        32
        sage: dimension_cusp_forms(Gamma0(389),4)
        97
        sage: dimension_cusp_forms(Gamma0(2005),2)
        199
        sage: dimension_cusp_forms(Gamma0(11),1)
        0

        sage: dimension_cusp_forms(Gamma1(11),2)
        1
        sage: dimension_cusp_forms(Gamma1(1),12)
        1
        sage: dimension_cusp_forms(Gamma1(1),2)
        0
        sage: dimension_cusp_forms(Gamma1(1),4)
        0

        sage: dimension_cusp_forms(Gamma1(389),2)
        6112
        sage: dimension_cusp_forms(Gamma1(389),4)
        18721
        sage: dimension_cusp_forms(Gamma1(2005),2)
        159201

        sage: dimension_cusp_forms(Gamma1(11),1)
        0

        sage: e = DirichletGroup(13).0
        sage: e.order()
        12
        sage: dimension_cusp_forms(e,2)
        0
        sage: dimension_cusp_forms(e^2,2)
        1

    Check that :issue:`12640` is fixed::

        sage: dimension_cusp_forms(DirichletGroup(1)(1), 12)
        1
        sage: dimension_cusp_forms(DirichletGroup(2)(1), 24)
        5
    """
def dimension_eis(X, k: int = 2):
    """
    The dimension of the space of Eisenstein series for the given
    congruence subgroup.

    INPUT:

    - ``X`` -- congruence subgroup or Dirichlet character
      or integer

    - ``k`` -- integer; weight

    EXAMPLES::

        sage: from sage.modular.dims import dimension_eis
        sage: dimension_eis(5,4)
        2

        sage: dimension_eis(Gamma0(11),2)
        1
        sage: dimension_eis(Gamma1(13),2)
        11
        sage: dimension_eis(Gamma1(2006),2)
        3711

        sage: e = DirichletGroup(13).0
        sage: e.order()
        12
        sage: dimension_eis(e,2)
        0
        sage: dimension_eis(e^2,2)
        2

        sage: e = DirichletGroup(13).0
        sage: e.order()
        12
        sage: dimension_eis(e,2)
        0
        sage: dimension_eis(e^2,2)
        2
        sage: dimension_eis(e,13)
        2

        sage: G = DirichletGroup(20)
        sage: dimension_eis(G.0,3)
        4
        sage: dimension_eis(G.1,3)
        6
        sage: dimension_eis(G.1^2,2)
        6

        sage: G = DirichletGroup(200)
        sage: e = prod(G.gens(), G(1))
        sage: e.conductor()
        200
        sage: dimension_eis(e,2)
        4

        sage: from sage.modular.dims import dimension_modular_forms
        sage: dimension_modular_forms(Gamma1(4), 11)
        6
    """
def dimension_modular_forms(X, k: int = 2):
    """
    The dimension of the space of cusp forms for the given congruence
    subgroup (either `\\Gamma_0(N)`, `\\Gamma_1(N)`, or
    `\\Gamma_H(N)`) or Dirichlet character.

    INPUT:

    - ``X`` -- congruence subgroup or Dirichlet character

    - ``k`` -- integer; weight

    EXAMPLES::

        sage: from sage.modular.dims import dimension_modular_forms
        sage: dimension_modular_forms(Gamma0(11),2)
        2
        sage: dimension_modular_forms(Gamma0(11),0)
        1
        sage: dimension_modular_forms(Gamma1(13),2)
        13
        sage: dimension_modular_forms(GammaH(11, [10]), 2)
        10
        sage: dimension_modular_forms(GammaH(11, [10]))
        10
        sage: dimension_modular_forms(GammaH(11, [10]), 4)
        20
        sage: e = DirichletGroup(20).1
        sage: dimension_modular_forms(e,3)
        9
        sage: from sage.modular.dims import dimension_cusp_forms
        sage: dimension_cusp_forms(e,3)
        3
        sage: from sage.modular.dims import dimension_eis
        sage: dimension_eis(e,3)
        6
        sage: dimension_modular_forms(11,2)
        2
    """
def sturm_bound(level, weight: int = 2):
    """
    Return the Sturm bound for modular forms with given level and weight.

    For more details, see the documentation for the ``sturm_bound`` method
    of :class:`sage.modular.arithgroup.CongruenceSubgroup` objects.

    INPUT:

    - ``level`` -- integer (interpreted as a level for `\\Gamma0`) or a
      congruence subgroup

    - ``weight`` -- integer `\\geq 2` (default: 2)

    EXAMPLES::

        sage: from sage.modular.dims import sturm_bound
        sage: sturm_bound(11,2)
        2
        sage: sturm_bound(389,2)
        65
        sage: sturm_bound(1,12)
        1
        sage: sturm_bound(100,2)
        30
        sage: sturm_bound(1,36)
        3
        sage: sturm_bound(11)
        2
    """
