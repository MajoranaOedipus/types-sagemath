from _typeshed import Incomplete
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets as FiniteEnumeratedSets
from sage.combinat.combinat import CombinatorialElement as CombinatorialElement
from sage.combinat.words.paths import FiniteWordPath_north_east as FiniteWordPath_north_east, WordPaths_north_east as WordPaths_north_east
from sage.misc.latex import latex as latex
from sage.rings.integer import Integer as Integer
from sage.sets.recursively_enumerated_set import RecursivelyEnumeratedSet as RecursivelyEnumeratedSet
from sage.structure.element import Element as Element
from sage.structure.global_options import GlobalOptions as GlobalOptions
from sage.structure.parent import Parent as Parent

ndw_open_symbol: int
ndw_close_symbol: int

def update_ndw_symbols(os, cs) -> None:
    """
    A way to alter the open and close symbols from sage.

    INPUT:

    - ``os`` -- the open symbol
    - ``cs`` -- the close symbol

    EXAMPLES::

        sage: from sage.combinat.nu_dyck_word import update_ndw_symbols
        sage: update_ndw_symbols(0,1)
        sage: dw = NuDyckWord('0101001','0110010'); dw
        [0, 1, 0, 1, 0, 0, 1]

        sage: dw = NuDyckWord('1010110','1001101'); dw
        Traceback (most recent call last):
        ...
        ValueError: invalid nu-Dyck word
        sage: update_ndw_symbols(1,0)
    """
def replace_dyck_char(x):
    """
    A map sending an opening character (``'1'``, ``'N'``, and ``'('``) to
    ``ndw_open_symbol``, a closing character (``'0'``, ``'E'``, and ``')'``) to
    ``ndw_close_symbol``, and raising an error on any input other than one of
    the opening or closing characters.

    This is the inverse map of :func:`replace_dyck_symbol`.

    INPUT:

    - ``x`` -- string; a ``'1'``, ``'0'``, ``'N'``, ``'E'``, ``'('`` or ``')'``

    OUTPUT:

    - If ``x`` is an opening character, replace ``x`` with the
      constant ``ndw_open_symbol``.

    - If ``x`` is a closing character, replace ``x`` with the
      constant ``ndw_close_symbol``.

    - Raise a :exc:`ValueError` if ``x`` is neither an opening nor a
      closing character.

    .. SEEALSO:: :func:`replace_dyck_symbol`

    EXAMPLES::

        sage: from sage.combinat.nu_dyck_word import replace_dyck_char
        sage: replace_dyck_char('(')
        1
        sage: replace_dyck_char(')')
        0
        sage: replace_dyck_char(1)
        Traceback (most recent call last):
        ...
        ValueError
    """
def replace_dyck_symbol(x, open_char: str = 'N', close_char: str = 'E') -> str:
    """
    A map sending ``ndw_open_symbol`` to ``open_char`` and ``ndw_close_symbol``
    to ``close_char``, and raising an error on any input other than
    ``ndw_open_symbol`` and ``ndw_close_symbol``. The values of the constants
    ``ndw_open_symbol`` and ``ndw_close_symbol`` are subject to change.

    This is the inverse map of :func:`replace_dyck_char`.

    INPUT:

    - ``x`` -- either ``ndw_open_symbol`` or ``ndw_close_symbol``

    - ``open_char`` -- string (optional) default ``'N'``

    - ``close_char`` -- string (optional) default ``'E'``

    OUTPUT: if ``x`` is ``ndw_open_symbol``, replace ``x`` with ``open_char``

    - If ``x`` is ``ndw_close_symbol``, replace ``x`` with ``close_char``.

    - If ``x`` is neither ``ndw_open_symbol`` nor ``ndw_close_symbol``, a
      :exc:`ValueError` is raised.

    .. SEEALSO:: :func:`replace_dyck_char`

    EXAMPLES::

        sage: from sage.combinat.nu_dyck_word import replace_dyck_symbol
        sage: replace_dyck_symbol(1)
        'N'
        sage: replace_dyck_symbol(0)
        'E'
        sage: replace_dyck_symbol(3)
        Traceback (most recent call last):
        ...
        ValueError
    """

class NuDyckWord(CombinatorialElement):
    """
    A `\\nu`-Dyck word.

    Given a lattice path `\\nu` in the `\\ZZ^2` grid starting at the origin
    `(0,0)` consisting of North `N = (0,1)` and East `E = (1,0)` steps, a
    `\\nu`-Dyck path is a lattice path in the `\\ZZ^2` grid starting at the
    origin `(0,0)` and ending at the same coordinate as `\\nu` such that it is
    weakly above `\\nu`. A `\\nu`-Dyck word is the representation of a
    `\\nu`-Dyck path where a North step is represented by a 1 and an East step
    is represented by a 0.

    INPUT:

    - ``k1`` -- a path for the `\\nu`-Dyck word

    - ``k2`` -- a path for `\\nu`

    EXAMPLES::

        sage: dw = NuDyckWord([1,0,1,0],[1,0,0,1]); dw
        [1, 0, 1, 0]
        sage: print(dw)
        NENE
        sage: dw.height()
        2

        sage: dw = NuDyckWord('1010',[1,0,0,1]); dw
        [1, 0, 1, 0]

        sage: dw = NuDyckWord('NENE',[1,0,0,1]); dw
        [1, 0, 1, 0]

        sage: NuDyckWord([1,0,1,0],[1,0,0,1]).pretty_print()
           __
         _|x
        | . .

        sage: from sage.combinat.nu_dyck_word import update_ndw_symbols
        sage: update_ndw_symbols(0,1)
        sage: dw = NuDyckWord('0101001','0110010'); dw
        [0, 1, 0, 1, 0, 0, 1]
        sage: dw.pp()
             __
            |x
           _| .
         _|x  .
        | . . .
        sage: update_ndw_symbols(1,0)
    """
    @staticmethod
    def __classcall_private__(cls, dw=None, nu=None, **kwargs):
        """
        Return an element with the appropriate parent.

        EXAMPLES::

            sage: NuDyckWord('110100','101010')
            [1, 1, 0, 1, 0, 0]
            sage: NuDyckWord('010','010')
            [0, 1, 0]
        """
    def __init__(self, parent, dw, latex_options=None) -> None:
        """
        Initialize a nu-Dyck word.

        EXAMPLES::

            sage: NuDyckWord('010', '010')
            [0, 1, 0]
            sage: NuDyckWord('110100','101010')
            [1, 1, 0, 1, 0, 0]
        """
    def __eq__(self, other):
        """
        Return if two paths are equal.

        EXAMPLES::

            sage: u = NuDyckWord('010','010')
            sage: w = NuDyckWord('110100','101010')
            sage: w == w
            True
            sage: u == w
            False
            sage: u == 4
            False
        """
    def __neq__(self, other):
        """
        Return if two paths are not equal.

        EXAMPLES::

            sage: u = NuDyckWord('010','010')
            sage: w = NuDyckWord('110100','101010')
            sage: w != w
            False
            sage: u != w
            True
            sage: u != 4
            True
        """
    def __le__(self, other):
        """
        Return if one path is included in another.

        EXAMPLES::

            sage: ND1 = NuDyckWord('101', '011')
            sage: ND2 = NuDyckWord('110', '011')
            sage: ND3 = NuDyckWord('011', '011')
            sage: ND1 <= ND1
            True
            sage: ND1 <= ND2
            True
            sage: ND2 <= ND1
            False
            sage: ND3 <= ND2
            True
            sage: ND3 <= ND1
            True
        """
    def __lt__(self, other):
        """
        Return if one path is strictly included in another.

        EXAMPLES::

            sage: ND1 = NuDyckWord('101', '011')
            sage: ND2 = NuDyckWord('110', '011')
            sage: ND3 = NuDyckWord('011', '011')
            sage: ND1 < ND1
            False
            sage: ND1 < ND2
            True
            sage: ND2 < ND1
            False
            sage: ND3 < ND2
            True
            sage: ND3 < ND1
            True
        """
    def __ge__(self, other):
        """
        Return if one path is included in another.

        EXAMPLES::

            sage: ND1 = NuDyckWord('101', '011')
            sage: ND2 = NuDyckWord('110', '011')
            sage: ND3 = NuDyckWord('011', '011')
            sage: ND1 >= ND1
            True
            sage: ND1 >= ND2
            False
            sage: ND2 >= ND1
            True
            sage: ND1 >= ND3
            True
            sage: ND2 >= ND3
            True
        """
    def __gt__(self, other):
        """
        Return if one path is strictly included in another.

        EXAMPLES::

            sage: ND1 = NuDyckWord('101', '011')
            sage: ND2 = NuDyckWord('110', '011')
            sage: ND3 = NuDyckWord('011', '011')
            sage: ND1 > ND1
            False
            sage: ND1 > ND2
            False
            sage: ND2 > ND1
            True
            sage: ND1 > ND3
            True
            sage: ND2 > ND3
            True
        """
    def __hash__(self) -> int:
        """
        Return a hash for ``self``.

        EXAMPLES::

            sage: u = NuDyckWord('010','010')
            sage: hash(u)  # random
            -4577085166836515071
        """
    def set_latex_options(self, D) -> None:
        '''
        Set the latex options for use in the ``_latex_`` function.

        The default values are set in the ``__init__`` function.

        - ``color`` -- (default: black) the line color

        - ``line width`` -- (default: `2 \\times` ``tikz_scale``) value
          representing the line width

        - ``nu_options`` -- (default: ``\'rounded corners=1, color=red, line
          width=1\'``) string to indicate what the tikz options should be for
          path of `\\nu`

        - ``points_color`` -- (default: ``\'black\'``) str to indicate color
          points should be drawn with

        - ``show_grid`` -- boolean (default: ``True``); value to indicate if
          grid should be shown

        - ``show_nu`` -- boolean (default: ``True``); value to indicate if `\\nu`
          should be shown

        - ``show_points`` -- boolean (default: ``False``); value to indicate
          if points should be shown on path

        - ``tikz_scale`` -- (default: 1) scale for use with the tikz package

        INPUT:

        - ``D`` -- dictionary with a list of latex parameters to change

        EXAMPLES::

            sage: NDW = NuDyckWord(\'010\',\'010\')
            sage: NDW.set_latex_options({"tikz_scale":2})
            sage: NDW.set_latex_options({"color":"blue", "show_points":True})

        .. TODO::

            This should probably be merged into NuDyckWord.options.
        '''
    def latex_options(self) -> dict:
        """
        Return the latex options for use in the ``_latex_`` function as a
        dictionary.

        The default values are set using the options.

        - ``color`` -- (default: black) the line color

        - ``line width`` -- (default: 2*``tikz_scale``) value representing the
          line width

        - ``nu_options`` -- (default: ``'rounded corners=1, color=red, line
          width=1'``) string to indicate what the tikz options should be for
          path of `\\nu`

        - ``points_color`` -- (default: ``'black'``) str to indicate color
          points should be drawn with

        - ``show_grid`` -- boolean (default: ``True``); value to indicate if
          grid should be shown

        - ``show_nu`` -- boolean (default: ``True``); value to indicate if `\\nu`
          should be shown

        - ``show_points`` -- boolean (default: ``False``); value to indicate
          if points should be shown on path

        - ``tikz_scale`` -- (default: 1) scale for use with the tikz package

        EXAMPLES::

            sage: NDW = NuDyckWord('010','010')
            sage: NDW.latex_options()
            {'color': black,
             'line width': 2,
             'nu_options': rounded corners=1, color=red, line width=1,
             'points_color': black,
             'show_grid': True,
             'show_nu': True,
             'show_points': False,
             'tikz_scale': 1}

        .. TODO::

            This should probably be merged into NuDyckWord.options.
        """
    def pretty_print(self, style=None, labelling=None) -> None:
        '''
        Display a NuDyckWord as a lattice path in the `\\ZZ^2` grid.

        If the ``style`` is "N-E", then a cell below the diagonal is
        indicated by a period, whereas a cell below the path but above
        the diagonal is indicated by an x. If a list of labels is
        included, they are displayed along the vertical edges of the
        Dyck path.

        INPUT:

        - ``style`` -- (default: ``None``) can either be:

          - ``None`` to use the option default
          - "N-E" to show ``self`` as a path of north and east steps, or

        - ``labelling`` -- (if style is "N-E") a list of labels assigned to
          the up steps in ``self``

        - ``underpath`` -- (if style is "N-E", default: ``True``) if ``True``,
          an ``x`` to show the boxes between `\\nu` and the `\\nu`-Dyck Path

        EXAMPLES::

            sage: for ND in NuDyckWords(\'101010\'): ND.pretty_print()
                 __
               _| .
             _| . .
            | . . .
                 __
             ___| .
            |x  . .
            | . . .
               ____
              |x  .
             _| . .
            | . . .
               ____
             _|x  .
            |x  . .
            | . . .
             ______
            |x x  .
            |x  . .
            | . . .

        ::

            sage: nu = [1,0,1,0,1,0,1,0,1,0,1,0]
            sage: ND = NuDyckWord([1,1,1,0,1,0,0,1,1,0,0,0],nu)
            sage: ND.pretty_print()
                   ______
                  |x x  .
               ___|x  . .
             _|x x  . . .
            |x x  . . . .
            |x  . . . . .
            | . . . . . .

        ::

            sage: NuDyckWord([1,1,0,0,1,0],[1,0,1,0,1,0]).pretty_print(
            ....: labelling=[1,3,2])
                 __
             ___| . 2
            |x  . . 3
            | . . . 1

        ::

            sage: NuDyckWord(\'1101110011010010001101111000110000\',
            ....: \'1010101010101010101010101010101010\').pretty_print(
            ....: labelling=list(range(1,18)))
                                       ________
                                      |x x x  . 17
                                 _____|x x  . . 16
                                |x x x x  . . . 15
                                |x x x  . . . . 14
                                |x x  . . . . . 13
                               _|x  . . . . . . 12
                              |x  . . . . . . . 11
                         _____| . . . . . . . . 10
                     ___|x x  . . . . . . . . .  9
                   _|x x x  . . . . . . . . . .  8
                  |x x x  . . . . . . . . . . .  7
               ___|x x  . . . . . . . . . . . .  6
              |x x x  . . . . . . . . . . . . .  5
              |x x  . . . . . . . . . . . . . .  4
             _|x  . . . . . . . . . . . . . . .  3
            |x  . . . . . . . . . . . . . . . .  2
            | . . . . . . . . . . . . . . . . .  1


        ::

            sage: NuDyckWord().pretty_print()
            .
        '''
    pp = pretty_print
    def plot(self, **kwds):
        """
        Plot a `\\nu`-Dyck word as a continuous path.

        EXAMPLES::

            sage: NDW = NuDyckWord('010','010')
            sage: NDW.plot()                                                            # needs sage.plot
            Graphics object consisting of 1 graphics primitive
        """
    def path(self):
        """
        Return the underlying path object.

        EXAMPLES::

            sage: NDW = NuDyckWord('10011001000','00100101001')
            sage: NDW.path()
            Path: 10011001000
        """
    def height(self):
        """
        Return the height of ``self``.

        The height is the number of ``north`` steps.

        EXAMPLES::

            sage: NuDyckWord('1101110011010010001101111000110000',
            ....: '1010101010101010101010101010101010').height()
            17
        """
    def width(self):
        """
        Return the width of ``self``.

        The width is the number of ``east`` steps.

        EXAMPLES::

            sage: NuDyckWord('110111001101001000110111100011000',
            ....: '101010101010101010101010101010101').width()
            16
        """
    def length(self):
        """
        Return the length of ``self``.

        The length is the total number of steps.

        EXAMPLES::

            sage: NDW = NuDyckWord('10011001000','00100101001')
            sage: NDW.length()
            11
        """
    def points(self):
        """
        Return an iterator for the points on the `\\nu`-Dyck path.

        EXAMPLES::

            sage: list(NuDyckWord('110111001101001000110111100011000',
            ....: '101010101010101010101010101010101')._path.points())
            [(0, 0),
             (0, 1),
             (0, 2),
             (1, 2),
             (1, 3),
             (1, 4),
             (1, 5),
             (2, 5),
             (3, 5),
             (3, 6),
             (3, 7),
             (4, 7),
             (4, 8),
             (5, 8),
             (6, 8),
             (6, 9),
             (7, 9),
             (8, 9),
             (9, 9),
             (9, 10),
             (9, 11),
             (10, 11),
             (10, 12),
             (10, 13),
             (10, 14),
             (10, 15),
             (11, 15),
             (12, 15),
             (13, 15),
             (13, 16),
             (13, 17),
             (14, 17),
             (15, 17),
             (16, 17)]
        """
    def heights(self):
        """
        Return the heights of each point on ``self``.

        We view the Dyck word as a Dyck path from `(0,0)` to
        `(x,y)` in the first quadrant by letting ``1``'s represent
        steps in the direction `(0,1)` and ``0``'s represent steps in
        the direction `(1,0)`.

        The heights is the sequence of the `y`-coordinates of all
        `x+y` lattice points along the path.

        EXAMPLES::

            sage: NuDyckWord('010','010').heights()
            [0, 0, 1, 1]
            sage: NuDyckWord('110100','101010').heights()
            [0, 1, 2, 2, 3, 3, 3]
        """
    def widths(self):
        """
        Return the widths of each point on ``self``.

        We view the Dyck word as a Dyck path from `(0,0)` to
        `(x,y)` in the first quadrant by letting ``1``'s represent
        steps in the direction `(0,1)` and ``0``'s represent steps in
        the direction `(1,0)`.

        The widths is the sequence of the `x`-coordinates of all
        `x+y` lattice points along the path.

        EXAMPLES::

            sage: NuDyckWord('010','010').widths()
            [0, 1, 1, 2]
            sage: NuDyckWord('110100','101010').widths()
            [0, 0, 0, 1, 1, 2, 3]
        """
    def horizontal_distance(self):
        """
        Return a list of how far each point is from `\\nu`.

        EXAMPLES::

            sage: NDW = NuDyckWord('10010100','00000111')
            sage: NDW.horizontal_distance()
            [5, 5, 4, 3, 3, 2, 2, 1, 0]
            sage: NDW = NuDyckWord('10010100','00001011')
            sage: NDW.horizontal_distance()
            [4, 5, 4, 3, 3, 2, 2, 1, 0]
            sage: NDW = NuDyckWord('10011001000','00100101001')
            sage: NDW.horizontal_distance()
            [2, 4, 3, 2, 3, 5, 4, 3, 3, 2, 1, 0]
        """
    def can_mutate(self, i) -> bool | int:
        """
        Return True/False based off if mutable at height `i`.

        Can only mutate if an east step is followed by a north step at height
        `i`.

        OUTPUT: whether we can mutate at height of `i`

        EXAMPLES::

            sage: NDW = NuDyckWord('10010100','00000111')
            sage: NDW.can_mutate(1)
            False
            sage: NDW.can_mutate(3)
            5

        TESTS::

            sage: NDW = NuDyckWord('10010100','00000111')
            sage: NDW.can_mutate(33)
            Traceback (most recent call last):
            ...
            ValueError: cannot mutate above or below path
        """
    def mutate(self, i) -> None | NuDyckWord:
        """
        Return a new `\\nu`-Dyck Word if possible.

        If at height `i` we have an east step E meeting a north step N then we
        calculate all horizontal distances from this point until we find
        the first point that has the same horizontal distance to `\\nu`. We let

        - d is everything up until EN (not including EN)

        - f be everything between N and the point with the same horizontal
          distance (including N)

        - g is everything after f

        .. SEEALSO:: :meth:`can_mutate`

        EXAMPLES::

            sage: NDW = NuDyckWord('10010100','00000111')
            sage: NDW.mutate(1)
            sage: NDW.mutate(3)
            [1, 0, 0, 1, 1, 0, 0, 0]
        """

class NuDyckWords(Parent):
    """
    `\\nu`-Dyck words.

    Given a lattice path `\\nu` in the `\\ZZ^2` grid starting at the origin
    `(0,0)` consisting of North `N = (0,1)` and East `E = (1,0)` steps, a
    `\\nu`-Dyck path is a lattice path in the`\\ZZ^2` grid starting at the
    origin `(0,0)` and ending at the same coordinate as `\\nu` such that it is
    weakly above `\\nu`. A `\\nu`-Dyck word is the representation of a
    `\\nu`-Dyck path where a North step is represented by a 1 and an East step
    is represented by a 0.

    INPUT:

    - ``nu`` -- the base lattice path

    EXAMPLES::

        sage: NDW = NuDyckWords('1010'); NDW
        [1, 0, 1, 0] Dyck words
        sage: [1,0,1,0] in NDW
        True
        sage: [1,1,0,0] in NDW
        True
        sage: [1,0,0,1] in NDW
        False
        sage: [0,1,0,1] in NDW
        False
        sage: NDW.cardinality()
        2
    """
    Element = NuDyckWord
    def __init__(self, nu=()) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: TestSuite(NuDyckWords(nu=[1,0,1])).run()
        """
    class options(GlobalOptions):
        """
        Set and display the options for `\\nu`-Dyck words. If no parameters
        are set, then the function returns a copy of the options dictionary.

        The ``options`` to `\\nu`-Dyck words can be accessed as the method
        :meth:`NuDyckWords.options` of :class:`NuDyckWords` and
        related parent classes.

        @OPTIONS

        EXAMPLES::

            sage: ND = NuDyckWords('101')
            sage: ND
            [1, 0, 1] Dyck words
            sage: ND.options
            Current options for NuDyckWords
              - ascii_art:               pretty_output
              - diagram_style:           grid
              - display:                 list
              - latex_color:             black
              - latex_line_width_scalar: 2
              - latex_nu_options:        rounded corners=1, color=red, line width=1
              - latex_points_color:      black
              - latex_show_grid:         True
              - latex_show_nu:           True
              - latex_show_points:       False
              - latex_tikz_scale:        1
        """
        NAME: str
        module: str
        display: Incomplete
        ascii_art: Incomplete
        diagram_style: Incomplete
        latex_tikz_scale: Incomplete
        latex_line_width_scalar: Incomplete
        latex_color: Incomplete
        latex_show_points: Incomplete
        latex_points_color: Incomplete
        latex_show_grid: Incomplete
        latex_show_nu: Incomplete
        latex_nu_options: Incomplete
    def __contains__(self, x) -> bool:
        """
        Check for containment.

        TESTS::

            sage: NDW = NuDyckWords([1,0,1,1])
            sage: [1,1,0,1] in NDW
            True
            sage: [1,0,1,1] in NDW
            True
            sage: [0] in NDW
            False
            sage: [1, 0] in NDW
            False
        """
    def __eq__(self, other):
        """
        Return equality.

        TESTS::

            sage: A = NuDyckWords([1,0,1,1])
            sage: B = NuDyckWords([1,0,1,1])
            sage: C = NuDyckWords([1,0,1,1,1])
            sage: A == B
            True
            sage: A == C
            False
        """
    def __neq__(self, other):
        """
        Return inequality.

        TESTS::

            sage: A = NuDyckWords([1,0,1,1])
            sage: B = NuDyckWords([1,0,1,1])
            sage: C = NuDyckWords([1,0,1,1,1])
            sage: A != B
            False
            sage: A != C
            True
        """
    def __iter__(self, N=[], D=[], i=None, X=None):
        """
        Iterate over ``self``.

        The iterator interchanges a 0,1 pair whenever the 0 comes before a 1

        EXAMPLES::

            sage: it = NuDyckWords('101010').__iter__()
            sage: [i for i in it]
            [[1, 0, 1, 0, 1, 0],
             [1, 1, 0, 0, 1, 0],
             [1, 0, 1, 1, 0, 0],
             [1, 1, 0, 1, 0, 0],
             [1, 1, 1, 0, 0, 0]]
        """
    def cardinality(self):
        """
        Return the number of `\\nu`-Dyck words.

        EXAMPLES::

            sage: NDW = NuDyckWords('101010'); NDW.cardinality()
            5
            sage: NDW = NuDyckWords('1010010'); NDW.cardinality()
            7
            sage: NDW = NuDyckWords('100100100'); NDW.cardinality()
            12
        """

def to_word_path(word):
    """
    Convert input into a word path over an appropriate alphabet.

    Helper function.

    INPUT:

    - ``word`` -- word to convert to wordpath

    OUTPUT: a ``FiniteWordPath_north_east`` object

    EXAMPLES::

        sage: from sage.combinat.nu_dyck_word import to_word_path
        sage: wp = to_word_path('NEENENEN'); wp
        Path: 10010101
        sage: from sage.combinat.words.paths import FiniteWordPath_north_east
        sage: isinstance(wp,FiniteWordPath_north_east)
        True
        sage: to_word_path('1001')
        Path: 1001
        sage: to_word_path([0,1,0,0,1,0])
        Path: 010010
    """
def path_weakly_above_other(path, other) -> bool:
    """
    Test if ``path`` is weakly above ``other``.

    A path `P` is wealy above another path `Q` if `P` and `Q` are the same
    length and if any prefix of length `n` of `Q` contains more North steps
    than the prefix of length `n` of `P`.

    INPUT:

    - ``path`` -- the path to verify is weakly above the other path

    - ``other`` -- the other path to verify is weakly below the path

    OUTPUT: boolean

    EXAMPLES::

        sage: from sage.combinat.nu_dyck_word import path_weakly_above_other
        sage: path_weakly_above_other('1001','0110')
        False
        sage: path_weakly_above_other('1001','0101')
        True
        sage: path_weakly_above_other('1111','0101')
        False
        sage: path_weakly_above_other('111100','0101')
        False
    """
