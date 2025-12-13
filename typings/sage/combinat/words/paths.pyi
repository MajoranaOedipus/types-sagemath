from .word_datatypes import WordDatatype_list as WordDatatype_list, WordDatatype_str as WordDatatype_str, WordDatatype_tuple as WordDatatype_tuple
from .word_infinite_datatypes import WordDatatype_callable as WordDatatype_callable, WordDatatype_callable_with_caching as WordDatatype_callable_with_caching, WordDatatype_iter as WordDatatype_iter, WordDatatype_iter_with_caching as WordDatatype_iter_with_caching
from _typeshed import Incomplete
from collections.abc import Generator
from sage.combinat.words.alphabet import build_alphabet as build_alphabet
from sage.combinat.words.word import FiniteWord_class as FiniteWord_class
from sage.combinat.words.words import FiniteWords as FiniteWords
from sage.matrix.constructor import vector_on_axis_rotation_matrix as vector_on_axis_rotation_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.real_mpfr import RR as RR
from sage.structure.sage_object import SageObject as SageObject

def WordPaths(alphabet, steps=None):
    """
    Return the combinatorial class of paths of the given type of steps.

    INPUT:

    - ``alphabet`` -- ordered alphabet

    - ``steps`` -- (default: ``None``) it can be one of the following:

      - an iterable ordered container of as many vectors as there are
        letters in the alphabet. The vectors are associated to the letters
        according to their order in steps. The vectors can be a tuple or
        anything that can be passed to vector function.

      - an iterable ordered container of k vectors where k is half the
        size of alphabet. The vectors and their opposites are associated
        to the letters according to their order in steps (given vectors
        first, opposite vectors after).

      - ``None`` -- in this case, the type of steps are guessed from the
        length of alphabet

      - ``'square_grid'`` or ``'square'`` -- (default when size of alphabet is 4)
        The order is : East, North, West, South.

      - ``'triangle_grid'`` or ``'triangle'``

      - ``'hexagonal_grid'`` or ``'hexagon'`` -- (default when size of alphabet is 6)

      - ``'cube_grid'`` or ``'cube'``

      - ``'north_east'``, ``'ne'`` or ``'NE'`` -- (the default when size of alphabet is 2)

      - ``'dyck'``

    OUTPUT: the combinatorial class of all paths of the given type

    EXAMPLES:

    The steps can be given explicitly::

        sage: WordPaths('abc', steps=[(1,2), (-1,4), (0,-3)])
        Word Paths over 3 steps

    Different type of input alphabet::

        sage: WordPaths(range(3), steps=[(1,2), (-1,4), (0,-3)])
        Word Paths over 3 steps
        sage: WordPaths(['cric','crac','croc'], steps=[(1,2), (1,4), (0,3)])
        Word Paths over 3 steps

    Directions can be in three dimensions as well::

        sage: WordPaths('ab', steps=[(1,2,2),(-1,4,2)])
        Word Paths over 2 steps

    When the number of given steps is half the size of alphabet, the
    opposite of vectors are used::

        sage: P = WordPaths('abcd', [(1,0), (0,1)])
        sage: P
        Word Paths over 4 steps
        sage: sorted(P.letters_to_steps().items())
        [('a', (1, 0)), ('b', (0, 1)), ('c', (-1, 0)), ('d', (0, -1))]

    When no steps are given, default classes are returned::

        sage: WordPaths('ab')
        Word Paths in North and East steps
        sage: WordPaths(range(4))
        Word Paths on the square grid
        sage: WordPaths(range(6))
        Word Paths on the hexagonal grid

    There are many type of built-in steps...

    On a two letters alphabet::

        sage: WordPaths('ab', steps='north_east')
        Word Paths in North and East steps
        sage: WordPaths('()', steps='dyck')
        Finite Dyck paths

    On a four letters alphabet::

        sage: WordPaths('ruld', steps='square_grid')
        Word Paths on the square grid

    On a six letters alphabet::

        sage: WordPaths('abcdef', steps='hexagonal_grid')
        Word Paths on the hexagonal grid
        sage: WordPaths('abcdef', steps='triangle_grid')
        Word Paths on the triangle grid
        sage: WordPaths('abcdef', steps='cube_grid')
        Word Paths on the cube grid

    TESTS::

        sage: WordPaths(range(5))
        Traceback (most recent call last):
        ...
        TypeError: Unable to make a class WordPaths from {0, 1, 2, 3, 4}
        sage: WordPaths('abAB', steps='square_gridd')
        Traceback (most recent call last):
        ...
        TypeError: Unknown type of steps : square_gridd
    """

class WordPaths_all(FiniteWords):
    """
    The combinatorial class of all paths, i.e of all words over
    an alphabet where each letter is mapped to a step (a vector).
    """
    def __init__(self, alphabet, steps) -> None:
        """
        INPUT:

        - ``alphabet`` -- an ordered alphabet

        - ``steps`` -- an iterable (of same length as alphabet or half the
          length of alphabet) of ordered vectors

        EXAMPLES::

            sage: from sage.combinat.words.paths import WordPaths_all
            sage: d = ((1,1), (-1,1), (1,-1), (-1,-1))
            sage: P = WordPaths_all('abAB', d); P
            Word Paths over 4 steps
            sage: P == loads(dumps(P))
            True

        If size of alphabet is twice the number of steps, then opposite
        vectors are used for the second part of the alphabet::

            sage: WordPaths('abcd',[(2,1),(2,4)])
            Word Paths over 4 steps
            sage: _.letters_to_steps()
            {'a': (2, 1), 'b': (2, 4), 'c': (-2, -1), 'd': (-2, -4)}

        TESTS::

            sage: from sage.combinat.words.paths import WordPaths_all
            sage: d = ((1,1), (-1,1), (1,-1), (-1,-1))
            sage: WordPaths_all('abA', d)
            Traceback (most recent call last):
            ...
            TypeError: size of steps (=4) must equal the size of alphabet (=3) or half the size of alphabet

            sage: d = ((1,1), 1)
            sage: WordPaths_all('ab', d)
            Traceback (most recent call last):
            ...
            ValueError: cannot make vectors from steps

            sage: d = ((1,1), (-1,1,0))
            sage: WordPaths_all('ab', d)
            Traceback (most recent call last):
            ...
            ValueError: cannot make summable vectors from steps
        """
    def __eq__(self, other):
        """
        TESTS::

            sage: W1 = WordPaths(['a','b'], [vector((0,1)), vector((0,2))])
            sage: W2 = WordPaths(['a','b'], [vector((0,1)), vector((0,2))])
            sage: W3 = WordPaths(['a','b'], [vector((0,2)), vector((1,0))])
            sage: W1 == W2
            True
            sage: W1 == W3
            False
        """
    def __ne__(self, other):
        """
        TESTS::

            sage: W1 = WordPaths(['a','b'], [vector((0,1)), vector((0,2))])
            sage: W2 = WordPaths(['a','b'], [vector((0,1)), vector((0,2))])
            sage: W3 = WordPaths(['a','b'], [vector((0,2)), vector((1,0))])
            sage: W1 != W2
            False
            sage: W1 != W3
            True
        """
    def letters_to_steps(self) -> dict:
        """
        Return the dictionary mapping letters to vectors (steps).

        EXAMPLES::

            sage: d = WordPaths('ab').letters_to_steps()
            sage: sorted(d.items())
            [('a', (0, 1)), ('b', (1, 0))]
            sage: d = WordPaths('abcd').letters_to_steps()
            sage: sorted(d.items())
            [('a', (1, 0)), ('b', (0, 1)), ('c', (-1, 0)), ('d', (0, -1))]
            sage: d = WordPaths('abcdef').letters_to_steps()
            sage: sorted(d.items())
            [('a', (1, 0)),
             ('b', (1/2, 1/2*sqrt3)),
             ('c', (-1/2, 1/2*sqrt3)),
             ('d', (-1, 0)),
             ('e', (-1/2, -1/2*sqrt3)),
             ('f', (1/2, -1/2*sqrt3))]
        """
    def vector_space(self):
        """
        Return the vector space over which the steps of the paths are defined.

        EXAMPLES::

            sage: WordPaths('ab',steps='dyck').vector_space()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: WordPaths('ab',steps='north_east').vector_space()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: WordPaths('abcd',steps='square_grid').vector_space()
            Ambient free module of rank 2 over the principal ideal domain Integer Ring
            sage: WordPaths('abcdef',steps='hexagonal_grid').vector_space()
            Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3 with sqrt3 = 1.732050807568878?
            sage: WordPaths('abcdef',steps='cube_grid').vector_space()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: WordPaths('abcdef',steps='triangle_grid').vector_space()
            Vector space of dimension 2 over Number Field in sqrt3 with defining polynomial x^2 - 3 with sqrt3 = 1.732050807568878?
        """

class WordPaths_square_grid(WordPaths_all):
    """
    The combinatorial class of all paths on the square grid.
    """
    def __init__(self, alphabet) -> None:
        """
        The combinatorial class of all finite paths on the square grid.

        INPUT:

        - ``alphabet`` -- ordered alphabet of length 4; the order for the steps
          is : East, North, West, South

        EXAMPLES::

            sage: from sage.combinat.words.paths import WordPaths_square_grid
            sage: P = WordPaths_square_grid('abAB'); P
            Word Paths on the square grid
            sage: P == loads(dumps(P))
            True
        """

class WordPaths_triangle_grid(WordPaths_all):
    """
    The combinatorial class of all paths on the triangle grid.
    """
    def __init__(self, alphabet) -> None:
        """
        The combinatorial class of all finite paths on the triangle grid.

        INPUT:

        - ``alphabet`` -- ordered alphabet of length 6. The order for the steps
          is : Right, Up-Right, Up-Left, Left, Down-Left, Down-Right.

        EXAMPLES::

            sage: from sage.combinat.words.paths import WordPaths_triangle_grid
            sage: P = WordPaths_triangle_grid('abcdef'); P
            Word Paths on the triangle grid
            sage: P == loads(dumps(P))
            True
        """

class WordPaths_hexagonal_grid(WordPaths_triangle_grid):
    """
    The combinatorial class of all paths on the hexagonal grid.
    """
    def __init__(self, alphabet) -> None:
        """
        The combinatorial class of all finite paths on the hexagonal grid.

        INPUT:

        - ``alphabet`` -- ordered alphabet of length 6. The order for the steps
          is : Right, Up-Right, Up-Left, Left, Down-Left, Down-Right.

        EXAMPLES::

            sage: from sage.combinat.words.paths import WordPaths_hexagonal_grid
            sage: P = WordPaths_hexagonal_grid('abcdef'); P
            Word Paths on the hexagonal grid
            sage: P == loads(dumps(P))
            True
        """

class WordPaths_cube_grid(WordPaths_all):
    """
    The combinatorial class of all paths on the cube grid.
    """
    def __init__(self, alphabet) -> None:
        """
        The combinatorial class of all finite paths on the cube grid.

        INPUT:

        - ``alphabet`` -- ordered alphabet of length 6. The order for
          the steps is `e_x, e_y, e_z, -e_x, -e_y, -e_z`, where `e_v`
          denotes the canonical basis.

        EXAMPLES::

            sage: from sage.combinat.words.paths import WordPaths_cube_grid
            sage: P = WordPaths_cube_grid('abcABC'); P
            Word Paths on the cube grid
            sage: P == loads(dumps(P))
            True
        """

class WordPaths_dyck(WordPaths_all):
    """
    The combinatorial class of all Dyck paths.
    """
    def __init__(self, alphabet) -> None:
        """
        The combinatorial class of all finite Dyck paths.

        INPUT:

        - ``alphabet`` -- ordered alphabet of length 2. The order for the steps
          is : (1,1), (1,-1)

        EXAMPLES::

            sage: from sage.combinat.words.paths import WordPaths_dyck
            sage: P = WordPaths_dyck('[]'); P
            Finite Dyck paths
            sage: P == loads(dumps(P))
            True
        """

class WordPaths_north_east(WordPaths_all):
    """
    The combinatorial class of all paths using North and East directions.
    """
    def __init__(self, alphabet) -> None:
        """
        The combinatorial class of all finite paths using only north and east
        steps on the square grid.

        INPUT:

        - ``alphabet`` -- ordered alphabet of length 2. The order for the steps
          is North, East

        EXAMPLES::

            sage: from sage.combinat.words.paths import WordPaths_north_east
            sage: P = WordPaths_north_east('ab'); P
            Word Paths in North and East steps
            sage: P == loads(dumps(P))
            True
        """

class FiniteWordPath_all(SageObject):
    def points(self, include_last: bool = True) -> Generator[Incomplete]:
        """
        Return an iterator yielding a list of points used to draw the path
        represented by this word.

        INPUT:

        - ``include_last`` -- boolean (default: ``True``); whether to include the
          last point

        EXAMPLES:

        A simple closed square::

            sage: P = WordPaths('abAB')
            sage: list(P('abAB').points())
            [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]

        A simple closed square without the last point::

            sage: list(P('abAB').points(include_last=False))
            [(0, 0), (1, 0), (1, 1), (0, 1)]

        ::

            sage: list(P('abaB').points())
            [(0, 0), (1, 0), (1, 1), (2, 1), (2, 0)]
        """
    def start_point(self):
        """
        Return the starting point of ``self``.

        OUTPUT: vector

        EXAMPLES::

            sage: WordPaths('abcdef')('abcdef').start_point()
            (0, 0)
            sage: WordPaths('abcdef', steps='cube_grid')('abcdef').start_point()
            (0, 0, 0)
            sage: P = WordPaths('ab', steps=[(1,0,0,0),(0,1,0,0)])
            sage: P('abbba').start_point()
            (0, 0, 0, 0)
        """
    @cached_method
    def end_point(self):
        """
        Return the end point of the path.

        EXAMPLES::

            sage: WordPaths('abcdef')('abababab').end_point()
            (6, 2*sqrt3)
            sage: WordPaths('abAB')('abababab').end_point()
            (4, 4)
            sage: P = WordPaths('abcABC', steps='cube_grid')
            sage: P('ababababCC').end_point()
            (4, 4, -2)
            sage: WordPaths('abcdef')('abcdef').end_point()
            (0, 0)
            sage: P = WordPaths('abc', steps=[(1,3,7,9),(-4,1,0,0),(0,32,1,8)])
            sage: P('abcabababacaacccbbcac').end_point()
            (-16, 254, 63, 128)
        """
    def directive_vector(self):
        """
        Return the directive vector of ``self``.

        The directive vector is the vector starting at the start point
        and ending at the end point of the path ``self``.

        EXAMPLES::

            sage: WordPaths('abcdef')('abababab').directive_vector()
            (6, 2*sqrt3)
            sage: WordPaths('abAB')('abababab').directive_vector()
            (4, 4)
            sage: P = WordPaths('abcABC', steps='cube_grid')
            sage: P('ababababCC').directive_vector()
            (4, 4, -2)
            sage: WordPaths('abcdef')('abcdef').directive_vector()
            (0, 0)
            sage: P = WordPaths('abc', steps=[(1,3,7,9),(-4,1,0,0),(0,32,1,8)])
            sage: P('abcabababacaacccbbcac').directive_vector()
            (-16, 254, 63, 128)
        """
    def is_closed(self) -> bool:
        """
        Return ``True`` if the path is closed.

        A path is closed if the origin and the end of
        the path are equal.

        EXAMPLES::

            sage: P = WordPaths('abcd', steps=[(1,0),(0,1),(-1,0),(0,-1)])
            sage: P('abcd').is_closed()
            True
            sage: P('abc').is_closed()
            False
            sage: P().is_closed()
            True
            sage: P('aacacc').is_closed()
            True
        """
    def is_simple(self) -> bool:
        """
        Return ``True`` if the path is simple.

        A path is simple if all its points are
        distinct.

        If the path is closed, the last point is not considered.

        EXAMPLES::

            sage: P = WordPaths('abcdef',steps='triangle_grid');P
            Word Paths on the triangle grid
            sage: P('abc').is_simple()
            True
            sage: P('abcde').is_simple()
            True
            sage: P('abcdef').is_simple()
            True
            sage: P('ad').is_simple()
            True
            sage: P('aabdee').is_simple()
            False
        """
    def tikz_trajectory(self) -> str:
        """
        Return the trajectory of ``self`` as a ``tikz`` string.

        EXAMPLES::

            sage: P = WordPaths('abcdef')
            sage: p = P('abcde')
            sage: p.tikz_trajectory()
            '(0.000, 0.000) -- (1.00, 0.000) -- (1.50, 0.866) -- (1.00, 1.73) -- (0.000, 1.73) -- (-0.500, 0.866)'
        """
    def projected_point_iterator(self, v=None, ring=None) -> Generator[Incomplete]:
        """
        Return an iterator of the projection of the orbit points of the
        path into the space orthogonal to the given vector.

        INPUT:

        - ``v`` -- vector (default: ``None``); if ``None``, the directive
          vector (i.e. the end point minus starting point) of the path is
          considered

        - ``ring`` -- ring (default: ``None``); where to do the
          computations. If ``None``, RealField(53) is used.

        OUTPUT: iterator of points

        EXAMPLES:

        Projected points of the Rauzy fractal::

            sage: s = WordMorphism('1->12,2->13,3->1')
            sage: D = s.fixed_point('1')
            sage: v = s.pisot_eigenvector_right()
            sage: P = WordPaths('123',[(1,0,0),(0,1,0),(0,0,1)])
            sage: w = P(D[:200])
            sage: it = w.projected_point_iterator(v)
            sage: for i in range(6): next(it)
            (0.000000000000000, 0.000000000000000)
            (-0.526233343362516, 0.000000000000000)
            (0.220830337618112, -0.477656250512816)
            (-0.305403005744404, -0.477656250512816)
            (0.100767309386062, 0.400890564600664)
            (-0.425466033976454, 0.400890564600664)

        Projected points of a 2d path::

            sage: P = WordPaths('ab','ne')
            sage: p = P('aabbabbab')
            sage: it = p.projected_point_iterator(ring=RealField(20))
            sage: for i in range(8): next(it)
            (0.00000)
            (0.78087)
            (1.5617)
            (0.93704)
            (0.31235)
            (1.0932)
            (0.46852)
            (-0.15617)
        """
    def plot_projection(self, v=None, letters=None, color=None, ring=None, size: int = 12, kind: str = 'right'):
        """
        Return an image of the projection of the successive points of the
        path into the space orthogonal to the given vector.

        INPUT:

        - ``self`` -- a word path in a 3 or 4 dimension vector space

        - ``v`` -- vector (default: ``None``); if ``None``, the directive
          vector (i.e. the end point minus starting point) of the path is
          considered.

        - ``letters`` -- iterable (default: ``None``); of the letters
          to be projected. If ``None``, then all the letters are considered.

        - ``color`` -- dictionary (default: ``None``); of the letters
          mapped to colors. If ``None``, automatic colors are chosen.

        - ``ring`` -- ring (default: ``None``); where to do the
          computations. If ``None``, RealField(53) is used.

        - ``size`` -- number (default: ``12``); size of the points

        - ``kind`` -- string (default: ``'right'``); either
          ``'right'`` or ``'left'``. The color of a letter is given to the
          projected prefix to the right or the left of the letter.

        OUTPUT: 2d or 3d Graphic object

        EXAMPLES:

        The Rauzy fractal::

            sage: s = WordMorphism('1->12,2->13,3->1')
            sage: D = s.fixed_point('1')
            sage: v = s.pisot_eigenvector_right()
            sage: P = WordPaths('123',[(1,0,0),(0,1,0),(0,0,1)])
            sage: w = P(D[:200])
            sage: w.plot_projection(v)  # long time (2s)
            Graphics object consisting of 200 graphics primitives

        In this case, the abelianized vector doesn't give a good
        projection::

            sage: w.plot_projection()  # long time (2s)
            Graphics object consisting of 200 graphics primitives

        You can project only the letters you want::

            sage: w.plot_projection(v, letters='12')  # long time (2s)
            Graphics object consisting of 168 graphics primitives

        You can increase or decrease the precision of the computations by
        changing the ring of the projection matrix::

            sage: w.plot_projection(v, ring=RealField(20))  # long time (2s)
            Graphics object consisting of 200 graphics primitives

        You can change the size of the points::

            sage: w.plot_projection(v, size=30)  # long time (2s)
            Graphics object consisting of 200 graphics primitives

        You can assign the color of a letter to the projected prefix to the
        right or the left of the letter::

            sage: w.plot_projection(v, kind='left')  # long time (2s)
            Graphics object consisting of 200 graphics primitives

        To remove the axis, do like this::

            sage: r = w.plot_projection(v)                                              # needs sage.plot
            sage: r.axes(False)                                                         # needs sage.plot
            sage: r                             # long time (2s)                        # needs sage.plot
            Graphics object consisting of 200 graphics primitives

        You can assign different colors to each letter::

            sage: color = {'1': 'purple', '2': (.2,.3,.4), '3': 'magenta'}
            sage: w.plot_projection(v, color=color)     # long time (2s)                # needs sage.plot
            Graphics object consisting of 200 graphics primitives

        The 3d-Rauzy fractal::

            sage: s = WordMorphism('1->12,2->13,3->14,4->1')
            sage: D = s.fixed_point('1')
            sage: v = s.pisot_eigenvector_right()
            sage: P = WordPaths('1234',[(1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1)])
            sage: w = P(D[:200])
            sage: w.plot_projection(v)                                                  # needs sage.plot
            Graphics3d Object

        The dimension of vector space of the parent must be 3 or 4::

            sage: P = WordPaths('ab', [(1, 0), (0, 1)])
            sage: p = P('aabbabbab')
            sage: p.plot_projection()                                                   # needs sage.plot
            Traceback (most recent call last):
            ...
            TypeError: The dimension of the vector space (=2) must be 3 or 4
        """
    def projected_path(self, v=None, ring=None):
        """
        Return the path projected into the space orthogonal to the given
        vector.

        INPUT:

        - ``v`` -- vector (default: ``None``); if ``None``, the directive
          vector (i.e. the end point minus starting point) of the path is
          considered.

        - ``ring`` -- ring (default: ``None``); where to do the
          computations. If ``None``, RealField(53) is used.

        OUTPUT: word path

        EXAMPLES:

        The projected path of the tribonacci word::

            sage: s = WordMorphism('1->12,2->13,3->1')
            sage: D = s.fixed_point('1')
            sage: v = s.pisot_eigenvector_right()
            sage: P = WordPaths('123',[(1,0,0),(0,1,0),(0,0,1)])
            sage: w = P(D[:1000])
            sage: p = w.projected_path(v)
            sage: p
            Path: 1213121121312121312112131213121121312121...
            sage: p[:20].plot()                                                         # needs sage.plot
            Graphics object consisting of 3 graphics primitives

        The ``ring`` argument allows to change the precision of the
        projected steps::

            sage: p = w.projected_path(v, RealField(10))
            sage: p
            Path: 1213121121312121312112131213121121312121...
            sage: p.parent().letters_to_steps()
            {'1': (-0.53, 0.00), '2': (0.75, -0.48), '3': (0.41, 0.88)}
        """
    def is_tangent(self) -> None:
        """
        The is_tangent() method, which is implemented for words, has
        an extended meaning for word paths, which is not implemented yet.

        TESTS::

            sage: WordPaths('ab')('abbab').is_tangent()
            Traceback (most recent call last):
            ...
            NotImplementedError

        AUTHOR:

        -   Thierry Monteil
        """

class FiniteWordPath_2d(FiniteWordPath_all):
    def plot(self, pathoptions={'rgbcolor': 'red', 'thickness': 3}, fill: bool = True, filloptions={'rgbcolor': 'red', 'alpha': 0.2}, startpoint: bool = True, startoptions={'rgbcolor': 'red', 'pointsize': 100}, endarrow: bool = True, arrowoptions={'rgbcolor': 'red', 'arrowsize': 20, 'width': 3}, gridlines: bool = False, gridoptions={}):
        """
        Return a 2d Graphics illustrating the path.

        INPUT:

        - ``pathoptions`` -- (dict,
          default:dict(rgbcolor='red',thickness=3)), options for the
          path drawing

        - ``fill`` -- boolean (default: ``True``); if fill is ``True`` and if
          the path is closed, the inside is colored

        - ``filloptions`` -- (dict,
          default:dict(rgbcolor='red',alpha=0.2)), options for the
          inside filling

        - ``startpoint`` -- boolean (default: ``True``); draw the start point?

        - ``startoptions`` -- (dict,
          default:dict(rgbcolor='red',pointsize=100)) options for the
          start point drawing

        - ``endarrow`` -- boolean (default: ``True``); draw an arrow end at the end?

        - ``arrowoptions`` -- (dict,
          default:dict(rgbcolor='red',arrowsize=20, width=3)) options
          for the end point arrow

        - ``gridlines`` -- boolean (default: ``False``); show gridlines?

        - ``gridoptions`` -- (dict, default: {}), options for the gridlines

        EXAMPLES:

        A non closed path on the square grid::

            sage: P = WordPaths('abAB')
            sage: P('abababAABAB').plot()                                               # needs sage.plot
            Graphics object consisting of 3 graphics primitives

        A closed path on the square grid::

            sage: P('abababAABABB').plot()                                              # needs sage.plot
            Graphics object consisting of 4 graphics primitives

        A Dyck path::

            sage: P = WordPaths('()', steps='dyck')
            sage: P('()()()((()))').plot()                                              # needs sage.plot
            Graphics object consisting of 3 graphics primitives

        A path in the triangle grid::

            sage: P = WordPaths('abcdef', steps='triangle_grid')
            sage: P('abcdedededefab').plot()                                            # needs sage.plot
            Graphics object consisting of 3 graphics primitives

        A polygon of length 220 that tiles the plane in two ways::

            sage: P = WordPaths('abAB')
            sage: P('aBababAbabaBaBABaBabaBaBABAbABABaBabaBaBABaBababAbabaBaBABaBabaBaBABAbABABaBABAbAbabAbABABaBABAbABABaBabaBaBABAbABABaBABAbAbabAbABAbAbabaBababAbABAbAbabAbABABaBABAbAbabAbABAbAbabaBababAbabaBaBABaBababAbabaBababAbABAbAbab').plot()  # needs sage.plot
            Graphics object consisting of 4 graphics primitives

        With gridlines::

            sage: P('ababababab').plot(gridlines=True)                                  # needs sage.plot

        TESTS::

            sage: P = WordPaths('abAB')
            sage: P().plot()                                                            # needs sage.plot
            Graphics object consisting of 3 graphics primitives
            sage: sum(map(plot,map(P,['a','A','b','B'])))                               # needs sage.plot
            Graphics object consisting of 12 graphics primitives
        """
    def animate(self):
        """
        Return an animation object illustrating the path growing step by step.

        EXAMPLES::

            sage: P = WordPaths('abAB')
            sage: p = P('aaababbb')
            sage: a = p.animate(); print(a)                                             # needs sage.plot
            Animation with 9 frames
            sage: show(a)                       # long time, optional - imagemagick, needs sage.plot
            sage: show(a, delay=35, iterations=3)       # long time, optional - imagemagick, needs sage.plot

        ::

            sage: P = WordPaths('abcdef',steps='triangle')
            sage: p =  P('abcdef')
            sage: a = p.animate(); print(a)                                             # needs sage.plot
            Animation with 8 frames
            sage: show(a)                       # long time, optional - imagemagick, needs sage.plot

        If the path is closed, the plain polygon is added at the end of the
        animation::

            sage: P = WordPaths('abAB')
            sage: p = P('ababAbABABaB')
            sage: a = p.animate(); print(a)                                             # needs sage.plot
            Animation with 14 frames
            sage: show(a)                       # long time, optional - imagemagick, needs sage.plot

        Another example illustrating a Fibonacci tile::

            sage: w = words.fibonacci_tile(2)
            sage: a = w.animate(); print(a)                                             # needs sage.plot
            Animation with 54 frames
            sage: show(a)                       # long time, optional - imagemagick, needs sage.plot

        The first 4 Fibonacci tiles in an animation::

            sage: # needs sage.plot
            sage: a = words.fibonacci_tile(0).animate()
            sage: b = words.fibonacci_tile(1).animate()
            sage: c = words.fibonacci_tile(2).animate()
            sage: d = words.fibonacci_tile(3).animate()
            sage: print(a*b*c*d)
            Animation with 296 frames
            sage: show(a*b*c*d)                 # long time, optional - imagemagick

        .. NOTE::

            If ImageMagick is not installed, you will get an error
            message like this::

               convert: not found

               Error: ImageMagick does not appear to be installed. Saving an
               animation to a GIF file or displaying an animation requires
               ImageMagick, so please install it and try again.

            See www.imagemagick.org, for example.
        """
    def plot_directive_vector(self, options={'rgbcolor': 'blue'}):
        """
        Return an arrow 2d graphics that goes from the start of the path
        to the end.

        INPUT:

        - ``options`` -- dictionary, default: {'rgbcolor': 'blue'} graphic
          options for the arrow

        If the start is the same as the end, a single point is returned.

        EXAMPLES::

            sage: P = WordPaths('abcd'); P
            Word Paths on the square grid
            sage: p = P('aaaccaccacacacaccccccbbdd'); p
            Path: aaaccaccacacacaccccccbbdd
            sage: R = p.plot() + p.plot_directive_vector()                              # needs sage.plot
            sage: R.axes(False)                                                         # needs sage.plot
            sage: R.set_aspect_ratio(1)                                                 # needs sage.plot
            sage: R.plot()                                                              # needs sage.plot
            Graphics object consisting of 4 graphics primitives

        TESTS:

        A closed path::

            sage: P('acbd').plot_directive_vector()                                     # needs sage.plot
            Graphics object consisting of 1 graphics primitive
        """
    def area(self):
        """
        Return the area of a closed path.

        INPUT:

        - ``self`` -- a closed path

        EXAMPLES::

            sage: P = WordPaths('abcd',steps=[(1,1),(-1,1),(-1,-1),(1,-1)])
            sage: p = P('abcd')
            sage: p.area()          #todo: not implemented
            2
        """
    def height(self):
        """
        Return the height of ``self``.

        The height of a `2d`-path is merely the difference
        between the highest and the lowest `y`-coordinate of each
        points traced by it.

        OUTPUT: nonnegative real number

        EXAMPLES::

            sage: Freeman = WordPaths('abAB')
            sage: Freeman('aababaabbbAA').height()
            5

        The function is well-defined if ``self`` is not simple or close::

            sage: Freeman('aabAAB').height()
            1
            sage: Freeman('abbABa').height()
            2

        This works for any `2d`-paths::

            sage: Paths = WordPaths('ab', steps=[(1,0),(1,1)])
            sage: p = Paths('abbaa')
            sage: p.height()
            2
            sage: DyckPaths = WordPaths('ab', steps='dyck')
            sage: p = DyckPaths('abaabb')
            sage: p.height()
            2
            sage: w = WordPaths('abcABC', steps='triangle')('ababcaaBC')
            sage: w.height()
            2.59807621135332
        """
    def height_vector(self):
        """
        Return the height at each point.

        EXAMPLES::

            sage: Paths = WordPaths('ab', steps=[(1,0),(0,1)])
            sage: p = Paths('abbba')
            sage: p.height_vector()
            [0, 0, 1, 2, 3, 3]
        """
    def width(self):
        """
        Return the width of ``self``.

        The height of a `2d`-path is merely the difference
        between the rightmost and the leftmost `x`-coordinate of each
        points traced by it.

        OUTPUT: nonnegative real number

        EXAMPLES::

            sage: Freeman = WordPaths('abAB')
            sage: Freeman('aababaabbbAA').width()
            5

        The function is well-defined if ``self`` is not simple or close::

            sage: Freeman('aabAAB').width()
            2
            sage: Freeman('abbABa').width()
            1

        This works for any `2d`-paths::

            sage: Paths = WordPaths('ab', steps=[(1,0),(1,1)])
            sage: p = Paths('abbaa')
            sage: p.width()
            5
            sage: DyckPaths = WordPaths('ab', steps='dyck')
            sage: p = DyckPaths('abaabb')
            sage: p.width()
            6
            sage: w = WordPaths('abcABC', steps='triangle')('ababcaaBC')
            sage: w.width()
            4.50000000000000
        """
    def width_vector(self):
        """
        Return the width at each point.

        EXAMPLES::

            sage: Paths = WordPaths('ab', steps=[(1,0),(0,1)])
            sage: p = Paths('abbba')
            sage: p.width_vector()
            [0, 1, 1, 1, 1, 2]
        """
    def xmin(self):
        """
        Return the minimum of the x-coordinates of the path.

        EXAMPLES::

            sage: P = WordPaths('0123')
            sage: p = P('0101013332')
            sage: p.xmin()
            0

        This works for any `2d`-paths::

            sage: Paths = WordPaths('ab', steps=[(1,0),(-1,1)])
            sage: p = Paths('abbba')
            sage: p.xmin()
            -2
            sage: DyckPaths = WordPaths('ab', steps='dyck')
            sage: p = DyckPaths('abaabb')
            sage: p.xmin()
            0
            sage: w = WordPaths('abcABC', steps='triangle')('ababcaaBC')
            sage: w.xmin()
            0.000000000000000
        """
    def ymin(self):
        """
        Return the minimum of the y-coordinates of the path.

        EXAMPLES::

            sage: P = WordPaths('0123')
            sage: p = P('0101013332')
            sage: p.ymin()
            0

        This works for any `2d`-paths::

            sage: Paths = WordPaths('ab', steps=[(1,-1),(-1,1)])
            sage: p = Paths('ababa')
            sage: p.ymin()
            -1
            sage: DyckPaths = WordPaths('ab', steps='dyck')
            sage: p = DyckPaths('abaabb')
            sage: p.ymin()
            0
            sage: w = WordPaths('abcABC', steps='triangle')('ababcaaBC')
            sage: w.ymin()
            0.000000000000000
        """
    def xmax(self):
        """
        Return the maximum of the x-coordinates of the path.

        EXAMPLES::

            sage: P = WordPaths('0123')
            sage: p = P('0101013332')
            sage: p.xmax()
            3

        This works for any `2d`-paths::

            sage: Paths = WordPaths('ab', steps=[(1,-1),(-1,1)])
            sage: p = Paths('ababa')
            sage: p.xmax()
            1
            sage: DyckPaths = WordPaths('ab', steps='dyck')
            sage: p = DyckPaths('abaabb')
            sage: p.xmax()
            6
            sage: w = WordPaths('abcABC', steps='triangle')('ababcaaBC')
            sage: w.xmax()
            4.50000000000000
        """
    def ymax(self):
        """
        Return the maximum of the y-coordinates of the path.

        EXAMPLES::

            sage: P = WordPaths('0123')
            sage: p = P('0101013332')
            sage: p.ymax()
            3

        This works for any `2d`-paths::

            sage: Paths = WordPaths('ab', steps=[(1,-1),(-1,1)])
            sage: p = Paths('ababa')
            sage: p.ymax()
            0
            sage: DyckPaths = WordPaths('ab', steps='dyck')
            sage: p = DyckPaths('abaabb')
            sage: p.ymax()
            2
            sage: w = WordPaths('abcABC', steps='triangle')('ababcaaBC')
            sage: w.ymax()
            2.59807621135332
        """

class FiniteWordPath_3d(FiniteWordPath_all):
    def plot(self, pathoptions={'rgbcolor': 'red', 'arrow_head': True, 'thickness': 3}, startpoint: bool = True, startoptions={'rgbcolor': 'red', 'size': 10}):
        """
        INPUT:

        - ``pathoptions`` -- (dict, default:dict(rgbcolor='red',arrow_head=True,
          thickness=3)), options for the path drawing

        - ``startpoint`` -- boolean (default: ``True``); draw the start point?

        - ``startoptions`` -- (dict, default:dict(rgbcolor='red',size=10))
          options for the start point drawing

        EXAMPLES::

            sage: d = ( vector((1,3,2)), vector((2,-4,5)) )
            sage: P = WordPaths(alphabet='ab', steps=d); P
            Word Paths over 2 steps
            sage: p = P('ababab'); p
            Path: ababab
            sage: p.plot()                                                              # needs sage.plot
            Graphics3d Object

            sage: P = WordPaths('abcABC', steps='cube_grid')
            sage: p = P('abcabcAABBC')
            sage: p.plot()                                                              # needs sage.plot
            Graphics3d Object
        """

class FiniteWordPath_square_grid(FiniteWordPath_2d):
    def is_closed(self) -> bool:
        """
        Return whether ``self`` represents a closed path.

        EXAMPLES::

            sage: P = WordPaths('abAB', steps='square_grid')
            sage: P('aA').is_closed()
            True
            sage: P('abAB').is_closed()
            True
            sage: P('ababAABB').is_closed()
            True
            sage: P('aaabbbAABB').is_closed()
            False
            sage: P('ab').is_closed()
            False
        """
    def area(self):
        """
        Return the area of a closed path.

        INPUT:

        - ``self`` -- a closed path

        EXAMPLES::

            sage: P = WordPaths('abAB', steps='square_grid')
            sage: P('abAB').area()
            1
            sage: P('aabbAABB').area()
            4
            sage: P('aabbABAB').area()
            3

        The area of the Fibonacci tiles::

            sage: [words.fibonacci_tile(i).area() for i in range(6)]
            [1, 5, 29, 169, 985, 5741]
            sage: [words.dual_fibonacci_tile(i).area() for i in range(6)]
            [1, 5, 29, 169, 985, 5741]
            sage: oeis(_)[0]                            # optional -- internet
            A001653: Numbers k such that 2*k^2 - 1 is a square.
            sage: _.first_terms()                       # optional -- internet
            (1,
             5,
             29,
             169,
             985,
             5741,
             33461,
             195025,
             1136689,
             6625109,
             38613965,
             225058681,
             1311738121,
             7645370045,
             44560482149,
             259717522849,
             1513744654945,
             8822750406821,
             51422757785981,
             299713796309065,
             1746860020068409,
             10181446324101389,
             59341817924539925)

        TESTS::

            sage: P = WordPaths('abAB', steps='square_grid')
            sage: P('a').area()
            Traceback (most recent call last):
            ...
            TypeError: the path must be closed to compute its area
        """
    def is_simple(self) -> bool:
        """
        Return whether the path is simple.

        A path is simple if all its points are
        distinct.

        If the path is closed, the last point is not considered.

        .. NOTE::

            The linear algorithm described in the thesis of Xavier Provençal
            should be implemented here.

        EXAMPLES::

            sage: P = WordPaths('abAB', steps='square_grid')
            sage: P('abab').is_simple()
            True
            sage: P('abAB').is_simple()
            True
            sage: P('abA').is_simple()
            True
            sage: P('aabABB').is_simple()
            False
            sage: P().is_simple()
            True
            sage: P('A').is_simple()
            True
            sage: P('aA').is_simple()
            True
            sage: P('aaA').is_simple()
            False

        REFERENCES:

        - Provençal, X., *Combinatoires des mots, géometrie discrète et
          pavages*, Thèse de doctorat en Mathématiques, Montréal, UQAM,
          septembre 2008, 115 pages.
        """
    def tikz_trajectory(self) -> str:
        """
        Return the trajectory of ``self`` as a ``tikz`` string.

        EXAMPLES::

            sage: f = words.fibonacci_tile(1)
            sage: f.tikz_trajectory()
            '(0, 0) -- (0, -1) -- (-1, -1) -- (-1, -2) -- (0, -2) -- (0, -3) -- (1, -3) -- (1, -2) -- (2, -2) -- (2, -1) -- (1, -1) -- (1, 0) -- (0, 0)'
        """

class FiniteWordPath_triangle_grid(FiniteWordPath_2d):
    def xmin(self):
        """
        Return the minimum of the x-coordinates of the path.

        EXAMPLES::

            sage: w = WordPaths('abcABC', steps='triangle')('ababcaaBC')
            sage: w.xmin()
            0.000000000000000
            sage: w = WordPaths('abcABC', steps='triangle')('ABAcacacababababcbcbAC')
            sage: w.xmin()
            -3.00000000000000
        """
    def ymin(self):
        """
        Return the minimum of the y-coordinates of the path.

        EXAMPLES::

            sage: w = WordPaths('abcABC', steps='triangle')('ababcaaBC')
            sage: w.ymin()
            0.000000000000000
            sage: w = WordPaths('abcABC', steps='triangle')('ABAcacacababababcbcbAC')
            sage: w.ymin()
            -0.866025403784439
        """
    def xmax(self):
        """
        Return the maximum of the x-coordinates of the path.

        EXAMPLES::

            sage: w = WordPaths('abcABC', steps='triangle')('ababcaaBC')
            sage: w.xmax()
            4.50000000000000
            sage: w = WordPaths('abcABC', steps='triangle')('ABAcacacababababcbcbAC')
            sage: w.xmax()
            4.00000000000000
        """
    def ymax(self):
        """
        Return the maximum of the y-coordinates of the path.

        EXAMPLES::

            sage: w = WordPaths('abcABC', steps='triangle')('ababcaaBC')
            sage: w.ymax()
            2.59807621135332
            sage: w = WordPaths('abcABC', steps='triangle')('ABAcacacababababcbcbAC')
            sage: w.ymax()
            8.66025403784439
        """

class FiniteWordPath_hexagonal_grid(FiniteWordPath_triangle_grid):
    def __init__(self, parent, *args, **kwds) -> None:
        """
        INPUT:

        - ``parent`` -- a parent object inheriting from Words_all
          that has the alphabet attribute defined

        - ``*args``, ``**kwds`` -- arguments accepted by AbstractWord

        EXAMPLES::

            sage: F = WordPaths('abcdef', steps='hexagon'); F
            Word Paths on the hexagonal grid
            sage: f = F('aaabbbccddef'); f
            Path: aaabbbccddef

        ::

            sage: f == loads(dumps(f))
            True
        """

class FiniteWordPath_cube_grid(FiniteWordPath_3d): ...
class FiniteWordPath_north_east(FiniteWordPath_2d): ...
class FiniteWordPath_dyck(FiniteWordPath_2d): ...
class FiniteWordPath_all_list(WordDatatype_list, FiniteWordPath_all, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths(['a','b'],[(1,2,0,0),(3,4,0,0)])
        sage: p = P(['a','b','a']);p
        Path: aba
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_all_list'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_all_str(WordDatatype_str, FiniteWordPath_all, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('ab',[(1,2,0,0),(3,4,0,0)])
        sage: p = P('aabbb'); p
        Path: aabbb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_all_str'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_all_tuple(WordDatatype_tuple, FiniteWordPath_all, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('ab',[(1,2,0,0),(3,4,0,0)])
        sage: p = P( ('a','b','b') ); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_all_tuple'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_all_iter_with_caching(WordDatatype_iter_with_caching, FiniteWordPath_all, FiniteWord_class): ...
class FiniteWordPath_all_iter(WordDatatype_iter, FiniteWordPath_all, FiniteWord_class): ...
class FiniteWordPath_all_callable_with_caching(WordDatatype_callable_with_caching, FiniteWordPath_all, FiniteWord_class): ...
class FiniteWordPath_all_callable(WordDatatype_callable, FiniteWordPath_all, FiniteWord_class): ...
class FiniteWordPath_2d_list(WordDatatype_list, FiniteWordPath_2d, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths(['a','b'],[(1,2),(3,4)])
        sage: p = P(['a','b','a']);p
        Path: aba
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_2d_list'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_2d_str(WordDatatype_str, FiniteWordPath_2d, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths(['a','b'],[(1,2),(3,4)])
        sage: p = P('aba'); p
        Path: aba
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_2d_str'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_2d_tuple(WordDatatype_tuple, FiniteWordPath_2d, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths(['a','b'],[(1,2),(3,4)])
        sage: p = P(('a','b','a'));p
        Path: aba
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_2d_tuple'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_2d_iter_with_caching(WordDatatype_iter_with_caching, FiniteWordPath_2d, FiniteWord_class): ...
class FiniteWordPath_2d_iter(WordDatatype_iter, FiniteWordPath_2d, FiniteWord_class): ...
class FiniteWordPath_2d_callable_with_caching(WordDatatype_callable_with_caching, FiniteWordPath_2d, FiniteWord_class): ...
class FiniteWordPath_2d_callable(WordDatatype_callable, FiniteWordPath_2d, FiniteWord_class): ...
class FiniteWordPath_3d_list(WordDatatype_list, FiniteWordPath_3d, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths(['a','b'],[(1,2,0),(3,4,0)])
        sage: p = P(['a','b','a']);p
        Path: aba
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_3d_list'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_3d_str(WordDatatype_str, FiniteWordPath_3d, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths(['a','b'],[(1,2,0),(3,4,0)])
        sage: p = P('aba'); p
        Path: aba
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_3d_str'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_3d_tuple(WordDatatype_tuple, FiniteWordPath_3d, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths(['a','b'],[(1,2,0),(3,4,0)])
        sage: p = P(('a','b','a'));p
        Path: aba
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_3d_tuple'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_3d_iter_with_caching(WordDatatype_iter_with_caching, FiniteWordPath_3d, FiniteWord_class): ...
class FiniteWordPath_3d_iter(WordDatatype_iter, FiniteWordPath_3d, FiniteWord_class): ...
class FiniteWordPath_3d_callable_with_caching(WordDatatype_callable_with_caching, FiniteWordPath_3d, FiniteWord_class): ...
class FiniteWordPath_3d_callable(WordDatatype_callable, FiniteWordPath_3d, FiniteWord_class): ...
class FiniteWordPath_square_grid_list(WordDatatype_list, FiniteWordPath_square_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcd', steps='square')
        sage: p = P(['a','b','b']); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_square_grid_list'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_square_grid_str(WordDatatype_str, FiniteWordPath_square_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcd', steps='square')
        sage: p = P('abccc'); p
        Path: abccc
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_square_grid_str'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_square_grid_tuple(WordDatatype_tuple, FiniteWordPath_square_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcd', steps='square')
        sage: p = P(('a','b','b')); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_square_grid_tuple'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_square_grid_iter_with_caching(WordDatatype_iter_with_caching, FiniteWordPath_square_grid, FiniteWord_class): ...
class FiniteWordPath_square_grid_iter(WordDatatype_iter, FiniteWordPath_square_grid, FiniteWord_class): ...
class FiniteWordPath_square_grid_callable_with_caching(WordDatatype_callable_with_caching, FiniteWordPath_square_grid, FiniteWord_class): ...
class FiniteWordPath_square_grid_callable(WordDatatype_callable, FiniteWordPath_square_grid, FiniteWord_class): ...
class FiniteWordPath_triangle_grid_list(WordDatatype_list, FiniteWordPath_triangle_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcdef', steps='triangle')
        sage: p = P(['a','b','b']); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_triangle_grid_list'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_triangle_grid_str(WordDatatype_str, FiniteWordPath_triangle_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcdef', steps='triangle')
        sage: p = P('abb'); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_triangle_grid_str'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_triangle_grid_tuple(WordDatatype_tuple, FiniteWordPath_triangle_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcdef', steps='triangle')
        sage: p = P(('a','b','b')); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_triangle_grid_tuple'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_triangle_grid_iter_with_caching(WordDatatype_iter_with_caching, FiniteWordPath_triangle_grid, FiniteWord_class): ...
class FiniteWordPath_triangle_grid_iter(WordDatatype_iter, FiniteWordPath_triangle_grid, FiniteWord_class): ...
class FiniteWordPath_triangle_grid_callable_with_caching(WordDatatype_callable_with_caching, FiniteWordPath_triangle_grid, FiniteWord_class): ...
class FiniteWordPath_triangle_grid_callable(WordDatatype_callable, FiniteWordPath_triangle_grid, FiniteWord_class): ...
class FiniteWordPath_hexagonal_grid_list(WordDatatype_list, FiniteWordPath_hexagonal_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcdef', steps='hexagon')
        sage: p = P(['a','b','b']); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_hexagonal_grid_list'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_hexagonal_grid_str(WordDatatype_str, FiniteWordPath_hexagonal_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcdef', steps='hexagon')
        sage: p = P('abb'); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_hexagonal_grid_str'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_hexagonal_grid_tuple(WordDatatype_tuple, FiniteWordPath_hexagonal_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcdef', steps='hexagon')
        sage: p = P(('a','b','b')); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_hexagonal_grid_tuple'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_hexagonal_grid_iter_with_caching(WordDatatype_iter_with_caching, FiniteWordPath_hexagonal_grid, FiniteWord_class): ...
class FiniteWordPath_hexagonal_grid_iter(WordDatatype_iter, FiniteWordPath_hexagonal_grid, FiniteWord_class): ...
class FiniteWordPath_hexagonal_grid_callable_with_caching(WordDatatype_callable_with_caching, FiniteWordPath_hexagonal_grid, FiniteWord_class): ...
class FiniteWordPath_hexagonal_grid_callable(WordDatatype_callable, FiniteWordPath_hexagonal_grid, FiniteWord_class): ...
class FiniteWordPath_cube_grid_list(WordDatatype_list, FiniteWordPath_cube_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcdef', steps='cube')
        sage: p = P(['a','b','b']); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_cube_grid_list'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_cube_grid_str(WordDatatype_str, FiniteWordPath_cube_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcdef', steps='cube')
        sage: p = P('abb'); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_cube_grid_str'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_cube_grid_tuple(WordDatatype_tuple, FiniteWordPath_cube_grid, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('abcdef', steps='cube')
        sage: p = P(('a','b','b')); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_cube_grid_tuple'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_cube_grid_iter_with_caching(WordDatatype_iter_with_caching, FiniteWordPath_cube_grid, FiniteWord_class): ...
class FiniteWordPath_cube_grid_iter(WordDatatype_iter, FiniteWordPath_cube_grid, FiniteWord_class): ...
class FiniteWordPath_cube_grid_callable_with_caching(WordDatatype_callable_with_caching, FiniteWordPath_cube_grid, FiniteWord_class): ...
class FiniteWordPath_cube_grid_callable(WordDatatype_callable, FiniteWordPath_cube_grid, FiniteWord_class): ...
class FiniteWordPath_north_east_list(WordDatatype_list, FiniteWordPath_north_east, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('ab', steps='ne')
        sage: p = P(['a','b','b']); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_north_east_list'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_north_east_str(WordDatatype_str, FiniteWordPath_north_east, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('ab', steps='ne')
        sage: p = P('abb'); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_north_east_str'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_north_east_tuple(WordDatatype_tuple, FiniteWordPath_north_east, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('ab', steps='ne')
        sage: p = P(('a','b','b')); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_north_east_tuple'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_north_east_iter_with_caching(WordDatatype_iter_with_caching, FiniteWordPath_north_east, FiniteWord_class): ...
class FiniteWordPath_north_east_iter(WordDatatype_iter, FiniteWordPath_north_east, FiniteWord_class): ...
class FiniteWordPath_north_east_callable_with_caching(WordDatatype_callable_with_caching, FiniteWordPath_north_east, FiniteWord_class): ...
class FiniteWordPath_north_east_callable(WordDatatype_callable, FiniteWordPath_north_east, FiniteWord_class): ...
class FiniteWordPath_dyck_list(WordDatatype_list, FiniteWordPath_dyck, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('ab', steps='dyck')
        sage: p = P(['a','b','b']); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_dyck_list'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_dyck_str(WordDatatype_str, FiniteWordPath_dyck, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('ab', steps='dyck')
        sage: p = P('abb'); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_dyck_str'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_dyck_tuple(WordDatatype_tuple, FiniteWordPath_dyck, FiniteWord_class):
    """
    TESTS::

        sage: P = WordPaths('ab', steps='dyck')
        sage: p = P(('a','b','b')); p
        Path: abb
        sage: type(p)
        <class 'sage.combinat.words.paths.FiniteWordPath_dyck_tuple'>
        sage: p == loads(dumps(p))
        True
    """
class FiniteWordPath_dyck_iter_with_caching(WordDatatype_iter_with_caching, FiniteWordPath_dyck, FiniteWord_class): ...
class FiniteWordPath_dyck_iter(WordDatatype_iter, FiniteWordPath_dyck, FiniteWord_class): ...
class FiniteWordPath_dyck_callable_with_caching(WordDatatype_callable_with_caching, FiniteWordPath_dyck, FiniteWord_class): ...
class FiniteWordPath_dyck_callable(WordDatatype_callable, FiniteWordPath_dyck, FiniteWord_class): ...
