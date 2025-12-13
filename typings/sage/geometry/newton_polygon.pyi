from _typeshed import Incomplete
from sage.geometry.polyhedron.constructor import Polyhedron as Polyhedron
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.infinity import Infinity as Infinity
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import op_EQ as op_EQ, op_GE as op_GE, op_LE as op_LE, op_LT as op_LT, op_NE as op_NE
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class NewtonPolygon_element(Element):
    """
    Class for infinite Newton polygons with last slope.
    """
    def __init__(self, polyhedron, parent) -> None:
        """
        Initialize a Newton polygon.

        INPUT:

        - ``polyhedron`` -- a polyhedron defining the Newton polygon

        TESTS::

            sage: from sage.geometry.newton_polygon import NewtonPolygon
            sage: NewtonPolygon([ (0,0), (1,1), (3,5) ])
            Finite Newton polygon with 3 vertices: (0, 0), (1, 1), (3, 5)

            sage: NewtonPolygon([ (0,0), (1,1), (2,8), (3,5) ], last_slope=3)
            Infinite Newton polygon with 3 vertices: (0, 0), (1, 1), (3, 5)
            ending by an infinite line of slope 3

        ::

            sage: TestSuite(NewtonPolygon).run()
        """
    def vertices(self, copy: bool = True) -> list:
        """
        Return the list of vertices of this Newton polygon.

        INPUT:

        - ``copy`` -- boolean (default: ``True``)

        OUTPUT: the list of vertices of this Newton polygon (or a copy of it
        if ``copy`` is set to ``True``)

        EXAMPLES::

            sage: from sage.geometry.newton_polygon import NewtonPolygon
            sage: NP = NewtonPolygon([ (0,0), (1,1), (2,5) ]); NP
            Finite Newton polygon with 3 vertices: (0, 0), (1, 1), (2, 5)

            sage: v = NP.vertices(); v
            [(0, 0), (1, 1), (2, 5)]

        TESTS::

            sage: del v[0]
            sage: v
            [(1, 1), (2, 5)]
            sage: NP.vertices()
            [(0, 0), (1, 1), (2, 5)]
        """
    @cached_method
    def last_slope(self):
        """
        Return the last (infinite) slope of this Newton polygon
        if it is infinite and ``+Infinity`` otherwise.

        EXAMPLES::

            sage: from sage.geometry.newton_polygon import NewtonPolygon
            sage: NP1 = NewtonPolygon([ (0,0), (1,1), (2,8), (3,5) ], last_slope=3)
            sage: NP1.last_slope()
            3

            sage: NP2 = NewtonPolygon([ (0,0), (1,1), (2,5) ])
            sage: NP2.last_slope()
            +Infinity

        We check that the last slope of a sum (resp. a product) is the
        minimum of the last slopes of the summands (resp. the factors)::

            sage: (NP1 + NP2).last_slope()
            3
            sage: (NP1 * NP2).last_slope()
            3
        """
    def slopes(self, repetition: bool = True) -> list:
        """
        Return the slopes of this Newton polygon.

        INPUT:

        - ``repetition`` -- boolean (default: ``True``)

        OUTPUT:

        The consecutive slopes (not including the last slope
        if the polygon is infinity) of this Newton polygon.

        If ``repetition`` is ``True``, each slope is repeated a number of
        times equal to its length. Otherwise, it appears only one time.

        EXAMPLES::

            sage: from sage.geometry.newton_polygon import NewtonPolygon
            sage: NP = NewtonPolygon([ (0,0), (1,1), (3,6) ]); NP
            Finite Newton polygon with 3 vertices: (0, 0), (1, 1), (3, 6)

            sage: NP.slopes()
            [1, 5/2, 5/2]

            sage: NP.slopes(repetition=False)
            [1, 5/2]
        """
    def __pow__(self, exp, ignored=None):
        """
        Return ``self`` dilated by ``exp``.

        INPUT:

        - ``exp`` -- positive integer

        OUTPUT: this Newton polygon scaled by a factor ``exp``

        .. NOTE::

            If ``self`` is the Newton polygon of a polynomial `f`, then
            ``self^exp`` is the Newton polygon of `f^{exp}`.

        EXAMPLES::

            sage: from sage.geometry.newton_polygon import NewtonPolygon
            sage: NP = NewtonPolygon([ (0,0), (1,1), (2,6) ]); NP
            Finite Newton polygon with 3 vertices: (0, 0), (1, 1), (2, 6)

            sage: NP^10
            Finite Newton polygon with 3 vertices: (0, 0), (10, 10), (20, 60)
        """
    def __lshift__(self, i):
        """
        Return ``self`` shifted by `(0,i)`.

        INPUT:

        - ``i`` -- a rational number

        OUTPUT: this Newton polygon shifted by the vector `(0,i)`

        EXAMPLES::

            sage: from sage.geometry.newton_polygon import NewtonPolygon
            sage: NP = NewtonPolygon([ (0,0), (1,1), (2,6) ]); NP
            Finite Newton polygon with 3 vertices: (0, 0), (1, 1), (2, 6)

            sage: NP << 2
            Finite Newton polygon with 3 vertices: (0, 2), (1, 3), (2, 8)
        """
    def __rshift__(self, i):
        """
        Return ``self`` shifted by `(0,-i)`.

        INPUT:

        - ``i`` -- a rational number

        OUTPUT: this Newton polygon shifted by the vector `(0,-i)`

        EXAMPLES::

            sage: from sage.geometry.newton_polygon import NewtonPolygon
            sage: NP = NewtonPolygon([ (0,0), (1,1), (2,6) ]); NP
            Finite Newton polygon with 3 vertices: (0, 0), (1, 1), (2, 6)

            sage: NP >> 2
            Finite Newton polygon with 3 vertices: (0, -2), (1, -1), (2, 4)
        """
    def __call__(self, x):
        """
        Return `self(x)`.

        INPUT:

        - ``x`` -- a real number

        OUTPUT: the value of this Newton polygon at abscissa `x`

        EXAMPLES::

            sage: from sage.geometry.newton_polygon import NewtonPolygon
            sage: NP = NewtonPolygon([ (0,0), (1,1), (3,6) ]); NP
            Finite Newton polygon with 3 vertices: (0, 0), (1, 1), (3, 6)

            sage: [ NP(i) for i in range(4) ]
            [0, 1, 7/2, 6]
        """
    def plot(self, **kwargs):
        """
        Plot this Newton polygon.

        .. NOTE::

            All usual rendering options (color, thickness, etc.) are available.

        EXAMPLES::

            sage: from sage.geometry.newton_polygon import NewtonPolygon
            sage: NP = NewtonPolygon([ (0,0), (1,1), (2,6) ])
            sage: polygon = NP.plot()                                                   # needs sage.plot
        """
    def reverse(self, degree=None):
        """
        Return the symmetric of ``self``.

        INPUT:

        - ``degree`` -- integer (default: the top right abscissa of
          this Newton polygon)

        OUTPUT:

        The image this Newton polygon under the symmetry
        '(x,y) \\mapsto (degree-x, y)`.

        EXAMPLES::

            sage: from sage.geometry.newton_polygon import NewtonPolygon
            sage: NP = NewtonPolygon([ (0,0), (1,1), (2,5) ])
            sage: NP2 = NP.reverse(); NP2
            Finite Newton polygon with 3 vertices: (0, 5), (1, 1), (2, 0)

        We check that the slopes of the symmetric Newton polygon are
        the opposites of the slopes of the original Newton polygon::

            sage: NP.slopes()
            [1, 4]
            sage: NP2.slopes()
            [-4, -1]
        """

class ParentNewtonPolygon(Parent, UniqueRepresentation):
    """
    Construct a Newton polygon.

    INPUT:

    - ``arg`` -- list/tuple/iterable of vertices or of
      slopes. Currently, slopes must be rational numbers

    - ``sort_slopes`` -- boolean (default: ``True``);  whether slopes must be
      first sorted

    - ``last_slope`` -- rational or infinity (default:
      ``Infinity``); the last slope of the Newton polygon

    OUTPUT: the corresponding Newton polygon

    .. NOTE::

        By convention, a Newton polygon always contains the point
        at infinity `(0, \\infty)`. These polygons are attached to
        polynomials or series over discrete valuation rings (e.g. padics).

    EXAMPLES:

    We specify here a Newton polygon by its vertices::

        sage: from sage.geometry.newton_polygon import NewtonPolygon
        sage: NewtonPolygon([ (0,0), (1,1), (3,5) ])
        Finite Newton polygon with 3 vertices: (0, 0), (1, 1), (3, 5)

    We note that the convex hull of the vertices is automatically
    computed::

        sage: NewtonPolygon([ (0,0), (1,1), (2,8), (3,5) ])
        Finite Newton polygon with 3 vertices: (0, 0), (1, 1), (3, 5)

    Note that the value ``+Infinity`` is allowed as the second coordinate
    of a vertex::

        sage: NewtonPolygon([ (0,0), (1,Infinity), (2,8), (3,5) ])
        Finite Newton polygon with 2 vertices: (0, 0), (3, 5)

    If last_slope is set, the returned Newton polygon is infinite
    and ends with an infinite line having the specified slope::

        sage: NewtonPolygon([ (0,0), (1,1), (2,8), (3,5) ], last_slope=3)
        Infinite Newton polygon with 3 vertices: (0, 0), (1, 1), (3, 5)
        ending by an infinite line of slope 3

    Specifying a last slope may discard some vertices::

        sage: NewtonPolygon([ (0,0), (1,1), (2,8), (3,5) ], last_slope=3/2)
        Infinite Newton polygon with 2 vertices: (0, 0), (1, 1)
        ending by an infinite line of slope 3/2

    Next, we define a Newton polygon by its slopes::

        sage: NP = NewtonPolygon([0, 1/2, 1/2, 2/3, 2/3, 2/3, 1, 1])
        sage: NP
        Finite Newton polygon with 5 vertices: (0, 0), (1, 0), (3, 1), (6, 3), (8, 5)
        sage: NP.slopes()
        [0, 1/2, 1/2, 2/3, 2/3, 2/3, 1, 1]

    By default, slopes are automatically sorted::

        sage: NP2 = NewtonPolygon([0, 1, 1/2, 2/3, 1/2, 2/3, 1, 2/3])
        sage: NP2
        Finite Newton polygon with 5 vertices: (0, 0), (1, 0), (3, 1), (6, 3), (8, 5)
        sage: NP == NP2
        True

    except if the contrary is explicitly mentioned::

        sage: NewtonPolygon([0, 1, 1/2, 2/3, 1/2, 2/3, 1, 2/3], sort_slopes=False)
        Finite Newton polygon with 4 vertices: (0, 0), (1, 0), (6, 10/3), (8, 5)

    Slopes greater that or equal last_slope (if specified) are discarded::

        sage: NP = NewtonPolygon([0, 1/2, 1/2, 2/3, 2/3, 2/3, 1, 1], last_slope=2/3)
        sage: NP
        Infinite Newton polygon with 3 vertices: (0, 0), (1, 0), (3, 1)
        ending by an infinite line of slope 2/3
        sage: NP.slopes()
        [0, 1/2, 1/2]

    Be careful, do not confuse Newton polygons provided by this class
    with Newton polytopes. Compare::

        sage: NP = NewtonPolygon([ (0,0), (1,45), (3,6) ]); NP
        Finite Newton polygon with 2 vertices: (0, 0), (3, 6)

        sage: x, y = polygen(QQ,'x, y')
        sage: p = 1 + x*y**45 + x**3*y**6
        sage: p.newton_polytope()
        A 2-dimensional polyhedron in ZZ^2 defined as the convex hull
        of 3 vertices
        sage: p.newton_polytope().vertices()
        (A vertex at (0, 0), A vertex at (1, 45), A vertex at (3, 6))
    """
    Element = NewtonPolygon_element
    def __init__(self) -> None:
        """
        Parent class for all Newton polygons.

        EXAMPLES::

            sage: from sage.geometry.newton_polygon import ParentNewtonPolygon
            sage: ParentNewtonPolygon()
            Parent for Newton polygons

        TESTS:

        This class is a singleton::

            sage: ParentNewtonPolygon() is ParentNewtonPolygon()
            True

        ::

            sage: TestSuite(ParentNewtonPolygon()).run()
        """

NewtonPolygon: Incomplete
