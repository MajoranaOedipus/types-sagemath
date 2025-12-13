from _typeshed import Incomplete
from collections.abc import Generator
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.structure.sage_object import SageObject as SageObject

def ncube_isometry_group(n, orientation_preserving: bool = True):
    """
    Return the isometry group of the `n`-cube as a list of matrices.

    INPUT:

    - ``n`` -- positive integer, dimension of the space
    - ``orientation_preserving`` -- boolean (default: ``True``);
      whether the orientation is preserved

    OUTPUT: list of matrices

    EXAMPLES::

        sage: from sage.combinat.tiling import ncube_isometry_group
        sage: ncube_isometry_group(2)
        [
        [1 0]  [ 0  1]  [-1  0]  [ 0 -1]
        [0 1], [-1  0], [ 0 -1], [ 1  0]
        ]
        sage: ncube_isometry_group(2, orientation_preserving=False)
        [
        [1 0]  [ 0 -1]  [ 1  0]  [ 0  1]  [0 1]  [-1  0]  [ 0 -1]  [-1  0]
        [0 1], [-1  0], [ 0 -1], [-1  0], [1 0], [ 0 -1], [ 1  0], [ 0  1]
        ]

    There are 24 orientation preserving isometries of the 3-cube::

        sage: ncube_isometry_group(3)
        [
        [1 0 0]  [ 1  0  0]  [ 1  0  0]  [ 0  1  0]  [0 1 0]  [ 0  0  1]
        [0 1 0]  [ 0  0  1]  [ 0  0 -1]  [-1  0  0]  [0 0 1]  [ 0 -1  0]
        [0 0 1], [ 0 -1  0], [ 0  1  0], [ 0  0  1], [1 0 0], [ 1  0  0],
        <BLANKLINE>
        [-1  0  0]  [ 0 -1  0]  [-1  0  0]  [-1  0  0]  [ 0 -1  0]  [ 0  0 -1]
        [ 0 -1  0]  [ 0  0 -1]  [ 0  0 -1]  [ 0  1  0]  [ 0  0  1]  [ 1  0  0]
        [ 0  0  1], [ 1  0  0], [ 0 -1  0], [ 0  0 -1], [-1  0  0], [ 0 -1  0],
        <BLANKLINE>
        [ 0  1  0]  [ 0  0  1]  [0 0 1]  [ 0 -1  0]  [ 0  0 -1]  [-1  0  0]
        [ 1  0  0]  [ 0  1  0]  [1 0 0]  [ 1  0  0]  [ 0  1  0]  [ 0  0  1]
        [ 0  0 -1], [-1  0  0], [0 1 0], [ 0  0  1], [ 1  0  0], [ 0  1  0],
        <BLANKLINE>
        [ 0 -1  0]  [ 0  0 -1]  [ 0  0  1]  [ 1  0  0]  [ 0  0 -1]  [ 0  1  0]
        [-1  0  0]  [-1  0  0]  [-1  0  0]  [ 0 -1  0]  [ 0 -1  0]  [ 0  0 -1]
        [ 0  0 -1], [ 0  1  0], [ 0 -1  0], [ 0  0 -1], [-1  0  0], [-1  0  0]
        ]

    TESTS::

        sage: ncube_isometry_group(1)
        [[1]]
        sage: ncube_isometry_group(0)
        Traceback (most recent call last):
        ...
        ValueError: ['B', 0] is not a valid Cartan type
    """
@cached_function
def ncube_isometry_group_cosets(n, orientation_preserving: bool = True):
    """
    Return the quotient of the isometry group of the `n`-cube by the
    the isometry group of the rectangular parallelepiped.

    INPUT:

    - ``n`` -- positive integer, dimension of the space
    - ``orientation_preserving`` -- boolean (default: ``True``);
      whether the orientation is preserved

    OUTPUT: list of cosets, each coset being a sorted list of matrices

    EXAMPLES::

        sage: from sage.combinat.tiling import ncube_isometry_group_cosets
        sage: sorted(ncube_isometry_group_cosets(2))
        [[
        [-1  0]  [1 0]
        [ 0 -1], [0 1]
        ], [
        [ 0 -1]  [ 0  1]
        [ 1  0], [-1  0]
        ]]
        sage: sorted(ncube_isometry_group_cosets(2, False))
        [[
        [-1  0]  [-1  0]  [ 1  0]  [1 0]
        [ 0 -1], [ 0  1], [ 0 -1], [0 1]
        ], [
        [ 0 -1]  [ 0 -1]  [ 0  1]  [0 1]
        [-1  0], [ 1  0], [-1  0], [1 0]
        ]]

    ::

        sage: sorted(ncube_isometry_group_cosets(3))
        [[
        [-1  0  0]  [-1  0  0]  [ 1  0  0]  [1 0 0]
        [ 0 -1  0]  [ 0  1  0]  [ 0 -1  0]  [0 1 0]
        [ 0  0  1], [ 0  0 -1], [ 0  0 -1], [0 0 1]
        ], [
        [-1  0  0]  [-1  0  0]  [ 1  0  0]  [ 1  0  0]
        [ 0  0 -1]  [ 0  0  1]  [ 0  0 -1]  [ 0  0  1]
        [ 0 -1  0], [ 0  1  0], [ 0  1  0], [ 0 -1  0]
        ], [
        [ 0 -1  0]  [ 0 -1  0]  [ 0  1  0]  [ 0  1  0]
        [-1  0  0]  [ 1  0  0]  [-1  0  0]  [ 1  0  0]
        [ 0  0 -1], [ 0  0  1], [ 0  0  1], [ 0  0 -1]
        ], [
        [ 0 -1  0]  [ 0 -1  0]  [ 0  1  0]  [0 1 0]
        [ 0  0 -1]  [ 0  0  1]  [ 0  0 -1]  [0 0 1]
        [ 1  0  0], [-1  0  0], [-1  0  0], [1 0 0]
        ], [
        [ 0  0 -1]  [ 0  0 -1]  [ 0  0  1]  [0 0 1]
        [-1  0  0]  [ 1  0  0]  [-1  0  0]  [1 0 0]
        [ 0  1  0], [ 0 -1  0], [ 0 -1  0], [0 1 0]
        ], [
        [ 0  0 -1]  [ 0  0 -1]  [ 0  0  1]  [ 0  0  1]
        [ 0 -1  0]  [ 0  1  0]  [ 0 -1  0]  [ 0  1  0]
        [-1  0  0], [ 1  0  0], [ 1  0  0], [-1  0  0]
        ]]

    TESTS::

        sage: cosets = ncube_isometry_group_cosets(3, False)
        sage: len(cosets)
        6
        sage: [len(c) for c in cosets]
        [8, 8, 8, 8, 8, 8]
        sage: type(cosets[0][0])
        <class 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
    """

class Polyomino(SageObject):
    """
    A polyomino in `\\ZZ^d`.

    The polyomino is the union of the unit square (or cube, or n-cube)
    centered at those coordinates. Such an object should be connected, but
    the code does not make this assumption.

    INPUT:

    - ``coords`` -- iterable of integer coordinates in `\\ZZ^d`
    - ``color`` -- string (default: ``'gray'``); color for display
    - ``dimension`` -- integer (default: ``None``); dimension of the space,
      if ``None``, it is guessed from the ``coords`` if ``coords`` is non
      empty

    EXAMPLES::

        sage: from sage.combinat.tiling import Polyomino
        sage: Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')
        Polyomino: [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1)], Color: blue
    """
    def __init__(self, coords, color: str = 'gray', dimension=None) -> None:
        """
        Constructor.

        See :mod:`Polyomino` for full documentation.

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')
            Polyomino: [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1)], Color: blue

        ::

            sage: Polyomino([(0,0), (1,0), (2,0)])
            Polyomino: [(0, 0), (1, 0), (2, 0)], Color: gray

        TESTS::

            sage: Polyomino([], dimension=2)
            Polyomino: [], Color: gray
        """
    def color(self, color=None):
        """
        Return or change the color of the polyomino.

        INPUT:

        - ``color`` -- string, RBG tuple or ``None`` (default: ``None``),
          if ``None``, it returns the current color

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')
            sage: p.color()
            'blue'
        """
    def frozenset(self):
        """
        Return the elements of `\\ZZ^d` in the polyomino as a frozenset.

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='red')
            sage: p.frozenset()
            frozenset({(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1)})
        """
    @cached_method
    def sorted_list(self):
        """
        Return the color of the polyomino.

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')
            sage: p.sorted_list()
            [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 1, 1)]
        """
    def __len__(self) -> int:
        """
        Return the size of the polyomino, i.e. the number of n-dimensional
        unit cubes.

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')
            sage: len(p)
            4
        """
    def __iter__(self):
        """
        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')
            sage: it = iter(p)
            sage: next(it)
            (0, 0, 0)
        """
    @cached_method
    def bounding_box(self):
        """
        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0),(1,0,0),(1,1,0),(1,1,1),(1,2,0)], color='deeppink')
            sage: p.bounding_box()
            [[0, 0, 0], [1, 2, 1]]
        """
    def __hash__(self):
        """
        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')
            sage: hash(p)     # random
            2059134902
        """
    def __eq__(self, other):
        """
        Return whether ``self`` is equal to ``other``.

        INPUT:

        - ``other`` -- a polyomino

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')
            sage: q = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='red')
            sage: p == q
            True
            sage: r = Polyomino([(0,0,0), (0,1,0), (1,1,0)], color='blue')
            sage: p == r
            False
        """
    def __ne__(self, other):
        """
        Return whether ``self`` is not equal to ``other``.

        INPUT:

        - ``other`` -- a polyomino

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')
            sage: q = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='red')
            sage: p != q
            False
            sage: r = Polyomino([(0,0,0), (0,1,0), (1,1,0)], color='blue')
            sage: p != r
            True
        """
    def __le__(self, other):
        """
        Return whether ``self`` is inside of ``other``.

        INPUT:

        - ``other`` -- a polyomino

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0)])
            sage: b = Polyomino([(0,0), (0,1), (1,1), (2,1)])
            sage: p <= b
            True
            sage: b <= p
            False
        """
    def __ge__(self, other):
        """
        Return whether ``self`` contains ``other``.

        INPUT:

        - ``other`` -- a polyomino

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0)])
            sage: b = Polyomino([(0,0), (0,1), (1,1), (2,1)])
            sage: p >= b
            False
            sage: b >= p
            True
        """
    def __lt__(self, other):
        """
        Return whether ``self`` is strictly inside of ``other``.

        INPUT:

        - ``other`` -- a polyomino

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0)])
            sage: b = Polyomino([(0,0), (0,1), (1,1), (2,1)])
            sage: p < b
            True
            sage: b < p
            False
        """
    def __gt__(self, other):
        """
        Return whether ``self`` strictly contains ``other``.

        INPUT:

        - ``other`` -- a polyomino

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0)])
            sage: b = Polyomino([(0,0), (0,1), (1,1), (2,1)])
            sage: p > b
            False
            sage: b > p
            True
        """
    def intersection(self, other):
        """
        Return the intersection of ``self`` and ``other``.

        INPUT:

        - ``other`` -- a polyomino

        OUTPUT: polyomino

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: a = Polyomino([(0,0)])
            sage: b = Polyomino([(0,0), (0,1), (1,1), (2,1)])
            sage: a.intersection(b)
            Polyomino: [(0, 0)], Color: gray
            sage: a.intersection(b+(1,1))
            Polyomino: [], Color: gray
        """
    def __sub__(self, v):
        """
        Return a translated copy of ``self`` by the opposite of the
        vector v.

        INPUT:

        - ``v`` -- tuple

        OUTPUT: polyomino

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0),(1,0,0),(1,1,0),(1,1,1),(1,2,0)], color='deeppink')
            sage: p - (2,2,2)
            Polyomino: [(-2, -2, -2), (-1, -2, -2), (-1, -1, -2), (-1, -1, -1), (-1, 0, -2)], Color: deeppink
        """
    def __add__(self, v):
        """
        Return a translated copy of ``self`` by the vector v.

        INPUT:

        - ``v`` -- tuple

        OUTPUT: polyomino

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0),(1,0,0),(1,1,0),(1,1,1),(1,2,0)], color='deeppink')
            sage: p + (2,2,2)
            Polyomino: [(2, 2, 2), (3, 2, 2), (3, 3, 2), (3, 3, 3), (3, 4, 2)], Color: deeppink
        """
    def __rmul__(self, m):
        """
        Return the image of the polyomino under the application of the
        matrix m.

        INPUT:

        - ``m`` -- square matrix, matching the dimension of ``self``

        OUTPUT: polyomino

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0),(1,0,0),(1,1,0),(1,1,1),(1,2,0)], color='deeppink')
            sage: m = matrix(3, [1,0,0,0,1,0,0,0,1])
            sage: m * p
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0)], Color: deeppink
            sage: m = matrix(3, [1,0,0,0,0,-1,0,1,0])
            sage: m * p
            Polyomino: [(0, 0, 0), (1, -1, 1), (1, 0, 0), (1, 0, 1), (1, 0, 2)], Color: deeppink

        TESTS::

            sage: m = matrix(2, [1,0,0,1])
            sage: m * p
            Traceback (most recent call last):
            ...
            ValueError: Dimension of input matrix must match the dimension of the polyomino
        """
    def canonical(self):
        """
        Return the translated copy of ``self`` having minimal and nonnegative
        coordinates

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0),(1,0,0),(1,1,0),(1,1,1),(1,2,0)], color='deeppink')
            sage: p
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0)], Color: deeppink
            sage: p.canonical()
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0)], Color: deeppink

        TESTS::

            sage: p
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0)], Color: deeppink
            sage: p + (3,4,5)
            Polyomino: [(3, 4, 5), (4, 4, 5), (4, 5, 5), (4, 5, 6), (4, 6, 5)], Color: deeppink
            sage: (p + (3,4,5)).canonical()
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0)], Color: deeppink
        """
    def canonical_isometric_copies(self, orientation_preserving: bool = True, mod_box_isometries: bool = False):
        """
        Return the list of image of ``self`` under isometries of the `n`-cube
        where the coordinates are all nonnegative and minimal.

        INPUT:

        - ``orientation_preserving`` -- boolean (default: ``True``);
          if ``True``, the group of isometries of the `n`-cube is restricted
          to those that preserve the orientation, i.e. of determinant 1.

        - ``mod_box_isometries`` -- boolean (default: ``False``); whether to
          quotient the group of isometries of the `n`-cube by the
          subgroup of isometries of the `a_1\\times a_2\\cdots \\times a_n`
          rectangular box where are the `a_i` are assumed to be distinct.

        OUTPUT: set of Polyomino

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')
            sage: s = p.canonical_isometric_copies()
            sage: len(s)
            12

        With the non orientation-preserving::

            sage: s = p.canonical_isometric_copies(orientation_preserving=False)
            sage: len(s)
            24

        Modulo rotation by angle 180 degrees::

            sage: s = p.canonical_isometric_copies(mod_box_isometries=True)
            sage: len(s)
            3

        TESTS::

            sage: from sage.games.quantumino import pentaminos
            sage: [len(p.canonical_isometric_copies((5,8,2), mod_box_isometries=False)) for p in pentaminos]
            [24, 24, 24, 24, 24, 24, 12, 12, 24, 24, 24, 24, 12, 12, 24, 24, 12]
            sage: [len(p.canonical_isometric_copies((5,8,2), mod_box_isometries=True)) for p in pentaminos]
            [6, 6, 6, 6, 6, 6, 3, 3, 6, 6, 6, 6, 3, 3, 6, 6, 3]
        """
    def translated_copies(self, box) -> Generator[Incomplete]:
        """
        Return an iterator over the translated images of ``self`` inside a
        polyomino.

        INPUT:

        - ``box`` -- polyomino or tuple of integers (size of a box)

        OUTPUT: iterator of 3d polyominoes

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0),(1,0,0),(1,1,0),(1,1,1),(1,2,0)], color='deeppink')
            sage: for t in p.translated_copies(box=(5,8,2)): t
            Polyomino: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0)], Color: deeppink
            Polyomino: [(0, 1, 0), (1, 1, 0), (1, 2, 0), (1, 2, 1), (1, 3, 0)], Color: deeppink
            Polyomino: [(0, 2, 0), (1, 2, 0), (1, 3, 0), (1, 3, 1), (1, 4, 0)], Color: deeppink
            Polyomino: [(0, 3, 0), (1, 3, 0), (1, 4, 0), (1, 4, 1), (1, 5, 0)], Color: deeppink
            Polyomino: [(0, 4, 0), (1, 4, 0), (1, 5, 0), (1, 5, 1), (1, 6, 0)], Color: deeppink
            Polyomino: [(0, 5, 0), (1, 5, 0), (1, 6, 0), (1, 6, 1), (1, 7, 0)], Color: deeppink
            Polyomino: [(1, 0, 0), (2, 0, 0), (2, 1, 0), (2, 1, 1), (2, 2, 0)], Color: deeppink
            Polyomino: [(1, 1, 0), (2, 1, 0), (2, 2, 0), (2, 2, 1), (2, 3, 0)], Color: deeppink
            Polyomino: [(1, 2, 0), (2, 2, 0), (2, 3, 0), (2, 3, 1), (2, 4, 0)], Color: deeppink
            Polyomino: [(1, 3, 0), (2, 3, 0), (2, 4, 0), (2, 4, 1), (2, 5, 0)], Color: deeppink
            Polyomino: [(1, 4, 0), (2, 4, 0), (2, 5, 0), (2, 5, 1), (2, 6, 0)], Color: deeppink
            Polyomino: [(1, 5, 0), (2, 5, 0), (2, 6, 0), (2, 6, 1), (2, 7, 0)], Color: deeppink
            Polyomino: [(2, 0, 0), (3, 0, 0), (3, 1, 0), (3, 1, 1), (3, 2, 0)], Color: deeppink
            Polyomino: [(2, 1, 0), (3, 1, 0), (3, 2, 0), (3, 2, 1), (3, 3, 0)], Color: deeppink
            Polyomino: [(2, 2, 0), (3, 2, 0), (3, 3, 0), (3, 3, 1), (3, 4, 0)], Color: deeppink
            Polyomino: [(2, 3, 0), (3, 3, 0), (3, 4, 0), (3, 4, 1), (3, 5, 0)], Color: deeppink
            Polyomino: [(2, 4, 0), (3, 4, 0), (3, 5, 0), (3, 5, 1), (3, 6, 0)], Color: deeppink
            Polyomino: [(2, 5, 0), (3, 5, 0), (3, 6, 0), (3, 6, 1), (3, 7, 0)], Color: deeppink
            Polyomino: [(3, 0, 0), (4, 0, 0), (4, 1, 0), (4, 1, 1), (4, 2, 0)], Color: deeppink
            Polyomino: [(3, 1, 0), (4, 1, 0), (4, 2, 0), (4, 2, 1), (4, 3, 0)], Color: deeppink
            Polyomino: [(3, 2, 0), (4, 2, 0), (4, 3, 0), (4, 3, 1), (4, 4, 0)], Color: deeppink
            Polyomino: [(3, 3, 0), (4, 3, 0), (4, 4, 0), (4, 4, 1), (4, 5, 0)], Color: deeppink
            Polyomino: [(3, 4, 0), (4, 4, 0), (4, 5, 0), (4, 5, 1), (4, 6, 0)], Color: deeppink
            Polyomino: [(3, 5, 0), (4, 5, 0), (4, 6, 0), (4, 6, 1), (4, 7, 0)], Color: deeppink

        This method is independent of the translation of the polyomino::

            sage: q = Polyomino([(0,0,0), (1,0,0)])
            sage: list(q.translated_copies((2,2,1)))
            [Polyomino: [(0, 0, 0), (1, 0, 0)], Color: gray,
             Polyomino: [(0, 1, 0), (1, 1, 0)], Color: gray]
            sage: q = Polyomino([(34,7,-9), (35,7,-9)])
            sage: list(q.translated_copies((2,2,1)))
            [Polyomino: [(0, 0, 0), (1, 0, 0)], Color: gray,
             Polyomino: [(0, 1, 0), (1, 1, 0)], Color: gray]

        Inside smaller boxes::

            sage: list(p.translated_copies(box=(2,2,3)))
            []
            sage: list(p.translated_copies(box=(2,3,2)))
            [Polyomino: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 0)], Color: deeppink]
            sage: list(p.translated_copies(box=(3,2,2)))
            []
            sage: list(p.translated_copies(box=(1,1,1)))
            []

        Using a Polyomino as input::

            sage: b = Polyomino([(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)])
            sage: p = Polyomino([(0,0)])
            sage: list(p.translated_copies(b))
            [Polyomino: [(0, 0)], Color: gray,
             Polyomino: [(0, 1)], Color: gray,
             Polyomino: [(0, 2)], Color: gray,
             Polyomino: [(1, 0)], Color: gray,
             Polyomino: [(1, 1)], Color: gray,
             Polyomino: [(1, 2)], Color: gray]

        ::

            sage: p = Polyomino([(0,0), (1,0), (0,1)])
            sage: b = Polyomino([(0,0), (1,0), (2,0), (0,1), (1,1), (0,2)])
            sage: list(p.translated_copies(b))
            [Polyomino: [(0, 0), (0, 1), (1, 0)], Color: gray,
             Polyomino: [(0, 1), (0, 2), (1, 1)], Color: gray,
             Polyomino: [(1, 0), (1, 1), (2, 0)], Color: gray]
        """
    def translated_copies_intersection(self, box):
        """
        Return the set of non empty intersections of translated images of
        ``self`` with a polyomino.

        INPUT:

        - ``box`` -- polyomino or tuple of integers (size of a box)

        OUTPUT: set of 3d polyominoes

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0),(1,0)], color='deeppink')
            sage: sorted(sorted(a.frozenset())
            ....:        for a in p.translated_copies_intersection(box=(2,3)))
            [[(0, 0)],
             [(0, 0), (1, 0)],
             [(0, 1)],
             [(0, 1), (1, 1)],
             [(0, 2)],
             [(0, 2), (1, 2)],
             [(1, 0)],
             [(1, 1)],
             [(1, 2)]]

        Using a Polyomino as input::

            sage: b = Polyomino([(0,0), (0,1), (0,2), (1,0), (2,0)])
            sage: p = Polyomino([(0,0), (1,0)])
            sage: sorted(sorted(a.frozenset())
            ....:        for a in p.translated_copies_intersection(b))
            [[(0, 0)], [(0, 0), (1, 0)], [(0, 1)], [(0, 2)], [(1, 0), (2, 0)], [(2, 0)]]
        """
    def isometric_copies(self, box, orientation_preserving: bool = True, mod_box_isometries: bool = False) -> Generator[Incomplete, Incomplete]:
        """
        Return the translated and isometric images of ``self`` that lies in the box.

        INPUT:

        - ``box`` -- polyomino or tuple of integers (size of a box)

        - ``orientation_preserving`` -- boolean (default: ``True``);
          if ``True``, the group of isometries of the `n`-cube is restricted
          to those that preserve the orientation, i.e. of determinant 1.

        - ``mod_box_isometries`` -- boolean (default: ``False``); whether to
          quotient the group of isometries of the `n`-cube by the
          subgroup of isometries of the `a_1\\times a_2\\cdots \\times a_n`
          rectangular box where are the `a_i` are assumed to be distinct.

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0),(1,0,0),(1,1,0),(1,1,1),(1,2,0)], color='deeppink')
            sage: L = list(p.isometric_copies(box=(5,8,2)))
            sage: len(L)
            360

        ::

            sage: p = Polyomino([(0,0,0),(1,0,0),(1,1,0),(1,2,0),(1,2,1)], color='orange')
            sage: L = list(p.isometric_copies(box=(5,8,2)))
            sage: len(L)
            180
            sage: L = list(p.isometric_copies((5,8,2), False))
            sage: len(L)
            360
            sage: L = list(p.isometric_copies((5,8,2), mod_box_isometries=True))
            sage: len(L)
            45

        ::

            sage: p = Polyomino([(0,0), (1,0), (0,1)])
            sage: b = Polyomino([(0,0), (1,0), (2,0), (0,1), (1,1), (0,2)])
            sage: sorted(p.isometric_copies(b), key=lambda p: p.sorted_list())
            [Polyomino: [(0, 0), (0, 1), (1, 0)], Color: gray,
             Polyomino: [(0, 0), (0, 1), (1, 1)], Color: gray,
             Polyomino: [(0, 0), (1, 0), (1, 1)], Color: gray,
             Polyomino: [(0, 1), (0, 2), (1, 1)], Color: gray,
             Polyomino: [(0, 1), (1, 0), (1, 1)], Color: gray,
             Polyomino: [(1, 0), (1, 1), (2, 0)], Color: gray]
        """
    def isometric_copies_intersection(self, box, orientation_preserving: bool = True):
        """
        Return the set of non empty intersections of isometric images of
        ``self`` with a polyomino.

        INPUT:

        - ``box`` -- polyomino or tuple of integers (size of a box)

        - ``orientation_preserving`` -- boolean (default: ``True``);
          if ``True``, the group of isometries of the `n`-cube is restricted
          to those that preserve the orientation, i.e. of determinant 1.

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0),(1,0)], color='deeppink')
            sage: sorted(sorted(a.frozenset()) for a in p.isometric_copies_intersection(box=(2,3)))
            [[(0, 0)],
             [(0, 0), (0, 1)],
             [(0, 0), (1, 0)],
             [(0, 1)],
             [(0, 1), (0, 2)],
             [(0, 1), (1, 1)],
             [(0, 2)],
             [(0, 2), (1, 2)],
             [(1, 0)],
             [(1, 0), (1, 1)],
             [(1, 1)],
             [(1, 1), (1, 2)],
             [(1, 2)]]
        """
    def neighbor_edges(self) -> Generator[Incomplete]:
        """
        Return an iterator over the pairs of neighbor coordinates inside of
        the polyomino.

        Two points `P` and `Q` in the polyomino are neighbor if `P - Q` has
        one coordinate equal to `+1` or `-1` and zero everywhere else.

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0),(0,0,1)])
            sage: [sorted(edge) for edge in p.neighbor_edges()]
            [[(0, 0, 0), (0, 0, 1)]]

        In 3d::

            sage: p = Polyomino([(0,0,0),(1,0,0),(1,1,0),(1,1,1),(1,2,0)], color='deeppink')
            sage: L = sorted(sorted(edge) for edge in p.neighbor_edges())
            sage: for a in L: a
            [(0, 0, 0), (1, 0, 0)]
            [(1, 0, 0), (1, 1, 0)]
            [(1, 1, 0), (1, 1, 1)]
            [(1, 1, 0), (1, 2, 0)]

        In 2d::

            sage: p = Polyomino([(0,0),(1,0),(1,1),(1,2)])
            sage: L = sorted(sorted(edge) for edge in p.neighbor_edges())
            sage: for a in L: a
            [(0, 0), (1, 0)]
            [(1, 0), (1, 1)]
            [(1, 1), (1, 2)]
        """
    def center(self):
        """
        Return the center of the polyomino.

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0),(0,0,1)])
            sage: p.center()
            (0, 0, 1/2)

        In 3d::

            sage: p = Polyomino([(0,0,0),(1,0,0),(1,1,0),(1,1,1),(1,2,0)], color='deeppink')
            sage: p.center()
            (4/5, 4/5, 1/5)

        In 2d::

            sage: p = Polyomino([(0,0),(1,0),(1,1),(1,2)])
            sage: p.center()
            (3/4, 3/4)
        """
    def boundary(self):
        """
        Return the boundary of a 2d polyomino.

        INPUT:

        - ``self`` -- a 2d polyomino

        OUTPUT:

        - list of edges (an edge is a pair of adjacent 2d coordinates)

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0), (1,0), (0,1), (1,1)])
            sage: sorted(p.boundary())
            [((-0.5, -0.5), (-0.5, 0.5)), ((-0.5, -0.5), (0.5, -0.5)),
             ((-0.5, 0.5), (-0.5, 1.5)), ((-0.5, 1.5), (0.5, 1.5)),
             ((0.5, -0.5), (1.5, -0.5)), ((0.5, 1.5), (1.5, 1.5)),
             ((1.5, -0.5), (1.5, 0.5)), ((1.5, 0.5), (1.5, 1.5))]
            sage: len(_)
            8
            sage: p = Polyomino([(5,5)])
            sage: sorted(p.boundary())
            [((4.5, 4.5), (4.5, 5.5)), ((4.5, 4.5), (5.5, 4.5)),
             ((4.5, 5.5), (5.5, 5.5)), ((5.5, 4.5), (5.5, 5.5))]
        """
    def show3d(self, size: int = 1):
        """
        Return a 3d Graphic object representing the polyomino.

        INPUT:

        - ``self`` -- a polyomino of dimension 3
        - ``size`` -- number (default: ``1``); the size of each
          ``1 \\times 1 \\times 1`` cube. This does a homothety with respect
          to the center of the polyomino.

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0,0), (0,1,0), (1,1,0), (1,1,1)], color='blue')
            sage: p.show3d()                    # long time (2s)                        # needs sage.plot
            Graphics3d Object
        """
    def show2d(self, size: float = 0.7, color: str = 'black', thickness: int = 1):
        """
        Return a 2d Graphic object representing the polyomino.

        INPUT:

        - ``self`` -- a polyomino of dimension 2
        - ``size`` -- number (default: ``0.7``); the size of each square
        - ``color`` -- color (default: ``'black'``); color of the boundary line
        - ``thickness`` -- number (default: ``1``); how thick the boundary line is

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: p = Polyomino([(0,0),(1,0),(1,1),(1,2)], color='deeppink')
            sage: p.show2d()                    # long time (0.5s)                      # needs sage.plot
            Graphics object consisting of 17 graphics primitives
        """
    def self_surrounding(self, radius, remove_incomplete_copies: bool = True, ncpus=None):
        """
        Return a list of isometric copies of ``self`` surrounding it with an
        annulus of given radius.

        INPUT:

        - ``self`` -- a polyomino of dimension 2
        - ``radius`` -- integer
        - ``remove_incomplete_copies`` -- boolean (default: ``True``); whether
          to keep only complete copies of ``self`` in the output
        - ``ncpus`` -- integer (default: ``None``); maximal number of
          subprocesses to use at the same time. If ``None``, it detects the
          number of effective CPUs in the system using
          :func:`sage.parallel.ncpus.ncpus()`.
          If ``ncpus=1``, the first solution is searched serially.

        OUTPUT: list of polyominoes

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino
            sage: H = Polyomino([(-1, 1), (-1, 4), (-1, 7), (0, 0), (0, 1), (0, 2),
            ....: (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 1), (1, 2),
            ....: (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 0), (2, 2),
            ....: (2, 3), (2, 5), (2, 6), (2, 8)])
            sage: solution = H.self_surrounding(8)
            sage: G = sum([p.show2d() for p in solution], Graphics())                   # needs sage.plot

        ::

            sage: solution = H.self_surrounding(8, remove_incomplete_copies=False)
            sage: G = sum([p.show2d() for p in solution], Graphics())                   # needs sage.plot
        """

class TilingSolver(SageObject):
    """
    Tiling solver.

    Solve the problem of tiling a polyomino with a certain number
    of polyominoes.

    INPUT:

    - ``pieces`` -- iterable of Polyominoes
    - ``box`` -- polyomino or tuple of integers (size of a box)
    - ``rotation`` -- boolean (default: ``True``); whether to allow
      rotations
    - ``reflection`` -- boolean (default: ``False``); whether to allow
      reflections
    - ``reusable`` -- boolean (default: ``False``); whether to allow
      the pieces to be reused
    - ``outside`` -- boolean (default: ``False``); whether to allow
      pieces to partially go outside of the box (all non-empty intersection
      of the pieces with the box are considered)

    EXAMPLES:

    By default, rotations are allowed and reflections are not allowed::

        sage: from sage.combinat.tiling import TilingSolver, Polyomino
        sage: p = Polyomino([(0,0,0)])
        sage: q = Polyomino([(0,0,0), (0,0,1)])
        sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
        sage: T = TilingSolver([p,q,r], box=(1,1,6))
        sage: T
        Tiling solver of 3 pieces into a box of size 6
        Rotation allowed: True
        Reflection allowed: False
        Reusing pieces allowed: False

    Solutions are given by an iterator::

        sage: it = T.solve()
        sage: for p in next(it): p
        Polyomino: [(0, 0, 0)], Color: gray
        Polyomino: [(0, 0, 1), (0, 0, 2)], Color: gray
        Polyomino: [(0, 0, 3), (0, 0, 4), (0, 0, 5)], Color: gray

    Another solution::

        sage: for p in next(it): p
        Polyomino: [(0, 0, 0)], Color: gray
        Polyomino: [(0, 0, 1), (0, 0, 2), (0, 0, 3)], Color: gray
        Polyomino: [(0, 0, 4), (0, 0, 5)], Color: gray

    Tiling of a polyomino by polyominoes::

        sage: b = Polyomino([(0,0), (1,0), (1,1), (2,1), (1,2), (2,2), (0,3), (1,3)])
        sage: p = Polyomino([(0,0), (1,0)])
        sage: T = TilingSolver([p], box=b, reusable=True)
        sage: T.number_of_solutions()
        2

    TESTS::

        sage: T = TilingSolver([p,q,r], box=(1,1,6), rotation=False, reflection=True)
        Traceback (most recent call last):
        ...
        NotImplementedError: When reflection is allowed and rotation is not allowed
    """
    def __init__(self, pieces, box, rotation: bool = True, reflection: bool = False, reusable: bool = False, outside: bool = False) -> None:
        """
        Constructor.

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0,0)])
            sage: q = Polyomino([(0,0,0), (0,0,1)])
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,1,6))
            sage: T
            Tiling solver of 3 pieces into a box of size 6
            Rotation allowed: True
            Reflection allowed: False
            Reusing pieces allowed: False
        """
    def is_suitable(self):
        """
        Return whether the volume of the box is equal to sum of the volume
        of the polyominoes and the number of rows sent to the DLX solver is
        larger than zero.

        If these conditions are not verified, then the problem is not suitable
        in the sense that there are no solution.

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0,0)])
            sage: q = Polyomino([(0,0,0), (0,0,1)])
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,1,6))
            sage: T.is_suitable()
            True
            sage: T = TilingSolver([p,q,r], box=(1,1,7))
            sage: T.is_suitable()
            False
        """
    def pieces(self):
        """
        Return the list of pieces.

        OUTPUT: list of 3d polyominoes

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0,0)])
            sage: q = Polyomino([(0,0,0), (0,0,1)])
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,1,6))
            sage: for p in T._pieces: p
            Polyomino: [(0, 0, 0)], Color: gray
            Polyomino: [(0, 0, 0), (0, 0, 1)], Color: gray
            Polyomino: [(0, 0, 0), (0, 0, 1), (0, 0, 2)], Color: gray
        """
    def space(self):
        """
        Return an iterator over all the nonnegative integer coordinates
        contained in the space to tile.

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0,0)])
            sage: q = Polyomino([(0,0,0), (0,0,1)])
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,1,6))
            sage: list(T.space())
            [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 0, 4), (0, 0, 5)]
        """
    @cached_method
    def coord_to_int_dict(self):
        """
        Return a dictionary mapping coordinates to integers.

        OUTPUT: dictionary

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0,0)])
            sage: q = Polyomino([(0,0,0), (0,0,1)])
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,1,6))
            sage: A = T.coord_to_int_dict()
            sage: sorted(A.items())
            [((0, 0, 0), 3), ((0, 0, 1), 4), ((0, 0, 2), 5),
             ((0, 0, 3), 6), ((0, 0, 4), 7), ((0, 0, 5), 8)]

        Reusable pieces::

            sage: p = Polyomino([(0,0), (0,1)])
            sage: q = Polyomino([(0,0), (0,1), (1,0), (1,1)])
            sage: T = TilingSolver([p,q], box=[3,2], reusable=True)
            sage: B = T.coord_to_int_dict()
            sage: sorted(B.items())
            [((0, 0), 0), ((0, 1), 1), ((1, 0), 2), ((1, 1), 3),
             ((2, 0), 4), ((2, 1), 5)]
        """
    @cached_method
    def int_to_coord_dict(self):
        """
        Return a dictionary mapping integers to coordinates.

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0,0)])
            sage: q = Polyomino([(0,0,0), (0,0,1)])
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,1,6))
            sage: B = T.int_to_coord_dict()
            sage: sorted(B.items())
            [(3, (0, 0, 0)), (4, (0, 0, 1)), (5, (0, 0, 2)),
             (6, (0, 0, 3)), (7, (0, 0, 4)), (8, (0, 0, 5))]

        Reusable pieces::

            sage: from sage.combinat.tiling import Polyomino, TilingSolver
            sage: p = Polyomino([(0,0), (0,1)])
            sage: q = Polyomino([(0,0), (0,1), (1,0), (1,1)])
            sage: T = TilingSolver([p,q], box=[3,2], reusable=True)
            sage: B = T.int_to_coord_dict()
            sage: sorted(B.items())
            [(0, (0, 0)), (1, (0, 1)), (2, (1, 0)),
             (3, (1, 1)), (4, (2, 0)), (5, (2, 1))]

        TESTS:

        The methods ``int_to_coord_dict`` and ``coord_to_int_dict`` returns
        dictionary that are inverse of each other::

            sage: A = T.coord_to_int_dict()
            sage: B = T.int_to_coord_dict()
            sage: all(A[B[i]] == i for i in B)
            True
            sage: all(B[A[i]] == i for i in A)
            True
        """
    @cached_method
    def rows_for_piece(self, i, mod_box_isometries: bool = False):
        """
        Return the rows for the `i`-th piece.

        INPUT:

        - ``i`` -- integer; the `i`-th piece

        - ``mod_box_isometries`` -- boolean (default: ``False``); whether to
          consider only rows for positions up to the action of the
          quotient the group of isometries of the `n`-cube by the
          subgroup of isometries of the `a_1\\times a_2\\cdots \\times a_n`
          rectangular box where are the `a_i` are assumed to be distinct.

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0,0)])
            sage: q = Polyomino([(0,0,0), (0,0,1)])
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,1,6))
            sage: T.rows_for_piece(0)
            [[0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]]
            sage: T.rows_for_piece(1)
            [[1, 3, 4], [1, 4, 5], [1, 5, 6], [1, 6, 7], [1, 7, 8]]
            sage: T.rows_for_piece(2)
            [[2, 3, 4, 5], [2, 4, 5, 6], [2, 5, 6, 7], [2, 6, 7, 8]]

        Less rows when using ``mod_box_isometries=True``::

            sage: a = Polyomino([(0,0,0), (0,0,1), (1,0,0)])
            sage: b = Polyomino([(0,0,0), (1,0,0), (0,1,0)])
            sage: T = TilingSolver([a,b], box=(2,1,3))
            sage: T.rows_for_piece(0)
            [[0, 2, 3, 5],
             [0, 3, 4, 6],
             [0, 2, 3, 6],
             [0, 3, 4, 7],
             [0, 2, 5, 6],
             [0, 3, 6, 7],
             [0, 3, 5, 6],
             [0, 4, 6, 7]]
            sage: T.rows_for_piece(0, mod_box_isometries=True)
            [[0, 2, 3, 5], [0, 3, 4, 6]]
            sage: T.rows_for_piece(1, mod_box_isometries=True)
            [[1, 2, 3, 5], [1, 3, 4, 6]]
        """
    @cached_method
    def rows(self):
        """
        Creation of the rows.

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0,0)])
            sage: q = Polyomino([(0,0,0), (0,0,1)])
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,1,6))
            sage: rows = T.rows()
            sage: for row in rows: row
            [0, 3]
            [0, 4]
            [0, 5]
            [0, 6]
            [0, 7]
            [0, 8]
            [1, 3, 4]
            [1, 4, 5]
            [1, 5, 6]
            [1, 6, 7]
            [1, 7, 8]
            [2, 3, 4, 5]
            [2, 4, 5, 6]
            [2, 5, 6, 7]
            [2, 6, 7, 8]
        """
    def nrows_per_piece(self):
        """
        Return the number of rows necessary by each piece.

        OUTPUT: list

        EXAMPLES::

            sage: from sage.games.quantumino import QuantuminoSolver
            sage: q = QuantuminoSolver(0)
            sage: T = q.tiling_solver()
            sage: T.nrows_per_piece()             # long time (10s)
            [360, 360, 360, 360, 360, 180, 180, 672, 672, 360, 360, 180, 180, 360, 360, 180]
        """
    def starting_rows(self):
        """
        Return the starting rows for each piece.

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0,0)])
            sage: q = Polyomino([(0,0,0), (0,0,1)])
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,1,6))
            sage: T.starting_rows()
            [0, 6, 11, 15]
        """
    def row_to_polyomino(self, row_number):
        """
        Return a polyomino associated to a row.

        INPUT:

        - ``row_number`` -- integer; the `i`-th row

        OUTPUT: polyomino

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: a = Polyomino([(0,0,0), (0,0,1), (1,0,0)], color='blue')
            sage: b = Polyomino([(0,0,0), (1,0,0), (0,1,0)], color='red')
            sage: T = TilingSolver([a,b], box=(2,1,3))
            sage: len(T.rows())
            16

        ::

            sage: T.row_to_polyomino(7)
            Polyomino: [(0, 0, 2), (1, 0, 1), (1, 0, 2)], Color: blue

        ::

            sage: T.row_to_polyomino(13)
            Polyomino: [(0, 0, 1), (1, 0, 1), (1, 0, 2)], Color: red

        TESTS:

        We check that issue :issue:`32252` is fixed and that colors of
        polyominoes are properly recovered::

            sage: v = Polyomino([(0, 0), (0, 1)], color='blue')
            sage: h = Polyomino([(0, 0), (1, 0)], color='red')
            sage: T = TilingSolver(pieces=[v, h], box=(2, 2),
            ....:                  rotation=False, reflection=False, reusable=True)
            sage: for i in range(4): print(i,T.row_to_polyomino(i))
            0 Polyomino: [(0, 0), (0, 1)], Color: blue
            1 Polyomino: [(1, 0), (1, 1)], Color: blue
            2 Polyomino: [(0, 0), (1, 0)], Color: red
            3 Polyomino: [(0, 1), (1, 1)], Color: red
        """
    def dlx_solver(self):
        """
        Return the sage DLX solver of that tiling problem.

        OUTPUT: dLX Solver

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0,0)])
            sage: q = Polyomino([(0,0,0), (0,0,1)])
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,1,6))
            sage: T.dlx_solver()
            Dancing links solver for 9 columns and 15 rows
        """
    def solve(self, partial=None) -> Generator[Incomplete]:
        """
        Return an iterator of list of polyominoes that are an exact cover
        of the box.

        INPUT:

        - ``partial`` -- string (default: ``None``); whether to
          include partial (incomplete) solutions. It can be one of the
          following:

          - ``None`` -- include only complete solution
          - ``'common_prefix'`` -- common prefix between two consecutive solutions
          - ``'incremental'`` -- one piece change at a time

        OUTPUT: iterator of list of polyominoes

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0,0)])
            sage: q = Polyomino([(0,0,0), (0,0,1)])
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,1,6))
            sage: it = T.solve()
            sage: for p in next(it): p
            Polyomino: [(0, 0, 0)], Color: gray
            Polyomino: [(0, 0, 1), (0, 0, 2)], Color: gray
            Polyomino: [(0, 0, 3), (0, 0, 4), (0, 0, 5)], Color: gray
            sage: for p in next(it): p
            Polyomino: [(0, 0, 0)], Color: gray
            Polyomino: [(0, 0, 1), (0, 0, 2), (0, 0, 3)], Color: gray
            Polyomino: [(0, 0, 4), (0, 0, 5)], Color: gray
            sage: for p in next(it): p
            Polyomino: [(0, 0, 0), (0, 0, 1)], Color: gray
            Polyomino: [(0, 0, 2), (0, 0, 3), (0, 0, 4)], Color: gray
            Polyomino: [(0, 0, 5)], Color: gray

        Including the partial solutions::

            sage: it = T.solve(partial='common_prefix')
            sage: for p in next(it): p
            Polyomino: [(0, 0, 0)], Color: gray
            Polyomino: [(0, 0, 1), (0, 0, 2)], Color: gray
            Polyomino: [(0, 0, 3), (0, 0, 4), (0, 0, 5)], Color: gray
            sage: for p in next(it): p
            Polyomino: [(0, 0, 0)], Color: gray
            sage: for p in next(it): p
            Polyomino: [(0, 0, 0)], Color: gray
            Polyomino: [(0, 0, 1), (0, 0, 2), (0, 0, 3)], Color: gray
            Polyomino: [(0, 0, 4), (0, 0, 5)], Color: gray
            sage: for p in next(it): p
            sage: for p in next(it): p
            Polyomino: [(0, 0, 0), (0, 0, 1)], Color: gray
            Polyomino: [(0, 0, 2), (0, 0, 3), (0, 0, 4)], Color: gray
            Polyomino: [(0, 0, 5)], Color: gray

        Colors are preserved when the polyomino can be reused::

            sage: p = Polyomino([(0,0,0)], color='yellow')
            sage: q = Polyomino([(0,0,0), (0,0,1)], color='yellow')
            sage: r = Polyomino([(0,0,0), (0,0,1), (0,0,2)], color='yellow')
            sage: T = TilingSolver([p,q,r], box=(1,1,6), reusable=True)
            sage: it = T.solve()
            sage: for p in next(it): p
            Polyomino: [(0, 0, 0)], Color: yellow
            Polyomino: [(0, 0, 1)], Color: yellow
            Polyomino: [(0, 0, 2)], Color: yellow
            Polyomino: [(0, 0, 3)], Color: yellow
            Polyomino: [(0, 0, 4)], Color: yellow
            Polyomino: [(0, 0, 5)], Color: yellow

        TESTS::

            sage: T = TilingSolver([p,q,r], box=(1,1,7))
            sage: next(T.solve())
            Traceback (most recent call last):
            ...
            StopIteration
        """
    def number_of_solutions(self):
        """
        Return the number of distinct solutions.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.combinat.tiling import TilingSolver, Polyomino
            sage: p = Polyomino([(0,0)])
            sage: q = Polyomino([(0,0), (0,1)])
            sage: r = Polyomino([(0,0), (0,1), (0,2)])
            sage: T = TilingSolver([p,q,r], box=(1,6))
            sage: T.number_of_solutions()
            6

        ::

            sage: T = TilingSolver([p,q,r], box=(1,7))
            sage: T.number_of_solutions()
            0
        """
    def animate(self, partial=None, stop=None, size: float = 0.75, axes: bool = False):
        """
        Return an animation of evolving solutions.

        INPUT:

        - ``partial`` -- string (default: ``None``); whether to
          include partial (incomplete) solutions. It can be one of the
          following:

          - ``None`` -- include only complete solutions
          - ``'common_prefix'`` -- common prefix between two consecutive solutions
          - ``'incremental'`` -- one piece change at a time

        - ``stop`` -- integer (default: ``None``); number of frames

        - ``size`` -- number (default: ``0.75``); the size of each
          ``1 \\times 1`` square. This does a homothety with respect
          to the center of each polyomino.

        - ``axes`` -- boolean (default: ``False``); whether the x and
          y axes are shown

        EXAMPLES::

            sage: from sage.combinat.tiling import Polyomino, TilingSolver
            sage: y = Polyomino([(0,0),(1,0),(2,0),(3,0),(2,1)], color='cyan')
            sage: T = TilingSolver([y], box=(5,10), reusable=True, reflection=True)
            sage: a = T.animate()                                                       # needs sage.plot
            sage: a                             # long time, optional - imagemagick, needs sage.plot
            Animation with 10 frames

        Include partial solutions (common prefix between two consecutive
        solutions)::

            sage: a = T.animate('common_prefix')                                        # needs sage.plot
            sage: a                             # long time, optional - imagemagick, needs sage.plot
            Animation with 19 frames

        Incremental solutions (one piece removed or added at a time)::

            sage: a = T.animate('incremental')  # long time (2s)                        # needs sage.plot
            sage: a                             # long time (2s), optional - imagemagick, needs sage.plot
            Animation with 123 frames

        ::

            sage: a.show()                      # long time, optional - imagemagick, needs sage.plot

        The ``show`` function takes arguments to specify the delay between
        frames (measured in hundredths of a second, default value 20) and
        the number of iterations (default: 0, which means to iterate
        forever). To iterate 4 times with half a second between each frame::

            sage: a.show(delay=50, iterations=4)        # long time, optional - imagemagick, needs sage.plot

        Limit the number of frames::

            sage: a = T.animate('incremental', stop=13); a      # not tested            # needs sage.plot
            Animation with 13 frames
        """
