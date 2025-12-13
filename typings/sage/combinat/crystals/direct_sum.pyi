from _typeshed import Incomplete
from sage.categories.category import Category as Category
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets as DisjointUnionEnumeratedSets
from sage.sets.family import Family as Family
from sage.structure.element import get_coercion_model as get_coercion_model
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper

class DirectSumOfCrystals(DisjointUnionEnumeratedSets):
    """
    Direct sum of crystals.

    Given a list of crystals `B_0, \\ldots, B_k` of the same Cartan type,
    one can form the direct sum `B_0 \\oplus \\cdots \\oplus B_k`.

    INPUT:

    - ``crystals`` -- list of crystals of the same Cartan type
    - ``keepkey`` -- boolean

    The option ``keepkey`` is by default set to ``False``, assuming
    that the crystals are all distinct. In this case the elements of
    the direct sum are just represented by the elements in the
    crystals `B_i`.  If the crystals are not all distinct, one should
    set the ``keepkey`` option to ``True``.  In this case, the
    elements of the direct sum are represented as tuples `(i, b)`
    where `b \\in B_i`.

    EXAMPLES::

        sage: C = crystals.Letters(['A',2])
        sage: C1 = crystals.Tableaux(['A',2],shape=[1,1])
        sage: B = crystals.DirectSum([C,C1])
        sage: B.list()
        [1, 2, 3, [[1], [2]], [[1], [3]], [[2], [3]]]
        sage: [b.f(1) for b in B]
        [2, None, None, None, [[2], [3]], None]
        sage: B.module_generators
        (1, [[1], [2]])

    ::

        sage: B = crystals.DirectSum([C,C], keepkey=True)
        sage: B.list()
        [(0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3)]
        sage: B.module_generators
        ((0, 1), (1, 1))
        sage: b = B( tuple([0,C(1)]) )
        sage: b
        (0, 1)
        sage: b.weight()
        (1, 0, 0)

    The following is required, because
    :class:`~sage.combinat.crystals.direct_sum.DirectSumOfCrystals`
    takes the same arguments as :class:`DisjointUnionEnumeratedSets`
    (which see for details).

    TESTS::

        sage: C = crystals.Letters(['A',2])
        sage: B = crystals.DirectSum([C,C], keepkey=True)
        sage: B
        Direct sum of the crystals Family (The crystal of letters for type ['A', 2], The crystal of letters for type ['A', 2])

        sage: TestSuite(C).run()
    """
    @staticmethod
    def __classcall_private__(cls, crystals, facade: bool = True, keepkey: bool = False, category=None):
        """
        Normalization of arguments; see :class:`UniqueRepresentation`.

        TESTS:

        We check that direct sum of crystals have unique representation::

            sage: B = crystals.Tableaux(['A',2], shape=[2,1])
            sage: C = crystals.Letters(['A',2])
            sage: D1 = crystals.DirectSum([B, C])
            sage: D2 = crystals.DirectSum((B, C))
            sage: D1 is D2
            True
            sage: D3 = crystals.DirectSum([B, C, C])
            sage: D4 = crystals.DirectSum([D1, C])
            sage: D3 is D4
            True
        """
    crystals: Incomplete
    module_generators: Incomplete
    def __init__(self, crystals, facade, keepkey, category, **options) -> None:
        """
        TESTS::

            sage: C = crystals.Letters(['A',2])
            sage: B = crystals.DirectSum([C,C], keepkey=True)
            sage: B
            Direct sum of the crystals Family (The crystal of letters for type ['A', 2], The crystal of letters for type ['A', 2])
            sage: B.cartan_type()
            ['A', 2]

            sage: from sage.combinat.crystals.direct_sum import DirectSumOfCrystals
            sage: isinstance(B, DirectSumOfCrystals)
            True
        """
    def weight_lattice_realization(self):
        """
        Return the weight lattice realization used to express weights.

        The weight lattice realization is the common parent which all
        weight lattice realizations of the crystals of ``self`` coerce
        into.

        EXAMPLES::

            sage: LaZ = RootSystem(['A',2,1]).weight_lattice(extended=True).fundamental_weights()
            sage: LaQ = RootSystem(['A',2,1]).weight_space(extended=True).fundamental_weights()
            sage: B = crystals.LSPaths(LaQ[1])
            sage: B.weight_lattice_realization()
            Extended weight space over the Rational Field of the Root system of type ['A', 2, 1]
            sage: C = crystals.AlcovePaths(LaZ[1])
            sage: C.weight_lattice_realization()
            Extended weight lattice of the Root system of type ['A', 2, 1]
            sage: D = crystals.DirectSum([B,C])
            sage: D.weight_lattice_realization()
            Extended weight space over the Rational Field of the Root system of type ['A', 2, 1]
        """
    class Element(ElementWrapper):
        """
        A class for elements of direct sums of crystals.
        """
        def e(self, i):
            """
            Return the action of `e_i` on ``self``.

            EXAMPLES::

                sage: C = crystals.Letters(['A',2])
                sage: B = crystals.DirectSum([C,C], keepkey=True)
                sage: [[b, b.e(2)] for b in B]
                [[(0, 1), None], [(0, 2), None], [(0, 3), (0, 2)], [(1, 1), None], [(1, 2), None], [(1, 3), (1, 2)]]
            """
        def f(self, i):
            """
            Return the action of `f_i` on ``self``.

            EXAMPLES::

                sage: C = crystals.Letters(['A',2])
                sage: B = crystals.DirectSum([C,C], keepkey=True)
                sage: [[b,b.f(1)] for b in B]
                [[(0, 1), (0, 2)], [(0, 2), None], [(0, 3), None], [(1, 1), (1, 2)], [(1, 2), None], [(1, 3), None]]
            """
        def weight(self):
            """
            Return the weight of ``self``.

            EXAMPLES::

                sage: C = crystals.Letters(['A',2])
                sage: B = crystals.DirectSum([C,C], keepkey=True)
                sage: b = B( tuple([0,C(2)]) )
                sage: b
                (0, 2)
                sage: b.weight()
                (0, 1, 0)
            """
        def phi(self, i):
            """
            EXAMPLES::

                sage: C = crystals.Letters(['A',2])
                sage: B = crystals.DirectSum([C,C], keepkey=True)
                sage: b = B( tuple([0,C(2)]) )
                sage: b.phi(2)
                1
            """
        def epsilon(self, i):
            """
            EXAMPLES::

                sage: C = crystals.Letters(['A',2])
                sage: B = crystals.DirectSum([C,C], keepkey=True)
                sage: b = B( tuple([0,C(2)]) )
                sage: b.epsilon(2)
                0
            """
