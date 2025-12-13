from _typeshed import Incomplete
from sage.combinat.words.morphism import WordMorphism as WordMorphism
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import det as det
from sage.misc.latex import LatexExpr as LatexExpr
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.richcmp import richcmp_by_eq_and_lt as richcmp_by_eq_and_lt, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

cm: Incomplete

class Face(SageObject):
    """
    A class to model a unit face of arbitrary dimension.

    A unit face in dimension `d` is represented by
    a `d`-dimensional vector ``v`` and a type ``t`` in `\\{1, \\ldots, d\\}`.
    The type of the face corresponds to the canonical unit vector
    to which the face is orthogonal.
    The optional ``color`` argument is used in plotting functions.

    INPUT:

    - ``v`` -- tuple of integers
    - ``t`` -- integer in ``[1, ..., len(v)]``, type of the face. The face of type `i`
      is orthogonal to the canonical vector `e_i`.
    - ``color`` -- color (default: ``None``); color of the face,
      used for plotting only. If ``None``, its value is guessed from the
      face type.

    EXAMPLES::

        sage: from sage.combinat.e_one_star import Face
        sage: f = Face((0,2,0), 3)
        sage: f.vector()
        (0, 2, 0)
        sage: f.type()
        3

    ::

        sage: f = Face((0,2,0), 3, color=(0.5, 0.5, 0.5))
        sage: f.color()
        RGB color (0.5, 0.5, 0.5)
    """
    def __init__(self, v, t, color=None) -> None:
        """
        Face constructor. See class doc for more information.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face
            sage: f = Face((0,2,0), 3)
            sage: f.vector()
            (0, 2, 0)
            sage: f.type()
            3

        TESTS:

        We test that types can be given by an int (see :issue:`10699`)::

            sage: f = Face((0,2,0), int(1))
        """
    __richcmp__: Incomplete
    def __hash__(self) -> int:
        """
        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face
            sage: f = Face((0,0,0,3), 3)
            sage: g = Face((0,0,0,3), 3)
            sage: hash(f) == hash(g)
            True
        """
    def __add__(self, other):
        """
        Addition of ``self`` with a Face, a Patch or a finite iterable of faces.

        INPUT:

        - ``other`` -- a Patch or a Face or a finite iterable of faces

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: f = Face([0,0,0], 3)
            sage: g = Face([0,1,-1], 2)
            sage: f + g
            Patch: [[(0, 0, 0), 3]*, [(0, 1, -1), 2]*]
            sage: P = Patch([Face([0,0,0], 1), Face([0,0,0], 2)])
            sage: f + P
            Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(0, 0, 0), 3]*]

        Adding a finite iterable of faces::

            sage: from sage.combinat.e_one_star import Face
            sage: f = Face([0,0,0], 3)
            sage: f + [f,f]
            Patch: [[(0, 0, 0), 3]*]
        """
    def vector(self):
        """
        Return the vector of the face.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face
            sage: f = Face((0,2,0), 3)
            sage: f.vector()
            (0, 2, 0)
        """
    def type(self):
        """
        Return the type of the face.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face
            sage: f = Face((0,2,0), 3)
            sage: f.type()
            3

        ::

            sage: f = Face((0,2,0), 3)
            sage: f.type()
            3
        """
    def color(self, color=None):
        """
        Return or change the color of the face.

        INPUT:

        - ``color`` -- string, rgb tuple, color (default: ``None``)
          the new color to assign to the face. If ``None``, it returns the
          color of the face.

        OUTPUT: color or None

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face
            sage: f = Face((0,2,0), 3)
            sage: f.color()
            RGB color (0.0, 0.0, 1.0)
            sage: f.color('red')
            sage: f.color()
            RGB color (1.0, 0.0, 0.0)
        """

class Patch(SageObject):
    """
    A class to model a collection of faces. A patch is represented by an immutable set of Faces.

    .. NOTE::

        The dimension of a patch is the length of the vectors of the faces in the patch,
        which is assumed to be the same for every face in the patch.

    .. NOTE::

        Since version 4.7.1, Patches are immutable, except for the colors of the faces,
        which are not taken into account for equality tests and hash functions.

    INPUT:

    - ``faces`` -- finite iterable of faces
    - ``face_contour`` -- dictionary (default: ``None``); maps the face
      type to vectors describing the contour of unit faces. If ``None``,
      defaults contour are assumed for faces of type 1, 2, 3 or 1, 2, 3.
      Used in plotting methods only.

    EXAMPLES::

        sage: from sage.combinat.e_one_star import Face, Patch
        sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
        sage: P
        Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(0, 0, 0), 3]*]

    ::

        sage: face_contour = {}
        sage: face_contour[1] = map(vector, [(0,0,0),(0,1,0),(0,1,1),(0,0,1)])
        sage: face_contour[2] = map(vector, [(0,0,0),(0,0,1),(1,0,1),(1,0,0)])
        sage: face_contour[3] = map(vector, [(0,0,0),(1,0,0),(1,1,0),(0,1,0)])
        sage: Patch([Face((0,0,0),t) for t in [1,2,3]], face_contour=face_contour)
        Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(0, 0, 0), 3]*]
    """
    def __init__(self, faces, face_contour=None) -> None:
        """
        Constructor of a patch (set of faces).

        See class doc for more information.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: P
            Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(0, 0, 0), 3]*]

        TESTS:

        We test that colors are not anymore mixed up between
        Patches (see :issue:`11255`)::

            sage: P = Patch([Face([0,0,0],2)])
            sage: Q = Patch(P)
            sage: next(iter(P)).color()
            RGB color (0.0, 1.0, 0.0)
            sage: next(iter(Q)).color('yellow')
            sage: next(iter(P)).color()
            RGB color (0.0, 1.0, 0.0)
        """
    def __eq__(self, other) -> bool:
        """
        Equality test for Patch.

        INPUT:

        - ``other`` -- an object

        EXAMPLES::

            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: P = Patch([Face((0,0,0),1), Face((0,0,0),2), Face((0,0,0),3)])
            sage: Q = Patch([Face((0,1,0),1), Face((0,0,0),3)])
            sage: P == P
            True
            sage: P == Q
            False
            sage: P == 4
            False

        ::

            sage: s = WordMorphism({1:[1,3], 2:[1,2,3], 3:[3]})
            sage: t = WordMorphism({1:[1,2,3], 2:[2,3], 3:[3]})
            sage: P = Patch([Face((0,0,0), 1), Face((0,0,0), 2), Face((0,0,0), 3)])
            sage: E1Star(s)(P) == E1Star(t)(P)
            False
            sage: E1Star(s*t)(P) == E1Star(t)(E1Star(s)(P))
            True
        """
    def __hash__(self) -> int:
        """
        Hash function of Patch.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: x = [Face((0,0,0),t) for t in [1,2,3]]
            sage: P = Patch(x)
            sage: hash(P)      #random
            -4839605361791007520

        TESTS:

        We test that two equal patches have the same hash (see :issue:`11255`)::

            sage: P = Patch([Face([0,0,0],1), Face([0,0,0],2)])
            sage: Q = Patch([Face([0,0,0],2), Face([0,0,0],1)])
            sage: P == Q
            True
            sage: hash(P) == hash(Q)
            True

        Changing the color does not affect the hash value::

            sage: p = Patch([Face((0,0,0), t) for t in [1,2,3]])
            sage: H1 = hash(p)
            sage: p.repaint(['blue'])
            sage: H2 = hash(p)
            sage: H1 == H2
            True
        """
    def __len__(self) -> int:
        """
        Return the number of faces contained in the patch.

        OUTPUT: integer

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: x = [Face((0,0,0),t) for t in [1,2,3]]
            sage: P = Patch(x)
            sage: len(P)       #indirect doctest
            3
        """
    def __iter__(self):
        """
        Return an iterator over the faces of the patch.

        OUTPUT: iterator

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: x = [Face((0,0,0),t) for t in [1,2,3]]
            sage: P = Patch(x)
            sage: it = iter(P)
            sage: type(next(it))
            <class 'sage.combinat.e_one_star.Face'>
            sage: type(next(it))
            <class 'sage.combinat.e_one_star.Face'>
            sage: type(next(it))
            <class 'sage.combinat.e_one_star.Face'>
            sage: type(next(it))
            Traceback (most recent call last):
            ...
            StopIteration
        """
    def __add__(self, other):
        """
        Addition of patches (union).

        INPUT:

        - ``other`` -- a Patch or a Face or a finite iterable of faces

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: P = Patch([Face([0,0,0], 1), Face([0,0,0], 2)])
            sage: Q = P.translate([1,-1,0])
            sage: P + Q
            Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(1, -1, 0), 1]*, [(1, -1, 0), 2]*]
            sage: P + Face([0,0,0],3)
            Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(0, 0, 0), 3]*]
            sage: P + [Face([0,0,0],3), Face([1,1,1],2)]
            Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(0, 0, 0), 3]*, [(1, 1, 1), 2]*]
        """
    def __sub__(self, other):
        """
        Subtraction of patches (difference).

        INPUT:

        - ``other`` -- a Patch or a Face or a finite iterable of faces

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: P - Face([0,0,0],2)
            Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 3]*]
            sage: P - P
            Patch: []
        """
    def union(self, other) -> Patch:
        """
        Return a Patch consisting of the union of ``self`` and ``other``.

        INPUT:

        - ``other`` -- a Patch or a Face or a finite iterable of faces

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: P = Patch([Face((0,0,0),1), Face((0,0,0),2)])
            sage: P.union(Face((1,2,3), 3))
            Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(1, 2, 3), 3]*]
            sage: P.union([Face((1,2,3), 3), Face((2,3,3), 2)])
            Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(1, 2, 3), 3]*, [(2, 3, 3), 2]*]
        """
    def difference(self, other) -> Patch:
        """
        Return the difference of ``self`` and ``other``.

        INPUT:

        - ``other`` -- a finite iterable of faces or a single face

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: P.difference(Face([0,0,0],2))
            Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 3]*]
            sage: P.difference(P)
            Patch: []
        """
    def dimension(self) -> None | int:
        """
        Return the dimension of the vectors of the faces of ``self``.

        It returns ``None`` if ``self`` is the empty patch.

        The dimension of a patch is the length of the vectors of the faces in the patch,
        which is assumed to be the same for every face in the patch.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: P.dimension()
            3

        TESTS::

            sage: from sage.combinat.e_one_star import Patch
            sage: p = Patch([])
            sage: p.dimension() is None
            True

        It works when the patch is created from an iterator::

            sage: p = Patch(Face((0,0,0),t) for t in [1,2,3])
            sage: p.dimension()
            3
        """
    def faces_of_vector(self, v) -> list[Face]:
        """
        Return a list of the faces whose vector is ``v``.

        INPUT:

        - ``v`` -- a vector

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: P = Patch([Face((0,0,0),1), Face((1,2,0),3), Face((1,2,0),1)])
            sage: sorted(P.faces_of_vector([1,2,0]))
            [[(1, 2, 0), 1]*, [(1, 2, 0), 3]*]
        """
    def faces_of_type(self, t) -> list[Face]:
        """
        Return a list of the faces that have type ``t``.

        INPUT:

        - ``t`` -- integer or any other type

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: P = Patch([Face((0,0,0),1), Face((1,2,0),3), Face((1,2,0),1)])
            sage: sorted(P.faces_of_type(1))
            [[(0, 0, 0), 1]*, [(1, 2, 0), 1]*]
        """
    def faces_of_color(self, color) -> list[Face]:
        """
        Return a list of the faces that have the given color.

        INPUT:

        - ``color`` -- color

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: P = Patch([Face((0,0,0),1, 'red'), Face((1,2,0),3, 'blue'), Face((1,2,0),1, 'red')])
            sage: sorted(P.faces_of_color('red'))
            [[(0, 0, 0), 1]*, [(1, 2, 0), 1]*]
        """
    def translate(self, v) -> Patch:
        """
        Return a translated copy of ``self`` by vector `v`.

        INPUT:

        - ``v`` -- vector or tuple

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: P = Patch([Face((0,0,0),1), Face((1,2,0),3), Face((1,2,0),1)])
            sage: P.translate([-1,-2,0])
            Patch: [[(-1, -2, 0), 1]*, [(0, 0, 0), 1]*, [(0, 0, 0), 3]*]
        """
    def occurrences_of(self, other) -> list:
        """
        Return all positions at which other appears in self, that is,
        all vectors v such that ``set(other.translate(v)) <= set(self)``.

        INPUT:

        - ``other`` -- a Patch

        OUTPUT: list of vectors

        EXAMPLES::

            sage: from sage.combinat.e_one_star import Face, Patch, E1Star
            sage: P = Patch([Face([0,0,0], 1), Face([0,0,0], 2), Face([0,0,0], 3)])
            sage: Q = Patch([Face([0,0,0], 1), Face([0,0,0], 2)])
            sage: P.occurrences_of(Q)
            [(0, 0, 0)]
            sage: Q = Q.translate([1,2,3])
            sage: P.occurrences_of(Q)
            [(-1, -2, -3)]

        ::

            sage: E = E1Star(WordMorphism({1:[1,2], 2:[1,3], 3:[1]}))
            sage: P = Patch([Face([0,0,0], 1), Face([0,0,0], 2), Face([0,0,0], 3)])
            sage: P = E(P,4)
            sage: Q = Patch([Face([0,0,0], 1), Face([0,0,0], 2)])
            sage: L = P.occurrences_of(Q)
            sage: sorted(L)
            [(0, 0, 0), (0, 0, 1), (0, 1, -1), (1, 0, -1), (1, 1, -3), (1, 1, -2)]
        """
    def repaint(self, cmap: str = 'Set1') -> None:
        """
        Repaint all the faces of ``self`` from the given color map.

        This only changes the colors of the faces of ``self``.

        INPUT:

        - ``cmap`` -- color map (default: ``'Set1'``). It can be one of the
          following:

           - ``string`` -- a coloring map; for available coloring map names type:
             ``sorted(colormaps)``
           - ``list`` -- list of colors to assign cyclically to the faces
             A list of a single color colors all the faces with the same color
           - ``dict`` -- dictionary of face types mapped to colors, to color the
             faces according to their type
           - ``{}``, the empty dict -- shortcut for
             ``{1:'red', 2:'green', 3:'blue'}``

        EXAMPLES:

        Using a color map::

            sage: from sage.combinat.e_one_star import Face, Patch
            sage: color = (0, 0, 0)
            sage: P = Patch([Face((0,0,0),t,color) for t in [1,2,3]])
            sage: for f in P: f.color()
            RGB color (0.0, 0.0, 0.0)
            RGB color (0.0, 0.0, 0.0)
            RGB color (0.0, 0.0, 0.0)
            sage: P.repaint()
            sage: next(iter(P)).color()    #random
            RGB color (0.498..., 0.432..., 0.522...)

        Using a list of colors::

            sage: P = Patch([Face((0,0,0),t,color) for t in [1,2,3]])
            sage: P.repaint([(0.9, 0.9, 0.9), (0.65,0.65,0.65), (0.4,0.4,0.4)])
            sage: for f in P: f.color()
            RGB color (0.9, 0.9, 0.9)
            RGB color (0.65, 0.65, 0.65)
            RGB color (0.4, 0.4, 0.4)

        Using a dictionary to color faces according to their type::

            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: P.repaint({1:'black', 2:'yellow', 3:'green'})
            sage: P.plot()                   #not tested
            sage: P.repaint({})
            sage: P.plot()                   #not tested
        """
    def plot(self, projmat=None, opacity: float = 0.75) -> Graphics:
        """
        Return a 2D graphic object depicting the patch.

        INPUT:

        - ``projmat`` -- matrix (default: ``None``); the projection
          matrix. Its number of lines must be two. Its number of columns
          must equal the dimension of the ambient space of the faces. If
          ``None``, the isometric projection is used by default.

        - ``opacity`` -- float between ``0`` and ``1`` (default: ``0.75``)
          opacity of the face

        .. WARNING::

            Plotting is implemented only for patches in two or three dimensions.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: P.plot()                                                              # needs sage.plot
            Graphics object consisting of 3 graphics primitives

        ::

            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: P = E(P, 5)
            sage: P.plot()                                                              # needs sage.plot
            Graphics object consisting of 57 graphics primitives

        Plot with a different projection matrix::

            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: M = matrix(2, 3, [1,0,-1,0.3,1,-3])
            sage: P = E(P, 3)
            sage: P.plot(projmat=M)                                                     # needs sage.plot
            Graphics object consisting of 17 graphics primitives

        Plot patches made of unit segments::

            sage: P = Patch([Face([0,0], 1), Face([0,0], 2)])
            sage: E = E1Star(WordMorphism({1:[1,2],2:[1]}))
            sage: F = E1Star(WordMorphism({1:[1,1,2],2:[2,1]}))
            sage: E(P,5).plot()                                                         # needs sage.plot
            Graphics object consisting of 21 graphics primitives
            sage: F(P,3).plot()                                                         # needs sage.plot
            Graphics object consisting of 34 graphics primitives
        """
    def plot3d(self):
        """
        Return a 3D graphics object depicting the patch.

        .. WARNING::

            3D plotting is implemented only for patches in three dimensions.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: P.plot3d()                #not tested

        ::

            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: P = E(P, 5)
            sage: P.repaint()
            sage: P.plot3d()                #not tested
        """
    def plot_tikz(self, projmat=None, print_tikz_env: bool = True, edgecolor: str = 'black', scale: float = 0.25, drawzero: bool = False, extra_code_before: str = '', extra_code_after: str = '') -> str:
        '''
        Return a string containing some TikZ code to be included into
        a LaTeX document, depicting the patch.

        .. WARNING::

            Tikz Plotting is implemented only for patches in three dimensions.

        INPUT:

        - ``projmat`` -- matrix (default: ``None``); the projection
          matrix. Its number of lines must be two. Its number of columns
          must equal the dimension of the ambient space of the faces. If
          ``None``, the isometric projection is used by default.
        - ``print_tikz_env`` -- boolean (default: ``True``); if ``True``,
          the tikzpicture environment are printed
        - ``edgecolor`` -- string (default: ``\'black\'``); either
          ``\'black\'`` or ``\'facecolor\'`` (color of unit face edges)
        - ``scale`` -- real number (default: ``0.25``) scaling
          constant for the whole figure
        - ``drawzero`` -- boolean (default: ``False``); if ``True``,
          mark the origin by a black dot
        - ``extra_code_before`` -- string (default: ``\'\'``); extra code to
          include in the tikz picture
        - ``extra_code_after`` -- string (default: ``\'\'``); extra code to
          include in the tikz picture

        EXAMPLES::

            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: s = P.plot_tikz()
            sage: len(s)
            602
            sage: print(s)       #not tested
            \\begin{tikzpicture}
            [x={(-0.216506cm,-0.125000cm)}, y={(0.216506cm,-0.125000cm)}, z={(0.000000cm,0.250000cm)}]
            \\definecolor{facecolor}{rgb}{0.000,1.000,0.000}
            \\fill[fill=facecolor, draw=black, shift={(0,0,0)}]
            (0, 0, 0) -- (0, 0, 1) -- (1, 0, 1) -- (1, 0, 0) -- cycle;
            \\definecolor{facecolor}{rgb}{1.000,0.000,0.000}
            \\fill[fill=facecolor, draw=black, shift={(0,0,0)}]
            (0, 0, 0) -- (0, 1, 0) -- (0, 1, 1) -- (0, 0, 1) -- cycle;
            \\definecolor{facecolor}{rgb}{0.000,0.000,1.000}
            \\fill[fill=facecolor, draw=black, shift={(0,0,0)}]
            (0, 0, 0) -- (1, 0, 0) -- (1, 1, 0) -- (0, 1, 0) -- cycle;
            \\end{tikzpicture}

        ::

            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: P = E(P, 4)
            sage: from sage.misc.latex import latex             #not tested
            sage: latex.add_to_preamble(\'\\\\usepackage{tikz}\')   #not tested
            sage: view(P)                       #not tested

        Plot using shades of gray (useful for article figures)::

            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: P.repaint([(0.9, 0.9, 0.9), (0.65,0.65,0.65), (0.4,0.4,0.4)])
            sage: P = E(P, 4)
            sage: s = P.plot_tikz()

        Plotting with various options::

            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: M = matrix(2,3,[float(u) for u in [1,0,-0.7071,0,1,-0.7071]])
            sage: P = E(P, 3)
            sage: s = P.plot_tikz(projmat=M, edgecolor=\'facecolor\', scale=0.6, drawzero=True)

        Adding X, Y, Z axes using the extra code feature::

            sage: length = 1.5
            sage: space = 0.3
            sage: axes = \'\'
            sage: axes += "\\\\draw[->, thick, black] (0,0,0) -- (%s, 0, 0);\\n" % length
            sage: axes += "\\\\draw[->, thick, black] (0,0,0) -- (0, %s, 0);\\n" % length
            sage: axes += "\\\\node at (%s,0,0) {$x$};\\n" % (length + space)
            sage: axes += "\\\\node at (0,%s,0) {$y$};\\n" % (length + space)
            sage: axes += "\\\\node at (0,0,%s) {$z$};\\n" % (length + space)
            sage: axes += "\\\\draw[->, thick, black] (0,0,0) -- (0, 0, %s);\\n" % length
            sage: cube = Patch([Face((0,0,0),1), Face((0,0,0),2), Face((0,0,0),3)])
            sage: options = dict(scale=0.5,drawzero=True,extra_code_before=axes)
            sage: s = cube.plot_tikz(**options)
            sage: len(s)
            986
            sage: print(s)   #not tested
            \\begin{tikzpicture}
            [x={(-0.433013cm,-0.250000cm)}, y={(0.433013cm,-0.250000cm)}, z={(0.000000cm,0.500000cm)}]
            \\draw[->, thick, black] (0,0,0) -- (1.50000000000000, 0, 0);
            \\draw[->, thick, black] (0,0,0) -- (0, 1.50000000000000, 0);
            \\node at (1.80000000000000,0,0) {$x$};
            \\node at (0,1.80000000000000,0) {$y$};
            \\node at (0,0,1.80000000000000) {$z$};
            \\draw[->, thick, black] (0,0,0) -- (0, 0, 1.50000000000000);
            \\definecolor{facecolor}{rgb}{0.000,1.000,0.000}
            \\fill[fill=facecolor, draw=black, shift={(0,0,0)}]
            (0, 0, 0) -- (0, 0, 1) -- (1, 0, 1) -- (1, 0, 0) -- cycle;
            \\definecolor{facecolor}{rgb}{1.000,0.000,0.000}
            \\fill[fill=facecolor, draw=black, shift={(0,0,0)}]
            (0, 0, 0) -- (0, 1, 0) -- (0, 1, 1) -- (0, 0, 1) -- cycle;
            \\definecolor{facecolor}{rgb}{0.000,0.000,1.000}
            \\fill[fill=facecolor, draw=black, shift={(0,0,0)}]
            (0, 0, 0) -- (1, 0, 0) -- (1, 1, 0) -- (0, 1, 0) -- cycle;
            \\node[circle,fill=black,draw=black,minimum size=1.5mm,inner sep=0pt] at (0,0,0) {};
            \\end{tikzpicture}
        '''

class E1Star(SageObject):
    """
    A class to model the `E_1^*(\\sigma)` map associated with
    a unimodular substitution `\\sigma`.

    INPUT:

    - ``sigma`` -- unimodular ``WordMorphism``, i.e. such that its incidence
      matrix has determinant `\\pm 1`

    - ``method`` -- 'prefix' or 'suffix' (default: ``'suffix'``);
      enables to use an alternative definition `E_1^*(\\sigma)` substitutions,
      where the abelianized of the prefix` is used instead of the suffix

    .. NOTE::

        The alphabet of the domain and the codomain of `\\sigma` must be
        equal, and they must be of the form ``[1, ..., d]``, where ``d``
        is a positive integer corresponding to the length of the vectors
        of the faces on which `E_1^*(\\sigma)` will act.

    EXAMPLES::

        sage: from sage.combinat.e_one_star import E1Star, Face, Patch
        sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
        sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
        sage: E = E1Star(sigma)
        sage: E(P)
        Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(0, 0, 0), 3]*, [(0, 1, -1), 2]*, [(1, 0, -1), 1]*]

    ::

        sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
        sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
        sage: E = E1Star(sigma, method='prefix')
        sage: E(P)
        Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(0, 0, 0), 3]*, [(0, 0, 1), 1]*, [(0, 0, 1), 2]*]

    ::

        sage: x = [Face((0,0,0,0),1), Face((0,0,0,0),4)]
        sage: P = Patch(x)
        sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1,4], 4:[1]})
        sage: E = E1Star(sigma)
        sage: E(P)
        Patch: [[(0, 0, 0, 0), 3]*, [(0, 0, 0, 0), 4]*, [(0, 0, 1, -1), 3]*, [(0, 1, 0, -1), 2]*, [(1, 0, 0, -1), 1]*]
    """
    def __init__(self, sigma, method: str = 'suffix') -> None:
        """
        E1Star constructor. See class doc for more information.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: E
            E_1^*(1->12, 2->13, 3->1)
        """
    def __eq__(self, other) -> bool:
        """
        Equality test for E1Star morphisms.

        INPUT:

        - ``other`` -- an object

        EXAMPLES::

            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: s = WordMorphism({1:[1,3], 2:[1,2,3], 3:[3]})
            sage: t = WordMorphism({1:[1,2,3], 2:[2,3], 3:[3]})
            sage: S = E1Star(s)
            sage: T = E1Star(t)
            sage: S == T
            False
            sage: S2 = E1Star(s, method='prefix')
            sage: S == S2
            False
        """
    def __call__(self, patch, iterations: int = 1) -> Patch:
        """
        Applies a generalized substitution to a Patch; this returns a new object.

        The color of every new face in the image is given the same color as its preimage.

        INPUT:

        - ``patch`` -- a patch
        - ``iterations`` -- integer (default: 1); number of iterations

        OUTPUT: a patch

        EXAMPLES::

            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: E(P)
            Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(0, 0, 0), 3]*, [(0, 1, -1), 2]*, [(1, 0, -1), 1]*]
            sage: E(P, iterations=4)
            Patch of 31 faces

        TESTS:

        We test that iterations=0 works (see :issue:`10699`)::

            sage: P = Patch([Face((0,0,0),t) for t in [1,2,3]])
            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: E(P, iterations=0)
            Patch: [[(0, 0, 0), 1]*, [(0, 0, 0), 2]*, [(0, 0, 0), 3]*]
        """
    def __mul__(self, other) -> E1Star:
        """
        Return the product of ``self`` and ``other``.

        The product satisfies the following rule:
        `E_1^*(\\sigma\\circ\\sigma') = E_1^*(\\sigma')` \\circ  E_1^*(\\sigma)`

        INPUT:

        - ``other`` -- an instance of E1Star

        OUTPUT: an instance of E1Star

        EXAMPLES::

            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: s = WordMorphism({1:[2],2:[3],3:[1,2]})
            sage: t = WordMorphism({1:[1,3,1],2:[1],3:[1,1,3,2]})
            sage: E1Star(s) * E1Star(t)
            E_1^*(1->1, 2->1132, 3->1311)
            sage: E1Star(t * s)
            E_1^*(1->1, 2->1132, 3->1311)
        """
    @cached_method
    def matrix(self):
        """
        Return the matrix associated with ``self``.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: E.matrix()
            [1 1 1]
            [1 0 0]
            [0 1 0]
        """
    @cached_method
    def inverse_matrix(self):
        """
        Return the inverse of the matrix associated with ``self``.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: E.inverse_matrix()
            [ 0  1  0]
            [ 0  0  1]
            [ 1 -1 -1]
        """
    def sigma(self) -> WordMorphism:
        """
        Return the ``WordMorphism`` associated with ``self``.

        EXAMPLES::

            sage: from sage.combinat.e_one_star import E1Star, Face, Patch
            sage: sigma = WordMorphism({1:[1,2], 2:[1,3], 3:[1]})
            sage: E = E1Star(sigma)
            sage: E.sigma()
            WordMorphism: 1->12, 2->13, 3->1
        """
