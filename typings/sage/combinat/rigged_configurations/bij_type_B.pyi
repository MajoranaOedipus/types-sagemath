from _typeshed import Incomplete
from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA as KRTToRCBijectionTypeA
from sage.combinat.rigged_configurations.bij_type_C import KRTToRCBijectionTypeC as KRTToRCBijectionTypeC, RCToKRTBijectionTypeC as RCToKRTBijectionTypeC

class KRTToRCBijectionTypeB(KRTToRCBijectionTypeC):
    """
    Specific implementation of the bijection from KR tableaux to rigged
    configurations for type `B_n^{(1)}`.
    """
    ret_rig_con: Incomplete
    def run(self, verbose: bool = False):
        """
        Run the bijection from a tensor product of KR tableaux to a rigged
        configuration.

        INPUT:

        - ``tp_krt`` -- a tensor product of KR tableaux

        - ``verbose`` -- (default: ``False``) display each step in the
          bijection

        EXAMPLES::

            sage: from sage.combinat.rigged_configurations.bij_type_B import KRTToRCBijectionTypeB
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['B', 3, 1], [[2, 1]])
            sage: KRTToRCBijectionTypeB(KRT(pathlist=[[0,3]])).run()
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            -1[ ]-1
            -1[ ]-1
            <BLANKLINE>
            0[]0
            <BLANKLINE>
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['B', 3, 1], [[3, 1]])
            sage: KRTToRCBijectionTypeB(KRT(pathlist=[[-2,3,1]])).run()
            <BLANKLINE>
            (/)
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            0[]0
            <BLANKLINE>

        TESTS:

        Check that :issue:`19384` is fixed::

            sage: RC = RiggedConfigurations(['B',3,1], [[3,1],[3,1]])
            sage: RC._test_bijection()
            sage: RC = RiggedConfigurations(['B',3,1], [[1,1],[3,1],[1,1]])
            sage: RC._test_bijection()
        """
    def next_state(self, val) -> None:
        """
        Build the next state for type `B_n^{(1)}`.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['B', 3, 1], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_B import KRTToRCBijectionTypeB
            sage: bijection = KRTToRCBijectionTypeB(KRT(pathlist=[[-1,2]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [3])
            sage: bijection.next_state(3)
        """
    def other_outcome(self, rc, pos_val, width_n) -> None:
        """
        Do the other case `(QS)` possibility.

        This arises from the ambiguity when we found a singular string at the
        max width in `\\nu^{(n)}`. We had first attempted case `(S)`, and if
        that resulted in an invalid rigged configuration, we now
        finish the bijection using case `(QS)`.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['B',3,1], [[2,1],[1,2]])
            sage: rc = RC(partition_list=[[2,1], [2,1,1], [5,1]])
            sage: t = rc.to_tensor_product_of_kirillov_reshetikhin_tableaux()
            sage: t.to_rigged_configuration() == rc # indirect doctest
            True
        """

class RCToKRTBijectionTypeB(RCToKRTBijectionTypeC):
    """
    Specific implementation of the bijection from rigged configurations to
    tensor products of KR tableaux for type `B_n^{(1)}`.
    """
    cur_partitions: Incomplete
    def run(self, verbose: bool = False, build_graph: bool = False):
        """
        Run the bijection from rigged configurations to tensor product of KR
        tableaux for type `B_n^{(1)}`.

        INPUT:

        - ``verbose`` -- boolean (default: ``False``); display each step in the
          bijection
        - ``build_graph`` -- boolean (default: ``False``); build the graph of each
          step of the bijection

        EXAMPLES::

            sage: RC = RiggedConfigurations(['B', 3, 1], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_B import RCToKRTBijectionTypeB
            sage: RCToKRTBijectionTypeB(RC(partition_list=[[1],[1,1],[1]])).run()
            [[3], [0]]

            sage: RC = RiggedConfigurations(['B', 3, 1], [[3, 1]])
            sage: x = RC(partition_list=[[],[1],[1]])
            sage: RCToKRTBijectionTypeB(x).run()
            [[1], [3], [-2]]
            sage: bij = RCToKRTBijectionTypeB(x)
            sage: bij.run(build_graph=True)
            [[1], [3], [-2]]
            sage: bij._graph
            Digraph on 6 vertices
        """
    def next_state(self, height):
        """
        Build the next state for type `B_n^{(1)}`.

        TESTS::

            sage: RC = RiggedConfigurations(['B', 3, 1], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_B import RCToKRTBijectionTypeB
            sage: bijection = RCToKRTBijectionTypeB(RC(partition_list=[[1],[1,1],[1]]))
            sage: bijection.next_state(0)
            0
        """
