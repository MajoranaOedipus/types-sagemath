from _typeshed import Incomplete
from sage.combinat.binary_tree import BinaryTree as BinaryTree, BinaryTrees as BinaryTrees, LabelledBinaryTree as LabelledBinaryTree
from sage.combinat.composition import Compositions as Compositions
from sage.combinat.core import Core as Core, Cores as Cores
from sage.combinat.k_tableau import StrongTableau as StrongTableau, WeakTableau as WeakTableau
from sage.combinat.partition import Partitions as Partitions
from sage.combinat.shifted_primed_tableau import ShiftedPrimedTableau as ShiftedPrimedTableau
from sage.combinat.skew_partition import SkewPartition as SkewPartition
from sage.combinat.skew_tableau import SkewTableau as SkewTableau
from sage.combinat.words.word import Word as Word
from sage.combinat.words.words import Words as Words
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class GrowthDiagram(SageObject):
    """
    A generalized Schensted growth diagram in the sense of Fomin.

    Growth diagrams were introduced by Sergey Fomin [Fom1994]_,
    [Fom1995]_ and provide a vast generalization of the
    Robinson-Schensted-Knuth (RSK) correspondence between matrices
    with nonnegative integer entries and pairs of semistandard Young
    tableaux of the same shape.

    A growth diagram is based on the notion of *dual graded graphs*,
    a pair of digraphs `P, Q` (multiple edges being allowed) on the
    same set of vertices `V`, that satisfy the following conditions:

    * the graphs are graded, that is, there is a function `\\rho:
      V \\to \\NN`, such that for any edge `(v, w)` of `P` and also
      of `Q` we have `\\rho(w) = \\rho(v) + 1`,

    * there is a vertex `0` with rank zero, and

    * there is a positive integer `r` such that `DU = UD + rI` on the
      free `\\ZZ`-module `\\ZZ[V]`, where `D` is the down operator of
      `Q`, assigning to each vertex the formal sum of its
      predecessors, `U` is the up operator of `P`, assigning to each
      vertex the formal sum of its successors, and `I` is the
      identity operator.

    Growth diagrams are defined by providing a pair of local rules: a
    'forward' rule, whose input are three vertices `y`, `t` and `x`
    of the dual graded graphs and an integer, and whose output is a
    fourth vertex `z`.  This rule should be invertible in the
    following sense: there is a so-called 'backward' rule that
    recovers the integer and `t` given `y`, `z` and `x`.

    All implemented growth diagram rules are available by
    ``GrowthDiagram.rules.<tab>``. The current list is:

    - :class:`~sage.combinat.growth.RuleRSK` -- RSK
    - :class:`~sage.combinat.growth.RuleBurge` -- a variation of RSK
      originally due to Burge
    - :class:`~sage.combinat.growth.RuleBinaryWord` -- a correspondence
      producing binary words originally due to Viennot
    - :class:`~sage.combinat.growth.RuleDomino` -- a correspondence
      producing domino tableaux originally due to Barbasch and Vogan
    - :class:`~sage.combinat.growth.RuleShiftedShapes` -- a correspondence
      for shifted shapes, where the original insertion algorithm is due
      to Sagan and Worley, and Haiman.
    - :class:`~sage.combinat.growth.RuleSylvester` -- the Sylvester
      correspondence, producing binary trees
    - :class:`~sage.combinat.growth.RuleYoungFibonacci` -- the
      Young-Fibonacci correspondence
    - :class:`~sage.combinat.growth.RuleLLMS` -- LLMS insertion

    INPUT:

    - ``rule`` -- :class:`~sage.combinat.growth.Rule`;
      the growth diagram rule

    - ``filling`` -- (optional) a dictionary whose keys are coordinates
      and values are integers, a list of lists of integers, or a word
      with integer values; if a word, then negative letters but without
      repetitions are allowed and interpreted as coloured permutations

    - ``shape`` -- (optional) a (possibly skew) partition

    - ``labels`` -- (optional) a list that specifies a path whose length
      in the half-perimeter of the shape; more details given below

    If ``filling`` is not given, then the growth diagram is determined
    by applying the backward rule to ``labels`` decorating the
    boundary opposite of the origin of the ``shape``. In this case,
    ``labels`` are interpreted as labelling the boundary opposite of
    the origin.

    Otherwise, ``shape`` is inferred from ``filling`` or ``labels`` if
    possible and ``labels`` is set to ``rule.zero`` if not specified.
    Here, ``labels`` are labelling the boundary on the side of the origin.

    For ``labels``, if ``rule.has_multiple_edges`` is ``True``, then the
    elements should be of the form `(v_1, e_1, \\ldots, e_{n-1}, v_n)`,
    where `n` is the half-perimeter of ``shape``, and `(v_{i-1}, e_i, v_i)`
    is an edge in the dual graded graph for all `i`.  Otherwise, it is a
    list of `n` vertices.

    .. NOTE::

        Coordinates are of the form ``(col, row)`` where the origin is
        in the upper left, to be consistent with permutation matrices
        and skew tableaux (in English convention).  This is different
        from Fomin's convention, who uses a Cartesian coordinate system.

        Conventions are chosen such that for permutations, the same
        growth diagram is constructed when passing the permutation
        matrix instead.

    EXAMPLES:

    We create a growth diagram using the forward RSK rule and a permutation::

        sage: RuleRSK = GrowthDiagram.rules.RSK()
        sage: pi = Permutation([4, 1, 2, 3])
        sage: G = GrowthDiagram(RuleRSK, pi); G
        0  1  0  0
        0  0  1  0
        0  0  0  1
        1  0  0  0
        sage: G.out_labels()
        [[], [1], [1, 1], [2, 1], [3, 1], [3], [2], [1], []]

    Passing the permutation matrix instead gives the same result::

        sage: G = GrowthDiagram(RuleRSK, pi.to_matrix())                                # needs sage.modules
        sage: ascii_art([G.P_symbol(), G.Q_symbol()])                                   # needs sage.modules
        [   1  2  3    1  3  4 ]
        [   4      ,   2       ]

    We give the same example but using a skew shape::

        sage: shape = SkewPartition([[4,4,4,2],[1,1]])
        sage: G = GrowthDiagram(RuleRSK, pi, shape=shape); G
        .  1  0  0
        .  0  1  0
        0  0  0  1
        1  0
        sage: G.out_labels()
        [[], [1], [1, 1], [1], [2], [3], [2], [1], []]

    We construct a growth diagram using the backwards RSK rule by
    specifying the labels::

        sage: GrowthDiagram(RuleRSK, labels=G.out_labels())
        0  1  0  0
        0  0  1  0
        0  0  0  1
        1  0
    """
    rule: Incomplete
    def __init__(self, rule, filling=None, shape=None, labels=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: w = [3,3,2,4,1]; G = GrowthDiagram(RuleRSK, w)
            sage: [G.P_symbol(), G.Q_symbol()]
            [[[1, 3, 4], [2], [3]], [[1, 2, 4], [3], [5]]]
            sage: RSK(w)
            [[[1, 3, 4], [2], [3]], [[1, 2, 4], [3], [5]]]

            sage: TestSuite(G).run()

            sage: GrowthDiagram(RuleRSK)
            Traceback (most recent call last):
            ...
            ValueError: please provide a filling or a sequence of labels
        """
    def filling(self):
        """
        Return the filling of the diagram as a dictionary.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = GrowthDiagram(RuleRSK, [[0,1,0], [1,0,2]])
            sage: G.filling()
            {(0, 1): 1, (1, 0): 1, (2, 1): 2}
        """
    def conjugate(self):
        """
        Return the conjugate growth diagram of ``self``.

        This is the growth diagram with the filling reflected over the
        main diagonal.

        The sequence of labels along the boundary on the side of the
        origin is the reversal of the corresponding sequence of the
        original growth diagram.

        When the filling is a permutation, the conjugate filling
        corresponds to its inverse.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = GrowthDiagram(RuleRSK, [[0,1,0], [1,0,2]])
            sage: Gc = G.conjugate()
            sage: (Gc.P_symbol(), Gc.Q_symbol()) == (G.Q_symbol(), G.P_symbol())
            True

        TESTS:

        Check that labels and shape are handled correctly::

            sage: o = [[2,1],[2,2],[3,2],[4,2],[4,1],[4,1,1],[3,1,1],[3,1],[3,2],[3,1],[2,1]]
            sage: l = [o[i//2] if is_even(i) else min(o[(i-1)//2],o[(i+1)//2])
            ....:      for i in range(2*len(o)-1)]
            sage: la = list(range(len(o)-2, 0, -1))
            sage: G = RuleRSK(labels=l[1:-1], shape=la)
            sage: G.out_labels() == G.conjugate().out_labels()[::-1]
            True
        """
    def rotate(self):
        """
        Return the growth diagram with the filling rotated by 180 degrees.

        The rotated growth diagram is initialized with
        ``labels=None``, that is, all labels along the boundary on
        the side of the origin are set to ``rule.zero``.

        For RSK-growth diagrams and rectangular fillings, this
        corresponds to evacuation of the `P`- and the `Q`-symbol.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = GrowthDiagram(RuleRSK, [[0,1,0], [1,0,2]])
            sage: Gc = G.rotate()
            sage: ascii_art([Gc.P_symbol(), Gc.Q_symbol()])
            [   1  1  1    1  1  2 ]
            [   2      ,   3       ]

            sage: ascii_art([Tableau(t).evacuation()
            ....:            for t in [G.P_symbol(), G.Q_symbol()]])
            [   1  1  1    1  1  2 ]
            [   2      ,   3       ]

        TESTS:

        Check that shape is handled correctly::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = GrowthDiagram(RuleRSK,
            ....:                   filling={(0,2):1, (3,1):2, (2,1):3},
            ....:                   shape=SkewPartition([[5,5,5,3],[3,1]]))
            sage: G
            .  .  .  0  0
            .  0  3  2  0
            1  0  0  0  0
            0  0  0
            sage: G.rotate()
            .  .  0  0  0
            0  0  0  0  1
            0  2  3  0
            0  0
        """
    def half_perimeter(self):
        """
        Return half the perimeter of the shape of the growth diagram.

        TESTS::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = GrowthDiagram(RuleRSK, {(0,1):1, (2,0):1}, SkewPartition([[3,1],[1]])); G
            .  0  1
            1
            sage: G.half_perimeter()
            6
        """
    def shape(self):
        """
        Return the shape of the growth diagram as a skew partition.

        .. WARNING::

            In the literature the label on the corner opposite of the
            origin of a rectangular filling is often called the shape
            of the filling.  This method returns the shape of the
            region instead.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: GrowthDiagram(RuleRSK, [1]).shape()
            [1] / []
        """
    def out_labels(self):
        """
        Return the labels along the boundary opposite of the origin.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = GrowthDiagram(RuleRSK, [[0,1,0], [1,0,2]])
            sage: G.out_labels()
            [[], [1], [1, 1], [3, 1], [1], []]
        """
    def in_labels(self):
        """
        Return the labels along the boundary on the side of the origin.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = GrowthDiagram(RuleRSK, labels=[[2,2],[3,2],[3,3],[3,2]]); G
            1 0
            sage: G.in_labels()
            [[2, 2], [2, 2], [2, 2], [3, 2]]
        """
    def P_symbol(self):
        """
        Return the labels along the vertical boundary of a rectangular
        growth diagram as a generalized standard tableau.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = GrowthDiagram(RuleRSK, [[0,1,0], [1,0,2]])
            sage: ascii_art([G.P_symbol(), G.Q_symbol()])
            [   1  2  2    1  3  3 ]
            [   2      ,   2       ]
        """
    def Q_symbol(self):
        """
        Return the labels along the horizontal boundary of a rectangular
        growth diagram as a generalized standard tableau.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = GrowthDiagram(RuleRSK, [[0,1,0], [1,0,2]])
            sage: ascii_art([G.P_symbol(), G.Q_symbol()])
            [   1  2  2    1  3  3 ]
            [   2      ,   2       ]
        """
    def P_chain(self):
        """
        Return the labels along the vertical boundary of a rectangular
        growth diagram.

        EXAMPLES::

            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: G = GrowthDiagram(BinaryWord, [4, 1, 2, 3])
            sage: G.P_chain()
            [word: , word: 1, word: 11, word: 111, word: 1011]

        Check that :issue:`25631` is fixed::

            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: BinaryWord(filling = {}).P_chain()
            [word: ]
        """
    def Q_chain(self):
        """
        Return the labels along the horizontal boundary of a rectangular
        growth diagram.

        EXAMPLES::

            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: G = GrowthDiagram(BinaryWord, [[0,1,0,0], [0,0,1,0], [0,0,0,1], [1,0,0,0]])
            sage: G.Q_chain()
            [word: , word: 1, word: 10, word: 101, word: 1011]

        Check that :issue:`25631` is fixed::

            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: BinaryWord(filling = {}).Q_chain()
            [word: ]
        """
    def is_rectangular(self):
        """
        Return ``True`` if the shape of the growth diagram is rectangular.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: GrowthDiagram(RuleRSK, [2,3,1]).is_rectangular()
            True
            sage: GrowthDiagram(RuleRSK, [[1,0,1],[0,1]]).is_rectangular()
            False
        """
    def to_word(self):
        """
        Return the filling as a word, if the shape is rectangular and
        there is at most one nonzero entry in each column, which must
        be 1.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: w = [3,3,2,4,1]; G = GrowthDiagram(RuleRSK, w)
            sage: G
            0  0  0  0  1
            0  0  1  0  0
            1  1  0  0  0
            0  0  0  1  0
            sage: G.to_word()
            [3, 3, 2, 4, 1]
        """
    def to_biword(self):
        """
        Return the filling as a biword, if the shape is rectangular.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: P = Tableau([[1,2,2],[2]])
            sage: Q = Tableau([[1,3,3],[2]])
            sage: bw = RSK_inverse(P, Q); bw
            [[1, 2, 3, 3], [2, 1, 2, 2]]
            sage: G = GrowthDiagram(RuleRSK, labels=Q.to_chain()[:-1]+P.to_chain()[::-1]); G
            0  1  0
            1  0  2

            sage: P = SemistandardTableau([[1, 1, 2], [2]])
            sage: Q = SemistandardTableau([[1, 2, 2], [2]])
            sage: G = GrowthDiagram(RuleRSK, labels=Q.to_chain()[:-1]+P.to_chain()[::-1]); G
            0  2
            1  1
            sage: G.to_biword()
            ([1, 2, 2, 2], [2, 1, 1, 2])
            sage: RSK([1, 2, 2, 2], [2, 1, 1, 2])
            [[[1, 1, 2], [2]], [[1, 2, 2], [2]]]
        """
    def __iter__(self):
        """
        Return the rows of the filling.

        TESTS::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = GrowthDiagram(RuleRSK, {(0,1):1, (1,0):1}, SkewPartition([[2,1],[1]]))
            sage: list(G)
            [[None, 1], [1]]

            sage: pi = Permutation([2,3,1,6,4,5])
            sage: G = GrowthDiagram(RuleRSK, pi)
            sage: list(G)
            [[0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1],
             [0, 0, 0, 1, 0, 0]]
        """
    def __eq__(self, other):
        """
        Return ``True`` if the growth diagram ``other`` has the same
        shape and the same filling as ``self``.

        EXAMPLES:

        Equality ignores zeros in fillings::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G1 = GrowthDiagram(RuleRSK, {(0, 1): 1, (1, 0): 1})
            sage: G2 = GrowthDiagram(RuleRSK, {(0, 0): 0, (0, 1): 1, (1, 0): 1})
            sage: G1 == G2
            True

        Growth diagrams with different shapes are different::

            sage: G1 = GrowthDiagram(RuleRSK, [[0,1,0],[1,0]])
            sage: G2 = GrowthDiagram(RuleRSK, [[0,1,0],[1]])
            sage: G1 == G2
            False

        Growth diagrams with different rules are different::

            sage: G1 = GrowthDiagram(RuleRSK, {(0, 1): 1, (1, 0): 1})
            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: G2 = GrowthDiagram(BinaryWord, {(0, 1): 1, (1, 0): 1})
            sage: G1 == G2
            False
        """
    def __ne__(self, other):
        """
        Return ``True`` if the growth diagram ``other`` does not have the
        same shape and the same filling as ``self``.

        TESTS:

        Equality ignores zeros in fillings::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G1 = GrowthDiagram(RuleRSK, {(0, 1): 1, (1, 0): 1})
            sage: G2 = GrowthDiagram(RuleRSK, {(0, 0): 0, (0, 1): 1, (1, 0): 1})
            sage: G1 != G2
            False

        Growth diagrams with different shapes are different::

            sage: G1 = GrowthDiagram(RuleRSK, [[0,1,0],[1,0]])
            sage: G2 = GrowthDiagram(RuleRSK, [[0,1,0],[1]])
            sage: G1 != G2
            True

        Growth diagrams with different rules are different::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: G1 = GrowthDiagram(RuleRSK, {(0, 1): 1, (1, 0): 1})
            sage: G2 = GrowthDiagram(BinaryWord, {(0, 1): 1, (1, 0): 1})
            sage: G1 != G2
            True
        """

class Rule(UniqueRepresentation):
    """
    Generic base class for a rule for a growth diagram.

    Subclasses may provide the following attributes:

    - ``zero`` -- the zero element of the vertices of the graphs

    - ``r`` -- (default: 1) the parameter in the equation `DU - UD = rI`

    - ``has_multiple_edges`` -- boolean (default: ``False``); if the dual
      graded graph has multiple edges and therefore edges are
      triples consisting of two vertices and a label

    - ``zero_edge`` -- (default: 0) the zero label of the
      edges of the graphs used for degenerate edges.  It is
      allowed to use this label also for other edges.

    Subclasses may provide the following methods:

    - ``normalize_vertex`` -- a function that converts its input to a
      vertex

    - ``vertices`` -- a function that takes a nonnegative integer
      as input and returns the list of vertices on this rank

    - ``rank`` -- the rank function of the dual graded graphs

    - ``forward_rule`` -- a function with input ``(y, t, x,
      content)`` or ``(y, e, t, f, x, content)`` if
      ``has_multiple_edges`` is ``True``.  ``(y, e, t)`` is an
      edge in the graph `P`, ``(t, f, x)`` an edge in the graph
      ``Q``.  It should return the fourth vertex ``z``, or, if
      ``has_multiple_edges`` is ``True``, the path ``(g, z, h)``
      from ``y`` to ``x``.

    - ``backward_rule`` -- a function with input ``(y, z, x)`` or
      ``(y, g, z, h, x)`` if ``has_multiple_edges`` is ``True``.
      ``(y, g, z)`` is an edge in the graph `Q`, ``(z, h, x)`` an
      edge in the graph ``P``.  It should return the fourth
      vertex and the content ``(t, content)``, or, if
      ``has_multiple_edges`` is ``True``, the path from ``y`` to
      ``x`` and the content as ``(e, t, f, content)``.

    - ``is_P_edge``, ``is_Q_edge`` -- functions that take two
      vertices as arguments and return ``True`` or ``False``, or,
      if multiple edges are allowed, the list of edge labels of
      the edges from the first vertex to the second in the
      respective graded graph.  These are only used for checking
      user input and providing the dual graded graph, and are
      therefore not mandatory.

    Note that the class :class:`GrowthDiagram` is able to use
    partially implemented subclasses just fine.  Suppose that
    ``MyRule`` is such a subclass.  Then:

    - ``GrowthDiagram(MyRule, my_filling)`` requires only an
      implementation of ``forward_rule``, ``zero`` and possibly
      ``has_multiple_edges``.

    - ``GrowthDiagram(MyRule, labels=my_labels, shape=my_shape)``
      requires only an implementation of ``backward_rule`` and
      possibly ``has_multiple_edges``, provided that the labels
      ``my_labels`` are given as needed by ``backward_rule``.

    - ``GrowthDiagram(MyRule, labels=my_labels)`` additionally needs
      an implementation of ``rank`` to deduce the shape.

    In particular, this allows to implement rules which do not quite
    fit Fomin's notion of dual graded graphs.  An example would be
    Bloom and Saracino's variant of the RSK correspondence [BS2012]_,
    where a backward rule is not available.

    Similarly:

    - ``MyRule.P_graph`` only requires an implementation of
      ``vertices``, ``is_P_edge`` and possibly ``has_multiple_edges``
      is required, mutatis mutandis for ``MyRule.Q_graph``.

    - ``MyRule._check_duality`` requires ``P_graph`` and ``Q_graph``.

    In particular, this allows to work with dual graded graphs
    without local rules.
    """
    has_multiple_edges: bool
    zero_edge: int
    r: int
    def normalize_vertex(self, v):
        '''
        Return ``v`` as a vertex of the dual graded graph.

        This is a default implementation, returning its argument.

        EXAMPLES::

            sage: from sage.combinat.growth import Rule
            sage: Rule().normalize_vertex("hello") == "hello"
            True
        '''
    def __call__(self, *args, **kwds):
        """
        Return the growth diagram corresponding to the parameters.

        This provides a shorthand for calling :class:`GrowthDiagram`
        directly.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: RuleRSK([2,3,1], shape=[3,2,2])
            0  0  1
            1  0
            0  1

            sage: RuleRSK(labels=[[], [1], [2], [1], [], [1], []])
            0  0  1
            1  0
            0  1
        """
    def P_graph(self, n):
        """
        Return the first ``n`` levels of the first dual graded graph.

        The non-degenerate edges in the vertical direction come from
        this graph.

        EXAMPLES::

            sage: Domino = GrowthDiagram.rules.Domino()
            sage: Domino.P_graph(3)
            Finite poset containing 8 elements
        """
    def Q_graph(self, n):
        """
        Return the first ``n`` levels of the second dual graded graph.

        The non-degenerate edges in the horizontal direction come
        from this graph.

        EXAMPLES::

            sage: Domino = GrowthDiagram.rules.Domino()
            sage: Q = Domino.Q_graph(3); Q
            Finite poset containing 8 elements

            sage: Q.upper_covers(Partition([1,1]))
            [[1, 1, 1, 1], [3, 1], [2, 2]]
        """

class RuleShiftedShapes(Rule):
    """
    A class modelling the Schensted correspondence for shifted
    shapes.

    This agrees with Sagan [Sag1987]_ and Worley's [Wor1984]_, and
    Haiman's [Hai1989]_ insertion algorithms, see Proposition 4.5.2
    of [Fom1995]_.

    EXAMPLES::

        sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
        sage: GrowthDiagram(Shifted, [3,1,2])
        0  1  0
        0  0  1
        1  0  0

    The vertices of the dual graded graph are shifted shapes::

        sage: Shifted.vertices(3)
        Partitions of the integer 3 satisfying constraints max_slope=-1

    Let us check the example just before Corollary 3.2 in [Sag1987]_.
    Note that, instead of passing the rule to :class:`GrowthDiagram`,
    we can also call the rule to create growth diagrams::

        sage: G = Shifted([2,6,5,1,7,4,3])
        sage: G.P_chain()
        [[], 0, [1], 0, [2], 0, [3], 0, [3, 1], 0, [3, 2], 0, [4, 2], 0, [5, 2]]
        sage: G.Q_chain()
        [[], 1, [1], 2, [2], 1, [2, 1], 3, [3, 1], 2, [4, 1], 3, [4, 2], 3, [5, 2]]

    TESTS::

        sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
        sage: Shifted.zero
        []

        sage: Shifted._check_duality(4)

    Check that the rules are bijective::

        sage: all(Shifted(labels=Shifted(pi).out_labels()).to_word() == pi
        ....:     for pi in Permutations(5))
        True
        sage: pi = Permutations(10).random_element()
        sage: G = Shifted(pi)
        sage: list(Shifted(labels=G.out_labels())) == list(G)
        True
    """
    zero: Incomplete
    has_multiple_edges: bool
    def normalize_vertex(self, v):
        """
        Return ``v`` as a partition.

        EXAMPLES::

            sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
            sage: Shifted.normalize_vertex([3,1]).parent()
            Partitions
        """
    def vertices(self, n):
        """
        Return the vertices of the dual graded graph on level ``n``.

        EXAMPLES::

            sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
            sage: Shifted.vertices(3)
            Partitions of the integer 3 satisfying constraints max_slope=-1
        """
    def rank(self, v):
        """
        Return the rank of ``v``: the size of the shifted partition.

        EXAMPLES::

            sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
            sage: Shifted.rank(Shifted.vertices(3)[0])
            3
        """
    def is_Q_edge(self, v, w):
        """
        Return whether ``(v, w)`` is a `Q`-edge of ``self``.

        ``(v, w)`` is an edge if ``w`` is obtained from ``v`` by adding a
        cell.  It is a black (color 1) edge, if the cell is on the
        diagonal, otherwise it can be blue or red (color 2 or 3).

        EXAMPLES::

            sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
            sage: v = Shifted.vertices(2)[0]; v
            [2]
            sage: [(w, Shifted.is_Q_edge(v, w)) for w in Shifted.vertices(3)]
            [([3], [2, 3]), ([2, 1], [1])]
            sage: all(Shifted.is_Q_edge(v, w) == [] for w in Shifted.vertices(4))
            True
        """
    def is_P_edge(self, v, w):
        """
        Return whether ``(v, w)`` is a `P`-edge of ``self``.

        ``(v, w)`` is an edge if ``w`` contains ``v``.

        EXAMPLES::

            sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
            sage: v = Shifted.vertices(2)[0]; v
            [2]
            sage: [w for w in Shifted.vertices(3) if Shifted.is_P_edge(v, w)]
            [[3], [2, 1]]
        """
    def P_symbol(self, P_chain):
        """
        Return the labels along the vertical boundary of a rectangular
        growth diagram as a shifted tableau.

        EXAMPLES:

        Check the example just before Corollary 3.2 in [Sag1987]_::

            sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
            sage: G = Shifted([2,6,5,1,7,4,3])
            sage: G.P_symbol().pp()
            1  2  3  6  7
               4  5

        Check the example just before Corollary 8.2 in [SS1990]_::

            sage: T = ShiftedPrimedTableau([[4],[1],[5]], skew=[3,1])
            sage: T.pp()
             .  .  .  4
                .  1
                   5
            sage: U = ShiftedPrimedTableau([[1],[3.5],[5]], skew=[3,1])
            sage: U.pp()
             .  .  .  1
                .  4'
                   5
            sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
            sage: labels = [mu if is_even(i) else 0
            ....:           for i, mu in enumerate(T.to_chain()[::-1])] + U.to_chain()[1:]
            sage: G = Shifted({(1,2):1, (2,1):1}, shape=[5,5,5,5,5], labels=labels)
            sage: G.P_symbol().pp()
             .  .  .  .  2
                .  .  1  3
                   .  4  5
        """
    def Q_symbol(self, Q_chain):
        """
        Return the labels along the horizontal boundary of a rectangular
        growth diagram as a skew tableau.

        EXAMPLES:

        Check the example just before Corollary 3.2 in [Sag1987]_::

            sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
            sage: G = Shifted([2,6,5,1,7,4,3])
            sage: G.Q_symbol().pp()
            1  2  4' 5  7'
               3  6'

        Check the example just before Corollary 8.2 in [SS1990]_::

            sage: T = ShiftedPrimedTableau([[4],[1],[5]], skew=[3,1])
            sage: T.pp()
             .  .  .  4
                .  1
                   5
            sage: U = ShiftedPrimedTableau([[1],[3.5],[5]], skew=[3,1])
            sage: U.pp()
             .  .  .  1
                .  4'
                   5
            sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
            sage: labels = [mu if is_even(i) else 0
            ....:           for i, mu in enumerate(T.to_chain()[::-1])] + U.to_chain()[1:]
            sage: G = Shifted({(1,2):1, (2,1):1}, shape=[5,5,5,5,5], labels=labels)
            sage: G.Q_symbol().pp()
             .  .  .  .  2
                .  .  1  4'
                   .  3' 5'
        """
    def forward_rule(self, y, e, t, f, x, content):
        """
        Return the output path given two incident edges and the content.

        See [Fom1995]_ Lemma 4.5.1, page 38.

        INPUT:

        - ``y``, ``e``, ``t``, ``f``, ``x`` -- a path of three partitions and
          two colors from a cell in a growth diagram, labelled as::

              t f x
              e
              y

        - ``content`` -- `0` or `1`; the content of the cell

        OUTPUT:

        The two colors and the fourth partition ``g``, ``z``, ``h``
        according to Sagan-Worley insertion.

        EXAMPLES::

            sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
            sage: Shifted.forward_rule([], 0, [], 0, [], 1)
            (1, [1], 0)

            sage: Shifted.forward_rule([1], 0, [1], 0, [1], 1)
            (2, [2], 0)

        if ``x != y``::

            sage: Shifted.forward_rule([3], 0, [2], 1, [2,1], 0)
            (1, [3, 1], 0)

            sage: Shifted.forward_rule([2,1], 0, [2], 2, [3], 0)
            (2, [3, 1], 0)

        if ``x == y != t``::

            sage: Shifted.forward_rule([3], 0, [2], 2, [3], 0)
            (1, [3, 1], 0)

            sage: Shifted.forward_rule([3,1], 0, [2,1], 2, [3,1], 0)
            (2, [3, 2], 0)

            sage: Shifted.forward_rule([2,1], 0, [2], 1, [2,1], 0)
            (3, [3, 1], 0)

            sage: Shifted.forward_rule([3], 0, [2], 3, [3], 0)
            (3, [4], 0)
        """
    def backward_rule(self, y, g, z, h, x):
        """
        Return the input path and the content given two incident edges.

        See [Fom1995]_ Lemma 4.5.1, page 38.

        INPUT:

        - ``y``, ``g``, ``z``, ``h``, ``x`` -- a path of three partitions and
          two colors from a cell in a growth diagram, labelled as::

                  x
                  h
              y g z

        OUTPUT:

        A tuple ``(e, t, f, content)`` consisting of the shape ``t``
        of the fourth word, the colours of the incident edges and the
        content of the cell according to Sagan - Worley insertion.

        EXAMPLES::

            sage: Shifted = GrowthDiagram.rules.ShiftedShapes()
            sage: Shifted.backward_rule([], 1, [1], 0, [])
            (0, [], 0, 1)

            sage: Shifted.backward_rule([1], 2, [2], 0, [1])
            (0, [1], 0, 1)

        if ``x != y``::

            sage: Shifted.backward_rule([3], 1, [3, 1], 0, [2,1])
            (0, [2], 1, 0)

            sage: Shifted.backward_rule([2,1], 2, [3, 1], 0, [3])
            (0, [2], 2, 0)

        if ``x == y != t``::

            sage: Shifted.backward_rule([3], 1, [3, 1], 0, [3])
            (0, [2], 2, 0)

            sage: Shifted.backward_rule([3,1], 2, [3, 2], 0, [3,1])
            (0, [2, 1], 2, 0)

            sage: Shifted.backward_rule([2,1], 3, [3, 1], 0, [2,1])
            (0, [2], 1, 0)

            sage: Shifted.backward_rule([3], 3, [4], 0, [3])
            (0, [2], 3, 0)
        """

class RuleLLMS(Rule):
    """
    A rule modelling the Schensted correspondence for affine
    permutations.

    EXAMPLES::

        sage: LLMS3 = GrowthDiagram.rules.LLMS(3)
        sage: GrowthDiagram(LLMS3, [3,1,2])
        0  1  0
        0  0  1
        1  0  0

    The vertices of the dual graded graph are
    :class:`~sage.combinat.core.Cores`::

        sage: LLMS3.vertices(4)
        3-Cores of length 4

    Let us check example of Figure 1 in [LS2007]_.  Note that,
    instead of passing the rule to :class:`GrowthDiagram`, we can
    also call the rule to create growth diagrams::

        sage: G = LLMS3([4,1,2,6,3,5]); G
        0  1  0  0  0  0
        0  0  1  0  0  0
        0  0  0  0  1  0
        1  0  0  0  0  0
        0  0  0  0  0  1
        0  0  0  1  0  0

    The :meth:`P_symbol` is a
    :class:`~sage.combinat.k_tableau.StrongTableau`::

        sage: G.P_symbol().pp()
        -1 -2 -3 -5
         3  5
        -4 -6
         5
         6

    The :meth:`Q_symbol` is a
    :class:`~sage.combinat.k_tableau.WeakTableau`::

        sage: G.Q_symbol().pp()
        1  3  4  5
        2  5
        3  6
        5
        6

    Let us also check Example 6.2 in [LLMSSZ2013]_::

        sage: G = LLMS3([4,1,3,2])
        sage: G.P_symbol().pp()
        -1 -2  3
        -3
        -4

        sage: G.Q_symbol().pp()
        1  3  4
        2
        3

    TESTS::

        sage: LLMS3 = GrowthDiagram.rules.LLMS(3)
        sage: LLMS3.zero
        []
    """
    zero_edge: Incomplete
    has_multiple_edges: bool
    k: Incomplete
    zero: Incomplete
    def __init__(self, k) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: LLMS3 = GrowthDiagram.rules.LLMS(3)
            sage: TestSuite(LLMS3).run()
        """
    def normalize_vertex(self, v):
        """
        Convert ``v`` to a `k`-core.

        EXAMPLES::

            sage: LLMS3 = GrowthDiagram.rules.LLMS(3)
            sage: LLMS3.normalize_vertex([3,1]).parent()
            3-Cores of length 3
        """
    def rank(self, v):
        """
        Return the rank of ``v``: the length of the core.

        EXAMPLES::

            sage: LLMS3 = GrowthDiagram.rules.LLMS(3)
            sage: LLMS3.rank(LLMS3.vertices(3)[0])
            3
        """
    def vertices(self, n):
        """
        Return the vertices of the dual graded graph on level ``n``.

        EXAMPLES::

            sage: LLMS3 = GrowthDiagram.rules.LLMS(3)
            sage: LLMS3.vertices(2)
            3-Cores of length 2
        """
    def is_Q_edge(self, v, w):
        """
        Return whether ``(v, w)`` is a `Q`-edge of ``self``.

        ``(v, w)`` is an edge if ``w`` is a weak cover of ``v``, see
        :meth:`~sage.combinat.core.Core.weak_covers()`.

        EXAMPLES::

            sage: LLMS4 = GrowthDiagram.rules.LLMS(4)
            sage: v = LLMS4.vertices(3)[1]; v
            [2, 1]
            sage: [w for w in LLMS4.vertices(4) if len(LLMS4.is_Q_edge(v, w)) > 0]
            [[2, 2], [3, 1, 1]]
            sage: all(LLMS4.is_Q_edge(v, w) == [] for w in LLMS4.vertices(5))
            True
        """
    def is_P_edge(self, v, w):
        """
        Return whether ``(v, w)`` is a `P`-edge of ``self``.

        For two k-cores v and w containing v, there are as many edges as
        there are components in the skew partition w/v.  These
        components are ribbons, and therefore contain a unique cell
        with maximal content.  We index the edge with this content.

        EXAMPLES::

            sage: LLMS4 = GrowthDiagram.rules.LLMS(4)
            sage: v = LLMS4.vertices(2)[0]; v
            [2]
            sage: [(w, LLMS4.is_P_edge(v, w)) for w in LLMS4.vertices(3)]
            [([3], [2]), ([2, 1], [-1]), ([1, 1, 1], [])]
            sage: all(LLMS4.is_P_edge(v, w) == [] for w in LLMS4.vertices(4))
            True
        """
    def P_symbol(self, P_chain):
        """
        Return the labels along the vertical boundary of a
        rectangular growth diagram as a skew
        :class:`~sage.combinat.k_tableau.StrongTableau`.

        EXAMPLES::

            sage: LLMS4 = GrowthDiagram.rules.LLMS(4)
            sage: G = LLMS4([3,4,1,2])
            sage: G.P_symbol().pp()
            -1 -2
            -3 -4
        """
    def Q_symbol(self, Q_chain):
        """
        Return the labels along the horizontal boundary of a
        rectangular growth diagram as a skew
        :class:`~sage.combinat.k_tableau.WeakTableau`.

        EXAMPLES::

            sage: LLMS4 = GrowthDiagram.rules.LLMS(4)
            sage: G = LLMS4([3,4,1,2])
            sage: G.Q_symbol().pp()
            1 2
            3 4
        """
    def forward_rule(self, y, e, t, f, x, content):
        """
        Return the output path given two incident edges and the content.

        See [LS2007]_ Section 3.4 and [LLMSSZ2013]_ Section 6.3.

        INPUT:

        - ``y``, ``e``, ``t``, ``f``, ``x`` -- a path of three partitions and
          two colors from a cell in a growth diagram, labelled as::

              t f x
              e
              y

        - ``content`` -- `0` or `1`; the content of the cell

        OUTPUT:

        The two colors and the fourth partition g, z, h according to
        LLMS insertion.

        EXAMPLES::

            sage: LLMS3 = GrowthDiagram.rules.LLMS(3)
            sage: LLMS4 = GrowthDiagram.rules.LLMS(4)

            sage: Z = LLMS3.zero
            sage: LLMS3.forward_rule(Z, None, Z, None, Z, 0)
            (None, [], None)

            sage: LLMS3.forward_rule(Z, None, Z, None, Z, 1)
            (None, [1], 0)

            sage: Y = Core([3,1,1], 3)
            sage: LLMS3.forward_rule(Y, None, Y, None, Y, 1)
            (None, [4, 2, 1, 1], 3)

        if ``x != y``::

            sage: Y = Core([1,1], 3); T = Core([1], 3); X = Core([2], 3)
            sage: LLMS3.forward_rule(Y, -1, T, None, X, 0)
            (None, [2, 1, 1], -1)

            sage: Y = Core([2], 4); T = Core([1], 4); X = Core([1,1], 4)
            sage: LLMS4.forward_rule(Y, 1, T, None, X, 0)
            (None, [2, 1], 1)

            sage: Y = Core([2,1,1], 3); T = Core([2], 3); X = Core([3,1], 3)
            sage: LLMS3.forward_rule(Y, -1, T, None, X, 0)
            (None, [3, 1, 1], -2)

        if ``x == y != t``::

            sage: Y = Core([1], 3); T = Core([], 3); X = Core([1], 3)
            sage: LLMS3.forward_rule(Y, 0, T, None, X, 0)
            (None, [1, 1], -1)

            sage: Y = Core([1], 4); T = Core([], 4); X = Core([1], 4)
            sage: LLMS4.forward_rule(Y, 0, T, None, X, 0)
            (None, [1, 1], -1)

            sage: Y = Core([2,1], 4); T = Core([1,1], 4); X = Core([2,1], 4)
            sage: LLMS4.forward_rule(Y, 1, T, None, X, 0)
            (None, [2, 2], 0)
        """

class RuleBinaryWord(Rule):
    """
    A rule modelling a Schensted-like correspondence for binary words.

    EXAMPLES::

        sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
        sage: GrowthDiagram(BinaryWord, [3,1,2])
        0  1  0
        0  0  1
        1  0  0

    The vertices of the dual graded graph are binary words::

        sage: BinaryWord.vertices(3)
        [word: 100, word: 101, word: 110, word: 111]

    Note that, instead of passing the rule to :class:`GrowthDiagram`,
    we can also use call the rule to create growth diagrams.  For
    example::

        sage: BinaryWord([2,4,1,3]).P_chain()
        [word: , word: 1, word: 10, word: 101, word: 1101]
        sage: BinaryWord([2,4,1,3]).Q_chain()
        [word: , word: 1, word: 11, word: 110, word: 1101]

    The Kleitman Greene invariant is the descent word, encoded by the
    positions of the zeros::

        sage: pi = Permutation([4,1,8,3,6,5,2,7,9])
        sage: G = BinaryWord(pi); G
        0  1  0  0  0  0  0  0  0
        0  0  0  0  0  0  1  0  0
        0  0  0  1  0  0  0  0  0
        1  0  0  0  0  0  0  0  0
        0  0  0  0  0  1  0  0  0
        0  0  0  0  1  0  0  0  0
        0  0  0  0  0  0  0  1  0
        0  0  1  0  0  0  0  0  0
        0  0  0  0  0  0  0  0  1
        sage: pi.descents()
        [1, 3, 5, 6]

    TESTS::

        sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
        sage: BinaryWord.zero
        word:
        sage: G = BinaryWord(labels=[[1,1],[1,1,0],[0,1]])
        Traceback (most recent call last):
        ...
        ValueError: 01 has smaller rank than 110 but is not covered by it in P

        sage: G = BinaryWord(labels=[[1,1],[1,0,1],[0,1]])
        Traceback (most recent call last):
        ...
        ValueError: 11 has smaller rank than 101 but is not covered by it in Q

    Check duality::

        sage: BinaryWord._check_duality(4)

    Check that the rules are bijective::

        sage: all(BinaryWord(labels=BinaryWord(pi).out_labels()).to_word()
        ....:      == pi for pi in Permutations(4))
        True
        sage: pi = Permutations(10).random_element()
        sage: G = BinaryWord(pi)
        sage: list(BinaryWord(labels=G.out_labels())) == list(G)
        True

    Test that the Kleitman Greene invariant is indeed the descent word::

        sage: r = 4
        sage: all(Word([0 if i in w.descents() else 1 for i in range(r)])
        ....:      == BinaryWord(w).out_labels()[r]
        ....:     for w in Permutations(r))
        True
    """
    zero: Incomplete
    def normalize_vertex(self, v):
        """
        Return ``v`` as a binary word.

        EXAMPLES::

            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: BinaryWord.normalize_vertex([0,1]).parent()
            Finite words over {0, 1}
        """
    def vertices(self, n):
        """
        Return the vertices of the dual graded graph on level ``n``.

        EXAMPLES::

            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: BinaryWord.vertices(3)
            [word: 100, word: 101, word: 110, word: 111]
        """
    def rank(self, v):
        """
        Return the rank of ``v``: number of letters of the word.

        EXAMPLES::

            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: BinaryWord.rank(BinaryWord.vertices(3)[0])
            3
        """
    def is_Q_edge(self, v, w):
        """
        Return whether ``(v, w)`` is a `Q`-edge of ``self``.

        ``(w, v)`` is an edge if ``w`` is obtained from ``v`` by
        appending a letter.

        EXAMPLES::

            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: v = BinaryWord.vertices(2)[0]; v
            word: 10
            sage: [w for w in BinaryWord.vertices(3) if BinaryWord.is_Q_edge(v, w)]
            [word: 100, word: 101]
            sage: [w for w in BinaryWord.vertices(4) if BinaryWord.is_Q_edge(v, w)]
            []
        """
    def is_P_edge(self, v, w):
        """
        Return whether ``(v, w)`` is a `P`-edge of ``self``.

        ``(v, w)`` is an edge if ``v`` is obtained from ``w`` by
        deleting a letter.

        EXAMPLES::

            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: v = BinaryWord.vertices(2)[1]; v
            word: 11
            sage: [w for w in BinaryWord.vertices(3) if BinaryWord.is_P_edge(v, w)]
            [word: 101, word: 110, word: 111]
            sage: [w for w in BinaryWord.vertices(4) if BinaryWord.is_P_edge(v, w)]
            []
        """
    def forward_rule(self, y, t, x, content):
        """
        Return the output shape given three shapes and the content.

        See [Fom1995]_ Lemma 4.6.1, page 40.

        INPUT:

        - ``y``, ``t``, ``x`` -- three binary words from a cell in a growth
          diagram, labelled as::

              t x
              y

        - ``content`` -- `0` or `1`; the content of the cell

        OUTPUT:

        The fourth binary word ``z`` according to Viennot's
        bijection [Vie1983]_.

        EXAMPLES::

            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()

            sage: BinaryWord.forward_rule([], [], [], 1)
            word: 1

            sage: BinaryWord.forward_rule([1], [1], [1], 1)
            word: 11

        if ``x != y`` append last letter of ``x`` to ``y``::

            sage: BinaryWord.forward_rule([1,0], [1], [1,1], 0)
            word: 101

        if ``x == y != t`` append ``0`` to ``y``::

            sage: BinaryWord.forward_rule([1,1], [1], [1,1], 0)
            word: 110
        """
    def backward_rule(self, y, z, x):
        """
        Return the content and the input shape.

        See [Fom1995]_ Lemma 4.6.1, page 40.

        - ``y``, ``z``, ``x`` -- three binary words from a cell in a growth diagram,
          labelled as::

                x
              y z

        OUTPUT:

        A pair ``(t, content)`` consisting of the shape of the fourth
        word and the content of the cell according to Viennot's
        bijection [Vie1983]_.

        TESTS::

            sage: BinaryWord = GrowthDiagram.rules.BinaryWord()
            sage: w = [4,1,8,3,6,5,2,7,9]; G = GrowthDiagram(BinaryWord, w)
            sage: BinaryWord(labels=G.out_labels()).to_word() == w  # indirect doctest
            True
        """

class RuleSylvester(Rule):
    """
    A rule modelling a Schensted-like correspondence for binary trees.

    EXAMPLES::

        sage: Sylvester = GrowthDiagram.rules.Sylvester()
        sage: GrowthDiagram(Sylvester, [3,1,2])
        0  1  0
        0  0  1
        1  0  0

    The vertices of the dual graded graph are
    :class:`~sage.combinat.binary_tree.BinaryTrees`::

        sage: Sylvester.vertices(3)
        Binary trees of size 3

    The :meth:`~sage.combinat.growth.Rule.P_graph` is also known as
    the bracket tree, the :meth:`~sage.combinat.growth.Rule.Q_graph`
    is the lattice of finite order ideals of the infinite binary
    tree, see Example 2.4.6 in [Fom1994]_.

    For a permutation, the :meth:`P_symbol` is the binary search
    tree, the :meth:`Q_symbol` is the increasing tree corresponding
    to the inverse permutation.  Note that, instead of passing the
    rule to :class:`GrowthDiagram`, we can also call the rule to
    create growth diagrams.  From [Nze2007]_::

        sage: pi = Permutation([3,5,1,4,2,6]); G = Sylvester(pi); G
        0  0  1  0  0  0
        0  0  0  0  1  0
        1  0  0  0  0  0
        0  0  0  1  0  0
        0  1  0  0  0  0
        0  0  0  0  0  1
        sage: ascii_art(G.P_symbol())
          __3__
         /     \\\n        1       5
         \\     / \\\n          2   4   6
        sage: ascii_art(G.Q_symbol())
          __1__
         /     \\\n        3       2
         \\     / \\\n          5   4   6

        sage: all(Sylvester(pi).P_symbol() == pi.binary_search_tree()
        ....:     for pi in Permutations(5))
        True

        sage: all(Sylvester(pi).Q_symbol() == pi.inverse().increasing_tree()
        ....:     for pi in Permutations(5))
        True

    TESTS::

        sage: Sylvester.zero
        .

        sage: B = BinaryTree; R = B([None,[]]); L = B([[],None])
        sage: T = B([[],[]]); S = B([L,None])
        sage: G = Sylvester(labels=[R, T, R])
        Traceback (most recent call last):
        ...
        ValueError: [., [., .]] has smaller rank than [[., .], [., .]]
         but is not covered by it in P

        sage: G = Sylvester(labels=[R, S, R])
        Traceback (most recent call last):
        ...
        ValueError: [., [., .]] has smaller rank than [[[., .], .], .]
         but is not covered by it in Q

    Check duality::

        sage: Sylvester._check_duality(4)

    Check that the rules are bijective::

        sage: all(Sylvester(labels=GrowthDiagram(Sylvester, pi).out_labels()).to_word()
        ....:      == pi for pi in Permutations(4))
        True
        sage: pi = Permutations(10).random_element()
        sage: G = GrowthDiagram(Sylvester, pi)
        sage: list(Sylvester(labels=G.out_labels())) == list(G)
        True
    """
    zero: Incomplete
    def normalize_vertex(self, v):
        """
        Return ``v`` as a binary tree.

        EXAMPLES::

            sage: Sylvester = GrowthDiagram.rules.Sylvester()
            sage: Sylvester.normalize_vertex([[],[]]).parent()
            Binary trees
        """
    def vertices(self, n):
        """
        Return the vertices of the dual graded graph on level ``n``.

        EXAMPLES::

            sage: Sylvester = GrowthDiagram.rules.Sylvester()
            sage: Sylvester.vertices(3)
            Binary trees of size 3
        """
    def rank(self, v):
        """
        Return the rank of ``v``: the number of nodes of the tree.

        EXAMPLES::

            sage: Sylvester = GrowthDiagram.rules.Sylvester()
            sage: Sylvester.rank(Sylvester.vertices(3)[0])
            3
        """
    def is_Q_edge(self, v, w):
        """
        Return whether ``(v, w)`` is a `Q`-edge of ``self``.

        ``(v, w)`` is an edge if ``v`` is a sub-tree of ``w`` with one
        node less.

        EXAMPLES::

            sage: Sylvester = GrowthDiagram.rules.Sylvester()
            sage: v = Sylvester.vertices(2)[1]; ascii_art(v)
              o
             /
            o
            sage: ascii_art([w for w in Sylvester.vertices(3) if Sylvester.is_Q_edge(v, w)])
            [   o  ,   o,     o ]
            [  / \\    /      /  ]
            [ o   o  o      o   ]
            [         \\    /    ]
            [          o  o     ]
            sage: [w for w in Sylvester.vertices(4) if Sylvester.is_Q_edge(v, w)]
            []
        """
    def is_P_edge(self, v, w):
        """
        Return whether ``(v, w)`` is a `P`-edge of ``self``.

        ``(v, w)`` is an edge if ``v`` is obtained from ``w`` by deleting
        its right-most node.

        EXAMPLES::

            sage: Sylvester = GrowthDiagram.rules.Sylvester()
            sage: v = Sylvester.vertices(2)[1]; ascii_art(v)
              o
             /
            o

            sage: ascii_art([w for w in Sylvester.vertices(3) if Sylvester.is_P_edge(v, w)])
            [   o  ,     o ]
            [  / \\      /  ]
            [ o   o    o   ]
            [         /    ]
            [        o     ]

            sage: [w for w in Sylvester.vertices(4) if Sylvester.is_P_edge(v, w)]
            []
        """
    def P_symbol(self, P_chain):
        """
        Return the labels along the vertical boundary of a rectangular
        growth diagram as a labelled binary tree.

        For permutations, this coincides with the binary search tree.

        EXAMPLES::

            sage: Sylvester = GrowthDiagram.rules.Sylvester()
            sage: pi = Permutation([2,4,3,1])
            sage: ascii_art(Sylvester(pi).P_symbol())
              _2_
             /   \\\n            1     4
                 /
                3
            sage: Sylvester(pi).P_symbol() == pi.binary_search_tree()
            True

        We can also do the skew version::

            sage: B = BinaryTree; E = B(); N = B([])
            sage: ascii_art(Sylvester([3,2], shape=[3,3,3], labels=[N,N,N,E,E,E,N]).P_symbol())
              __1___
             /      \\\n            None     3
                    /
                   2
        """
    def Q_symbol(self, Q_chain):
        """
        Return the labels along the vertical boundary of a rectangular
        growth diagram as a labelled binary tree.

        For permutations, this coincides with the increasing tree.

        EXAMPLES::

            sage: Sylvester = GrowthDiagram.rules.Sylvester()
            sage: pi = Permutation([2,4,3,1])
            sage: ascii_art(Sylvester(pi).Q_symbol())
              _1_
             /   \\\n            4     2
                 /
                3
            sage: Sylvester(pi).Q_symbol() == pi.inverse().increasing_tree()
            True

        We can also do the skew version::

            sage: B = BinaryTree; E = B(); N = B([])
            sage: ascii_art(Sylvester([3,2], shape=[3,3,3], labels=[N,N,N,E,E,E,N]).Q_symbol())
              _None_
             /      \\\n            3        1
                    /
                   2
        """
    def forward_rule(self, y, t, x, content):
        """
        Return the output shape given three shapes and the content.

        See [Nze2007]_, page 9.

        INPUT:

        - ``y``, ``t``, ``x`` -- three binary trees from a cell in a growth
          diagram, labelled as::

              t x
              y

        - ``content`` -- `0` or `1`; the content of the cell

        OUTPUT: the fourth binary tree ``z``

        EXAMPLES::

            sage: Sylvester = GrowthDiagram.rules.Sylvester()
            sage: B = BinaryTree; E = B(); N = B([]); L = B([[],None])
            sage: R = B([None,[]]); T = B([[],[]])

            sage: ascii_art(Sylvester.forward_rule(E, E, E, 1))
            o
            sage: ascii_art(Sylvester.forward_rule(N, N, N, 1))
            o
             \\\n              o
            sage: ascii_art(Sylvester.forward_rule(L, L, L, 1))
              o
             / \\\n            o   o
            sage: ascii_art(Sylvester.forward_rule(R, R, R, 1))
            o
             \\\n              o
               \\\n                o

        If ``y != x``, obtain ``z`` from ``y`` adding a node such
        that deleting the right most gives ``x``::

            sage: ascii_art(Sylvester.forward_rule(R, N, L, 0))
              o
             / \\\n            o   o

            sage: ascii_art(Sylvester.forward_rule(L, N, R, 0))
              o
             /
            o
             \\\n              o

        If ``y == x != t``, obtain ``z`` from ``x`` by adding a node
        as left child to the right most node::

            sage: ascii_art(Sylvester.forward_rule(N, E, N, 0))
              o
             /
            o
            sage: ascii_art(Sylvester.forward_rule(T, L, T, 0))
              _o_
             /   \\\n            o     o
                 /
                o
            sage: ascii_art(Sylvester.forward_rule(L, N, L, 0))
                o
               /
              o
             /
            o
            sage: ascii_art(Sylvester.forward_rule(R, N, R, 0))
            o
             \\\n              o
             /
            o
        """
    def backward_rule(self, y, z, x):
        """
        Return the output shape given three shapes and the content.

        See [Nze2007]_, page 9.

        INPUT:

        - ``y``, ``z``, ``x`` -- three binary trees from a cell in a growth
          diagram, labelled as::

                x
              y z

        OUTPUT:

        A pair ``(t, content)`` consisting of the shape of the fourth
        binary tree t and the content of the cell.

        EXAMPLES::

            sage: Sylvester = GrowthDiagram.rules.Sylvester()
            sage: B = BinaryTree; E = B(); N = B([]); L = B([[],None])
            sage: R = B([None,[]]); T = B([[],[]])

            sage: ascii_art(Sylvester.backward_rule(E, E, E))
            ( , 0 )
            sage: ascii_art(Sylvester.backward_rule(N, N, N))
            ( o, 0 )
        """

class RuleYoungFibonacci(Rule):
    """
    A rule modelling a Schensted-like correspondence for
    Young-Fibonacci-tableaux.

    EXAMPLES::

        sage: YF = GrowthDiagram.rules.YoungFibonacci()
        sage: GrowthDiagram(YF, [3,1,2])
        0  1  0
        0  0  1
        1  0  0

    The vertices of the dual graded graph are Fibonacci words -
    compositions into parts of size at most two::

        sage: YF.vertices(4)
        [word: 22, word: 211, word: 121, word: 112, word: 1111]

    Note that, instead of passing the rule to :class:`GrowthDiagram`,
    we can also use call the rule to create growth diagrams.  For
    example::

        sage: G = YF([2, 3, 7, 4, 1, 6, 5]); G
        0  0  0  0  1  0  0
        1  0  0  0  0  0  0
        0  1  0  0  0  0  0
        0  0  0  1  0  0  0
        0  0  0  0  0  0  1
        0  0  0  0  0  1  0
        0  0  1  0  0  0  0

    The Kleitman Greene invariant is: take the last letter and the
    largest letter of the permutation and remove them.  If they
    coincide write 1, otherwise write 2::

        sage: G.P_chain()[-1]
        word: 21211

    TESTS::

        sage: YF = GrowthDiagram.rules.YoungFibonacci()
        sage: YF.zero
        word:

    Check duality::

        sage: YF._check_duality(4)

        sage: G = YF(labels=[[1],[1,0],[1]])
        Traceback (most recent call last):
        ...
        ValueError: 0 not in alphabet

        sage: G = YF(labels=[[1,1],[1,2]])
        Traceback (most recent call last):
        ...
        ValueError: 11 has smaller rank than 12 but is not covered by it in Q

        sage: G = YF(labels=[[1,2],[1,1]])
        Traceback (most recent call last):
        ...
        ValueError: 11 has smaller rank than 12 but is not covered by it in P

        sage: all(YF(labels=YF(pi).out_labels()).to_word()
        ....:      == pi for pi in Permutations(4))
        True
        sage: pi = Permutations(10).random_element()
        sage: G = YF(pi)
        sage: list(YF(labels=G.out_labels())) == list(G)
        True
    """
    zero: Incomplete
    def normalize_vertex(self, v):
        """
        Return ``v`` as a word with letters 1 and 2.

        EXAMPLES::

            sage: YF = GrowthDiagram.rules.YoungFibonacci()
            sage: YF.normalize_vertex([1,2,1]).parent()
            Finite words over {1, 2}
        """
    def vertices(self, n):
        """
        Return the vertices of the dual graded graph on level ``n``.

        EXAMPLES::

            sage: YF = GrowthDiagram.rules.YoungFibonacci()
            sage: YF.vertices(3)
            [word: 21, word: 12, word: 111]
        """
    def rank(self, v):
        """
        Return the rank of ``v``: the size of the corresponding composition.

        EXAMPLES::

            sage: YF = GrowthDiagram.rules.YoungFibonacci()
            sage: YF.rank(YF.vertices(3)[0])
            3
        """
    def is_P_edge(self, v, w):
        """
        Return whether ``(v, w)`` is a `P`-edge of ``self``.

        ``(v, w)`` is an edge if ``v`` is obtained from ``w`` by deleting
        a ``1`` or replacing the left-most ``2`` by a ``1``.

        EXAMPLES::

            sage: YF = GrowthDiagram.rules.YoungFibonacci()
            sage: v = YF.vertices(5)[5]; v
            word: 1121
            sage: [w for w in YF.vertices(6) if YF.is_P_edge(v, w)]
            [word: 2121, word: 11121]
            sage: [w for w in YF.vertices(7) if YF.is_P_edge(v, w)]
            []
        """
    is_Q_edge = is_P_edge
    def forward_rule(self, y, t, x, content):
        """
        Return the output shape given three shapes and the content.

        See [Fom1995]_ Lemma 4.4.1, page 35.

        INPUT:

        - ``y``, ``t``, ``x`` -- three Fibonacci words from a
          cell in a growth diagram, labelled as::

              t x
              y

        - ``content`` -- `0` or `1`; the content of the cell

        OUTPUT: the fourth Fibonacci word

        EXAMPLES::

            sage: YF = GrowthDiagram.rules.YoungFibonacci()

            sage: YF.forward_rule([], [], [], 1)
            word: 1

            sage: YF.forward_rule([1], [1], [1], 1)
            word: 11

            sage: YF.forward_rule([1,2], [1], [1,1], 0)
            word: 21

            sage: YF.forward_rule([1,1], [1], [1,1], 0)
            word: 21
        """
    def backward_rule(self, y, z, x):
        """
        Return the content and the input shape.

        See [Fom1995]_ Lemma 4.4.1, page 35.

        - ``y``, ``z``, ``x`` -- three Fibonacci words from a cell in a
          growth diagram, labelled as::

                x
              y z

        OUTPUT:

        A pair ``(t, content)`` consisting of the shape of the fourth
        word and the content of the cell.

        TESTS::

            sage: YF = GrowthDiagram.rules.YoungFibonacci()
            sage: w = [4,1,8,3,6,5,2,7,9]; G = YF(w)
            sage: GrowthDiagram(YF, labels=G.out_labels()).to_word() == w  # indirect doctest
            True
        """

class RulePartitions(Rule):
    """
    A rule for growth diagrams on Young's lattice on integer
    partitions graded by size.

    TESTS::

        sage: Burge = GrowthDiagram.rules.Burge()
        sage: Burge.zero
        []
        sage: G = GrowthDiagram(Burge, labels=[[1],[1]])
        Traceback (most recent call last):
        ...
        ValueError: can only determine the shape of the growth diagram
         if ranks of successive labels differ
    """
    zero: Incomplete
    def vertices(self, n):
        """
        Return the vertices of the dual graded graph on level ``n``.

        EXAMPLES::

            sage: RSK = GrowthDiagram.rules.RSK()
            sage: RSK.vertices(3)
            Partitions of the integer 3
        """
    def normalize_vertex(self, v):
        """
        Return ``v`` as a partition.

        EXAMPLES::

            sage: RSK = GrowthDiagram.rules.RSK()
            sage: RSK.normalize_vertex([3,1]).parent()
            Partitions
        """
    def rank(self, v):
        """
        Return the rank of ``v``: the size of the partition.

        EXAMPLES::

            sage: RSK = GrowthDiagram.rules.RSK()
            sage: RSK.rank(RSK.vertices(3)[0])
            3
        """
    def P_symbol(self, P_chain):
        """
        Return the labels along the vertical boundary of a rectangular
        growth diagram as a (skew) tableau.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = RuleRSK([[0,1,0], [1,0,2]])
            sage: G.P_symbol().pp()
            1  2  2
            2
        """
    def Q_symbol(self, Q_chain):
        """
        Return the labels along the horizontal boundary of a rectangular
        growth diagram as a skew tableau.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: G = RuleRSK([[0,1,0], [1,0,2]])
            sage: G.Q_symbol().pp()
            1  3  3
            2
        """

class RuleRSK(RulePartitions):
    """
    A rule modelling Robinson-Schensted-Knuth insertion.

    EXAMPLES::

        sage: RuleRSK = GrowthDiagram.rules.RSK()
        sage: GrowthDiagram(RuleRSK, [3,2,1,2,3])
        0  0  1  0  0
        0  1  0  1  0
        1  0  0  0  1

    The vertices of the dual graded graph are integer partitions::

        sage: RuleRSK.vertices(3)
        Partitions of the integer 3

    The local rules implemented provide the RSK correspondence
    between matrices with nonnegative integer entries and pairs of
    semistandard tableaux, the
    :meth:`~sage.combinat.growth.RulePartitions.P_symbol` and the
    :meth:`~sage.combinat.growth.RulePartitions.Q_symbol`.  For
    permutations, it reduces to classical Schensted insertion.

    Instead of passing the rule to :class:`GrowthDiagram`, we can
    also call the rule to create growth diagrams.  For example::

        sage: m = matrix([[0,0,0,0,1],[1,1,0,2,0], [0,3,0,0,0]])
        sage: G = RuleRSK(m); G
        0  0  0  0  1
        1  1  0  2  0
        0  3  0  0  0

        sage: ascii_art([G.P_symbol(), G.Q_symbol()])
        [   1  2  2  2  3    1  2  2  2  2 ]
        [   2  3             4  4          ]
        [   3            ,   5             ]

    For rectangular fillings, the Kleitman-Greene invariant is the
    shape of the :meth:`P_symbol` (or the :meth:`Q_symbol`).  Put
    differently, it is the partition labelling the lower right corner
    of the filling (recall that we are using matrix coordinates).  It
    can be computed alternatively as the partition
    `(\\mu_1,\\dots,\\mu_n)`, where `\\mu_1 + \\dots + \\mu_i` is the
    maximal sum of entries in a collection of `i` pairwise disjoint
    sequences of cells with weakly increasing coordinates.

    For rectangular fillings, we could also use the (faster)
    implementation provided via :func:`~sage.combinat.rsk.RSK`.
    Because the of the coordinate conventions in
    :func:`~sage.combinat.rsk.RSK`, we have to transpose matrices::

        sage: [G.P_symbol(), G.Q_symbol()] == RSK(m.transpose())
        True

        sage: n = 5; l = [(pi, RuleRSK(pi)) for pi in Permutations(n)]
        sage: all([G.P_symbol(), G.Q_symbol()] == RSK(pi) for pi, G in l)
        True

        sage: n = 5; l = [(w, RuleRSK(w)) for w in Words([1,2,3], 5)]
        sage: all([G.P_symbol(), G.Q_symbol()] == RSK(pi) for pi, G in l)
        True
    """
    def forward_rule(self, y, t, x, content):
        """
        Return the output shape given three shapes and the content.

        See [Kra2006]_ `(F^1 0)-(F^1 2)`.

        INPUT:

        - ``y``, ``t``, ``x`` -- three partitions from a cell in a
          growth diagram, labelled as::

              t x
              y

        - ``content`` -- nonnegative integer; the content of the cell

        OUTPUT:

        The fourth partition according to the Robinson-Schensted-Knuth
        correspondence.

        EXAMPLES::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: RuleRSK.forward_rule([2,1],[2,1],[2,1],1)
            [3, 1]

            sage: RuleRSK.forward_rule([1],[],[2],2)
            [4, 1]
        """
    def backward_rule(self, y, z, x):
        """
        Return the content and the input shape.

        See [Kra2006]_ `(B^1 0)-(B^1 2)`.

        INPUT:

        - ``y``, ``z``, ``x`` -- three partitions from a cell in a
          growth diagram, labelled as::

              x
            y z

        OUTPUT:

        A pair ``(t, content)`` consisting of the shape of the fourth
        word according to the Robinson-Schensted-Knuth correspondence
        and the content of the cell.

        TESTS::

            sage: RuleRSK = GrowthDiagram.rules.RSK()
            sage: w = [4,1,8,3,6,5,2,7,9]; G = RuleRSK(w)
            sage: GrowthDiagram(RuleRSK, labels=G._out_labels).to_word() == w  # indirect doctest
            True
        """

class RuleBurge(RulePartitions):
    """
    A rule modelling Burge insertion.

    EXAMPLES::

        sage: Burge = GrowthDiagram.rules.Burge()
        sage: GrowthDiagram(Burge, labels=[[],[1,1,1],[2,1,1,1],[2,1,1],[2,1],[1,1],[]])
        1  1
        0  1
        1  0
        1  0

    The vertices of the dual graded graph are integer partitions::

        sage: Burge.vertices(3)
        Partitions of the integer 3

    The local rules implemented provide Burge's correspondence
    between matrices with nonnegative integer entries and pairs of
    semistandard tableaux, the
    :meth:`~sage.combinat.growth.RulePartitions.P_symbol` and the
    :meth:`~sage.combinat.growth.RulePartitions.Q_symbol`.  For
    permutations, it reduces to classical Schensted insertion.

    Instead of passing the rule to :class:`GrowthDiagram`, we can
    also call the rule to create growth diagrams.  For example::

        sage: m = matrix([[2,0,0,1,0],[1,1,0,0,0], [0,0,0,0,3]])
        sage: G = Burge(m); G
        2  0  0  1  0
        1  1  0  0  0
        0  0  0  0  3

        sage: ascii_art([G.P_symbol(), G.Q_symbol()])
        [   1  2  3    1  2  5 ]
        [   1  3       1  5    ]
        [   1  3       1  5    ]
        [   2      ,   4       ]

    For rectangular fillings, the Kleitman-Greene invariant is the
    shape of the
    :meth:`~sage.combinat.growth.RulePartitions.P_symbol`.  Put
    differently, it is the partition labelling the lower right corner
    of the filling (recall that we are using matrix coordinates).  It
    can be computed alternatively as the transpose of the partition
    `(\\mu_1, \\ldots, \\mu_n)`, where `\\mu_1 + \\cdots + \\mu_i` is the
    maximal sum of entries in a collection of `i` pairwise disjoint
    sequences of cells with weakly decreasing row indices and weakly
    increasing column indices.
    """
    def forward_rule(self, y, t, x, content):
        """
        Return the output shape given three shapes and the content.

        See [Kra2006]_ `(F^4 0)-(F^4 2)`.

        INPUT:

        - ``y``, ``t``, ``x`` -- three  from a cell in a growth diagram,
          labelled as::

              t x
              y

        - ``content`` -- nonnegative integer; the content of the cell

        OUTPUT: the fourth partition according to the Burge correspondence

        EXAMPLES::

            sage: Burge = GrowthDiagram.rules.Burge()
            sage: Burge.forward_rule([2,1],[2,1],[2,1],1)
            [3, 1]

            sage: Burge.forward_rule([1],[],[2],2)
            [2, 1, 1, 1]
        """
    def backward_rule(self, y, z, x):
        """
        Return the content and the input shape.

        See [Kra2006]_ `(B^4 0)-(B^4 2)`.  (In the arXiv version of
        the article there is a typo: in the computation of carry in
        `(B^4 2)` , `\\rho` must be replaced by `\\lambda`).

        INPUT:

        - ``y``, ``z``, ``x`` -- three partitions from a cell in a
          growth diagram, labelled as::

              x
            y z

        OUTPUT:

        A pair ``(t, content)`` consisting of the shape of the fourth
        partition according to the Burge correspondence and the content of
        the cell.

        EXAMPLES::

            sage: Burge = GrowthDiagram.rules.Burge()
            sage: Burge.backward_rule([1,1,1],[2,1,1,1],[2,1,1])
            ([1, 1], 0)

        TESTS::

            sage: w = [4,1,8,3,6,5,2,7,9]; G = Burge(w)
            sage: GrowthDiagram(Burge, labels=G._out_labels).to_word() == w  # indirect doctest
            True
        """

class RuleDomino(Rule):
    """
    A rule modelling domino insertion.

    EXAMPLES::

        sage: Domino = GrowthDiagram.rules.Domino()
        sage: GrowthDiagram(Domino, [[1,0,0],[0,0,1],[0,-1,0]])
        1  0  0
        0  0  1
        0 -1  0

    The vertices of the dual graded graph are integer partitions
    whose Ferrers diagram can be tiled with dominoes::

        sage: Domino.vertices(2)
        [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]

    Instead of passing the rule to :class:`GrowthDiagram`, we can
    also call the rule to create growth diagrams.  For example, let
    us check Figure 3 in [Lam2004]_::

        sage: G = Domino([[0,0,0,-1],[0,0,1,0],[-1,0,0,0],[0,1,0,0]]); G
         0  0  0 -1
         0  0  1  0
        -1  0  0  0
         0  1  0  0

        sage: ascii_art([G.P_symbol(), G.Q_symbol()])
        [   1  2  4    1  2  2 ]
        [   1  2  4    1  3  3 ]
        [   3  3   ,   4  4    ]

    The spin of a domino tableau is half the number of vertical dominoes::

        sage: def spin(T):
        ....:     return sum(2*len(set(row)) - len(row) for row in T)/4

    According to [Lam2004]_, the number of negative entries in the
    signed permutation equals the sum of the spins of the two
    associated tableaux::

        sage: pi = [3,-1,2,4,-5]
        sage: G = Domino(pi)
        sage: list(G.filling().values()).count(-1) == spin(G.P_symbol()) + spin(G.Q_symbol())
        True

    Negating all signs transposes all the partitions::

        sage: G.P_symbol() == Domino([-e for e in pi]).P_symbol().conjugate()
        True

    TESTS:

    Check duality::

        sage: Domino = GrowthDiagram.rules.Domino()
        sage: Domino._check_duality(3)

        sage: G = Domino([[0,1,0],[0,0,-1],[1,0,0]]); G
        0  1  0
        0  0 -1
        1  0  0

        sage: ascii_art([G.P_symbol(), G.Q_symbol()])
        [   1  1    1  1 ]
        [   2  3    2  2 ]
        [   2  3,   3  3 ]

        sage: l = {pi: Domino(pi) for pi in SignedPermutations(4)}
        sage: S = Set([(G.P_symbol(), G.Q_symbol()) for G in l.values()])
        sage: S.cardinality()
        384

    Check the color-to-spin property for all permutations of size 4::

        sage: all(list(G.filling().values()).count(-1) == spin(G.P_symbol()) + spin(G.Q_symbol())
        ....:     for G in l.values())
        True

    Negating all signs transposes all the partitions::

        sage: W = SignedPermutations(4)
        sage: all(l[pi].P_symbol() == l[W([-e for e in pi])].P_symbol().conjugate()
        ....:     for pi in l)
        True

    Check part of Theorem 4.2.3 in [Lee1996]_::

        sage: def to_permutation(pi):
        ....:     pi1 = list(pi)
        ....:     n = len(pi1)
        ....:     pi2 = [-e for e in pi][::-1] + pi1
        ....:     return Permutation([e+n+1 if e<0 else e+n for e in pi2])
        sage: RuleRSK = GrowthDiagram.rules.RSK()
        sage: def good(pi):
        ....:     return Domino(pi).P_chain()[-1] == RuleRSK(to_permutation(pi)).P_chain()[-1]
        sage: all(good(pi) for pi in SignedPermutations(4))
        True

        sage: G = Domino(labels=[[1],[2,1]])
        Traceback (most recent call last):
        ...
        ValueError: [1] has smaller rank than [2, 1] but is not covered by it in Q

        sage: G = Domino(labels=[[2,1],[1]])
        Traceback (most recent call last):
        ...
        ValueError: [1] has smaller rank than [2, 1] but is not covered by it in P
    """
    r: int
    zero: Incomplete
    def normalize_vertex(self, v):
        """
        Return ``v`` as a partition.

        EXAMPLES::

            sage: Domino = GrowthDiagram.rules.Domino()
            sage: Domino.normalize_vertex([3,1]).parent()
            Partitions
        """
    def vertices(self, n):
        """
        Return the vertices of the dual graded graph on level ``n``.

        EXAMPLES::

            sage: Domino = GrowthDiagram.rules.Domino()
            sage: Domino.vertices(2)
            [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
        """
    def rank(self, v):
        """
        Return the rank of ``v``.

        The rank of a vertex is half the size of the partition,
        which equals the number of dominoes in any filling.

        EXAMPLES::

            sage: Domino = GrowthDiagram.rules.Domino()
            sage: Domino.rank(Domino.vertices(3)[0])
            3
        """
    def is_P_edge(self, v, w):
        """
        Return whether ``(v, w)`` is a `P`-edge of ``self``.

        ``(v, w)`` is an edge if ``v`` is obtained from ``w`` by deleting
        a domino.

        EXAMPLES::

            sage: Domino = GrowthDiagram.rules.Domino()
            sage: v = Domino.vertices(2)[1]; ascii_art(v)
            ***
            *
            sage: ascii_art([w for w in Domino.vertices(3) if Domino.is_P_edge(v, w)])
            [             *** ]
            [             *   ]
            [ *****  ***  *   ]
            [ *    , ***, *   ]
            sage: [w for w in Domino.vertices(4) if Domino.is_P_edge(v, w)]
            []
        """
    is_Q_edge = is_P_edge
    def P_symbol(self, P_chain):
        """
        Return the labels along the vertical boundary of a rectangular
        growth diagram as a (skew) domino tableau.

        EXAMPLES::

            sage: Domino = GrowthDiagram.rules.Domino()
            sage: G = Domino([[0,1,0],[0,0,-1],[1,0,0]])
            sage: G.P_symbol().pp()
            1  1
            2  3
            2  3
        """
    Q_symbol = P_symbol
    def forward_rule(self, y, t, x, content):
        """
        Return the output shape given three shapes and the content.

        See [Lam2004]_ Section 3.1.

        INPUT:

        - ``y``, ``t``, ``x`` -- three partitions from a cell in a
          growth diagram, labelled as::

              t x
              y

        - ``content`` -- `-1`, `0` or `1`; the content of the cell

        OUTPUT: the fourth partition according to domino insertion

        EXAMPLES::

            sage: Domino = GrowthDiagram.rules.Domino()

        Rule 1::

            sage: Domino.forward_rule([], [], [], 1)
            [2]

            sage: Domino.forward_rule([1,1], [1,1], [1,1], 1)
            [3, 1]

        Rule 2::

            sage: Domino.forward_rule([1,1], [1,1], [1,1], -1)
            [1, 1, 1, 1]

        Rule 3::

            sage: Domino.forward_rule([1,1], [1,1], [2,2], 0)
            [2, 2]

        Rule 4::

            sage: Domino.forward_rule([2,2,2], [2,2], [3,3], 0)
            [3, 3, 2]

            sage: Domino.forward_rule([2], [], [1,1], 0)
            [2, 2]

            sage: Domino.forward_rule([1,1], [], [2], 0)
            [2, 2]

            sage: Domino.forward_rule([2], [], [2], 0)
            [2, 2]

            sage: Domino.forward_rule([4], [2], [4], 0)
            [4, 2]

            sage: Domino.forward_rule([1,1,1,1], [1,1], [1,1,1,1], 0)
            [2, 2, 1, 1]

            sage: Domino.forward_rule([2,1,1], [2], [4], 0)
            [4, 1, 1]
        """

class Rules:
    """
    Catalog of rules for growth diagrams.
    """
    ShiftedShapes = RuleShiftedShapes
    LLMS = RuleLLMS
    BinaryWord = RuleBinaryWord
    Sylvester = RuleSylvester
    YoungFibonacci = RuleYoungFibonacci
    RSK = RuleRSK
    Burge = RuleBurge
    Domino = RuleDomino
