from _typeshed import Incomplete
from sage.structure.sage_object import SageObject as SageObject

MAX_WIDTH: Incomplete

class CharacterArt(SageObject):
    def __init__(self, lines=[], breakpoints=[], baseline=None) -> None:
        '''
        Abstract base class for character art.

        INPUT:

        - ``lines`` -- the list of lines of the representation of the
          character art object

        - ``breakpoints`` -- the list of points where the representation can be
          split

        - ``baseline`` -- the reference line (from the bottom)

        Instead of just integers, ``breakpoints`` may also contain tuples
        consisting of an offset and the breakpoints of a nested substring at
        that offset. This is used to prioritize the breakpoints, as line breaks
        inside the substring will be avoided if possible.

        EXAMPLES::

            sage: i = var(\'i\')                                                          # needs sage.symbolic
            sage: ascii_art(sum(pi^i/factorial(i)*x^i, i, 0, oo))                       # needs sage.symbolic
             pi*x
            e

        TESTS::

            sage: from sage.typeset.ascii_art import AsciiArt
            sage: aao = AsciiArt()
            sage: aao
            <BLANKLINE>
            sage: aa = AsciiArt(["  *  ", " * * ", "*****"]); aa
              *
             * *
            *****

        If there are nested breakpoints, line breaks are avoided inside the
        nested elements (:issue:`29204`)::

            sage: s = ascii_art([[1..5], [1..17], [1..25]])
            sage: s._breakpoints
            [(2, [4, 7, 10, 13]), 20, (21, [4, 7,..., 56]), 83, (84, [4, 7,..., 88])]
            sage: str(s)
            \'[ [ 1, 2, 3, 4, 5 ],\\n\\n
              [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ],\\n\\n
              [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,\\n\\n
              22, 23, 24, 25 ] ]\'
        '''
    @classmethod
    def empty(cls):
        """
        Return the empty character art object.

        EXAMPLES::

            sage: from sage.typeset.ascii_art import AsciiArt
            sage: AsciiArt.empty()
        """
    def __getitem__(self, key):
        '''
        Return the line `key` of the ASCII art object.

        TESTS::

            sage: from sage.typeset.ascii_art import AsciiArt
            sage: p5 = AsciiArt(["  *  ", " * * ", "*****"])
            sage: p5[1]
            \' * * \'
        '''
    def __iter__(self):
        '''
        Iterator on all lines of the ASCII art object.

        TESTS::

            sage: from sage.typeset.ascii_art import AsciiArt
            sage: p5 = AsciiArt(["  *  ", " * * ", "*****"])
            sage: for line in p5:
            ....:     print(line)
              *
             * *
            *****
        '''
    def __format__(self, fmt) -> str:
        """
        Format ``self``.

        EXAMPLES::

            sage: M = matrix([[1,2],[3,4]])                                             # needs sage.modules
            sage: format(ascii_art(M))                                                  # needs sage.modules
            '[1 2]\\n[3 4]'
            sage: format(unicode_art(M))                                                # needs sage.modules
            '\\u239b1 2\\u239e\\n\\u239d3 4\\u23a0'
        """
    def get_baseline(self):
        '''
        Return the line where the baseline is, for example::

                5      4
            14*x  + 5*x

        the baseline has at line `0` and ::

            { o       }
            {  \\  : 4 }
            {   o     }

        has at line `1`.

        TESTS::

            sage: from sage.typeset.ascii_art import AsciiArt
            sage: aa = AsciiArt(["   *   ", "  * *  ", " *   * ", "*******"], baseline=1);aa
               *
              * *
             *   *
            *******
            sage: aa.get_baseline()
            1
            sage: b = AsciiArt(["<-"])
            sage: aa+b
               *
              * *
             *   * <-
            *******
        '''
    def get_breakpoints(self):
        '''
        Return an iterator of breakpoints where the object can be split.

        This method is deprecated, as its output is an implementation detail.
        The mere breakpoints of a character art element do not reflect the best
        way to split it if nested structures are involved. For details, see
        :issue:`29204`.

        For example the expression::

               5    4
            14x + 5x

        can be split on position 4 (on the ``+``).

        EXAMPLES::

            sage: from sage.typeset.ascii_art import AsciiArt
            sage: p3 = AsciiArt([" * ", "***"])
            sage: p5 = AsciiArt(["  *  ", " * * ", "*****"])
            sage: aa = ascii_art([p3, p5])
            sage: aa.get_breakpoints()
            doctest:...: DeprecationWarning: get_breakpoints() is deprecated
            See https://github.com/sagemath/sage/issues/29204 for details.
            [6]
        '''
    def split(self, pos):
        '''
        Split the representation at the position ``pos``.

        EXAMPLES::

            sage: from sage.typeset.ascii_art import AsciiArt
            sage: p3 = AsciiArt([" * ", "***"])
            sage: p5 = AsciiArt(["  *  ", " * * ", "*****"])
            sage: aa = ascii_art([p3, p5])
            sage: a,b= aa.split(6)
            sage: a
            [
            [  *
            [ ***,
            sage: b
               *   ]
              * *  ]
             ***** ]
        '''
    def width(self):
        '''
        Return the length (width) of the ASCII art object.

        OUTPUT: integer; the number of characters in each line

        TESTS::

            sage: from sage.typeset.ascii_art import AsciiArt
            sage: p3 = AsciiArt([" * ", "***"])
            sage: len(p3), p3.width(), p3.height()
            (3, 3, 2)
            sage: p5 = AsciiArt(["  *  ", " * * ", "*****"])
            sage: len(p5), p5.width(), p5.height()
            (5, 5, 3)
        '''
    __len__ = width
    def height(self):
        '''
        Return the height of the ASCII art object.

        OUTPUT: integer; the number of lines

        TESTS::

            sage: from sage.typeset.ascii_art import AsciiArt
            sage: p3 = AsciiArt([" * ", "***"])
            sage: p3.height()
            2
            sage: p5 = AsciiArt(["  *  ", " * * ", "*****"])
            sage: p5.height()
            3
        '''
    def __add__(self, Nelt):
        """
        Concatenate two character art objects.

        By default, when two objects are concatenated, the new one will be
        splittable between both.

        If the baseline is defined, the concatenation is computed such that the
        new baseline coincides with the olders.

        For example, let `T` be a tree with its baseline ascii art
        representation in the middle::

            o
             \\\n              o
             / \\\n            o   o

        and let `M` be a matrix with its baseline ascii art representation at
        the middle two::

            [1 2 3]
            [4 5 6]
            [7 8 9]

        then the concatenation of both will give::

            o
             \\   [1 2 3]
              o  [4 5 6]
             / \\ [7 8 9]
            o   o

        Since :issue:`28527`, the baseline must always be a number.

        TESTS::

            sage: from sage.typeset.ascii_art import AsciiArt
            sage: l5 = AsciiArt(lines=['|' for _ in range(5)], baseline=2); l5
            |
            |
            |
            |
            |
            sage: l3 = AsciiArt(lines=['|' for _ in range(3)], baseline=1); l3
            |
            |
            |
            sage: l3 + l5
             |
            ||
            ||
            ||
             |
            sage: l5 + l3
            |
            ||
            ||
            ||
            |
            sage: l5._baseline = 0
            sage: l5 + l3
            |
            |
            |
            ||
            ||
             |
            sage: l5._baseline = 4
            sage: l5 + l3
             |
            ||
            ||
            |
            |
            |
            sage: l3._baseline = 0
            sage: l3 + l5
            |
            |
            ||
             |
             |
             |
             |
        """
    def __mul__(self, Nelt):
        """
        Stack two character art objects vertically.

        TESTS::

            sage: from sage.typeset.ascii_art import AsciiArt
            sage: cub = AsciiArt(lines=['***' for _ in range(3)]); cub
            ***
            ***
            ***
            sage: pyr = AsciiArt(lines=[' ^ ', '/ \\\\', '---']); pyr
             ^
            / \\\n            ---
            sage: cub * pyr
            ***
            ***
            ***
             ^
            / \\\n            ---
        """
