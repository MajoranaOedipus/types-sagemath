from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA as KRTToRCBijectionTypeA
from sage.combinat.rigged_configurations.bij_type_A2_even import KRTToRCBijectionTypeA2Even as KRTToRCBijectionTypeA2Even, RCToKRTBijectionTypeA2Even as RCToKRTBijectionTypeA2Even
from sage.combinat.rigged_configurations.bij_type_D import KRTToRCBijectionTypeD as KRTToRCBijectionTypeD, RCToKRTBijectionTypeD as RCToKRTBijectionTypeD

class KRTToRCBijectionTypeDTwisted(KRTToRCBijectionTypeD, KRTToRCBijectionTypeA2Even):
    """
    Specific implementation of the bijection from KR tableaux to rigged
    configurations for type `D_{n+1}^{(2)}`.

    This inherits from type `C_n^{(1)}` and `D_n^{(1)}` because we use the
    same methods in some places.
    """
    def run(self, verbose: bool = False):
        """
        Run the bijection from a tensor product of KR tableaux to a rigged
        configuration for type `D_{n+1}^{(2)}`.

        INPUT:

        - ``tp_krt`` -- a tensor product of KR tableaux

        - ``verbose`` -- (default: ``False``) display each step in the
          bijection

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 2], [[3,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D_twisted import KRTToRCBijectionTypeDTwisted
            sage: KRTToRCBijectionTypeDTwisted(KRT(pathlist=[[-1,3,2]])).run()
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            1[ ]1
            <BLANKLINE>
        """
    def next_state(self, val) -> None:
        """
        Build the next state for type `D_{n+1}^{(2)}`.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 2], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D_twisted import KRTToRCBijectionTypeDTwisted
            sage: bijection = KRTToRCBijectionTypeDTwisted(KRT(pathlist=[[-1,2]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [2])
            sage: bijection.next_state(2)
        """

class RCToKRTBijectionTypeDTwisted(RCToKRTBijectionTypeD, RCToKRTBijectionTypeA2Even):
    """
    Specific implementation of the bijection from rigged configurations to
    tensor products of KR tableaux for type `D_{n+1}^{(2)}`.
    """
    def run(self, verbose: bool = False, build_graph: bool = False):
        """
        Run the bijection from rigged configurations to tensor product of KR
        tableaux for type `D_{n+1}^{(2)}`.

        INPUT:

        - ``verbose`` -- boolean (default: ``False``); display each step in the
          bijection
        - ``build_graph`` -- boolean (default: ``False``); build the graph of each
          step of the bijection

        EXAMPLES::

            sage: RC = RiggedConfigurations(['D', 4, 2], [[3, 1]])
            sage: x = RC(partition_list=[[],[1],[1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D_twisted import RCToKRTBijectionTypeDTwisted
            sage: RCToKRTBijectionTypeDTwisted(x).run()
            [[1], [3], [-2]]
            sage: bij = RCToKRTBijectionTypeDTwisted(x)
            sage: bij.run(build_graph=True)
            [[1], [3], [-2]]
            sage: bij._graph
            Digraph on 6 vertices
        """
    def next_state(self, height):
        """
        Build the next state for type `D_{n+1}^{(2)}`.

        TESTS::

            sage: RC = RiggedConfigurations(['D', 4, 2], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D_twisted import RCToKRTBijectionTypeDTwisted
            sage: bijection = RCToKRTBijectionTypeDTwisted(RC(partition_list=[[2],[2,2],[2,2]]))
            sage: bijection.next_state(0)
            -1
        """
