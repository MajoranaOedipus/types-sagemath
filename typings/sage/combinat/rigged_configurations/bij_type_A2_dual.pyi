from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA as KRTToRCBijectionTypeA
from sage.combinat.rigged_configurations.bij_type_C import KRTToRCBijectionTypeC as KRTToRCBijectionTypeC, RCToKRTBijectionTypeC as RCToKRTBijectionTypeC
from sage.rings.rational_field import QQ as QQ

class KRTToRCBijectionTypeA2Dual(KRTToRCBijectionTypeC):
    """
    Specific implementation of the bijection from KR tableaux to rigged
    configurations for type `A_{2n}^{(2)\\dagger}`.

    This inherits from type `C_n^{(1)}` because we use the same methods in
    some places.
    """
    def next_state(self, val) -> None:
        """
        Build the next state for type `A_{2n}^{(2)\\dagger}`.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(CartanType(['A', 4, 2]).dual(), [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A2_dual import KRTToRCBijectionTypeA2Dual
            sage: bijection = KRTToRCBijectionTypeA2Dual(KRT(pathlist=[[-1,2]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [2])
            sage: bijection.next_state(2)
        """

class RCToKRTBijectionTypeA2Dual(RCToKRTBijectionTypeC):
    """
    Specific implementation of the bijection from rigged configurations to
    tensor products of KR tableaux for type `A_{2n}^{(2)\\dagger}`.
    """
    def next_state(self, height):
        """
        Build the next state for type `A_{2n}^{(2)\\dagger}`.

        TESTS::

            sage: RC = RiggedConfigurations(CartanType(['A', 4, 2]).dual(), [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A2_dual import RCToKRTBijectionTypeA2Dual
            sage: bijection = RCToKRTBijectionTypeA2Dual(RC(partition_list=[[2],[2,2]]))
            sage: bijection.next_state(2)
            -1
        """
