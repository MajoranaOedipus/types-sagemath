from _typeshed import Incomplete
from sage.arith.misc import factorial as factorial
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.combinatorial_map import combinatorial_map as combinatorial_map
from sage.combinat.gelfand_tsetlin_patterns import GelfandTsetlinPatternsTopRow as GelfandTsetlinPatternsTopRow
from sage.combinat.non_decreasing_parking_function import NonDecreasingParkingFunction as NonDecreasingParkingFunction
from sage.combinat.permutation import Permutation as Permutation
from sage.combinat.six_vertex_model import SquareIceModel as SquareIceModel
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass
from sage.misc.flatten import flatten as flatten
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.modules.free_module_element import zero_vector as zero_vector
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class AlternatingSignMatrix(Element, metaclass=InheritComparisonClasscallMetaclass):
    """
    An alternating sign matrix.

    An alternating sign matrix is a square matrix of `0`'s, `1`'s and `-1`'s
    such that the sum of each row and column is `1` and the nonzero
    entries in each row and column alternate in sign.

    These were introduced in [MRR1983]_.
    """
    @staticmethod
    def __classcall_private__(cls, asm, check: bool = True):
        """
        Create an ASM.

        EXAMPLES::

            sage: AlternatingSignMatrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
            [1 0 0]
            [0 1 0]
            [0 0 1]

            sage: AlternatingSignMatrix([[0, 1, 0],[1, -1, 1],[0, 1, 0]])
            [ 0  1  0]
            [ 1 -1  1]
            [ 0  1  0]

        TESTS:

        Check that :issue:`22032` is fixed::

            sage: AlternatingSignMatrix([])
            []

        Check dimension 1::

            sage: AlternatingSignMatrix([1])
            [1]

            sage: AlternatingSignMatrix([-1])
            Traceback (most recent call last):
            ...
            ValueError: invalid alternating sign matrix
        """
    def __init__(self, parent, asm) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: elt = A([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
            sage: TestSuite(elt).run()
        """
    def __hash__(self):
        """
        TESTS::

            sage: A = AlternatingSignMatrices(3)
            sage: elt = A([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            sage: hash(elt)
            1
        """
    def to_matrix(self):
        """
        Return ``self`` as a regular matrix.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: asm = A([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
            sage: m = asm.to_matrix(); m
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: m.parent()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
        """
    def to_monotone_triangle(self):
        """
        Return a monotone triangle from ``self``.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[1, 0, 0],[0, 1, 0],[0, 0, 1]]).to_monotone_triangle()
            [[3, 2, 1], [2, 1], [1]]
            sage: asm = A([[0, 1, 0],[1, -1, 1],[0, 1, 0]])
            sage: asm.to_monotone_triangle()
            [[3, 2, 1], [3, 1], [2]]
            sage: asm = A([[0, 0, 1],[1, 0, 0],[0, 1, 0]])
            sage: asm.to_monotone_triangle()
            [[3, 2, 1], [3, 1], [3]]
            sage: A.from_monotone_triangle(asm.to_monotone_triangle()) == asm
            True
        """
    def rotate_ccw(self):
        """
        Return the counterclockwise quarter turn rotation of ``self``.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[1, 0, 0],[0, 1, 0],[0, 0, 1]]).rotate_ccw()
            [0 0 1]
            [0 1 0]
            [1 0 0]
            sage: asm = A([[0, 0, 1],[1, 0, 0],[0, 1, 0]])
            sage: asm.rotate_ccw()
            [1 0 0]
            [0 0 1]
            [0 1 0]
        """
    def inversion_number(self):
        """
        Return the inversion number of ``self``.

        If we denote the entries of the alternating sign matrix as `a_{i,j}`,
        the inversion number is defined as `\\sum_{i>k}\\sum_{j<l}a_{i,j}a_{k,l}`.
        When restricted to permutation matrices, this gives the usual inversion
        number of the permutation.

        This definition is equivalent to the one given in [MRR1983]_.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[1, 0, 0],[0, 1, 0],[0, 0, 1]]).inversion_number()
            0
            sage: asm = A([[0, 0, 1],[1, 0, 0],[0, 1, 0]])
            sage: asm.inversion_number()
            2
            sage: asm = A([[0, 1, 0],[1, -1, 1],[0, 1, 0]])
            sage: asm.inversion_number()
            2
            sage: P = Permutations(5)
            sage: all(p.number_of_inversions()==AlternatingSignMatrix(p.to_matrix()).inversion_number() for p in P)
            True
        """
    def rotate_cw(self):
        """
        Return the clockwise quarter turn rotation of ``self``.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[1, 0, 0],[0, 1, 0],[0, 0, 1]]).rotate_cw()
            [0 0 1]
            [0 1 0]
            [1 0 0]
            sage: asm = A([[0, 0, 1],[1, 0, 0],[0, 1, 0]])
            sage: asm.rotate_cw()
            [0 1 0]
            [1 0 0]
            [0 0 1]
        """
    def transpose(self):
        """
        Return ``self`` transposed.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[1, 0, 0],[0, 1, 0],[0, 0, 1]]).transpose()
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: asm = A([[0, 0, 1],[1, 0, 0],[0, 1, 0]])
            sage: asm.transpose()
            [0 1 0]
            [0 0 1]
            [1 0 0]
        """
    def corner_sum_matrix(self):
        """
        Return the corner sum matrix of ``self``.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[1, 0, 0],[0, 1, 0],[0, 0, 1]]).corner_sum_matrix()
            [0 0 0 0]
            [0 1 1 1]
            [0 1 2 2]
            [0 1 2 3]
            sage: asm = A([[0, 1, 0],[1, -1, 1],[0, 1, 0]])
            sage: asm.corner_sum_matrix()
            [0 0 0 0]
            [0 0 1 1]
            [0 1 1 2]
            [0 1 2 3]
            sage: asm = A([[0, 0, 1],[1, 0, 0],[0, 1, 0]])
            sage: asm.corner_sum_matrix()
            [0 0 0 0]
            [0 0 0 1]
            [0 1 1 2]
            [0 1 2 3]

        TESTS:

        Some non-symmetric tests::

            sage: A = AlternatingSignMatrices(3)
            sage: asm = A([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
            sage: asm.corner_sum_matrix()
            [0 0 0 0]
            [0 0 1 1]
            [0 0 1 2]
            [0 1 2 3]
            sage: B = AlternatingSignMatrices(4)
            sage: asm = B([[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, -1, 1], [0, 0, 1, 0]])
            sage: asm.corner_sum_matrix()
            [0 0 0 0 0]
            [0 0 0 1 1]
            [0 1 1 2 2]
            [0 1 2 2 3]
            [0 1 2 3 4]
        """
    def height_function(self):
        """
        Return the height function from ``self``.

        A height function
        corresponding to an `n \\times n` ASM is an `(n+1) \\times (n+1)` matrix
        such that the first row is `0, 1, \\ldots, n`, the last row is
        `n, n-1, \\ldots, 1, 0`, and the difference between adjacent entries
        is 1.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[1, 0, 0],[0, 1, 0],[0, 0, 1]]).height_function()
            [0 1 2 3]
            [1 0 1 2]
            [2 1 0 1]
            [3 2 1 0]
            sage: asm = A([[0, 1, 0],[1, -1, 1],[0, 1, 0]])
            sage: asm.height_function()
            [0 1 2 3]
            [1 2 1 2]
            [2 1 2 1]
            [3 2 1 0]
            sage: asm = A([[0, 0, 1],[1, 0, 0],[0, 1, 0]])
            sage: asm.height_function()
            [0 1 2 3]
            [1 2 1 2]
            [2 3 2 1]
            [3 2 1 0]

            sage: A = AlternatingSignMatrices(4)
            sage: all(A.from_height_function(a.height_function()) == a for a in A)
            True
        """
    def to_six_vertex_model(self):
        """
        Return the six vertex model configuration from ``self``.

        This method calls :meth:`sage.combinat.six_vertex_model.from_alternating_sign_matrix`.

        EXAMPLES::

            sage: asm = AlternatingSignMatrix([[0,1,0],[1,-1,1],[0,1,0]])
            sage: asm.to_six_vertex_model()
                ^    ^    ^
                |    |    |
            --> # -> # <- # <--
                ^    |    ^
                |    V    |
            --> # <- # -> # <--
                |    ^    |
                V    |    V
            --> # -> # <- # <--
                |    |    |
                V    V    V

        TESTS::

            sage: ASM = AlternatingSignMatrices(5)
            sage: all((x.to_six_vertex_model()).to_alternating_sign_matrix() == x
            ....:     for x in ASM)
            True
        """
    def to_fully_packed_loop(self):
        """
        Return the fully packed loop configuration from ``self``.

        .. SEEALSO::

            :class:`FullyPackedLoop`

        EXAMPLES::

            sage: asm = AlternatingSignMatrix([[1,0,0],[0,1,0],[0,0,1]])
            sage: fpl = asm.to_fully_packed_loop()
            sage: fpl
                │         │
                │         │
                +    + ── +
                │    │
                │    │
             ── +    +    + ──
                     │    │
                     │    │
                + ── +    +
                │         │
                │         │
        """
    def link_pattern(self):
        """
        Return the link pattern corresponding to the fully packed loop
        corresponding to ``self``.

        EXAMPLES:

        We can extract the underlying link pattern (a non-crossing
        partition) from a fully packed loop::

            sage: A = AlternatingSignMatrix([[0, 1, 0], [1, -1, 1], [0, 1, 0]])
            sage: A.link_pattern()
            [(1, 2), (3, 6), (4, 5)]

            sage: B = AlternatingSignMatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            sage: B.link_pattern()
            [(1, 6), (2, 5), (3, 4)]
        """
    def gyration(self):
        """
        Return the alternating sign matrix obtained by applying gyration
        to the height function in bijection with ``self``.

        Gyration acts on height functions as follows. Go through the entries of
        the matrix, first those for which the sum of the row and column indices
        is even, then for those for which it is odd, and increment or decrement
        the squares by 2 wherever possible such that the resulting matrix is
        still a height function. Gyration was first defined in [Wie2000]_ as
        an action on fully-packed loops.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[1, 0, 0],[0, 1, 0],[0, 0, 1]]).gyration()
            [0 0 1]
            [0 1 0]
            [1 0 0]
            sage: asm = A([[0, 1, 0],[1, -1, 1],[0, 1, 0]])
            sage: asm.gyration()
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: asm = A([[0, 0, 1],[1, 0, 0],[0, 1, 0]])
            sage: asm.gyration()
            [0 1 0]
            [0 0 1]
            [1 0 0]
            sage: A = AlternatingSignMatrices(3)
            sage: A([[1, 0, 0],[0, 1, 0],[0, 0, 1]]).gyration().gyration()
            [ 0  1  0]
            [ 1 -1  1]
            [ 0  1  0]
            sage: A([[1, 0, 0],[0, 1, 0],[0, 0, 1]]).gyration().gyration().gyration()
            [1 0 0]
            [0 1 0]
            [0 0 1]

            sage: A = AlternatingSignMatrices(4)
            sage: M = A([[0,0,1,0],[1,0,0,0],[0,1,-1,1],[0,0,1,0]])
            sage: for i in range(5):
            ....:     M = M.gyration()
            sage: M
            [1 0 0 0]
            [0 0 0 1]
            [0 1 0 0]
            [0 0 1 0]

            sage: a0 = a = AlternatingSignMatrices(5).random_element()
            sage: for i in range(20):
            ....:     a = a.gyration()
            sage: a == a0
            True
        """
    def gyration_orbit(self):
        """
        Return the gyration orbit of ``self`` (including ``self``).

        EXAMPLES::

            sage: AlternatingSignMatrix([[0,1,0],[1,-1,1],[0,1,0]]).gyration_orbit()
            [
            [ 0  1  0]  [1 0 0]  [0 0 1]
            [ 1 -1  1]  [0 1 0]  [0 1 0]
            [ 0  1  0], [0 0 1], [1 0 0]
            ]

            sage: AlternatingSignMatrix([[0,1,0,0],[1,-1,1,0],[0,1,-1,1],[0,0,1,0]]).gyration_orbit()
            [
            [ 0  1  0  0]  [1 0 0 0]  [ 0  0  1  0]  [0 0 0 1]
            [ 1 -1  1  0]  [0 1 0 0]  [ 0  1 -1  1]  [0 0 1 0]
            [ 0  1 -1  1]  [0 0 1 0]  [ 1 -1  1  0]  [0 1 0 0]
            [ 0  0  1  0], [0 0 0 1], [ 0  1  0  0], [1 0 0 0]
            ]

            sage: len(AlternatingSignMatrix([[0,1,0,0,0,0],[0,0,1,0,0,0],[1,-1,0,0,0,1],
            ....: [0,1,0,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0]]).gyration_orbit())
            12
        """
    def ASM_compatible(self, B):
        """
        Return ``True`` if ``self`` and ``B`` are compatible alternating sign
        matrices in the sense of [EKLP1992]_. (If ``self`` is of size `n`, ``B``
        must  be of size `n+1`.)

        In [EKLP1992]_, there is a notion of a pair of ASM's with sizes differing
        by 1 being compatible, in the sense that they can be combined to encode
        a tiling of the Aztec Diamond.

        EXAMPLES::

            sage: A = AlternatingSignMatrix(matrix([[0,0,1,0],[0,1,-1,1],[1,0,0,0],[0,0,1,0]]))
            sage: B = AlternatingSignMatrix(matrix([[0,0,1,0,0],[0,0,0,1,0],[1,0,0,-1,1],[0,1,0,0,0],[0,0,0,1,0]]))
            sage: A.ASM_compatible(B)
            True
            sage: A = AlternatingSignMatrix(matrix([[0,1,0],[1,-1,1],[0,1,0]]))
            sage: B = AlternatingSignMatrix(matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]]))
            sage: A.ASM_compatible(B)
            False
        """
    def ASM_compatible_bigger(self):
        """
        Return all ASM's compatible with ``self`` that are of size one greater
        than ``self``.

        Given an `n \\times n` alternating sign matrix `A`, there are as many
        ASM's of size `n+1` compatible with `A` as 2 raised to the power of
        the number of 1s in `A` [EKLP1992]_.

        EXAMPLES::

            sage: A = AlternatingSignMatrix([[1,0],[0,1]])
            sage: A.ASM_compatible_bigger()
            [
            [ 0  1  0]  [1 0 0]  [0 1 0]  [1 0 0]
            [ 1 -1  1]  [0 0 1]  [1 0 0]  [0 1 0]
            [ 0  1  0], [0 1 0], [0 0 1], [0 0 1]
            ]
            sage: B = AlternatingSignMatrix([[0,1],[1,0]])
            sage: B.ASM_compatible_bigger()
            [
            [0 0 1]  [0 0 1]  [0 1 0]  [ 0  1  0]
            [0 1 0]  [1 0 0]  [0 0 1]  [ 1 -1  1]
            [1 0 0], [0 1 0], [1 0 0], [ 0  1  0]
            ]

            sage: B = AlternatingSignMatrix([[0,1,0],[1,-1,1],[0,1,0]])
            sage: len(B.ASM_compatible_bigger()) == 2**4
            True
        """
    def ASM_compatible_smaller(self):
        """
        Return the list of all ASMs compatible with ``self`` that are of size
        one smaller than ``self``.

        Given an alternating sign matrix `A` of size `n`, there are as many
        ASM's of size `n-1` compatible with it as 2 raised to the power of
        the number of `-1`'s in `A` [EKLP1992]_.

        EXAMPLES::

            sage: A = AlternatingSignMatrix(matrix([[0,0,1,0],[0,1,-1,1],[1,0,0,0],[0,0,1,0]]))
            sage: A.ASM_compatible_smaller()
            [
            [0 0 1]  [ 0  1  0]
            [1 0 0]  [ 1 -1  1]
            [0 1 0], [ 0  1  0]
            ]
            sage: B = AlternatingSignMatrix(matrix([[1,0,0],[0,0,1],[0,1,0]]))
            sage: B.ASM_compatible_smaller()
            [
            [1 0]
            [0 1]
            ]
        """
    def to_dyck_word(self, algorithm):
        """
        Return a Dyck word determined by the specified algorithm.

        The algorithm 'last_diagonal' uses the last diagonal of the monotone
        triangle corresponding to ``self``. The algorithm 'link_pattern' returns
        the Dyck word in bijection with the link pattern of the fully packed
        loop.

        Note that these two algorithms in general yield different Dyck words for a
        given alternating sign matrix.

        INPUT:

        - ``algorithm`` -- either ``'last_diagonal'`` or ``'link_pattern'``

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[0,1,0],[1,0,0],[0,0,1]]).to_dyck_word(algorithm = 'last_diagonal')
            [1, 1, 0, 0, 1, 0]
            sage: d = A([[0,1,0],[1,-1,1],[0,1,0]]).to_dyck_word(algorithm = 'last_diagonal'); d
            [1, 1, 0, 1, 0, 0]
            sage: parent(d)
            Complete Dyck words
            sage: A = AlternatingSignMatrices(3)
            sage: asm = A([[0,1,0],[1,0,0],[0,0,1]])
            sage: asm.to_dyck_word(algorithm = 'link_pattern')
            [1, 0, 1, 0, 1, 0]
            sage: asm = A([[0,1,0],[1,-1,1],[0,1,0]])
            sage: asm.to_dyck_word(algorithm = 'link_pattern')
            [1, 0, 1, 1, 0, 0]
            sage: A = AlternatingSignMatrices(4)
            sage: asm = A([[0,0,1,0],[1,0,0,0],[0,1,-1,1],[0,0,1,0]])
            sage: asm.to_dyck_word(algorithm = 'link_pattern')
            [1, 1, 1, 0, 1, 0, 0, 0]
            sage: asm.to_dyck_word()
            Traceback (most recent call last):
            ...
            TypeError: ...to_dyck_word() ...argument...
            sage: asm.to_dyck_word(algorithm = 'notamethod')
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm 'notamethod'
        """
    def number_negative_ones(self):
        """
        Return the number of entries in ``self`` equal to -1.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: asm = A([[0,1,0],[1,0,0],[0,0,1]])
            sage: asm.number_negative_ones()
            0
            sage: asm = A([[0,1,0],[1,-1,1],[0,1,0]])
            sage: asm.number_negative_ones()
            1
        """
    def is_permutation(self):
        """
        Return ``True`` if ``self`` is a permutation matrix
        and ``False`` otherwise.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: asm = A([[0,1,0],[1,0,0],[0,0,1]])
            sage: asm.is_permutation()
            True
            sage: asm = A([[0,1,0],[1,-1,1],[0,1,0]])
            sage: asm.is_permutation()
            False
        """
    def to_permutation(self):
        """
        Return the corresponding permutation if ``self`` is a permutation
        matrix.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: asm = A([[0,1,0],[1,0,0],[0,0,1]])
            sage: p = asm.to_permutation(); p
            [2, 1, 3]
            sage: parent(p)
            Standard permutations
            sage: asm = A([[0,1,0],[1,-1,1],[0,1,0]])
            sage: asm.to_permutation()
            Traceback (most recent call last):
            ...
            ValueError: not a permutation matrix
        """
    def to_semistandard_tableau(self):
        """
        Return the semistandard tableau corresponding the monotone triangle
        corresponding to ``self``.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[0,0,1],[1,0,0],[0,1,0]]).to_semistandard_tableau()
            [[1, 1, 3], [2, 3], [3]]
            sage: t = A([[0,1,0],[1,-1,1],[0,1,0]]).to_semistandard_tableau(); t
            [[1, 1, 2], [2, 3], [3]]
            sage: parent(t)
            Semistandard tableaux
        """
    def left_key(self):
        """
        Return the left key of the alternating sign matrix ``self``.

        The left key of an alternating sign matrix was defined by Lascoux
        in [Lasc]_ and is obtained by successively removing all the
        `-1`'s until what remains is a permutation matrix. This notion
        corresponds to the notion of left key for semistandard tableaux. So
        our algorithm proceeds as follows: we map ``self`` to its
        corresponding monotone triangle, view that monotone triangle as a
        semistandard tableau, take its left key, and then map back through
        monotone triangles to the permutation matrix which is the left key.

        See also [Ava2007]_.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[0,0,1],[1,0,0],[0,1,0]]).left_key()
            [0 0 1]
            [1 0 0]
            [0 1 0]
            sage: t = A([[0,1,0],[1,-1,1],[0,1,0]]).left_key(); t
            [1 0 0]
            [0 0 1]
            [0 1 0]
            sage: parent(t)
            Alternating sign matrices of size 3
        """
    def left_key_as_permutation(self):
        """
        Return the permutation of the left key of ``self``.

        .. SEEALSO::

            - :meth:`left_key()`

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A([[0,0,1],[1,0,0],[0,1,0]]).left_key_as_permutation()
            [3, 1, 2]
            sage: t = A([[0,1,0],[1,-1,1],[0,1,0]]).left_key_as_permutation(); t
            [1, 3, 2]
            sage: parent(t)
            Standard permutations
        """

class AlternatingSignMatrices(UniqueRepresentation, Parent):
    """
    Class of all `n \\times n` alternating sign matrices.

    An alternating sign matrix of size `n` is an `n \\times n` matrix of `0`'s,
    `1`'s and `-1`'s such that the sum of each row and column is `1` and the
    nonzero entries in each row and column alternate in sign.

    Alternating sign matrices of size `n` are in bijection with
    :class:`monotone triangles <MonotoneTriangles>` with `n` rows.

    INPUT:

    - ``n`` -- integer; the size of the matrices

    EXAMPLES:

    This will create an instance to manipulate the alternating sign
    matrices of size 3::

        sage: A = AlternatingSignMatrices(3)
        sage: A
        Alternating sign matrices of size 3
        sage: A.cardinality()
        7

    Notably, this implementation allows to make a lattice of it::

        sage: L = A.lattice()
        sage: L
        Finite lattice containing 7 elements
        sage: L.category()
        Category of facade finite enumerated lattice posets
    """
    def __init__(self, n) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: A = AlternatingSignMatrices(4)
            sage: TestSuite(A).run()
        """
    def __contains__(self, asm) -> bool:
        """
        Check if ``asm`` is in ``self``.

        TESTS::

            sage: A = AlternatingSignMatrices(3)
            sage: [[0,1,0],[1,0,0],[0,0,1]] in A
            True
            sage: [[0,1,0],[1,-1,1],[0,1,0]] in A
            True
            sage: [[0, 1],[1,0]] in A
            False
            sage: [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] in A
            False
            sage: [[-1, 1, 1],[1,-1,1],[1,1,-1]] in A
            False

            sage: M = MatrixSpace(ZZ, 3)
            sage: for p in [[-1,1,1,1,0,0,1,0,0],
            ....:           [0,1,0,0,1,0,1,-1,1],
            ....:           [0,1,0,0,2,0,1,-2,1],
            ....:           [0,2,0,1,-2,1,0,1,0]]:
            ....:     m = M(p)
            ....:     assert not m in A
            ....:     m = m.transpose()
            ....:     assert not m in A
            ....:     m = m.antitranspose()
            ....:     assert not m in A
            ....:     m = m.transpose()
            ....:     assert not m in A

        Exhaustive verifications for `2 \times 2` and `3 \times 3` matrices::

            sage: from itertools import product

            sage: M = MatrixSpace(ZZ, 2)
            sage: A = AlternatingSignMatrices(2)
            sage: mats = [M(p) for p in product([-1,0,1], repeat=4)]
            sage: sum(1 for m in mats if m in A)
            2

            sage: M = MatrixSpace(ZZ, 3)
            sage: A = AlternatingSignMatrices(3)
            sage: mats = [M(p) for p in product([-1,0,1], repeat=9)]
            sage: sum(1 for m in mats if m in A)
            7
        """
    Element = AlternatingSignMatrix
    def random_element(self):
        '''
        Return a uniformly random alternating sign matrix.

        EXAMPLES::

            sage: AlternatingSignMatrices(7).random_element()  # random
            [ 0  0  0  0  1  0  0]
            [ 0  0  1  0 -1  0  1]
            [ 0  0  0  0  1  0  0]
            [ 0  1 -1  0  0  1  0]
            [ 1 -1  1  0  0  0  0]
            [ 0  0  0  1  0  0  0]
            [ 0  1  0  0  0  0  0]
            sage: a = AlternatingSignMatrices(5).random_element()
            sage: bool(a.number_negative_ones()) or a.is_permutation()
            True

        This is done using a modified version of Propp and Wilson\'s "coupling
        from the past" algorithm. It creates a uniformly random Gelfand-Tsetlin
        triangle with top row `[n, n-1, \\ldots 2, 1]`, and then converts it to
        an alternating sign matrix.
        '''
    def from_monotone_triangle(self, triangle, check: bool = True):
        """
        Return an alternating sign matrix from a monotone triangle.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A.from_monotone_triangle([[3, 2, 1], [2, 1], [1]])
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: A.from_monotone_triangle([[3, 2, 1], [3, 2], [3]])
            [0 0 1]
            [0 1 0]
            [1 0 0]


            sage: A.from_monotone_triangle([[3, 2, 1], [2, 2], [1]])
            Traceback (most recent call last):
            ...
            ValueError: not a valid triangle
        """
    def from_corner_sum(self, corner):
        """
        Return an alternating sign matrix from a corner sum matrix.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A.from_corner_sum(matrix([[0,0,0,0],[0,1,1,1],[0,1,2,2],[0,1,2,3]]))
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: A.from_corner_sum(matrix([[0,0,0,0],[0,0,1,1],[0,1,1,2],[0,1,2,3]]))
            [ 0  1  0]
            [ 1 -1  1]
            [ 0  1  0]

        TESTS::

            sage: A = AlternatingSignMatrices(4)
            sage: all(A.from_corner_sum(a.corner_sum_matrix()) == a for a in A)
            True
        """
    def from_height_function(self, height):
        """
        Return an alternating sign matrix from a height function.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A.from_height_function(matrix([[0,1,2,3],[1,2,1,2],[2,3,2,1],[3,2,1,0]]))
            [0 0 1]
            [1 0 0]
            [0 1 0]
            sage: A.from_height_function(matrix([[0,1,2,3],[1,2,1,2],[2,1,2,1],[3,2,1,0]]))
            [ 0  1  0]
            [ 1 -1  1]
            [ 0  1  0]
        """
    def from_contre_tableau(self, comps):
        """
        Return an alternating sign matrix from a contre-tableau.

        EXAMPLES::

            sage: ASM = AlternatingSignMatrices(3)
            sage: ASM.from_contre_tableau([[1, 2, 3], [1, 2], [1]])
            [0 0 1]
            [0 1 0]
            [1 0 0]
            sage: ASM.from_contre_tableau([[1, 2, 3], [2, 3], [3]])
            [1 0 0]
            [0 1 0]
            [0 0 1]
        """
    def size(self):
        """
        Return the size of the matrices in ``self``.

        TESTS::

            sage: A = AlternatingSignMatrices(4)
            sage: A.size()
            4
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        The number of `n \\times n` alternating sign matrices is equal to

        .. MATH::

            \\prod_{k=0}^{n-1} \\frac{(3k+1)!}{(n+k)!} = \\frac{1! 4! 7! 10!
            \\cdots (3n-2)!}{n! (n+1)! (n+2)! (n+3)! \\cdots (2n-1)!}

        EXAMPLES::

            sage: [AlternatingSignMatrices(n).cardinality() for n in range(11)]
            [1, 1, 2, 7, 42, 429, 7436, 218348, 10850216, 911835460, 129534272700]
        """
    def matrix_space(self):
        """
        Return the underlying matrix space.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: A.matrix_space()
            Full MatrixSpace of 3 by 3 dense matrices over Integer Ring
        """
    def __iter__(self):
        """
        Iterator on the alternating sign matrices of size `n`.

        TESTS::

            sage: AlternatingSignMatrices(3).list()
            [
            [1 0 0]  [0 1 0]  [1 0 0]  [ 0  1  0]  [0 0 1]  [0 1 0]  [0 0 1]
            [0 1 0]  [1 0 0]  [0 0 1]  [ 1 -1  1]  [1 0 0]  [0 0 1]  [0 1 0]
            [0 0 1], [0 0 1], [0 1 0], [ 0  1  0], [0 1 0], [1 0 0], [1 0 0]
            ]
            sage: sum(1 for a in AlternatingSignMatrices(4))
            42
        """
    def first(self):
        """
        Return the first alternating sign matrix.

        EXAMPLES::

            sage: AlternatingSignMatrices(5).first()
            [1 0 0 0 0]
            [0 1 0 0 0]
            [0 0 1 0 0]
            [0 0 0 1 0]
            [0 0 0 0 1]
        """
    def last(self):
        """
        Return the last alternating sign matrix.

        EXAMPLES::

            sage: AlternatingSignMatrices(5).last()
            [0 0 0 0 1]
            [0 0 0 1 0]
            [0 0 1 0 0]
            [0 1 0 0 0]
            [1 0 0 0 0]
        """
    def cover_relations(self):
        """
        Iterate on the cover relations between the alternating sign
        matrices.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: for a, b in A.cover_relations():
            ....:   eval('a, b')
            (
            [1 0 0]  [0 1 0]
            [0 1 0]  [1 0 0]
            [0 0 1], [0 0 1]
            )
            (
            [1 0 0]  [1 0 0]
            [0 1 0]  [0 0 1]
            [0 0 1], [0 1 0]
            )
            (
            [0 1 0]  [ 0  1  0]
            [1 0 0]  [ 1 -1  1]
            [0 0 1], [ 0  1  0]
            )
            (
            [1 0 0]  [ 0  1  0]
            [0 0 1]  [ 1 -1  1]
            [0 1 0], [ 0  1  0]
            )
            (
            [ 0  1  0]  [0 0 1]
            [ 1 -1  1]  [1 0 0]
            [ 0  1  0], [0 1 0]
            )
            (
            [ 0  1  0]  [0 1 0]
            [ 1 -1  1]  [0 0 1]
            [ 0  1  0], [1 0 0]
            )
            (
            [0 0 1]  [0 0 1]
            [1 0 0]  [0 1 0]
            [0 1 0], [1 0 0]
            )
            (
            [0 1 0]  [0 0 1]
            [0 0 1]  [0 1 0]
            [1 0 0], [1 0 0]
            )
        """
    def lattice(self):
        """
        Return the lattice of the alternating sign matrices of size
        `n`, created by ``LatticePoset``.

        EXAMPLES::

            sage: A = AlternatingSignMatrices(3)
            sage: L = A.lattice()
            sage: L
            Finite lattice containing 7 elements
        """
    @cached_method
    def gyration_orbits(self):
        """
        Return the list of gyration orbits of ``self``.

        EXAMPLES::

            sage: AlternatingSignMatrices(3).gyration_orbits()
            ((
              [1 0 0]  [0 0 1]  [ 0  1  0]
              [0 1 0]  [0 1 0]  [ 1 -1  1]
              [0 0 1], [1 0 0], [ 0  1  0]
             ),
             (
              [0 1 0]  [1 0 0]
              [1 0 0]  [0 0 1]
              [0 0 1], [0 1 0]
             ),
             (
              [0 0 1]  [0 1 0]
              [1 0 0]  [0 0 1]
              [0 1 0], [1 0 0]
             ))
        """
    def gyration_orbit_sizes(self):
        """
        Return the sizes of gyration orbits of ``self``.

        EXAMPLES::

            sage: AlternatingSignMatrices(3).gyration_orbit_sizes()
            [3, 2, 2]
            sage: AlternatingSignMatrices(4).gyration_orbit_sizes()
            [4, 8, 2, 8, 8, 8, 2, 2]

            sage: A = AlternatingSignMatrices(5)
            sage: li = [5,10,10,10,10,10,2,5,10,10,10,10,10,10,10,10,10,10,10,10,
            ....: 4,10,10,10,10,10,10,4,5,10,10,10,10,10,10,10,2,4,5,10,10,10,10,10,10,
            ....: 4,5,10,10,2,2]
            sage: A.gyration_orbit_sizes() == li
            True
        """

class MonotoneTriangles(GelfandTsetlinPatternsTopRow):
    """
    Monotone triangles with `n` rows.

    A monotone triangle is a number triangle `(a_{i,j})_{1 \\leq i \\leq
    n , 1 \\leq j \\leq i}` on `\\{1, \\dots, n\\}` such that:

    - `a_{i,j} < a_{i,j+1}`

    - `a_{i+1,j} < a_{i,j} \\leq a_{i+1,j+1}`

    This notably requires that the bottom column is ``[1,...,n]``.

    Alternatively a monotone triangle is a strict Gelfand-Tsetlin pattern with
    top row `(n, \\ldots, 2, 1)`.

    INPUT:

    - ``n`` -- the number of rows in the monotone triangles

    EXAMPLES:

    This represents the monotone triangles with base ``[3,2,1]``::

        sage: M = MonotoneTriangles(3)
        sage: M
        Monotone triangles with 3 rows
        sage: M.cardinality()
        7

    The monotone triangles are a lattice::

        sage: M.lattice()
        Finite lattice containing 7 elements

    Monotone triangles can be converted to alternating sign matrices
    and back::

        sage: M = MonotoneTriangles(5)
        sage: A = AlternatingSignMatrices(5)
        sage: all(A.from_monotone_triangle(m).to_monotone_triangle() == m for m in M)
        True
    """
    def __init__(self, n) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: M = MonotoneTriangles(4)
            sage: TestSuite(M).run()
            sage: M2 = MonotoneTriangles(int(4))
            sage: M is M2
            True
        """
    def cardinality(self):
        """
        Cardinality of ``self``.

        The number of monotone triangles with `n` rows is equal to

        .. MATH::

            \\prod_{k=0}^{n-1} \\frac{(3k+1)!}{(n+k)!} = \\frac{1! 4! 7! 10!
            \\cdots (3n-2)!}{n! (n+1)! (n+2)! (n+3)! \\cdots (2n-1)!}

        EXAMPLES::

            sage: M = MonotoneTriangles(4)
            sage: M.cardinality()
            42
        """
    def cover_relations(self):
        """
        Iterate on the cover relations in the set of monotone triangles
        with `n` rows.

        EXAMPLES::

            sage: M = MonotoneTriangles(3)
            sage: for a, b in M.cover_relations():
            ....:   eval('a, b')
            ([[3, 2, 1], [2, 1], [1]], [[3, 2, 1], [2, 1], [2]])
            ([[3, 2, 1], [2, 1], [1]], [[3, 2, 1], [3, 1], [1]])
            ([[3, 2, 1], [2, 1], [2]], [[3, 2, 1], [3, 1], [2]])
            ([[3, 2, 1], [3, 1], [1]], [[3, 2, 1], [3, 1], [2]])
            ([[3, 2, 1], [3, 1], [2]], [[3, 2, 1], [3, 1], [3]])
            ([[3, 2, 1], [3, 1], [2]], [[3, 2, 1], [3, 2], [2]])
            ([[3, 2, 1], [3, 1], [3]], [[3, 2, 1], [3, 2], [3]])
            ([[3, 2, 1], [3, 2], [2]], [[3, 2, 1], [3, 2], [3]])
        """
    def lattice(self):
        """
        Return the lattice of the monotone triangles with `n` rows.

        EXAMPLES::

            sage: M = MonotoneTriangles(3)
            sage: P = M.lattice()
            sage: P
            Finite lattice containing 7 elements
        """

class ContreTableaux(Parent, metaclass=ClasscallMetaclass):
    """
    Factory class for the combinatorial class of contre tableaux of size `n`.

    EXAMPLES::

        sage: ct4 = ContreTableaux(4); ct4
        Contre tableaux of size 4
        sage: ct4.cardinality()
        42
    """
    @staticmethod
    def __classcall_private__(cls, n, **kwds):
        """
        Factory pattern.

        Check properties on arguments, then call the appropriate class.

        EXAMPLES::

            sage: C = ContreTableaux(4)
            sage: type(C)
            <class 'sage.combinat.alternating_sign_matrix.ContreTableaux_n'>
        """

class ContreTableaux_n(ContreTableaux):
    n: Incomplete
    def __init__(self, n) -> None:
        """
        TESTS::

            sage: ct2 = ContreTableaux(2); ct2
            Contre tableaux of size 2
            sage: ct2 == loads(dumps(ct2))
            True
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: C = ContreTableaux(4)
            sage: C == loads(dumps(C))
            True
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: [ContreTableaux(n).cardinality() for n in range(11)]
            [1, 1, 2, 7, 42, 429, 7436, 218348, 10850216, 911835460, 129534272700]
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: list(ContreTableaux(0))
            [[]]
            sage: list(ContreTableaux(1))
            [[[1]]]
            sage: list(ContreTableaux(2))
            [[[1, 2], [1]], [[1, 2], [2]]]
            sage: list(ContreTableaux(3))
            [[[1, 2, 3], [1, 2], [1]],
             [[1, 2, 3], [1, 2], [2]],
             [[1, 2, 3], [1, 3], [1]],
             [[1, 2, 3], [1, 3], [2]],
             [[1, 2, 3], [1, 3], [3]],
             [[1, 2, 3], [2, 3], [2]],
             [[1, 2, 3], [2, 3], [3]]]
        """

class TruncatedStaircases(Parent, metaclass=ClasscallMetaclass):
    """
    Factory class for the combinatorial class of truncated staircases
    of size ``n`` with last column ``last_column``.

    EXAMPLES::

        sage: t4 = TruncatedStaircases(4, [2,3]); t4
        Truncated staircases of size 4 with last column [2, 3]
        sage: t4.cardinality()
        4
    """
    @staticmethod
    def __classcall_private__(cls, n, last_column, **kwds):
        """
        Factory pattern.

        Check properties on arguments, then call the appropriate class.

        TESTS::

            sage: T = TruncatedStaircases(4, [2,3])
            sage: type(T)
            <class 'sage.combinat.alternating_sign_matrix.TruncatedStaircases_nlastcolumn'>
        """

class TruncatedStaircases_nlastcolumn(TruncatedStaircases):
    n: Incomplete
    last_column: Incomplete
    def __init__(self, n, last_column) -> None:
        """
        TESTS::

            sage: t4 = TruncatedStaircases(4, [2,3]); t4
            Truncated staircases of size 4 with last column [2, 3]
            sage: t4 == loads(dumps(t4))
            True
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: list(TruncatedStaircases(4, [2,3]))
            [[[4, 3, 2, 1], [3, 2, 1], [3, 2]], [[4, 3, 2, 1], [4, 2, 1], [3, 2]], [[4, 3, 2, 1], [4, 3, 1], [3, 2]], [[4, 3, 2, 1], [4, 3, 2], [3, 2]]]
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: T = TruncatedStaircases(4, [2,3])
            sage: T == loads(dumps(T))
            True
        """
    def cardinality(self):
        """
        EXAMPLES::

            sage: T = TruncatedStaircases(4, [2,3])
            sage: T.cardinality()
            4
        """
