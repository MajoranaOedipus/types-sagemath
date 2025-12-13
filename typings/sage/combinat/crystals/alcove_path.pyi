from _typeshed import Incomplete
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.categories.loop_crystals import LoopCrystals as LoopCrystals
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.root_system import RootSystem as RootSystem
from sage.misc.cachefunc import cached_in_parent_method as cached_in_parent_method, cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.integer import Integer as Integer
from sage.structure.element import Element as Element
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class CrystalOfAlcovePaths(UniqueRepresentation, Parent):
    '''
    Crystal of alcove paths generated from a "straight-line" path to the
    negative of a given dominant weight.

    INPUT:

    - ``cartan_type`` -- Cartan type of a finite or affine untwisted root
      system

    - ``weight`` -- dominant weight as a list of (integral) coefficients of
      the fundamental weights

    - ``highest_weight_crystal`` -- (default: ``True``) if ``True``
      returns the highest weight crystal.  If ``False`` returns an
      object which is close to being isomorphic to the tensor product
      of Kirillov-Reshetikhin crystals of column shape in the
      following sense: We get all the vertices, but only some of the
      edges.  We\'ll call the included edges pseudo-Demazure.  They are
      all nonzero edges and the 0-edges not at the end of a 0-string
      of edges, i.e.  not those with `f_{0}(b) = b\'` with
      `\\varphi_0(b) =1`.  (Whereas Demazure 0-edges are those that
      are not at the beginning of a zero string.) In this case the
      weight `[c_1, c_2, \\ldots, c_k]` represents
      `\\sum_{i=1}^k c_i \\omega_i`.

      .. NOTE::

          If ``highest_weight_crystal`` = ``False``, since we do not
          get the full crystal, ``TestSuite`` will fail on the
          Stembridge axioms.

    .. SEEALSO::

        - :class:`Crystals`

    EXAMPLES:

    The following example appears in Figure 2 of [LP2008]_::

        sage: C = crystals.AlcovePaths([\'G\',2],[0,1])
        sage: G = C.digraph()
        sage: GG = DiGraph({
        ....:     ()        : {(0)         : 2 },
        ....:     (0)       : {(0,8)       : 1 },
        ....:     (0,1)     : {(0,1,7)     : 2 },
        ....:     (0,1,2)   : {(0,1,2,9)   : 1 },
        ....:     (0,1,2,3) : {(0,1,2,3,4) : 2 },
        ....:     (0,1,2,6) : {(0,1,2,3)   : 1 },
        ....:     (0,1,2,9) : {(0,1,2,6)   : 1 },
        ....:     (0,1,7)   : {(0,1,2)     : 2 },
        ....:     (0,1,7,9) : {(0,1,2,9)   : 2 },
        ....:     (0,5)     : {(0,1)       : 1, (0,5,7) : 2 },
        ....:     (0,5,7)   : {(0,5,7,9)   : 1 },
        ....:     (0,5,7,9) : {(0,1,7,9)   : 1 },
        ....:     (0,8)     : {(0,5)       : 1 },
        ....:     })
        sage: G.is_isomorphic(GG)
        True
        sage: for u, v, i in G.edges(sort=True):
        ....:     print((u.integer_sequence() , v.integer_sequence(), i))
        ([], [0], 2)
        ([0], [0, 8], 1)
        ([0, 1], [0, 1, 7], 2)
        ([0, 1, 2], [0, 1, 2, 9], 1)
        ([0, 1, 2, 3], [0, 1, 2, 3, 4], 2)
        ([0, 1, 2, 6], [0, 1, 2, 3], 1)
        ([0, 1, 2, 9], [0, 1, 2, 6], 1)
        ([0, 1, 7], [0, 1, 2], 2)
        ([0, 1, 7, 9], [0, 1, 2, 9], 2)
        ([0, 5], [0, 1], 1)
        ([0, 5], [0, 5, 7], 2)
        ([0, 5, 7], [0, 5, 7, 9], 1)
        ([0, 5, 7, 9], [0, 1, 7, 9], 1)
        ([0, 8], [0, 5], 1)

    Alcove path crystals are a discrete version of Littelmann paths.
    We verify that the alcove path crystal is isomorphic to the LS
    path crystal::

        sage: C1 = crystals.AlcovePaths([\'C\',3],[2,1,0])
        sage: g1 = C1.digraph() #long time
        sage: C2 = crystals.LSPaths([\'C\',3],[2,1,0])
        sage: g2 = C2.digraph() #long time
        sage: g1.is_isomorphic(g2, edge_labels=True) #long time
        True

    The preferred initialization method is via explicit weights rather than a Cartan type
    and the coefficients of the fundamental weights::

        sage: R = RootSystem([\'C\',3])
        sage: P = R.weight_lattice()
        sage: La = P.fundamental_weights()
        sage: C = crystals.AlcovePaths(2*La[1]+La[2]); C
        Highest weight crystal of alcove paths of type [\'C\', 3] and weight 2*Lambda[1] + Lambda[2]
        sage: C1==C
        True

    We now explain the data structure::

        sage: C = crystals.AlcovePaths([\'A\',2],[2,0]) ; C
        Highest weight crystal of alcove paths of type [\'A\', 2] and weight 2*Lambda[1]
        sage: C._R.lambda_chain()
        [(alpha[1], 0), (alpha[1] + alpha[2], 0), (alpha[1], 1), (alpha[1] + alpha[2], 1)]

    The previous list gives the initial "straight line" path from the
    fundamental alcove `A_o` to its translation  `A_o - \\lambda` where
    `\\lambda = 2\\omega_1` in this example. The initial path for weight
    `\\lambda` is called the `\\lambda`-chain. This path is constructed from
    the ordered pairs `(\\beta, k)`, by crossing the hyperplane orthogonal to
    `\\beta` at height `-k`. We can view a plot of this path as follows::

        sage: x=C( () )
        sage: x.plot() # not tested - outputs a pdf

    An element of the crystal is given by a subset of the `\\lambda`-chain.
    This subset indicates the hyperplanes where the initial path should be
    folded. The highest weight element is given by the empty subset. ::

        sage: x
        ()
        sage: x.f(1).f(2)
        ((alpha[1], 1), (alpha[1] + alpha[2], 1))
        sage: x.f(1).f(2).integer_sequence()
        [2, 3]
        sage: C([2,3])
        ((alpha[1], 1), (alpha[1] + alpha[2], 1))
        sage: C([2,3]).is_admissible() #check if a valid vertex
        True
        sage: C([1,3]).is_admissible() #check if a valid vertex
        False

    Alcove path crystals now works in affine type (:issue:`14143`)::

        sage: C = crystals.AlcovePaths([\'A\',2,1],[1,0,0]) ; C
        Highest weight crystal of alcove paths of type [\'A\', 2, 1] and weight Lambda[0]
        sage: x=C(  () )
        sage: x.f(0)
        ((alpha[0], 0),)
        sage: C.R
        Root system of type [\'A\', 2, 1]
        sage: C.weight
        Lambda[0]

    Test that the tensor products of Kirillov-Reshetikhin crystals
    minus non-pseudo-Demazure arrows is in bijection with alcove path
    construction::

        sage: K = crystals.KirillovReshetikhin([\'B\',3,1],2,1)
        sage: T = crystals.TensorProduct(K,K)
        sage: g = T.digraph() #long time
        sage: for e in g.edges(sort=False):  #long time
        ....:     if e[0].phi(0) == 1 and e[2] == 0:
        ....:         g.delete_edge(e)

        sage: C = crystals.AlcovePaths([\'B\',3,1],[0,2,0], highest_weight_crystal=False)
        sage: g2 = C.digraph() #long time
        sage: g.is_isomorphic(g2, edge_labels = True) #long time
        True

    .. NOTE::

        In type `C_n^{(1)}`, the Kirillov-Reshetikhin crystal is not connected
        when restricted to pseudo-Demazure arrows, hence the previous example will
        fail for type `C_n^{(1)}` crystals.

    ::

        sage: R = RootSystem([\'B\',3])
        sage: P = R.weight_lattice()
        sage: La = P.fundamental_weights()
        sage: D = crystals.AlcovePaths(2*La[2], highest_weight_crystal=False)
        sage: C == D
        True

    .. WARNING:: Weights from finite root systems index non-highest weight crystals.
    '''
    @staticmethod
    def __classcall_private__(cls, starting_weight, cartan_type=None, highest_weight_crystal=None):
        """
        Classcall to mend the input.

        Internally, the
        :class:`~sage.combinat.crystals.alcove_path.CrystalOfAlcovePaths`
        code works with a ``starting_weight`` that is in the weight space
        associated to the crystal. The user can, however, also input a
        ``cartan_type`` and the coefficients of the fundamental weights as
        ``starting_weight``. This code transforms the input into the right
        format (also necessary for :class:`UniqueRepresentation`).

        TESTS::

            sage: C = crystals.AlcovePaths(['A',2,1], [1,0,0])
            sage: C2 = crystals.AlcovePaths(CartanType(['A',2,1]), (1,0,0))
            sage: C is C2
            True
            sage: R = RootSystem(['B',2,1])
            sage: La = R.weight_space().basis()
            sage: B1 = crystals.AlcovePaths(['B',2,1],[0,0,1])
            sage: B2 = crystals.AlcovePaths(La[2])
            sage: B1 is B2
            True
        """
    weight: Incomplete
    R: Incomplete
    module_generators: Incomplete
    def __init__(self, starting_weight, highest_weight_crystal) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: C = crystals.AlcovePaths(['G',2],[0,1])
            sage: TestSuite(C).run()

            sage: C = crystals.AlcovePaths(['A',2,1],[1,0,0])
            sage: TestSuite(C).run() #long time

            sage: C = crystals.AlcovePaths(['A',2,1],[1,0],False)
            sage: TestSuite(C).run(skip='_test_stembridge_local_axioms') #long time

        Check that :issue:`20292` is fixed::

            sage: A = crystals.AlcovePaths(['A',2], [1,0])
            sage: A.category()
            Category of classical crystals
        """
    def vertices(self):
        """
        Return a list of all the vertices of the crystal.

        The vertices are represented as lists of integers recording the folding
        positions.

        One can compute all vertices of the crystal by finding all the
        admissible subsets of the `\\lambda`-chain  (see method
        is_admissible, for definition).  We use the breadth first
        search algorithm.

        .. WARNING::

            This method is (currently) only useful for the case when
            ``highest_weight_crystal = False``, where you cannot always
            reach all vertices of the crystal using crystal operators,
            starting from the highest weight vertex.  This method is
            typically slower than generating the crystal graph using
            crystal operators.

        EXAMPLES::

            sage: C = crystals.AlcovePaths(['C', 2], [1, 0])
            sage: C.vertices()
            [[], [0], [0, 1], [0, 1, 2]]
            sage: C = crystals.AlcovePaths(['C', 2, 1], [2, 1], False)
            sage: len(C.vertices())
            80

        The number of elements reachable using the crystal operators from the
        module generator::

            sage: len(list(C))
            55
        """

class CrystalOfAlcovePathsElement(ElementWrapper):
    """
    Crystal of alcove paths element.

    INPUT:

    - ``data`` -- list of folding positions in the lambda chain (indexing
      starts at 0) or a tuple of :class:`RootsWithHeight` giving folding
      positions in the lambda chain.

    EXAMPLES::

        sage: C = crystals.AlcovePaths(['A',2],[3,2])
        sage: x = C ( () )
        sage: x.f(1).f(2)
        ((alpha[1], 2), (alpha[1] + alpha[2], 4))
        sage: x.f(1).f(2).integer_sequence()
        [8, 9]
        sage: C([8,9])
        ((alpha[1], 2), (alpha[1] + alpha[2], 4))
    """
    def __iter__(self):
        """
        Initialize ``self``.

        EXAMPLES::

            sage: C = crystals.AlcovePaths(['A',2],[1,0])
            sage: lst = list(C)
            sage: for i in lst[2]: i
            (alpha[1], 0)
            (alpha[1] + alpha[2], 0)
        """
    def is_admissible(self):
        """
        Diagnostic test to check if ``self`` is a valid element of the crystal.

        If ``self.value`` is given by

        .. MATH::

            (\\beta_1, i_1), (\\beta_2, i_2), \\ldots, (\\beta_k, i_k),

        for highest weight crystals this checks if the sequence

        .. MATH::

            1 \\rightarrow s_{\\beta_1} \\rightarrow
            s_{\\beta_1}s_{\\beta_2} \\rightarrow \\cdots \\rightarrow
            s_{\\beta_1}s_{\\beta_2} \\ldots s_{\\beta_k}

        is a path in the Bruhat graph. If ``highest_weight_crystal=False``,
        then the method checks if the above sequence is a path in the quantum
        Bruhat graph.

        EXAMPLES::

            sage: C = crystals.AlcovePaths(['A',2],[1,1]); C
            Highest weight crystal of alcove paths of type ['A', 2] and weight Lambda[1] + Lambda[2]
            sage: roots = sorted(C._R._root_lattice.positive_roots()); roots
            [alpha[1], alpha[1] + alpha[2], alpha[2]]
            sage: r1 = C._R(roots[0],0); r1
            (alpha[1], 0)
            sage: r2 = C._R(roots[2],0); r2
            (alpha[2], 0)
            sage: r3 = C._R(roots[1],1); r3
            (alpha[1] + alpha[2], 1)
            sage: x = C( ( r1,r2) )
            sage: x.is_admissible()
            True
            sage: x = C( (r3,) ); x
            ((alpha[1] + alpha[2], 1),)
            sage: x.is_admissible()
            False
            sage: C = crystals.AlcovePaths(['C',2,1],[2,1],False)
            sage: C([7,8]).is_admissible()
            True
            sage: C = crystals.AlcovePaths(['A',2],[3,2])
            sage: C([2,3]).is_admissible()
            True

        .. TODO:: Better doctest
        """
    @cached_in_parent_method
    def integer_sequence(self):
        """
        Return a list of integers corresponding to positions in
        the `\\lambda`-chain where it is folded.

        .. TODO::

            Incorporate this method into the ``_repr_`` for finite Cartan type.

        .. NOTE::

            Only works for finite Cartan types and indexing starts at 0.

        EXAMPLES::

            sage: C = crystals.AlcovePaths(['A',2],[3,2])
            sage: x = C( () )
            sage: x.f(1).f(2).integer_sequence()
            [8, 9]
        """
    def phi(self, i):
        """
        Return the distance to the end of the `i`-string.

        This method overrides the generic implementation in the category of
        crystals since this computation is more efficient.

        EXAMPLES::

            sage: C = crystals.AlcovePaths(['A',2],[1,1])
            sage: [c.phi(1) for c in C]
            [1, 0, 0, 1, 0, 2, 1, 0]
            sage: [c.phi(2) for c in C]
            [1, 2, 1, 0, 0, 0, 0, 1]
        """
    def epsilon(self, i):
        """
        Return the distance to the start of the `i`-string.

        EXAMPLES::

            sage: C = crystals.AlcovePaths(['A',2],[1,1])
            sage: [c.epsilon(1) for c in C]
            [0, 1, 0, 0, 1, 0, 1, 2]
            sage: [c.epsilon(2) for c in C]
            [0, 0, 1, 2, 1, 1, 0, 0]
        """
    def weight(self):
        """
        Return the weight of ``self``.

        EXAMPLES::

            sage: C = crystals.AlcovePaths(['A',2],[2,0])
            sage: for i in C: i.weight()
            (2, 0, 0)
            (1, 1, 0)
            (0, 2, 0)
            (0, -1, 0)
            (-1, 0, 0)
            (-2, -2, 0)
            sage: B = crystals.AlcovePaths(['A',2,1],[1,0,0])
            sage: p = B.module_generators[0].f_string([0,1,2])
            sage: p.weight()
            Lambda[0] - delta

        TESTS:

        Check that crystal morphisms work (:issue:`19481`)::

            sage: C1 = crystals.AlcovePaths(['A',2],[1,0])
            sage: C2 = crystals.AlcovePaths(['A',2],[2,0])
            sage: phi = C1.crystal_morphism(C2.module_generators, scaling_factors={1:2, 2:2})
            sage: [phi(x) for x in C1]
            [(), ((alpha[1], 0),), ((alpha[1], 0), (alpha[1] + alpha[2], 0))]

        Check that all weights are of level 0 in the KR crystal setting
        (:issue:`20292`)::

            sage: A = crystals.AlcovePaths(['A',2,1], [1,0], highest_weight_crystal=False)
            sage: all(x.weight().level() == 0 for x in A)
            True
        """
    def plot(self):
        """
        Return a plot ``self``.

        .. NOTE::

            Currently only implemented for types `A_2`, `B_2`, and `C_2`.

        EXAMPLES::

            sage: C = crystals.AlcovePaths(['A',2],[2,0])
            sage: x = C( () ).f(1).f(2)
            sage: x.plot() # Not tested - creates a pdf
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: C = crystals.AlcovePaths(['B',2],[1,0])
            sage: lst = list(C)
            sage: hash(lst[2]) == hash(lst[2])
            True
        """
    def e(self, i):
        """
        Return the `i`-th crystal raising operator on ``self``.

        INPUT:

        - ``i`` -- element of the index set of the underlying root system

        EXAMPLES::

            sage: C = crystals.AlcovePaths(['A',2],[2,0]); C
            Highest weight crystal of alcove paths of type ['A', 2] and weight 2*Lambda[1]
            sage: x = C( () )
            sage: x.e(1)
            sage: x.f(1) == x.f(1).f(2).e(2)
            True
        """
    def f(self, i):
        """
        Return the `i`-th crystal lowering operator on ``self``.

        INPUT:

        - ``i`` -- element of the index_set of the underlying root_system

        EXAMPLES::

            sage: C=crystals.AlcovePaths(['B',2],[1,1])
            sage: x=C(  () )
            sage: x.f(1)
            ((alpha[1], 0),)
            sage: x.f(1).f(2)
            ((alpha[1], 0), (alpha[1] + alpha[2], 2))
        """
    def path(self):
        """
        Return the path in the (quantum) Bruhat graph corresponding
        to ``self``.

        EXAMPLES::

            sage: C = crystals.AlcovePaths(['B', 3], [3,1,2])
            sage: b = C.highest_weight_vector().f_string([1,3,2,1,3,1])
            sage: b.path()
            [1, s1, s3*s1, s2*s3*s1, s3*s2*s3*s1]
            sage: b = C.highest_weight_vector().f_string([2,3,3,2])
            sage: b.path()
            [1, s2, s3*s2, s2*s3*s2]
            sage: b = C.highest_weight_vector().f_string([2,3,3,2,1])
            sage: b.path()
            [1, s2, s3*s2, s2*s3*s2, s1*s2*s3*s2]
        """

class InfinityCrystalOfAlcovePaths(UniqueRepresentation, Parent):
    """
    `\\mathcal{B}(\\infty)` crystal of alcove paths.
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type):
        """
        Normalize input to ensure a unique representation.

        TESTS::

            sage: A1 = crystals.infinity.AlcovePaths(['A',2])
            sage: A2 = crystals.infinity.AlcovePaths(CartanType(['A',2]))
            sage: A3 = crystals.infinity.AlcovePaths('A2')
            sage: A1 is A2 and A2 is A3
            True
        """
    module_generators: Incomplete
    def __init__(self, cartan_type) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: A = crystals.infinity.AlcovePaths(['C',3])
            sage: TestSuite(A).run(max_runs=20)

            sage: A = crystals.infinity.AlcovePaths(['A',2,1])
            sage: TestSuite(A).run() # long time
        """
    class Element(ElementWrapper):
        def __init__(self, parent, elt, shift) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: A = crystals.infinity.AlcovePaths(['F',4])
                sage: mg = A.highest_weight_vector()
                sage: x = mg.f_string([2,3,1,4,4,2,3,1])
                sage: TestSuite(x).run()
            """
        def e(self, i):
            """
            Return the action of `e_i` on ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: A = crystals.infinity.AlcovePaths(['D',5,1])
                sage: mg = A.highest_weight_vector()
                sage: x = mg.f_string([1,3,4,2,5,4,5,5])
                sage: x.f(4).e(5) == x.e(5).f(4)
                True
            """
        def f(self, i):
            """
            Return the action of `f_i` on ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: A = crystals.infinity.AlcovePaths(['E',7,1])
                sage: mg = A.highest_weight_vector()
                sage: mg.f_string([1,3,5,6,4,2,0,2,1,0,2,4,7,4,2])
                ((alpha[2], -3), (alpha[5], -1), (alpha[1], -1),
                 (alpha[0] + alpha[1], -2),
                 (alpha[2] + alpha[4] + alpha[5], -2),
                 (alpha[5] + alpha[6], -1), (alpha[1] + alpha[3], -1),
                 (alpha[5] + alpha[6] + alpha[7], -1),
                 (alpha[0] + alpha[1] + alpha[3], -1),
                 (alpha[1] + alpha[3] + alpha[4] + alpha[5], -1))
            """
        def epsilon(self, i):
            """
            Return `\\varepsilon_i` of ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: A = crystals.infinity.AlcovePaths(['A',7,2])
                sage: mg = A.highest_weight_vector()
                sage: x = mg.f_string([1,0,2,3,4,4,4,2,3,3,3])
                sage: [x.epsilon(i) for i in A.index_set()]
                [0, 0, 0, 3, 0]
                sage: x = mg.f_string([2,2,1,1,0,1,0,2,3,3,3,4])
                sage: [x.epsilon(i) for i in A.index_set()]
                [1, 2, 0, 1, 1]
            """
        def phi(self, i):
            """
            Return `\\varphi_i` of ``self``.

            Let `A \\in \\mathcal{B}(\\infty)` Define `\\varphi_i(A) :=
            \\varepsilon_i(A) + \\langle h_i, \\mathrm{wt}(A) \\rangle`,
            where `h_i` is the `i`-th simple coroot and `\\mathrm{wt}(A)`
            is the :meth:`weight` of `A`.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: A = crystals.infinity.AlcovePaths(['A',8,2])
                sage: mg = A.highest_weight_vector()
                sage: x = mg.f_string([1,0,2,3,4,4,4,2,3,3,3])
                sage: [x.phi(i) for i in A.index_set()]
                [1, 1, 1, 3, -2]
                sage: x = mg.f_string([2,2,1,1,0,1,0,2,3,3,3,4])
                sage: [x.phi(i) for i in A.index_set()]
                [4, -1, 0, 0, 2]
            """
        def weight(self):
            """
            Return the weight of ``self``.

            EXAMPLES::

                sage: A = crystals.infinity.AlcovePaths(['E',6])
                sage: mg = A.highest_weight_vector()
                sage: fstr = [1,3,4,2,1,2,3,6,5,3,2,6,2]
                sage: x = mg.f_string(fstr)
                sage: al = A.weight_lattice_realization().simple_roots()
                sage: x.weight() == -sum(al[i]*fstr.count(i) for i in A.index_set())
                True
            """
        def projection(self, k=None):
            """
            Return the projection ``self`` onto `B(k \\rho)`.

            INPUT:

            - ``k`` -- (optional) if not given, defaults to the smallest
              value such that ``self`` is not ``None`` under the projection

            EXAMPLES::

                sage: A = crystals.infinity.AlcovePaths(['G',2])
                sage: mg = A.highest_weight_vector()
                sage: x = mg.f_string([2,1,1,2,2,2,1,1]); x
                ((alpha[2], -3), (alpha[1] + alpha[2], -3),
                 (3*alpha[1] + 2*alpha[2], -1), (2*alpha[1] + alpha[2], -1))
                sage: x.projection()
                ((alpha[2], 0), (alpha[1] + alpha[2], 9),
                 (3*alpha[1] + 2*alpha[2], 8), (2*alpha[1] + alpha[2], 14))
                sage: x.projection().parent()
                Highest weight crystal of alcove paths of type ['G', 2]
                 and weight 3*Lambda[1] + 3*Lambda[2]

                sage: mg.projection().parent()
                Highest weight crystal of alcove paths of type ['G', 2]
                 and weight 0
                sage: mg.f(1).projection().parent()
                Highest weight crystal of alcove paths of type ['G', 2]
                 and weight Lambda[1] + Lambda[2]
                sage: mg.f(1).f(2).projection().parent()
                Highest weight crystal of alcove paths of type ['G', 2]
                 and weight Lambda[1] + Lambda[2]
                sage: b = mg.f_string([1,2,2,1,2])
                sage: b.projection().parent()
                Highest weight crystal of alcove paths of type ['G', 2]
                 and weight 2*Lambda[1] + 2*Lambda[2]
                sage: b.projection(3).parent()
                Highest weight crystal of alcove paths of type ['G', 2]
                 and weight 3*Lambda[1] + 3*Lambda[2]
                sage: b.projection(1)
            """

class RootsWithHeight(UniqueRepresentation, Parent):
    """
    Data structure of the ordered pairs `(\\beta,k)`,
    where `\\beta` is a positive root and `k` is a nonnegative integer. A total
    order is implemented on this set, and depends on the weight.

    INPUT:

    - ``cartan_type`` -- Cartan type of a finite or affine untwisted root
      system

    - ``weight`` -- dominant weight as a list of (integral) coefficients of
      the fundamental weights

    EXAMPLES::

        sage: from sage.combinat.crystals.alcove_path import RootsWithHeight
        sage: R = RootsWithHeight(['A',2],[1,1]); R
        Roots with height of Cartan type ['A', 2] and dominant weight Lambda[1] + Lambda[2]

        sage: r1 = R._root_lattice.from_vector(vector([1,0])); r1
        alpha[1]
        sage: r2 = R._root_lattice.from_vector(vector([1,1])); r2
        alpha[1] + alpha[2]

        sage: x = R(r1,0); x
        (alpha[1], 0)
        sage: y = R(r2,1); y
        (alpha[1] + alpha[2], 1)
        sage: x < y
        True
    """
    @staticmethod
    def __classcall_private__(cls, starting_weight, cartan_type=None):
        """
        Classcall to mend the input.

        Internally, the RootsWithHeight code works with a ``starting_weight`` that
        is in the ``weight_space`` associated to the crystal. The user can, however,
        also input a ``cartan_type`` and the coefficients of the fundamental weights
        as ``starting_weight``. This code transforms the input into the right
        format (also necessary for UniqueRepresentation).

        TESTS::

            sage: from sage.combinat.crystals.alcove_path import RootsWithHeight
            sage: R = RootsWithHeight(['A',2],[3,2])
            sage: S = RootsWithHeight(CartanType(['A',2]), (3,2))
            sage: R is S
            True

            sage: R = RootSystem(['B',2,1])
            sage: La = R.weight_space().basis()
            sage: C = RootsWithHeight(['B',2,1],[0,0,1])
            sage: B = RootsWithHeight(La[2])
            sage: B is C
            True
        """
    weight: Incomplete
    def __init__(self, weight) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.combinat.crystals.alcove_path import RootsWithHeight
            sage: R = RootsWithHeight(['A',2],[3,2])
            sage: TestSuite(R).run()
        """
    @cached_method
    def word(self):
        """
        Give the initial alcove path (`\\lambda`-chain) in terms of simple
        roots. Used for plotting the path.

        .. NOTE::

            Currently only implemented for finite Cartan types.

        EXAMPLES::

            sage: from sage.combinat.crystals.alcove_path import RootsWithHeight
            sage: R = RootsWithHeight(['A',2],[3,2])
            sage: R.word()
            [2, 1, 2, 0, 1, 2, 1, 0, 1, 2]
        """
    @cached_method
    def lambda_chain(self):
        """
        Return the unfolded `\\lambda`-chain.

        .. NOTE:: Only works in root systems of finite type.

        EXAMPLES::

            sage: from sage.combinat.crystals.alcove_path import RootsWithHeight
            sage: R = RootsWithHeight(['A',2],[1,1]); R
            Roots with height of Cartan type ['A', 2] and dominant weight Lambda[1] + Lambda[2]
            sage: R.lambda_chain()
            [(alpha[2], 0), (alpha[1] + alpha[2], 0), (alpha[1], 0), (alpha[1] + alpha[2], 1)]
        """

class RootsWithHeightElement(Element):
    """
    Element of :class:`RootsWithHeight`.

    INPUT:

    - ``root`` -- a positive root `\\beta` in our root system
    - ``height`` -- integer such that
      `0 \\leq l \\leq \\langle \\lambda, \\beta^{\\vee} \\rangle`

    EXAMPLES::

        sage: from sage.combinat.crystals.alcove_path import RootsWithHeight
        sage: rl = RootSystem(['A',2]).root_lattice()
        sage: x = rl.from_vector(vector([1,1])); x
        alpha[1] + alpha[2]
        sage: R = RootsWithHeight(['A',2],[1,1]); R
        Roots with height of Cartan type ['A', 2] and dominant weight Lambda[1] + Lambda[2]
        sage: y = R(x, 1); y
        (alpha[1] + alpha[2], 1)
    """
    root: Incomplete
    height: Incomplete
    def __init__(self, parent, root, height) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.combinat.crystals.alcove_path import RootsWithHeight
            sage: rl = RootSystem(['A',2]).root_lattice()
            sage: x = rl.from_vector(vector([1,1]))
            sage: R = RootsWithHeight(['A',2],[3,2])
            sage: y = R(x, 1); y
            (alpha[1] + alpha[2], 1)
            sage: TestSuite(x).run()
        """
    def __hash__(self):
        """

        EXAMPLES::

            sage: from sage.combinat.crystals.alcove_path import RootsWithHeight
            sage: R = RootsWithHeight(['A',2],[3,2])
            sage: rl = RootSystem(['A',2]).root_lattice()
            sage: root = rl.from_vector(vector([1,1]))
            sage: vec = R(root,0)
            sage: hash(vec) == hash(vec)
            True
        """
    def __eq__(self, other):
        """

        EXAMPLES::

            sage: from sage.combinat.crystals.alcove_path import RootsWithHeight
            sage: R = RootsWithHeight(['A',2],[3,2])
            sage: rl = RootSystem(['A',2]).root_lattice()
            sage: v1 = rl.from_vector(vector([1,1]))
            sage: v2 = rl.from_vector(vector([1]))
            sage: x1 = R(v1,1) ; x2 = R(v1,0) ; x3 = R(v2,1)
            sage: x1.__eq__(x1)
            True
            sage: x1.__eq__(x2)
            False
            sage: x1.__eq__(x3)
            False
        """

def compare_graphs(g1, g2, node1, node2):
    """
    Compare two edge-labeled :class:`graphs <DiGraph>` obtained from
    ``Crystal.digraph()``, starting from the root nodes of each graph.

    - ``g1`` -- :class:`graphs <DiGraph>`, first digraph
    - ``g2`` -- :class:`graphs <DiGraph>`, second digraph
    - ``node1`` -- element of ``g1``
    - ``node2`` -- element of ``g2``

    Traverse ``g1`` starting at ``node1`` and compare this graph with
    the one obtained by traversing ``g2`` starting with ``node2``.
    If the graphs match (including labels) then return ``True``.
    Return ``False`` otherwise.

    EXAMPLES::

        sage: from sage.combinat.crystals.alcove_path import compare_graphs
        sage: G1 = crystals.Tableaux(['A',3], shape=[1,1]).digraph()
        sage: C = crystals.AlcovePaths(['A',3],[0,1,0])
        sage: G2 = C.digraph()
        sage: compare_graphs(G1, G2, C( () ), G2.vertices(sort=True)[0])
        True
    """
