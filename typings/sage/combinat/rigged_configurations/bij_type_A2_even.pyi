from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA as KRTToRCBijectionTypeA
from sage.combinat.rigged_configurations.bij_type_C import KRTToRCBijectionTypeC as KRTToRCBijectionTypeC, RCToKRTBijectionTypeC as RCToKRTBijectionTypeC

class KRTToRCBijectionTypeA2Even(KRTToRCBijectionTypeC):
    """
    Specific implementation of the bijection from KR tableaux to rigged
    configurations for type `A_{2n}^{(2)}`.

    This inherits from type `C_n^{(1)}` because we use the same methods in
    some places.
    """
    def next_state(self, val) -> None:
        """
        Build the next state for type `A_{2n}^{(2)}`.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 4, 2], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A2_even import KRTToRCBijectionTypeA2Even
            sage: bijection = KRTToRCBijectionTypeA2Even(KRT(pathlist=[[-1,-2]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [-2])
            sage: bijection.next_state(-2)
        """

class RCToKRTBijectionTypeA2Even(RCToKRTBijectionTypeC):
    """
    Specific implementation of the bijection from rigged configurations to
    tensor products of KR tableaux for type `A_{2n}^{(2)}`.
    """
    def next_state(self, height):
        """
        Build the next state for type `A_{2n}^{(2)}`.

        TESTS::

            sage: RC = RiggedConfigurations(['A', 4, 2], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A2_even import RCToKRTBijectionTypeA2Even
            sage: bijection = RCToKRTBijectionTypeA2Even(RC(partition_list=[[2],[2,2]]))
            sage: bijection.next_state(2)
            -1
        """
