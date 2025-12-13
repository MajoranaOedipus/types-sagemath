from _typeshed import Incomplete
from sage.categories.groups import Groups as Groups
from sage.groups.group import AbelianGroup as AbelianGroupBase
from sage.groups.libgap_mixin import GroupMixinLibGAP as GroupMixinLibGAP
from sage.groups.libgap_wrapper import ElementLibGAP as ElementLibGAP, ParentLibGAP as ParentLibGAP
from sage.libs.gap.element import GapElement as GapElement
from sage.libs.gap.libgap import libgap as libgap
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class AbelianGroupElement_gap(ElementLibGAP):
    """
    An element of an abelian group via libgap.

    EXAMPLES::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: G = AbelianGroupGap([3,6])
        sage: G.gens()
        (f1, f2)
    """
    def __init__(self, parent, x, check: bool = True) -> None:
        """
        The Python constructor.

        See :class:`AbelianGroupElement_gap` for details.

        INPUT:

        - ``parent`` -- an instance of :class:`AbelianGroup_gap`
        - ``x`` -- an instance of :class:`sage.libs.gap.element.GapElement`
        - ``check`` -- boolean (default: ``True``); check
          if ``x`` is an element  of the group

        TESTS::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([3,6])
            sage: g = G.an_element()
            sage: TestSuite(g).run()
        """
    def __hash__(self):
        """
        Return the hash of this element.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([3,2,4])
            sage: g = G.an_element()
            sage: g.__hash__()    # random
            1693277541873681615
        """
    def __reduce__(self):
        """
        Implement pickling.

        OUTPUT: tuple ``f`` such that this element is ``f[0](*f[1])``

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([3,2,4])
            sage: g = G.an_element()
            sage: g == loads(dumps(g))
            True
            sage: g.__reduce__()
            (Abelian group with gap, generator orders (3, 2, 4), ((1, 1, 1),))
        """
    def exponents(self):
        """
        Return the tuple of exponents of this element.

        OUTPUT: tuple of integers

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([4,7,9])
            sage: gens = G.gens()
            sage: g = gens[0]^2 * gens[1]^4 * gens[2]^8
            sage: g.exponents()
            (2, 4, 8)
            sage: S = G.subgroup(G.gens()[:1])
            sage: s = S.gens()[0]
            sage: s
            f1
            sage: s.exponents()
            (1,)

        It can handle quite large groups too::

            sage: G = AbelianGroupGap([2^10, 5^10])
            sage: f1, f2 = G.gens()
            sage: g = f1^123*f2^789
            sage: g.exponents()
            (123, 789)

        .. WARNING::

            Crashes for very large groups.

        .. TODO::

            Make exponents work for very large groups.
            This could be done by using Pcgs in gap.
        """
    def order(self):
        """
        Return the order of this element.

        OUTPUT: integer or infinity

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([4])
            sage: g = G.gens()[0]
            sage: g.order()
            4
            sage: G = AbelianGroupGap([0])          # optional - gap_package_polycyclic
            sage: g = G.gens()[0]                   # optional - gap_package_polycyclic
            sage: g.order()                         # optional - gap_package_polycyclic
            +Infinity
        """

class AbelianGroupElement_polycyclic(AbelianGroupElement_gap):
    """
    An element of an abelian group using the GAP package ``Polycyclic``.

    TESTS::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: G = AbelianGroupGap([4,7,0])          # optional - gap_package_polycyclic
        sage: TestSuite(G.an_element()).run()       # optional - gap_package_polycyclic
    """
    def exponents(self):
        """
        Return the tuple of exponents of ``self``.

        OUTPUT: tuple of integers

        EXAMPLES::

            sage: # optional - gap_package_polycyclic
            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([4,7,0])
            sage: gens = G.gens()
            sage: g = gens[0]^2 * gens[1]^4 * gens[2]^8
            sage: g.exponents()
            (2, 4, 8)

        Efficiently handles very large groups::

            sage: # optional - gap_package_polycyclic
            sage: G = AbelianGroupGap([2^30,5^30,0])
            sage: f1, f2, f3 = G.gens()
            sage: (f1^12345*f2^123456789).exponents()
            (12345, 123456789, 0)
        """

class AbelianGroup_gap(UniqueRepresentation, GroupMixinLibGAP, ParentLibGAP, AbelianGroupBase):
    """
    Finitely generated abelian groups implemented in GAP.

    Needs the gap package ``Polycyclic`` in case the group is infinite.

    INPUT:

    - ``G`` -- a GAP group
    - ``category`` -- a category
    - ``ambient`` -- (optional) an :class:`AbelianGroupGap`

    EXAMPLES::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: G = AbelianGroupGap([3, 2, 5])
        sage: G
        Abelian group with gap, generator orders (3, 2, 5)
    """
    def __init__(self, G, category, ambient=None) -> None:
        """
        Create an instance of this class.

        See :class:`AbelianGroup_gap` for details

        TESTS::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([3,2,5])
            sage: TestSuite(G).run()
        """
    Element = AbelianGroupElement_gap
    def all_subgroups(self):
        """
        Return the list of all subgroups of this group.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2, 3])
            sage: G.all_subgroups()
            [Subgroup of Abelian group with gap, generator orders (2, 3) generated by (),
             Subgroup of Abelian group with gap, generator orders (2, 3) generated by (f1,),
             Subgroup of Abelian group with gap, generator orders (2, 3) generated by (f2,),
             Subgroup of Abelian group with gap, generator orders (2, 3) generated by (f2, f1)]
        """
    def automorphism_group(self):
        """
        Return the group of automorphisms of ``self``.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2, 3])
            sage: G.aut()
            Full group of automorphisms of Abelian group with gap, generator orders (2, 3)
        """
    aut = automorphism_group
    def is_trivial(self):
        """
        Return ``True`` if this group is the trivial group.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([])
            sage: G
            Abelian group with gap, generator orders ()
            sage: G.is_trivial()
            True
            sage: AbelianGroupGap([1]).is_trivial()
            True
            sage: AbelianGroupGap([1,1,1]).is_trivial()
            True
            sage: AbelianGroupGap([2]).is_trivial()
            False
            sage: AbelianGroupGap([2,1]).is_trivial()
            False
        """
    def identity(self):
        """
        Return the identity element of this group.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([4,10])
            sage: G.identity()
            1
        """
    @cached_method
    def elementary_divisors(self):
        """
        Return the elementary divisors of this group.

        See :meth:`sage.groups.abelian_gps.abelian_group_gap.elementary_divisors`.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: G.elementary_divisors()
            (2, 60)
        """
    @cached_method
    def exponent(self):
        """
        Return the exponent of this abelian group.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,7])
            sage: G
            Abelian group with gap, generator orders (2, 3, 7)
            sage: G = AbelianGroupGap([2,4,6])
            sage: G
            Abelian group with gap, generator orders (2, 4, 6)
            sage: G.exponent()
            12
        """
    @cached_method
    def gens_orders(self):
        """
        Return the orders of the generators.

        Use :meth:`elementary_divisors` if you are looking for an
        invariant of the group.

        OUTPUT: tuple of integers

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: Z2xZ3 = AbelianGroupGap([2,3])
            sage: Z2xZ3.gens_orders()
            (2, 3)
            sage: Z2xZ3.elementary_divisors()
            (6,)
            sage: Z6 = AbelianGroupGap([6])
            sage: Z6.gens_orders()
            (6,)
            sage: Z6.elementary_divisors()
            (6,)
            sage: Z2xZ3.is_isomorphic(Z6)
            True
            sage: Z2xZ3 is Z6
            False
        """
    def is_subgroup_of(self, G):
        """
        Return if ``self`` is a subgroup of ``G`` considered in
        the same ambient group.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: gen = G.gens()[:2]
            sage: S1 = G.subgroup(gen)
            sage: S1.is_subgroup_of(G)
            True
            sage: S2 = G.subgroup(G.gens()[1:])
            sage: S2.is_subgroup_of(S1)
            False
        """
    def quotient(self, N):
        """
        Return the quotient of this group by the normal subgroup `N`.

        INPUT:

        - ``N`` -- a subgroup
        - ``check`` -- boolean (default: ``True``); check if `N` is normal

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: A = AbelianGroupGap([2,3,4,5])
            sage: S = A.subgroup(A.gens()[:1])
            sage: A.quotient(S)
            Quotient abelian group with generator orders (1, 3, 4, 5)
        """
    def subgroup(self, gens):
        """
        Return the subgroup of this group generated by ``gens``.

        INPUT:

        - ``gens`` -- list of elements coercible into this group

        OUTPUT: a subgroup

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: gen = G.gens()[:2]
            sage: S = G.subgroup(gen)
            sage: S
            Subgroup of Abelian group with gap, generator orders (2, 3, 4, 5)
             generated by (f1, f2)
            sage: g = G.an_element()
            sage: s = S.an_element()
            sage: g * s
            f2^2*f3*f5

            sage: # optional - gap_package_polycyclic
            sage: G = AbelianGroupGap([3,4,0,2])
            sage: gen = G.gens()[:2]
            sage: S = G.subgroup(gen)
            sage: g = G.an_element()
            sage: s = S.an_element()
            sage: g * s
            g1^2*g2^2*g3*g4

        TESTS::

            sage: h = G.gens()[3]
            sage: h in S
            False
        """

class AbelianGroupGap(AbelianGroup_gap):
    """
    Abelian groups implemented using GAP.

    INPUT:

    - ``generator_orders`` -- list of nonnegative integers where `0`
      gives a factor isomorphic to `\\ZZ`

    OUTPUT: an abelian group

    EXAMPLES::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: AbelianGroupGap([3,6])
        Abelian group with gap, generator orders (3, 6)
        sage: AbelianGroupGap([3,6,5])
        Abelian group with gap, generator orders (3, 6, 5)
        sage: AbelianGroupGap([3,6,0])      # optional - gap_package_polycyclic
        Abelian group with gap, generator orders (3, 6, 0)

    .. WARNING::

        Needs the GAP package ``Polycyclic`` in case the group is infinite.
    """
    @staticmethod
    def __classcall_private__(cls, generator_orders):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: A1 = AbelianGroupGap((2,3,4))
            sage: A2 = AbelianGroupGap([4/2,3,4])
            sage: A1 is A2
            True
        """
    Element: Incomplete
    def __init__(self, generator_orders) -> None:
        """
        Constructor.

        TESTS::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: A = AbelianGroup((2,3,4))
            sage: TestSuite(A).run()
        """
    def __reduce__(self):
        """
        Implement pickling.

        We have to work around the fact that gap does not provide pickling.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([3,2,5])
            sage: G == loads(dumps(G))
            True
            sage: G is loads(dumps(G))
            True
        """

class AbelianGroupSubgroup_gap(AbelianGroup_gap):
    """
    Subgroups of abelian groups with GAP.

    INPUT:

    - ``ambient`` -- the ambient group
    - ``gens`` -- generators of the subgroup

    .. NOTE::

        Do not construct this class directly. Instead use
        :meth:`~sage.groups.abelian_groups.AbelianGroupGap.subgroup`.

    EXAMPLES::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: G = AbelianGroupGap([2,3,4,5])
        sage: gen = G.gens()[:2]
        sage: S = G.subgroup(gen)
    """
    def __init__(self, ambient, gens) -> None:
        """
        Initialize this subgroup.

        TESTS::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap, AbelianGroupSubgroup_gap
            sage: G = AbelianGroupGap([])
            sage: gen = G.gens()
            sage: A = AbelianGroupSubgroup_gap(G, gen)
            sage: TestSuite(A).run()

        Check that we are in the correct category::

            sage: # optional - gap_package_polycyclic
            sage: G = AbelianGroupGap([2,3,0])
            sage: g = G.gens()
            sage: H1 = G.subgroup([g[0],g[1]])
            sage: H1 in Groups().Finite()
            True
            sage: H2 = G.subgroup([g[0],g[2]])
            sage: H2 in Groups().Infinite()
            True
        """
    def __reduce__(self):
        """
        Implement pickling.

        We have to work around the fact that gap does not provide pickling.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: gen = G.gens()[:2]
            sage: S = G.subgroup(gen)
            sage: S == loads(dumps(S))
            True
            sage: S is loads(dumps(S))
            True
        """
    def lift(self, x):
        """
        Coerce to the ambient group.

        The terminology comes from the category framework and the more general notion of a subquotient.

        INPUT:

        - ``x`` -- an element of this subgroup

        OUTPUT: the corresponding element of the ambient group

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([4])
            sage: g = G.gen(0)
            sage: H = G.subgroup([g^2])
            sage: h = H.gen(0); h
            f2
            sage: h.parent()
            Subgroup of Abelian group with gap, generator orders (4,) generated by (f2,)
            sage: H.lift(h)
            f2
            sage: H.lift(h).parent()
            Abelian group with gap, generator orders (4,)
        """
    def retract(self, x):
        """
        Convert an element of the ambient group into this subgroup.

        The terminology comes from the category framework and the more general
        notion of a subquotient.

        INPUT:

        - ``x`` -- an element of the ambient group that actually lies in this subgroup

        OUTPUT: the corresponding element of this subgroup

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([4])
            sage: g = G.gen(0)
            sage: H = G.subgroup([g^2])
            sage: H.retract(g^2)
            f2
            sage: H.retract(g^2).parent()
            Subgroup of Abelian group with gap, generator orders (4,) generated by (f2,)
        """

class AbelianGroupQuotient_gap(AbelianGroup_gap):
    """
    Quotients of abelian groups by a subgroup.

    .. NOTE::

        Do not call this directly. Instead use :meth:`quotient`.

    EXAMPLES::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: A = AbelianGroupGap([4,3])
        sage: N = A.subgroup([A.gen(0)^2])
        sage: Q1 = A.quotient(N)
        sage: Q1
        Quotient abelian group with generator orders (2, 3)
        sage: Q2 = Q1.quotient(Q1.subgroup(Q1.gens()[:1]))
        sage: Q2
        Quotient abelian group with generator orders (1, 3)
    """
    def __init__(self, G, N) -> None:
        """
        Constructor.

        TESTS::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: gen = G.gens()[:2]
            sage: S = G.subgroup(gen)
            sage: Q = G.quotient(S)
            sage: TestSuite(Q).run()
        """
    def __reduce__(self):
        """
        Implement pickling.

        We have to work around the fact that gap does not provide pickling.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: A = AbelianGroupGap([4])
            sage: N = A.subgroup([A.gen(0)^2])
            sage: Q = A.quotient(N)
            sage: Q is loads(dumps(Q))
            True
        """
    def cover(self):
        """
        Return the covering group of this quotient group.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: gen = G.gens()[:2]
            sage: S = G.subgroup(gen)
            sage: Q = G.quotient(S)
            sage: Q.cover() is G
            True
        """
    def relations(self):
        """
        Return the relations of this quotient group.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: gen = G.gens()[:2]
            sage: S = G.subgroup(gen)
            sage: Q = G.quotient(S)
            sage: Q.relations() is S
            True
        """
    @cached_method
    def natural_homomorphism(self):
        """
        Return the defining homomorphism into ``self``.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: A = AbelianGroupGap([4])
            sage: N = A.subgroup([A.gen(0)^2])
            sage: Q = A.quotient(N)
            sage: Q.natural_homomorphism()
            Group morphism:
            From: Abelian group with gap, generator orders (4,)
            To:   Quotient abelian group with generator orders (2,)
        """
    def lift(self, x):
        """
        Lift an element to the cover.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: A = AbelianGroupGap([4])
            sage: N = A.subgroup([A.gen(0)^2])
            sage: Q = A.quotient(N)
            sage: Q.lift(Q.0)
            f1
        """
