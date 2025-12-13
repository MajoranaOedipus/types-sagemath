class PseudolineArrangement:
    def __init__(self, seq, encoding: str = 'auto') -> None:
        """
        Create an arrangement of pseudolines.

        INPUT:

        - ``seq`` -- a sequence describing the line arrangement. It can be:

          - A list of `n` permutations of size `n-1`.
          - A list of `\\binom n 2` transpositions
          - A Felsner matrix, given as a sequence of `n` binary vectors of
            length `n-1`.

        - ``encoding`` -- information on how the data should be interpreted, and
          can assume any value among 'transpositions', 'permutations', 'Felsner'
          or 'auto'. In the latter case, the type will be guessed (default
          behaviour).

        .. NOTE::

           * The pseudolines are assumed to be integers `0,\\dots,n-1`.

           * For more information on the different encodings, see the
             :mod:`pseudolines module <sage.geometry.pseudolines>`'s
             documentation.

        TESTS:

        From permutations::

            sage: from sage.geometry.pseudolines import PseudolineArrangement
            sage: permutations = [[3, 2, 1], [3, 2, 0], [3, 1, 0], [2, 1, 0]]
            sage: PseudolineArrangement(permutations)
            Arrangement of pseudolines of size 4

        From transpositions ::

            sage: from sage.geometry.pseudolines import PseudolineArrangement
            sage: transpositions = [(3, 2), (3, 1), (0, 3), (2, 1), (0, 2), (0, 1)]
            sage: PseudolineArrangement(transpositions)
            Arrangement of pseudolines of size 4

        From a Felsner matrix::

            sage: from sage.geometry.pseudolines import PseudolineArrangement
            sage: permutations = [[3, 2, 1], [3, 2, 0], [3, 1, 0], [2, 1, 0]]
            sage: p = PseudolineArrangement(permutations)
            sage: matrix = p.felsner_matrix()
            sage: PseudolineArrangement(matrix) == p
            True

        Wrong input::

            sage: PseudolineArrangement([[5, 2, 1], [3, 2, 0], [3, 1, 0], [2, 1, 0]])
            Traceback (most recent call last):
            ...
            ValueError: Are the lines really numbered from 0 to n-1?
            sage: PseudolineArrangement([(3, 2), (3, 1), (0, 3), (2, 1), (0, 2)])
            Traceback (most recent call last):
            ...
            ValueError: A line is numbered 3 but the number of transpositions ...
        """
    def transpositions(self):
        """
        Return the arrangement as `\\binom n 2` transpositions.

        See the :mod:`pseudolines module <sage.geometry.pseudolines>`'s
        documentation for more information on this encoding.

        EXAMPLES::

            sage: from sage.geometry.pseudolines import PseudolineArrangement
            sage: permutations = [[3, 2, 1], [3, 2, 0], [3, 1, 0], [2, 1, 0]]
            sage: p1 = PseudolineArrangement(permutations)
            sage: transpositions = [(3, 2), (3, 1), (0, 3), (2, 1), (0, 2), (0, 1)]
            sage: p2 = PseudolineArrangement(transpositions)
            sage: p1 == p2
            True
            sage: p1.transpositions()
            [(3, 2), (3, 1), (0, 3), (2, 1), (0, 2), (0, 1)]
            sage: p2.transpositions()
            [(3, 2), (3, 1), (0, 3), (2, 1), (0, 2), (0, 1)]
        """
    def permutations(self):
        """
        Return the arrangements as `n` permutations of size `n-1`.

        See the :mod:`pseudolines module <sage.geometry.pseudolines>`'s
        documentation for more information on this encoding.

        EXAMPLES::

            sage: from sage.geometry.pseudolines import PseudolineArrangement
            sage: permutations = [[3, 2, 1], [3, 2, 0], [3, 1, 0], [2, 1, 0]]
            sage: p = PseudolineArrangement(permutations)
            sage: p.permutations()
            [[3, 2, 1], [3, 2, 0], [3, 1, 0], [2, 1, 0]]
        """
    def felsner_matrix(self):
        """
        Return a Felsner matrix describing the arrangement.

        See the :mod:`pseudolines module <sage.geometry.pseudolines>`'s
        documentation for more information on this encoding.

        EXAMPLES::

            sage: from sage.geometry.pseudolines import PseudolineArrangement
            sage: permutations = [[3, 2, 1], [3, 2, 0], [3, 1, 0], [2, 1, 0]]
            sage: p = PseudolineArrangement(permutations)
            sage: p.felsner_matrix()
            [[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]]
        """
    def show(self, **args):
        """
        Displays the pseudoline arrangement as a wiring diagram.

        INPUT:

        - ``**args`` -- any arguments to be forwarded to the ``show`` method. In
          particular, to tune the dimensions, use the ``figsize`` argument
          (example below).

        EXAMPLES::

            sage: from sage.geometry.pseudolines import PseudolineArrangement
            sage: permutations = [[3, 2, 1], [3, 2, 0], [3, 1, 0], [2, 1, 0]]
            sage: p = PseudolineArrangement(permutations)
            sage: p.show(figsize=[7,5])                                                 # needs sage.plot

        TESTS::

            sage: from sage.geometry.pseudolines import PseudolineArrangement
            sage: permutations = [[3, 2, 1], [3, 2, 0], [3, 0, 1], [2, 0, 1]]
            sage: p = PseudolineArrangement(permutations)
            sage: p.show()                                                              # needs sage.plot
            Traceback (most recent call last):
            ...
            ValueError: There has been a problem while plotting the figure...
        """
    def __eq__(self, other):
        """
        Test of equality.

        TESTS::

            sage: from sage.geometry.pseudolines import PseudolineArrangement
            sage: permutations = [[3, 2, 1], [3, 2, 0], [3, 1, 0], [2, 1, 0]]
            sage: p1 = PseudolineArrangement(permutations)
            sage: transpositions = [(3, 2), (3, 1), (0, 3), (2, 1), (0, 2), (0, 1)]
            sage: p2 = PseudolineArrangement(transpositions)
            sage: p1 == p2
            True
        """
    def __ne__(self, other):
        """
        Test for non-equality.

        TESTS::

            sage: from sage.geometry.pseudolines import PseudolineArrangement
            sage: permutations = [[3, 2, 1], [3, 2, 0], [3, 1, 0], [2, 1, 0]]
            sage: p1 = PseudolineArrangement(permutations)
            sage: transpositions = [(3, 2), (3, 1), (0, 3), (2, 1), (0, 2), (0, 1)]
            sage: p2 = PseudolineArrangement(transpositions)
            sage: p1 != p2
            False
        """
