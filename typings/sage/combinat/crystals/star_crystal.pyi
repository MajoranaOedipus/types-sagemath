from _typeshed import Incomplete
from sage.categories.highest_weight_crystals import HighestWeightCrystals as HighestWeightCrystals
from sage.combinat.crystals.elementary_crystals import ElementaryCrystal as ElementaryCrystal
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class StarCrystal(UniqueRepresentation, Parent):
    """
    The star-crystal or `*`-crystal version of a highest weight crystal.

    The `*`-crystal structure on `B(\\infty)` is the structure induced by
    the algebra antiautomorphism `* \\colon U_q(\\mathfrak{g}) \\longrightarrow
    U_q(\\mathfrak{g})` that stabilizes the negative half `U_q^-(\\mathfrak{g})`.
    It is defined by

    .. MATH::

        E_i^* = E_i , \\ \\ \\\n        F_i^* = F_i , \\ \\ \\\n        q^* = q, \\ \\ \\\n        (q^h)^* = q^{-h},

    where `E_i` and `F_i` are the Chevalley generators of `U_q(\\mathfrak{g})`
    and `h` is an element of the Cartan subalgebra.

    The induced operation on the crystal `B(\\infty)` is called the
    *Kashiwara involution*.  Its implementation here is based on the
    recursive algorithm from Theorem 2.2.1 of [Ka1993]_, which states
    that for any `i \\in I` there is a unique strict crystal embedding

    .. MATH::

        \\Psi_i\\colon B(\\infty) \\longrightarrow B_i \\otimes B(\\infty)

    such that

    - `u_{\\infty} \\mapsto b_i(0) \\otimes u_{\\infty}`, where `u_{\\infty}`
      is the highest weight vector in `B(\\infty)`;

    - if `\\Psi_i(b) = f_i^mb_i(0) \\otimes b_0`, then
      `\\Psi_i(f_i^*b) = f_i^{m+1}b_i(0) \\otimes b_0`
      and `\\varepsilon_i(b^*) = m`;

    - the image of `\\Psi_i` is `\\{f_i^mb_i(0)\\otimes b :
      \\varepsilon_i(b^*) = 0, \\ m\\ge 0\\}`.

    Here, `B_i` is the `i`-th elementary crystal.  See
    :class:`~sage.combinat.crystals.elementary_crystals.ElementaryCrystal`
    for more information.

    INPUT:

    - ``Binf`` -- a crystal from
      :class:`~sage.combinat.crystals.catalog_infinity_crystals`

    EXAMPLES::

        sage: B = crystals.infinity.Tableaux(['A',2])
        sage: Bstar = crystals.infinity.Star(B)
        sage: mg = Bstar.highest_weight_vector()
        sage: mg
        [[1, 1], [2]]
        sage: mg.f_string([1,2,1,2,2])
        [[1, 1, 1, 1, 1, 2, 2], [2, 3, 3, 3]]
    """
    module_generators: Incomplete
    def __init__(self, Binf) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: B = crystals.infinity.Tableaux(['A',2])
            sage: Bstar = crystals.infinity.Star(B)
            sage: TestSuite(Bstar).run(max_runs=40)
            sage: TestSuite(Bstar).run(max_runs=1000) # long time
        """
    class Element(ElementWrapper):
        def e(self, i):
            """
            Return the action of `e_i^*` on ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: RC = crystals.infinity.RiggedConfigurations(['E',6,1])
                sage: RCstar = crystals.infinity.Star(RC)
                sage: nuJ = RCstar.module_generators[0].f_string([0,4,6,1,2])
                sage: ascii_art(nuJ.e(1))
                -1[ ]-1   (/)   0[ ]1   (/)   -1[ ]-1   (/)   -2[ ]-1

                sage: M = crystals.infinity.NakajimaMonomials(['B',2,1])
                sage: Mstar = crystals.infinity.Star(M)
                sage: m = Mstar.module_generators[0].f_string([0,1,2,2,1,0])
                sage: m.e(1)
                Y(0,0)^-1 Y(0,2)^-1 Y(1,1) Y(1,2)^-1 Y(2,1)^2
            """
        def f(self, i):
            '''
            Return the action of `f_i^*` on ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: T = crystals.infinity.Tableaux("G2")
                sage: Tstar = crystals.infinity.Star(T)
                sage: t = Tstar.module_generators[0].f_string([1,2,1,1,2])
                sage: t
                [[1, 1, 1, 2, 0], [2, 3]]

                sage: M = crystals.infinity.NakajimaMonomials([\'B\',2,1])
                sage: Mstar = crystals.infinity.Star(M)
                sage: m = Mstar.module_generators[0].f_string([0,1,2,2,1,0])
                sage: m
                Y(0,0)^-1 Y(0,2)^-1 Y(1,0)^-1 Y(1,2)^-1 Y(2,0)^2 Y(2,1)^2
            '''
        def weight(self):
            """
            Return the weight of ``self``.

            EXAMPLES::

                sage: RC = crystals.infinity.RiggedConfigurations(['E',6,1])
                sage: RCstar = crystals.infinity.Star(RC)
                sage: nuJ = RCstar.module_generators[0].f_string([0,4,6,1,2])
                sage: nuJ.weight()
                -Lambda[0] - 2*Lambda[1] + 2*Lambda[3] - Lambda[4]
                 + 2*Lambda[5] - 2*Lambda[6] - delta
            """
        def epsilon(self, i):
            """
            Return `\\varepsilon_i^*` of ``self``.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: Y = crystals.infinity.GeneralizedYoungWalls(3)
                sage: Ystar = crystals.infinity.Star(Y)
                sage: y = Ystar.module_generators[0].f_string([0,1,3,2,1,0])
                sage: [y.epsilon(i) for i in y.index_set()]
                [1, 0, 1, 0]

                sage: RC = crystals.infinity.RiggedConfigurations(['E',6,1])
                sage: RCstar = crystals.infinity.Star(RC)
                sage: nuJ = RCstar.module_generators[0].f_string([0,4,6,1,2])
                sage: [nuJ.epsilon(i) for i in nuJ.index_set()]
                [0, 1, 1, 0, 0, 0, 1]
            """
        def phi(self, i):
            '''
            Return `\\varphi_i^*` of ``self``.

            For `b \\in B(\\infty)`,

            .. MATH::

                \\varphi_i^*(b) = \\varepsilon_i^*(b) + \\langle h_i,
                \\mathrm{wt}(b) \\rangle,

            where `h_i` is a simple coroot.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: T = crystals.infinity.Tableaux("A2")
                sage: Tstar = crystals.infinity.Star(T)
                sage: t = Tstar.module_generators[0].f_string([1,2,1,1,2])
                sage: [t.phi(i) for i in t.index_set()]
                [-3, 1]

                sage: M = crystals.infinity.NakajimaMonomials([\'B\',2,1])
                sage: Mstar = crystals.infinity.Star(M)
                sage: m = Mstar.module_generators[0].f_string([0,1,2,2,1,0])
                sage: [m.phi(i) for i in m.index_set()]
                [-1, -1, 4]
            '''
        def jump(self, i):
            '''
            Return the `i`-jump of ``self``.

            For `b \\in B(\\infty)`,

            .. MATH::

                \\operatorname{jump}_i(b) = \\varepsilon_i(b) + \\varepsilon_i^*(b)
                + \\langle h_i, \\mathrm{wt}(b) \\rangle,

            where `h_i` is a simple coroot.

            INPUT:

            - ``i`` -- an element of the index set

            EXAMPLES::

                sage: RC = crystals.infinity.RiggedConfigurations("D4")
                sage: RCstar = crystals.infinity.Star(RC)
                sage: nu0star = RCstar.module_generators[0]
                sage: nustar = nu0star.f_string([2,1,3,4,2])
                sage: [nustar.jump(i) for i in RC.index_set()]
                [0, 1, 0, 0]
                sage: nustar = nu0star.f_string([2,1,3,4,2,2,1,3,2]) # long time
                sage: [nustar.jump(i) for i in RC.index_set()] # long time
                [1, 0, 1, 2]
            '''
