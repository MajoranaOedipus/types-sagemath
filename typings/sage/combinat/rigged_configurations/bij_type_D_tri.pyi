from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA as KRTToRCBijectionTypeA, RCToKRTBijectionTypeA as RCToKRTBijectionTypeA

class KRTToRCBijectionTypeDTri(KRTToRCBijectionTypeA):
    """
    Specific implementation of the bijection from KR tableaux to rigged
    configurations for type `D_4^{(3)}`.

    This inherits from type `A_n^{(1)}` because we use the same methods in
    some places.
    """
    def next_state(self, val) -> None:
        """
        Build the next state for type `D_4^{(3)}`.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 3], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D_tri import KRTToRCBijectionTypeDTri
            sage: bijection = KRTToRCBijectionTypeDTri(KRT(pathlist=[[-1,2]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [2])
            sage: bijection.next_state(2)
        """

class RCToKRTBijectionTypeDTri(RCToKRTBijectionTypeA):
    """
    Specific implementation of the bijection from rigged configurations to
    tensor products of KR tableaux for type `D_4^{(3)}`.
    """
    def next_state(self, height):
        """
        Build the next state for type `D_4^{(3)}`.

        TESTS::

            sage: RC = RiggedConfigurations(['D', 4, 3], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D_tri import RCToKRTBijectionTypeDTri
            sage: bijection = RCToKRTBijectionTypeDTri(RC(partition_list=[[3],[2]]))
            sage: bijection.next_state(2)
            -3
        """
