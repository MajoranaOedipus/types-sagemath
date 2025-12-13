from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.partition import Partitions as Partitions
from sage.combinat.tableau import SemistandardTableaux as SemistandardTableaux, Tableau as Tableau
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.misc_c import prod as prod
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class GelfandTsetlinPattern(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    '''
    A Gelfand-Tsetlin (sometimes written as Gelfand-Zetlin or Gelfand-Cetlin)
    pattern.  They were originally defined in [GC50]_.

    A Gelfand-Tsetlin pattern is a triangular array:

    .. MATH::

        \\begin{array}{ccccccccc}
        a_{1,1} & & a_{1,2} & & a_{1,3} & & \\cdots & & a_{1,n} \\\\\n        & a_{2,2} & & a_{2,3} & & \\cdots & & a_{2,n} \\\\\n        & & a_{3,3} & &  \\cdots & & a_{3,n} \\\\\n        & & & \\ddots \\\\\n        & & & & a_{n,n}
        \\end{array}

    such that `a_{i,j} \\geq a_{i+1,j+1} \\geq a_{i,j+1}`.

    Gelfand-Tsetlin patterns are in bijection with semistandard Young tableaux
    by the following algorithm. Let `G` be a Gelfand-Tsetlin pattern with
    `\\lambda^{(k)}` being the `(n-k+1)`-st row (note that this is a partition).
    The definition of `G` implies

    .. MATH::

        \\lambda^{(0)} \\subseteq \\lambda^{(1)} \\subseteq \\cdots \\subseteq
        \\lambda^{(n)},

    where `\\lambda^{(0)}` is the empty partition, and each skew shape
    `\\lambda^{(k)}/\\lambda^{(k-1)}` is a horizontal strip. Thus define `T(G)`
    by inserting `k` into the squares of the skew shape
    `\\lambda^{(k)}/ \\lambda^{(k-1)}`, for `k=1,\\dots,n`.

    To each entry in a Gelfand-Tsetlin pattern, one may attach a decoration of
    a circle or a box (or both or neither).  These decorations appear in the
    study of Weyl group multiple Dirichlet series, and are implemented here
    following the exposition in [BBF]_.

    .. NOTE::

        We use the "right-hand" rule for determining circled and boxed entries.

    .. WARNING::

        The entries in Sage are 0-based and are thought of as flushed to the
        left in a matrix. In other words, the coordinates of entries in the
        Gelfand-Tsetlin patterns are thought of as the matrix:

        .. MATH::

            \\begin{bmatrix}
            g_{0,0} & g_{0,1} & g_{0,2} & \\cdots & g_{0,n-2} & g_{n-1,n-1} \\\\\n            g_{1,0} & g_{1,1} & g_{1,2} & \\cdots & g_{1,n-2} \\\\\n            g_{2,0} & g_{2,1} & g_{2,2} & \\cdots \\\\\n            \\vdots & \\vdots & \\vdots \\\\\n            g_{n-2,0} & g_{n-2,1} \\\\\n            g_{n-1,0}
            \\end{bmatrix}.

        However, in the discussions, we will be using the **standard**
        numbering system.

    EXAMPLES::

        sage: G = GelfandTsetlinPattern([[3, 2, 1], [2, 1], [1]]); G
        [[3, 2, 1], [2, 1], [1]]
        sage: G.pp()
          3     2     1
             2     1
                1
        sage: G = GelfandTsetlinPattern([[7, 7, 4, 0], [7, 7, 3], [7, 5], [5]]); G.pp()
          7     7     4     0
             7     7     3
                7     5
                   5
        sage: G.to_tableau().pp()
          1  1  1  1  1  2  2
          2  2  2  2  2  3  3
          3  3  3  4
    '''
    @staticmethod
    def __classcall_private__(self, gt):
        """
        Return ``gt`` as a proper element of :class:`GelfandTsetlinPatterns`.

        EXAMPLES::

            sage: G = GelfandTsetlinPattern([[3,2,1],[2,1],[1]])
            sage: G.parent()
            Gelfand-Tsetlin patterns
            sage: TestSuite(G).run()
        """
    def check(self) -> None:
        """
        Check that this is a valid Gelfand-Tsetlin pattern.

        EXAMPLES::

            sage: G = GelfandTsetlinPatterns()
            sage: G([[3,2,1],[2,1],[1]]).check()
        """
    def pp(self) -> None:
        """
        Pretty print ``self``.

        EXAMPLES::

            sage: G = GelfandTsetlinPatterns()
            sage: G([[3,2,1],[2,1],[1]]).pp()
              3     2     1
                 2     1
                    1
        """
    def to_tableau(self):
        """
        Return ``self`` as a semistandard Young tableau.

        The conversion from a Gelfand-Tsetlin pattern to a semistandard Young
        tableaux is as follows. Let `G` be a Gelfand-Tsetlin pattern with
        `\\lambda^{(k)}` being the `(n-k+1)`-st row (note that this is a
        partition).  The definition of `G` implies

        .. MATH::

            \\lambda^{(0)} \\subseteq \\lambda^{(1)} \\subseteq \\cdots \\subseteq
            \\lambda^{(n)},

        where `\\lambda^{(0)}` is the empty partition, and each skew shape
        `\\lambda^{(k)} / \\lambda^{(k-1)}` is a horizontal strip. Thus define
        `T(G)` by inserting `k` into the squares of the skew shape
        `\\lambda^{(k)} / \\lambda^{(k-1)}`, for `k=1,\\dots,n`.

        EXAMPLES::

            sage: G = GelfandTsetlinPatterns()
            sage: elt = G([[3,2,1],[2,1],[1]])
            sage: T = elt.to_tableau(); T
            [[1, 2, 3], [2, 3], [3]]
            sage: T.pp()
              1  2  3
              2  3
              3
            sage: G(T) == elt
            True
        """
    @cached_method
    def boxed_entries(self) -> tuple:
        """
        Return the position of the boxed entries of ``self``.

        Using the *right-hand* rule, an entry `a_{i,j}` is boxed if
        `a_{i,j} = a_{i-1,j-1}`; i.e., `a_{i,j}` has the same value as its
        neighbor to the northwest.

        EXAMPLES::

            sage: G = GelfandTsetlinPattern([[3,2,1],[3,1],[1]])
            sage: G.boxed_entries()
            ((1, 0),)
        """
    @cached_method
    def circled_entries(self) -> tuple:
        """
        Return the circled entries of ``self``.

        Using the *right-hand* rule, an entry `a_{i,j}` is circled if
        `a_{i,j} = a_{i-1,j}`; i.e., `a_{i,j}` has the same value as its
        neighbor to the northeast.

        EXAMPLES::

            sage: G = GelfandTsetlinPattern([[3,2,1],[3,1],[1]])
            sage: G.circled_entries()
            ((1, 1), (2, 0))
        """
    @cached_method
    def special_entries(self) -> tuple:
        """
        Return the special entries.

        An entry `a_{i,j}` is special if `a_{i-1,j-1} > a_{i,j} > a_{i-1,j}`,
        that is to say, the entry is neither boxed nor circled and is **not**
        in the first row. The name was coined by [Tok88]_.

        EXAMPLES::

            sage: G = GelfandTsetlinPattern([[3,2,1],[3,1],[1]])
            sage: G.special_entries()
            ()
            sage: G = GelfandTsetlinPattern([[4,2,1],[4,1],[2]])
            sage: G.special_entries()
            ((2, 0),)
        """
    def number_of_boxes(self) -> int:
        """
        Return the number of boxed entries. See :meth:`boxed_entries()`.

        EXAMPLES::

            sage: G = GelfandTsetlinPattern([[3,2,1],[3,1],[1]])
            sage: G.number_of_boxes()
            1
        """
    def number_of_circles(self) -> int:
        """
        Return the number of boxed entries. See :meth:`circled_entries()`.

        EXAMPLES::

            sage: G = GelfandTsetlinPattern([[3,2,1],[3,1],[1]])
            sage: G.number_of_circles()
            2
        """
    def number_of_special_entries(self) -> int:
        """
        Return the number of special entries. See :meth:`special_entries()`.

        EXAMPLES::

            sage: G = GelfandTsetlinPattern([[4,2,1],[4,1],[2]])
            sage: G.number_of_special_entries()
            1
        """
    def is_strict(self) -> bool:
        """
        Return ``True`` if ``self`` is a strict Gelfand-Tsetlin pattern.

        A Gelfand-Tsetlin pattern is said to be *strict* if every row is
        strictly decreasing.

        EXAMPLES::

            sage: GelfandTsetlinPattern([[7,3,1],[6,2],[4]]).is_strict()
            True
            sage: GelfandTsetlinPattern([[3,2,1],[3,1],[1]]).is_strict()
            True
            sage: GelfandTsetlinPattern([[6,0,0],[3,0],[2]]).is_strict()
            False
        """
    def row_sums(self) -> list:
        """
        Return the list of row sums.

        For a Gelfand-Tsetlin pattern `G`, the `i`-th row sum `d_i` is

        .. MATH::

            d_i = d_i(G) = \\sum_{j=i}^{n} a_{i,j}.

        EXAMPLES::

            sage: G = GelfandTsetlinPattern([[5,3,2,1,0],[4,3,2,0],[4,2,1],[3,2],[3]])
            sage: G.row_sums()
            [11, 9, 7, 5, 3]
            sage: G = GelfandTsetlinPattern([[3,2,1],[3,1],[2]])
            sage: G.row_sums()
            [6, 4, 2]
        """
    def weight(self) -> tuple:
        """
        Return the weight of ``self``.

        Define the weight of `G` to be the content of the tableau to which `G`
        corresponds under the bijection between Gelfand-Tsetlin patterns and
        semistandard tableaux.  More precisely,

        .. MATH::

            \\mathrm{wt}(G) = (d_n, d_{n-1}-d_n, \\dots, d_1-d_2),

        where the `d_i` are the row sums.

        EXAMPLES::

            sage: G = GelfandTsetlinPattern([[2,1,0],[1,0],[1]])
            sage: G.weight()
            (1, 0, 2)
            sage: G = GelfandTsetlinPattern([[4,2,1],[3,1],[2]])
            sage: G.weight()
            (2, 2, 3)
        """
    def Tokuyama_coefficient(self, name: str = 't'):
        """
        Return the Tokuyama coefficient attached to ``self``.

        Following the exposition of [BBF]_, Tokuyama's formula asserts

        .. MATH::

            \\sum_{G} (t+1)^{s(G)} t^{l(G)}
            z_1^{d_{n+1}} z_2^{d_{n}-d_{n+1}} \\cdots z_{n+1}^{d_1-d_2}
            =
            s_{\\lambda}(z_1,\\dots,z_{n+1}) \\prod_{i<j} (z_j+tz_i),

        where the sum is over all strict Gelfand-Tsetlin patterns with fixed
        top row `\\lambda + \\rho`, with `\\lambda` a partition with at most
        `n+1` parts and `\\rho = (n, n-1, \\ldots, 1, 0)`, and `s_\\lambda` is a
        Schur function.

        INPUT:

        - ``name`` -- (default: ``'t'``) an alternative name for the
          variable `t`

        EXAMPLES::

            sage: P = GelfandTsetlinPattern([[3,2,1],[2,2],[2]])
            sage: P.Tokuyama_coefficient()
            0
            sage: G = GelfandTsetlinPattern([[3,2,1],[3,1],[2]])
            sage: G.Tokuyama_coefficient()
            t^2 + t
            sage: G = GelfandTsetlinPattern([[2,1,0],[1,1],[1]])
            sage: G.Tokuyama_coefficient()
            0
            sage: G = GelfandTsetlinPattern([[5,3,2,1,0],[4,3,2,0],[4,2,1],[3,2],[3]])
            sage: G.Tokuyama_coefficient()
            t^8 + 3*t^7 + 3*t^6 + t^5
        """
    def bender_knuth_involution(self, i) -> GelfandTsetlinPattern:
        """
        Return the image of ``self`` under the `i`-th Bender-Knuth involution.

        If the triangle ``self`` has size `n` then this is defined for `0 < i < n`.

        The entries of ``self`` can take values in any ordered ring. Usually,
        this will be the integers but can also be the rationals or the real numbers.

        This implements the construction of the Bender-Knuth involution using toggling
        due to Berenstein-Kirillov.

        This agrees with the Bender-Knuth involution on semistandard tableaux.

        EXAMPLES::

            sage: G = GelfandTsetlinPattern([[5,3,2,1,0],[4,3,2,0],[4,2,1],[3,2],[3]])
            sage: G.bender_knuth_involution(2)
            [[5, 3, 2, 1, 0], [4, 3, 2, 0], [4, 2, 1], [4, 1], [3]]

            sage: G = GelfandTsetlinPattern([[3,2,0],[2.2,0],[2]])
            sage: G.bender_knuth_involution(2)
            [[3, 2, 0], [2.80000000000000, 2], [2]]

        TESTS::

            sage: all(all( G.bender_knuth_involution(i).to_tableau() == G.to_tableau().bender_knuth_involution(i)
            ....:       for i in range(1,len(G)) ) for G in GelfandTsetlinPatterns(top_row=[3,3,3,0,0]))
            True

            sage: G = GelfandTsetlinPattern([[2,1,0],[1,0],[0]])
            sage: G.bender_knuth_involution(0)
            Traceback (most recent call last):
            ...
            ValueError: must have 0 < 0 < 3
            sage: G.bender_knuth_involution(3)
            Traceback (most recent call last):
            ...
            ValueError: must have 0 < 3 < 3
        """

class GelfandTsetlinPatterns(UniqueRepresentation, Parent):
    """
    Gelfand-Tsetlin patterns.

    INPUT:

    - ``n`` -- the width or depth of the array, also known as the rank

    - ``k`` -- (default: ``None``) if specified, this is the maximum value that
      can occur in the patterns

    - ``top_row`` -- (default: ``None``) if specified, this is the fixed top
      row of all patterns

    - ``strict`` -- (default: ``False``) set to ``True`` if all patterns are
      strict patterns

    TESTS:

    Check that the number of Gelfand-Tsetlin patterns is equal to the number
    of semistandard Young tableaux::

        sage: G = GelfandTsetlinPatterns(3,3)
        sage: c = 0
        sage: from sage.combinat.crystals.kirillov_reshetikhin import partitions_in_box
        sage: for p in partitions_in_box(3,3):
        ....:    S = SemistandardTableaux(p, max_entry=3)
        ....:    c += S.cardinality()
        sage: c == G.cardinality()
        True

    Note that the top row in reverse of the Gelfand-Tsetlin pattern is the
    shape of the corresponding semistandard Young tableau under the bijection
    described in :meth:`GelfandTsetlinPattern.to_tableau()`::

        sage: G = GelfandTsetlinPatterns(top_row=[2,2,1])
        sage: S = SemistandardTableaux([2,2,1], max_entry=3)
        sage: G.cardinality() == S.cardinality()
        True
    """
    @staticmethod
    def __classcall_private__(cls, n=None, k=None, strict: bool = False, top_row=None):
        """
        Return the correct parent based upon the inputs.

        EXAMPLES::

            sage: G = GelfandTsetlinPatterns()
            sage: G2 = GelfandTsetlinPatterns()
            sage: G is G2
            True
            sage: G = GelfandTsetlinPatterns(3,4, strict=True)
            sage: G2 = GelfandTsetlinPatterns(int(3),int(4), strict=True)
            sage: G is G2
            True
            sage: G = GelfandTsetlinPatterns(top_row=[3,1,1])
            sage: G2 = GelfandTsetlinPatterns(top_row=(3,1,1))
            sage: G is G2
            True
        """
    def __init__(self, n, k, strict) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = GelfandTsetlinPatterns()
            sage: TestSuite(G).run()
            sage: G = GelfandTsetlinPatterns(3)
            sage: TestSuite(G).run()
            sage: G = GelfandTsetlinPatterns(3, 3)
            sage: TestSuite(G).run()
            sage: G = GelfandTsetlinPatterns(3, 3, strict=True)
            sage: TestSuite(G).run()
        """
    def __contains__(self, gt) -> bool:
        """
        Check to see if ``gt`` is in ``self``.

        EXAMPLES::

            sage: G = GelfandTsetlinPatterns()
            sage: [[3, 1],[2]] in G
            True
            sage: [[2, 3],[4]] in G
            False
            sage: [[3, 1],[0]] in G
            False
            sage: [] in G
            True
            sage: G = GelfandTsetlinPatterns(3,2)
            sage: [] in G
            False
            sage: [[2,0,0],[1,0],[1]] in G
            True
            sage: [[0,0],[0]] in G
            False
            sage: [[3,0,0],[2,0],[0]] in G
            False
            sage: G = GelfandTsetlinPatterns(3,strict=True)
            sage: [[2,1,0],[2,1],[1]] in G
            True
            sage: [[3,0,0],[3,0],[0]] in G
            False
        """
    Element = GelfandTsetlinPattern
    def __iter__(self):
        """
        Iterate through ``self`` by using a backtracing algorithm.

        EXAMPLES::

            sage: L = list(GelfandTsetlinPatterns(3,3))
            sage: c = 0
            sage: from sage.combinat.crystals.kirillov_reshetikhin import partitions_in_box
            sage: for p in partitions_in_box(3,3):
            ....:    S = SemistandardTableaux(p, max_entry=3)
            ....:    c += S.cardinality()
            sage: c == len(L)
            True
            sage: G = GelfandTsetlinPatterns(3, 3, strict=True)
            sage: all(x.is_strict() for x in G)
            True
            sage: G = GelfandTsetlinPatterns(k=3, strict=True)
            sage: all(x.is_strict() for x in G)
            True

        Checking iterator when the set is infinite::

            sage: T = GelfandTsetlinPatterns()
            sage: it = T.__iter__()
            sage: [next(it) for i in range(10)]
            [[],
             [[1]],
             [[2]],
             [[1, 1], [1]],
             [[3]],
             [[2, 1], [1]],
             [[2, 1], [2]],
             [[1, 1, 1], [1, 1], [1]],
             [[4]],
             [[3, 1], [1]]]
            sage: T = GelfandTsetlinPatterns(k=1)
            sage: it = T.__iter__()
            sage: [next(it) for i in range(10)]
            [[],
             [[0]],
             [[1]],
             [[0, 0], [0]],
             [[1, 0], [0]],
             [[1, 0], [1]],
             [[1, 1], [1]],
             [[0, 0, 0], [0, 0], [0]],
             [[1, 0, 0], [0, 0], [0]],
             [[1, 0, 0], [1, 0], [0]]]

        Check that :issue:`14718` is fixed::

            sage: T = GelfandTsetlinPatterns(1,3)
            sage: list(T)
            [[[0]],
             [[1]],
             [[2]],
             [[3]]]
        """
    def random_element(self) -> GelfandTsetlinPattern:
        """
        Return a uniformly random Gelfand-Tsetlin pattern.

        EXAMPLES::

            sage: g = GelfandTsetlinPatterns(4, 5)
            sage: x = g.random_element()
            sage: x in g
            True
            sage: len(x)
            4
            sage: all(y in range(5+1) for z in x for y in z)
            True
            sage: x.check()

        ::

            sage: g = GelfandTsetlinPatterns(4, 5, strict=True)
            sage: x = g.random_element()
            sage: x in g
            True
            sage: len(x)
            4
            sage: all(y in range(5+1) for z in x for y in z)
            True
            sage: x.check()
            sage: x.is_strict()
            True
        """

class GelfandTsetlinPatternsTopRow(GelfandTsetlinPatterns):
    """
    Gelfand-Tsetlin patterns with a fixed top row.
    """
    def __init__(self, top_row, strict) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: G = GelfandTsetlinPatterns(top_row=[4,4,3,1])
            sage: TestSuite(G).run()

        TESTS:

        Check a border case in :issue:`14765`::

            sage: G = GelfandTsetlinPatterns(top_row=[])
            sage: list(G)
            [[]]
        """
    def __contains__(self, gt) -> bool:
        """
        Check if ``gt`` is in ``self``.

        EXAMPLES::

            sage: G = GelfandTsetlinPatterns(top_row=[4,4,1])
            sage: [[4,4,1], [4,2], [3]] in G
            True
            sage: [[4,3,1], [4,2], [3]] in G
            False
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: G = GelfandTsetlinPatterns(top_row=[4,2,1])
            sage: list(G)
            [[[4, 2, 1], [2, 1], [1]],
             [[4, 2, 1], [2, 1], [2]],
             [[4, 2, 1], [2, 2], [2]],
             [[4, 2, 1], [3, 1], [1]],
             [[4, 2, 1], [3, 1], [2]],
             [[4, 2, 1], [3, 1], [3]],
             [[4, 2, 1], [3, 2], [2]],
             [[4, 2, 1], [3, 2], [3]],
             [[4, 2, 1], [4, 1], [1]],
             [[4, 2, 1], [4, 1], [2]],
             [[4, 2, 1], [4, 1], [3]],
             [[4, 2, 1], [4, 1], [4]],
             [[4, 2, 1], [4, 2], [2]],
             [[4, 2, 1], [4, 2], [3]],
             [[4, 2, 1], [4, 2], [4]]]
        """
    def top_row(self):
        """
        Return the top row of ``self``.

        EXAMPLES::

            sage: G = GelfandTsetlinPatterns(top_row=[4,4,3,1])
            sage: G.top_row()
            (4, 4, 3, 1)
        """
    def Tokuyama_formula(self, name: str = 't'):
        """
        Return the Tokuyama formula of ``self``.

        Following the exposition of [BBF]_, Tokuyama's formula asserts

        .. MATH::

            \\sum_{G} (t+1)^{s(G)} t^{l(G)}
            z_1^{d_{n+1}} z_2^{d_{n}-d_{n+1}} \\cdots z_{n+1}^{d_1-d_2}
            = s_{\\lambda} (z_1, \\ldots, z_{n+1}) \\prod_{i<j} (z_j+tz_i),

        where the sum is over all strict Gelfand-Tsetlin patterns with fixed
        top row `\\lambda+\\rho`, with `\\lambda` a partition with at most
        `n+1` parts and `\\rho = (n,n-1,\\dots,1,0)`, and `s_{\\lambda}` is a Schur
        function.

        INPUT:

        - ``name`` -- (default: ``'t'``) an alternative name for the
          variable `t`

        EXAMPLES::

            sage: GT = GelfandTsetlinPatterns(top_row=[2,1,0],strict=True)
            sage: GT.Tokuyama_formula()
            t^3*x1^2*x2 + t^2*x1*x2^2 + t^2*x1^2*x3 + t^2*x1*x2*x3 + t*x1*x2*x3 + t*x2^2*x3 + t*x1*x3^2 + x2*x3^2
            sage: GT = GelfandTsetlinPatterns(top_row=[3,2,1],strict=True)
            sage: GT.Tokuyama_formula()
            t^3*x1^3*x2^2*x3 + t^2*x1^2*x2^3*x3 + t^2*x1^3*x2*x3^2 + t^2*x1^2*x2^2*x3^2 + t*x1^2*x2^2*x3^2 + t*x1*x2^3*x3^2 + t*x1^2*x2*x3^3 + x1*x2^2*x3^3
            sage: GT = GelfandTsetlinPatterns(top_row=[1,1,1],strict=True)
            sage: GT.Tokuyama_formula()
            0
        """
    def random_element(self) -> GelfandTsetlinPattern:
        """
        Return a uniformly random Gelfand-Tsetlin pattern with specified top row.

        EXAMPLES::

            sage: g = GelfandTsetlinPatterns(top_row = [4, 3, 1, 1])
            sage: x = g.random_element()
            sage: x in g
            True
            sage: x[0] == [4, 3, 1, 1]
            True
            sage: x.check()

            sage: g = GelfandTsetlinPatterns(top_row=[4, 3, 2, 1], strict=True)
            sage: x = g.random_element()
            sage: x in g
            True
            sage: x[0] == [4, 3, 2, 1]
            True
            sage: x.is_strict()
            True
            sage: x.check()
        """
