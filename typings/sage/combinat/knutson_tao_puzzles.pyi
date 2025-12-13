from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.finite_rings.integer_mod_ring import Integers as Integers
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class PuzzlePiece:
    """
    Abstract class for puzzle pieces.

    This abstract class contains information on how to test equality of
    puzzle pieces, and sets color and plotting options.
    """
    def __eq__(self, other) -> bool:
        """
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: delta = DeltaPiece('a','b','c')
            sage: delta1 = DeltaPiece('a','b','c')
            sage: delta == delta1
            True
            sage: delta1 = DeltaPiece('A','b','c')
            sage: delta == delta1
            False
        """
    def __hash__(self):
        """
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: delta = DeltaPiece('a','b','c')
            sage: hash(delta) == hash(delta)
            True
        """
    def border(self) -> tuple:
        """
        Return the border of ``self``.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: delta = DeltaPiece('a','b','c')
            sage: sorted(delta.border())
            ['a', 'b', 'c']
        """
    def color(self) -> str:
        """
        Return the color of ``self``.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: delta = DeltaPiece('a','b','c')
            sage: delta.color()
            'white'
            sage: delta = DeltaPiece('0','0','0')
            sage: delta.color()
            'red'
            sage: delta = DeltaPiece('1','1','1')
            sage: delta.color()
            'blue'
            sage: delta = DeltaPiece('2','2','2')
            sage: delta.color()
            'green'
            sage: delta = DeltaPiece('2','K','2')
            sage: delta.color()
            'orange'
            sage: delta = DeltaPiece('2','T1/2','2')
            sage: delta.color()
            'yellow'
        """
    def edge_color(self, edge) -> str:
        """
        Color of the specified edge of ``self`` (to be used when plotting the
        piece).

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: delta = DeltaPiece('1','0','10')
            sage: delta.edge_color('south')
            'blue'
            sage: delta.edge_color('north_west')
            'red'
            sage: delta.edge_color('north_east')
            'white'
        """
    def edge_label(self, edge) -> str:
        """
        Return the edge label of ``edge``.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: delta = DeltaPiece('2','K','2')
            sage: delta.edge_label('south')
            '2'
            sage: delta.edge_label('north_east')
            '2'
            sage: delta.edge_label('north_west')
            'K'
        """
    __getitem__ = edge_label

class NablaPiece(PuzzlePiece):
    """
    Nabla Piece takes as input three labels, inputted as strings. They label
    the North, Southeast and Southwest edges, respectively.

    EXAMPLES::

        sage: from sage.combinat.knutson_tao_puzzles import NablaPiece
        sage: NablaPiece('a','b','c')
        c\\a/b
    """
    def __init__(self, north, south_east, south_west) -> None:
        """
        INPUT:

        - ``north``, ``south_east``, ``south_west`` -- strings, which label the edges

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import NablaPiece
            sage: NablaPiece('1','2','3')
            3\\1/2
        """
    def __eq__(self, other) -> bool:
        """
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import NablaPiece
            sage: n = NablaPiece('a','b','c')
            sage: n1 = NablaPiece('a','b','c')
            sage: n == n1
            True
            sage: n1 = NablaPiece('A','b','c')
            sage: n == n1
            False
        """
    def __hash__(self):
        """
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import NablaPiece
            sage: n = NablaPiece('a','b','c')
            sage: hash(n) == hash(n)
            True
        """
    def clockwise_rotation(self) -> NablaPiece:
        """
        Rotate the Nabla piece by 120 degree clockwise.

        OUTPUT: Nabla piece

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import NablaPiece
            sage: nabla = NablaPiece('1','2','3')
            sage: nabla.clockwise_rotation()
            2\\3/1
        """
    def half_turn_rotation(self) -> DeltaPiece:
        """
        Rotate the Nabla piece by 180 degree.

        OUTPUT: Delta piece

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import NablaPiece
            sage: nabla = NablaPiece('1','2','3')
            sage: nabla.half_turn_rotation()
            2/1\\3
        """
    def edges(self) -> tuple:
        """
        Return the tuple of edge names.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import NablaPiece
            sage: nabla = NablaPiece('1','2','3')
            sage: nabla.edges()
            ('north', 'south_east', 'south_west')
        """

class DeltaPiece(PuzzlePiece):
    """
    Delta Piece takes as input three labels, inputted as strings. They label
    the South, Northwest and Northeast edges, respectively.

    EXAMPLES::

        sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
        sage: DeltaPiece('a','b','c')
        b/a\\c
    """
    def __init__(self, south, north_west, north_east) -> None:
        """
        INPUT:

        - ``south``, ``north_west``, ``north_east`` -- strings, which label the edges

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: DeltaPiece('1','2','3')
            2/1\\3
        """
    def __eq__(self, other) -> bool:
        """
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: delta = DeltaPiece('a','b','c')
            sage: delta1 = DeltaPiece('a','b','c')
            sage: delta == delta1
            True
            sage: delta1 = DeltaPiece('A','b','c')
            sage: delta == delta1
            False
        """
    def __hash__(self):
        """
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: delta = DeltaPiece('a','b','c')
            sage: hash(delta) == hash(delta)
            True
        """
    def clockwise_rotation(self) -> DeltaPiece:
        """
        Rotate the Delta piece by 120 degree clockwise.

        OUTPUT: Delta piece

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: delta = DeltaPiece('1','2','3')
            sage: delta.clockwise_rotation()
            1/3\\2
        """
    def half_turn_rotation(self) -> NablaPiece:
        """
        Rotate the Delta piece by 180 degree.

        OUTPUT: Nabla piece

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: delta = DeltaPiece('1','2','3')
            sage: delta.half_turn_rotation()
            3\\1/2
        """
    def edges(self) -> tuple:
        """
        Return the tuple of edge names.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece
            sage: delta = DeltaPiece('1','2','3')
            sage: delta.edges()
            ('south', 'north_west', 'north_east')
        """

class RhombusPiece(PuzzlePiece):
    """
    Class of rhombi pieces.

    To construct a rhombus piece we input a delta and a nabla piece.
    The delta and nabla pieces are joined along the south and north edge,
    respectively.

    EXAMPLES::

        sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece, NablaPiece, RhombusPiece
        sage: delta = DeltaPiece('1','2','3')
        sage: nabla = NablaPiece('4','5','6')
        sage: RhombusPiece(delta,nabla)
        2/\\3  6\\/5
    """
    def __init__(self, north_piece, south_piece) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece, NablaPiece, RhombusPiece
            sage: delta = DeltaPiece('1','2','3')
            sage: nabla = NablaPiece('4','5','6')
            sage: RhombusPiece(delta,nabla)
            2/\\3  6\\/5
        """
    def __eq__(self, other) -> bool:
        """
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece, NablaPiece, RhombusPiece
            sage: delta = DeltaPiece('1','2','3')
            sage: nabla = NablaPiece('4','5','6')
            sage: r = RhombusPiece(delta,nabla)
            sage: r == r
            True
            sage: delta1 = DeltaPiece('A','b','c')
            sage: r == RhombusPiece(delta1,nabla)
            False
        """
    def __hash__(self):
        """
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece, NablaPiece, RhombusPiece
            sage: delta = DeltaPiece('1','2','3')
            sage: nabla = NablaPiece('4','5','6')
            sage: r = RhombusPiece(delta,nabla)
            sage: hash(r) == hash(r)
            True
        """
    def __iter__(self):
        """
        Return the list of the north and south piece.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece, NablaPiece, RhombusPiece
            sage: delta = DeltaPiece('1','2','3')
            sage: nabla = NablaPiece('4','5','6')
            sage: r = RhombusPiece(delta,nabla)
            sage: list(r)
            [2/1\\3, 6\\4/5]
        """
    def north_piece(self) -> DeltaPiece:
        """
        Return the north piece.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece, NablaPiece, RhombusPiece
            sage: delta = DeltaPiece('1','2','3')
            sage: nabla = NablaPiece('4','5','6')
            sage: r = RhombusPiece(delta,nabla)
            sage: r.north_piece()
            2/1\\3
        """
    def south_piece(self) -> NablaPiece:
        """
        Return the south piece.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece, NablaPiece, RhombusPiece
            sage: delta = DeltaPiece('1','2','3')
            sage: nabla = NablaPiece('4','5','6')
            sage: r = RhombusPiece(delta,nabla)
            sage: r.south_piece()
            6\\4/5
        """
    def edges(self) -> tuple:
        """
        Return the tuple of edge names.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece, NablaPiece, RhombusPiece
            sage: delta = DeltaPiece('1','2','3')
            sage: nabla = NablaPiece('4','5','6')
            sage: RhombusPiece(delta,nabla).edges()
            ('north_west', 'north_east', 'south_east', 'south_west')
        """

class PuzzlePieces:
    """
    Construct a valid set of puzzle pieces.

    This class constructs the set of valid puzzle pieces. It can take a list of
    forbidden border labels as input. These labels are forbidden from appearing
    on the south edge of a puzzle filling. The user can add valid nabla or
    delta pieces and specify which rotations of these pieces are legal. For
    example, ``rotations=0`` does not add any additional pieces (only the piece
    itself), ``rotations=60`` adds six pieces (the pieces and its rotations by
    60, 120, 180, 240, 300), etc..

    EXAMPLES::

        sage: from sage.combinat.knutson_tao_puzzles import PuzzlePieces, NablaPiece
        sage: forbidden_border_labels = ['10']
        sage: pieces = PuzzlePieces(forbidden_border_labels)
        sage: pieces.add_piece(NablaPiece('0','0','0'), rotations=60)
        sage: pieces.add_piece(NablaPiece('1','1','1'), rotations=60)
        sage: pieces.add_piece(NablaPiece('1','0','10'), rotations=60)
        sage: pieces
        Nablas : [0\\0/0, 0\\10/1, 10\\1/0, 1\\0/10, 1\\1/1]
        Deltas : [0/0\\0, 0/1\\10, 1/10\\0, 1/1\\1, 10/0\\1]

    The user can obtain the list of valid rhombi pieces as follows::

        sage: sorted([p for p in pieces.rhombus_pieces()], key=str)
        [0/\\0  0\\/0, 0/\\0  1\\/10, 0/\\10  10\\/0, 0/\\10  1\\/1, 1/\\0  0\\/1,
        1/\\1  10\\/0, 1/\\1  1\\/1, 10/\\1  0\\/0, 10/\\1  1\\/10]
    """
    def __init__(self, forbidden_border_labels=None) -> None:
        """
        INPUT:

        - ``forbidden_border_labels`` -- list of forbidden border labels given as strings

        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzlePieces
            sage: forbidden_border_labels = ['10']
            sage: pieces = PuzzlePieces(forbidden_border_labels)
            sage: pieces
            Nablas : []
            Deltas : []

            sage: PuzzlePieces('10')
            Traceback (most recent call last):
            ...
            TypeError: Input must be a list
        """
    def __eq__(self, other) -> bool:
        """
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import H_grassmannian_pieces
            sage: x = H_grassmannian_pieces()
            sage: y = H_grassmannian_pieces()
            sage: x == y
            True
        """
    def __hash__(self):
        """
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import H_grassmannian_pieces
            sage: x = H_grassmannian_pieces()
            sage: hash(x) == hash(x)
            True
        """
    def add_piece(self, piece, rotations: int = 120) -> None:
        """
        Add ``piece`` to the list of pieces.

        INPUT:

        - ``piece`` -- a nabla piece or a delta piece
        - ``rotations`` -- (default: 120) 0, 60, 120, 180

        The user can add valid nabla or delta pieces and specify
        which rotations of these pieces are legal. For example, ``rotations=0``
        does not add any additional pieces (only the piece itself), ``rotations=60`` adds
        six pieces (namely three delta and three nabla pieces), while
        ``rotations=120`` adds only delta or nabla (depending on which piece ``self`` is).
        ``rotations=180`` adds the piece and its 180 degree rotation, i.e. one delta and one
        nabla piece.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzlePieces, DeltaPiece
            sage: delta = DeltaPiece('a','b','c')
            sage: pieces = PuzzlePieces()
            sage: pieces
            Nablas : []
            Deltas : []
            sage: pieces.add_piece(delta)
            sage: pieces
            Nablas : []
            Deltas : [a/c\\b, b/a\\c, c/b\\a]

            sage: pieces = PuzzlePieces()
            sage: pieces.add_piece(delta,rotations=0)
            sage: pieces
            Nablas : []
            Deltas : [b/a\\c]

            sage: pieces = PuzzlePieces()
            sage: pieces.add_piece(delta,rotations=60)
            sage: pieces
            Nablas : [a\\b/c, b\\c/a, c\\a/b]
            Deltas : [a/c\\b, b/a\\c, c/b\\a]
        """
    def add_forbidden_label(self, label) -> None:
        """
        Add forbidden border labels.

        INPUT:

        - ``label`` -- string specifying a new forbidden label

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzlePieces
            sage: pieces = PuzzlePieces()
            sage: pieces.add_forbidden_label('1')
            sage: pieces._forbidden_border_labels
            ['1']
            sage: pieces.add_forbidden_label('2')
            sage: pieces._forbidden_border_labels
            ['1', '2']
        """
    def add_T_piece(self, label1, label2) -> None:
        """
        Add a nabla and delta piece with ``label1`` and ``label2``.

        This method adds a nabla piece with edges ``label2``\\ T``label1``|``label2`` / ``label1``.
        and a delta piece with edges ``label1``/ T``label1``|``label2`` \\ ``label2``.
        It also adds T``label1``|``label2`` to the forbidden list.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzlePieces
            sage: pieces = PuzzlePieces()
            sage: pieces.add_T_piece('1','3')
            sage: pieces
            Nablas : [3\\T1|3/1]
            Deltas : [1/T1|3\\3]
            sage: pieces._forbidden_border_labels
            ['T1|3']
        """
    def delta_pieces(self):
        """
        Return the delta pieces as a set.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzlePieces, DeltaPiece
            sage: pieces = PuzzlePieces()
            sage: delta = DeltaPiece('a','b','c')
            sage: pieces.add_piece(delta,rotations=60)
            sage: sorted([p for p in pieces.delta_pieces()], key=str)
            [a/c\\b, b/a\\c, c/b\\a]
        """
    def nabla_pieces(self):
        """
        Return the nabla pieces as a set.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzlePieces, DeltaPiece
            sage: pieces = PuzzlePieces()
            sage: delta = DeltaPiece('a','b','c')
            sage: pieces.add_piece(delta,rotations=60)
            sage: sorted([p for p in pieces.nabla_pieces()], key=str)
            [a\\b/c, b\\c/a, c\\a/b]
        """
    def rhombus_pieces(self) -> set:
        """
        Return a set of all allowable rhombus pieces.

        Allowable rhombus pieces are those where the south edge of the delta
        piece equals the north edge of the nabla piece.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzlePieces, DeltaPiece
            sage: pieces = PuzzlePieces()
            sage: delta = DeltaPiece('a','b','c')
            sage: pieces.add_piece(delta,rotations=60)
            sage: sorted([p for p in pieces.rhombus_pieces()], key=str)
            [a/\\b  b\\/a, b/\\c  c\\/b, c/\\a  a\\/c]
        """
    def boundary_deltas(self) -> tuple:
        """
        Return deltas with south edges not in the forbidden list.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzlePieces, DeltaPiece
            sage: pieces = PuzzlePieces(['a'])
            sage: delta = DeltaPiece('a','b','c')
            sage: pieces.add_piece(delta,rotations=60)
            sage: sorted([p for p in pieces.boundary_deltas()], key=str)
            [a/c\\b, c/b\\a]
        """

def H_grassmannian_pieces():
    """
    Define the puzzle pieces used in computing the cohomology of the Grassmannian.

    REFERENCES:

    .. [KTW] Allen Knutson, Terence Tao, Christopher Woodward,
       The honeycomb model of GL(n) tensor products II: Puzzles determine facets of the Littlewood-Richardson cone,
       :arxiv:`math/0107011`

    EXAMPLES::

        sage: from sage.combinat.knutson_tao_puzzles import H_grassmannian_pieces
        sage: H_grassmannian_pieces()
        Nablas : [0\\0/0, 0\\10/1, 10\\1/0, 1\\0/10, 1\\1/1]
        Deltas : [0/0\\0, 0/1\\10, 1/10\\0, 1/1\\1, 10/0\\1]
    """
def HT_grassmannian_pieces():
    """
    Define the puzzle pieces used in computing the torus-equivariant cohomology of the Grassmannian.

    REFERENCES:

    .. [KT2003] Allen Knutson, Terence Tao, Puzzles and (equivariant) cohomology of Grassmannians,
       Duke Math. J. 119 (2003) 221

    EXAMPLES::

        sage: from sage.combinat.knutson_tao_puzzles import HT_grassmannian_pieces
        sage: HT_grassmannian_pieces()
        Nablas : [0\\0/0, 0\\10/1, 10\\1/0, 1\\0/10, 1\\1/1, 1\\T0|1/0]
        Deltas : [0/0\\0, 0/1\\10, 0/T0|1\\1, 1/10\\0, 1/1\\1, 10/0\\1]
    """
def K_grassmannian_pieces():
    """
    Define the puzzle pieces used in computing the K-theory of the Grassmannian.

    REFERENCES:

    .. [Buch00] \\A. Buch, A Littlewood-Richardson rule for the K-theory of Grassmannians, :arxiv:`math.AG/0004137`

    EXAMPLES::

        sage: from sage.combinat.knutson_tao_puzzles import K_grassmannian_pieces
        sage: K_grassmannian_pieces()
        Nablas : [0\\0/0, 0\\10/1, 0\\K/1, 10\\1/0, 1\\0/10, 1\\0/K, 1\\1/1, K\\1/0]
        Deltas : [0/0\\0, 0/1\\10, 1/10\\0, 1/1\\1, 10/0\\1, K/K\\K]
    """
def H_two_step_pieces():
    """
    Define the puzzle pieces used in two step flags.

    This rule is currently only conjecturally true. See [BuchKreschTamvakis03]_.

    REFERENCES:

    .. [BuchKreschTamvakis03] \\A. Buch, A. Kresch, H. Tamvakis, Gromov-Witten invariants on Grassmannian, :arxiv:`math/0306388`

    EXAMPLES::

        sage: from sage.combinat.knutson_tao_puzzles import H_two_step_pieces
        sage: H_two_step_pieces()
        Nablas : [(21)0\\21/0, 0\\(21)0/21, 0\\0/0, 0\\10/1, 0\\20/2, 10\\1/0, 10\\2(10)/2, 1\\0/10, 1\\1/1, 1\\21/2,
        2(10)\\2/10, 20\\2/0, 21\\0/(21)0, 21\\2/1, 2\\0/20, 2\\1/21, 2\\10/2(10), 2\\2/2]
        Deltas : [(21)0/0\\21, 0/0\\0, 0/1\\10, 0/21\\(21)0, 0/2\\20, 1/10\\0, 1/1\\1, 1/2\\21, 10/0\\1, 10/2\\2(10),
        2(10)/10\\2, 2/2(10)\\10, 2/20\\0, 2/21\\1, 2/2\\2, 20/0\\2, 21/(21)0\\0, 21/1\\2]
    """
def HT_two_step_pieces():
    """
    Define the puzzle pieces used in computing the equivariant two step puzzle pieces.

    For the puzzle pieces, see Figure 26 on page 22 of [CoskunVakil06]_.

    REFERENCES:

    .. [CoskunVakil06] \\I. Coskun, R. Vakil, Geometric positivity in the cohomology of homogeneous spaces
       and generalized Schubert calculus, :arxiv:`math/0610538`

    EXAMPLES::

       sage: from sage.combinat.knutson_tao_puzzles import HT_two_step_pieces
       sage: HT_two_step_pieces()
       Nablas : [(21)0\\21/0, 0\\(21)0/21, 0\\0/0, 0\\10/1, 0\\20/2, 10\\1/0, 10\\2(10)/2,
       1\\0/10, 1\\1/1, 1\\21/2, 1\\T0|1/0, 2(10)\\2/10, 20\\2/0, 21\\0/(21)0, 21\\2/1, 21\\T0|21/0,
       21\\T10|21/10, 2\\0/20, 2\\1/21, 2\\10/2(10), 2\\2/2, 2\\T0|2/0, 2\\T10|2/10, 2\\T1|2/1]
       Deltas : [(21)0/0\\21, 0/0\\0, 0/1\\10, 0/21\\(21)0, 0/2\\20, 0/T0|1\\1, 0/T0|21\\21, 0/T0|2\\2,
       1/10\\0, 1/1\\1, 1/2\\21, 1/T1|2\\2, 10/0\\1, 10/2\\2(10), 10/T10|21\\21, 10/T10|2\\2, 2(10)/10\\2,
       2/2(10)\\10, 2/20\\0, 2/21\\1, 2/2\\2, 20/0\\2, 21/(21)0\\0, 21/1\\2]
    """
def BK_pieces(max_letter):
    """
    The puzzle pieces used in computing the Belkale-Kumar coefficients for any
    partial flag variety in type `A`.

    There are two types of puzzle pieces:

    - a triangle, with each edge labeled with the same letter;
    - a rhombus, with edges labeled `i`, `j`, `i`, `j` in clockwise order with
      `i > j`.

    Each of these is rotated by 60 degrees, but not reflected.

    We model the rhombus pieces as two triangles: a delta piece north-west
    label `i`, north-east label `j` and south label `i(j)`; and a nabla piece
    with south-east label `i`, south-west label `j` and north label `i(j)`.

    INPUT:

    - ``max_letter`` -- positive integer specifying the number of steps in the
      partial flag variety, equivalently, the number of elements in the
      alphabet for the edge labels. The smallest label is `1`.

    REFERENCES:

    .. [KnutsonPurbhoo10] \\A. Knutson, K. Purbhoo, Product and puzzle formulae
       for `GL_n` Belkale-Kumar coefficients, :arxiv:`1008.4979`

    EXAMPLES::

        sage: from sage.combinat.knutson_tao_puzzles import BK_pieces
        sage: BK_pieces(3)
        Nablas : [1\\1/1, 1\\2(1)/2, 1\\3(1)/3, 2(1)\\2/1, 2\\1/2(1), 2\\2/2, 2\\3(2)/3, 3(1)\\3/1, 3(2)\\3/2, 3\\1/3(1), 3\\2/3(2), 3\\3/3]
        Deltas : [1/1\\1, 1/2\\2(1), 1/3\\3(1), 2(1)/1\\2, 2/2(1)\\1, 2/2\\2, 2/3\\3(2), 3(1)/1\\3, 3(2)/2\\3, 3/3(1)\\1, 3/3(2)\\2, 3/3\\3]
    """

class PuzzleFilling:
    """
    Create partial puzzles and provides methods to build puzzles from them.
    """
    def __init__(self, north_west_labels, north_east_labels) -> None:
        """
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzleFilling
            sage: P = PuzzleFilling('0101','0101')
            sage: P
            {}
        """
    def __getitem__(self, key):
        '''
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver
            sage: ps = KnutsonTaoPuzzleSolver("H")
            sage: puzzle = ps(\'0101\',\'1001\')[0]
            sage: puzzle
            {(1, 1): 0/1\\10,
             (1, 2): 1/\\1  10\\/0,
             (1, 3): 0/\\10  1\\/1,
             (1, 4): 1/\\1  10\\/0,
             (2, 2): 0/0\\0,
             (2, 3): 1/\\0  0\\/1,
             (2, 4): 0/\\0  0\\/0,
             (3, 3): 1/1\\1,
             (3, 4): 0/\\0  1\\/10,
             (4, 4): 10/0\\1}
            sage: puzzle[(1,2)]  # indirect doctest
            1/\\1  10\\/0
        '''
    def kink_coordinates(self) -> tuple:
        """
        Provide the coordinates of the kinks.

        The kink coordinates are the coordinates up to which the puzzle has already
        been built. The kink starts in the north corner and then moves down the diagonals
        as the puzzles is built.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzleFilling
            sage: P = PuzzleFilling('0101','0101')
            sage: P
            {}
            sage: P.kink_coordinates()
            (1, 4)
        """
    def is_in_south_edge(self) -> bool:
        """
        Check whether kink coordinates of partial puzzle is in south corner.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzleFilling
            sage: P = PuzzleFilling('0101','0101')
            sage: P.is_in_south_edge()
            False
        """
    def north_west_label_of_kink(self):
        """
        Return north-west label of kink.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzleFilling
            sage: P = PuzzleFilling('0101','0101')
            sage: P.north_west_label_of_kink()
            '1'
        """
    def north_east_label_of_kink(self):
        """
        Return north east label of kink.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzleFilling
            sage: P = PuzzleFilling('0101','0101')
            sage: P.north_east_label_of_kink()
            '0'
        """
    def is_completed(self):
        '''
        Whether partial puzzle is complete (completely filled) or not.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import PuzzleFilling
            sage: P = PuzzleFilling(\'0101\',\'0101\')
            sage: P.is_completed()
            False

            sage: from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver
            sage: ps = KnutsonTaoPuzzleSolver("H")
            sage: puzzle = ps(\'0101\',\'1001\')[0]
            sage: puzzle.is_completed()
            True
        '''
    def south_labels(self):
        '''
        Return south labels for completed puzzle.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver
            sage: ps = KnutsonTaoPuzzleSolver("H")
            sage: ps(\'0101\',\'1001\')[0].south_labels()
            (\'1\', \'0\', \'1\', \'0\')
        '''
    def add_piece(self, piece) -> None:
        """
        Add ``piece`` to partial puzzle.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece, PuzzleFilling
            sage: piece = DeltaPiece('0','1','0')
            sage: P = PuzzleFilling('0101','0101'); P
            {}
            sage: P.add_piece(piece); P
            {(1, 4): 1/0\\0}
        """
    def add_pieces(self, pieces) -> None:
        """
        Add ``piece`` to partial puzzle.

        INPUT:

        - ``pieces`` -- tuple of pieces

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece, PuzzleFilling
            sage: P = PuzzleFilling('0101','0101'); P
            {}
            sage: piece = DeltaPiece('0','1','0')
            sage: pieces = [piece,piece]
            sage: P.add_pieces(pieces)
            sage: P
            {(1, 4): 1/0\\0, (2, 4): 1/0\\0}
        """
    def copy(self):
        """
        Return copy of ``self``.

        EXAMPLES::


            sage: from sage.combinat.knutson_tao_puzzles import DeltaPiece, PuzzleFilling
            sage: piece = DeltaPiece('0','1','0')
            sage: P = PuzzleFilling('0101','0101'); P
            {}
            sage: PP = P.copy()
            sage: P.add_piece(piece); P
            {(1, 4): 1/0\\0}
            sage: PP
            {}
        """
    def contribution(self):
        '''
        Return equivariant contributions from ``self`` in polynomial ring.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver
            sage: ps = KnutsonTaoPuzzleSolver("HT")
            sage: puzzles = ps(\'0101\',\'1001\')
            sage: sorted([p.contribution() for p in puzzles], key=str)
            [1, y1 - y3]
        '''
    def __iter__(self):
        '''
        Iterator.

        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver
            sage: ps = KnutsonTaoPuzzleSolver("H")
            sage: puzzle = ps(\'0101\',\'1001\')[0]
            sage: puzzle
            {(1, 1): 0/1\\10,
             (1, 2): 1/\\1  10\\/0,
             (1, 3): 0/\\10  1\\/1,
             (1, 4): 1/\\1  10\\/0,
             (2, 2): 0/0\\0,
             (2, 3): 1/\\0  0\\/1,
             (2, 4): 0/\\0  0\\/0,
             (3, 3): 1/1\\1,
             (3, 4): 0/\\0  1\\/10,
             (4, 4): 10/0\\1}
            sage: [p for p in puzzle]
            [1/\\1  10\\/0,
            0/\\10  1\\/1,
            0/\\0  0\\/0,
            1/\\1  10\\/0,
            1/\\0  0\\/1,
            0/\\0  1\\/10,
            0/1\\10,
            0/0\\0,
            1/1\\1,
            10/0\\1]
        '''
    def plot(self, labels: bool = True, style: str = 'fill'):
        '''
        Plot completed puzzle.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver
            sage: ps = KnutsonTaoPuzzleSolver("H")
            sage: puzzle = ps(\'0101\',\'1001\')[0]
            sage: puzzle.plot()  #not tested
            sage: puzzle.plot(style=\'fill\')  #not tested
            sage: puzzle.plot(style=\'edges\')  #not tested
        '''

class KnutsonTaoPuzzleSolver(UniqueRepresentation):
    '''
    Return puzzle solver function used to create all puzzles with given boundary conditions.

    This class implements a generic algorithm to solve Knutson-Tao puzzles.
    An instance of this class will be callable: the arguments are the
    labels of north-east and north-west sides of the puzzle boundary; the
    output is the list of the fillings of the puzzle with the specified
    pieces.

    INPUT:

    - ``puzzle_pieces`` -- takes either a collection of puzzle pieces or
      a string indicating a pre-programmed collection of puzzle pieces:

        - ``H`` -- cohomology of the Grassmannian
        - ``HT`` -- equivariant cohomology of the Grassmannian
        - ``K`` -- K-theory
        - ``H2step`` -- cohomology of the *2-step* Grassmannian
        - ``HT2step`` -- equivariant cohomology of the *2-step* Grassmannian
        - ``BK`` -- Belkale-Kumar puzzle pieces

    - ``max_letter`` -- ``None`` or a positive integer(default: ``None``); this
      is only required for Belkale-Kumar puzzles

    EXAMPLES:

    Each puzzle piece is an edge-labelled triangle oriented in such a way
    that it has a south edge (called a *delta* piece) or a north edge
    (called a *nabla* piece). For example, the puzzle pieces corresponding
    to the cohomology of the Grassmannian are the following::

        sage: from sage.combinat.knutson_tao_puzzles import H_grassmannian_pieces
        sage: H_grassmannian_pieces()
        Nablas : [0\\0/0, 0\\10/1, 10\\1/0, 1\\0/10, 1\\1/1]
        Deltas : [0/0\\0, 0/1\\10, 1/10\\0, 1/1\\1, 10/0\\1]

    In the string representation, the nabla pieces are depicted as
    ``c\\a/b``, where `a` is the label of the north edge, `b` is the label
    of the south-east edge, `c` is the label of the south-west edge.
    A similar string representation exists for the delta pieces.

    To create a puzzle solver, one specifies a collection of puzzle pieces::

        sage: KnutsonTaoPuzzleSolver(H_grassmannian_pieces())
        Knutson-Tao puzzle solver with pieces:
        Nablas : [0\\0/0, 0\\10/1, 10\\1/0, 1\\0/10, 1\\1/1]
        Deltas : [0/0\\0, 0/1\\10, 1/10\\0, 1/1\\1, 10/0\\1]

    The following shorthand to create the above puzzle solver is also supported::

        sage: KnutsonTaoPuzzleSolver(\'H\')
        Knutson-Tao puzzle solver with pieces:
        Nablas : [0\\0/0, 0\\10/1, 10\\1/0, 1\\0/10, 1\\1/1]
        Deltas : [0/0\\0, 0/1\\10, 1/10\\0, 1/1\\1, 10/0\\1]

    The solver will compute all fillings of the puzzle with the given
    puzzle pieces. The user specifies the labels of north-east and
    north-west sides of the puzzle boundary and the output is a list of the
    fillings of the puzzle with the specified pieces. For example, there is
    one solution to the puzzle whose north-west and north-east edges are
    both labeled \'0\'::

        sage: ps = KnutsonTaoPuzzleSolver(\'H\')
        sage: ps(\'0\', \'0\')
        [{(1, 1): 0/0\\0}]

    There are two solutions to the puzzle whose north-west and north-east
    edges are both labeled \'0101\'::

        sage: ps = KnutsonTaoPuzzleSolver(\'H\')
        sage: solns = ps(\'0101\', \'0101\')
        sage: len(solns)
        2
        sage: solns.sort(key=str)
        sage: solns
        [{(1, 1): 0/0\\0,
          (1, 2): 1/\\0  0\\/1,
          (1, 3): 0/\\0  0\\/0,
          (1, 4): 1/\\0  0\\/1,
          (2, 2): 1/1\\1,
          (2, 3): 0/\\10  1\\/1,
          (2, 4): 1/\\1  10\\/0,
          (3, 3): 1/1\\1,
          (3, 4): 0/\\0  1\\/10,
          (4, 4): 10/0\\1}, {(1, 1): 0/1\\10,
          (1, 2): 1/\\1  10\\/0,
          (1, 3): 0/\\0  1\\/10,
          (1, 4): 1/\\0  0\\/1,
          (2, 2): 0/0\\0,
          (2, 3): 10/\\1  0\\/0,
          (2, 4): 1/\\1  1\\/1,
          (3, 3): 0/0\\0,
          (3, 4): 1/\\0  0\\/1,
          (4, 4): 1/1\\1}]

    The pieces in a puzzle filling are indexed by pairs of nonnegative
    integers `(i, j)` with `1 \\leq i \\leq j \\leq n`, where `n` is the
    length of the word labelling the triangle edge. The pieces indexed by
    `(i, i)` are the triangles along the south edge of the puzzle. ::

        sage: f = solns[0]
        sage: [f[i, i] for i in range(1,5)]
        [0/0\\0, 1/1\\1, 1/1\\1, 10/0\\1]

    The pieces indexed by `(i, j)` for `j > i` are a pair consisting of
    a delta piece and nabla piece glued together along the south edge and
    north edge, respectively (these pairs are called *rhombi*). ::

        sage: f = solns[0]
        sage: f[1, 2]
        1/\\0  0\\/1

    There are various methods and options to display puzzle solutions.
    A single puzzle can be displayed using the plot method of the puzzle::

        sage: ps = KnutsonTaoPuzzleSolver("H")
        sage: puzzle = ps(\'0101\',\'1001\')[0]
        sage: puzzle.plot()  #not tested
        sage: puzzle.plot(style=\'fill\')  #not tested
        sage: puzzle.plot(style=\'edges\')  #not tested

    To plot several puzzle solutions, use the plot method of the puzzle
    solver::

        sage: ps = KnutsonTaoPuzzleSolver(\'K\')
        sage: solns = ps(\'0101\', \'0101\')
        sage: ps.plot(solns)        # not tested

    The code can also generate a PDF of a puzzle (using LaTeX and *tikz*)::

        sage: latex.extra_preamble(r\'\'\'\\usepackage{tikz}\'\'\')
        sage: ps = KnutsonTaoPuzzleSolver(\'H\')
        sage: solns = ps(\'0101\', \'0101\')
        sage: view(solns[0], viewer=\'pdf\')  # not tested


    Below are examples of using each of the currently supported puzzles.

    Cohomology of the Grassmannian::

        sage: ps = KnutsonTaoPuzzleSolver("H")
        sage: solns = ps(\'0101\', \'0101\')
        sage: sorted(solns, key=str)
        [{(1, 1): 0/0\\0,
          (1, 2): 1/\\0  0\\/1,
          (1, 3): 0/\\0  0\\/0,
          (1, 4): 1/\\0  0\\/1,
          (2, 2): 1/1\\1,
          (2, 3): 0/\\10  1\\/1,
          (2, 4): 1/\\1  10\\/0,
          (3, 3): 1/1\\1,
          (3, 4): 0/\\0  1\\/10,
          (4, 4): 10/0\\1}, {(1, 1): 0/1\\10,
          (1, 2): 1/\\1  10\\/0,
          (1, 3): 0/\\0  1\\/10,
          (1, 4): 1/\\0  0\\/1,
          (2, 2): 0/0\\0,
          (2, 3): 10/\\1  0\\/0,
          (2, 4): 1/\\1  1\\/1,
          (3, 3): 0/0\\0,
          (3, 4): 1/\\0  0\\/1,
          (4, 4): 1/1\\1}]

    Equivariant puzzles::

        sage: ps = KnutsonTaoPuzzleSolver("HT")
        sage: solns = ps(\'0101\', \'0101\')
        sage: sorted(solns, key=str)
        [{(1, 1): 0/0\\0,
          (1, 2): 1/\\0  0\\/1,
          (1, 3): 0/\\0  0\\/0,
          (1, 4): 1/\\0  0\\/1,
          (2, 2): 1/1\\1,
          (2, 3): 0/\\1  1\\/0,
          (2, 4): 1/\\1  1\\/1,
          (3, 3): 0/0\\0,
          (3, 4): 1/\\0  0\\/1,
          (4, 4): 1/1\\1}, {(1, 1): 0/0\\0,
          (1, 2): 1/\\0  0\\/1,
          (1, 3): 0/\\0  0\\/0,
          (1, 4): 1/\\0  0\\/1,
          (2, 2): 1/1\\1,
          (2, 3): 0/\\10  1\\/1,
          (2, 4): 1/\\1  10\\/0,
          (3, 3): 1/1\\1,
          (3, 4): 0/\\0  1\\/10,
          (4, 4): 10/0\\1}, {(1, 1): 0/1\\10,
          (1, 2): 1/\\1  10\\/0,
          (1, 3): 0/\\0  1\\/10,
          (1, 4): 1/\\0  0\\/1,
          (2, 2): 0/0\\0,
          (2, 3): 10/\\1  0\\/0,
          (2, 4): 1/\\1  1\\/1,
          (3, 3): 0/0\\0,
          (3, 4): 1/\\0  0\\/1,
          (4, 4): 1/1\\1}]

    K-Theory puzzles::

        sage: ps = KnutsonTaoPuzzleSolver("K")
        sage: solns = ps(\'0101\', \'0101\')
        sage: sorted(solns, key=str)
        [{(1, 1): 0/0\\0,
          (1, 2): 1/\\0  0\\/1,
          (1, 3): 0/\\0  0\\/0,
          (1, 4): 1/\\0  0\\/1,
          (2, 2): 1/1\\1,
          (2, 3): 0/\\10  1\\/1,
          (2, 4): 1/\\1  10\\/0,
          (3, 3): 1/1\\1,
          (3, 4): 0/\\0  1\\/10,
          (4, 4): 10/0\\1}, {(1, 1): 0/1\\10,
          (1, 2): 1/\\1  10\\/0,
          (1, 3): 0/\\0  1\\/10,
          (1, 4): 1/\\0  0\\/1,
          (2, 2): 0/0\\0,
          (2, 3): 10/\\1  0\\/0,
          (2, 4): 1/\\1  1\\/1,
          (3, 3): 0/0\\0,
          (3, 4): 1/\\0  0\\/1,
          (4, 4): 1/1\\1}, {(1, 1): 0/1\\10,
          (1, 2): 1/\\1  10\\/0,
          (1, 3): 0/\\0  1\\/K,
          (1, 4): 1/\\0  0\\/1,
          (2, 2): 0/0\\0,
          (2, 3): K/\\K  0\\/1,
          (2, 4): 1/\\1  K\\/0,
          (3, 3): 1/1\\1,
          (3, 4): 0/\\0  1\\/10,
          (4, 4): 10/0\\1}]

    Two-step puzzles::

        sage: ps = KnutsonTaoPuzzleSolver("H2step")
        sage: solns = ps(\'01201\', \'01021\')
        sage: sorted(solns, key=str)
        [{(1, 1): 0/0\\0,
          (1, 2): 1/\\0  0\\/1,
          (1, 3): 2/\\0  0\\/2,
          (1, 4): 0/\\0  0\\/0,
          (1, 5): 1/\\0  0\\/1,
          (2, 2): 1/2\\21,
          (2, 3): 2/\\2  21\\/1,
          (2, 4): 0/\\10  2\\/21,
          (2, 5): 1/\\1  10\\/0,
          (3, 3): 1/1\\1,
          (3, 4): 21/\\2  1\\/1,
          (3, 5): 0/\\0  2\\/20,
          (4, 4): 1/1\\1,
          (4, 5): 20/\\2  1\\/10,
          (5, 5): 10/0\\1}, {(1, 1): 0/1\\10,
          (1, 2): 1/\\1  10\\/0,
          (1, 3): 2/\\1  1\\/2,
          (1, 4): 0/\\0  1\\/10,
          (1, 5): 1/\\0  0\\/1,
          (2, 2): 0/2\\20,
          (2, 3): 2/\\2  20\\/0,
          (2, 4): 10/\\1  2\\/20,
          (2, 5): 1/\\1  1\\/1,
          (3, 3): 0/0\\0,
          (3, 4): 20/\\2  0\\/0,
          (3, 5): 1/\\0  2\\/2(10),
          (4, 4): 0/0\\0,
          (4, 5): 2(10)/\\2  0\\/1,
          (5, 5): 1/1\\1}, {(1, 1): 0/2\\20,
          (1, 2): 1/\\21  20\\/0,
          (1, 3): 2/\\2  21\\/1,
          (1, 4): 0/\\0  2\\/20,
          (1, 5): 1/\\0  0\\/1,
          (2, 2): 0/0\\0,
          (2, 3): 1/\\0  0\\/1,
          (2, 4): 20/\\2  0\\/0,
          (2, 5): 1/\\1  2\\/21,
          (3, 3): 1/1\\1,
          (3, 4): 0/\\0  1\\/10,
          (3, 5): 21/\\0  0\\/21,
          (4, 4): 10/0\\1,
          (4, 5): 21/\\2  1\\/1,
          (5, 5): 1/1\\1}]

    Two-step equivariant puzzles::

        sage: ps = KnutsonTaoPuzzleSolver("HT2step")
        sage: solns = ps(\'10212\', \'12012\')
        sage: sorted(solns, key=str)
        [{(1, 1): 1/1\\1,
          (1, 2): 0/\\(21)0  1\\/2,
          (1, 3): 2/\\1  (21)0\\/0,
          (1, 4): 1/\\1  1\\/1,
          (1, 5): 2/\\1  1\\/2,
          (2, 2): 2/2\\2,
          (2, 3): 0/\\2  2\\/0,
          (2, 4): 1/\\2  2\\/1,
          (2, 5): 2/\\2  2\\/2,
          (3, 3): 0/0\\0,
          (3, 4): 1/\\0  0\\/1,
          (3, 5): 2/\\0  0\\/2,
          (4, 4): 1/1\\1,
          (4, 5): 2/\\1  1\\/2,
          (5, 5): 2/2\\2}, {(1, 1): 1/1\\1,
          (1, 2): 0/\\(21)0  1\\/2,
          (1, 3): 2/\\1  (21)0\\/0,
          (1, 4): 1/\\1  1\\/1,
          (1, 5): 2/\\1  1\\/2,
          (2, 2): 2/2\\2,
          (2, 3): 0/\\2  2\\/0,
          (2, 4): 1/\\21  2\\/2,
          (2, 5): 2/\\2  21\\/1,
          (3, 3): 0/0\\0,
          (3, 4): 2/\\0  0\\/2,
          (3, 5): 1/\\0  0\\/1,
          (4, 4): 2/2\\2,
          (4, 5): 1/\\1  2\\/21,
          (5, 5): 21/1\\2}, {(1, 1): 1/1\\1,
          (1, 2): 0/\\(21)0  1\\/2,
          (1, 3): 2/\\1  (21)0\\/0,
          (1, 4): 1/\\1  1\\/1,
          (1, 5): 2/\\1  1\\/2,
          (2, 2): 2/2\\2,
          (2, 3): 0/\\20  2\\/2,
          (2, 4): 1/\\21  20\\/0,
          (2, 5): 2/\\2  21\\/1,
          (3, 3): 2/2\\2,
          (3, 4): 0/\\0  2\\/20,
          (3, 5): 1/\\0  0\\/1,
          (4, 4): 20/0\\2,
          (4, 5): 1/\\1  2\\/21,
          (5, 5): 21/1\\2}, {(1, 1): 1/1\\1,
          (1, 2): 0/\\1  1\\/0,
          (1, 3): 2/\\1  1\\/2,
          (1, 4): 1/\\1  1\\/1,
          (1, 5): 2/\\1  1\\/2,
          (2, 2): 0/2\\20,
          (2, 3): 2/\\2  20\\/0,
          (2, 4): 1/\\2  2\\/1,
          (2, 5): 2/\\2  2\\/2,
          (3, 3): 0/0\\0,
          (3, 4): 1/\\0  0\\/1,
          (3, 5): 2/\\0  0\\/2,
          (4, 4): 1/1\\1,
          (4, 5): 2/\\1  1\\/2,
          (5, 5): 2/2\\2}, {(1, 1): 1/1\\1,
          (1, 2): 0/\\1  1\\/0,
          (1, 3): 2/\\1  1\\/2,
          (1, 4): 1/\\1  1\\/1,
          (1, 5): 2/\\1  1\\/2,
          (2, 2): 0/2\\20,
          (2, 3): 2/\\2  20\\/0,
          (2, 4): 1/\\21  2\\/2,
          (2, 5): 2/\\2  21\\/1,
          (3, 3): 0/0\\0,
          (3, 4): 2/\\0  0\\/2,
          (3, 5): 1/\\0  0\\/1,
          (4, 4): 2/2\\2,
          (4, 5): 1/\\1  2\\/21,
          (5, 5): 21/1\\2}, {(1, 1): 1/1\\1,
          (1, 2): 0/\\10  1\\/1,
          (1, 3): 2/\\10  10\\/2,
          (1, 4): 1/\\1  10\\/0,
          (1, 5): 2/\\1  1\\/2,
          (2, 2): 1/2\\21,
          (2, 3): 2/\\2  21\\/1,
          (2, 4): 0/\\2  2\\/0,
          (2, 5): 2/\\2  2\\/2,
          (3, 3): 1/1\\1,
          (3, 4): 0/\\0  1\\/10,
          (3, 5): 2/\\0  0\\/2,
          (4, 4): 10/0\\1,
          (4, 5): 2/\\1  1\\/2,
          (5, 5): 2/2\\2}, {(1, 1): 1/1\\1,
          (1, 2): 0/\\10  1\\/1,
          (1, 3): 2/\\10  10\\/2,
          (1, 4): 1/\\1  10\\/0,
          (1, 5): 2/\\1  1\\/2,
          (2, 2): 1/2\\21,
          (2, 3): 2/\\2  21\\/1,
          (2, 4): 0/\\20  2\\/2,
          (2, 5): 2/\\2  20\\/0,
          (3, 3): 1/1\\1,
          (3, 4): 2/\\1  1\\/2,
          (3, 5): 0/\\0  1\\/10,
          (4, 4): 2/2\\2,
          (4, 5): 10/\\1  2\\/20,
          (5, 5): 20/0\\2}, {(1, 1): 1/2\\21,
          (1, 2): 0/\\20  21\\/1,
          (1, 3): 2/\\2  20\\/0,
          (1, 4): 1/\\1  2\\/21,
          (1, 5): 2/\\1  1\\/2,
          (2, 2): 1/1\\1,
          (2, 3): 0/\\1  1\\/0,
          (2, 4): 21/\\2  1\\/1,
          (2, 5): 2/\\2  2\\/2,
          (3, 3): 0/0\\0,
          (3, 4): 1/\\0  0\\/1,
          (3, 5): 2/\\0  0\\/2,
          (4, 4): 1/1\\1,
          (4, 5): 2/\\1  1\\/2,
          (5, 5): 2/2\\2}, {(1, 1): 1/2\\21,
          (1, 2): 0/\\20  21\\/1,
          (1, 3): 2/\\2  20\\/0,
          (1, 4): 1/\\1  2\\/21,
          (1, 5): 2/\\1  1\\/2,
          (2, 2): 1/1\\1,
          (2, 3): 0/\\10  1\\/1,
          (2, 4): 21/\\2  10\\/0,
          (2, 5): 2/\\2  2\\/2,
          (3, 3): 1/1\\1,
          (3, 4): 0/\\0  1\\/10,
          (3, 5): 2/\\0  0\\/2,
          (4, 4): 10/0\\1,
          (4, 5): 2/\\1  1\\/2,
          (5, 5): 2/2\\2}, {(1, 1): 1/2\\21,
          (1, 2): 0/\\21  21\\/0,
          (1, 3): 2/\\2  21\\/1,
          (1, 4): 1/\\1  2\\/21,
          (1, 5): 2/\\1  1\\/2,
          (2, 2): 0/1\\10,
          (2, 3): 1/\\1  10\\/0,
          (2, 4): 21/\\2  1\\/1,
          (2, 5): 2/\\2  2\\/2,
          (3, 3): 0/0\\0,
          (3, 4): 1/\\0  0\\/1,
          (3, 5): 2/\\0  0\\/2,
          (4, 4): 1/1\\1,
          (4, 5): 2/\\1  1\\/2,
          (5, 5): 2/2\\2}]


    Belkale-Kumar puzzles (the following example is Figure 2 of [KnutsonPurbhoo10]_)::

        sage: ps = KnutsonTaoPuzzleSolver(\'BK\', 3)
        sage: solns = ps(\'12132\', \'23112\')
        sage: len(solns)
        1
        sage: solns[0].south_labels()
        (\'3\', \'2\', \'1\', \'2\', \'1\')
        sage: solns
        [{(1, 1): 1/3\\3(1),
          (1, 2): 2/\\3(2)  3(1)\\/1,
          (1, 3): 1/\\3(1)  3(2)\\/2,
          (1, 4): 3/\\3  3(1)\\/1,
          (1, 5): 2/\\2  3\\/3(2),
          (2, 2): 1/2\\2(1),
          (2, 3): 2/\\2  2(1)\\/1,
          (2, 4): 1/\\2(1)  2\\/2,
          (2, 5): 3(2)/\\3  2(1)\\/1,
          (3, 3): 1/1\\1,
          (3, 4): 2/\\1  1\\/2,
          (3, 5): 1/\\1  1\\/1,
          (4, 4): 2/2\\2,
          (4, 5): 1/\\1  2\\/2(1),
          (5, 5): 2(1)/1\\2}]
    '''
    def __init__(self, puzzle_pieces) -> None:
        '''
        Knutson-Tao puzzle solver.

        TESTS:

        Check that UniqueRepresentation works::

            sage: from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver, H_grassmannian_pieces
            sage: ps = KnutsonTaoPuzzleSolver(H_grassmannian_pieces())
            sage: qs = KnutsonTaoPuzzleSolver("H")
            sage: ps
            Knutson-Tao puzzle solver with pieces:
            Nablas : [0\\0/0, 0\\10/1, 10\\1/0, 1\\0/10, 1\\1/1]
            Deltas : [0/0\\0, 0/1\\10, 1/10\\0, 1/1\\1, 10/0\\1]
            sage: qs
            Knutson-Tao puzzle solver with pieces:
            Nablas : [0\\0/0, 0\\10/1, 10\\1/0, 1\\0/10, 1\\1/1]
            Deltas : [0/0\\0, 0/1\\10, 1/10\\0, 1/1\\1, 10/0\\1]
            sage: ps == qs
            True
        '''
    @staticmethod
    def __classcall_private__(cls, puzzle_pieces, max_letter=None):
        '''
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import *
            sage: KnutsonTaoPuzzleSolver(H_grassmannian_pieces()) == KnutsonTaoPuzzleSolver("H") # indirect doctest
            True
            sage: KnutsonTaoPuzzleSolver(HT_grassmannian_pieces()) == KnutsonTaoPuzzleSolver("HT")
            True
            sage: KnutsonTaoPuzzleSolver(K_grassmannian_pieces()) == KnutsonTaoPuzzleSolver("K")
            True
            sage: KnutsonTaoPuzzleSolver(H_two_step_pieces()) == KnutsonTaoPuzzleSolver("H2step")
            True
            sage: KnutsonTaoPuzzleSolver(HT_two_step_pieces()) == KnutsonTaoPuzzleSolver("HT2step")
            True
            sage: KnutsonTaoPuzzleSolver(BK_pieces(3)) == KnutsonTaoPuzzleSolver("BK",3)
            True
        '''
    def __call__(self, lamda, mu, algorithm: str = 'strips'):
        '''
        TESTS::

            sage: from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver
            sage: ps = KnutsonTaoPuzzleSolver("H")
            sage: ps(\'0101\',\'1001\')
            [{(1, 1): 0/1\\10,
              (1, 2): 1/\\1  10\\/0,
              (1, 3): 0/\\10  1\\/1,
              (1, 4): 1/\\1  10\\/0,
              (2, 2): 0/0\\0,
              (2, 3): 1/\\0  0\\/1,
              (2, 4): 0/\\0  0\\/0,
              (3, 3): 1/1\\1,
              (3, 4): 0/\\0  1\\/10,
              (4, 4): 10/0\\1}]
            sage: ps(\'0101\',\'1001\',algorithm=\'pieces\')
            [{(1, 1): 0/1\\10,
              (1, 2): 1/\\1  10\\/0,
              (1, 3): 0/\\10  1\\/1,
              (1, 4): 1/\\1  10\\/0,
              (2, 2): 0/0\\0,
              (2, 3): 1/\\0  0\\/1,
              (2, 4): 0/\\0  0\\/0,
              (3, 3): 1/1\\1,
              (3, 4): 0/\\0  1\\/10,
              (4, 4): 10/0\\1}]
        '''
    solutions = __call__
    def puzzle_pieces(self):
        """
        The puzzle pieces used for filling in the puzzles.

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver
            sage: ps = KnutsonTaoPuzzleSolver('H')
            sage: ps.puzzle_pieces()
            Nablas : [0\\0/0, 0\\10/1, 10\\1/0, 1\\0/10, 1\\1/1]
            Deltas : [0/0\\0, 0/1\\10, 1/10\\0, 1/1\\1, 10/0\\1]
        """
    def plot(self, puzzles):
        """
        Return plot of puzzles.

        INPUT:

        - ``puzzles`` -- list of puzzles

        EXAMPLES::

            sage: from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver
            sage: ps = KnutsonTaoPuzzleSolver('K')
            sage: solns = ps('0101', '0101')
            sage: ps.plot(solns)        # not tested
        """
    def structure_constants(self, lamda, mu, nu=None):
        """
        Compute cohomology structure coefficients from puzzles.

        INPUT:

        - ``pieces`` -- puzzle pieces to be used
        - ``lambda``, ``mu`` -- edge labels of puzzle for northwest and north east side
        - ``nu`` -- (default: ``None``) if ``nu`` is not specified a dictionary is returned with
          the structure coefficients corresponding to all south labels; if ``nu`` is given, only
          the coefficients with the specified label is returned

        OUTPUT: dictionary

        EXAMPLES:

        Note: In order to standardize the output of the following examples,
        we output a sorted list of items from the dictionary instead of the
        dictionary itself.

        Grassmannian cohomology::

            sage: ps = KnutsonTaoPuzzleSolver('H')
            sage: cp = ps.structure_constants('0101', '0101')
            sage: sorted(cp.items(), key=str)
            [(('0', '1', '1', '0'), 1), (('1', '0', '0', '1'), 1)]
            sage: ps.structure_constants('001001', '001010', '010100')
            1

        Equivariant cohomology::

            sage: ps = KnutsonTaoPuzzleSolver('HT')
            sage: cp = ps.structure_constants('0101', '0101')
            sage: sorted(cp.items(), key=str)
            [(('0', '1', '0', '1'), y2 - y3),
            (('0', '1', '1', '0'), 1),
            (('1', '0', '0', '1'), 1)]

        K-theory::

            sage: ps = KnutsonTaoPuzzleSolver('K')
            sage: cp = ps.structure_constants('0101', '0101')
            sage: sorted(cp.items(), key=str)
            [(('0', '1', '1', '0'), 1), (('1', '0', '0', '1'), 1), (('1', '0', '1', '0'), -1)]

        Two-step::

            sage: ps = KnutsonTaoPuzzleSolver('H2step')
            sage: cp = ps.structure_constants('01122', '01122')
            sage: sorted(cp.items(), key=str)
            [(('0', '1', '1', '2', '2'), 1)]
            sage: cp = ps.structure_constants('01201', '01021')
            sage: sorted(cp.items(), key=str)
            [(('0', '2', '1', '1', '0'), 1),
             (('1', '2', '0', '0', '1'), 1),
             (('2', '0', '1', '0', '1'), 1)]

        Two-step equivariant::

            sage: ps = KnutsonTaoPuzzleSolver('HT2step')
            sage: cp = ps.structure_constants('10212', '12012')
            sage: sorted(cp.items(), key=str)
            [(('1', '2', '0', '1', '2'), y1*y2 - y2*y3 - y1*y4 + y3*y4),
             (('1', '2', '0', '2', '1'), y1 - y3),
             (('1', '2', '1', '0', '2'), y2 - y4),
             (('1', '2', '1', '2', '0'), 1),
             (('1', '2', '2', '0', '1'), 1),
             (('2', '1', '0', '1', '2'), y1 - y3),
             (('2', '1', '1', '0', '2'), 1)]
        """
