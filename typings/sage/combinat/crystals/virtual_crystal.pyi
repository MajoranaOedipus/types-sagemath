from sage.categories.crystals import Crystals as Crystals
from sage.categories.finite_crystals import FiniteCrystals as FiniteCrystals
from sage.combinat.crystals.subcrystal import Subcrystal as Subcrystal
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.sets.family import Family as Family

class VirtualCrystal(Subcrystal):
    """
    A virtual crystal `V` of an ambient crystal `\\widehat{B}` is a crystal
    formed by taking a subset of `\\widehat{B}` and whose crystal structure
    is given by

    .. MATH::

        e_i = \\prod_{j \\in \\sigma_i} \\widehat{e}_j^{\\gamma_i}, \\quad
        f_i = \\prod_{j \\in \\sigma_i} \\widehat{f}_j^{\\gamma_i},

    .. MATH::

        \\varepsilon_i = \\frac{\\widehat{\\varepsilon}_j}{\\gamma_j}, \\quad
        \\varphi_i = \\frac{\\widehat{\\varphi}_j}{\\gamma_j}, \\quad
        \\operatorname{wt} = \\Psi^{-1} \\circ \\widehat{\\operatorname{wt}}

    where `\\sigma_i` is a subset of the index set of `B`, `\\gamma_i \\in \\ZZ`
    are the *scaling factors*, and `\\Psi : P \\to \\widehat{P}` is an embedding
    of the weight lattices. We note that for the crystal to be well-defined,
    we must have

    .. MATH::

        \\widehat{\\varepsilon}_j = \\widehat{\\varepsilon|j^{\\prime}},
        \\quad \\widehat{\\varphi}_j = \\widehat{\\varphi}_{j^{\\prime}}

    for all `j, j^{\\prime} \\in \\sigma_i` and that the order that the Kashiwara
    operators in the ambient space are applied does not affect the result.

    INPUT:

    - ``ambient`` -- the ambient crystal
    - ``virtualization`` -- dictionary whose key `i` corresponds
      to the set `\\sigma_i`
    - ``scaling_factors`` -- dictionary whose key `i` corresponds to
      the scaling factor `\\gamma_i`
    - ``contained`` -- (optional) a set (or function) which specifies when an
      element is contained in the subcrystal; the default is everything
      possible is included
    - ``generators`` -- (optional) the generators for the virtual crystal; the
      default is the generators for the ambient crystal
    - ``cartan_type`` -- (optional) the Cartan type for the virtual crystal;
      the default is the Cartan type for the ambient crystal
    - ``index_set`` -- (optional) the index set for the virtual crystal; the
      default is the index set for the Cartan type
    - ``category`` -- (optional) the category for the virtual crystal; the
      default is the :class:`~sage.categories.crystals.Crystals` category

    EXAMPLES:

    We construct an example from a natural virtualization map of type `C_n`
    in type `A_{2n-1}`::

        sage: C = crystals.Tableaux(['C',2], shape=[1])
        sage: A = crystals.Tableaux(['A',3], shape=[2,1,1])
        sage: psi = C.crystal_morphism(A.module_generators)
        sage: V = psi.image()
        sage: list(V)
        [[[1, 1], [2], [3]],
         [[1, 2], [2], [4]],
         [[1, 3], [3], [4]],
         [[2, 4], [3], [4]]]
        sage: V.digraph().is_isomorphic(C.digraph(), edge_labels=True)
        True

    We construct the virtualization of a `U_q'(\\mathfrak{g})`-crystal
    `B^{r,s}` of type `C_n^{(1)}` in type `A_{2n+1}^{(2)}`. Here it is not
    a default folding known to Sage, so we have to explicitly state the
    folding (since the scaling factors are not specified, they are all
    assumed to be 1)::

        sage: K = crystals.KirillovReshetikhin(['C',2,1], 1,1)
        sage: VK = crystals.KirillovReshetikhin(['A',5,2], 1,1)
        sage: target = VK.module_generator().f(1); target
        [[2]]
        sage: psi = K.crystal_morphism({K.module_generator(): target},
        ....:                          virtualization={0:[0,1], 1:[2], 2:[3]})
        sage: V = psi.image()
        sage: list(V)
        [[[2]], [[3]], [[-2]], [[-3]]]
        sage: V.digraph().is_isomorphic(K.digraph(), edge_labels=True)
        True

    We create an example of `B(\\Lambda_n)` of type `B_n` inside
    of `B(2\\Lambda_n)` using the doubling map through the (virtual)
    subcrystal method::

        sage: BB = crystals.Tableaux(['B',3], shape=[1,1,1])
        sage: S = BB.subcrystal(scaling_factors={1:2, 2:2, 3:2})
        sage: B = crystals.Tableaux(['B',3], shape=[1/2,1/2,1/2])
        sage: S.digraph().is_isomorphic(B.digraph(), edge_labels=True)
        True

    We can also directly construct a virtual crystal using
    :class:`VirtualCrystal` (however it is recommended to use either
    :meth:`~sage.categories.crystals.Crystals.ParentMethods.crystal_morphism`
    or :meth:`~sage.categories.crystals.Crystals.ParentMethods.subcrystal`)::

        sage: from sage.combinat.crystals.virtual_crystal import VirtualCrystal
        sage: A = crystals.Tableaux(['A',3], shape=[2,1,1])
        sage: V = VirtualCrystal(A, {1:(1,3), 2:(2,)}, {1:1, 2:2}, cartan_type=['C',2])
        sage: G = crystals.Tableaux(['C',2], shape=[1]).digraph()
        sage: V.digraph().is_isomorphic(G, edge_labels=True)
        True

        sage: C1 = crystals.Tableaux(['A',3], shape=[1])
        sage: C2 = crystals.Tableaux(['A',3], shape=[1,1,1])
        sage: T = C1.tensor(C2)
        sage: mg = T(C1.module_generators[0], C2.module_generators[0])
        sage: V = VirtualCrystal(A, {1:(1,3), 2:(2,)}, {1:1, 2:2},
        ....:                    cartan_type=['C',2], generators=[mg])
        sage: V.digraph().is_isomorphic(G, edge_labels=True)
        True

    REFERENCES:

    - [FOS2009]_
    - [OSS03]_
    - [OSS2003]_
    """
    @staticmethod
    def __classcall_private__(cls, ambient, virtualization, scaling_factors, contained=None, generators=None, cartan_type=None, index_set=None, category=None):
        """
        Normalize arguments to ensure a unique representation.

        EXAMPLES::

            sage: B = crystals.Tableaux(['B',3], shape=[1])
            sage: C = crystals.Tableaux(['D',4], shape=[2])
            sage: psi1 = B.crystal_morphism(C.module_generators)
            sage: V1 = psi1.image()
            sage: psi2 = B.crystal_morphism(C.module_generators, index_set=[1,2,3])
            sage: V2 = psi2.image()
            sage: V1 is V2
            True

        TESTS:

        Check that :issue:`19481` is fixed::

            sage: from sage.combinat.crystals.virtual_crystal import VirtualCrystal
            sage: A = crystals.Tableaux(['A',3], shape=[2,1,1])
            sage: V = VirtualCrystal(A, {1:(1,3), 2:(2,)}, {1:1, 2:2}, cartan_type=['C',2])
            sage: V.category()
            Category of finite crystals
        """
    def __init__(self, ambient, virtualization, scaling_factors, contained, generators, cartan_type, index_set, category) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: B = crystals.Tableaux(['B',3], shape=[1])
            sage: C = crystals.Tableaux(['D',4], shape=[2])
            sage: psi = B.crystal_morphism(C.module_generators)
            sage: V = psi.image()
            sage: TestSuite(V).run()
        """
    def __contains__(self, x) -> bool:
        """
        Check if ``x`` is in ``self``.

        EXAMPLES::

            sage: B = crystals.Tableaux(['B',3], shape=[1])
            sage: C = crystals.Tableaux(['D',4], shape=[2])
            sage: psi = B.crystal_morphism(C.module_generators)
            sage: V = psi.image()
            sage: mg = C.module_generators[0]
            sage: mg in V
            True
            sage: mg.f(1) in V
            False
            sage: mg.f(1).f(1) in V
            True
        """
    def virtualization(self):
        """
        Return the virtualization sets `\\sigma_i`.

        EXAMPLES::

            sage: B = crystals.Tableaux(['B',3], shape=[1])
            sage: C = crystals.Tableaux(['D',4], shape=[2])
            sage: psi = B.crystal_morphism(C.module_generators)
            sage: V = psi.image()
            sage: V.virtualization()
            Finite family {1: (1,), 2: (2,), 3: (3, 4)}
        """
    def scaling_factors(self):
        """
        Return the scaling factors `\\gamma_i`.

        EXAMPLES::

            sage: B = crystals.Tableaux(['B',3], shape=[1])
            sage: C = crystals.Tableaux(['D',4], shape=[2])
            sage: psi = B.crystal_morphism(C.module_generators)
            sage: V = psi.image()
            sage: V.scaling_factors()
            Finite family {1: 2, 2: 2, 3: 1}
        """
    class Element(Subcrystal.Element):
        """
        An element of a virtual (sub)crystal. Wraps an element in the
        ambient crystal.
        """
        def e(self, i):
            """
            Return `e_i` of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['B',3], shape=[1])
                sage: C = crystals.Tableaux(['D',4], shape=[2])
                sage: psi = B.crystal_morphism(C.module_generators)
                sage: V = psi.image()
                sage: mg = V.module_generators[0]
                sage: mg.e(1)
                sage: b = psi(B.module_generators[0].f(1))
                sage: V(b).e(1)
                [[1, 1]]
            """
        def f(self, i):
            """
            Return `f_i` of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['B',3], shape=[1])
                sage: C = crystals.Tableaux(['D',4], shape=[2])
                sage: psi = B.crystal_morphism(C.module_generators)
                sage: V = psi.image()
                sage: mg = V.module_generators[0]
                sage: mg.f(1)
                [[2, 2]]
                sage: mg.f(2)
            """
        def epsilon(self, i):
            """
            Return `\\varepsilon_i` of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['B',3], shape=[1])
                sage: C = crystals.Tableaux(['D',4], shape=[2])
                sage: psi = B.crystal_morphism(C.module_generators)
                sage: V = psi.image()
                sage: mg = V.module_generators[0]
                sage: mg.epsilon(2)
                0
                sage: mg.f(1).epsilon(1)
                1
            """
        def phi(self, i):
            """
            Return `\\varphi_i` of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['B',3], shape=[1])
                sage: C = crystals.Tableaux(['D',4], shape=[2])
                sage: psi = B.crystal_morphism(C.module_generators)
                sage: V = psi.image()
                sage: mg = V.module_generators[0]
                sage: mg.phi(1)
                1
                sage: mg.phi(2)
                0
            """
        def weight(self):
            """
            Return the weight of ``self``.

            EXAMPLES::

                sage: B = crystals.Tableaux(['B',3], shape=[1])
                sage: C = crystals.Tableaux(['D',4], shape=[2])
                sage: psi = B.crystal_morphism(C.module_generators)
                sage: V = psi.image()
                sage: mg = V.module_generators[0]
                sage: mg.weight()
                (1, 0, 0)
                sage: mg.f(1).weight()
                (0, 1, 0)
                sage: all(V(psi(x)).weight() == x.weight() for x in B)
                True
            """
