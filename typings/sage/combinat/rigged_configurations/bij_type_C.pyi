from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA as KRTToRCBijectionTypeA, RCToKRTBijectionTypeA as RCToKRTBijectionTypeA

class KRTToRCBijectionTypeC(KRTToRCBijectionTypeA):
    """
    Specific implementation of the bijection from KR tableaux to rigged
    configurations for type `C_n^{(1)}`.

    This inherits from type `A_n^{(1)}` because we use the same methods in
    some places.
    """
    def next_state(self, val) -> None:
        """
        Build the next state for type `C_n^{(1)}`.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['C', 3, 1], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_C import KRTToRCBijectionTypeC
            sage: bijection = KRTToRCBijectionTypeC(KRT(pathlist=[[-1,2]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [2])
            sage: bijection.next_state(2)
        """

class RCToKRTBijectionTypeC(RCToKRTBijectionTypeA):
    """
    Specific implementation of the bijection from rigged configurations to
    tensor products of KR tableaux for type `C_n^{(1)}`.
    """
    def next_state(self, height):
        """
        Build the next state for type `C_n^{(1)}`.

        TESTS::

            sage: RC = RiggedConfigurations(['C', 3, 1], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_C import RCToKRTBijectionTypeC
            sage: bijection = RCToKRTBijectionTypeC(RC(partition_list=[[2],[2],[1]]))
            sage: bijection.next_state(1)
            -1
        """
