from _typeshed import Incomplete
from sage.categories.crystals import Crystals as Crystals
from sage.categories.finite_crystals import FiniteCrystals as FiniteCrystals
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.regular_crystals import RegularCrystals as RegularCrystals
from sage.categories.regular_supercrystals import RegularSuperCrystals as RegularSuperCrystals
from sage.categories.supercrystals import SuperCrystals as SuperCrystals
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.root_lattice_realizations import RootLatticeRealizations as RootLatticeRealizations
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class AbstractSingleCrystalElement(Element):
    """
    Abstract base class for elements in crystals with a single element.
    """
    def __lt__(self, other):
        '''
        EXAMPLES::

            sage: La = RootSystem("D4").ambient_space().fundamental_weights()
            sage: T = crystals.elementary.T("D4",La[3]+La[4])
            sage: t = T.highest_weight_vector()
            sage: t < t.e(1)
            False
            sage: t < t
            False
        '''
    def __hash__(self):
        '''
        TESTS::

            sage: C = crystals.elementary.Component("D7")
            sage: c = C.highest_weight_vector()
            sage: hash(c) # random
            879
        '''
    def __eq__(self, other):
        '''
        EXAMPLES::

            sage: La = RootSystem("A2").weight_lattice().fundamental_weights()
            sage: T = crystals.elementary.T("A2",La[1])
            sage: U = crystals.elementary.T("A2",La[2])
            sage: la = RootSystem("B2").weight_lattice().fundamental_weights()
            sage: V = crystals.elementary.T("B2",la[1])
            sage: t = T.highest_weight_vector()
            sage: u = U.highest_weight_vector()
            sage: v = V.highest_weight_vector()
            sage: [t == t, u == u, v == v]
            [True, True, True]
            sage: [t == u, u == v, t == v]
            [False, False, False]

            sage: C = crystals.elementary.Component("D7")
            sage: c = C.highest_weight_vector()
            sage: c == c
            True
            sage: c == c.f(7)
            False
        '''
    def __ne__(self, other):
        '''
        EXAMPLES::

            sage: La = RootSystem("A2").weight_lattice().fundamental_weights()
            sage: T = crystals.elementary.T("A2",La[1])
            sage: T.highest_weight_vector() != T.highest_weight_vector()
            False
            sage: T.highest_weight_vector() != T.highest_weight_vector().e(1)
            True
        '''
    def e(self, i) -> None:
        """
        Return `e_i` of ``self``, which is ``None`` for all `i`.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: ct = CartanType(['A',2])
            sage: la = RootSystem(ct).weight_lattice().fundamental_weights()
            sage: T = crystals.elementary.T(ct,la[1])
            sage: t = T.highest_weight_vector()
            sage: t.e(1)
            sage: t.e(2)
        """
    def f(self, i) -> None:
        """
        Return `f_i` of ``self``, which is ``None`` for all `i`.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: ct = CartanType(['A',2])
            sage: la = RootSystem(ct).weight_lattice().fundamental_weights()
            sage: T = crystals.elementary.T(ct,la[1])
            sage: t = T.highest_weight_vector()
            sage: t.f(1)
            sage: t.f(2)
        """

class TCrystal(UniqueRepresentation, Parent):
    """
    The crystal `T_{\\lambda}`.

    Let `\\lambda` be a weight. As defined in [Ka1993]_ the crystal
    `T_{\\lambda} = \\{ t_{\\lambda} \\}` is a single element crystal with the
    crystal structure defined by

    .. MATH::

        \\mathrm{wt}(t_\\lambda) = \\lambda, \\quad
        e_i t_{\\lambda} = f_i t_{\\lambda} = 0, \\quad
        \\varepsilon_i(t_{\\lambda}) = \\varphi_i(t_{\\lambda}) = -\\infty.

    The crystal `T_{\\lambda}` shifts the weights of the vertices in a crystal
    `B` by `\\lambda` when tensored with `B`, but leaves the graph structure of
    `B` unchanged. That is to say, for all `b \\in B`, we have `\\mathrm{wt}(b
    \\otimes t_{\\lambda}) = \\mathrm{wt}(b) + \\lambda`.

    INPUT:

    - ``cartan_type`` -- a Cartan type

    - ``weight`` -- an element of the weight lattice of type ``cartan_type``

    EXAMPLES::

        sage: ct = CartanType(['A',2])
        sage: C = crystals.Tableaux(ct, shape=[1])
        sage: for x in C: x.weight()
        (1, 0, 0)
        (0, 1, 0)
        (0, 0, 1)
        sage: La = RootSystem(ct).ambient_space().fundamental_weights()
        sage: TLa = crystals.elementary.T(ct, 3*(La[1] + La[2]))
        sage: TP = crystals.TensorProduct(TLa, C)
        sage: for x in TP: x.weight()
        (7, 3, 0)
        (6, 4, 0)
        (6, 3, 1)
        sage: G = C.digraph()
        sage: H = TP.digraph()
        sage: G.is_isomorphic(H,edge_labels=True)
        True
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type, weight=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: ct = CartanType(['A',3])
            sage: la = RootSystem(ct).weight_lattice().fundamental_weights()
            sage: wts = RootSystem(ct).ambient_space().fundamental_weights()
            sage: X = crystals.elementary.T(['A',3], la[1])
            sage: Y = crystals.elementary.T(la[1])
            sage: X is Y
            True
        """
    module_generators: Incomplete
    def __init__(self, cartan_type, weight) -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: la = RootSystem("A2").weight_lattice().fundamental_weights()
            sage: B = crystals.elementary.T("A2", 5*la[2])
            sage: TestSuite(B).run()
        '''
    def cardinality(self):
        """
        Return the cardinality of ``self``, which is always `1`.

        EXAMPLES::

            sage: La = RootSystem(['C',12]).weight_lattice().fundamental_weights()
            sage: T = crystals.elementary.T(['C',12], La[9])
            sage: T.cardinality()
            1
        """
    def weight_lattice_realization(self):
        """
        Return a realization of the lattice containing the weights
        of ``self``.

        EXAMPLES::

            sage: La = RootSystem(['C',12]).weight_lattice().fundamental_weights()
            sage: T = crystals.elementary.T(['C',12], La[9])
            sage: T.weight_lattice_realization()
            Weight lattice of the Root system of type ['C', 12]

            sage: ct = CartanMatrix([[2, -4], [-5, 2]])
            sage: La = RootSystem(ct).weight_lattice().fundamental_weights()
            sage: T = crystals.elementary.T(ct, La[1])
            sage: T.weight_lattice_realization()
            Weight lattice of the Root system of type
            [ 2 -4]
            [-5  2]
        """
    class Element(AbstractSingleCrystalElement):
        """
        Element of a `T_{\\lambda}` crystal.
        """
        def epsilon(self, i):
            """
            Return `\\varepsilon_i` of ``self``, which is `-\\infty` for all `i`.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: ct = CartanType(['C',5])
                sage: la = RootSystem(ct).weight_lattice().fundamental_weights()
                sage: T = crystals.elementary.T(ct,la[4]+la[5]-la[1]-la[2])
                sage: t = T.highest_weight_vector()
                sage: [t.epsilon(i) for i in T.index_set()]
                [-inf, -inf, -inf, -inf, -inf]
            """
        def phi(self, i):
            """
            Return `\\varphi_i` of ``self``, which is `-\\infty` for all `i`.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: ct = CartanType(['C',5])
                sage: la = RootSystem(ct).weight_lattice().fundamental_weights()
                sage: T = crystals.elementary.T(ct,la[4]+la[5]-la[1]-la[2])
                sage: t = T.highest_weight_vector()
                sage: [t.phi(i) for i in T.index_set()]
                [-inf, -inf, -inf, -inf, -inf]
            """
        def weight(self):
            """
            Return the weight of ``self``, which is always `\\lambda`.

            EXAMPLES::

                sage: ct = CartanType(['C',5])
                sage: la = RootSystem(ct).weight_lattice().fundamental_weights()
                sage: T = crystals.elementary.T(ct,la[4]+la[5]-la[1]-la[2])
                sage: t = T.highest_weight_vector()
                sage: t.weight()
                -Lambda[1] - Lambda[2] + Lambda[4] + Lambda[5]
            """

class RCrystal(UniqueRepresentation, Parent):
    '''
    The crystal `R_{\\lambda}`.

    For a fixed weight `\\lambda`, the crystal `R_{\\lambda} = \\{ r_{\\lambda} \\}`
    is a single element crystal with the crystal structure defined by

    .. MATH::

        \\mathrm{wt}(r_{\\lambda}) = \\lambda, \\quad
        e_i r_{\\lambda} = f_i r_{\\lambda} = 0, \\quad
        \\varepsilon_i(r_{\\lambda}) = -\\langle h_i, \\lambda\\rangle, \\quad
        \\varphi_i(r_{\\lambda}) = 0,

    where `\\{h_i\\}` are the simple coroots.

    Tensoring `R_{\\lambda}` with a crystal `B` results in shifting the weights
    of the vertices in `B` by `\\lambda` and may also cut a subset out of the
    original graph of `B`.  That is, `\\mathrm{wt}(r_{\\lambda} \\otimes b) =
    \\mathrm{wt}(b) + \\lambda`, where `b \\in B`, provided `r_{\\lambda} \\otimes
    b \\neq 0`. For example, the crystal graph of `B(\\lambda)` is the same as
    the crystal graph of `R_{\\lambda} \\otimes B(\\infty)` generated from the
    component `r_{\\lambda} \\otimes u_{\\infty}`.

    There is also a dual version of this crystal given by
    `R^{\\vee}_{\\lambda} = \\{ r^{\\vee}_{\\lambda} \\}` with the crystal
    structure defined by

    .. MATH::

        \\mathrm{wt}(r^{\\vee}_{\\lambda}) = \\lambda, \\quad
        e_i r^{\\vee}_{\\lambda} = f_i r^{\\vee}_{\\lambda} = 0, \\quad
        \\varepsilon_i(r^{\\vee}_{\\lambda}) = 0, \\quad
        \\varphi_i(r^{\\vee}_{\\lambda}) = \\langle h_i, \\lambda\\rangle.

    INPUT:

    - ``cartan_type`` -- a Cartan type
    - ``weight`` -- an element of the weight lattice of type ``cartan_type``
    - ``dual`` -- boolean (default: ``False``)

    EXAMPLES:

    We check by tensoring `R_{\\lambda}` with `B(\\infty)` results in a
    component of `B(\\lambda)`::

        sage: B = crystals.infinity.Tableaux("A2")
        sage: R = crystals.elementary.R("A2", B.Lambda()[1]+B.Lambda()[2])
        sage: T = crystals.TensorProduct(R, B)
        sage: mg = T(R.highest_weight_vector(), B.highest_weight_vector())
        sage: S = T.subcrystal(generators=[mg])
        sage: sorted([x.weight() for x in S], key=str)
        [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 1, 1),
         (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
        sage: C = crystals.Tableaux("A2", shape=[2,1])
        sage: sorted([x.weight() for x in C], key=str)
        [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 1, 1),
         (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
        sage: GT = T.digraph(subset=S)
        sage: GC = C.digraph()
        sage: GT.is_isomorphic(GC, edge_labels=True)
        True
    '''
    @staticmethod
    def __classcall_private__(cls, cartan_type, weight=None, dual: bool = False):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: ct = CartanType(['A',3])
            sage: la = RootSystem(ct).weight_lattice().fundamental_weights()
            sage: X = crystals.elementary.R(['A',3], la[1])
            sage: Y = crystals.elementary.R(la[1])
            sage: X is Y
            True
        """
    module_generators: Incomplete
    def __init__(self, cartan_type, weight, dual) -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: la = RootSystem("A2").weight_lattice().fundamental_weights()
            sage: B = crystals.elementary.R("A2",5*la[2])
            sage: TestSuite(B).run()
        '''
    def cardinality(self):
        """
        Return the cardinality of ``self``, which is always `1`.

        EXAMPLES::

            sage: La = RootSystem(['C',12]).weight_lattice().fundamental_weights()
            sage: R = crystals.elementary.R(['C',12],La[9])
            sage: R.cardinality()
            1
        """
    def weight_lattice_realization(self):
        """
        Return a realization of the lattice containing the weights
        of ``self``.

        EXAMPLES::

            sage: La = RootSystem(['C',12]).weight_lattice().fundamental_weights()
            sage: R = crystals.elementary.R(['C',12], La[9])
            sage: R.weight_lattice_realization()
            Weight lattice of the Root system of type ['C', 12]

            sage: ct = CartanMatrix([[2, -4], [-5, 2]])
            sage: La = RootSystem(ct).weight_lattice().fundamental_weights()
            sage: R = crystals.elementary.R(ct, La[1])
            sage: R.weight_lattice_realization()
            Weight lattice of the Root system of type
            [ 2 -4]
            [-5  2]
        """
    class Element(AbstractSingleCrystalElement):
        """
        Element of a `R_{\\lambda}` crystal.
        """
        def epsilon(self, i):
            '''
            Return `\\varepsilon_i` of ``self``.

            We have `\\varepsilon_i(r_{\\lambda}) = -\\langle h_i, \\lambda
            \\rangle` for all `i`, where `h_i` is a simple coroot.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: la = RootSystem([\'A\',2]).weight_lattice().fundamental_weights()
                sage: R = crystals.elementary.R("A2", la[1])
                sage: r = R.highest_weight_vector()
                sage: [r.epsilon(i) for i in R.index_set()]
                [-1, 0]

                sage: R = crystals.elementary.R("A2", la[1], dual=True)
                sage: r = R.highest_weight_vector()
                sage: [r.epsilon(i) for i in R.index_set()]
                [0, 0]
            '''
        def phi(self, i):
            '''
            Return `\\varphi_i` of ``self``, which is `0` for all `i`.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: la = RootSystem("C5").weight_lattice().fundamental_weights()
                sage: R = crystals.elementary.R("C5", la[4]+la[5])
                sage: r = R.highest_weight_vector()
                sage: [r.phi(i) for i in R.index_set()]
                [0, 0, 0, 0, 0]

                sage: R = crystals.elementary.R("C5", la[4]+la[5], dual=True)
                sage: r = R.highest_weight_vector()
                sage: [r.phi(i) for i in R.index_set()]
                [0, 0, 0, 1, 1]
            '''
        def weight(self):
            """
            Return the weight of ``self``, which is always `\\lambda`.

            EXAMPLES::

                sage: ct = CartanType(['C',5])
                sage: la = RootSystem(ct).weight_lattice().fundamental_weights()
                sage: T = crystals.elementary.T(ct,la[4]+la[5]-la[1]-la[2])
                sage: t = T.highest_weight_vector()
                sage: t.weight()
                -Lambda[1] - Lambda[2] + Lambda[4] + Lambda[5]
            """

class ElementaryCrystal(UniqueRepresentation, Parent):
    """
    The elementary crystal `B_i`.

    For `i` an element of the index set of type `X`, the crystal `B_i` of type
    `X` is the set

    .. MATH::

        B_i = \\{ b_i(m) : m \\in \\ZZ \\},

    where the crystal structure is given by

    .. MATH::

        \\begin{aligned}
        \\mathrm{wt}\\bigl(b_i(m)\\bigr) &= m\\alpha_i \\\\\n        \\varphi_j\\bigl(b_i(m)\\bigr) &= \\begin{cases}
            m & \\text{ if } j=i, \\\\\n            -\\infty & \\text{ if } j\\neq i,
        \\end{cases} \\\\\n        \\varepsilon_j\\bigl(b_i(m)\\bigr) &= \\begin{cases}
            -m & \\text{ if } j=i, \\\\\n            -\\infty & \\text{ if } j\\neq i,
        \\end{cases} \\\\\n        e_j b_i(m) &= \\begin{cases}
            b_i(m+1) & \\text{ if } j=i, \\\\\n            0 & \\text{ if } j\\neq i,
        \\end{cases} \\\\\n        f_j b_i(m) &= \\begin{cases}
            b_i(m-1) & \\text{ if } j=i, \\\\\n            0 & \\text{ if } j\\neq i.
        \\end{cases}
        \\end{aligned}

    The *Kashiwara embedding theorem* asserts there is a unique strict crystal
    embedding of crystals

    .. MATH::

        B(\\infty) \\hookrightarrow B_i \\otimes B(\\infty),

    satisfying certain properties (see [Ka1993]_).  The above embedding
    may be iterated to obtain a new embedding

    .. MATH::

        B(\\infty) \\hookrightarrow B_{i_N} \\otimes B_{i_{N-1}}
        \\otimes \\cdots \\otimes B_{i_2} \\otimes B_{i_1} \\otimes B(\\infty),

    which is a foundational object in the study of *polyhedral realizations of
    crystals* (see, for example, [NZ1997]_).
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type, i):
        '''
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: B = crystals.elementary.Elementary([\'A\',4], 3)
            sage: C = crystals.elementary.Elementary(CartanType("A4"), int(3))
            sage: B is C
            True
        '''
    module_generators: Incomplete
    def __init__(self, cartan_type, i) -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: B = crystals.elementary.Elementary("D4",3)
            sage: TestSuite(B).run()
        '''
    def weight_lattice_realization(self):
        """
        Return a realization of the lattice containing the weights
        of ``self``.

        EXAMPLES::

            sage: B = crystals.elementary.Elementary(['A',4, 1], 2)
            sage: B.weight_lattice_realization()
            Root lattice of the Root system of type ['A', 4, 1]
        """
    class Element(Element):
        """
        Element of a `B_i` crystal.
        """
        def __init__(self, parent, m) -> None:
            """
            EXAMPLES::

                sage: B = crystals.elementary.Elementary(['B',7],7)
                sage: elt = B(17); elt
                17
            """
        def __hash__(self):
            """
            TESTS::

                sage: B = crystals.elementary.Elementary(['B',7],7)
                sage: hash(B(17))
                17
            """
        def __lt__(self, other):
            '''
            EXAMPLES::

                sage: B = crystals.elementary.Elementary("D4",3)
                sage: b = B(1)
                sage: c = B(-1)
                sage: b.__lt__(c)
                False
                sage: c.__lt__(b)
                True
            '''
        def __eq__(self, other):
            '''
            EXAMPLES::

                sage: B = crystals.elementary.Elementary("A2",1)
                sage: C = crystals.elementary.Elementary("A2",2)
                sage: D = crystals.elementary.Elementary("B2",1)
                sage: [B(0) == B(1), B(0) == C(0), B(0) == D(0), C(0) == D(0)]
                [False, False, False, False]
                sage: [B(1) == B(1), C(12) == C(12), D(-1) == D(-1)]
                [True, True, True]
            '''
        def __ne__(self, other):
            '''
            EXAMPLES::

                sage: B = crystals.elementary.Elementary("A2",1)
                sage: B(0) != B(2)
                True
                sage: B(0) != B(0)
                False
            '''
        def e(self, i):
            """
            Return the action of `e_i` on ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: B = crystals.elementary.Elementary(['E',7],1)
                sage: B(3).e(1)
                4
                sage: B(172).e_string([1]*171)
                343
                sage: B(0).e(2)
            """
        def f(self, i):
            """
            Return the action of `f_i` on ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: B = crystals.elementary.Elementary(['E',7],1)
                sage: B(3).f(1)
                2
                sage: B(172).f_string([1]*171)
                1
                sage: B(0).e(2)
            """
        def epsilon(self, i):
            """
            Return `\\varepsilon_i` of ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: B = crystals.elementary.Elementary(['F',4],3)
                sage: [[B(j).epsilon(i) for i in B.index_set()] for j in range(5)]
                [[-inf, -inf, 0, -inf],
                 [-inf, -inf, -1, -inf],
                 [-inf, -inf, -2, -inf],
                 [-inf, -inf, -3, -inf],
                 [-inf, -inf, -4, -inf]]
            """
        def phi(self, i):
            """
            Return `\\varphi_i` of ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: B = crystals.elementary.Elementary(['E',8,1],4)
                sage: [[B(m).phi(j) for j in B.index_set()] for m in range(44,49)]
                [[-inf, -inf, -inf, -inf, 44, -inf, -inf, -inf, -inf],
                 [-inf, -inf, -inf, -inf, 45, -inf, -inf, -inf, -inf],
                 [-inf, -inf, -inf, -inf, 46, -inf, -inf, -inf, -inf],
                 [-inf, -inf, -inf, -inf, 47, -inf, -inf, -inf, -inf],
                 [-inf, -inf, -inf, -inf, 48, -inf, -inf, -inf, -inf]]
            """
        def weight(self):
            """
            Return the weight of ``self``.

            EXAMPLES::

                sage: B = crystals.elementary.Elementary(['C',14],12)
                sage: B(-385).weight()
                -385*alpha[12]
            """

class ComponentCrystal(UniqueRepresentation, Parent):
    """
    The component crystal.

    Defined in [Ka1993]_, the component crystal `C = \\{c\\}` is the single
    element crystal whose crystal structure is defined by

    .. MATH::

        \\mathrm{wt}(c) = 0, \\quad
        e_i c = f_i c = 0, \\quad
        \\varepsilon_i(c) = \\varphi_i(c) = 0.

    Note `C \\cong B(0)`, where `B(0)` is the highest weight crystal of highest
    weight `0`.

    INPUT:

    - ``cartan_type`` -- a Cartan type
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type, P=None):
        '''
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: C = crystals.elementary.Component("A2")
            sage: D = crystals.elementary.Component(CartanType([\'A\',2]))
            sage: C is D
            True
            sage: AS = RootSystem([\'A\',2]).ambient_space()
            sage: E = crystals.elementary.Component(AS)
            sage: F = crystals.elementary.Component(CartanType([\'A\',2]), AS)
            sage: C is E and C is F
            True
        '''
    module_generators: Incomplete
    def __init__(self, cartan_type, P) -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: B = crystals.elementary.Component("D4")
            sage: TestSuite(B).run()
        '''
    def cardinality(self):
        '''
        Return the cardinality of ``self``, which is always `1`.

        EXAMPLES::

            sage: C = crystals.elementary.Component("E6")
            sage: c = C.highest_weight_vector()
            sage: C.cardinality()
            1
        '''
    def weight_lattice_realization(self):
        '''
        Return the weight lattice realization of ``self``.

        EXAMPLES::

            sage: C = crystals.elementary.Component("A2")
            sage: C.weight_lattice_realization()
            Ambient space of the Root system of type [\'A\', 2]

            sage: P = RootSystem([\'A\',2]).weight_lattice()
            sage: C = crystals.elementary.Component(P)
            sage: C.weight_lattice_realization() is P
            True
        '''
    class Element(AbstractSingleCrystalElement):
        """
        Element of a component crystal.
        """
        def epsilon(self, i):
            '''
            Return `\\varepsilon_i` of ``self``, which is `0` for all `i`.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: C = crystals.elementary.Component("C5")
                sage: c = C.highest_weight_vector()
                sage: [c.epsilon(i) for i in C.index_set()]
                [0, 0, 0, 0, 0]
            '''
        def phi(self, i):
            '''
            Return `\\varphi_i` of ``self``, which is `0` for all `i`.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: C = crystals.elementary.Component("C5")
                sage: c = C.highest_weight_vector()
                sage: [c.phi(i) for i in C.index_set()]
                [0, 0, 0, 0, 0]
            '''
        def weight(self):
            '''
            Return the weight of ``self``, which is always `0`.

            EXAMPLES::

                sage: C = crystals.elementary.Component("F4")
                sage: c = C.highest_weight_vector()
                sage: c.weight()
                (0, 0, 0, 0)
            '''
