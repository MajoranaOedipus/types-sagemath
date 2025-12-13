from . import eis_series as eis_series, element as element, submodule as submodule
from sage.arith.functions import lcm as lcm
from sage.arith.misc import euler_phi as euler_phi
from sage.categories.objects import Objects as Objects
from sage.matrix.constructor import Matrix as Matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.structure.sequence import Sequence as Sequence

class EisensteinSubmodule(submodule.ModularFormsSubmodule):
    """
    The Eisenstein submodule of an ambient space of modular forms.
    """
    def __init__(self, ambient_space) -> None:
        """
        Return the Eisenstein submodule of the given space.

        EXAMPLES::

            sage: E = ModularForms(23,4).eisenstein_subspace()  # indirect doctest
            sage: E
            Eisenstein subspace of dimension 2 of Modular Forms space of dimension 7
             for Congruence Subgroup Gamma0(23) of weight 4 over Rational Field
            sage: E == loads(dumps(E))
            True
        """
    def eisenstein_submodule(self):
        """
        Return the Eisenstein submodule of ``self``.
        (Yes, this is just self.)

        EXAMPLES::

            sage: E = ModularForms(23,4).eisenstein_subspace()
            sage: E == E.eisenstein_submodule()
            True
        """
    @cached_method
    def modular_symbols(self, sign: int = 0):
        """
        Return the corresponding space of modular symbols with given sign. This
        will fail in weight 1.

        .. warning::

           If sign != 0, then the space of modular symbols will, in general,
           only correspond to a *subspace* of this space of modular forms.
           This can be the case for both sign +1 or -1.

        EXAMPLES::

            sage: E = ModularForms(11,2).eisenstein_submodule()
            sage: M = E.modular_symbols(); M
            Modular Symbols subspace of dimension 1 of Modular Symbols space
            of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field
            sage: M.sign()
            0

            sage: M = E.modular_symbols(sign=-1); M
            Modular Symbols subspace of dimension 0 of Modular Symbols space of
            dimension 1 for Gamma_0(11) of weight 2 with sign -1 over Rational Field

            sage: E = ModularForms(1,12).eisenstein_submodule()
            sage: E.modular_symbols()
            Modular Symbols subspace of dimension 1 of Modular Symbols space of
            dimension 3 for Gamma_0(1) of weight 12 with sign 0 over Rational Field

            sage: eps = DirichletGroup(13).0
            sage: E = EisensteinForms(eps^2, 2)
            sage: E.modular_symbols()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of
             dimension 4 and level 13, weight 2, character [zeta6], sign 0,
             over Cyclotomic Field of order 6 and degree 2

            sage: E = EisensteinForms(eps, 1); E
            Eisenstein subspace of dimension 1 of Modular Forms space of character
             [zeta12] and weight 1 over Cyclotomic Field of order 12 and degree 4
            sage: E.modular_symbols()
            Traceback (most recent call last):
            ...
            ValueError: the weight must be at least 2
        """

class EisensteinSubmodule_params(EisensteinSubmodule):
    @cached_method
    def parameters(self):
        """
        Return a list of parameters for each Eisenstein series
        spanning ``self``. That is, for each such series, return a triple
        of the form (`\\psi`, `\\chi`, level), where `\\psi` and `\\chi`
        are the characters defining the Eisenstein series, and level
        is the smallest level at which this series occurs.

        EXAMPLES::

            sage: ModularForms(24,2).eisenstein_submodule().parameters()
            [(Dirichlet character modulo 24 of conductor 1 mapping 7 |--> 1, 13 |--> 1, 17 |--> 1,
              Dirichlet character modulo 24 of conductor 1 mapping 7 |--> 1, 13 |--> 1, 17 |--> 1, 2),
              ...
              Dirichlet character modulo 24 of conductor 1 mapping 7 |--> 1, 13 |--> 1, 17 |--> 1, 24)]
            sage: EisensteinForms(12,6).parameters()[-1]
            (Dirichlet character modulo 12 of conductor 1 mapping 7 |--> 1, 5 |--> 1,
             Dirichlet character modulo 12 of conductor 1 mapping 7 |--> 1, 5 |--> 1, 12)

            sage: pars = ModularForms(DirichletGroup(24).0,3).eisenstein_submodule().parameters()
            sage: [(x[0].values_on_gens(),x[1].values_on_gens(),x[2]) for x in pars]
            [((1, 1, 1), (-1, 1, 1), 1),
            ((1, 1, 1), (-1, 1, 1), 2),
            ((1, 1, 1), (-1, 1, 1), 3),
            ((1, 1, 1), (-1, 1, 1), 6),
            ((-1, 1, 1), (1, 1, 1), 1),
            ((-1, 1, 1), (1, 1, 1), 2),
            ((-1, 1, 1), (1, 1, 1), 3),
            ((-1, 1, 1), (1, 1, 1), 6)]
            sage: EisensteinForms(DirichletGroup(24).0,1).parameters()
            [(Dirichlet character modulo 24 of conductor 1 mapping 7 |--> 1, 13 |--> 1, 17 |--> 1,
              Dirichlet character modulo 24 of conductor 4 mapping 7 |--> -1, 13 |--> 1, 17 |--> 1, 1),
             (Dirichlet character modulo 24 of conductor 1 mapping 7 |--> 1, 13 |--> 1, 17 |--> 1,
              Dirichlet character modulo 24 of conductor 4 mapping 7 |--> -1, 13 |--> 1, 17 |--> 1, 2),
             (Dirichlet character modulo 24 of conductor 1 mapping 7 |--> 1, 13 |--> 1, 17 |--> 1,
              Dirichlet character modulo 24 of conductor 4 mapping 7 |--> -1, 13 |--> 1, 17 |--> 1, 3),
             (Dirichlet character modulo 24 of conductor 1 mapping 7 |--> 1, 13 |--> 1, 17 |--> 1,
              Dirichlet character modulo 24 of conductor 4 mapping 7 |--> -1, 13 |--> 1, 17 |--> 1, 6)]
        """
    def new_submodule(self, p=None):
        """
        Return the new submodule of ``self``.

        EXAMPLES::

            sage: e = EisensteinForms(Gamma0(225), 2).new_submodule(); e
            Modular Forms subspace of dimension 3 of Modular Forms space of dimension 42
             for Congruence Subgroup Gamma0(225) of weight 2 over Rational Field
            sage: e.basis()
            [q + O(q^6), q^2 + O(q^6), q^4 + O(q^6)]
        """
    def change_ring(self, base_ring):
        """
        Return ``self`` as a module over ``base_ring``.

        EXAMPLES::

            sage: E = EisensteinForms(12,2) ; E
            Eisenstein subspace of dimension 5 of Modular Forms space of dimension 5
             for Congruence Subgroup Gamma0(12) of weight 2 over Rational Field
            sage: E.basis()
            [1 + O(q^6), q + 6*q^5 + O(q^6), q^2 + O(q^6), q^3 + O(q^6), q^4 + O(q^6)]
            sage: E.change_ring(GF(5))
            Eisenstein subspace of dimension 5 of Modular Forms space of dimension 5
             for Congruence Subgroup Gamma0(12) of weight 2 over Finite Field of size 5
            sage: E.change_ring(GF(5)).basis()
            [1 + O(q^6), q + q^5 + O(q^6), q^2 + O(q^6), q^3 + O(q^6), q^4 + O(q^6)]
        """
    def eisenstein_series(self):
        """
        Return the Eisenstein series that span this space (over the
        algebraic closure).

        EXAMPLES::

            sage: EisensteinForms(11,2).eisenstein_series()
            [5/12 + q + 3*q^2 + 4*q^3 + 7*q^4 + 6*q^5 + O(q^6)]
            sage: EisensteinForms(1,4).eisenstein_series()
            [1/240 + q + 9*q^2 + 28*q^3 + 73*q^4 + 126*q^5 + O(q^6)]
            sage: EisensteinForms(1,24).eisenstein_series()
            [236364091/131040 + q + 8388609*q^2 + 94143178828*q^3 + 70368752566273*q^4 + 11920928955078126*q^5 + O(q^6)]
            sage: EisensteinForms(5,4).eisenstein_series()
            [1/240 + q + 9*q^2 + 28*q^3 + 73*q^4 + 126*q^5 + O(q^6), 1/240 + q^5 + O(q^6)]
            sage: EisensteinForms(13,2).eisenstein_series()
            [1/2 + q + 3*q^2 + 4*q^3 + 7*q^4 + 6*q^5 + O(q^6)]

            sage: E = EisensteinForms(Gamma1(7),2)
            sage: E.set_precision(4)
            sage: E.eisenstein_series()
            [1/4 + q + 3*q^2 + 4*q^3 + O(q^4),
             1/7*zeta6 - 3/7 + q + (-2*zeta6 + 1)*q^2 + (3*zeta6 - 2)*q^3 + O(q^4),
             q + (-zeta6 + 2)*q^2 + (zeta6 + 2)*q^3 + O(q^4),
             -1/7*zeta6 - 2/7 + q + (2*zeta6 - 1)*q^2 + (-3*zeta6 + 1)*q^3 + O(q^4),
             q + (zeta6 + 1)*q^2 + (-zeta6 + 3)*q^3 + O(q^4)]

            sage: eps = DirichletGroup(13).0^2
            sage: ModularForms(eps,2).eisenstein_series()
            [-7/13*zeta6 - 11/13 + q + (2*zeta6 + 1)*q^2 + (-3*zeta6 + 1)*q^3 + (6*zeta6 - 3)*q^4 - 4*q^5 + O(q^6),
             q + (zeta6 + 2)*q^2 + (-zeta6 + 3)*q^3 + (3*zeta6 + 3)*q^4 + 4*q^5 + O(q^6)]

            sage: M = ModularForms(19,3).eisenstein_subspace()
            sage: M.eisenstein_series()
            []

            sage: M = ModularForms(DirichletGroup(13).0, 1)
            sage: M.eisenstein_series()
            [-1/13*zeta12^3 + 6/13*zeta12^2 + 4/13*zeta12 + 2/13 + q + (zeta12 + 1)*q^2 + zeta12^2*q^3 + (zeta12^2 + zeta12 + 1)*q^4 + (-zeta12^3 + 1)*q^5 + O(q^6)]

            sage: M = ModularForms(GammaH(15, [4]), 4)
            sage: M.eisenstein_series()
            [1/240 + q + 9*q^2 + 28*q^3 + 73*q^4 + 126*q^5 + O(q^6),
             1/240 + q^3 + O(q^6),
             1/240 + q^5 + O(q^6),
             1/240 + O(q^6),
             1 + q - 7*q^2 - 26*q^3 + 57*q^4 + q^5 + O(q^6),
             1 + q^3 + O(q^6),
             q + 7*q^2 + 26*q^3 + 57*q^4 + 125*q^5 + O(q^6),
             q^3 + O(q^6)]
        """
    def new_eisenstein_series(self):
        """
        Return a list of the Eisenstein series in this space that are new.

        EXAMPLES::

            sage: E = EisensteinForms(25, 4)
            sage: E.new_eisenstein_series()
            [q + 7*zeta4*q^2 - 26*zeta4*q^3 - 57*q^4 + O(q^6),
             q - 9*q^2 - 28*q^3 + 73*q^4 + O(q^6),
             q - 7*zeta4*q^2 + 26*zeta4*q^3 - 57*q^4 + O(q^6)]
        """

class EisensteinSubmodule_g0_Q(EisensteinSubmodule_params):
    """
    Space of Eisenstein forms for `\\Gamma_0(N)`.
    """
class EisensteinSubmodule_gH_Q(EisensteinSubmodule_params):
    """
    Space of Eisenstein forms for `\\Gamma_H(N)`.
    """
class EisensteinSubmodule_g1_Q(EisensteinSubmodule_gH_Q):
    """
    Space of Eisenstein forms for `\\Gamma_1(N)`.
    """
class EisensteinSubmodule_eps(EisensteinSubmodule_params):
    """
    Space of Eisenstein forms with given Dirichlet character.

    EXAMPLES::

        sage: e = DirichletGroup(27,CyclotomicField(3)).0**2
        sage: M = ModularForms(e,2,prec=10).eisenstein_subspace()
        sage: M.dimension()
        6

        sage: M.eisenstein_series()
        [-1/3*zeta6 - 1/3 + q + (2*zeta6 - 1)*q^2 + q^3 + (-2*zeta6 - 1)*q^4 + (-5*zeta6 + 1)*q^5 + O(q^6),
         -1/3*zeta6 - 1/3 + q^3 + O(q^6),
         q + (-2*zeta6 + 1)*q^2 + (-2*zeta6 - 1)*q^4 + (5*zeta6 - 1)*q^5 + O(q^6),
         q + (zeta6 + 1)*q^2 + 3*q^3 + (zeta6 + 2)*q^4 + (-zeta6 + 5)*q^5 + O(q^6),
         q^3 + O(q^6),
         q + (-zeta6 - 1)*q^2 + (zeta6 + 2)*q^4 + (zeta6 - 5)*q^5 + O(q^6)]
        sage: M.eisenstein_subspace().T(2).matrix().fcp()
        (x + 2*zeta3 + 1) * (x + zeta3 + 2) * (x - zeta3 - 2)^2 * (x - 2*zeta3 - 1)^2
        sage: ModularSymbols(e,2).eisenstein_subspace().T(2).matrix().fcp()
        (x + 2*zeta3 + 1) * (x + zeta3 + 2) * (x - zeta3 - 2)^2 * (x - 2*zeta3 - 1)^2

        sage: M.basis()
        [1 - 3*zeta3*q^6 + (-2*zeta3 + 2)*q^9 + O(q^10),
         q + (5*zeta3 + 5)*q^7 + O(q^10),
         q^2 - 2*zeta3*q^8 + O(q^10),
         q^3 + (zeta3 + 2)*q^6 + 3*q^9 + O(q^10),
         q^4 - 2*zeta3*q^7 + O(q^10),
         q^5 + (zeta3 + 1)*q^8 + O(q^10)]
    """

def cyclotomic_restriction(L, K):
    """
    Given two cyclotomic fields `L` and `K`, compute the compositum
    `M` of `K` and `L`, and return a function `f` and the index `[M:K]`.

    The function `f` is a map that acts as follows (here `M =\\QQ(\\zeta_m)`):

        INPUT: element alpha in `L`
        OUTPUT: a polynomial `f(x)` in `K[x]` such that `f(\\zeta_m) = \\alpha`,
        where we view alpha as living in `M`. (Note that `\\zeta_m` generates
        `M`, not `L`.)

    EXAMPLES::

        sage: L = CyclotomicField(12); N = CyclotomicField(33); M = CyclotomicField(132)
        sage: z, n = sage.modular.modform.eisenstein_submodule.cyclotomic_restriction(L, N)
        sage: n
        2

        sage: z(L.0)
        -zeta33^19*x
        sage: z(L.0)(M.0)
        zeta132^11

        sage: z(L.0^3 - L.0 + 1)
        (zeta33^19 + zeta33^8)*x + 1
        sage: z(L.0^3 - L.0 + 1)(M.0)
        zeta132^33 - zeta132^11 + 1
        sage: z(L.0^3 - L.0 + 1)(M.0) - M(L.0^3 - L.0 + 1)
        0
    """
def cyclotomic_restriction_tower(L, K):
    """
    Suppose `L/K` is an extension of cyclotomic fields and `L=Q(\\zeta_m)`.
    This function computes a map with the following property:

        INPUT: element alpha in `L`
        OUTPUT: a polynomial `f(x)` in `K[x]` such that `f(\\zeta_m) = alpha`

    EXAMPLES::

        sage: L = CyclotomicField(12) ; K = CyclotomicField(6)
        sage: z = sage.modular.modform.eisenstein_submodule.cyclotomic_restriction_tower(L,K)
        sage: z(L.0)
        x
        sage: z(L.0^2+L.0)
        x + zeta6
    """
