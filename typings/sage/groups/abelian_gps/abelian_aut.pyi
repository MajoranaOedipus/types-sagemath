from sage.categories.groups import Groups as Groups
from sage.groups.abelian_gps.abelian_group_gap import AbelianGroup_gap as AbelianGroup_gap
from sage.groups.group import Group as Group
from sage.groups.libgap_mixin import GroupMixinLibGAP as GroupMixinLibGAP
from sage.groups.libgap_wrapper import ElementLibGAP as ElementLibGAP, ParentLibGAP as ParentLibGAP
from sage.libs.gap.libgap import libgap as libgap
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.unique_representation import CachedRepresentation as CachedRepresentation

class AbelianGroupAutomorphism(ElementLibGAP):
    """
    Automorphisms of abelian groups with gap.

    INPUT:

    - ``x`` -- a libgap element
    - ``parent`` -- the parent :class:`~AbelianGroupAutomorphismGroup_gap`
    - ``check`` -- boolean (default: ``True``); checks if ``x`` is an element
      of the group

    EXAMPLES::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: G = AbelianGroupGap([2,3,4,5])
        sage: f = G.aut().an_element()
    """
    def __init__(self, parent, x, check: bool = True) -> None:
        """
        The Python constructor.

        TESTS::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: f = G.aut().an_element()
            sage: TestSuite(f).run()
        """
    def __hash__(self):
        """
        The hash of this element.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: f = G.aut().an_element()
            sage: f.__hash__() == hash(f.matrix())
            True
        """
    def __reduce__(self):
        """
        Implement pickling.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: f = G.aut().an_element()
            sage: f == loads(dumps(f))
            True
        """
    def __call__(self, a):
        """
        Return the image of ``a`` under this automorphism.

        INPUT:

        - ``a`` -- something convertible into the domain

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4])
            sage: f = G.aut().an_element()
            sage: f
            Pcgs([ f1, f2, f3, f4 ]) -> [ f1*f4, f2^2, f1*f3, f4 ]
        """
    def matrix(self):
        """
        Return the matrix defining ``self``.

        The `i`-th row is the exponent vector of
        the image of the `i`-th generator.

        OUTPUT: a square matrix over the integers

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4])
            sage: f = G.aut().an_element()
            sage: f
            Pcgs([ f1, f2, f3, f4 ]) -> [ f1*f4, f2^2, f1*f3, f4 ]
            sage: f.matrix()
            [1 0 2]
            [0 2 0]
            [1 0 1]

        Compare with the exponents of the images::

            sage: f(G.gens()[0]).exponents()
            (1, 0, 2)
            sage: f(G.gens()[1]).exponents()
            (0, 2, 0)
            sage: f(G.gens()[2]).exponents()
            (1, 0, 1)
        """

class AbelianGroupAutomorphismGroup_gap(CachedRepresentation, GroupMixinLibGAP, Group, ParentLibGAP):
    """
    Base class for groups of automorphisms of abelian groups.

    Do not construct this directly.

     INPUT:

    - ``domain`` -- :class:`~sage.groups.abelian_gps.abelian_group_gap.AbelianGroup_gap`
    - ``libgap_parent`` -- the libgap element that is the parent in GAP
    - ``category`` -- a category
    - ``ambient`` -- an instance of a derived class of
      :class:`~sage.groups.libgap_wrapper.ParentLibGAP` or ``None`` (default);
      the ambient group if ``libgap_parent`` has been defined as a subgroup

    EXAMPLES::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: from sage.groups.abelian_gps.abelian_aut import AbelianGroupAutomorphismGroup_gap
        sage: domain = AbelianGroupGap([2,3,4,5])
        sage: aut = domain.gap().AutomorphismGroupAbelianGroup()
        sage: AbelianGroupAutomorphismGroup_gap(domain, aut, Groups().Finite())
        <group with 6 generators>
    """
    Element = AbelianGroupAutomorphism
    def __init__(self, domain, gap_group, category, ambient=None) -> None:
        """
        Constructor.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: G.aut()
            Full group of automorphisms of Abelian group with gap, generator orders (2, 3, 4, 5)
        """
    def covering_matrix_ring(self):
        """
        Return the covering matrix ring of this group.

        This is the ring of `n \\times n` matrices over `\\ZZ` where
        `n` is the number of (independent) generators.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: aut = G.aut()
            sage: aut.covering_matrix_ring()
            Full MatrixSpace of 4 by 4 dense matrices over Integer Ring
        """
    def domain(self):
        """
        Return the domain of this group of automorphisms.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: aut = G.aut()
            sage: aut.domain()
            Abelian group with gap, generator orders (2, 3, 4, 5)
        """
    def is_subgroup_of(self, G):
        """
        Return if ``self`` is a subgroup of ``G`` considered in the same ambient group.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: aut = G.aut()
            sage: gen = aut.gens()
            sage: S1 = aut.subgroup(gen[:2])
            sage: S1.is_subgroup_of(aut)
            True
            sage: S2 = aut.subgroup(aut.gens()[1:])
            sage: S2.is_subgroup_of(S1)
            False
        """

class AbelianGroupAutomorphismGroup(AbelianGroupAutomorphismGroup_gap):
    """
    The full automorphism group of a finite abelian group.

    INPUT:

    - ``AbelianGroupGap`` -- an instance of
      :class:`~sage.groups.abelian_gps.abelian_group_gap.AbelianGroup_gap`

    EXAMPLES::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: from sage.groups.abelian_gps.abelian_aut import AbelianGroupAutomorphismGroup
        sage: G = AbelianGroupGap([2,3,4,5])
        sage: aut = G.aut()

    Equivalently::

        sage: aut1 = AbelianGroupAutomorphismGroup(G)
        sage: aut is aut1
        True
    """
    Element = AbelianGroupAutomorphism
    def __init__(self, AbelianGroupGap) -> None:
        """
        Constructor.

        EXAMPLES::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: aut = G.aut()
            sage: TestSuite(aut).run()
        """

class AbelianGroupAutomorphismGroup_subgroup(AbelianGroupAutomorphismGroup_gap):
    """
    Groups of automorphisms of abelian groups.

    They are subgroups of the full automorphism group.

    .. NOTE::

        Do not construct this class directly; instead use
        :meth:`sage.groups.abelian_gps.abelian_group_gap.AbelianGroup_gap.subgroup`.

    INPUT:

    - ``ambient`` -- the ambient group
    - ``generators`` -- tuple of gap elements of the ambient group

    EXAMPLES::

        sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
        sage: from sage.groups.abelian_gps.abelian_aut import AbelianGroupAutomorphismGroup_subgroup
        sage: G = AbelianGroupGap([2,3,4,5])
        sage: aut = G.aut()
        sage: gen = aut.gens()
        sage: AbelianGroupAutomorphismGroup_subgroup(aut, gen)
        Subgroup of automorphisms of Abelian group with gap, generator orders (2, 3, 4, 5)
        generated by 6 automorphisms
    """
    Element = AbelianGroupAutomorphism
    def __init__(self, ambient, generators) -> None:
        """
        Constructor.

        TESTS::

            sage: from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
            sage: G = AbelianGroupGap([2,3,4,5])
            sage: aut = G.automorphism_group()
            sage: f = aut.an_element()
            sage: sub = aut.subgroup([f])
            sage: TestSuite(sub).run()
        """
