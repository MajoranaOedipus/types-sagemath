from _typeshed import Incomplete
from sage.misc.abstract_method import abstract_method as abstract_method

class KRTToRCBijectionAbstract:
    """
    Root abstract class for the bijection from KR tableaux to rigged configurations.

    This class holds the state of the bijection and generates the next state.
    This class should never be created directly.
    """
    tp_krt: Incomplete
    n: Incomplete
    ret_rig_con: Incomplete
    cur_dims: Incomplete
    cur_path: Incomplete
    def __init__(self, tp_krt) -> None:
        """
        Initialize the bijection by obtaining the important information from
        the KR tableaux.

        INPUT:

        - ``parent`` -- the parent of tensor product of KR tableaux

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 4, 1], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA
            sage: bijection = KRTToRCBijectionTypeA(KRT(pathlist=[[3,1]]))
            sage: TestSuite(bijection).run()
        """
    def __eq__(self, rhs):
        """
        Check equality.

        This is only here for pickling check. This is a temporary placeholder
        class, and as such, should never be compared.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 4, 1], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA
            sage: bijection = KRTToRCBijectionTypeA(KRT(pathlist=[[5,3]]))
            sage: bijection2 = KRTToRCBijectionTypeA(KRT(pathlist=[[5,3]]))
            sage: bijection == bijection2
            True
        """
    def run(self, verbose: bool = False):
        """
        Run the bijection from a tensor product of KR tableaux to a rigged
        configuration.

        INPUT:

        - ``tp_krt`` -- a tensor product of KR tableaux

        - ``verbose`` -- (default: ``False``) display each step in the
          bijection

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 4, 1], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA
            sage: KRTToRCBijectionTypeA(KRT(pathlist=[[5,2]])).run()
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            1[ ]1
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
        """
    @abstract_method
    def next_state(self, val) -> None:
        """
        Build the next state in the bijection.

        INPUT:

        - ``val`` -- the value we are adding

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 4, 1], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA
            sage: bijection = KRTToRCBijectionTypeA(KRT(pathlist=[[5,3]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [3])
            sage: bijection.next_state(3)
            sage: bijection.ret_rig_con
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
        """

class RCToKRTBijectionAbstract:
    """
    Root abstract class for the bijection from rigged configurations to
    tensor product of Kirillov-Reshetikhin tableaux.

    This class holds the state of the bijection and generates the next state.
    This class should never be created directly.
    """
    rigged_con: Incomplete
    n: Incomplete
    KRT: Incomplete
    cur_dims: Incomplete
    cur_partitions: Incomplete
    def __init__(self, RC_element) -> None:
        """
        Initialize the bijection helper.

        INPUT:

        - ``RC_element`` -- the rigged configuration

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_abstract_class import RCToKRTBijectionAbstract
            sage: bijection = RCToKRTBijectionAbstract(RC(partition_list=[[1],[1],[1],[1]]))
            sage: TestSuite(bijection).run()
        """
    def __eq__(self, rhs):
        """
        Check equality.

        This is only here for pickling check. This is a temporary placeholder
        class, and as such, should never be compared.

        TESTS::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A import RCToKRTBijectionTypeA
            sage: bijection = RCToKRTBijectionTypeA(RC(partition_list=[[1],[1],[1],[1]]))
            sage: bijection2 = RCToKRTBijectionTypeA(RC(partition_list=[[1],[1],[1],[1]]))
            sage: bijection == bijection2
            True
        """
    def run(self, verbose: bool = False, build_graph: bool = False):
        """
        Run the bijection from rigged configurations to tensor product of KR
        tableaux.

        INPUT:

        - ``verbose`` -- boolean (default: ``False``); display each step in the
          bijection
        - ``build_graph`` -- boolean (default: ``False``); build the graph of each
          step of the bijection

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 1]])
            sage: x = RC(partition_list=[[1],[1],[1],[1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A import RCToKRTBijectionTypeA
            sage: RCToKRTBijectionTypeA(x).run()
            [[2], [5]]
            sage: bij = RCToKRTBijectionTypeA(x)
            sage: bij.run(build_graph=True)
            [[2], [5]]
            sage: bij._graph
            Digraph on 3 vertices
        """
    @abstract_method
    def next_state(self, height) -> None:
        """
        Build the next state in the bijection.

        TESTS::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_A import RCToKRTBijectionTypeA
            sage: bijection = RCToKRTBijectionTypeA(RC(partition_list=[[1],[1],[1],[1]]))
            sage: bijection.next_state(1)
            5
            sage: bijection.cur_partitions
            [(/)
             , (/)
             , (/)
             , (/)
             ]
        """
