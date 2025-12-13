from .parser import Parser as Parser
from _typeshed import Incomplete
from collections.abc import MutableMapping
from sage.combinat.subset import powerset as powerset
from sage.cpython.string import bytes_to_str as bytes_to_str
from sage.matrix.constructor import matrix as matrix, vector as vector
from sage.misc.latex import latex as latex
from sage.misc.temporary_file import tmp_filename as tmp_filename
from sage.numerical.mip import MixedIntegerLinearProgram as MixedIntegerLinearProgram
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

class NormalFormGame(SageObject, MutableMapping):
    """
    An object representing a Normal Form Game. Primarily used to compute the
    Nash Equilibria.

    INPUT:

    - ``generator`` -- can be a list of 2 matrices, a single matrix or left
      blank
    """
    players: Incomplete
    utilities: Incomplete
    def __init__(self, generator=None) -> None:
        """
        Initialize a Normal Form game and checks the inputs.

        EXAMPLES:

        Can have games with more than 2 players::

            sage: threegame = NormalFormGame()
            sage: threegame.add_player(2)  # Adding first player with 2 strategies
            sage: threegame.add_player(2)  # Adding second player with 2 strategies
            sage: threegame.add_player(2)  # Adding third player with 2 strategies
            sage: threegame[0, 0, 0][0] = 3
            sage: threegame[0, 0, 0][1] = 1
            sage: threegame[0, 0, 0][2] = 4
            sage: threegame[0, 0, 1][0] = 1
            sage: threegame[0, 0, 1][1] = 5
            sage: threegame[0, 0, 1][2] = 9
            sage: threegame[0, 1, 0][0] = 2
            sage: threegame[0, 1, 0][1] = 6
            sage: threegame[0, 1, 0][2] = 5
            sage: threegame[0, 1, 1][0] = 3
            sage: threegame[0, 1, 1][1] = 5
            sage: threegame[0, 1, 1][2] = 8
            sage: threegame[1, 0, 0][0] = 9
            sage: threegame[1, 0, 0][1] = 7
            sage: threegame[1, 0, 0][2] = 9
            sage: threegame[1, 0, 1][0] = 3
            sage: threegame[1, 0, 1][1] = 2
            sage: threegame[1, 0, 1][2] = 3
            sage: threegame[1, 1, 0][0] = 8
            sage: threegame[1, 1, 0][1] = 4
            sage: threegame[1, 1, 0][2] = 6
            sage: threegame[1, 1, 1][0] = 2
            sage: threegame[1, 1, 1][1] = 6
            sage: threegame[1, 1, 1][2] = 4
            sage: threegame.obtain_nash()
            Traceback (most recent call last):
            ...
            NotImplementedError: Nash equilibrium for games with more than
             2 players have not been implemented yet. Please see the gambit
             website (http://gambit.sourceforge.net/) that has a variety of
             available algorithms

        Can initialise a game from a gambit game object::

            sage: # optional - gambit
            sage: from gambit import Game
            sage: gambitgame= Game.new_table([2, 2])
            sage: gambitgame[int(0), int(0)][int(0)] = int(5)
            sage: gambitgame[int(0), int(0)][int(1)] = int(8)
            sage: gambitgame[int(0), int(1)][int(0)] = int(2)
            sage: gambitgame[int(0), int(1)][int(1)] = int(11)
            sage: gambitgame[int(1), int(0)][int(0)] = int(10)
            sage: gambitgame[int(1), int(0)][int(1)] = int(7)
            sage: gambitgame[int(1), int(1)][int(0)] = int(5)
            sage: gambitgame[int(1), int(1)][int(1)] = int(5)
            sage: g = NormalFormGame(gambitgame); g
            Normal Form Game with the following utilities: {(0, 0): [5.0, 8.0],
             (0, 1): [2.0, 11.0],
             (1, 0): [10.0, 7.0],
             (1, 1): [5.0, 5.0]}

        TESTS:

        Raise error if matrices aren't the same size::

            sage: p1 = matrix([[1, 2], [3, 4]])
            sage: p2 = matrix([[3, 3], [1, 4], [6, 6]])
            sage: error = NormalFormGame([p1, p2])
            Traceback (most recent call last):
            ...
            ValueError: matrices must be the same size

        Note that when initializing, a single argument must be passed::

            sage: p1 = matrix([[1, 2], [3, 4]])
            sage: p2 = matrix([[3, 3], [1, 4], [6, 6]])
            sage: error = NormalFormGame(p1, p2)
            Traceback (most recent call last):
            ...
            TypeError: ...__init__() takes from 1 to 2 positional arguments but 3 were given

        When initiating, argument passed must be a list or nothing::

            sage: error = NormalFormGame({4:6, 6:9})
            Traceback (most recent call last):
            ...
            TypeError: Generator function must be a list, gambit game or nothing

        When passing nothing, the utilities then need to be entered manually::

            sage: game = NormalFormGame()
            sage: game
            Normal Form Game with the following utilities: {}
        """
    def __delitem__(self, key) -> None:
        """
        This method is one of a collection that aims to make a game
        instance behave like a dictionary which can be used if a game
        is to be generated without using a matrix.

        Here we set up deleting an element of the utilities dictionary::

            sage: A = matrix([[2, 5], [0, 4]])
            sage: B = matrix([[2, 0], [5, 4]])
            sage: prisoners_dilemma = NormalFormGame([A, B])
            sage: prisoners_dilemma
            Normal Form Game with the following utilities: {(0, 0): [2, 2],
             (0, 1): [5, 0], (1, 0): [0, 5], (1, 1): [4, 4]}
            sage: del(prisoners_dilemma[(0,1)])
            sage: prisoners_dilemma
            Normal Form Game with the following utilities: {(0, 0): [2, 2],
             (1, 0): [0, 5], (1, 1): [4, 4]}
        """
    def __getitem__(self, key):
        """
        This method is one of a collection that aims to make a game
        instance behave like a dictionary which can be used if a game
        is to be generated without using a matrix.

        Here we allow for querying a key::

            sage: A = matrix([[2, 5], [0, 4]])
            sage: B = matrix([[2, 0], [5, 4]])
            sage: prisoners_dilemma = NormalFormGame([A, B])
            sage: prisoners_dilemma[(0, 1)]
            [5, 0]
            sage: del(prisoners_dilemma[(0,1)])
            sage: prisoners_dilemma[(0, 1)]
            Traceback (most recent call last):
            ...
            KeyError: (0, 1)
        """
    def __iter__(self):
        '''
        This method is one of a collection that aims to make a game
        instance behave like a dictionary which can be used if a game
        is to be generated without using a matrix.

        Here we allow for iteration over the game to correspond to
        iteration over keys of the utility dictionary::

            sage: A = matrix([[2, 5], [0, 4]])
            sage: B = matrix([[2, 0], [5, 4]])
            sage: prisoners_dilemma = NormalFormGame([A, B])
            sage: for key, value in sorted(prisoners_dilemma.items()):
            ....:     print("The strategy pair {} gives utilities {}".format(key, value))
            The strategy pair (0, 0) gives utilities [2, 2]
            The strategy pair (0, 1) gives utilities [5, 0]
            The strategy pair (1, 0) gives utilities [0, 5]
            The strategy pair (1, 1) gives utilities [4, 4]
        '''
    def __setitem__(self, key, value) -> None:
        """
        This method is one of a collection that aims to make a game
        instance behave like a dictionary which can be used if a game
        is to be generated without using a matrix.

        Here we set up setting the value of a key::

            sage: A = matrix([[2, 5], [0, 4]])
            sage: B = matrix([[2, 0], [5, 4]])
            sage: prisoners_dilemma = NormalFormGame([A, B])
            sage: del(prisoners_dilemma[(0,1)])
            sage: prisoners_dilemma[(0,1)] = [5,6]
            sage: prisoners_dilemma.payoff_matrices()
            (
            [2 5]  [2 6]
            [0 4], [5 4]
            )

        We can use the dictionary-like interface to overwrite a strategy
        profile::

            sage: prisoners_dilemma[(0,1)] = [-3,-30]
            sage: prisoners_dilemma.payoff_matrices()
            (
            [ 2 -3]  [  2 -30]
            [ 0  4], [  5   4]
            )
        """
    def __len__(self) -> int:
        """
        Return the length of the game to be the length of the utilities.

        EXAMPLES::

            sage: A = matrix([[2, 5], [0, 4]])
            sage: B = matrix([[2, 0], [5, 4]])
            sage: prisoners_dilemma = NormalFormGame([A, B])
            sage: len(prisoners_dilemma)
            4
        """
    def is_constant_sum(self):
        """
        Check if the game is constant sum.

        EXAMPLES::

            sage: A = matrix([[2, 1], [1, 2.5]])
            sage: g = NormalFormGame([A])
            sage: g.is_constant_sum()
            True
            sage: g = NormalFormGame([A, A])
            sage: g.is_constant_sum()
            False
            sage: A = matrix([[1, 1], [1, 1]])
            sage: g = NormalFormGame([A, A])
            sage: g.is_constant_sum()
            True
            sage: A = matrix([[1, 1, 2], [1, 1, -1], [1, -1, 1]])
            sage: B = matrix([[2, 2, 1], [2, 2, 4], [2, 4, 2]])
            sage: g = NormalFormGame([A, B])
            sage: g.is_constant_sum()
            True
            sage: A = matrix([[1, 1, 2], [1, 1, -1], [1, -1, 1]])
            sage: B = matrix([[2, 2, 1], [2, 2.1, 4], [2, 4, 2]])
            sage: g = NormalFormGame([A, B])
            sage: g.is_constant_sum()
            False
        """
    def payoff_matrices(self):
        """
        Return 2 matrices representing the payoffs for each player.

        EXAMPLES::

            sage: p1 = matrix([[1, 2], [3, 4]])
            sage: p2 = matrix([[3, 3], [1, 4]])
            sage: g = NormalFormGame([p1, p2])
            sage: g.payoff_matrices()
            (
            [1 2]  [3 3]
            [3 4], [1 4]
            )

        If we create a game with 3 players we will not be able to
        obtain payoff matrices::

            sage: g = NormalFormGame()
            sage: g.add_player(2)  # adding first player with 2 strategies
            sage: g.add_player(2)  # adding second player with 2 strategies
            sage: g.add_player(2)  # adding third player with 2 strategies
            sage: g.payoff_matrices()
            Traceback (most recent call last):
            ...
            ValueError: Only available for 2 player games

        If we do create a two player game but it is not complete
        then an error is also raised::

            sage: g = NormalFormGame()
            sage: g.add_player(1)  # Adding first player with 1 strategy
            sage: g.add_player(1)  # Adding second player with 1 strategy
            sage: g.payoff_matrices()
            Traceback (most recent call last):
            ...
            ValueError: utilities have not been populated

        The above creates a 2 player game where each player has
        a single strategy. Here we populate the strategies and
        can then view the payoff matrices::

            sage: g[0, 0] = [1,2]
            sage: g.payoff_matrices()
            ([1], [2])
        """
    def add_player(self, num_strategies) -> None:
        """
        Add a player to a NormalFormGame.

        INPUT:

        - ``num_strategies`` -- the number of strategies the player should have

        EXAMPLES::

            sage: g = NormalFormGame()
            sage: g.add_player(2)  # Adding first player with 2 strategies
            sage: g.add_player(1)  # Adding second player with 1 strategy
            sage: g.add_player(1)  # Adding third player with 1 strategy
            sage: g
            Normal Form Game with the following utilities:
             {(0, 0, 0): [False, False, False],
              (1, 0, 0): [False, False, False]}
        """
    def add_strategy(self, player) -> None:
        """
        Add a strategy to a player, will not affect already completed
        strategy profiles.

        INPUT:

        - ``player`` -- the index of the player

        EXAMPLES:

        A simple example::

            sage: s = matrix([[1, 0], [-2, 3]])
            sage: t = matrix([[3, 2], [-1, 0]])
            sage: example = NormalFormGame([s, t])
            sage: example
            Normal Form Game with the following utilities: {(0, 0): [1, 3],
             (0, 1): [0, 2], (1, 0): [-2, -1], (1, 1): [3, 0]}
            sage: example.add_strategy(0)
            sage: example
            Normal Form Game with the following utilities: {(0, 0): [1, 3],
             (0, 1): [0, 2],
             (1, 0): [-2, -1],
             (1, 1): [3, 0],
             (2, 0): [False, False],
             (2, 1): [False, False]}
        """
    def obtain_nash(self, algorithm: bool = False, maximization: bool = True, solver=None):
        """
        A function to return the Nash equilibrium for the game.
        Optional arguments can be used to specify the algorithm used.
        If no algorithm is passed then an attempt is made to use the most
        appropriate algorithm.

        INPUT:

        - ``algorithm`` -- the following algorithms should be available through
          this function:

          * ``'lrs'`` -- this algorithm is only suited for 2 player games.
            See the lrs web site (http://cgm.cs.mcgill.ca/~avis/C/lrs.html).

          * ``'LCP'`` -- this algorithm is only suited for 2 player games.
            See the gambit web site (http://gambit.sourceforge.net/).

          * ``'lp'`` -- this algorithm is only suited for 2 player
            constant sum games. Uses MILP solver determined by the
            ``solver`` argument.

          * ``'enumeration'`` -- this is a very inefficient
            algorithm (in essence a brute force approach).

            1. For each k in 1...min(size of strategy sets)
            2. For each I,J supports of size k
            3. Prune: check if supports are dominated
            4. Solve indifference conditions and check that have Nash Equilibrium.

            Solving the indifference conditions is done by building the
            corresponding linear system.  If  `\\rho_1, \\rho_2` are the
            supports player 1 and 2 respectively.  Then, indifference implies:

            .. MATH::

                u_1(s_1,\\rho_2) = u_1(s_2, \\rho_2)

            for all `s_1, s_2` in the support of `\\rho_1`. This corresponds to:

            .. MATH::

                \\sum_{j\\in S(\\rho_2)}A_{s_1,j}{\\rho_2}_j = \\sum_{j\\in S(\\rho_2)}A_{s_2,j}{\\rho_2}_j

            for all `s_1, s_2` in the support of `\\rho_1` where `A` is the payoff
            matrix of player 1. Equivalently we can consider consecutive rows of
            `A` (instead of all pairs of strategies). Thus the corresponding
            linear system can be written as:

            .. MATH::

                \\left(\\sum_{j \\in S(\\rho_2)}A_{i,j} - A_{i+1,j}\\right){\\rho_2}_j

            for all `1\\leq i \\leq |S(\\rho_1)|` (where `A` has been modified to only
            contain the rows corresponding to `S(\\rho_1)`). We also require all
            elements of `\\rho_2` to sum to 1:

            .. MATH::

                \\sum_{j\\in S(\\rho_1)}{\\rho_2}_j = 1

        - ``maximization`` -- boolean (default: ``True``); whether a player is
          trying to maximize their utility or minimize it:

          * When set to ``True`` it is assumed that players aim to
            maximise their utility.

          * When set to ``False`` it is assumed that players aim to
            minimise their utility.

        - ``solver`` -- (optional) see :class:`MixedIntegerLinearProgram`
          for more information on the MILP solvers in Sage, may also
          be ``'gambit'`` to use the MILP solver included with the gambit
          library. Note that ``None`` means to use the default Sage LP solver,
          normally GLPK.

        EXAMPLES:

        A game with 1 equilibrium when ``maximization`` is ``True`` and 3 when
        ``maximization`` is ``False``::

            sage: A = matrix([[10, 500, 44],
            ....:       [15, 10, 105],
            ....:       [19, 204, 55],
            ....:       [20, 200, 590]])
            sage: B = matrix([[2, 1, 2],
            ....:             [0, 5, 6],
            ....:             [3, 4, 1],
            ....:             [4, 1, 20]])
            sage: g=NormalFormGame([A, B])
            sage: g.obtain_nash(algorithm='lrs')  # optional - lrslib
            [[(0, 0, 0, 1), (0, 0, 1)]]
            sage: g.obtain_nash(algorithm='lrs', maximization=False)  # optional - lrslib
            [[(2/3, 1/12, 1/4, 0), (6333/8045, 247/8045, 293/1609)],
             [(3/4, 0, 1/4, 0), (0, 11/307, 296/307)],
             [(5/6, 1/6, 0, 0), (98/99, 1/99, 0)]]

        This particular game has 3 Nash equilibria::

            sage: A = matrix([[3,3],
            ....:             [2,5],
            ....:             [0,6]])
            sage: B = matrix([[3,2],
            ....:             [2,6],
            ....:             [3,1]])
            sage: g = NormalFormGame([A, B])
            sage: g.obtain_nash(algorithm='enumeration')
            [[(0, 1/3, 2/3), (1/3, 2/3)],
             [(4/5, 1/5, 0), (2/3, 1/3)],
             [(1, 0, 0), (1, 0)]]

        Here is a slightly larger game::

            sage: A = matrix([[160, 205, 44],
            ....:             [175, 180, 45],
            ....:             [201, 204, 50],
            ....:             [120, 207, 49]])
            sage: B = matrix([[2, 2, 2],
            ....:             [1, 0, 0],
            ....:             [3, 4, 1],
            ....:             [4, 1, 2]])
            sage: g=NormalFormGame([A, B])
            sage: g.obtain_nash(algorithm='enumeration')
            [[(0, 0, 3/4, 1/4), (1/28, 27/28, 0)]]
            sage: g.obtain_nash(algorithm='lrs')  # optional - lrslib
            [[(0, 0, 3/4, 1/4), (1/28, 27/28, 0)]]
            sage: g.obtain_nash(algorithm='LCP')  # optional - gambit
            [[(0.0, 0.0, 0.75, 0.25), (0.0357142857, 0.9642857143, 0.0)]]

        2 random matrices::

            sage: player1 = matrix([[2, 8, -1, 1, 0],
            ....:                   [1, 1, 2, 1, 80],
            ....:                   [0, 2, 15, 0, -12],
            ....:                   [-2, -2, 1, -20, -1],
            ....:                   [1, -2, -1, -2, 1]])
            sage: player2 = matrix([[0, 8, 4, 2, -1],
            ....:                   [6, 14, -5, 1, 0],
            ....:                   [0, -2, -1, 8, -1],
            ....:                   [1, -1, 3, -3, 2],
            ....:                   [8, -4, 1, 1, -17]])
            sage: fivegame = NormalFormGame([player1, player2])
            sage: fivegame.obtain_nash(algorithm='enumeration')
            [[(1, 0, 0, 0, 0), (0, 1, 0, 0, 0)]]
            sage: fivegame.obtain_nash(algorithm='lrs')  # optional - lrslib
            [[(1, 0, 0, 0, 0), (0, 1, 0, 0, 0)]]
            sage: fivegame.obtain_nash(algorithm='LCP')  # optional - gambit
            [[(1.0, 0.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0, 0.0)]]

        Here are some examples of finding Nash equilibria for constant-sum games::

            sage: A = matrix.identity(2)
            sage: cg = NormalFormGame([A])
            sage: cg.obtain_nash(algorithm='lp')
            [[(0.5, 0.5), (0.5, 0.5)]]
            sage: cg.obtain_nash(algorithm='lp', solver='Coin')                   # optional - sage_numerical_backends_coin
            [[(0.5, 0.5), (0.5, 0.5)]]
            sage: cg.obtain_nash(algorithm='lp', solver='PPL')
            [[(1/2, 1/2), (1/2, 1/2)]]
            sage: cg.obtain_nash(algorithm='lp', solver='gambit')                 # optional - gambit
            [[(0.5, 0.5), (0.5, 0.5)]]
            sage: A = matrix([[2, 1], [1, 3]])
            sage: cg = NormalFormGame([A])
            sage: ne = cg.obtain_nash(algorithm='lp', solver='glpk')
            sage: [[[round(el, 6) for el in v] for v in eq] for eq in ne]
            [[[0.666667, 0.333333], [0.666667, 0.333333]]]
            sage: ne = cg.obtain_nash(algorithm='lp', solver='Coin')              # optional - sage_numerical_backends_coin
            sage: [[[round(el, 6) for el in v] for v in eq] for eq in ne]         # optional - sage_numerical_backends_coin
            [[[0.666667, 0.333333], [0.666667, 0.333333]]]
            sage: cg.obtain_nash(algorithm='lp', solver='PPL')
            [[(2/3, 1/3), (2/3, 1/3)]]
            sage: ne = cg.obtain_nash(algorithm='lp', solver='gambit')            # optional - gambit
            sage: [[[round(el, 6) for el in v] for v in eq] for eq in ne]         # optional - gambit
            [[[0.666667, 0.333333], [0.666667, 0.333333]]]
            sage: A = matrix([[1, 2, 1], [1, 1, 2], [2, 1, 1]])
            sage: B = matrix([[2, 1, 2], [2, 2, 1], [1, 2, 2]])
            sage: cg = NormalFormGame([A, B])
            sage: ne = cg.obtain_nash(algorithm='lp', solver='glpk')
            sage: [[[round(el, 6) for el in v] for v in eq] for eq in ne]
            [[[0.333333, 0.333333, 0.333333], [0.333333, 0.333333, 0.333333]]]
            sage: ne = cg.obtain_nash(algorithm='lp', solver='Coin')              # optional - sage_numerical_backends_coin
            sage: [[[round(el, 6) for el in v] for v in eq] for eq in ne]         # optional - sage_numerical_backends_coin
            [[[0.333333, 0.333333, 0.333333], [0.333333, 0.333333, 0.333333]]]
            sage: cg.obtain_nash(algorithm='lp', solver='PPL')
            [[(1/3, 1/3, 1/3), (1/3, 1/3, 1/3)]]
            sage: ne = cg.obtain_nash(algorithm='lp', solver='gambit')            # optional - gambit
            sage: [[[round(el, 6) for el in v] for v in eq] for eq in ne]         # optional - gambit
            [[[0.333333, 0.333333, 0.333333], [0.333333, 0.333333, 0.333333]]]
            sage: A = matrix([[160, 205, 44],
            ....:             [175, 180, 45],
            ....:             [201, 204, 50],
            ....:             [120, 207, 49]])
            sage: cg = NormalFormGame([A])
            sage: cg.obtain_nash(algorithm='lp', solver='PPL')
            [[(0, 0, 1, 0), (0, 0, 1)]]

        Running the constant-sum solver on a game which is not a constant sum
        game generates a :exc:`ValueError`::

            sage: cg = NormalFormGame([A, A])
            sage: cg.obtain_nash(algorithm='lp', solver='glpk')
            Traceback (most recent call last):
            ...
            ValueError: Input game needs to be a two player constant sum game

        Here is an example of a 3 by 2 game with 3 Nash equilibrium::

            sage: A = matrix([[3,3],
            ....:             [2,5],
            ....:             [0,6]])
            sage: B = matrix([[3,2],
            ....:             [2,6],
            ....:             [3,1]])
            sage: g = NormalFormGame([A, B])
            sage: g.obtain_nash(algorithm='enumeration')
            [[(0, 1/3, 2/3), (1/3, 2/3)], [(4/5, 1/5, 0), (2/3, 1/3)], [(1, 0, 0), (1, 0)]]

        Of the algorithms implemented, only ``'lrs'`` and ``'enumeration'``
        are guaranteed to find all Nash equilibria in a game. The solver for
        constant sum games only ever finds one Nash equilibrium. Although it
        is possible for the ``'LCP'`` solver to find all Nash equilibria
        in some instances, there are instances where it will not be able to
        find all Nash equilibria.::

            sage: A = matrix(2, 2)
            sage: gg = NormalFormGame([A])
            sage: gg.obtain_nash(algorithm='enumeration')
            [[(0, 1), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, 1)], [(1, 0), (1, 0)]]
            sage: gg.obtain_nash(algorithm='lrs')  # optional - lrs
            [[(0, 1), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, 1)], [(1, 0), (1, 0)]]
            sage: gg.obtain_nash(algorithm='lp', solver='glpk')
            [[(1.0, 0.0), (1.0, 0.0)]]
            sage: gg.obtain_nash(algorithm='LCP')  # optional - gambit
            [[(1.0, 0.0), (1.0, 0.0)]]
            sage: gg.obtain_nash(algorithm='enumeration', maximization=False)
            [[(0, 1), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, 1)], [(1, 0), (1, 0)]]
            sage: gg.obtain_nash(algorithm='lrs', maximization=False)  # optional - lrs
            [[(0, 1), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, 1)], [(1, 0), (1, 0)]]
            sage: gg.obtain_nash(algorithm='lp', solver='glpk', maximization=False)
            [[(1.0, 0.0), (1.0, 0.0)]]
            sage: gg.obtain_nash(algorithm='LCP', maximization=False)  # optional - gambit
            [[(1.0, 0.0), (1.0, 0.0)]]

        Note that outputs for all algorithms are as lists of lists of
        tuples and the equilibria have been sorted so that all algorithms give
        a comparable output (although ``'LCP'`` returns floats)::

            sage: enumeration_eqs = g.obtain_nash(algorithm='enumeration')
            sage: [[type(s) for s in eq] for eq in enumeration_eqs]
            [[<... 'tuple'>, <... 'tuple'>], [<... 'tuple'>, <... 'tuple'>], [<... 'tuple'>, <... 'tuple'>]]
            sage: lrs_eqs = g.obtain_nash(algorithm='lrs')  # optional - lrslib
            sage: [[type(s) for s in eq] for eq in lrs_eqs]  # optional - lrslib
            [[<... 'tuple'>, <... 'tuple'>], [<... 'tuple'>, <... 'tuple'>], [<... 'tuple'>, <... 'tuple'>]]
            sage: LCP_eqs = g.obtain_nash(algorithm='LCP')  # optional - gambit
            sage: [[type(s) for s in eq] for eq in LCP_eqs]  # optional - gambit
            [[<... 'tuple'>, <... 'tuple'>], [<... 'tuple'>, <... 'tuple'>], [<... 'tuple'>, <... 'tuple'>]]
            sage: enumeration_eqs == sorted(enumeration_eqs)
            True
            sage: lrs_eqs == sorted(lrs_eqs)  # optional - lrslib
            True
            sage: LCP_eqs == sorted(LCP_eqs)  # optional - gambit
            True
            sage: lrs_eqs == enumeration_eqs  # optional - lrslib
            True
            sage: enumeration_eqs == LCP_eqs  # optional - gambit
            False
            sage: [[[round(float(p), 6) for p in str] for str in eq] for eq in enumeration_eqs] == [[[round(float(p), 6) for p in str] for str in eq] for eq in LCP_eqs]  # optional - gambit
            True

        Also, not specifying a valid solver would lead to an error::

            sage: A = matrix.identity(2)
            sage: g = NormalFormGame([A])
            sage: g.obtain_nash(algorithm='invalid')
            Traceback (most recent call last):
            ...
            ValueError: 'algorithm' should be set to 'enumeration', 'LCP', 'lp' or 'lrs'
            sage: g.obtain_nash(algorithm='lp', solver='invalid')
            Traceback (most recent call last):
            ...
            ValueError: 'solver' should be set to 'GLPK', ..., None
             (in which case the default one is used), or a callable.
        """
    def is_degenerate(self, certificate: bool = False) -> bool:
        """
        A function to check whether the game is degenerate or not.

        Will return a boolean.

        A two-player game is called nondegenerate if no mixed strategy of
        support size `k` has more than `k` pure best responses [NN2007]_. In a
        degenerate game, this definition is violated, for example if there
        is a pure strategy that has two pure best responses.

        The implementation here transforms the search over mixed strategies to a
        search over supports which is a discrete search. A full explanation of
        this is given in [CK2015]_. This problem is known to be NP-Hard
        [Du2009]_.  Another possible implementation is via best response
        polytopes, see :issue:`18958`.

        The game Rock-Paper-Scissors is an example of a non-degenerate game,::

            sage: g = game_theory.normal_form_games.RPS()
            sage: g.is_degenerate()
            False

        whereas `Rock-Paper-Scissors-Lizard-Spock
        <http://www.samkass.com/theories/RPSSL.html>`_ is degenerate because
        for every pure strategy there are two best responses.::

            sage: g = game_theory.normal_form_games.RPSLS()
            sage: g.is_degenerate()
            True

        EXAMPLES:

        Here is an example of a degenerate game given in [DGRB2010]_::

            sage: A = matrix([[3, 3], [2, 5], [0, 6]])
            sage: B = matrix([[3, 3], [2, 6], [3, 1]])
            sage: degenerate_game = NormalFormGame([A,B])
            sage: degenerate_game.is_degenerate()
            True

        Here is an example of a degenerate game given in [NN2007]_::

            sage: A = matrix([[0, 6], [2, 5], [3, 3]])
            sage: B = matrix([[1, 0], [0, 2], [4, 4]])
            sage: d_game = NormalFormGame([A, B])
            sage: d_game.is_degenerate()
            True

        Here are some other examples of degenerate games::

            sage: M = matrix([[2, 1], [1, 1]])
            sage: N = matrix([[1, 1], [1, 2]])
            sage: game  = NormalFormGame([M, N])
            sage: game.is_degenerate()
            True

        If more information is required, it may be useful to use
        ``certificate=True``. This will return a boolean of whether the game is
        degenerate or not, and if True; a tuple containing the strategy where
        degeneracy was found and the player it belongs to. ``0`` is the row
        player and ``1`` is the column player.::

            sage: M = matrix([[2, 1], [1, 1]])
            sage: N = matrix([[1, 1], [1, 2]])
            sage: g  = NormalFormGame([M, N])
            sage: test, certificate = g.is_degenerate(certificate=True)
            sage: test, certificate
            (True, ((1, 0), 0))

        Using the output, we see that the opponent has more best responses than
        the size of the support of the strategy in question ``(1, 0)``. (We
        specify the player as ``(player + 1) % 2`` to ensure that we have the
        opponent's index.)::

            sage: g.best_responses(certificate[0], (certificate[1] + 1) % 2)
            [0, 1]

        Another example with a mixed strategy causing degeneracy.::

            sage: A = matrix([[3, 0], [0, 3], [1.5, 1.5]])
            sage: B = matrix([[4, 3], [2, 6], [3, 1]])
            sage: g = NormalFormGame([A, B])
            sage: test, certificate = g.is_degenerate(certificate=True)
            sage: test, certificate
            (True, ((1/2, 1/2), 1))

        Again, we see that the opponent has more best responses than the size of
        the support of the strategy in question ``(1/2, 1/2)``.::

            sage: g.best_responses(certificate[0], (certificate[1] + 1) % 2)
            [0, 1, 2]

        Sometimes, the different algorithms for obtaining nash_equilibria don't
        agree with each other. This can happen when games are degenerate::

            sage: a = matrix([[-75, 18, 45, 33],
            ....:            [42, -8, -77, -18],
            ....:            [83, 18, 11, 40],
            ....:            [-10, -38, 76, -9]])
            sage: b = matrix([[62, 64, 87, 51],
            ....:            [-41, -27, -69, 52],
            ....:            [-17, 25, -97, -82],
            ....:            [30, 31, -1, 50]])
            sage: d_game = NormalFormGame([a, b])
            sage: d_game.obtain_nash(algorithm='lrs')  # optional - lrslib
            [[(0, 0, 1, 0), (0, 1, 0, 0)],
             [(17/29, 0, 0, 12/29), (0, 0, 42/73, 31/73)],
             [(122/145, 0, 23/145, 0), (0, 1, 0, 0)]]
            sage: d_game.obtain_nash(algorithm='LCP')  # optional - gambit
            [[(0.5862068966, 0.0, 0.0, 0.4137931034),
              (0.0, 0.0, 0.5753424658, 0.4246575342)]]
            sage: d_game.obtain_nash(algorithm='enumeration')
            [[(0, 0, 1, 0), (0, 1, 0, 0)], [(17/29, 0, 0, 12/29), (0, 0, 42/73, 31/73)]]
            sage: d_game.is_degenerate()
            True

        TESTS::

            sage: g = NormalFormGame()
            sage: g.add_player(3)  # Adding first player with 3 strategies
            sage: g.add_player(3)  # Adding second player with 3 strategies
            sage: for key in g:
            ....:     g[key] = [0, 0]
            sage: g.is_degenerate()
            True

            sage: A = matrix([[3, 0], [0, 3], [1.5, 1.5]])
            sage: B = matrix([[4, 3], [2, 6], [3, 1]])
            sage: g = NormalFormGame([A, B])
            sage: g.is_degenerate()
            True

            sage: A = matrix([[1, -1], [-1, 1]])
            sage: B = matrix([[-1, 1], [1, -1]])
            sage: matching_pennies = NormalFormGame([A, B])
            sage: matching_pennies.is_degenerate()
            False

            sage: A = matrix([[2, 5], [0, 4]])
            sage: B = matrix([[2, 0], [5, 4]])
            sage: prisoners_dilemma = NormalFormGame([A, B])
            sage: prisoners_dilemma.is_degenerate()
            False

            sage: g = NormalFormGame()
            sage: g.add_player(2)
            sage: g.add_player(2)
            sage: g.add_player(2)
            sage: g.is_degenerate()
            Traceback (most recent call last):
            ...
            NotImplementedError: Tests for Degeneracy is not yet implemented for
             games with more than two players.
        """
    def best_responses(self, strategy, player):
        """
        For a given strategy for a player and the index of the opponent,
        computes the payoff for the opponent and returns a list of the indices
        of the best responses. Only implemented for two player games

        INPUT:

        - ``strategy`` -- a probability distribution vector

        - ``player`` -- the index of the opponent, ``0`` for the row player,
          ``1`` for the column player

        EXAMPLES::

            sage: A = matrix([[3, 0], [0, 3], [1.5, 1.5]])
            sage: B = matrix([[4, 3], [2, 6], [3, 1]])
            sage: g = NormalFormGame([A, B])

        Now we can obtain the best responses for Player 1, when Player 2 uses
        different strategies::

            sage: g.best_responses((1/2, 1/2), player=0)
            [0, 1, 2]
            sage: g.best_responses((3/4, 1/4), player=0)
            [0]

        To get the best responses for Player 2 we pass the argument :code:`player=1`::

            sage: g.best_responses((4/5, 1/5, 0), player=1)
            [0, 1]

            sage: A = matrix([[1, 0], [0, 1], [0, 0]])
            sage: B = matrix([[1, 0], [0, 1], [0.7, 0.8]])
            sage: g = NormalFormGame([A, B])
            sage: g.best_responses((0, 1, 0), player=1)
            [1]

            sage: A = matrix([[3,3],[2,5],[0,6]])
            sage: B = matrix([[3,3],[2,6],[3,1]])
            sage: degenerate_game = NormalFormGame([A,B])
            sage: degenerate_game.best_responses((1, 0, 0), player=1)
            [0, 1]

            sage: A = matrix([[3, 0], [0, 3], [1.5, 1.5]])
            sage: B = matrix([[4, 3], [2, 6], [3, 1]])
            sage: g = NormalFormGame([A, B])
            sage: g.best_responses((1/3, 1/3, 1/3), player=1)
            [1]

        Note that this has only been implemented for 2 player games::

            sage: g = NormalFormGame()
            sage: g.add_player(2)  # adding first player with 2 strategies
            sage: g.add_player(2)  # adding second player with 2 strategies
            sage: g.add_player(2)  # adding third player with 2 strategies
            sage: g.best_responses((1/2, 1/2), player=2)
            Traceback (most recent call last):
            ...
            ValueError: Only available for 2 player games

        If the strategy is not of the correct dimension for the given player
        then an error is returned::

            sage: A = matrix([[3, 0], [0, 3], [1.5, 1.5]])
            sage: B = matrix([[4, 3], [2, 6], [3, 1]])
            sage: g = NormalFormGame([A, B])
            sage: g.best_responses((1/2, 1/2), player=1)
            Traceback (most recent call last):
            ...
            ValueError: Strategy is not of correct dimension

            sage: g.best_responses((1/3, 1/3, 1/3), player=0)
            Traceback (most recent call last):
            ...
            ValueError: Strategy is not of correct dimension

        If the strategy is not a true probability vector then an error is
        passed::

            sage: A = matrix([[3, 0], [0, 3], [1.5, 1.5]])
            sage: B = matrix([[4, 3], [2, 6], [3, 1]])
            sage: g = NormalFormGame([A, B])
            sage: g.best_responses((1/3, 1/2, 0), player=1)
            Traceback (most recent call last):
            ...
            ValueError: Strategy is not a probability distribution vector

            sage: A = matrix([[3, 0], [0, 3], [1.5, 1.5]])
            sage: B = matrix([[4, 3], [2, 6], [3, 1]])
            sage: g = NormalFormGame([A, B])
            sage: g.best_responses((3/2, -1/2), player=0)
            Traceback (most recent call last):
            ...
            ValueError: Strategy is not a probability distribution vector

        If the player specified is not `0` or `1`, an error is raised::

            sage: A = matrix([[3, 0], [0, 3], [1.5, 1.5]])
            sage: B = matrix([[4, 3], [2, 6], [3, 1]])
            sage: g = NormalFormGame([A, B])
            sage: g.best_responses((1/2, 1/2), player='Player1')
            Traceback (most recent call last):
            ...
            ValueError: Player1 is not an index of the opponent, must be 0 or 1
        """

class _Player:
    num_strategies: Incomplete
    def __init__(self, num_strategies) -> None:
        """
        TESTS::

            sage: from sage.game_theory.normal_form_game import _Player
            sage: p = _Player(5)
            sage: p.num_strategies
            5
        """
    def add_strategy(self) -> None:
        """
        TESTS::

            sage: from sage.game_theory.normal_form_game import _Player
            sage: p = _Player(5)
            sage: p.add_strategy()
            sage: p.num_strategies
            6
        """
