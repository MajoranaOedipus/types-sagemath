from sage.modules.fp_graded.free_morphism import FreeGradedModuleMorphism as FreeGradedModuleMorphism
from sage.modules.fp_graded.homspace import FPModuleHomspace as FPModuleHomspace

class FreeGradedModuleHomspace(FPModuleHomspace):
    """
    Homspace between two free graded modules.
    """
    Element = FreeGradedModuleMorphism
