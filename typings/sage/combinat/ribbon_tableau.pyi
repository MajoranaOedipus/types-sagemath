from . import permutation as permutation
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.sets_cat import Sets as Sets
from sage.combinat.combinat import CombinatorialElement as CombinatorialElement
from sage.combinat.partition import Partition as Partition
from sage.combinat.permutation import to_standard as to_standard
from sage.combinat.skew_partition import SkewPartition as SkewPartition, SkewPartitions as SkewPartitions
from sage.combinat.skew_tableau import SemistandardSkewTableaux as SemistandardSkewTableaux, SkewTableau as SkewTableau, SkewTableaux as SkewTableaux
from sage.combinat.tableau import Tableaux as Tableaux
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import parent as parent
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class RibbonTableau(SkewTableau):
    """
    A ribbon tableau.

    A ribbon is a connected skew shape which does not contain any
    `2 \\times 2` boxes.  A ribbon tableau is a skew tableau
    whose shape is partitioned into ribbons, each of which is filled
    with identical entries.

    EXAMPLES::

        sage: rt = RibbonTableau([[None, 1],[2,3]]); rt
        [[None, 1], [2, 3]]
        sage: rt.inner_shape()
        [1]
        sage: rt.outer_shape()
        [2, 2]

        sage: rt = RibbonTableau([[None, None, 0, 0, 0], [None, 0, 0, 2], [1, 0, 1]]); rt.pp()
          .  .  0  0  0
          .  0  0  2
          1  0  1

    In the previous example, each ribbon is uniquely determined by a
    nonzero entry.  The 0 entries are used to fill in the rest of the
    skew shape.

    .. NOTE::

        Sanity checks are not performed; lists can contain any object.

    ::

        sage: RibbonTableau(expr=[[1,1],[[5],[3,4],[1,2]]])
        [[None, 1, 2], [None, 3, 4], [5]]

    TESTS::

        sage: RibbonTableau([[0, 0, 3, 0], [1, 1, 0], [2, 0, 4]]).evaluation()
        [2, 1, 1, 1]
    """
    @staticmethod
    def __classcall_private__(cls, rt=None, expr=None):
        """
        Return a ribbon tableau object.

        EXAMPLES::

            sage: rt = RibbonTableau([[None, 1],[2,3]]); rt
            [[None, 1], [2, 3]]
            sage: TestSuite(rt).run()
        """
    def length(self):
        """
        Return the length of the ribbons into a ribbon tableau.

        EXAMPLES::

            sage: RibbonTableau([[None, 1],[2,3]]).length()
            1
            sage: RibbonTableau([[1,0],[2,0]]).length()
            2
        """
    def to_word(self):
        """
        Return a word obtained from a row reading of ``self``.

        .. WARNING::

            Unlike the ``to_word`` method on skew tableaux (which are a
            superclass of this), this method does not filter out
            ``None`` entries.

        EXAMPLES::

            sage: R = RibbonTableau([[0, 0, 3, 0], [1, 1, 0], [2, 0, 4]])
            sage: R.to_word()
            word: 2041100030
        """

class RibbonTableaux(UniqueRepresentation, Parent):
    '''
    Ribbon tableaux.

    A ribbon tableau is a skew tableau whose skew shape ``shape`` is
    tiled by ribbons of length ``length``. The weight ``weight`` is
    calculated from the labels on the ribbons.

    .. NOTE::

        Here we impose the condition that the ribbon tableaux are semistandard.

    INPUT(Optional):

    - ``shape`` -- skew shape as a list of lists or an object of type
      SkewPartition

    - ``length`` -- integer; ``shape`` is partitioned into ribbons of
      length ``length``

    - ``weight`` -- list of integers; computed from the values of
      nonzero entries labeling the ribbons

    EXAMPLES::

        sage: RibbonTableaux([[2,1],[]], [1,1,1], 1)
        Ribbon tableaux of shape [2, 1] / [] and weight [1, 1, 1] with 1-ribbons

        sage: R = RibbonTableaux([[5,4,3],[2,1]], [2,1], 3)
        sage: for i in R: i.pp(); print("\\n")
          .  .  0  0  0
          .  0  0  2
          1  0  1
        <BLANKLINE>
          .  .  1  0  0
          .  0  0  0
          1  0  2
        <BLANKLINE>
          .  .  0  0  0
          .  1  0  1
          2  0  0
        <BLANKLINE>

    REFERENCES:

    .. [vanLeeuwen91] Marc. A. A. van Leeuwen, *Edge sequences,
       ribbon tableaux, and an action of affine permutations*.
       Europe J. Combinatorics. **20** (1999).
       http://wwwmathlabo.univ-poitiers.fr/~maavl/pdf/edgeseqs.pdf
    '''
    @staticmethod
    def __classcall_private__(cls, shape=None, weight=None, length=None):
        """
        Return the correct parent object.

        EXAMPLES::

            sage: R = RibbonTableaux([[2,1],[]],[1,1,1],1)
            sage: R2 = RibbonTableaux(SkewPartition([[2,1],[]]),(1,1,1),1)
            sage: R is R2
            True
        """
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: R = RibbonTableaux()
            sage: TestSuite(R).run()
        """
    def from_expr(self, l):
        """
        Return a :class:`RibbonTableau` from a MuPAD-Combinat expr for a skew
        tableau. The first list in ``expr`` is the inner shape of the skew
        tableau. The second list are the entries in the rows of the skew
        tableau from bottom to top.

        Provided primarily for compatibility with MuPAD-Combinat.

        EXAMPLES::

            sage: RibbonTableaux().from_expr([[1,1],[[5],[3,4],[1,2]]])
            [[None, 1, 2], [None, 3, 4], [5]]
        """
    Element = RibbonTableau
    options = Tableaux.options

class RibbonTableaux_shape_weight_length(RibbonTableaux):
    """
    Ribbon tableaux of a given shape, weight, and length.
    """
    @staticmethod
    def __classcall_private__(cls, shape, weight, length):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: R = RibbonTableaux([[2,1],[]],[1,1,1],1)
            sage: R2 = RibbonTableaux(SkewPartition([[2,1],[]]),(1,1,1),1)
            sage: R is R2
            True
        """
    def __init__(self, shape, weight, length) -> None:
        """
        EXAMPLES::

            sage: R = RibbonTableaux([[2,1],[]],[1,1,1],1)
            sage: TestSuite(R).run()
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: RibbonTableaux([[2,1],[]],[1,1,1],1).list()
            [[[1, 3], [2]], [[1, 2], [3]]]
            sage: RibbonTableaux([[2,2],[]],[1,1],2).list()
            [[[0, 0], [1, 2]], [[1, 0], [2, 0]]]
        """
    def __contains__(self, x) -> bool:
        """
        Note that this just checks to see if ``x`` appears in ``self``.

        This should be improved to provide actual checking.

        EXAMPLES::

            sage: r = RibbonTableaux([[2,2],[]],[1,1],2)
            sage: [[0, 0], [1, 2]] in r
            True
            sage: [[1, 0], [2, 0]] in r
            True
            sage: [[0, 1], [2, 0]] in r
            False
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: RibbonTableaux([[2,1],[]],[1,1,1],1).cardinality()
            2
            sage: RibbonTableaux([[2,2],[]],[1,1],2).cardinality()
            2
            sage: RibbonTableaux([[4,3,3],[]],[2,1,1,1],2).cardinality()
            5

        TESTS::

            sage: RibbonTableaux([6,6,6], [4,2], 3).cardinality()
            6
            sage: RibbonTableaux([3,3,3,2,1], [3,1], 3).cardinality()
            1
            sage: RibbonTableaux([3,3,3,2,1], [2,2], 3).cardinality()
            2
            sage: RibbonTableaux([3,3,3,2,1], [2,1,1], 3).cardinality()
            5
            sage: RibbonTableaux([3,3,3,2,1], [1,1,1,1], 3).cardinality()
            12
            sage: RibbonTableaux([5,4,3,2,1], [2,2,1], 3).cardinality()
            10

        ::

            sage: RibbonTableaux([8,7,6,5,1,1], [3,2,2,1], 3).cardinality()
            85
            sage: RibbonTableaux([5,4,3,2,1,1,1], [2,2,1], 3).cardinality()
            10

        ::

            sage: RibbonTableaux([7,7,7,2,1,1], [3,2,0,1,1], 3).cardinality()
            25

        Weights with some zeros in the middle and end::

            sage: RibbonTableaux([3,3,3], [0,1,0,2,0], 3).cardinality()
            3
            sage: RibbonTableaux([3,3,3], [1,0,1,0,1,0,0,0], 3).cardinality()
            6
        """

def insertion_tableau(skp, perm, evaluation, tableau, length):
    """
    INPUT:

    - ``skp`` -- skew partitions

    - ``perm, evaluation`` -- nonnegative integers

    - ``tableau`` -- skew tableau

    - ``length`` -- integer

    TESTS::

        sage: from sage.combinat.ribbon_tableau import insertion_tableau
        sage: insertion_tableau([[1], []], [1], 1, [[], []], 1)
        [[], [[1]]]
        sage: insertion_tableau([[2, 1], []], [1, 1], 2, [[], [[1]]], 1)
        [[], [[2], [1, 2]]]
        sage: insertion_tableau([[2, 1], []], [0, 0], 3, [[], [[2], [1, 2]]], 1)
        [[], [[2], [1, 2]]]
        sage: insertion_tableau([[1, 1], []], [1], 2, [[], [[1]]], 1)
        [[], [[2], [1]]]
        sage: insertion_tableau([[2], []], [0, 1], 2, [[], [[1]]], 1)
        [[], [[1, 2]]]
        sage: insertion_tableau([[2, 1], []], [0, 1], 3, [[], [[2], [1]]], 1)
        [[], [[2], [1, 3]]]
        sage: insertion_tableau([[1, 1], []], [2], 1, [[], []], 2)
        [[], [[1], [0]]]
        sage: insertion_tableau([[2], []], [2, 0], 1, [[], []], 2)
        [[], [[1, 0]]]
        sage: insertion_tableau([[2, 2], []], [0, 2], 2, [[], [[1], [0]]], 2)
        [[], [[1, 2], [0, 0]]]
        sage: insertion_tableau([[2, 2], []], [2, 0], 2, [[], [[1, 0]]], 2)
        [[], [[2, 0], [1, 0]]]
        sage: insertion_tableau([[2, 2], [1]], [3, 0], 1, [[], []], 3)
        [[1], [[1, 0], [0]]]
    """
def count_rec(nexts, current, part, weight, length):
    """
    INPUT:

    - ``nexts, current, part`` -- skew partitions

    - ``weight`` -- nonnegative integer list

    - ``length`` -- integer

    TESTS::

        sage: from sage.combinat.ribbon_tableau import count_rec
        sage: count_rec([], [], [[2, 1, 1], []], [2], 2)
        [0]
        sage: count_rec([[0], [1]], [[[2, 1, 1], [0, 0, 2, 0]], [[4], [2, 0, 0, 0]]], [[4, 1, 1], []], [2, 1], 2)
        [1]
        sage: count_rec([], [[[], [2, 2]]], [[2, 2], []], [2], 2)
        [1]
        sage: count_rec([], [[[], [2, 0, 2, 0]]], [[4], []], [2], 2)
        [1]
        sage: count_rec([[1], [1]], [[[2, 2], [0, 0, 2, 0]], [[4], [2, 0, 0, 0]]], [[4, 2], []], [2, 1], 2)
        [2]
        sage: count_rec([[1], [1], [2]], [[[2, 2, 2], [0, 0, 2, 0]], [[4, 1, 1], [0, 2, 0, 0]], [[4, 2], [2, 0, 0, 0]]], [[4, 2, 2], []], [2, 1, 1], 2)
        [4]
        sage: count_rec([[4], [1]], [[[4, 2, 2], [0, 0, 2, 0]], [[4, 3, 1], [0, 2, 0, 0]]], [[4, 3, 3], []], [2, 1, 1, 1], 2)
        [5]
    """
def list_rec(nexts, current, part, weight, length):
    """
    INPUT:

    - ``nexts, current, part`` -- skew partitions

    - ``weight`` -- nonnegative integer list

    - ``length`` -- integer

    TESTS::

        sage: from sage.combinat.ribbon_tableau import list_rec
        sage: list_rec([], [[[], [1]]], [[1], []], [1], 1)
        [[[], [[1]]]]
        sage: list_rec([[[[], [[1]]]]], [[[1], [1, 1]]], [[2, 1], []], [1, 2], 1)
        [[[], [[2], [1, 2]]]]
        sage: list_rec([], [[[1], [3, 0]]], [[2, 2], [1]], [1], 3)
        [[[1], [[1, 0], [0]]]]
        sage: list_rec([[[[], [[2]]]]], [[[1], [1, 1]]], [[2, 1], []], [0, 1, 2], 1)
        [[[], [[3], [2, 3]]]]
        sage: list_rec([], [[[], [2]]], [[1, 1], []], [1], 2)
        [[[], [[1], [0]]]]
        sage: list_rec([], [[[], [2, 0]]], [[2], []], [1], 2)
        [[[], [[1, 0]]]]
        sage: list_rec([[[[], [[1], [0]]]], [[[], [[1, 0]]]]], [[[1, 1], [0, 2]], [[2], [2, 0]]], [[2, 2], []], [1, 1], 2)
        [[[], [[1, 2], [0, 0]]], [[], [[2, 0], [1, 0]]]]
        sage: list_rec([], [[[], [2, 2]]], [[2, 2], []], [2], 2)
        [[[], [[1, 1], [0, 0]]]]
        sage: list_rec([], [[[], [1, 1]]], [[2], []], [2], 1)
        [[[], [[1, 1]]]]
        sage: list_rec([[[[], [[1, 1]]]]], [[[2], [1, 1]]], [[2, 2], []], [2, 2], 1)
        [[[], [[2, 2], [1, 1]]]]
    """
def spin_rec(t, nexts, current, part, weight, length):
    """
    Routine used for constructing the spin polynomial.

    INPUT:

    - ``weight`` -- list of nonnegative integers

    - ``length`` -- the length of the ribbons we're tiling with

    - ``t`` -- the variable

    EXAMPLES::

        sage: from sage.combinat.ribbon_tableau import spin_rec
        sage: sp = SkewPartition
        sage: t = ZZ['t'].gen()
        sage: spin_rec(t, [], [[[], [3, 3]]], sp([[2, 2, 2], []]), [2], 3)
        [t^4]
        sage: spin_rec(t, [[0], [t^4]], [[[2, 1, 1, 1, 1], [0, 3]], [[2, 2, 2], [3, 0]]], sp([[2, 2, 2, 2, 1], []]), [2, 1], 3)
        [t^5]
        sage: spin_rec(t, [], [[[], [3, 3, 0]]], sp([[3, 3], []]), [2], 3)
        [t^2]
        sage: spin_rec(t, [[t^4], [t^3], [t^2]], [[[2, 2, 2], [0, 0, 3]], [[3, 2, 1], [0, 3, 0]], [[3, 3], [3, 0, 0]]], sp([[3, 3, 3], []]), [2, 1], 3)
        [t^6 + t^4 + t^2]
        sage: spin_rec(t, [[t^5], [t^4], [t^6 + t^4 + t^2]], [[[2, 2, 2, 2, 1], [0, 0, 3]], [[3, 3, 1, 1, 1], [0, 3, 0]], [[3, 3, 3], [3, 0, 0]]], sp([[3, 3, 3, 2, 1], []]), [2, 1, 1], 3)
        [2*t^7 + 2*t^5 + t^3]
    """
def spin_polynomial_square(part, weight, length):
    """
    Return the spin polynomial associated with ``part``, ``weight``, and
    ``length``, with the substitution `t \\to t^2` made.

    EXAMPLES::

        sage: from sage.combinat.ribbon_tableau import spin_polynomial_square
        sage: spin_polynomial_square([6,6,6],[4,2],3)
        t^12 + t^10 + 2*t^8 + t^6 + t^4
        sage: spin_polynomial_square([6,6,6],[4,1,1],3)
        t^12 + 2*t^10 + 3*t^8 + 2*t^6 + t^4
        sage: spin_polynomial_square([3,3,3,2,1], [2,2], 3)
        t^7 + t^5
        sage: spin_polynomial_square([3,3,3,2,1], [2,1,1], 3)
        2*t^7 + 2*t^5 + t^3
        sage: spin_polynomial_square([3,3,3,2,1], [1,1,1,1], 3)
        3*t^7 + 5*t^5 + 3*t^3 + t
        sage: spin_polynomial_square([5,4,3,2,1,1,1], [2,2,1], 3)
        2*t^9 + 6*t^7 + 2*t^5
        sage: spin_polynomial_square([[6]*6, [3,3]], [4,4,2], 3)
        3*t^18 + 5*t^16 + 9*t^14 + 6*t^12 + 3*t^10
    """
def spin_polynomial(part, weight, length):
    """
    Return the spin polynomial associated to ``part``, ``weight``, and
    ``length``.

    EXAMPLES::

        sage: # needs sage.symbolic
        sage: from sage.combinat.ribbon_tableau import spin_polynomial
        sage: spin_polynomial([6,6,6],[4,2],3)
        t^6 + t^5 + 2*t^4 + t^3 + t^2
        sage: spin_polynomial([6,6,6],[4,1,1],3)
        t^6 + 2*t^5 + 3*t^4 + 2*t^3 + t^2
        sage: spin_polynomial([3,3,3,2,1], [2,2], 3)
        t^(7/2) + t^(5/2)
        sage: spin_polynomial([3,3,3,2,1], [2,1,1], 3)
        2*t^(7/2) + 2*t^(5/2) + t^(3/2)
        sage: spin_polynomial([3,3,3,2,1], [1,1,1,1], 3)
        3*t^(7/2) + 5*t^(5/2) + 3*t^(3/2) + sqrt(t)
        sage: spin_polynomial([5,4,3,2,1,1,1], [2,2,1], 3)
        2*t^(9/2) + 6*t^(7/2) + 2*t^(5/2)
        sage: spin_polynomial([[6]*6, [3,3]], [4,4,2], 3)
        3*t^9 + 5*t^8 + 9*t^7 + 6*t^6 + 3*t^5
    """
def cospin_polynomial(part, weight, length):
    """
    Return the cospin polynomial associated to ``part``, ``weight``, and
    ``length``.

    EXAMPLES::

        sage: from sage.combinat.ribbon_tableau import cospin_polynomial
        sage: cospin_polynomial([6,6,6],[4,2],3)
        t^4 + t^3 + 2*t^2 + t + 1
        sage: cospin_polynomial([3,3,3,2,1], [3,1], 3)
        1
        sage: cospin_polynomial([3,3,3,2,1], [2,2], 3)
        t + 1
        sage: cospin_polynomial([3,3,3,2,1], [2,1,1], 3)
        t^2 + 2*t + 2
        sage: cospin_polynomial([3,3,3,2,1], [1,1,1,1], 3)
        t^3 + 3*t^2 + 5*t + 3
        sage: cospin_polynomial([5,4,3,2,1,1,1], [2,2,1], 3)
        2*t^2 + 6*t + 2
        sage: cospin_polynomial([[6]*6, [3,3]], [4,4,2], 3)
        3*t^4 + 6*t^3 + 9*t^2 + 5*t + 3
    """
def graph_implementation_rec(skp, weight, length, function):
    """
    TESTS::

        sage: from sage.combinat.ribbon_tableau import graph_implementation_rec, list_rec
        sage: graph_implementation_rec(SkewPartition([[1], []]), [1], 1, list_rec)
        [[[], [[1]]]]
        sage: graph_implementation_rec(SkewPartition([[2, 1], []]), [1, 2], 1, list_rec)
        [[[], [[2], [1, 2]]]]
        sage: graph_implementation_rec(SkewPartition([[], []]), [0], 1, list_rec)
        [[[], []]]
    """

class MultiSkewTableau(CombinatorialElement):
    """
    A multi skew tableau which is a tuple of skew tableaux.

    EXAMPLES::

        sage: s = MultiSkewTableau([ [[None,1],[2,3]], [[1,2],[2]] ])
        sage: s.size()
        6
        sage: s.weight()
        [2, 3, 1]
        sage: s.shape()
        [[2, 2] / [1], [2, 1] / []]

    TESTS::

        sage: mst = MultiSkewTableau([ [[None,1],[2,3]], [[1,2],[2]] ])
        sage: TestSuite(mst).run()
    """
    @staticmethod
    def __classcall_private__(cls, x):
        """
        Construct a multi skew tableau.

        EXAMPLES::

            sage: s = MultiSkewTableau([ [[None,1],[2,3]], [[1,2],[2]] ])
        """
    def size(self):
        """
        Return the size of ``self``.

        This is the sum of the sizes of the skew
        tableaux in ``self``.

        EXAMPLES::

            sage: s = SemistandardSkewTableaux([[2,2],[1]]).list()
            sage: a = MultiSkewTableau([s[0],s[1],s[2]])
            sage: a.size()
            9
        """
    def weight(self):
        """
        Return the weight of ``self``.

        EXAMPLES::

            sage: s = SemistandardSkewTableaux([[2,2],[1]]).list()
            sage: a = MultiSkewTableau([s[0],s[1],s[2]])
            sage: a.weight()
            [5, 3, 1]
        """
    def shape(self):
        """
        Return the shape of ``self``.

        EXAMPLES::

            sage: s = SemistandardSkewTableaux([[2,2],[1]]).list()
            sage: a = MultiSkewTableau([s[0],s[1],s[2]])
            sage: a.shape()
            [[2, 2] / [1], [2, 2] / [1], [2, 2] / [1]]
        """
    def inversion_pairs(self):
        """
        Return a list of the inversion pairs of ``self``.

        EXAMPLES::

            sage: s = MultiSkewTableau([ [[2,3],[5,5]], [[1,1],[3,3]], [[2],[6]] ])
            sage: s.inversion_pairs()
            [((0, (0, 0)), (1, (0, 0))),
             ((0, (1, 0)), (1, (0, 1))),
             ((0, (1, 1)), (1, (0, 0))),
             ((0, (1, 1)), (1, (1, 1))),
             ((0, (1, 1)), (2, (0, 0))),
             ((1, (0, 1)), (2, (0, 0))),
             ((1, (1, 1)), (2, (0, 0)))]
        """
    def inversions(self):
        """
        Return the number of inversion pairs of ``self``.

        EXAMPLES::

            sage: t1 = SkewTableau([[1]])
            sage: t2 = SkewTableau([[2]])
            sage: MultiSkewTableau([t1,t1]).inversions()
            0
            sage: MultiSkewTableau([t1,t2]).inversions()
            0
            sage: MultiSkewTableau([t2,t2]).inversions()
            0
            sage: MultiSkewTableau([t2,t1]).inversions()
            1
            sage: s = MultiSkewTableau([ [[2,3],[5,5]], [[1,1],[3,3]], [[2],[6]] ])
            sage: s.inversions()
            7
        """

class MultiSkewTableaux(UniqueRepresentation, Parent):
    """
    Multiskew tableaux.
    """
    def __init__(self, category=None) -> None:
        """
        EXAMPLES::

            sage: R = MultiSkewTableaux()
            sage: TestSuite(R).run()
        """
    Element = MultiSkewTableau

class SemistandardMultiSkewTableaux(MultiSkewTableaux):
    """
    Semistandard multi skew tableaux.

    A multi skew tableau is a `k`-tuple of skew tableaux of
    given shape with a specified total weight.

    EXAMPLES::

        sage: S = SemistandardMultiSkewTableaux([ [[2,1],[]], [[2,2],[1]] ], [2,2,2]); S
        Semistandard multi skew tableaux of shape [[2, 1] / [], [2, 2] / [1]] and weight [2, 2, 2]
        sage: S.list()
        [[[[1, 1], [2]], [[None, 2], [3, 3]]],
         [[[1, 2], [2]], [[None, 1], [3, 3]]],
         [[[1, 3], [2]], [[None, 2], [1, 3]]],
         [[[1, 3], [2]], [[None, 1], [2, 3]]],
         [[[1, 1], [3]], [[None, 2], [2, 3]]],
         [[[1, 2], [3]], [[None, 2], [1, 3]]],
         [[[1, 2], [3]], [[None, 1], [2, 3]]],
         [[[2, 2], [3]], [[None, 1], [1, 3]]],
         [[[1, 3], [3]], [[None, 1], [2, 2]]],
         [[[2, 3], [3]], [[None, 1], [1, 2]]]]
    """
    @staticmethod
    def __classcall_private__(cls, shape, weight):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: S1 = SemistandardMultiSkewTableaux([ [[2,1],[]], [[2,2],[1]] ], [2,2,2])
            sage: shape_alt = ( SkewPartition([[2,1],[]]), SkewPartition([[2,2],[1]]) )
            sage: S2 = SemistandardMultiSkewTableaux(shape_alt, (2,2,2))
            sage: S1 is S2
            True
        """
    def __init__(self, shape, weight) -> None:
        """
        TESTS::

            sage: S = SemistandardMultiSkewTableaux([ [[2,1],[]], [[2,2],[1]] ], [2,2,2])
            sage: TestSuite(S).run()
        """
    def __contains__(self, x) -> bool:
        """
        TESTS::

            sage: s = SemistandardMultiSkewTableaux([ [[2,1],[]], [[2,2],[1]] ], [2,2,2])
            sage: all(i in s for i in s)
            True
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: sp = SkewPartitions(3).list()
            sage: SemistandardMultiSkewTableaux([SkewPartition([[1, 1, 1], []]), SkewPartition([[3], []])],[2,2,2]).list()
            [[[[1], [2], [3]], [[1, 2, 3]]]]

            sage: a = SkewPartition([[8,7,6,5,1,1],[2,1,1]])
            sage: weight = [3,3,2]
            sage: k = 3
            sage: s = SemistandardMultiSkewTableaux(a.quotient(k),weight)
            sage: len(s.list())
            34
            sage: RibbonTableaux(a,weight,k).cardinality()
            34

        TESTS:

        Check that :issue:`36196` is fixed::

            sage: shapes = [[[1], [0]], [[1], [0]], [[1], [0]]]
            sage: weight = [1, 1, 1]
            sage: SMST = SemistandardMultiSkewTableaux(shapes, weight)
            sage: list(SMST)
            [[[[1]], [[2]], [[3]]],
             [[[2]], [[1]], [[3]]],
             [[[1]], [[3]], [[2]]],
             [[[2]], [[3]], [[1]]],
             [[[3]], [[1]], [[2]]],
             [[[3]], [[2]], [[1]]]]
        """

class RibbonTableau_class(RibbonTableau):
    """
    This exists solely for unpickling ``RibbonTableau_class`` objects.
    """
