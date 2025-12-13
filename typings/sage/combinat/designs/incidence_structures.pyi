from _typeshed import Incomplete
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.rest_index_of_methods import gen_rest_table_index as gen_rest_table_index
from sage.rings.integer import Integer as Integer
from sage.sets.set import Set as Set

class IncidenceStructure:
    '''
    A base class for incidence structures (i.e. hypergraphs, i.e. set systems)

    An incidence structure (i.e. hypergraph, i.e. set system) can be defined
    from a collection of blocks (i.e. sets, i.e. edges), optionally with an
    explicit ground set (i.e. point set, i.e. vertex set). Alternatively they
    can be defined from a binary incidence matrix.

    INPUT:

    - ``points`` -- (i.e. ground set, i.e. vertex set) the underlying set. If
      ``points`` is an integer `v`, then the set is considered to be `\\{0, ...,
      v-1\\}`.

      .. NOTE::

          The following syntax, where ``points`` is omitted, automatically
          defines the ground set as the union of the blocks::

              sage: H = IncidenceStructure([[\'a\',\'b\',\'c\'],[\'c\',\'d\',\'e\']])
              sage: sorted(H.ground_set())
              [\'a\', \'b\', \'c\', \'d\', \'e\']

    - ``blocks`` -- (i.e. edges, i.e. sets) the blocks defining the incidence
      structure; can be any iterable

    - ``incidence_matrix`` -- a binary incidence matrix; each column represents
      a set

    - ``name`` -- string (such as "Fano plane")

    - ``check`` -- whether to check the input

    - ``copy`` -- (use with caution) if set to ``False`` then ``blocks`` must be
      a list of lists of integers. The list will not be copied but will be
      modified in place (each block is sorted, and the whole list is
      sorted). Your ``blocks`` object will become the
      :class:`IncidenceStructure` instance\'s internal data.

    EXAMPLES:

    An incidence structure can be constructed by giving the number of points and
    the list of blocks::

        sage: IncidenceStructure(7, [[0,1,2],[0,3,4],[0,5,6],[1,3,5],[1,4,6],[2,3,6],[2,4,5]])
        Incidence structure with 7 points and 7 blocks

    Only providing the set of blocks is sufficient. In this case, the ground set
    is defined as the union of the blocks::

        sage: IncidenceStructure([[1,2,3],[2,3,4]])
        Incidence structure with 4 points and 2 blocks

    Or by its adjacency matrix (a `\\{0,1\\}`-matrix in which rows are indexed by
    points and columns by blocks)::

        sage: m = matrix([[0,1,0],[0,0,1],[1,0,1],[1,1,1]])                             # needs sage.modules
        sage: IncidenceStructure(m)                                                     # needs sage.modules
        Incidence structure with 4 points and 3 blocks

    The points can be any (hashable) object::

        sage: V = [(0,\'a\'),(0,\'b\'),(1,\'a\'),(1,\'b\')]
        sage: B = [(V[0],V[1],V[2]), (V[1],V[2]), (V[0],V[2])]
        sage: I = IncidenceStructure(V, B)
        sage: I.ground_set()
        [(0, \'a\'), (0, \'b\'), (1, \'a\'), (1, \'b\')]
        sage: I.blocks()
        [[(0, \'a\'), (0, \'b\'), (1, \'a\')], [(0, \'a\'), (1, \'a\')], [(0, \'b\'), (1, \'a\')]]

    The order of the points and blocks does not matter as they are sorted on
    input (see :issue:`11333`)::

        sage: A = IncidenceStructure([0,1,2], [[0],[0,2]])
        sage: B = IncidenceStructure([1,0,2], [[0],[2,0]])
        sage: B == A
        True

        sage: C = BlockDesign(2, [[0], [1,0]])
        sage: D = BlockDesign(2, [[0,1], [0]])
        sage: C == D
        True

    If you care for speed, you can set ``copy`` to ``False``, but in that
    case, your input must be a list of lists and the ground set must be `{0,
    ..., v-1}`::

        sage: blocks = [[0,1],[2,0],[1,2]]  # a list of lists of integers
        sage: I = IncidenceStructure(3, blocks, copy=False)
        sage: I._blocks is blocks
        True
    '''
    def __init__(self, points=None, blocks=None, incidence_matrix=None, name=None, check: bool = True, copy: bool = True) -> None:
        """
        TESTS::

            sage: IncidenceStructure(3, [[4]])
            Traceback (most recent call last):
            ...
            ValueError: Block [4] is not contained in the point set

            sage: IncidenceStructure(3, [[0,1],[0,2]], check=True)
            Incidence structure with 3 points and 2 blocks

            sage: IncidenceStructure(2, [[0,1,2,3,4,5]], check=False)
            Incidence structure with 2 points and 1 blocks

        We avoid to convert to integers when the points are not (but compare
        equal to integers because of coercion)::

            sage: # needs sage.rings.finite_rings
            sage: V = GF(5)
            sage: e0,e1,e2,e3,e4 = V
            sage: [e0,e1,e2,e3,e4] == list(range(5))  # coercion makes them equal
            True
            sage: blocks = [[e0,e1,e2],[e0,e1],[e2,e4]]
            sage: I = IncidenceStructure(V, blocks)
            sage: type(I.ground_set()[0])
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: type(I.blocks()[0][0])
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>

        TESTS::

            sage: IncidenceStructure([])
            Incidence structure with 0 points and 0 blocks
        """
    def __iter__(self):
        """
        Iterator over the blocks.

        EXAMPLES::

            sage: sts = designs.steiner_triple_system(9)
            sage: list(sts)
            [[0, 1, 5], [0, 2, 4], [0, 3, 6], [0, 7, 8], [1, 2, 3], [1, 4, 7],
            [1, 6, 8], [2, 5, 8], [2, 6, 7], [3, 4, 8], [3, 5, 7], [4, 5, 6]]

            sage: b = IncidenceStructure('ab', ['a','ab'])
            sage: it = iter(b)
            sage: next(it)
            ['a']
            sage: next(it)
            ['a', 'b']
        """
    def __eq__(self, other):
        """
        Test whether the two incidence structures are equal.

        TESTS::

            sage: blocks = [[0,1,2],[0,3,4],[0,5,6],[1,3,5],[1,4,6],[2,3,6],[2,4,5]]
            sage: BD1 = IncidenceStructure(7, blocks)
            sage: M = BD1.incidence_matrix()                                            # needs sage.modules
            sage: BD2 = IncidenceStructure(incidence_matrix=M)                          # needs sage.modules
            sage: BD1 == BD2                                                            # needs sage.modules
            True

            sage: e1 = frozenset([0,1])
            sage: e2 = frozenset([2])
            sage: sorted([e1,e2]) == [e1,e2]
            True
            sage: sorted([e2,e1]) == [e2,e1]
            True
            sage: I1 = IncidenceStructure([e1,e2], [[e1],[e1,e2]])
            sage: I2 = IncidenceStructure([e1,e2], [[e2,e1],[e1]])
            sage: I3 = IncidenceStructure([e2,e1], [[e1,e2],[e1]])
            sage: I1 == I2 and I2 == I1 and I1 == I3 and I3 == I1 and I2 == I3 and I3 == I2
            True
        """
    def __ne__(self, other):
        """
        Difference test.

        EXAMPLES::

            sage: BD1 = IncidenceStructure(7, [[0,1,2],[0,3,4],[0,5,6],[1,3,5],[1,4,6],[2,3,6],[2,4,5]])
            sage: M = BD1.incidence_matrix()                                            # needs sage.modules
            sage: BD2 = IncidenceStructure(incidence_matrix=M)                          # needs sage.modules
            sage: BD1 != BD2                                                            # needs sage.modules
            False
        """
    def __contains__(self, block) -> bool:
        '''
        Test if a block belongs to the incidence structure.

        INPUT:

        - ``block`` -- a block

        EXAMPLES::

            sage: [1,2,3,4] in IncidenceStructure([[1,2,3,4]])
            True
            sage: [1,2,4,3] in IncidenceStructure([[1,2,3,4]])
            True
            sage: [1,2,"3",4] in IncidenceStructure([[1,2,3,4]])
            False
            sage: [1,2,"3",4] in IncidenceStructure([[1,2,"3",4]])
            True

        More complicated examples::

            sage: str="I had a dream of a time when a 3-lines patch does not kill one hour"
            sage: sets = Subsets(str.split(), 4)
            sage: IS = IncidenceStructure(sets)  # a complete 4-uniform hypergraph
            sage: ["I", "dream", "of", "one"] in IS
            True
            sage: ["does", "patch", "kill", "dream"] in IS
            True
            sage: ["Am", "I", "finally", "done ?"] in IS
            False
            sage: IS = designs.ProjectiveGeometryDesign(3, 1, GF(2),                    # needs sage.combinat
            ....:                                       point_coordinates=False)
            sage: [3,8,7] in IS                                                         # needs sage.combinat
            True
            sage: [3,8,9] in IS                                                         # needs sage.combinat
            False
        '''
    def canonical_label(self):
        """
        Return a canonical label for the incidence structure.

        A canonical label is relabeling of the points into integers
        `\\{0,...,n-1\\}` such that isomorphic incidence structures are
        relabelled to equal objects.

        EXAMPLES::

            sage: # needs sage.schemes
            sage: fano1 = designs.balanced_incomplete_block_design(7,3)
            sage: fano2 = designs.projective_plane(2)
            sage: fano1 == fano2
            False
            sage: fano1.relabel(fano1.canonical_label())
            sage: fano2.relabel(fano2.canonical_label())
            sage: fano1 == fano2
            True
        """
    def is_isomorphic(self, other, certificate: bool = False):
        '''
        Return whether the two incidence structures are isomorphic.

        INPUT:

        - ``other`` -- an incidence structure

        - ``certificate`` -- boolean (default: ``False``); whether to return an
          isomorphism from ``self`` to ``other`` instead of a boolean answer

        EXAMPLES::

            sage: # needs sage.schemes
            sage: fano1 = designs.balanced_incomplete_block_design(7,3)
            sage: fano2 = designs.projective_plane(2)
            sage: fano1.is_isomorphic(fano2)
            True
            sage: fano1.is_isomorphic(fano2,certificate=True)
            {0: 0, 1: 1, 2: 2, 3: 6, 4: 4, 5: 3, 6: 5}

        TESTS::

            sage: # needs sage.symbolic
            sage: IS  = IncidenceStructure([["A",5,pi],["A",5,"Wouhou"],
            ....:                           ["A","Wouhou",(9,9)],[pi,12]])
            sage: IS2 = IS.copy()
            sage: IS2.relabel(IS2.canonical_label())
            sage: IS.is_isomorphic(IS2)
            True
            sage: canon = IS.is_isomorphic(IS2, certificate=True)
            sage: IS.relabel(canon)
            sage: IS==IS2
            True

            sage: IS2 = IncidenceStructure([[1,2]])
            sage: IS2.is_isomorphic(IS)                                                 # needs sage.symbolic
            False
            sage: IS2.is_isomorphic(IS, certificate=True)                               # needs sage.symbolic
            {}

        Checking whether two :class:`IncidenceStructure` are isomorphic
        incidentally computes their canonical label (if necessary). Thus,
        subsequent calls to :meth:`is_isomorphic` will be faster::

            sage: # needs sage.schemes
            sage: IS1 = designs.projective_plane(3)
            sage: IS2 = IS1.relabel(Permutations(IS1.ground_set()).random_element(),
            ....:                   inplace=False)
            sage: IS2 = IncidenceStructure(IS2.blocks())
            sage: IS1._canonical_label is None and IS2._canonical_label is None
            True
            sage: IS1.is_isomorphic(IS2)
            True
            sage: IS1._canonical_label is None or IS2._canonical_label is None
            False
        '''
    def isomorphic_substructures_iterator(self, H2, induced: bool = False):
        """
        Iterate over all copies of ``H2`` contained in ``self``.

        A hypergraph `H_1` contains an isomorphic copy of a hypergraph `H_2` if
        there exists an injection `f:V(H_2)\\mapsto V(H_1)` such that for any set
        `S_2\\in E(H_2)` the set `S_1=f(S2)` belongs to `E(H_1)`.

        It is an *induced* copy if no other set of `E(H_1)` is contained in
        `f(V(H_2))`, i.e. `|E(H_2)|=\\{S:S\\in E(H_1)\\text{ and }f(V(H_2))\\}`.

        This function lists all such injections. In particular, the number of
        copies of `H` in itself is equal to *the size of its automorphism
        group*.

        See :mod:`~sage.combinat.designs.subhypergraph_search` for more information.

        INPUT:

        - ``H2`` -- an :class:`IncidenceStructure` object

        - ``induced`` -- boolean (default: ``False``); whether to require the copies to be
          induced

        EXAMPLES:

        How many distinct `C_5` in Petersen's graph ? ::

            sage: P = graphs.PetersenGraph()
            sage: C = graphs.CycleGraph(5)
            sage: IP = IncidenceStructure(P.edges(sort=True, labels=False))
            sage: IC = IncidenceStructure(C.edges(sort=True, labels=False))
            sage: sum(1 for _ in IP.isomorphic_substructures_iterator(IC))
            120

        As the automorphism group of `C_5` has size 10, the number of distinct
        unlabelled copies is 12. Let us check that all functions returned
        correspond to an actual `C_5` subgraph::

            sage: for f in IP.isomorphic_substructures_iterator(IC):
            ....:     assert all(P.has_edge(f[x],f[y]) for x,y in C.edges(sort=True, labels=False))

        The number of induced copies, in this case, is the same::

            sage: sum(1 for _ in IP.isomorphic_substructures_iterator(IC,induced=True))
            120

        They begin to differ if we make one vertex universal::

            sage: P.add_edges([(0,x) for x in P], loops=False)
            sage: IP = IncidenceStructure(P.edges(sort=True, labels=False))
            sage: IC = IncidenceStructure(C.edges(sort=True, labels=False))
            sage: sum(1 for _ in IP.isomorphic_substructures_iterator(IC))
            420
            sage: sum(1 for _ in IP.isomorphic_substructures_iterator(IC,induced=True))
            60

        The number of copies of `H` in itself is the size of its automorphism
        group::

            sage: H = designs.projective_plane(3)                                       # needs sage.schemes
            sage: sum(1 for _ in H.isomorphic_substructures_iterator(H))                # needs sage.schemes
            5616
            sage: H.automorphism_group().cardinality()                                  # needs sage.groups sage.schemes
            5616
        """
    def copy(self):
        '''
        Return a copy of the incidence structure.

        EXAMPLES::

            sage: IS = IncidenceStructure([[1,2,3,"e"]], name=\'Test\')
            sage: IS
            Incidence structure with 4 points and 1 blocks
            sage: copy(IS)
            Incidence structure with 4 points and 1 blocks
            sage: [1, 2, 3, \'e\'] in copy(IS)
            True
            sage: copy(IS)._name
            \'Test\'
        '''
    __copy__ = copy
    def induced_substructure(self, points):
        '''
        Return the substructure induced by a set of points.

        The substructure induced in `\\mathcal H` by a set `X\\subseteq V(\\mathcal
        H)` of points is the incidence structure `\\mathcal H_X` defined on `X`
        whose sets are all `S\\in \\mathcal H` such that `S\\subseteq X`.

        INPUT:

        - ``points`` -- set of points

        .. NOTE::

            This method goes over all sets of ``self`` before building a new
            :class:`IncidenceStructure` (which involves some relabelling and
            sorting). It probably should not be called in a performance-critical
            code.

        EXAMPLES:

        A Fano plane with one point removed::

            sage: F = designs.steiner_triple_system(7)
            sage: F.induced_substructure([0..5])
            Incidence structure with 6 points and 4 blocks

        TESTS::

            sage: F.induced_substructure([0..50])
            Traceback (most recent call last):
            ...
            ValueError: 7 is not a point of the incidence structure
            sage: F.relabel(dict(enumerate("abcdefg")))
            sage: F.induced_substructure("abc")
            Incidence structure with 3 points and ...
            sage: F.induced_substructure("Y")
            Traceback (most recent call last):
            ...
            ValueError: \'Y\' is not a point of the incidence structure
        '''
    def trace(self, points, min_size: int = 1, multiset: bool = True):
        '''
        Return the trace of a set of points.

        Given an hypergraph `\\mathcal H`, the *trace* of a set `X` of points in
        `\\mathcal H` is the hypergraph whose blocks are all non-empty `S \\cap X`
        where `S \\in \\mathcal H`.

        INPUT:

        - ``points`` -- set of points

        - ``min_size`` -- integer (default: 1); minimum size of the sets to
          keep. By default all empty sets are discarded, i.e. ``min_size=1``

        - ``multiset`` -- boolean (default: ``True``); whether to keep multiple
          copies of the same set

        .. NOTE::

            This method goes over all sets of ``self`` before building a new
            :class:`IncidenceStructure` (which involves some relabelling and
            sorting). It probably should not be called in a performance-critical
            code.

        EXAMPLES:

        A Baer subplane of order 2 (i.e. a Fano plane) in a projective plane of order 4::

            sage: # needs sage.schemes
            sage: P4 = designs.projective_plane(4)
            sage: F = designs.projective_plane(2)
            sage: for x in Subsets(P4.ground_set(),7):
            ....:     if P4.trace(x,min_size=2).is_isomorphic(F):
            ....:         break
            sage: subplane = P4.trace(x,min_size=2); subplane
            Incidence structure with 7 points and 7 blocks
            sage: subplane.is_isomorphic(F)
            True

        TESTS::

            sage: # needs sage.schemes
            sage: F.trace([0..50])
            Traceback (most recent call last):
            ...
            ValueError: 7 is not a point of the incidence structure
            sage: F.relabel(dict(enumerate("abcdefg")))
            sage: F.trace("abc")
            Incidence structure with 3 points and ...
            sage: F.trace("Y")
            Traceback (most recent call last):
            ...
            ValueError: \'Y\' is not a point of the incidence structure
        '''
    def ground_set(self):
        """
        Return the ground set (i.e the list of points).

        EXAMPLES::

            sage: IncidenceStructure(3, [[0,1],[0,2]]).ground_set()
            [0, 1, 2]
        """
    def num_points(self):
        """
        Return the size of the ground set.

        EXAMPLES::

            sage: designs.DesarguesianProjectivePlaneDesign(2).num_points()
            7
            sage: B = IncidenceStructure(4, [[0,1],[0,2],[0,3],[1,2], [1,2,3]])
            sage: B.num_points()
            4
        """
    def num_blocks(self):
        """
        Return the number of blocks.

        EXAMPLES::

            sage: designs.DesarguesianProjectivePlaneDesign(2).num_blocks()
            7
            sage: B = IncidenceStructure(4, [[0,1],[0,2],[0,3],[1,2], [1,2,3]])
            sage: B.num_blocks()
            5
        """
    def blocks(self):
        """
        Return the list of blocks.

        EXAMPLES::

            sage: BD = IncidenceStructure(7,[[0,1,2],[0,3,4],[0,5,6],[1,3,5],[1,4,6],[2,3,6],[2,4,5]])
            sage: BD.blocks()
            [[0, 1, 2], [0, 3, 4], [0, 5, 6], [1, 3, 5], [1, 4, 6], [2, 3, 6], [2, 4, 5]]
        """
    def block_sizes(self):
        """
        Return the set of block sizes.

        EXAMPLES::

            sage: BD = IncidenceStructure(8, [[0,1,3],[1,4,5,6],[1,2],[5,6,7]])
            sage: BD.block_sizes()
            [3, 2, 4, 3]
            sage: BD = IncidenceStructure(7,[[0,1,2],[0,3,4],[0,5,6],[1,3,5],[1,4,6],[2,3,6],[2,4,5]])
            sage: BD.block_sizes()
            [3, 3, 3, 3, 3, 3, 3]
        """
    def degree(self, p=None, subset: bool = False):
        """
        Return the degree of a point ``p`` (or a set of points).

        The degree of a point (or set of points) is the number of blocks that
        contain it.

        INPUT:

        - ``p`` -- a point (or a set of points) of the incidence structure

        - ``subset`` -- boolean (default: ``False``); whether to interpret the
          argument as a set of point or as a point (default)

        EXAMPLES::

            sage: designs.steiner_triple_system(9).degree(3)
            4
            sage: designs.steiner_triple_system(9).degree({1,2},subset=True)
            1

        TESTS::

            sage: designs.steiner_triple_system(9).degree(subset=True)
            Traceback (most recent call last):
            ...
            ValueError: subset must be False when p is None
        """
    def degrees(self, size=None):
        """
        Return the degree of all sets of given size, or the degree of all points.

        The degree of a point (or set of point) is the number of blocks that
        contain it.

        INPUT:

        - ``size`` -- integer; return the degree of all subsets of points of
          cardinality ``size``. When ``size=None``, the function outputs the
          degree of all points.

          .. NOTE::

              When ``size=None`` the output is indexed by the points. When
              ``size=1`` it is indexed by tuples of size 1. This is the same
              information, stored slightly differently.

        OUTPUT: a dictionary whose values are degrees and keys are either:

        - the points of the incidence structure if ``size=None`` (default)

        - the subsets of size ``size`` of the points stored as tuples

        EXAMPLES::

            sage: IncidenceStructure([[1,2,3],[1,4]]).degrees(2)
            {(1, 2): 1, (1, 3): 1, (1, 4): 1, (2, 3): 1, (2, 4): 0, (3, 4): 0}

        In a Steiner triple system, all pairs have degree 1::

            sage: S13 = designs.steiner_triple_system(13)
            sage: all(v == 1 for v in S13.degrees(2).values())
            True
        """
    def rank(self):
        """
        Return the rank of the hypergraph (the maximum size of a block).

        EXAMPLES::

            sage: h = Hypergraph(8, [[0,1,3],[1,4,5,6],[1,2]])
            sage: h.rank()
            4
        """
    def is_regular(self, r=None) -> bool | int:
        """
        Test whether the incidence structure is `r`-regular.

        An incidence structure is said to be `r`-regular if all its points are
        incident with exactly `r` blocks.

        INPUT:

        - ``r`` -- integer

        OUTPUT:

        If ``r`` is defined, a boolean is returned. If ``r`` is set to ``None``
        (default), the method returns either ``False`` or the integer ``r`` such
        that the incidence structure is `r`-regular.

        .. WARNING::

            In case of `0`-regular incidence structure, beware that ``if not
            H.is_regular()`` is a satisfied condition.

        EXAMPLES::

            sage: designs.balanced_incomplete_block_design(7,3).is_regular()            # needs sage.schemes
            3
            sage: designs.balanced_incomplete_block_design(7,3).is_regular(r=3)         # needs sage.schemes
            True
            sage: designs.balanced_incomplete_block_design(7,3).is_regular(r=4)         # needs sage.schemes
            False

        TESTS::

            sage: IncidenceStructure([]).is_regular()
            Traceback (most recent call last):
            ...
            ValueError: This incidence structure has no points.
        """
    def is_uniform(self, k=None) -> bool | int:
        """
        Test whether the incidence structure is `k`-uniform

        An incidence structure is said to be `k`-uniform if all its blocks have
        size `k`.

        INPUT:

        - ``k`` -- integer

        OUTPUT:

        If ``k`` is defined, a boolean is returned. If ``k`` is set to ``None``
        (default), the method returns either ``False`` or the integer ``k`` such
        that the incidence structure is `k`-uniform.

        .. WARNING::

            In case of `0`-uniform incidence structure, beware that ``if not
            H.is_uniform()`` is a satisfied condition.

        EXAMPLES::

            sage: designs.balanced_incomplete_block_design(7,3).is_uniform()            # needs sage.schemes
            3
            sage: designs.balanced_incomplete_block_design(7,3).is_uniform(k=3)         # needs sage.schemes
            True
            sage: designs.balanced_incomplete_block_design(7,3).is_uniform(k=4)         # needs sage.schemes
            False

        TESTS::

            sage: IncidenceStructure([]).is_uniform()
            Traceback (most recent call last):
            ...
            ValueError: This incidence structure has no blocks.
        """
    def is_connected(self) -> bool:
        """
        Test whether the design is connected.

        EXAMPLES::

            sage: IncidenceStructure(3, [[0,1],[0,2]]).is_connected()
            True
            sage: IncidenceStructure(4, [[0,1],[2,3]]).is_connected()
            False
        """
    def is_simple(self) -> bool:
        """
        Test whether this design is simple (i.e. no repeated block).

        EXAMPLES::

            sage: IncidenceStructure(3, [[0,1],[1,2],[0,2]]).is_simple()
            True
            sage: IncidenceStructure(3, [[0],[0]]).is_simple()
            False

            sage: V = [(0,'a'),(0,'b'),(1,'a'),(1,'b')]
            sage: B = [[V[0],V[1]], [V[1],V[2]]]
            sage: I = IncidenceStructure(V, B)
            sage: I.is_simple()
            True
            sage: I2 = IncidenceStructure(V, B*2)
            sage: I2.is_simple()
            False
        """
    def intersection_graph(self, sizes=None):
        """
        Return the intersection graph of the incidence structure.

        The vertices of this graph are the :meth:`blocks` of the incidence
        structure. Two of them are adjacent if the size of their intersection
        belongs to the set ``sizes``.

        INPUT:

        - ``sizes`` -- list/set of integers; for convenience, setting
          ``sizes`` to ``5`` has the same effect as ``sizes=[5]``. When set to
          ``None`` (default), behaves as ``sizes=PositiveIntegers()``.

        EXAMPLES:

        The intersection graph of a
        :func:`~sage.combinat.designs.bibd.balanced_incomplete_block_design` is
        a :meth:`strongly regular graph <Graph.is_strongly_regular>` (when it is
        not trivial)::

            sage: BIBD =  designs.balanced_incomplete_block_design(19,3)
            sage: G = BIBD.intersection_graph(1)
            sage: G.is_strongly_regular(parameters=True)
            (57, 24, 11, 9)
        """
    def incidence_matrix(self):
        """
        Return the incidence matrix `A` of the design. A is a `(v \\times b)`
        matrix defined by: ``A[i,j] = 1`` if ``i`` is in block ``B_j`` and 0
        otherwise.

        EXAMPLES::

            sage: BD = IncidenceStructure(7, [[0,1,2],[0,3,4],[0,5,6],[1,3,5],
            ....:                             [1,4,6],[2,3,6],[2,4,5]])
            sage: BD.block_sizes()
            [3, 3, 3, 3, 3, 3, 3]
            sage: BD.incidence_matrix()                                                 # needs sage.modules
            [1 1 1 0 0 0 0]
            [1 0 0 1 1 0 0]
            [1 0 0 0 0 1 1]
            [0 1 0 1 0 1 0]
            [0 1 0 0 1 0 1]
            [0 0 1 1 0 0 1]
            [0 0 1 0 1 1 0]

            sage: I = IncidenceStructure('abc', ('ab','abc','ac','c'))
            sage: I.incidence_matrix()                                                  # needs sage.modules
            [1 1 1 0]
            [1 1 0 0]
            [0 1 1 1]
        """
    def incidence_graph(self, labels: bool = False):
        """
        Return the incidence graph of the incidence structure.

        A point and a block are adjacent in this graph whenever they are
        incident.

        INPUT:

        - ``labels`` -- boolean; whether to return a graph whose vertices are
          integers, or labelled elements

          - ``labels is False`` -- default; in this case the first vertices
            of the graphs are the elements of :meth:`ground_set`, and appear
            in the same order. Similarly, the following vertices represent the
            elements of :meth:`blocks`, and appear in the same order.

          - ``labels is True``, the points keep their original labels, and the
            blocks are :func:`Set <Set>` objects.

            Note that the labelled incidence graph can be incorrect when
            blocks are repeated, and on some (rare) occasions when the
            elements of :meth:`ground_set` mix :func:`Set` and non-:func:`Set
            <Set>` objects.

        EXAMPLES::

            sage: BD = IncidenceStructure(7, [[0,1,2],[0,3,4],[0,5,6],[1,3,5],
            ....:                             [1,4,6],[2,3,6],[2,4,5]])
            sage: BD.incidence_graph()                                                  # needs sage.modules
            Bipartite graph on 14 vertices
            sage: A = BD.incidence_matrix()                                             # needs sage.modules
            sage: Graph(block_matrix([[A*0, A],                                         # needs sage.modules
            ....:                     [A.transpose(),A*0]])) == BD.incidence_graph()
            True

        TESTS:

        With ``labels = True``::

            sage: BD.incidence_graph(labels=True).has_edge(0,Set([0,1,2]))
            True
        """
    def is_berge_cyclic(self):
        '''
        Check whether ``self`` is a Berge-Cyclic uniform hypergraph.

        A `k`-uniform Berge cycle (named after Claude Berge) of length `\\ell`
        is a cyclic list of distinct `k`-sets `F_1,\\ldots,F_\\ell`, `\\ell>1`,
        and distinct vertices `C = \\{v_1,\\ldots,v_\\ell\\}` such that for each
        `1\\le i\\le \\ell`, `F_i` contains `v_i` and `v_{i+1}` (where `v_{l+1} =
        v_1`).

        A uniform hypergraph is Berge-cyclic if its incidence graph is cyclic.
        It is called "Berge-acyclic" otherwise.

        For more information, see [Fag1983]_ and :wikipedia:`Hypergraph`.

        EXAMPLES::

            sage: Hypergraph(5, [[1, 2, 3], [2, 3, 4]]).is_berge_cyclic()               # needs sage.modules
            True
            sage: Hypergraph(6, [[1, 2, 3], [3, 4, 5]]).is_berge_cyclic()               # needs sage.modules
            False

        TESTS::

            sage: Hypergraph(5, [[1, 2, 3], [2, 3]]).is_berge_cyclic()
            Traceback (most recent call last):
            ...
            TypeError: Berge cycles are defined for uniform hypergraphs only
        '''
    def complement(self, uniform: bool = False):
        '''
        Return the complement of the incidence structure.

        Two different definitions of "complement" are made available, according
        to the value of ``uniform``.

        INPUT:

        - ``uniform`` -- boolean

          - if set to ``False`` (default), returns the incidence structure whose
            blocks are the complements of all blocks of the incidence structure.

          - If set to ``True`` and the incidence structure is `k`-uniform,
            returns the incidence structure whose blocks are all `k`-sets of the
            ground set that do not appear in ``self``.

        EXAMPLES:

        The complement of a
        :class:`~sage.combinat.designs.bibd.BalancedIncompleteBlockDesign` is
        also a `2`-design::

            sage: bibd = designs.balanced_incomplete_block_design(13,4)                 # needs sage.schemes
            sage: bibd.is_t_design(return_parameters=True)                              # needs sage.schemes
            (True, (2, 13, 4, 1))
            sage: bibd.complement().is_t_design(return_parameters=True)                 # needs sage.schemes
            (True, (2, 13, 9, 6))

        The "uniform" complement of a graph is a graph::

            sage: g = graphs.PetersenGraph()
            sage: G = IncidenceStructure(g.edges(sort=True, labels=False))
            sage: H = G.complement(uniform=True)
            sage: h = Graph(H.blocks())
            sage: g == h
            False
            sage: g == h.complement()
            True

        TESTS::

            sage: bibd.relabel({i:str(i) for i in bibd.ground_set()})                   # needs sage.schemes
            sage: bibd.complement().ground_set()                                        # needs sage.schemes
            [\'0\', \'1\', \'2\', \'3\', \'4\', \'5\', \'6\', \'7\', \'8\', \'9\', \'10\', \'11\', \'12\']

            sage: I = IncidenceStructure(\'abc\', [\'ab\',\'ac\',\'bc\'])
            sage: I.is_t_design(return_parameters=True)
            (True, (2, 3, 2, 1))
        '''
    def relabel(self, perm=None, inplace: bool = True):
        """
        Relabel the ground set.

        INPUT:

        - ``perm`` -- can be one of

            - a dictionary -- then each point ``p`` (which should be a key of
              ``d``) is relabeled to ``d[p]``

            - a list or a tuple of length ``n`` -- the first point returned by
              :meth:`ground_set` is relabeled to ``l[0]``, the second to
              ``l[1]``, ...

            - ``None`` -- the incidence structure is relabeled to be on
              `\\{0,1,...,n-1\\}` in the ordering given by :meth:`ground_set`

        - ``inplace`` -- boolean (default: ``False``); if ``True`` then return
          a relabeled graph and does not touch ``self``

        EXAMPLES::

            sage: # needs sage.schemes
            sage: TD = designs.transversal_design(5,5)
            sage: TD.relabel({i: chr(97+i) for i in range(25)})
            sage: TD.ground_set()
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
            sage: TD.blocks()[:3]
            [['a', 'f', 'k', 'p', 'u'], ['a', 'g', 'm', 's', 'y'], ['a', 'h', 'o', 'q', 'x']]

        Relabel to integer points::

            sage: TD.relabel()                                                          # needs sage.schemes
            sage: TD.blocks()[:3]                                                       # needs sage.schemes
            [[0, 5, 10, 15, 20], [0, 6, 12, 18, 24], [0, 7, 14, 16, 23]]

        TESTS:

        Check that the relabel is consistent on a fixed incidence structure::

            sage: I = IncidenceStructure([0,1,2,3,4],
            ....:               [[0,1,3],[0,2,4],[2,3,4],[0,1]])
            sage: I.relabel()
            sage: from itertools import permutations
            sage: for p in permutations([0,1,2,3,4]):
            ....:     J = I.relabel(p,inplace=False)
            ....:     if I == J: print(p)
            (0, 1, 2, 3, 4)
            (0, 1, 4, 3, 2)

        And one can also verify that we have exactly two automorphisms::

            sage: I.automorphism_group()                                                # needs sage.groups
            Permutation Group with generators [(2,4)]
        """
    def packing(self, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        """
        Return a maximum packing.

        A maximum packing in a hypergraph is collection of disjoint sets/blocks
        of maximal cardinality. This problem is NP-complete in general, and in
        particular on 3-uniform hypergraphs. It is solved here with an Integer
        Linear Program.

        For more information, see the :wikipedia:`Packing_in_a_hypergraph`.

        INPUT:

        - ``solver`` -- (default: ``None``) specify a Mixed Integer Linear
          Programming (MILP) solver to be used. If set to ``None``, the default
          one is used. For more information on LP solvers and which default
          solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: 0); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``integrality_tolerance`` -- parameter for use with MILP solvers over
          an inexact base ring; see
          :meth:`MixedIntegerLinearProgram.get_values`.

        EXAMPLES::

            sage: P = IncidenceStructure([[1,2],[3,4],[2,3]]).packing()                 # needs sage.numerical.mip
            sage: sorted(sorted(b) for b in P)                                          # needs sage.numerical.mip
            [[1, 2], [3, 4]]
            sage: len(designs.steiner_triple_system(9).packing())                       # needs sage.numerical.mip
            3
        """
    def is_t_design(self, t=None, v=None, k=None, l=None, return_parameters: bool = False):
        """
        Test whether ``self`` is a `t-(v,k,l)` design.

        A `t-(v,k,\\lambda)` (sometimes called `t`-design for short) is a block
        design in which:

        - the underlying set has cardinality `v`
        - the blocks have size `k`
        - each `t`-subset of points is covered by `\\lambda` blocks

        INPUT:

        - ``t``, ``v``, ``k``, ``l`` -- integers; their value is set to
          ``None`` by default. The function tests whether the design is a
          `t-(v,k,l)` design using the provided values and guesses the
          others. Note that ``l`` cannot be specified if ``t`` is not.

        - ``return_parameters`` -- boolean; whether to return the parameters of
          the `t`-design. If set to ``True``, the function returns a pair
          ``(boolean_answer,(t,v,k,l))``.

        EXAMPLES::

            sage: fano_blocks = [[0,1,2],[0,3,4],[0,5,6],[1,3,5],[1,4,6],[2,3,6],[2,4,5]]
            sage: BD = IncidenceStructure(7, fano_blocks)
            sage: BD.is_t_design()
            True
            sage: BD.is_t_design(return_parameters=True)
            (True, (2, 7, 3, 1))
            sage: BD.is_t_design(2, 7, 3, 1)
            True
            sage: BD.is_t_design(1, 7, 3, 3)
            True
            sage: BD.is_t_design(0, 7, 3, 7)
            True

            sage: BD.is_t_design(0,6,3,7) or BD.is_t_design(0,7,4,7) or BD.is_t_design(0,7,3,8)
            False

            sage: BD = designs.AffineGeometryDesign(3, 1, GF(2))                        # needs sage.combinat
            sage: BD.is_t_design(1)                                                     # needs sage.combinat
            True
            sage: BD.is_t_design(2)                                                     # needs sage.combinat
            True

        Steiner triple and quadruple systems are other names for `2-(v,3,1)` and
        `3-(v,4,1)` designs::

            sage: S3_9 = designs.steiner_triple_system(9)
            sage: S3_9.is_t_design(2,9,3,1)
            True

            sage: blocks = designs.steiner_quadruple_system(8)
            sage: S4_8 = IncidenceStructure(8, blocks)
            sage: S4_8.is_t_design(3,8,4,1)
            True

            sage: blocks = designs.steiner_quadruple_system(14)
            sage: S4_14 = IncidenceStructure(14, blocks)
            sage: S4_14.is_t_design(3,14,4,1)
            True

        Some examples of Witt designs that need the gap database::

            sage: # optional - gap_package_design
            sage: BD = designs.WittDesign(9)
            sage: BD.is_t_design(2,9,3,1)
            True
            sage: W12 = designs.WittDesign(12)
            sage: W12.is_t_design(5,12,6,1)
            True
            sage: W12.is_t_design(4)
            True

        Further examples::

            sage: D = IncidenceStructure(4,[[],[]])
            sage: D.is_t_design(return_parameters=True)
            (True,  (0, 4, 0, 2))

            sage: D = IncidenceStructure(4, [[0,1],[0,2],[0,3]])
            sage: D.is_t_design(return_parameters=True)
            (True, (0, 4, 2, 3))

            sage: D = IncidenceStructure(4, [[0],[1],[2],[3]])
            sage: D.is_t_design(return_parameters=True)
            (True, (1, 4, 1, 1))

            sage: D = IncidenceStructure(4,[[0,1],[2,3]])
            sage: D.is_t_design(return_parameters=True)
            (True, (1, 4, 2, 1))

            sage: D = IncidenceStructure(4, [list(range(4))])
            sage: D.is_t_design(return_parameters=True)
            (True, (4, 4, 4, 1))

        TESTS::

            sage: blocks = designs.steiner_quadruple_system(8)
            sage: S4_8 = IncidenceStructure(8, blocks)
            sage: R = list(range(15))
            sage: [(v,k,l) for v in R for k in R for l in R if S4_8.is_t_design(3,v,k,l)]
            [(8, 4, 1)]
            sage: [(v,k,l) for v in R for k in R for l in R if S4_8.is_t_design(2,v,k,l)]
            [(8, 4, 3)]
            sage: [(v,k,l) for v in R for k in R for l in R if S4_8.is_t_design(1,v,k,l)]
            [(8, 4, 7)]
            sage: [(v,k,l) for v in R for k in R for l in R if S4_8.is_t_design(0,v,k,l)]
            [(8, 4, 14)]

            sage: # needs sage.rings.finite_rings
            sage: A = designs.AffineGeometryDesign(3, 1, GF(2))
            sage: A.is_t_design(return_parameters=True)
            (True, (2, 8, 2, 1))
            sage: A = designs.AffineGeometryDesign(4, 2, GF(2))
            sage: A.is_t_design(return_parameters=True)
            (True, (3, 16, 4, 1))

            sage: I = IncidenceStructure(2, [])
            sage: I.is_t_design(return_parameters=True)
            (True, (0, 2, 0, 0))
            sage: I = IncidenceStructure(2, [[0],[0,1]])
            sage: I.is_t_design(return_parameters=True)
            (False, (0, 0, 0, 0))

        Verify that :issue:`38454` is fixed::

            sage: I = IncidenceStructure(points=[0,1,2,3,4,5],
            ....:                        blocks=[[0,1], [1,2], [0,2]])
            sage: I.is_t_design(return_parameters=True)
            (True, (0, 6, 2, 3))
        """
    def is_generalized_quadrangle(self, verbose: bool = False, parameters: bool = False):
        """
        Test if the incidence structure is a generalized quadrangle.

        An incidence structure is a generalized quadrangle iff (see [BH2012]_,
        section 9.6):

        - two blocks intersect on at most one point.

        - For every point `p` not in a block `B`, there is a unique block `B'`
          intersecting both `\\{p\\}` and `B`

        It is a *regular* generalized quadrangle if furthermore:

        - it is `s+1`-:meth:`uniform <is_uniform>` for some positive integer `s`.

        - it is `t+1`-:meth:`regular <is_regular>` for some positive integer `t`.

        For more information, see the :wikipedia:`Generalized_quadrangle`.

        .. NOTE::

            Some references (e.g. [PT2009]_ or
            :wikipedia:`Generalized_quadrangle`) only allow *regular*
            generalized quadrangles. To use such a definition, see the
            ``parameters`` optional argument described below, or the methods
            :meth:`is_regular` and :meth:`is_uniform`.

        INPUT:

        - ``verbose`` -- boolean; whether to print an explanation when the
          instance is not a generalized quadrangle

        - ``parameters`` -- (boolean; ``False``); if set to ``True``, the
          function returns a pair ``(s,t)`` instead of ``True`` answers. In this
          case, `s` and `t` are the integers defined above if they exist (each
          can be set to ``False`` otherwise).

        EXAMPLES::

            sage: h = designs.CremonaRichmondConfiguration()                            # needs networkx
            sage: h.is_generalized_quadrangle()                                         # needs networkx
            True

        This is actually a *regular* generalized quadrangle::

            sage: h.is_generalized_quadrangle(parameters=True)                          # needs networkx
            (2, 2)

        TESTS::

            sage: H = IncidenceStructure((2*graphs.CompleteGraph(3)).edges(sort=True, labels=False))
            sage: H.is_generalized_quadrangle(verbose=True)                             # needs sage.modules
            Some point is at distance >3 from some block.
            False

            sage: G = graphs.CycleGraph(5)
            sage: B = list(G.subgraph_search_iterator(graphs.PathGraph(3),              # needs sage.modules
            ....:                                     return_graphs=False))
            sage: H = IncidenceStructure(B)                                             # needs sage.modules
            sage: H.is_generalized_quadrangle(verbose=True)                             # needs sage.modules
            Two blocks intersect on >1 points.
            False

            sage: hypergraphs.CompleteUniform(4,2).is_generalized_quadrangle(verbose=1)             # needs sage.modules
            Some point has two projections on some line.
            False
        """
    def dual(self, algorithm=None):
        """
        Return the dual of the incidence structure.

        INPUT:

        - ``algorithm`` -- whether to use Sage's implementation
          (``algorithm=None``, default) or use GAP's (``algorithm='gap'``)

          .. NOTE::

              The ``algorithm='gap'`` option requires GAP's Design package
              (included in the ``gap_packages`` Sage spkg).

        EXAMPLES:

        The dual of a projective plane is a projective plane::

            sage: PP = designs.DesarguesianProjectivePlaneDesign(4)                     # needs sage.rings.finite_rings
            sage: PP.dual().is_t_design(return_parameters=True)                         # needs sage.modules sage.rings.finite_rings
            (True, (2, 21, 5, 1))

        TESTS::

            sage: D = IncidenceStructure(4, [[0,2],[1,2,3],[2,3]]); D
            Incidence structure with 4 points and 3 blocks
            sage: D.dual()                                                              # needs sage.modules
            Incidence structure with 3 points and 4 blocks
            sage: print(D.dual(algorithm='gap'))            # optional - gap_package_design
            Incidence structure with 3 points and 4 blocks
            sage: blocks = [[0,1,2],[0,3,4],[0,5,6],[1,3,5],[1,4,6],[2,3,6],[2,4,5]]
            sage: BD = IncidenceStructure(7, blocks, name='FanoPlane'); BD
            Incidence structure with 7 points and 7 blocks
            sage: print(BD.dual(algorithm='gap'))           # optional - gap_package_design
            Incidence structure with 7 points and 7 blocks
            sage: BD.dual()                                                             # needs sage.modules
            Incidence structure with 7 points and 7 blocks

        REFERENCE:

        - Leonard Soicher, :gap_package:`Design package manual <design/htm/CHAP003.htm>`
        """
    def automorphism_group(self):
        """
        Return the subgroup of the automorphism group of the incidence graph
        which respects the P B partition. It is (isomorphic to) the automorphism
        group of the block design, although the degrees differ.

        EXAMPLES::

            sage: # needs sage.groups sage.rings.finite_rings
            sage: P = designs.DesarguesianProjectivePlaneDesign(2); P
            (7,3,1)-Balanced Incomplete Block Design
            sage: G = P.automorphism_group()
            sage: G.is_isomorphic(PGL(3,2))
            True
            sage: G
            Permutation Group with generators [...]
            sage: G.cardinality()
            168

        A non self-dual example::

            sage: IS = IncidenceStructure(list(range(4)), [[0,1,2,3],[1,2,3]])
            sage: IS.automorphism_group().cardinality()                                 # needs sage.groups
            6
            sage: IS.dual().automorphism_group().cardinality()                          # needs sage.groups sage.modules
            1

        Examples with non-integer points::

            sage: I = IncidenceStructure('abc', ('ab','ac','bc'))
            sage: I.automorphism_group()                                                # needs sage.groups
            Permutation Group with generators [('b','c'), ('a','b')]
            sage: IncidenceStructure([[(1,2),(3,4)]]).automorphism_group()              # needs sage.groups
            Permutation Group with generators [((1,2),(3,4))]
        """
    def is_resolvable(self, certificate: bool = False, solver=None, verbose: int = 0, check: bool = True, *, integrality_tolerance: float = 0.001):
        """
        Test whether the hypergraph is resolvable.

        A hypergraph is said to be resolvable if its sets can be partitionned
        into classes, each of which is a partition of the ground set.

        .. NOTE::

            This problem is solved using an Integer Linear Program, and GLPK
            (the default LP solver) has been reported to be very slow on some
            instances. If you hit this wall, consider installing a more powerful
            MILP solver (CPLEX, Gurobi, ...).

        INPUT:

        - ``certificate`` -- boolean; whether to return the classes along with
          the binary answer (see examples below)

        - ``solver`` -- (default: ``None``) specify a Mixed Integer Linear
          Programming (MILP) solver to be used. If set to ``None``, the default
          one is used. For more information on MILP solvers and which default
          solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- integer (default: 0); sets the level of
          verbosity. Set to 0 by default, which means quiet.

        - ``check`` -- boolean (default: ``True``); whether to check that
          output is correct before returning it. As this is expected to be
          useless, you may want to disable it whenever you want speed.

        - ``integrality_tolerance`` -- parameter for use with MILP solvers over
          an inexact base ring; see :meth:`MixedIntegerLinearProgram.get_values`

        EXAMPLES:

        Some resolvable designs::

            sage: TD = designs.transversal_design(2,2,resolvable=True)
            sage: TD.is_resolvable()
            True

            sage: AG = designs.AffineGeometryDesign(3,1,GF(2))                          # needs sage.combinat
            sage: AG.is_resolvable()                                                    # needs sage.combinat
            True

        Their classes::

            sage: b, cls = TD.is_resolvable(True)
            sage: b
            True
            sage: cls # random
            [[[0, 3], [1, 2]], [[1, 3], [0, 2]]]

            sage: # needs sage.combinat
            sage: b, cls = AG.is_resolvable(True)
            sage: b
            True
            sage: cls  # random
            [[[6, 7], [4, 5], [0, 1], [2, 3]],
             [[5, 7], [0, 4], [3, 6], [1, 2]],
             [[0, 2], [4, 7], [1, 3], [5, 6]],
             [[3, 4], [0, 7], [1, 5], [2, 6]],
             [[3, 7], [1, 6], [0, 5], [2, 4]],
             [[0, 6], [2, 7], [1, 4], [3, 5]],
             [[4, 6], [0, 3], [2, 5], [1, 7]]]

        A non-resolvable design::

            sage: Fano = designs.balanced_incomplete_block_design(7,3)                  # needs sage.schemes
            sage: Fano.is_resolvable()                                                  # needs sage.schemes
            False
            sage: Fano.is_resolvable(True)                                              # needs sage.schemes
            (False, [])

        TESTS::

            sage: # needs sage.combinat
            sage: _, cls1 = AG.is_resolvable(certificate=True)
            sage: _, cls2 = AG.is_resolvable(certificate=True)
            sage: cls1 is cls2
            False
        """
    def coloring(self, k=None, solver=None, verbose: int = 0, *, integrality_tolerance: float = 0.001):
        """
        Compute a (weak) `k`-coloring of the hypergraph.

        A weak coloring of a hypergraph `\\mathcal H` is an assignment of colors
        to its vertices such that no set is monochromatic.

        INPUT:

        - ``k`` -- integer; compute a coloring with `k` colors if an integer is
          provided, otherwise returns an optimal coloring (i.e. with the minimum
          possible number of colors).

        - ``solver`` -- (default: ``None``) specify a Mixed Integer Linear
          Programming (MILP) solver to be used. If set to ``None``, the default
          one is used. For more information on MILP solvers and which default
          solver is used, see the method :meth:`solve
          <sage.numerical.mip.MixedIntegerLinearProgram.solve>` of the class
          :class:`MixedIntegerLinearProgram
          <sage.numerical.mip.MixedIntegerLinearProgram>`.

        - ``verbose`` -- nonnegative integer (default: `0`); set the level
          of verbosity you want from the linear program solver. Since the
          problem is `NP`-complete, its solving may take some time depending on
          the graph. A value of `0` means that there will be no message printed by
          the solver.

        - ``integrality_tolerance`` -- parameter for use with MILP solvers over
          an inexact base ring; see :meth:`MixedIntegerLinearProgram.get_values`

        EXAMPLES:

        The Fano plane has chromatic number 3::

            sage: len(designs.steiner_triple_system(7).coloring())                      # needs sage.numerical.mip
            3

        One admissible 3-coloring::

            sage: designs.steiner_triple_system(7).coloring()   # not tested            # needs sage.numerical.mip
            [[0, 2, 5, 1], [4, 3], [6]]

        The chromatic number of a graph is equal to the chromatic number of its
        2-uniform corresponding hypergraph::

            sage: g = graphs.PetersenGraph()
            sage: H = IncidenceStructure(g.edges(sort=True, labels=False))
            sage: len(g.coloring())
            3
            sage: len(H.coloring())                                                     # needs sage.numerical.mip
            3
        """
    def edge_coloring(self) -> list:
        """
        Compute a proper edge-coloring.

        A proper edge-coloring is an assignment of colors to the sets of the
        incidence structure such that two sets with non-empty intersection
        receive different colors. The coloring returned minimizes the number of
        colors.

        OUTPUT: a partition of the sets into color classes

        EXAMPLES::

            sage: H = Hypergraph([{1,2,3},{2,3,4},{3,4,5},{4,5,6}]); H
            Incidence structure with 6 points and 4 blocks
            sage: C = H.edge_coloring()
            sage: C # random
            [[[3, 4, 5]], [[2, 3, 4]], [[4, 5, 6], [1, 2, 3]]]
            sage: Set(map(Set,sum(C,[]))) == Set(map(Set,H.blocks()))
            True
        """
    def is_spread(self, spread) -> bool:
        """
        Check whether the input is a spread for ``self``.

        A spread of an incidence structure `(P, B)` is a subset of `B` which
        forms a partition of `P`.

        INPUT:

        - ``spread`` -- iterable; defines the spread

        EXAMPLES::

            sage: E = IncidenceStructure([[1, 2, 3], [4, 5, 6], [1, 5, 6]])
            sage: E.is_spread([[1, 2, 3], [4, 5, 6]])
            True
            sage: E.is_spread([1, 2, 3, 4, 5, 6])
            Traceback (most recent call last):
            ...
            TypeError: 'sage.rings.integer.Integer' object is not iterable
            sage: E.is_spread([[1, 2, 3, 4], [5, 6]])
            False

        Order of blocks or of points within each block doesn't matter::

            sage: E = IncidenceStructure([[1, 2, 3], [4, 5, 6], [1, 5, 6]])
            sage: E.is_spread([[5, 6, 4], [3, 1, 2]])
            True

        TESTS::

            sage: E = IncidenceStructure([])
            sage: E.is_spread([])
            True
            sage: E = IncidenceStructure([[1]])
            sage: E.is_spread([])
            False
            sage: E.is_spread([[1]])
            True
            sage: E = IncidenceStructure([[1], [1]])
            sage: E.is_spread([[1]])
            True
        """

__doc__: Incomplete
