from _typeshed import Incomplete
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.categories.regular_crystals import RegularCrystals as RegularCrystals
from sage.rings.infinity import Infinity as Infinity
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class AffinizationOfCrystal(UniqueRepresentation, Parent):
    """
    An affinization of a crystal.

    Let `\\mathfrak{g}` be a Kac-Moody algebra of affine type. The
    affinization of a finite `U_q^{\\prime}(\\mathfrak{g})`-crystal `B`
    is the (infinite) `U_q(\\mathfrak{g})`-crystal with underlying set:

    .. MATH::

        B^{\\mathrm{aff}} = \\{ b(m) \\mid b \\in B, m \\in \\ZZ \\}

    and crystal structure determined by:

    .. MATH::

        \\begin{aligned}
            e_i(b(m)) & =
            \\begin{cases}
              (e_0 b)(m+1) & i = 0, \\\\\n              (e_i b)(m)   & i \\neq 0,
            \\end{cases} \\\\\n            f_i(b(m)) &=
            \\begin{cases}
              (f_0 b)(m-1) & i = 0, \\\\\n              (f_i b)(m)   & i \\neq 0,
            \\end{cases} \\\\\n            \\mathrm{wt}(b(m)) &= \\mathrm{wt}(b) + m \\delta.
        \\end{aligned}

    EXAMPLES:

    We first construct a Kirillov-Reshetikhin crystal and then take it's
    corresponding affinization::

        sage: K = crystals.KirillovReshetikhin(['A',2,1], 2, 2)
        sage: A = K.affinization()

    Next we construct an affinization crystal from a tensor product of KR
    crystals::

        sage: KT = crystals.TensorProductOfKirillovReshetikhinTableaux(['C',2,1], [[1,2],[2,1]])
        sage: A = crystals.AffinizationOf(KT)

    REFERENCES:

    - [HK2002]_ Chapter 10
    """
    module_generators: Incomplete
    def __init__(self, B) -> None:
        """
        Initialize ``self``.

        EXAMPLES:

        We skip the Stembridge axioms test since this is an abstract crystal::

            sage: A = crystals.KirillovReshetikhin(['A',2,1], 2, 2).affinization()
            sage: TestSuite(A).run(skip='_test_stembridge_local_axioms') # long time
        """
    class Element(Element):
        """
        An element in an affinization crystal.
        """
        def __init__(self, parent, b, m) -> None:
            """
            Initialize ``self``.

            EXAMPLES::

                sage: A = crystals.KirillovReshetikhin(['A',2,1], 2, 2).affinization()
                sage: mg = A.module_generators[0]
                sage: TestSuite(mg).run()
            """
        def __hash__(self):
            """
            TESTS::

                sage: A = crystals.KirillovReshetikhin(['A',2,1], 2, 2).affinization()
                sage: mg = A.module_generators[0]
                sage: hash(mg) == hash(mg._b) ^^ hash(mg._m)
                True
            """
        def e(self, i):
            """
            Return the action of `e_i` on ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: A = crystals.KirillovReshetikhin(['A',2,1], 2,2).affinization()
                sage: mg = A.module_generators[0]
                sage: mg.e(0)
                [[1, 2], [2, 3]](1)
                sage: mg.e(1)
                sage: mg.e(0).e(1)
                [[1, 1], [2, 3]](1)
            """
        def f(self, i):
            """
            Return the action of `f_i` on ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: A = crystals.KirillovReshetikhin(['A',2,1], 2,2).affinization()
                sage: mg = A.module_generators[0]
                sage: mg.f(2)
                [[1, 1], [2, 3]](0)
                sage: mg.f(2).f(2).f(0)
                sage: mg.f_string([2,1,1])
                sage: mg.f_string([2,1])
                [[1, 2], [2, 3]](0)
                sage: mg.f_string([2,1,0])
                [[1, 1], [2, 2]](-1)
            """
        def epsilon(self, i):
            """
            Return `\\varepsilon_i` of ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: A = crystals.KirillovReshetikhin(['A',2,1], 2,2).affinization()
                sage: mg = A.module_generators[0]
                sage: mg.epsilon(0)
                2
                sage: mg.epsilon(1)
                0
            """
        def phi(self, i):
            """
            Return `\\varphi_i` of ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: A = crystals.KirillovReshetikhin(['A',2,1], 2,2).affinization()
                sage: mg = A.module_generators[0]
                sage: mg.phi(0)
                0
                sage: mg.phi(2)
                2
            """
        def weight(self):
            """
            Return the weight of ``self``.

            The weight `\\mathrm{wt}` of an element is:

            .. MATH::

                \\mathrm{wt}\\bigl( b(m) \\bigr) = \\mathrm{wt}(b) + m \\delta,

            where `\\delta` is the null root.

            EXAMPLES::

                sage: A = crystals.KirillovReshetikhin(['A',2,1], 2,2).affinization()
                sage: mg = A.module_generators[0]
                sage: mg.weight()
                -2*Lambda[0] + 2*Lambda[2]
                sage: mg.e(0).weight()
                -Lambda[1] + Lambda[2] + delta
                sage: mg.e(0).e(0).weight()
                2*Lambda[0] - 2*Lambda[1] + 2*delta
            """
