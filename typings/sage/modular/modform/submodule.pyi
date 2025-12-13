import sage.modular.hecke.submodule
from .space import ModularFormsSpace as ModularFormsSpace

class ModularFormsSubmodule(ModularFormsSpace, sage.modular.hecke.submodule.HeckeSubmodule):
    """
    A submodule of an ambient space of modular forms.
    """
    def __init__(self, ambient_module, submodule, dual=None, check: bool = False) -> None:
        """
        INPUT:

        - ``ambient_module`` -- ModularFormsSpace
        - ``submodule`` -- a submodule of the ambient space
        - ``dual_module`` -- (default: ``None``) ignored
        - ``check`` -- boolean (default: ``False``); whether to check that the
          submodule is Hecke equivariant

        EXAMPLES::

          sage: M = ModularForms(Gamma1(13),2); M
          Modular Forms space of dimension 13 for Congruence Subgroup Gamma1(13) of weight 2 over Rational Field
          sage: M.eisenstein_subspace()
          Eisenstein subspace of dimension 11 of Modular Forms space of dimension 13 for Congruence Subgroup Gamma1(13) of weight 2 over Rational Field
        """

class ModularFormsSubmoduleWithBasis(ModularFormsSubmodule): ...
