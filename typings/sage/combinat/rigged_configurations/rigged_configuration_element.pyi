from sage.combinat.rigged_configurations.rigged_partition import RiggedPartition as RiggedPartition, RiggedPartitionTypeB as RiggedPartitionTypeB
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.list_clone import ClonableArray as ClonableArray

class RiggedConfigurationElement(ClonableArray):
    """
    A rigged configuration for simply-laced types.

    For more information on rigged configurations, see
    :class:`RiggedConfigurations`. For rigged configurations for
    non-simply-laced types, use :class:`RCNonSimplyLacedElement`.

    Typically to create a specific rigged configuration, the user will pass in
    the optional argument ``partition_list`` and if the user wants to specify
    the rigging values, give the optional argument ``rigging_list`` as well.
    If ``rigging_list`` is not passed, the rigging values are set to the
    corresponding vacancy numbers.

    INPUT:

    - ``parent`` -- the parent of this element

    - ``rigged_partitions`` -- list of rigged partitions

    There are two optional arguments to explicitly construct a rigged
    configuration. The first is ``partition_list`` which gives a list of
    partitions, and the second is ``rigging_list`` which is a list of
    corresponding lists of riggings. If only partition_list is specified,
    then it sets the rigging equal to the calculated vacancy numbers.

    If we are constructing a rigged configuration from a rigged configuration
    (say of another type) and we don't want to recompute the vacancy numbers,
    we can use the ``use_vacancy_numbers`` to avoid the recomputation.

    EXAMPLES:

    Type `A_n^{(1)}` examples::

        sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 2]])
        sage: RC(partition_list=[[2], [2, 2], [2], [2]])
        <BLANKLINE>
        0[ ][ ]0
        <BLANKLINE>
        -2[ ][ ]-2
        -2[ ][ ]-2
        <BLANKLINE>
        2[ ][ ]2
        <BLANKLINE>
        -2[ ][ ]-2
        <BLANKLINE>

        sage: RC = RiggedConfigurations(['A', 4, 1], [[1, 1], [1, 1]])
        sage: RC(partition_list=[[], [], [], []])
        <BLANKLINE>
        (/)
        <BLANKLINE>
        (/)
        <BLANKLINE>
        (/)
        <BLANKLINE>
        (/)
        <BLANKLINE>

    Type `D_n^{(1)}` examples::

        sage: RC = RiggedConfigurations(['D', 4, 1], [[2, 2]])
        sage: RC(partition_list=[[3], [3,2], [4], [3]])
        <BLANKLINE>
        -1[ ][ ][ ]-1
        <BLANKLINE>
        1[ ][ ][ ]1
        0[ ][ ]0
        <BLANKLINE>
        -3[ ][ ][ ][ ]-3
        <BLANKLINE>
        -1[ ][ ][ ]-1
        <BLANKLINE>

        sage: RC = RiggedConfigurations(['D', 4, 1], [[1, 1], [2, 1]])
        sage: RC(partition_list=[[1], [1,1], [1], [1]])
        <BLANKLINE>
        1[ ]1
        <BLANKLINE>
        0[ ]0
        0[ ]0
        <BLANKLINE>
        0[ ]0
        <BLANKLINE>
        0[ ]0
        <BLANKLINE>
        sage: elt = RC(partition_list=[[1], [1,1], [1], [1]], rigging_list=[[0], [0,0], [0], [0]]); elt
        <BLANKLINE>
        1[ ]0
        <BLANKLINE>
        0[ ]0
        0[ ]0
        <BLANKLINE>
        0[ ]0
        <BLANKLINE>
        0[ ]0
        <BLANKLINE>

        sage: from sage.combinat.rigged_configurations.rigged_partition import RiggedPartition
        sage: RC2 = RiggedConfigurations(['D', 5, 1], [[2, 1], [3, 1]])
        sage: l = [RiggedPartition()] + list(elt)
        sage: ascii_art(RC2(*l))
        (/)  1[ ]0  0[ ]0  0[ ]0  0[ ]0
                    0[ ]0
        sage: ascii_art(RC2(*l, use_vacancy_numbers=True))
        (/)  1[ ]0  0[ ]0  0[ ]0  0[ ]0
                    0[ ]0
    """
    def __init__(self, parent, rigged_partitions=[], **options) -> None:
        """
        Construct a rigged configuration element.

        .. WARNING::

            This changes the vacancy numbers of the rigged partitions, so
            if the rigged partitions comes from another rigged configuration,
            a deep copy should be made before being passed here. We do not
            make a deep copy here because the crystal operators generate
            their own rigged partitions. See :issue:`17054`.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 1]])
            sage: RC(partition_list=[[], [], [], []])
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            sage: RC(partition_list=[[1], [1], [], []])
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            sage: elt = RC(partition_list=[[1], [1], [], []], rigging_list=[[-1], [0], [], []]); elt
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            sage: TestSuite(elt).run()
        """
    def check(self) -> None:
        """
        Check the rigged configuration is properly defined.

        There is nothing to check here.

        EXAMPLES::

            sage: RC = crystals.infinity.RiggedConfigurations(['A', 4])
            sage: b = RC.module_generators[0].f_string([1,2,1,1,2,4,2,3,3,2])
            sage: b.check()
        """
    def nu(self):
        """
        Return the list `\\nu` of rigged partitions of this rigged
        configuration element.

        OUTPUT: the `\\nu` array as a list

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 2]])
            sage: RC(partition_list=[[2], [2,2], [2], [2]]).nu()
            [0[ ][ ]0
             , -2[ ][ ]-2
             -2[ ][ ]-2
             , 2[ ][ ]2
             , -2[ ][ ]-2
             ]
        """
    def e(self, a):
        """
        Return the action of the crystal operator `e_a` on ``self``.

        This implements the method defined in [CrysStructSchilling06]_ which
        finds the value `k` which is  the length of the string with the
        smallest negative rigging of smallest length. Then it removes a box
        from a string of length `k` in the `a`-th rigged partition, keeping all
        colabels fixed and increasing the new label by one. If no such string
        exists, then `e_a` is undefined.

        This method can also be used when the underlying Cartan matrix is a
        Borcherds-Cartan matrix.  In this case, then method of [SS2018]_ is
        used, where the new label is increased by half of the `a`-th diagonal
        entry of the underlying Borcherds-Cartan matrix.  This method will also
        return ``None`` if `a` is imaginary and the smallest rigging in the
        `a`-th rigged partition is not exactly half of the `a`-th diagonal entry
        of the Borcherds-Cartan matrix.

        INPUT:

        - ``a`` -- the index of the partition to remove a box

        OUTPUT: the resulting rigged configuration element

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2,1]])
            sage: elt = RC(partition_list=[[1], [1], [1], [1]])
            sage: elt.e(3)
            sage: elt.e(1)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>

            sage: A = CartanMatrix([[-2,-1],[-1,-2]], borcherds=True)
            sage: RC = crystals.infinity.RiggedConfigurations(A)
            sage: nu0 = RC(partition_list=[[],[]])
            sage: nu = nu0.f_string([1,0,0,0])
            sage: ascii_art(nu.e(0))
            5[ ]3  4[ ]3
            5[ ]1
        """
    def f(self, a):
        """
        Return the action of the crystal operator `f_a` on ``self``.

        This implements the method defined in [CrysStructSchilling06]_ which
        finds the value `k` which is the length of the string with the
        smallest nonpositive rigging of largest length. Then it adds a box from
        a string of length `k` in the `a`-th rigged partition, keeping all
        colabels fixed and decreasing the new label by one. If no such string
        exists, then it adds a new string of length 1 with label `-1`. However
        we need to modify the definition to work for `B(\\infty)` by removing
        the condition that the resulting rigged configuration is valid.

        This method can also be used when the underlying Cartan matrix is a
        Borcherds-Cartan matrix.  In this case, then method of [SS2018]_ is
        used, where the new label is decreased by half of the `a`-th diagonal
        entry of the underlying Borcherds-Cartan matrix.

        INPUT:

        - ``a`` -- the index of the partition to add a box

        OUTPUT: the resulting rigged configuration element

        EXAMPLES::

            sage: RC = crystals.infinity.RiggedConfigurations(['A', 3])
            sage: nu0 = RC.module_generators[0]
            sage: nu0.f(2)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            -2[ ]-1
            <BLANKLINE>
            (/)
            <BLANKLINE>

            sage: A = CartanMatrix([[-2,-1],[-1,-2]], borcherds=True)
            sage: RC = crystals.infinity.RiggedConfigurations(A)
            sage: nu0 = RC(partition_list=[[],[]])
            sage: nu = nu0.f_string([1,0,0,0])
            sage: ascii_art(nu.f(0))
            9[ ]7  6[ ]5
            9[ ]5
            9[ ]3
            9[ ]1
        """
    def epsilon(self, a):
        """
        Return `\\varepsilon_a` of ``self``.

        Let `x_{\\ell}` be the smallest string of `\\nu^{(a)}` or `0` if
        `\\nu^{(a)} = \\emptyset`, then we have
        `\\varepsilon_a = -\\min(0, x_{\\ell})`.

        EXAMPLES::

            sage: La = RootSystem(['B',2]).weight_lattice().fundamental_weights()
            sage: RC = crystals.RiggedConfigurations(La[1]+La[2])
            sage: I = RC.index_set()
            sage: matrix([[rc.epsilon(i) for i in I] for rc in RC[:4]])
            [0 0]
            [1 0]
            [0 1]
            [0 2]
        """
    def phi(self, a):
        """
        Return `\\varphi_a` of ``self``.

        Let `x_{\\ell}` be the smallest string of `\\nu^{(a)}` or `0` if
        `\\nu^{(a)} = \\emptyset`, then we have
        `\\varepsilon_a = p_{\\infty}^{(a)} - \\min(0, x_{\\ell})`.

        EXAMPLES::

            sage: La = RootSystem(['B',2]).weight_lattice().fundamental_weights()
            sage: RC = crystals.RiggedConfigurations(La[1]+La[2])
            sage: I = RC.index_set()
            sage: matrix([[rc.phi(i) for i in I] for rc in RC[:4]])
            [1 1]
            [0 3]
            [0 2]
            [1 1]
        """
    def vacancy_number(self, a, i):
        """
        Return the vacancy number `p_i^{(a)}`.

        INPUT:

        - ``a`` -- the index of the rigged partition

        - ``i`` -- the row of the rigged partition

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 2]])
            sage: elt = RC(partition_list=[[1], [2,1], [1], []])
            sage: elt.vacancy_number(2, 3)
            -2
            sage: elt.vacancy_number(2, 2)
            -2
            sage: elt.vacancy_number(2, 1)
            -1

            sage: RC = RiggedConfigurations(['D',4,1], [[2,1], [2,1]])
            sage: x = RC(partition_list=[[3], [3,1,1], [2], [3,1]]); ascii_art(x)
            -1[ ][ ][ ]-1  1[ ][ ][ ]1  0[ ][ ]0  -3[ ][ ][ ]-3
                           0[ ]0                  -1[ ]-1
                           0[ ]0
            sage: x.vacancy_number(2,2)
            1
        """
    def partition_rigging_lists(self):
        """
        Return the list of partitions and the associated list of riggings
        of ``self``.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A',3,1], [[1,2],[2,2]])
            sage: rc = RC(partition_list=[[2],[1],[1]], rigging_list=[[-1],[0],[-1]]); rc
            <BLANKLINE>
            -1[ ][ ]-1
            <BLANKLINE>
            1[ ]0
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            sage: rc.partition_rigging_lists()
            [[[2], [1], [1]], [[-1], [0], [-1]]]
        """

class RCNonSimplyLacedElement(RiggedConfigurationElement):
    """
    Rigged configuration elements for non-simply-laced types.

    TESTS::

        sage: vct = CartanType(['C',2,1]).as_folding()
        sage: RC = crystals.infinity.RiggedConfigurations(vct)
        sage: elt = RC.module_generators[0].f_string([1,0,2,2,0,1]); elt
        <BLANKLINE>
        -2[ ][ ]-1
        <BLANKLINE>
        -2[ ]-1
        -2[ ]-1
        <BLANKLINE>
        -2[ ][ ]-1
        <BLANKLINE>
        sage: TestSuite(elt).run()
    """
    def to_virtual_configuration(self):
        """
        Return the corresponding rigged configuration in the virtual crystal.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['C',2,1], [[1,2],[1,1],[2,1]])
            sage: elt = RC(partition_list=[[3],[2]]); elt
            <BLANKLINE>
            0[ ][ ][ ]0
            <BLANKLINE>
            0[ ][ ]0
            sage: elt.to_virtual_configuration()
            <BLANKLINE>
            0[ ][ ][ ]0
            <BLANKLINE>
            0[ ][ ][ ][ ]0
            <BLANKLINE>
            0[ ][ ][ ]0
        """
    def e(self, a):
        """
        Return the action of `e_a` on ``self``.

        This works by lifting into the virtual configuration, then applying

        .. MATH::

            e^v_a = \\prod_{j \\in \\iota(a)} \\hat{e}_j^{\\gamma_j}

        and pulling back.

        EXAMPLES::

            sage: vct = CartanType(['C',2,1]).as_folding()
            sage: RC = crystals.infinity.RiggedConfigurations(vct)
            sage: elt = RC(partition_list=[[2],[1,1],[2]], rigging_list=[[-1],[-1,-1],[-1]])
            sage: ascii_art(elt.e(0))
            0[ ]0  -2[ ]-1  -2[ ][ ]-1
                   -2[ ]-1
            sage: ascii_art(elt.e(1))
            -3[ ][ ]-2  0[ ]1  -3[ ][ ]-2
            sage: ascii_art(elt.e(2))
            -2[ ][ ]-1  -2[ ]-1  0[ ]0
                        -2[ ]-1
        """
    def f(self, a):
        """
        Return the action of `f_a` on ``self``.

        This works by lifting into the virtual configuration, then applying

        .. MATH::

            f^v_a = \\prod_{j \\in \\iota(a)} \\hat{f}_j^{\\gamma_j}

        and pulling back.

        EXAMPLES::

            sage: vct = CartanType(['C',2,1]).as_folding()
            sage: RC = crystals.infinity.RiggedConfigurations(vct)
            sage: elt = RC(partition_list=[[2],[1,1],[2]], rigging_list=[[-1],[-1,-1],[-1]])
            sage: ascii_art(elt.f(0))
            -4[ ][ ][ ]-2  -2[ ]-1  -2[ ][ ]-1
                           -2[ ]-1
            sage: ascii_art(elt.f(1))
            -1[ ][ ]0  -2[ ][ ]-2  -1[ ][ ]0
                       -2[ ]-1
            sage: ascii_art(elt.f(2))
            -2[ ][ ]-1  -2[ ]-1  -4[ ][ ][ ]-2
                        -2[ ]-1
        """

class RCHighestWeightElement(RiggedConfigurationElement):
    """
    Rigged configurations in highest weight crystals.

    TESTS::

        sage: La = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()
        sage: RC = crystals.RiggedConfigurations(['A',2,1], La[0])
        sage: elt = RC(partition_list=[[1,1],[1],[2]]); elt
        <BLANKLINE>
        -1[ ]-1
        -1[ ]-1
        <BLANKLINE>
        1[ ]1
        <BLANKLINE>
        -1[ ][ ]-1
        <BLANKLINE>
        sage: TestSuite(elt).run()
    """
    def check(self) -> None:
        """
        Make sure all of the riggings are less than or equal to the
        vacancy number.

        TESTS::

            sage: La = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()
            sage: RC = crystals.RiggedConfigurations(['A',2,1], La[0])
            sage: elt = RC(partition_list=[[1,1],[1],[2]])
            sage: elt.check()
        """
    def f(self, a):
        """
        Return the action of the crystal operator `f_a` on ``self``.

        This implements the method defined in [CrysStructSchilling06]_ which
        finds the value `k` which is  the length of the string with the
        smallest nonpositive rigging of largest length. Then it adds a box
        from a string of length `k` in the `a`-th rigged partition, keeping
        all colabels fixed and decreasing the new label by one. If no such
        string exists, then it adds a new string of length 1 with label `-1`.
        If any of the resulting vacancy numbers are larger than the labels
        (i.e. it is an invalid rigged configuration), then `f_a` is
        undefined.

        INPUT:

        - ``a`` -- the index of the partition to add a box

        OUTPUT: the resulting rigged configuration element

        EXAMPLES::

            sage: La = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()
            sage: RC = crystals.RiggedConfigurations(['A',2,1], La[0])
            sage: elt = RC(partition_list=[[1,1],[1],[2]])
            sage: elt.f(0)
            <BLANKLINE>
            -2[ ][ ]-2
            -1[ ]-1
            <BLANKLINE>
            1[ ]1
            <BLANKLINE>
            0[ ][ ]0
            <BLANKLINE>
            sage: elt.f(1)
            <BLANKLINE>
            0[ ]0
            0[ ]0
            <BLANKLINE>
            -1[ ]-1
            -1[ ]-1
            <BLANKLINE>
            0[ ][ ]0
            <BLANKLINE>
            sage: elt.f(2)
        """
    def weight(self):
        """
        Return the weight of ``self``.

        EXAMPLES::

            sage: La = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()
            sage: B = crystals.RiggedConfigurations(['A',2,1], La[0])
            sage: mg = B.module_generators[0]
            sage: mg.f_string([0,1,2,0]).weight()
            -Lambda[0] + Lambda[1] + Lambda[2] - 2*delta
        """

class RCHWNonSimplyLacedElement(RCNonSimplyLacedElement):
    """
    Rigged configurations in highest weight crystals.

    TESTS::

        sage: La = RootSystem(['C',2,1]).weight_lattice(extended=True).fundamental_weights()
        sage: vct = CartanType(['C',2,1]).as_folding()
        sage: RC = crystals.RiggedConfigurations(vct, La[0])
        sage: elt = RC(partition_list=[[1,1],[2],[2]]); ascii_art(elt)
        -1[ ]-1  2[ ][ ]2  -2[ ][ ]-2
        -1[ ]-1
        sage: TestSuite(elt).run()
    """
    def check(self) -> None:
        """
        Make sure all of the riggings are less than or equal to the
        vacancy number.

        TESTS::

            sage: La = RootSystem(['C',2,1]).weight_lattice(extended=True).fundamental_weights()
            sage: vct = CartanType(['C',2,1]).as_folding()
            sage: RC = crystals.RiggedConfigurations(vct, La[0])
            sage: elt = RC(partition_list=[[1,1],[2],[2]])
            sage: elt.check()
        """
    def f(self, a):
        """
        Return the action of `f_a` on ``self``.

        This works by lifting into the virtual configuration, then applying

        .. MATH::

            f^v_a = \\prod_{j \\in \\iota(a)} \\hat{f}_j^{\\gamma_j}

        and pulling back.

        EXAMPLES::

            sage: La = RootSystem(['C',2,1]).weight_lattice(extended=True).fundamental_weights()
            sage: vct = CartanType(['C',2,1]).as_folding()
            sage: RC = crystals.RiggedConfigurations(vct, La[0])
            sage: elt = RC(partition_list=[[1,1],[2],[2]])
            sage: elt.f(0)
            sage: ascii_art(elt.f(1))
            0[ ]0   0[ ][ ]0  -1[ ][ ]-1
            0[ ]0  -1[ ]-1
            sage: elt.f(2)
        """
    def weight(self):
        """
        Return the weight of ``self``.

        EXAMPLES::

            sage: La = RootSystem(['C',2,1]).weight_lattice(extended=True).fundamental_weights()
            sage: vct = CartanType(['C',2,1]).as_folding()
            sage: B = crystals.RiggedConfigurations(vct, La[0])
            sage: mg = B.module_generators[0]
            sage: mg.f_string([0,1,2]).weight()
            2*Lambda[1] - Lambda[2] - delta
        """

class KRRiggedConfigurationElement(RiggedConfigurationElement):
    """
    `U_q^{\\prime}(\\mathfrak{g})` rigged configurations.

    EXAMPLES:

    We can go between :class:`rigged configurations <RiggedConfigurations>`
    and tensor products of :class:`tensor products of KR tableaux
    <sage.combinat.rigged_configurations.tensor_product_kr_tableaux.TensorProductOfKirillovReshetikhinTableaux>`::

        sage: RC = RiggedConfigurations(['D', 4, 1], [[1,1], [2,1]])
        sage: rc_elt = RC(partition_list=[[1], [1,1], [1], [1]])
        sage: tp_krtab = rc_elt.to_tensor_product_of_kirillov_reshetikhin_tableaux(); tp_krtab
        [[-2]] (X) [[1], [2]]
        sage: tp_krcrys = rc_elt.to_tensor_product_of_kirillov_reshetikhin_crystals(); tp_krcrys
        [[[-2]], [[1], [2]]]
        sage: tp_krcrys == tp_krtab.to_tensor_product_of_kirillov_reshetikhin_crystals()
        True
        sage: RC(tp_krcrys) == rc_elt
        True
        sage: RC(tp_krtab) == rc_elt
        True
        sage: tp_krtab.to_rigged_configuration() == rc_elt
        True
    """
    def __init__(self, parent, rigged_partitions=[], **options) -> None:
        """
        Construct a rigged configuration element.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 1]])
            sage: RC(partition_list=[[], [], [], []])
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            sage: RC(partition_list=[[1], [1], [], []])
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            sage: elt = RC(partition_list=[[1], [1], [], []], rigging_list=[[-1], [0], [], []]); elt
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            (/)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            sage: TestSuite(elt).run()
        """
    def check(self) -> None:
        """
        Make sure all of the riggings are less than or equal to the
        vacancy number.

        TESTS::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 1]])
            sage: elt = RC(partition_list=[[1], [1], [], []])
            sage: elt.check()
        """
    def e(self, a):
        """
        Return the action of the crystal operator `e_a` on ``self``.

        For the classical operators, this implements the method defined
        in [CrysStructSchilling06]_. For `e_0`, this converts the class to
        a tensor product of KR tableaux and does the corresponding `e_0`
        and pulls back.

        .. TODO::

            Implement `e_0` without appealing to tensor product of
            KR tableaux.

        INPUT:

        - ``a`` -- the index of the partition to remove a box

        OUTPUT: the resulting rigged configuration element

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2,1]])
            sage: elt = RC(partition_list=[[1], [1], [1], [1]])
            sage: elt.e(3)
            sage: elt.e(1)
            <BLANKLINE>
            (/)
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
        """
    def f(self, a):
        """
        Return the action of the crystal operator `f_a` on ``self``.

        For the classical operators, this implements the method defined
        in [CrysStructSchilling06]_. For `f_0`, this converts the class to
        a tensor product of KR tableaux and does the corresponding `f_0`
        and pulls back.

        .. TODO::

            Implement `f_0` without appealing to tensor product of
            KR tableaux.

        INPUT:

        - ``a`` -- the index of the partition to add a box

        OUTPUT: the resulting rigged configuration element

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2,1]])
            sage: elt = RC(partition_list=[[1], [1], [1], [1]])
            sage: elt.f(1)
            sage: elt.f(2)
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            -1[ ]-1
            -1[ ]-1
            <BLANKLINE>
            1[ ]1
            <BLANKLINE>
            -1[ ]-1
            <BLANKLINE>
        """
    def epsilon(self, a):
        """
        Return `\\varepsilon_a` of ``self``.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['D', 4, 1], [[2, 2]])
            sage: I = RC.index_set()
            sage: matrix([[mg.epsilon(i) for i in I] for mg in RC.module_generators])
            [4 0 0 0 0]
            [3 0 0 0 0]
            [2 0 0 0 0]
        """
    def phi(self, a):
        """
        Return `\\varphi_a` of ``self``.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['D', 4, 1], [[2, 2]])
            sage: I = RC.index_set()
            sage: matrix([[mg.phi(i) for i in I] for mg in RC.module_generators])
            [0 0 2 0 0]
            [1 0 1 0 0]
            [2 0 0 0 0]
        """
    def weight(self):
        """
        Return the weight of ``self``.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['E', 6, 1], [[2,2]])
            sage: [x.weight() for x in RC.module_generators]
            [-4*Lambda[0] + 2*Lambda[2], -2*Lambda[0] + Lambda[2], 0]
            sage: KR = crystals.KirillovReshetikhin(['E',6,1], 2,2)
            sage: [x.weight() for x in KR.module_generators]  # long time
            [0, -2*Lambda[0] + Lambda[2], -4*Lambda[0] + 2*Lambda[2]]

            sage: RC = RiggedConfigurations(['D', 6, 1], [[4,2]])
            sage: [x.weight() for x in RC.module_generators]
            [-4*Lambda[0] + 2*Lambda[4], -4*Lambda[0] + Lambda[2] + Lambda[4],
             -2*Lambda[0] + Lambda[4], -4*Lambda[0] + 2*Lambda[2],
             -2*Lambda[0] + Lambda[2], 0]
        """
    @cached_method
    def classical_weight(self):
        """
        Return the classical weight of ``self``.

        The classical weight `\\Lambda` of a rigged configuration is

        .. MATH::

            \\Lambda = \\sum_{a \\in \\overline{I}} \\sum_{i > 0}
            i L_i^{(a)} \\Lambda_a - \\sum_{a \\in \\overline{I}} \\sum_{i > 0}
            i m_i^{(a)} \\alpha_a.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['D',4,1], [[2,2]])
            sage: elt = RC(partition_list=[[2],[2,1],[1],[1]])
            sage: elt.classical_weight()
            (0, 1, 1, 0)

        This agrees with the corresponding classical weight as KR tableaux::

            sage: krt = elt.to_tensor_product_of_kirillov_reshetikhin_tableaux(); krt
            [[2, 1], [3, -1]]
            sage: krt.classical_weight() == elt.classical_weight()
            True

        TESTS:

        We check the classical weights agree in an entire crystal::

            sage: RC = RiggedConfigurations(['A',2,1], [[2,1], [1,1]])
            sage: for x in RC:
            ....:     y = x.to_tensor_product_of_kirillov_reshetikhin_tableaux()
            ....:     assert x.classical_weight() == y.classical_weight()
        """
    def to_tensor_product_of_kirillov_reshetikhin_tableaux(self, display_steps: bool = False, build_graph: bool = False):
        """
        Perform the bijection from this rigged configuration to a tensor
        product of Kirillov-Reshetikhin tableaux given in [RigConBijection]_
        for single boxes and with [BijectionLRT]_ and [BijectionDn]_ for
        multiple columns and rows.

        .. NOTE::

            This is only proven to be a bijection in types `A_n^{(1)}`
            and `D_n^{(1)}`, as well as `\\bigotimes_i B^{r_i,1}` and
            `\\bigotimes_i B^{1,s_i}` for general affine types.

        INPUT:

        - ``display_steps`` -- boolean (default: ``False``); indicates whether
          to print each step in the algorithm
        - ``build_graph`` -- boolean (default: ``False``); indicates whether
          to construct and return a graph of the bijection whose
          vertices are rigged configurations obtained at each step and edges
          are labeled by either the return value of `\\delta` or the
          doubling/halving map

        OUTPUT:

        - The tensor product of KR tableaux element corresponding to this
          rigged configuration.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 4, 1], [[2, 2]])
            sage: RC(partition_list=[[2], [2,2], [2], [2]]).to_tensor_product_of_kirillov_reshetikhin_tableaux()
            [[3, 3], [5, 5]]
            sage: RC = RiggedConfigurations(['D', 4, 1], [[2, 2]])
            sage: elt = RC(partition_list=[[2], [2,2], [1], [1]])
            sage: tp_krt = elt.to_tensor_product_of_kirillov_reshetikhin_tableaux(); tp_krt
            [[2, 3], [3, -2]]

        This is invertible by calling
        :meth:`~sage.combinat.rigged_configurations.tensor_product_kr_tableaux_element.TensorProductOfKirillovReshetikhinTableauxElement.to_rigged_configuration()`::

            sage: ret = tp_krt.to_rigged_configuration(); ret
            <BLANKLINE>
            0[ ][ ]0
            <BLANKLINE>
            -2[ ][ ]-2
            -2[ ][ ]-2
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            sage: elt == ret
            True

        To view the steps of the bijection in the output, run with
        the ``display_steps=True`` option::

            sage: elt.to_tensor_product_of_kirillov_reshetikhin_tableaux(True)
            ====================
            ...
            ====================
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            -2[ ][ ]-2
             0[ ]0
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            --------------------
            [[3, 2]]
            --------------------
            ...
            [[2, 3], [3, -2]]

        We can also construct and display a graph of the bijection
        as follows::

            sage: ret, G = elt.to_tensor_product_of_kirillov_reshetikhin_tableaux(build_graph=True)
            sage: view(G) # not tested
        """
    def to_tensor_product_of_kirillov_reshetikhin_crystals(self, display_steps: bool = False, build_graph: bool = False):
        """
        Return the corresponding tensor product of Kirillov-Reshetikhin
        crystals.

        This is a composition of the map to a tensor product of KR tableaux,
        and then to a tensor product of KR crystals.

        INPUT:

        - ``display_steps`` -- boolean (default: ``False``); indicates whether
          to print each step in the algorithm
        - ``build_graph`` -- boolean (default: ``False``); indicates whether
          to construct and return a graph of the bijection whose
          vertices are rigged configurations obtained at each step and edges
          are labeled by either the return value of `\\delta` or the
          doubling/halving map

        EXAMPLES::

            sage: RC = RiggedConfigurations(['D', 4, 1], [[2, 2]])
            sage: elt = RC(partition_list=[[2], [2,2], [1], [1]])
            sage: krc = elt.to_tensor_product_of_kirillov_reshetikhin_crystals(); krc
            [[[2, 3], [3, -2]]]

        We can recover the rigged configuration::

            sage: ret = RC(krc); ret
            <BLANKLINE>
            0[ ][ ]0
            <BLANKLINE>
            -2[ ][ ]-2
            -2[ ][ ]-2
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            sage: elt == ret
            True

        We can also construct and display a graph of the bijection
        as follows::

            sage: ret, G = elt.to_tensor_product_of_kirillov_reshetikhin_crystals(build_graph=True)
            sage: view(G) # not tested
        """
    def left_split(self):
        """
        Return the image of ``self`` under the left column splitting
        map `\\beta`.

        Consider the map `\\beta : RC(B^{r,s} \\otimes B) \\to RC(B^{r,1}
        \\otimes B^{r,s-1} \\otimes B)` for `s > 1` which is a natural classical
        crystal injection. On rigged configurations, the map `\\beta` does
        nothing (except possibly changing the vacancy numbers).

        EXAMPLES::

            sage: RC = RiggedConfigurations(['C',4,1], [[3,3]])
            sage: mg = RC.module_generators[-1]
            sage: ascii_art(mg)
            0[ ][ ]0  0[ ][ ]0  0[ ][ ]0  0[ ]0
                      0[ ][ ]0  0[ ][ ]0  0[ ]0
                                0[ ][ ]0  0[ ]0
            sage: ascii_art(mg.left_split())
            0[ ][ ]0  0[ ][ ]0  1[ ][ ]0  0[ ]0
                      0[ ][ ]0  1[ ][ ]0  0[ ]0
                                1[ ][ ]0  0[ ]0
        """
    def right_split(self):
        """
        Return the image of ``self`` under the right column splitting
        map `\\beta^*`.

        Let `\\theta` denote the
        :meth:`complement rigging map<complement_rigging>` which reverses
        the tensor factors and `\\beta` denote the
        :meth:`left splitting map<left_split>`, we define the right
        splitting map by `\\beta^* := \\theta \\circ \\beta \\circ \\theta`.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['C',4,1], [[3,3]])
            sage: mg = RC.module_generators[-1]
            sage: ascii_art(mg)
            0[ ][ ]0  0[ ][ ]0  0[ ][ ]0  0[ ]0
                      0[ ][ ]0  0[ ][ ]0  0[ ]0
                                0[ ][ ]0  0[ ]0
            sage: ascii_art(mg.right_split())
            0[ ][ ]0  0[ ][ ]0  1[ ][ ]1  0[ ]0
                      0[ ][ ]0  1[ ][ ]1  0[ ]0
                                1[ ][ ]1  0[ ]0

            sage: RC = RiggedConfigurations(['D',4,1], [[2,2],[1,2]])
            sage: elt = RC(partition_list=[[3,1], [2,2,1], [2,1], [2]])
            sage: ascii_art(elt)
            -1[ ][ ][ ]-1  0[ ][ ]0  -1[ ][ ]-1  1[ ][ ]1
             0[ ]0         0[ ][ ]0  -1[ ]-1
                           0[ ]0
            sage: ascii_art(elt.right_split())
            -1[ ][ ][ ]-1  0[ ][ ]0  -1[ ][ ]-1  1[ ][ ]1
             1[ ]0         0[ ][ ]0  -1[ ]-1
                           0[ ]0

        We check that the bijection commutes with the right splitting map::

            sage: RC = RiggedConfigurations(['A', 3, 1], [[1,1], [2,2]])
            sage: all(rc.right_split().to_tensor_product_of_kirillov_reshetikhin_tableaux()
            ....:     == rc.to_tensor_product_of_kirillov_reshetikhin_tableaux().right_split() for rc in RC)
            True
        """
    def left_box(self, return_b: bool = False):
        """
        Return the image of ``self`` under the left box removal map `\\delta`.

        The map `\\delta : RC(B^{r,1} \\otimes B) \\to RC(B^{r-1,1}
        \\otimes B)` (if `r = 1`, then we remove the left-most factor) is the
        basic map in the bijection `\\Phi` between rigged configurations and
        tensor products of Kirillov-Reshetikhin tableaux. For more
        information, see
        :meth:`to_tensor_product_of_kirillov_reshetikhin_tableaux()`.
        We can extend `\\delta` when the left-most factor is not a single
        column by precomposing with a :meth:`left_split()`.

        .. NOTE::

            Due to the special nature of the bijection for the spinor cases in
            types `D_n^{(1)}`, `B_n^{(1)}`, and `A_{2n-1}^{(2)}`, this map is
            not defined in these cases.

        INPUT:

        - ``return_b`` -- boolean (default: ``False``); whether to return the
          resulting letter from `\\delta`

        OUTPUT:

        The resulting rigged configuration or if ``return_b`` is ``True``,
        then a tuple of the resulting rigged configuration and the letter.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['C',4,1], [[3,2]])
            sage: mg = RC.module_generators[-1]
            sage: ascii_art(mg)
            0[ ][ ]0  0[ ][ ]0  0[ ][ ]0  0[ ]0
                      0[ ][ ]0  0[ ][ ]0  0[ ]0
                                0[ ][ ]0  0[ ]0
            sage: ascii_art(mg.left_box())
            0[ ]0  0[ ][ ]0  0[ ][ ]0  0[ ]0
                   0[ ]0     0[ ][ ]0  0[ ]0
            sage: x,b = mg.left_box(True)
            sage: b
            -1
            sage: b.parent()
            The crystal of letters for type ['C', 4]
        """
    delta = left_box
    def left_column_box(self):
        """
        Return the image of ``self`` under the left column box splitting
        map `\\gamma`.

        Consider the map `\\gamma : RC(B^{r,1} \\otimes B) \\to RC(B^{1,1}
        \\otimes B^{r-1,1} \\otimes B)` for `r > 1`, which is a natural strict
        classical crystal injection. On rigged configurations, the map
        `\\gamma` adds a singular string of length `1` to `\\nu^{(a)}`.

        We can extend `\\gamma` when the left-most factor is not a single
        column by precomposing with a :meth:`left_split()`.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['C',3,1], [[3,1], [2,1]])
            sage: mg = RC.module_generators[-1]
            sage: ascii_art(mg)
            0[ ]0  0[ ][ ]0  0[ ]0
                   0[ ]0     0[ ]0
            sage: ascii_art(mg.left_column_box())
            0[ ]0  0[ ][ ]0  0[ ]0
            0[ ]0  0[ ]0     0[ ]0
                   0[ ]0

            sage: RC = RiggedConfigurations(['C',3,1], [[2,1], [1,1], [3,1]])
            sage: mg = RC.module_generators[7]
            sage: ascii_art(mg)
            1[ ]0  0[ ][ ]0  0[ ]0
                   0[ ]0     0[ ]0
            sage: ascii_art(mg.left_column_box())
            1[ ]1  0[ ][ ]0  0[ ]0
            1[ ]0  0[ ]0     0[ ]0
        """
    def right_column_box(self):
        """
        Return the image of ``self`` under the right column box splitting
        map `\\gamma^*`.

        Consider the map `\\gamma^* : RC(B \\otimes B^{r,1}) \\to RC(B \\otimes
        B^{r-1,1} \\otimes B^{1,1})` for `r > 1`, which is a natural strict
        classical crystal injection. On rigged configurations, the map
        `\\gamma` adds a string of length `1` with rigging 0 to `\\nu^{(a)}`
        for all `a < r` to a classically highest weight element and extended
        as a classical crystal morphism.

        We can extend `\\gamma^*` when the right-most factor is not a single
        column by precomposing with a :meth:`right_split()`.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['C',3,1], [[2,1], [1,1], [3,1]])
            sage: mg = RC.module_generators[7]
            sage: ascii_art(mg)
            1[ ]0  0[ ][ ]0  0[ ]0
                   0[ ]0     0[ ]0
            sage: ascii_art(mg.right_column_box())
            1[ ]0  0[ ][ ]0  0[ ]0
            1[ ]0  0[ ]0     0[ ]0
                   0[ ]0
        """
    def complement_rigging(self, reverse_factors: bool = False):
        """
        Apply the complement rigging morphism `\\theta` to ``self``.

        Consider a highest weight rigged configuration `(\\nu, J)`, the
        complement rigging morphism `\\theta : RC(L) \\to RC(L)` is given by
        sending `(\\nu, J) \\mapsto (\\nu, J')`, where `J'` is obtained by
        taking the coriggings `x' = p_i^{(a)} - x`, and then extending as
        a crystal morphism. (The name comes from taking the complement
        partition for the riggings in a `m_i^{(a)} \\times p_i^{(a)}` box.)

        INPUT:

        - ``reverse_factors`` -- boolean (default: ``False``); if ``True``, then this
          returns an element in `RC(B')` where `B'` is the tensor factors
          of ``self`` in reverse order

        EXAMPLES::

            sage: RC = RiggedConfigurations(['D',4,1], [[1,1],[2,2]])
            sage: mg = RC.module_generators[-1]
            sage: ascii_art(mg)
            1[ ][ ]1  0[ ][ ]0  0[ ][ ]0  0[ ][ ]0
                      0[ ][ ]0
            sage: ascii_art(mg.complement_rigging())
            1[ ][ ]0  0[ ][ ]0  0[ ][ ]0  0[ ][ ]0
                      0[ ][ ]0

            sage: lw = mg.to_lowest_weight([1,2,3,4])[0]
            sage: ascii_art(lw)
            -1[ ][ ]-1  0[ ][ ]0  0[ ][ ]0  0[ ][ ]0
            -1[ ]-1     0[ ][ ]0  0[ ]0     0[ ]0
            -1[ ]-1     0[ ]0
                        0[ ]0
            sage: ascii_art(lw.complement_rigging())
            -1[ ][ ][ ]-1  0[ ][ ][ ]0  0[ ][ ][ ]0  0[ ][ ][ ]0
            -1[ ]-1        0[ ][ ][ ]0
            sage: lw.complement_rigging() == mg.complement_rigging().to_lowest_weight([1,2,3,4])[0]
            True

            sage: mg.complement_rigging(True).parent()
            Rigged configurations of type ['D', 4, 1] and factor(s) ((2, 2), (1, 1))

        We check that the Lusztig involution (under the modification of also
        mapping to the highest weight element) intertwines with the
        complement map `\\theta` (that reverses the tensor factors)
        under the bijection `\\Phi`::

            sage: RC = RiggedConfigurations(['D', 4, 1], [[2, 2], [2, 1], [1, 2]])
            sage: for mg in RC.module_generators: # long time
            ....:     y = mg.to_tensor_product_of_kirillov_reshetikhin_tableaux()
            ....:     hw = y.lusztig_involution().to_highest_weight([1,2,3,4])[0]
            ....:     c = mg.complement_rigging(True)
            ....:     hwc = c.to_tensor_product_of_kirillov_reshetikhin_tableaux()
            ....:     assert hw == hwc

        TESTS:

        We check that :issue:`18898` is fixed::

            sage: RC = RiggedConfigurations(['D',4,1], [[2,1], [2,1], [2,3]])
            sage: x = RC(partition_list=[[1], [1,1], [1], [1]], rigging_list=[[0], [2,1], [0], [0]])
            sage: ascii_art(x)
            0[ ]0  2[ ]2  0[ ]0  0[ ]0
                   2[ ]1
            sage: ascii_art(x.complement_rigging())
            0[ ]0  2[ ]1  0[ ]0  0[ ]0
                   2[ ]0
        """

class KRRCSimplyLacedElement(KRRiggedConfigurationElement):
    """
    `U_q^{\\prime}(\\mathfrak{g})` rigged configurations in simply-laced types.

    TESTS::

        sage: RC = RiggedConfigurations(['A', 3, 1], [[3, 2], [2,1], [1,1]])
        sage: elt = RC(partition_list=[[1], [1], []]); elt
        <BLANKLINE>
        0[ ]0
        <BLANKLINE>
        0[ ]0
        <BLANKLINE>
        (/)
        <BLANKLINE>
        sage: TestSuite(elt).run()
    """
    @cached_method
    def cocharge(self):
        """
        Compute the cocharge statistic of ``self``.

        Computes the cocharge statistic [CrysStructSchilling06]_ on this
        rigged configuration `(\\nu, J)`. The cocharge statistic is defined as:

        .. MATH::

            cc(\\nu, J) = \\frac{1}{2} \\sum_{a, b \\in I_0}
            \\sum_{j,k > 0} \\left( \\alpha_a \\mid \\alpha_b \\right)
            \\min(j, k) m_j^{(a)} m_k^{(b)}
            + \\sum_{a \\in I} \\sum_{i > 0} \\left\\lvert J^{(a, i)} \\right\\rvert.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 3, 1], [[3, 2], [2,1], [1,1]])
            sage: RC(partition_list=[[1], [1], []]).cocharge()
            1
        """
    cc = cocharge
    @cached_method
    def charge(self):
        """
        Compute the charge statistic of ``self``.

        Let `B` denote a set of rigged configurations. The *charge* `c` of
        a rigged configuration `b` is computed as

        .. MATH::

            c(b) = \\max(cc(b) \\mid b \\in B) - cc(b).

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A', 3, 1], [[3, 2], [2,1], [1,1]])
            sage: RC(partition_list=[[],[],[]]).charge()
            2
            sage: RC(partition_list=[[1], [1], []]).charge()
            1
        """

class KRRCNonSimplyLacedElement(KRRiggedConfigurationElement, RCNonSimplyLacedElement):
    """
    `U_q^{\\prime}(\\mathfrak{g})` rigged configurations in non-simply-laced
    types.

    TESTS::

        sage: RC = RiggedConfigurations(['C',2,1], [[1,2],[1,1],[2,1]])
        sage: elt = RC(partition_list=[[3],[2]]); elt
        <BLANKLINE>
        0[ ][ ][ ]0
        <BLANKLINE>
        0[ ][ ]0
        sage: TestSuite(elt).run()
    """
    def e(self, a):
        """
        Return the action of `e_a` on ``self``.

        This works by lifting into the virtual configuration, then applying

        .. MATH::

            e^v_a = \\prod_{j \\in \\iota(a)} \\hat{e}_j^{\\gamma_j}

        and pulling back.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A',6,2], [[1,1]]*7)
            sage: elt = RC(partition_list=[[1]*5,[2,1,1],[3,2]])
            sage: elt.e(3)
            <BLANKLINE>
            0[ ]0
            0[ ]0
            0[ ]0
            0[ ]0
            0[ ]0
            <BLANKLINE>
            0[ ][ ]0
            1[ ]1
            1[ ]1
            <BLANKLINE>
            1[ ][ ]1
            1[ ]0
            <BLANKLINE>
        """
    def f(self, a):
        """
        Return the action of `f_a` on ``self``.

        This works by lifting into the virtual configuration, then applying

        .. MATH::

            f^v_a = \\prod_{j \\in \\iota(a)} \\hat{f}_j^{\\gamma_j}

        and pulling back.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['A',6,2], [[1,1]]*7)
            sage: elt = RC(partition_list=[[1]*5,[2,1,1],[2,1]], rigging_list=[[0]*5,[0,1,1],[1,0]])
            sage: elt.f(3)
            <BLANKLINE>
            0[ ]0
            0[ ]0
            0[ ]0
            0[ ]0
            0[ ]0
            <BLANKLINE>
            1[ ][ ]1
            1[ ]1
            1[ ]1
            <BLANKLINE>
            -1[ ][ ][ ]-1
             0[ ][ ]0
            <BLANKLINE>
        """
    @cached_method
    def cocharge(self):
        """
        Compute the cocharge statistic.

        Computes the cocharge statistic [OSS03]_ on this
        rigged configuration `(\\nu, J)` by computing the cocharge as a virtual
        rigged configuration `(\\hat{\\nu}, \\hat{J})` and then using the
        identity `cc(\\hat{\\nu}, \\hat{J}) = \\gamma_0 cc(\\nu, J)`.

        EXAMPLES::

            sage: RC = RiggedConfigurations(['C', 3, 1], [[2,1], [1,1]])
            sage: RC(partition_list=[[1,1],[2,1],[1,1]]).cocharge()
            1
        """
    cc = cocharge

class KRRCTypeA2DualElement(KRRCNonSimplyLacedElement):
    """
    `U_q^{\\prime}(\\mathfrak{g})` rigged configurations in type
    `A_{2n}^{(2)\\dagger}`.
    """
    def epsilon(self, a):
        """
        Return the value of `\\varepsilon_a` of ``self``.

        Here we need to modify the usual definition by
        `\\varepsilon_n^{\\prime} := 2 \\varepsilon_n`.

        EXAMPLES::

            sage: RC = RiggedConfigurations(CartanType(['A',4,2]).dual(), [[1,1], [2,2]])
            sage: def epsilon(x, i):
            ....:     x = x.e(i)
            ....:     eps = 0
            ....:     while x is not None:
            ....:         x = x.e(i)
            ....:         eps = eps + 1
            ....:     return eps
            sage: all(epsilon(rc, 2) == rc.epsilon(2) for rc in RC)
            True
        """
    def phi(self, a):
        """
        Return the value of `\\varphi_a` of ``self``.

        Here we need to modify the usual definition by
        `\\varphi_n^{\\prime} := 2 \\varphi_n`.

        EXAMPLES::

            sage: RC = RiggedConfigurations(CartanType(['A',4,2]).dual(), [[1,1], [2,2]])
            sage: def phi(x, i):
            ....:     x = x.f(i)
            ....:     ph = 0
            ....:     while x is not None:
            ....:         x = x.f(i)
            ....:         ph = ph + 1
            ....:     return ph
            sage: all(phi(rc, 2) == rc.phi(2) for rc in RC)
            True
        """
    @cached_method
    def cocharge(self):
        """
        Compute the cocharge statistic.

        Computes the cocharge statistic [RigConBijection]_ on this
        rigged configuration `(\\nu, J)`. The cocharge statistic is
        computed as:

        .. MATH::

            cc(\\nu, J) = \\frac{1}{2} \\sum_{a \\in I_0} \\sum_{i > 0}
            t_a^{\\vee} m_i^{(a)} \\left( \\sum_{j > 0} \\min(i, j) L_j^{(a)}
            - p_i^{(a)} \\right) + \\sum_{a \\in I} t_a^{\\vee} \\sum_{i > 0}
            \\left\\lvert J^{(a, i)} \\right\\rvert.

        EXAMPLES::

            sage: RC = RiggedConfigurations(CartanType(['A',4,2]).dual(), [[1,1],[2,2]])
            sage: sc = RC.cartan_type().as_folding().scaling_factors()
            sage: all(mg.cocharge() * sc[0] == mg.to_virtual_configuration().cocharge()
            ....:     for mg in RC.module_generators)
            True
        """
    cc = cocharge
