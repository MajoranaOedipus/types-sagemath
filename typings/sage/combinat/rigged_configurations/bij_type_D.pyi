from sage.combinat.rigged_configurations.bij_type_A import KRTToRCBijectionTypeA as KRTToRCBijectionTypeA, RCToKRTBijectionTypeA as RCToKRTBijectionTypeA

class KRTToRCBijectionTypeD(KRTToRCBijectionTypeA):
    """
    Specific implementation of the bijection from KR tableaux to rigged
    configurations for type `D_n^{(1)}`.

    This inherits from type `A_n^{(1)}` because we use the same methods in
    some places.
    """
    def run(self, verbose: bool = False):
        """
        Run the bijection from a tensor product of KR tableaux to a rigged
        configuration for type `D_n^{(1)}`.

        INPUT:

        - ``tp_krt`` -- a tensor product of KR tableaux

        - ``verbose`` -- (default: ``False``) display each step in the
          bijection

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D import KRTToRCBijectionTypeD
            sage: KRTToRCBijectionTypeD(KRT(pathlist=[[-3,2]])).run()
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            2[ ]2
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
        """
    def next_state(self, val) -> None:
        """
        Build the next state for type `D_n^{(1)}`.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[2,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D import KRTToRCBijectionTypeD
            sage: bijection = KRTToRCBijectionTypeD(KRT(pathlist=[[5,3]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [3])
            sage: bijection.next_state(3)
        """
    def doubling_map(self) -> None:
        """
        Perform the doubling map of the rigged configuration at the current
        state of the bijection.

        This is the map `B(\\Lambda) \\hookrightarrow B(2 \\Lambda)` which
        doubles each of the rigged partitions and updates the vacancy numbers
        accordingly.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[4,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D import KRTToRCBijectionTypeD
            sage: bijection = KRTToRCBijectionTypeD(KRT(pathlist=[[-1,4,3,2]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [2])
            sage: bijection.next_state(2)
            sage: bijection.ret_rig_con
            <BLANKLINE>
            -2[ ]-2
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            sage: bijection.cur_dims
            [[0, 1]]
            sage: bijection.doubling_map()
            sage: bijection.ret_rig_con
            <BLANKLINE>
            -4[ ][ ]-4
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            sage: bijection.cur_dims
            [[0, 2]]
        """
    def halving_map(self) -> None:
        """
        Perform the halving map of the rigged configuration at the current
        state of the bijection.

        This is the inverse map to `B(\\Lambda) \\hookrightarrow B(2 \\Lambda)`
        which halves each of the rigged partitions and updates the vacancy
        numbers accordingly.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[4,1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D import KRTToRCBijectionTypeD
            sage: bijection = KRTToRCBijectionTypeD(KRT(pathlist=[[-1,4,3,2]]))
            sage: bijection.cur_path.insert(0, [])
            sage: bijection.cur_dims.insert(0, [0, 1])
            sage: bijection.cur_path[0].insert(0, [2])
            sage: bijection.next_state(2)
            sage: test = bijection.ret_rig_con
            sage: bijection.doubling_map()
            sage: bijection.halving_map()
            sage: test == bijection.ret_rig_con
            True
        """

class RCToKRTBijectionTypeD(RCToKRTBijectionTypeA):
    """
    Specific implementation of the bijection from rigged configurations to tensor products of KR tableaux for type `D_n^{(1)}`.
    """
    def run(self, verbose: bool = False, build_graph: bool = False):
        """
        Run the bijection from rigged configurations to tensor product of KR
        tableaux for type `D_n^{(1)}`.

        INPUT:

        - ``verbose`` -- boolean (default: ``False``); display each step in the
          bijection
        - ``build_graph`` -- boolean (default: ``False``); build the graph of each
          step of the bijection

        EXAMPLES::

            sage: RC = RiggedConfigurations(['D', 4, 1], [[2, 1]])
            sage: x = RC(partition_list=[[1],[1],[1],[1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D import RCToKRTBijectionTypeD
            sage: RCToKRTBijectionTypeD(x).run()
            [[2], [-3]]
            sage: bij = RCToKRTBijectionTypeD(x)
            sage: bij.run(build_graph=True)
            [[2], [-3]]
            sage: bij._graph
            Digraph on 3 vertices
        """
    def next_state(self, height):
        """
        Build the next state for type `D_n^{(1)}`.

        TESTS::

            sage: RC = RiggedConfigurations(['D', 4, 1], [[2, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D import RCToKRTBijectionTypeD
            sage: bijection = RCToKRTBijectionTypeD(RC(partition_list=[[],[1,1],[1],[1]]))
            sage: bijection.next_state(0)
            1
        """
    def doubling_map(self) -> None:
        """
        Perform the doubling map of the rigged configuration at the current
        state of the bijection.

        This is the map `B(\\Lambda) \\hookrightarrow B(2 \\Lambda)` which
        doubles each of the rigged partitions and updates the vacancy numbers
        accordingly.

        TESTS::

            sage: RC = RiggedConfigurations(['D', 4, 1], [[4, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D import RCToKRTBijectionTypeD
            sage: bijection = RCToKRTBijectionTypeD(RC(partition_list=[[],[],[],[1]]))
            sage: bijection.cur_partitions
            [(/)
             , (/)
             , (/)
             , -1[ ]-1
             ]
            sage: bijection.doubling_map()
            sage: bijection.cur_partitions
            [(/)
             , (/)
             , (/)
             , -2[ ][ ]-2
             ]
        """
    def halving_map(self) -> None:
        """
        Perform the halving map of the rigged configuration at the current
        state of the bijection.

        This is the inverse map to `B(\\Lambda) \\hookrightarrow B(2 \\Lambda)`
        which halves each of the rigged partitions and updates the vacancy
        numbers accordingly.

        TESTS::

            sage: RC = RiggedConfigurations(['D', 4, 1], [[4, 1]])
            sage: from sage.combinat.rigged_configurations.bij_type_D import RCToKRTBijectionTypeD
            sage: bijection = RCToKRTBijectionTypeD(RC(partition_list=[[],[],[],[1]]))
            sage: test = bijection.cur_partitions
            sage: bijection.doubling_map()
            sage: bijection.halving_map()
            sage: test == bijection.cur_partitions
            True
        """
