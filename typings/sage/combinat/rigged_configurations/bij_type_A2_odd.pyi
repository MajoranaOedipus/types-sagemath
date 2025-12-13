from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA as KRTToRCBijectionTypeA, RCToKRTBijectionTypeA as RCToKRTBijectionTypeA

class KRTToRCBijectionTypeA2Odd(KRTToRCBijectionTypeA):
    """
    Specific implementation of the bijection from KR tableaux to rigged
    configurations for type `A_{2n-1}^{(2)}`.

    This inherits from type `A_n^{(1)}` because we use the same methods in
    some places.
    """
    def next_state(self, val) -> None:
        """
        Build the next state for type `A_{2n-1}^{(2)}`.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 5, 2], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A2_odd import KRTToRCBijectionTypeA2Odd
            sage: bijection = KRTToRCBijectionTypeA2Odd(KRT(pathlist=[[-2,3]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [3])
            sage: bijection.next_state(3)
        """

class RCToKRTBijectionTypeA2Odd(RCToKRTBijectionTypeA):
    """
    Specific implementation of the bijection from rigged configurations to
    tensor products of KR tableaux for type `A_{2n-1}^{(2)}`.
    """
    def next_state(self, height):
        """
        Build the next state for type `A_{2n-1}^{(2)}`.

        TESTS::

            sage: RC = RiggedConfigurations(['A', 5, 2], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A2_odd import RCToKRTBijectionTypeA2Odd
            sage: bijection = RCToKRTBijectionTypeA2Odd(RC(partition_list=[[1],[2,1],[2]]))
            sage: bijection.next_state(1)
            -2
        """
