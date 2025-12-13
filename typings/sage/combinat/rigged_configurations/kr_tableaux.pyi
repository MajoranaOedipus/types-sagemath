from _typeshed import Incomplete
from sage.categories.loop_crystals import KirillovReshetikhinCrystals as KirillovReshetikhinCrystals
from sage.combinat.crystals.kirillov_reshetikhin import KashiwaraNakashimaTableaux as KashiwaraNakashimaTableaux, KirillovReshetikhinGenericCrystalElement as KirillovReshetikhinGenericCrystalElement, horizontal_dominoes_removed as horizontal_dominoes_removed, partitions_in_box as partitions_in_box, vertical_dominoes_removed as vertical_dominoes_removed
from sage.combinat.crystals.letters import CrystalOfLetters as CrystalOfLetters, EmptyLetter as EmptyLetter
from sage.combinat.crystals.tensor_product import CrystalOfWords as CrystalOfWords, TensorProductOfRegularCrystalsElement as TensorProductOfRegularCrystalsElement
from sage.combinat.partition import Partition as Partition
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.tableau import Tableau as Tableau
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.flatten import flatten as flatten
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.structure.parent import Parent as Parent

class KirillovReshetikhinTableaux(CrystalOfWords):
    """
    Kirillov-Reshetikhin tableaux.

    Kirillov-Reshetikhin tableaux are rectangular tableaux with `r` rows and
    `s` columns that naturally arise under the bijection between rigged
    configurations and tableaux [RigConBijection]_. They are in bijection with
    the elements of the Kirillov-Reshetikhin crystal `B^{r,s}` under the
    (inverse) filling map.

    Whenever `B^{r,s} \\cong B(s\\Lambda_r)` as a classical crystal (which is
    the case for `B^{r,s}` in type `A_n^{(1)}`, `B^{n,s}` in type `C_n^{(1)}`
    and `D_{n+1}^{(2)}`, `B^{n,s}` and `B^{n-1,s}` in type `D_n^{(1)}`) then
    the filling map is trivial.

    For `B^{r,s}` in:

    - type `D_n^{(1)}` when `r \\leq n-2`,
    - type `B_n^{(1)}` when `r < n`,
    - type `A_{2n-1}^{(2)}` for all `r`,

    the filling map is defined in [OSS2011]_.

    For the spinor cases in type `D_n^{(1)}`, the crystal `B^{k,s}` where
    `k = n-1, n`,  is isomorphic as a classical crystal to `B(s\\Lambda_k)`,
    and here we consider the Kirillov-Reshetikhin tableaux as living in
    `B(2s \\Lambda_k)` under the natural doubling map. In this case, the
    crystal operators `e_i` and `f_i` act as `e_i^2` and `f_i^2` respectively.
    See [BijectionDn]_.

    For the spinor case in type `B_n^{(1)}`, the crystal `B^{n,s}`, we
    consider the images under the natural doubling map into `B^{n,2s}`.
    The classical components of this crystal are now given by
    removing `2 \\times 2` boxes. The filling map is the same as below
    (see the non-spin type `C_n^{(1)}`).

    For `B^{r,s}` in:

    - type `C_n^{(1)}` when `r < n`,
    - type `A_{2n}^{(2)\\dagger}` for all `r`,

    the filling map is given as follows. Suppose we are considering the
    (classically) highest weight element in the classical component
    `B(\\lambda)`. Then we fill it in with the horizontal dominoes
    `[\\bar{\\imath}, i]` in the `i`-th row from the top (in English notation)
    and reordering the columns so that they are increasing. Recall from above
    that `B^{n,s} \\cong B(s\\Lambda_n)` in type `C^{(1)}_n`.

    For `B^{r,s}` in:

    - type `A_{2n}^{(2)}` for all `r`,
    - type `D_{n+1}^{(2)}` when `r < n`,
    - type `D_4^{(3)}` when `r = 1`,

    the filling map is the same as given in [OSS2011]_ except for
    the rightmost column which is given by the column `[1, 2, \\ldots, k,
    \\emptyset, \\ldots \\emptyset]` where `k = (r+x-1)/2` in Step 3 of
    [OSS2011]_.

    For the spinor case in type `D_{n+1}^{(2)}`, the crystal `B^{n,s}`, we
    define the filling map in the same way as in type `D_n^{(1)}`.

    .. NOTE::

        The filling map and classical decompositions in non-spinor cases can
        be classified by how the special node `0` connects with the
        corresponding classical diagram.

    The classical crystal structure is given by the usual Kashiwara-Nakashima
    tableaux rules. That is to embed this into `B(\\Lambda_1)^{\\otimes n s}`
    by using the reading word and then applying the classical crystal
    operator. The affine crystal structure is given by converting to
    the corresponding KR crystal element, performing the affine crystal
    operator, and pulling back to a KR tableau.

    For more information about the bijection between rigged configurations
    and tensor products of Kirillov-Reshetikhin tableaux, see
    :class:`~sage.combinat.rigged_configurations.tensor_product_kr_tableaux.TensorProductOfKirillovReshetikhinTableaux`.

    .. NOTE::

        The tableaux for all non-simply-laced types are provably correct if the
        bijection with :class:`rigged configurations
        <sage.combinat.rigged_configurations.rigged_configurations.RiggedConfigurations>`
        holds. Therefore this is currently only proven for `B^{r,1}` or
        `B^{1,s}` and in general for types `A_n^{(1)}` and `D_n^{(1)}`.

    INPUT:

    - ``cartan_type`` -- the Cartan type

    - ``r`` -- the Dynkin diagram index (typically the number of rows)

    - ``s`` -- the number of columns

    EXAMPLES::

        sage: KRT = crystals.KirillovReshetikhin(['A', 4, 1], 2, 1, model='KR')
        sage: elt = KRT(4, 3); elt
        [[3], [4]]

        sage: KRT = crystals.KirillovReshetikhin(['D', 4, 1], 2, 1, model='KR')
        sage: elt = KRT(-1, 1); elt
        [[1], [-1]]

    We can create highest weight crystals from a given shape or weight::

        sage: KRT = crystals.KirillovReshetikhin(['D', 4, 1], 2, 2, model='KR')
        sage: KRT.module_generator(shape=[1,1])
        [[1, 1], [2, -1]]
        sage: KRT.module_generator(column_shape=[2])
        [[1, 1], [2, -1]]
        sage: WS = RootSystem(['D',4,1]).weight_space()
        sage: KRT.module_generator(weight=WS.sum_of_terms([[0,-2],[2,1]]))
        [[1, 1], [2, -1]]
        sage: WSC = RootSystem(['D',4]).weight_space()
        sage: KRT.module_generator(classical_weight=WSC.fundamental_weight(2))
        [[1, 1], [2, -1]]

    We can go between
    :func:`~sage.combinat.crystals.kirillov_reshetikhin.KashiwaraNakashimaTableaux`
    and
    :class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableaux`
    elements::

        sage: KRCrys = crystals.KirillovReshetikhin(['D', 4, 1], 2, 2, model='KN')
        sage: KRTab = crystals.KirillovReshetikhin(['D', 4, 1], 2, 2, model='KR')
        sage: elt = KRCrys(3, 2); elt
        [[2], [3]]
        sage: k = KRTab(elt); k
        [[2, 1], [3, -1]]
        sage: KRCrys(k)
        [[2], [3]]

    We check that the classical weights in the classical decompositions
    agree in a few different type::

        sage: KRCrys = crystals.KirillovReshetikhin(['D', 4, 1], 2, 2, model='KN')
        sage: KRTab = crystals.KirillovReshetikhin(['D', 4, 1], 2, 2, model='KR')
        sage: all(t.classical_weight() == KRCrys(t).classical_weight() for t in KRTab)
        True
        sage: KRCrys = crystals.KirillovReshetikhin(['B', 3, 1], 2, 2, model='KN')
        sage: KRTab = crystals.KirillovReshetikhin(['B', 3, 1], 2, 2, model='KR')
        sage: all(t.classical_weight() == KRCrys(t).classical_weight() for t in KRTab)
        True
        sage: KRCrys = crystals.KirillovReshetikhin(['C', 3, 1], 2, 2, model='KN')
        sage: KRTab = crystals.KirillovReshetikhin(['C', 3, 1], 2, 2, model='KR')
        sage: all(t.classical_weight() == KRCrys(t).classical_weight() for t in KRTab)
        True
        sage: KRCrys = crystals.KirillovReshetikhin(['D', 4, 2], 2, 2, model='KN')
        sage: KRTab = crystals.KirillovReshetikhin(['D', 4, 2], 2, 2, model='KR')
        sage: all(t.classical_weight() == KRCrys(t).classical_weight() for t in KRTab)
        True
        sage: KRCrys = crystals.KirillovReshetikhin(['A', 4, 2], 2, 2, model='KN')
        sage: KRTab = crystals.KirillovReshetikhin(['A', 4, 2], 2, 2, model='KR')
        sage: all(t.classical_weight() == KRCrys(t).classical_weight() for t in KRTab)
        True
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type, r, s):
        """
        Normalize the input arguments to ensure unique representation.

        EXAMPLES::

            sage: KRT1 = crystals.KirillovReshetikhin(CartanType(['A',3,1]), 2, 3, model='KR')
            sage: KRT2 = crystals.KirillovReshetikhin(['A',3,1], 2, 3, model='KR')
            sage: KRT1 is KRT2
            True
        """
    letters: Incomplete
    module_generators: Incomplete
    def __init__(self, cartan_type, r, s) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['A', 4, 1], 2, 2, model='KR')
            sage: TestSuite(KRT).run()
            sage: KRT = crystals.KirillovReshetikhin(['D', 4, 1], 2, 2, model='KR')
            sage: TestSuite(KRT).run()  # long time
            sage: KRT = crystals.KirillovReshetikhin(['D', 4, 1], 4, 1, model='KR'); KRT
            Kirillov-Reshetikhin tableaux of type ['D', 4, 1] and shape (4, 1)
            sage: TestSuite(KRT).run()
        """
    def __iter__(self):
        """
        Return the iterator of ``self``.

        EXAMPLES::

            sage: KR = crystals.KirillovReshetikhin(['A', 5, 2], 2, 1, model='KR')
            sage: L = [x for x in KR]
            sage: len(L)
            15
        """
    def module_generator(self, i=None, **options):
        """
        Return the specified module generator.

        INPUT:

        - ``i`` -- the index of the module generator

        We can also get a module generator by using one of the following
        optional arguments:

        - ``shape`` -- the associated shape
        - ``column_shape`` -- the shape given as columns (a column of length
          `k` correspond to a classical weight `\\omega_k`)
        - ``weight`` -- the weight
        - ``classical_weight`` -- the classical weight

        If no arguments are specified, then return the unique module generator
        of classical weight `s \\Lambda_r`.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D', 4, 1], 2, 2, model='KR')
            sage: KRT.module_generator(1)
            [[1, 1], [2, -1]]
            sage: KRT.module_generator(shape=[1,1])
            [[1, 1], [2, -1]]
            sage: KRT.module_generator(column_shape=[2])
            [[1, 1], [2, -1]]
            sage: WS = RootSystem(['D',4,1]).weight_space()
            sage: KRT.module_generator(weight=WS.sum_of_terms([[0,-2],[2,1]]))
            [[1, 1], [2, -1]]
            sage: WSC = RootSystem(['D',4]).weight_space()
            sage: KRT.module_generator(classical_weight=WSC.fundamental_weight(2))
            [[1, 1], [2, -1]]
            sage: KRT.module_generator()
            [[1, 1], [2, 2]]

            sage: KRT = crystals.KirillovReshetikhin(['A', 3, 1], 2, 2, model='KR')
            sage: KRT.module_generator()
            [[1, 1], [2, 2]]
        """
    def from_kirillov_reshetikhin_crystal(self, krc) -> None:
        """
        Construct an element of ``self`` from the Kirillov-Reshetikhin
        crystal element ``krc``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['A', 4, 1], 2, 1, model='KR')
            sage: C = crystals.KirillovReshetikhin(['A',4,1], 2, 1, model='KN')
            sage: krc = C(4,3); krc
            [[3], [4]]
            sage: KRT.from_kirillov_reshetikhin_crystal(krc)
            [[3], [4]]
        """
    def r(self):
        """
        Return the value `r` for this tableaux class which corresponds to the
        number of rows.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['A', 4, 1], 2, 1, model='KR')
            sage: KRT.r()
            2
        """
    def s(self):
        """
        Return the value `s` for this tableaux class which corresponds to the
        number of columns.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['A', 4, 1], 2, 1, model='KR')
            sage: KRT.s()
            1
        """
    @cached_method
    def kirillov_reshetikhin_crystal(self):
        """
        Return the corresponding KR crystal in the
        :func:`Kashiwara-Nakashima model
        <sage.combinat.crystals.kirillov_reshetikhin.KashiwaraNakashimaTableaux>`.

        EXAMPLES::

            sage: crystals.KirillovReshetikhin(['A', 4, 1], 2, 1, model='KR').kirillov_reshetikhin_crystal()
            Kirillov-Reshetikhin crystal of type ['A', 4, 1] with (r,s)=(2,1)
        """
    def classical_decomposition(self):
        """
        Return the classical crystal decomposition of ``self``.

        EXAMPLES::

            sage: crystals.KirillovReshetikhin(['D', 4, 1], 2, 2, model='KR').classical_decomposition()
            The crystal of tableaux of type ['D', 4] and shape(s) [[], [1, 1], [2, 2]]
        """
    def tensor(self, *crystals, **options):
        """
        Return the tensor product of ``self`` with ``crystals``.

        If ``crystals`` is a list of (a tensor product of) KR tableaux, this
        returns a
        :class:`~sage.combinat.rigged_configurations.tensor_product_kr_tableaux.TensorProductOfKirillovReshetikhinTableaux`.

        EXAMPLES::

            sage: K = crystals.KirillovReshetikhin(['A', 3, 1], 2, 2, model='KR')
            sage: TP = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 3, 1], [[1,3],[3,1]])
            sage: K.tensor(TP, K)
            Tensor product of Kirillov-Reshetikhin tableaux of type ['A', 3, 1]
             and factor(s) ((2, 2), (1, 3), (3, 1), (2, 2))

            sage: C = crystals.KirillovReshetikhin(['A',3,1], 3, 1, model='KN')
            sage: K.tensor(K, C)
            Full tensor product of the crystals
             [Kirillov-Reshetikhin tableaux of type ['A', 3, 1] and shape (2, 2),
              Kirillov-Reshetikhin tableaux of type ['A', 3, 1] and shape (2, 2),
              Kirillov-Reshetikhin crystal of type ['A', 3, 1] with (r,s)=(3,1)]
        """

class KRTableauxRectangle(KirillovReshetikhinTableaux):
    """
    Kirillov-Reshetkhin tableaux `B^{r,s}` whose module generator is a single
    `r \\times s` rectangle.

    These are Kirillov-Reshetkhin tableaux `B^{r,s}` of type:

    - `A_n^{(1)}` for all `1 \\leq r \\leq n`,
    - `C_n^{(1)}` when `r = n`.

    TESTS::

        sage: KRT = crystals.KirillovReshetikhin(['A', 3, 1], 2, 2, model='KR')
        sage: TestSuite(KRT).run()
        sage: KRT = crystals.KirillovReshetikhin(['C', 3, 1], 3, 2, model='KR')
        sage: TestSuite(KRT).run() # long time
    """
    def from_kirillov_reshetikhin_crystal(self, krc):
        """
        Construct a
        :class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableauxElement`.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['A', 4, 1], 2, 1, model='KR')
            sage: C = crystals.KirillovReshetikhin(['A',4,1], 2, 1, model='KN')
            sage: krc = C(4,3); krc
            [[3], [4]]
            sage: KRT.from_kirillov_reshetikhin_crystal(krc)
            [[3], [4]]
        """

class KRTableauxTypeVertical(KirillovReshetikhinTableaux):
    """
    Kirillov-Reshetkihn tableaux `B^{r,s}` of type:

    - `D_n^{(1)}` for all `1 \\leq r < n-1`,
    - `B_n^{(1)}` for all `1 \\leq r < n`,
    - `A_{2n-1}^{(2)}` for all `1 \\leq r \\leq n`.

    TESTS::

        sage: KRT = crystals.KirillovReshetikhin(['D', 4, 1], 1, 1, model='KR')
        sage: TestSuite(KRT).run()
        sage: KRT = crystals.KirillovReshetikhin(['B', 3, 1], 2, 2, model='KR')
        sage: TestSuite(KRT).run() # long time
        sage: KRT = crystals.KirillovReshetikhin(['A', 5, 2], 2, 2, model='KR')
        sage: TestSuite(KRT).run() # long time
    """
    def from_kirillov_reshetikhin_crystal(self, krc):
        """
        Construct an element of ``self`` from the Kirillov-Reshetikhin
        crystal element ``krc``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 2, 3, model='KR')
            sage: C = crystals.KirillovReshetikhin(['D',4,1], 2, 3, model='KN')
            sage: krc = C(4,3); krc
            [[3], [4]]
            sage: KRT.from_kirillov_reshetikhin_crystal(krc)
            [[3, -2, 1], [4, -1, 2]]
        """

class KRTableauxTypeHorizonal(KirillovReshetikhinTableaux):
    """
    Kirillov-Reshetikhin tableaux `B^{r,s}` of type:

    - `C_n^{(1)}` for `1 \\leq r < n`,
    - `A_{2n}^{(2)\\dagger}` for `1 \\leq r \\leq n`.

    TESTS::

        sage: KRT = crystals.KirillovReshetikhin(['C', 3, 1], 2, 2, model='KR')
        sage: TestSuite(KRT).run() # long time
        sage: KRT = crystals.KirillovReshetikhin(CartanType(['A', 4, 2]).dual(), 2, 2, model='KR')
        sage: TestSuite(KRT).run()
    """
    def from_kirillov_reshetikhin_crystal(self, krc):
        """
        Construct an element of ``self`` from the Kirillov-Reshetikhin
        crystal element ``krc``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['C',4,1], 2, 3, model='KR')
            sage: C = crystals.KirillovReshetikhin(['C',4,1], 2, 3, model='KN')
            sage: krc = C(4,3); krc
            [[3], [4]]
            sage: KRT.from_kirillov_reshetikhin_crystal(krc)
            [[3, -2, 1], [4, -1, 2]]
        """

class KRTableauxTypeBox(KRTableauxTypeVertical):
    """
    Kirillov-Reshetikhin tableaux `B^{r,s}` of type:

    - `A_{2n}^{(2)}` for all `r \\leq n`,
    - `D_{n+1}^{(2)}` for all `r < n`,
    - `D_4^{(3)}` for `r = 1`.

    TESTS::

        sage: KRT = crystals.KirillovReshetikhin(['A', 4, 2], 2, 2, model='KR')
        sage: TestSuite(KRT).run()
        sage: KRT = crystals.KirillovReshetikhin(['D', 4, 2], 2, 2, model='KR')
        sage: TestSuite(KRT).run() # long time
        sage: KRT = crystals.KirillovReshetikhin(['D', 4, 3], 1, 2, model='KR')
        sage: TestSuite(KRT).run() # long time
    """
class KRTableauxSpin(KRTableauxRectangle):
    """
    Kirillov-Reshetikhin tableaux `B^{r,s}` of type `D_n^{(1)}` with
    `r = n, n-1`.

    TESTS::

        sage: KRT = crystals.KirillovReshetikhin(['D', 4, 1], 3, 2, model='KR')
        sage: TestSuite(KRT).run()
        sage: KRT = crystals.KirillovReshetikhin(['D', 4, 1], 4, 2, model='KR')
        sage: TestSuite(KRT).run()
    """

class KRTableauxBn(KRTableauxTypeHorizonal):
    """
    Kirillov-Reshetkhin tableaux `B^{n,s}` of type `B_n^{(1)}`.

    TESTS::

        sage: KRT = crystals.KirillovReshetikhin(['B', 2, 1], 2, 3, model='KR')
        sage: TestSuite(KRT).run()
    """
    def from_kirillov_reshetikhin_crystal(self, krc):
        """
        Construct an element of ``self`` from the Kirillov-Reshetikhin
        crystal element ``krc``.

        EXAMPLES::

            sage: KR = crystals.KirillovReshetikhin(['B',3,1], 3, 3, model='KR')
            sage: C = crystals.KirillovReshetikhin(['B',3,1], 3, 3, model='KN')
            sage: krc = C.module_generators[1].f_string([3,2,3,1,3,3]); krc
            [++-, [[2], [0], [-3]]]
            sage: KR.from_kirillov_reshetikhin_crystal(krc)
            [[1, 1, 2], [2, 2, -3], [-3, -3, -1]]
        """

class KirillovReshetikhinTableauxElement(TensorProductOfRegularCrystalsElement):
    """
    A Kirillov-Reshetikhin tableau.

    For more information, see
    :class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableaux`
    and
    :class:`~sage.combinat.rigged_configurations.tensor_product_kr_tableaux.TensorProductOfKirillovReshetikhinTableaux`.
    """
    def __init__(self, parent, list, **options) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['A', 4, 1], 2, 1, model='KR')
            sage: elt = KRT(4, 3); elt
            [[3], [4]]
            sage: TestSuite(elt).run()
        """
    def to_kirillov_reshetikhin_crystal(self):
        """
        Construct a
        :func:`~sage.combinat.crystals.kirillov_reshetihkin.KashiwaraNakashimaTableaux`
        element from ``self``.

        We construct the Kirillov-Reshetikhin crystal element as follows:

        1. Determine the shape `\\lambda` of the KR crystal from the weight.
        2. Determine a path `e_{i_1} e_{i_2} \\cdots e_{i_k}` to the highest
           weight.
        3. Apply `f_{i_k} \\cdots f_{i_2} f_{i_1}` to a highest weight KR
           crystal of shape `\\lambda`.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 2, 2, model='KR')
            sage: elt = KRT(3,2,-1,1); elt
            [[2, 1], [3, -1]]
            sage: elt.to_kirillov_reshetikhin_crystal()
            [[2], [3]]

        TESTS:

        Spinor tests::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 4, 3, model='KR')
            sage: KRC = crystals.KirillovReshetikhin(['D',4,1], 4, 3, model='KN')
            sage: elt = KRT(-3,-4,2,1,-3,-4,2,1,-2,-4,3,1); elt
            [[1, 1, 1], [2, 2, 3], [-4, -4, -4], [-3, -3, -2]]
            sage: ret = elt.to_kirillov_reshetikhin_crystal(); ret
            [++--, [[1], [3], [-4], [-3]]]
            sage: test = KRT(ret); test
            [[1, 1, 1], [2, 2, 3], [-4, -4, -4], [-3, -3, -2]]
            sage: test == elt
            True
        """
    @cached_method
    def to_array(self, rows: bool = True):
        """
        Return a 2-dimensional array representation of this
        Kirillov-Reshetikhin element.

        If the output is in rows, then it outputs the top row first (in the
        English convention) from left to right.

        For example: if the reading word is `[2, 1, 4, 3]`, so as a
        `2 \\times 2` tableau::

            1 3
            2 4

        we output ``[[1, 3], [2, 4]]``.

        If the output is in columns, then it outputs the leftmost column first
        with the bottom element first. In other words this parses the reading
        word into its columns.

        Continuing with the previous example, the output would be
        ``[[2, 1], [4, 3]]``.

        INPUT:

        - ``rows`` -- boolean (default: ``True``); set to ``True`` if the
          resulting array is by row, otherwise it is by column

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['A', 4, 1], 2, 2, model='KR')
            sage: elt = KRT(2, 1, 4, 3)
            sage: elt.to_array()
            [[1, 3], [2, 4]]
            sage: elt.to_array(False)
            [[2, 1], [4, 3]]
        """
    @cached_method
    def to_tableau(self):
        """
        Return a :class:`Tableau` object of ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['A', 4, 1], 2, 2, model='KR')
            sage: elt = KRT(2, 1, 4, 3); elt
            [[1, 3], [2, 4]]
            sage: t = elt.to_tableau(); t
            [[1, 3], [2, 4]]
            sage: type(t)
            <class 'sage.combinat.tableau.Tableaux_all_with_category.element_class'>
        """
    def pp(self) -> None:
        """
        Pretty print ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['A', 4, 1], 2, 2, model='KR')
            sage: elt = KRT(2, 1, 4, 3); elt
            [[1, 3], [2, 4]]
            sage: elt.pp()
            1  3
            2  4
        """
    def to_classical_highest_weight(self, index_set=None):
        """
        Return the classical highest weight element corresponding to ``self``.

        INPUT:

        - ``index_set`` -- (default: ``None``) return the highest weight
          with respect to the index set; if ``None`` is passed in, then this
          uses the classical index set

        OUTPUT:

        A pair ``[H, f_str]`` where ``H`` is the highest weight element and
        ``f_str`` is a list of `a_i` of `f_{a_i}` needed to reach ``H``.

        EXAMPLES::

            sage: KRTab = crystals.KirillovReshetikhin(['D',4,1], 2, 2, model='KR')
            sage: elt = KRTab(3,2,-1,1); elt
            [[2, 1], [3, -1]]
            sage: elt.to_classical_highest_weight()
            [[[1, 1], [2, -1]], [1, 2]]
        """
    def weight(self):
        """
        Return the weight of ``self``.

        EXAMPLES::

            sage: KR = crystals.KirillovReshetikhin(['D',4,1], 2, 2, model='KR')
            sage: KR.module_generators[1].weight()
            -2*Lambda[0] + Lambda[2]
        """
    @cached_method
    def classical_weight(self):
        """
        Return the classical weight of ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 2, 2, model='KR')
            sage: elt = KRT(3,2,-1,1); elt
            [[2, 1], [3, -1]]
            sage: elt.classical_weight()
            (0, 1, 1, 0)
        """
    def e(self, i):
        """
        Perform the action of `e_i` on ``self``.

        .. TODO::

            Implement a direct action of `e_0` without moving to KR crystals.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 2, 2, model='KR')
            sage: KRT.module_generators[0].e(0)
            [[-2, 1], [-1, -1]]
        """
    def f(self, i):
        """
        Perform the action of `f_i` on ``self``.

        .. TODO::

            Implement a direct action of `f_0` without moving to KR crystals.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 2, 2, model='KR')
            sage: KRT.module_generators[0].f(0)
            [[1, 1], [2, -1]]
        """
    def epsilon(self, i):
        """
        Compute `\\varepsilon_i` of ``self``.

        .. TODO::

            Implement a direct action of `\\varepsilon_0` without moving to
            KR crystals.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 2, 2, model='KR')
            sage: KRT.module_generators[0].epsilon(0)
            2
        """
    def phi(self, i):
        """
        Compute `\\varphi_i` of ``self``.

        .. TODO::

            Compute `\\varphi_0` without moving to KR crystals.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 2, 2, model='KR')
            sage: KRT.module_generators[0].phi(0)
            2
        """
    def left_split(self):
        """
        Return the image of ``self`` under the left column splitting map.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 2, 3, model='KR')
            sage: mg = KRT.module_generators[1]; mg.pp()
              1 -2  1
              2 -1  2
            sage: ls = mg.left_split(); ls.pp()
              1 (X)  -2  1
              2      -1  2
            sage: ls.parent()
            Tensor product of Kirillov-Reshetikhin tableaux of type ['D', 4, 1] and factor(s) ((2, 1), (2, 2))
        """
    def right_split(self):
        """
        Return the image of ``self`` under the right column splitting map.

        Let `\\ast` denote the :meth:`Lusztig involution<lusztig_involution>`,
        and `\\mathrm{ls}` as the :meth:`left splitting map<left_split>`.
        The right splitting map is defined as
        `\\mathrm{rs} := \\ast \\circ \\mathrm{ls} \\circ \\ast`.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 2, 3, model='KR')
            sage: mg = KRT.module_generators[1]; mg.pp()
              1 -2  1
              2 -1  2
            sage: ls = mg.right_split(); ls.pp()
             -2  1 (X)   1
             -1  2       2
            sage: ls.parent()
            Tensor product of Kirillov-Reshetikhin tableaux of type ['D', 4, 1] and factor(s) ((2, 2), (2, 1))
        """

class KRTableauxSpinElement(KirillovReshetikhinTableauxElement):
    """
    Kirillov-Reshetikhin tableau for spinors.

    Here we are in the embedding `B(\\Lambda_n) \\hookrightarrow
    B(2 \\Lambda_n)`, so `e_i` and `f_i` act by `e_i^2` and `f_i^2`
    respectively for all `i \\neq 0`. We do this so our columns are full
    width (as opposed to half width and/or uses a `\\pm` representation).
    """
    def e(self, i):
        """
        Calculate the action of `e_i` on ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 4, 1, model='KR')
            sage: KRT(-1, -4, 3, 2).e(1)
            [[1], [3], [-4], [-2]]
            sage: KRT(-1, -4, 3, 2).e(3)
        """
    def f(self, i):
        """
        Calculate the action of `f_i` on ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 4, 1, model='KR')
            sage: KRT(-1, -4, 3, 2).f(1)
            sage: KRT(-1, -4, 3, 2).f(3)
            [[2], [4], [-3], [-1]]
        """
    def epsilon(self, i):
        """
        Compute `\\varepsilon_i` of ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 4, 1, model='KR')
            sage: KRT(-1, -4, 3, 2).epsilon(1)
            1
            sage: KRT(-1, -4, 3, 2).epsilon(3)
            0
        """
    def phi(self, i):
        """
        Compute `\\varphi_i` of ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,1], 4, 1, model='KR')
            sage: KRT(-1, -4, 3, 2).phi(1)
            0
            sage: KRT(-1, -4, 3, 2).phi(3)
            1
        """
    @cached_method
    def to_array(self, rows: bool = True):
        """
        Return a 2-dimensional array representation of this
        Kirillov-Reshetikhin element.

        If the output is in rows, then it outputs the top row first (in the
        English convention) from left to right.

        For example: if the reading word is `[2, 1, 4, 3]`, so as a
        `2 \\times 2` tableau::

            1 3
            2 4

        we output ``[[1, 3], [2, 4]]``.

        If the output is in columns, then it outputs the leftmost column first
        with the bottom element first. In other words this parses the reading
        word into its columns.

        Continuing with the previous example, the output would be
        ``[[2, 1], [4, 3]]``.

        INPUT:

        - ``rows`` -- boolean (default: ``True``); set to ``True`` if the
          resulting array is by row, otherwise it is by column

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D', 4, 1], 4, 3, model='KR')
            sage: elt = KRT(-3,-4,2,1,-3,-4,2,1,-2,-4,3,1)
            sage: elt.to_array()
            [[1, 1, 1], [2, 2, 3], [-4, -4, -4], [-3, -3, -2]]
            sage: elt.to_array(False)
            [[-3, -4, 2, 1], [-3, -4, 2, 1], [-2, -4, 3, 1]]
        """
    def left_split(self):
        """
        Return the image of ``self`` under the left column splitting map.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D', 4, 1], 4, 3, model='KR')
            sage: elt = KRT(-3,-4,2,1,-3,-4,2,1,-2,-4,3,1); elt.pp()
              1  1  1
              2  2  3
             -4 -4 -4
             -3 -3 -2
            sage: elt.left_split().pp()
              1 (X)   1  1
              2       2  3
             -4      -4 -4
             -3      -3 -2
        """
    @cached_method
    def classical_weight(self):
        """
        Return the classical weight of ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D', 4, 1], 4, 1, model='KR')
            sage: KRT.module_generators[0].classical_weight()
            (1/2, 1/2, 1/2, 1/2)
        """

class KRTableauxDTwistedSpin(KRTableauxRectangle):
    """
    Kirillov-Reshetikhin tableaux `B^{r,s}` of type `D_n^{(2)}` with `r = n`.

    EXAMPLES::

        sage: KRT = crystals.KirillovReshetikhin(['D', 4, 2], 1, 1, model='KR')
        sage: KRT.cardinality()
        8
        sage: KRC = crystals.KirillovReshetikhin(['D', 4, 2], 1, 1, model='KN')
        sage: KRT.cardinality() == KRC.cardinality()
        True
    """
    Element = KRTableauxSpinElement

class KRTableauxTypeFromRCElement(KirillovReshetikhinTableauxElement):
    """
    A Kirillov-Reshetikhin tableau constructed from rigged configurations
    under the bijection `\\Phi`.
    """
    def e(self, i):
        """
        Perform the action of `e_i` on ``self``.

        .. TODO::

            Implement a direct action of `e_0` without moving to
            rigged configurations.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,3], 2, 1, model='KR')
            sage: KRT.module_generators[0].e(0)
            [[2], [E]]
        """
    def f(self, i):
        """
        Perform the action of `f_i` on ``self``.

        .. TODO::

            Implement a direct action of `f_0` without moving to
            rigged configurations.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,3], 2, 1, model='KR')
            sage: KRT.module_generators[0].f(0)
            sage: KRT.module_generators[3].f(0)
            [[1], [0]]
        """
    def epsilon(self, i):
        """
        Compute `\\varepsilon_i` of ``self``.

        .. TODO::

            Implement a direct action of `\\epsilon_0` without moving to
            KR crystals.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,3], 2, 2, model='KR')
            sage: KRT.module_generators[0].epsilon(0)
            6
        """
    def phi(self, i):
        """
        Compute `\\varphi_i` of ``self``.

        .. TODO::

            Compute `\\phi_0` without moving to KR crystals.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,3], 2, 2, model='KR')
            sage: KRT.module_generators[0].phi(0)
            0
        """

class KRTableauxTypeFromRC(KirillovReshetikhinTableaux):
    """
    Kirillov-Reshetikhin tableaux `B^{r,s}` constructed from rigged
    configurations under the bijection `\\Phi`.

    .. WARNING::

        The Kashiwara-Nakashima version is not implemented due to the
        non-trivial multiplicities of classical components, so
        :meth:`classical_decomposition` does not work.
    """
    letters: Incomplete
    def __init__(self, cartan_type, r, s) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D', 4, 3], 2, 1, model='KR')
            sage: TestSuite(KRT).run() # long time
        """
    @lazy_attribute
    def module_generators(self):
        """
        The module generators of ``self``.

        EXAMPLES::

            sage: KRT = crystals.KirillovReshetikhin(['D',4,3], 2, 1, model='KR')
            sage: KRT.module_generators
            ([[1], [2]], [[1], [0]], [[1], [E]], [[E], [E]])
        """
    Element = KRTableauxTypeFromRCElement
