from sage.combinat.rigged_configurations.bij_abstract_class import KRTToRCBijectionAbstract as KRTToRCBijectionAbstract, RCToKRTBijectionAbstract as RCToKRTBijectionAbstract

class KRTToRCBijectionTypeA(KRTToRCBijectionAbstract):
    """
    Specific implementation of the bijection from KR tableaux to rigged
    configurations for type `A_n^{(1)}`.
    """
    def next_state(self, val) -> None:
        """
        Build the next state for type `A_n^{(1)}`.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 4, 1], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA
            sage: bijection = KRTToRCBijectionTypeA(KRT(pathlist=[[4,3]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [3])
            sage: bijection.next_state(3)
        """

class RCToKRTBijectionTypeA(RCToKRTBijectionAbstract):
    """
    Specific implementation of the bijection from rigged configurations to
    tensor products of KR tableaux for type `A_n^{(1)}`.
    """
    def next_state(self, height):
        """
        Build the next state for type `A_n^{(1)}`.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A import RCToKRTBijectionTypeA
            sage: bijection = RCToKRTBijectionTypeA(RC(partition_list=[[1],[1],[1],[1]]))
            sage: bijection.next_state(1)
            5
        """
