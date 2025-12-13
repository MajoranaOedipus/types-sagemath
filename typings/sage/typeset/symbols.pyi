from _typeshed import Incomplete
from sage.structure.sage_object import SageObject as SageObject

class CompoundSymbol(SageObject):
    character: Incomplete
    top: Incomplete
    extension: Incomplete
    bottom: Incomplete
    middle: Incomplete
    middle_top: Incomplete
    middle_bottom: Incomplete
    top_2: Incomplete
    bottom_2: Incomplete
    def __init__(self, character, top, extension, bottom, middle=None, middle_top=None, middle_bottom=None, top_2=None, bottom_2=None) -> None:
        """
        A multi-character (ascii/unicode art) symbol.

        INPUT:

        Instead of a string, each of these can be unicode in Python 2:

        - ``character`` -- string; the single-line version of the symbol

        - ``top`` -- string; the top line of a multi-line symbol

        - ``extension`` -- string; the extension line of a multi-line symbol (will
          be repeated)

        - ``bottom`` -- string; the bottom line of a multi-line symbol

        - ``middle`` -- (optional) string; the middle part, for example
          in curly braces. Will be used only once for the symbol, and
          only if its height is odd.

        - ``middle_top`` -- (optional) string; the upper half of the
          2-line middle part if the height of the symbol is even.
          Will be used only once for the symbol.

        - ``middle_bottom`` -- (optional) string; the lower half of the
          2-line middle part if the height of the symbol is even.
          Will be used only once for the symbol.

        - ``top_2`` -- (optional) string; the upper half of a 2-line symbol

        - ``bottom_2`` -- (optional) string; the lower half of a 2-line symbol

        EXAMPLES::

            sage: from sage.typeset.symbols import CompoundSymbol
            sage: i = CompoundSymbol('I', '+', '|', '+', '|')
            sage: i.print_to_stdout(1)
            I
            sage: i.print_to_stdout(3)
            +
            |
            +
        """
    def __call__(self, num_lines):
        """
        Return the lines for a multi-line symbol.

        INPUT:

        - ``num_lines`` -- integer; the total number of lines

        OUTPUT: list of strings / unicode strings

        EXAMPLES::

            sage: from sage.typeset.symbols import unicode_left_parenthesis
            sage: unicode_left_parenthesis(4)
            ['\\u239b', '\\u239c', '\\u239c', '\\u239d']
        """
    def print_to_stdout(self, num_lines) -> None:
        """
        Print the multi-line symbol.

        This method is for testing purposes.

        INPUT:

        - ``num_lines`` -- integer; the total number of lines

        EXAMPLES::

            sage: from sage.typeset.symbols import *
            sage: unicode_integral.print_to_stdout(1)
            ∫
            sage: unicode_integral.print_to_stdout(2)
            ⌠
            ⌡
            sage: unicode_integral.print_to_stdout(3)
            ⌠
            ⎮
            ⌡
            sage: unicode_integral.print_to_stdout(4)
            ⌠
            ⎮
            ⎮
            ⌡
        """

class CompoundAsciiSymbol(CompoundSymbol):
    def character_art(self, num_lines):
        """
        Return the ASCII art of the symbol.

        EXAMPLES::

            sage: from sage.typeset.symbols import *
            sage: ascii_left_curly_brace.character_art(3)
            {
            {
            {
        """

class CompoundUnicodeSymbol(CompoundSymbol):
    def character_art(self, num_lines):
        """
        Return the unicode art of the symbol.

        EXAMPLES::

            sage: from sage.typeset.symbols import *
            sage: unicode_left_curly_brace.character_art(3)
            ⎧
            ⎨
            ⎩
        """

ascii_integral: Incomplete
unicode_integral: Incomplete
ascii_left_parenthesis: Incomplete
ascii_right_parenthesis: Incomplete
unicode_left_parenthesis: Incomplete
unicode_right_parenthesis: Incomplete
ascii_left_square_bracket: Incomplete
ascii_right_square_bracket: Incomplete
unicode_left_square_bracket: Incomplete
unicode_right_square_bracket: Incomplete
ascii_left_curly_brace: Incomplete
ascii_right_curly_brace: Incomplete
unicode_left_curly_brace: Incomplete
unicode_right_curly_brace: Incomplete
