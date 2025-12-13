from _typeshed import Incomplete
from sage.categories.classical_crystals import ClassicalCrystals as ClassicalCrystals
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.loop_crystals import KirillovReshetikhinCrystals as KirillovReshetikhinCrystals, RegularLoopCrystals as RegularLoopCrystals
from sage.categories.regular_crystals import RegularCrystals as RegularCrystals
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.root_system import RootSystem as RootSystem
from sage.misc.cachefunc import cached_in_parent_method as cached_in_parent_method, cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class CrystalOfLSPaths(UniqueRepresentation, Parent):
    """
    Crystal graph of LS paths generated from the straight-line path
    to a given weight.

    INPUT:

    - ``cartan_type`` -- (optional) the Cartan type
    - ``starting_weight`` -- a weight; if ``cartan_type`` is given,
      then the weight should be given as a list of coefficients of
      the fundamental weights, otherwise it should be given in the
      ``weight_space`` basis; for affine highest weight crystals,
      one needs to use the extended weight space

    The crystal class of piecewise linear paths in the weight space,
    generated from a straight-line path from the origin to a given
    element of the weight lattice.

    EXAMPLES::

        sage: R = RootSystem(['A',2,1])
        sage: La = R.weight_space(extended = True).basis()
        sage: B = crystals.LSPaths(La[2]-La[0]); B
        The crystal of LS paths of type ['A', 2, 1] and weight -Lambda[0] + Lambda[2]

        sage: C = crystals.LSPaths(['A',2,1],[-1,0,1]); C
        The crystal of LS paths of type ['A', 2, 1] and weight -Lambda[0] + Lambda[2]
        sage: B == C
        True
        sage: c = C.module_generators[0]; c
        (-Lambda[0] + Lambda[2],)
        sage: [c.f(i) for i in C.index_set()]
        [None, None, (Lambda[1] - Lambda[2],)]

        sage: R = C.R; R
        Root system of type ['A', 2, 1]
        sage: Lambda = R.weight_space().basis(); Lambda
        Finite family {0: Lambda[0], 1: Lambda[1], 2: Lambda[2]}
        sage: b=C(tuple([-Lambda[0]+Lambda[2]]))
        sage: b==c
        True
        sage: b.f(2)
        (Lambda[1] - Lambda[2],)

    For classical highest weight crystals, we can also compare the results
    with the tableaux implementation::

        sage: C = crystals.LSPaths(['A',2],[1,1])
        sage: sorted(C, key=str)
        [(-2*Lambda[1] + Lambda[2],), (-Lambda[1] + 1/2*Lambda[2], Lambda[1] - 1/2*Lambda[2]),
         (-Lambda[1] + 2*Lambda[2],), (-Lambda[1] - Lambda[2],),
         (1/2*Lambda[1] - Lambda[2], -1/2*Lambda[1] + Lambda[2]), (2*Lambda[1] - Lambda[2],),
         (Lambda[1] + Lambda[2],), (Lambda[1] - 2*Lambda[2],)]
        sage: C.cardinality()
        8
        sage: B = crystals.Tableaux(['A',2],shape=[2,1])
        sage: B.cardinality()
        8
        sage: B.digraph().is_isomorphic(C.digraph())
        True

    Make sure you use the weight space and not the weight lattice
    for your weights::

        sage: R = RootSystem(['A',2,1])
        sage: La = R.weight_lattice(extended = True).basis()
        sage: B = crystals.LSPaths(La[2]); B
        Traceback (most recent call last):
        ...
        ValueError: use the weight space, rather than weight lattice for your weights

    REFERENCES:

    - [Li1995b]_
    """
    @staticmethod
    def __classcall_private__(cls, starting_weight, cartan_type=None, starting_weight_parent=None):
        """
        Classcall to mend the input.

        Internally, the
        :class:`~sage.combinat.crystals.littelmann_path.CrystalOfLSPaths` code
        works with a ``starting_weight`` that is in the weight space associated
        to the crystal. The user can, however, also input a ``cartan_type``
        and the coefficients of the fundamental weights as
        ``starting_weight``. This code transforms the input into the right
        format (also necessary for UniqueRepresentation).

        TESTS::

            sage: crystals.LSPaths(['A',2,1], [-1,0,1])
            The crystal of LS paths of type ['A', 2, 1] and weight -Lambda[0] + Lambda[2]

            sage: R = RootSystem(['B',2,1])
            sage: La = R.weight_space(extended=True).basis()
            sage: C = crystals.LSPaths(['B',2,1],[0,0,1])
            sage: B = crystals.LSPaths(La[2])
            sage: B is C
            True

            sage: La = RootSystem(['A', 3]).weight_space().fundamental_weights()
            sage: crystals.LSPaths(['A', 3], La[2])
            The crystal of LS paths of type ['A', 3] and weight Lambda[2]

            sage: crystals.LSPaths(La[2] + 2*La[3], ['A', 3])
            The crystal of LS paths of type ['A', 3] and weight Lambda[2] + 2*Lambda[3]

            sage: crystals.LSPaths(La[2], starting_weight_parent=RootSystem(['B', 3]).weight_space())
            Traceback (most recent call last):
            ...
            ValueError: the passed parent is not equal to parent of the inputted weight
        """
    R: Incomplete
    weight: Incomplete
    module_generators: Incomplete
    def __init__(self, starting_weight, starting_weight_parent) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: C = crystals.LSPaths(['A',2,1],[-1,0,1]); C
            The crystal of LS paths of type ['A', 2, 1] and weight -Lambda[0] + Lambda[2]
            sage: C.R
            Root system of type ['A', 2, 1]
            sage: C.weight
            -Lambda[0] + Lambda[2]
            sage: C.weight.parent()
            Extended weight space over the Rational Field of the Root system of type ['A', 2, 1]
            sage: C.module_generators
            ((-Lambda[0] + Lambda[2],),)

        TESTS::

            sage: C = crystals.LSPaths(['A',2,1], [-1,0,1])
            sage: TestSuite(C).run() # long time
            sage: C = crystals.LSPaths(['E',6], [1,0,0,0,0,0])
            sage: TestSuite(C).run()

            sage: R = RootSystem(['C',3,1])
            sage: La = R.weight_space().basis()
            sage: LaE = R.weight_space(extended=True).basis()
            sage: B = crystals.LSPaths(La[0])
            sage: BE = crystals.LSPaths(LaE[0])
            sage: B is BE
            False
            sage: B.weight_lattice_realization()
            Weight space over the Rational Field of the Root system of type ['C', 3, 1]
            sage: BE.weight_lattice_realization()
            Extended weight space over the Rational Field of the Root system of type ['C', 3, 1]
        """
    def weight_lattice_realization(self):
        """
        Return weight lattice realization of ``self``.

        EXAMPLES::

            sage: B = crystals.LSPaths(['B',3],[1,1,0])
            sage: B.weight_lattice_realization()
            Weight space over the Rational Field of the Root system of type ['B', 3]
            sage: B = crystals.LSPaths(['B',3,1],[1,1,1,0])
            sage: B.weight_lattice_realization()
            Extended weight space over the Rational Field of the Root system of type ['B', 3, 1]
        """
    class Element(ElementWrapper):
        """
        A Littelmann path (crystal element).

        TESTS::

            sage: C = crystals.LSPaths(['E',6],[1,0,0,0,0,0])
            sage: c = C.an_element()
            sage: TestSuite(c).run()
        """
        def endpoint(self):
            """
            Compute the endpoint of ``self``.

            EXAMPLES::

                sage: C = crystals.LSPaths(['A',2],[1,1])
                sage: b = C.module_generators[0]
                sage: b.endpoint()
                Lambda[1] + Lambda[2]
                sage: b.f_string([1,2,2,1])
                (-Lambda[1] - Lambda[2],)
                sage: b.f_string([1,2,2,1]).endpoint()
                -Lambda[1] - Lambda[2]
                sage: b.f_string([1,2])
                (1/2*Lambda[1] - Lambda[2], -1/2*Lambda[1] + Lambda[2])
                sage: b.f_string([1,2]).endpoint()
                0
                sage: b = C([])
                sage: b.endpoint()
                0
            """
        def compress(self):
            """
            Merge consecutive positively parallel steps present in ``self``.

            EXAMPLES::

                sage: C = crystals.LSPaths(['A',2],[1,1])
                sage: Lambda = C.R.weight_space().fundamental_weights(); Lambda
                Finite family {1: Lambda[1], 2: Lambda[2]}
                sage: c = C(tuple([1/2*Lambda[1]+1/2*Lambda[2], 1/2*Lambda[1]+1/2*Lambda[2]]))
                sage: c.compress()
                (Lambda[1] + Lambda[2],)
            """
        def split_step(self, which_step, r):
            """
            Split the indicated step into two parallel steps of relative
            lengths `r` and `1-r`.

            INPUT:

            - ``which_step`` -- a position in the tuple ``self``
            - ``r`` -- a rational number between 0 and 1

            EXAMPLES::

                sage: C = crystals.LSPaths(['A',2],[1,1])
                sage: b = C.module_generators[0]
                sage: b.split_step(0,1/3)
                (1/3*Lambda[1] + 1/3*Lambda[2], 2/3*Lambda[1] + 2/3*Lambda[2])
            """
        def reflect_step(self, which_step, i):
            """
            Apply the `i`-th simple reflection to the indicated step in ``self``.

            EXAMPLES::

                sage: C = crystals.LSPaths(['A',2],[1,1])
                sage: b = C.module_generators[0]
                sage: b.reflect_step(0,1)
                (-Lambda[1] + 2*Lambda[2],)
                sage: b.reflect_step(0,2)
                (2*Lambda[1] - Lambda[2],)
            """
        def epsilon(self, i):
            """
            Return the distance to the beginning of the `i`-string.

            This method overrides the generic implementation in the category of crystals
            since this computation is more efficient.

            EXAMPLES::

                sage: C = crystals.LSPaths(['A',2],[1,1])
                sage: [c.epsilon(1) for c in C]
                [0, 1, 0, 0, 1, 0, 1, 2]
                sage: [c.epsilon(2) for c in C]
                [0, 0, 1, 2, 1, 1, 0, 0]
            """
        def phi(self, i):
            """
            Return the distance to the end of the `i`-string.

            This method overrides the generic implementation in the category of crystals
            since this computation is more efficient.

            EXAMPLES::

                sage: C = crystals.LSPaths(['A',2],[1,1])
                sage: [c.phi(1) for c in C]
                [1, 0, 0, 1, 0, 2, 1, 0]
                sage: [c.phi(2) for c in C]
                [1, 2, 1, 0, 0, 0, 0, 1]
            """
        def e(self, i, power: int = 1, to_string_end: bool = False, length_only: bool = False):
            """
            Return the `i`-th crystal raising operator on ``self``.

            INPUT:

            - ``i`` -- element of the index set of the underlying root system
            - ``power`` -- positive integer (default: 1); specifies the power
              of the raising operator to be applied
            - ``to_string_end`` -- boolean (default: ``False``); if ``True``,
              returns the dominant end of the `i`-string of ``self``
            - ``length_only`` -- boolean; if ``True``, returns the distance
              to the dominant end of the `i`-string of ``self``

            EXAMPLES::

                sage: C = crystals.LSPaths(['A',2],[1,1])
                sage: c = C[2]; c
                (1/2*Lambda[1] - Lambda[2], -1/2*Lambda[1] + Lambda[2])
                sage: c.e(1)
                sage: c.e(2)
                (-Lambda[1] + 2*Lambda[2],)
                sage: c.e(2,to_string_end=True)
                (-Lambda[1] + 2*Lambda[2],)
                sage: c.e(1,to_string_end=True)
                (1/2*Lambda[1] - Lambda[2], -1/2*Lambda[1] + Lambda[2])
                sage: c.e(1,length_only=True)
                0
            """
        def dualize(self):
            '''
            Return the dualized path of ``self``.

            EXAMPLES::

                sage: C = crystals.LSPaths([\'A\',2],[1,1])
                sage: for c in C:
                ....:     print("{} {}".format(c, c.dualize()))
                (Lambda[1] + Lambda[2],) (-Lambda[1] - Lambda[2],)
                (-Lambda[1] + 2*Lambda[2],) (Lambda[1] - 2*Lambda[2],)
                (1/2*Lambda[1] - Lambda[2], -1/2*Lambda[1] + Lambda[2]) (1/2*Lambda[1] - Lambda[2], -1/2*Lambda[1] + Lambda[2])
                (Lambda[1] - 2*Lambda[2],) (-Lambda[1] + 2*Lambda[2],)
                (-Lambda[1] - Lambda[2],) (Lambda[1] + Lambda[2],)
                (2*Lambda[1] - Lambda[2],) (-2*Lambda[1] + Lambda[2],)
                (-Lambda[1] + 1/2*Lambda[2], Lambda[1] - 1/2*Lambda[2]) (-Lambda[1] + 1/2*Lambda[2], Lambda[1] - 1/2*Lambda[2])
                (-2*Lambda[1] + Lambda[2],) (2*Lambda[1] - Lambda[2],)
            '''
        def f(self, i, power: int = 1, to_string_end: bool = False, length_only: bool = False):
            """
            Return the `i`-th crystal lowering operator on ``self``.

            INPUT:

            - ``i`` -- element of the index set of the underlying root system
            - ``power`` -- positive integer (default: 1); specifies the power
              of the lowering operator to be applied
            - ``to_string_end`` -- boolean (default: ``False``); if ``True``,
              returns the anti-dominant end of the `i`-string of ``self``
            - ``length_only`` -- boolean; if ``True``, returns the distance
              to the anti-dominant end of the `i`-string of ``self``

            EXAMPLES::

                sage: C = crystals.LSPaths(['A',2],[1,1])
                sage: c = C.module_generators[0]
                sage: c.f(1)
                (-Lambda[1] + 2*Lambda[2],)
                sage: c.f(1,power=2)
                sage: c.f(2)
                (2*Lambda[1] - Lambda[2],)
                sage: c.f(2,to_string_end=True)
                (2*Lambda[1] - Lambda[2],)
                sage: c.f(2,length_only=True)
                1

                sage: C = crystals.LSPaths(['A',2,1],[-1,-1,2])
                sage: c = C.module_generators[0]
                sage: c.f(2,power=2)
                (Lambda[0] + Lambda[1] - 2*Lambda[2],)
            """
        def s(self, i):
            """
            Compute the reflection of ``self`` along the `i`-string.

            This method is more efficient than the generic implementation since
            it uses powers of `e` and `f` in the Littelmann model directly.

            EXAMPLES::

                sage: C = crystals.LSPaths(['A',2],[1,1])
                sage: c = C.module_generators[0]
                sage: c.s(1)
                (-Lambda[1] + 2*Lambda[2],)
                sage: c.s(2)
                (2*Lambda[1] - Lambda[2],)

                sage: C = crystals.LSPaths(['A',2,1],[-1,0,1])
                sage: c = C.module_generators[0]; c
                (-Lambda[0] + Lambda[2],)
                sage: c.s(2)
                (Lambda[1] - Lambda[2],)
                sage: c.s(1)
                (-Lambda[0] + Lambda[2],)
                sage: c.f(2).s(1)
                (Lambda[0] - Lambda[1],)
            """
        def weight(self):
            """
            Return the weight of ``self``.

            EXAMPLES::

                sage: B = crystals.LSPaths(['A',1,1],[1,0])
                sage: b = B.highest_weight_vector()
                sage: b.f(0).weight()
                -Lambda[0] + 2*Lambda[1] - delta
            """

class CrystalOfProjectedLevelZeroLSPaths(CrystalOfLSPaths):
    """
    Crystal of projected level zero LS paths.

    INPUT:

    - ``weight`` -- a dominant weight of the weight space of an affine
      Kac-Moody root system

    When ``weight`` is just a single fundamental weight `\\Lambda_r`, this
    crystal is isomorphic to a Kirillov-Reshetikhin (KR) crystal, see also
    :meth:`sage.combinat.crystals.kirillov_reshetikhin.KirillovReshetikhinFromLSPaths`.
    For general weights, it is isomorphic to a tensor product of
    single-column KR crystals.

    EXAMPLES::

        sage: R = RootSystem(['C',3,1])
        sage: La = R.weight_space().basis()
        sage: LS = crystals.ProjectedLevelZeroLSPaths(La[1]+La[3])
        sage: LS.cardinality()
        84
        sage: GLS = LS.digraph()

        sage: K1 = crystals.KirillovReshetikhin(['C',3,1],1,1)
        sage: K3 = crystals.KirillovReshetikhin(['C',3,1],3,1)
        sage: T = crystals.TensorProduct(K3,K1)
        sage: T.cardinality()
        84
        sage: GT = T.digraph() # long time
        sage: GLS.is_isomorphic(GT, edge_labels = True) # long time
        True

    TESTS::

        sage: ct = CartanType(['A',4,2]).dual()
        sage: P = RootSystem(ct).weight_space()
        sage: La = P.fundamental_weights()
        sage: C = crystals.ProjectedLevelZeroLSPaths(La[1])
        sage: sorted(C, key=str)
        [(-Lambda[0] + Lambda[1],),
         (-Lambda[1] + 2*Lambda[2],),
         (1/2*Lambda[1] - Lambda[2], -1/2*Lambda[1] + Lambda[2]),
         (Lambda[0] - Lambda[1],),
         (Lambda[1] - 2*Lambda[2],)]
    """
    @staticmethod
    def __classcall_private__(cls, weight):
        """
        Classcall to mend the input.

        Internally, the
        :class:`~sage.combinat.crystals.littelmann_path.CrystalOfProjectedLevelZeroLSPaths`
        uses a level zero weight, which is passed on to
        :class:`~sage.combinat.crystals.littelmann_path.CrystalOfLSPaths`.
        ``weight`` is first coerced to a level zero weight.

        TESTS::

            sage: R = RootSystem(['C',3,1])
            sage: La = R.weight_space().basis()
            sage: C = crystals.ProjectedLevelZeroLSPaths(La[1] + La[2])
            sage: C2 = crystals.ProjectedLevelZeroLSPaths(La[1] + La[2])
            sage: C is C2
            True

            sage: R = RootSystem(['C',3,1])
            sage: La = R.weight_space(extended = True).basis()
            sage: crystals.ProjectedLevelZeroLSPaths(La[1] + La[2])
            Traceback (most recent call last):
            ...
            ValueError: the weight should be in the non-extended weight lattice
        """
    @cached_method
    def maximal_vector(self):
        """
        Return the maximal vector of ``self``.

        EXAMPLES::

            sage: R = RootSystem(['A',2,1])
            sage: La = R.weight_space().basis()
            sage: LS = crystals.ProjectedLevelZeroLSPaths(2*La[1]+La[2])
            sage: LS.maximal_vector()
            (-3*Lambda[0] + 2*Lambda[1] + Lambda[2],)
        """
    @cached_method
    def classically_highest_weight_vectors(self):
        """
        Return the classically highest weight vectors of ``self``.

        EXAMPLES::

            sage: R = RootSystem(['A',2,1])
            sage: La = R.weight_space().basis()
            sage: LS = crystals.ProjectedLevelZeroLSPaths(2*La[1])
            sage: LS.classically_highest_weight_vectors()
            ((-2*Lambda[0] + 2*Lambda[1],),
             (-Lambda[0] + Lambda[1], -Lambda[1] + Lambda[2]))
        """
    def one_dimensional_configuration_sum(self, q=None, group_components: bool = True):
        """
        Compute the one-dimensional configuration sum.

        INPUT:

        - ``q`` -- (default: ``None``) a variable or ``None``; if ``None``,
          a variable ``q`` is set in the code
        - ``group_components`` -- boolean (default: ``True``); if ``True``,
          then the terms are grouped by classical component

        The one-dimensional configuration sum is the sum of the weights
        of all elements in the crystal weighted by the energy function.
        For untwisted types it uses the parabolic quantum Bruhat graph,
        see [LNSSS2013]_. In the dual-of-untwisted case, the parabolic
        quantum Bruhat graph is defined by exchanging the roles of roots
        and coroots (which is still conjectural at this point).

        EXAMPLES::

            sage: R = RootSystem(['A',2,1])
            sage: La = R.weight_space().basis()
            sage: LS = crystals.ProjectedLevelZeroLSPaths(2*La[1])
            sage: LS.one_dimensional_configuration_sum() # long time
            B[-2*Lambda[1] + 2*Lambda[2]] + (q+1)*B[-Lambda[1]]
             + (q+1)*B[Lambda[1] - Lambda[2]] + B[2*Lambda[1]]
             + B[-2*Lambda[2]] + (q+1)*B[Lambda[2]]
            sage: R.<t> = ZZ[]
            sage: LS.one_dimensional_configuration_sum(t, False) # long time
            B[-2*Lambda[1] + 2*Lambda[2]] + (t+1)*B[-Lambda[1]]
             + (t+1)*B[Lambda[1] - Lambda[2]] + B[2*Lambda[1]]
             + B[-2*Lambda[2]] + (t+1)*B[Lambda[2]]

        TESTS::

            sage: R = RootSystem(['B',3,1])
            sage: La = R.weight_space().basis()
            sage: LS = crystals.ProjectedLevelZeroLSPaths(La[1]+La[2])
            sage: LS.one_dimensional_configuration_sum() == LS.one_dimensional_configuration_sum(group_components=False) # long time
            True
            sage: K1 = crystals.KirillovReshetikhin(['B',3,1],1,1)
            sage: K2 = crystals.KirillovReshetikhin(['B',3,1],2,1)
            sage: T = crystals.TensorProduct(K2,K1)
            sage: T.one_dimensional_configuration_sum() == LS.one_dimensional_configuration_sum() # long time
            True

            sage: R = RootSystem(['D',4,2])
            sage: La = R.weight_space().basis()
            sage: LS = crystals.ProjectedLevelZeroLSPaths(La[1]+La[2])
            sage: K1 = crystals.KirillovReshetikhin(['D',4,2],1,1)
            sage: K2 = crystals.KirillovReshetikhin(['D',4,2],2,1)
            sage: T = crystals.TensorProduct(K2,K1)
            sage: T.one_dimensional_configuration_sum() == LS.one_dimensional_configuration_sum() # long time
            True

            sage: R = RootSystem(['A',5,2])
            sage: La = R.weight_space().basis()
            sage: LS = crystals.ProjectedLevelZeroLSPaths(3*La[1])
            sage: K1 = crystals.KirillovReshetikhin(['A',5,2],1,1)
            sage: T = crystals.TensorProduct(K1,K1,K1)
            sage: T.one_dimensional_configuration_sum() == LS.one_dimensional_configuration_sum() # long time
            True
        """
    def is_perfect(self, level: int = 1):
        """
        Check whether the crystal ``self`` is perfect (of level ``level``).

        INPUT:

        - ``level`` -- (default: 1) positive integer

        A crystal `\\mathcal{B}` is perfect of level `\\ell` if:

        #. `\\mathcal{B}` is isomorphic to the crystal graph of a
           finite-dimensional `U_q^{'}(\\mathfrak{g})`-module.
        #. `\\mathcal{B}\\otimes \\mathcal{B}` is connected.
        #. There exists a `\\lambda\\in X`, such that
           `\\mathrm{wt}(\\mathcal{B}) \\subset \\lambda + \\sum_{i\\in I} \\ZZ_{\\le 0} \\alpha_i`
           and there is a unique element in
           `\\mathcal{B}` of classical weight `\\lambda`.
        #. For all `b \\in \\mathcal{B}`,
           `\\mathrm{level}(\\varepsilon (b)) \\geq \\ell`.
        #. For all `\\Lambda` dominant weights of level `\\ell`, there exist
           unique elements `b_{\\Lambda}, b^{\\Lambda} \\in \\mathcal{B}`, such
           that `\\varepsilon (b_{\\Lambda}) = \\Lambda = \\varphi(b^{\\Lambda})`.

        Points (1)-(3) are known to hold. This method checks points (4) and (5).

        EXAMPLES::

            sage: C = CartanType(['C',2,1])
            sage: R = RootSystem(C)
            sage: La = R.weight_space().basis()
            sage: LS = crystals.ProjectedLevelZeroLSPaths(La[1])
            sage: LS.is_perfect()
            False
            sage: LS = crystals.ProjectedLevelZeroLSPaths(La[2])
            sage: LS.is_perfect()
            True

            sage: C = CartanType(['E',6,1])
            sage: R = RootSystem(C)
            sage: La = R.weight_space().basis()
            sage: LS = crystals.ProjectedLevelZeroLSPaths(La[1])
            sage: LS.is_perfect()
            True
            sage: LS.is_perfect(2)
            False

            sage: C = CartanType(['D',4,1])
            sage: R = RootSystem(C)
            sage: La = R.weight_space().basis()
            sage: all(crystals.ProjectedLevelZeroLSPaths(La[i]).is_perfect() for i in [1,2,3,4])
            True

            sage: C = CartanType(['A',6,2])
            sage: R = RootSystem(C)
            sage: La = R.weight_space().basis()
            sage: LS = crystals.ProjectedLevelZeroLSPaths(La[1]+La[2])
            sage: LS.is_perfect()
            True
            sage: LS.is_perfect(2)
            False
        """
    class Element(CrystalOfLSPaths.Element):
        """
        Element of a crystal of projected level zero LS paths.
        """
        @cached_in_parent_method
        def scalar_factors(self):
            """
            Return the scalar factors for ``self``.

            Each LS path (or ``self``) can be written as a piecewise linear map

            .. MATH::

                \\pi(t) = \\sum_{u'=1}^{u-1} (\\sigma_{u'} - \\sigma_{u'-1}) \\nu_{u'}
                + (t-\\sigma_{u-1}) \\nu_{u}

            for `0 < \\sigma_1 < \\sigma_2 < \\cdots < \\sigma_s=1` and
            `\\sigma_{u-1} \\le t \\le \\sigma_{u}` and `1 \\le u \\le s`.
            This method returns the tuple of `(\\sigma_1,\\ldots,\\sigma_s)`.

            EXAMPLES::

                sage: R = RootSystem(['C',3,1])
                sage: La = R.weight_space().basis()
                sage: LS = crystals.ProjectedLevelZeroLSPaths(La[1]+La[3])
                sage: b = LS.module_generators[0]
                sage: b.scalar_factors()
                [1]
                sage: c = b.f(1).f(3).f(2)
                sage: c.scalar_factors()
                [1/3, 1]
            """
        @cached_in_parent_method
        def weyl_group_representation(self):
            """
            Transform the weights in the LS path ``self`` to elements
            in the Weyl group.

            Each LS path can be written as the piecewise linear map:

            .. MATH::

                \\pi(t) = \\sum_{u'=1}^{u-1} (\\sigma_{u'} - \\sigma_{u'-1}) \\nu_{u'}
                + (t-\\sigma_{u-1}) \\nu_{u}

            for `0 < \\sigma_1 < \\sigma_2 < \\cdots < \\sigma_s = 1` and
            `\\sigma_{u-1} \\le t \\le \\sigma_{u}` and `1 \\le u \\le s`.
            Each weight `\\nu_u` is also associated to a Weyl group element.
            This method returns the list of Weyl group elements associated
            to the `\\nu_u` for `1\\le u\\le s`.

            EXAMPLES::

                sage: R = RootSystem(['C',3,1])
                sage: La = R.weight_space().basis()
                sage: LS = crystals.ProjectedLevelZeroLSPaths(La[1]+La[3])
                sage: b = LS.module_generators[0]
                sage: c = b.f(1).f(3).f(2)
                sage: c.weyl_group_representation()
                [s2*s1*s3, s1*s3]
            """
        @cached_in_parent_method
        def energy_function(self):
            '''
            Return the energy function of ``self``.

            The energy function `D(\\pi)` of the level zero LS path
            `\\pi \\in \\mathbb{B}_\\mathrm{cl}(\\lambda)` requires a series
            of definitions; for simplicity the root system is assumed to
            be untwisted affine.

            The LS path `\\pi` is a piecewise linear map from the unit
            interval `[0,1]` to the weight lattice. It is specified by
            "times" `0 = \\sigma_0 < \\sigma_1 < \\dotsm < \\sigma_s = 1` and
            "direction vectors" `x_u \\lambda` where `x_u \\in W / W_J` for
            `1 \\le u \\le s`, and `W_J` is the stabilizer of `\\lambda` in
            the finite Weyl group `W`. Precisely,

            .. MATH::

                \\pi(t) = \\sum_{u\'=1}^{u-1} (\\sigma_{u\'}-\\sigma_{u\'-1})
                x_{u\'} \\lambda + (t-\\sigma_{u-1}) x_{u} \\lambda

            for `1 \\le u \\le s` and `\\sigma_{u-1} \\le t \\le \\sigma_{u}`.

            For any `x,y \\in W / W_J`, let

            .. MATH::

                d: x = w_{0} \\stackrel{\\beta_{1}}{\\leftarrow}
                w_{1} \\stackrel{\\beta_{2}}{\\leftarrow} \\cdots
                \\stackrel{\\beta_{n}}{\\leftarrow} w_{n}=y

            be a shortest directed path in the parabolic quantum
            Bruhat graph. Define

            .. MATH::

                \\mathrm{wt}(d) := \\sum_{\\substack{1 \\le k \\le n
                \\\\ \\ell(w_{k-1}) < \\ell(w_k)}}
                \\beta_{k}^{\\vee}.

            It can be shown that `\\mathrm{wt}(d)` depends only on `x,y`;
            call its value `\\mathrm{wt}(x,y)`. The energy function `D(\\pi)`
            is defined by

            .. MATH::

                D(\\pi) = -\\sum_{u=1}^{s-1} (1-\\sigma_{u}) \\langle \\lambda,
                \\mathrm{wt}(x_u,x_{u+1}) \\rangle.

            For more information, see [LNSSS2013]_.

            .. NOTE::

                In the dual-of-untwisted case the parabolic quantum
                Bruhat graph that is used is obtained by exchanging the
                roles of roots and coroots. Moreover, in the computation
                of the pairing the short roots must be doubled (or tripled
                for type `G`). This factor is determined by the translation
                factor of the corresponding root. Type `BC` is viewed as
                untwisted type, whereas the dual of `BC` is viewed as twisted.
                Except for the untwisted cases, these formulas are
                currently still conjectural.

            EXAMPLES::

                sage: R = RootSystem([\'C\',3,1])
                sage: La = R.weight_space().basis()
                sage: LS = crystals.ProjectedLevelZeroLSPaths(La[1]+La[3])
                sage: b = LS.module_generators[0]
                sage: c = b.f(1).f(3).f(2)
                sage: c.energy_function()
                0
                sage: c=b.e(0)
                sage: c.energy_function()
                1

                sage: R = RootSystem([\'A\',2,1])
                sage: La = R.weight_space().basis()
                sage: LS = crystals.ProjectedLevelZeroLSPaths(2*La[1])
                sage: b = LS.module_generators[0]
                sage: c = b.e(0)
                sage: c.energy_function()
                1
                sage: for c in sorted(LS, key=str):
                ....:     print("{} {}".format(c,c.energy_function()))
                (-2*Lambda[0] + 2*Lambda[1],)                    0
                (-2*Lambda[1] + 2*Lambda[2],)                    0
                (-Lambda[0] + Lambda[1], -Lambda[1] + Lambda[2]) 1
                (-Lambda[0] + Lambda[1], Lambda[0] - Lambda[2])  1
                (-Lambda[1] + Lambda[2], -Lambda[0] + Lambda[1]) 0
                (-Lambda[1] + Lambda[2], Lambda[0] - Lambda[2])  1
                (2*Lambda[0] - 2*Lambda[2],)                     0
                (Lambda[0] - Lambda[2], -Lambda[0] + Lambda[1])  0
                (Lambda[0] - Lambda[2], -Lambda[1] + Lambda[2])  0

            The next test checks that the energy function is constant
            on classically connected components::

                sage: R = RootSystem([\'A\',2,1])
                sage: La = R.weight_space().basis()
                sage: LS = crystals.ProjectedLevelZeroLSPaths(2*La[1]+La[2])
                sage: G = LS.digraph(index_set=[1,2])
                sage: C = G.connected_components(sort=False)
                sage: [all(c[0].energy_function()==a.energy_function() for a in c) for c in C]
                [True, True, True, True]

                sage: R = RootSystem([\'D\',4,2])
                sage: La = R.weight_space().basis()
                sage: LS = crystals.ProjectedLevelZeroLSPaths(La[2])
                sage: J = R.cartan_type().classical().index_set()
                sage: hw = [x for x in LS if x.is_highest_weight(J)]
                sage: [(x.weight(), x.energy_function()) for x in hw]
                [(-2*Lambda[0] + Lambda[2], 0), (-2*Lambda[0] + Lambda[1], 1), (0, 2)]
                sage: G = LS.digraph(index_set=J)
                sage: C = G.connected_components(sort=False)
                sage: [all(c[0].energy_function()==a.energy_function() for a in c) for c in C]
                [True, True, True]

                sage: R = RootSystem(CartanType([\'G\',2,1]).dual())
                sage: La = R.weight_space().basis()
                sage: LS = crystals.ProjectedLevelZeroLSPaths(La[1]+La[2])
                sage: G = LS.digraph(index_set=[1,2])
                sage: C = G.connected_components(sort=False)
                sage: [all(c[0].energy_function()==a.energy_function() for a in c) for c in C] # long time
                [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]

                sage: ct = CartanType([\'BC\',2,2]).dual()
                sage: R = RootSystem(ct)
                sage: La = R.weight_space().basis()
                sage: LS = crystals.ProjectedLevelZeroLSPaths(2*La[1]+La[2])
                sage: G = LS.digraph(index_set=R.cartan_type().classical().index_set())
                sage: C = G.connected_components(sort=False)
                sage: [all(c[0].energy_function()==a.energy_function() for a in c) for c in C] # long time
                [True, True, True, True, True, True, True, True, True, True, True]

                sage: R = RootSystem([\'BC\',2,2])
                sage: La = R.weight_space().basis()
                sage: LS = crystals.ProjectedLevelZeroLSPaths(2*La[1]+La[2])
                sage: G = LS.digraph(index_set=R.cartan_type().classical().index_set())
                sage: C = G.connected_components(sort=False)
                sage: [all(c[0].energy_function()==a.energy_function() for a in c) for c in C] # long time
                [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
            '''

class InfinityCrystalOfLSPaths(UniqueRepresentation, Parent):
    """
    LS path model for `\\mathcal{B}(\\infty)`.

    Elements of `\\mathcal{B}(\\infty)` are equivalence classes of paths `[\\pi]`
    in `\\mathcal{B}(k\\rho)` for `k\\gg 0`, where `\\rho` is the Weyl vector.  A
    canonical representative for an element of `\\mathcal{B}(\\infty)` is chosen
    by taking `k` to be minimal such that the endpoint of `\\pi` is strictly
    dominant but its representative in `\\mathcal{B}((k-1)\\rho)` is on the wall
    of the dominant chamber.

    REFERENCES:

    - [LZ2011]_
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: B1 = crystals.infinity.LSPaths(['A',4])
            sage: B2 = crystals.infinity.LSPaths('A4')
            sage: B3 = crystals.infinity.LSPaths(CartanType(['A',4]))
            sage: B1 is B2 and B2 is B3
            True
        """
    module_generators: Incomplete
    def __init__(self, cartan_type) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.LSPaths(['D',4,3])
            sage: TestSuite(B).run(max_runs=500)
            sage: B = crystals.infinity.LSPaths(['B',3])
            sage: TestSuite(B).run() # long time
        """
    @cached_method
    def module_generator(self):
        """
        Return the module generator (or highest weight element) of ``self``.

        The module generator is the unique path
        `\\pi_\\infty\\colon t \\mapsto t\\rho`, for `t \\in [0,\\infty)`.

        EXAMPLES::

            sage: B = crystals.infinity.LSPaths(['A',6,2])
            sage: mg = B.module_generator(); mg
            (Lambda[0] + Lambda[1] + Lambda[2] + Lambda[3],)
            sage: mg.weight()
            0
        """
    def weight_lattice_realization(self):
        """
        Return the weight lattice realization of ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.LSPaths(['C',4])
            sage: B.weight_lattice_realization()
            Weight space over the Rational Field of the Root system of type ['C', 4]
        """
    class Element(CrystalOfLSPaths.Element):
        def e(self, i, power: int = 1, length_only: bool = False):
            """
            Return the `i`-th crystal raising operator on ``self``.

            INPUT:

            - ``i`` -- element of the index set
            - ``power`` -- (default: 1) positive integer; specifies the
              power of the lowering operator to be applied
            - ``length_only`` -- boolean (default: ``False``); if ``True``,
              then return the distance to the anti-dominant end of the
              `i`-string of ``self``

            EXAMPLES::

                sage: B = crystals.infinity.LSPaths(['B',3,1])
                sage: mg = B.module_generator()
                sage: mg.e(0)
                sage: mg.e(1)
                sage: mg.e(2)
                sage: x = mg.f_string([1,0,2,1,0,2,1,1,0])
                sage: all(x.f(i).e(i) == x for i in B.index_set())
                True
                sage: all(x.e(i).f(i) == x for i in B.index_set() if x.epsilon(i) > 0)
                True

            TESTS:

            Check that this works in affine types::

                sage: B = crystals.infinity.LSPaths(['A',3,1])
                sage: mg = B.highest_weight_vector()
                sage: x = mg.f_string([0,1,2,3])
                sage: x.e_string([3,2,1,0]) == mg
                True

            We check that :meth:`epsilon` works::

                sage: B = crystals.infinity.LSPaths(['D',4])
                sage: mg = B.highest_weight_vector()
                sage: x = mg.f_string([1,3,4,2,4,3,2,1,4])
                sage: [x.epsilon(i) for i in B.index_set()]
                [1, 1, 0, 1]

            Check that :issue:`21671` is fixed::

                sage: B = crystals.infinity.LSPaths(['G',2])
                sage: len(B.subcrystal(max_depth=7))
                116
            """
        def f(self, i, power: int = 1, length_only: bool = False):
            """
            Return the `i`-th crystal lowering operator on ``self``.

            INPUT:

            - ``i`` -- element of the index set
            - ``power`` -- (default: 1) positive integer; specifies the
              power of the lowering operator to be applied
            - ``length_only`` -- boolean (default: ``False``); if ``True``,
              then return the distance to the anti-dominant end of the
              `i`-string of ``self``

            EXAMPLES::

                sage: B = crystals.infinity.LSPaths(['D',3,2])
                sage: mg = B.highest_weight_vector()
                sage: mg.f(1)
                (3*Lambda[0] - Lambda[1] + 3*Lambda[2],
                 2*Lambda[0] + 2*Lambda[1] + 2*Lambda[2])
                sage: mg.f(2)
                (Lambda[0] + 2*Lambda[1] - Lambda[2],
                 2*Lambda[0] + 2*Lambda[1] + 2*Lambda[2])
                sage: mg.f(0)
                (-Lambda[0] + 2*Lambda[1] + Lambda[2] - delta,
                 2*Lambda[0] + 2*Lambda[1] + 2*Lambda[2])
            """
        @cached_method
        def weight(self):
            """
            Return the weight of ``self``.

            .. TODO::

                This is a generic algorithm. We should find a better
                description and implement it.

            EXAMPLES::

                sage: B = crystals.infinity.LSPaths(['E',6])
                sage: mg = B.highest_weight_vector()
                sage: f_seq = [1,4,2,6,4,2,3,1,5,5]
                sage: x = mg.f_string(f_seq)
                sage: x.weight()
                -3*Lambda[1] - 2*Lambda[2] + 2*Lambda[3] + Lambda[4] - Lambda[5]

                sage: al = B.cartan_type().root_system().weight_space().simple_roots()
                sage: x.weight() == -sum(al[i] for i in f_seq)
                True
            """
        def phi(self, i):
            """
            Return `\\varphi_i` of ``self``.

            Let `\\pi \\in \\mathcal{B}(\\infty)`. Define

            .. MATH::

                \\varphi_i(\\pi) := \\varepsilon_i(\\pi) + \\langle h_i,
                \\mathrm{wt}(\\pi) \\rangle,

            where `h_i` is the `i`-th simple coroot and `\\mathrm{wt}(\\pi)`
            is the :meth:`weight` of `\\pi`.

            INPUT:

            - ``i`` -- element of the index set

            EXAMPLES::

                sage: B = crystals.infinity.LSPaths(['D',4])
                sage: mg = B.highest_weight_vector()
                sage: x = mg.f_string([1,3,4,2,4,3,2,1,4])
                sage: [x.phi(i) for i in B.index_set()]
                [-1, 4, -2, -3]
            """

def positively_parallel_weights(v, w):
    """
    Check whether the vectors ``v`` and ``w`` are positive scalar
    multiples of each other.

    EXAMPLES::

        sage: from sage.combinat.crystals.littelmann_path import positively_parallel_weights
        sage: La = RootSystem(['A',5,2]).weight_space(extended=True).fundamental_weights()
        sage: rho = sum(La)
        sage: positively_parallel_weights(rho, 4*rho)
        True
        sage: positively_parallel_weights(4*rho, rho)
        True
        sage: positively_parallel_weights(rho, -rho)
        False
        sage: positively_parallel_weights(rho, La[1] + La[2])
        False
    """
