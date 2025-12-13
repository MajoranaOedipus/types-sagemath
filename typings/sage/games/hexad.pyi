from _typeshed import Incomplete
from sage.calculus.calculus import SR as SR
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.infinity import infinity as infinity

def view_list(L):
    """
    This provides a printout of the lines, crosses and squares
    of the MINIMOG, as in Curtis' paper [Cu1984]_.

    EXAMPLES::

        sage: from sage.games.hexad import *
        sage: M = Minimog(type='shuffle')
        sage: view_list(M.line[1])
        <BLANKLINE>
        [0 0 0]
        [1 1 1]
        [0 0 0]
        sage: view_list(M.cross[1])
        <BLANKLINE>
        [1 1 1]
        [0 0 1]
        [0 0 1]
        sage: view_list(M.square[1])
        <BLANKLINE>
        [0 0 0]
        [1 1 0]
        [1 1 0]
    """
def picture_set(A, L) -> set:
    """
    This is needed in the :meth:`Minimog.find_hexad` function below.

    EXAMPLES::

        sage: from sage.games.hexad import *
        sage: M = Minimog(type='shuffle')
        sage: picture_set(M.picture00, M.cross[2])
        {5, 7, 8, 9, 10}
        sage: picture_set(M.picture02, M.square[7])
        {2, 3, 5, 8}
    """

class Minimog:
    '''
    This implements the Conway/Curtis minimog idea for describing
    the Steiner triple system `S(5, 6, 12)`.

    EXAMPLES::

        sage: from sage.games.hexad import *
        sage: Minimog(type=\'shuffle\')
        Minimog of type shuffle
        sage: M = Minimog(type = "modulo11")
        sage: M.minimog
        [        0         3 +Infinity         2]
        [        5         9         8        10]
        [        4         1         6         7]
    '''
    type: Incomplete
    minimog: Incomplete
    picture00: Incomplete
    picture02: Incomplete
    picture21: Incomplete
    line: Incomplete
    cross: Incomplete
    box: Incomplete
    square: Incomplete
    col: Incomplete
    tet: Incomplete
    def __init__(self, type: str = 'shuffle') -> None: ...
    def print_kitten(self) -> None:
        '''
        This simply prints the "kitten" (expressed as a triangular diagram
        of symbols).

        EXAMPLES::

            sage: from sage.games.hexad import *
            sage: M = Minimog("shuffle")
            sage: M.print_kitten()
                     0
            <BLANKLINE>
                     8
                   9  10
                  5  11  3
                 8  2  4  8
               9  10  7  9  10
            <BLANKLINE>
            6                   1
            sage: M = Minimog("modulo11")
            sage: M.print_kitten()
                     +Infinity
            <BLANKLINE>
                     6
                   2  10
                  5  7  3
                 6  9  4  6
               2  10  8  2  10
            <BLANKLINE>
            0                   1
        '''
    def find_hexad0(self, pts):
        '''
        Find a hexad of type 0.

        INPUT:

        - ``pts`` -- set of 2 distinct elements of MINIMOG, but not
          including the "points at infinity"

        OUTPUT:

        hexad containing ``pts`` and of type 0 (the 3 points "at
        infinity" union a line)

        .. NOTE::

            The 3 points "at infinity" are
            ``{MINIMOG[0][2], MINIMOG[2][1], MINIMOG[0][0]}``.

        EXAMPLES::

            sage: from sage.games.hexad import *
            sage: M = Minimog(type=\'shuffle\')
            sage: M.find_hexad0(set([2, 4]))
            ([0, 1, 2, 4, 6, 8], [\'line 1\', \'picture 1\'])
        '''
    def find_hexad1(self, pts):
        '''
        Find a hexad of type 1.

        INPUT:

        - ``pts`` -- set of 5 distinct elements of MINIMOG

        OUTPUT:

        hexad containing ``pts`` and of type 1 (union of 2 parallel
        lines -- *no* points "at infinity")

        .. NOTE::

            The 3 points "at infinity" are
            ``{MINIMOG[0][2], MINIMOG[2][1], MINIMOG[0][0]}``.

        EXAMPLES::

            sage: from sage.games.hexad import *
            sage: M = Minimog(type=\'shuffle\')
            sage: M.find_hexad1(set([2, 3, 4, 5, 8]))
            ([2, 3, 4, 5, 8, 11], [\'lines (1, 2)\', \'picture 1\'])
        '''
    def find_hexad2(self, pts, x0):
        '''
        Find a hexad of type 2.

        INPUT:

        - ``pts`` -- list S of 4 elements of MINIMOG, not including
          any "points at infinity"
        - ``x0`` -- in ``{MINIMOG[0][2], MINIMOG[2][1], MINIMOG[0][0]}``

        OUTPUT: hexad containing `S \\cup \\{x0\\}` of type 2

        EXAMPLES::

            sage: from sage.games.hexad import *
            sage: M = Minimog(type=\'shuffle\')
            sage: M.find_hexad2([2, 3, 4, 5], 1)
            ([], [])

        The above output indicates that there is no hexad of type 2
        containing `\\{2, 3, 4, 5\\}`. However, there is one containing
        `\\{2, 3, 4, 8\\}`::

            sage: M.find_hexad2([2, 3, 4, 8], 0)
            ([0, 2, 3, 4, 8, 9], [\'cross 12\', \'picture 0\'])
        '''
    def find_hexad3(self, pts, x0, x1):
        '''
        Find a hexad of type 3.

        INPUT:

        - ``pts`` -- list of 3 elements of MINIMOG, not including any
          "points at infinity"
        - ``x0``, ``x1`` -- in ``{MINIMOG[0][2], MINIMOG[2][1],
          MINIMOG[0][0]}``

        OUTPUT:

        hexad containing pts union \\{x0, x1\\} of type 3 (square at
        picture of "omitted point at infinity")

        EXAMPLES::

            sage: from sage.games.hexad import *
            sage: M = Minimog(type=\'shuffle\')
            sage: M.find_hexad3([2, 3, 4], 0, 1)
            ([0, 1, 2, 3, 4, 11], [\'square 2\', \'picture 6\'])
        '''
    def find_hexad(self, pts):
        '''
        Find a hexad of some type.

        INPUT:

        - ``pts`` -- list S of 5 elements of MINIMOG

        OUTPUT: hexad containing `S \\cup \\{x0\\}` of some type

        .. NOTE::

            The 3 "points at infinity" are
            ``{MINIMOG[0][2], MINIMOG[2][1], MINIMOG[0][0]}``.

        Theorem ([Cu1984]_,  [Co1984]_): Each hexads is of exactly one
        of the following types:

        0. {3 "points at infinity"} union {any line},
        1. the union of any two (distinct) parallel lines in the same
           picture,
        2. one "point at infinity" union a cross in the corresponding
           picture, or
        3. two "points at infinity" union a square in the picture
           corresponding to the omitted point at infinity.

        More precisely, there are 132 such hexads (12 of type 0,
        12 of type 1, 54 of type 2, and 54 of type 3).
        They form a Steiner system of type `(5, 6, 12)`.

        EXAMPLES::

            sage: from sage.games.hexad import *
            sage: M = Minimog(type=\'shuffle\')
            sage: M.find_hexad([0, 1, 2, 3, 4])
            ([0, 1, 2, 3, 4, 11], [\'square 2\', \'picture 6\'])
            sage: M.find_hexad([1, 2, 3, 4, 5])
            ([1, 2, 3, 4, 5, 6], [\'square 8\', \'picture 0\'])
            sage: M.find_hexad([2, 3, 4, 5, 8])
            ([2, 3, 4, 5, 8, 11], [\'lines (1, 2)\', \'picture 1\'])
            sage: M.find_hexad([0, 1, 2, 4, 6])
            ([0, 1, 2, 4, 6, 8], [\'line 1\', \'picture 1\'])
            sage: M = Minimog(type=\'modulo11\')
            sage: M.find_hexad([1, 2, 3, 4, SR(infinity)]) # random (machine dependent?) order
            ([+Infinity, 2, 3, 4, 1, 10], [\'square 8\', \'picture 0\'])

        AUTHOR:

        David Joyner (2006-05)

        REFERENCES: [Cu1984]_,  [Co1984]_
        '''
    def blackjack_move(self, L0):
        '''
        Perform a blackjack move.

        INPUT:

        - ``L0`` -- list of cards of length 6, taken
          from `\\{0, 1, ..., 11\\}`

        .. RUBRIC:: MATHEMATICAL BLACKJACK

        Mathematical blackjack is played with 12 cards, labeled `0, ..., 11`
        (for example:  king,  ace, `2`, `3`, ..., `10`, jack, where the
        king is `0` and the  jack is `11`). Divide the 12 cards into two
        piles of `6` (to be fair, this should be done randomly). Each of
        the `6` cards of one of these piles are to be placed face up on
        the table. The remaining cards are in a stack which is shared
        and visible to both players. If the sum of the cards face up on
        the table is less than 21 then no legal move is possible so you
        must shuffle the cards and deal a new game. (Conway calls such
        a game `*={0|0}`, where `0={|}`; in this game the first player
        automatically wins.)

        * Players alternate moves.
        * A move consists of exchanging a card on the table with a
          lower card from the other pile.
        * The player whose move makes the sum of the cards on the table
          under 21 loses.

        The winning strategy (given below) for this game is due to
        Conway and Ryba. There is a Steiner system `S(5, 6, 12)` of hexads
        in the set `\\{0, 1, ..., 11\\}`. This Steiner system is associated
        to the MINIMOG of in the "shuffle numbering" rather than the
        "modulo `11` labeling".

        **Proposition** ([KR2001]_) For this Steiner system, the
        winning strategy is to choose a move which is a hexad from
        this system.

        EXAMPLES::

            sage: M = Minimog(type=\'modulo11\')
            sage: M.blackjack_move([0, 2, 3, 6, 1, 10])
            \'6 --> 5. The total went from 22 to 21.\'
            sage: M = Minimog(type=\'shuffle\')
            sage: M.blackjack_move([0, 2, 4, 6, 7, 11])
            \'4 --> 3. The total went from 30 to 29.\'

        Is this really a hexad? ::

            sage: M.find_hexad([11, 2, 3, 6, 7])
            ([0, 2, 3, 6, 7, 11], [\'square 9\', \'picture 1\'])

        So, yes it is, but here is further confirmation::

            sage: M.blackjack_move([0, 2, 3, 6, 7, 11])
            This is a hexad.
            There is no winning move, so make a random legal move.
            [0, 2, 3, 6, 7, 11]

        Now, suppose player 2 replaced the 11 by a 9. Your next move::

            sage: M.blackjack_move([0, 2, 3, 6, 7, 9])
            \'7 --> 1. The total went from 27 to 21.\'

        You have now won. Sage will even tell you so::

            sage: M.blackjack_move([0, 2, 3, 6, 1, 9])
            \'No move possible. Shuffle the deck and redeal.\'

        AUTHOR:

        David Joyner (2006-05)

        REFERENCES: [CS1986]_, [KR2001]_
        '''
