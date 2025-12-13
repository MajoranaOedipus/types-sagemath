from sage.structure.sage_object import SageObject as SageObject
from sage.typeset.ascii_art import AsciiArt as AsciiArt
from sage.typeset.unicode_art import UnicodeArt as UnicodeArt

class GraftalLaceCellularAutomata(SageObject):
    """
    Graftal Lace Cellular Automata (GLCA).

    A GLCA is a deterministic cellular automaton whose rule is given
    by an 8-digit octal number `r_7 \\cdots r_0`. For a node `s_i`, let
    `b_k`, for `k = -1,0,1` denote if there is an edge from `s_i` to
    `s'_{i+k}`, where `s'_j` is the previous row. We determine the value
    at `t_{i+k}` by considering the value of `r_m`, where the binary
    representation of `m` is `b_{-1} b_0 b_1`. If `r_m` has a binary
    representation of b'_1 b'_0 b'_{-1}`, then we add `b'_k` to `t_{i+k}`.

    INPUT:

    - ``rule`` -- list of length 8 with integer entries `0 \\leq x < 8`

    EXAMPLES::

        sage: G = cellular_automata.GraftalLace([0,2,5,4,7,2,3,3])
        sage: G.evolve(3)
        sage: ascii_art(G)
               o
               |
               o
               |
             o o o
            /| |/|
           o o o o o
          /| |/|\\|/|
         o o o o o o o

        sage: G = cellular_automata.GraftalLace([3,0,3,4,7,6,3,1])
        sage: G.evolve(3)
        sage: ascii_art(G)
               o
               |
               o
               |\\\n             o o o
            /  |\\ \\\n           o o o o o
          /|/  |\\ \\ \\\n         o o o o o o o

        sage: G = cellular_automata.GraftalLace([2,0,3,3,6,0,2,7])
        sage: G.evolve(20)
        sage: G.plot()                                                                  # needs sage.plot
        Graphics object consisting of 842 graphics primitives

    .. PLOT::

        G = cellular_automata.GraftalLace([2,0,3,3,6,0,2,7])
        G.evolve(20)
        P = G.plot()
        sphinx_plot(P)

    REFERENCES:

    - [Kas2018]_
    """
    def __init__(self, rule) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: G = cellular_automata.GraftalLace([5,1,2,5,4,5,5,0])
            sage: TestSuite(G).run()

            sage: G = cellular_automata.GraftalLace([5,1,2,5,4,5,5])
            Traceback (most recent call last):
            ...
            ValueError: invalid rule
            sage: G = cellular_automata.GraftalLace([5,1,2,5,4,5,5,0,5])
            Traceback (most recent call last):
            ...
            ValueError: invalid rule
            sage: G = cellular_automata.GraftalLace([5,1,2,5,-1,5,5,0])
            Traceback (most recent call last):
            ...
            ValueError: invalid rule
            sage: G = cellular_automata.GraftalLace([8,5,1,2,5,4,5,5])
            Traceback (most recent call last):
            ...
            ValueError: invalid rule
        """
    def __eq__(self, other):
        """
        Check equality.

        Two GLCAs are equal if and only if they have the same rule.

        TESTS::

            sage: G1 = cellular_automata.GraftalLace([5,1,2,5,4,5,5,0])
            sage: G2 = cellular_automata.GraftalLace([0,5,5,4,5,2,1,5])
            sage: G3 = cellular_automata.GraftalLace([5,1,2,5,4,5,5,0])
            sage: G1 == G2
            False
            sage: G1 == G3
            True
            sage: G1 is G3
            False
        """
    def __ne__(self, other):
        """
        Check non equality.

        TESTS::

            sage: G1 = cellular_automata.GraftalLace([5,1,2,5,4,5,5,0])
            sage: G2 = cellular_automata.GraftalLace([0,5,5,4,5,2,1,5])
            sage: G3 = cellular_automata.GraftalLace([5,1,2,5,4,5,5,0])
            sage: G1 != G2
            True
            sage: G1 != G3
            False
            sage: G1 is G3
            False
        """
    def evolve(self, number=None) -> None:
        """
        Evolve ``self``.

        INPUT:

        - ``number`` -- (default: 1) the number of times to perform
          the evolution

        EXAMPLES::

            sage: G = cellular_automata.GraftalLace([5,1,2,5,4,5,5,0])
            sage: ascii_art(G)
             o
             |
             o
            sage: G.evolve(2)
            sage: ascii_art(G)
                 o
                 |
                 o
                / \\\n               o o o
              / \\ / \\\n             o o o o o

            sage: G = cellular_automata.GraftalLace([0,2,1,4,7,2,3,0])
            sage: G.evolve(3)
            sage: ascii_art(G)
                   o
                   |
                   o
                   |
                 o o o
                   |
               o o o o o
                   |
             o o o o o o o
        """
    def print_states(self, number=None, use_unicode: bool = False) -> None:
        """
        Print the first ``num`` states of ``self``.

        .. NOTE::

            If the number of states computed for ``self`` is less than
            ``num``, then this evolves the system using the default
            time evolution.

        INPUT:

        - ``number`` -- the number of states to print

        EXAMPLES::

            sage: G = cellular_automata.GraftalLace([5,1,2,5,4,5,5,0])
            sage: G.evolve(2)
            sage: G.print_states()
                 o
                 |
                 o
                / \\\n               o o o
              / \\ / \\\n             o o o o o
            sage: G.evolve(20)
            sage: G.print_states(3)
                 o
                 |
                 o
                / \\\n               o o o
              / \\ / \\\n             o o o o o
        """
    def plot(self, number=None):
        """
        Return a plot of ``self``.

        INPUT:

        - ``number`` -- the number of states to plot

        EXAMPLES::

            sage: G = cellular_automata.GraftalLace([5,1,2,5,4,5,5,0])
            sage: G.evolve(20)
            sage: G.plot()                                                              # needs sage.plot
            Graphics object consisting of 865 graphics primitives
        """
