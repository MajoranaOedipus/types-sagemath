from .morphism import SteenrodFPModuleMorphism as SteenrodFPModuleMorphism, SteenrodFreeModuleMorphism as SteenrodFreeModuleMorphism
from sage.modules.fp_graded.free_homspace import FreeGradedModuleHomspace as FreeGradedModuleHomspace
from sage.modules.fp_graded.homspace import FPModuleHomspace as FPModuleHomspace

class SteenrodFPModuleHomspace(FPModuleHomspace):
    Element = SteenrodFPModuleMorphism

class SteenrodFreeModuleHomspace(SteenrodFPModuleHomspace, FreeGradedModuleHomspace):
    Element = SteenrodFreeModuleMorphism
