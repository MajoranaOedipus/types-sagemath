from _typeshed import Incomplete
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.regular_crystals import RegularCrystals as RegularCrystals
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.root_system import RootSystem as RootSystem
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class NakajimaMonomial(Element):
    '''
    An element of the monomial crystal.

    Monomials of the form `Y_{i_1,k_1}^{y_1} \\cdots Y_{i_t,k_t}^{y_t}`,
    where `i_1, \\dots, i_t` are elements of the index set, `k_1, \\dots, k_t`
    are nonnegative integers, and `y_1, \\dots, y_t` are integers.

    EXAMPLES::

        sage: M = crystals.infinity.NakajimaMonomials([\'B\',3,1])
        sage: mg = M.module_generators[0]
        sage: mg
        1
        sage: mg.f_string([1,3,2,0,1,2,3,0,0,1])
        Y(0,0)^-1 Y(0,1)^-1 Y(0,2)^-1 Y(0,3)^-1 Y(1,0)^-3
         Y(1,1)^-2 Y(1,2) Y(2,0)^3 Y(2,2) Y(3,0) Y(3,2)^-1

    An example using the `A` variables::

        sage: M = crystals.infinity.NakajimaMonomials("A3")
        sage: M.set_variables(\'A\')
        sage: mg = M.module_generators[0]
        sage: mg.f_string([1,2,3,2,1])
        A(1,0)^-1 A(1,1)^-1 A(2,0)^-2 A(3,0)^-1
        sage: mg.f_string([3,2,1])
        A(1,2)^-1 A(2,1)^-1 A(3,0)^-1
        sage: M.set_variables(\'Y\')
    '''
    def __init__(self, parent, Y, A) -> None:
        '''
        INPUT:

        - ``d`` -- dictionary of with pairs of the form ``{(i,k): y}``

        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials("C5")
            sage: mg = M.module_generators[0]
            sage: TestSuite(mg).run()
        '''
    def __hash__(self):
        """
        TESTS::

            sage: M = crystals.infinity.NakajimaMonomials(['C',5])
            sage: m1 = M.module_generators[0].f(1)
            sage: m2 = M.module_generators[0].f(2)
            sage: hash(m1) != hash(m2)
            True
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials(['C',5])
            sage: m1 = M.module_generators[0].f(1)
            sage: m2 = M.module_generators[0].f(2)
            sage: m1.__eq__(m2)
            False
            sage: m1.__eq__(m1)
            True
        """
    def __ne__(self, other):
        """
        EXAMPLES::

            sage: La = RootSystem(['A',2]).weight_lattice().fundamental_weights()
            sage: M = crystals.NakajimaMonomials(['A',2],La[1]+La[2])
            sage: m0 = M.module_generators[0]
            sage: m = M.module_generators[0].f(1).f(2).f(2).f(1)
            sage: m.__ne__(m0)
            True
            sage: m.__ne__(m)
            False
        """
    def __lt__(self, other):
        """
        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials(['F',4])
            sage: mg = M.module_generators[0]
            sage: m = mg.f(4)
            sage: m.__lt__(mg)
            False
            sage: mg.__lt__(m)
            False
        """
    def weight_in_root_lattice(self):
        """
        Return the weight of ``self`` as an element of the root lattice.

        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials(['F',4])
            sage: m = M.module_generators[0].f_string([3,3,1,2,4])
            sage: m.weight_in_root_lattice()
            -alpha[1] - alpha[2] - 2*alpha[3] - alpha[4]

            sage: M = crystals.infinity.NakajimaMonomials(['B',3,1])
            sage: mg = M.module_generators[0]
            sage: m = mg.f_string([1,3,2,0,1,2,3,0,0,1])
            sage: m.weight_in_root_lattice()
            -3*alpha[0] - 3*alpha[1] - 2*alpha[2] - 2*alpha[3]

            sage: M = crystals.infinity.NakajimaMonomials(['C',3,1])
            sage: m = M.module_generators[0].f_string([3,0,1,2,0])
            sage: m.weight_in_root_lattice()
            -2*alpha[0] - alpha[1] - alpha[2] - alpha[3]
        """
    def weight(self):
        """
        Return the weight of ``self`` as an element of the weight lattice.

        EXAMPLES::

            sage: C = crystals.infinity.NakajimaMonomials(['A',1,1])
            sage: v = C.highest_weight_vector()
            sage: v.f(1).weight() + v.f(0).weight()
            -delta

            sage: M = crystals.infinity.NakajimaMonomials(['A',4,2])
            sage: m = M.highest_weight_vector().f_string([1,2,0,1])
            sage: m.weight()
            2*Lambda[0] - Lambda[1] - delta
        """
    def epsilon(self, i):
        """
        Return the value of `\\varepsilon_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials(['G',2,1])
            sage: m = M.module_generators[0].f(2)
            sage: [m.epsilon(i) for i in M.index_set()]
            [0, 0, 1]

            sage: M = crystals.infinity.NakajimaMonomials(['C',4,1])
            sage: m = M.module_generators[0].f_string([4,2,3])
            sage: [m.epsilon(i) for i in M.index_set()]
            [0, 0, 0, 1, 0]
        """
    def phi(self, i):
        """
        Return the value of `\\varphi_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials(['D',4,3])
            sage: m = M.module_generators[0].f(1)
            sage: [m.phi(i) for i in M.index_set()]
            [1, -1, 1]

            sage: M = crystals.infinity.NakajimaMonomials(['C',4,1])
            sage: m = M.module_generators[0].f_string([4,2,3])
            sage: [m.phi(i) for i in M.index_set()]
            [0, 1, -1, 2, -1]
        """
    def e(self, i):
        '''
        Return the action of `e_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials([\'E\',7,1])
            sage: m = M.module_generators[0].f_string([0,1,4,3])
            sage: [m.e(i) for i in M.index_set()]
            [None,
             None,
             None,
             Y(0,0)^-1 Y(1,1)^-1 Y(2,1) Y(3,0) Y(3,1) Y(4,0)^-1 Y(4,1)^-1 Y(5,0),
             None,
             None,
             None,
             None]

            sage: M = crystals.infinity.NakajimaMonomials("C5")
            sage: m = M.module_generators[0].f_string([1,3])
            sage: [m.e(i) for i in M.index_set()]
            [Y(2,1) Y(3,0)^-1 Y(3,1)^-1 Y(4,0),
             None,
             Y(1,0)^-1 Y(1,1)^-1 Y(2,0),
             None,
             None]

            sage: M = crystals.infinity.NakajimaMonomials([\'D\',4,1])
            sage: M.set_variables(\'A\')
            sage: m = M.module_generators[0].f_string([4,2,3,0])
            sage: [m.e(i) for i in M.index_set()]
            [A(2,1)^-1 A(3,1)^-1 A(4,0)^-1,
             None,
             None,
             A(0,2)^-1 A(2,1)^-1 A(4,0)^-1,
             None]
            sage: M.set_variables(\'Y\')
        '''
    def f(self, i):
        '''
        Return the action of `f_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials("B4")
            sage: m = M.module_generators[0].f_string([1,3,4])
            sage: [m.f(i) for i in M.index_set()]
            [Y(1,0)^-2 Y(1,1)^-2 Y(2,0)^2 Y(2,1) Y(3,0)^-1 Y(4,0) Y(4,1)^-1,
             Y(1,0)^-1 Y(1,1)^-1 Y(1,2) Y(2,0) Y(2,2)^-1 Y(3,0)^-1 Y(3,1) Y(4,0) Y(4,1)^-1,
             Y(1,0)^-1 Y(1,1)^-1 Y(2,0) Y(2,1)^2 Y(3,0)^-2 Y(3,1)^-1 Y(4,0)^3 Y(4,1)^-1,
             Y(1,0)^-1 Y(1,1)^-1 Y(2,0) Y(2,1) Y(3,0)^-1 Y(3,1) Y(4,1)^-2]
        '''

class InfinityCrystalOfNakajimaMonomials(UniqueRepresentation, Parent):
    '''
    Crystal `B(\\infty)` in terms of (modified) Nakajima monomials.

    Let `Y_{i,k}`, for `i \\in I` and `k \\in \\ZZ`, be a commuting set of
    variables, and let `\\boldsymbol{1}` be a new variable which commutes
    with each `Y_{i,k}`.  (Here, `I` represents the index set of a Cartan
    datum.)  One may endow the structure of a crystal on the
    set `\\widehat{\\mathcal{M}}` of monomials of the form

    .. MATH::

        M = \\prod_{(i,k) \\in I\\times \\ZZ_{\\ge0}} Y_{i,k}^{y_i(k)}\\boldsymbol{1}.

    Elements of `\\widehat{\\mathcal{M}}` are called
    *modified Nakajima monomials*. We will omit the `\\boldsymbol{1}`
    from the end of a monomial if there exists at least one `y_i(k) \\neq 0`.
    The crystal structure on this set is defined by

    .. MATH::

        \\begin{aligned}
        \\mathrm{wt}(M) & = \\sum_{i\\in I} \\Bigl( \\sum_{k \\ge 0}
        y_i(k) \\Bigr) \\Lambda_i, \\\\\n        \\varphi_i(M) & = \\max\\Bigl\\{ \\sum_{0 \\le j \\le k} y_i(j) :
        k \\ge 0 \\Bigr\\}, \\\\\n        \\varepsilon_i(M) & = \\varphi_i(M) -
        \\langle h_i, \\mathrm{wt}(M) \\rangle, \\\\\n        k_f = k_f(M) & = \\min\\Bigl\\{ k \\ge 0 :
        \\varphi_i(M) = \\sum_{0 \\le j \\le k} y_i(j) \\Bigr\\}, \\\\\n        k_e = k_e(M) & = \\max\\Bigl\\{ k \\ge 0 :
        \\varphi_i(M) = \\sum_{0 \\le j \\le k} y_i(j) \\Bigr\\},
        \\end{aligned}

    where `\\{h_i : i \\in I\\}` and `\\{\\Lambda_i : i \\in I \\}` are the simple
    coroots and fundamental weights, respectively.  With a chosen set of
    nonnegative integers `C = (c_{ij})_{i\\neq j}` such that
    `c_{ij} + c_{ji} = 1`, one defines

    .. MATH::

        A_{i,k} = Y_{i,k} Y_{i,k+1} \\prod_{j\\neq i} Y_{j,k+c_{ji}}^{a_{ji}},

    where `(a_{ij})_{i,j \\in I}` is a Cartan matrix.  Then

    .. MATH::

        \\begin{aligned}
        e_iM &= \\begin{cases} 0 & \\text{if } \\varepsilon_i(M) = 0, \\\\\n        A_{i,k_e}M & \\text{if } \\varepsilon_i(M) > 0, \\end{cases} \\\\\n        f_iM &= A_{i,k_f}^{-1} M.
        \\end{aligned}

    It is shown in [KKS2007]_ that the connected component of
    `\\widehat{\\mathcal{M}}` containing the element `\\boldsymbol{1}`,
    which we denote by `\\mathcal{M}(\\infty)`, is crystal isomorphic
    to the crystal `B(\\infty)`.

    INPUT:

    - ``cartan_type`` -- a Cartan type

    - ``c`` -- (optional) the matrix `(c_{ij})_{i,j \\in I}` such that
      `c_{ii} = 0` for all `i \\in I`, `c_{ij} \\in \\ZZ_{>0}` for all
      `i,j \\in I`, and `c_{ij} + c_{ji} = 1` for all `i \\neq j`; the
      default is `c_{ij} = 0` if `i < j` and `0` otherwise

    EXAMPLES::

        sage: B = crystals.infinity.Tableaux("C3")
        sage: S = B.subcrystal(max_depth=4)
        sage: G = B.digraph(subset=S) # long time
        sage: M = crystals.infinity.NakajimaMonomials("C3") # long time
        sage: T = M.subcrystal(max_depth=4) # long time
        sage: H = M.digraph(subset=T) # long time
        sage: G.is_isomorphic(H,edge_labels=True) # long time
        True

        sage: M = crystals.infinity.NakajimaMonomials([\'A\',2,1])
        sage: T = M.subcrystal(max_depth=3)
        sage: H = M.digraph(subset=T) # long time
        sage: Y = crystals.infinity.GeneralizedYoungWalls(2)
        sage: YS = Y.subcrystal(max_depth=3)
        sage: YG = Y.digraph(subset=YS) # long time
        sage: YG.is_isomorphic(H,edge_labels=True) # long time
        True

        sage: M = crystals.infinity.NakajimaMonomials("D4")
        sage: B = crystals.infinity.Tableaux("D4")
        sage: MS = M.subcrystal(max_depth=3)
        sage: BS = B.subcrystal(max_depth=3)
        sage: MG = M.digraph(subset=MS) # long time
        sage: BG = B.digraph(subset=BS) # long time
        sage: BG.is_isomorphic(MG,edge_labels=True) # long time
        True
    '''
    @staticmethod
    def __classcall_private__(cls, ct, c=None):
        '''
        Normalize input to ensure a unique representation.

        INPUT:

        - ``ct`` -- a Cartan type

        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials("E8")
            sage: M1 = crystals.infinity.NakajimaMonomials([\'E\',8])
            sage: M2 = crystals.infinity.NakajimaMonomials(CartanType([\'E\',8]))
            sage: M is M1 is M2
            True
        '''
    module_generators: Incomplete
    def __init__(self, ct, c, category=None) -> None:
        """
        EXAMPLES::

            sage: Minf = crystals.infinity.NakajimaMonomials(['A',3])
            sage: TestSuite(Minf).run() # long time
        """
    def c(self):
        """
        Return the matrix `c_{ij}` of ``self``.

        EXAMPLES::

            sage: La = RootSystem(['B',3]).weight_lattice().fundamental_weights()
            sage: M = crystals.NakajimaMonomials(La[1]+La[2])
            sage: M.c()
            [0 1 1]
            [0 0 1]
            [0 0 0]

            sage: c = Matrix([[0,0,1],[1,0,0],[0,1,0]])
            sage: La = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()
            sage: M = crystals.NakajimaMonomials(2*La[1], c=c)
            sage: M.c() == c
            True
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``, which is always `\\infty`.

        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials(['A',5,2])
            sage: M.cardinality()
            +Infinity
        """
    def set_variables(self, letter) -> None:
        """
        Set the type of monomials to use for the element output.

        If the `A` variables are used, the output is written as
        `\\prod_{i\\in I} Y_{i,0}^{\\lambda_i} \\prod_{i,k} A_{i,k}^{c_{i,k}}`, where
        `\\sum_{i \\in I} \\lambda_i \\Lambda_i` is the corresponding
        dominant weight.

        INPUT:

        - ``letter`` -- can be one of the following:

          * ``'Y'`` -- use `Y_{i,k}`, corresponds to fundamental weights
          * ``'A'`` -- use `A_{i,k}`, corresponds to simple roots

        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials(['A', 4])
            sage: elt = M.highest_weight_vector().f_string([2,1,3,2,3,2,4,3])
            sage: elt
            Y(1,2) Y(2,0)^-1 Y(2,2)^-1 Y(3,0)^-1 Y(3,2)^-1 Y(4,0)
            sage: M.set_variables('A')
            sage: elt
            A(1,1)^-1 A(2,0)^-1 A(2,1)^-2 A(3,0)^-2 A(3,1)^-1 A(4,0)^-1
            sage: M.set_variables('Y')

        ::

            sage: La = RootSystem(['A',2]).weight_lattice().fundamental_weights()
            sage: M = crystals.NakajimaMonomials(La[1]+La[2])
            sage: lw = M.lowest_weight_vectors()[0]
            sage: lw
            Y(1,2)^-1 Y(2,1)^-1
            sage: M.set_variables('A')
            sage: lw
            Y(1,0) Y(2,0) A(1,0)^-1 A(1,1)^-1 A(2,0)^-2
            sage: M.set_variables('Y')
        """
    def get_variables(self):
        """
        Return the type of monomials to use for the element output.

        EXAMPLES::

            sage: M = crystals.infinity.NakajimaMonomials(['A', 4])
            sage: M.get_variables()
            'Y'
        """
    Element = NakajimaMonomial

class CrystalOfNakajimaMonomialsElement(NakajimaMonomial):
    """
    Element class for
    :class:`~sage.combinat.crystals.monomial_crystals.CrystalOfNakajimaMonomials`.

    The `f_i` operators need to be modified from the version in
    :class:`~sage.combinat.crystals.monomial_crystalsNakajimaMonomial`
    in order to create irreducible highest weight realizations.
    This modified `f_i` is defined as

    .. MATH::

        f_iM = \\begin{cases} 0 & \\text{if } \\varphi_i(M) = 0, \\\\\n        A_{i,k_f}^{-1}M & \\text{if } \\varphi_i(M) > 0. \\end{cases}

    EXAMPLES::

        sage: La = RootSystem(['A',5,2]).weight_lattice(extended=True).fundamental_weights()
        sage: M = crystals.NakajimaMonomials(['A',5,2],3*La[0])
        sage: m = M.module_generators[0].f(0); m
        Y(0,0)^2 Y(0,1)^-1 Y(2,0)
        sage: TestSuite(m).run()
    """
    def f(self, i):
        '''
        Return the action of `f_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: La = RootSystem([\'A\',5,2]).weight_lattice(extended=True).fundamental_weights()
            sage: M = crystals.NakajimaMonomials([\'A\',5,2],3*La[0])
            sage: m = M.module_generators[0]
            sage: [m.f(i) for i in M.index_set()]
            [Y(0,0)^2 Y(0,1)^-1 Y(2,0), None, None, None]

        ::

            sage: M = crystals.infinity.NakajimaMonomials("E8")
            sage: M.set_variables(\'A\')
            sage: m = M.module_generators[0].f_string([4,2,3,8])
            sage: m
            A(2,1)^-1 A(3,1)^-1 A(4,0)^-1 A(8,0)^-1
            sage: [m.f(i) for i in M.index_set()]
            [A(1,2)^-1 A(2,1)^-1 A(3,1)^-1 A(4,0)^-1 A(8,0)^-1,
             A(2,0)^-1 A(2,1)^-1 A(3,1)^-1 A(4,0)^-1 A(8,0)^-1,
             A(2,1)^-1 A(3,0)^-1 A(3,1)^-1 A(4,0)^-1 A(8,0)^-1,
             A(2,1)^-1 A(3,1)^-1 A(4,0)^-1 A(4,1)^-1 A(8,0)^-1,
             A(2,1)^-1 A(3,1)^-1 A(4,0)^-1 A(5,0)^-1 A(8,0)^-1,
             A(2,1)^-1 A(3,1)^-1 A(4,0)^-1 A(6,0)^-1 A(8,0)^-1,
             A(2,1)^-1 A(3,1)^-1 A(4,0)^-1 A(7,1)^-1 A(8,0)^-1,
             A(2,1)^-1 A(3,1)^-1 A(4,0)^-1 A(8,0)^-2]
            sage: M.set_variables(\'Y\')
        '''
    def weight(self):
        '''
        Return the weight of ``self`` as an element of the weight lattice.

        EXAMPLES::

            sage: La = RootSystem("A2").weight_lattice().fundamental_weights()
            sage: M = crystals.NakajimaMonomials("A2",La[1]+La[2])
            sage: M.module_generators[0].weight()
            (2, 1, 0)
        '''

class CrystalOfNakajimaMonomials(InfinityCrystalOfNakajimaMonomials):
    '''
    Let `\\widetilde{\\mathcal{M}}` be `\\widehat{\\mathcal{M}}` as a set, and with
    crystal structure defined as on `\\widehat{\\mathcal{M}}` with the exception
    that

    .. MATH::

        f_iM = \\begin{cases} 0 & \\text{if } \\varphi_i(M) = 0, \\\\\n        A_{i,k_f}^{-1}M & \\text{if } \\varphi_i(M) > 0. \\end{cases}

    Then Kashiwara [Ka2003]_ showed that the connected component in
    `\\widetilde{\\mathcal{M}}` containing a monomial `M` such that `e_iM = 0`,
    for all `i \\in I`, is crystal isomorphic to the irreducible highest weight
    crystal `B(\\mathrm{wt}(M))`.

    INPUT:

    - ``ct`` -- a Cartan type

    - ``La`` -- an element of the weight lattice

    EXAMPLES::

        sage: La = RootSystem("A2").weight_lattice().fundamental_weights()
        sage: M = crystals.NakajimaMonomials("A2",La[1]+La[2])
        sage: B = crystals.Tableaux("A2",shape=[2,1])
        sage: GM = M.digraph()
        sage: GB = B.digraph()
        sage: GM.is_isomorphic(GB,edge_labels=True)
        True

        sage: La = RootSystem("G2").weight_lattice().fundamental_weights()
        sage: M = crystals.NakajimaMonomials("G2",La[1]+La[2])
        sage: B = crystals.Tableaux("G2",shape=[2,1])
        sage: GM = M.digraph()
        sage: GB = B.digraph()
        sage: GM.is_isomorphic(GB,edge_labels=True)
        True

        sage: La = RootSystem("B2").weight_lattice().fundamental_weights()
        sage: M = crystals.NakajimaMonomials([\'B\',2],La[1]+La[2])
        sage: B = crystals.Tableaux("B2",shape=[3/2,1/2])
        sage: GM = M.digraph()
        sage: GB = B.digraph()
        sage: GM.is_isomorphic(GB,edge_labels=True)
        True

        sage: La = RootSystem([\'A\',3,1]).weight_lattice(extended=True).fundamental_weights()
        sage: M = crystals.NakajimaMonomials([\'A\',3,1],La[0]+La[2])
        sage: B = crystals.GeneralizedYoungWalls(3,La[0]+La[2])
        sage: SM = M.subcrystal(max_depth=4)
        sage: SB = B.subcrystal(max_depth=4)
        sage: GM = M.digraph(subset=SM) # long time
        sage: GB = B.digraph(subset=SB) # long time
        sage: GM.is_isomorphic(GB,edge_labels=True) # long time
        True

        sage: La = RootSystem([\'A\',5,2]).weight_lattice(extended=True).fundamental_weights()
        sage: LA = RootSystem([\'A\',5,2]).weight_space().fundamental_weights()
        sage: M = crystals.NakajimaMonomials([\'A\',5,2],3*La[0])
        sage: B = crystals.LSPaths(3*LA[0])
        sage: SM = M.subcrystal(max_depth=4)
        sage: SB = B.subcrystal(max_depth=4)
        sage: GM = M.digraph(subset=SM)
        sage: GB = B.digraph(subset=SB)
        sage: GM.is_isomorphic(GB,edge_labels=True)
        True

        sage: c = matrix([[0,1,0],[0,0,1],[1,0,0]])
        sage: La = RootSystem([\'A\',2,1]).weight_lattice(extended=True).fundamental_weights()
        sage: M = crystals.NakajimaMonomials(2*La[1], c=c)
        sage: sorted(M.subcrystal(max_depth=3), key=str)
        [Y(0,0) Y(0,1) Y(1,0) Y(2,1)^-1,
         Y(0,0) Y(0,1)^2 Y(1,1)^-1 Y(2,0) Y(2,1)^-1,
         Y(0,0) Y(0,2)^-1 Y(1,0) Y(1,1) Y(2,1)^-1 Y(2,2),
         Y(0,1) Y(0,2)^-1 Y(1,1)^-1 Y(2,0)^2 Y(2,2),
         Y(0,1) Y(1,0) Y(1,1)^-1 Y(2,0),
         Y(0,1)^2 Y(1,1)^-2 Y(2,0)^2,
         Y(0,2)^-1 Y(1,0) Y(2,0) Y(2,2),
         Y(1,0) Y(1,3) Y(2,0) Y(2,3)^-1,
         Y(1,0)^2]
    '''
    @staticmethod
    def __classcall_private__(cls, cartan_type, La=None, c=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: La = RootSystem(['E',8,1]).weight_lattice(extended=True).fundamental_weights()
            sage: M = crystals.NakajimaMonomials(['E',8,1],La[0]+La[8])
            sage: M1 = crystals.NakajimaMonomials(CartanType(['E',8,1]),La[0]+La[8])
            sage: M2 = crystals.NakajimaMonomials(['E',8,1],M.Lambda()[0] + M.Lambda()[8])
            sage: M is M1 is M2
            True
        """
    hw: Incomplete
    module_generators: Incomplete
    def __init__(self, ct, La, c) -> None:
        """
        EXAMPLES::

            sage: La = RootSystem(['A',2]).weight_lattice().fundamental_weights()
            sage: M = crystals.NakajimaMonomials(['A',2], La[1]+La[2])
            sage: TestSuite(M).run()

            sage: La = RootSystem(['C',2,1]).weight_lattice(extended=True).fundamental_weights()
            sage: M = crystals.NakajimaMonomials(['C',2,1], La[0])
            sage: TestSuite(M).run(max_runs=100)
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: La = RootSystem(['A',2]).weight_lattice().fundamental_weights()
            sage: M = crystals.NakajimaMonomials(['A',2], La[1])
            sage: M.cardinality()
            3

            sage: La = RootSystem(['D',4,2]).weight_lattice(extended=True).fundamental_weights()
            sage: M = crystals.NakajimaMonomials(['D',4,2], La[1])
            sage: M.cardinality()
            +Infinity
        """
    Element = CrystalOfNakajimaMonomialsElement
