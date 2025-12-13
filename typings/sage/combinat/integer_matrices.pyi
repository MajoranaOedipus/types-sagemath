from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.integer_lists import IntegerListsLex as IntegerListsLex
from sage.matrix.constructor import matrix as matrix
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class IntegerMatrices(UniqueRepresentation, Parent):
    """
    The class of nonnegative integer matrices with
    prescribed row sums and column sums.

    An *integer matrix* `m` with column sums `c := (c_1,...,c_k)` and row
    sums `l := (l_1,...,l_n)` where `c_1+...+c_k` is equal to `l_1+...+l_n`,
    is a `n \\times k` matrix `m = (m_{i,j})` such that
    `m_{1,j}+\\dots+m_{n,j} = c_j`, for all `j` and
    `m_{i,1}+\\dots+m_{i,k} = l_i`, for all `i`.

    EXAMPLES:

    There are `6` integer matrices with row sums `[3,2,2]` and column sums
    `[2,5]`::

        sage: from sage.combinat.integer_matrices import IntegerMatrices
        sage: IM = IntegerMatrices([3,2,2], [2,5]); IM
        Non-negative integer matrices with row sums [3, 2, 2] and column sums [2, 5]
        sage: IM.list()
        [
        [2 1]  [1 2]  [1 2]  [0 3]  [0 3]  [0 3]
        [0 2]  [1 1]  [0 2]  [2 0]  [1 1]  [0 2]
        [0 2], [0 2], [1 1], [0 2], [1 1], [2 0]
        ]
        sage: IM.cardinality()
        6
    """
    @staticmethod
    def __classcall__(cls, row_sums, column_sums):
        """
        Normalize the inputs so that they are hashable.

        INPUT:

        - ``row_sums`` -- list, tuple, or anything defining a Composition
        - ``column_sums`` -- list, tuple, or anything defining a Composition

        EXAMPLES::

            sage: from sage.combinat.integer_matrices import IntegerMatrices
            sage: IM = IntegerMatrices([4,4,5], [3,7,1,2]); IM
            Non-negative integer matrices with row sums [4, 4, 5] and column sums [3, 7, 1, 2]
            sage: IM = IntegerMatrices((4,4,5), (3,7,1,2)); IM
            Non-negative integer matrices with row sums [4, 4, 5] and column sums [3, 7, 1, 2]
            sage: IM = IntegerMatrices(Composition([4,4,5]), Composition([3,7,1,2])); IM
            Non-negative integer matrices with row sums [4, 4, 5] and column sums [3, 7, 1, 2]
        """
    def __init__(self, row_sums, column_sums) -> None:
        """
        Constructor of this class; for documentation, see
        :class:`IntegerMatrices`.

        INPUT:

        - ``row_sums`` -- Composition
        - ``column_sums`` -- Composition

        TESTS::

            sage: from sage.combinat.integer_matrices import IntegerMatrices
            sage: IM = IntegerMatrices([3,2,2], [2,5]); IM
            Non-negative integer matrices with row sums [3, 2, 2] and column sums [2, 5]
            sage: TestSuite(IM).run()
        """
    def __iter__(self):
        """
        An iterator for the integer matrices with the prescribed row sums and
        columns sums.

        EXAMPLES::

            sage: from sage.combinat.integer_matrices import IntegerMatrices
            sage: IntegerMatrices([2,2], [1,2,1]).list()
            [
            [1 1 0]  [1 0 1]  [0 2 0]  [0 1 1]
            [0 1 1], [0 2 0], [1 0 1], [1 1 0]
            ]
            sage: IntegerMatrices([0,0],[0,0,0]).list()
            [
            [0 0 0]
            [0 0 0]
            ]
            sage: IntegerMatrices([1,1],[1,1]).list()
            [
            [1 0]  [0 1]
            [0 1], [1 0]
            ]
        """
    def __contains__(self, x) -> bool:
        """
        Test if ``x`` is an element of ``self``.

        INPUT:

        - ``x`` -- matrix

        EXAMPLES::

            sage: from sage.combinat.integer_matrices import IntegerMatrices
            sage: IM = IntegerMatrices([4], [1,2,1])
            sage: matrix([[1, 2, 1]]) in IM
            True
            sage: matrix(QQ, [[1, 2, 1]]) in IM
            True
            sage: matrix([[2, 1, 1]]) in IM
            False

        TESTS::

            sage: from sage.combinat.integer_matrices import IntegerMatrices
            sage: IM = IntegerMatrices([4], [1,2,1])
            sage: [1, 2, 1] in IM
            False
            sage: matrix([[-1, 3, 1]]) in IM
            False
        """
    def cardinality(self):
        """
        The number of integer matrices with the prescribed row sums and columns
        sums.

        EXAMPLES::

            sage: from sage.combinat.integer_matrices import IntegerMatrices
            sage: IntegerMatrices([2,5], [3,2,2]).cardinality()
            6
            sage: IntegerMatrices([1,1,1,1,1], [1,1,1,1,1]).cardinality()
            120
            sage: IntegerMatrices([2,2,2,2], [2,2,2,2]).cardinality()
            282
            sage: IntegerMatrices([4], [3]).cardinality()
            0
            sage: len(IntegerMatrices([0,0], [0]).list())
            1

        This method computes the cardinality using symmetric functions. Below
        are the same examples, but computed by generating the actual matrices::

            sage: from sage.combinat.integer_matrices import IntegerMatrices
            sage: len(IntegerMatrices([2,5], [3,2,2]).list())
            6
            sage: len(IntegerMatrices([1,1,1,1,1], [1,1,1,1,1]).list())
            120
            sage: len(IntegerMatrices([2,2,2,2], [2,2,2,2]).list())
            282
            sage: len(IntegerMatrices([4], [3]).list())
            0
            sage: len(IntegerMatrices([0], [0]).list())
            1
        """
    def row_sums(self):
        """
        The row sums of the integer matrices in ``self``.

        OUTPUT: Composition

        EXAMPLES::

            sage: from sage.combinat.integer_matrices import IntegerMatrices
            sage: IM = IntegerMatrices([3,2,2], [2,5])
            sage: IM.row_sums()
            [3, 2, 2]
        """
    def column_sums(self):
        """
        The column sums of the integer matrices in ``self``.

        OUTPUT: Composition

        EXAMPLES::

            sage: from sage.combinat.integer_matrices import IntegerMatrices
            sage: IM = IntegerMatrices([3,2,2], [2,5])
            sage: IM.column_sums()
            [2, 5]
        """
    def to_composition(self, x):
        """
        The composition corresponding to the integer matrix.

        This is the composition obtained by reading the entries of the matrix
        from left to right along each row, and reading the rows from top to
        bottom, ignore zeros.

        INPUT:

        - ``x`` -- matrix

        EXAMPLES::

            sage: from sage.combinat.integer_matrices import IntegerMatrices
            sage: IM = IntegerMatrices([3,2,2], [2,5]); IM
            Non-negative integer matrices with row sums [3, 2, 2] and column sums [2, 5]
            sage: IM.list()
            [
            [2 1]  [1 2]  [1 2]  [0 3]  [0 3]  [0 3]
            [0 2]  [1 1]  [0 2]  [2 0]  [1 1]  [0 2]
            [0 2], [0 2], [1 1], [0 2], [1 1], [2 0]
            ]
            sage: for m in IM: print(IM.to_composition(m))
            [2, 1, 2, 2]
            [1, 2, 1, 1, 2]
            [1, 2, 2, 1, 1]
            [3, 2, 2]
            [3, 1, 1, 1, 1]
            [3, 2, 2]
        """

def integer_matrices_generator(row_sums, column_sums) -> Generator[Incomplete]:
    """
    Recursively generate the integer matrices with the prescribed row sums and
    column sums.

    INPUT:

    - ``row_sums`` -- list or tuple
    - ``column_sums`` -- list or tuple

    OUTPUT: an iterator producing a list of lists

    EXAMPLES::

        sage: from sage.combinat.integer_matrices import integer_matrices_generator
        sage: iter = integer_matrices_generator([3,2,2], [2,5]); iter
        <generator object ...integer_matrices_generator at ...>
        sage: for m in iter: print(m)
        [[2, 1], [0, 2], [0, 2]]
        [[1, 2], [1, 1], [0, 2]]
        [[1, 2], [0, 2], [1, 1]]
        [[0, 3], [2, 0], [0, 2]]
        [[0, 3], [1, 1], [1, 1]]
        [[0, 3], [0, 2], [2, 0]]
    """
