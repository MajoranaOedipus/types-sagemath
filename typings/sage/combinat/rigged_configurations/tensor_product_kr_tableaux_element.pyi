from sage.combinat.crystals.tensor_product import TensorProductOfRegularCrystalsElement as TensorProductOfRegularCrystalsElement

class TensorProductOfKirillovReshetikhinTableauxElement(TensorProductOfRegularCrystalsElement):
    """
    An element in a tensor product of Kirillov-Reshetikhin tableaux.

    For more on tensor product of Kirillov-Reshetikhin tableaux, see
    :class:`~sage.combinat.rigged_configurations.tensor_product_kr_tableaux.TensorProductOfKirillovReshetikhinTableaux`.

    The most common way to construct an element is to specify the option
    ``pathlist`` which is a list of lists which will be used to generate
    the individual factors of
    :class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableauxElement`.

    EXAMPLES:

    Type `A_n^{(1)}` examples::

        sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 3, 1], [[1,1], [2,1], [1,1], [2,1], [2,1], [2,1]])
        sage: T = KRT(pathlist=[[2], [4,1], [3], [4,2], [3,1], [2,1]])
        sage: T
        [[2]] (X) [[1], [4]] (X) [[3]] (X) [[2], [4]] (X) [[1], [3]] (X) [[1], [2]]
        sage: T.to_rigged_configuration()
        <BLANKLINE>
        0[ ][ ]0
        1[ ]1
        <BLANKLINE>
        1[ ][ ]0
        1[ ]0
        1[ ]0
        <BLANKLINE>
        0[ ][ ]0
        <BLANKLINE>
        sage: T = KRT(pathlist=[[1], [2,1], [1], [4,1], [3,1], [2,1]])
        sage: T
        [[1]] (X) [[1], [2]] (X) [[1]] (X) [[1], [4]] (X) [[1], [3]] (X) [[1], [2]]
        sage: T.to_rigged_configuration()
        <BLANKLINE>
        (/)
        <BLANKLINE>
        1[ ]0
        1[ ]0
        <BLANKLINE>
        0[ ]0
        <BLANKLINE>

    Type `D_n^{(1)}` examples::

        sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[1,1], [1,1], [1,1], [1,1]])
        sage: T = KRT(pathlist=[[-1], [-1], [1], [1]])
        sage: T
        [[-1]] (X) [[-1]] (X) [[1]] (X) [[1]]
        sage: T.to_rigged_configuration()
        <BLANKLINE>
        0[ ][ ]0
        0[ ][ ]0
        <BLANKLINE>
        0[ ][ ]0
        0[ ][ ]0
        <BLANKLINE>
        0[ ][ ]0
        <BLANKLINE>
        0[ ][ ]0
        <BLANKLINE>
        sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[2,1], [1,1], [1,1], [1,1]])
        sage: T = KRT(pathlist=[[3,2], [1], [-1], [1]])
        sage: T
        [[2], [3]] (X) [[1]] (X) [[-1]] (X) [[1]]
        sage: T.to_rigged_configuration()
        <BLANKLINE>
        0[ ]0
        0[ ]0
        0[ ]0
        <BLANKLINE>
        0[ ]0
        0[ ]0
        0[ ]0
        <BLANKLINE>
        1[ ]0
        <BLANKLINE>
        1[ ]0
        <BLANKLINE>
        sage: T.to_rigged_configuration().to_tensor_product_of_kirillov_reshetikhin_tableaux()
        [[2], [3]] (X) [[1]] (X) [[-1]] (X) [[1]]
    """
    def __init__(self, parent, list=[[]], **options) -> None:
        """
        Construct a TensorProductOfKirillovReshetikhinTableauxElement.

        INPUT:

        - ``parent`` -- parent for this element

        - ``list`` -- the list of KR tableaux elements

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 3, 1], [[1, 1], [2, 1], [1, 1], [2, 1], [2, 1], [2, 1]])
            sage: T = KRT(pathlist=[[2], [4, 1], [3], [4, 2], [3, 1], [2, 1]])
            sage: T
            [[2]] (X) [[1], [4]] (X) [[3]] (X) [[2], [4]] (X) [[1], [3]] (X) [[1], [2]]
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 3, 1], [[3,3], [2,1]])
            sage: T = KRT(pathlist=[[3, 2, 1, 4, 2, 1, 4, 3, 1], [2, 1]])
            sage: T
            [[1, 1, 1], [2, 2, 3], [3, 4, 4]] (X) [[1], [2]]
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[2, 1], [1, 1], [1, 1], [1, 1]])
            sage: T = KRT(pathlist=[[3,2], [1], [-1], [1]])
            sage: T
            [[2], [3]] (X) [[1]] (X) [[-1]] (X) [[1]]
            sage: TestSuite(T).run()
        """
    def pp(self) -> None:
        """
        Pretty print ``self``.

        EXAMPLES::

            sage: TPKRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',4,1], [[2,2],[3,1],[3,3]])
            sage: TPKRT.module_generators[0].pp()
              1  1 (X)   1 (X)   1  1  1
              2  2       2       2  2  2
                         3       3  3  3
        """
    def classical_weight(self):
        """
        Return the classical weight of ``self``.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D',4,1], [[2,2]])
            sage: elt = KRT(pathlist=[[3,2,-1,1]]); elt
            [[2, 1], [3, -1]]
            sage: elt.classical_weight()
            (0, 1, 1, 0)
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[2,2],[1,3]])
            sage: elt = KRT(pathlist=[[2,1,3,2],[1,4,4]]); elt
            [[1, 2], [2, 3]] (X) [[1, 4, 4]]
            sage: elt.classical_weight()
            (2, 2, 1, 2)
        """
    def lusztig_involution(self):
        """
        Return the result of the classical Lusztig involution on ``self``.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[2,2],[1,3]])
            sage: elt = KRT(pathlist=[[2,1,3,2],[1,4,4]])
            sage: li = elt.lusztig_involution(); li
            [[1, 1, 4]] (X) [[2, 3], [3, 4]]
            sage: li.parent()
            Tensor product of Kirillov-Reshetikhin tableaux of type ['A', 3, 1] and factor(s) ((1, 3), (2, 2))
        """
    def left_split(self):
        """
        Return the image of ``self`` under the left column splitting map.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[2,2],[1,3]])
            sage: elt = KRT(pathlist=[[2,1,3,2],[1,4,4]]); elt.pp()
              1  2 (X)   1  4  4
              2  3
            sage: elt.left_split().pp()
              1 (X)   2 (X)   1  4  4
              2       3
        """
    def right_split(self):
        """
        Return the image of ``self`` under the right column splitting map.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[2,2],[1,3]])
            sage: elt = KRT(pathlist=[[2,1,3,2],[1,4,4]]); elt.pp()
              1  2 (X)   1  4  4
              2  3
            sage: elt.right_split().pp()
              1  2 (X)   1  4 (X)   4
              2  3

        Let `\\ast` denote the :meth:`Lusztig involution<lusztig_involution>`,
        we check that `\\ast \\circ \\mathrm{ls} \\circ \\ast = \\mathrm{rs}`::

            sage: all(x.lusztig_involution().left_split().lusztig_involution() == x.right_split() for x in KRT)
            True
        """
    def to_rigged_configuration(self, display_steps: bool = False):
        """
        Perform the bijection from ``self`` to a
        :class:`rigged configuration<sage.combinat.rigged_configurations.rigged_configuration_element.RiggedConfigurationElement>`
        which is described in [RigConBijection]_, [BijectionLRT]_, and
        [BijectionDn]_.

        .. NOTE::

            This is only proven to be a bijection in types `A_n^{(1)}`
            and `D_n^{(1)}`, as well as `\\bigotimes_i B^{r_i,1}` and
            `\\bigotimes_i B^{1,s_i}` for general affine types.

        INPUT:

        - ``display_steps`` -- boolean (default: ``False``); whether to output
          each step in the algorithm

        OUTPUT: the rigged configuration corresponding to ``self``

        EXAMPLES:

        Type `A_n^{(1)}` example::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 3, 1], [[2,1], [2,1], [2,1]])
            sage: T = KRT(pathlist=[[4, 2], [3, 1], [2, 1]])
            sage: T
            [[2], [4]] (X) [[1], [3]] (X) [[1], [2]]
            sage: T.to_rigged_configuration()
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            1[ ]1
            1[ ]0
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>

        Type `D_n^{(1)}` example::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[2,2]])
            sage: T = KRT(pathlist=[[2,1,4,3]])
            sage: T
            [[1, 3], [2, 4]]
            sage: T.to_rigged_configuration()
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            -1[ ]-1
            -1[ ]-1
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            (/)

        Type `D_n^{(1)}` spinor example::

            sage: CP = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 5, 1], [[5,1],[2,1],[1,1],[1,1],[1,1]])
            sage: elt = CP(pathlist=[[-2,-5,4,3,1],[-1,2],[1],[1],[1]])
            sage: elt
            [[1], [3], [4], [-5], [-2]] (X) [[2], [-1]] (X) [[1]] (X) [[1]] (X) [[1]]
            sage: elt.to_rigged_configuration()
            <BLANKLINE>
            2[ ][ ]1
            <BLANKLINE>
            0[ ][ ]0
            0[ ]0
            <BLANKLINE>
            0[ ][ ]0
            0[ ]0
            <BLANKLINE>
            0[ ]0
            <BLANKLINE>
            0[ ][ ]0
            <BLANKLINE>

        This is invertible by calling
        :meth:`~sage.combinat.rigged_configurations.rigged_configuration_element.RiggedConfigurationElement.to_tensor_product_of_kirillov_reshetikhin_tableaux()`::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[2,2]])
            sage: T = KRT(pathlist=[[2,1,4,3]])
            sage: rc = T.to_rigged_configuration()
            sage: ret = rc.to_tensor_product_of_kirillov_reshetikhin_tableaux(); ret
            [[1, 3], [2, 4]]
            sage: ret == T
            True
        """
    def to_tensor_product_of_kirillov_reshetikhin_crystals(self):
        """
        Return a tensor product of Kirillov-Reshetikhin crystals corresponding
        to ``self``.

        This works by performing the filling map on each individual factor.
        For more on the filling map, see
        :class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableaux`.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D',4,1], [[1,1],[2,2]])
            sage: elt = KRT(pathlist=[[-1],[-1,2,-1,1]]); elt
            [[-1]] (X) [[2, 1], [-1, -1]]
            sage: tp_krc = elt.to_tensor_product_of_kirillov_reshetikhin_crystals(); tp_krc
            [[[-1]], [[2], [-1]]]

        We can recover the original tensor product of KR tableaux::

            sage: ret = KRT(tp_krc); ret
            [[-1]] (X) [[2, 1], [-1, -1]]
            sage: ret == elt
            True
        """
