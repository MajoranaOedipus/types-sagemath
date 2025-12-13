from .dlxcpp import DLXCPP as DLXCPP
from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import is_prime as is_prime
from sage.combinat.permutation import Permutation as Permutation
from sage.groups.perm_gps.permgroup import PermutationGroup as PermutationGroup
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement as PermutationGroupElement
from sage.libs.gap.element import GapElement as GapElement
from sage.libs.gap.libgap import libgap as libgap
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_integer_dense import Matrix_integer_dense as Matrix_integer_dense
from sage.misc.flatten import flatten as flatten
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ

class LatinSquare:
    square: Incomplete
    def __init__(self, *args) -> None:
        """
        Latin squares.

        This class implements a latin square of order n with rows and
        columns indexed by the set 0, 1, ..., n-1 and symbols from the same
        set. The underlying latin square is a matrix(ZZ, n, n). If L is a
        latin square, then the cell at row r, column c is empty if and only
        if L[r, c] < 0. In this way we allow partial latin squares and can
        speak of completions to latin squares, etc.

        There are two ways to declare a latin square:

        Empty latin square of order n::

            sage: n = 3
            sage: L = LatinSquare(n)
            sage: L
            [-1 -1 -1]
            [-1 -1 -1]
            [-1 -1 -1]

        Latin square from a matrix::

            sage: M = matrix(ZZ, [[0, 1], [2, 3]])
            sage: LatinSquare(M)
            [0 1]
            [2 3]
        """
    def dumps(self):
        """
        Since the latin square class does not hold any other private
        variables we just call dumps on self.square:

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: back_circulant(2) == loads(dumps(back_circulant(2)))
            True
        """
    def __getitem__(self, rc):
        """
        If L is a LatinSquare then this method allows us to evaluate L[r,
        c].

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: B = back_circulant(3)
            sage: B[1, 1]
            2
        """
    def __setitem__(self, rc, val) -> None:
        """
        If L is a LatinSquare then this method allows us to set L[r, c].

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: B = back_circulant(3)
            sage: B[1, 1] = 10
            sage: B[1, 1]
            10
        """
    def set_immutable(self) -> None:
        """
        A latin square is immutable if the underlying matrix is immutable.

        EXAMPLES::

            sage: L = LatinSquare(matrix(ZZ, [[0, 1], [2, 3]]))
            sage: L.set_immutable()
            sage: {L : 0}   # this would fail without set_immutable()
            {[0 1]
            [2 3]: 0}
        """
    def __hash__(self):
        """
        The hash of a latin square is precisely the hash of the underlying
        matrix.

        EXAMPLES::

            sage: L = LatinSquare(matrix(ZZ, [[0, 1], [2, 3]]))
            sage: L.set_immutable()
            sage: L.__hash__()
            1677951251422179082  # 64-bit
            -479138038           # 32-bit
        """
    def __eq__(self, Q):
        """
        Two latin squares are equal if the underlying matrices are equal.

        EXAMPLES::

            sage: A = LatinSquare(matrix(ZZ, [[0, 1], [2, 3]]))
            sage: B = LatinSquare(matrix(ZZ, [[0, 4], [2, 3]]))
            sage: A == B
            False
            sage: B[0, 1] = 1
            sage: A == B
            True
        """
    def __copy__(self):
        """
        To copy a latin square we must copy the underlying matrix.

        EXAMPLES::

            sage: A = LatinSquare(matrix(ZZ, [[0, 1], [2, 3]]))
            sage: B = copy(A)
            sage: B
            [0 1]
            [2 3]
        """
    def clear_cells(self) -> None:
        """
        Mark every cell in ``self`` as being empty.

        EXAMPLES::

            sage: A = LatinSquare(matrix(ZZ, [[0, 1], [2, 3]]))
            sage: A.clear_cells()
            sage: A
            [-1 -1]
            [-1 -1]
        """
    def nrows(self):
        """
        Number of rows in the latin square.

        EXAMPLES::

            sage: LatinSquare(3).nrows()
            3
        """
    def ncols(self):
        """
        Number of columns in the latin square.

        EXAMPLES::

            sage: LatinSquare(3).ncols()
            3
        """
    def row(self, x):
        """
        Return row x of the latin square.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: back_circulant(3).row(0)
            (0, 1, 2)
        """
    def column(self, x):
        """
        Return column x of the latin square.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: back_circulant(3).column(0)
            (0, 1, 2)
        """
    def list(self):
        """
        Convert the latin square into a list, in a row-wise manner.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: back_circulant(3).list()
            [0, 1, 2, 1, 2, 0, 2, 0, 1]
        """
    def nr_filled_cells(self):
        """
        Return the number of filled cells (i.e. cells with a positive
        value) in the partial latin square ``self``.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: LatinSquare(matrix([[0, -1], [-1, 0]])).nr_filled_cells()
            2
        """
    def actual_row_col_sym_sizes(self):
        """
        Bitrades sometimes end up in partial latin squares with unused
        rows, columns, or symbols. This function works out the actual
        number of used rows, columns, and symbols.

        .. warning::

           We assume that the unused rows/columns occur in the lower
           right of self, and that the used symbols are in the range
           {0, 1, ..., m} (no holes in that list).

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: B = back_circulant(3)
            sage: B[0,2] = B[1,2] = B[2,2] = -1
            sage: B[0,0] = B[2,1] = -1
            sage: B
            [-1  1 -1]
            [ 1  2 -1]
            [ 2 -1 -1]
            sage: B.actual_row_col_sym_sizes()
            (3, 2, 2)
        """
    def is_empty_column(self, c):
        """
        Check if column c of the partial latin square ``self`` is empty.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: L = back_circulant(4)
            sage: L.is_empty_column(0)
            False
            sage: L[0,0] = L[1,0] = L[2,0] = L[3,0] = -1
            sage: L.is_empty_column(0)
            True
        """
    def is_empty_row(self, r):
        """
        Check if row r of the partial latin square ``self`` is empty.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: L = back_circulant(4)
            sage: L.is_empty_row(0)
            False
            sage: L[0,0] = L[0,1] = L[0,2] = L[0,3] = -1
            sage: L.is_empty_row(0)
            True
        """
    def nr_distinct_symbols(self):
        """
        Return the number of distinct symbols in the partial latin square
        ``self``.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: back_circulant(5).nr_distinct_symbols()
            5
            sage: L = LatinSquare(10)
            sage: L.nr_distinct_symbols()
            0
            sage: L[0, 0] = 0
            sage: L[0, 1] = 1
            sage: L.nr_distinct_symbols()
            2
        """
    def apply_isotopism(self, row_perm, col_perm, sym_perm):
        """
        An isotopism is a permutation of the rows, columns, and symbols of
        a partial latin square ``self``. Use isotopism() to convert a tuple
        (indexed from 0) to a Permutation object.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: B = back_circulant(5)
            sage: B
            [0 1 2 3 4]
            [1 2 3 4 0]
            [2 3 4 0 1]
            [3 4 0 1 2]
            [4 0 1 2 3]
            sage: alpha = isotopism((0,1,2,3,4))
            sage: beta  = isotopism((1,0,2,3,4))
            sage: gamma = isotopism((2,1,0,3,4))
            sage: B.apply_isotopism(alpha, beta, gamma)
            [3 4 2 0 1]
            [0 2 3 1 4]
            [1 3 0 4 2]
            [4 0 1 2 3]
            [2 1 4 3 0]
        """
    def filled_cells_map(self):
        """
        Number the filled cells of ``self`` with integers from {1, 2, 3, ...}.

        INPUT:

        - ``self`` -- partial latin square ``self`` (empty cells
          have negative values)

        OUTPUT:

        A dictionary ``cells_map`` where ``cells_map[(i,j)] = m`` means that
        ``(i,j)`` is the ``m``-th filled cell in ``P``,
        while ``cells_map[m] = (i,j)``.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: (a, b, c, G) = alternating_group_bitrade_generators(1)
            sage: (T1, T2) = bitrade_from_group(a, b, c, G)
            sage: D = T1.filled_cells_map()
            sage: {i: v for i,v in D.items() if i in ZZ}
            {1: (0, 0),
             2: (0, 2),
             3: (0, 3),
             4: (1, 1),
             5: (1, 2),
             6: (1, 3),
             7: (2, 0),
             8: (2, 1),
             9: (2, 2),
             10: (3, 0),
             11: (3, 1),
             12: (3, 3)}
            sage: {i: v for i,v in D.items() if i not in ZZ}
            {(0, 0): 1,
             (0, 2): 2,
             (0, 3): 3,
             (1, 1): 4,
             (1, 2): 5,
             (1, 3): 6,
             (2, 0): 7,
             (2, 1): 8,
             (2, 2): 9,
             (3, 0): 10,
             (3, 1): 11,
             (3, 3): 12}
        """
    def top_left_empty_cell(self):
        """
        Return the least ``[r, c]`` such that ``self[r, c]`` is an empty cell.
        If all cells are filled then we return ``None``.

        INPUT:

        - ``self`` -- LatinSquare

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: B = back_circulant(5)
            sage: B[3, 4] = -1
            sage: B.top_left_empty_cell()
            [3, 4]
        """
    def is_partial_latin_square(self):
        """
        ``self`` is a partial latin square if it is an n by n matrix, and each
        symbol in [0, 1, ..., n-1] appears at most once in each row, and at
        most once in each column.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: LatinSquare(4).is_partial_latin_square()
            True
            sage: back_circulant(3).gcs().is_partial_latin_square()
            True
            sage: back_circulant(6).is_partial_latin_square()
            True
        """
    def is_latin_square(self):
        """
        ``self`` is a latin square if it is an n by n matrix, and each symbol
        in [0, 1, ..., n-1] appears exactly once in each row, and exactly
        once in each column.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: elementary_abelian_2group(4).is_latin_square()
            True

        ::

            sage: forward_circulant(7).is_latin_square()
            True
        """
    def permissable_values(self, r, c):
        """
        Find all values that do not appear in row r and column c of the
        latin square ``self``. If ``self[r, c]`` is filled then we return the
        empty list.

        INPUT:

        - ``self`` -- LatinSquare

        - ``r`` -- integer; row of the latin square

        - ``c`` -- integer; column of the latin square

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: L = back_circulant(5)
            sage: L[0, 0] = -1
            sage: L.permissable_values(0, 0)
            [0]
        """
    def random_empty_cell(self):
        """
        Find an empty cell of self, uniformly at random.

        INPUT:

        - ``self`` -- LatinSquare

        OUTPUT:

        - ``[r, c]`` -- cell such that ``self[r, c]`` is empty, or returns
          ``None`` if ``self`` is a (full) latin square

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: P = back_circulant(2)
            sage: P[1,1] = -1
            sage: P.random_empty_cell()
            [1, 1]
        """
    def is_uniquely_completable(self):
        """
        Return ``True`` if the partial latin square ``self`` has exactly one
        completion to a latin square. This is just a wrapper for the
        current best-known algorithm, Dancing Links by Knuth. See
        dancing_links.spyx

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: back_circulant(4).gcs().is_uniquely_completable()
            True

        ::

            sage: G = elementary_abelian_2group(3).gcs()
            sage: G.is_uniquely_completable()
            True

        ::

            sage: G[0, 0] = -1
            sage: G.is_uniquely_completable()
            False
        """
    def is_completable(self):
        """
        Return ``True`` if the partial latin square can be completed to a
        latin square.

        EXAMPLES:

        The following partial latin square has no completion because there
        is nowhere that we can place the symbol 0 in the third row::

            sage: B = LatinSquare(3)

        ::

            sage: B[0, 0] = 0
            sage: B[1, 1] = 0
            sage: B[2, 2] = 1

        ::

            sage: B
            [ 0 -1 -1]
            [-1  0 -1]
            [-1 -1  1]

        ::

            sage: B.is_completable()
            False

        ::

            sage: B[2, 2] = 0
            sage: B.is_completable()
            True
        """
    def gcs(self):
        """
        A greedy critical set of a latin square ``self`` is found by
        successively removing elements in a row-wise (bottom-up) manner,
        checking for unique completion at each step.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: A = elementary_abelian_2group(3)
            sage: G = A.gcs()
            sage: A
            [0 1 2 3 4 5 6 7]
            [1 0 3 2 5 4 7 6]
            [2 3 0 1 6 7 4 5]
            [3 2 1 0 7 6 5 4]
            [4 5 6 7 0 1 2 3]
            [5 4 7 6 1 0 3 2]
            [6 7 4 5 2 3 0 1]
            [7 6 5 4 3 2 1 0]
            sage: G
            [ 0  1  2  3  4  5  6 -1]
            [ 1  0  3  2  5  4 -1 -1]
            [ 2  3  0  1  6 -1  4 -1]
            [ 3  2  1  0 -1 -1 -1 -1]
            [ 4  5  6 -1  0  1  2 -1]
            [ 5  4 -1 -1  1  0 -1 -1]
            [ 6 -1  4 -1  2 -1  0 -1]
            [-1 -1 -1 -1 -1 -1 -1 -1]
        """
    def dlxcpp_has_unique_completion(self):
        """
        Check if the partial latin square ``self`` of order n can be embedded
        in precisely one latin square of order n.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: back_circulant(2).dlxcpp_has_unique_completion()
            True
            sage: P = LatinSquare(2)
            sage: P.dlxcpp_has_unique_completion()
            False
            sage: P[0, 0] = 0
            sage: P.dlxcpp_has_unique_completion()
            True
        """
    def vals_in_row(self, r):
        """
        Return a dictionary with key e if and only if row r of ``self`` has
        the symbol e.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: B = back_circulant(3)
            sage: B[0, 0] = -1
            sage: back_circulant(3).vals_in_row(0)
            {0: True, 1: True, 2: True}
        """
    def vals_in_col(self, c):
        """
        Return a dictionary with key e if and only if column c of ``self`` has
        the symbol e.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: B = back_circulant(3)
            sage: B[0, 0] = -1
            sage: back_circulant(3).vals_in_col(0)
            {0: True, 1: True, 2: True}
        """
    def latex(self):
        """
        Return LaTeX code for the latin square.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: print(back_circulant(3).latex())
            \\begin{array}{|c|c|c|}\\hline 0 & 1 & 2\\\\\\hline 1 & 2 & 0\\\\\\hline 2 & 0 & 1\\\\\\hline\\end{array}
        """
    def disjoint_mate_dlxcpp_rows_and_map(self, allow_subtrade):
        """
        Internal function for find_disjoint_mates.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: B = back_circulant(4)
            sage: B.disjoint_mate_dlxcpp_rows_and_map(allow_subtrade = True)
            ([[0, 16, 32],
              [1, 17, 32],
              [2, 18, 32],
              [3, 19, 32],
              [4, 16, 33],
              [5, 17, 33],
              [6, 18, 33],
              [7, 19, 33],
              [8, 16, 34],
              [9, 17, 34],
              [10, 18, 34],
              [11, 19, 34],
              [12, 16, 35],
              [13, 17, 35],
              [14, 18, 35],
              [15, 19, 35],
              [0, 20, 36],
              [1, 21, 36],
              [2, 22, 36],
              [3, 23, 36],
              [4, 20, 37],
              [5, 21, 37],
              [6, 22, 37],
              [7, 23, 37],
              [8, 20, 38],
              [9, 21, 38],
              [10, 22, 38],
              [11, 23, 38],
              [12, 20, 39],
              [13, 21, 39],
              [14, 22, 39],
              [15, 23, 39],
              [0, 24, 40],
              [1, 25, 40],
              [2, 26, 40],
              [3, 27, 40],
              [4, 24, 41],
              [5, 25, 41],
              [6, 26, 41],
              [7, 27, 41],
              [8, 24, 42],
              [9, 25, 42],
              [10, 26, 42],
              [11, 27, 42],
              [12, 24, 43],
              [13, 25, 43],
              [14, 26, 43],
              [15, 27, 43],
              [0, 28, 44],
              [1, 29, 44],
              [2, 30, 44],
              [3, 31, 44],
              [4, 28, 45],
              [5, 29, 45],
              [6, 30, 45],
              [7, 31, 45],
              [8, 28, 46],
              [9, 29, 46],
              [10, 30, 46],
              [11, 31, 46],
              [12, 28, 47],
              [13, 29, 47],
              [14, 30, 47],
              [15, 31, 47]],
             {(0, 16, 32): (0, 0, 0),
              (0, 20, 36): (1, 0, 0),
              (0, 24, 40): (2, 0, 0),
              (0, 28, 44): (3, 0, 0),
              (1, 17, 32): (0, 0, 1),
              (1, 21, 36): (1, 0, 1),
              (1, 25, 40): (2, 0, 1),
              (1, 29, 44): (3, 0, 1),
              (2, 18, 32): (0, 0, 2),
              (2, 22, 36): (1, 0, 2),
              (2, 26, 40): (2, 0, 2),
              (2, 30, 44): (3, 0, 2),
              (3, 19, 32): (0, 0, 3),
              (3, 23, 36): (1, 0, 3),
              (3, 27, 40): (2, 0, 3),
              (3, 31, 44): (3, 0, 3),
              (4, 16, 33): (0, 1, 0),
              (4, 20, 37): (1, 1, 0),
              (4, 24, 41): (2, 1, 0),
              (4, 28, 45): (3, 1, 0),
              (5, 17, 33): (0, 1, 1),
              (5, 21, 37): (1, 1, 1),
              (5, 25, 41): (2, 1, 1),
              (5, 29, 45): (3, 1, 1),
              (6, 18, 33): (0, 1, 2),
              (6, 22, 37): (1, 1, 2),
              (6, 26, 41): (2, 1, 2),
              (6, 30, 45): (3, 1, 2),
              (7, 19, 33): (0, 1, 3),
              (7, 23, 37): (1, 1, 3),
              (7, 27, 41): (2, 1, 3),
              (7, 31, 45): (3, 1, 3),
              (8, 16, 34): (0, 2, 0),
              (8, 20, 38): (1, 2, 0),
              (8, 24, 42): (2, 2, 0),
              (8, 28, 46): (3, 2, 0),
              (9, 17, 34): (0, 2, 1),
              (9, 21, 38): (1, 2, 1),
              (9, 25, 42): (2, 2, 1),
              (9, 29, 46): (3, 2, 1),
              (10, 18, 34): (0, 2, 2),
              (10, 22, 38): (1, 2, 2),
              (10, 26, 42): (2, 2, 2),
              (10, 30, 46): (3, 2, 2),
              (11, 19, 34): (0, 2, 3),
              (11, 23, 38): (1, 2, 3),
              (11, 27, 42): (2, 2, 3),
              (11, 31, 46): (3, 2, 3),
              (12, 16, 35): (0, 3, 0),
              (12, 20, 39): (1, 3, 0),
              (12, 24, 43): (2, 3, 0),
              (12, 28, 47): (3, 3, 0),
              (13, 17, 35): (0, 3, 1),
              (13, 21, 39): (1, 3, 1),
              (13, 25, 43): (2, 3, 1),
              (13, 29, 47): (3, 3, 1),
              (14, 18, 35): (0, 3, 2),
              (14, 22, 39): (1, 3, 2),
              (14, 26, 43): (2, 3, 2),
              (14, 30, 47): (3, 3, 2),
              (15, 19, 35): (0, 3, 3),
              (15, 23, 39): (1, 3, 3),
              (15, 27, 43): (2, 3, 3),
              (15, 31, 47): (3, 3, 3)})
        """
    def find_disjoint_mates(self, nr_to_find=None, allow_subtrade: bool = False) -> Generator[Incomplete]:
        """
        .. warning::

            If allow_subtrade is ``True`` then we may return a partial
            latin square that is *not* disjoint to ``self``. In that case,
            use bitrade(P, Q) to get an actual bitrade.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: B = back_circulant(4)
            sage: g = B.find_disjoint_mates(allow_subtrade = True)
            sage: B1 = next(g)
            sage: B0, B1 = bitrade(B, B1)
            sage: assert is_bitrade(B0, B1)
            sage: print(B0)
            [-1  1  2 -1]
            [-1  2 -1  0]
            [-1 -1 -1 -1]
            [-1  0  1  2]
            sage: print(B1)
            [-1  2  1 -1]
            [-1  0 -1  2]
            [-1 -1 -1 -1]
            [-1  1  2  0]
        """
    def contained_in(self, Q):
        """
        Return ``True`` if ``self`` is a subset of `Q`.

        EXAMPLES::

            sage: from sage.combinat.matrices.latin import *
            sage: P = elementary_abelian_2group(2)
            sage: P[0, 0] = -1
            sage: P.contained_in(elementary_abelian_2group(2))
            True
            sage: back_circulant(4).contained_in(elementary_abelian_2group(2))
            False
        """

def genus(T1, T2):
    """
    Return the genus of hypermap embedding associated with the bitrade
    (T1, T2).

    Informally, we compute the [tau_1, tau_2, tau_3]
    permutation representation of the bitrade. Each cycle of tau_1,
    tau_2, and tau_3 gives a rotation scheme for a black, white, and
    star vertex (respectively). The genus then comes from Euler's
    formula.

    For more details see Carlo Hamalainen: *Partitioning
    3-homogeneous latin bitrades*. To appear in Geometriae Dedicata,
    available at :arxiv:`0710.0938`

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: (a, b, c, G) = alternating_group_bitrade_generators(1)
        sage: (T1, T2) = bitrade_from_group(a, b, c, G)
        sage: genus(T1, T2)
        1
        sage: (a, b, c, G) = pq_group_bitrade_generators(3, 7)
        sage: (T1, T2) = bitrade_from_group(a, b, c, G)
        sage: genus(T1, T2)
        3
    """
def tau123(T1, T2):
    """
    Compute the tau_i representation for a bitrade (T1, T2).

    See the
    functions tau1, tau2, and tau3 for the mathematical definitions.

    OUTPUT:

    - (cells_map, t1, t2, t3)

    where cells_map is a map to/from the filled cells of T1, and t1,
    t2, t3 are the tau1, tau2, tau3 permutations.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: (a, b, c, G) = pq_group_bitrade_generators(3, 7)
        sage: (T1, T2) = bitrade_from_group(a, b, c, G)
        sage: T1
        [ 0  1  3 -1 -1 -1 -1]
        [ 1  2  4 -1 -1 -1 -1]
        [ 2  3  5 -1 -1 -1 -1]
        [ 3  4  6 -1 -1 -1 -1]
        [ 4  5  0 -1 -1 -1 -1]
        [ 5  6  1 -1 -1 -1 -1]
        [ 6  0  2 -1 -1 -1 -1]
        sage: T2
        [ 1  3  0 -1 -1 -1 -1]
        [ 2  4  1 -1 -1 -1 -1]
        [ 3  5  2 -1 -1 -1 -1]
        [ 4  6  3 -1 -1 -1 -1]
        [ 5  0  4 -1 -1 -1 -1]
        [ 6  1  5 -1 -1 -1 -1]
        [ 0  2  6 -1 -1 -1 -1]
        sage: (cells_map, t1, t2, t3) = tau123(T1, T2)
        sage: D = cells_map
        sage: {i: v for i,v in D.items() if i in ZZ}
        {1: (0, 0),
         2: (0, 1),
         3: (0, 2),
         4: (1, 0),
         5: (1, 1),
         6: (1, 2),
         7: (2, 0),
         8: (2, 1),
         9: (2, 2),
         10: (3, 0),
         11: (3, 1),
         12: (3, 2),
         13: (4, 0),
         14: (4, 1),
         15: (4, 2),
         16: (5, 0),
         17: (5, 1),
         18: (5, 2),
         19: (6, 0),
         20: (6, 1),
         21: (6, 2)}
        sage: {i: v for i,v in D.items() if i not in ZZ}
        {(0, 0): 1,
         (0, 1): 2,
         (0, 2): 3,
         (1, 0): 4,
         (1, 1): 5,
         (1, 2): 6,
         (2, 0): 7,
         (2, 1): 8,
         (2, 2): 9,
         (3, 0): 10,
         (3, 1): 11,
         (3, 2): 12,
         (4, 0): 13,
         (4, 1): 14,
         (4, 2): 15,
         (5, 0): 16,
         (5, 1): 17,
         (5, 2): 18,
         (6, 0): 19,
         (6, 1): 20,
         (6, 2): 21}
        sage: cells_map_as_square(cells_map, max(T1.nrows(), T1.ncols()))
        [ 1  2  3 -1 -1 -1 -1]
        [ 4  5  6 -1 -1 -1 -1]
        [ 7  8  9 -1 -1 -1 -1]
        [10 11 12 -1 -1 -1 -1]
        [13 14 15 -1 -1 -1 -1]
        [16 17 18 -1 -1 -1 -1]
        [19 20 21 -1 -1 -1 -1]
        sage: t1
        [3, 1, 2, 6, 4, 5, 9, 7, 8, 12, 10, 11, 15, 13, 14, 18, 16, 17, 21, 19, 20]
        sage: t2
        [4, 8, 15, 7, 11, 18, 10, 14, 21, 13, 17, 3, 16, 20, 6, 19, 2, 9, 1, 5, 12]
        sage: t3
        [20, 18, 10, 2, 21, 13, 5, 3, 16, 8, 6, 19, 11, 9, 1, 14, 12, 4, 17, 15, 7]

    ::

        sage: t1.to_cycles()
        [(1, 3, 2), (4, 6, 5), (7, 9, 8), (10, 12, 11), (13, 15, 14), (16, 18, 17), (19, 21, 20)]
        sage: t2.to_cycles()
        [(1, 4, 7, 10, 13, 16, 19), (2, 8, 14, 20, 5, 11, 17), (3, 15, 6, 18, 9, 21, 12)]
        sage: t3.to_cycles()
        [(1, 20, 15), (2, 18, 4), (3, 10, 8), (5, 21, 7), (6, 13, 11), (9, 16, 14), (12, 19, 17)]

    The product t1\\*t2\\*t3 is the identity, i.e. it fixes every point::

        sage: len((t1*t2*t3).fixed_points()) == T1.nr_filled_cells()
        True
    """
def isotopism(p):
    """
    Return a Permutation object that represents an isotopism (for rows,
    columns or symbols of a partial latin square).

    Technically, all this function does is take as input a
    representation of a permutation of `0,...,n-1` and return a
    :class:`Permutation` object defined on `1,...,n`.

    For a definition of isotopism, see the :wikipedia:`wikipedia section on
    isotopism <Latin_square#Equivalence_classes_of_Latin_squares>`.

    INPUT:

    According to the type of input (see examples below):

    - an integer `n` -- the function returns the identity on `1,...,n`

    - a string representing a permutation in disjoint cycles notation,
      e.g. `(0,1,2)(3,4,5)` -- the corresponding permutation is returned,
      shifted by 1 to act on `1,...,n`

    - list/tuple of tuples -- assumes disjoint cycle notation, see previous
      entry

    - a list of integers -- the function adds `1` to each member of the
      list, and returns the corresponding permutation

    - a :class:`PermutationGroupElement` ``p`` -- returns a permutation
      describing ``p`` **without** any shift

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: isotopism(5) # identity on 5 points
        [1, 2, 3, 4, 5]

    ::

        sage: G = PermutationGroup(['(1,2,3)(4,5)'])
        sage: g = G.gen(0)
        sage: isotopism(g)
        [2, 3, 1, 5, 4]

    ::

        sage: isotopism([0,3,2,1]) # 0 goes to 0, 1 goes to 3, etc.
        [1, 4, 3, 2]

    ::

        sage: isotopism( (0,1,2) ) # single cycle, presented as a tuple
        [2, 3, 1]

    ::

        sage: x = isotopism( ((0,1,2), (3,4)) ) # tuple of cycles
        sage: x
        [2, 3, 1, 5, 4]
        sage: x.to_cycles()
        [(1, 2, 3), (4, 5)]
    """
def cells_map_as_square(cells_map, n):
    """
    Return a LatinSquare with cells numbered from 1, 2, ... to given
    the dictionary cells_map.

    .. NOTE::

       The value n should be the maximum of the number of rows and
       columns of the original partial latin square

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: (a, b, c, G) = alternating_group_bitrade_generators(1)
        sage: (T1, T2) = bitrade_from_group(a, b, c, G)
        sage: T1
        [ 0 -1  3  1]
        [-1  1  0  2]
        [ 1  3  2 -1]
        [ 2  0 -1  3]

    There are 12 filled cells in T::

        sage: cells_map_as_square(T1.filled_cells_map(), max(T1.nrows(), T1.ncols()))
        [ 1 -1  2  3]
        [-1  4  5  6]
        [ 7  8  9 -1]
        [10 11 -1 12]
    """
def beta1(rce, T1, T2):
    """
    Find the unique (x, c, e) in T2 such that (r, c, e) is in T1.

    INPUT:

    - ``rce`` -- tuple (or list) (r, c, e) in T1

    - ``T1``, ``T2`` -- latin bitrade

    OUTPUT: (x, c, e) in T2

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: T1 = back_circulant(5)
        sage: x = isotopism( (0,1,2,3,4) )
        sage: y = isotopism(5) # identity
        sage: z = isotopism(5) # identity
        sage: T2 = T1.apply_isotopism(x, y, z)
        sage: is_bitrade(T1, T2)
        True
        sage: beta1([0, 0, 0], T1, T2)
        (1, 0, 0)
    """
def beta2(rce, T1, T2):
    """
    Find the unique (r, x, e) in T2 such that (r, c, e) is in T1.

    INPUT:

    - ``rce`` -- tuple (or list) (r, c, e) in T1

    - ``T1``, ``T2`` -- latin bitrade

    OUTPUT: (r, x, e) in T2

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: T1 = back_circulant(5)
        sage: x = isotopism( (0,1,2,3,4) )
        sage: y = isotopism(5) # identity
        sage: z = isotopism(5) # identity
        sage: T2 = T1.apply_isotopism(x, y, z)
        sage: is_bitrade(T1, T2)
        True
        sage: beta2([0, 0, 0], T1, T2)
        (0, 1, 0)
    """
def beta3(rce, T1, T2):
    """
    Find the unique (r, c, x) in T2 such that (r, c, e) is in T1.

    INPUT:

    - ``rce`` -- tuple (or list) (r, c, e) in T1

    - ``T1, T2`` -- latin bitrade

    OUTPUT: (r, c, x) in T2.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: T1 = back_circulant(5)
        sage: x = isotopism( (0,1,2,3,4) )
        sage: y = isotopism(5) # identity
        sage: z = isotopism(5) # identity
        sage: T2 = T1.apply_isotopism(x, y, z)
        sage: is_bitrade(T1, T2)
        True
        sage: beta3([0, 0, 0], T1, T2)
        (0, 0, 4)
    """
def tau1(T1, T2, cells_map):
    """
    The definition of `\\tau_1` is

    .. MATH::

       \\tau_1 : T1 \\rightarrow T1 \\\\\n       \\tau_1 = \\beta_2^{-1} \\beta_3

    where the composition is left to right and `\\beta_i : T2 \\rightarrow T1`
    changes just the `i`-th coordinate of a triple.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: T1 = back_circulant(5)
        sage: x = isotopism( (0,1,2,3,4) )
        sage: y = isotopism(5) # identity
        sage: z = isotopism(5) # identity
        sage: T2 = T1.apply_isotopism(x, y, z)
        sage: is_bitrade(T1, T2)
        True
        sage: (cells_map, t1, t2, t3) = tau123(T1, T2)
        sage: t1 = tau1(T1, T2, cells_map)
        sage: t1
        [2, 3, 4, 5, 1, 7, 8, 9, 10, 6, 12, 13, 14, 15, 11, 17, 18, 19, 20, 16, 22, 23, 24, 25, 21]
        sage: t1.to_cycles()
        [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15), (16, 17, 18, 19, 20), (21, 22, 23, 24, 25)]
    """
def tau2(T1, T2, cells_map):
    """
    The definition of `\\tau_2` is

    .. MATH::

       \\tau_2 : T1 \\rightarrow T1 \\\\\n       \\tau_2 = \\beta_3^{-1} \\beta_1

    where the composition is left to right and `\\beta_i : T2 \\rightarrow T1`
    changes just the `i`-th coordinate of a triple.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: T1 = back_circulant(5)
        sage: x = isotopism( (0,1,2,3,4) )
        sage: y = isotopism(5) # identity
        sage: z = isotopism(5) # identity
        sage: T2 = T1.apply_isotopism(x, y, z)
        sage: is_bitrade(T1, T2)
        True
        sage: (cells_map, t1, t2, t3) = tau123(T1, T2)
        sage: t2 = tau2(T1, T2, cells_map)
        sage: t2
        [21, 22, 23, 24, 25, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        sage: t2.to_cycles()
        [(1, 21, 16, 11, 6), (2, 22, 17, 12, 7), (3, 23, 18, 13, 8), (4, 24, 19, 14, 9), (5, 25, 20, 15, 10)]
    """
def tau3(T1, T2, cells_map):
    """
    The definition of `\\tau_3` is

    .. MATH::

       \\tau_3 : T1 \\rightarrow T1 \\\\\n       \\tau_3 = \\beta_1^{-1} \\beta_2

    where the composition is left to right and `\\beta_i : T2 \\rightarrow T1`
    changes just the `i`-th coordinate of a triple.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: T1 = back_circulant(5)
        sage: x = isotopism( (0,1,2,3,4) )
        sage: y = isotopism(5) # identity
        sage: z = isotopism(5) # identity
        sage: T2 = T1.apply_isotopism(x, y, z)
        sage: is_bitrade(T1, T2)
        True
        sage: (cells_map, t1, t2, t3) = tau123(T1, T2)
        sage: t3 = tau3(T1, T2, cells_map)
        sage: t3
        [10, 6, 7, 8, 9, 15, 11, 12, 13, 14, 20, 16, 17, 18, 19, 25, 21, 22, 23, 24, 5, 1, 2, 3, 4]
        sage: t3.to_cycles()
        [(1, 10, 14, 18, 22), (2, 6, 15, 19, 23), (3, 7, 11, 20, 24), (4, 8, 12, 16, 25), (5, 9, 13, 17, 21)]
    """
def back_circulant(n):
    """
    The back-circulant latin square of order n is the Cayley table for
    (Z_n, +), the integers under addition modulo n.

    INPUT:

    - ``n`` -- integer; order of the latin square

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: back_circulant(5)
        [0 1 2 3 4]
        [1 2 3 4 0]
        [2 3 4 0 1]
        [3 4 0 1 2]
        [4 0 1 2 3]
    """
def forward_circulant(n):
    """
    The forward-circulant latin square of order n is the Cayley table
    for the operation r + c = (n-c+r) mod n.

    INPUT:

    - ``n`` -- integer; order of the latin square

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: forward_circulant(5)
        [0 4 3 2 1]
        [1 0 4 3 2]
        [2 1 0 4 3]
        [3 2 1 0 4]
        [4 3 2 1 0]
    """
def direct_product(L1, L2, L3, L4):
    """
    The 'direct product' of four latin squares L1, L2, L3, L4 of order
    n is the latin square of order 2n consisting of

    ::

        -----------
        | L1 | L2 |
        -----------
        | L3 | L4 |
        -----------

    where the subsquares L2 and L3 have entries offset by n.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: direct_product(back_circulant(4), back_circulant(4), elementary_abelian_2group(2), elementary_abelian_2group(2))
        [0 1 2 3 4 5 6 7]
        [1 2 3 0 5 6 7 4]
        [2 3 0 1 6 7 4 5]
        [3 0 1 2 7 4 5 6]
        [4 5 6 7 0 1 2 3]
        [5 4 7 6 1 0 3 2]
        [6 7 4 5 2 3 0 1]
        [7 6 5 4 3 2 1 0]
    """
def elementary_abelian_2group(s):
    """
    Return the latin square based on the Cayley table for the
    elementary abelian 2-group of order 2s.

    INPUT:

    - ``s`` -- integer; order of the latin square will be 2s

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: elementary_abelian_2group(3)
        [0 1 2 3 4 5 6 7]
        [1 0 3 2 5 4 7 6]
        [2 3 0 1 6 7 4 5]
        [3 2 1 0 7 6 5 4]
        [4 5 6 7 0 1 2 3]
        [5 4 7 6 1 0 3 2]
        [6 7 4 5 2 3 0 1]
        [7 6 5 4 3 2 1 0]
    """
def coin():
    """
    Simulate a fair coin (returns ``True`` or ``False``) using
    ZZ.random_element(2).

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import coin
        sage: x = coin()
        sage: x == 0 or x == 1
        True
    """
def next_conjugate(L):
    """
    Permute L[r, c] = e to the conjugate L[c, e] = r.

    We assume that L is an n by n matrix and has values in the range 0,
    1, ..., n-1.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: L = back_circulant(6)
        sage: L
        [0 1 2 3 4 5]
        [1 2 3 4 5 0]
        [2 3 4 5 0 1]
        [3 4 5 0 1 2]
        [4 5 0 1 2 3]
        [5 0 1 2 3 4]
        sage: next_conjugate(L)
        [0 1 2 3 4 5]
        [5 0 1 2 3 4]
        [4 5 0 1 2 3]
        [3 4 5 0 1 2]
        [2 3 4 5 0 1]
        [1 2 3 4 5 0]
        sage: L == next_conjugate(next_conjugate(next_conjugate(L)))
        True
    """
def row_containing_sym(L, c, x):
    """
    Given an improper latin square L with L[r1, c] = L[r2, c] = x,
    return r1 or r2 with equal probability. This is an internal
    function and should only be used in LatinSquare_generator().

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: L = matrix([(0, 1, 0, 3), (3, 0, 2, 1), (1, 0, 3, 2), (2, 3, 1, 0)])
        sage: L
        [0 1 0 3]
        [3 0 2 1]
        [1 0 3 2]
        [2 3 1 0]
        sage: c = row_containing_sym(L, 1, 0)
        sage: c == 1 or c == 2
        True
    """
def column_containing_sym(L, r, x):
    """
    Given an improper latin square L with L[r, c1] = L[r, c2] = x,
    return c1 or c2 with equal probability. This is an internal
    function and should only be used in LatinSquare_generator().

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: L = matrix([(1, 0, 2, 3), (0, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2)])
        sage: L
        [1 0 2 3]
        [0 2 3 0]
        [2 3 0 1]
        [3 0 1 2]
        sage: c = column_containing_sym(L, 1, 0)
        sage: c == 0 or c == 3
        True
    """
def LatinSquare_generator(L_start, check_assertions: bool = False) -> Generator[Incomplete]:
    '''
    Generator for a sequence of uniformly distributed latin squares,
    given L_start as the initial latin square.

    This code implements
    the Markov chain algorithm of Jacobson and Matthews (1996), see
    below for the BibTex entry. This generator will never throw the
    ``StopIteration`` exception, so it provides an infinite sequence of
    latin squares.

    EXAMPLES:

    Use the back circulant latin square of order 4 as the initial
    square and print the next two latin squares given by the Markov
    chain::

        sage: from sage.combinat.matrices.latin import *
        sage: g = LatinSquare_generator(back_circulant(4))
        sage: next(g).is_latin_square()
        True

    REFERENCES:

    .. [JacMat96] Mark T. Jacobson and Peter Matthews, "Generating uniformly
       distributed random Latin squares", Journal of Combinatorial Designs,
       4 (1996)
    '''
def group_to_LatinSquare(G):
    """
    Construct a latin square on the symbols [0, 1, ..., n-1] for a
    group with an n by n Cayley table.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import group_to_LatinSquare

        sage: group_to_LatinSquare(DihedralGroup(2))
        [0 1 2 3]
        [1 0 3 2]
        [2 3 0 1]
        [3 2 1 0]

    ::

        sage: G = libgap.Group(PermutationGroupElement((1,2,3)))
        sage: group_to_LatinSquare(G)
        [0 1 2]
        [1 2 0]
        [2 0 1]
    """
def alternating_group_bitrade_generators(m):
    """
    Construct generators a, b, c for the alternating group on 3m+1
    points, such that a\\*b\\*c = 1.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: a, b, c, G = alternating_group_bitrade_generators(1)
        sage: (a, b, c, G)
        ((1,2,3), (1,4,2), (2,4,3), Permutation Group with generators [(1,2,3), (1,4,2)])
        sage: a*b*c
        ()

    ::

        sage: (T1, T2) = bitrade_from_group(a, b, c, G)
        sage: T1
        [ 0 -1  3  1]
        [-1  1  0  2]
        [ 1  3  2 -1]
        [ 2  0 -1  3]
        sage: T2
        [ 1 -1  0  3]
        [-1  0  2  1]
        [ 2  1  3 -1]
        [ 0  3 -1  2]
    """
def pq_group_bitrade_generators(p, q):
    """
    Generators for a group of order pq where p and q are primes such
    that (q % p) == 1.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: pq_group_bitrade_generators(3,7)
        ((2,3,5)(4,7,6), (1,2,3,4,5,6,7), (1,4,2)(3,5,6), Permutation Group with generators [(2,3,5)(4,7,6), (1,2,3,4,5,6,7)])
    """
def p3_group_bitrade_generators(p):
    """
    Generators for a group of order p3 where p is a prime.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: p3_group_bitrade_generators(3)  # random output
        ((2,6,7)(3,8,9),
         (1,2,3)(4,7,8)(5,6,9),
         (1,9,2)(3,7,4)(5,8,6),
         Permutation Group with generators [(2,6,7)(3,8,9), (1,2,3)(4,7,8)(5,6,9)])
    """
def check_bitrade_generators(a, b, c):
    """
    Three group elements a, b, c will generate a bitrade if a\\*b\\*c = 1
    and the subgroups a, b, c intersect (pairwise) in just the
    identity.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: a, b, c, G = p3_group_bitrade_generators(3)
        sage: check_bitrade_generators(a, b, c)
        True
        sage: check_bitrade_generators(a, b, libgap(gap('()')))
        False
    """
def is_bitrade(T1, T2):
    """
    Combinatorially, a pair (T1, T2) of partial latin squares is a
    bitrade if they are disjoint, have the same shape, and have row and
    column balance. For definitions of each of these terms see the
    relevant function in this file.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: T1 = back_circulant(5)
        sage: x = isotopism( (0,1,2,3,4) )
        sage: y = isotopism(5) # identity
        sage: z = isotopism(5) # identity
        sage: T2 = T1.apply_isotopism(x, y, z)
        sage: is_bitrade(T1, T2)
        True
    """
def is_primary_bitrade(a, b, c, G):
    """
    A bitrade generated from elements a, b, c is primary if a, b, c =
    G.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: (a, b, c, G) = p3_group_bitrade_generators(5)
        sage: is_primary_bitrade(a, b, c, G)
        True
    """
def tau_to_bitrade(t1, t2, t3):
    """
    Given permutations t1, t2, t3 that represent a latin bitrade,
    convert them to an explicit latin bitrade (T1, T2). The result is
    unique up to isotopism.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: T1 = back_circulant(5)
        sage: x = isotopism( (0,1,2,3,4) )
        sage: y = isotopism(5) # identity
        sage: z = isotopism(5) # identity
        sage: T2 = T1.apply_isotopism(x, y, z)
        sage: _, t1, t2, t3 = tau123(T1, T2)
        sage: U1, U2 = tau_to_bitrade(t1, t2, t3)
        sage: assert is_bitrade(U1, U2)
        sage: U1
        [0 1 2 3 4]
        [1 2 3 4 0]
        [2 3 4 0 1]
        [3 4 0 1 2]
        [4 0 1 2 3]
        sage: U2
        [4 0 1 2 3]
        [0 1 2 3 4]
        [1 2 3 4 0]
        [2 3 4 0 1]
        [3 4 0 1 2]
    """
def bitrade_from_group(a, b, c, G):
    """
    Given group elements a, b, c in G such that abc = 1 and the
    subgroups a, b, c intersect (pairwise) only in the identity,
    construct a bitrade (T1, T2) where rows, columns, and symbols
    correspond to cosets of a, b, and c, respectively.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: a, b, c, G = alternating_group_bitrade_generators(1)
        sage: (T1, T2) = bitrade_from_group(a, b, c, G)
        sage: T1
        [ 0 -1  3  1]
        [-1  1  0  2]
        [ 1  3  2 -1]
        [ 2  0 -1  3]
        sage: T2
        [ 1 -1  0  3]
        [-1  0  2  1]
        [ 2  1  3 -1]
        [ 0  3 -1  2]
    """
def is_disjoint(T1, T2):
    """
    The partial latin squares T1 and T2 are disjoint if T1[r, c] !=
    T2[r, c] or T1[r, c] == T2[r, c] == -1 for each cell [r, c].

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import is_disjoint, back_circulant, isotopism
        sage: is_disjoint(back_circulant(2), back_circulant(2))
        False

    ::

        sage: T1 = back_circulant(5)
        sage: x = isotopism( (0,1,2,3,4) )
        sage: y = isotopism(5) # identity
        sage: z = isotopism(5) # identity
        sage: T2 = T1.apply_isotopism(x, y, z)
        sage: is_disjoint(T1, T2)
        True
    """
def is_same_shape(T1, T2):
    """
    Two partial latin squares T1, T2 have the same shape if T1[r, c] =
    0 if and only if T2[r, c] = 0.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: is_same_shape(elementary_abelian_2group(2), back_circulant(4))
        True
        sage: is_same_shape(LatinSquare(5), LatinSquare(5))
        True
        sage: is_same_shape(forward_circulant(5), LatinSquare(5))
        False
    """
def is_row_and_col_balanced(T1, T2):
    """
    Partial latin squares T1 and T2 are balanced if the symbols
    appearing in row r of T1 are the same as the symbols appearing in
    row r of T2, for each r, and if the same condition holds on
    columns.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: T1 = matrix([[0,1,-1,-1], [-1,-1,-1,-1], [-1,-1,-1,-1], [-1,-1,-1,-1]])
        sage: T2 = matrix([[0,1,-1,-1], [-1,-1,-1,-1], [-1,-1,-1,-1], [-1,-1,-1,-1]])
        sage: is_row_and_col_balanced(T1, T2)
        True
        sage: T2 = matrix([[0,3,-1,-1], [-1,-1,-1,-1], [-1,-1,-1,-1], [-1,-1,-1,-1]])
        sage: is_row_and_col_balanced(T1, T2)
        False
    """
def dlxcpp_rows_and_map(P):
    """
    Internal function for ``dlxcpp_find_completions``. Given a partial
    latin square P we construct a list of rows of a 0-1 matrix M such
    that an exact cover of M corresponds to a completion of P to a
    latin square.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: dlxcpp_rows_and_map(LatinSquare(2))
        ([[0, 4, 8],
          [1, 5, 8],
          [2, 4, 9],
          [3, 5, 9],
          [0, 6, 10],
          [1, 7, 10],
          [2, 6, 11],
          [3, 7, 11]],
         {(0, 4, 8): (0, 0, 0),
          (0, 6, 10): (1, 0, 0),
          (1, 5, 8): (0, 0, 1),
          (1, 7, 10): (1, 0, 1),
          (2, 4, 9): (0, 1, 0),
          (2, 6, 11): (1, 1, 0),
          (3, 5, 9): (0, 1, 1),
          (3, 7, 11): (1, 1, 1)})
    """
def dlxcpp_find_completions(P, nr_to_find=None):
    """
    Return a list of all latin squares L of the same order as P such
    that P is contained in L. The optional parameter nr_to_find
    limits the number of latin squares that are found.

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: dlxcpp_find_completions(LatinSquare(2))
        [[0 1]
        [1 0], [1 0]
        [0 1]]

    ::

        sage: dlxcpp_find_completions(LatinSquare(2), 1)
        [[0 1]
        [1 0]]
    """
def bitrade(T1, T2):
    """
    Form the bitrade (Q1, Q2) from (T1, T2) by setting empty the cells
    (r, c) such that T1[r, c] == T2[r, c].

    EXAMPLES::

        sage: from sage.combinat.matrices.latin import *
        sage: B1 = back_circulant(5)
        sage: alpha = isotopism((0,1,2,3,4))
        sage: beta  = isotopism((1,0,2,3,4))
        sage: gamma = isotopism((2,1,0,3,4))
        sage: B2 = B1.apply_isotopism(alpha, beta, gamma)
        sage: T1, T2 = bitrade(B1, B2)
        sage: T1
        [ 0  1 -1  3  4]
        [ 1 -1 -1  4  0]
        [ 2 -1  4  0  1]
        [ 3  4  0  1  2]
        [ 4  0  1  2  3]
        sage: T2
        [ 3  4 -1  0  1]
        [ 0 -1 -1  1  4]
        [ 1 -1  0  4  2]
        [ 4  0  1  2  3]
        [ 2  1  4  3  0]
    """
