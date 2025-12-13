from sage.categories.infinite_enumerated_sets import InfiniteEnumeratedSets as InfiniteEnumeratedSets
from sage.combinat.composition import Composition as Composition
from sage.combinat.partition import Partition as Partition
from sage.combinat.permutation import Permutations as Permutations
from sage.combinat.skew_partition import SkewPartition as SkewPartition
from sage.combinat.skew_tableau import SkewTableaux as SkewTableaux
from sage.combinat.tableau import Tableau as Tableau
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.element import Matrix as Matrix
from sage.structure.list_clone import ClonableArray as ClonableArray
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class Diagram(ClonableArray, metaclass=InheritComparisonClasscallMetaclass):
    """
    Combinatorial diagrams with positions indexed by rows and columns.

    The positions are indexed by rows and columns as in a matrix. For example,
    a Ferrers diagram is a diagram obtained from a partition
    `\\lambda = (\\lambda_0, \\lambda_1, \\ldots, \\lambda_{\\ell})`, where the
    cells are in rows `i` for `0 \\leq i \\leq \\ell` and the cells in row `i`
    consist of `(i,j)` for `0 \\leq j < \\lambda_i`. In English notation, the
    indices are read from top left to bottom right as in a matrix.

    Indexing conventions are the same as
    :class:`~sage.combinat.partition.Partition`. Printing the diagram of a
    partition, however, will always be in English notation.

    EXAMPLES:

    To create an arbitrary diagram, pass a list of all cells::

        sage: from sage.combinat.diagram import Diagram
        sage: cells = [(0,0), (0,1), (1,0), (1,1), (4,4), (4,5), (4,6), (5,4), (7, 6)]
        sage: D = Diagram(cells); D
        [(0, 0), (0, 1), (1, 0), (1, 1), (4, 4), (4, 5), (4, 6), (5, 4), (7, 6)]

    We can visualize the diagram by printing ``O``'s and ``.``'s. ``O``'s are
    present in the cells which are present in the diagram and a ``.`` represents
    the absence of a cell in the diagram::

        sage: D.pp()
        O O . . . . .
        O O . . . . .
        . . . . . . .
        . . . . . . .
        . . . . O O O
        . . . . O . .
        . . . . . . .
        . . . . . . O

    We can also check if certain cells are contained in a given diagram::

        sage: (1, 0) in D
        True
        sage: (2, 2) in D
        False

    If you know that there are entire empty rows or columns at the end of the
    diagram, you can manually pass them with keyword arguments ``n_rows=`` or
    ``n_cols=``::

        sage: Diagram([(0,0), (0,3), (2,2), (2,4)]).pp()
        O . . O .
        . . . . .
        . . O . O
        sage: Diagram([(0,0), (0,3), (2,2), (2,4)], n_rows=6, n_cols=6).pp()
        O . . O . .
        . . . . . .
        . . O . O .
        . . . . . .
        . . . . . .
        . . . . . .
    """
    @staticmethod
    def __classcall_private__(self, cells, n_rows=None, n_cols=None, check: bool = True):
        """
        Normalize the input so that it lives in the correct parent.

        EXAMPLES::

            sage: from sage.combinat.diagram import Diagram
            sage: D = Diagram([(0,0), (0,3), (2,2), (2,4)])
            sage: D.parent()
            Combinatorial diagrams
        """
    def __init__(self, parent, cells, n_rows=None, n_cols=None, check: bool = True) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.combinat.diagram import Diagram
            sage: D1 = Diagram([(0,2),(0,3),(1,1),(3,2)])
            sage: D1.cells()
            [(0, 2), (0, 3), (1, 1), (3, 2)]
            sage: D1.nrows()
            4
            sage: D1.ncols()
            4
            sage: TestSuite(D1).run()

        We can specify the number of rows and columns explicitly,
        in case they are supposed to be empty::

            sage: D2 = Diagram([(0,2),(0,3),(1,1),(3,2)], n_cols=5)
            sage: D2.cells()
            [(0, 2), (0, 3), (1, 1), (3, 2)]
            sage: D2.ncols()
            5
            sage: D2.pp()
            . . O O .
            . O . . .
            . . . . .
            . . O . .
            sage: TestSuite(D2).run()
        """
    def pp(self) -> None:
        """
        Return a visualization of the diagram.

        Cells which are present in the
        diagram are filled with a ``O``. Cells which are not present in the
        diagram are filled with a ``.``.

        EXAMPLES::

            sage: from sage.combinat.diagram import Diagram
            sage: Diagram([(0,0), (0,3), (2,2), (2,4)]).pp()
            O . . O .
            . . . . .
            . . O . O
            sage: Diagram([(0,0), (0,3), (2,2), (2,4)], n_rows=6, n_cols=6).pp()
            O . . O . .
            . . . . . .
            . . O . O .
            . . . . . .
            . . . . . .
            . . . . . .
            sage: Diagram([]).pp()
            -
        """
    def number_of_rows(self):
        """
        Return the total number of rows of ``self``.

        EXAMPLES:

        The following example has three rows which are filled, but they
        are contained in rows 0 to 3 (for a total of four)::

            sage: from sage.combinat.diagram import Diagram
            sage: D1 = Diagram([(0,2),(0,3),(1,1),(3,2)])
            sage: D1.number_of_rows()
            4
            sage: D1.nrows()
            4

        The total number of rows includes including those which are empty.
        We can also include empty rows at the end::

            sage: from sage.combinat.diagram import Diagram
            sage: D = Diagram([(0,2),(0,3),(1,1),(3,2)], n_rows=6)
            sage: D.number_of_rows()
            6
            sage: D.pp()
            . . O O
            . O . .
            . . . .
            . . O .
            . . . .
            . . . .
        """
    nrows = number_of_rows
    def number_of_cols(self):
        """
        Return the total number of rows of ``self``.

        EXAMPLES:

        The following example has three columns which are filled, but they
        are contained in rows 0 to 3 (for a total of four)::

            sage: from sage.combinat.diagram import Diagram
            sage: D = Diagram([(0,2),(0,3),(1,1),(3,2)])
            sage: D.number_of_cols()
            4
            sage: D.ncols()
            4

        We can also include empty columns at the end::

            sage: from sage.combinat.diagram import Diagram
            sage: D = Diagram([(0,2),(0,3),(1,1),(3,2)], n_cols=6)
            sage: D.number_of_cols()
            6
            sage: D.pp()
            . . O O . .
            . O . . . .
            . . . . . .
            . . O . . .
        """
    ncols = number_of_cols
    def cells(self):
        """
        Return a ``list`` of the cells contained in the diagram ``self``.

        EXAMPLES::

            sage: from sage.combinat.diagram import Diagram
            sage: D1 = Diagram([(0,2),(0,3),(1,1),(3,2)])
            sage: D1.cells()
            [(0, 2), (0, 3), (1, 1), (3, 2)]
        """
    def number_of_cells(self):
        """
        Return the total number of cells contained in the diagram ``self``.

        EXAMPLES::

            sage: from sage.combinat.diagram import Diagram
            sage: D1 = Diagram([(0,2),(0,3),(1,1),(3,2)])
            sage: D1.number_of_cells()
            4
            sage: D1.n_cells()
            4
        """
    n_cells = number_of_cells
    size = number_of_cells
    def check(self) -> None:
        """
        Check that this is a valid diagram.

        EXAMPLES::

            sage: from sage.combinat.diagram import Diagram
            sage: D = Diagram([(0,0), (0,3), (2,2), (2,4)])
            sage: D.check()

        In the next two examples, a bad diagram is passed.
        The first example fails because one cell is indexed by negative
        integers::

            sage: D = Diagram([(0,0), (0,-3), (2,2), (2,4)])
            Traceback (most recent call last):
            ...
            ValueError: diagrams must be indexed by nonnegative integers

        The next example fails because one cell is indexed by rational
        numbers::

            sage: D = Diagram([(0,0), (0,3), (2/3,2), (2,4)])
            Traceback (most recent call last):
            ...
            ValueError: diagrams must be indexed by nonnegative integers
        """
    def specht_module(self, base_ring=None):
        """
        Return the Specht module corresponding to ``self``.

        EXAMPLES::

            sage: from sage.combinat.diagram import Diagram
            sage: D = Diagram([(0,0), (1,1), (2,2), (2,3)])
            sage: SM = D.specht_module(QQ)                                              # needs sage.modules
            sage: s = SymmetricFunctions(QQ).s()                                        # needs sage.modules
            sage: s(SM.frobenius_image())                                               # needs sage.modules
            s[2, 1, 1] + s[2, 2] + 2*s[3, 1] + s[4]
        """
    def specht_module_dimension(self, base_ring=None):
        """
        Return the dimension of the Specht module corresponding to ``self``.

        INPUT:

        - ``base_ring`` -- (default: `\\QQ`) the base ring

        EXAMPLES::

            sage: from sage.combinat.diagram import Diagram
            sage: D = Diagram([(0,0), (1,1), (2,2), (2,3)])
            sage: D.specht_module_dimension()                                           # needs sage.modules
            12
            sage: D.specht_module(QQ).dimension()                                       # needs sage.modules
            12
        """
    @cached_method
    def essential_set(self):
        """
        Return the essential set of ``self`` as defined by Fulton.

        Let `D` be a diagram. Then the *essential set* of `D` are the
        cells `(i, j) \\in D` such that `(i+1, j) \\notin D` and
        `(i, j+1) \\notin D`; that is, the maximally southwest elements
        in each connected component of `D`.

        EXAMPLES::

            sage: w = Permutation([2, 1, 5, 4, 3])
            sage: D = w.rothe_diagram()
            sage: D.essential_set()
            ((0, 0), (2, 3), (3, 2))
        """

class Diagrams(UniqueRepresentation, Parent):
    """
    The class of combinatorial diagrams.

    A *combinatorial diagram* is a set of cells indexed by pairs of natural
    numbers. Calling an instance of :class:`Diagrams` is one way to construct
    diagrams.

    EXAMPLES::

        sage: from sage.combinat.diagram import Diagrams
        sage: Dgms = Diagrams()
        sage: D = Dgms([(0,0), (0,3), (2,2), (2,4)])
        sage: D.parent()
        Combinatorial diagrams
    """
    def __init__(self, category=None) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: from sage.combinat.diagram import Diagrams
            sage: Dgms = Diagrams(); Dgms
            Combinatorial diagrams

        TESTS::

            sage: TestSuite(Dgms).run()
        """
    def __iter__(self):
        """
        Iterate over ``self``.

        EXAMPLES::

            sage: from sage.combinat.diagram import Diagrams
            sage: I = iter(Diagrams())
            sage: for i in range(10):
            ....:   print(next(I))
            []
            [(0, 0)]
            [(1, 0)]
            [(0, 0), (1, 0)]
            [(0, 1)]
            [(0, 0), (0, 1)]
            [(0, 1), (1, 0)]
            [(0, 0), (0, 1), (1, 0)]
            [(2, 0)]
            [(0, 0), (2, 0)]
            sage: next(I).parent()
            Combinatorial diagrams

            sage: from sage.combinat.diagram import NorthwestDiagrams
            sage: I = iter(NorthwestDiagrams())
            sage: for i in range(20):
            ....:   print(next(I))
            []
            [(0, 0)]
            [(1, 0)]
            [(0, 0), (1, 0)]
            [(0, 1)]
            [(0, 0), (0, 1)]
            [(0, 0), (0, 1), (1, 0)]
            [(2, 0)]
            [(0, 0), (2, 0)]
            [(1, 0), (2, 0)]
            [(0, 0), (1, 0), (2, 0)]
            [(0, 0), (0, 1), (2, 0)]
            [(0, 0), (0, 1), (1, 0), (2, 0)]
            [(1, 1)]
            [(0, 0), (1, 1)]
            [(1, 0), (1, 1)]
            [(0, 0), (1, 0), (1, 1)]
            [(0, 1), (1, 1)]
            [(0, 0), (0, 1), (1, 1)]
            [(0, 0), (0, 1), (1, 0), (1, 1)]
        """
    def from_polyomino(self, p):
        """
        Create the diagram corresponding to a 2d
        :class:`~sage.combinat.tiling.Polyomino`

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino                            # needs sage.modules
            sage: p = Polyomino([(0,0),(1,0),(1,1),(1,2)])                              # needs sage.modules
            sage: from sage.combinat.diagram import Diagrams
            sage: Diagrams()(p).pp()                                                    # needs sage.modules
            O . .
            O O O

        We can also call this method directly::

            sage: Diagrams().from_polyomino(p).pp()                                     # needs sage.modules
            O . .
            O O O

        This only works for a 2d :class:`~sage.combinat.tiling.Polyomino`::

            sage: p = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')     # needs sage.modules
            sage: Diagrams().from_polyomino(p)                                          # needs sage.modules
            Traceback (most recent call last):
            ...
            ValueError: the polyomino must be 2 dimensional
        """
    def from_composition(self, alpha):
        """
        Create the diagram corresponding to a weak composition `\\alpha \\vDash n`.

        EXAMPLES::

            sage: alpha = Composition([3,0,2,1,4,4])
            sage: from sage.combinat.diagram import Diagrams
            sage: Diagrams()(alpha).pp()
            O O O .
            . . . .
            O O . .
            O . . .
            O O O O
            O O O O
            sage: Diagrams().from_composition(alpha).pp()
            O O O .
            . . . .
            O O . .
            O . . .
            O O O O
            O O O O
        """
    def from_zero_one_matrix(self, M, check: bool = True):
        """
        Get a diagram from a matrix with entries in `\\{0, 1\\}`, where
        positions of cells are indicated by the `1`'s.

        EXAMPLES::

            sage: M = matrix([[1,0,1,1],[0,1,1,0]])                                     # needs sage.modules
            sage: from sage.combinat.diagram import Diagrams
            sage: Diagrams()(M).pp()                                                    # needs sage.modules
            O . O O
            . O O .
            sage: Diagrams().from_zero_one_matrix(M).pp()                               # needs sage.modules
            O . O O
            . O O .

            sage: M = matrix([[1, 0, 0], [1, 0, 0], [0, 0, 0]])                         # needs sage.modules
            sage: Diagrams()(M).pp()                                                    # needs sage.modules
            O . .
            O . .
            . . .
        """
    Element = Diagram

class NorthwestDiagram(Diagram, metaclass=InheritComparisonClasscallMetaclass):
    """
    Diagrams with the northwest property.

    A diagram is a set of cells indexed by natural numbers. Such a diagram
    has the *northwest property* if the presence of cells `(i1, j1)` and
    `(i2, j2)` implies the presence of the cell
    `(\\min(i1, i2), \\min(j1, j2))`. Diagrams with the northwest property are
    called *northwest diagrams*.

    For general diagrams see :class:`Diagram`.

    EXAMPLES::

        sage: from sage.combinat.diagram import NorthwestDiagram
        sage: N = NorthwestDiagram([(0,0), (0, 2), (2,0)])

    To visualize them, use the ``.pp()`` method::

        sage: N.pp()
        O . O
        . . .
        O . .
    """
    @staticmethod
    def __classcall_private__(self, cells, n_rows=None, n_cols=None, check: bool = True):
        """
        Normalize input to ensure a correct parent. This method also allows
        one to specify whether or not to check the northwest property for the
        provided cells.

        EXAMPLES::

            sage: from sage.combinat.diagram import NorthwestDiagram, NorthwestDiagrams
            sage: N1 = NorthwestDiagram([(0,1), (0,2)])
            sage: N2 = NorthwestDiagram([(0,1), (0,3)])
            sage: N1.parent() is N2.parent()
            True
            sage: N3 = NorthwestDiagrams()([(0,1), (0,2)])
            sage: N3.parent() is NorthwestDiagrams()
            True
            sage: N1.parent() is NorthwestDiagrams()
            True
        """
    def check(self) -> None:
        """
        A diagram has the northwest property if the presence of cells
        `(i1, j1)` and `(i2, j2)` implies the presence of the cell
        `(min(i1, i2), min(j1, j2))`. This method checks if the northwest
        property is satisfied for ``self``

        EXAMPLES::

            sage: from sage.combinat.diagram import NorthwestDiagram
            sage: N = NorthwestDiagram([(0,0), (0,3), (3,0)])
            sage: N.check()

        Here is a non-example::

            sage: notN = NorthwestDiagram([(0,1), (1,0)])  #.check() is implicit
            Traceback (most recent call last):
            ...
            ValueError: diagram is not northwest

        TESTS::

            sage: NorthwestDiagram([(0,1/2)])
            Traceback (most recent call last):
            ...
            ValueError: diagrams must be indexed by nonnegative integers
        """
    def peelable_tableaux(self):
        """
        Return the set of peelable tableaux whose diagram is ``self``.

        For a fixed northwest diagram `D`, we say that a Young tableau `T` is
        `D`-peelable if:

        1. the row indices of the cells in the first column of `D` are
           the entries in an initial segment in the first column of `T` and
        2. the tableau `Q` obtained by removing those cells from `T` and playing
           jeu de taquin is `(D-C)`-peelable, where `D-C` is the diagram formed
           by forgetting the first column of `D`.

        Reiner and Shimozono [RS1995]_ showed that the number
        `\\operatorname{red}(w)` of reduced words of a permutation `w` may be
        computed using the peelable tableaux of the Rothe diagram `D(w)`.
        Explicitly,

        .. MATH::

            \\operatorname{red}(w) = \\sum_{T} f_{\\operatorname{shape} T},

        where the sum runs over the `D(w)`-peelable tableaux `T` and `f_\\lambda`
        is the number of standard Young tableaux of shape `\\lambda` (which may
        be computed using the hook-length formula).

        EXAMPLES:

        We can compute the `D`-peelable diagrams for a northwest diagram `D`::

            sage: from sage.combinat.diagram import NorthwestDiagram
            sage: cells = [(0,0), (0,1), (0,2), (1,0), (2,0), (2,2), (2,4),
            ....:          (4,0), (4,2)]
            sage: D = NorthwestDiagram(cells); D.pp()
            O O O . .
            O . . . .
            O . O . O
            . . . . .
            O . O . .
            sage: D.peelable_tableaux()
            {[[1, 1, 1], [2, 3, 3], [3, 5], [5]],
            [[1, 1, 1, 3], [2, 3], [3, 5], [5]]}

        EXAMPLES:

        If the diagram is only one column, there is only one peelable tableau::

            sage: from sage.combinat.diagram import NorthwestDiagram
            sage: NWD = NorthwestDiagram([(0,0), (2,0)])
            sage: NWD.peelable_tableaux()
            {[[1], [3]]}

        From [RS1995]_, we know that there is only one peelable tableau for the
        Rothe diagram of the permutation (in one line notation) `251643`::

            sage: D = NorthwestDiagram([(1, 2), (1, 3), (3, 2), (3, 3), (4, 2)])
            sage: D.pp()
            . . . .
            . . O O
            . . . .
            . . O O
            . . O .

            sage: D.peelable_tableaux()
            {[[2, 2], [4, 4], [5]]}

        Here are all the intermediate steps to compute the peelables for the
        Rothe diagram of (in one-line notation) `64817235`. They are listed from
        deepest in the recursion to the final step. The recursion has depth five
        in this case so we will label the intermediate tableaux by `D_i` where
        `i` is the step in the recursion at which they appear.

        Start with the one that has a single column::

            sage: D5 = NorthwestDiagram([(2,0)]); D5.pp()
            .
            .
            O
            sage: D5.peelable_tableaux()
            {[[3]]}

        Now we know all of the `D_5` peelables, so we can compute the `D_4`
        peelables::

            sage: D4 = NorthwestDiagram([(0, 0), (2,0), (4, 0), (2, 2)])
            sage: D4.pp()
            O . .
            . . .
            O . O
            . . .
            O . .

            sage: D4.peelable_tableaux()
            {[[1, 3], [3], [5]]}

        There is only one `D_4` peelable, so we can compute the `D_3`
        peelables::

            sage: D3 = NorthwestDiagram([(0,0), (0,1), (2, 1), (2, 3), (4,1)])
            sage: D3.pp()
            O O . .
            . . . .
            . O . O
            . . . .
            . O . .

            sage: D3.peelable_tableaux()
            {[[1, 1], [3, 3], [5]], [[1, 1, 3], [3], [5]]}

        Now compute the `D_2` peelables::

            sage: cells = [(0,0), (0,1), (0,2), (1,0), (2,0), (2,2), (2,4),
            ....:          (4,0), (4,2)]
            sage: D2 = NorthwestDiagram(cells); D2.pp()
            O O O . .
            O . . . .
            O . O . O
            . . . . .
            O . O . .

            sage: D2.peelable_tableaux()
            {[[1, 1, 1], [2, 3, 3], [3, 5], [5]],
            [[1, 1, 1, 3], [2, 3], [3, 5], [5]]}

        And the `D_1` peelables::

            sage: cells = [(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (2,0),
            ....:          (2,1), (2,3), (2,5), (4,0), (4,1), (4,3)]
            sage: D1 = NorthwestDiagram(cells); D1.pp()
            O O O O . .
            O O . . . .
            O O . O . O
            . . . . . .
            O O . O . .

            sage: D1.peelable_tableaux()
            {[[1, 1, 1, 1], [2, 2, 3, 3], [3, 3, 5], [5, 5]],
            [[1, 1, 1, 1, 3], [2, 2, 3], [3, 3, 5], [5, 5]]}

        Which we can use to get the `D` peelables::

            sage: cells = [(0,0), (0,1), (0,2), (0,3), (0,4),
            ....:          (1,0), (1,1), (1,2),
            ....:          (2,0), (2,1), (2,2), (2,4), (2,6),
            ....:                 (4,1), (4,2), (4,4)]
            sage: D = NorthwestDiagram(cells); D.pp()
            O O O O O . .
            O O O . . . .
            O O O . O . O
            . . . . . . .
            . O O . O . .
            sage: D.peelable_tableaux()
            {[[1, 1, 1, 1, 1], [2, 2, 2, 3, 3], [3, 3, 3], [5, 5, 5]],
             [[1, 1, 1, 1, 1], [2, 2, 2, 3, 3], [3, 3, 3, 5], [5, 5]],
             [[1, 1, 1, 1, 1, 3], [2, 2, 2, 3], [3, 3, 3], [5, 5, 5]],
             [[1, 1, 1, 1, 1, 3], [2, 2, 2, 3], [3, 3, 3, 5], [5, 5]]}

        ALGORITHM:

        This implementation uses the algorithm suggested in Remark 25
        of [RS1995]_.

        TESTS:

        Corner case::

            sage: from sage.combinat.diagram import NorthwestDiagram
            sage: D = NorthwestDiagram([])
            sage: D.peelable_tableaux()
            {[]}
        """

class NorthwestDiagrams(Diagrams):
    '''
    Diagrams satisfying the northwest property.

    A diagram `D` is a *northwest diagram* if for every two cells `(i_1, j_1)`
    and `(i_2, j_2)` in `D` then there exists the cell
    `(\\min(i_1, i_2), \\min(j_1, j_2)) \\in D`.

    EXAMPLES::

        sage: from sage.combinat.diagram import NorthwestDiagram
        sage: N = NorthwestDiagram([(0,0), (0, 10), (5,0)]); N.pp()
        O . . . . . . . . . O
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        O . . . . . . . . . .

    Note that checking whether or not the northwest property is satisfied is
    automatically checked. The diagram found by adding the cell `(1,1)` to the
    diagram above is *not* a northwest diagram. The cell `(1,0)` should be
    present due to the presence of `(5,0)` and `(1,1)`::

        sage: from sage.combinat.diagram import Diagram
        sage: Diagram([(0, 0), (0, 10), (5, 0), (1, 1)]).pp()
        O . . . . . . . . . O
        . O . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        O . . . . . . . . . .
        sage: NorthwestDiagram([(0, 0), (0, 10), (5, 0), (1, 1)])
        Traceback (most recent call last):
        ...
        ValueError: diagram is not northwest

    However, this behavior can be turned off if you are confident that
    you are providing a northwest diagram::

        sage: N = NorthwestDiagram([(0, 0), (0, 10), (5, 0),
        ....:                      (1, 1), (0, 1), (1, 0)],
        ....:                      check=False)
        sage: N.pp()
        O O . . . . . . . . O
        O O . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        O . . . . . . . . . .

    Note that arbitrary diagrams which happen to be northwest diagrams
    only live in the parent of :class:`Diagrams`::

        sage: D = Diagram([(0, 0), (0, 10), (5, 0), (1, 1), (0, 1), (1, 0)])
        sage: D.pp()
        O O . . . . . . . . O
        O O . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        . . . . . . . . . . .
        O . . . . . . . . . .
        sage: from sage.combinat.diagram import NorthwestDiagrams
        sage: D in NorthwestDiagrams()
        False

    Here are some more examples::

        sage: from sage.combinat.diagram import NorthwestDiagram, NorthwestDiagrams
        sage: D = NorthwestDiagram([(0,1), (0,2), (1,1)]); D.pp()
        . O O
        . O .
        sage: NWDgms = NorthwestDiagrams()
        sage: D = NWDgms([(1,1), (1,2), (2,1)]); D.pp()
        . . .
        . O O
        . O .
        sage: D.parent()
        Combinatorial northwest diagrams

    Additionally, there are natural constructions of a northwest diagram
    given the data of a permutation (Rothe diagrams are the prototypical example
    of northwest diagrams), or the data of a partition of an integer, or a
    skew partition.

    The Rothe diagram `D(\\omega)` of a permutation `\\omega` is specified by
    the cells

    .. MATH::

        D(\\omega) = \\{(\\omega_j, i) : i<j,\\, \\omega_i > \\omega_j \\}.

    We can construct one by calling :meth:`rothe_diagram` method on the set
    of all :class:`~sage.combinat.diagram.NorthwestDiagrams`::

        sage: w = Permutations(4)([4,3,2,1])
        sage: NorthwestDiagrams().rothe_diagram(w).pp()
        O O O .
        O O . .
        O . . .
        . . . .

    To turn a Ferrers diagram into a northwest diagram, we may call
    :meth:`from_partition`. This will return a Ferrer\'s diagram in the
    set of all northwest diagrams. For many use-cases it is probably better
    to get Ferrer\'s diagrams by the corresponding method on partitions, namely
    :meth:`sage.combinat.partitions.Partitions.ferrers_diagram`::

        sage: mu = Partition([7,3,1,1])
        sage: mu.pp()
        *******
        ***
        *
        *
        sage: NorthwestDiagrams().from_partition(mu).pp()
        O O O O O O O
        O O O . . . .
        O . . . . . .
        O . . . . . .

    It is also possible to turn a Ferrers diagram of a skew partition into a
    northwest diagram, although it is more subtle than just using the skew
    diagram itself. One must first reflect the partition about a vertical axis
    so that the skew partition looks "backwards"::

        sage: mu, nu = Partition([5,4,3,2,1]), Partition([3,2,1])
        sage: s = mu/nu; s.pp()
           **
          **
         **
        **
        *
        sage: NorthwestDiagrams().from_skew_partition(s).pp()
        O O . . .
        . O O . .
        . . O O .
        . . . O O
        . . . . O
    '''
    def rothe_diagram(self, w):
        '''
        Return the Rothe diagram of ``w``.

        We construct a northwest diagram from a permutation by
        constructing its Rothe diagram. Formally, if `\\omega` is
        a :class:`~sage.combinat.permutation.Permutation`
        then the Rothe diagram `D(\\omega)` is the diagram whose cells are

        .. MATH::

            D(\\omega) = \\{(\\omega_j, i) : i<j,\\, \\omega_i > \\omega_j \\}.

        Informally, one can construct the Rothe diagram by starting with all
        `n^2` possible cells, and then deleting the cells `(i, \\omega(i))` as
        well as all cells to the right and below. (These are sometimes called
        "death rays".)

        .. SEEALSO::

            :func:`~sage.combinat.diagram.RotheDiagram`

        EXAMPLES::

            sage: from sage.combinat.diagram import NorthwestDiagrams
            sage: w = Permutations(3)([2,1,3])
            sage: NorthwestDiagrams().rothe_diagram(w).pp()
            O . .
            . . .
            . . .
            sage: NorthwestDiagrams().from_permutation(w).pp()
            O . .
            . . .
            . . .

            sage: w = Permutations(8)([2,5,4,1,3,6,7,8])
            sage: NorthwestDiagrams().rothe_diagram(w).pp()
            O . . . . . . .
            O . O O . . . .
            O . O . . . . .
            . . . . . . . .
            . . . . . . . .
            . . . . . . . .
            . . . . . . . .
            . . . . . . . .
        '''
    from_permutation = rothe_diagram
    def from_partition(self, mu):
        '''
        Return the Ferrer\'s diagram of ``mu`` as a northwest diagram.

        EXAMPLES::

            sage: mu = Partition([5,2,1]); mu.pp()
            *****
            **
            *
            sage: mu.parent()
            Partitions
            sage: from sage.combinat.diagram import NorthwestDiagrams
            sage: D = NorthwestDiagrams().from_partition(mu)
            sage: D.pp()
            O O O O O
            O O . . .
            O . . . .
            sage: D.parent()
            Combinatorial northwest diagrams

        This will print in English notation even if the notation is set to
        French for the partition::

            sage: Partitions.options.convention="french"
            sage: mu.pp()
            *
            **
            *****
            sage: D.pp()
            O O O O O
            O O . . .
            O . . . .

        TESTS::

            sage: from sage.combinat.diagram import NorthwestDiagrams
            sage: mu = [5, 2, 1]
            sage: D = NorthwestDiagrams().from_partition(mu)
            Traceback (most recent call last):
            ...
            ValueError: mu must be a Partition
        '''
    def from_skew_partition(self, s):
        """
        Get the northwest diagram found by reflecting a skew shape across
        a vertical plane.

        EXAMPLES::

            sage: mu, nu = Partition([3,2,1]), Partition([2,1])
            sage: s = mu/nu; s.pp()
              *
             *
            *
            sage: from sage.combinat.diagram import NorthwestDiagrams
            sage: D = NorthwestDiagrams().from_skew_partition(s)
            sage: D.pp()
            O . .
            . O .
            . . O

            sage: mu, nu = Partition([3,3,2]), Partition([2,2,2])
            sage: s = mu/nu; s.pp()
              *
              *
            sage: NorthwestDiagrams().from_skew_partition(s).pp()
            O . .
            O . .
            . . .

        TESTS::

            sage: mu = Partition([3,2,1])
            sage: NorthwestDiagrams().from_skew_partition(mu)
            Traceback (most recent call last):
            ...
            ValueError: mu must be a SkewPartition
        """
    def from_parallelogram_polyomino(self, p):
        """
        Create the diagram corresponding to a
        :class:`~sage.combinat.parallelogram_polyomino.ParallelogramPolyomino`.

        EXAMPLES::

            sage: p = ParallelogramPolyomino([[0, 0, 1, 0, 0, 0, 1, 1],                 # needs sage.modules
            ....:                              [1, 1, 0, 1, 0, 0, 0, 0]])
            sage: from sage.combinat.diagram import NorthwestDiagrams
            sage: NorthwestDiagrams().from_parallelogram_polyomino(p).pp()              # needs sage.modules
            O O .
            O O O
            . O O
            . O O
            . O O
        """
    Element = NorthwestDiagram

def RotheDiagram(w):
    """
    The Rothe diagram of a permutation ``w``.

    EXAMPLES::

        sage: w = Permutations(9)([1, 7, 4, 5, 9, 3, 2, 8, 6])
        sage: from sage.combinat.diagram import RotheDiagram
        sage: D = RotheDiagram(w); D.pp()
        . . . . . . . . .
        . O O O O O . . .
        . O O . . . . . .
        . O O . . . . . .
        . O O . . O . O .
        . O . . . . . . .
        . . . . . . . . .
        . . . . . O . . .
        . . . . . . . . .

    The Rothe diagram is a northwest diagram::

        sage: D.parent()
        Combinatorial northwest diagrams

    Some other examples::

        sage: RotheDiagram([2, 1, 4, 3]).pp()
        O . . .
        . . . .
        . . O .
        . . . .

        sage: RotheDiagram([4, 1, 3, 2]).pp()
        O O O .
        . . . .
        . O . .
        . . . .

    Currently, only elements of the set of
    :class:`sage.combinat.permutations.Permutations` are supported. In
    particular, elements of permutation groups are not supported::

        sage: w = SymmetricGroup(9).an_element()                                        # needs sage.groups
        sage: RotheDiagram(w)                                                           # needs sage.groups
        Traceback (most recent call last):
        ...
        ValueError: w must be a permutation

    TESTS::

        sage: w = Permutations(5)([1,2,3,4,5])
        sage: from sage.combinat.diagram import RotheDiagram
        sage: RotheDiagram(w).pp()
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
    """
