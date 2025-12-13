from _typeshed import Incomplete
from sage.combinat.crystals.letters import CrystalOfLetters as CrystalOfLetters
from sage.combinat.crystals.tensor_product import FullTensorProductOfRegularCrystals as FullTensorProductOfRegularCrystals
from sage.combinat.rigged_configurations.kr_tableaux import KirillovReshetikhinTableaux as KirillovReshetikhinTableaux, KirillovReshetikhinTableauxElement as KirillovReshetikhinTableauxElement
from sage.combinat.rigged_configurations.tensor_product_kr_tableaux_element import TensorProductOfKirillovReshetikhinTableauxElement as TensorProductOfKirillovReshetikhinTableauxElement
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer import Integer as Integer
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class HighestWeightTensorKRT(UniqueRepresentation):
    """
    Class so we do not have to build the module generators for
    :class:`~sage.combinat.rigged_configurations.tensor_product_kr_tableaux.TensorProductOfKirillovReshetikhinTableaux`
    at initialization.

    .. WARNING::

        This class is for internal use only!
    """
    tp_krt: Incomplete
    def __init__(self, tp_krt) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D',4,1], [[2,2]])
            sage: from sage.combinat.rigged_configurations.tensor_product_kr_tableaux import HighestWeightTensorKRT
            sage: hw = HighestWeightTensorKRT(KRT)
            sage: hw2 = HighestWeightTensorKRT(KRT)
            sage: hw is hw2
            True
        """
    def __getitem__(self, i):
        """
        Return the `i`-th highest weight element in the cache.

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[3,1], [2,1]])
            sage: KRT.module_generators[0]
            [[1], [2], [3]] (X) [[1], [2]]
        """
    def __iter__(self):
        """
        Iterate over the highest weight elements.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D',4,1], [[2,1]])
            sage: from sage.combinat.rigged_configurations.tensor_product_kr_tableaux import HighestWeightTensorKRT
            sage: for x in HighestWeightTensorKRT(KRT): x
            [[1], [2]]
            [[1], [-1]]
        """
    @cached_method
    def cardinality(self):
        """
        Return the cardinality of ``self``, which is the number of
        highest weight elements.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D',4,1], [[2,2]])
            sage: from sage.combinat.rigged_configurations.tensor_product_kr_tableaux import HighestWeightTensorKRT
            sage: HW = HighestWeightTensorKRT(KRT)
            sage: HW.cardinality()
            3
            sage: len(HW)
            3
            sage: len(KRT.module_generators)
            3
        """
    __len__ = cardinality

class TensorProductOfKirillovReshetikhinTableaux(FullTensorProductOfRegularCrystals):
    """
    A tensor product of
    :class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableaux`.

    Through the bijection with rigged configurations, the tableaux that are
    produced in all nonexceptional types are all of rectangular shapes and do
    not necessarily obey the usual strict increase in columns and weak
    increase in rows. The relation between the elements of the
    Kirillov-Reshetikhin crystal, given by the Kashiwara-Nakashima tableaux,
    and the Kirillov-Reshetikhin tableaux is given by a filling map.

    .. NOTE::

        The tableaux for all non-simply-laced types are provably correct if the
        bijection with :class:`rigged configurations
        <sage.combinat.rigged_configurations.rigged_configurations.RiggedConfigurations>`
        holds. Therefore this is currently only proven for `B^{r,1}` or
        `B^{1,s}` and in general for types `A_n^{(1)}` and `D_n^{(1)}`.

    For more information see [OSS2011]_ and
    :class:`~sage.combinat.rigged_configurations.kr_tableaux.KirillovReshetikhinTableaux`.

    For more information on KR crystals, see
    :mod:`sage.combinat.crystals.kirillov_reshetikhin`.

    INPUT:

    - ``cartan_type`` -- a Cartan type

    - ``B`` -- an (ordered) list of pairs `(r,s)` which give the dimension
      of a rectangle with `r` rows and `s` columns and corresponds to a
      Kirillov-Reshetikhin tableaux factor of `B^{r,s}`.

    REFERENCES:

    .. [OSS2011] Masato Okado, Reiho Sakamoto, Anne Schilling,
       Affine crystal structure on rigged configurations of type `D_n^{(1)}`,
       J. Algebraic Combinatorics 37(3) (2013) 571-599 (:arxiv:`1109.3523` [math.QA])

    EXAMPLES:

    We can go between tensor products of KR crystals and rigged
    configurations::

        sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[3,1],[2,2]])
        sage: tp_krt = KRT(pathlist=[[3,2,1],[3,2,3,2]]); tp_krt
        [[1], [2], [3]] (X) [[2, 2], [3, 3]]
        sage: RC = RiggedConfigurations(['A',3,1], [[3,1],[2,2]])
        sage: rc_elt = tp_krt.to_rigged_configuration(); rc_elt
        <BLANKLINE>
        -2[ ][ ]-2
        <BLANKLINE>
        0[ ][ ]0
        <BLANKLINE>
        (/)
        <BLANKLINE>
        sage: tp_krc = tp_krt.to_tensor_product_of_kirillov_reshetikhin_crystals(); tp_krc
        [[[1], [2], [3]], [[2, 2], [3, 3]]]
        sage: KRT(tp_krc) == tp_krt
        True
        sage: rc_elt == tp_krt.to_rigged_configuration()
        True
        sage: KR1 = crystals.KirillovReshetikhin(['A',3,1], 3,1)
        sage: KR2 = crystals.KirillovReshetikhin(['A',3,1], 2,2)
        sage: T = crystals.TensorProduct(KR1, KR2)
        sage: t = T(KR1(3,2,1), KR2(3,2,3,2))
        sage: KRT(t) == tp_krt
        True
        sage: t == tp_krc
        True

    We can get the highest weight elements by using the attribute
    ``module_generators``::

        sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[3,1], [2,1]])
        sage: list(KRT.module_generators)
        [[[1], [2], [3]] (X) [[1], [2]], [[1], [3], [4]] (X) [[1], [2]]]

    To create elements directly (i.e. not passing in KR tableaux elements),
    there is the **pathlist** option will receive a list of lists which
    contain the reversed far-eastern reading word of the tableau. That is to
    say, in English notation, the word obtain from reading bottom-to-top,
    left-to-right. ::

        sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[3,2], [1,2], [2,1]])
        sage: elt = KRT(pathlist=[[3, 2, 1, 4, 2, 1], [1, 3], [3, 1]])
        sage: elt.pp()
          1  1 (X)   1  3 (X)   1
          2  2                  3
          3  4

    One can still create elements in the same way as tensor product of
    crystals::

        sage: K1 = crystals.KirillovReshetikhin(['A',3,1], 3, 2, model='KR')
        sage: K2 = crystals.KirillovReshetikhin(['A',3,1], 1, 2, model='KR')
        sage: K3 = crystals.KirillovReshetikhin(['A',3,1], 2, 1, model='KR')
        sage: eltlong = KRT(K1(3, 2, 1, 4, 2, 1), K2(1, 3), K3(3, 1))
        sage: eltlong == elt
        True
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type, B):
        """
        Normalize the input arguments to ensure unique representation.

        EXAMPLES::

            sage: T1 = crystals.TensorProductOfKirillovReshetikhinTableaux(CartanType(['A',3,1]), [[2,2]])
            sage: T2 = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [(2,2)])
            sage: T3 = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], ((2,2),))
            sage: T2 is T1, T3 is T1
            (True, True)
        """
    dims: Incomplete
    letters: Incomplete
    module_generators: Incomplete
    def __init__(self, cartan_type, B) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[3,1],[2,2]]); KRT
            Tensor product of Kirillov-Reshetikhin tableaux of type ['A', 3, 1] and factor(s) ((3, 1), (2, 2))
            sage: TestSuite(KRT).run() # long time
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D',4,1], [[2,2]])
            sage: TestSuite(KRT).run() # long time
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D',4,1], [[3,1]])
            sage: TestSuite(KRT).run() # long time
            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D',4,1], [[4,3]])
            sage: TestSuite(KRT).run() # long time
        """
    def __iter__(self):
        """
        Return the iterator of ``self``.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 3, 1], [[2,1], [1,1]])
            sage: g = KRT.__iter__()
            sage: next(g)         # random
            [[2], [3]] (X) [[1]]
            sage: next(g)         # random
            [[2], [4]] (X) [[1]]
        """
    @cached_method
    def rigged_configurations(self):
        """
        Return the corresponding set of rigged configurations.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[1,3], [2,1]])
            sage: KRT.rigged_configurations()
            Rigged configurations of type ['A', 3, 1] and factor(s) ((1, 3), (2, 1))
        """
    @cached_method
    def tensor_product_of_kirillov_reshetikhin_crystals(self):
        """
        Return the corresponding tensor product of Kirillov-Reshetikhin
        crystals.

        EXAMPLES::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['A',3,1], [[3,1],[2,2]])
            sage: KRT.tensor_product_of_kirillov_reshetikhin_crystals()
            Full tensor product of the crystals [Kirillov-Reshetikhin crystal of type ['A', 3, 1] with (r,s)=(3,1),
            Kirillov-Reshetikhin crystal of type ['A', 3, 1] with (r,s)=(2,2)]

        TESTS::

            sage: KRT = crystals.TensorProductOfKirillovReshetikhinTableaux(['D', 4, 1], [[4,1], [3,3]])
            sage: KR1 = crystals.KirillovReshetikhin(['D', 4, 1], 4, 1)
            sage: KR2 = crystals.KirillovReshetikhin(['D', 4, 1], 3, 3)
            sage: T = crystals.TensorProduct(KR1, KR2)
            sage: T == KRT.tensor_product_of_kirillov_reshetikhin_crystals()
            True
            sage: T is KRT.tensor_product_of_kirillov_reshetikhin_crystals()
            True
        """
    def tensor(self, *crystals, **options):
        """
        Return the tensor product of ``self`` with ``crystals``.

        If ``crystals`` is a list of (a tensor product of) KR tableaux, this
        returns a :class:`TensorProductOfKirillovReshetikhinTableaux`.

        EXAMPLES::

            sage: TP = crystals.TensorProductOfKirillovReshetikhinTableaux(['A', 3, 1], [[1,3],[3,1]])
            sage: K = crystals.KirillovReshetikhin(['A', 3, 1], 2, 2, model='KR')
            sage: TP.tensor(K, TP)
            Tensor product of Kirillov-Reshetikhin tableaux of type ['A', 3, 1]
             and factor(s) ((1, 3), (3, 1), (2, 2), (1, 3), (3, 1))

            sage: C = crystals.KirillovReshetikhin(['A',3,1], 3, 1, model='KN')
            sage: TP.tensor(K, C)
            Full tensor product of the crystals
             [Kirillov-Reshetikhin tableaux of type ['A', 3, 1] and shape (1, 3),
              Kirillov-Reshetikhin tableaux of type ['A', 3, 1] and shape (3, 1),
              Kirillov-Reshetikhin tableaux of type ['A', 3, 1] and shape (2, 2),
              Kirillov-Reshetikhin crystal of type ['A', 3, 1] with (r,s)=(3,1)]
        """
