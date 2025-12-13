from . import ambient as ambient, cuspidal_submodule as cuspidal_submodule, eisenstein_submodule as eisenstein_submodule
from sage.misc.cachefunc import cached_method as cached_method
from sage.modular.arithgroup.congroup_gamma0 import Gamma0_constructor as Gamma0_constructor

class ModularFormsAmbient_g0_Q(ambient.ModularFormsAmbient):
    """
    A space of modular forms for `\\Gamma_0(N)` over `\\QQ`.
    """
    def __init__(self, level, weight) -> None:
        """
        Create a space of modular symbols for `\\Gamma_0(N)` of given
        weight defined over `\\QQ`.

        EXAMPLES::

            sage: m = ModularForms(Gamma0(11),4); m
            Modular Forms space of dimension 4 for Congruence Subgroup Gamma0(11)
             of weight 4 over Rational Field
            sage: type(m)
            <class 'sage.modular.modform.ambient_g0.ModularFormsAmbient_g0_Q_with_category'>
        """
    @cached_method
    def cuspidal_submodule(self):
        """
        Return the cuspidal submodule of this space of modular forms for
        `\\Gamma_0(N)`.

        EXAMPLES::

            sage: m = ModularForms(Gamma0(33),4)
            sage: s = m.cuspidal_submodule(); s
            Cuspidal subspace of dimension 10 of Modular Forms space of dimension 14
             for Congruence Subgroup Gamma0(33) of weight 4 over Rational Field
            sage: type(s)
            <class 'sage.modular.modform.cuspidal_submodule.CuspidalSubmodule_g0_Q_with_category'>
        """
    @cached_method
    def eisenstein_submodule(self):
        """
        Return the Eisenstein submodule of this space of modular forms for
        `\\Gamma_0(N)`.

        EXAMPLES::

            sage: m = ModularForms(Gamma0(389),6)
            sage: m.eisenstein_submodule()
            Eisenstein subspace of dimension 2 of Modular Forms space of dimension 163
             for Congruence Subgroup Gamma0(389) of weight 6 over Rational Field
        """
