from . import weight1 as weight1
from .submodule import ModularFormsSubmodule as ModularFormsSubmodule
from sage.matrix.constructor import Matrix as Matrix
from sage.matrix.special import identity_matrix as identity_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.verbose import verbose as verbose
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ

class CuspidalSubmodule(ModularFormsSubmodule):
    """
    Base class for cuspidal submodules of ambient spaces of modular forms.
    """
    def __init__(self, ambient_space) -> None:
        """
        The cuspidal submodule of an ambient space of modular forms.

        EXAMPLES::

            sage: S = CuspForms(SL2Z,12); S
            Cuspidal subspace of dimension 1 of Modular Forms space of dimension 2 for
            Modular Group SL(2,Z) of weight 12 over Rational Field
            sage: S.basis()
            [q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)]

            sage: S = CuspForms(Gamma0(33),2); S
            Cuspidal subspace of dimension 3 of Modular Forms space of dimension 6 for
            Congruence Subgroup Gamma0(33) of weight 2 over Rational Field
            sage: S.basis()
            [q - q^5 + O(q^6), q^2 - q^4 - q^5 + O(q^6), q^3 + O(q^6)]

            sage: S = CuspForms(Gamma1(3),6); S
            Cuspidal subspace of dimension 1 of Modular Forms space of dimension 3 for
            Congruence Subgroup Gamma1(3) of weight 6 over Rational Field
            sage: S.basis()
            [q - 6*q^2 + 9*q^3 + 4*q^4 + 6*q^5 + O(q^6)]
            sage: S == loads(dumps(S))
            True
        """
    def is_cuspidal(self) -> bool:
        """
        Return ``True`` since spaces of cusp forms are cuspidal.

        EXAMPLES::

            sage: CuspForms(4,10).is_cuspidal()
            True
        """
    @cached_method
    def modular_symbols(self, sign: int = 0):
        """
        Return the corresponding space of modular symbols with the given sign.

        EXAMPLES::

            sage: S = ModularForms(11,2).cuspidal_submodule()
            sage: S.modular_symbols()
            Modular Symbols subspace of dimension 2 of Modular Symbols space
            of dimension 3 for Gamma_0(11) of weight 2 with sign 0 over Rational Field

            sage: S.modular_symbols(sign=-1)
            Modular Symbols subspace of dimension 1 of Modular Symbols space
            of dimension 1 for Gamma_0(11) of weight 2 with sign -1 over Rational Field

            sage: M = S.modular_symbols(sign=1); M
            Modular Symbols subspace of dimension 1 of Modular Symbols space of
            dimension 2 for Gamma_0(11) of weight 2 with sign 1 over Rational Field
            sage: M.sign()
            1

            sage: S = ModularForms(1,12).cuspidal_submodule()
            sage: S.modular_symbols()
            Modular Symbols subspace of dimension 2 of Modular Symbols space of
            dimension 3 for Gamma_0(1) of weight 12 with sign 0 over Rational Field

            sage: # needs sage.rings.number_field
            sage: eps = DirichletGroup(13).0
            sage: S = CuspForms(eps^2, 2)
            sage: S.modular_symbols(sign=0)
            Modular Symbols subspace of dimension 2 of Modular Symbols space
            of dimension 4 and level 13, weight 2, character [zeta6], sign 0,
            over Cyclotomic Field of order 6 and degree 2
            sage: S.modular_symbols(sign=1)
            Modular Symbols subspace of dimension 1 of Modular Symbols space
            of dimension 3 and level 13, weight 2, character [zeta6], sign 1,
            over Cyclotomic Field of order 6 and degree 2
            sage: S.modular_symbols(sign=-1)
            Modular Symbols subspace of dimension 1 of Modular Symbols space
            of dimension 1 and level 13, weight 2, character [zeta6], sign -1,
            over Cyclotomic Field of order 6 and degree 2
        """
    def change_ring(self, R):
        """
        Change the base ring of ``self`` to ``R``, when this makes sense.

        This differs from
        :meth:`~sage.modular.modform.space.ModularFormsSpace.base_extend`
        in that there may not be a canonical map from ``self`` to the new
        space, as in the first example below. If this space has a
        character then this may fail when the character cannot be
        defined over ``R``, as in the second example.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: chi = DirichletGroup(109, CyclotomicField(3)).0
            sage: S9 = CuspForms(chi, 2, base_ring = CyclotomicField(9)); S9
            Cuspidal subspace of dimension 8 of
             Modular Forms space of dimension 10, character [zeta3 + 1] and weight 2
             over Cyclotomic Field of order 9 and degree 6
            sage: S9.change_ring(CyclotomicField(3))
            Cuspidal subspace of dimension 8 of
             Modular Forms space of dimension 10, character [zeta3 + 1] and weight 2
             over Cyclotomic Field of order 3 and degree 2
            sage: S9.change_ring(QQ)
            Traceback (most recent call last):
            ...
            ValueError: Space cannot be defined over Rational Field
        """

class CuspidalSubmodule_R(CuspidalSubmodule):
    """
    Cuspidal submodule over a non-minimal base ring.
    """

class CuspidalSubmodule_modsym_qexp(CuspidalSubmodule):
    """
    Cuspidal submodule with `q`-expansions calculated via modular symbols.
    """
    def hecke_polynomial(self, n, var: str = 'x'):
        """
        Return the characteristic polynomial of the Hecke operator `T_n` on this
        space. This is computed via modular symbols, and in particular is
        faster to compute than the matrix itself.

        EXAMPLES::

            sage: CuspForms(105, 2).hecke_polynomial(2, 'y')
            y^13 + 5*y^12 - 4*y^11 - 52*y^10 - 34*y^9 + 174*y^8 + 212*y^7
             - 196*y^6 - 375*y^5 - 11*y^4 + 200*y^3 + 80*y^2

        Check that this gives the same answer as computing the Hecke matrix::

            sage: CuspForms(105, 2).hecke_matrix(2).charpoly(var='y')
            y^13 + 5*y^12 - 4*y^11 - 52*y^10 - 34*y^9 + 174*y^8 + 212*y^7
             - 196*y^6 - 375*y^5 - 11*y^4 + 200*y^3 + 80*y^2

        Check that :issue:`21546` is fixed (this example used to take about 5 hours)::

            sage: CuspForms(1728, 2).hecke_polynomial(2) # long time (20 sec)
            x^253 + x^251 - 2*x^249
        """
    def new_submodule(self, p=None):
        """
        Return the new subspace of this space of cusp forms. This is computed
        using modular symbols.

        EXAMPLES::

            sage: CuspForms(55).new_submodule()
            Modular Forms subspace of dimension 3 of
             Modular Forms space of dimension 8 for
              Congruence Subgroup Gamma0(55) of weight 2 over Rational Field
        """

class CuspidalSubmodule_level1_Q(CuspidalSubmodule):
    """
    Space of cusp forms of level 1 over `\\QQ`.
    """
class CuspidalSubmodule_wt1_eps(CuspidalSubmodule):
    """
    Space of cusp forms of weight 1 with specified character.
    """
class CuspidalSubmodule_wt1_gH(CuspidalSubmodule):
    """
    Space of cusp forms of weight 1 for a GammaH group.
    """
class CuspidalSubmodule_g0_Q(CuspidalSubmodule_modsym_qexp):
    """
    Space of cusp forms for `\\Gamma_0(N)` over `\\QQ`.
    """
class CuspidalSubmodule_gH_Q(CuspidalSubmodule_modsym_qexp):
    """
    Space of cusp forms for `\\Gamma_H(N)` over `\\QQ`.
    """
class CuspidalSubmodule_g1_Q(CuspidalSubmodule_gH_Q):
    """
    Space of cusp forms for `\\Gamma_1(N)` over `\\QQ`.
    """
class CuspidalSubmodule_eps(CuspidalSubmodule_modsym_qexp):
    """
    Space of cusp forms with given Dirichlet character.

    EXAMPLES::

        sage: S = CuspForms(DirichletGroup(5).0,5); S
        Cuspidal subspace of dimension 1 of Modular Forms space of dimension 3,
        character [zeta4] and weight 5 over Cyclotomic Field of order 4 and degree 2

        sage: S.basis()
        [q + (-zeta4 - 1)*q^2 + (6*zeta4 - 6)*q^3 - 14*zeta4*q^4 + (15*zeta4 + 20)*q^5 + O(q^6)]
        sage: f = S.0
        sage: f.qexp()
        q + (-zeta4 - 1)*q^2 + (6*zeta4 - 6)*q^3 - 14*zeta4*q^4 + (15*zeta4 + 20)*q^5 + O(q^6)
        sage: f.qexp(7)
        q + (-zeta4 - 1)*q^2 + (6*zeta4 - 6)*q^3 - 14*zeta4*q^4 + (15*zeta4 + 20)*q^5 + 12*q^6 + O(q^7)
        sage: f.qexp(3)
        q + (-zeta4 - 1)*q^2 + O(q^3)
        sage: f.qexp(2)
        q + O(q^2)
        sage: f.qexp(1)
        O(q^1)
    """
