from _typeshed import Incomplete
from sage.categories.crystals import CrystalMorphism as CrystalMorphism
from sage.categories.homset import Hom as Hom
from sage.categories.loop_crystals import KirillovReshetikhinCrystals as KirillovReshetikhinCrystals
from sage.categories.map import Map as Map
from sage.combinat.combinat import CombinatorialObject as CombinatorialObject
from sage.combinat.crystals.affine import AffineCrystalFromClassical as AffineCrystalFromClassical, AffineCrystalFromClassicalAndPromotion as AffineCrystalFromClassicalAndPromotion, AffineCrystalFromClassicalAndPromotionElement as AffineCrystalFromClassicalAndPromotionElement, AffineCrystalFromClassicalElement as AffineCrystalFromClassicalElement
from sage.combinat.crystals.direct_sum import DirectSumOfCrystals as DirectSumOfCrystals
from sage.combinat.crystals.highest_weight_crystals import HighestWeightCrystal as HighestWeightCrystal
from sage.combinat.crystals.littelmann_path import CrystalOfProjectedLevelZeroLSPaths as CrystalOfProjectedLevelZeroLSPaths
from sage.combinat.crystals.tensor_product import CrystalOfTableaux as CrystalOfTableaux
from sage.combinat.integer_vector import IntegerVectors as IntegerVectors
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.root_system import RootSystem as RootSystem
from sage.combinat.tableau import Tableau as Tableau
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import is_even as is_even, is_odd as is_odd
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent import Parent as Parent

def KirillovReshetikhinCrystalFromLSPaths(cartan_type, r, s: int = 1):
    """
    Single column Kirillov-Reshetikhin crystals.

    This yields the single column Kirillov-Reshetikhin crystals
    from the projected level zero LS paths, see
    :class:`~sage.combinat.crystals.littelmann_path.CrystalOfLSPaths`.
    This works for all types (even exceptional types).
    The weight of the canonical element in this crystal is `\\Lambda_r`.
    For other implementation see
    :func:`~sage.combinat.crystals.kirillov_reshetikhin.KirillovReshetikhinCrystal`.

    EXAMPLES::

        sage: K = crystals.kirillov_reshetikhin.LSPaths(['A',2,1],2) # indirect doctest
        sage: KR = crystals.KirillovReshetikhin(['A',2,1],2,1)
        sage: G = K.digraph()
        sage: GR = KR.digraph()
        sage: G.is_isomorphic(GR, edge_labels = True)
        True

        sage: K = crystals.kirillov_reshetikhin.LSPaths(['C',3,1],2)
        sage: KR = crystals.KirillovReshetikhin(['C',3,1],2,1)
        sage: G = K.digraph()
        sage: GR = KR.digraph()
        sage: G.is_isomorphic(GR, edge_labels = True)
        True

        sage: K = crystals.kirillov_reshetikhin.LSPaths(['E',6,1],1)
        sage: KR = crystals.KirillovReshetikhin(['E',6,1],1,1)
        sage: G = K.digraph()
        sage: GR = KR.digraph()
        sage: G.is_isomorphic(GR, edge_labels = True)
        True
        sage: K.cardinality()
        27

        sage: K = crystals.kirillov_reshetikhin.LSPaths(['G',2,1],1)
        sage: K.cardinality()
        7

        sage: K = crystals.kirillov_reshetikhin.LSPaths(['B',3,1],2)
        sage: KR = crystals.KirillovReshetikhin(['B',3,1],2,1)
        sage: KR.cardinality()
        22
        sage: K.cardinality()
        22
        sage: G = K.digraph()
        sage: GR = KR.digraph()
        sage: G.is_isomorphic(GR, edge_labels = True)
        True

    TESTS::

        sage: K = crystals.kirillov_reshetikhin.LSPaths(['G',2,1],2)
        sage: K.cardinality()
        15

    For `s > 1` these crystals yield `s`-fold tensor products of
    Kirillov-Reshetikhin crystals::

        sage: K = crystals.kirillov_reshetikhin.LSPaths(['A',1,1],1,3)
        sage: B = crystals.KirillovReshetikhin(['A',1,1],1,1)
        sage: T = crystals.TensorProduct(B,B,B)
        sage: G = K.digraph()
        sage: GT = T.digraph()
        sage: G.is_isomorphic(GT, edge_labels = True)
        True

        sage: K = crystals.kirillov_reshetikhin.LSPaths(['B',2,1],1,2)
        sage: B = crystals.KirillovReshetikhin(['B',2,1],1,1)
        sage: T = crystals.TensorProduct(B,B)
        sage: G = K.digraph()
        sage: GT = T.digraph()
        sage: G.is_isomorphic(GT, edge_labels = True)
        True

        sage: K = crystals.kirillov_reshetikhin.LSPaths(['B',2,1],2,3)
        sage: B = crystals.KirillovReshetikhin(['B',2,1],2,1)
        sage: T = crystals.TensorProduct(B,B,B)
        sage: GT = T.digraph()
        sage: G = K.digraph()
        sage: G.is_isomorphic(GT, edge_labels = True)
        True
    """
def KirillovReshetikhinCrystal(cartan_type, r, s, model: str = 'KN'):
    """
    Return the Kirillov-Reshetikhin crystal `B^{r,s}` of the given type
    in the given model.

    For more information about general crystals see
    :mod:`sage.combinat.crystals.crystals`.

    There are a variety of models for Kirillov-Reshetikhin crystals. There is
    one using the classical crystal with :func:`Kashiwara-Nakashima tableaux
    <sage.combinat.crystals.kirillov_reshetikhin.KashiwaraNakashimaTableaux>`.
    There is one using :class:`rigged configurations <RiggedConfigurations>`.
    Another tableaux model comes from the bijection between rigged configurations
    and tensor products of tableaux called :class:`Kirillov-Reshetikhin tableaux
    <sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableaux>`
    Lastly there is a model of Kirillov-Reshetikhin crystals for `s = 1` from
    crystals of :func:`LS paths
    <sage.combinat.crystals.kirillov_reshetikhin.KirillovReshetikhinCrystalFromLSPaths>`.

    INPUT:

    - ``cartan_type`` -- an affine Cartan type

    - ``r`` -- a label of finite Dynkin diagram

    - ``s`` -- positive integer

    - ``model`` -- (default: ``'KN'``) can be one of the following:

      * ``'KN'`` or ``'KashiwaraNakashimaTableaux'`` -- use the
        Kashiwara-Nakashima tableaux model
      * ``'KR'`` or ``'KirillovReshetkihinTableaux'`` -- use the
        Kirillov-Reshetkihin tableaux model
      * ``'RC'`` or ``'RiggedConfiguration'`` -- use the rigged
        configuration model
      * ``'LSPaths'`` -- use the LS path model

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['A',3,1], 2, 1)
        sage: K.index_set()
        (0, 1, 2, 3)
        sage: K.list()
        [[[1], [2]], [[1], [3]], [[2], [3]], [[1], [4]], [[2], [4]], [[3], [4]]]
        sage: b=K(rows=[[1],[2]])
        sage: b.weight()
        -Lambda[0] + Lambda[2]

        sage: K = crystals.KirillovReshetikhin(['A',3,1], 2,2)
        sage: K.automorphism(K.module_generators[0])
        [[2, 2], [3, 3]]
        sage: K.module_generators[0].e(0)
        [[1, 2], [2, 4]]
        sage: K.module_generators[0].f(2)
        [[1, 1], [2, 3]]
        sage: K.module_generators[0].f(1)
        sage: K.module_generators[0].phi(0)
        0
        sage: K.module_generators[0].phi(1)
        0
        sage: K.module_generators[0].phi(2)
        2
        sage: K.module_generators[0].epsilon(0)
        2
        sage: K.module_generators[0].epsilon(1)
        0
        sage: K.module_generators[0].epsilon(2)
        0
        sage: b = K(rows=[[1,2],[2,3]])
        sage: b
        [[1, 2], [2, 3]]
        sage: b.f(2)
        [[1, 2], [3, 3]]

        sage: K = crystals.KirillovReshetikhin(['D',4,1], 2, 1)
        sage: K.cartan_type()
        ['D', 4, 1]
        sage: type(K.module_generators[0])
        <class 'sage.combinat.crystals.kirillov_reshetikhin.KR_type_vertical_with_category.element_class'>

    The following gives some tests with regards to Lemma 3.11 in [LOS2012]_.

    TESTS::

        sage: K = crystals.KirillovReshetikhin(['A',4,2],2,1)
        sage: Lambda = K.weight_lattice_realization().fundamental_weights()
        sage: [b for b in K if b.Epsilon() == Lambda[0]]
        [[]]

        sage: K = crystals.KirillovReshetikhin(['D',4,2],1,2)
        sage: Lambda = K.weight_lattice_realization().fundamental_weights()
        sage: [b for b in K if b.Epsilon() == 2*Lambda[0]]
        [[]]
        sage: [b for b in K if b.Epsilon() == 2*Lambda[3]]
        [[[3, -3]]]
        sage: K = crystals.KirillovReshetikhin(['D',4,2],1,1)
        sage: [b for b in K if b.Epsilon() == Lambda[3]]
        [[[0]]]

        sage: K = crystals.KirillovReshetikhin(['B',3,1],2,1)
        sage: Lambda = K.weight_lattice_realization().fundamental_weights()
        sage: [b for b in K if b.Epsilon() == Lambda[0]]
        [[]]
        sage: [b for b in K if b.Epsilon() == Lambda[1]]
        [[[2], [-2]]]
        sage: K = crystals.KirillovReshetikhin(['B',3,1],2,2)
        sage: [b for b in K if b.Epsilon() == 2*Lambda[0]]
        [[]]
        sage: [b for b in K if b.Epsilon() == 2*Lambda[1]]
        [[[1, 2], [-2, -1]]]
        sage: K = crystals.KirillovReshetikhin(['B',3,1],2,3)
        sage: [b for b in K if b.Epsilon() == 3*Lambda[1]] # long time
        [[[1, 2, 2], [-2, -2, -1]]]

        sage: K = crystals.KirillovReshetikhin(['D',4,1],2,2)
        sage: Lambda = K.weight_lattice_realization().fundamental_weights()
        sage: [b for b in K if b.Epsilon() == 2*Lambda[0]] # long time
        [[]]
        sage: [b for b in K if b.Epsilon() == 2*Lambda[4]] # long time
        [[[3, -4], [4, -3]]]

        sage: K = crystals.KirillovReshetikhin(['B',3,1],3,1)
        sage: Lambda = K.weight_lattice_realization().fundamental_weights()
        sage: [b for b in K if b.Epsilon() == Lambda[0]]
        [[+++, []]]
        sage: [b for b in K if b.Epsilon() == Lambda[1]]
        [[-++, []]]
        sage: K = crystals.KirillovReshetikhin(['B',3,1],3,3)
        sage: [b for b in K if b.Epsilon() == 2*Lambda[0]] # long time
        [[+++, [[1]]]]
        sage: [b for b in K if b.Epsilon() == 2*Lambda[1]] # long time
        [[-++, [[-1]]]]

        sage: K = crystals.KirillovReshetikhin(['B',4,1],4,1)
        sage: Lambda = K.weight_lattice_realization().fundamental_weights()
        sage: [b for b in K if b.Epsilon() == Lambda[0]]
        [[++++, []]]
        sage: [b for b in K if b.Epsilon() == Lambda[1]]
        [[-+++, []]]

        sage: K = crystals.KirillovReshetikhin(['C',3,1],1,1)
        sage: Lambda = K.weight_lattice_realization().fundamental_weights()
        sage: [b for b in K if b.Epsilon() == Lambda[0]]
        [[[1]]]
        sage: [b for b in K if b.Epsilon() == Lambda[3]]
        [[[-3]]]
        sage: K = crystals.KirillovReshetikhin(['C',3,1],1,3)
        sage: [b for b in K if b.Epsilon() == 2*Lambda[3]] # long time
        [[[3, -3, -3]]]
        sage: [b for b in K if b.Epsilon() == 2*Lambda[0]] # long time
        [[[1]]]

    We check the various models agree::

        sage: KN = crystals.KirillovReshetikhin(['D',4,1], 2, 1)
        sage: KR = crystals.KirillovReshetikhin(['D',4,1], 2, 1, model='KR')
        sage: RC = crystals.KirillovReshetikhin(['D',4,1], 2, 1, model='RC')
        sage: LS = crystals.KirillovReshetikhin(['D',4,1], 2, 1, model='LSPaths')
        sage: G = KN.digraph()
        sage: G.is_isomorphic(KR.digraph(), edge_labels=True)
        True
        sage: G.is_isomorphic(RC.digraph(), edge_labels=True)
        True
        sage: G.is_isomorphic(LS.digraph(), edge_labels=True)
        True

        sage: KN = crystals.KirillovReshetikhin(['D',4,1], 2, 1)
        sage: KN2 = crystals.KirillovReshetikhin(['D',4,1], 2, 1, model='KN')
        sage: KN3 = crystals.KirillovReshetikhin(['D',4,1], 2, 1, model='KashiwaraNakashimaTableaux')
        sage: KN is KN2 and KN is KN3
        True

    REFERENCES:

    - [Shi2002]_

    - [Sch2008]_

    - [JS2010]_

    - [FOS2009]_

    - [LOS2012]_
    """
def KashiwaraNakashimaTableaux(cartan_type, r, s):
    """
    Return the Kashiwara-Nakashima model for the Kirillov-Reshetikhin crystal
    `B^{r,s}` in the given type.

    The Kashiwara-Nakashima (KN) model constructs the KR crystal from the
    KN tableaux model for the corresponding classical crystals. This model
    is named for the underlying KN tableaux.

    Many Kirillov-Reshetikhin crystals are constructed from a
    classical crystal together with an automorphism `p` on the level of
    crystals which corresponds to a Dynkin diagram automorphism mapping
    node 0 to some other node `i`. The action of `f_0` and `e_0` is then
    constructed using `f_0 = p^{-1} \\circ f_i \\circ p`.

    For example, for type `A_n^{(1)}` the Kirillov-Reshetikhin crystal `B^{r,s}`
    is obtained from the classical crystal `B(s \\omega_r)` using the
    promotion operator. For other types, see [Shi2002]_, [Sch2008]_,
    and [JS2010]_.

    Other Kirillov-Reshetikhin crystals are constructed using similarity methods.
    See Section 4 of [FOS2009]_.

    For more information on Kirillov-Reshetikhin crystals, see
    :func:`~sage.combinat.crystals.kirillov_reshetikhin.KirillovReshetikhinCrystal`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['A',3,1], 2, 1)
        sage: K2 = crystals.kirillov_reshetikhin.KashiwaraNakashimaTableaux(['A',3,1], 2, 1)
        sage: K is K2
        True
    """

class KirillovReshetikhinGenericCrystal(AffineCrystalFromClassical):
    """
    Generic class for Kirillov-Reshetikhin crystal `B^{r,s}` of the given type.

    Input is a Dynkin node ``r``, a positive integer ``s``, and a Cartan type
    ``cartan_type``.
    """
    def __init__(self, cartan_type, r, s, dual=None) -> None:
        """
        Initialize a generic Kirillov-Reshetikhin crystal.

        TESTS::

            sage: K = crystals.KirillovReshetikhin(CartanType(['A',2,1]), 1, 1)
            sage: K
            Kirillov-Reshetikhin crystal of type ['A', 2, 1] with (r,s)=(1,1)
            sage: K.r()
            1
            sage: K.s()
            1
        """
    def module_generator(self):
        """
        Return the unique module generator of classical weight
        `s \\Lambda_r` of a Kirillov-Reshetikhin crystal `B^{r,s}`

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',2,1],1,2)
            sage: K.module_generator()
            [[1, 1]]
            sage: K = crystals.KirillovReshetikhin(['E',6,1],1,1)
            sage: K.module_generator()
            [(1,)]

            sage: K = crystals.KirillovReshetikhin(['D',4,1],2,1)
            sage: K.module_generator()
            [[1], [2]]
        """
    def r(self):
        """
        Return `r` of the underlying Kirillov-Reshetikhin crystal `B^{r,s}`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1], 2, 1)
            sage: K.r()
            2
        """
    def s(self):
        """
        Return `s` of the underlying Kirillov-Reshetikhin crystal `B^{r,s}`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1], 2, 1)
            sage: K.s()
            1
        """
    @cached_method
    def classically_highest_weight_vectors(self):
        """
        Return the classically highest weight vectors of ``self``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D', 4, 1], 2, 2)
            sage: K.classically_highest_weight_vectors()
            ([], [[1], [2]], [[1, 1], [2, 2]])
        """
    def kirillov_reshetikhin_tableaux(self):
        """
        Return the corresponding set of
        :class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableaux`.

        EXAMPLES::

            sage: KRC = crystals.KirillovReshetikhin(['D', 4, 1], 2, 2)
            sage: KRC.kirillov_reshetikhin_tableaux()
            Kirillov-Reshetikhin tableaux of type ['D', 4, 1] and shape (2, 2)
        """

class KirillovReshetikhinGenericCrystalElement(AffineCrystalFromClassicalElement):
    """
    Abstract class for all Kirillov-Reshetikhin crystal elements.
    """
    def pp(self) -> None:
        """
        Pretty print ``self``.

        EXAMPLES::

            sage: C = crystals.KirillovReshetikhin(['D',4,1], 2,1)
            sage: C(2,1).pp()
              1
              2
            sage: C = crystals.KirillovReshetikhin(['B',3,1], 3,3)
            sage: C.module_generators[0].pp()
            + (X)   1
            +
            +
        """
    @cached_method
    def to_kirillov_reshetikhin_tableau(self):
        """
        Construct the corresponding
        :class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableauxElement`
        from ``self``.

        We construct the Kirillov-Reshetikhin tableau element as follows:

        1. Let `\\lambda` be the shape of ``self``.
        2. Determine a path `e_{i_1} e_{i_2} \\cdots e_{i_k}` to the highest
           weight.
        3. Apply `f_{i_k} \\cdots f_{i_2} f_{i_1}` to a highest weight KR
           tableau from filling the shape `\\lambda`.

        EXAMPLES::

            sage: KRC = crystals.KirillovReshetikhin(['A', 4, 1], 2, 1)
            sage: KRC(columns=[[2,1]]).to_kirillov_reshetikhin_tableau()
            [[1], [2]]
            sage: KRC = crystals.KirillovReshetikhin(['D', 4, 1], 2, 1)
            sage: KRC(rows=[]).to_kirillov_reshetikhin_tableau()
            [[1], [-1]]
        """
    @cached_method
    def to_tableau(self):
        """
        Return the :class:`Tableau` corresponding to ``self``.

        EXAMPLES::

            sage: C = crystals.KirillovReshetikhin(['D',4,1], 2,1)
            sage: t = C(2,1).to_tableau(); t
            [[1], [2]]
            sage: type(t)
            <class 'sage.combinat.tableau.Tableaux_all_with_category.element_class'>
        """
    def lusztig_involution(self):
        """
        Return the classical Lusztig involution on ``self``.

        EXAMPLES::

            sage: KRC = crystals.KirillovReshetikhin(['D',4,1], 2,2)
            sage: elt = KRC(-1,2); elt
            [[2], [-1]]
            sage: elt.lusztig_involution()
            [[1], [-2]]
        """

class KirillovReshetikhinCrystalFromPromotion(KirillovReshetikhinGenericCrystal, AffineCrystalFromClassicalAndPromotion):
    """
    This generic class assumes that the Kirillov-Reshetikhin crystal is
    constructed from a classical crystal using the
    ``classical_decomposition`` and an automorphism ``promotion``
    and its inverse, which corresponds to a Dynkin diagram automorphism
    ``dynkin_diagram_automorphism``.

    Each instance using this class needs to implement the methods:

    - ``classical_decomposition``
    - ``promotion``
    - ``promotion_inverse``
    - ``dynkin_diagram_automorphism``
    """
    def __init__(self, cartan_type, r, s) -> None:
        """
        TESTS::

            sage: K = crystals.KirillovReshetikhin(['B',2,1], 1, 1)
            sage: K
            Kirillov-Reshetikhin crystal of type ['B', 2, 1] with (r,s)=(1,1)
            sage: TestSuite(K).run()
        """

class KirillovReshetikhinCrystalFromPromotionElement(AffineCrystalFromClassicalAndPromotionElement, KirillovReshetikhinGenericCrystalElement):
    """
    Element for a Kirillov-Reshetikhin crystal from promotion.
    """

class KR_type_A(KirillovReshetikhinCrystalFromPromotion):
    """
    Class of Kirillov-Reshetikhin crystals of type `A_n^{(1)}`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['A',3,1], 2,2)
        sage: b = K(rows=[[1,2],[2,4]])
        sage: b.f(0)
        [[1, 1], [2, 2]]
    """
    def classical_decomposition(self):
        """
        Specifies the classical crystal underlying the KR crystal of type A.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',3,1], 2,2)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['A', 3] and shape(s) [[2, 2]]
        """
    @cached_method
    def promotion(self):
        """
        Specifies the promotion operator used to construct the affine
        type `A` crystal.

        For type `A` this corresponds to the Dynkin diagram automorphism
        which `i \\mapsto i+1 \\mod n+1`, where `n` is the rank.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',3,1], 2,2)
            sage: b = K.classical_decomposition()(rows=[[1,2],[3,4]])
            sage: K.promotion()(b)
            [[1, 3], [2, 4]]
        """
    @cached_method
    def promotion_inverse(self):
        """
        Specifies the inverse promotion operator used to construct the
        affine type `A` crystal.

        For type `A` this corresponds to the Dynkin diagram automorphism
        which `i \\mapsto i-1 \\mod n+1`, where `n` is the rank.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',3,1], 2,2)
            sage: b = K.classical_decomposition()(rows=[[1,3],[2,4]])
            sage: K.promotion_inverse()(b)
            [[1, 2], [3, 4]]
            sage: b = K.classical_decomposition()(rows=[[1,2],[3,3]])
            sage: K.promotion_inverse()(K.promotion()(b))
            [[1, 2], [3, 3]]
        """
    def dynkin_diagram_automorphism(self, i):
        """
        Specifies the Dynkin diagram automorphism underlying the promotion
        action on the crystal elements. The automorphism needs to map node
        0 to some other Dynkin node.

        For type `A` we use the Dynkin diagram automorphism which
        `i \\mapsto i+1 \\mod n+1`, where `n` is the rank.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',3,1], 2,2)
            sage: K.dynkin_diagram_automorphism(0)
            1
            sage: K.dynkin_diagram_automorphism(3)
            0
        """

class KR_type_vertical(KirillovReshetikhinCrystalFromPromotion):
    """
    Class of Kirillov-Reshetikhin crystals `B^{r,s}` of type
    `D_n^{(1)}` for `r \\le n-2`, `B_n^{(1)}` for `r < n`, and
    `A_{2n-1}^{(2)}` for `r \\le n`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['D',4,1], 2,2)
        sage: b = K(rows=[])
        sage: b.f(0)
        [[1], [2]]
        sage: b.f(0).f(0)
        [[1, 1], [2, 2]]
        sage: b.e(0)
        [[-2], [-1]]
        sage: b.e(0).e(0)
        [[-2, -2], [-1, -1]]

        sage: K = crystals.KirillovReshetikhin(['D',5,1], 3,1)
        sage: b = K(rows=[[1]])
        sage: b.e(0)
        [[3], [-3], [-2]]

        sage: K = crystals.KirillovReshetikhin(['B',3,1], 1,1)
        sage: [[b,b.f(0)] for b in K]
        [[[[1]], None], [[[2]], None], [[[3]], None], [[[0]], None],
         [[[-3]], None], [[[-2]], [[1]]], [[[-1]], [[2]]]]

        sage: K = crystals.KirillovReshetikhin(['A',5,2], 1,1)
        sage: [[b,b.f(0)] for b in K]
        [[[[1]], None], [[[2]], None], [[[3]], None], [[[-3]], None],
         [[[-2]], [[1]]], [[[-1]], [[2]]]]
    """
    def classical_decomposition(self):
        """
        Specifies the classical crystal underlying the Kirillov-Reshetikhin
        crystal of type `D_n^{(1)}`, `B_n^{(1)}`, and `A_{2n-1}^{(2)}`.

        It is given by `B^{r,s} \\cong \\bigoplus_\\Lambda B(\\Lambda)`,
        where `\\Lambda` are weights obtained from a rectangle of width `s`
        and height `r` by removing vertical dominoes. Here we identify
        the fundamental weight `\\Lambda_i` with a column of height `i`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1], 2,2)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['D', 4] and shape(s) [[], [1, 1], [2, 2]]
        """
    @cached_method
    def promotion(self):
        """
        Specifies the promotion operator used to construct the affine
        type `D_n^{(1)}` etc. crystal.

        This corresponds to the Dynkin diagram automorphism which
        interchanges nodes 0 and 1, and leaves all other nodes unchanged.
        On the level of crystals it is constructed using `\\pm` diagrams.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1], 2,2)
            sage: promotion = K.promotion()
            sage: b = K.classical_decomposition()(rows=[])
            sage: promotion(b)
            [[1, 2], [-2, -1]]
            sage: b = K.classical_decomposition()(rows=[[1,3],[2,-1]])
            sage: promotion(b)
            [[1, 3], [2, -1]]
            sage: b = K.classical_decomposition()(rows=[[1],[-3]])
            sage: promotion(b)
            [[2, -3], [-2, -1]]
        """
    def promotion_inverse(self):
        """
        Return inverse of promotion.

        In this case promotion is an involution, so promotion
        inverse equals promotion.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1], 2,2)
            sage: promotion = K.promotion()
            sage: promotion_inverse = K.promotion_inverse()
            sage: all( promotion_inverse(promotion(b.lift())) == b.lift() for b in K )
            True
        """
    def dynkin_diagram_automorphism(self, i):
        """
        Specifies the Dynkin diagram automorphism underlying the promotion
        action on the crystal elements. The automorphism needs to map
        node 0 to some other Dynkin node.

        Here we use the Dynkin diagram automorphism which interchanges
        nodes 0 and 1 and leaves all other nodes unchanged.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1],1,1)
            sage: K.dynkin_diagram_automorphism(0)
            1
            sage: K.dynkin_diagram_automorphism(1)
            0
            sage: K.dynkin_diagram_automorphism(4)
            4
        """
    def promotion_on_highest_weight_vector(self, b):
        """
        Calculate promotion on a `{2, 3, \\ldots, n}` highest weight vector `b`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1], 2,2)
            sage: T = K.classical_decomposition()
            sage: hw = [ b for b in T if all(b.epsilon(i)==0 for i in [2,3,4]) ]
            sage: [K.promotion_on_highest_weight_vector(b) for b in hw]
            [[[1, 2], [-2, -1]], [[2, 2], [-2, -1]], [[1, 2], [3, -1]],
             [[2], [-2]], [[1, 2], [2, -2]], [[2, 2], [-1, -1]],
             [[2, 2], [3, -1]], [[2, 2], [3, 3]], [], [[1], [2]],
             [[1, 1], [2, 2]], [[2], [-1]], [[1, 2], [2, -1]],
             [[2], [3]], [[1, 2], [2, 3]]]
        """
    def from_highest_weight_vector_to_pm_diagram(self, b):
        """
        This gives the bijection between an element ``b`` in the classical
        decomposition of the KR crystal that is `{2, 3, \\ldots, n}`-highest
        weight and `\\pm` diagrams.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1], 2,2)
            sage: T = K.classical_decomposition()
            sage: b = T(rows=[[2],[-2]])
            sage: pm = K.from_highest_weight_vector_to_pm_diagram(b); pm
            [[1, 1], [0, 0], [0]]
            sage: pm.pp()
            +
            -
            sage: b = T(rows=[])
            sage: pm=K.from_highest_weight_vector_to_pm_diagram(b); pm
            [[0, 2], [0, 0], [0]]
            sage: pm.pp()

            sage: hw = [ b for b in T if all(b.epsilon(i)==0 for i in [2,3,4]) ]
            sage: all(K.from_pm_diagram_to_highest_weight_vector(K.from_highest_weight_vector_to_pm_diagram(b)) == b for b in hw)
            True
        """
    def from_pm_diagram_to_highest_weight_vector(self, pm):
        """
        This gives the bijection between a `\\pm` diagram and an element
        ``b`` in the classical decomposition of the KR crystal that
        is `{2, 3, \\ldots, n}`-highest weight.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1], 2,2)
            sage: pm = sage.combinat.crystals.kirillov_reshetikhin.PMDiagram([[1, 1], [0, 0], [0]])
            sage: K.from_pm_diagram_to_highest_weight_vector(pm)
            [[2], [-2]]
        """

class KR_type_E6(KirillovReshetikhinCrystalFromPromotion):
    """
    Class of Kirillov-Reshetikhin crystals of type `E_6^{(1)}` for `r=1,2,6`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['E',6,1],2,1)
        sage: K.module_generator().e(0)
        []
        sage: K.module_generator().e(0).f(0)
        [[(2, -1), (1,)]]
        sage: K = crystals.KirillovReshetikhin(['E',6,1], 1,1)
        sage: b = K.module_generator()
        sage: b
        [(1,)]
        sage: b.e(0)
        [(-2, 1)]
        sage: b = next(t for t in K if t.epsilon(1) == 1 and t.phi(3) == 1 and t.phi(2) == 0 and t.epsilon(2) == 0)
        sage: b
        [(-1, 3)]
        sage: b.e(0)
        [(-1, -2, 3)]

    The elements of the Kirillov-Reshetikhin crystals can be constructed from
    a classical crystal element using
    :meth:`~sage.combinat.crystals.affine.AffineCrystalFromClassical.retract()`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['E',6,1],2,1)
        sage: La = K.cartan_type().classical().root_system().weight_lattice().fundamental_weights()
        sage: H = crystals.HighestWeight(La[2])
        sage: t = H.module_generator()
        sage: t
        [[(2, -1), (1,)]]
        sage: type(K.retract(t))
        <class 'sage.combinat.crystals.kirillov_reshetikhin.KR_type_E6_with_category.element_class'>
        sage: K.retract(t).e(0)
        []

    TESTS::

        sage: K = crystals.KirillovReshetikhin(['E',6,1], 2,1)
        sage: La = K.weight_lattice_realization().fundamental_weights()
        sage: all(b.weight() == sum( (K.affine_weight(b.lift())[i] * La[i] for i in K.index_set()), 0*La[0]) for b in K)  # long time (26s on sage.math, 2011)
        True
    """
    def classical_decomposition(self):
        """
        Specifies the classical crystal underlying the KR crystal
        of type `E_6^{(1)}`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',6,1], 2,2)
            sage: K.classical_decomposition()
            Direct sum of the crystals Family
             (Finite dimensional highest weight crystal of type ['E', 6] and highest weight 0,
              Finite dimensional highest weight crystal of type ['E', 6] and highest weight Lambda[2],
              Finite dimensional highest weight crystal of type ['E', 6] and highest weight 2*Lambda[2])
            sage: K = crystals.KirillovReshetikhin(['E',6,1], 1,2)
            sage: K.classical_decomposition()
            Direct sum of the crystals Family
             (Finite dimensional highest weight crystal of type ['E', 6] and highest weight 2*Lambda[1],)
        """
    def dynkin_diagram_automorphism(self, i):
        """
        Specifies the Dynkin diagram automorphism underlying the promotion
        action on the crystal elements.

        Here we use the Dynkin diagram automorphism of order 3 which maps
        node 0 to node 1.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',6,1],2,1)
            sage: [K.dynkin_diagram_automorphism(i) for i in K.index_set()]
            [1, 6, 3, 5, 4, 2, 0]
        """
    def affine_weight(self, b):
        """
        Return the affine level zero weight corresponding to the element
        ``b`` of the classical crystal underlying ``self``.

        For the coefficients to calculate the level, see Table Aff 1
        in [Ka1990]_.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',6,1],2,1)
            sage: [K.affine_weight(x.lift()) for x in K
            ....:  if all(x.epsilon(i) == 0 for i in [2,3,4,5])]
            [(0, 0, 0, 0, 0, 0, 0),
             (-2, 0, 1, 0, 0, 0, 0),
             (-1, -1, 0, 0, 0, 1, 0),
             (0, 0, 0, 0, 0, 0, 0),
             (0, 0, 0, 0, 0, 1, -2),
             (0, -1, 1, 0, 0, 0, -1),
             (-1, 0, 0, 1, 0, 0, -1),
             (-1, -1, 0, 0, 1, 0, -1),
             (0, 0, 0, 0, 0, 0, 0),
             (0, -2, 0, 1, 0, 0, 0)]
        """
    @cached_method
    def hw_auxiliary(self):
        """
        Return the `{2,3,4,5}` highest weight elements of ``self``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',6,1],2,1)
            sage: K.hw_auxiliary()
            ([], [[(2, -1), (1,)]],
             [[(5, -3), (-1, 3)]],
             [[(6, -2), (-6, 2)]],
             [[(5, -2, -6), (-6, 2)]],
             [[(-1,), (-6, 2)]],
             [[(3, -1, -6), (1,)]],
             [[(4, -3, -6), (-1, 3)]],
             [[(1, -3), (-1, 3)]],
             [[(-1,), (-1, 3)]])
        """
    @cached_method
    def highest_weight_dict(self):
        """
        Return a dictionary between `\\{1,2,3,4,5\\}`-highest weight elements,
        and a tuple of affine weights and its classical component.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',6,1],2,1)
            sage: sorted(K.highest_weight_dict().items(), key=str)
            [([[(2, -1), (1,)]], ((-2, 0, 1, 0, 0, 0, 0), 1)),
             ([[(3, -1, -6), (1,)]], ((-1, 0, 0, 1, 0, 0, -1), 1)),
             ([[(5, -2, -6), (-6, 2)]], ((0, 0, 0, 0, 0, 1, -2), 1)),
             ([[(6, -2), (-6, 2)]], ((0, 0, 0, 0, 0, 0, 0), 1)),
             ([], ((0, 0, 0, 0, 0, 0, 0), 0))]
        """
    @cached_method
    def highest_weight_dict_inv(self):
        """
        Return a dictionary between a tuple of affine weights and a classical
        component, and `\\{2,3,4,5,6\\}`-highest weight elements.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',6,1],2,1)
            sage: K.highest_weight_dict_inv()
            {((-2, 0, 1, 0, 0, 0, 0), 1): [[(2, -1), (1,)]],
             ((-1, -1, 0, 0, 0, 1, 0), 1): [[(5, -3), (-1, 3)]],
             ((0, -2, 0, 1, 0, 0, 0), 1): [[(-1,), (-1, 3)]],
             ((0, 0, 0, 0, 0, 0, 0), 0): [],
             ((0, 0, 0, 0, 0, 0, 0), 1): [[(1, -3), (-1, 3)]]}
        """
    def automorphism_on_affine_weight(self, weight):
        """
        Act with the Dynkin diagram automorphism on affine weights
        as outputted by the ``affine_weight`` method.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',6,1],2,1)
            sage: sorted([x[0], K.automorphism_on_affine_weight(x[0])]
            ....:  for x in K.highest_weight_dict().values())
            [[(-2, 0, 1, 0, 0, 0, 0), (0, -2, 0, 1, 0, 0, 0)],
             [(-1, 0, 0, 1, 0, 0, -1), (-1, -1, 0, 0, 0, 1, 0)],
             [(0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0)],
             [(0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0)],
             [(0, 0, 0, 0, 0, 1, -2), (-2, 0, 1, 0, 0, 0, 0)]]
        """
    @cached_method
    def promotion_on_highest_weight_vectors(self):
        """
        Return a dictionary of the promotion map on `\\{1,2,3,4,5\\}`-highest
        weight elements to `\\{2,3,4,5,6\\}`-highest weight elements
        in ``self``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',6,1], 2, 1)
            sage: dic = K.promotion_on_highest_weight_vectors()
            sage: sorted(dic.items(), key=str)
            [([[(2, -1), (1,)]], [[(-1,), (-1, 3)]]),
             ([[(3, -1, -6), (1,)]], [[(5, -3), (-1, 3)]]),
             ([[(5, -2, -6), (-6, 2)]], [[(2, -1), (1,)]]),
             ([[(6, -2), (-6, 2)]], []),
             ([], [[(1, -3), (-1, 3)]])]
        """
    @cached_method
    def promotion_on_highest_weight_vectors_function(self):
        """
        Return a lambda function on ``x`` defined by
        ``self.promotion_on_highest_weight_vectors()[x]``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',6,1], 2, 1)
            sage: f = K.promotion_on_highest_weight_vectors_function()
            sage: f(K.module_generator().lift())
            [[(-1,), (-1, 3)]]
        """
    @cached_method
    def promotion(self):
        """
        Specifies the promotion operator used to construct the
        affine type `E_6^{(1)}` crystal.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',6,1], 2,1)
            sage: promotion = K.promotion()
            sage: all(promotion(promotion(promotion(b))) == b for b in K.classical_decomposition())
            True
            sage: K = crystals.KirillovReshetikhin(['E',6,1],1,1)
            sage: promotion = K.promotion()
            sage: all(promotion(promotion(promotion(b))) == b for b in K.classical_decomposition())
            True
        """
    @cached_method
    def promotion_inverse(self):
        """
        Return the inverse promotion. Since promotion is of order 3,
        the inverse promotion is the same as promotion applied twice.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',6,1], 2,1)
            sage: p = K.promotion()
            sage: p_inv = K.promotion_inverse()
            sage: all(p_inv(p(b)) == b for b in K.classical_decomposition())
            True
        """

class KR_type_C(KirillovReshetikhinGenericCrystal):
    """
    Class of Kirillov-Reshetikhin crystals `B^{r,s}` of type `C_n^{(1)}`
    for `r < n`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['C',2,1], 1,2)
        sage: K
        Kirillov-Reshetikhin crystal of type ['C', 2, 1] with (r,s)=(1,2)
        sage: b = K(rows=[])
        sage: b.f(0)
        [[1, 1]]
        sage: b.e(0)
        [[-1, -1]]
    """
    def classical_decomposition(self):
        """
        Return the classical crystal underlying the Kirillov-Reshetikhin
        crystal of type `C_n^{(1)}`.

        It is given by `B^{r,s} \\cong \\bigoplus_{\\Lambda} B(\\Lambda)`,
        where `\\Lambda` are weights obtained from a rectangle of width `s`
        and height `r` by removing horizontal dominoes. Here we identify
        the fundamental weight `\\Lambda_i` with a column of height `i`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',3,1], 2,2)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['C', 3] and shape(s) [[], [2], [2, 2]]
        """
    def ambient_crystal(self):
        """
        Return the ambient crystal `B^{r,s}` of type `A_{2n+1}^{(2)}`
        associated to the Kirillov-Reshetikhin crystal of type `C_n^{(1)}`.

        This ambient crystal is used to construct the zero arrows.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',3,1], 2,3)
            sage: K.ambient_crystal()
            Kirillov-Reshetikhin crystal of type ['B', 4, 1]^* with (r,s)=(2,3)
        """
    @cached_method
    def ambient_dict_pm_diagrams(self):
        """
        Return a dictionary of all self-dual `\\pm` diagrams for the
        ambient crystal whose keys are their inner shape.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',2,1], 1,2)
            sage: K.ambient_dict_pm_diagrams()
            {[]: [[1, 1], [0]], [2]: [[0, 0], [2]]}
            sage: K = crystals.KirillovReshetikhin(['C',3,1], 2,2)
            sage: K.ambient_dict_pm_diagrams()
            {[]: [[1, 1], [0, 0], [0]],
             [2]: [[0, 0], [1, 1], [0]],
             [2, 2]: [[0, 0], [0, 0], [2]]}
            sage: K = crystals.KirillovReshetikhin(['C',3,1], 2,3)
            sage: K.ambient_dict_pm_diagrams()
            {[1, 1]: [[1, 1], [0, 0], [1]],
             [3, 1]: [[0, 0], [1, 1], [1]],
             [3, 3]: [[0, 0], [0, 0], [3]]}
        """
    @cached_method
    def ambient_highest_weight_dict(self):
        """
        Return a dictionary of all `\\{2,\\ldots,n+1\\}`-highest weight vectors
        in the ambient crystal.

        The key is the inner shape of their corresponding `\\pm` diagram,
        or equivalently, their `\\{2,\\ldots,n+1\\}` weight.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',3,1], 2,2)
            sage: K.ambient_highest_weight_dict()
            {[]: [[2], [-2]], [2]: [[1, 2], [2, -1]], [2, 2]: [[2, 2], [3, 3]]}
        """
    @cached_method
    def highest_weight_dict(self):
        """
        Return a dictionary of the classical highest weight vectors of
        ``self`` whose keys are their shape.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',3,1], 2,2)
            sage: K.highest_weight_dict()
            {[]: [], [2]: [[1, 1]], [2, 2]: [[1, 1], [2, 2]]}
        """
    @cached_method
    def to_ambient_crystal(self):
        """
        Return a map from the Kirillov-Reshetikhin crystal of type
        `C_n^{(1)}` to the ambient crystal of type `A_{2n+1}^{(2)}`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',3,1], 2,2)
            sage: b=K(rows=[[1,1]])
            sage: K.to_ambient_crystal()(b)
            [[1, 2], [2, -1]]
            sage: b=K(rows=[])
            sage: K.to_ambient_crystal()(b)
            [[2], [-2]]
            sage: K.to_ambient_crystal()(b).parent()
            Kirillov-Reshetikhin crystal of type ['B', 4, 1]^* with (r,s)=(2,2)
        """
    @cached_method
    def from_ambient_crystal(self):
        """
        Return a map from the ambient crystal of type `A_{2n+1}^{(2)}` to
        the Kirillov-Reshetikhin crystal of type `C_n^{(1)}`.

        Note that this map is only well-defined on type `C_n^{(1)}` elements
        that are in the image under :meth:`to_ambient_crystal`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',3,1], 2,2)
            sage: b = K.ambient_crystal()(rows=[[2,2],[3,3]])
            sage: K.from_ambient_crystal()(b)
            [[1, 1], [2, 2]]
        """

class KR_type_CElement(KirillovReshetikhinGenericCrystalElement):
    """
    Class for the elements in the Kirillov-Reshetikhin crystals `B^{r,s}`
    of type `C_n^{(1)}` for `r<n`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['C', 3, 1], 1, 2)
        sage: type(K.module_generators[0])
        <class 'sage.combinat.crystals.kirillov_reshetikhin.KR_type_C_with_category.element_class'>
    """
    def e0(self):
        """
        Return `e_0` on ``self`` by mapping ``self`` to the ambient crystal,
        calculating `e_1 e_0` there and pulling the element back.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C', 3, 1], 1, 2)
            sage: b = K(rows=[])
            sage: b.e(0) # indirect doctest
            [[-1, -1]]
        """
    def f0(self):
        """
        Return `f_0` on ``self`` by mapping ``self`` to the ambient crystal,
        calculating `f_1 f_0` there and pulling the element back.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C', 3, 1], 1, 2)
            sage: b = K(rows=[])
            sage: b.f(0) # indirect doctest
            [[1, 1]]
        """
    def epsilon0(self):
        """
        Calculate `\\varepsilon_0` of ``self`` by mapping the element to
        the ambient crystal and calculating `\\varepsilon_1` there.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',2,1], 1,2)
            sage: b=K(rows=[[1,1]])
            sage: b.epsilon(0) # indirect doctest
            2
        """
    def phi0(self):
        """
        Calculate `\\varphi_0` of ``self`` by mapping the element to
        the ambient crystal and calculating `\\varphi_1` there.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',2,1], 1,2)
            sage: b=K(rows=[[-1,-1]])
            sage: b.phi(0) # indirect doctest
            2
        """

class KR_type_A2(KirillovReshetikhinGenericCrystal):
    """
    Class of Kirillov-Reshetikhin crystals `B^{r,s}` of type `A_{2n}^{(2)}`
    for `1 \\leq r \\leq n` in the realization with classical subalgebra `B_n`.
    The Cartan type in this case is inputted as the dual of `A_{2n}^{(2)}`.

    This is an alternative implementation to :class:`KR_type_box` that uses
    the classical decomposition into type `C_n` crystals.

    EXAMPLES::

        sage: C = CartanType(['A',4,2]).dual()
        sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 1)
        sage: K
        Kirillov-Reshetikhin crystal of type ['BC', 2, 2]^* with (r,s)=(1,1)
        sage: b = K(rows=[[-1]])
        sage: b.f(0)
        [[1]]
        sage: b.e(0)

    We can now check whether the two KR crystals of type `A_4^{(2)}`
    (namely the KR crystal and its dual construction) are isomorphic
    up to relabelling of the edges::

        sage: C = CartanType(['A',4,2])
        sage: K = crystals.KirillovReshetikhin(C,1,1)
        sage: Kdual = crystals.KirillovReshetikhin(C.dual(),1,1)
        sage: G = K.digraph()
        sage: Gdual = Kdual.digraph()
        sage: f = {0:2, 1:1, 2:0}
        sage: Gnew = DiGraph(); Gnew.add_vertices(Gdual.vertices(sort=True)); Gnew.add_edges([(u,v,f[i]) for u, v, i in Gdual.edges(sort=True)])
        sage: G.is_isomorphic(Gnew, edge_labels=True)
        True
    """
    def module_generator(self):
        """
        Return the unique module generator of classical weight
        `s \\Lambda_r` of a Kirillov-Reshetikhin crystal `B^{r,s}`.

        EXAMPLES::

            sage: ct = CartanType(['A',8,2]).dual()
            sage: K = crystals.KirillovReshetikhin(ct, 3, 5)
            sage: K.module_generator()
            [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]

        TESTS:

        Check that :issue:`23028` is fixed::

            sage: ct = CartanType(['A',8,2]).dual()
            sage: K = crystals.KirillovReshetikhin(ct, 4, 3)
            sage: K.module_generator()
            [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
            sage: K = crystals.KirillovReshetikhin(ct, 4, 1)
            sage: K.module_generator()
            [[1], [2], [3], [4]]
        """
    def classical_decomposition(self):
        """
        Return the classical crystal underlying the Kirillov-Reshetikhin
        crystal of type `A_{2n}^{(2)}` with `B_n` as classical subdiagram.

        It is given by `B^{r,s} \\cong \\bigoplus_{\\Lambda} B(\\Lambda)`,
        where `B(\\Lambda)` is a highest weight crystal of type `B_n`
        of highest weight `\\Lambda`. The sum is over all weights `\\Lambda`
        obtained from a rectangle of width `s` and height `r` by removing
        horizontal dominoes. Here we identify the fundamental weight
        `\\Lambda_i` with a column of height `i`.

        EXAMPLES::

            sage: C = CartanType(['A',4,2]).dual()
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 2, 2)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['B', 2] and shape(s) [[], [2], [2, 2]]
        """
    def ambient_crystal(self):
        """
        Return the ambient crystal `B^{r,s}` of type `B_{n+1}^{(1)}`
        associated to the Kirillov-Reshetikhin crystal of type
        `A_{2n}^{(2)}` dual.

        This ambient crystal is used to construct the zero arrows.

        EXAMPLES::

            sage: C = CartanType(['A',4,2]).dual()
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 2, 3)
            sage: K.ambient_crystal()
            Kirillov-Reshetikhin crystal of type ['B', 3, 1] with (r,s)=(2,3)
        """
    @cached_method
    def ambient_dict_pm_diagrams(self):
        """
        Return a dictionary of all self-dual `\\pm` diagrams for the
        ambient crystal whose keys are their inner shape.

        EXAMPLES::

            sage: C = CartanType(['A',4,2]).dual()
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 1)
            sage: K.ambient_dict_pm_diagrams()
            {[1]: [[0, 0], [1]]}
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 2)
            sage: K.ambient_dict_pm_diagrams()
            {[]: [[1, 1], [0]], [2]: [[0, 0], [2]]}
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 2, 2)
            sage: K.ambient_dict_pm_diagrams()
            {[]: [[1, 1], [0, 0], [0]],
             [2]: [[0, 0], [1, 1], [0]],
             [2, 2]: [[0, 0], [0, 0], [2]]}
        """
    @cached_method
    def ambient_highest_weight_dict(self):
        """
        Return a dictionary of all `\\{2,\\ldots,n+1\\}`-highest weight vectors
        in the ambient crystal.

        The key is the inner shape of their corresponding `\\pm` diagram,
        or equivalently, their `\\{2,\\ldots,n+1\\}` weight.

        EXAMPLES::

            sage: C = CartanType(['A',4,2]).dual()
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 2)
            sage: K.ambient_highest_weight_dict()
            {[]: [[1, -1]], [2]: [[2, 2]]}
        """
    @cached_method
    def highest_weight_dict(self):
        """
        Return a dictionary of the classical highest weight vectors
        of ``self`` whose keys are their shape.

        EXAMPLES::

            sage: C = CartanType(['A',4,2]).dual()
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 2)
            sage: K.highest_weight_dict()
            {[]: [], [2]: [[1, 1]]}
        """
    @cached_method
    def to_ambient_crystal(self):
        """
        Return a map from the Kirillov-Reshetikhin crystal of type
        `A_{2n}^{(2)}` to the ambient crystal of type `B_{n+1}^{(1)}`.

        EXAMPLES::

            sage: C = CartanType(['A',4,2]).dual()
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 2)
            sage: b=K(rows=[[1,1]])
            sage: K.to_ambient_crystal()(b)
            [[2, 2]]
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 2, 2)
            sage: b=K(rows=[[1,1]])
            sage: K.to_ambient_crystal()(b)
            [[1, 2], [2, -1]]
            sage: K.to_ambient_crystal()(b).parent()
            Kirillov-Reshetikhin crystal of type ['B', 3, 1] with (r,s)=(2,2)
        """
    @cached_method
    def from_ambient_crystal(self):
        """
        Return a map from the ambient crystal of type `B_{n+1}^{(1)}` to
        the Kirillov-Reshetikhin crystal of type `A_{2n}^{(2)}`.

        Note that this map is only well-defined on type `A_{2n}^{(2)}`
        elements that are in the image under :meth:`to_ambient_crystal`.

        EXAMPLES::

            sage: C = CartanType(['A',4,2]).dual()
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 2)
            sage: b = K.ambient_crystal()(rows=[[2,2]])
            sage: K.from_ambient_crystal()(b)
            [[1, 1]]
        """

class KR_type_A2Element(KirillovReshetikhinGenericCrystalElement):
    """
    Class for the elements in the Kirillov-Reshetikhin crystals `B^{r,s}` of
    type `A_{2n}^{(2)}` for `r<n` with underlying classical algebra `B_n`.

    EXAMPLES::

        sage: C = CartanType(['A',4,2]).dual()
        sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 2)
        sage: type(K.module_generators[0])
        <class 'sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2_with_category.element_class'>
    """
    def e0(self):
        """
        Return `e_0` on ``self`` by mapping ``self`` to the ambient crystal,
        calculating `e_1 e_0` there and pulling the element back.

        EXAMPLES::

            sage: C = CartanType(['A',4,2]).dual()
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 1)
            sage: b = K(rows=[[1]])
            sage: b.e(0) # indirect doctest
            [[-1]]
        """
    def f0(self):
        """
        Return `f_0` on ``self`` by mapping ``self`` to the ambient crystal,
        calculating `f_1 f_0` there and pulling the element back.

        EXAMPLES::

            sage: C = CartanType(['A',4,2]).dual()
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 1)
            sage: b = K(rows=[[-1]])
            sage: b.f(0) # indirect doctest
            [[1]]
        """
    def epsilon0(self):
        """
        Calculate `\\varepsilon_0` of ``self`` by mapping the element to
        the ambient crystal and calculating ``\\varepsilon_1`` there.

        EXAMPLES::

            sage: C = CartanType(['A',4,2]).dual()
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 1)
            sage: b=K(rows=[[1]])
            sage: b.epsilon(0) # indirect doctest
            1
        """
    def phi0(self):
        """
        Calculate `\\varphi_0` of ``self`` by mapping the element to
        the ambient crystal and calculating `\\varphi_1` there.

        EXAMPLES::

            sage: C = CartanType(['A',4,2]).dual()
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_A2(C, 1, 1)
            sage: b = K(rows=[[-1]])
            sage: b.phi(0) # indirect doctest
            1
        """

class KR_type_box(KirillovReshetikhinGenericCrystal, AffineCrystalFromClassical):
    """
    Class of Kirillov-Reshetikhin crystals `B^{r,s}` of type `A_{2n}^{(2)}`
    for `r\\le n` and type `D_{n+1}^{(2)}` for `r<n`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['A',4,2], 1,1)
        sage: K
        Kirillov-Reshetikhin crystal of type ['BC', 2, 2] with (r,s)=(1,1)
        sage: b = K(rows=[])
        sage: b.f(0)
        [[1]]
        sage: b.e(0)
        [[-1]]
    """
    def __init__(self, cartan_type, r, s) -> None:
        """
        Initialize a Kirillov-Reshetikhin crystal ``self``.

        TESTS::

            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_box(['A',4,2], 1, 1)
            sage: K
            Kirillov-Reshetikhin crystal of type ['BC', 2, 2] with (r,s)=(1,1)
            sage: K = sage.combinat.crystals.kirillov_reshetikhin.KR_type_box(['D',4,2], 1, 1)
            sage: K
            Kirillov-Reshetikhin crystal of type ['C', 3, 1]^* with (r,s)=(1,1)
            sage: TestSuite(K).run()
        """
    def classical_decomposition(self):
        """
        Return the classical crystal underlying the Kirillov-Reshetikhin
        crystal of type `A_{2n}^{(2)}` and `D_{n+1}^{(2)}`.

        It is given by `B^{r,s} \\cong \\bigoplus_{\\Lambda} B(\\Lambda)`,
        where `\\Lambda` are weights obtained from a rectangle of width `s`
        and height `r` by removing boxes. Here we identify the fundamental
        weight `\\Lambda_i` with a column of height `i`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',4,2], 2,2)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['C', 2] and shape(s) [[], [1], [2], [1, 1], [2, 1], [2, 2]]
            sage: K = crystals.KirillovReshetikhin(['D',4,2], 2,3)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['B', 3] and shape(s) [[], [1], [2], [1, 1], [3], [2, 1], [3, 1], [2, 2], [3, 2], [3, 3]]
        """
    def ambient_crystal(self):
        """
        Return the ambient crystal `B^{r,2s}` of type `C_n^{(1)}`
        associated to the Kirillov-Reshetikhin crystal.

        The ambient crystal is used to construct the zero arrows.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',4,2], 2,2)
            sage: K.ambient_crystal()
            Kirillov-Reshetikhin crystal of type ['C', 2, 1] with (r,s)=(2,4)
        """
    @cached_method
    def highest_weight_dict(self):
        """
        Return a dictionary of the classical highest weight vectors
        of ``self`` whose keys are 2 times their shape.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',6,2], 2,2)
            sage: K.highest_weight_dict()
            {[]: [],
             [2]: [[1]],
             [2, 2]: [[1], [2]],
             [4]: [[1, 1]],
             [4, 2]: [[1, 1], [2]],
             [4, 4]: [[1, 1], [2, 2]]}
        """
    @cached_method
    def ambient_highest_weight_dict(self):
        """
        Return a dictionary of the classical highest weight vectors of
        the ambient crystal of ``self`` whose keys are their shape.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',6,2], 2,2)
            sage: K.ambient_highest_weight_dict()
            {[]: [],
             [2]: [[1, 1]],
             [2, 2]: [[1, 1], [2, 2]],
             [4]: [[1, 1, 1, 1]],
             [4, 2]: [[1, 1, 1, 1], [2, 2]],
             [4, 4]: [[1, 1, 1, 1], [2, 2, 2, 2]]}
        """
    def similarity_factor(self):
        """
        Set the similarity factor used to map to the ambient crystal.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',6,2], 2,2)
            sage: K.similarity_factor()
            {1: 2, 2: 2, 3: 2}
            sage: K = crystals.KirillovReshetikhin(['D',5,2], 1,1)
            sage: K.similarity_factor()
            {1: 2, 2: 2, 3: 2, 4: 1}
        """
    @cached_method
    def to_ambient_crystal(self):
        """
        Return a map from ``self`` to the ambient crystal of type `C_n^{(1)}`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,2], 1,1)
            sage: [K.to_ambient_crystal()(b) for b in K]
            [[], [[1, 1]], [[2, 2]], [[3, 3]], [[3, -3]], [[-3, -3]], [[-2, -2]], [[-1, -1]]]
            sage: K = crystals.KirillovReshetikhin(['A',4,2], 1,1)
            sage: [K.to_ambient_crystal()(b) for b in K]
            [[], [[1, 1]], [[2, 2]], [[-2, -2]], [[-1, -1]]]
        """
    @cached_method
    def from_ambient_crystal(self):
        """
        Return a map from the ambient crystal of type `C_n^{(1)}` to the
        Kirillov-Reshetikhin crystal ``self``.

        Note that this map is only well-defined on elements that are in the
        image under :meth:`to_ambient_crystal`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,2], 1,1)
            sage: b = K.ambient_crystal()(rows=[[3,-3]])
            sage: K.from_ambient_crystal()(b)
            [[0]]
            sage: K = crystals.KirillovReshetikhin(['A',4,2], 1,1)
            sage: b = K.ambient_crystal()(rows=[])
            sage: K.from_ambient_crystal()(b)
            []
        """

class KR_type_boxElement(KirillovReshetikhinGenericCrystalElement):
    """
    Class for the elements in the Kirillov-Reshetikhin crystals `B^{r,s}` of
    type `A_{2n}^{(2)}` for `r \\leq n` and type `D_{n+1}^{(2)}` for `r < n`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['A',4,2],1,2)
        sage: type(K.module_generators[0])
        <class 'sage.combinat.crystals.kirillov_reshetikhin.KR_type_box_with_category.element_class'>
    """
    def e0(self):
        """
        Return `e_0` on ``self`` by mapping ``self`` to the ambient crystal,
        calculating `e_0` there and pulling the element back.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',4,2],1,1)
            sage: b = K(rows=[])
            sage: b.e(0) # indirect doctest
            [[-1]]
        """
    def f0(self):
        """
        Return `f_0` on ``self`` by mapping ``self`` to the ambient crystal,
        calculating `f_0` there and pulling the element back.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',4,2],1,1)
            sage: b = K(rows=[])
            sage: b.f(0) # indirect doctest
            [[1]]
        """
    def epsilon0(self):
        """
        Return `\\varepsilon_0` of ``self`` by mapping the element
        to the ambient crystal and calculating `\\varepsilon_0` there.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',4,2], 1,1)
            sage: b = K(rows=[[1]])
            sage: b.epsilon(0) # indirect doctest
            2
        """
    def phi0(self):
        """
        Return `\\varphi_0` of ``self`` by mapping the element to
        the ambient crystal and calculating `\\varphi_0` there.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',3,2], 1,1)
            sage: b = K(rows=[[-1]])
            sage: b.phi(0) # indirect doctest
            2
        """

class KR_type_Bn(KirillovReshetikhinGenericCrystal):
    """
    Class of Kirillov-Reshetikhin crystals `B^{n,s}` of type `B_{n}^{(1)}`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['B',3,1],3,2)
        sage: K
        Kirillov-Reshetikhin crystal of type ['B', 3, 1] with (r,s)=(3,2)
        sage: b = K(rows=[[1],[2],[3]])
        sage: b.f(0)
        sage: b.e(0)
        [[3]]

        sage: K = crystals.KirillovReshetikhin(['B',3,1],3,2)
        sage: [b.weight() for b in K if b.is_highest_weight([1,2,3])]
        [-Lambda[0] + Lambda[1], -2*Lambda[0] + 2*Lambda[3]]
        sage: [b.weight() for b in K if b.is_highest_weight([0,2,3])]
        [Lambda[0] - Lambda[1], -2*Lambda[1] + 2*Lambda[3]]
    """
    def classical_decomposition(self):
        """
        Return the classical crystal underlying the Kirillov-Reshetikhin
        crystal `B^{n,s}` of type `B_n^{(1)}`.

        It is the same as for `r < n`, given by
        `B^{n,s} \\cong \\bigoplus_{\\Lambda} B(\\Lambda)`, where `\\Lambda` are
        weights obtained from a rectangle of width `s/2` and height `n` by
        removing horizontal dominoes. Here we identify the fundamental weight
        `\\Lambda_i` with a column of height `i` for `i<n` and a column of
        width `1/2` for `i=n`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B',3,1], 3, 2)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['B', 3] and shape(s) [[1], [1, 1, 1]]
            sage: K = crystals.KirillovReshetikhin(['B',3,1], 3, 3)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['B', 3] and shape(s) [[3/2, 1/2, 1/2], [3/2, 3/2, 3/2]]
        """
    def ambient_crystal(self):
        """
        Return the ambient crystal `B^{n,s}` of type `A_{2n-1}^{(2)}`
        associated to the Kirillov-Reshetikhin crystal.

        The ambient crystal is used to construct the zero arrows.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B',3,1],3,2)
            sage: K.ambient_crystal()
            Kirillov-Reshetikhin crystal of type ['B', 3, 1]^* with (r,s)=(3,2)
        """
    @cached_method
    def highest_weight_dict(self):
        """
        Return a dictionary of the classical highest weight vectors
        of ``self`` whose keys are 2 times their shape.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B',3,1],3,2)
            sage: K.highest_weight_dict()
            {(2,): [[1]], (2, 2, 2): [[1], [2], [3]]}
            sage: K = crystals.KirillovReshetikhin(['B',3,1],3,3)
            sage: K.highest_weight_dict()
            {(3, 1, 1): [+++, [[1]]], (3, 3, 3): [+++, [[1], [2], [3]]]}
        """
    @cached_method
    def ambient_highest_weight_dict(self):
        """
        Return a dictionary of the classical highest weight vectors of
        the ambient crystal of ``self`` whose keys are their shape.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B',3,1],3,2)
            sage: K.ambient_highest_weight_dict()
            {(2,): [[1, 1]], (2, 1, 1): [[1, 1], [2], [3]], (2, 2, 2): [[1, 1], [2, 2], [3, 3]]}

            sage: K = crystals.KirillovReshetikhin(['B',3,1],3,3)
            sage: K.ambient_highest_weight_dict()
            {(3,): [[1, 1, 1]],
             (3, 1, 1): [[1, 1, 1], [2], [3]],
             (3, 2, 2): [[1, 1, 1], [2, 2], [3, 3]],
             (3, 3, 3): [[1, 1, 1], [2, 2, 2], [3, 3, 3]]}
        """
    def similarity_factor(self):
        """
        Set the similarity factor used to map to the ambient crystal.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B',3,1],3,2)
            sage: K.similarity_factor()
            {1: 2, 2: 2, 3: 1}
        """
    @cached_method
    def to_ambient_crystal(self):
        """
        Return a map from ``self`` to the ambient crystal of type `A_{2n-1}^{(2)}`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B',3,1],3,1)
            sage: [K.to_ambient_crystal()(b) for b in K]
            [[[1], [2], [3]], [[1], [2], [-3]], [[1], [3], [-2]], [[2], [3], [-1]], [[1], [-3], [-2]],
            [[2], [-3], [-1]], [[3], [-2], [-1]], [[-3], [-2], [-1]]]
        """
    @cached_method
    def from_ambient_crystal(self):
        """
        Return a map from the ambient crystal of type `A_{2n-1}^{(2)}` to
        the Kirillov-Reshetikhin crystal ``self``.

        Note that this map is only well-defined on elements that are in the
        image under :meth:`to_ambient_crystal`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B',3,1],3,1)
            sage: [b == K.from_ambient_crystal()(K.to_ambient_crystal()(b)) for b in K]
            [True, True, True, True, True, True, True, True]
            sage: b = K.ambient_crystal()(rows=[[1],[2],[-3]])
            sage: K.from_ambient_crystal()(b)
            [++-, []]
        """

class KR_type_BnElement(KirillovReshetikhinGenericCrystalElement):
    """
    Class for the elements in the Kirillov-Reshetikhin crystals `B^{n,s}`
    of type `B_n^{(1)}`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['B', 3, 1], 3, 2)
        sage: type(K.module_generators[0])
        <class 'sage.combinat.crystals.kirillov_reshetikhin.KR_type_Bn_with_category.element_class'>
    """
    def e0(self):
        """
        Return `e_0` on ``self`` by mapping ``self`` to the ambient crystal,
        calculating `e_0` there and pulling the element back.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B',3,1],3,1)
            sage: b = K.module_generators[0]
            sage: b.e(0) # indirect doctest
            [--+, []]
        """
    def f0(self):
        """
        Return `f_0` on ``self`` by mapping ``self`` to the ambient crystal,
        calculating `f_0` there and pulling the element back.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B', 3, 1], 3, 1)
            sage: b = K.module_generators[0]
            sage: b.f(0) # indirect doctest
        """
    def epsilon0(self):
        """
        Calculate `\\varepsilon_0` of ``self`` by mapping the element
        to the ambient crystal and calculating `\\varepsilon_0` there.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B', 3, 1], 3, 1)
            sage: b = K.module_generators[0]
            sage: b.epsilon(0) # indirect doctest
            1
        """
    def phi0(self):
        """
        Calculate `\\varphi_0` of ``self`` by mapping the element to
        the ambient crystal and calculating `\\varphi_0` there.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B', 3, 1], 3, 1)
            sage: b = K.module_generators[0]
            sage: b.phi(0) # indirect doctest
            0
        """

class KR_type_Cn(KirillovReshetikhinGenericCrystal):
    """
    Class of Kirillov-Reshetikhin crystals `B^{n,s}` of type `C_n^{(1)}`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['C',3,1],3,1)
        sage: [[b,b.f(0)] for b in K]
        [[[[1], [2], [3]], None], [[[1], [2], [-3]], None],
         [[[1], [3], [-3]], None], [[[2], [3], [-3]], None],
         [[[1], [3], [-2]], None], [[[2], [3], [-2]], None],
         [[[2], [3], [-1]], [[1], [2], [3]]], [[[1], [-3], [-2]], None],
         [[[2], [-3], [-2]], None], [[[2], [-3], [-1]], [[1], [2], [-3]]],
         [[[3], [-3], [-2]], None], [[[3], [-3], [-1]], [[1], [3], [-3]]],
         [[[3], [-2], [-1]], [[1], [3], [-2]]],
         [[[-3], [-2], [-1]], [[1], [-3], [-2]]]]
    """
    def classical_decomposition(self):
        """
        Specifies the classical crystal underlying the Kirillov-Reshetikhin
        crystal `B^{n,s}` of type `C_n^{(1)}`.

        The classical decomposition is given by
        `B^{n,s} \\cong B(s \\Lambda_n)`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',3,1],3,2)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['C', 3] and shape(s) [[2, 2, 2]]
        """
    def from_highest_weight_vector_to_pm_diagram(self, b):
        """
        This gives the bijection between an element ``b`` in the classical
        decomposition of the KR crystal that is `{2,3,..,n}`-highest weight
        and `\\pm` diagrams.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',3,1],3,2)
            sage: T = K.classical_decomposition()
            sage: b = T(rows=[[2, 2], [3, 3], [-3, -1]])
            sage: pm = K.from_highest_weight_vector_to_pm_diagram(b); pm
            [[0, 0], [1, 0], [0, 1], [0]]
            sage: pm.pp()
            .  .
            .  +
            -  -

            sage: hw = [ b for b in T if all(b.epsilon(i)==0 for i in [2,3]) ]
            sage: all(K.from_pm_diagram_to_highest_weight_vector(K.from_highest_weight_vector_to_pm_diagram(b)) == b for b in hw)
            True
        """
    def from_pm_diagram_to_highest_weight_vector(self, pm):
        """
        This gives the bijection between a `\\pm` diagram and an element ``b``
        in the classical decomposition of the KR crystal that is
        `\\{2,3,..,n\\}`-highest weight.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',3,1],3,2)
            sage: pm = sage.combinat.crystals.kirillov_reshetikhin.PMDiagram([[0, 0], [1, 0], [0, 1], [0]])
            sage: K.from_pm_diagram_to_highest_weight_vector(pm)
            [[2, 2], [3, 3], [-3, -1]]
        """

class KR_type_CnElement(KirillovReshetikhinGenericCrystalElement):
    """
    Class for the elements in the Kirillov-Reshetikhin crystals `B^{n,s}`
    of type `C_n^{(1)}`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['C', 3, 1], 3, 2)
        sage: type(K.module_generators[0])
        <class 'sage.combinat.crystals.kirillov_reshetikhin.KR_type_Cn_with_category.element_class'>
    """
    def e0(self):
        """
        Return `e_0` on ``self`` by going to the `\\pm`-diagram corresponding
        to the `\\{2,...,n\\}`-highest weight vector in the component of
        ``self``, then applying [Definition 6.1, 4], and pulling back from
        `\\pm`-diagrams.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C', 3, 1], 3, 2)
            sage: b = K.module_generators[0]
            sage: b.e(0) # indirect doctest
            [[1, 2], [2, 3], [3, -1]]
            sage: b = K(rows=[[1,2],[2,3],[3,-1]])
            sage: b.e(0)
            [[2, 2], [3, 3], [-1, -1]]
            sage: b=K(rows=[[1, -3], [3, -2], [-3, -1]])
            sage: b.e(0)
            [[3, -3], [-3, -2], [-1, -1]]
        """
    def f0(self):
        """
        Return `e_0` on ``self`` by going to the `\\pm`-diagram corresponding
        to the `\\{2,...,n\\}`-highest weight vector in the component of
        ``self``, then applying [Definition 6.1, 4], and pulling back from
        `\\pm`-diagrams.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C',3,1],3,1)
            sage: b = K.module_generators[0]
            sage: b.f(0) # indirect doctest
        """
    def epsilon0(self):
        """
        Calculate `\\varepsilon_0` of ``self`` using Lemma 6.1 of [4].

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C', 3, 1], 3, 1)
            sage: b = K.module_generators[0]
            sage: b.epsilon(0) # indirect doctest
            1
        """
    def phi0(self):
        """
        Calculate `\\varphi_0` of ``self``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['C', 3, 1], 3, 1)
            sage: b = K.module_generators[0]
            sage: b.phi(0) # indirect doctest
            0
        """

class KR_type_Dn_twisted(KirillovReshetikhinGenericCrystal):
    """
    Class of Kirillov-Reshetikhin crystals `B^{n,s}` of type `D_{n+1}^{(2)}`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['D',4,2],3,1)
        sage: [[b,b.f(0)] for b in K]
        [[[+++, []], None], [[++-, []], None], [[+-+, []], None], [[-++, []],
        [+++, []]], [[+--, []], None], [[-+-, []], [++-, []]], [[--+, []], [+-+, []]],
        [[---, []], [+--, []]]]
    """
    def classical_decomposition(self):
        """
        Return the classical crystal underlying the Kirillov-Reshetikhin
        crystal `B^{n,s}` of type `D_{n+1}^{(2)}`.

        The classical decomposition is given by
        `B^{n,s} \\cong B(s \\Lambda_n)`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,2],3,1)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['B', 3] and shape(s) [[1/2, 1/2, 1/2]]
            sage: K = crystals.KirillovReshetikhin(['D',4,2],3,2)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['B', 3] and shape(s) [[1, 1, 1]]
        """
    def from_highest_weight_vector_to_pm_diagram(self, b):
        """
        This gives the bijection between an element ``b`` in the
        classical decomposition of the KR crystal that is
        `\\{2,3,\\ldots,n\\}`-highest weight and `\\pm` diagrams.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,2],3,1)
            sage: T = K.classical_decomposition()
            sage: hw = [ b for b in T if all(b.epsilon(i)==0 for i in [2,3]) ]
            sage: [K.from_highest_weight_vector_to_pm_diagram(b) for b in hw]
            [[[0, 0], [0, 0], [1, 0], [0]], [[0, 0], [0, 0], [0, 1], [0]]]

            sage: K = crystals.KirillovReshetikhin(['D',4,2],3,2)
            sage: T = K.classical_decomposition()
            sage: hw = [ b for b in T if all(b.epsilon(i)==0 for i in [2,3]) ]
            sage: [K.from_highest_weight_vector_to_pm_diagram(b) for b in hw]
            [[[0, 0], [0, 0], [2, 0], [0]], [[0, 0], [0, 0], [0, 0], [2]],
             [[0, 0], [2, 0], [0, 0], [0]], [[0, 0], [0, 0], [0, 2], [0]]]

        Note that, since the classical decomposition of this crystal is of
        type `B_n`, there can be (at most one) entry `0` in the
        `\\{2,3,\\ldots,n\\}`-highest weight elements at height `n`.
        In the following implementation this is realized as an empty
        column of height `n` since this uniquely specifies the existence
        of the `0`.

        EXAMPLES::

            sage: b = hw[1]
            sage: pm = K.from_highest_weight_vector_to_pm_diagram(b)
            sage: pm.pp()
            .  .
            .  .
            .  .

        TESTS::

            sage: all(K.from_pm_diagram_to_highest_weight_vector(K.from_highest_weight_vector_to_pm_diagram(b)) == b for b in hw)
            True
            sage: K = crystals.KirillovReshetikhin(['D',4,2],3,2)
            sage: T = K.classical_decomposition()
            sage: hw = [ b for b in T if all(b.epsilon(i)==0 for i in [2,3]) ]
            sage: all(K.from_pm_diagram_to_highest_weight_vector(K.from_highest_weight_vector_to_pm_diagram(b)) == b for b in hw)
            True
            sage: K = crystals.KirillovReshetikhin(['D',4,2],3,3)
            sage: T = K.classical_decomposition()
            sage: hw = [ b for b in T if all(b.epsilon(i)==0 for i in [2,3]) ]
            sage: all(K.from_pm_diagram_to_highest_weight_vector(K.from_highest_weight_vector_to_pm_diagram(b)) == b for b in hw)
            True
        """
    def from_pm_diagram_to_highest_weight_vector(self, pm):
        """
        This gives the bijection between a `\\pm` diagram and an element
        ``b`` in the classical decomposition of the KR crystal that is
        `\\{2,3,\\ldots,n\\}`-highest weight.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,2],3,2)
            sage: pm = sage.combinat.crystals.kirillov_reshetikhin.PMDiagram([[0, 0], [0, 0], [0, 0], [2]])
            sage: K.from_pm_diagram_to_highest_weight_vector(pm)
            [[2], [3], [0]]
        """

class KR_type_Dn_twistedElement(KirillovReshetikhinGenericCrystalElement):
    """
    Class for the elements in the Kirillov-Reshetikhin crystals `B^{n,s}`
    of type `D_{n+1}^{(2)}`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['D', 4, 2], 3, 2)
        sage: type(K.module_generators[0])
        <class 'sage.combinat.crystals.kirillov_reshetikhin.KR_type_Dn_twisted_with_category.element_class'>
    """
    def e0(self):
        """
        Return `e_0` on ``self`` by going to the `\\pm`-diagram corresponding
        to the `\\{2,\\ldots,n\\}`-highest weight vector in the component of
        ``self``, then applying [Definition 6.2, 4], and pulling back from
        `\\pm`-diagrams.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D', 4, 2], 3, 3)
            sage: b = K.module_generators[0]
            sage: b.e(0) # indirect doctest
            [+++, [[2], [3], [0]]]
        """
    def f0(self):
        """
        Return `e_0` on ``self`` by going to the `\\pm`-diagram corresponding
        to the `\\{2,\\ldots,n\\}`-highest weight vector in the component of
        ``self``, then applying [Definition 6.2, 4], and pulling back from
        `\\pm`-diagrams.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,2],3,2)
            sage: b = K.module_generators[0]
            sage: b.f(0) # indirect doctest
        """
    def epsilon0(self):
        """
        Calculate `\\varepsilon_0` of ``self`` using Lemma 6.2 of [4].

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D', 4, 2], 3, 1)
            sage: b = K.module_generators[0]
            sage: b.epsilon(0) # indirect doctest
            1

        TESTS:

        Check that :issue:`19982` is fixed::

            sage: K = crystals.KirillovReshetikhin(['D',3,2], 2,3)
            sage: def eps0_defn(elt):
            ....:     x = elt.e(0)
            ....:     eps = 0
            ....:     while x is not None:
            ....:         x = x.e(0)
            ....:         eps = eps + 1
            ....:     return eps
            sage: all(eps0_defn(x) == x.epsilon0() for x in K)
            True
        """
    def phi0(self):
        """
        Calculate `\\varphi_0` of ``self``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,2],3,1)
            sage: b = K.module_generators[0]
            sage: b.phi(0) # indirect doctest
            0

        TESTS:

        Check that :issue:`19982` is fixed::

            sage: K = crystals.KirillovReshetikhin(['D',3,2], 2,3)
            sage: def phi0_defn(elt):
            ....:     x = elt.f(0)
            ....:     phi = 0
            ....:     while x is not None:
            ....:         x = x.f(0)
            ....:         phi = phi + 1
            ....:     return phi
            sage: all(phi0_defn(x) == x.phi0() for x in K)
            True
        """

class KR_type_spin(KirillovReshetikhinCrystalFromPromotion):
    """
    Class of Kirillov-Reshetikhin crystals `B^{n,s}` of type `D_n^{(1)}`.

    EXAMPLES::

        sage: K = crystals.KirillovReshetikhin(['D',4,1],4,1); K
        Kirillov-Reshetikhin crystal of type ['D', 4, 1] with (r,s)=(4,1)
        sage: [[b,b.f(0)] for b in K]
        [[[++++, []], None], [[++--, []], None], [[+-+-, []], None],
         [[-++-, []], None], [[+--+, []], None], [[-+-+, []], None],
         [[--++, []], [++++, []]], [[----, []], [++--, []]]]

        sage: K = crystals.KirillovReshetikhin(['D',4,1],4,2); K
        Kirillov-Reshetikhin crystal of type ['D', 4, 1] with (r,s)=(4,2)
        sage: [[b,b.f(0)] for b in K]
        [[[[1], [2], [3], [4]], None], [[[1], [2], [-4], [4]], None],
         [[[1], [3], [-4], [4]], None], [[[2], [3], [-4], [4]], None],
         [[[1], [4], [-4], [4]], None], [[[2], [4], [-4], [4]], None],
         [[[3], [4], [-4], [4]], [[1], [2], [3], [4]]],
         [[[-4], [4], [-4], [4]], [[1], [2], [-4], [4]]],
         [[[-4], [4], [-4], [-3]], [[1], [2], [-4], [-3]]],
         [[[-4], [4], [-4], [-2]], [[1], [3], [-4], [-3]]],
         [[[-4], [4], [-4], [-1]], [[2], [3], [-4], [-3]]],
         [[[-4], [4], [-3], [-2]], [[1], [4], [-4], [-3]]],
         [[[-4], [4], [-3], [-1]], [[2], [4], [-4], [-3]]],
         [[[-4], [4], [-2], [-1]], [[-4], [4], [-4], [4]]],
         [[[-4], [-3], [-2], [-1]], [[-4], [4], [-4], [-3]]],
         [[[1], [2], [-4], [-3]], None], [[[1], [3], [-4], [-3]], None],
         [[[2], [3], [-4], [-3]], None], [[[1], [3], [-4], [-2]], None],
         [[[2], [3], [-4], [-2]], None], [[[2], [3], [-4], [-1]], None],
         [[[1], [4], [-4], [-3]], None], [[[2], [4], [-4], [-3]], None],
         [[[3], [4], [-4], [-3]], None],
         [[[3], [4], [-4], [-2]], [[1], [3], [-4], [4]]],
         [[[3], [4], [-4], [-1]], [[2], [3], [-4], [4]]],
         [[[1], [4], [-4], [-2]], None], [[[2], [4], [-4], [-2]], None],
         [[[2], [4], [-4], [-1]], None], [[[1], [4], [-3], [-2]], None],
         [[[2], [4], [-3], [-2]], None], [[[2], [4], [-3], [-1]], None],
         [[[3], [4], [-3], [-2]], [[1], [4], [-4], [4]]],
         [[[3], [4], [-3], [-1]], [[2], [4], [-4], [4]]],
         [[[3], [4], [-2], [-1]], [[3], [4], [-4], [4]]]]

    TESTS::

        sage: K = crystals.KirillovReshetikhin(['D',4,1],3,1)
        sage: all(b.e(0).f(0) == b for b in K if b.epsilon(0)>0)
        True

        sage: K = crystals.KirillovReshetikhin(['D',5,1],5,2)
        sage: all(b.f(0).e(0) == b for b in K if b.phi(0)>0)
        True
    """
    def classical_decomposition(self):
        """
        Return the classical crystal underlying the Kirillov-Reshetikhin
        crystal `B^{r,s}` of type `D_n^{(1)}` for `r=n-1,n`.

        The classical decomposition is given by
        `B^{n,s} \\cong B(s \\Lambda_r)`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1],4,1)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['D', 4] and shape(s) [[1/2, 1/2, 1/2, 1/2]]
            sage: K = crystals.KirillovReshetikhin(['D',4,1],3,1)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['D', 4] and shape(s) [[1/2, 1/2, 1/2, -1/2]]
            sage: K = crystals.KirillovReshetikhin(['D',4,1],3,2)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['D', 4] and shape(s) [[1, 1, 1, -1]]

        TESTS:

        Check that this is robust against python ints::

            sage: K = crystals.KirillovReshetikhin(['D',4,1], 4, int(1))
            sage: K.classical_crystal
            The crystal of tableaux of type ['D', 4] and shape(s) [[1/2, 1/2, 1/2, 1/2]]
        """
    def dynkin_diagram_automorphism(self, i):
        """
        Specifies the Dynkin diagram automorphism underlying the promotion
        action on the crystal elements.

        Here we use the Dynkin diagram automorphism which interchanges
        nodes 0 and 1 and leaves all other nodes unchanged.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1],4,1)
            sage: K.dynkin_diagram_automorphism(0)
            1
            sage: K.dynkin_diagram_automorphism(1)
            0
            sage: K.dynkin_diagram_automorphism(4)
            4
        """
    @cached_method
    def promotion_on_highest_weight_vectors(self):
        '''
        Return the promotion operator on `\\{2,3,\\ldots,n\\}`-highest
        weight vectors.

        A `\\{2,3,\\ldots,n\\}`-highest weight vector in `B(s\\Lambda_n)` of
        weight `w = (w_1,\\ldots,w_n)` is mapped to a
        `\\{2,3,\\ldots,n\\}`-highest weight vector in `B(s\\Lambda_{n-1})`
        of weight `(-w_1,w_2,\\ldots,w_n)` and vice versa.

        .. SEEALSO::

            - :meth:`promotion_on_highest_weight_vectors_inverse`
            - :meth:`promotion`

        EXAMPLES::

            sage: KR = crystals.KirillovReshetikhin([\'D\',4,1],4,2)
            sage: prom = KR.promotion_on_highest_weight_vectors()
            sage: T = KR.classical_decomposition()
            sage: HW = [t for t in T if t.is_highest_weight([2,3,4])]
            sage: for t in HW:
            ....:     print("{} {}".format(t, prom[t]))
            [[1], [2], [3], [4]] [[2], [3], [4], [-1]]
            [[2], [3], [-4], [4]] [[2], [3], [4], [-4]]
            [[2], [3], [-4], [-1]] [[1], [2], [3], [-4]]

            sage: KR = crystals.KirillovReshetikhin([\'D\',4,1],4,1)
            sage: prom = KR.promotion_on_highest_weight_vectors()
            sage: T = KR.classical_decomposition()
            sage: HW = [t for t in T if t.is_highest_weight([2,3,4])]
            sage: for t in HW:
            ....:     print("{} {}".format(t, prom[t]))
            [++++, []] [-+++, []]
            [-++-, []] [+++-, []]
        '''
    @cached_method
    def promotion_on_highest_weight_vectors_inverse(self):
        """
        Return the inverse promotion operator on
        `\\{2,3,\\ldots,n\\}`-highest weight vectors.

        .. SEEALSO::

            - :meth:`promotion_on_highest_weight_vectors`
            - :meth:`promotion_inverse`

        EXAMPLES::

            sage: KR = crystals.KirillovReshetikhin(['D',4,1],3,2)
            sage: prom = KR.promotion_on_highest_weight_vectors()
            sage: prom_inv = KR.promotion_on_highest_weight_vectors_inverse()
            sage: T = KR.classical_decomposition()
            sage: HW = [t for t in T if t.is_highest_weight([2,3,4])]
            sage: all(prom_inv[prom[t]] == t for t in HW)
            True
        """
    @cached_method
    def promotion(self):
        '''
        Return the promotion operator on `B^{r,s}` of type
        `D_n^{(1)}` for `r = n-1,n`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin([\'D\',4,1],3,1)
            sage: T = K.classical_decomposition()
            sage: promotion = K.promotion()
            sage: for t in T:
            ....:     print("{} {}".format(t, promotion(t)))
            [+++-, []] [-++-, []]
            [++-+, []] [-+-+, []]
            [+-++, []] [--++, []]
            [-+++, []] [++++, []]
            [+---, []] [----, []]
            [-+--, []] [++--, []]
            [--+-, []] [+-+-, []]
            [---+, []] [+--+, []]
        '''
    @cached_method
    def promotion_inverse(self):
        """
        Return the inverse promotion operator on `B^{r,s}` of type
        `D_n^{(1)}` for `r=n-1,n`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,1],3,1)
            sage: T = K.classical_decomposition()
            sage: promotion = K.promotion()
            sage: promotion_inverse = K.promotion_inverse()
            sage: all(promotion_inverse(promotion(t)) == t for t in T)
            True
        """

class KR_type_D_tri1(KirillovReshetikhinGenericCrystal):
    """
    Class of Kirillov-Reshetikhin crystals `B^{1,s}` of type `D_4^{(3)}`.

    The crystal structure was defined in Section 4 of [KMOY2007]_ using
    the coordinate representation.
    """
    def __init__(self, ct, s) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,3], 1, 2)
            sage: TestSuite(K).run()
        """
    def classical_decomposition(self):
        """
        Return the classical decomposition of ``self``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,3], 1, 5)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['G', 2]
             and shape(s) [[], [1], [2], [3], [4], [5]]
        """
    def from_coordinates(self, coords):
        """
        Return an element of ``self`` from the coordinates ``coords``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['D',4,3], 1, 5)
            sage: K.from_coordinates((0, 2, 3, 1, 0, 1))
            [[2, 2, 3, 0, -1]]
        """
    class Element(KirillovReshetikhinGenericCrystalElement):
        @cached_method
        def coordinates(self):
            """
            Return ``self`` as coordinates.

            EXAMPLES::

                sage: K = crystals.KirillovReshetikhin(['D',4,3], 1, 3)
                sage: all(K.from_coordinates(x.coordinates()) == x for x in K)
                True
            """
        def e0(self):
            """
            Return the action of `e_0` on ``self``.

            EXAMPLES::

                sage: K = crystals.KirillovReshetikhin(['D',4,3], 1,1)
                sage: [x.e0() for x in K]
                [[[-1]], [], [[-3]], [[-2]], None, None, None, None]
            """
        def f0(self):
            """
            Return the action of `f_0` on ``self``.

            EXAMPLES::

                sage: K = crystals.KirillovReshetikhin(['D',4,3], 1,1)
                sage: [x.f0() for x in K]
                [[[1]], None, None, None, None, [[2]], [[3]], []]
            """
        def epsilon0(self):
            """
            Return `\\varepsilon_0` of ``self``.

            EXAMPLES::

                sage: K = crystals.KirillovReshetikhin(['D',4,3], 1, 5)
                sage: [mg.epsilon0() for mg in K.module_generators]
                [5, 6, 7, 8, 9, 10]
            """
        def phi0(self):
            """
            Return `\\varphi_0` of ``self``.

            EXAMPLES::

                sage: K = crystals.KirillovReshetikhin(['D',4,3], 1, 5)
                sage: [mg.phi0() for mg in K.module_generators]
                [5, 4, 3, 2, 1, 0]
            """

class CrystalOfTableaux_E7(CrystalOfTableaux):
    """
    The type `E_7` crystal `B(s\\Lambda_7)`.

    This is a helper class for the corresponding:class:`KR crystal
    <sage.combinat.crystals.kirillov_reshetikhin.KR_type_E7>` `B^{7,s}`.
    """
    def module_generator(self, shape):
        """
        Return the module generator of ``self`` with shape ``shape``.

        .. NOTE::

            Only implemented for single rows (i.e., highest weight
            `s\\Lambda_7`).

        EXAMPLES::

            sage: from sage.combinat.crystals.kirillov_reshetikhin import CrystalOfTableaux_E7
            sage: T = CrystalOfTableaux_E7(CartanType(['E',7]), shapes=(Partition([5]),))
            sage: T.module_generator([5])
            [[(7,), (7,), (7,), (7,), (7,)]]
        """

class KR_type_E7(KirillovReshetikhinGenericCrystal):
    """
    The Kirillov-Reshetikhin crystal `B^{7,s}` of type `E_7^{(1)}`.
    """
    def __init__(self, ct, r, s) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',7,1], 7, 1)
            sage: TestSuite(K).run()

            sage: K = crystals.KirillovReshetikhin(['E',7,1], 7, 2)
            sage: TestSuite(K).run()  # long time
        """
    def classical_decomposition(self):
        """
        Return the classical decomposition of ``self``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',7,1], 7, 4)
            sage: K.classical_decomposition()
            The crystal of tableaux of type ['E', 7] and shape(s) [[4]]
        """
    @cached_method
    def A7_decomposition(self):
        """
        Return the decomposition of ``self`` into `A_7` highest
        weight crystals.

        The `A_7` decomposition of `B^{7,s}` is given by
        the parameters `m_4, m_5, m_6, m_7 \\geq 0` such that
        `m_4 + m_5 \\leq m_7` and `s = m_4 + m_5 + m_6 + m_7`. The
        corresponding `A_7` highest weight crystal has highest weight
        `\\lambda = (m_7 - m_4 - m_5) \\Lambda_6 + m_5 \\Lambda_4
        + m_6 \\Lambda_2`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',7,1], 7, 3)
            sage: K.A7_decomposition()
            The crystal of tableaux of type ['A', 7] and shape(s)
             [[3, 3, 3, 3, 3, 3], [3, 3, 2, 2, 2, 2], [3, 3, 1, 1, 1, 1], [3, 3],
              [2, 2, 2, 2, 1, 1], [2, 2, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1]]
        """
    @cached_method
    def to_A7_crystal(self):
        """
        Return the map decomposing the KR crystal `B^{7,s}` of
        type `E_7^{(1)}` into type `A_7` highest weight crystals.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',7,1], 7, 2)
            sage: K.to_A7_crystal()
            ['A', 6] relabelled by {1: 1, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7} -> ['A', 7] Virtual Crystal morphism:
              From: Kirillov-Reshetikhin crystal of type ['E', 7, 1] with (r,s)=(7,2)
              To:   The crystal of tableaux of type ['A', 7] and shape(s)
                [[2, 2, 2, 2, 2, 2], [2, 2, 1, 1, 1, 1], [2, 2], [1, 1, 1, 1], []]
              Defn: ...
        """
    @cached_method
    def from_A7_crystal(self):
        """
        Return the inclusion of the KR crystal `B^{7,s}` of
        type `E_7^{(1)}` into type `A_7` highest weight crystals.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['E',7,1], 7, 2)
            sage: K.from_A7_crystal()
            ['A', 6] -> ['E', 7, 1] Virtual Crystal morphism:
              From: The crystal of tableaux of type ['A', 7] and shape(s)
                [[2, 2, 2, 2, 2, 2], [2, 2, 1, 1, 1, 1], [2, 2], [1, 1, 1, 1], []]
              To:   Kirillov-Reshetikhin crystal of type ['E', 7, 1] with (r,s)=(7,2)
              Defn: ...
        """
    class Element(KirillovReshetikhinGenericCrystalElement):
        def e0(self):
            """
            Return the action of `e_0` on ``self``.

            EXAMPLES::

                sage: K = crystals.KirillovReshetikhin(['E',7,1], 7, 2)
                sage: mg = K.module_generator()
                sage: mg.e0()
                [[(7,), (-1, 7)]]
                sage: mg.e0().e0()
                [[(-1, 7), (-1, 7)]]
                sage: mg.e_string([0,0,0]) is None
                True
            """
        def f0(self):
            """
            Return the action of `f_0` on ``self``.

            EXAMPLES::

                sage: K = crystals.KirillovReshetikhin(['E',7,1], 7, 2)
                sage: mg = K.module_generator()
                sage: x = mg.f_string([7,6,5,4,3,2,4,5,6,1,3,4,5,2,4,3,1])
                sage: x.f0()
                [[(7,), (7,)]]
                sage: mg.f0() is None
                True
            """

class PMDiagram(CombinatorialObject):
    """
    Class of `\\pm` diagrams. These diagrams are in one-to-one bijection with
    `X_{n-1}` highest weight vectors in an `X_n` highest weight crystal
    `X=B,C,D`. See Section 4.1 of [Sch2008]_.

    The input is a list `pm = [[a_0,b_0], [a_1,b_1], ...,
    [a_{n-1},b_{n-1}], [b_n]]` of pairs and a last 1-tuple (or list of
    length 1). The pair `[a_i,b_i]` specifies the number of `a_i` `+` and
    `b_i` `-` in the `i`-th row of the `\\pm` diagram if `n-i` is odd and the
    number of `a_i` `\\pm` pairs above row `i` and `b_i` columns of height `i`
    not containing any `+` or `-` if `n-i` is even.

    Setting the option ``from_shapes = True`` one can also input a `\\pm`
    diagram in terms of its outer, intermediate, and inner shape by
    specifying a list ``[n, s, outer, intermediate, inner]``
    where ``s`` is the width of the `\\pm` diagram, and ``outer``,
    ``intermediate``, and ``inner`` are the outer, intermediate, and inner
    shapes, respectively.

    EXAMPLES::

        sage: from sage.combinat.crystals.kirillov_reshetikhin import PMDiagram
        sage: pm = PMDiagram([[0,1],[1,2],[1]])
        sage: pm.pm_diagram
        [[0, 1], [1, 2], [1]]
        sage: pm._list
        [1, 1, 2, 0, 1]
        sage: pm.n
        2
        sage: pm.width
        5
        sage: pm.pp()
        .  .  .  .
        .  +  -  -
        sage: PMDiagram([2,5,[4,4],[4,2],[4,1]], from_shapes=True)
        [[0, 1], [1, 2], [1]]

    TESTS::

        sage: from sage.combinat.crystals.kirillov_reshetikhin import PMDiagram
        sage: pm = PMDiagram([[1,2],[1,1],[1,1],[1,1],[1]])
        sage: PMDiagram([pm.n, pm.width, pm.outer_shape(), pm.intermediate_shape(), pm.inner_shape()], from_shapes=True) == pm
        True
        sage: pm = PMDiagram([[1,2],[1,2],[1,1],[1,1],[1,1],[1]])
        sage: PMDiagram([pm.n, pm.width, pm.outer_shape(), pm.intermediate_shape(), pm.inner_shape()], from_shapes=True) == pm
        True
    """
    pm_diagram: Incomplete
    n: Incomplete
    width: Incomplete
    def __init__(self, pm_diagram, from_shapes=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: from sage.combinat.crystals.kirillov_reshetikhin import PMDiagram
            sage: pm = PMDiagram([[0,1],[1,2],[1]]); pm
            [[0, 1], [1, 2], [1]]
            sage: PMDiagram([2,5,[4,4],[4,2],[4,1]], from_shapes=True)
            [[0, 1], [1, 2], [1]]
            sage: TestSuite(pm).run()
        """
    def pp(self) -> None:
        """
        Pretty print ``self``.

        EXAMPLES::

            sage: from sage.combinat.crystals.kirillov_reshetikhin import PMDiagram
            sage: pm = PMDiagram([[1,0],[0,1],[2,0],[0,0],[0]])
            sage: pm.pp()
            .  .  .  +
            .  .  -  -
            +  +
            -  -
            sage: pm = PMDiagram([[0,2], [0,0], [0]])
            sage: pm.pp()
        """
    def inner_shape(self):
        """
        Return the inner shape of the pm diagram.

        EXAMPLES::

            sage: from sage.combinat.crystals.kirillov_reshetikhin import PMDiagram
            sage: pm = PMDiagram([[0,1],[1,2],[1]])
            sage: pm.inner_shape()
            [4, 1]
            sage: pm = PMDiagram([[1,2],[1,1],[1,1],[1,1],[1]])
            sage: pm.inner_shape()
            [7, 5, 3, 1]
            sage: pm = PMDiagram([[1,2],[1,2],[1,1],[1,1],[1,1],[1]])
            sage: pm.inner_shape()
            [10, 7, 5, 3, 1]
        """
    def outer_shape(self):
        """
        Return the outer shape of the `\\pm` diagram.

        EXAMPLES::

            sage: from sage.combinat.crystals.kirillov_reshetikhin import PMDiagram
            sage: pm = PMDiagram([[0,1],[1,2],[1]])
            sage: pm.outer_shape()
            [4, 4]
            sage: pm = PMDiagram([[1,2],[1,1],[1,1],[1,1],[1]])
            sage: pm.outer_shape()
            [8, 8, 4, 4]
            sage: pm = PMDiagram([[1,2],[1,2],[1,1],[1,1],[1,1],[1]])
            sage: pm.outer_shape()
            [13, 8, 8, 4, 4]
        """
    def intermediate_shape(self):
        """
        Return the intermediate shape of the pm diagram (inner shape plus
        positions of plusses).

        EXAMPLES::

            sage: from sage.combinat.crystals.kirillov_reshetikhin import PMDiagram
            sage: pm = PMDiagram([[0,1],[1,2],[1]])
            sage: pm.intermediate_shape()
            [4, 2]
            sage: pm = PMDiagram([[1,2],[1,1],[1,1],[1,1],[1]])
            sage: pm.intermediate_shape()
            [8, 6, 4, 2]
            sage: pm = PMDiagram([[1,2],[1,2],[1,1],[1,1],[1,1],[1]])
            sage: pm.intermediate_shape()
            [11, 8, 6, 4, 2]
            sage: pm = PMDiagram([[1,0],[0,1],[2,0],[0,0],[0]])
            sage: pm.intermediate_shape()
            [4, 2, 2]
            sage: pm = PMDiagram([[1, 0], [0, 0], [0, 0], [0, 0], [0]])
            sage: pm.intermediate_shape()
            [1]
        """
    def heights_of_minus(self) -> list:
        """
        Return a list with the heights of all minus in the `\\pm` diagram.

        EXAMPLES::

            sage: from sage.combinat.crystals.kirillov_reshetikhin import PMDiagram
            sage: pm = PMDiagram([[1,2],[1,2],[1,1],[1,1],[1,1],[1]])
            sage: pm.heights_of_minus()
            [5, 5, 3, 3, 1, 1]
            sage: pm = PMDiagram([[1,2],[1,1],[1,1],[1,1],[1]])
            sage: pm.heights_of_minus()
            [4, 4, 2, 2]
        """
    def heights_of_addable_plus(self) -> list:
        """
        Return a list with the heights of all addable plus in the `\\pm` diagram.

        EXAMPLES::

            sage: from sage.combinat.crystals.kirillov_reshetikhin import PMDiagram
            sage: pm = PMDiagram([[1,2],[1,2],[1,1],[1,1],[1,1],[1]])
            sage: pm.heights_of_addable_plus()
            [1, 1, 2, 3, 4, 5]
            sage: pm = PMDiagram([[1,2],[1,1],[1,1],[1,1],[1]])
            sage: pm.heights_of_addable_plus()
            [1, 2, 3, 4]
        """
    def sigma(self):
        """
        Return sigma on pm diagrams as needed for the analogue of the Dynkin diagram automorphism
        that interchanges nodes `0` and `1` for type `D_n(1)`, `B_n(1)`, `A_{2n-1}(2)` for
        Kirillov-Reshetikhin crystals.

        EXAMPLES::

            sage: pm = sage.combinat.crystals.kirillov_reshetikhin.PMDiagram([[0,1],[1,2],[1]])
            sage: pm.sigma()
            [[1, 0], [2, 1], [1]]
        """

def partitions_in_box(r, s):
    """
    Return all partitions in a box of width s and height r.

    EXAMPLES::

        sage: sage.combinat.crystals.kirillov_reshetikhin.partitions_in_box(3,2)
        [[], [1], [2], [1, 1], [2, 1], [1, 1, 1], [2, 2], [2, 1, 1],
        [2, 2, 1], [2, 2, 2]]
    """
def vertical_dominoes_removed(r, s):
    """
    Return all partitions obtained from a rectangle of width s and height r by removing
    vertical dominoes.

    EXAMPLES::

        sage: sage.combinat.crystals.kirillov_reshetikhin.vertical_dominoes_removed(2,2)
        [[], [1, 1], [2, 2]]
        sage: sage.combinat.crystals.kirillov_reshetikhin.vertical_dominoes_removed(3,2)
        [[2], [2, 1, 1], [2, 2, 2]]
        sage: sage.combinat.crystals.kirillov_reshetikhin.vertical_dominoes_removed(4,2)
        [[], [1, 1], [1, 1, 1, 1], [2, 2], [2, 2, 1, 1], [2, 2, 2, 2]]
    """
def horizontal_dominoes_removed(r, s):
    """
    Return all partitions obtained from a rectangle of width s and height r by removing
    horizontal dominoes.

    EXAMPLES::

        sage: sage.combinat.crystals.kirillov_reshetikhin.horizontal_dominoes_removed(2,2)
        [[], [2], [2, 2]]
        sage: sage.combinat.crystals.kirillov_reshetikhin.horizontal_dominoes_removed(3,2)
        [[], [2], [2, 2], [2, 2, 2]]
    """

class AmbientRetractMap(Map):
    """
    The retraction map from the ambient crystal.

    Consider a crystal embedding `\\phi : X \\to Y`, then the elements `X`
    can be considered as a subcrystal of the ambient crystal `Y`. The
    ambient retract is the partial map `\\tilde{\\phi} : Y \\to X` such that
    `\\tilde{\\phi} \\circ \\phi` is the identity on `X`.
    """
    def __init__(self, base, ambient, pdict_inv, index_set, similarity_factor_domain=None, automorphism=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['B',3,1], 3,1)
            sage: phi = K.from_ambient_crystal()
            sage: TestSuite(phi).run(skip=['_test_category', '_test_pickling'])
        """

class CrystalDiagramAutomorphism(CrystalMorphism):
    """
    The crystal automorphism induced from the diagram automorphism.

    For example, in type `A_n^{(1)}` this is the promotion operator and in
    type `D_n^{(1)}`, this corresponds to the automorphism induced from
    interchanging the `0` and `1` nodes in the Dynkin diagram.

    INPUT:

    - ``C`` -- a crystal
    - ``on_hw`` -- a function for the images of the ``index_set``-highest
      weight elements
    - ``index_set`` -- (default: the empty set) the index set
    - ``automorphism`` -- (default: the identity) the twisting automorphism
    - ``cache`` -- boolean (default: ``True``); cache the result
    """
    def __init__(self, C, on_hw, index_set=None, automorphism=None, cache: bool = True) -> None:
        """
        Construct the promotion operator.

        TESTS::

            sage: K = crystals.KirillovReshetikhin(['A',3,1], 2,2)
            sage: p = K.promotion()
            sage: TestSuite(p).run(skip=['_test_category', '_test_pickling'])
        """
    def is_isomorphism(self) -> bool:
        """
        Return ``True`` as ``self`` is a crystal isomorphism.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A',3,1], 2,2)
            sage: K.promotion().is_isomorphism()
            True
        """
    is_surjective = is_isomorphism
    is_embedding = is_isomorphism
    is_strict = is_isomorphism
    __bool__ = is_isomorphism
