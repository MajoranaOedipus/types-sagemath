from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import factorial as factorial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.combinat.combinat import bell_number as bell_number
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.partition import Partition as Partition, Partitions as Partitions
from sage.combinat.permutation import Permutation as Permutation
from sage.combinat.set_partition_iterator import set_partition_iterator as set_partition_iterator, set_partition_iterator_blocks as set_partition_iterator_blocks
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.prandom import randint as randint, random as random, sample as sample
from sage.rings.infinity import infinity as infinity
from sage.rings.integer import Integer as Integer
from sage.sets.disjoint_set import DisjointSet as DisjointSet
from sage.sets.set import Set as Set, Set_generic as Set_generic
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class AbstractSetPartition(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    """
    Methods of set partitions which are independent of the base set
    """
    def __hash__(self):
        """
        Return the hash of ``self``.

        The parent is not included as part of the hash.

        EXAMPLES::

            sage: P = SetPartitions(4)
            sage: A = SetPartition([[1], [2,3], [4]])
            sage: B = P([[1], [2,3], [4]])
            sage: hash(A) == hash(B)
            True
        """
    def __eq__(self, y):
        """
        Check equality of ``self`` and ``y``.

        The parent is not included as part of the equality check.

        EXAMPLES::

            sage: P = SetPartitions(4)
            sage: A = SetPartition([[1], [2,3], [4]])
            sage: B = P([[1], [2,3], [4]])
            sage: A == B
            True
            sage: C = P([[2, 3], [1], [4]])
            sage: A == C
            True
            sage: D = P([[1], [2, 4], [3]])
            sage: A == D
            False

        Note that this may give incorrect answers if the base set is not totally ordered::

            sage: a,b = frozenset([0,1]), frozenset([2,3])
            sage: p1 = SetPartition([[a], [b]])
            sage: p2 = SetPartition([[b], [a]])
            sage: p1 == p2
            False
        """
    def __ne__(self, y):
        """
        Check lack of equality of ``self`` and ``y``.

        The parent is not included as part of the equality check.

        EXAMPLES::

            sage: P = SetPartitions(4)
            sage: A = SetPartition([[1], [2,3], [4]])
            sage: B = P([[1], [2,3], [4]])
            sage: A != B
            False
            sage: C = P([[2, 3], [1], [4]])
            sage: A != C
            False
            sage: D = P([[1], [2, 4], [3]])
            sage: A != D
            True

        Note that this may give incorrect answers if the base set is not totally ordered::

            sage: a,b = frozenset([0,1]), frozenset([2,3])
            sage: p1 = SetPartition([[a], [b]])
            sage: p2 = SetPartition([[b], [a]])
            sage: p1 != p2
            True
        """
    def __lt__(self, y):
        """
        Check that ``self`` is less than ``y``.

        The ordering used is lexicographic, where:

        - a set partition is considered as the list of its parts
          sorted by increasing smallest element;

        - each part is regarded as a list of its elements, sorted
          in increasing order;

        - the parts themselves are compared lexicographically.

        EXAMPLES::

            sage: P = SetPartitions(4)
            sage: A = P([[1], [2,3], [4]])
            sage: B = SetPartition([[1,2,3], [4]])
            sage: A < B
            True
            sage: C = P([[1,2,4], [3]])
            sage: B < C
            True
            sage: B < B
            False
            sage: D = P([[1,4], [2], [3]])
            sage: E = P([[1,4], [2,3]])
            sage: D < E
            True
            sage: F = P([[1,2,4], [3]])
            sage: E < C
            False
            sage: A < E
            True
            sage: A < C
            True
        """
    def __gt__(self, y):
        """
        Check that ``self`` is greater than ``y``.

        The ordering used is lexicographic, where:

        - a set partition is considered as the list of its parts
          sorted by increasing smallest element;

        - each part is regarded as a list of its elements, sorted
          in increasing order;

        - the parts themselves are compared lexicographically.

        EXAMPLES::

            sage: P = SetPartitions(4)
            sage: A = P([[1], [2,3], [4]])
            sage: B = SetPartition([[1,2,3], [4]])
            sage: B > A
            True
            sage: A > B
            False
        """
    def __le__(self, y):
        """
        Check that ``self`` is less than or equals ``y``.

        The ordering used is lexicographic, where:

        - a set partition is considered as the list of its parts
          sorted by increasing smallest element;

        - each part is regarded as a list of its elements, sorted
          in increasing order;

        - the parts themselves are compared lexicographically.

        EXAMPLES::

            sage: P = SetPartitions(4)
            sage: A = P([[1], [2,3], [4]])
            sage: B = SetPartition([[1,2,3], [4]])
            sage: A <= B
            True
            sage: A <= A
            True
        """
    def __ge__(self, y):
        """
        Check that ``self`` is greater than or equals ``y``.

        The ordering used is lexicographic, where:

        - a set partition is considered as the list of its parts
          sorted by increasing smallest element;

        - each part is regarded as a list of its elements, sorted
          in increasing order;

        - the parts themselves are compared lexicographically.

        EXAMPLES::

            sage: P = SetPartitions(4)
            sage: A = P([[1], [2,3], [4]])
            sage: B = SetPartition([[1,2,3], [4]])
            sage: B >= A
            True
            sage: B >= B
            True
        """
    def __mul__(self, other):
        """
        The product of the set partitions ``self`` and ``other``.

        The product of two set partitions `B` and `C` is defined as the
        set partition whose parts are the nonempty intersections between
        each part of `B` and each part of `C`. This product is also
        the infimum of `B` and `C` in the classical set partition
        lattice (that is, the coarsest set partition which is finer than
        each of `B` and `C`). Consequently, ``inf`` acts as an alias for
        this method.

        .. SEEALSO::

            :meth:`sup`

        EXAMPLES::

            sage: x = SetPartition([ [1,2], [3,5,4] ])
            sage: y = SetPartition(( (3,1,2), (5,4) ))
            sage: x * y
            {{1, 2}, {3}, {4, 5}}

            sage: S = SetPartitions(4)
            sage: sp1 = S([[2,3,4], [1]])
            sage: sp2 = S([[1,3], [2,4]])
            sage: s = S([[2,4], [3], [1]])
            sage: sp1.inf(sp2) == s
            True

        TESTS:

        Here is a different implementation of the ``__mul__`` method
        (one that was formerly used for the ``inf`` method, before it
        was realized that the methods do the same thing)::

            sage: def mul2(s, t):
            ....:     temp = [ss.intersection(ts) for ss in s for ts in t]
            ....:     temp = filter(bool, temp)
            ....:     return s.__class__(s.parent(), temp)

        Let us check that this gives the same as ``__mul__`` on set
        partitions of `\\{1, 2, 3, 4\\}`::

            sage: all( all( mul2(s, t) == s * t for s in SetPartitions(4) )
            ....:      for t in SetPartitions(4) )
            True
        """
    inf = __mul__
    def sup(self, t):
        """
        Return the supremum of ``self`` and ``t`` in the classical set
        partition lattice.

        The supremum of two set partitions `B` and `C` is obtained as the
        transitive closure of the relation which relates `i` to `j` if
        and only if `i` and `j` are in the same part in at least
        one of the set partitions `B` and `C`.

        .. SEEALSO::

            :meth:`__mul__`

        EXAMPLES::

            sage: S = SetPartitions(4)
            sage: sp1 = S([[2,3,4], [1]])
            sage: sp2 = S([[1,3], [2,4]])
            sage: s = S([[1,2,3,4]])
            sage: sp1.sup(sp2) == s
            True
        """
    def standard_form(self):
        """
        Return ``self`` as a list of lists.

        When the ground set is totally ordered, the elements of each
        block are listed in increasing order.

        This is not related to standard set partitions (which simply
        means set partitions of `[n] = \\{ 1, 2, \\ldots , n \\}` for some
        integer `n`) or standardization (:meth:`standardization`).

        EXAMPLES::

            sage: [x.standard_form() for x in SetPartitions(4, [2,2])]                  # needs sage.graphs sage.rings.finite_rings
            [[[1, 2], [3, 4]], [[1, 4], [2, 3]], [[1, 3], [2, 4]]]

        TESTS::

            sage: SetPartition([(1, 9, 8), (2, 3, 4, 5, 6, 7)]).standard_form()
            [[1, 8, 9], [2, 3, 4, 5, 6, 7]]
        """
    def base_set(self):
        """
        Return the base set of ``self``, which is the union of all parts
        of ``self``.

        EXAMPLES::

            sage: SetPartition([[1], [2,3], [4]]).base_set()
            {1, 2, 3, 4}
            sage: SetPartition([[1,2,3,4]]).base_set()
            {1, 2, 3, 4}
            sage: SetPartition([]).base_set()
            {}
        """
    def base_set_cardinality(self):
        """
        Return the cardinality of the base set of ``self``, which is the sum
        of the sizes of the parts of ``self``.

        This is also known as the *size* (sometimes the *weight*) of
        a set partition.

        EXAMPLES::

            sage: SetPartition([[1], [2,3], [4]]).base_set_cardinality()
            4
            sage: SetPartition([[1,2,3,4]]).base_set_cardinality()
            4
        """
    def coarsenings(self):
        """
        Return a list of coarsenings of ``self``.

        .. SEEALSO::

            :meth:`refinements`

        EXAMPLES::

            sage: SetPartition([[1,3],[2,4]]).coarsenings()
            [{{1, 2, 3, 4}}, {{1, 3}, {2, 4}}]
            sage: SetPartition([[1],[2,4],[3]]).coarsenings()
            [{{1, 2, 3, 4}},
             {{1, 2, 4}, {3}},
             {{1, 3}, {2, 4}},
             {{1}, {2, 3, 4}},
             {{1}, {2, 4}, {3}}]
            sage: SetPartition([]).coarsenings()
            [{}]
        """
    def max_block_size(self):
        """
        The maximum block size of the diagram.

        EXAMPLES::

            sage: # needs sage.modules
            sage: from sage.combinat.diagram_algebras import PartitionDiagram, PartitionDiagrams
            sage: pd = PartitionDiagram([[1,-3,-5],[2,4],[3,-1,-2],[5],[-4]])
            sage: pd.max_block_size()
            3
            sage: sorted(d.max_block_size() for d in PartitionDiagrams(2))
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4]
            sage: sorted(sp.max_block_size() for sp in SetPartitions(3))
            [1, 2, 2, 2, 3]
        """
    def conjugate(self):
        """
        An involution exchanging singletons and circular adjacencies.

        This method implements the definition of the conjugate of
        a set partition defined in [Cal2005]_.

        INPUT:

        - ``self`` -- set partition of an ordered set

        OUTPUT: a set partition

        EXAMPLES::

            sage: SetPartition([[1,6,7],[2,8],[3,4,5]]).conjugate()
            {{1, 4, 7}, {2, 8}, {3}, {5}, {6}}
            sage: all(sp.conjugate().conjugate()==sp for sp in SetPartitions([1,3,5,7]))
            True
            sage: SetPartition([]).conjugate()
            {}
        """

class SetPartition(AbstractSetPartition, metaclass=InheritComparisonClasscallMetaclass):
    """
    A partition of a set.

    A set partition `p` of a set `S` is a partition of `S` into subsets
    called parts and represented as a set of sets. By extension, a set
    partition of a nonnegative integer `n` is the set partition of the
    integers from 1 to `n`. The number of set partitions of `n` is called
    the `n`-th Bell number.

    There is a natural integer partition associated with a set partition,
    namely the nonincreasing sequence of sizes of all its parts.

    There is a classical lattice associated with all set partitions of
    `n`. The infimum of two set partitions is the set partition obtained
    by intersecting all the parts of both set partitions. The supremum
    is obtained by transitive closure of the relation `i` related to `j`
    if and only if they are in the same part in at least one of the set
    partitions.

    We will use terminology from partitions, in particular the *length* of
    a set partition `A = \\{A_1, \\ldots, A_k\\}` is the number of parts of `A`
    and is denoted by `|A| := k`. The *size* of `A` is the cardinality of `S`.
    We will also sometimes use the notation `[n] := \\{1, 2, \\ldots, n\\}`.

    EXAMPLES:

    There are 5 set partitions of the set `\\{1,2,3\\}`::

        sage: SetPartitions(3).cardinality()                                            # needs sage.libs.flint
        5

    Here is the list of them::

        sage: SetPartitions(3).list()                                                   # needs sage.graphs
        [{{1, 2, 3}}, {{1, 2}, {3}}, {{1, 3}, {2}}, {{1}, {2, 3}}, {{1}, {2}, {3}}]

    There are 6 set partitions of `\\{1,2,3,4\\}` whose underlying partition is
    `[2, 1, 1]`::

        sage: SetPartitions(4, [2,1,1]).list()                                          # needs sage.graphs sage.rings.finite_rings
        [{{1}, {2, 4}, {3}},
         {{1}, {2}, {3, 4}},
         {{1, 4}, {2}, {3}},
         {{1, 3}, {2}, {4}},
         {{1, 2}, {3}, {4}},
         {{1}, {2, 3}, {4}}]

    Since :issue:`14140`, we can create a set partition directly by
    :class:`SetPartition`, which creates the base set by taking the
    union of the parts passed in::

        sage: s = SetPartition([[1,3],[2,4]]); s
        {{1, 3}, {2, 4}}
        sage: s.parent()
        Set partitions
    """
    @staticmethod
    def __classcall_private__(cls, parts, check: bool = True):
        """
        Create a set partition from ``parts`` with the appropriate parent.

        EXAMPLES::

            sage: s = SetPartition([[1,3],[2,4]]); s
            {{1, 3}, {2, 4}}
            sage: s.parent()
            Set partitions
        """
    def __init__(self, parent, s, check: bool = True) -> None:
        """
        Initialize ``self``.

        Internally, a set partition is stored as iterable of blocks,
        sorted by minimal element.

        EXAMPLES::

            sage: S = SetPartitions(4)
            sage: s = S([[1,3],[2,4]])
            sage: TestSuite(s).run()
            sage: SetPartition([])
            {}
        """
    def check(self) -> None:
        """
        Check that we are a valid set partition.

        EXAMPLES::

            sage: S = SetPartitions(4)
            sage: s = S([[1, 3], [2, 4]])
            sage: s.check()

        TESTS::

            sage: s = S([[1, 2, 3]], check=False)
            sage: s.check()
            Traceback (most recent call last):
            ...
            ValueError: {{1, 2, 3}} is not an element of Set partitions of {1, 2, 3, 4}

            sage: s = S([1, 2, 3])
            Traceback (most recent call last):
            ...
            TypeError: 'sage.rings.integer.Integer' object is not iterable
        """
    def set_latex_options(self, **kwargs) -> None:
        """
        Set the latex options for use in the ``_latex_`` function.

        - ``tikz_scale`` -- (default: 1) scale for use with tikz package

        - ``plot`` -- (default: ``None``) ``None`` returns the set notation,
          ``linear`` returns a linear plot, ``cyclic`` returns a cyclic
          plot

        - ``color`` -- (default: ``'black'``) the arc colors

        - ``fill`` -- boolean (default: ``False``); if ``True`` then fills
          ``color``, else you can pass in a color to alter the fill color -
          *only works with cyclic plot*

        - ``show_labels`` -- boolean (default: ``True``); if ``True`` shows
          labels (*only works with plots*)

        - ``radius`` -- (default: ``'1cm'``) radius of circle for cyclic
          plot - *only works with cyclic plot*

        - ``angle`` -- (default: 0) angle for linear plot

        EXAMPLES::

            sage: SP = SetPartition([[1,6], [3,5,4]])
            sage: SP.set_latex_options(tikz_scale=2,plot='linear',fill=True,color='blue',angle=45)
            sage: SP.set_latex_options(plot='cyclic')
            sage: SP.latex_options()
            {'angle': 45,
             'color': 'blue',
             'fill': True,
             'plot': 'cyclic',
             'radius': '1cm',
             'show_labels': True,
             'tikz_scale': 2}
        """
    def latex_options(self):
        """
        Return the latex options for use in the ``_latex_`` function as a
        dictionary. The default values are set using the global options.

        Options can be found in :meth:`set_latex_options`

        EXAMPLES::

            sage: SP = SetPartition([[1,6], [3,5,4]]); SP.latex_options()
            {'angle': 0,
             'color': 'black',
             'fill': False,
             'plot': None,
             'radius': '1cm',
             'show_labels': True,
             'tikz_scale': 1}
        """
    cardinality: Incomplete
    size: Incomplete
    def pipe(self, other):
        """
        Return the pipe of the set partitions ``self`` and ``other``.

        The pipe of two set partitions is defined as follows:

        For any integer `k` and any subset `I` of `\\ZZ`, let `I + k`
        denote the subset of `\\ZZ` obtained by adding `k` to every
        element of `k`.

        If `B` and `C` are set partitions of `[n]` and `[m]`,
        respectively, then the pipe of `B` and `C` is defined as the
        set partition

        .. MATH::

            \\{ B_1, B_2, \\ldots, B_b,
            C_1 + n, C_2 + n, \\ldots, C_c + n \\}

        of `[n+m]`, where `B = \\{ B_1, B_2, \\ldots, B_b \\}` and
        `C = \\{ C_1, C_2, \\ldots, C_c \\}`. This pipe is denoted by
        `B | C`.

        EXAMPLES::

            sage: SetPartition([[1,3],[2,4]]).pipe(SetPartition([[1,3],[2]]))
            {{1, 3}, {2, 4}, {5, 7}, {6}}
            sage: SetPartition([]).pipe(SetPartition([[1,2],[3,5],[4]]))
            {{1, 2}, {3, 5}, {4}}
            sage: SetPartition([[1,2],[3,5],[4]]).pipe(SetPartition([]))
            {{1, 2}, {3, 5}, {4}}
            sage: SetPartition([[1,2],[3]]).pipe(SetPartition([[1]]))
            {{1, 2}, {3}, {4}}
        """
    def shape(self):
        """
        Return the integer partition whose parts are the sizes of the sets
        in ``self``.

        EXAMPLES::

            sage: S = SetPartitions(5)
            sage: x = S([[1,2], [3,5,4]])
            sage: x.shape()
            [3, 2]
            sage: y = S([[2], [3,1], [5,4]])
            sage: y.shape()
            [2, 2, 1]
        """
    shape_partition = shape
    to_partition = shape
    def to_permutation(self):
        """
        Convert a set partition of `\\{1,...,n\\}` to a permutation by considering
        the blocks of the partition as cycles.

        The cycles are such that the number of excedences is maximised, that is,
        each cycle is of the form `(a_1,a_2, ...,a_k)` with `a_1<a_2<...<a_k`.

        EXAMPLES::

            sage: s = SetPartition([[1,3],[2,4]])
            sage: s.to_permutation()
            [3, 4, 1, 2]
        """
    def to_restricted_growth_word(self, bijection: str = 'blocks'):
        '''
        Convert a set partition of `\\{1,...,n\\}` to a word of length `n`
        with letters in the nonnegative integers such that each
        letter is at most 1 larger than all the letters before.

        INPUT:

        - ``bijection`` -- (default: ``blocks``) defines the map from
          set partitions to restricted growth functions.  These are
          currently:

          - ``blocks``: :meth:`to_restricted_growth_word_blocks`.

          - ``intertwining``: :meth:`to_restricted_growth_word_intertwining`.

        OUTPUT: a restricted growth word

        .. SEEALSO::

            :meth:`SetPartitions.from_restricted_growth_word`

        EXAMPLES::

            sage: P = SetPartition([[1,4],[2,8],[3,5,6,9],[7]])
            sage: P.to_restricted_growth_word()
            [0, 1, 2, 0, 2, 2, 3, 1, 2]

            sage: P.to_restricted_growth_word("intertwining")
            [0, 1, 2, 2, 1, 0, 3, 3, 2]

            sage: P = SetPartition([[1,2,4,7],[3,9],[5,6,10,11,13],[8],[12]])
            sage: P.to_restricted_growth_word()
            [0, 0, 1, 0, 2, 2, 0, 3, 1, 2, 2, 4, 2]

            sage: P.to_restricted_growth_word("intertwining")
            [0, 0, 1, 1, 2, 0, 1, 3, 3, 3, 0, 4, 1]

        TESTS::

            sage: P = SetPartition([])
            sage: P.to_restricted_growth_word()
            []
            sage: P.to_restricted_growth_word("intertwining")
            []
            sage: S = SetPartitions(5, 2)
            sage: all(S.from_restricted_growth_word(P.to_restricted_growth_word()) == P for P in S)
            True

            sage: S = SetPartitions(5, 2)
            sage: all(S.from_restricted_growth_word(P.to_restricted_growth_word("intertwining"), "intertwining") == P for P in S)
            True
        '''
    def to_restricted_growth_word_blocks(self):
        """
        Convert a set partition of `\\{1,...,n\\}` to a word of length `n`
        with letters in the nonnegative integers such that each
        letter is at most 1 larger than all the letters before.

        The word is obtained by sorting the blocks by their minimal
        element and setting the letters at the positions of the
        elements in the `i`-th block to `i`.

        OUTPUT: a restricted growth word

        .. SEEALSO::

            :meth:`to_restricted_growth_word`
            :meth:`SetPartitions.from_restricted_growth_word`

        EXAMPLES::

            sage: P = SetPartition([[1,4],[2,8],[3,5,6,9],[7]])
            sage: P.to_restricted_growth_word_blocks()
            [0, 1, 2, 0, 2, 2, 3, 1, 2]
        """
    def to_restricted_growth_word_intertwining(self):
        """
        Convert a set partition of `\\{1,...,n\\}` to a word of length `n`
        with letters in the nonnegative integers such that each
        letter is at most 1 larger than all the letters before.

        The `i`-th letter of the word is the numbers of crossings of
        the arc (or half-arc) in the extended arc diagram ending at
        `i`, with arcs (or half-arcs) beginning at a smaller element
        and ending at a larger element.

        OUTPUT: a restricted growth word

        .. SEEALSO::

            :meth:`to_restricted_growth_word`
            :meth:`SetPartitions.from_restricted_growth_word`

        EXAMPLES::

            sage: P = SetPartition([[1,4],[2,8],[3,5,6,9],[7]])
            sage: P.to_restricted_growth_word_intertwining()
            [0, 1, 2, 2, 1, 0, 3, 3, 2]
        """
    def openers(self):
        """
        Return the minimal elements of the blocks.

        EXAMPLES::

            sage: P = SetPartition([[1,2,4,7],[3,9],[5,6,10,11,13],[8],[12]])
            sage: P.openers()
            [1, 3, 5, 8, 12]
        """
    def closers(self):
        """
        Return the maximal elements of the blocks.

        EXAMPLES::

            sage: P = SetPartition([[1,2,4,7],[3,9],[5,6,10,11,13],[8],[12]])
            sage: P.closers()
            [7, 8, 9, 12, 13]
        """
    def to_rook_placement(self, bijection: str = 'arcs'):
        '''
        Return a set of pairs defining a placement of non-attacking rooks
        on a triangular board.

        The cells of the board corresponding to a set partition of
        `\\{1,...,n\\}` are the pairs `(i,j)` with `0 < i < j < n+1`.

        INPUT:

        - ``bijection`` -- (default: ``arcs``) defines the bijection
          from set partitions to rook placements.  These are
          currently:

          - ``arcs``: :meth:`arcs`
          - ``gamma``: :meth:`to_rook_placement_gamma`
          - ``rho``: :meth:`to_rook_placement_rho`
          - ``psi``: :meth:`to_rook_placement_psi`

        .. SEEALSO::

            :meth:`SetPartitions.from_rook_placement`

        EXAMPLES::

            sage: P = SetPartition([[1,2,4,7],[3,9],[5,6,10,11,13],[8],[12]])
            sage: P.to_rook_placement()
            [(1, 2), (2, 4), (4, 7), (3, 9), (5, 6), (6, 10), (10, 11), (11, 13)]
            sage: P.to_rook_placement("gamma")
            [(1, 4), (3, 5), (4, 6), (5, 8), (7, 11), (8, 9), (10, 12), (12, 13)]
            sage: P.to_rook_placement("rho")
            [(1, 2), (2, 6), (3, 4), (4, 10), (5, 9), (6, 7), (10, 11), (11, 13)]
            sage: P.to_rook_placement("psi")
            [(1, 2), (2, 6), (3, 4), (5, 9), (6, 7), (7, 10), (9, 11), (11, 13)]
        '''
    def to_rook_placement_gamma(self):
        '''
        Return the rook diagram obtained by placing rooks according to
        Wachs and White\'s bijection gamma.

        Note that our index convention differs from the convention in
        [WW1991]_: regarding the rook board as a lower-right
        triangular grid, we refer with `(i,j)` to the cell in the
        `i`-th column from the right and the `j`-th row from the top.

        The algorithm proceeds as follows: non-attacking rooks are
        placed beginning at the left column.  If `n+1-i` is an
        opener, column `i` remains empty.  Otherwise, we place a rook
        into column `i`, such that the number of cells below the
        rook, which are not yet attacked by another rook, equals the
        index of the block to which `n+1-i` belongs.

        OUTPUT: list of coordinates

        .. SEEALSO::

            - :meth:`to_rook_placement`
            - :meth:`SetPartitions.from_rook_placement`
            - :meth:`SetPartitions.from_rook_placement_gamma`

        EXAMPLES::

            sage: P = SetPartition([[1,4],[2,8],[3,5,6,9],[7]])
            sage: P.to_rook_placement_gamma()
            [(1, 3), (2, 7), (4, 5), (5, 6), (6, 9)]

        Figure 5 in [WW1991]_::

            sage: P = SetPartition([[1,2,4,7],[3,9],[5,6,10,11,13],[8],[12]])
            sage: r = P.to_rook_placement_gamma(); r
            [(1, 4), (3, 5), (4, 6), (5, 8), (7, 11), (8, 9), (10, 12), (12, 13)]

        TESTS::

            sage: P = SetPartition([])
            sage: P.to_rook_placement_gamma()
            []
            sage: S = SetPartitions(5, 2)
            sage: all(S.from_rook_placement(P.to_rook_placement("gamma"), "gamma") == P for P in S)
            True
        '''
    def to_rook_placement_rho(self):
        '''
        Return the rook diagram obtained by placing rooks according to
        Wachs and White\'s bijection rho.

        Note that our index convention differs from the convention in
        [WW1991]_: regarding the rook board as a lower-right
        triangular grid, we refer with `(i,j)` to the cell in the
        `i`-th column from the right and the `j`-th row from the top.

        The algorithm proceeds as follows: non-attacking rooks are
        placed beginning at the top row.  The columns corresponding
        to the closers of the set partition remain empty.  Let `rs_j`
        be the number of closers which are larger than `j` and
        whose block is before the block of `j`.

        We then place a rook into row `j`, such that the number of
        cells to the left of the rook, which are not yet attacked by
        another rook and are not in a column corresponding to a
        closer, equals `rs_j`, unless there are not enough cells in
        this row available, in which case the row remains empty.

        One can show that the precisely those rows which correspond
        to openers of the set partition remain empty.

        OUTPUT: list of coordinates

        .. SEEALSO::

            - :meth:`to_rook_placement`
            - :meth:`SetPartitions.from_rook_placement`
            - :meth:`SetPartitions.from_rook_placement_rho`

        EXAMPLES::

            sage: P = SetPartition([[1,4],[2,8],[3,5,6,9],[7]])
            sage: P.to_rook_placement_rho()
            [(1, 5), (2, 6), (3, 4), (5, 9), (6, 8)]

        Figure 6 in [WW1991]_::

            sage: P = SetPartition([[1,2,4,7],[3,9],[5,6,10,11,13],[8],[12]])
            sage: r = P.to_rook_placement_rho(); r
            [(1, 2), (2, 6), (3, 4), (4, 10), (5, 9), (6, 7), (10, 11), (11, 13)]

            sage: sorted(P.closers() + [i for i, _ in r]) == list(range(1,14))
            True
            sage: sorted(P.openers() + [j for _, j in r]) == list(range(1,14))
            True

        TESTS::

            sage: P = SetPartition([])
            sage: P.to_rook_placement_rho()
            []
            sage: S = SetPartitions(5, 2)
            sage: all(S.from_rook_placement(P.to_rook_placement("rho"), "rho") == P for P in S)
            True
        '''
    def to_rook_placement_psi(self):
        '''
        Return the rook diagram obtained by placing rooks according to
        Yip\'s bijection psi.

        OUTPUT: list of coordinates

        .. SEEALSO::

            - :meth:`to_rook_placement`
            - :meth:`SetPartitions.from_rook_placement`
            - :meth:`SetPartitions.from_rook_placement_psi`

        EXAMPLES:

        Example 36 (arXiv version: Example 4.5) in [Yip2018]_::

            sage: P = SetPartition([[1, 5], [2], [3, 8, 9], [4], [6, 7]])
            sage: P.to_rook_placement_psi()
            [(1, 7), (3, 8), (4, 5), (7, 9)]

        Note that the columns corresponding to the minimal elements
        of the blocks remain empty.

        TESTS::

            sage: P = SetPartition([])
            sage: P.to_rook_placement_psi()
            []
            sage: S = SetPartitions(5,2)
            sage: all(S.from_rook_placement(P.to_rook_placement("psi"), "psi") == P for P in S)
            True
        '''
    def apply_permutation(self, p):
        """
        Apply ``p`` to the underlying set of ``self``.

        INPUT:

        - ``p`` -- a permutation

        EXAMPLES::

            sage: x = SetPartition([[1,2], [3,5,4]])
            sage: p = Permutation([2,1,4,5,3])
            sage: x.apply_permutation(p)
            {{1, 2}, {3, 4, 5}}
            sage: q = Permutation([3,2,1,5,4])
            sage: x.apply_permutation(q)
            {{1, 4, 5}, {2, 3}}

            sage: m = PerfectMatching([(1,4),(2,6),(3,5)])
            sage: m.apply_permutation(Permutation([4,1,5,6,3,2]))
            [(1, 2), (3, 5), (4, 6)]
        """
    def crossings_iterator(self) -> Generator[Incomplete]:
        """
        Return the crossing arcs of a set partition on a totally ordered set.

        OUTPUT:

        We place the elements of the ground set in order on a
        line and draw the set partition by linking consecutive
        elements of each block in the upper half-plane. This
        function returns an iterator over the pairs of crossing
        lines (as a line correspond to a pair, the iterator
        produces pairs of pairs).

        EXAMPLES::

            sage: p = SetPartition([[1,4],[2,5,7],[3,6]])
            sage: next(p.crossings_iterator())
            ((1, 4), (2, 5))

        TESTS::

            sage: p = SetPartition([]);  p.crossings()
            []
        """
    def crossings(self):
        """
        Return the crossing arcs of a set partition on a totally ordered set.

        OUTPUT:

        We place the elements of the ground set in order on a
        line and draw the set partition by linking consecutive
        elements of each block in the upper half-plane. This
        function returns a list of the pairs of crossing lines
        (as a line correspond to a pair, it returns a list of
        pairs of pairs).

        EXAMPLES::

            sage: p = SetPartition([[1,4],[2,5,7],[3,6]])
            sage: p.crossings()
            [((1, 4), (2, 5)), ((1, 4), (3, 6)), ((2, 5), (3, 6)), ((3, 6), (5, 7))]

        TESTS::

            sage: p = SetPartition([]);  p.crossings()
            []
        """
    def number_of_crossings(self):
        """
        Return the number of crossings.

        OUTPUT:

        We place the elements of the ground set in order on a
        line and draw the set partition by linking consecutive
        elements of each block in the upper half-plane. This
        function returns the number the pairs of crossing lines.

        EXAMPLES::

            sage: p = SetPartition([[1,4],[2,5,7],[3,6]])
            sage: p.number_of_crossings()
            4

            sage: n = PerfectMatching([3,8,1,7,6,5,4,2]); n
            [(1, 3), (2, 8), (4, 7), (5, 6)]
            sage: n.number_of_crossings()
            1
        """
    def is_noncrossing(self) -> bool:
        """
        Check if ``self`` is noncrossing.

        OUTPUT:

        We place the elements of the ground set in order on a
        line and draw the set partition by linking consecutive
        elements of each block in the upper half-plane.  This
        function returns ``True`` if the picture obtained this
        way has no crossings.

        EXAMPLES::

            sage: p = SetPartition([[1,4],[2,5,7],[3,6]])
            sage: p.is_noncrossing()
            False

            sage: n = PerfectMatching([3,8,1,7,6,5,4,2]); n
            [(1, 3), (2, 8), (4, 7), (5, 6)]
            sage: n.is_noncrossing()
            False
            sage: PerfectMatching([(1, 4), (2, 3), (5, 6)]).is_noncrossing()
            True
        """
    def nestings_iterator(self) -> Generator[Incomplete]:
        """
        Iterate over the nestings of ``self``.

        OUTPUT:

        We place the elements of the ground set in order on a
        line and draw the set partition by linking consecutive
        elements of each block in the upper half-plane. This
        function returns an iterator over the pairs of nesting
        lines (as a line correspond to a pair, the iterator
        produces pairs of pairs).

        EXAMPLES::

            sage: n = PerfectMatching([(1, 6), (2, 7), (3, 5), (4, 8)])
            sage: it = n.nestings_iterator()
            sage: next(it)
            ((1, 6), (3, 5))
            sage: next(it)
            ((2, 7), (3, 5))
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration
        """
    def nestings(self):
        """
        Return the nestings of ``self``.

        OUTPUT:

        We place the elements of the ground set in order on a
        line and draw the set partition by linking consecutive
        elements of each block in the upper half-plane. This
        function returns the list of the pairs of nesting lines
        (as a line correspond to a pair, it returns a list of
        pairs of pairs).

        EXAMPLES::

            sage: m = PerfectMatching([(1, 6), (2, 7), (3, 5), (4, 8)])
            sage: m.nestings()
            [((1, 6), (3, 5)), ((2, 7), (3, 5))]

            sage: n = PerfectMatching([3,8,1,7,6,5,4,2]); n
            [(1, 3), (2, 8), (4, 7), (5, 6)]
            sage: n.nestings()
            [((2, 8), (4, 7)), ((2, 8), (5, 6)), ((4, 7), (5, 6))]

        TESTS::

            sage: m = PerfectMatching([]); m.nestings()
            []
        """
    def number_of_nestings(self):
        """
        Return the number of nestings of ``self``.

        OUTPUT:

        We place the elements of the ground set in order on a
        line and draw the set partition by linking consecutive
        elements of each block in the upper half-plane. This
        function returns the number the pairs of nesting lines.

        EXAMPLES::

            sage: n = PerfectMatching([3,8,1,7,6,5,4,2]); n
            [(1, 3), (2, 8), (4, 7), (5, 6)]
            sage: n.number_of_nestings()
            3
        """
    def is_nonnesting(self) -> bool:
        """
        Return if ``self`` is nonnesting or not.

        OUTPUT:

        We place the elements of the ground set in order on a
        line and draw the set partition by linking consecutive
        elements of each block in the upper half-plane. This
        function returns ``True`` if the picture obtained this
        way has no nestings.

        EXAMPLES::

            sage: n = PerfectMatching([3,8,1,7,6,5,4,2]); n
            [(1, 3), (2, 8), (4, 7), (5, 6)]
            sage: n.is_nonnesting()
            False
            sage: PerfectMatching([(1, 3), (2, 5), (4, 6)]).is_nonnesting()
            True
        """
    def is_atomic(self) -> bool:
        """
        Return if ``self`` is an atomic set partition.

        A (standard) set partition `A` can be split if there exist `j < i`
        such that `\\max(A_j) < \\min(A_i)` where `A` is ordered by minimal
        elements. This means we can write `A = B | C` for some nonempty set
        partitions `B` and `C`. We call a set partition *atomic* if it
        cannot be split and is nonempty. Here, the pipe symbol
        `|` is as defined in method :meth:`pipe`.

        EXAMPLES::

            sage: SetPartition([[1,3], [2]]).is_atomic()
            True
            sage: SetPartition([[1,3], [2], [4]]).is_atomic()
            False
            sage: SetPartition([[1], [2,4], [3]]).is_atomic()
            False
            sage: SetPartition([[1,2,3,4]]).is_atomic()
            True
            sage: SetPartition([[1, 4], [2], [3]]).is_atomic()
            True
            sage: SetPartition([]).is_atomic()
            False
        """
    def standardization(self):
        """
        Return the standardization of ``self``.

        Given a set partition `A = \\{A_1, \\ldots, A_n\\}` of an ordered
        set `S`, the standardization of `A` is the set partition of
        `\\{1, 2, \\ldots, |S|\\}` obtained by replacing the elements of
        the parts of `A` by the integers `1, 2, \\ldots, |S|` in such
        a way that their relative order is preserved (i. e., the
        smallest element in the whole set partition is replaced by
        `1`, the next-smallest by `2`, and so on).

        EXAMPLES::

            sage: SetPartition([[4], [1, 3]]).standardization()
            {{1, 2}, {3}}
            sage: SetPartition([[4], [6, 3]]).standardization()
            {{1, 3}, {2}}
            sage: SetPartition([]).standardization()
            {}
            sage: SetPartition([('c','b'),('d','f'),('e','a')]).standardization()
            {{1, 5}, {2, 3}, {4, 6}}
        """
    def restriction(self, I):
        """
        Return the restriction of ``self`` to a subset ``I``
        (which is given as a set or list or any other iterable).

        EXAMPLES::

            sage: A = SetPartition([[1], [2,3]])
            sage: A.restriction([1,2])
            {{1}, {2}}
            sage: A.restriction([2,3])
            {{2, 3}}
            sage: A.restriction([])
            {}
            sage: A.restriction([4])
            {}
        """
    def ordered_set_partition_action(self, s):
        """
        Return the action of an ordered set partition ``s`` on ``self``.

        Let `A = \\{A_1, A_2, \\ldots, A_k\\}` be a set partition of some
        set `S` and `s` be an ordered set partition (i.e., set composition)
        of a subset of `[k]`. Let `A^{\\downarrow}` denote the standardization
        of `A`, and `A_{\\{ i_1, i_2, \\ldots, i_m \\}}` denote the sub-partition
        `\\{A_{i_1}, A_{i_2}, \\ldots, A_{i_m}\\}` for any subset
        `\\{i_1, \\ldots, i_m\\}` of `\\{1, \\ldots, k\\}`. We define the set
        partition `s(A)` by

        .. MATH::

            s(A) = A_{s_1}^{\\downarrow} | A_{s_2}^{\\downarrow} | \\cdots
            | A_{s_q}^{\\downarrow}.

        where `s = (s_1, s_2, \\ldots, s_q)`. Here, the pipe symbol
        `|` is as defined in method :meth:`pipe`.

        This is `s[A]` in section 2.3 in [LM2011]_.

        INPUT:

        - ``s`` -- an ordered set partition with base set a subset
          of `\\{1, \\ldots, k\\}`

        EXAMPLES::

            sage: A = SetPartition([[1], [2,4], [3]])
            sage: s = OrderedSetPartition([[1,3], [2]])
            sage: A.ordered_set_partition_action(s)
            {{1}, {2}, {3, 4}}
            sage: s = OrderedSetPartition([[2,3], [1]])
            sage: A.ordered_set_partition_action(s)
            {{1, 3}, {2}, {4}}

        We create Figure 1 in [LM2011]_ (we note that there is a typo in the
        lower-left corner of the table in the published version of the
        paper, whereas the arXiv version gives the correct partition)::

            sage: A = SetPartition([[1,3], [2,9], [4,5,8], [7]])
            sage: B = SetPartition([[1,3], [2,8], [4,5,6], [7]])
            sage: C = SetPartition([[1,5], [2,8], [3,4,6], [7]])
            sage: s = OrderedSetPartition([[1,3], [2]])
            sage: t = OrderedSetPartition([[2], [3,4]])
            sage: u = OrderedSetPartition([[1], [2,3,4]])
            sage: A.ordered_set_partition_action(s)
            {{1, 2}, {3, 4, 5}, {6, 7}}
            sage: A.ordered_set_partition_action(t)
            {{1, 2}, {3, 4, 6}, {5}}
            sage: A.ordered_set_partition_action(u)
            {{1, 2}, {3, 8}, {4, 5, 7}, {6}}
            sage: B.ordered_set_partition_action(s)
            {{1, 2}, {3, 4, 5}, {6, 7}}
            sage: B.ordered_set_partition_action(t)
            {{1, 2}, {3, 4, 5}, {6}}
            sage: B.ordered_set_partition_action(u)
            {{1, 2}, {3, 8}, {4, 5, 6}, {7}}
            sage: C.ordered_set_partition_action(s)
            {{1, 4}, {2, 3, 5}, {6, 7}}
            sage: C.ordered_set_partition_action(t)
            {{1, 2}, {3, 4, 5}, {6}}
            sage: C.ordered_set_partition_action(u)
            {{1, 2}, {3, 8}, {4, 5, 6}, {7}}

        REFERENCES:

        - [LM2011]_
        """
    def refinements(self):
        """
        Return a list of refinements of ``self``.

        .. SEEALSO::

            :meth:`coarsenings`

        EXAMPLES::

            sage: SetPartition([[1,3],[2,4]]).refinements()                             # needs sage.graphs sage.libs.flint
            [{{1, 3}, {2, 4}},
             {{1, 3}, {2}, {4}},
             {{1}, {2, 4}, {3}},
             {{1}, {2}, {3}, {4}}]
            sage: SetPartition([[1],[2,4],[3]]).refinements()                           # needs sage.graphs sage.libs.flint
            [{{1}, {2, 4}, {3}}, {{1}, {2}, {3}, {4}}]
            sage: SetPartition([]).refinements()                                        # needs sage.graphs sage.libs.flint
            [{}]
        """
    def strict_coarsenings(self):
        """
        Return all strict coarsenings of ``self``.

        Strict coarsening is the binary relation on set partitions
        defined as the transitive-and-reflexive closure of the
        relation `\\prec` defined as follows: For two set partitions
        `A` and `B`, we have `A \\prec B` if there exist parts
        `A_i, A_j` of `A` such that `\\max(A_i) < \\min(A_j)` and
        `B = A \\setminus \\{A_i, A_j\\} \\cup \\{ A_i \\cup A_j \\}`.

        EXAMPLES::

            sage: A = SetPartition([[1],[2,3],[4]])
            sage: A.strict_coarsenings()
            [{{1}, {2, 3}, {4}}, {{1, 2, 3}, {4}}, {{1, 4}, {2, 3}},
             {{1}, {2, 3, 4}}, {{1, 2, 3, 4}}]
            sage: SetPartition([[1],[2,4],[3]]).strict_coarsenings()
            [{{1}, {2, 4}, {3}}, {{1, 2, 4}, {3}}, {{1, 3}, {2, 4}}]
            sage: SetPartition([]).strict_coarsenings()
            [{}]
        """
    def arcs(self):
        """
        Return ``self`` as a list of arcs.

        Assuming that the blocks are sorted, the arcs are the pairs
        of consecutive elements in the blocks.

        EXAMPLES::

            sage: A = SetPartition([[1],[2,3],[4]])
            sage: A.arcs()
            [(2, 3)]
            sage: B = SetPartition([[1,3,6,7],[2,5],[4]])
            sage: B.arcs()
            [(1, 3), (3, 6), (6, 7), (2, 5)]
        """
    def plot(self, angle=None, color: str = 'black', base_set_dict=None):
        """
        Return a plot of ``self``.

        INPUT:

        - ``angle`` -- (default: `\\pi/4`) the angle at which the arcs take off
          (if angle is negative, the arcs are drawn below the horizontal line)

        - ``color`` -- (default: ``'black'``) color of the arcs

        - ``base_set_dict`` -- (optional) dictionary with keys elements
          of :meth:`base_set()` and values as integer or float

        EXAMPLES::

            sage: p = SetPartition([[1,10,11],[2,3,7],[4,5,6],[8,9]])
            sage: p.plot()                                                              # needs sage.plot sage.symbolic
            Graphics object consisting of 29 graphics primitives

        .. PLOT::

            p = SetPartition([[1,10,11],[2,3,7],[4,5,6],[8,9]])
            sphinx_plot(p.plot())

        ::

            sage: p = SetPartition([[1,3,4],[2,5]])
            sage: print(p.plot().description())                                         # needs sage.plot sage.symbolic
            Point set defined by 1 point(s):    [(0.0, 0.0)]
            Point set defined by 1 point(s):    [(1.0, 0.0)]
            Point set defined by 1 point(s):    [(2.0, 0.0)]
            Point set defined by 1 point(s):    [(3.0, 0.0)]
            Point set defined by 1 point(s):    [(4.0, 0.0)]
            Text '1' at the point (0.0,-0.1)
            Text '2' at the point (1.0,-0.1)
            Text '3' at the point (2.0,-0.1)
            Text '4' at the point (3.0,-0.1)
            Text '5' at the point (4.0,-0.1)
            Arc with center (1.0,-1.0) radii (1.41421356237...,1.41421356237...)
             angle 0.0 inside the sector (0.785398163397...,2.35619449019...)
            Arc with center (2.5,-0.5) radii (0.70710678118...,0.70710678118...)
             angle 0.0 inside the sector (0.785398163397...,2.35619449019...)
            Arc with center (2.5,-1.5) radii (2.1213203435...,2.1213203435...)
             angle 0.0 inside the sector (0.785398163397...,2.35619449019...)
            sage: p = SetPartition([['a','c'],['b','d'],['e']])
            sage: print(p.plot().description())                                         # needs sage.plot sage.symbolic
            Point set defined by 1 point(s):  [(0.0, 0.0)]
            Point set defined by 1 point(s):    [(1.0, 0.0)]
            Point set defined by 1 point(s):    [(2.0, 0.0)]
            Point set defined by 1 point(s):    [(3.0, 0.0)]
            Point set defined by 1 point(s):    [(4.0, 0.0)]
            Text 'a' at the point (0.0,-0.1)
            Text 'b' at the point (1.0,-0.1)
            Text 'c' at the point (2.0,-0.1)
            Text 'd' at the point (3.0,-0.1)
            Text 'e' at the point (4.0,-0.1)
            Arc with center (1.0,-1.0) radii (1.41421356237...,1.41421356237...)
             angle 0.0 inside the sector (0.785398163397...,2.35619449019...)
            Arc with center (2.0,-1.0) radii (1.41421356237...,1.41421356237...)
             angle 0.0 inside the sector (0.785398163397...,2.35619449019...)
            sage: p = SetPartition([['a','c'],['b','d'],['e']])
            sage: print(p.plot(base_set_dict={'a':0,'b':1,'c':2,                        # needs sage.plot sage.symbolic
            ....:                             'd':-2.3,'e':5.4}).description())
            Point set defined by 1 point(s):    [(-2.3, 0.0)]
            Point set defined by 1 point(s):    [(0.0, 0.0)]
            Point set defined by 1 point(s):    [(1.0, 0.0)]
            Point set defined by 1 point(s):    [(2.0, 0.0)]
            Point set defined by 1 point(s):    [(5.4, 0.0)]
            Text 'a' at the point (0.0,-0.1)
            Text 'b' at the point (1.0,-0.1)
            Text 'c' at the point (2.0,-0.1)
            Text 'd' at the point (-2.3,-0.1)
            Text 'e' at the point (5.4,-0.1)
            Arc with center (-0.6...,-1.65) radii (2.3334523779...,2.3334523779...)
             angle 0.0 inside the sector (0.785398163397...,2.35619449019...)
            Arc with center (1.0,-1.0) radii (1.4142135623...,1.4142135623...)
             angle 0.0 inside the sector (0.785398163397...,2.35619449019...)
        """

class SetPartitions(UniqueRepresentation, Parent):
    """
    An (unordered) partition of a set `S` is a set of pairwise
    disjoint nonempty subsets with union `S`, and is represented
    by a sorted list of such subsets.

    ``SetPartitions(s)`` returns the class of all set partitions of the set
    ``s``, which can be given as a set or a string; if a string, each
    character is considered an element.

    ``SetPartitions(n)``, where ``n`` is an integer, returns the class of
    all set partitions of the set `\\{1, 2, \\ldots, n\\}`.

    You may specify a second argument `k`. If `k` is an integer,
    :class:`SetPartitions` returns the class of set partitions into `k` parts;
    if it is an integer partition, :class:`SetPartitions` returns the class of
    set partitions whose block sizes correspond to that integer partition.

    The Bell number `B_n`, named in honor of Eric Temple Bell,
    is the number of different partitions of a set with `n` elements.

    EXAMPLES::

        sage: S = [1,2,3,4]
        sage: SetPartitions(S, 2)
        Set partitions of {1, 2, 3, 4} with 2 parts
        sage: SetPartitions([1,2,3,4], [3,1]).list()                                    # needs sage.graphs sage.rings.finite_rings
        [{{1}, {2, 3, 4}}, {{1, 2, 3}, {4}}, {{1, 2, 4}, {3}}, {{1, 3, 4}, {2}}]
        sage: SetPartitions(7, [3,3,1]).cardinality()                                   # needs sage.libs.flint
        70

    In strings, repeated letters are not considered distinct as of
    :issue:`14140`::

        sage: SetPartitions('abcde').cardinality()                                      # needs sage.libs.flint
        52
        sage: SetPartitions('aabcd').cardinality()                                      # needs sage.libs.flint
        15

    If the number of parts exceeds the length of the set,
    an empty iterator is returned (:issue:`37643`)::

        sage: SetPartitions(range(3), 4).list()
        []
        sage: SetPartitions('abcd', 6).list()
        []

    REFERENCES:

    - :wikipedia:`Partition_of_a_set`
    """
    @staticmethod
    def __classcall_private__(cls, s=None, part=None):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: S = SetPartitions(4)
            sage: T = SetPartitions([1,2,3,4])
            sage: S is T
            True
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: S = SetPartitions(4, [2,2])
            sage: SA = SetPartitions()
            sage: all(sp in SA for sp in S)                                             # needs sage.graphs sage.modules sage.rings.finite_rings
            True
            sage: Set([Set([1,2]),Set([3,7])]) in SA                                    # needs sage.graphs
            True
            sage: Set([Set([1,2]),Set([2,3])]) in SA                                    # needs sage.graphs
            False
            sage: Set([]) in SA                                                         # needs sage.graphs
            True
        """
    Element = SetPartition
    def from_restricted_growth_word(self, w, bijection: str = 'blocks'):
        '''
        Convert a word of length `n` with letters in the nonnegative
        integers such that each letter is at most 1 larger than all
        the letters before to a set partition of `\\{1,...,n\\}`.

        INPUT:

        - ``w`` -- a restricted growth word

        - ``bijection`` -- (default: ``blocks``) defines the map from
          restricted growth functions to set partitions.  These are
          currently:

          - ``blocks``: .

          - ``intertwining``: :meth:`from_restricted_growth_word_intertwining`.

        OUTPUT: a set partition

        .. SEEALSO::

            :meth:`SetPartition.to_restricted_growth_word`

        EXAMPLES::

            sage: SetPartitions().from_restricted_growth_word([0, 1, 2, 0, 2, 2, 3, 1, 2])
            {{1, 4}, {2, 8}, {3, 5, 6, 9}, {7}}

            sage: SetPartitions().from_restricted_growth_word([0, 0, 1, 0, 2, 2, 0, 3, 1, 2, 2, 4, 2])
            {{1, 2, 4, 7}, {3, 9}, {5, 6, 10, 11, 13}, {8}, {12}}

            sage: SetPartitions().from_restricted_growth_word([0, 0, 1, 0, 2, 2, 0, 3, 1, 2, 2, 4, 2], "intertwining")
            {{1, 2, 6, 7, 9}, {3, 4}, {5, 10, 13}, {8, 11}, {12}}
        '''
    def from_restricted_growth_word_blocks(self, w):
        """
        Convert a word of length `n` with letters in the nonnegative
        integers such that each letter is at most 1 larger than all
        the letters before to a set partition of `\\{1,...,n\\}`.

        ``w[i]`` is the index of the block containing ``i+1`` when
        sorting the blocks by their minimal element.

        INPUT:

        - ``w`` -- a restricted growth word

        OUTPUT: a set partition

        .. SEEALSO::

            :meth:`from_restricted_growth_word`
            :meth:`SetPartition.to_restricted_growth_word`

        EXAMPLES::

            sage: SetPartitions().from_restricted_growth_word_blocks([0, 0, 1, 0, 2, 2, 0, 3, 1, 2, 2, 4, 2])
            {{1, 2, 4, 7}, {3, 9}, {5, 6, 10, 11, 13}, {8}, {12}}
        """
    def from_restricted_growth_word_intertwining(self, w):
        """
        Convert a word of length `n` with letters in the nonnegative
        integers such that each letter is at most 1 larger than all
        the letters before to a set partition of `\\{1,...,n\\}`.

        The `i`-th letter of the word is the numbers of crossings of
        the arc (or half-arc) in the extended arc diagram ending at
        `i`, with arcs (or half-arcs) beginning at a smaller element
        and ending at a larger element.

        INPUT:

        - ``w`` -- a restricted growth word

        OUTPUT: a set partition

        .. SEEALSO::

            :meth:`from_restricted_growth_word`
            :meth:`SetPartition.to_restricted_growth_word`

        EXAMPLES::

            sage: SetPartitions().from_restricted_growth_word_intertwining([0, 0, 1, 0, 2, 2, 0, 3, 1, 2, 2, 4, 2])
            {{1, 2, 6, 7, 9}, {3, 4}, {5, 10, 13}, {8, 11}, {12}}
        """
    def from_rook_placement(self, rooks, bijection: str = 'arcs', n=None):
        '''
        Convert a rook placement of the triangular grid to a set
        partition of `\\{1,...,n\\}`.

        If ``n`` is not given, it is first checked whether it can be
        determined from the parent, otherwise it is the maximal
        occurring integer in the set of rooks.

        INPUT:

        - ``rooks`` -- list of pairs `(i,j)` satisfying
          `0 < i < j < n+1`

        - ``bijection`` -- (default: ``arcs``) defines the map from
          rook placements to set partitions.  These are currently:

          - ``arcs``: :meth:`from_arcs`.
          - ``gamma``: :meth:`from_rook_placement_gamma`.
          - ``rho``: :meth:`from_rook_placement_rho`.
          - ``psi``: :meth:`from_rook_placement_psi`.

        - ``n`` -- (optional) the size of the ground set

        .. SEEALSO::

            :meth:`SetPartition.to_rook_placement`

        EXAMPLES::

            sage: SetPartitions(9).from_rook_placement([[1,4],[2,8],[3,5],[5,6],[6,9]])
            {{1, 4}, {2, 8}, {3, 5, 6, 9}, {7}}

            sage: SetPartitions(13).from_rook_placement([[12,13],[10,12],[8,9],[7,11],[5,8],[4,6],[3,5],[1,4]], "gamma")
            {{1, 2, 4, 7}, {3, 9}, {5, 6, 10, 11, 13}, {8}, {12}}

        TESTS::

            sage: SetPartitions().from_rook_placement([])
            {}
            sage: SetPartitions().from_rook_placement([], "gamma")
            {}
            sage: SetPartitions().from_rook_placement([], "rho")
            {}
            sage: SetPartitions().from_rook_placement([], "psi")
            {}
            sage: SetPartitions().from_rook_placement([], n=2)
            {{1}, {2}}
            sage: SetPartitions().from_rook_placement([], "gamma", 2)
            {{1}, {2}}
            sage: SetPartitions().from_rook_placement([], "rho", 2)
            {{1}, {2}}
            sage: SetPartitions().from_rook_placement([], "psi", 2)
            {{1}, {2}}
        '''
    def from_arcs(self, arcs, n):
        """
        Return the coarsest set partition of `\\{1,...,n\\}` such that any
        two elements connected by an arc are in the same block.

        INPUT:

        - ``n`` -- integer specifying the size of the set
          partition to be produced

        - ``arcs`` -- list of pairs specifying which elements are
          in the same block

        .. SEEALSO::

            - :meth:`from_rook_placement`
            - :meth:`SetPartition.to_rook_placement`
            - :meth:`SetPartition.arcs`

        EXAMPLES::

            sage: SetPartitions().from_arcs([(2,3)], 5)
            {{1}, {2, 3}, {4}, {5}}
        """
    def from_rook_placement_gamma(self, rooks, n):
        """
        Return the set partition of `\\{1,...,n\\}` corresponding to the
        given rook placement by applying Wachs and White's bijection
        gamma.

        Note that our index convention differs from the convention in
        [WW1991]_: regarding the rook board as a lower-right
        triangular grid, we refer with `(i,j)` to the cell in the
        `i`-th column from the right and the `j`-th row from the top.

        INPUT:

        - ``n`` -- integer specifying the size of the set
          partition to be produced

        - ``rooks`` -- list of pairs `(i,j)` such that `0 < i < j < n+1`

        OUTPUT: a set partition

        .. SEEALSO::

            - :meth:`from_rook_placement`
            - :meth:`SetPartition.to_rook_placement`
            - :meth:`SetPartition.to_rook_placement_gamma`

        EXAMPLES:

        Figure 5 in [WW1991]_ concerns the following rook placement::

            sage: r = [(1, 4), (3, 5), (4, 6), (5, 8), (7, 11), (8, 9), (10, 12), (12, 13)]

        Note that the rook `(1, 4)`, translated into Wachs and
        White's convention, is a rook in row 4 from the top and
        column 13 from the left.  The corresponding set partition
        is::

            sage: SetPartitions().from_rook_placement_gamma(r, 13)
            {{1, 2, 4, 7}, {3, 9}, {5, 6, 10, 11, 13}, {8}, {12}}
        """
    def from_rook_placement_rho(self, rooks, n):
        """
        Return the set partition of `\\{1,...,n\\}` corresponding to the
        given rook placement by applying Wachs and White's bijection
        rho.

        Note that our index convention differs from the convention in
        [WW1991]_: regarding the rook board as a lower-right
        triangular grid, we refer with `(i,j)` to the cell in the
        `i`-th column from the right and the `j`-th row from the top.

        INPUT:

        - ``n`` -- integer specifying the size of the set
          partition to be produced

        - ``rooks`` -- list of pairs `(i,j)` such that `0 < i < j < n+1`

        OUTPUT: a set partition

        .. SEEALSO::

            - :meth:`from_rook_placement`
            - :meth:`SetPartition.to_rook_placement`
            - :meth:`SetPartition.to_rook_placement_rho`

        EXAMPLES:

        Figure 5 in [WW1991]_ concerns the following rook placement::

            sage: r = [(1, 2), (2, 6), (3, 4), (4, 10), (5, 9), (6, 7), (10, 11), (11, 13)]

        Note that the rook `(1, 2)`, translated into Wachs and
        White's convention, is a rook in row 2 from the top and
        column 13 from the left.  The corresponding set partition
        is::

            sage: SetPartitions().from_rook_placement_rho(r, 13)
            {{1, 2, 4, 7}, {3, 9}, {5, 6, 10, 11, 13}, {8}, {12}}
        """
    def from_rook_placement_psi(self, rooks, n):
        """
        Return the set partition of `\\{1,...,n\\}` corresponding to the
        given rook placement by applying Yip's bijection psi.

        INPUT:

        - ``n`` -- integer specifying the size of the set
          partition to be produced

        - ``rooks`` -- list of pairs `(i,j)` such that `0 < i < j < n+1`

        OUTPUT: a set partition

        .. SEEALSO::

            - :meth:`from_rook_placement`
            - :meth:`SetPartition.to_rook_placement`
            - :meth:`SetPartition.to_rook_placement_psi`

        EXAMPLES:

        Example 36 (arXiv version: Example 4.5) in [Yip2018]_
        concerns the following rook placement::

            sage: r = [(4,5), (1,7), (3, 8), (7,9)]
            sage: SetPartitions().from_rook_placement_psi(r, 9)
            {{1, 5}, {2}, {3, 8, 9}, {4}, {6, 7}}
        """
    def is_less_than(self, s, t) -> bool:
        """
        Check if `s < t` in the refinement ordering on set partitions.

        This means that `s` is a refinement of `t` and satisfies
        `s \\neq t`.

        A set partition `s` is said to be a refinement of a set
        partition `t` of the same set if and only if each part of
        `s` is a subset of a part of `t`.

        EXAMPLES::

            sage: S = SetPartitions(4)
            sage: s = S([[1,3],[2,4]])
            sage: t = S([[1],[2],[3],[4]])
            sage: S.is_less_than(t, s)
            True
            sage: S.is_less_than(s, t)
            False
            sage: S.is_less_than(s, s)
            False
        """
    lt = is_less_than
    def is_strict_refinement(self, s, t) -> bool:
        """
        Return ``True`` if ``s`` is a strict refinement of ``t`` and
        satisfies `s \\neq t`.

        A set partition `s` is said to be a strict refinement of a set
        partition `t` of the same set if and only if one can obtain
        `t` from `s` by repeatedly combining pairs of parts whose
        convex hulls don't intersect (i. e., whenever we are combining
        two parts, the maximum of each of them should be smaller than
        the minimum of the other).

        EXAMPLES::

            sage: S = SetPartitions(4)
            sage: s = S([[1],[2],[3],[4]])
            sage: t = S([[1,3],[2,4]])
            sage: u = S([[1,2,3,4]])
            sage: S.is_strict_refinement(s, t)
            True
            sage: S.is_strict_refinement(t, u)
            False
            sage: A = SetPartition([[1,3],[2,4]])
            sage: B = SetPartition([[1,2,3,4]])
            sage: S.is_strict_refinement(s, A)
            True
            sage: S.is_strict_refinement(t, B)
            False
        """

class SetPartitions_all(SetPartitions):
    """
    All set partitions.
    """
    def __init__(self) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = SetPartitions()
            sage: TestSuite(S).run()
        """
    def subset(self, size=None, **kwargs):
        """
        Return the subset of set partitions of a given size and
        additional keyword arguments.

        EXAMPLES::

            sage: P = SetPartitions()
            sage: P.subset(4)
            Set partitions of {1, 2, 3, 4}
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: it = SetPartitions().__iter__()
            sage: [next(it) for x in range(10)]
            [{}, {{1}}, {{1, 2}}, {{1}, {2}}, {{1, 2, 3}}, {{1, 2}, {3}},
             {{1, 3}, {2}}, {{1}, {2, 3}}, {{1}, {2}, {3}}, {{1, 2, 3, 4}}]
        """

class SetPartitions_set(SetPartitions):
    """
    Set partitions of a fixed set `S`.
    """
    @staticmethod
    def __classcall_private__(cls, s):
        """
        Normalize ``s`` to ensure a unique representation.

        EXAMPLES::

            sage: S1 = SetPartitions(set([2,1,4]))
            sage: S2 = SetPartitions([4,1,2])
            sage: S3 = SetPartitions((1,2,4))
            sage: S1 is S2, S1 is S3
            (True, True)
        """
    def __init__(self, s) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: S = SetPartitions(3)
            sage: TestSuite(S).run()
            sage: SetPartitions(0).list()
            [{}]
            sage: SetPartitions([]).list()
            [{}]
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: S = SetPartitions(4, [2,2])
            sage: all(sp in S for sp in S)                                              # needs sage.graphs sage.rings.finite_rings
            True
            sage: SetPartition([[1,3],[2,4]]) in SetPartitions(3)                       # needs sage.graphs
            False
            sage: SetPartition([[1,3],[2,4]]) in SetPartitions(4, [3,1])                # needs sage.graphs
            False
            sage: SetPartition([[2],[1,3,4]]) in SetPartitions(4, [3,1])                # needs sage.graphs
            True
        """
    def random_element(self):
        '''
        Return a random set partition.

        This is a very naive implementation of Knuths outline in F3B,
        7.2.1.5.

        EXAMPLES::

            sage: S = SetPartitions(10)
            sage: s = S.random_element()                                                # needs sage.symbolic
            sage: s.parent() is S                                                       # needs sage.symbolic
            True
            sage: assert s in S, s                                                      # needs sage.symbolic

            sage: S = SetPartitions(["a", "b", "c"])
            sage: s = S.random_element()                                                # needs sage.symbolic
            sage: s.parent() is S                                                       # needs sage.symbolic
            True
            sage: assert s in S, s                                                      # needs sage.symbolic
        '''
    def cardinality(self):
        """
        Return the number of set partitions of the set `S`.

        The cardinality is given by the `n`-th Bell number where `n` is the
        number of elements in the set `S`.

        EXAMPLES::

            sage: # needs sage.libs.flint
            sage: SetPartitions([1,2,3,4]).cardinality()
            15
            sage: SetPartitions(3).cardinality()
            5
            sage: SetPartitions(3,2).cardinality()
            3
            sage: SetPartitions([]).cardinality()
            1
        """
    def __iter__(self):
        '''
        Iterate over ``self``.

        EXAMPLES::

            sage: SetPartitions(3).list()
            [{{1, 2, 3}}, {{1, 2}, {3}}, {{1, 3}, {2}}, {{1}, {2, 3}}, {{1}, {2}, {3}}]

            sage: SetPartitions(["a", "b"]).list()
            [{{\'a\', \'b\'}}, {{\'a\'}, {\'b\'}}]
        '''
    def base_set(self):
        '''
        Return the base set of ``self``.

        EXAMPLES::

            sage: SetPartitions(3).base_set()
            {1, 2, 3}

            sage: sorted(SetPartitions(["a", "b", "c"]).base_set())
            [\'a\', \'b\', \'c\']
        '''
    def base_set_cardinality(self):
        """
        Return the cardinality of the base set of ``self``.

        EXAMPLES::

            sage: SetPartitions(3).base_set_cardinality()
            3
        """

class SetPartitions_setparts(SetPartitions_set):
    """
    Set partitions with fixed partition sizes corresponding to an
    integer partition `\\lambda`.
    """
    @staticmethod
    def __classcall_private__(cls, s, parts):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: S = SetPartitions(4, [2,2])
            sage: T = SetPartitions([1,2,3,4], Partition([2,2]))
            sage: S is T
            True

            sage: S = SetPartitions(4, [3,1])
            sage: T = SetPartitions(4, (1,3))
            sage: S is T
            True
        """
    def __init__(self, s, parts) -> None:
        """
        Initialize the data structure.

        We can assume here that ``parts`` is a :class:`Partition`.

        TESTS::

            sage: S = SetPartitions(4, [2,2])
            sage: TestSuite(S).run()                                                    # needs sage.graphs sage.libs.flint
        """
    def shape(self):
        """
        Return the partition of block sizes of the set partitions in ``self``.

        EXAMPLES::

            sage: SetPartitions(5, [2,2,1]).shape()
            [2, 2, 1]
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        This algorithm counts for each block of the partition the
        number of ways to fill it using values from the set.  Then,
        for each distinct value `v` of block size, we divide the result by
        the number of ways to arrange the blocks of size `v` in the
        set partition.

        For example, if we want to count the number of set partitions
        of size 13 having [3,3,3,2,2] as underlying partition we
        compute the number of ways to fill each block of the
        partition, which is `\\binom{13}{3} \\binom{10}{3} \\binom{7}{3}
        \\binom{4}{2}\\binom{2}{2}` and as we have three blocks of size
        `3` and two blocks of size `2`, we divide the result by
        `3!2!` which gives us `600600`.

        EXAMPLES::

            sage: SetPartitions(3, [2,1]).cardinality()
            3
            sage: SetPartitions(13, Partition([3,3,3,2,2])).cardinality()
            600600

        TESTS::

            sage: all((len(SetPartitions(size, part)) == SetPartitions(size, part).cardinality()
            ....:     for size in range(8) for part in Partitions(size)))
            True
            sage: sum((SetPartitions(13, p).cardinality()                               # needs sage.libs.flint
            ....:     for p in Partitions(13))) == SetPartitions(13).cardinality()
            True
        """
    def __iter__(self):
        '''
        An iterator for all the set partitions of the given set with
        the given sizes.

        EXAMPLES::

            sage: SetPartitions(3, [2,1]).list()                                        # needs sage.graphs sage.rings.finite_rings
            [{{1}, {2, 3}}, {{1, 2}, {3}}, {{1, 3}, {2}}]

            sage: SetPartitions(["a", "b", "c"], [2,1]).list()                          # needs sage.graphs sage.rings.finite_rings
            [{{\'a\'}, {\'b\', \'c\'}}, {{\'a\', \'b\'}, {\'c\'}}, {{\'a\', \'c\'}, {\'b\'}}]

        TESTS::

            sage: n = 8
            sage: all(SetPartitions(n, mu).cardinality()                                # needs sage.graphs sage.rings.finite_rings
            ....:      == len(list(SetPartitions(n, mu))) for mu in Partitions(n))
            True
        '''
    def __contains__(self, x) -> bool:
        """
        Check containment.

        TESTS::

            sage: S = SetPartitions(4, [3,1])
            sage: Set([Set([1,2,3]), Set([4])]) in S
            True
            sage: Set([Set([1,3]), Set([2,4])]) in S
            False
            sage: Set([Set([1,2,3,4])]) in S
            False
        """
    def random_element(self):
        '''
        Return a random set partition of ``self``.

        ALGORITHM:

        Based on the cardinality method. For each block size `k_i`,
        we choose a uniformly random subset `X_i \\subseteq S_i` of
        size `k_i` of the elements `S_i` that have not yet been selected.
        Thus, we define `S_{i+1} = S_i \\setminus X_i` with `S_i = S`
        being the defining set. This is not yet proven to be uniformly
        distributed, but numerical tests show this is likely uniform.

        EXAMPLES::

            sage: S = SetPartitions(10, [4,3,2,1])
            sage: s = S.random_element()
            sage: s.parent() is S
            True
            sage: assert s in S, s

            sage: S = SetPartitions(["a", "b", "c", "d"], [2,2])
            sage: s = S.random_element()
            sage: s.parent() is S
            True
            sage: assert s in S, s
        '''

class SetPartitions_setn(SetPartitions_set):
    """
    Set partitions with a given number of blocks.
    """
    @staticmethod
    def __classcall_private__(cls, s, k):
        """
        Normalize ``s`` to ensure a unique representation.

        EXAMPLES::

            sage: S1 = SetPartitions(set([2,1,4]), 2)
            sage: S2 = SetPartitions([4,1,2], 2)
            sage: S3 = SetPartitions((1,2,4), 2)
            sage: S1 is S2, S1 is S3
            (True, True)
        """
    def __init__(self, s, k) -> None:
        """
        TESTS::

            sage: S = SetPartitions(5, 3)
            sage: TestSuite(S).run()
        """
    def number_of_blocks(self):
        """
        Return the number of blocks of the set partitions in ``self``.

        EXAMPLES::

            sage: SetPartitions(5, 3).number_of_blocks()
            3
        """
    def cardinality(self):
        """
        The Stirling number of the second kind is the number of partitions
        of a set of size `n` into `k` blocks.

        EXAMPLES::

            sage: SetPartitions(5, 3).cardinality()
            25
            sage: stirling_number2(5,3)
            25
        """
    def __iter__(self):
        '''
        Iterate over ``self``.

        EXAMPLES::

            sage: SetPartitions(4, 2).list()
            [{{1, 3, 4}, {2}},
             {{1, 4}, {2, 3}},
             {{1, 2, 4}, {3}},
             {{1, 3}, {2, 4}},
             {{1}, {2, 3, 4}},
             {{1, 2}, {3, 4}},
             {{1, 2, 3}, {4}}]

            sage: SetPartitions(["a", "b", "c"], 2).list()
            [{{\'a\', \'c\'}, {\'b\'}}, {{\'a\'}, {\'b\', \'c\'}}, {{\'a\', \'b\'}, {\'c\'}}]
        '''
    def __contains__(self, x) -> bool:
        """
        Check containment.

        TESTS::

            sage: S = SetPartitions(4, 2)
            sage: Set([Set([1,2,3]), Set([4])]) in S
            True
            sage: Set([Set([1,3]), Set([2,4])]) in S
            True
            sage: Set([Set([1,2,3,4])]) in S
            False
        """
    def random_element(self):
        '''
        Return a random set partition of ``self``.

        See https://mathoverflow.net/questions/141999.

        EXAMPLES::

            sage: S = SetPartitions(10, 4)
            sage: s = S.random_element()
            sage: s.parent() is S
            True
            sage: assert s in S, s

            sage: S = SetPartitions(["a", "b", "c"], 2)
            sage: s = S.random_element()
            sage: s.parent() is S
            True
            sage: assert s in S, s
        '''

def cyclic_permutations_of_set_partition(set_part):
    """
    Return all combinations of cyclic permutations of each cell of the
    set partition.

    AUTHORS:

    - Robert L. Miller

    EXAMPLES::

        sage: from sage.combinat.set_partition import cyclic_permutations_of_set_partition
        sage: cyclic_permutations_of_set_partition([[1,2,3,4],[5,6,7]])
        [[[1, 2, 3, 4], [5, 6, 7]],
         [[1, 2, 4, 3], [5, 6, 7]],
         [[1, 3, 2, 4], [5, 6, 7]],
         [[1, 3, 4, 2], [5, 6, 7]],
         [[1, 4, 2, 3], [5, 6, 7]],
         [[1, 4, 3, 2], [5, 6, 7]],
         [[1, 2, 3, 4], [5, 7, 6]],
         [[1, 2, 4, 3], [5, 7, 6]],
         [[1, 3, 2, 4], [5, 7, 6]],
         [[1, 3, 4, 2], [5, 7, 6]],
         [[1, 4, 2, 3], [5, 7, 6]],
         [[1, 4, 3, 2], [5, 7, 6]]]
    """
def cyclic_permutations_of_set_partition_iterator(set_part) -> Generator[Incomplete]:
    """
    Iterate over all combinations of cyclic permutations of each cell
    of the set partition.

    AUTHORS:

    - Robert L. Miller

    EXAMPLES::

        sage: from sage.combinat.set_partition import cyclic_permutations_of_set_partition_iterator
        sage: list(cyclic_permutations_of_set_partition_iterator([[1,2,3,4],[5,6,7]]))
        [[[1, 2, 3, 4], [5, 6, 7]],
         [[1, 2, 4, 3], [5, 6, 7]],
         [[1, 3, 2, 4], [5, 6, 7]],
         [[1, 3, 4, 2], [5, 6, 7]],
         [[1, 4, 2, 3], [5, 6, 7]],
         [[1, 4, 3, 2], [5, 6, 7]],
         [[1, 2, 3, 4], [5, 7, 6]],
         [[1, 2, 4, 3], [5, 7, 6]],
         [[1, 3, 2, 4], [5, 7, 6]],
         [[1, 3, 4, 2], [5, 7, 6]],
         [[1, 4, 2, 3], [5, 7, 6]],
         [[1, 4, 3, 2], [5, 7, 6]]]
    """
