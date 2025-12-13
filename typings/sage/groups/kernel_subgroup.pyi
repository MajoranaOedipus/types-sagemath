from sage.categories.groups import Groups as Groups
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element_wrapper import ElementWrapper as ElementWrapper
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class KernelSubgroup(UniqueRepresentation, Parent):
    """
    The kernel (normal) subgroup.

    Let `\\phi : G \\to H` be a group homomorphism. The kernel
    `K = \\{\\phi(g) = 1 | g \\in G\\}` is a normal subgroup of `G`.
    """
    def __init__(self, morphism) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S2 = SymmetricGroup(2)
            sage: S3 = SymmetricGroup(3)
            sage: H = Hom(S3, S2)
            sage: phi = H(S2.__call__)
            sage: from sage.groups.kernel_subgroup import KernelSubgroup
            sage: K = KernelSubgroup(phi)
            sage: TestSuite(K).run()
        """
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: S2 = SymmetricGroup(2)
            sage: S3 = SymmetricGroup(3)
            sage: H = Hom(S3, S2)
            sage: phi = H(S2.__call__)
            sage: from sage.groups.kernel_subgroup import KernelSubgroup
            sage: K = KernelSubgroup(phi)
            sage: K.gens()
            ((),)
        """
    def defining_morphism(self):
        """
        Return the defining morphism of ``self``.

        EXAMPLES::

            sage: PJ3 = groups.misc.PureCactus(3)                                       # needs sage.rings.number_field
            sage: PJ3.defining_morphism()                                               # needs sage.rings.number_field
            Conversion via _from_cactus_group_element map:
              From: Cactus Group with 3 fruit
              To:   Symmetric group of order 3! as a permutation group
        """
    @cached_method
    def ambient(self):
        """
        Return the ambient group of ``self``.

        EXAMPLES::

            sage: PJ3 = groups.misc.PureCactus(3)                                       # needs sage.rings.number_field
            sage: PJ3.ambient()                                                         # needs sage.rings.number_field
            Cactus Group with 3 fruit
        """
    def lift(self, x):
        """
        Lift ``x`` to the ambient group of ``self``.

        EXAMPLES::

            sage: PJ3 = groups.misc.PureCactus(3)                                       # needs sage.rings.number_field
            sage: PJ3.lift(PJ3.an_element()).parent()                                   # needs sage.rings.number_field
            Cactus Group with 3 fruit
        """
    def retract(self, x):
        """
        Convert ``x`` to an element of ``self``.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: J3 = groups.misc.Cactus(3)
            sage: s12,s13,s23 = J3.group_generators()
            sage: PJ3 = groups.misc.PureCactus(3)
            sage: elt = PJ3.retract(s23*s12*s23*s13); elt
            s[2,3]*s[1,2]*s[2,3]*s[1,3]
            sage: elt.parent() is PJ3
            True
        """
    def __iter__(self):
        """
        Iterate through ``self``.

        EXAMPLES::

            sage: S2 = SymmetricGroup(2)
            sage: S3 = SymmetricGroup(3)
            sage: H = Hom(S3, S2)
            sage: phi = H(S2.__call__)
            sage: from sage.groups.kernel_subgroup import KernelSubgroup
            sage: K = KernelSubgroup(phi)
            sage: list(K)
            [()]
        """
    class Element(ElementWrapper):
        def __invert__(self):
            """
            Return the inverse of ``self``.

            EXAMPLES::

                sage: # needs sage.rings.number_field
                sage: J3 = groups.misc.Cactus(3)
                sage: s12,s13,s23 = J3.group_generators()
                sage: PJ3 = groups.misc.PureCactus(3)
                sage: elt = PJ3(s23*s12*s23*s13)
                sage: ~elt
                s[1,2]*s[2,3]*s[1,2]*s[1,3]
            """
