from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.groups.abelian_gps.abelian_group import AbelianGroup as AbelianGroup
from sage.groups.class_function import ClassFunction_libgap as ClassFunction_libgap
from sage.groups.conjugacy_classes import ConjugacyClassGAP as ConjugacyClassGAP
from sage.groups.generic import structure_description as structure_description
from sage.groups.group import FiniteGroup as FiniteGroup
from sage.groups.perm_gps.constructor import standardize_generator as standardize_generator
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement as PermutationGroupElement
from sage.interfaces.abc import ExpectElement as ExpectElement, GapElement as GapElement
from sage.libs.gap.libgap import libgap as libgap
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.randstate import current_randstate as current_randstate
from sage.misc.rest_index_of_methods import gen_rest_table_index as gen_rest_table_index
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ as QQ
from sage.sets.finite_enumerated_set import FiniteEnumeratedSet as FiniteEnumeratedSet
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, rich_to_bool as rich_to_bool, richcmp as richcmp, richcmp_method as richcmp_method

def load_hap() -> None:
    """
    Load the GAP hap package into the default GAP interpreter interface.

    EXAMPLES::

        sage: sage.groups.perm_gps.permgroup.load_hap()         # optional - gap_package_hap
    """
def hap_decorator(f):
    '''
    A decorator for permutation group methods that require HAP.  It
    checks to see that HAP is installed as well as checks that the
    argument ``p`` is either 0 or prime.

    EXAMPLES::

        sage: # optional - gap_package_hap
        sage: from sage.groups.perm_gps.permgroup import hap_decorator
        sage: def foo(self, n, p=0): print("Done")
        sage: foo = hap_decorator(foo)
        sage: foo(None, 3)
        Done
        sage: foo(None, 3, 0)
        Done
        sage: foo(None, 3, 5)
        Done
        sage: foo(None, 3, 4)
        Traceback (most recent call last):
        ...
        ValueError: p must be 0 or prime
    '''
def direct_product_permgroups(P):
    """
    Take the direct product of the permutation groups listed in ``P``.

    EXAMPLES::

        sage: G1 = AlternatingGroup([1,2,4,5])
        sage: G2 = AlternatingGroup([3,4,6,7])
        sage: D = direct_product_permgroups([G1,G2,G1])
        sage: D.order()
        1728
        sage: D = direct_product_permgroups([G1])
        sage: D == G1
        True
        sage: direct_product_permgroups([])
        Symmetric group of order 0! as a permutation group
    """
def from_gap_list(G, src):
    '''
    Convert a string giving a list of GAP permutations into a list of
    elements of ``G``.

    EXAMPLES::

        sage: from sage.groups.perm_gps.permgroup import from_gap_list
        sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
        sage: L = from_gap_list(G, "[(1,2,3)(4,5), (3,4)]"); L
        [(1,2,3)(4,5), (3,4)]
        sage: L[0].parent() is G
        True
        sage: L[1].parent() is G
        True
    '''
def PermutationGroup(gens=None, *args, **kwds):
    '''
    Return the permutation group associated to `x` (typically a
    list of generators).

    INPUT:

    - ``gens`` -- (default: ``None``) list of generators

    - ``gap_group`` -- (optional) a gap permutation group

    - ``canonicalize`` -- boolean (default: ``True``); if ``True``,
      sort generators and remove duplicates

    OUTPUT: a permutation group

    EXAMPLES::

        sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
        sage: G
        Permutation Group with generators [(3,4), (1,2,3)(4,5)]

    We can also make permutation groups from PARI groups::

        sage: # needs sage.libs.pari
        sage: H = pari(\'x^4 - 2*x^3 - 2*x + 1\').polgalois()
        sage: G = PariGroup(H, 4); G
        PARI group [8, -1, 3, "D(4)"] of degree 4
        sage: H = PermutationGroup(G); H
        Transitive group number 3 of degree 4
        sage: H.gens()
        ((1,2,3,4), (1,3))

    We can also create permutation groups whose generators are GAP
    permutation objects::

        sage: p = gap(\'(1,2)(3,7)(4,6)(5,8)\'); p
        (1,2)(3,7)(4,6)(5,8)
        sage: PermutationGroup([p])
        Permutation Group with generators [(1,2)(3,7)(4,6)(5,8)]

    Permutation groups can work on any domain. In the following
    examples, the permutations are specified in list notation,
    according to the order of the elements of the domain::

        sage: list(PermutationGroup([[\'b\',\'c\',\'a\']], domain=[\'a\',\'b\',\'c\']))
        [(), (\'a\',\'b\',\'c\'), (\'a\',\'c\',\'b\')]
        sage: list(PermutationGroup([[\'b\',\'c\',\'a\']], domain=[\'b\',\'c\',\'a\']))
        [()]
        sage: list(PermutationGroup([[\'b\',\'c\',\'a\']], domain=[\'a\',\'c\',\'b\']))
        [(), (\'a\',\'b\')]

    There is an underlying gap object that implements each
    permutation group::

        sage: G = PermutationGroup([[(1,2,3,4)]])
        sage: G._gap_()
        Group( [ (1,2,3,4) ] )
        sage: gap(G)
        Group( [ (1,2,3,4) ] )
        sage: gap(G) is G._gap_()
        True
        sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
        sage: current_randstate().set_seed_gap()
        sage: G1, G2 = G._gap_().DerivedSeries()
        sage: G1
        Group( [ (3,4), (1,2,3)(4,5) ] )
        sage: G2.GeneratorsSmallest()
        [ (3,4,5), (2,3)(4,5), (1,2)(4,5) ]

    We can create a permutation group from a group action::

        sage: a = lambda x: (2*x) % 7
        sage: H = PermutationGroup(action=a, domain=range(7))                           # needs sage.combinat
        sage: H.orbits()                                                                # needs sage.libs.pari
        ((0,), (1, 2, 4), (3, 6, 5))
        sage: H.gens()                                                                  # needs sage.libs.pari
        ((1,2,4), (3,6,5))

    Note that we provide generators for the acting group.  The
    permutation group we construct is its homomorphic image::

        sage: # needs sage.combinat
        sage: a = lambda g, x: vector(g*x, immutable=True)
        sage: X = [vector(x, immutable=True) for x in GF(3)^2]
        sage: G = SL(2,3); G.gens()
        (
        [1 1]  [0 1]
        [0 1], [2 0]
        )
        sage: H = PermutationGroup(G.gens(), action=a, domain=X)
        sage: H.orbits()
        (((0, 0),), ((1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)))
        sage: H.gens()
        (((0,1),(1,1),(2,1))((0,2),(2,2),(1,2)),
         ((1,0),(0,2),(2,0),(0,1))((1,1),(1,2),(2,2),(2,1)))

    The orbits of the conjugation action are the conjugacy classes,
    i.e., in bijection with integer partitions::

        sage: a = lambda g, x: g*x*g^-1
        sage: [len(PermutationGroup(SymmetricGroup(n).gens(), action=a,                 # needs sage.combinat
        ....:                       domain=SymmetricGroup(n)).orbits())
        ....:  for n in range(1, 8)]
        [1, 2, 3, 5, 7, 11, 15]

    TESTS::

        sage: r = Permutation("(1,7,9,3)(2,4,8,6)")
        sage: f = Permutation("(1,3)(4,6)(7,9)")
        sage: PermutationGroup([r,f]) #See Issue #12597
        Permutation Group with generators [(1,3)(4,6)(7,9), (1,7,9,3)(2,4,8,6)]

        sage: PermutationGroup(SymmetricGroup(5))
        Traceback (most recent call last):
        ...
        TypeError: gens must be a tuple, list, or GapElement

    This now raises an error (:issue:`31510`)::

        sage: G = PermutationGroup([(1,2,3,4)], [(1,7,3,5)])
        Traceback (most recent call last):
        ...
        ValueError: please use keywords gap_group=, domain=, canonicalize=, category= in the input
    '''

class PermutationGroup_generic(FiniteGroup):
    """
    A generic permutation group.

    EXAMPLES::

        sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
        sage: G
        Permutation Group with generators [(3,4), (1,2,3)(4,5)]
        sage: G.center()
        Subgroup generated by [()] of
         (Permutation Group with generators [(3,4), (1,2,3)(4,5)])
        sage: G.group_id()
        [120, 34]
        sage: n = G.order(); n
        120
        sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
        sage: TestSuite(G).run()
    """
    def __init__(self, gens=None, gap_group=None, canonicalize: bool = True, domain=None, category=None) -> None:
        '''
        Initialize ``self``.

        INPUT:

        - ``gens`` -- list of generators (default: ``None``)

        - ``gap_group`` -- a gap or libgap permutation group, or a string
          defining one (default: ``None``)

        - ``canonicalize`` -- boolean (default: ``True``); if ``True``,
          sort generators and remove duplicates

        OUTPUT: a permutation group

        EXAMPLES:

        We explicitly construct the alternating group on four
        elements::

            sage: A4 = PermutationGroup([[(1,2,3)],[(2,3,4)]]); A4
            Permutation Group with generators [(2,3,4), (1,2,3)]
            sage: A4.__init__([[(1,2,3)],[(2,3,4)]]); A4
            Permutation Group with generators [(2,3,4), (1,2,3)]
            sage: A4.center()
            Subgroup generated by [()] of (Permutation Group with generators [(2,3,4), (1,2,3)])
            sage: A4.category()
            Category of finite enumerated permutation groups
            sage: TestSuite(A4).run()

        TESTS::

            sage: TestSuite(PermutationGroup([[]])).run()
            sage: TestSuite(PermutationGroup([])).run()
            sage: TestSuite(PermutationGroup([(0,1)])).run()

        Check that :issue:`37590` is fixed::

            sage: lgg = libgap.eval("Group((1,2,3,4,5),(4,5,6))")
            sage: P = PermutationGroup(gap_group=lgg)
            sage: h = P.hom(codomain=P, im_gens=P.gens())
            sage: h
            Group endomorphism of Permutation Group with generators [(1,2,3,4,5), (4,5,6)]
            sage: P.gens()
            ((1,2,3,4,5), (4,5,6))
            sage: P.gap().GeneratorsOfGroup()
            [ (1,2,3,4,5), (4,5,6) ]

            sage: gg = gap.eval("Group((1,2,3,4,5),(4,5,6))")
            sage: P = PermutationGroup(gap_group=gg)
            sage: P.gens()
            ((1,2,3,4,5), (4,5,6))
            sage: h = P.hom(codomain=P, im_gens=P.gens())
            sage: h
            Group endomorphism of Permutation Group with generators [(1,2,3,4,5), (4,5,6)]
        '''
    def __copy__(self):
        '''
        Return a "copy" of ``self`` by returning ``self``.

        EXAMPLES::

            sage: G = PermutationGroup(((1,2), (4,5)))
            sage: copy(G) is G
            True
        '''
    __deepcopy__ = __copy__
    def construction(self):
        """
        Return the construction of ``self``.

        EXAMPLES::

            sage: P1 = PermutationGroup([[(1,2)]])
            sage: P1.construction()
            (PermutationGroupFunctor[(1,2)], Permutation Group with generators [()])

            sage: PermutationGroup([]).construction() is None
            True

        This allows us to perform computations like the following::

            sage: P1 = PermutationGroup([[(1,2)]]); p1 = P1.gen()
            sage: P2 = PermutationGroup([[(1,3)]]); p2 = P2.gen()
            sage: p = p1*p2; p
            (1,2,3)
            sage: p.parent()
            Permutation Group with generators [(1,2), (1,3)]
            sage: p.parent().domain()
            {1, 2, 3}

        Note that this will merge permutation groups with different
        domains::

            sage: g1 = PermutationGroupElement([(1,2),(3,4,5)])
            sage: g2 = PermutationGroup([('a','b')], domain=['a', 'b']).gens()[0]
            sage: g2
            ('a','b')
            sage: p = g1*g2; p
            (1,2)(3,4,5)('a','b')
            sage: P = parent(p)
            sage: P
            Permutation Group with generators [('a','b'), (1,2), (1,2,3,4,5)]
        """
    @cached_method
    def gap(self):
        """
        This method from :class:`sage.groups.libgap_wrapper.ParentLibGAP` is added in order to achieve
        compatibility and have :class:`sage.groups.libgap_morphism.GroupHomset_libgap` work for permutation
        groups, as well

        OUTPUT: an instance of :class:`sage.libs.gap.element.GapElement`
        representing this group

        EXAMPLES::

            sage: P8 = PSp(8,3)
            sage: P8.gap()
            <permutation group of size 65784756654489600 with 2 generators>
            sage: gap(P8) == P8.gap()
            False
            sage: S3 = SymmetricGroup(3)
            sage: S3.gap()
            Sym( [ 1 .. 3 ] )
            sage: gap(S3) == S3.gap()
            False

        TESTS:

        see that this method does not harm pickling::

            sage: A4 = PermutationGroup([[(1,2,3)],[(2,3,4)]])
            sage: A4.gap()
            Group([ (2,3,4), (1,2,3) ])
            sage: TestSuite(A4).run()

        the following test shows, that support for the ``self._libgap``
        attribute is needed in the constructor of the class::

            sage: # needs sage.libs.pari
            sage: PG = PGU(6,2)
            sage: g, h = PG.gens()
            sage: p1 = h^-3*(h^-1*g^-1)^2*h*g*h^2*g^-1*h^2*g*h^-5*g^-1
            sage: p2 = g*(g*h)^2*g*h^-4*(g*h)^2*(h^2*g*h^-2*g)^2*h^-2*g*h^-2*g^-1*h^-1*g*h*g*h^-1*g
            sage: p3 = h^-3*g^-1*h*g*h^4*g^-1*h^-1*g*h*(h^2*g^-1)^2*h^-4*g*h^2*g^-1*h^-7*g^-2*h^-2*g*h^-2*g^-1*h^-1*(g*h)^2*h^3
            sage: p4 = h*(h^3*g)^2*h*g*h^-1*g*h^2*g^-1*h^-2*g*h^4*g^-1*h^3*g*h^-2*g*h^-1*g^-1*h^2*g*h*g^-1*h^-2*g*h*g^-1*h^2*g*h^2*g^-1
            sage: p5 = h^2*g*h^2*g^-1*h*g*h^-1*g*h*g^-1*h^2*g*h^-2*g*h^2*g*h^-2*(h^-1*g)^2*h^4*(g*h^-1)^2*g^-1
            sage: UPG = PG.subgroup([p1, p2, p3, p4, p5], canonicalize=False)
            sage: UPG.gap()
            <permutation group with 5 generators>

        the caching of _libgap_() works::

            sage: S = SymmetricGroup(4)
            sage: g1 = S._libgap_()
            sage: g1.IsIdenticalObj(S._libgap_())
            true
        """
    def __richcmp__(self, right, op):
        """
        Compare ``self`` and ``right``.

        The comparison extends the subgroup relation. Hence, it is first checked
        whether one of the groups is subgroup of the other. If this is not the
        case then the ordering is whatever it is in GAP.

        .. NOTE::

            The comparison does not provide a total ordering, as can be seen
            in the examples below.

        EXAMPLES::

            sage: G1 = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
            sage: G2 = PermutationGroup([[(1,2,3),(4,5)]])
            sage: G1 > G2 # since G2 is a subgroup of G1
            True
            sage: G1 < G2
            False

        The following example shows that the comparison does not yield a total
        ordering::

            sage: H1 = PermutationGroup([[(1,2)],[(5,6)]])
            sage: H2 = PermutationGroup([[(3,4)]])
            sage: H3 = PermutationGroup([[(1,2)]])
            sage: H1 < H2 # according to GAP's ordering
            True
            sage: H2 < H3 # according to GAP's ordering
            True
            sage: H3 < H1 # since H3 is a subgroup of H1
            True

        TESTS:

        Check that :issue:`29624` is fixed::

            sage: G = SymmetricGroup(2)
            sage: H = PermutationGroup([(1,2)])
            sage: not G == H
            False
            sage: G != H
            False
        """
    Element = PermutationGroupElement
    def list(self):
        '''
        Return list of all elements of this group.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3,4)], [(1,2)]])
            sage: G.list()
            [(), (1,4)(2,3), (1,2)(3,4), (1,3)(2,4), (2,4,3), (1,4,2),
             (1,2,3), (1,3,4), (2,3,4), (1,4,3), (1,2,4), (1,3,2), (3,4),
             (1,4,2,3), (1,2), (1,3,2,4), (2,4), (1,4,3,2), (1,2,3,4),
             (1,3), (2,3), (1,4), (1,2,4,3), (1,3,4,2)]

            sage: G = PermutationGroup([[(\'a\',\'b\')]], domain=(\'a\', \'b\')); G
            Permutation Group with generators [(\'a\',\'b\')]
            sage: G.list()
            [(), (\'a\',\'b\')]

        TESTS:

        Test :issue:`9155`::

            sage: G = SymmetricGroup(2)
            sage: elements = G.list()
            sage: elements.remove(G("()"))
            sage: elements
            [(1,2)]
            sage: G.list()
            [(), (1,2)]
        '''
    def __contains__(self, item) -> bool:
        """
        Return whether ``item`` is an element of this group.

        EXAMPLES::

            sage: G = SymmetricGroup(16)
            sage: g = G.gen(0)
            sage: h = G.gen(1)
            sage: g^7*h*g*h in G
            True
            sage: G = SymmetricGroup(4)
            sage: g = G((1,2,3,4))
            sage: h = G((1,2))
            sage: H = PermutationGroup([[(1,2,3,4)], [(1,2),(3,4)]])
            sage: g in H
            True
            sage: h in H
            False

            sage: G = PermutationGroup([[('a','b')]], domain=('a', 'b'))
            sage: [('a', 'b')] in G
            True

            sage: G = CyclicPermutationGroup(4)
            sage: H = DihedralGroup(4)
            sage: g = G([(1,2,3,4)]); g
            (1,2,3,4)
            sage: g in H
            True
        """
    def __iter__(self):
        """
        Return an iterator going through all elements in ``self``.

        For options and faster iteration see :meth:`iteration`.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3,4)], [(1,2)]])
            sage: [g for g in G]
            [(), (1,4)(2,3), (1,2)(3,4), (1,3)(2,4), (2,4,3), (1,4,2),
             (1,2,3), (1,3,4), (2,3,4), (1,4,3), (1,2,4), (1,3,2), (3,4),
             (1,4,2,3), (1,2), (1,3,2,4), (2,4), (1,4,3,2), (1,2,3,4),
             (1,3), (2,3), (1,4), (1,2,4,3), (1,3,4,2)]

            sage: G = PermutationGroup([('A','B'),('B','C')])
            sage: [g for g in G]
            [(), ('A','B','C'), ('A','C','B'), ('B','C'), ('A','B'), ('A','C')]

            sage: G = SymmetricGroup(5).subgroup([])
            sage: list(G)
            [()]

            sage: G = SymmetricGroup(5).subgroup(['(1,2,3)(4,5)'])
            sage: list(G)
            [(), (1,2,3)(4,5), (1,3,2), (4,5), (1,2,3), (1,3,2)(4,5)]
        """
    def iteration(self, algorithm: str = 'SGS'):
        """
        Return an iterator over the elements of this group.

        INPUT:

        - ``algorithm`` -- (default: ``'SGS'``) either

          * ``'SGS'`` -- using strong generating system
          * ``'BFS'`` -- a breadth first search on the Cayley graph with
            respect to ``self.gens()``
          * ``'DFS'`` -- a depth first search on the Cayley graph with
            respect to ``self.gens()``

        .. NOTE::

            In general, the algorithm ``'SGS'`` is faster. Yet, for
            small groups, ``'BFS'`` and ``'DFS'`` might be faster.

        .. NOTE::

            The order in which the iterator visits the elements differs
            in the algorithms.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2)], [(2,3)]])

            sage: list(G.iteration())
            [(), (1,2,3), (1,3,2), (2,3), (1,2), (1,3)]

            sage: list(G.iteration(algorithm='BFS'))
            [(), (2,3), (1,2), (1,2,3), (1,3,2), (1,3)]

            sage: list(G.iteration(algorithm='DFS'))
            [(), (1,2), (1,3,2), (1,3), (1,2,3), (2,3)]

        TESTS::

            sage: p = [(i,i+1) for i in range(1,601,2)]
            sage: q = [tuple(range(1+i,601,3)) for i in range(3)]
            sage: A = PermutationGroup([p,q])
            sage: A.cardinality()
            60000

            sage: sum(1 for x in A.iteration()) == 60000
            True
            sage: sum(1 for x in A.iteration(algorithm='BFS')) == 60000
            True
            sage: sum(1 for x in A.iteration(algorithm='DFS')) == 60000
            True
        """
    def gens(self) -> tuple:
        """
        Return tuple of generators of this group.

        These need not be
        minimal, as they are the generators used in defining this group.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3)], [(1,2)]])
            sage: G.gens()
            ((1,2), (1,2,3))

        Note that the generators need not be minimal, though duplicates are
        removed::

            sage: G = PermutationGroup([[(1,2)], [(1,3)], [(2,3)], [(1,2)]])
            sage: G.gens()
            ((2,3), (1,2), (1,3))

        We can use index notation to access the generators returned by
        ``self.gens``::

            sage: G = PermutationGroup([[(1,2,3,4), (5,6)], [(1,2)]])
            sage: g = G.gens()
            sage: g[0]
            (1,2)
            sage: g[1]
            (1,2,3,4)(5,6)

        TESTS:

        We make sure that the trivial group gets handled correctly::

            sage: SymmetricGroup(1).gens()
            ()
        """
    def gens_small(self):
        '''
        For this group, returns a generating set which has few elements.

        As neither irredundancy nor minimal length is proven, it is fast.

        EXAMPLES::

            sage: R = "(25,27,32,30)(26,29,31,28)( 3,38,43,19)( 5,36,45,21)( 8,33,48,24)" ## R = right
            sage: U = "( 1, 3, 8, 6)( 2, 5, 7, 4)( 9,33,25,17)(10,34,26,18)(11,35,27,19)" ## U = top
            sage: L = "( 9,11,16,14)(10,13,15,12)( 1,17,41,40)( 4,20,44,37)( 6,22,46,35)" ## L = left
            sage: F = "(17,19,24,22)(18,21,23,20)( 6,25,43,16)( 7,28,42,13)( 8,30,41,11)" ## F = front
            sage: B = "(33,35,40,38)(34,37,39,36)( 3, 9,46,32)( 2,12,47,29)( 1,14,48,27)" ## B = back or rear
            sage: D = "(41,43,48,46)(42,45,47,44)(14,22,30,38)(15,23,31,39)(16,24,32,40)" ## D = down or bottom
            sage: G = PermutationGroup([R,L,U,F,B,D])
            sage: len(G.gens_small())
            2

        The output may be unpredictable, due to the use of randomized
        algorithms in GAP. Note that both the following answers are equally valid.

        ::

            sage: G = PermutationGroup([[(\'a\',\'b\')], [(\'b\', \'c\')], [(\'a\', \'c\')]])
            sage: G.gens_small() # random
            [(\'b\',\'c\'), (\'a\',\'c\',\'b\')] ## (on 64-bit Linux)
            [(\'a\',\'b\'), (\'a\',\'c\',\'b\')] ## (on Solaris)
            sage: len(G.gens_small()) == 2 # random
            True
        '''
    def gen(self, i=None):
        """
        Return the `i`-th generator of ``self``; that is, the `i`-th element of
        the list ``self.gens()``.

        The argument `i` may be omitted if there is only one generator (but
        this will raise an error otherwise).

        EXAMPLES:

        We explicitly construct the alternating group on four
        elements::

            sage: A4 = PermutationGroup([[(1,2,3)],[(2,3,4)]]); A4
            Permutation Group with generators [(2,3,4), (1,2,3)]
            sage: A4.gens()
            ((2,3,4), (1,2,3))
            sage: A4.gen(0)
            (2,3,4)
            sage: A4.gen(1)
            (1,2,3)
            sage: A4.gens()[0]; A4.gens()[1]
            (2,3,4)
            (1,2,3)

            sage: P1 = PermutationGroup([[(1,2)]]); P1.gen()
            (1,2)
        """
    def ngens(self):
        """
        Return the number of generators of ``self``.

        EXAMPLES::

            sage: A4 = PermutationGroup([[(1,2,3)], [(2,3,4)]]); A4
            Permutation Group with generators [(2,3,4), (1,2,3)]
            sage: A4.ngens()
            2
        """
    def is_trivial(self):
        '''
        Return ``True`` if this group is the trivial group.

        A permutation group is trivial, if it consists only of the
        identity element, that is, if it has no generators or only
        trivial generators.

        EXAMPLES::

            sage: G = PermutationGroup([], domain=["a", "b", "c"])
            sage: G.is_trivial()
            True
            sage: SymmetricGroup(0).is_trivial()
            True
            sage: SymmetricGroup(1).is_trivial()
            True
            sage: SymmetricGroup(2).is_trivial()
            False
            sage: DihedralGroup(1).is_trivial()
            False

        TESTS::

            sage: G = PermutationGroup([[], []], canonicalize=False)
            sage: G.ngens()
            2
            sage: G.is_trivial()
            True
        '''
    @cached_method
    def one(self):
        """
        Return the identity element of this group.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3),(4,5)]])
            sage: e = G.identity(); e                       # indirect doctest
            ()
            sage: g = G.gen(0)
            sage: g*e
            (1,2,3)(4,5)
            sage: e*g
            (1,2,3)(4,5)

            sage: S = SymmetricGroup(['a','b','c'])
            sage: S.identity()
            ()
        """
    identity = one
    def exponent(self):
        """
        Compute the exponent of the group.

        The exponent `e` of a group `G` is the LCM of the orders of its
        elements, that is, `e` is the smallest integer such that `g^e=1` for all
        `g \\in G`.

        EXAMPLES::

            sage: G = AlternatingGroup(4)
            sage: G.exponent()
            6
        """
    def largest_moved_point(self):
        """
        Return the largest point moved by a permutation in this group.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4)]])
            sage: G.largest_moved_point()
            4
            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4,10)]])
            sage: G.largest_moved_point()
            10

        ::

            sage: G = PermutationGroup([[('a','b','c'),('d','e')]])
            sage: G.largest_moved_point()
            'e'

        .. WARNING::

           The name of this function is not good; this function
           should be deprecated in term of degree::

                sage: P = PermutationGroup([[1,2,3,4]])
                sage: P.largest_moved_point()
                4
                sage: P.cardinality()
                1
        """
    def degree(self):
        """
        Return the degree of this permutation group.

        EXAMPLES::

            sage: S = SymmetricGroup(['a','b','c'])
            sage: S.degree()
            3
            sage: G = PermutationGroup([(1,3),(4,5)])
            sage: G.degree()
            5

        Note that you can explicitly specify the domain to get a
        permutation group of smaller degree::

            sage: G = PermutationGroup([(1,3),(4,5)], domain=[1,3,4,5])
            sage: G.degree()
            4
        """
    def domain(self):
        """
        Return the underlying set that this permutation group acts
        on.

        EXAMPLES::

            sage: P = PermutationGroup([(1,2),(3,5)])
            sage: P.domain()
            {1, 2, 3, 4, 5}
            sage: S = SymmetricGroup(['a', 'b', 'c'])
            sage: S.domain()
            {'a', 'b', 'c'}
        """
    @cached_method
    def smallest_moved_point(self):
        """
        Return the smallest point moved by a permutation in this group.

        EXAMPLES::

            sage: G = PermutationGroup([[(3,4)], [(2,3,4)]])
            sage: G.smallest_moved_point()
            2
            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4,10)]])
            sage: G.smallest_moved_point()
            1

        Note that this function uses the ordering from the domain::

            sage: S = SymmetricGroup(['a','b','c'])
            sage: S.smallest_moved_point()
            'a'
        """
    @cached_method
    def disjoint_direct_product_decomposition(self):
        '''
        Return the finest partition of the underlying set such that ``self``
        is isomorphic to the direct product of the projections of ``self``
        onto each part of the partition. Each part is a union of orbits
        of ``self``.

        The algorithm is from [CJ2022]_, which runs in time polynomial in
        `n \\cdot |X|`, where `n` is the degree of the group and `|X|` is
        the size of a generating set, see Theorem 4.5.

        EXAMPLES:

        The example from the original paper::

            sage: H = PermutationGroup([[(1,2,3),(7,9,8),(10,12,11)],[(4,5,6),(7,8,9),(10,11,12)],[(5,6),(8,9),(11,12)],[(7,8,9),(10,11,12)]])
            sage: S = H.disjoint_direct_product_decomposition(); S
            {{1, 2, 3}, {4, 5, 6, 7, 8, 9, 10, 11, 12}}
            sage: A = libgap.Stabilizer(H, list(S[0]), libgap.OnTuples); A
            Group([ (7,8,9)(10,11,12), (5,6)(8,9)(11,12), (4,5,6)(7,8,9)(10,11,12) ])
            sage: B = libgap.Stabilizer(H, list(S[1]), libgap.OnTuples); B
            Group([ (1,2,3) ])
            sage: T = PermutationGroup(gap_group=libgap.DirectProduct(A,B))
            sage: T.is_isomorphic(H)
            True
            sage: PermutationGroup(PermutationGroup(gap_group=A).gens(),domain=list(S[1])).disjoint_direct_product_decomposition()
            {{4, 5, 6, 7, 8, 9, 10, 11, 12}}
            sage: PermutationGroup(PermutationGroup(gap_group=B).gens(),domain=list(S[0])).disjoint_direct_product_decomposition()
            {{1, 2, 3}}

        An example with a different domain::

            sage: PermutationGroup([[(\'a\',\'c\',\'d\'),(\'b\',\'e\')]]).disjoint_direct_product_decomposition()
            {{\'a\', \'c\', \'d\'}, {\'b\', \'e\'}}
            sage: PermutationGroup([[(\'a\',\'c\',\'d\',\'b\',\'e\')]]).disjoint_direct_product_decomposition()
            {{\'a\', \'b\', \'c\', \'d\', \'e\'}}

        Counting the number of "connected" permutation groups of degree `n`::

            sage: seq = [sum(1 for G in SymmetricGroup(n).conjugacy_classes_subgroups() if len(G.disjoint_direct_product_decomposition()) == 1) for n in range(1,8)]; seq
            [1, 1, 2, 6, 6, 27, 20]
            sage: oeis(seq) # optional -- internet
            0: A005226: Number of atomic species of degree n; also number of connected permutation groups of degree n.
        '''
    def representative_action(self, x, y):
        '''
        Return an element of ``self`` that maps `x` to `y` if it exists.

        This method wraps the gap function ``RepresentativeAction``, which can
        also return elements that map a given set of points on another set of
        points.

        INPUT:

        - ``x``, ``y`` -- two elements of the domain

        EXAMPLES::

            sage: G = groups.permutation.Cyclic(14)
            sage: g = G.representative_action(1, 10)
            sage: all(g(x) == 1 + ((x+9-1)%14) for x in G.domain())
            True

        TESTS::

            sage: # needs sage.graphs
            sage: g = graphs.PetersenGraph()
            sage: g.relabel(list("abcdefghik"))
            sage: g.vertices(sort=True)
            [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\', \'g\', \'h\', \'i\', \'k\']
            sage: ag = g.automorphism_group()
            sage: a = ag.representative_action(\'a\',\'b\')
            sage: g == g.relabel(a,inplace=False)
            True
            sage: a(\'a\') == \'b\'
            True
        '''
    @cached_method
    def orbits(self):
        """
        Return the orbits of the elements of the domain under the
        default group action.

        EXAMPLES::

            sage: G = PermutationGroup([ [(3,4)], [(1,3)] ])
            sage: G.orbits()
            ((1, 3, 4), (2,))
            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4,10)]])
            sage: G.orbits()
            ((1, 2, 3, 4, 10), (5,), (6,), (7,), (8,), (9,))

            sage: G = PermutationGroup([ [('c','d')], [('a','c')],[('b',)]])
            sage: G.orbits()
            (('a', 'c', 'd'), ('b',))

        The answer is cached::

            sage: G.orbits() is G.orbits()
            True

        AUTHORS:

        - Nathan Dunfield
        """
    @cached_method
    def orbit(self, point, action: str = 'OnPoints'):
        '''
        Return the orbit of a point under a group action.

        INPUT:

        - ``point`` -- can be a point or any of the list above, depending on the
          action to be considered

        - ``action`` -- string; if ``point`` is an element from the domain, a
          tuple of elements of the domain, a tuple of tuples [...], this
          variable describes how the group is acting

          The actions currently available through this method are
          ``\'OnPoints\'``, ``\'OnTuples\'``, ``\'OnSets\'``, ``\'OnPairs\'``,
          ``\'OnSetsSets\'``, ``\'OnSetsDisjointSets\'``,
          ``\'OnSetsTuples\'``, ``\'OnTuplesSets\'``,
          ``\'OnTuplesTuples\'``. They are taken from GAP\'s list of
          group actions, see ``gap.help(\'Group Actions\')``.

          It is set to ``\'OnPoints\'`` by default. See below for examples.

        OUTPUT:

        The orbit of ``point`` as a tuple. Each entry is an image
        under the action of the permutation group, if necessary
        converted to the corresponding container. That is, if
        ``action=\'OnSets\'`` then each entry will be a set even if
        ``point`` was given by a list/tuple/iterable.

        EXAMPLES::

            sage: G = PermutationGroup([ [(3,4)], [(1,3)] ])
            sage: G.orbit(3)
            (3, 4, 1)
            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4,10)]])
            sage: G.orbit(3)
            (3, 4, 10, 1, 2)
            sage: G = PermutationGroup([ [(\'c\',\'d\')], [(\'a\',\'c\')] ])
            sage: G.orbit(\'a\')
            (\'a\', \'c\', \'d\')

        Action of `S_3` on sets::

            sage: S3 = groups.permutation.Symmetric(3)
            sage: S3.orbit((1,2), action = "OnSets")
            ({1, 2}, {2, 3}, {1, 3})

        On tuples::

            sage: S3.orbit((1,2), action = "OnTuples")
            ((1, 2), (2, 3), (2, 1), (3, 1), (1, 3), (3, 2))

        Action of `S_4` on sets of disjoint sets::

            sage: S4 = groups.permutation.Symmetric(4)
            sage: O = S4.orbit(((1,2),(3,4)), action=\'OnSetsDisjointSets\')
            sage: {1, 2} in O[0] and {3, 4} in O[0]
            True
            sage: {1, 4} in O[1] and {2, 3} in O[1]
            True
            sage: all(x[0].union(x[1]) == {1,2,3,4} for x in O)
            True

        Action of `S_4` (on a nonstandard domain) on tuples of sets::

            sage: S4 = PermutationGroup([ [(\'c\',\'d\')], [(\'a\',\'c\')], [(\'a\',\'b\')] ])
            sage: orb = S4.orbit(((\'a\',\'c\'),(\'b\',\'d\')), "OnTuplesSets")
            sage: expect = (({\'a\', \'c\'}, {\'b\', \'d\'}), ({\'a\', \'d\'}, {\'c\', \'b\'}),
            ....:           ({\'c\', \'b\'}, {\'a\', \'d\'}), ({\'b\', \'d\'}, {\'a\', \'c\'}),
            ....:           ({\'c\', \'d\'}, {\'a\', \'b\'}), ({\'a\', \'b\'}, {\'c\', \'d\'}))
            sage: expect == orb
            True

        Action of `S_4` (on a very nonstandard domain) on tuples of sets::

            sage: S4 = PermutationGroup([ [((11,(12,13)),\'d\')],
            ....:         [((12,(12,11)),(11,(12,13)))], [((12,(12,11)),\'b\')] ])
            sage: orb = S4.orbit((( (11,(12,13)), (12,(12,11))),(\'b\',\'d\')),
            ....:                "OnTuplesSets")
            sage: expect = (({(11, (12, 13)), (12, (12, 11))}, {\'b\', \'d\'}),
            ....:           ({\'d\', (12, (12, 11))}, {(11, (12, 13)), \'b\'}),
            ....:           ({(11, (12, 13)), \'b\'}, {\'d\', (12, (12, 11))}),
            ....:           ({(11, (12, 13)), \'d\'}, {\'b\', (12, (12, 11))}),
            ....:           ({\'b\', \'d\'}, {(11, (12, 13)), (12, (12, 11))}),
            ....:           ({\'b\', (12, (12, 11))}, {(11, (12, 13)), \'d\'}))
            sage: all(x in orb for x in expect) and len(orb) == len(expect)
            True
        '''
    def transversals(self, point):
        """
        If G is a permutation group acting on the set `X = \\{1, 2, ...., n\\}`
        and H is the stabilizer subgroup of <integer>, a right
        (respectively left) transversal is a set containing exactly
        one element from each right (respectively left) coset of H. This
        method returns a right transversal of ``self`` by the stabilizer
        of ``self`` on <integer> position.

        EXAMPLES::

            sage: G = PermutationGroup([ [(3,4)], [(1,3)] ])
            sage: G.transversals(1)
            [(), (1,3,4), (1,4,3)]
            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4,10)]])
            sage: G.transversals(1)
            [(), (1,2)(3,4), (1,3,2,10,4), (1,4,2,10,3), (1,10,4,3,2)]

            sage: G = PermutationGroup([ [('c','d')], [('a','c')] ])
            sage: G.transversals('a')
            [(), ('a','c','d'), ('a','d','c')]
        """
    def stabilizer(self, point, action: str = 'OnPoints'):
        '''
        Return the subgroup of ``self`` which stabilize the given position.
        ``self`` and its stabilizers must have same degree.

        INPUT:

        - ``point`` -- a point of the :meth:`domain`, or a set of points
          depending on the value of ``action``

        - ``action`` -- string (default: ``\'OnPoints\'``); should the group be
          considered to act on points (``action="OnPoints"``) or on sets of
          points (``action="OnSets"``)? In the latter case, the first argument
          must be a subset of :meth:`domain`.

        EXAMPLES::

            sage: G = PermutationGroup([ [(3,4)], [(1,3)] ])
            sage: G.stabilizer(1)
            Subgroup generated by [(3,4)] of (Permutation Group with generators [(3,4), (1,3)])
            sage: G.stabilizer(3)
            Subgroup generated by [(1,4)] of (Permutation Group with generators [(3,4), (1,3)])

        The stabilizer of a set of points::

            sage: s10 = groups.permutation.Symmetric(10)
            sage: s10.stabilizer([1..3],"OnSets").cardinality()
            30240
            sage: factorial(3)*factorial(7)
            30240

        ::

            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4,10)]])
            sage: G.stabilizer(10)
            Subgroup generated by [(1,2)(3,4), (2,3,4)] of (Permutation Group with generators [(1,2)(3,4), (1,2,3,4,10)])
            sage: G.stabilizer(1) == G.subgroup([\'(2,3)(4,10)\', \'(2,10,3)\'])
            True
            sage: G = PermutationGroup([[(2,3,4)],[(6,7)]])
            sage: G.stabilizer(1)
            Subgroup generated by [(6,7), (2,3,4)] of (Permutation Group with generators [(6,7), (2,3,4)])
            sage: G.stabilizer(2)
            Subgroup generated by [(6,7)] of (Permutation Group with generators [(6,7), (2,3,4)])
            sage: G.stabilizer(3)
            Subgroup generated by [(6,7)] of (Permutation Group with generators [(6,7), (2,3,4)])
            sage: G.stabilizer(4)
            Subgroup generated by [(6,7)] of (Permutation Group with generators [(6,7), (2,3,4)])
            sage: G.stabilizer(5)
            Subgroup generated by [(6,7), (2,3,4)] of (Permutation Group with generators [(6,7), (2,3,4)])
            sage: G.stabilizer(6)
            Subgroup generated by [(2,3,4)] of (Permutation Group with generators [(6,7), (2,3,4)])
            sage: G.stabilizer(7)
            Subgroup generated by [(2,3,4)] of (Permutation Group with generators [(6,7), (2,3,4)])
            sage: G.stabilizer(8)
            Traceback (most recent call last):
            ...
            ValueError: 8 does not belong to the domain

        ::

            sage: G = PermutationGroup([ [(\'c\',\'d\')], [(\'a\',\'c\')] ], domain=\'abcd\')
            sage: G.stabilizer(\'a\')
            Subgroup generated by [(\'c\',\'d\')] of (Permutation Group with generators [(\'c\',\'d\'), (\'a\',\'c\')])
            sage: G.stabilizer(\'b\')
            Subgroup generated by [(\'c\',\'d\'), (\'a\',\'c\')] of (Permutation Group with generators [(\'c\',\'d\'), (\'a\',\'c\')])
            sage: G.stabilizer(\'c\')
            Subgroup generated by [(\'a\',\'d\')] of (Permutation Group with generators [(\'c\',\'d\'), (\'a\',\'c\')])
            sage: G.stabilizer(\'d\')
            Subgroup generated by [(\'a\',\'c\')] of (Permutation Group with generators [(\'c\',\'d\'), (\'a\',\'c\')])

        TESTS::

            sage: G.stabilizer([\'a\'],"OnMonkeys")
            Traceback (most recent call last):
            ...
            ValueError: \'action\' must be equal to \'OnPoints\' or to \'OnSets\'
        '''
    def base(self, seed=None):
        """
        Return a (minimum) base of this permutation group.

        A base `B` of a permutation group is a subset of the domain
        of the group such that the only group element stabilizing all
        of `B` is the identity.

        INPUT:

        - ``seed`` -- (default: ``None``) if given must be a
          subset of the domain of a base.  When used, an attempt to
          create a base containing all or part of ``seed`` will be
          made.

        EXAMPLES::

            sage: G = PermutationGroup([(1,2,3),(6,7,8)])
            sage: G.base()
            [1, 6]
            sage: G.base([2])
            [2, 6]

            sage: H = PermutationGroup([('a','b','c'),('a','y')])
            sage: H.base()
            ['a', 'b', 'c']

            sage: S = SymmetricGroup(13)
            sage: S.base()
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

            sage: S = MathieuGroup(12)
            sage: S.base()
            [1, 2, 3, 4, 5]
            sage: S.base([1,3,5,7,9,11]) # create a base for M12 with only odd integers
            [1, 3, 5, 7, 9]
        """
    def strong_generating_system(self, base_of_group=None, implementation: str = 'sage'):
        """
        Return a Strong Generating System of ``self`` according the given
        base for the right action of ``self`` on itself.

        ``base_of_group`` is a list of the  positions on which ``self`` acts,
        in any order. The algorithm returns a list of transversals and each
        transversal is a list of permutations. By default, ``base_of_group``
        is ``[1, 2, 3, ..., d]`` where `d` is the degree of the group.

        For ``base_of_group`` =
        `[ \\mathrm{pos}_1, \\mathrm{pos}_2, \\dots , \\mathrm{pos}_d]`
        let `G_i` be the subgroup of `G` = ``self`` which stabilizes
        `\\mathrm{pos}_1, \\mathrm{pos}_2, \\dots , \\mathrm{pos}_i`, so

        .. MATH::

           G = G_0 \\supset G_1 \\supset G_2 \\supset \\dots \\supset G_n = \\{e\\}

        Then the algorithm returns `[ G_i.\\mathrm{transversals}(\\mathrm{pos}_{i+1})]_{1 \\leq i \\leq n}`

        INPUT:

        - ``base_of_group`` -- (default: ``[1, 2, 3, ..., d]``)
          a list containing the integers `1, 2, \\ldots , d` in any order,
          where `d` is the degree of ``self``

        - ``implementation`` -- (default: ``'sage'``) either

          * ``'sage'`` -- use the direct implementation in Sage

          * ``'gap'`` -- if used, the ``base_of_group`` must be ``None``
            and the computation is directly performed in GAP

        OUTPUT: list of lists of permutations from the group, which forms a
        strong generating system

        .. WARNING::

            The outputs for implementations ``'sage'`` and ``'gap'`` differ:
            First, the output is reversed, and second, it might be that
            ``'sage'`` does not contain the trivial subgroup while ``'gap'``
            does.

            Also, both algorithms might yield different results based on the
            order in which ``base_of_group`` is given in the first situation.

        EXAMPLES::

            sage: G = PermutationGroup([[(7,8)],[(3,4)],[(4,5)]])
            sage: G.strong_generating_system()
            [[()], [()], [(), (3,4), (3,5,4)], [(), (4,5)], [()], [()], [(), (7,8)], [()]]
            sage: G = PermutationGroup([[(1,2,3,4)],[(1,2)]])
            sage: G.strong_generating_system()
            [[(), (1,2)(3,4), (1,3)(2,4), (1,4)(2,3)],
            [(), (2,4,3), (2,3,4)],
            [(), (3,4)],
            [()]]
            sage: G = PermutationGroup([[(1,2,3)],[(4,5,7)],[(1,4,6)]])
            sage: G.strong_generating_system()
            [[(), (1,2,3), (1,4,6), (1,3,2), (1,5,7,4,6), (1,6,4), (1,7,5,4,6)],
             [(), (2,3,6), (2,6,3), (2,7,5,6,3), (2,5,6,3)(4,7), (2,4,5,6,3)],
             [(), (3,5,6), (3,4,7,5,6), (3,6)(5,7), (3,7,4,5,6)],
             [(), (4,7,5), (4,5,7), (4,6,7)],
             [(), (5,6,7), (5,7,6)], [()], [()]]
            sage: G = PermutationGroup([[(1,2,3)],[(2,3,4)],[(3,4,5)]])
            sage: G.strong_generating_system([5,4,3,2,1])
            [[(), (1,5,3,4,2), (1,5,4,3,2), (1,5)(2,3), (1,5,2)],
             [(1,4)(2,3), (1,4,3), (1,4,2), ()],
             [(1,2,3), (1,3,2), ()], [()], [()]]
            sage: G = PermutationGroup([[(3,4)]])
            sage: G.strong_generating_system()
            [[()], [()], [(), (3,4)], [()]]
            sage: G.strong_generating_system(base_of_group=[3,1,2,4])
            [[(), (3,4)], [()], [()], [()]]
            sage: G = TransitiveGroup(12,17)
            sage: G.strong_generating_system()
            [[(), (1,4,11,2)(3,6,5,8)(7,10,9,12), (1,8,3,2)(4,11,10,9)(5,12,7,6),
              (1,7)(2,8)(3,9)(4,10)(5,11)(6,12), (1,12,7,2)(3,10,9,8)(4,11,6,5),
              (1,11)(2,8)(3,5)(4,10)(6,12)(7,9), (1,10,11,8)(2,3,12,5)(4,9,6,7),
              (1,3)(2,8)(4,10)(5,7)(6,12)(9,11), (1,2,3,8)(4,9,10,11)(5,6,7,12),
              (1,6,7,8)(2,3,4,9)(5,10,11,12), (1,5,9)(3,11,7), (1,9,5)(3,7,11)],
             [(), (2,6,10)(4,12,8), (2,10,6)(4,8,12)],
             [()], [()], [()], [()], [()], [()], [()], [()], [()], [()]]

            sage: A = PermutationGroup([(1,2),(1,2,3,4,5,6,7,8,9)])
            sage: X = A.strong_generating_system()
            sage: Y = A.strong_generating_system(implementation='gap')
            sage: [len(x) for x in X]
            [9, 8, 7, 6, 5, 4, 3, 2, 1]
            sage: [len(y) for y in Y]
            [1, 2, 3, 4, 5, 6, 7, 8, 9]

        TESTS::

            sage: G = SymmetricGroup(10)
            sage: H = PermutationGroup([G.random_element() for i in range(randrange(1,3,1))])
            sage: prod(len(x) for x in H.strong_generating_system()) == H.cardinality()
            True
        """
    def order(self):
        """
        Return the number of elements of this group.

        See also: :meth:`degree`.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3),(4,5)], [(1,2)]])
            sage: G.order()
            12
            sage: G = PermutationGroup([()])
            sage: G.order()
            1
            sage: G = PermutationGroup([])
            sage: G.order()
            1

        :meth:`cardinality` is just an alias::

            sage: PermutationGroup([(1,2,3)]).cardinality()
            3
        """
    cardinality = order
    def random_element(self):
        """
        Return a random element of this group.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3),(4,5)], [(1,2)]])
            sage: a = G.random_element()
            sage: a in G
            True
            sage: a.parent() is G
            True
            sage: a^6
            ()
        """
    def group_id(self):
        """
        Return the ID code of this group, which is a list of two integers.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3),(4,5)], [(1,2)]])
            sage: G.group_id()
            [12, 4]
        """
    def id(self):
        """
        Return the ID code of this group, which is a list of two integers.

        Same as :meth:`group_id`.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3),(4,5)], [(1,2)]])
            sage: G.group_id()
            [12, 4]
        """
    def group_primitive_id(self):
        """
        Return the index of this group in the GAP database of primitive groups.

        OUTPUT:

        A positive integer, following GAP's conventions. A
        :exc:`ValueError` is raised if the group is not primitive.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3,4,5)], [(1,5),(2,4)]])
            sage: G.group_primitive_id()
            2
            sage: G.degree()
            5

        From the information of the degree and the identification number,
        you can recover the isomorphism class of your group in the GAP
        database::

            sage: H = PrimitiveGroup(5,2)
            sage: G == H
            False
            sage: G.is_isomorphic(H)
            True
        """
    def center(self):
        """
        Return the subgroup of elements that commute with every element
        of this group.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3,4)]])
            sage: G.center()
            Subgroup generated by [(1,2,3,4)] of
             (Permutation Group with generators [(1,2,3,4)])
            sage: G = PermutationGroup([[(1,2,3,4)], [(1,2)]])
            sage: G.center()
            Subgroup generated by [()] of
             (Permutation Group with generators [(1,2), (1,2,3,4)])
        """
    def socle(self):
        """
        Return the socle of ``self``.

        The socle of a group `G` is the subgroup generated by all
        minimal normal subgroups.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: s = G.socle(); s
            Subgroup generated by [(1,2)(3,4), (1,4)(2,3)] of
             (Symmetric group of order 4! as a permutation group)

        The socle of the socle is, essentially, the socle::

            sage: s.socle() == s.subgroup(s.gens())
            True
        """
    def frattini_subgroup(self):
        """
        Return the Frattini subgroup of ``self``.

        The Frattini subgroup of a group `G` is the intersection of all maximal
        subgroups of `G`.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3,4)],[(2,4)]])
            sage: G.frattini_subgroup()
            Subgroup generated by [(1,3)(2,4)] of
             (Permutation Group with generators [(2,4), (1,2,3,4)])
            sage: G = SymmetricGroup(4)
            sage: G.frattini_subgroup()
            Subgroup generated by [()] of
             (Symmetric group of order 4! as a permutation group)
        """
    def fitting_subgroup(self):
        """
        Return the Fitting subgroup of ``self``.

        The Fitting subgroup of a group `G` is the largest nilpotent normal
        subgroup of `G`.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3,4)],[(2,4)]])
            sage: G.fitting_subgroup()
            Subgroup generated by [(2,4), (1,2,3,4), (1,3)] of
             (Permutation Group with generators [(2,4), (1,2,3,4)])
            sage: G = PermutationGroup([[(1,2,3,4)],[(1,2)]])
            sage: G.fitting_subgroup()
            Subgroup generated by [(1,2)(3,4), (1,3)(2,4)] of
             (Permutation Group with generators [(1,2), (1,2,3,4)])
        """
    def solvable_radical(self):
        """
        Return the solvable radical of ``self``.

        The solvable radical (or just radical) of a group `G` is the
        largest solvable normal subgroup of `G`.

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: G.solvable_radical()
            Subgroup generated by [(1,2,3,4), (1,2)] of
             (Symmetric group of order 4! as a permutation group)
            sage: G = SymmetricGroup(5)
            sage: G.solvable_radical()
            Subgroup generated by [()] of
             (Symmetric group of order 5! as a permutation group)
        """
    def intersection(self, other):
        '''
        Return the permutation group that is the intersection of
        ``self`` and ``other``.

        INPUT:

        - ``other`` -- a permutation group

        OUTPUT:

        A permutation group that is the set-theoretic intersection of ``self``
        with ``other``.  The groups are viewed as subgroups of a symmetric
        group big enough to contain both group\'s symbol sets.  So there is
        no strict notion of the two groups being subgroups of a common parent.

        EXAMPLES::

            sage: H = DihedralGroup(4)

            sage: K = CyclicPermutationGroup(4)
            sage: H.intersection(K)
            Permutation Group with generators [(1,2,3,4)]

            sage: L = DihedralGroup(5)
            sage: H.intersection(L)
            Permutation Group with generators [(1,4)(2,3)]

            sage: M = PermutationGroup(["()"])
            sage: H.intersection(M)
            Permutation Group with generators [()]

        Some basic properties. ::

            sage: H = DihedralGroup(4)
            sage: L = DihedralGroup(5)
            sage: H.intersection(L) == L.intersection(H)
            True
            sage: H.intersection(H) == H
            True

        The group ``other`` is verified as such.  ::

            sage: H = DihedralGroup(4)
            sage: H.intersection(\'junk\')
            Traceback (most recent call last):
            ...
            TypeError: junk is not a permutation group
        '''
    def conjugacy_class(self, g):
        """
        Return the conjugacy class of ``g`` inside the group ``self``.

        INPUT:

        - ``g`` -- an element of the permutation group ``self``

        OUTPUT:

        The conjugacy class of ``g`` in the group ``self``. If ``self`` is
        the group denoted by `G`, this method computes the set
        `\\{x^{-1}gx\\ \\vert\\ x \\in G \\}`

        EXAMPLES::

            sage: G = DihedralGroup(3)
            sage: g = G.gen(0)
            sage: G.conjugacy_class(g)
            Conjugacy class of (1,2,3) in Dihedral group of order 6 as a permutation group
        """
    def conjugacy_classes(self):
        """
        Return a list with all the conjugacy classes of ``self``.

        EXAMPLES::

            sage: G = DihedralGroup(3)
            sage: G.conjugacy_classes()
            [Conjugacy class of () in Dihedral group of order 6 as a permutation group,
             Conjugacy class of (2,3) in Dihedral group of order 6 as a permutation group,
             Conjugacy class of (1,2,3) in Dihedral group of order 6 as a permutation group]
        """
    def conjugate(self, g):
        '''
        Return the group formed by conjugating ``self`` with ``g``.

        INPUT:

        - ``g`` -- a permutation group element, or an object that converts
          to a permutation group element, such as a list of integers or
          a string of cycles.

        OUTPUT:

        If ``self`` is the group denoted by `H`, then this method computes
        the group

        .. MATH::

            g^{-1}Hg = \\{g^{-1}hg\\vert h\\in H\\}

        which is the group `H` conjugated by `g`.

        There are no restrictions on ``self`` and ``g`` belonging to
        a common permutation group, and correspondingly, there is no
        relationship (such as a common parent) between ``self`` and the
        output group.

        EXAMPLES::

            sage: G = DihedralGroup(6)
            sage: a = PermutationGroupElement("(1,2,3,4)")
            sage: G.conjugate(a)
            Permutation Group with generators [(1,5,6,2,3,4), (1,4)(2,6)(3,5)]

        The element performing the conjugation can be specified in
        several ways.  ::

            sage: G = DihedralGroup(6)
            sage: strng = "(1,2,3,4)"
            sage: G.conjugate(strng)
            Permutation Group with generators [(1,5,6,2,3,4), (1,4)(2,6)(3,5)]
            sage: G = DihedralGroup(6)
            sage: lst = [2,3,4,1]
            sage: G.conjugate(lst)
            Permutation Group with generators [(1,5,6,2,3,4), (1,4)(2,6)(3,5)]
            sage: G = DihedralGroup(6)
            sage: cycles = [(1,2,3,4)]
            sage: G.conjugate(cycles)
            Permutation Group with generators [(1,5,6,2,3,4), (1,4)(2,6)(3,5)]

        Conjugation is a group automorphism, so conjugate groups
        will be isomorphic. ::

            sage: G = DiCyclicGroup(6)
            sage: G.degree()
            11
            sage: cycle = [i+1 for i in range(1,11)] + [1]
            sage: C = G.conjugate(cycle)
            sage: G.is_isomorphic(C)
            True

        The conjugating element may be from a symmetric group with
        larger degree than the group being conjugated.  ::

            sage: G = AlternatingGroup(5)
            sage: G.degree()
            5
            sage: g = "(1,3)(5,6,7)"
            sage: H = G.conjugate(g); H
            Permutation Group with generators [(1,4,6,3,2), (1,4,6)]
            sage: H.degree()
            6

        The conjugating element is checked. ::

            sage: G = SymmetricGroup(3)
            sage: G.conjugate("junk")
            Traceback (most recent call last):
            ...
            TypeError: junk does not convert to a permutation group element
        '''
    def are_conjugate(self, H1, H2):
        """
        Return whether ``H1`` and ``H2`` are conjugate subgroups in ``G``.

        EXAMPLES::

            sage: G = SymmetricGroup(3)
            sage: H1 = PermutationGroup([(1,2)])
            sage: H2 = PermutationGroup([(2,3)])
            sage: G.are_conjugate(H1, H2)
            True
            sage: G = SymmetricGroup(4)
            sage: H1 = PermutationGroup([[(1,3),(2,4)], [(1,2),(3,4)]])
            sage: H2 = PermutationGroup([[(1,2)], [(1,2),(3,4)]])
            sage: G.are_conjugate(H1, H2)
            False
        """
    def direct_product(self, other, maps: bool = True):
        """
        Wraps GAP's ``DirectProduct``, ``Embedding``, and ``Projection``.

        Sage calls GAP's ``DirectProduct``, which chooses an efficient
        representation for the direct product. The direct product of
        permutation groups will be a permutation group again. For a direct
        product ``D``, the GAP operation ``Embedding(D,i)`` returns the
        homomorphism embedding the `i`-th factor into ``D``. The GAP operation
        ``Projection(D,i)`` gives the projection of ``D`` onto the `i`-th factor.
        This method returns a 5-tuple: a permutation group and 4 morphisms.

        INPUT:

        - ``self``, ``other`` -- permutation groups

        OUTPUT:

        - ``D`` -- a direct product of the inputs, returned as
          a permutation group as well

        - ``iota1`` -- an embedding of ``self`` into ``D``

        - ``iota2`` -- an embedding of ``other`` into ``D``

        - ``pr1`` -- the projection of ``D`` onto ``self`` (giving a
          splitting ``1 - other - D - self - 1``)

        - ``pr2`` -- the projection of ``D`` onto ``other`` (giving a
          splitting ``1 - self - D - other - 1``)

        EXAMPLES::

            sage: G = CyclicPermutationGroup(4)
            sage: D = G.direct_product(G, False); D
            Permutation Group with generators [(1,2,3,4), (5,6,7,8)]
            sage: D,iota1,iota2,pr1,pr2 = G.direct_product(G)
            sage: D; iota1; iota2; pr1; pr2
            Permutation Group with generators [(1,2,3,4), (5,6,7,8)]
            Permutation group morphism:
              From: Cyclic group of order 4 as a permutation group
              To:   Permutation Group with generators [(1,2,3,4), (5,6,7,8)]
              Defn: Embedding( Group( [ (1,2,3,4), (5,6,7,8) ] ), 1 )
            Permutation group morphism:
              From: Cyclic group of order 4 as a permutation group
              To:   Permutation Group with generators [(1,2,3,4), (5,6,7,8)]
              Defn: Embedding( Group( [ (1,2,3,4), (5,6,7,8) ] ), 2 )
            Permutation group morphism:
              From: Permutation Group with generators [(1,2,3,4), (5,6,7,8)]
              To:   Cyclic group of order 4 as a permutation group
              Defn: Projection( Group( [ (1,2,3,4), (5,6,7,8) ] ), 1 )
            Permutation group morphism:
              From: Permutation Group with generators [(1,2,3,4), (5,6,7,8)]
              To:   Cyclic group of order 4 as a permutation group
              Defn: Projection( Group( [ (1,2,3,4), (5,6,7,8) ] ), 2 )
            sage: g = D([(1,3),(2,4)]); g
            (1,3)(2,4)
            sage: d = D([(1,4,3,2),(5,7),(6,8)]); d
            (1,4,3,2)(5,7)(6,8)
            sage: iota1(g); iota2(g); pr1(d); pr2(d)
            (1,3)(2,4)
            (5,7)(6,8)
            (1,4,3,2)
            (1,3)(2,4)
        """
    def semidirect_product(self, N, mapping, check: bool = True):
        '''
        The semidirect product of ``self`` with ``N``.

        INPUT:

        - ``N`` -- a group which is acted on by ``self`` and
          naturally embeds as a normal subgroup of the returned semidirect
          product

        - ``mapping`` -- a pair of lists that together define a
          homomorphism, `\\phi :` ``self`` `\\rightarrow` Aut(``N``), by giving,
          in the second list, the images of the generators of ``self``
          in the order given in the first list

        - ``check`` -- a boolean that, if set to ``False``, will skip the
          initial tests which are made on ``mapping``. This may be beneficial
          for large ``N``, since in such cases the injectivity test can be
          expensive. Set to ``True`` by default.

        OUTPUT:

        The semidirect product of ``self`` and ``N`` defined by the
        action of ``self`` on ``N`` given in ``mapping`` (note that a
        homomorphism from `A` to the automorphism group of `B` is
        equivalent to an action of `A` on `B`\'s underlying set). The
        semidirect product of two groups, `H` and `N`, is a construct
        similar to the direct product in so far as the elements are
        the Cartesian product of the elements of `H` and the elements
        of `N`. The operation, however, is built upon an action of `H`
        on `N`, and is defined as such:

        .. MATH::

                (h_1,n_1)(h_2,n_2) = (h_{1}h_{2}, n_{1}^{h_2}n_2)

        This function is a wrapper for GAP\'s ``SemidirectProduct``
        command. The permutation group returned is built upon a
        permutation representation of the semidirect product of ``self``
        and ``N`` on a set of size `\\mid N \\mid`. The generators of
        ``N`` are given as their right regular representations, while the
        generators of ``self`` are defined by the underlying action of
        ``self`` on ``N``. It should be noted that the defining action is
        not always faithful, and in this case the inputted representations
        of the generators of ``self`` are placed on additional letters
        and adjoined to the output\'s generators of ``self``.

        EXAMPLES:

        Perhaps the most common example of a semidirect product comes
        from the family of dihedral groups. Each dihedral group is the
        semidirect product of `C_2` with `C_n`, where, by convention,
        `3 \\leq n`. In this case, the nontrivial element of `C_2` acts
        on `C_n` so as to send each element to its inverse. ::

            sage: C2 = CyclicPermutationGroup(2)
            sage: C8 = CyclicPermutationGroup(8)
            sage: alpha = PermutationGroupMorphism_im_gens(C8,C8,[(1,8,7,6,5,4,3,2)])
            sage: S = C2.semidirect_product(C8,[[(1,2)],[alpha]])
            sage: S == DihedralGroup(8)
            False
            sage: S.is_isomorphic(DihedralGroup(8))
            True
            sage: S.gens()
            ((3,4,5,6,7,8,9,10), (1,2)(4,10)(5,9)(6,8))

        A more complicated example can be drawn from [TW1980]_.
        It is there given that a semidirect product of `D_4` and `C_3`
        is isomorphic to one of `C_2` and the dicyclic group of order
        12. This nonabelian group of order 24 has very similar
        structure to the dicyclic and dihedral groups of order 24, the
        three being the only groups of order 24 with a two-element
        center and 9 conjugacy classes. ::

            sage: D4 = DihedralGroup(4)
            sage: C3 = CyclicPermutationGroup(3)
            sage: alpha1 = PermutationGroupMorphism_im_gens(C3,C3,[(1,3,2)])
            sage: alpha2 = PermutationGroupMorphism_im_gens(C3,C3,[(1,2,3)])
            sage: S1 = D4.semidirect_product(C3,[[(1,2,3,4),(1,3)],[alpha1,alpha2]])
            sage: C2 = CyclicPermutationGroup(2)
            sage: Q = DiCyclicGroup(3)
            sage: a = Q.gens()[0]; b=Q.gens()[1].inverse()
            sage: alpha = PermutationGroupMorphism_im_gens(Q,Q,[a,b])
            sage: S2 = C2.semidirect_product(Q,[[(1,2)],[alpha]])
            sage: S1.is_isomorphic(S2)
            True
            sage: S1.is_isomorphic(DihedralGroup(12))
            False
            sage: S1.is_isomorphic(DiCyclicGroup(6))
            False
            sage: S1.center()
            Subgroup generated by [(1,3)(2,4)] of
             (Permutation Group with generators [(5,6,7), (1,2,3,4)(6,7), (1,3)])
            sage: len(S1.conjugacy_classes_representatives())
            9

        If your normal subgroup is large, and you are confident that
        your inputs will successfully create a semidirect product, then
        it is beneficial, for the sake of time efficiency, to set the
        ``check`` parameter to ``False``.  ::

            sage: C2 = CyclicPermutationGroup(2)
            sage: C2000 = CyclicPermutationGroup(500)
            sage: alpha = PermutationGroupMorphism(C2000,C2000,[C2000.gen().inverse()])
            sage: S = C2.semidirect_product(C2000,[[(1,2)],[alpha]],check=False)

        TESTS::

            sage: C3 = CyclicPermutationGroup(3)
            sage: D4 = DihedralGroup(4)
            sage: alpha = PermutationGroupMorphism(C3,C3,[C3("(1,3,2)")])
            sage: alpha1 = PermutationGroupMorphism(C3,C3,[C3("(1,2,3)")])

            sage: s = D4.semidirect_product(\'junk\', [[(1,2,3,4),(1,2)], [alpha, alpha1]])
            Traceback (most recent call last):
            ...
            TypeError: junk is not a permutation group

            sage: s = D4.semidirect_product(C3, [[(1,2,3,4),(1,2)], [alpha, alpha1]])
            Traceback (most recent call last):
            ...
            ValueError: the generator list must generate the calling group, [(1, 2, 3, 4), (1, 2)]
            does not generate Dihedral group of order 8 as a permutation group

            sage: s = D4.semidirect_product(C3, [[(1,2,3,4),(1,3)], [alpha]])
            Traceback (most recent call last):
            ...
            ValueError: the list of generators and the list of morphisms must be of equal length

            sage: alpha2 = PermutationGroupMorphism(C3, D4, [D4("()")])
            sage: s = D4.semidirect_product(C3, [[(1,2,3,4),(1,3)], [alpha, alpha2]])
            Traceback (most recent call last):
            ...
            ValueError: an element of the automorphism list is not an endomorphism (and is therefore not an automorphism)

            sage: alpha3 = PermutationGroupMorphism(C3,C3,[C3("()")])
            sage: s = D4.semidirect_product(C3, [[(1,2,3,4),(1,3)], [alpha, alpha3]])
            Traceback (most recent call last):
            ...
            ValueError: an element of the automorphism list is not an injection (and is therefore not an automorphism)

        AUTHOR:

        - Kevin Halasz (2012-8-12)
        '''
    def holomorph(self):
        """
        The holomorph of a group as a permutation group.

        The holomorph of a group `G` is the semidirect product
        `G \\rtimes_{id} Aut(G)`, where `id` is the identity function
        on `Aut(G)`, the automorphism group of `G`.

        See :wikipedia:`Holomorph (mathematics)`

        OUTPUT: the holomorph of a given group as permutation group
        via a wrapping of GAP's semidirect product function

        EXAMPLES:

        Thomas and Wood's 'Group Tables' (Shiva Publishing, 1980) tells
        us that the holomorph of `C_5` is the unique group of order 20
        with a trivial center. ::

            sage: C5 = CyclicPermutationGroup(5)
            sage: A = C5.holomorph()
            sage: A.order()
            20
            sage: A.is_abelian()
            False
            sage: A.center()
            Subgroup generated by [()] of
             (Permutation Group with generators [(5,6,7,8,9), (1,2,4,3)(6,7,9,8)])
            sage: A
            Permutation Group with generators [(5,6,7,8,9), (1,2,4,3)(6,7,9,8)]

        Noting that the automorphism group of `D_4` is itself `D_4`, it
        can easily be shown that the holomorph is indeed an internal
        semidirect product of these two groups. ::

            sage: D4 = DihedralGroup(4)
            sage: H = D4.holomorph()
            sage: H.gens()
            ((2,3,5,8), (2,5)(3,8), (3,8)(4,7), (1,4,6,7)(2,3,5,8), (1,8)(2,7)(3,6)(4,5))
            sage: G = H.subgroup([H.gens()[0],H.gens()[1],H.gens()[2]])
            sage: N = H.subgroup([H.gens()[3],H.gens()[4]])
            sage: N.is_normal(H)
            True
            sage: G.is_isomorphic(D4)
            True
            sage: N.is_isomorphic(D4)
            True
            sage: G.intersection(N)
            Permutation Group with generators [()]
            sage: L = [H(x)*H(y) for x in G for y in N]; L.sort()
            sage: L1 = H.list(); L1.sort()
            sage: L == L1
            True

        Author:

        - Kevin Halasz (2012-08-14)
        """
    def subgroup(self, gens=None, gap_group=None, domain=None, category=None, canonicalize: bool = True, check: bool = True):
        """
        Wraps the ``PermutationGroup_subgroup`` constructor. The argument
        ``gens`` is a list of elements of ``self``.

        EXAMPLES::

            sage: G = PermutationGroup([(1,2,3),(3,4,5)])
            sage: g = G((1,2,3))
            sage: G.subgroup([g])
            Subgroup generated by [(1,2,3)] of
             (Permutation Group with generators [(3,4,5), (1,2,3)])
        """
    def as_finitely_presented_group(self, reduced: bool = False):
        """
        Return a finitely presented group isomorphic to ``self``.

        This method acts as wrapper for the GAP function ``IsomorphismFpGroupByGenerators``,
        which yields an isomorphism from a given group to a finitely presented group.

        INPUT:

        - ``reduced`` -- (default: ``False``) if ``True``,
          :meth:`FinitelyPresentedGroup.simplified <sage.groups.finitely_presented.FinitelyPresentedGroup.simplified>`
          is called, attempting to simplify the presentation of the finitely presented group
          to be returned

        OUTPUT: finite presentation of ``self``, obtained by taking the image
        of the isomorphism returned by the GAP function
        ``IsomorphismFpGroupByGenerators``

        ALGORITHM: uses GAP

        EXAMPLES::

            sage: CyclicPermutationGroup(50).as_finitely_presented_group()
            Finitely presented group < a | a^50 >
            sage: DihedralGroup(4).as_finitely_presented_group()
            Finitely presented group < a, b | b^2, a^4, (b*a)^2 >
            sage: GeneralDihedralGroup([2,2]).as_finitely_presented_group()
            Finitely presented group < a, b, c | a^2, b^2, c^2, (c*b)^2, (c*a)^2, (b*a)^2 >

        GAP algorithm is not guaranteed to produce minimal or canonical presentation::

            sage: G = PermutationGroup(['(1,2,3,4,5)', '(1,5)(2,4)'])
            sage: G.is_isomorphic(DihedralGroup(5))
            True
            sage: K = G.as_finitely_presented_group(); K
            Finitely presented group < a, b | b^2, (b*a)^2, b*a^-3*b*a^2 >
            sage: K.as_permutation_group().is_isomorphic(DihedralGroup(5))
            True

        We can attempt to reduce the output presentation::

            sage: H = PermutationGroup(['(1,2,3,4,5)', '(1,3,5,2,4)'])
            sage: H.as_finitely_presented_group()
            Finitely presented group < a, b | b^-2*a^-1, b*a^-2 >
            sage: H.as_finitely_presented_group(reduced=True)
            Finitely presented group < a | a^5 >

        TESTS::

            sage: PermutationGroup([]).as_finitely_presented_group()
            Finitely presented group < a | a >
            sage: S = SymmetricGroup(4)
            sage: perm_ls = [S.random_element() for i in range(3)]
            sage: G = PermutationGroup(perm_ls)
            sage: G.as_finitely_presented_group().as_permutation_group().is_isomorphic(G)
            True

        `D_9` is the only non-Abelian group of order 18
        with an automorphism group of order 54 [TW1980]_::

            sage: D = DihedralGroup(9).as_finitely_presented_group().gap()
            sage: D.Order(), D.IsAbelian(), D.AutomorphismGroup().Order()
            (18, false, 54)

        `S_3` is the only non-Abelian group of order 6 [TW1980]_::

            sage: S = SymmetricGroup(3).as_finitely_presented_group().gap()
            sage: S.Order(), S.IsAbelian()
            (6, false)

        We can manually construct a permutation representation using GAP
        coset enumeration methods::

            sage: D = GeneralDihedralGroup([3,3,4]).as_finitely_presented_group().gap()
            sage: ctab = D.CosetTable(D.Subgroup([]))
            sage: gen_ls = gap.List(ctab, gap.PermList)
            sage: PermutationGroup(gen_ls).is_isomorphic(GeneralDihedralGroup([3,3,4]))
            True
            sage: A = AlternatingGroup(5).as_finitely_presented_group().gap()
            sage: ctab = A.CosetTable(A.Subgroup([]))
            sage: gen_ls = gap.List(ctab, gap.PermList)
            sage: PermutationGroup(gen_ls).is_isomorphic(AlternatingGroup(5))
            True

        AUTHORS:

        - Davis Shurbert (2013-06-21): initial version
        """
    def quotient(self, N, **kwds):
        '''
        Return the quotient of this permutation group by the normal
        subgroup `N`, as a permutation group.

        Further named arguments are passed to the permutation group constructor.

        Wraps the GAP operator "/".

        EXAMPLES::

            sage: G = PermutationGroup([(1,2,3), (2,3)])
            sage: N = PermutationGroup([(1,2,3)])
            sage: G.quotient(N)
            Permutation Group with generators [(1,2)]
            sage: G.quotient(G)
            Permutation Group with generators [(), ()]
        '''
    def commutator(self, other=None):
        """
        Return the commutator subgroup of a group, or of a pair of groups.

        INPUT:

        - ``other`` -- (default: ``None``) a permutation group

        OUTPUT:

        Let `G` denote ``self``.  If ``other`` is ``None``, then this method
        returns the subgroup of `G` generated by the set of commutators,

        .. MATH::

            \\{[g_1,g_2]\\vert g_1, g_2\\in G\\} = \\{g_1^{-1}g_2^{-1}g_1g_2\\vert g_1, g_2\\in G\\}

        Let `H` denote ``other``, in the case that it is not ``None``.  Then
        this method returns the group generated by the set of commutators,

        .. MATH::

            \\{[g,h]\\vert g\\in G\\, h\\in H\\} = \\{g^{-1}h^{-1}gh\\vert  g\\in G\\, h\\in H\\}

        The two groups need only be permutation groups, there is no notion
        of requiring them to explicitly be subgroups of some other group.

        .. NOTE::

            For the identical statement, the generators of the returned
            group can vary from one execution to the next.

        EXAMPLES::

            sage: G = DiCyclicGroup(4)
            sage: G.commutator()
            Permutation Group with generators [(1,3,5,7)(2,4,6,8)(9,11,13,15)(10,12,14,16)]

            sage: G = SymmetricGroup(5)
            sage: H = CyclicPermutationGroup(5)
            sage: C = G.commutator(H)
            sage: C.is_isomorphic(AlternatingGroup(5))
            True

        An abelian group will have a trivial commutator.  ::

            sage: G = CyclicPermutationGroup(10)
            sage: G.commutator()
            Permutation Group with generators [()]

        The quotient of a group by its commutator is always abelian.  ::

            sage: G = DihedralGroup(20)
            sage: C = G.commutator()
            sage: Q = G.quotient(C)
            sage: Q.is_abelian()
            True

        When forming commutators from two groups, the order of the
        groups does not matter.  ::

            sage: D = DihedralGroup(3)
            sage: S = SymmetricGroup(2)
            sage: C1 = D.commutator(S); C1
            Permutation Group with generators [(1,2,3)]
            sage: C2 = S.commutator(D); C2
            Permutation Group with generators [(1,3,2)]
            sage: C1 == C2
            True

        This method calls two different functions in GAP, so
        this tests that their results are consistent.  The
        commutator groups may have different generators, but the
        groups are equal. ::

            sage: G = DiCyclicGroup(3)
            sage: C = G.commutator(); C
            Permutation Group with generators [(5,7,6)]
            sage: CC = G.commutator(G); CC
            Permutation Group with generators [(5,6,7)]
            sage: C == CC
            True

        The second group is checked.  ::

            sage: G = SymmetricGroup(2)
            sage: G.commutator('junk')
            Traceback (most recent call last):
            ...
            TypeError: junk is not a permutation group

        TESTS:

        Verify that :issue`39416` is fixed::

            sage: G = PermutationGroup(gens=[(1,2), (2,4)], domain={1, 2, 4})
            sage: G.commutator()
            Permutation Group with generators [(1,2,4)]
        """
    @hap_decorator
    def cohomology(self, n, p: int = 0):
        """
        Compute the group cohomology `H^n(G, F)`, where `F = \\ZZ`
        if `p=0` and `F = \\ZZ / p \\ZZ` if `p > 0` is a prime.

        Wraps HAP's ``GroupHomology`` function, written by Graham Ellis.

        REQUIRES: GAP package HAP (in gap_packages-\\*.spkg).

        EXAMPLES::

            sage: G = SymmetricGroup(4)
            sage: G.cohomology(1,2)                            # optional - gap_package_hap
            Multiplicative Abelian group isomorphic to C2
            sage: G = SymmetricGroup(3)
            sage: G.cohomology(5)                              # optional - gap_package_hap
            Trivial Abelian group
            sage: G.cohomology(5,2)                            # optional - gap_package_hap
            Multiplicative Abelian group isomorphic to C2
            sage: G.homology(5,3)                              # optional - gap_package_hap
            Trivial Abelian group
            sage: G.homology(5,4)                              # optional - gap_package_hap
            Traceback (most recent call last):
            ...
            ValueError: p must be 0 or prime

        This computes `H^4(S_3, \\ZZ)` and
        `H^4(S_3, \\ZZ / 2 \\ZZ)`, respectively.

        AUTHORS:

        - David Joyner and Graham Ellis

        REFERENCES:

        - G. Ellis, 'Computing group resolutions', J. Symbolic
          Computation. Vol.38, (2004)1077-1118 (Available at
          http://hamilton.nuigalway.ie/).

        - D. Joyner, 'A primer on computational group homology and
          cohomology', http://front.math.ucdavis.edu/0706.0549.
        """
    @hap_decorator
    def cohomology_part(self, n, p: int = 0):
        """
        Compute the p-part of the group cohomology `H^n(G, F)`,
        where `F = \\ZZ` if `p=0` and `F = \\ZZ / p \\ZZ` if
        `p > 0` is a prime.

        Wraps HAP's Homology function, written
        by Graham Ellis, applied to the `p`-Sylow subgroup of
        `G`.

        REQUIRES: GAP package HAP (in gap_packages-\\*.spkg).

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: G.cohomology_part(7,2)                   # optional - gap_package_hap
            Multiplicative Abelian group isomorphic to C2 x C2 x C2
            sage: G = SymmetricGroup(3)
            sage: G.cohomology_part(2,3)                   # optional - gap_package_hap
            Multiplicative Abelian group isomorphic to C3

        AUTHORS:

        - David Joyner and Graham Ellis
        """
    @hap_decorator
    def homology(self, n, p: int = 0):
        '''
        Compute the group homology `H_n(G, F)`, where
        `F = \\ZZ` if `p=0` and `F = \\ZZ / p \\ZZ` if
        `p > 0` is a prime. Wraps HAP\'s ``GroupHomology`` function,
        written by Graham Ellis.

        REQUIRES: GAP package HAP (in gap_packages-\\*.spkg).

        AUTHORS:

        - David Joyner and Graham Ellis

        The example below computes `H_7(S_5, \\ZZ)`,
        `H_7(S_5, \\ZZ / 2 \\ZZ)`,
        `H_7(S_5, \\ZZ / 3 \\ZZ)`, and
        `H_7(S_5, \\ZZ / 5 \\ZZ)`, respectively. To compute the
        `2`-part of `H_7(S_5, \\ZZ)`, use the method :meth:`homology_part`.

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: G.homology(7)                              # optional - gap_package_hap
            Multiplicative Abelian group isomorphic to C2 x C2 x C4 x C3 x C5
            sage: G.homology(7,2)                              # optional - gap_package_hap
            Multiplicative Abelian group isomorphic to C2 x C2 x C2 x C2 x C2
            sage: G.homology(7,3)                              # optional - gap_package_hap
            Multiplicative Abelian group isomorphic to C3
            sage: G.homology(7,5)                              # optional - gap_package_hap
            Multiplicative Abelian group isomorphic to C5

        REFERENCES:

        - G. Ellis, "Computing group resolutions", J. Symbolic
          Computation. Vol.38, (2004)1077-1118 (Available at
          http://hamilton.nuigalway.ie/.

        - D. Joyner, "A primer on computational group homology and cohomology",
          http://front.math.ucdavis.edu/0706.0549
        '''
    @hap_decorator
    def homology_part(self, n, p: int = 0):
        """
        Compute the `p`-part of the group homology
        `H_n(G, F)`, where `F = \\ZZ` if `p=0` and
        `F = \\ZZ / p \\ZZ` if `p > 0` is a prime. Wraps HAP's
        ``Homology`` function, written by Graham Ellis, applied to the
        `p`-Sylow subgroup of `G`.

        REQUIRES: GAP package HAP (in gap_packages-\\*.spkg).

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: G.homology_part(7,2)                              # optional - gap_package_hap
            Multiplicative Abelian group isomorphic to C2 x C2 x C2 x C2 x C4

        AUTHORS:

        - David Joyner and Graham Ellis
        """
    def character_table(self):
        '''
        Return the matrix of values of the irreducible
        characters of a permutation group `G` at the conjugacy
        classes of `G`.

        The columns represent the conjugacy classes of
        `G` and the rows represent the different irreducible
        characters in the ordering given by GAP.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3)]])
            sage: G.order()
            12
            sage: G.character_table()                                                   # needs sage.rings.number_field
            [         1          1          1          1]
            [         1 -zeta3 - 1      zeta3          1]
            [         1      zeta3 -zeta3 - 1          1]
            [         3          0          0         -1]
            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3)]])
            sage: CT = gap(G).CharacterTable()

        Type ``CT.Display()`` to display this nicely.

        ::

            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4)]])
            sage: G.order()
            8
            sage: G.character_table()                                                   # needs sage.rings.number_field
            [ 1  1  1  1  1]
            [ 1 -1 -1  1  1]
            [ 1 -1  1 -1  1]
            [ 1  1 -1 -1  1]
            [ 2  0  0  0 -2]
            sage: CT = gap(G).CharacterTable()

        Again, type ``CT.Display()`` to display this nicely.

        ::

            sage: # needs sage.rings.number_field
            sage: SymmetricGroup(2).character_table()
            [ 1 -1]
            [ 1  1]
            sage: SymmetricGroup(3).character_table()
            [ 1 -1  1]
            [ 2  0 -1]
            [ 1  1  1]
            sage: SymmetricGroup(5).character_table()
            [ 1 -1  1  1 -1 -1  1]
            [ 4 -2  0  1  1  0 -1]
            [ 5 -1  1 -1 -1  1  0]
            [ 6  0 -2  0  0  0  1]
            [ 5  1  1 -1  1 -1  0]
            [ 4  2  0  1 -1  0 -1]
            [ 1  1  1  1  1  1  1]
            sage: list(AlternatingGroup(6).character_table())
            [(1, 1, 1, 1, 1, 1, 1), (5, 1, 2, -1, -1, 0, 0), (5, 1, -1, 2, -1, 0, 0),
             (8, 0, -1, -1, 0, zeta5^3 + zeta5^2 + 1, -zeta5^3 - zeta5^2),
             (8, 0, -1, -1, 0, -zeta5^3 - zeta5^2, zeta5^3 + zeta5^2 + 1),
             (9, 1, 0, 0, 1, -1, -1), (10, -2, 1, 1, 0, 0, 0)]

        Suppose that you have a class function `f(g)` on
        `G` and you know the values `v_1, \\ldots, v_n` on
        the conjugacy class elements in
        ``conjugacy_classes_representatives(G)`` =
        `[g_1, \\ldots, g_n]`. Since the irreducible characters
        `\\rho_1, \\ldots, \\rho_n` of `G` form an
        `E`-basis of the space of all class functions (`E`
        a "sufficiently large" cyclotomic field), such a class function is
        a linear combination of these basis elements,
        `f = c_1 \\rho_1 + \\cdots + c_n \\rho_n`. To find
        the coefficients `c_i`, you simply solve the linear system
        ``character_table_values(G)`` `[v_1, ..., v_n] = [c_1, ..., c_n]`,
        where `[v_1, \\ldots, v_n]` = ``character_table_values(G)`` `^{(-1)}[c_1, ..., c_n]`.

        AUTHORS:

        - David Joyner and William Stein (2006-01-04)
        '''
    def irreducible_characters(self):
        """
        Return a list of the irreducible characters of ``self``.

        EXAMPLES::

            sage: irr = SymmetricGroup(3).irreducible_characters()                      # needs sage.rings.number_field
            sage: [x.values() for x in irr]                                             # needs sage.rings.number_field
            [[1, -1, 1], [2, 0, -1], [1, 1, 1]]
        """
    def trivial_character(self):
        """
        Return the trivial character of ``self``.

        EXAMPLES::

            sage: SymmetricGroup(3).trivial_character()                                 # needs sage.rings.number_field
            Character of Symmetric group of order 3! as a permutation group
        """
    def character(self, values):
        """
        Return a group character from ``values``, where ``values`` is
        a list of the values of the character evaluated on the conjugacy
        classes.

        EXAMPLES::

            sage: G = AlternatingGroup(4)
            sage: n = len(G.conjugacy_classes_representatives())
            sage: G.character([1]*n)                                                    # needs sage.rings.number_field
            Character of Alternating group of order 4!/2 as a permutation group
        """
    def conjugacy_classes_representatives(self):
        """
        Return a complete list of representatives of conjugacy classes in
        a permutation group `G`.

        The ordering is that given by GAP.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4)]])
            sage: cl = G.conjugacy_classes_representatives(); cl
            [(), (2,4), (1,2)(3,4), (1,2,3,4), (1,3)(2,4)]
            sage: cl[3] in G
            True

        ::

            sage: G = SymmetricGroup(5)
            sage: G.conjugacy_classes_representatives()                                 # needs sage.combinat
            [(), (1,2), (1,2)(3,4), (1,2,3), (1,2,3)(4,5), (1,2,3,4), (1,2,3,4,5)]

        ::

            sage: S = SymmetricGroup(['a','b','c'])
            sage: S.conjugacy_classes_representatives()                                 # needs sage.combinat
            [(), ('a','b'), ('a','b','c')]

        AUTHORS:

        - David Joyner and William Stein (2006-01-04)
        """
    def conjugacy_classes_subgroups(self):
        """
        Return a complete list of representatives of conjugacy classes of
        subgroups in a permutation group `G`.

        The ordering is that given by GAP.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4)]])
            sage: cl = G.conjugacy_classes_subgroups(); cl
            [Subgroup generated by [()] of
              (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)]),
             Subgroup generated by [(1,2)(3,4)] of
              (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)]),
             Subgroup generated by [(1,3)(2,4)] of
              (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)]),
             Subgroup generated by [(2,4)] of
              (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)]),
             Subgroup generated by [(1,4)(2,3), (1,2)(3,4)] of
              (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)]),
             Subgroup generated by [(2,4), (1,3)(2,4)] of
              (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)]),
             Subgroup generated by [(1,2,3,4), (1,3)(2,4)] of
              (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)]),
             Subgroup generated by [(1,4)(2,3), (1,2)(3,4), (2,4)] of
              (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)])]

        ::

            sage: G = SymmetricGroup(3)
            sage: G.conjugacy_classes_subgroups()
            [Subgroup generated by [()] of
              (Symmetric group of order 3! as a permutation group),
             Subgroup generated by [(2,3)] of
              (Symmetric group of order 3! as a permutation group),
             Subgroup generated by [(1,2,3)] of
              (Symmetric group of order 3! as a permutation group),
             Subgroup generated by [(1,2,3), (2,3)] of
              (Symmetric group of order 3! as a permutation group)]

        AUTHORS:

        - David Joyner (2006-10)
        """
    def subgroups(self):
        """
        Return a list of all the subgroups of ``self``.

        OUTPUT:

        Each possible subgroup of ``self`` is contained once
        in the returned list.  The list is in order, according
        to the size of the subgroups, from the trivial subgroup
        with one element on through up to the whole group.
        Conjugacy classes of subgroups are contiguous in the list.

        .. WARNING::

            For even relatively small groups this method can
            take a very long time to execute, or create vast
            amounts of output.  Likely both.  Its purpose is
            instructional, as it can be useful for studying
            small groups.  The 156 subgroups of the full
            symmetric group on 5 symbols of order 120, `S_5`,
            can be computed in about a minute on commodity hardware
            in 2011. The 64 subgroups of the cyclic group of order
            `30030 = 2\\cdot 3\\cdot 5\\cdot 7\\cdot 11\\cdot 13` takes
            about twice as long.

            For faster results, which still exhibit the structure of
            the possible subgroups, use
            :meth:`conjugacy_classes_subgroups`.

        EXAMPLES::

            sage: G = SymmetricGroup(3)
            sage: G.subgroups()
            [Subgroup generated by [()] of
              (Symmetric group of order 3! as a permutation group),
             Subgroup generated by [(2,3)] of
              (Symmetric group of order 3! as a permutation group),
             Subgroup generated by [(1,2)] of
              (Symmetric group of order 3! as a permutation group),
             Subgroup generated by [(1,3)] of
              (Symmetric group of order 3! as a permutation group),
             Subgroup generated by [(1,2,3)] of
              (Symmetric group of order 3! as a permutation group),
             Subgroup generated by [(1,2,3), (2,3)] of
              (Symmetric group of order 3! as a permutation group)]

            sage: G = CyclicPermutationGroup(14)
            sage: G.subgroups()
            [Subgroup generated by [()] of
              (Cyclic group of order 14 as a permutation group),
             Subgroup generated by [(1,8)(2,9)(3,10)(4,11)(5,12)(6,13)(7,14)] of
              (Cyclic group of order 14 as a permutation group),
             Subgroup generated by [(1,3,5,7,9,11,13)(2,4,6,8,10,12,14)] of
              (Cyclic group of order 14 as a permutation group),
             Subgroup generated by [(1,3,5,7,9,11,13)(2,4,6,8,10,12,14),
                                    (1,2,3,4,5,6,7,8,9,10,11,12,13,14)] of
              (Cyclic group of order 14 as a permutation group)]

        AUTHOR:

        - Rob Beezer (2011-01-24)
        """
    @cached_method
    def has_regular_subgroup(self, return_group: bool = False):
        """
        Return whether the group contains a regular subgroup.

        INPUT:

        - ``return_group`` -- boolean; if ``True``, a regular
          subgroup is returned if there is one, and ``None`` if there isn't.
          When ``return_group=False`` (default), only a boolean indicating
          whether such a group exists is returned instead.

        EXAMPLES:

        The symmetric group on 4 elements has a regular subgroup::

            sage: S4 = groups.permutation.Symmetric(4)
            sage: S4.has_regular_subgroup()
            True
            sage: S4.has_regular_subgroup(return_group=True)  # random
            Subgroup of (Symmetric group of order 4! as a permutation group)
             generated by [(1,3)(2,4), (1,4)(2,3)]

        But the automorphism group of Petersen's graph does not::

            sage: # needs sage.graphs
            sage: G = graphs.PetersenGraph().automorphism_group()
            sage: G.has_regular_subgroup()
            False
        """
    def blocks_all(self, representatives: bool = True):
        '''
        Return the list of block systems of imprimitivity.

        For more information on primitivity, see the :wikipedia:`Wikipedia
        article on primitive group actions <Primitive_permutation_group>`.

        INPUT:

        - ``representative`` -- boolean; whether to return all possible block
          systems of imprimitivity or only one of their representatives (the
          block can be obtained from its representative set `S` by computing the
          orbit of `S` under ``self``).

          This parameter is set to ``True`` by default (as it is GAP\'s default
          behaviour).

        OUTPUT:

        This method returns a description of *all* block systems. Hence, the
        output is a "list of lists of lists" or a "list of lists" depending on
        the value of ``representatives``. A bit more clearly, output is:

        * A list of length (#number of different block systems) of

          * block systems, each of them being defined as

            * If ``representatives=True``: a list of representatives of
              each set of the block system

            * If ``representatives=False``: a partition of the elements
              defining an imprimitivity block.

        .. SEEALSO::

            - :meth:`~PermutationGroup_generic.is_primitive`

        EXAMPLES:

        Picking an interesting group::

            sage: # needs sage.graphs
            sage: g = graphs.DodecahedralGraph()
            sage: g.is_vertex_transitive()
            True
            sage: ag = g.automorphism_group()
            sage: ag.is_primitive()
            False

        Computing its blocks representatives::

            sage: ag.blocks_all()                                                       # needs sage.graphs
            [[0, 15]]

        Now the full block::

            sage: sorted(ag.blocks_all(representatives=False)[0])                       # needs sage.graphs
            [[0, 15], [1, 16], [2, 12], [3, 13], [4, 9],
             [5, 10], [6, 11], [7, 18], [8, 17], [14, 19]]

        TESTS::

            sage: g = PermutationGroup([("a","b","c","d")])
            sage: g.blocks_all()
            [[\'a\', \'c\']]
            sage: g.blocks_all(False)
            [[[\'a\', \'c\'], [\'b\', \'d\']]]
        '''
    def cosets(self, S, side: str = 'right'):
        '''
        Return a list of the cosets of ``S`` in ``self``.

        INPUT:

        - ``S`` -- a subgroup of ``self``;  an error is raised
          if ``S`` is not a subgroup

        - ``side`` -- (default: ``\'right\'``) determines if right cosets or
          left cosets are returned.  ``side`` refers to where the
          representative is placed in the products forming the cosets
          and thus allowable values are only ``\'right\'`` and ``\'left\'``.

        OUTPUT:

        A list of lists.  Each inner list is a coset of the subgroup
        in the group.  The first element of each coset is the smallest
        element (based on the ordering of the elements of ``self``)
        of all the group elements that have not yet appeared in a
        previous coset. The elements of each coset are in the same
        order as the subgroup elements used to build the coset\'s
        elements.

        As a consequence, the subgroup itself is the first coset,
        and its first element is the identity element.  For each coset,
        the first element listed is the element used as a representative
        to build the coset.  These representatives form an increasing
        sequence across the list of cosets, and within a coset the
        representative is the smallest element of its coset (both
        orderings are based on of the ordering of elements of ``self``).

        In the case of a normal subgroup, left and right cosets should
        appear in the same order as part of the outer list.  However,
        the list of the elements of a particular coset may be in a
        different order for the right coset versus the order in the
        left coset. So, if you check to see if a subgroup is normal,
        it is necessary to sort each individual coset first (but not
        the list of cosets, due to the ordering of the representatives).
        See below for examples of this.

        .. NOTE::

            This is a naive implementation intended for instructional
            purposes, and hence is slow for larger groups.  Sage and GAP
            provide more sophisticated functions for working quickly with
            cosets of larger groups.

        EXAMPLES:

        The default is to build right cosets. This example works with
        the symmetry group of an 8-gon and a normal subgroup.
        Notice that a straight check on the equality of the output
        is not sufficient to check normality, while sorting the
        individual cosets is sufficient to then simply test equality of
        the list of lists.  Study the second coset in each list to understand the
        need for sorting the elements of the cosets.  ::

            sage: G = DihedralGroup(8)
            sage: quarter_turn = G(\'(1,3,5,7)(2,4,6,8)\'); quarter_turn
            (1,3,5,7)(2,4,6,8)
            sage: S = G.subgroup([quarter_turn])
            sage: rc = G.cosets(S); rc
            [[(), (1,3,5,7)(2,4,6,8), (1,5)(2,6)(3,7)(4,8), (1,7,5,3)(2,8,6,4)],
             [(2,8)(3,7)(4,6), (1,7)(2,6)(3,5), (1,5)(2,4)(6,8), (1,3)(4,8)(5,7)],
             [(1,2)(3,8)(4,7)(5,6), (1,8)(2,7)(3,6)(4,5), (1,6)(2,5)(3,4)(7,8), (1,4)(2,3)(5,8)(6,7)],
             [(1,2,3,4,5,6,7,8), (1,4,7,2,5,8,3,6), (1,6,3,8,5,2,7,4), (1,8,7,6,5,4,3,2)]]
            sage: lc = G.cosets(S, side=\'left\'); lc
            [[(), (1,3,5,7)(2,4,6,8), (1,5)(2,6)(3,7)(4,8), (1,7,5,3)(2,8,6,4)],
             [(2,8)(3,7)(4,6), (1,3)(4,8)(5,7), (1,5)(2,4)(6,8), (1,7)(2,6)(3,5)],
             [(1,2)(3,8)(4,7)(5,6), (1,4)(2,3)(5,8)(6,7), (1,6)(2,5)(3,4)(7,8), (1,8)(2,7)(3,6)(4,5)],
             [(1,2,3,4,5,6,7,8), (1,4,7,2,5,8,3,6), (1,6,3,8,5,2,7,4), (1,8,7,6,5,4,3,2)]]

            sage: S.is_normal(G)
            True
            sage: rc == lc
            False
            sage: rc_sorted = [sorted(c) for c in rc]
            sage: lc_sorted = [sorted(c) for c in lc]
            sage: rc_sorted == lc_sorted
            True

        An example with the symmetry group of a regular
        tetrahedron and a subgroup that is not normal.
        Thus, the right and left cosets are different
        (and so are the representatives). With each
        individual coset sorted, a naive test of normality
        is possible.  ::

            sage: A = AlternatingGroup(4)
            sage: face_turn = A(\'(1,2,3)\'); face_turn
            (1,2,3)
            sage: stabilizer = A.subgroup([face_turn])
            sage: rc = A.cosets(stabilizer, side=\'right\'); rc
            [[(), (1,2,3), (1,3,2)],
             [(2,3,4), (1,3)(2,4), (1,4,2)],
             [(2,4,3), (1,4,3), (1,2)(3,4)],
             [(1,2,4), (1,4)(2,3), (1,3,4)]]
            sage: lc = A.cosets(stabilizer, side=\'left\'); lc
            [[(), (1,2,3), (1,3,2)],
             [(2,3,4), (1,2)(3,4), (1,3,4)],
             [(2,4,3), (1,2,4), (1,3)(2,4)],
             [(1,4,2), (1,4,3), (1,4)(2,3)]]

            sage: stabilizer.is_normal(A)
            False
            sage: rc_sorted = [sorted(c) for c in rc]
            sage: lc_sorted = [sorted(c) for c in lc]
            sage: rc_sorted == lc_sorted
            False

        TESTS:

        The keyword ``side`` is checked for the two possible values. ::

            sage: G = SymmetricGroup(3)
            sage: S = G.subgroup([G("(1,2)")])
            sage: G.cosets(S, side=\'junk\')
            Traceback (most recent call last):
            ...
            ValueError: side should be \'right\' or \'left\', not junk

        The subgroup argument is checked to see if it is a permutation group.
        Even a legitimate GAP object can be rejected. ::

            sage: G = SymmetricGroup(3)
            sage: G.cosets(gap(3))
            Traceback (most recent call last):
            ...
            TypeError: 3 is not a permutation group

        The subgroup is verified as a subgroup of ``self``. ::

            sage: A = AlternatingGroup(3)
            sage: G = SymmetricGroup(3)
            sage: S = G.subgroup([G("(1,2)")])
            sage: A.cosets(S)
            Traceback (most recent call last):
            ...
            ValueError: Subgroup generated by [(1,2)] of (Symmetric group of order 3! as a permutation group) is not a subgroup of Alternating group of order 3!/2 as a permutation group

        AUTHOR:

        - Rob Beezer (2011-01-31)
        '''
    def minimal_generating_set(self):
        '''
        Return a minimal generating set.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: g = graphs.CompleteGraph(4)
            sage: g.relabel([\'a\',\'b\',\'c\',\'d\'])
            sage: mgs = g.automorphism_group().minimal_generating_set(); len(mgs)
            2
            sage: mgs # random
            [(\'b\',\'d\',\'c\'), (\'a\',\'c\',\'b\',\'d\')]


        TESTS::

            sage: PermutationGroup(["(1,2,3)(4,5,6)","(1,2,3,4,5,6)"]).minimal_generating_set()
            [(2,5)(3,6), (1,5,3,4,2,6)]
        '''
    def normalizer(self, g):
        """
        Return the normalizer of ``g`` in ``self``.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4)]])
            sage: g = G([(1,3)])
            sage: G.normalizer(g)
            Subgroup generated by [(1,3), (2,4)] of
             (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)])
            sage: g = G([(1,2,3,4)])
            sage: G.normalizer(g)
            Subgroup generated by  [(1,2,3,4), (1,3)(2,4), (2,4)] of
             (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)])
            sage: H = G.subgroup([G([(1,2,3,4)])])
            sage: G.normalizer(H)
            Subgroup generated by [(1,2,3,4), (1,3)(2,4), (2,4)] of
             (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)])
        """
    def centralizer(self, g):
        """
        Return the centralizer of ``g`` in ``self``.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2),(3,4)], [(1,2,3,4)]])
            sage: g = G([(1,3)])
            sage: G.centralizer(g)
            Subgroup generated by [(1,3), (2,4)] of
             (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)])
            sage: g = G([(1,2,3,4)])
            sage: G.centralizer(g)
            Subgroup generated by [(1,2,3,4)] of
             (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)])
            sage: H = G.subgroup([G([(1,2,3,4)])])
            sage: G.centralizer(H)
            Subgroup generated by [(1,2,3,4)] of
             (Permutation Group with generators [(1,2)(3,4), (1,2,3,4)])
        """
    def isomorphism_type_info_simple_group(self):
        '''
        If the group is simple, then this returns the name of the group.

        EXAMPLES::

            sage: G = CyclicPermutationGroup(5)
            sage: G.isomorphism_type_info_simple_group()
            rec(
              name := "Z(5)",
              parameter := 5,
              series := "Z",
              shortname := "C5" )

        TESTS:

        This shows that the issue at :issue:`7360` is fixed::

            sage: G = KleinFourGroup()
            sage: G.is_simple()
            False
            sage: G.isomorphism_type_info_simple_group()
            Traceback (most recent call last):
            ...
            TypeError: group must be simple
        '''
    def minimal_normal_subgroups(self):
        """
        Return the nontrivial minimal normal subgroups ``self``.

        EXAMPLES::

            sage: G = PermutationGroup([(1,2,3),(4,5)])
            sage: G.minimal_normal_subgroups()
            [Subgroup generated by [(4,5)] of (Permutation Group with generators [(4,5), (1,2,3)]),
             Subgroup generated by [(1,2,3)] of (Permutation Group with generators [(4,5), (1,2,3)])]
        """
    def maximal_normal_subgroups(self):
        """
        Return the maximal proper normal subgroups of ``self``.

        This raises an error if `G/[G, G]` is infinite, yielding infinitely
        many maximal normal subgroups.

        EXAMPLES::

            sage: G = PermutationGroup([(1,2,3),(4,5)])
            sage: G.maximal_normal_subgroups()
            [Subgroup generated by [(1,2,3)] of (Permutation Group with generators [(4,5), (1,2,3)]),
             Subgroup generated by [(4,5)] of (Permutation Group with generators [(4,5), (1,2,3)])]
        """
    def is_abelian(self):
        """
        Return ``True`` if this group is abelian.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: G.is_abelian()
            False
            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.is_abelian()
            True
        """
    def is_commutative(self):
        """
        Return ``True`` if this group is commutative.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: G.is_commutative()
            False
            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.is_commutative()
            True
        """
    def is_cyclic(self):
        """
        Return ``True`` if this group is cyclic.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: G.is_cyclic()
            False
            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.is_cyclic()
            True
        """
    def is_elementary_abelian(self):
        """
        Return ``True`` if this group is elementary abelian. An elementary
        abelian group is a finite abelian group, where every nontrivial
        element has order `p`, where `p` is a prime.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: G.is_elementary_abelian()
            False
            sage: G = PermutationGroup(['(1,2,3)','(4,5,6)'])
            sage: G.is_elementary_abelian()
            True
        """
    def isomorphism_to(self, right):
        """
        Return an isomorphism from ``self`` to ``right`` if the groups
        are isomorphic, otherwise ``None``.

        INPUT:

        - ``self`` -- this group

        - ``right`` -- a permutation group

        OUTPUT: ``None``, or a morphism of permutation groups

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: H = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.isomorphism_to(H) is None
            True
            sage: G = PermutationGroup([(1,2,3), (2,3)])
            sage: H = PermutationGroup([(1,2,4), (1,4)])
            sage: G.isomorphism_to(H)  # not tested, see below
            Permutation group morphism:
              From: Permutation Group with generators [(2,3), (1,2,3)]
              To:   Permutation Group with generators [(1,2,4), (1,4)]
              Defn: [(2,3), (1,2,3)] -> [(2,4), (1,2,4)]

        TESTS:

        Partial check that the output makes some sense::

            sage: G.isomorphism_to(H)
            Permutation group morphism:
              From: Permutation Group with generators [(2,3), (1,2,3)]
              To:   Permutation Group with generators [(1,2,4), (1,4)]
              Defn: [(2,3), (1,2,3)] -> [...]
        """
    def is_isomorphic(self, right):
        """
        Return ``True`` if the groups are isomorphic.

        INPUT:

        - ``self`` -- this group

        - ``right`` -- a permutation group

        OUTPUT: boolean; ``True`` if ``self`` and ``right`` are isomorphic
        groups; ``False`` otherwise

        EXAMPLES::

            sage: v = ['(1,2,3)(4,5)', '(1,2,3,4,5)']
            sage: G = PermutationGroup(v)
            sage: H = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.is_isomorphic(H)
            False
            sage: G.is_isomorphic(G)
            True
            sage: G.is_isomorphic(PermutationGroup(list(reversed(v))))
            True
        """
    def is_monomial(self):
        """
        Return ``True`` if the group is monomial. A finite group is monomial
        if every irreducible complex character is induced from a linear
        character of a subgroup.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.is_monomial()
            True
        """
    def is_nilpotent(self):
        """
        Return ``True`` if this group is nilpotent.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: G.is_nilpotent()
            False
            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.is_nilpotent()
            True
        """
    def is_normal(self, other):
        """
        Return ``True`` if this group is a normal subgroup of ``other``.

        EXAMPLES::

            sage: AlternatingGroup(4).is_normal(SymmetricGroup(4))
            True
            sage: H = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: H.is_normal(G)
            False
        """
    def is_perfect(self):
        """
        Return ``True`` if this group is perfect. A group is perfect if it
        equals its derived subgroup.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: G.is_perfect()
            False
            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.is_perfect()
            False
        """
    def is_pgroup(self):
        """
        Return ``True`` if this group is a `p`-group.

        A finite group is a `p`-group if its order is of the form
        `p^n` for a prime integer `p` and a nonnegative integer `n`.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3,4,5)'])
            sage: G.is_pgroup()
            True
        """
    def is_polycyclic(self):
        """
        Return ``True`` if this group is polycyclic. A group is polycyclic if
        it has a subnormal series with cyclic factors. (For finite groups,
        this is the same as if the group is solvable - see
        :meth:`is_solvable`.)

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: G.is_polycyclic()
            False
            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.is_polycyclic()
            True
        """
    def is_simple(self):
        """
        Return ``True`` if the group is simple.

        A group is simple if it has no proper normal subgroups.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.is_simple()
            False
        """
    def is_solvable(self):
        """
        Return ``True`` if the group is solvable.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.is_solvable()
            True
        """
    def is_subgroup(self, other):
        """
        Return ``True`` if ``self`` is a subgroup of ``other``.

        EXAMPLES::

            sage: G = AlternatingGroup(5)
            sage: H = SymmetricGroup(5)
            sage: G.is_subgroup(H)
            True
        """
    def is_supersolvable(self):
        """
        Return ``True`` if the group is supersolvable.

        A finite group is supersolvable if it has a normal series
        with cyclic factors.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: G.is_supersolvable()
            True
        """
    def non_fixed_points(self):
        """
        Return the list of points not fixed by ``self``, i.e., the subset
        of ``self.domain()`` moved by some element of ``self``.

        EXAMPLES::

            sage: G = PermutationGroup([[(3,4,5)],[(7,10)]])
            sage: G.non_fixed_points()
            [3, 4, 5, 7, 10]
            sage: G = PermutationGroup([[(2,3,6)],[(9,)]]) # note: 9 is fixed
            sage: G.non_fixed_points()
            [2, 3, 6]
        """
    def fixed_points(self):
        """
        Return the list of points fixed by ``self``, i.e., the subset
        of ``.domain()`` not moved by any element of ``self``.

        EXAMPLES::

            sage: G = PermutationGroup([(1,2,3)])
            sage: G.fixed_points()
            []
            sage: G = PermutationGroup([(1,2,3),(5,6)])
            sage: G.fixed_points()
            [4]
            sage: G = PermutationGroup([[(1,4,7)],[(4,3),(6,7)]])
            sage: G.fixed_points()
            [2, 5]
        """
    def is_transitive(self, domain=None):
        """
        Return ``True`` if ``self`` acts transitively on ``domain``.

        A group `G` acts transitively on set `S` if for all `x,y\\in S`
        there is some `g\\in G` such that `x^g=y`.

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: G.is_transitive()
            True
            sage: G = PermutationGroup(['(1,2)(3,4)(5,6)'])
            sage: G.is_transitive()
            False

        ::

            sage: G = PermutationGroup([[(1,2,3,4,5)],[(1,2)],[(6,7)]])
            sage: G.is_transitive([1,2,3,4,5])
            True
            sage: G.is_transitive([1..7])
            False
            sage: G.is_transitive(G.non_fixed_points())
            False
            sage: H = PermutationGroup([[(1,2,3)],[(4,5,6)]])
            sage: H.is_transitive(H.non_fixed_points())
            False

        If `G` does not act on the domain, it always returns ``False``::

            sage: G = PermutationGroup([[(1,2,3,4,5)],[(1,2)]]) #S_5 on [1..5]
            sage: G.is_transitive([1,4,5])
            False

        Note that this differs from the definition in GAP, where
        ``IsTransitive`` returns whether the group is transitive on the
        set of points moved by the group.

        ::

            sage: G = PermutationGroup([(2,3)])
            sage: G.is_transitive()
            False
            sage: gap(G).IsTransitive()
            true
        """
    def is_primitive(self, domain=None):
        """
        Return ``True`` if ``self`` acts primitively on ``domain``.

        A group `G` acts primitively on a set `S` if

        1. `G` acts transitively on `S` and

        2. the action induces no non-trivial block system on `S`.

        INPUT:

        - ``domain`` -- optional

        .. SEEALSO::

            - :meth:`~PermutationGroup_generic.blocks_all`

        EXAMPLES:

        By default, test for primitivity of ``self`` on its domain::

            sage: G = PermutationGroup([[(1,2,3,4)],[(1,2)]])
            sage: G.is_primitive()
            True
            sage: G = PermutationGroup([[(1,2,3,4)],[(2,4)]])
            sage: G.is_primitive()
            False

        You can specify a domain on which to test primitivity::

            sage: G = PermutationGroup([[(1,2,3,4)],[(2,4)]])
            sage: G.is_primitive([1..4])
            False
            sage: G = PermutationGroup([[(3,4,5,6)],[(3,4)]]) #S_4 on [3..6]
            sage: G.is_primitive(G.non_fixed_points())
            True

        If `G` does not act on the domain, it always returns ``False``::

            sage: G = PermutationGroup([[(1,2,3,4)],[(2,4)]])
            sage: G.is_primitive([1,2,3])
            False
        """
    def is_semi_regular(self, domain=None):
        """
        Return ``True`` if ``self`` acts semi-regularly on ``domain``.

        A group `G` acts semi-regularly on a set `S` if the point
        stabilizers of `S` in `G` are trivial.

        ``domain`` is optional and may take several forms. See examples.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3,4)]])
            sage: G.is_semi_regular()
            True
            sage: G = PermutationGroup([[(1,2,3,4)],[(5,6)]])
            sage: G.is_semi_regular()
            False

        You can pass in a domain to test semi-regularity::

            sage: G = PermutationGroup([[(1,2,3,4)],[(5,6)]])
            sage: G.is_semi_regular([1..4])
            True
            sage: G.is_semi_regular(G.non_fixed_points())
            False
        """
    def is_regular(self, domain=None):
        """
        Return ``True`` if ``self`` acts regularly on ``domain``.

        A group `G` acts regularly on a set `S` if

        1. `G` acts transitively on `S` and
        2. `G` acts semi-regularly on `S`.

        EXAMPLES::

            sage: G = PermutationGroup([[(1,2,3,4)]])
            sage: G.is_regular()
            True
            sage: G = PermutationGroup([[(1,2,3,4)],[(5,6)]])
            sage: G.is_regular()
            False

        You can pass in a domain on which to test regularity::

            sage: G = PermutationGroup([[(1,2,3,4)],[(5,6)]])
            sage: G.is_regular([1..4])
            True
            sage: G.is_regular(G.non_fixed_points())
            False
        """
    def normalizes(self, other):
        """
        Return ``True`` if the group ``other`` is normalized by ``self``.

        Wraps GAP's ``IsNormal`` function.

        A group `G` normalizes a group `U` if and only if for every
        `g \\in G` and `u \\in U` the element `u^g`
        is a member of `U`. Note that `U` need not be a subgroup of `G`.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)(4,5)'])
            sage: H = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: H.normalizes(G)
            False
            sage: G = SymmetricGroup(3)
            sage: H = PermutationGroup( [ (4,5,6) ] )
            sage: G.normalizes(H)
            True
            sage: H.normalizes(G)
            True

        In the last example, `G` and `H` are disjoint, so each normalizes the
        other.
        """
    def composition_series(self):
        """
        Return the composition series of this group as a list of
        permutation groups.

        EXAMPLES:

        These computations use pseudo-random numbers, so we set
        the seed for reproducible testing.

        ::

            sage: set_random_seed(0)
            sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
            sage: G.composition_series()
            [Subgroup generated by [(3,4), (1,2,3)(4,5)] of
              (Permutation Group with generators [(3,4), (1,2,3)(4,5)]),
             Subgroup generated by [(1,5)(3,4), (1,5)(2,4), (1,3,5)] of
              (Permutation Group with generators [(3,4), (1,2,3)(4,5)]),
             Subgroup generated by [()] of
              (Permutation Group with generators [(3,4), (1,2,3)(4,5)])]
            sage: G = PermutationGroup([[(1,2,3),(4,5)], [(1,2)]])
            sage: CS = G.composition_series()
            sage: CS[3]
            Subgroup generated by [()] of
             (Permutation Group with generators [(1,2), (1,2,3)(4,5)])
        """
    def derived_series(self):
        """
        Return the derived series of this group as a list of permutation
        groups.

        EXAMPLES:

        These computations use pseudo-random numbers, so we set
        the seed for reproducible testing.

        ::

            sage: set_random_seed(0)
            sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
            sage: G.derived_series()
            [Subgroup generated by [(3,4), (1,2,3)(4,5)] of
              (Permutation Group with generators [(3,4), (1,2,3)(4,5)]),
             Subgroup generated by [(1,5)(3,4), (1,5)(2,4), (1,3,5)] of
              (Permutation Group with generators [(3,4), (1,2,3)(4,5)])]
        """
    def lower_central_series(self):
        """
        Return the lower central series of this group as a list of
        permutation groups.

        EXAMPLES:

        These computations use pseudo-random numbers, so we set
        the seed for reproducible testing.

        ::

            sage: set_random_seed(0)
            sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
            sage: G.lower_central_series()
            [Subgroup generated by [(3,4), (1,2,3)(4,5)] of
              (Permutation Group with generators [(3,4), (1,2,3)(4,5)]),
             Subgroup generated by [(1,5)(3,4), (1,5)(2,4), (1,3,5)] of
              (Permutation Group with generators [(3,4), (1,2,3)(4,5)])]
        """
    def molien_series(self):
        '''
        Return the Molien series of a permutation group. The
        function

        .. MATH::

                     M(x) = (1/|G|)\\sum_{g\\in G} \\det(1-x*g)^{-1}

        is sometimes called the "Molien series" of `G`. GAP\'s
        ``MolienSeries`` is associated to a character of a
        group `G`. How are these related? A group `G`, given as a permutation
        group on `n` points, has a "natural" representation of dimension `n`,
        given by permutation matrices. The Molien series of `G` is the one
        associated to that permutation representation of `G` using the above
        formula. Character values then count fixed points of the
        corresponding permutations.

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: G.molien_series()
            -1/(x^15 - x^14 - x^13 + x^10 + x^9 + x^8 - x^7 - x^6 - x^5 + x^2 + x - 1)
            sage: G = SymmetricGroup(3)
            sage: G.molien_series()
            -1/(x^6 - x^5 - x^4 + x^2 + x - 1)

        Some further tests (after :issue:`15817`)::

            sage: G = PermutationGroup([[(1,2,3,4)]])
            sage: S4ms = SymmetricGroup(4).molien_series()
            sage: G.molien_series() / S4ms
            x^5 + 2*x^4 + x^3 + x^2 + 1

        This works for not-transitive groups::

            sage: G = PermutationGroup([[(1,2)],[(3,4)]])
            sage: G.molien_series() / S4ms
            x^4 + x^3 + 2*x^2 + x + 1

        This works for groups with fixed points::

            sage: G = PermutationGroup([[(2,)]])
            sage: G.molien_series()
            1/(x^2 - 2*x + 1)

        TESTS:

        Check that :issue:`34854` is fixed::

            sage: PG = PermutationGroup(["(1,2,3,4,5,6,7)","(5,6,7)"])
            sage: PG.molien_series()
            (-x^18 + x^15 - x^12 + x^9 - x^6 + x^3 - 1)/(x^25 - x^24 - x^23 - x^22 + x^21 + 2*x^20 + x^19 - x^17 - x^16 - x^15 - x^13 + x^12 + x^10 + x^9 + x^8 - x^6 - 2*x^5 - x^4 + x^3 + x^2 + x - 1)

        and 2 extra fixed points are correctly accounted for::

            sage: PG1 = PermutationGroup(["(9,2,3,4,5,6,7)","(5,6,7)"])
            sage: R.<x> = QQ[]
            sage: PG.molien_series() == PG1.molien_series()*(1-x)^2
            True
        '''
    def normal_subgroups(self):
        """
        Return the normal subgroups of this group as a (sorted in
        increasing order) list of permutation groups.

        The normal subgroups of `H = PSL(2,7) \\times PSL(2,7)` are
        `1`, two copies of `PSL(2,7)` and `H`
        itself, as the following example shows.

        EXAMPLES::

            sage: G = PSL(2,7)
            sage: D = G.direct_product(G)
            sage: H = D[0]
            sage: NH = H.normal_subgroups()
            sage: len(NH)
            4
            sage: NH[1].is_isomorphic(G)
            True
            sage: NH[2].is_isomorphic(G)
            True
        """
    def poincare_series(self, p: int = 2, n: int = 10):
        """
        Return the Poincaré series of `G \\mod p` (`p \\geq 2` must be a prime),
        for `n` large.

        In other words, if you input a finite group `G`, a prime `p`, and a
        positive integer `n`, it returns a quotient of polynomials `f(x) = P(x)
        / Q(x)` whose coefficient of `x^k` equals the rank of the vector space
        `H_k(G, \\ZZ / p \\ZZ)`, for all `k` in the range `1 \\leq k \\leq n`.

        REQUIRES: GAP package HAP (in gap_packages-\\*.spkg).

        EXAMPLES::

            sage: G = SymmetricGroup(5)
            sage: G.poincare_series(2, 10)                             # optional - gap_package_hap
            (x^2 + 1)/(x^4 - x^3 - x + 1)
            sage: G = SymmetricGroup(3)
            sage: G.poincare_series(2, 10)                             # optional - gap_package_hap
            -1/(x - 1)

        AUTHORS:

        - David Joyner and Graham Ellis
        """
    def sylow_subgroup(self, p):
        """
        Return a Sylow `p`-subgroup of the finite group `G`, where `p` is a
        prime.

        This is a `p`-subgroup of `G` whose index in `G` is coprime
        to `p`.

        Wraps the GAP function ``SylowSubgroup``.

        EXAMPLES::

            sage: G = PermutationGroup(['(1,2,3)', '(2,3)'])
            sage: G.sylow_subgroup(2)
            Subgroup generated by [(2,3)] of
             (Permutation Group with generators [(2,3), (1,2,3)])
            sage: G.sylow_subgroup(5)
            Subgroup generated by [()] of
             (Permutation Group with generators [(2,3), (1,2,3)])

        TESTS:

        Implementation details should not prevent us from computing
        large subgroups (:issue:`5491`)::

            sage: PSL(10,2).sylow_subgroup(7)
            Subgroup generated by...
        """
    def upper_central_series(self):
        """
        Return the upper central series of this group as a list of
        permutation groups.

        EXAMPLES:

        These computations use pseudo-random numbers, so we set
        the seed for reproducible testing::

            sage: G = PermutationGroup([[(1,2,3),(4,5)],[(3,4)]])
            sage: G.upper_central_series()
            [Subgroup generated by [()] of
             (Permutation Group with generators [(3,4), (1,2,3)(4,5)])]
        """
    def sign_representation(self, base_ring=None):
        """
        Return the sign representation of ``self`` over ``base_ring``.

        INPUT:

        - ``base_ring`` -- (optional) the base ring; the default is `\\ZZ`

        EXAMPLES::

            sage: G = groups.permutation.Dihedral(4)
            sage: G.sign_representation()
            Sign representation of Dihedral group of order 8
             as a permutation group over Integer Ring
        """

class PermutationGroup_subgroup(PermutationGroup_generic):
    """
    Subgroup subclass of ``PermutationGroup_generic``, so instance methods
    are inherited.

    EXAMPLES::

        sage: G = CyclicPermutationGroup(4)
        sage: gens = G.gens()
        sage: H = DihedralGroup(4)
        sage: H.subgroup(gens)
        Subgroup generated by [(1,2,3,4)] of
         (Dihedral group of order 8 as a permutation group)
        sage: K = H.subgroup(gens)
        sage: K.list()
        [(), (1,2,3,4), (1,3)(2,4), (1,4,3,2)]
        sage: K.ambient_group()
        Dihedral group of order 8 as a permutation group
        sage: K.gens()
        ((1,2,3,4),)
    """
    def __init__(self, ambient, gens=None, gap_group=None, domain=None, category=None, canonicalize: bool = True, check: bool = True) -> None:
        """
        Initialization method for the
        ``PermutationGroup_subgroup`` class.

        INPUT:

        - ``ambient`` -- the ambient group from which to construct this
          subgroup

        - ``gens`` -- the generators of the subgroup

        - ``gap_group`` -- a GAP permutation group contained in the ambient group;
          constructed from ``gens`` if not given

        - ``check`` -- boolean (default: ``True``);  checks if ``gens`` are
          indeed elements of the ambient group

        - ``canonicalize`` -- boolean (default: ``True``); if ``True``, sort
          generators and remove duplicates

        EXAMPLES:

        An example involving the dihedral group on four elements.
        `D_8` contains a cyclic subgroup or order four::

            sage: G = DihedralGroup(4)
            sage: H = CyclicPermutationGroup(4)
            sage: gens = H.gens(); gens
            ((1,2,3,4),)
            sage: S = G.subgroup(gens)
            sage: S
            Subgroup generated by [(1,2,3,4)] of (Dihedral group of order 8 as a permutation group)
            sage: S.list()
            [(), (1,2,3,4), (1,3)(2,4), (1,4,3,2)]
            sage: S.ambient_group()
            Dihedral group of order 8 as a permutation group

        However, `D_8` does not contain a cyclic subgroup of order
        three::

            sage: G = DihedralGroup(4)
            sage: H = CyclicPermutationGroup(3)
            sage: gens = H.gens()
            sage: S = PermutationGroup_subgroup(G,list(gens))
            Traceback (most recent call last):
            ...
            ValueError: permutation (1,2,3) not in Dihedral group of order 8 as a permutation group
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` and ``other``.

        First, ``self`` and ``other`` are compared as permutation
        groups, see :meth:`PermutationGroup_generic.__richcmp__`.

        Second, if both are equal, the ambient groups are compared,
        where (if necessary) ``other`` is considered a subgroup of
        itself.

        EXAMPLES::

            sage: G = SymmetricGroup(6)
            sage: G1 = G.subgroup([G((1,2,3,4,5)),G((1,2))])
            sage: G2 = G.subgroup([G((1,2,3,4)),G((1,2))])
            sage: K = G2.subgroup([G2((1,2,3))])
            sage: H = G1.subgroup([G1(())])

        ``H`` is subgroup of ``K``, and therefore we have::

            sage: H < K
            True
            sage: K < H
            False

        In the next example, both ``H`` and ``H2`` are trivial
        groups, but the ambient group of ``H2`` is strictly contained
        in the ambient group of ``H``, and thus we obtain::

            sage: H2 = G2.subgroup([G2(())])
            sage: H2 < H
            True

        Of course, ``G`` as a permutation group and ``G`` considered
        as sub-group of itself are different objects. But they
        compare equal, both when considered as permutation groups
        or permutation subgroups::

            sage: G3 = G.subgroup([G((1,2,3,4,5,6)),G((1,2))])
            sage: G
            Symmetric group of order 6! as a permutation group
            sage: G3
            Subgroup generated by [(1,2,3,4,5,6), (1,2)] of
             (Symmetric group of order 6! as a permutation group)
            sage: G is G3
            False
            sage: G == G3 # as permutation groups
            True
            sage: G3 == G # as permutation subgroups
            True

        TESTS::

            sage: G = SymmetricGroup(4)
            sage: G.subgroup([G((1,2,3))]) == G.subgroup([G((2,3,1))])
            True
            sage: G.subgroup([G((1,2,3))]) == G.subgroup([G((1,3,2))])
            True
        """
    def ambient_group(self):
        """
        Return the ambient group related to ``self``.

        EXAMPLES:

        An example involving the dihedral group on four elements,
        `D_8`::

            sage: G = DihedralGroup(4)
            sage: H = CyclicPermutationGroup(4)
            sage: gens = H.gens()
            sage: S = PermutationGroup_subgroup(G, list(gens))
            sage: S.ambient_group()
            Dihedral group of order 8 as a permutation group
            sage: S.ambient_group() == G
            True
        """
    def is_normal(self, other=None):
        """
        Return ``True`` if this group is a normal subgroup of
        ``other``.  If ``other`` is not specified, then it is assumed
        to be the ambient group.

        EXAMPLES::

           sage: S = SymmetricGroup(['a','b','c'])
           sage: H = S.subgroup([('a', 'b', 'c')]); H
           Subgroup generated by [('a','b','c')] of
            (Symmetric group of order 3! as a permutation group)
           sage: H.is_normal()
           True
        """

class PermutationGroup_action(PermutationGroup_generic):
    """
    A permutation group given by a finite group action.

    EXAMPLES:

    A cyclic action::

        sage: n = 3
        sage: a = lambda x: SetPartition([[e % n + 1 for e in b] for b in x])
        sage: S = SetPartitions(n)                                                      # needs sage.combinat
        sage: G = PermutationGroup(action=a, domain=S)                                  # needs sage.combinat
        sage: G.orbits()                                                                # needs sage.combinat
        (({{1}, {2}, {3}},),
         ({{1, 2}, {3}}, {{1}, {2, 3}}, {{1, 3}, {2}}),
         ({{1, 2, 3}},))

    The regular action of the symmetric group::

        sage: a = lambda g, x: g*x*g^-1
        sage: S = SymmetricGroup(3)
        sage: G = PermutationGroup(S.gens(), action=a, domain=S)                        # needs sage.combinat
        sage: G.orbits()                                                                # needs sage.combinat
        (((),), ((1,3,2), (1,2,3)), ((2,3), (1,3), (1,2)))

    The trivial action of the symmetric group::

        sage: PermutationGroup(SymmetricGroup(3).gens(),                                # needs sage.combinat
        ....:                  action=lambda g, x: x, domain=[1])
        Permutation Group with generators [()]
    """
    def __init__(self, gens, action, domain, gap_group=None, category=None, canonicalize=None) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``gens`` -- list of generators of the group or ``None`` if the action is cyclic

        - ``action`` -- a group action `G \times X\to X` if ``gens``
          is given, or a cyclic group action `X\to X` if ``gens`` is
          ``None``

        - ``domain`` -- the set the group is acting on

        - ``gap_group`` -- a gap or libgap permutation group, or a string
          defining one (default: ``None``), this is currently not supported

        - ``canonicalize`` -- boolean (default: ``True``); if ``True``,
          sort generators and remove duplicates

        OUTPUT: a finite group action given as a permutation group

        EXAMPLES::

            sage: a = lambda x: (2*x) % 7
            sage: G = PermutationGroup(action=a, domain=range(7))                       # needs sage.combinat
            sage: G.orbits()                                                            # needs sage.combinat
            ((0,), (1, 2, 4), (3, 6, 5))
        """
    def orbits(self):
        """
        Return the orbits of the elements of the domain under the
        default group action.

        EXAMPLES::

            sage: a = lambda x: (2*x) % 7
            sage: G = PermutationGroup(action=a, domain=range(7))                       # needs sage.combinat
            sage: G.orbits()                                                            # needs sage.combinat
            ((0,), (1, 2, 4), (3, 6, 5))
        """

__doc__: Incomplete
