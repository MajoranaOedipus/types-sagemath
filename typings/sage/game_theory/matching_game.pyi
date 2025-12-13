from _typeshed import Incomplete
from sage.graphs.bipartite_graph import BipartiteGraph as BipartiteGraph
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.sage_object import SageObject as SageObject

class MatchingGame(SageObject):
    """
    A matching game.

    A matching game (also called a stable matching problem) models a situation
    in a population of `N` suitors and `N` reviewers. Suitors and reviewers
    rank their preferences and attempt to find a match.

    Formally, a matching game of size `N` is defined by two disjoint sets `S`
    and `R` of size `N`. Associated to each element of `S` and `R` is a
    preference list:

    .. MATH::

        f : S \\to R^N
        \\text{ and }
        g : R \\to S^N.

    Here is an example of matching game on 4 players:

    .. MATH::

        S = \\{J, K, L, M\\}, \\\\\n        R = \\{A, B, C, D\\}.

    With preference functions:

    .. MATH::

        f(s) = \\begin{cases}
        (A, D, C, B) & \\text{ if } s=J,\\\\\n        (A, B, C, D) & \\text{ if } s=K,\\\\\n        (B, D, C, A) & \\text{ if } s=L,\\\\\n        (C, A, B, D) & \\text{ if } s=M,\\\\\n        \\end{cases}

        g(s) = \\begin{cases}
        (L, J, K, M) & \\text{ if } s=A,\\\\\n        (J, M, L, K) & \\text{ if } s=B,\\\\\n        (K, M, L, J) & \\text{ if } s=C,\\\\\n        (M, K, J, L) & \\text{ if } s=D.\\\\\n        \\end{cases}

    INPUT:

    Two potential inputs are accepted (see below to see the effect of each):

    - ``reviewer/suitors_preferences`` -- dictionary containing the
      preferences of all players:

      * key - each reviewer/suitors
      * value - a tuple of suitors/reviewers

    OR:

    - ``integer`` -- integer simply representing the number of reviewers
      and suitors

    To implement the above game in Sage::

        sage: suitr_pref = {'J': ('A', 'D', 'C', 'B'),
        ....:               'K': ('A', 'B', 'C', 'D'),
        ....:               'L': ('B', 'D', 'C', 'A'),
        ....:               'M': ('C', 'A', 'B', 'D')}
        sage: reviewr_pref = {'A': ('L', 'J', 'K', 'M'),
        ....:                 'B': ('J', 'M', 'L', 'K'),
        ....:                 'C': ('K', 'M', 'L', 'J'),
        ....:                 'D': ('M', 'K', 'J', 'L')}
        sage: m = MatchingGame([suitr_pref, reviewr_pref])
        sage: m
        A matching game with 4 suitors and 4 reviewers
        sage: m.suitors()
        ('J', 'K', 'L', 'M')
        sage: m.reviewers()
        ('A', 'B', 'C', 'D')

    A matching `M` is any bijection between `S` and `R`. If `s \\in S` and
    `r \\in R` are matched by `M` we denote:

    .. MATH::

        M(s) = r.

    On any given matching game, one intends to find a matching that is stable.
    In other words, so that no one individual has an incentive to break their
    current match.

    Formally, a stable matching is a matching that has no blocking pairs.
    A blocking pair is any pair `(s, r)` such that `M(s) \\neq r` but `s`
    prefers `r` to `M(r)` and `r` prefers `s` to `M^{-1}(r)`.

    To obtain the stable matching in Sage we use the ``solve`` method which
    uses the extended Gale-Shapley algorithm [DI1989]_::

        sage: m.solve()
        {'J': 'A', 'K': 'C', 'L': 'D', 'M': 'B'}

    Matchings have a natural representations as bipartite graphs::

        sage: plot(m)                                                                   # needs sage.plot
        Graphics object consisting of 13 graphics primitives

    The above plots the bipartite graph associated with the matching.
    This plot can be accessed directly::

        sage: graph = m.bipartite_graph()
        sage: graph
        Bipartite graph on 8 vertices

    It is possible to initiate a matching game without having to name each
    suitor and reviewer::

        sage: n = 8
        sage: big_game = MatchingGame(n)
        sage: big_game.suitors()
        (1, 2, 3, 4, 5, 6, 7, 8)
        sage: big_game.reviewers()
        (-1, -2, -3, -4, -5, -6, -7, -8)

    If we attempt to obtain the stable matching for the above game,
    without defining the preference function we obtain an error::

        sage: big_game.solve()
        Traceback (most recent call last):
        ...
        ValueError: suitor preferences are not complete

    To continue we have to populate the preference dictionary. Here
    is one example where the preferences are simply the corresponding
    element of the permutation group::

        sage: from itertools import permutations
        sage: suitr_preferences = list(permutations([-i-1 for i in range(n)]))
        sage: revr_preferences = list(permutations([i+1 for i in range(n)]))
        sage: for player in range(n):
        ....:     big_game.suitors()[player].pref = suitr_preferences[player]
        ....:     big_game.reviewers()[player].pref = revr_preferences[-player]
        sage: big_game.solve()
        {1: -1, 2: -8, 3: -6, 4: -7, 5: -5, 6: -4, 7: -3, 8: -2}

    Note that we can also combine the two ways of creating a game. For example
    here is an initial matching game::

        sage: suitrs = {'Romeo': ('Juliet', 'Rosaline'),
        ....:            'Mercutio': ('Juliet', 'Rosaline')}
        sage: revwrs = {'Juliet': ('Romeo', 'Mercutio'),
        ....:           'Rosaline': ('Mercutio', 'Romeo')}
        sage: g = MatchingGame(suitrs, revwrs)

    Let us assume that all of a sudden a new pair of suitors and reviewers is
    added but their names are not known::

        sage: g.add_reviewer()
        sage: g.add_suitor()
        sage: g.reviewers()
        (-3, 'Juliet', 'Rosaline')
        sage: g.suitors()
        (3, 'Mercutio', 'Romeo')

    Note that when adding a reviewer or a suitor all preferences are wiped::

        sage: [s.pref for s in g.suitors()]
        [[], [], []]
        sage: [r.pref for r in g.reviewers()]
        [[], [], []]

    If we now try to solve the game we will get an error as we have not
    specified the preferences which will need to be updated::

        sage: g.solve()
        Traceback (most recent call last):
        ...
        ValueError: suitor preferences are not complete

    Here we update the preferences so that the new reviewers and suitors
    do not affect things too much (they prefer each other and are the least
    preferred of the others)::

        sage: g.suitors()[1].pref = suitrs['Mercutio'] + (-3,)
        sage: g.suitors()[2].pref = suitrs['Romeo'] + (-3,)
        sage: g.suitors()[0].pref = (-3, 'Juliet', 'Rosaline')
        sage: g.reviewers()[2].pref = revwrs['Rosaline'] + (3,)
        sage: g.reviewers()[1].pref = revwrs['Juliet'] + (3,)
        sage: g.reviewers()[0].pref = (3, 'Romeo', 'Mercutio')

    Now the game can be solved::

        sage: D = g.solve()
        sage: D['Mercutio']
        'Rosaline'
        sage: D['Romeo']
        'Juliet'
        sage: D[3]
        -3

    Note that the above could be equivalently (and more simply) carried out
    by simply updated the original preference dictionaries::

        sage: for key in suitrs:
        ....:     suitrs[key] = suitrs[key] + (-3,)
        sage: for key in revwrs:
        ....:     revwrs[key] = revwrs[key] + (3,)
        sage: suitrs[3] = (-3, 'Juliet', 'Rosaline')
        sage: revwrs[-3] = (3, 'Romeo', 'Mercutio')
        sage: g = MatchingGame(suitrs, revwrs)
        sage: D = g.solve()
        sage: D['Mercutio']
        'Rosaline'
        sage: D['Romeo']
        'Juliet'
        sage: D[3]
        -3

    It can be shown that the Gale-Shapley algorithm will return the stable
    matching that is optimal from the point of view of the suitors and is in
    fact the worst possible matching from the point of view of the reviewers.
    To quickly obtain the matching that is optimal for the reviewers we
    use the ``solve`` method with the ``invert=True`` option::

        sage: left_dict = {'a': ('A', 'B', 'C'),
        ....:              'b': ('B', 'C', 'A'),
        ....:              'c': ('B', 'A', 'C')}
        sage: right_dict = {'A': ('b', 'c', 'a'),
        ....:               'B': ('a', 'c', 'b'),
        ....:               'C': ('a', 'b', 'c')}
        sage: quick_game = MatchingGame([left_dict, right_dict])
        sage: quick_game.solve()
        {'a': 'A', 'b': 'C', 'c': 'B'}
        sage: quick_game.solve(invert=True)
        {'A': 'c', 'B': 'a', 'C': 'b'}

    EXAMPLES:

    8 player letter game::

        sage: suitr_pref = {'J': ('A', 'D', 'C', 'B'),
        ....:               'K': ('A', 'B', 'C', 'D'),
        ....:               'L': ('B', 'D', 'C', 'A'),
        ....:               'M': ('C', 'A', 'B', 'D')}
        sage: reviewr_pref = {'A': ('L', 'J', 'K', 'M'),
        ....:                 'B': ('J', 'M', 'L', 'K'),
        ....:                 'C': ('K', 'M', 'L', 'J'),
        ....:                 'D': ('M', 'K', 'J', 'L')}
        sage: m = MatchingGame([suitr_pref, reviewr_pref])
        sage: m.suitors()
        ('J', 'K', 'L', 'M')
        sage: m.reviewers()
        ('A', 'B', 'C', 'D')

    Also works for numbers::

        sage: suit = {0: (3, 4),
        ....:         1: (3, 4)}
        sage: revr = {3: (0, 1),
        ....:         4: (1, 0)}
        sage: g = MatchingGame([suit, revr])

    Can create a game from an integer. This gives default set of preference
    functions::

        sage: g = MatchingGame(3)
        sage: g
        A matching game with 3 suitors and 3 reviewers

    We have an empty set of preferences for a default named set of
    preferences::

        sage: for s in g.suitors():
        ....:     s, s.pref
        (1, [])
        (2, [])
        (3, [])
        sage: for r in g.reviewers():
        ....:     r, r.pref
        (-1, [])
        (-2, [])
        (-3, [])

    Before trying to solve such a game the algorithm will check if it is
    complete or not::

        sage: g.solve()
        Traceback (most recent call last):
        ...
        ValueError: suitor preferences are not complete

    To be able to obtain the stable matching we must input the preferences::

        sage: for s in g.suitors():
        ....:   s.pref = (-1, -2, -3)
        sage: for r in g.reviewers():
        ....:   r.pref = (1, 2, 3)
        sage: g.solve()
        {1: -1, 2: -2, 3: -3}
    """
    def __init__(self, generator, revr=None) -> None:
        """
        Initialize a matching game and check the inputs.

        TESTS::

            sage: suit = {0: (3, 4), 1: (3, 4)}
            sage: revr = {3: (0, 1), 4: (1, 0)}
            sage: g = MatchingGame([suit, revr])
            sage: TestSuite(g).run()

            sage: g = MatchingGame(3)
            sage: TestSuite(g).run()

            sage: g2 = MatchingGame(QQ(3))
            sage: g == g2
            True

        The above shows that the input can be either two  dictionaries
        or an integer::

            sage: g = MatchingGame(suit, 3)
            Traceback (most recent call last):
            ...
            TypeError: generator must be an integer or a pair of 2 dictionaries

            sage: g = MatchingGame(matrix(2, [1, 2, 3, 4]))
            Traceback (most recent call last):
            ...
            TypeError: generator must be an integer or a pair of 2 dictionaries

            sage: g = MatchingGame('1,2,3', 'A,B,C')
            Traceback (most recent call last):
            ...
            TypeError: generator must be an integer or a pair of 2 dictionaries
        """
    def __eq__(self, other):
        """
        Check equality.

            sage: suit = {0: (3, 4), 1: (3, 4)}
            sage: revr = {3: (0, 1), 4: (1, 0)}
            sage: g = MatchingGame([suit, revr])
            sage: g2 = MatchingGame([suit, revr])
            sage: g == g2
            True

        Here the two sets of suitors have different preferences::

            sage: suit1 = {0: (3, 4), 1: (3, 4)}
            sage: revr1 = {3: (1, 0), 4: (1, 0)}
            sage: g1 = MatchingGame([suit1, revr1])
            sage: suit2 = {0: (4, 3), 1: (3, 4)}
            sage: revr2 = {3: (1, 0), 4: (1, 0)}
            sage: g2 = MatchingGame([suit2, revr2])
            sage: g == g2
            False

        Here the two sets of reviewers have different preferences::

            sage: suit1 = {0: (3, 4), 1: (3, 4)}
            sage: revr1 = {3: (0, 1), 4: (1, 0)}
            sage: g1 = MatchingGame([suit1, revr1])
            sage: suit2 = {0: (3, 4), 1: (3, 4)}
            sage: revr2 = {3: (1, 0), 4: (0, 1)}
            sage: g2 = MatchingGame([suit2, revr2])
            sage: g == g2
            False

        Note that if two games are created with players ordered differently
        they can still be equal::

            sage: g1 = MatchingGame(1)
            sage: g1.add_reviewer(-2)
            sage: g1.add_reviewer(-3)
            sage: g1.add_suitor(3)
            sage: g1.add_suitor(2)
            sage: g1.reviewers()
            (-1, -2, -3)
            sage: g1.suitors()
            (1, 2, 3)

            sage: g2 = MatchingGame(1)
            sage: g2.add_reviewer(-2)
            sage: g2.add_reviewer(-3)
            sage: g2.add_suitor(2)
            sage: g2.add_suitor(3)
            sage: g2.reviewers()
            (-1, -2, -3)
            sage: g2.suitors()
            (1, 2, 3)

            sage: g1 == g2
            True
        """
    __hash__: Incomplete
    def plot(self):
        """
        Create the plot representing the stable matching for the game.
        Note that the game must be solved for this to work.

        EXAMPLES:

        An error is returned if the game is not solved::

            sage: suit = {0: (3, 4),
            ....:         1: (3, 4)}
            sage: revr = {3: (0, 1),
            ....:         4: (1, 0)}
            sage: g = MatchingGame([suit, revr])
            sage: plot(g)                                                               # needs sage.plot
            Traceback (most recent call last):
            ...
            ValueError: game has not been solved yet

            sage: g.solve()
            {0: 3, 1: 4}
            sage: plot(g)                                                               # needs sage.plot
            Graphics object consisting of 7 graphics primitives
        """
    def bipartite_graph(self):
        """
        Construct a ``BipartiteGraph`` Object of the game.
        This method is similar to the plot method.
        Note that the game must be solved for this to work.

        EXAMPLES:

        An error is returned if the game is not solved::

            sage: suit = {0: (3, 4),
            ....:         1: (3, 4)}
            sage: revr = {3: (0, 1),
            ....:         4: (1, 0)}
            sage: g = MatchingGame([suit, revr])
            sage: g.bipartite_graph()
            Traceback (most recent call last):
            ...
            ValueError: game has not been solved yet

            sage: g.solve()
            {0: 3, 1: 4}
            sage: g.bipartite_graph()
            Bipartite graph on 4 vertices
        """
    def add_suitor(self, name=None) -> None:
        '''
        Add a suitor to the game.

        INPUT:

        - ``name`` -- can be a string or a number; if left blank will
          automatically generate an integer

        EXAMPLES:

        Creating a two player game::

            sage: g = MatchingGame(2)
            sage: g.suitors()
            (1, 2)

        Adding a suitor without specifying a name::

            sage: g.add_suitor()
            sage: g.suitors()
            (1, 2, 3)

        Adding a suitor while specifying a name::

            sage: g.add_suitor(\'D\')
            sage: g.suitors()
            (1, 2, 3, \'D\')

        Note that now our game is no longer complete::

            sage: g._is_complete()
            Traceback (most recent call last):
            ...
            ValueError: must have the same number of reviewers as suitors

        Note that an error is raised if one tries to add a suitor
        with a name that already exists::

            sage: g.add_suitor(\'D\')
            Traceback (most recent call last):
            ...
            ValueError: a suitor with name "D" already exists

        If we add a suitor without passing a name then the name
        of the suitor will not use one that is already chosen::

            sage: suit = {0: (-1,  -2),
            ....:         2: (-2, -1)}
            sage: revr = {-1: (0, 1),
            ....:         -2: (1, 0)}
            sage: g = MatchingGame([suit, revr])
            sage: g.suitors()
            (0, 2)

            sage: g.add_suitor()
            sage: g.suitors()
            (0, 2, 3)
        '''
    def add_reviewer(self, name=None) -> None:
        '''
        Add a reviewer to the game.

        INPUT:

        - ``name`` -- can be a string or number; if left blank will
          automatically generate an integer

        EXAMPLES:

        Creating a two player game::

            sage: g = MatchingGame(2)
            sage: g.reviewers()
            (-1, -2)

        Adding a suitor without specifying a name::

            sage: g.add_reviewer()
            sage: g.reviewers()
            (-1, -2, -3)

        Adding a suitor while specifying a name::

            sage: g.add_reviewer(10)
            sage: g.reviewers()
            (-1, -2, -3, 10)

        Note that now our game is no longer complete::

            sage: g._is_complete()
            Traceback (most recent call last):
            ...
            ValueError: must have the same number of reviewers as suitors

        Note that an error is raised if one tries to add a reviewer
        with a name that already exists::

            sage: g.add_reviewer(10)
            Traceback (most recent call last):
            ...
            ValueError: a reviewer with name "10" already exists

        If we add a reviewer without passing a name then the name
        of the reviewer will not use one that is already chosen::

            sage: suit = {0: (-1,  -3),
            ....:         1: (-3, -1)}
            sage: revr = {-1: (0, 1),
            ....:         -3: (1, 0)}
            sage: g = MatchingGame([suit, revr])
            sage: g.reviewers()
            (-1, -3)

            sage: g.add_reviewer()
            sage: g.reviewers()
            (-1, -3, -4)
        '''
    def suitors(self):
        """
        Return the suitors of ``self``.

        EXAMPLES::

            sage: g = MatchingGame(2)
            sage: g.suitors()
            (1, 2)
        """
    def reviewers(self):
        """
        Return the reviewers of ``self``.

        EXAMPLES::

            sage: g = MatchingGame(2)
            sage: g.reviewers()
            (-1, -2)
        """
    def solve(self, invert: bool = False):
        """
        Compute a stable matching for the game using the Gale-Shapley
        algorithm.

        EXAMPLES::

            sage: suitr_pref = {'J': ('A', 'D', 'C', 'B'),
            ....:               'K': ('A', 'B', 'C', 'D'),
            ....:               'L': ('B', 'C', 'D', 'A'),
            ....:               'M': ('C', 'A', 'B', 'D')}
            sage: reviewr_pref = {'A': ('L', 'J', 'K', 'M'),
            ....:                 'B': ('J', 'M', 'L', 'K'),
            ....:                 'C': ('M', 'K', 'L', 'J'),
            ....:                 'D': ('M', 'K', 'J', 'L')}
            sage: m = MatchingGame([suitr_pref, reviewr_pref])
            sage: m.solve()
            {'J': 'A', 'K': 'D', 'L': 'B', 'M': 'C'}

            sage: suitr_pref = {'J': ('A', 'D', 'C', 'B'),
            ....:               'K': ('A', 'B', 'C', 'D'),
            ....:               'L': ('B', 'C', 'D', 'A'),
            ....:               'M': ('C', 'A', 'B', 'D')}
            sage: reviewr_pref = {'A': ('L', 'J', 'K', 'M'),
            ....:                 'B': ('J', 'M', 'L', 'K'),
            ....:                 'C': ('M', 'K', 'L', 'J'),
            ....:                 'D': ('M', 'K', 'J', 'L')}
            sage: m = MatchingGame([suitr_pref, reviewr_pref])
            sage: m.solve(invert=True)
            {'A': 'L', 'B': 'J', 'C': 'M', 'D': 'K'}

            sage: suitr_pref = {1: (-1,)}
            sage: reviewr_pref = {-1: (1,)}
            sage: m = MatchingGame([suitr_pref, reviewr_pref])
            sage: m.solve()
            {1: -1}

            sage: suitr_pref = {}
            sage: reviewr_pref = {}
            sage: m = MatchingGame([suitr_pref, reviewr_pref])
            sage: m.solve()
            {}

        TESTS:

        This also works for players who are both a suitor and reviewer::

            sage: suit = {0: (3,4,2), 1: (3,4,2), 2: (2,3,4)}
            sage: revr = {2: (2,0,1), 3: (0,1,2), 4: (1,0,2)}
            sage: g = MatchingGame(suit, revr)
            sage: g.solve()
            {0: 3, 1: 4, 2: 2}
        """

class Player:
    """
    A class to act as a data holder for the players used of the
    matching games.

    These instances are used when initiating players and to keep track of
    whether or not partners have a preference.
    """
    pref: Incomplete
    partner: Incomplete
    def __init__(self, name) -> None:
        """
        TESTS::

            sage: from sage.game_theory.matching_game import Player
            sage: p = Player(10)
            sage: p
            10
            sage: p.pref
            []
            sage: p.partner is None
            True
        """
    def __hash__(self):
        """
        TESTS::

            sage: from sage.game_theory.matching_game import Player
            sage: p = Player(10)
            sage: d = {p : (1, 2, 3)}
            sage: d
            {10: (1, 2, 3)}
        """
    def __eq__(self, other):
        """

        Tests equality of two players. This only checks the name of the player
        and not their preferences.

        TESTS::

            sage: from sage.game_theory.matching_game import Player
            sage: p = Player(10)
            sage: q = Player('Karl')
            sage: p == q
            False

            sage: from sage.game_theory.matching_game import Player
            sage: p = Player(10)
            sage: q = Player(10)
            sage: p == q
            True

            sage: from sage.game_theory.matching_game import Player
            sage: p = Player(10)
            sage: q = Player(10)
            sage: p.pref = (1, 2)
            sage: p.pref = (2, 1)
            sage: p == q
            True
        """
    def __lt__(self, other):
        """
        Test less than inequality of two players. Allows for players to be
        sorted on their names.

        TESTS::

            sage: from sage.game_theory.matching_game import Player
            sage: p = Player('A')
            sage: q = Player('B')
            sage: p < q
            True
            sage: q < p
            False

            sage: p = Player(0)
            sage: q = Player(1)
            sage: p < q
            True
            sage: q < p
            False
        """
    def __gt__(self, other):
        """
        Test greater than inequality of two players. Allows for players to be
        sorted on their names.

        TESTS::

            sage: from sage.game_theory.matching_game import Player
            sage: p = Player('A')
            sage: q = Player('B')
            sage: p > q
            False
            sage: q > p
            True

            sage: p = Player(0)
            sage: q = Player(1)
            sage: p > q
            False
            sage: q > p
            True
        """
    def __ge__(self, other):
        """
        Test greater than or equal inequality of two players. Allows for
        players to be sorted on their names.

        TESTS::

            sage: from sage.game_theory.matching_game import Player
            sage: p = Player('A')
            sage: q = Player('B')
            sage: p >= q
            False
            sage: q >= p
            True

            sage: p = Player(0)
            sage: q = Player(1)
            sage: p >= q
            False
            sage: q >= p
            True

            sage: p = Player(0)
            sage: q = Player(0)
            sage: p >= q
            True

            sage: p = Player('C')
            sage: q = Player('C')
            sage: p >= q
            True
        """
    def __le__(self, other):
        """
        Test less than or equal inequality of two players. Allows for
        players to be sorted on their names.

        TESTS::

            sage: from sage.game_theory.matching_game import Player
            sage: p = Player('A')
            sage: q = Player('B')
            sage: p <= q
            True
            sage: q <= p
            False

            sage: p = Player(0)
            sage: q = Player(1)
            sage: p <= q
            True
            sage: q <= p
            False

            sage: p = Player(0)
            sage: q = Player(0)
            sage: p <= q
            True

            sage: p = Player('C')
            sage: q = Player('C')
            sage: p <= q
            True
        """
    def __ne__(self, other):
        """
        Test inequality of two players. Allows for
        players to be sorted on their names.

        TESTS::

            sage: from sage.game_theory.matching_game import Player
            sage: p = Player('A')
            sage: q = Player('B')
            sage: p != q
            True

            sage: p = Player(0)
            sage: q = Player(1)
            sage: p != q
            True

            sage: p = Player(0)
            sage: q = Player(0)
            sage: p != q
            False

            sage: p = Player('C')
            sage: q = Player('C')
            sage: p != q
            False
        """
