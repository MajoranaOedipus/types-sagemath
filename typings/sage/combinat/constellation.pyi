from sage.categories.groups import Groups as Groups
from sage.combinat.partition import Partition as Partition
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.integer import Integer as Integer
from sage.structure.element import Element as Element, parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, rich_to_bool as rich_to_bool, richcmp_not_equal as richcmp_not_equal
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

def Constellations(*data, **options):
    """
    Build a set of constellations.

    INPUT:

    - ``profile`` -- an optional profile

    - ``length`` -- an optional length

    - ``degree`` -- an optional degree

    - ``connected`` -- an optional boolean

    EXAMPLES::

        sage: Constellations(4,2)
        Connected constellations of length 4 and degree 2 on {1, 2}

        sage: Constellations([[3,2,1],[3,3],[3,3]])
        Connected constellations with profile ([3, 2, 1], [3, 3], [3, 3]) on {1, 2, 3, 4, 5, 6}
    """
def Constellation(g=None, mutable: bool = False, connected: bool = True, check: bool = True):
    """
    Constellation.

    INPUT:

    - ``g`` -- list of permutations

    - ``mutable`` -- boolean (default: ``False``); whether the result is
      mutable or not

    - ``connected`` -- boolean (default: ``True``); whether the result should
      be connected

    - ``check`` -- boolean (default: ``True``); whether or not to check. If it
      is ``True``, then the list ``g`` must contain no ``None``.

    EXAMPLES:

    Simple initialization::

        sage: Constellation(['(0,1)','(0,3)(1,2)','(0,3,1,2)'])
        Constellation of length 3 and degree 4
        g0 (0,1)(2)(3)
        g1 (0,3)(1,2)
        g2 (0,3,1,2)

    One of the permutation can be omitted::

        sage: Constellation(['(0,1)', None, '(0,4)(1,2,3)'])
        Constellation of length 3 and degree 5
        g0 (0,1)(2)(3)(4)
        g1 (0,3,2,1,4)
        g2 (0,4)(1,2,3)

    One can define mutable constellations::

        sage: Constellation(([0,2,1], [2,1,0], [1,2,0]), mutable=True)
        Constellation of length 3 and degree 3
        g0 (0)(1,2)
        g1 (0,2)(1)
        g2 (0,1,2)
    """

class Constellation_class(Element):
    """
    Constellation.

    A constellation or a tuple of permutations `(g_0,g_1,...,g_k)`
    such that the product `g_0 g_1 ... g_k` is the identity.
    """
    def __init__(self, parent, g, connected, mutable, check) -> None:
        """
        TESTS::

            sage: c = Constellation([[1,2,0],[0,2,1],[1,0,2],None])
            sage: c == loads(dumps(c))
            True
            sage: g0 = '(0,1)(2,4)'
            sage: g1 = '(0,3)(1,4)'
            sage: g2 = '(2,4,3)'
            sage: g3 = '(0,3)(1,2)'
            sage: c0 = Constellation([g0,g1,g2,g3])
            sage: c0 == Constellation([None,g1,g2,g3])
            True
            sage: c0 == Constellation([g0,None,g2,g3])
            True
            sage: c0 == Constellation([g0,g1,None,g3])
            True
            sage: c0 == Constellation([g0,g1,g2,None])
            True
        """
    def __hash__(self):
        """
        Return a hash for ``self``.

        EXAMPLES::

            sage: c = Constellation(([0,2,1],[2,1,0],[1,2,0]), mutable=False)
            sage: hash(c) == hash(tuple(c._g))
            True
        """
    def set_immutable(self) -> None:
        """
        Do nothing, as ``self`` is already immutable.

        EXAMPLES::

            sage: c = Constellation(([0,2,1],[2,1,0],[1,2,0]), mutable=False)
            sage: c.set_immutable()
            sage: c.is_mutable()
            False
        """
    def is_mutable(self):
        """
        Return ``False`` as ``self`` is immutable.

        EXAMPLES::

            sage: c = Constellation(([0,2,1],[2,1,0],[1,2,0]), mutable=False)
            sage: c.is_mutable()
            False
        """
    def switch(self, i, j0, j1) -> None:
        """
        Perform the multiplication by the transposition `(j0, j1)` between the
        permutations `g_i` and `g_{i+1}`.

        The modification is local in the sense that it modifies `g_i`
        and `g_{i+1}` but does not modify the product `g_i g_{i+1}`. The new
        constellation is

        .. MATH::

            (g_0, \\ldots, g_{i-1}, g_{i} (j0 j1), (j0 j1) g_{i+1}, g_{i+2}, \\ldots, g_k)

        EXAMPLES::

            sage: c = Constellation(['(0,1)(2,3,4)','(1,4)',None], mutable=True); c
            Constellation of length 3 and degree 5
            g0 (0,1)(2,3,4)
            g1 (0)(1,4)(2)(3)
            g2 (0,1,3,2,4)
            sage: c.is_mutable()
            True
            sage: c.switch(1,2,3); c
            Constellation of length 3 and degree 5
            g0 (0,1)(2,3,4)
            g1 (0)(1,4)(2,3)
            g2 (0,1,3,4)(2)
            sage: c._check()
            sage: c.switch(2,1,3); c
            Constellation of length 3 and degree 5
            g0 (0,1,4,2,3)
            g1 (0)(1,4)(2,3)
            g2 (0,3,4)(1)(2)
            sage: c._check()
            sage: c.switch(0,0,1); c
            Constellation of length 3 and degree 5
            g0 (0)(1,4,2,3)
            g1 (0,4,1)(2,3)
            g2 (0,3,4)(1)(2)
            sage: c._check()
        """
    def euler_characteristic(self):
        """
        Return the Euler characteristic of the surface.

        ALGORITHM:

        Hurwitz formula

        EXAMPLES::

            sage: c = Constellation(['(0,1)', '(0,2)', None])
            sage: c.euler_characteristic()
            2

            sage: c = Constellation(['(0,1,2,3)','(1,3,0,2)', '(0,3,1,2)', None])
            sage: c.euler_characteristic()
            -4

        TESTS::

            sage: parent(c.euler_characteristic())
            Integer Ring
        """
    def genus(self):
        """
        Return the genus of the surface.

        EXAMPLES::

            sage: c = Constellation(['(0,1)', '(0,2)', None])
            sage: c.genus()
            0

            sage: c = Constellation(['(0,1)(2,3,4)','(1,3,4)(2,0)', None])
            sage: c.genus()
            1

        TESTS::

            sage: parent(c.genus())
            Integer Ring
        """
    def __copy__(self):
        """
        Return a copy of ``self``.

        TESTS::

            sage: c = Constellation([[0,2,1],[1,0,2],[2,1,0],None])
            sage: c == copy(c)
            True
            sage: c is copy(c)
            False
            sage: c = Constellation([[0,2,1],[1,0,2],[2,1,0],None],mutable=True)
            sage: c == copy(c)
            True
            sage: c is copy(c)
            False
        """
    copy = __copy__
    def mutable_copy(self):
        """
        Return a mutable copy of ``self``.

        EXAMPLES::

            sage: c = Constellation(([0,2,1],[2,1,0],[1,2,0]), mutable=False)
            sage: d = c.mutable_copy()
            sage: d.is_mutable()
            True
        """
    def is_connected(self):
        """
        Test of connectedness.

        EXAMPLES::

            sage: c = Constellation(['(0,1)(2)', None, '(0,1)(2)'], connected=False)
            sage: c.is_connected()
            False
            sage: c = Constellation(['(0,1,2)', None], connected=False)
            sage: c.is_connected()
            True
        """
    def connected_components(self):
        """
        Return the connected components.

        OUTPUT: list of connected constellations

        EXAMPLES::

            sage: c = Constellation(['(0,1)(2)', None, '(0,1)(2)'], connected=False)
            sage: cc = c.connected_components(); cc
            [Constellation of length 3 and degree 2
            g0 (0,1)
            g1 (0)(1)
            g2 (0,1),
            Constellation of length 3 and degree 1
            g0 (0)
            g1 (0)
            g2 (0)]
            sage: all(c2.is_connected() for c2 in cc)
            True

            sage: c = Constellation(['(0,1,2)', None], connected=False)
            sage: c.connected_components()
            [Constellation of length 2 and degree 3
            g0 (0,1,2)
            g1 (0,2,1)]
        """
    def is_isomorphic(self, other, return_map: bool = False):
        """
        Test of isomorphism.

        Return ``True`` if the constellations are isomorphic
        (*i.e.* related by a common conjugacy) and return the permutation that
        conjugate the two permutations if ``return_map`` is ``True`` in
        such a way that ``self.relabel(m) == other``.

        ALGORITHM:

        uses canonical labels obtained from the method :meth:`relabel`.

        EXAMPLES::

            sage: c = Constellation([[1,0,2],[2,1,0],[0,2,1],None])
            sage: d = Constellation([[2,1,0],[0,2,1],[1,0,2],None])
            sage: answer, mapping = c.is_isomorphic(d,return_map=True)
            sage: answer
            True
            sage: c.relabel(mapping) == d
            True
        """
    def degree(self):
        """
        Return the degree of the constellation.

        The degree of a constellation is the number `n` that
        corresponds to the symmetric group `S(n)` in which the
        permutations of the constellation are defined.

        EXAMPLES::

            sage: c = Constellation([])
            sage: c.degree()
            0
            sage: c = Constellation(['(0,1)',None])
            sage: c.degree()
            2
            sage: c = Constellation(['(0,1)','(0,3,2)(1,5)',None,'(4,3,2,1)'])
            sage: c.degree()
            6

        TESTS::

            sage: parent(c.degree())
            Integer Ring
        """
    def length(self):
        """
        Return the number of permutations.

        EXAMPLES::

            sage: c = Constellation(['(0,1)','(0,2)','(0,3)',None])
            sage: c.length()
            4
            sage: c = Constellation(['(0,1,3)',None,'(1,2)'])
            sage: c.length()
            3

        TESTS::

            sage: parent(c.length())
            Integer Ring
        """
    def profile(self, i=None):
        """
        Return the profile of ``self``.

        The profile of a constellation is the tuple of partitions
        associated to the conjugacy classes of the permutations of the
        constellation.

        This is also called the passport.

        EXAMPLES::

            sage: c = Constellation(['(0,1,2)(3,4)','(0,3)',None])
            sage: c.profile()
            ([3, 2], [2, 1, 1, 1], [5])
        """
    passport = profile
    def g(self, i=None):
        """
        Return the permutation `g_i` of the constellation.

        INPUT:

        - ``i`` -- integer or ``None`` (default)

        If ``None`` , return instead the list of all `g_i`.

        EXAMPLES::

            sage: c = Constellation(['(0,1,2)(3,4)','(0,3)',None])
            sage: c.g(0)
            (0,1,2)(3,4)
            sage: c.g(1)
            (0,3)
            sage: c.g(2)
            (0,4,3,2,1)
            sage: c.g()
            [(0,1,2)(3,4), (0,3), (0,4,3,2,1)]
        """
    def relabel(self, perm=None, return_map: bool = False):
        '''
        Relabel ``self``.

        If ``perm`` is provided then relabel with respect to ``perm``. Otherwise
        use canonical labels. In that case, if ``return_map`` is provided, the
        return also the map used for canonical labels.

        Algorithm:

        the cycle for g(0) are adjacent and the cycle are joined with
        respect to the other permutations. The minimum is taken for
        all possible renumerotations.

        EXAMPLES::

            sage: c = Constellation([\'(0,1)(2,3,4)\',\'(1,4)\',None]); c
            Constellation of length 3 and degree 5
            g0 (0,1)(2,3,4)
            g1 (0)(1,4)(2)(3)
            g2 (0,1,3,2,4)
            sage: c2 = c.relabel(); c2
            Constellation of length 3 and degree 5
            g0 (0,1)(2,3,4)
            g1 (0)(1,2)(3)(4)
            g2 (0,1,4,3,2)

        The map returned when the option ``return_map`` is set to
        ``True`` can be used to set the relabelling::

            sage: c3, perm = c.relabel(return_map=True)
            sage: c3 == c2 and c3 == c.relabel(perm=perm)
            True

            sage: S5 = SymmetricGroup(range(5))
            sage: d = c.relabel(S5([4,3,1,0,2])); d
            Constellation of length 3 and degree 5
            g0 (0,2,1)(3,4)
            g1 (0)(1)(2,3)(4)
            g2 (0,1,2,4,3)
            sage: d.is_isomorphic(c)
            True

        We check that after a random relabelling the new constellation is
        isomorphic to the initial one::

            sage: c = Constellation([\'(0,1)(2,3,4)\',\'(1,4)\',None])
            sage: p = S5.random_element()
            sage: cc = c.relabel(perm=p)
            sage: cc.is_isomorphic(c)
            True

        Check that it works for "non standard" labels::

            sage: c = Constellation([((\'a\',\'b\'),(\'c\',\'d\',\'e\')),(\'b\',\'d\'), None])
            sage: c.relabel()
            Constellation of length 3 and degree 5
            g0 (\'a\',\'b\')(\'c\',\'d\',\'e\')
            g1 (\'a\')(\'b\',\'c\')(\'d\')(\'e\')
            g2 (\'a\',\'b\',\'e\',\'d\',\'c\')
        '''
    def braid_group_action(self, i):
        """
        Act on ``self`` as the braid group generator that exchanges
        position `i` and `i+1`.

        INPUT:

        - ``i`` -- integer in `[0, n-1]` where `n` is the length of ``self``

        EXAMPLES::

            sage: sigma = lambda c, i: c.braid_group_action(i)

            sage: c = Constellation(['(0,1)(2,3,4)','(1,4)',None]); c
            Constellation of length 3 and degree 5
            g0 (0,1)(2,3,4)
            g1 (0)(1,4)(2)(3)
            g2 (0,1,3,2,4)
            sage: sigma(c, 1)
            Constellation of length 3 and degree 5
            g0 (0,1)(2,3,4)
            g1 (0,1,3,2,4)
            g2 (0,3)(1)(2)(4)

        Check the commutation relation::

            sage: c = Constellation(['(0,1)(2,3,4)','(1,4)','(2,5)(0,4)',None])
            sage: d = Constellation(['(0,1,3,5)','(2,3,4)','(0,3,5)',None])
            sage: c13 = sigma(sigma(c, 0), 2)
            sage: c31 = sigma(sigma(c, 2), 0)
            sage: c13 == c31
            True
            sage: d13 = sigma(sigma(d, 0), 2)
            sage: d31 = sigma(sigma(d, 2), 0)
            sage: d13 == d31
            True

        Check the braid relation::

            sage: c121 = sigma(sigma(sigma(c, 1), 2), 1)
            sage: c212 = sigma(sigma(sigma(c, 2), 1), 2)
            sage: c121 == c212
            True
            sage: d121 = sigma(sigma(sigma(d, 1), 2), 1)
            sage: d212 = sigma(sigma(sigma(d, 2), 1), 2)
            sage: d121 == d212
            True
        """
    def braid_group_orbit(self):
        """
        Return the graph of the action of the braid group.

        The action is considered up to isomorphism of constellation.

        EXAMPLES::

            sage: c = Constellation(['(0,1)(2,3,4)','(1,4)',None]); c
            Constellation of length 3 and degree 5
            g0 (0,1)(2,3,4)
            g1 (0)(1,4)(2)(3)
            g2 (0,1,3,2,4)
            sage: G = c.braid_group_orbit()
            sage: G.num_verts()
            4
            sage: G.num_edges()
            12
        """

class Constellations_ld(UniqueRepresentation, Parent):
    """
    Constellations of given length and degree.

    EXAMPLES::

        sage: C = Constellations(2,3); C
        Connected constellations of length 2 and degree 3 on {1, 2, 3}
        sage: C([[2,3,1],[3,1,2]])
        Constellation of length 2 and degree 3
        g0 (1,2,3)
        g1 (1,3,2)
        sage: C.cardinality()
        2
        sage: Constellations(2,3,connected=False).cardinality()
        6
    """
    Element = Constellation_class
    def __init__(self, length, degree, sym=None, connected: bool = True) -> None:
        """
        TESTS::

            sage: TestSuite(Constellations(length=6,degree=4)).run(skip='_test_cardinality')
        """
    def is_empty(self):
        """
        Return whether this set of constellations is empty.

        EXAMPLES::

            sage: Constellations(2, 3).is_empty()
            False
            sage: Constellations(1, 2).is_empty()
            True
            sage: Constellations(1, 2, connected=False).is_empty()
            False
        """
    def __contains__(self, elt) -> bool:
        """
        TESTS::

            sage: C = Constellations(2, 3, connected=True)
            sage: D = Constellations(2, 3, connected=False)
            sage: e1 = [[3,1,2], None]
            sage: e2 = [[1,2,3], None]
            sage: C(e1) in C
            True
            sage: D(e1) in C
            True
            sage: D(e1) in D
            True
            sage: D(e2) in C
            False
            sage: D(e2) in D
            True

            sage: e1 in C and e1 in D
            True
            sage: e2 in C
            False
            sage: e2 in D
            True
        """
    def __iter__(self):
        """
        Iterator over all constellations of given degree and length.

        EXAMPLES::

            sage: const = Constellations(3,3); const
            Connected constellations of length 3 and degree 3 on {1, 2, 3}
            sage: len([v for v in const])
            26

        One can check the first few terms of sequence :oeis:`220754`::

            sage: Constellations(4,1).cardinality()
            1
            sage: Constellations(4,2).cardinality()
            7
            sage: Constellations(4,3).cardinality()
            194
            sage: Constellations(4,4).cardinality()  # long time
            12858
        """
    def random_element(self, mutable: bool = False):
        """
        Return a random element.

        This is found by trial and rejection, starting from
        a random list of permutations.

        EXAMPLES::

            sage: const = Constellations(3,3)
            sage: const.random_element()
            Constellation of length 3 and degree 3
            ...
            ...
            ...
            sage: c = const.random_element()
            sage: c.degree() == 3 and c.length() == 3
            True
        """
    def braid_group_action(self):
        """
        Return a list of graphs that corresponds to the braid group action on
        ``self`` up to isomorphism.

        OUTPUT: list of graphs

        EXAMPLES::

            sage: C = Constellations(3,3)
            sage: C.braid_group_action()
            [Looped multi-digraph on 3 vertices,
             Looped multi-digraph on 1 vertex,
             Looped multi-digraph on 3 vertices]
        """
    def braid_group_orbits(self):
        """
        Return the orbits under the action of braid group.

        EXAMPLES::

            sage: C = Constellations(3,3)
            sage: O = C.braid_group_orbits()
            sage: len(O)
            3
            sage: [x.profile() for x in O[0]]
            [([1, 1, 1], [3], [3]), ([3], [1, 1, 1], [3]), ([3], [3], [1, 1, 1])]
            sage: [x.profile() for x in O[1]]
            [([3], [3], [3])]
            sage: [x.profile() for x in O[2]]
            [([2, 1], [2, 1], [3]), ([2, 1], [3], [2, 1]), ([3], [2, 1], [2, 1])]
        """

class Constellations_p(UniqueRepresentation, Parent):
    """
    Constellations with fixed profile.

    EXAMPLES::

        sage: C = Constellations([[3,1],[3,1],[2,2]]); C
        Connected constellations with profile ([3, 1], [3, 1], [2, 2]) on {1, 2, 3, 4}
        sage: C.cardinality()
        24
        sage: C.first()
        Constellation of length 3 and degree 4
        g0 (1)(2,3,4)
        g1 (1,2,3)(4)
        g2 (1,2)(3,4)
        sage: C.last()
        Constellation of length 3 and degree 4
        g0 (1,4,3)(2)
        g1 (1,4,2)(3)
        g2 (1,2)(3,4)

    Note that the cardinality can also be computed using characters of the
    symmetric group (Frobenius formula)::

        sage: P = Partitions(4)
        sage: p1 = Partition([3,1])
        sage: p2 = Partition([3,1])
        sage: p3 = Partition([2,2])
        sage: i1 = P.cardinality() - P.rank(p1) - 1
        sage: i2 = P.cardinality() - P.rank(p2) - 1
        sage: i3 = P.cardinality() - P.rank(p3) - 1
        sage: s = 0
        sage: for c in SymmetricGroup(4).irreducible_characters():
        ....:     v = c.values()
        ....:     s += v[i1] * v[i2] * v[i3] / v[0]
        sage: c1 = p1.conjugacy_class_size()
        sage: c2 = p2.conjugacy_class_size()
        sage: c3 = p3.conjugacy_class_size()
        sage: c1 * c2 * c3 / factorial(4)**2 * s
        1

    The number obtained above is up to isomorphism. And we can check::

        sage: len(C.isomorphism_representatives())
        1
    """
    def __init__(self, profile, domain=None, connected: bool = True) -> None:
        """
        OPTIONS:

        - ``profile`` -- list of integer partitions of the same integer

        - ``connected`` -- boolean (default: ``True``); whether we consider
          only connected constellations

        TESTS::

            sage: C = Constellations([(3,1),(3,1),(2,2)])
            sage: TestSuite(C).run()
        """
    def isomorphism_representatives(self):
        """
        Return a set of isomorphism representative of ``self``.

        EXAMPLES::

            sage: C = Constellations([[5], [4,1], [3,2]])
            sage: C.cardinality()
            240
            sage: ir = sorted(C.isomorphism_representatives())
            sage: len(ir)
            2
            sage: ir[0]
            Constellation of length 3 and degree 5
            g0 (1,2,3,4,5)
            g1 (1)(2,3,4,5)
            g2 (1,5,3)(2,4)
            sage: ir[1]
            Constellation of length 3 and degree 5
            g0 (1,2,3,4,5)
            g1 (1)(2,5,3,4)
            g2 (1,5)(2,3,4)
        """
    def __iter__(self):
        """
        Iterator of the elements in ``self``.

        TESTS::

            sage: C = Constellations([(3,1),(3,1),(2,2)])
            sage: for c in C: print(c)
            Constellation of length 3 and degree 4
            g0 (1)(2,3,4)
            g1 (1,2,3)(4)
            g2 (1,2)(3,4)
            Constellation of length 3 and degree 4
            g0 (1)(2,3,4)
            g1 (1,4,2)(3)
            g2 (1,4)(2,3)
            ...
            Constellation of length 3 and degree 4
            g0 (1,4,3)(2)
            g1 (1,2,3)(4)
            g2 (1,4)(2,3)
            Constellation of length 3 and degree 4
            g0 (1,4,3)(2)
            g1 (1,4,2)(3)
            g2 (1,2)(3,4)

            sage: C = Constellations([(3,1),(3,1),(2,2)], domain='abcd')
            sage: for c in sorted(C): print(c)
            Constellation of length 3 and degree 4
            g0 ('a')('b','c','d')
            g1 ('a','b','c')('d')
            g2 ('a','b')('c','d')
            ...
            Constellation of length 3 and degree 4
            g0 ('a','d','c')('b')
            g1 ('a','d','b')('c')
            g2 ('a','b')('c','d')
        """

def perm_sym_domain(g):
    """
    Return the domain of a single permutation (before initialization).

    EXAMPLES::

        sage: from sage.combinat.constellation import perm_sym_domain
        sage: perm_sym_domain([1,2,3,4])
        {1, 2, 3, 4}
        sage: perm_sym_domain(((1,2),(0,4)))
        {0, 1, 2, 4}
        sage: sorted(perm_sym_domain('(1,2,0,5)'))
        [0, 1, 2, 5]
    """
def perms_sym_init(g, sym=None):
    """
    Initialize a list of permutations (in the same symmetric group).

    OUTPUT:

    - ``sym`` -- a symmetric group

    - ``gg`` -- list of permutations

    EXAMPLES::

        sage: from sage.combinat.constellation import perms_sym_init
        sage: S, g = perms_sym_init([[0,2,1,3], [1,3,2,0]])
        sage: S.domain()
        {0, 1, 2, 3}
        sage: g
        [(1,2), (0,1,3)]

        sage: S, g = perms_sym_init(['(2,1)', '(0,3)'])
        sage: S.domain()
        {0, 1, 2, 3}
        sage: g
        [(1,2), (0,3)]

        sage: S, g = perms_sym_init([(1,0), (2,1)])
        sage: S.domain()
        {0, 1, 2}
        sage: g
        [(0,1), (1,2)]

        sage: S, g = perms_sym_init([((1,0),(2,3)), '(0,1,4)'])
        sage: S.domain()
        {0, 1, 2, 3, 4}
        sage: g
        [(0,1)(2,3), (0,1,4)]
    """
def perms_are_connected(g, n):
    """
    Check that the action of the generated group is transitive.

    INPUT:

    - ``g`` -- list of permutations of `[0, n-1]` (in a SymmetricGroup)

    - ``n`` -- integer

    EXAMPLES::

        sage: from sage.combinat.constellation import perms_are_connected
        sage: S = SymmetricGroup(range(3))
        sage: perms_are_connected([S([0,1,2]),S([0,2,1])],3)
        False
        sage: perms_are_connected([S([0,1,2]),S([1,2,0])],3)
        True
    """
def perms_canonical_labels_from(x, y, j0, verbose: bool = False):
    """
    Return canonical labels for ``x``, ``y`` that starts at ``j0``.

    .. WARNING::

        The group generated by ``x`` and the elements of ``y`` should be
        transitive.

    INPUT:

    - ``x`` -- list; a permutation of `[0, ..., n]` as a list

    - ``y`` -- list of permutations of `[0, ..., n]` as a list of lists

    - ``j0`` -- an index in [0, ..., n]

    OUTPUT: mapping: a permutation that specify the new labels

    EXAMPLES::

        sage: from sage.combinat.constellation import perms_canonical_labels_from
        sage: perms_canonical_labels_from([0,1,2],[[1,2,0]], 0)
        [0, 1, 2]
        sage: perms_canonical_labels_from([1,0,2], [[2,0,1]], 0)
        [0, 1, 2]
        sage: perms_canonical_labels_from([1,0,2], [[2,0,1]], 1)
        [1, 0, 2]
        sage: perms_canonical_labels_from([1,0,2], [[2,0,1]], 2)
        [2, 1, 0]
    """
def perm_invert(p):
    """
    Return the inverse of the permutation `p`.

    INPUT:

    - ``p`` -- a permutation of {0,..,n-1} given by a list of values

    OUTPUT: a permutation of {0,..,n-1} given by a list of values

    EXAMPLES::

        sage: from sage.combinat.constellation import perm_invert
        sage: perm_invert([3,2,0,1])
        [2, 3, 1, 0]
    """
def perm_conjugate(p, s):
    """
    Return the conjugate of the permutation `p` by the permutation `s`.

    INPUT:

    - ``p``, ``s`` -- two permutations of {0,..,n-1} given by lists of values

    OUTPUT: a permutation of {0,..,n-1} given by a list of values

    EXAMPLES::

        sage: from sage.combinat.constellation import perm_conjugate
        sage: perm_conjugate([3,1,2,0], [3,2,0,1])
        [0, 3, 2, 1]
    """
def perms_canonical_labels(p, e=None):
    """
    Relabel a list with a common conjugation such that two conjugated
    lists are relabeled the same way.

    INPUT:

    - ``p`` -- list of at least 2 permutations

    - ``e`` -- ``None`` or a list of integer in the domain of the
      permutations. If provided, then the renumbering algorithm is
      only performed from the elements of ``e``.

    OUTPUT: a pair made of a list of permutations (as a list of lists) and a
    list that corresponds to the conjugacy used.

    EXAMPLES::

        sage: from sage.combinat.constellation import perms_canonical_labels
        sage: l0 = [[2,0,3,1], [3,1,2,0], [0,2,1,3]]
        sage: l, m = perms_canonical_labels(l0); l
        [[1, 2, 3, 0], [0, 3, 2, 1], [2, 1, 0, 3]]

        sage: S = SymmetricGroup(range(4))
        sage: [~S(m) * S(u) * S(m) for u in l0] == list(map(S, l))
        True

        sage: perms_canonical_labels([])
        Traceback (most recent call last):
        ...
        ValueError: input must have length >= 2
    """
