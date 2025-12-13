from _typeshed import Incomplete
from sage.categories.algebras import Algebras as Algebras
from sage.categories.cartesian_product import cartesian_product as cartesian_product
from sage.categories.fields import Fields as Fields
from sage.categories.homset import Hom as Hom, HomsetWithBase as HomsetWithBase
from sage.categories.hopf_algebras import HopfAlgebras as HopfAlgebras
from sage.categories.modules import Modules as Modules
from sage.categories.morphism import Morphism as Morphism
from sage.categories.rings import Rings as Rings
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.features.gap import GapPackage as GapPackage
from sage.libs.gap.libgap import libgap as libgap
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.rational_field import QQ as QQ
from sage.sets.family import Family as Family
from sage.sets.non_negative_integers import NonNegativeIntegers as NonNegativeIntegers
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class QuaGroupModuleElement(Element):
    """
    Base class for elements created using QuaGroup.
    """
    def __init__(self, parent, libgap_elt) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['G',2])
            sage: TestSuite(Q.an_element()).run()
        """
    def __reduce__(self):
        """
        Used in pickling.

        EXAMPLES::

            sage: Q = QuantumGroup(['G',2])
            sage: x = Q.an_element()
            sage: loads(dumps(x)) == x
            True
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['B',3])
            sage: x = Q.an_element()
            sage: hash(x) == hash(x.gap())
            True
        """
    def gap(self):
        """
        Return the gap representation of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['B',3])
            sage: x = Q.an_element()
            sage: x.gap()
            1+(q)*F1+E1+(q^4-1-q^-4+q^-8)*[ K1 ; 2 ]+K1+(-q^-2+q^-6)*K1[ K1 ; 1 ]
        """
    def e_tilde(self, i):
        """
        Return the action of the Kashiwara operator
        `\\widetilde{e}_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set or a list to
          perform a string of operators

        EXAMPLES::

            sage: Q = QuantumGroup(['B',2])
            sage: x = Q.one().f_tilde([1,2,1,1,2,2])
            sage: x.e_tilde([2,2,1,2])
            F[a1]^(2)
        """
    def f_tilde(self, i):
        """
        Return the action of the Kashiwara operator
        `\\widetilde{f}_i` on ``self``.

        INPUT:

        - ``i`` -- an element of the index set or a list to
          perform a string of operators

        EXAMPLES::

            sage: Q = QuantumGroup(['B',2])
            sage: Q.one().f_tilde(1)
            F[a1]
            sage: Q.one().f_tilde(2)
            F[a2]
            sage: Q.one().f_tilde([1,2,1,1,2])
            F[a1]*F[a1+a2]^(2)
        """

class QuantumGroup(UniqueRepresentation, Parent):
    """
    A Drinfel'd-Jimbo quantum group (implemented using the optional GAP
    package ``QuaGroup``).

    EXAMPLES:

    We check the quantum Serre relations. We first we import the
    `q`-binomial using the `q`-int for quantum groups::

        sage: from sage.algebras.quantum_groups.q_numbers import q_binomial

    We verify the Serre relations for type `A_2`::

        sage: Q = algebras.QuantumGroup(['A',2])
        sage: F1,F12,F2 = Q.F()
        sage: q = Q.q()
        sage: F1^2*F2 - q_binomial(2,1,q) * F1*F2*F1 + F2*F1^2
        0

    We verify the Serre relations for type `B_2`::

        sage: Q = algebras.QuantumGroup(['B',2])
        sage: F1, F12, F122, F2 = Q.F()
        sage: F1^2*F2 - q_binomial(2,1,q^2) * F1*F2*F1 + F2*F1^2
        0
        sage: (F2^3*F1 - q_binomial(3,1,q) * F2^2*F1*F2
        ....:  + q_binomial(3,2,q) * F2*F1*F2^2 - F1*F2^3)
        0

    REFERENCES:

    - :wikipedia:`Quantum_group`
    """
    @staticmethod
    def __classcall_private__(cls, cartan_type, q=None):
        """
        Initialize ``self``.

        TESTS::

            sage: Q = QuantumGroup(['A',2])
            sage: Q is QuantumGroup('A2', None)
            True
        """
    def __init__(self, cartan_type, q) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: Q = QuantumGroup(['A',2])
            sage: TestSuite(Q).run()            # long time

            sage: Q = QuantumGroup(['G',2])
            sage: TestSuite(Q).run()            # long time
        """
    def gap(self):
        """
        Return the gap representation of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: Q.gap()
            QuantumUEA( <root system of type A2>, Qpar = q )
        """
    def cartan_type(self):
        """
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: Q.cartan_type()
            ['A', 2]
        """
    @cached_method
    def one(self):
        """
        Return the multiplicative identity of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: Q.one()
            1
        """
    @cached_method
    def zero(self):
        """
        Return the multiplicative identity of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: Q.zero()
            0
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: Q.gens()
            (F[a1], F[a1+a2], F[a2],
             K1, (-q + q^-1)*[ K1 ; 1 ] + K1,
             K2, (-q + q^-1)*[ K2 ; 1 ] + K2,
             E[a1], E[a1+a2], E[a2])
        """
    def E(self):
        """
        Return the family of generators `\\{E_{\\alpha}\\}_{\\alpha \\in \\Phi}`,
        where `\\Phi` is the root system of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['B',2])
            sage: list(Q.E())
            [E[a1], E[a1+a2], E[a1+2*a2], E[a2]]
        """
    def E_simple(self):
        """
        Return the family of generators `\\{E_i := E_{\\alpha_i}\\}_{i \\in I}`.

        EXAMPLES::

            sage: Q = QuantumGroup(['B',2])
            sage: Q.E_simple()
            Finite family {1: E[a1], 2: E[a2]}
        """
    def F(self):
        """
        Return the family of generators `\\{F_{\\alpha}\\}_{\\alpha \\in \\Phi}`,
        where `\\Phi` is the root system of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['G',2])
            sage: list(Q.F())
            [F[a1], F[3*a1+a2], F[2*a1+a2], F[3*a1+2*a2], F[a1+a2], F[a2]]
        """
    def F_simple(self):
        """
        Return the family of generators `\\{F_i := F_{\\alpha_i}\\}_{i \\in I}`.

        EXAMPLES::

            sage: Q = QuantumGroup(['G',2])
            sage: Q.F_simple()
            Finite family {1: F[a1], 2: F[a2]}
        """
    def K(self):
        """
        Return the family of generators `\\{K_i\\}_{i \\in I}`.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',3])
            sage: Q.K()
            Finite family {1: K1, 2: K2, 3: K3}
            sage: Q.K_inverse()
            Finite family {1: (-q + q^-1)*[ K1 ; 1 ] + K1,
                           2: (-q + q^-1)*[ K2 ; 1 ] + K2,
                           3: (-q + q^-1)*[ K3 ; 1 ] + K3}
        """
    def K_inverse(self):
        """
        Return the family of generators `\\{K_i^{-1}\\}_{i \\in I}`.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',3])
            sage: Q.K_inverse()
            Finite family {1: (-q + q^-1)*[ K1 ; 1 ] + K1,
                           2: (-q + q^-1)*[ K2 ; 1 ] + K2,
                           3: (-q + q^-1)*[ K3 ; 1 ] + K3}
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: list(Q.algebra_generators())
            [F[a1], F[a2],
             K1, K2,
             (-q + q^-1)*[ K1 ; 1 ] + K1, (-q + q^-1)*[ K2 ; 1 ] + K2,
             E[a1], E[a2]]
        """
    def some_elements(self):
        """
        Return some elements of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',1])
            sage: Q.some_elements()
            [1 + (q)*F[a1] + E[a1] + (q^2-1-q^-2 + q^-4)*[ K1 ; 2 ]
              + K1 + (-q^-1 + q^-3)*K1[ K1 ; 1 ],
             K1, F[a1], E[a1]]
        """
    def q(self):
        """
        Return the parameter `q`.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',3])
            sage: Q.q()
            q
            sage: zeta3 = CyclotomicField(3).gen()
            sage: Q = QuantumGroup(['B',2], q=zeta3)
            sage: Q.q()
            zeta3
        """
    def highest_weight_module(self, weight):
        """
        Return the highest weight module of weight ``weight`` of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: Q.highest_weight_module([1,3])
            Highest weight module of weight Lambda[1] + 3*Lambda[2] of
             Quantum Group of type ['A', 2] with q=q
        """
    def lower_half(self):
        """
        Return the lower half of the quantum group ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: Q.lower_half()
            Lower Half of Quantum Group of type ['A', 2] with q=q
        """
    def coproduct(self, elt, n: int = 1):
        """
        Return the coproduct of ``elt`` (iterated ``n`` times).

        The comultiplication `\\Delta \\colon U_q(\\mathfrak{g}) \\to
        U_q(\\mathfrak{g}) \\otimes U_q(\\mathfrak{g})` is defined by

        .. MATH::

            \\begin{aligned}
            \\Delta(E_i) &= E_i \\otimes 1 + K_i \\otimes E_i, \\\\\n            \\Delta(F_i) &= F_i \\otimes K_i^{-1} + 1 \\otimes F_i, \\\\\n            \\Delta(K_i) &= K_i \\otimes K_i.
            \\end{aligned}

        EXAMPLES::

            sage: Q = QuantumGroup(['B',2])
            sage: [Q.coproduct(e) for e in Q.E()]
            [1*(E[a1]<x>1) + 1*(K1<x>E[a1]),
             1*(E[a1+a2]<x>1) + 1*(K1*K2<x>E[a1+a2]) + q^2-q^-2*(K2*E[a1]<x>E[a2]),
             q^4-q^2-1 + q^-2*(E[a1]<x>E[a2]^(2)) + 1*(E[a1+2*a2]<x>1)
              + 1*(K1<x>E[a1+2*a2]) + q-q^-1*(K1*K2[ K2 ; 1 ]<x>E[a1+2*a2])
              + q-q^-1*(K2*E[a1+a2]<x>E[a2]) + q^5-2*q^3
              + 2*q^-1-q^-3*(K2[ K2 ; 1 ]*E[a1]<x>E[a2]^(2)),
             1*(E[a2]<x>1) + 1*(K2<x>E[a2])]
            sage: [Q.coproduct(f, 2) for f in Q.F_simple()]
            [1*(1<x>1<x>F[a1]) + -q^2 + q^-2*(1<x>F[a1]<x>[ K1 ; 1 ])
              + 1*(1<x>F[a1]<x>K1) + q^4-2 + q^-4*(F[a1]<x>[ K1 ; 1 ]<x>[ K1 ; 1 ])
              + -q^2 + q^-2*(F[a1]<x>[ K1 ; 1 ]<x>K1) + -q^2
              + q^-2*(F[a1]<x>K1<x>[ K1 ; 1 ]) + 1*(F[a1]<x>K1<x>K1),
             1*(1<x>1<x>F[a2]) + -q + q^-1*(1<x>F[a2]<x>[ K2 ; 1 ])
              + 1*(1<x>F[a2]<x>K2) + q^2-2 + q^-2*(F[a2]<x>[ K2 ; 1 ]<x>[ K2 ; 1 ])
              + -q + q^-1*(F[a2]<x>[ K2 ; 1 ]<x>K2) + -q
              + q^-1*(F[a2]<x>K2<x>[ K2 ; 1 ]) + 1*(F[a2]<x>K2<x>K2)]
        """
    def antipode(self, elt):
        """
        Return the antipode of ``elt``.

        The antipode `S \\colon U_q(\\mathfrak{g}) \\to U_q(\\mathfrak{g})`
        is the anti-automorphism defined by

        .. MATH::

            S(E_i) = -K_i^{-1}E_i, \\qquad
            S(F_i) = -F_iK_i, \\qquad
            S(K_i) = K_i^{-1}.

        EXAMPLES::

            sage: Q = QuantumGroup(['B',2])
            sage: [Q.antipode(f) for f in Q.F()]
            [(-1)*F[a1]*K1,
             (-q^6 + q^2)*F[a1]*F[a2]*K1*K2 + (-q^4)*F[a1+a2]*K1*K2,
             (-q^8 + q^6 + q^4-q^2)*F[a1]*F[a2]^(2)*K1
              + (-q^9 + 2*q^7-2*q^3 + q)*F[a1]*F[a2]^(2)*K1*K2[ K2 ; 1 ]
              + (-q^5 + q^3)*F[a1+a2]*F[a2]*K1
              + (-q^6 + 2*q^4-q^2)*F[a1+a2]*F[a2]*K1*K2[ K2 ; 1 ]
              + (-q^4)*F[a1+2*a2]*K1 + (-q^5 + q^3)*F[a1+2*a2]*K1*K2[ K2 ; 1 ],
             (-1)*F[a2]*K2]
        """
    def counit(self, elt):
        """
        Return the counit of ``elt``.

        The counit `\\varepsilon \\colon U_q(\\mathfrak{g}) \\to \\QQ(q)` is
        defined by

        .. MATH::

            \\varepsilon(E_i) = \\varepsilon(F_i) = 0, \\qquad
            \\varepsilon(K_i) = 1.

        EXAMPLES::

            sage: Q = QuantumGroup(['B',2])
            sage: x = Q.an_element()^2
            sage: Q.counit(x)
            4
            sage: Q.counit(Q.one())
            1
            sage: Q.counit(Q.zero())
            0
        """
    class Element(QuaGroupModuleElement):
        def bar(self):
            """
            Return the bar involution on ``self``.

            The bar involution is defined by

            .. MATH::

                \\overline{E_i} = E_i, \\qquad\\qquad
                \\overline{F_i} = F_i, \\qquad\\qquad
                \\overline{K_i} = K_i^{-1}.

            EXAMPLES::

                sage: Q = QuantumGroup(['A',2])
                sage: [gen.bar() for gen in Q.gens()]
                [F[a1],
                 (q-q^-1)*F[a1]*F[a2] + F[a1+a2],
                 F[a2],
                 (-q + q^-1)*[ K1 ; 1 ] + K1, K1,
                 (-q + q^-1)*[ K2 ; 1 ] + K2, K2,
                 E[a1],
                 (-q^2 + 1)*E[a1]*E[a2] + (q^2)*E[a1+a2],
                 E[a2]]
            """
        def omega(self):
            """
            Return the action of the `\\omega` automorphism on ``self``.

            The `\\omega` automorphism is defined by

            .. MATH::

                \\omega(E_i) = F_i, \\qquad\\qquad
                \\omega(F_i) = E_i, \\qquad\\qquad
                \\omega(K_i) = K_i^{-1}.

            EXAMPLES::

                sage: Q = QuantumGroup(['A',2])
                sage: [gen.omega() for gen in Q.gens()]
                [E[a1],
                 (-q)*E[a1+a2],
                 E[a2],
                 (-q + q^-1)*[ K1 ; 1 ] + K1,
                 K1,
                 (-q + q^-1)*[ K2 ; 1 ] + K2,
                 K2,
                 F[a1],
                 (-q^-1)*F[a1+a2],
                 F[a2]]
            """
        def tau(self):
            """
            Return the action of the `\\tau` anti-automorphism on ``self``.

            The `\\tau` anti-automorphism is defined by

            .. MATH::

                \\tau(E_i) = E_i, \\qquad\\qquad
                \\tau(F_i) = F_i, \\qquad\\qquad
                \\tau(K_i) = K_i^{-1}.

            EXAMPLES::

                sage: Q = QuantumGroup(['A',2])
                sage: [gen.tau() for gen in Q.gens()]
                [F[a1],
                 (-q^2 + 1)*F[a1]*F[a2] + (-q)*F[a1+a2],
                 F[a2],
                 (-q + q^-1)*[ K1 ; 1 ] + K1,
                 K1,
                 (-q + q^-1)*[ K2 ; 1 ] + K2,
                 K2,
                 E[a1],
                 (q-q^-1)*E[a1]*E[a2] + (-q)*E[a1+a2],
                 E[a2]]
            """
        def braid_group_action(self, braid):
            """
            Return the action of the braid group element ``braid``.

            The braid group operator `T_i \\colon U_q(\\mathfrak{g}) \\to
            U_q(\\mathfrak{g})` is defined by

            .. MATH::

                \\begin{aligned}
                T_i(E_i) &= -F_iK_i, \\\\\n                T_i(E_j) &= \\sum_{k=0}^{-a_{ij}} (-1)^k q_i^{-k} E_i^{(-a_{ij}-k)} E_j E_i^{(k)} \\text{ if } i \\neq j,\\\\\n                T_i(K_j) &= K_jK_i^{a_{ij}}, \\\\\n                T_i(F_i) &= -K_i^{-1}E_i, \\\\\n                T_i(F_j) &= \\sum_{k=0}^{-a_{ij}} (-1)^k q_i^{-k} F_i^{(k)} F_j F_i^{(-a_{ij}-k)} \\text{ if } i \\neq j,
                \\end{aligned}

            where `a_{ij} = \\langle \\alpha_j, \\alpha_i^\\vee \\rangle` is the
            `(i,j)`-entry of the Cartan matrix associated to `\\mathfrak{g}`.

            INPUT:

            - ``braid`` -- a reduced word of a braid group element

            EXAMPLES::

                sage: Q = QuantumGroup(['A',2])
                sage: F1 = Q.F_simple()[1]
                sage: F1.braid_group_action([1])
                (q-q^-1)*[ K1 ; 1 ]*E[a1] + (-1)*K1*E[a1]
                sage: F1.braid_group_action([1,2])
                F[a2]
                sage: F1.braid_group_action([2,1])
                (-q^3 + 3*q-3*q^-1 + q^-3)*[ K1 ; 1 ]*[ K2 ; 1 ]*E[a1]*E[a2]
                 + (q^3-2*q + q^-1)*[ K1 ; 1 ]*[ K2 ; 1 ]*E[a1+a2]
                 + (q^2-2 + q^-2)*[ K1 ; 1 ]*K2*E[a1]*E[a2]
                 + (-q^2 + 1)*[ K1 ; 1 ]*K2*E[a1+a2]
                 + (q^2-2 + q^-2)*K1*[ K2 ; 1 ]*E[a1]*E[a2]
                 + (-q^2 + 1)*K1*[ K2 ; 1 ]*E[a1+a2]
                 + (-q + q^-1)*K1*K2*E[a1]*E[a2] + (q)*K1*K2*E[a1+a2]
                sage: F1.braid_group_action([1,2,1]) == F1.braid_group_action([2,1,2])
                True
                sage: F1.braid_group_action([]) == F1
                True
            """

class QuantumGroupMorphism(Morphism):
    """
    A morphism whose domain is a quantum group.
    """
    def __init__(self, parent, im_gens, check: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',1])
            sage: F, K, Ki, E = Q.gens()
            sage: phi = Q.hom([E, Ki, K, F])
            sage: TestSuite(phi).run(skip='_test_category')
        """
    def __reduce__(self):
        """
        For pickling.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',1])
            sage: F, K, Ki, E = Q.gens()
            sage: phi = Q.hom([E, Ki, K, F])
            sage: loads(dumps(phi)) == phi
            True
        """
    def __richcmp__(self, other, op):
        """
        Rich comparison of ``self`` and ``other`` by ``op``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',1])
            sage: F, K, Ki, E = Q.gens()
            sage: phi = Q.hom([E, Ki, K, F])
            sage: psi = Q.hom([F, K, Ki, E])
            sage: phi == Q.hom([E, Ki, K, F])
            True
            sage: phi == psi
            False
            sage: psi != Q.hom([F, K, Ki, E])
            False
            sage: phi != psi
            True

            sage: QB = QuantumGroup(['B',3])
            sage: QC = QuantumGroup(['C',3])
            sage: x = ZZ.one()
            sage: phi = QB.hom([x]*len(QB.algebra_generators()))
            sage: psi = QC.hom([x]*len(QC.algebra_generators()))
            sage: phi.im_gens() == psi.im_gens()
            True
            sage: phi == psi
            False
        """
    def im_gens(self):
        """
        Return the image of the generators under ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',1])
            sage: F, K, Ki, E = Q.gens()
            sage: phi = Q.hom([E, Ki, K, F])
            sage: phi.im_gens()
            (E[a1], (-q + q^-1)*[ K1 ; 1 ] + K1, K1, F[a1])
        """

class QuantumGroupHomset(HomsetWithBase):
    """
    The homset whose domain is a quantum group.
    """
    def __call__(self, im_gens, check: bool = True):
        """
        Construct an element of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',1])
            sage: H = Hom(Q, Q)
            sage: F, K, Ki, E = Q.gens()
            sage: phi = H([E, Ki, K, F]); phi
            Quantum group homomorphism endomorphism of Quantum Group of type ['A', 1] with q=q
              Defn: F[a1] |--> E[a1]
                    K1 |--> (-q + q^-1)*[ K1 ; 1 ] + K1
                    (-q + q^-1)*[ K1 ; 1 ] + K1 |--> K1
                    E[a1] |--> F[a1]
            sage: H(phi) == phi
            True
            sage: H2 = Hom(Q, Q, Modules(Fields()))
            sage: H == H2
            False
            sage: H2(phi)
            Quantum group homomorphism endomorphism of Quantum Group of type ['A', 1] with q=q
              Defn: F[a1] |--> E[a1]
                    K1 |--> (-q + q^-1)*[ K1 ; 1 ] + K1
                    (-q + q^-1)*[ K1 ; 1 ] + K1 |--> K1
                    E[a1] |--> F[a1]
        """

def projection_lower_half(Q):
    """
    Return the projection onto the lower half of the quantum group.

    EXAMPLES::

        sage: from sage.algebras.quantum_groups.quantum_group_gap import projection_lower_half
        sage: Q = QuantumGroup(['G',2])
        sage: phi = projection_lower_half(Q); phi
        Quantum group homomorphism endomorphism of Quantum Group of type ['G', 2] with q=q
          Defn: F[a1] |--> F[a1]
                F[a2] |--> F[a2]
                K1 |--> 0
                K2 |--> 0
                (-q + q^-1)*[ K1 ; 1 ] + K1 |--> 0
                (-q^3 + q^-3)*[ K2 ; 1 ] + K2 |--> 0
                E[a1] |--> 0
                E[a2] |--> 0
        sage: all(phi(f) == f for f in Q.F())
        True
        sage: all(phi(e) == Q.zero() for e in Q.E())
        True
        sage: all(phi(K) == Q.zero() for K in Q.K())
        True
    """

class QuaGroupRepresentationElement(QuaGroupModuleElement):
    """
    Element of a quantum group representation.
    """
    def __reduce__(self):
        """
        Used in pickling.

        EXAMPLES::

            sage: Q = QuantumGroup(['B',2])
            sage: F1, F2 = Q.F_simple()
            sage: q = Q.q()
            sage: V = Q.highest_weight_module([2,1])
            sage: v = V.highest_weight_vector()
            sage: x = (2 - q) * v + F1*v + q*F2*F1*v
            sage: loads(dumps(x)) == x
            True
        """
    def monomial_coefficients(self, copy: bool = True):
        """
        Return the dictionary of ``self`` whose keys are the basis indices
        and the values are coefficients.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,1])
            sage: v = V.highest_weight_vector()
            sage: F1, F2 = Q.F_simple()
            sage: q = Q.q()
            sage: x = v + F1*v + q*F2*F1*v; x
            1*v0 + F[a1]*v0 + (q^2)*F[a1]*F[a2]*v0 + (q)*F[a1+a2]*v0
            sage: sorted(x.monomial_coefficients().items(), key=str)
            [(0, 1), (1, 1), (3, q^2), (4, q)]
        """

class CrystalGraphVertex(SageObject):
    """
    Helper class used as the vertices of a crystal graph.
    """
    V: Incomplete
    s: Incomplete
    def __init__(self, V, s) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.algebras.quantum_groups.quantum_group_gap import CrystalGraphVertex
            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: v = CrystalGraphVertex(V, '<F2*v0>')
            sage: TestSuite(v).run()
        """
    def __hash__(self):
        """
        Return the hash of ``self``.

        EXAMPLES::

            sage: from sage.algebras.quantum_groups.quantum_group_gap import CrystalGraphVertex
            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: v = CrystalGraphVertex(V, '<F2*v0>')
            sage: hash(v) == hash('<F2*v0>')
            True
        """
    def __eq__(self, other):
        """
        Check equality of ``self`` and ``other``.

        EXAMPLES::

            sage: from sage.algebras.quantum_groups.quantum_group_gap import CrystalGraphVertex
            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: v = CrystalGraphVertex(V, '<F2*v0>')
            sage: vp = CrystalGraphVertex(V, '<F2*v0>')
            sage: v == vp
            True
            sage: vpp = CrystalGraphVertex(V, '<1*v0>')
            sage: v == vpp
            False
        """

class QuantumGroupModule(Parent, UniqueRepresentation):
    """
    Abstract base class for quantum group representations.
    """
    def __init__(self, Q, category) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['G',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: TestSuite(V).run()
        """
    def gap(self):
        """
        Return the gap representation of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,1])
            sage: V.gap()
            <8-dimensional left-module over QuantumUEA( <root system of type A2>,
             Qpar = q )>
        """
    @cached_method
    def basis(self):
        """
        Return a basis of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,1])
            sage: V.basis()
            Family (1*v0, F[a1]*v0, F[a2]*v0, F[a1]*F[a2]*v0, F[a1+a2]*v0,
                    F[a1]*F[a1+a2]*v0, F[a1+a2]*F[a2]*v0, F[a1+a2]^(2)*v0)
        """
    @cached_method
    def crystal_basis(self):
        """
        Return the crystal basis of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,1])
            sage: V.crystal_basis()
            Family (1*v0, F[a1]*v0, F[a2]*v0, F[a1]*F[a2]*v0,
                    (q)*F[a1]*F[a2]*v0 + F[a1+a2]*v0, F[a1+a2]*F[a2]*v0,
                    (-q^-2)*F[a1]*F[a1+a2]*v0, (-q^-1)*F[a1+a2]^(2)*v0)
        """
    @cached_method
    def R_matrix(self):
        """
        Return the `R`-matrix of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',1])
            sage: V = Q.highest_weight_module([1])
            sage: V.R_matrix()
            [       1        0        0        0]
            [       0        q -q^2 + 1        0]
            [       0        0        q        0]
            [       0        0        0        1]
        """
    def crystal_graph(self):
        """
        Return the crystal graph of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,1])
            sage: G = V.crystal_graph(); G
            Digraph on 8 vertices

            sage: B = crystals.Tableaux(['A',2], shape=[2,1])
            sage: G.is_isomorphic(B.digraph(), edge_labels=True)
            True
        """
    @cached_method
    def zero(self):
        """
        Return the zero element of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,1])
            sage: V.zero()
            0*v0
        """

class HighestWeightModule(QuantumGroupModule):
    """
    A highest weight module of a quantum group.
    """
    @staticmethod
    def __classcall_private__(cls, Q, weight):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: La = Q.cartan_type().root_system().weight_lattice().fundamental_weights()
            sage: V = Q.highest_weight_module([1,3])
            sage: V is Q.highest_weight_module(La[1]+3*La[2])
            True
        """
    def __init__(self, Q, weight) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,1])
            sage: TestSuite(V).run()
        """
    @cached_method
    def highest_weight_vector(self):
        """
        Return the highest weight vector of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,1])
            sage: V.highest_weight_vector()
            1*v0
        """
    an_element = highest_weight_vector
    def tensor(self, *V, **options):
        """
        Return the tensor product of ``self`` with ``V``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,1])
            sage: Vp = Q.highest_weight_module([1,0])
            sage: Vp.tensor(V)
            Highest weight module of weight Lambda[1] of Quantum Group of type ['A', 2] with q=q
             # Highest weight module of weight Lambda[1] + Lambda[2] of Quantum Group of type ['A', 2] with q=q
        """
    Element = QuaGroupRepresentationElement

class TensorProductOfHighestWeightModules(QuantumGroupModule):
    def __init__(self, *modules, **options) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,1])
            sage: T = tensor([V,V])
            sage: TestSuite(T).run()
        """
    def highest_weight_vectors(self):
        """
        Return the highest weight vectors of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: T = tensor([V,V])
            sage: T.highest_weight_vectors()
            [1*(1*v0<x>1*v0), -q^-1*(1*v0<x>F[a1]*v0) + 1*(F[a1]*v0<x>1*v0)]
        """
    some_elements = highest_weight_vectors
    @cached_method
    def highest_weight_decomposition(self):
        """
        Return the highest weight decomposition of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: T = tensor([V,V])
            sage: T.highest_weight_decomposition()
            [Highest weight submodule with weight 2*Lambda[1] generated by 1*(1*v0<x>1*v0),
             Highest weight submodule with weight Lambda[2] generated by -q^-1*(1*v0<x>F[a1]*v0) + 1*(F[a1]*v0<x>1*v0)]
        """
    def tensor_factors(self):
        """
        Return the factors of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: T = tensor([V,V])
            sage: T.tensor_factors()
            (Highest weight module of weight Lambda[1] of Quantum Group of type ['A', 2] with q=q,
             Highest weight module of weight Lambda[1] of Quantum Group of type ['A', 2] with q=q)
        """
    Element = QuaGroupRepresentationElement

class HighestWeightSubmodule(QuantumGroupModule):
    def __init__(self, ambient, gen, weight) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: T = tensor([V,V])
            sage: S = T.highest_weight_decomposition()[0]
            sage: TestSuite(S).run()
        """
    def ambient(self):
        """
        Return the ambient module of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: T = tensor([V,V])
            sage: S = T.highest_weight_decomposition()[0]
            sage: S.ambient() is T
            True
        """
    @lazy_attribute
    def lift(self):
        """
        The lift morphism from ``self`` to the ambient space.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: T = tensor([V,V])
            sage: S = T.highest_weight_decomposition()[0]
            sage: S.lift
            Generic morphism:
              From: Highest weight submodule with weight 2*Lambda[1] generated by 1*(1*v0<x>1*v0)
              To:   Highest weight module ... # Highest weight module ...
            sage: x = sum(S.basis())
            sage: x.lift()
            1*(1*v0<x>1*v0) + 1*(1*v0<x>F[a1]*v0) + 1*(1*v0<x>F[a1+a2]*v0)
             + q^-1*(F[a1]*v0<x>1*v0) + 1*(F[a1]*v0<x>F[a1]*v0)
             + 1*(F[a1]*v0<x>F[a1+a2]*v0) + q^-1*(F[a1+a2]*v0<x>1*v0)
             + q^-1*(F[a1+a2]*v0<x>F[a1]*v0) + 1*(F[a1+a2]*v0<x>F[a1+a2]*v0)
        """
    def retract(self, elt):
        """
        The retract map from the ambient space to ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: T = tensor([V,V])
            sage: all(S.retract(S.lift(x)) == x
            ....:     for S in T.highest_weight_decomposition()
            ....:     for x in S.basis())
            True
        """
    def highest_weight_vector(self):
        """
        Return the highest weight vector of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: T = tensor([V,V])
            sage: S = T.highest_weight_decomposition()[1]
            sage: u = S.highest_weight_vector(); u
            (1)*e.1
            sage: u.lift()
            -q^-1*(1*v0<x>F[a1]*v0) + 1*(F[a1]*v0<x>1*v0)
        """
    an_element = highest_weight_vector
    def crystal_graph(self, use_ambient: bool = True):
        """
        Return the crystal graph of ``self``.

        INPUT:

        - ``use_ambient`` -- boolean (default: ``True``); if ``True``,
          the vertices are given in terms of the ambient module

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: V = Q.highest_weight_module([1,0])
            sage: T = tensor([V,V])
            sage: S = T.highest_weight_decomposition()[1]
            sage: G = S.crystal_graph()
            sage: sorted(G.vertices(sort=False), key=str)
            [<-q^-1*(1*v0<x>F[a1+a2]*v0) + 1*(F[a1+a2]*v0<x>1*v0)>,
             <-q^-1*(1*v0<x>F[a1]*v0) + 1*(F[a1]*v0<x>1*v0)>,
             <-q^-1*(F[a1]*v0<x>F[a1+a2]*v0) + 1*(F[a1+a2]*v0<x>F[a1]*v0)>]
            sage: sorted(S.crystal_graph(False).vertices(sort=False), key=str)
            [<(1)*e.1>, <(1)*e.2>, <(1)*e.3>]
        """
    Element = QuaGroupRepresentationElement

class LowerHalfQuantumGroup(Parent, UniqueRepresentation):
    """
    The lower half of the quantum group.
    """
    @staticmethod
    def __classcall_private__(cls, Q):
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.algebras.quantum_groups.quantum_group_gap import LowerHalfQuantumGroup
            sage: Q = QuantumGroup(['A',2])
            sage: Q.lower_half() is LowerHalfQuantumGroup(Q)
            True
        """
    def __init__(self, Q) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: B = Q.lower_half()
            sage: TestSuite(B).run()
        """
    def ambient(self):
        """
        Return the ambient quantum group of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: B = Q.lower_half()
            sage: B.ambient() is Q
            True
        """
    @cached_method
    def highest_weight_vector(self):
        """
        Return the highest weight vector of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: B = Q.lower_half()
            sage: B.highest_weight_vector()
            1
        """
    one = highest_weight_vector
    an_element = highest_weight_vector
    @cached_method
    def zero(self):
        """
        Return the zero element of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: B = Q.lower_half()
            sage: B.zero()
            0
        """
    @cached_method
    def algebra_generators(self):
        """
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: B = Q.lower_half()
            sage: B.algebra_generators()
            Finite family {1: F[a1], 2: F[a2]}
        """
    gens = algebra_generators
    @cached_method
    def basis(self):
        """
        Return the basis of ``self``.

        This returns the PBW basis of ``self``, which is given by
        monomials in `\\{F_{\\alpha}\\}`, where `\\alpha` runs over all
        positive roots.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: B = Q.lower_half()
            sage: basis = B.basis(); basis
            Lazy family (monomial(i))_{i in The Cartesian product of
             (Non negative integers, Non negative integers, Non negative integers)}
            sage: basis[1,2,1]
            F[a1]*F[a1+a2]^(2)*F[a2]
            sage: basis[1,2,4]
            F[a1]*F[a1+a2]^(2)*F[a2]^(4)
            sage: basis[1,0,4]
            F[a1]*F[a2]^(4)
        """
    @cached_method
    def canonical_basis_elements(self):
        """
        Construct the monomial elements of ``self`` indexed by ``k``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: B = Q.lower_half()
            sage: C = B.canonical_basis_elements(); C
            Lazy family (Canonical basis(i))_{i in The Cartesian product of
             (Non negative integers, Non negative integers)}
            sage: C[2,1]
            [F[a1]^(2)*F[a2], F[a1]*F[a1+a2] + (q^2)*F[a1]^(2)*F[a2]]
            sage: C[1,2]
            [F[a1]*F[a2]^(2), (q^2)*F[a1]*F[a2]^(2) + F[a1+a2]*F[a2]]
        """
    def lift(self, elt):
        """
        Lift ``elt`` to the ambient quantum group of ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: B = Q.lower_half()
            sage: x = B.lift(B.an_element()); x
            1
            sage: x.parent() is Q
            True
        """
    def retract(self, elt):
        """
        Retract ``elt`` from the ambient quantum group to ``self``.

        EXAMPLES::

            sage: Q = QuantumGroup(['A',2])
            sage: B = Q.lower_half()
            sage: x = Q.an_element(); x
            1 + (q)*F[a1] + E[a1] + (q^2-1-q^-2 + q^-4)*[ K1 ; 2 ]
             + K1 + (-q^-1 + q^-3)*K1[ K1 ; 1 ]
            sage: B.retract(x)
            1 + (q)*F[a1]
        """
    class Element(QuaGroupModuleElement):
        """
        An element of the lower half of the quantum group.
        """
        def monomial_coefficients(self, copy: bool = True):
            """
            Return the dictionary of ``self`` whose keys are the basis
            indices and the values are coefficients.

            EXAMPLES::

                sage: Q = QuantumGroup(['A',2])
                sage: B = Q.lower_half()
                sage: x = B.retract(Q.an_element()); x
                1 + (q)*F[a1]
                sage: sorted(x.monomial_coefficients().items(), key=str)
                [((0, 0, 0), 1), ((1, 0, 0), q)]
            """
        def bar(self):
            """
            Return the bar involution on ``self``.

            EXAMPLES::

                sage: Q = QuantumGroup(['A',2])
                sage: F1, F2 = Q.F_simple()
                sage: B = Q.lower_half()
                sage: x = B(Q.an_element()); x
                1 + (q)*F[a1]
                sage: x.bar()
                1 + (q^-1)*F[a1]
                sage: (F1*x).bar() == F1 * x.bar()
                True
                sage: (F2*x).bar() == F2 * x.bar()
                True

                sage: Q = QuantumGroup(['G',2])
                sage: F1, F2 = Q.F_simple()
                sage: q = Q.q()
                sage: B = Q.lower_half()
                sage: x = B(q^-2*F1*F2^2*F1)
                sage: x
                (q + q^-5)*F[a1]*F[a1+a2]*F[a2]
                 + (q^8 + q^6 + q^2 + 1)*F[a1]^(2)*F[a2]^(2)
                sage: x.bar()
                (q^5 + q^-1)*F[a1]*F[a1+a2]*F[a2]
                 + (q^12 + q^10 + q^6 + q^4)*F[a1]^(2)*F[a2]^(2)
            """
        def tau(self):
            """
            Return the action of the `\\tau` anti-automorphism on ``self``.

            EXAMPLES::

                sage: Q = QuantumGroup(['A',2])
                sage: F1, F2 = Q.F_simple()
                sage: B = Q.lower_half()
                sage: x = B(Q.an_element()); x
                1 + (q)*F[a1]
                sage: x.tau()
                1 + (q)*F[a1]
                sage: (F1*x).tau() == x.tau() * F1.tau()
                True
                sage: (F2*x).tau() == x.tau() * F2.tau()
                True

                sage: Q = QuantumGroup(['G',2])
                sage: F1, F2 = Q.F_simple()
                sage: q = Q.q()
                sage: B = Q.lower_half()
                sage: x = B(q^-2*F1*F2^2*F1)
                sage: x
                (q + q^-5)*F[a1]*F[a1+a2]*F[a2]
                 + (q^8 + q^6 + q^2 + 1)*F[a1]^(2)*F[a2]^(2)
                sage: x.tau()
                (q + q^-5)*F[a1]*F[a1+a2]*F[a2]
                 + (q^8 + q^6 + q^2 + 1)*F[a1]^(2)*F[a2]^(2)
            """
        def braid_group_action(self, braid):
            """
            Return the action of the braid group element ``braid``
            projected into ``self``.

            INPUT:

            - ``braid`` -- a reduced word of a braid group element

            EXAMPLES::

                sage: Q = QuantumGroup(['A',2])
                sage: L = Q.lower_half()
                sage: v = L.highest_weight_vector().f_tilde([1,2,2,1]); v
                F[a1]*F[a1+a2]*F[a2]
                sage: v.braid_group_action([1])
                (-q^3-q)*F[a2]^(2)
                sage: v.braid_group_action([]) == v
                True
            """
