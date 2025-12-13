from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA as KRTToRCBijectionTypeA, RCToKRTBijectionTypeA as RCToKRTBijectionTypeA
from sage.combinat.rigged_configurations.bij_type_A2_dual import KRTToRCBijectionTypeA2Dual as KRTToRCBijectionTypeA2Dual, RCToKRTBijectionTypeA2Dual as RCToKRTBijectionTypeA2Dual
from sage.combinat.rigged_configurations.bij_type_A2_even import KRTToRCBijectionTypeA2Even as KRTToRCBijectionTypeA2Even, RCToKRTBijectionTypeA2Even as RCToKRTBijectionTypeA2Even
from sage.combinat.rigged_configurations.bij_type_A2_odd import KRTToRCBijectionTypeA2Odd as KRTToRCBijectionTypeA2Odd, RCToKRTBijectionTypeA2Odd as RCToKRTBijectionTypeA2Odd
from sage.combinat.rigged_configurations.bij_type_B import KRTToRCBijectionTypeB as KRTToRCBijectionTypeB, RCToKRTBijectionTypeB as RCToKRTBijectionTypeB
from sage.combinat.rigged_configurations.bij_type_C import KRTToRCBijectionTypeC as KRTToRCBijectionTypeC, RCToKRTBijectionTypeC as RCToKRTBijectionTypeC
from sage.combinat.rigged_configurations.bij_type_D import KRTToRCBijectionTypeD as KRTToRCBijectionTypeD, RCToKRTBijectionTypeD as RCToKRTBijectionTypeD
from sage.combinat.rigged_configurations.bij_type_D_tri import KRTToRCBijectionTypeDTri as KRTToRCBijectionTypeDTri, RCToKRTBijectionTypeDTri as RCToKRTBijectionTypeDTri
from sage.combinat.rigged_configurations.bij_type_D_twisted import KRTToRCBijectionTypeDTwisted as KRTToRCBijectionTypeDTwisted, RCToKRTBijectionTypeDTwisted as RCToKRTBijectionTypeDTwisted
from sage.combinat.rigged_configurations.bij_type_E67 import KRTToRCBijectionTypeE67 as KRTToRCBijectionTypeE67, RCToKRTBijectionTypeE67 as RCToKRTBijectionTypeE67

def KRTToRCBijection(tp_krt):
    """
    Return the correct KR tableaux to rigged configuration bijection helper class.

    TESTS::

        sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 4, 1], [[2,1]])
        sage: from sage.combinat.rigged_configurations.bijection import KRTToRCBijection
        sage: bijection = KRTToRCBijection(KRT(pathlist=[[5,2]]))
    """
def RCToKRTBijection(rigged_configuration_elt):
    """
    Return the correct rigged configuration to KR tableaux bijection helper class.

    TESTS::

        sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 1]])
        sage: from sage.combinat.rigged_configurations.bijection import RCToKRTBijection
        sage: bijection = RCToKRTBijection(RC(partition_list=[[1],[1],[1],[1]]))
    """
