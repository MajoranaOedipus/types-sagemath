from _typeshed import Incomplete
from sage.categories.crystals import Crystals as Crystals
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.categories.homset import Hom as Hom
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.supercrystals import SuperCrystals as SuperCrystals
from sage.combinat.crystals.letters import CrystalOfLetters as CrystalOfLetters
from sage.combinat.crystals.tensor_product import CrystalOfWords as CrystalOfWords
from sage.combinat.crystals.tensor_product_element import CrystalOfTableauxElement as CrystalOfTableauxElement, InfinityCrystalOfTableauxElement as InfinityCrystalOfTableauxElement, InfinityCrystalOfTableauxElementTypeD as InfinityCrystalOfTableauxElementTypeD, InfinityQueerCrystalOfTableauxElement as InfinityQueerCrystalOfTableauxElement
from sage.combinat.partition import Partition as Partition
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.structure.parent import Parent as Parent

class InfinityCrystalOfTableaux(CrystalOfWords):
    """
    `\\mathcal{B}(\\infty)` crystal of tableaux.

    A tableaux model `\\mathcal{T}(\\infty)` for the crystal
    `\\mathcal{B}(\\infty)` is introduced by Hong and Lee in [HL2008]_. This model
    is currently valid for types `A_n`, `B_n`, `C_n`, `D_n`, and `G_2`, and
    builds on the tableaux model given by Kashiwara and Nakashima [KN1994]_ in
    types `A_n`, `B_n`, `C_n`, and `D_n`, and by Kang and Misra [KM1994]_ in
    type `G_2`.

    .. NOTE::

        We are using the English convention for our tableaux.

    We say a tableau `T` is *marginally large* if:

    - for each `1 \\leq i \\leq n`, the leftmost box in the `i`-th row
      from the top in `T` is an `i`-box,

    - for each `1 \\leq i \\leq n`, the number of `i`-boxes in the `i`-th row
      from the top in `T` is greater than the total number of boxes in the
      `(i+1)`-th row by exactly one.

    We now will describe this tableaux model type-by-type.

    .. rubric:: Type `A_n`

    `\\mathcal{T}(\\infty)` is the set of marginally large semistandard
    tableaux with exactly `n` rows over the alphabet `\\{1 \\prec 2 \\prec
    \\cdots \\prec n+1 \\}`.

    .. rubric:: Type `B_n`

    `\\mathcal{T}(\\infty)` is the set of marginally large semistandard
    tableaux with exactly `n` rows over the alphabet `\\{1 \\prec \\cdots
    \\prec n \\prec 0 \\prec \\overline{n} \\prec \\cdots \\prec \\overline{1} \\}`
    and subject to the following constraints:

    - for each `1 \\le i \\le n`, the contents of the boxes in the
      `i`-th row are `\\preceq \\overline{i}`,

    - the entry `0` can appear at most once in a single row.

    .. rubric:: Type `C_n`

    `\\mathcal{T}(\\infty)` is the set of marginally large semistandard
    tableaux with exactly `n` rows over the alphabet `\\{1 \\prec \\cdots
    \\prec n \\prec \\overline{n} \\prec \\cdots \\prec \\overline{1} \\}` and
    for each `1 \\leq i \\leq n`, the contents of the boxes in the `i`-th
    row are `\\preceq \\overline{i}`.

    .. rubric:: Type `D_n`

    `\\mathcal{T}(\\infty)` is the set of marginally large semistandard
    tableaux with exactly `n-1` rows over the alphabet `\\{1 \\prec \\cdots
    \\prec n, \\overline{n} \\prec \\cdots \\prec \\overline{1} \\}` and subject
    to the following constraints:

    - for each `1 \\le i \\le n`, the contents of the boxes in the `i`-th
      row are `\\preceq \\overline{i}`,

    - the entries `n` and `\\overline{n}` may not appear simultaneously in
      a single row.

    .. rubric:: Type `G_2`

    `\\mathcal{T}(\\infty)` is the set of marginally large semistandard
    tableaux with exactly `2` rows over the ordered alphabet `\\{1 \\prec
    2 \\prec 3 \\prec 0 \\prec \\overline{3} \\prec \\overline{2} \\prec
    \\overline{1}\\}` and subject to the following constraints:

    - the contents of the boxes in the first row are `\\preceq \\overline{i}`,

    - the contents of the boxes in the second row are `\\preceq 3`,

    - the entry `0` can appear at most once in the first row and not at
      all in the second row.

    In particular, the shape of the tableaux is not fixed in any instance of
    `\\mathcal{T}(\\infty)`; the row lengths of a tableau can be arbitrarily long.

    INPUT:

    - ``cartan_type`` -- one of ``['A',n]``, ``['B',n]``, ``['C',n]``,
      ``['D',n]``, or ``['G',2]``, where ``n`` is a positive integer

    EXAMPLES::

        sage: B = crystals.infinity.Tableaux(['A',2])
        sage: b = B.highest_weight_vector(); b.pp()
        1  1
        2
        sage: b.f_string([2,1,1,2,2,2]).pp()
        1  1  1  1  1  2  3
        2  3  3  3

        sage: B = crystals.infinity.Tableaux(['G',2])
        sage: b = B(rows=[[1,1,1,1,1,2,3,3,0,-3,-1,-1,-1],[2,3,3,3]])
        sage: b.e_string([2,1,1,1,1,1,1]).pp()
        1  1  1  1  2  3  3  3  3 -2 -2 -2
        2  3  3
        sage: b.e_string([2,1,1,1,1,1,1,1])

    We check that a few classical crystals embed into `\\mathcal{T}(\\infty)`::

        sage: def crystal_test(B, C):
        ....:     T = crystals.elementary.T(C.cartan_type(), C.module_generators[0].weight())
        ....:     TP = crystals.TensorProduct(T, B)
        ....:     mg = TP(T[0], B.module_generators[0])
        ....:     g = {C.module_generators[0]: mg}
        ....:     f = C.crystal_morphism(g, category=HighestWeightCrystals())
        ....:     G = B.digraph(subset=[f(x) for x in C])
        ....:     return G.is_isomorphic(C.digraph(), edge_labels=True)
        sage: B = crystals.infinity.Tableaux(['A',2])
        sage: C = crystals.Tableaux(['A',2], shape=[2,1])
        sage: crystal_test(B, C)
        True
        sage: C = crystals.Tableaux(['A',2], shape=[6,2])
        sage: crystal_test(B, C)
        True
        sage: B = crystals.infinity.Tableaux(['B',2])
        sage: C = crystals.Tableaux(['B',2], shape=[3])
        sage: crystal_test(B, C)
        True
        sage: C = crystals.Tableaux(['B',2], shape=[2,1])
        sage: crystal_test(B, C)
        True
        sage: B = crystals.infinity.Tableaux(['C',3])
        sage: C = crystals.Tableaux(['C',3], shape=[2,1])
        sage: crystal_test(B, C)
        True
        sage: B = crystals.infinity.Tableaux(['D',4])
        sage: C = crystals.Tableaux(['D',4], shape=[2])
        sage: crystal_test(B, C)
        True
        sage: C = crystals.Tableaux(['D',4], shape=[1,1,1,1])
        sage: crystal_test(B, C)
        True
        sage: B = crystals.infinity.Tableaux(['G',2])
        sage: C = crystals.Tableaux(['G',2], shape=[3])
        sage: crystal_test(B, C)
        True
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['A',4])
            sage: B2 = crystals.infinity.Tableaux(CartanType(['A',4]))
            sage: B is B2
            True
        """
    letters: Incomplete
    module_generators: Incomplete
    def __init__(self, cartan_type) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['A',2])
            sage: TestSuite(B).run() # long time
        """
    @cached_method
    def module_generator(self):
        """
        Return the module generator (or highest weight element) of ``self``.

        The module generator is the unique tableau of shape `(n, n-1, \\ldots,
        2, 1)` with weight `0`.

        EXAMPLES::

            sage: T = crystals.infinity.Tableaux(['A',3])
            sage: T.module_generator()
            [[1, 1, 1], [2, 2], [3]]
        """
    class Element(InfinityCrystalOfTableauxElement):
        """
        Elements in `\\mathcal{B}(\\infty)` crystal of tableaux.
        """
        def phi(self, i):
            '''
            Return `\\varphi_i` of ``self``.

            Let `T \\in \\mathcal{B}(\\infty)` Define `\\varphi_i(T) :=
            \\varepsilon_i(T) + \\langle h_i, \\mathrm{wt}(T) \\rangle`, where `h_i`
            is the `i`-th simple coroot and `\\mathrm{wt}(T)` is the :meth:`weight`
            of `T`.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: B = crystals.infinity.Tableaux("A3")
                sage: [B.highest_weight_vector().f_string([1,3,2,3,1,3,2,1]).phi(i) for i in B.index_set()]
                [-3, 4, -3]

                sage: B = crystals.infinity.Tableaux("G2")
                sage: [B.highest_weight_vector().f_string([2,2,1,2,1,1,1,2]).phi(i) for i in B.index_set()]
                [5, -3]
            '''
        @cached_method
        def weight(self):
            '''
            Return the weight of ``self``.

            From the definition of a crystal and that the highest weight
            element `b_{\\infty}` of `\\mathcal{B}(\\infty)` is `0`, the weight of
            `T \\in \\mathcal{B}(\\infty)` can be defined as `\\mathrm{wt}(T)
            := -\\sum_j \\alpha_{i_j}` where `\\widetilde{e}_{i_1} \\cdots
            \\widetilde{e}_{i_{\\ell}} T = b_{\\infty}` and `\\{\\alpha_i\\}` is the
            set of simple roots. (Note that the weight is independent of the
            path chosen to get to the highest weight.)

            However we can also take advantage of the fact that
            `\\rho \\colon R_{\\lambda} \\otimes \\mathcal{B}(\\infty) \\longrightarrow
            B(\\lambda)`, where `\\lambda` is the shape of `T`, preserves the
            tableau representation of `T`. Therefore

            .. MATH::

                \\mathrm{wt}(T) = \\mathrm{wt}\\bigl( \\rho(T) \\bigr) - \\lambda

            where `\\mathrm{wt}\\bigl( \\rho(T) \\bigr)` is just the usual weight of
            the tableau `T`.

            Let `\\Lambda_i` be the `i`-th fundamental weight. In type `D`, the
            height `n-1` columns corresponds to `\\Lambda_{n-1} + \\Lambda_n` and
            the in type `B`, the height `n` columns corresponds to
            `2 \\Lambda_n`.

            EXAMPLES::

                sage: B = crystals.infinity.Tableaux("C7")
                sage: b = B.highest_weight_vector().f_string([1,6,4,7,4,2,4,6,2,4,6,7,1,2,4,7])
                sage: b.weight()
                (-2, -1, 3, -5, 5, -3, -3)

            Check that the definitions agree::

                sage: P = B.weight_lattice_realization()
                sage: alpha = P.simple_roots()
                sage: b.weight() == -2*alpha[1] - 3*alpha[2] - 5*alpha[4] - 3*alpha[6] - 3*alpha[7]
                True

            Check that it works for type `B`::

                sage: B = crystals.infinity.Tableaux("B2")
                sage: B.highest_weight_vector().weight()
                (0, 0)
                sage: b = B.highest_weight_vector().f_string([1,2,2,2,1,2])
                sage: P = B.weight_lattice_realization()
                sage: alpha = P.simple_roots()
                sage: b.weight() == -2*alpha[1] - 4*alpha[2]
                True

            Check that it works for type `D`::

                sage: B = crystals.infinity.Tableaux("D4")
                sage: B.highest_weight_vector().weight()
                (0, 0, 0, 0)
                sage: b = B.highest_weight_vector().f_string([1,4,4,2,4,3,2,4,1,3,2,4])
                sage: P = B.weight_lattice_realization()
                sage: alpha = P.simple_roots()
                sage: b.weight() == -2*alpha[1] - 3*alpha[2] - 2*alpha[3] - 5*alpha[4]
                True
            '''
        def reduced_form(self):
            """
            Return the reduced form of ``self``.

            The reduced form of a tableaux `T \\in \\mathcal{T}(\\infty)` is the
            (not necessarily semistandard) tableaux obtained from `T` by
            removing all `i`-boxes in the `i`-th row, subject to the condition
            that if the row is empty, a `\\ast` is put as a placeholder.
            This is described in [BN2010]_ and [LS2012]_.

            EXAMPLES::

                sage: B = crystals.infinity.Tableaux(['A',3])
                sage: b = B.highest_weight_vector().f_string([2,2,2,3,3,3,3,3])
                sage: b.pp()
                1  1  1  1  1  1  1  1
                2  2  2  2  4  4  4
                3  4  4
                sage: b.reduced_form()
                [['*'], [4, 4, 4], [4, 4]]
            """
        def seg(self):
            """
            Return the statistic `\\mathrm{seg}` of ``self``.

            More precisely, following [LS2012]_, define a `k`-segment of a
            tableau `T` in `\\mathcal{B}(\\infty)` to be a maximal string
            of `k`-boxes in a single row of `T`.  Set `\\mathrm{seg}^{\\prime}(T)`
            to be the number of `k`-segments in `T`, as `k` varies over
            all possible values.  Then `\\mathrm{seg}(T)` is determined
            type-by-type.

            - In types `A_n` and `C_n`, define `\\mathrm{seg}(T) :=
              \\mathrm{seg}^{\\prime}(T)`.

            - In types `B_n` and `G_2`, set `e(T)` to be the number of rows in
              `T` which contain both a `0`-box and an `\\overline{\\imath}`-box.
              Define `\\mathrm{seg}(T) := \\mathrm{seg}^{\\prime}(T) - e(T)`.

            - In type `D_n`, set `d(T)` to be the number of rows in `T` which
              contain an `\\overline{\\imath}`-box, but no `n`-box nor
              `\\overline{n}`-box. Define `\\mathrm{seg}(T) :=
              \\mathrm{seg}^{\\prime}(T) + d(T)`.

            EXAMPLES::

                sage: B = crystals.infinity.Tableaux(['A',3])
                sage: b = B.highest_weight_vector().f_string([1,3,2,2,3,1,1,3])
                sage: b.pp()
                1  1  1  1  1  1  2  2  4
                2  2  2  2  3
                3  4  4
                sage: b.seg()
                4

                sage: B = crystals.infinity.Tableaux(['D',4])
                sage: b = B(rows=[[1,1,1,1,1,1,3,-2,-1],[2,2,2,4,-2],[3,3],[4]])
                sage: b.pp()
                1  1  1  1  1  1  3 -2 -1
                2  2  2  4 -2
                3  3
                4
                sage: b.seg()
                6

                sage: B = crystals.infinity.Tableaux(['G',2])
                sage: b = B.highest_weight_vector().f_string([2,1,1,1,2,1,2,2,1,2,2,2,1,2,2,1])
                sage: b.pp()
                1  1  1  1  1  1  1  1  2  3  0 -3
                2  3  3  3  3  3  3
                sage: b.seg()
                5
            """
        def content(self):
            '''
            Return the content of ``self``.

            The content `|T|` of `T \\in \\mathcal{B}(\\infty)` is the number of
            blocks added to the highest weight to obtain `T` with any
            `\\overline{\\imath}`-boxes in the `i`-th row counted with
            multiplicity `2` provided the underlying Cartan type is of type
            `B`, `D`, or `G`.

            EXAMPLES::

                sage: B = crystals.infinity.Tableaux("D5")
                sage: b = B.highest_weight_vector().f_string([5,4,3,1,1,3,4,5,3,4,5,1,4,5,2,3,5,3,2,4])
                sage: b.content()
                13

                sage: B = crystals.infinity.Tableaux("B2")
                sage: b = B(rows=[[1,1,1,1,1,1,2,2,2,-2,-2],[2,0,-2,-2,-2]])
                sage: b.content()
                12

                sage: B = crystals.infinity.Tableaux("C2")
                sage: b = B(rows=[[1,1,1,1,1,1,2,2,2,-2,-2],[2,-2,-2,-2]])
                sage: b.content()
                8
            '''

class InfinityCrystalOfTableauxTypeD(InfinityCrystalOfTableaux):
    '''
    `\\mathcal{B}(\\infty)` crystal of tableaux for type `D_n`.

    This is the set `\\mathcal{T}(\\infty)` of marginally large semistandard
    tableaux with exactly `n-1` rows over the alphabet `\\{1 \\prec \\cdots
    \\prec n, \\overline{n} \\prec \\cdots \\prec \\overline{1} \\}` and subject
    to the following constraints:

    - for each `1 \\le i \\le n`, the contents of the boxes in the `i`-th
      row are `\\preceq \\overline{i}`,

    - the entries `n` and `\\overline{n}` may not appear simultaneously in
      a single row.

    For more information, see
    :class:`~sage.combinat.crystals.infinity_crystals.InfinityCrystalOfTableaux`.

    EXAMPLES::

        sage: B = crystals.infinity.Tableaux("D4")
        sage: b = B.highest_weight_vector().f_string([4,3,2,1,4])
        sage: b.pp()
        1  1  1  1  1  1  2
        2  2  2  2  3
        3 -4 -3
        sage: b.weight()
        (-1, 0, -2, -1)
    '''
    @staticmethod
    def __classcall_private__(cls, cartan_type):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['D',4])
            sage: B2 = crystals.infinity.Tableaux(CartanType(['D',4]))
            sage: B is B2
            True
        """
    @cached_method
    def module_generator(self):
        """
        Return the module generator (or highest weight element) of ``self``.

        The module generator is the unique tableau of shape `(n-1, \\ldots, 2,
        1)` with weight `0`.

        EXAMPLES::

            sage: T = crystals.infinity.Tableaux(['D',4])
            sage: T.module_generator()
            [[1, 1, 1], [2, 2], [3]]
        """
    class Element(InfinityCrystalOfTableauxElementTypeD, InfinityCrystalOfTableaux.Element):
        """
        Elements in `\\mathcal{B}(\\infty)` crystal of tableaux for type `D_n`.
        """

class DualInfinityQueerCrystalOfTableaux(CrystalOfWords):
    @staticmethod
    def __classcall_private__(cls, cartan_type):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['A',4])
            sage: B2 = crystals.infinity.Tableaux(CartanType(['A',4]))
            sage: B is B2
            True
        """
    letters: Incomplete
    module_generators: Incomplete
    def __init__(self, cartan_type) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['A',2])
            sage: TestSuite(B).run() # long time
        """
    @cached_method
    def module_generator(self):
        '''
        Return the module generator (or highest weight element) of ``self``.

        The module generator is the unique semistandard hook tableau of shape
        `(n, n-1, \\ldots,2, 1)` with weight `0`.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(["Q",5])
            sage: B.module_generator()
            [[5, 5, 5, 5, 5], [4, 4, 4, 4], [3, 3, 3], [2, 2], [1]]
        '''
    @cached_method
    def index_set(self):
        '''
        Return the index set of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(["Q",3])
            sage: B.index_set()
            (1, 2, -1)
        '''
    class Element(InfinityQueerCrystalOfTableauxElement): ...
