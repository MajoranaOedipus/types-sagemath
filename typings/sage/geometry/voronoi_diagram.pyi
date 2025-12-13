from sage.geometry.polyhedron.constructor import Polyhedron as Polyhedron
from sage.geometry.triangulation.point_configuration import PointConfiguration as PointConfiguration
from sage.modules.free_module_element import vector as vector
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

class VoronoiDiagram(SageObject):
    """
    Base class for the  Voronoi diagram.

    Compute the Voronoi diagram of a list of points.

    INPUT:

    - ``points`` -- list of points; any valid input for the
      :class:`PointConfiguration` will do

    OUTPUT: an instance of the VoronoiDiagram class

    EXAMPLES:

    Get the Voronoi diagram for some points in `\\RR^3`::

        sage: V = VoronoiDiagram([[1, 3, .3], [2, -2, 1], [-1, 2, -.1]]); V
        The Voronoi diagram of 3 points of dimension 3 in the Real Double Field

        sage: VoronoiDiagram([])
        The empty Voronoi diagram.

    Get the Voronoi diagram of a regular pentagon in ``AA^2``.
    All cells meet at the origin::

        sage: DV = VoronoiDiagram([[AA(c) for c in v]                                   # needs sage.rings.number_field
        ....:                      for v in polytopes.regular_polygon(5).vertices_list()]); DV
        The Voronoi diagram of 5 points of dimension 2 in the Algebraic Real Field
        sage: all(P.contains([0, 0]) for P in DV.regions().values())                    # needs sage.rings.number_field
        True
        sage: any(P.interior_contains([0, 0]) for P in DV.regions().values())           # needs sage.rings.number_field
        False

    If the vertices are not converted to ``AA`` before, the method throws an error::

        sage: polytopes.dodecahedron().vertices_list()[0][0].parent()                   # needs sage.groups sage.rings.number_field
        Number Field in sqrt5 with defining polynomial x^2 - 5 with sqrt5 = 2.236067977499790?
        sage: VoronoiDiagram(polytopes.dodecahedron().vertices_list())                  # needs sage.groups sage.rings.number_field
        Traceback (most recent call last):
        ...
        NotImplementedError: Base ring of the Voronoi diagram must be
        one of QQ, RDF, AA.

    ALGORITHM:

    We use hyperplanes tangent to the paraboloid one dimension higher to
    get a convex polyhedron and then project back to one dimension lower.

    .. TODO::

     - The dual construction: Delaunay triangulation
     - improve 2d-plotting
     - implement 3d-plotting
     - more general constructions, like Voroi diagrams with weights (power diagrams)

    REFERENCES:

     - [Mat2002]_ Ch.5.7, p.118.

    AUTHORS:

    - Moritz Firsching (2012-09-21)
    """
    def __init__(self, points) -> None:
        """
        See ``VoronoiDiagram`` for full documentation.

        EXAMPLES::

            sage: V = VoronoiDiagram([[1, 3, 3], [2, -2, 1], [-1 ,2, -1]]); V
            The Voronoi diagram of 3 points of dimension 3 in the Rational Field
        """
    def points(self):
        """
        Return the input points (as a PointConfiguration).

        EXAMPLES::

            sage: V = VoronoiDiagram([[.5, 3], [2, 5], [4, 5], [4, -1]]); V.points()
            A point configuration in affine 2-space over Real Field
            with 53 bits of precision consisting of 4 points.
            The triangulations of this point configuration are
            assumed to be connected, not necessarily fine,
            not necessarily regular.
        """
    def ambient_dim(self):
        """
        Return the ambient dimension of the points.

        EXAMPLES::

            sage: V = VoronoiDiagram([[.5, 3], [2, 5], [4, 5], [4, -1]])
            sage: V.ambient_dim()
            2
            sage: V = VoronoiDiagram([[1, 2, 3, 4, 5, 6]]); V.ambient_dim()
            6
        """
    def regions(self):
        """
        Return the Voronoi regions of the Voronoi diagram as a
        dictionary of polyhedra.

        EXAMPLES::

            sage: V = VoronoiDiagram([[1, 3, .3], [2, -2, 1], [-1, 2, -.1]])
            sage: P = V.points()
            sage: V.regions() == {P[0]: Polyhedron(base_ring=RDF, lines=[(-RDF(0.375), RDF(0.13888888890000001), RDF(1.5277777779999999))],
            ....:                                                 rays=[(RDF(9), -RDF(1), -RDF(20)), (RDF(4.5), RDF(1), -RDF(25))],
            ....:                                                 vertices=[(-RDF(1.1074999999999999), RDF(1.149444444), RDF(9.0138888890000004))]),
            ....:                 P[1]: Polyhedron(base_ring=RDF, lines=[(-RDF(0.375), RDF(0.13888888890000001), RDF(1.5277777779999999))],
            ....:                                                 rays=[(RDF(9), -RDF(1), -RDF(20)), (-RDF(2.25), -RDF(1), RDF(2.5))],
            ....:                                                  vertices=[(-RDF(1.1074999999999999), RDF(1.149444444), RDF(9.0138888890000004))]),
            ....:                 P[2]: Polyhedron(base_ring=RDF, lines=[(-RDF(0.375), RDF(0.13888888890000001), RDF(1.5277777779999999))],
            ....:                                                 rays=[(RDF(4.5), RDF(1), -RDF(25)), (-RDF(2.25), -RDF(1), RDF(2.5))],
            ....:                                                 vertices=[(-RDF(1.1074999999999999), RDF(1.149444444), RDF(9.0138888890000004))])}
            True
        """
    def base_ring(self):
        """
        Return the base_ring of the regions of the Voronoi diagram.

        EXAMPLES::

            sage: V = VoronoiDiagram([[1, 3, 1], [2, -2, 1], [-1, 2, 1/2]]); V.base_ring()
            Rational Field
            sage: V = VoronoiDiagram([[1, 3.14], [2, -2/3], [-1, 22]]); V.base_ring()
            Real Double Field
            sage: V = VoronoiDiagram([[1, 3], [2, 4]]); V.base_ring()
            Rational Field
        """
    def plot(self, cell_colors=None, **kwds):
        """
        Return a graphical representation for 2-dimensional Voronoi diagrams.

        INPUT:

        - ``cell_colors`` -- (default: ``None``) provide the colors for the cells, either as
          dictionary. Randomly colored cells are provided with ``None``.
        - ``**kwds`` -- optional keyword parameters, passed on as arguments for
          plot()

        OUTPUT: a graphics object

        EXAMPLES::

            sage: # needs sage.plot
            sage: P = [[0.671, 0.650], [0.258, 0.767], [0.562, 0.406],
            ....:      [0.254, 0.709], [0.493, 0.879]]
            sage: V = VoronoiDiagram(P); S=V.plot()
            sage: show(S, xmin=0, xmax=1, ymin=0, ymax=1, aspect_ratio=1, axes=false)
            sage: S = V.plot(cell_colors={0: 'red', 1: 'blue', 2: 'green',
            ....:                         3: 'white', 4: 'yellow'})
            sage: show(S, xmin=0, xmax=1, ymin=0, ymax=1, aspect_ratio=1, axes=false)
            sage: S = V.plot(cell_colors=['red', 'blue', 'red', 'white', 'white'])
            sage: show(S, xmin=0, xmax=1, ymin=0, ymax=1, aspect_ratio=1, axes=false)
            sage: S = V.plot(cell_colors='something else')
            Traceback (most recent call last):
            ...
            AssertionError: 'cell_colors' must be a list or a dictionary


        Trying to plot a Voronoi diagram of dimension other than 2 gives an
        error::

            sage: VoronoiDiagram([[1, 2, 3], [6, 5, 4]]).plot()                         # needs sage.plot
            Traceback (most recent call last):
            ...
            NotImplementedError: Plotting of 3-dimensional Voronoi diagrams not
            implemented
        """
