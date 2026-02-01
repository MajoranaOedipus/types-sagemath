from sage.modular.arithgroup.arithgroup_generic import (
    ArithmeticSubgroup as ArithmeticSubgroup,
    is_ArithmeticSubgroup as is_ArithmeticSubgroup,
)
from sage.modular.arithgroup.congroup import (
    degeneracy_coset_representatives_gamma0 as degeneracy_coset_representatives_gamma0,
    degeneracy_coset_representatives_gamma1 as degeneracy_coset_representatives_gamma1,
)
from sage.modular.arithgroup.congroup_gamma import (
    Gamma_constructor,
    Gamma_class as Gamma_class, 
    is_Gamma as is_Gamma
)
Gamma = Gamma_constructor
from sage.modular.arithgroup.congroup_gamma0 import (
    Gamma0_constructor,
    Gamma0_class as Gamma0_class, 
    is_Gamma0 as is_Gamma0
    )
Gamma0 = Gamma0_constructor
from sage.modular.arithgroup.congroup_gamma1 import (
    Gamma1_constructor,
    Gamma1_class as Gamma1_class, 
    is_Gamma1 as is_Gamma1
)
Gamma1 = Gamma1_constructor
from sage.modular.arithgroup.congroup_gammaH import (
    GammaH_constructor,
    GammaH_class as GammaH_class, 
    is_GammaH as is_GammaH
)
GammaH = GammaH_constructor
from sage.modular.arithgroup.congroup_generic import (
    CongruenceSubgroupBase as CongruenceSubgroupBase, 
    is_CongruenceSubgroup as is_CongruenceSubgroup,
    CongruenceSubgroup_constructor
)
CongruenceSubgroup = CongruenceSubgroup_constructor
from sage.modular.arithgroup.congroup_sl2z import (
    SL2Z as SL2Z,
    SL2Z_class as SL2Z_class,
    is_SL2Z as is_SL2Z,
)
from sage.modular.arithgroup.arithgroup_perm import (
    ArithmeticSubgroup_Permutation as ArithmeticSubgroup_Permutation,
)
from sage.modular.arithgroup.farey_symbol import Farey
FareySymbol = Farey
