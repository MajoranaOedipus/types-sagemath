from _typeshed import Incomplete
from sage.matrix.constructor import identity_matrix as identity_matrix, matrix as matrix
from sage.matrix.special import diagonal_matrix as diagonal_matrix
from sage.misc.functional import norm as norm
from sage.misc.latex import LatexExpr as LatexExpr
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module_element import vector as vector
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.sequence import Sequence as Sequence

def cyclic_sort_vertices_2d(Vlist):
    '''
    Return the vertices/rays in cyclic order if possible.

    .. NOTE::

        This works if and only if each vertex/ray is adjacent to exactly
        two others. For example, any 2-dimensional polyhedron satisfies
        this.

    See
    :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.vertex_adjacency_matrix`
    for a discussion of "adjacent".

    EXAMPLES::

        sage: from sage.geometry.polyhedron.plot import cyclic_sort_vertices_2d
        sage: square = Polyhedron([[1,0],[-1,0],[0,1],[0,-1]])
        sage: vertices = [v for v in square.vertex_generator()]
        sage: vertices
        [A vertex at (-1, 0),
         A vertex at (0, -1),
         A vertex at (0, 1),
         A vertex at (1, 0)]
        sage: cyclic_sort_vertices_2d(vertices)
        [A vertex at (1, 0),
         A vertex at (0, -1),
         A vertex at (-1, 0),
         A vertex at (0, 1)]

    Rays are allowed, too::

        sage: P = Polyhedron(vertices=[(0, 1), (1, 0), (2, 0), (3, 0), (4, 1)], rays=[(0,1)])
        sage: P.adjacency_matrix()
        [0 1 0 1 0]
        [1 0 1 0 0]
        [0 1 0 0 1]
        [1 0 0 0 1]
        [0 0 1 1 0]
        sage: cyclic_sort_vertices_2d(P.Vrepresentation())
        [A vertex at (3, 0),
         A vertex at (1, 0),
         A vertex at (0, 1),
         A ray in the direction (0, 1),
         A vertex at (4, 1)]

        sage: P = Polyhedron(vertices=[(0, 1), (1, 0), (2, 0), (3, 0), (4, 1)], rays=[(0,1), (1,1)])
        sage: P.adjacency_matrix()
        [0 1 0 0 0]
        [1 0 1 0 0]
        [0 1 0 0 1]
        [0 0 0 0 1]
        [0 0 1 1 0]
        sage: cyclic_sort_vertices_2d(P.Vrepresentation())
        [A ray in the direction (1, 1),
         A vertex at (3, 0),
         A vertex at (1, 0),
         A vertex at (0, 1),
         A ray in the direction (0, 1)]

        sage: P = Polyhedron(vertices=[(1,2)], rays=[(0,1)], lines=[(1,0)])
        sage: P.adjacency_matrix()
        [0 0 1]
        [0 0 0]
        [1 0 0]
        sage: cyclic_sort_vertices_2d(P.Vrepresentation())
        [A vertex at (0, 2),
         A line in the direction (1, 0),
         A ray in the direction (0, 1)]
    '''
def projection_func_identity(x):
    """
    The identity projection.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.plot import projection_func_identity
        sage: projection_func_identity((1,2,3))
        [1, 2, 3]
    """

class ProjectionFuncStereographic:
    """
    The stereographic (or perspective) projection onto a codimension-1 linear
    subspace with respect to a sphere centered at the origin.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.plot import ProjectionFuncStereographic
        sage: cube = polytopes.hypercube(3).vertices()
        sage: proj = ProjectionFuncStereographic([1.2, 3.4, 5.6])
        sage: ppoints = [proj(vector(x)) for x in cube]
        sage: ppoints[5]
        (-0.0918273..., -0.036375...)
    """
    projection_point: Incomplete
    dim: Incomplete
    psize: Incomplete
    house: Incomplete
    def __init__(self, projection_point) -> None:
        """
        Create a stereographic projection function.

        INPUT:

        - ``projection_point`` -- list of coordinates in the
          appropriate dimension, which is the point projected from

        EXAMPLES::

            sage: from sage.geometry.polyhedron.plot import ProjectionFuncStereographic
            sage: proj = ProjectionFuncStereographic([1.0,1.0])
            sage: proj.__init__([1.0,1.0])
            sage: proj.house
            [ 0.7071067811... -0.7071067811...]
            [ 0.7071067811...  0.7071067811...]
            sage: TestSuite(proj).run(skip='_test_pickling')
        """
    def __call__(self, x):
        """
        Action of the stereographic projection.

        INPUT:

        - ``x`` -- a vector or anything convertible to a vector

        OUTPUT:

        First reflects ``x`` with a Householder reflection which takes
        the projection point to ``(0,...,0,self.psize)`` where
        ``psize`` is the length of the projection point, and then
        dilates by ``1/(zdiff)`` where ``zdiff`` is the difference
        between the last coordinate of ``x`` and ``psize``.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.plot import ProjectionFuncStereographic
            sage: proj = ProjectionFuncStereographic([1.0,1.0])
            sage: proj.__call__(vector([1,2]))
            (1.0000000000000002)
            sage: proj = ProjectionFuncStereographic([2.0,1.0])
            sage: proj.__call__(vector([1,2]))  # abs tol 1e-14
            (-2.999999999999997)
            sage: proj = ProjectionFuncStereographic([0,0,2])
            sage: proj.__call__(vector([0,0,1]))
            (0.0, 0.0)
            sage: proj.__call__(vector([1,0,0]))
            (0.5, 0.0)
        """

class ProjectionFuncSchlegel:
    """
    The Schlegel projection from the given input point.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.plot import ProjectionFuncSchlegel
        sage: fcube = polytopes.hypercube(4)
        sage: facet = fcube.facets()[0]
        sage: proj = ProjectionFuncSchlegel(facet,[0,-1.5,0,0])
        sage: proj([0,0,0,0])[0]
        1.0
    """
    facet: Incomplete
    full_A: Incomplete
    full_b: Incomplete
    A: Incomplete
    b: Incomplete
    projection_point: Incomplete
    def __init__(self, facet, projection_point) -> None:
        """
        Initialize the projection.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.plot import ProjectionFuncSchlegel
            sage: fcube = polytopes.hypercube(4)
            sage: facet = fcube.facets()[0]
            sage: proj = ProjectionFuncSchlegel(facet,[0,-1.5,0,0])
            sage: proj.facet
            A 3-dimensional face of a Polyhedron in ZZ^4 defined as the convex hull of 8 vertices
            sage: proj.A
            [1.0 0.0 0.0]
            [0.0 0.0 0.0]
            [0.0 0.0 1.0]
            [0.0 1.0 0.0]
            sage: proj.b
            (1.0, 1.0, 1.0)
            sage: proj.projection_point
            (0.0, -1.5, 0.0, 0.0)
            sage: proj([-1,1,1,1])
            (0.8, 1.2, 1.2)
            sage: proj([1,1,1,1])
            (1.2, 1.2, 1.2)
            sage: proj([1,-1,1,1])
            (2.0, 2.0, 2.0)
            sage: proj([1,-1,-1,1])
            (2.0, 2.0, 0.0)
            sage: TestSuite(proj).run(skip='_test_pickling')
        """
    def __call__(self, x):
        """
        Apply the projection to a vector.

        - ``x`` -- a vector or anything convertible to a vector

        EXAMPLES::

            sage: from sage.geometry.polyhedron.plot import ProjectionFuncSchlegel
            sage: fcube = polytopes.hypercube(4)
            sage: facet = fcube.facets()[0]
            sage: proj = ProjectionFuncSchlegel(facet,[0,-1.5,0,0])
            sage: proj.__call__([0,0,0,0])
            (1.0, 1.0, 1.0)
        """

class Projection(SageObject):
    """
    The projection of a :class:`Polyhedron`.

    This class keeps track of the necessary data to plot the input
    polyhedron.
    """
    parent_polyhedron: Incomplete
    coords: Incomplete
    points: Incomplete
    lines: Incomplete
    arrows: Incomplete
    polygons: Incomplete
    polyhedron_ambient_dim: Incomplete
    polyhedron_dim: Incomplete
    def __init__(self, polyhedron, proj=...) -> None:
        """
        Initialize the projection of a Polyhedron() object.

        INPUT:

        - ``polyhedron`` -- a ``Polyhedron()`` object

        - ``proj`` -- a projection function for the points

        .. NOTE::

            Once initialized, the polyhedral data is fixed. However, the
            projection can be changed later on.

        EXAMPLES::

            sage: # needs sage.groups
            sage: p = polytopes.icosahedron(exact=False)
            sage: from sage.geometry.polyhedron.plot import Projection
            sage: Projection(p)
            The projection of a polyhedron into 3 dimensions
            sage: def pr_12(x): return [x[1],x[2]]
            sage: Projection(p, pr_12)
            The projection of a polyhedron into 2 dimensions
            sage: Projection(p,  lambda x: [x[1],x[2]] )   # another way of doing the same projection
            The projection of a polyhedron into 2 dimensions
            sage: _.plot()   # plot of the projected icosahedron in 2d                  # needs sage.plot
            Graphics object consisting of 51 graphics primitives
            sage: proj = Projection(p)
            sage: proj.stereographic([1,2,3])
            The projection of a polyhedron into 2 dimensions
            sage: proj.plot()                                                           # needs sage.plot
            Graphics object consisting of 51 graphics primitives
            sage: TestSuite(proj).run(skip='_test_pickling')
        """
    transformed_coords: Incomplete
    def __call__(self, proj=...):
        """
        Apply a projection.

        EXAMPLES::

            sage: # needs sage.groups
            sage: p = polytopes.icosahedron(exact=False)
            sage: from sage.geometry.polyhedron.plot import Projection
            sage: pproj = Projection(p)
            sage: from sage.geometry.polyhedron.plot import ProjectionFuncStereographic
            sage: pproj_stereo = pproj.__call__(proj=ProjectionFuncStereographic([1, 2, 3]))
            sage: sorted(pproj_stereo.polygons)
            [[2, 0, 9],
             [3, 1, 10],
             [4, 0, 8],
             ...
             [11, 1, 3],
             [11, 3, 7],
             [11, 7, 9]]
        """
    def identity(self):
        """
        Return the identity projection of the polyhedron.

        EXAMPLES::

            sage: # needs sage.groups
            sage: p = polytopes.icosahedron(exact=False)
            sage: from sage.geometry.polyhedron.plot import Projection
            sage: pproj = Projection(p)
            sage: ppid = pproj.identity()
            sage: ppid.dimension
            3
        """
    def stereographic(self, projection_point=None):
        """
        Return the stereographic projection.

        INPUT:

        - ``projection_point`` -- the projection point. This must be
          distinct from the polyhedron's vertices. Default is `(1,0,\\dots,0)`.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.plot import Projection
            sage: proj = Projection(polytopes.buckyball()); proj  # long time
            The projection of a polyhedron into 3 dimensions
            sage: proj.stereographic([5,2,3]).plot()    # long time                     # needs sage.plot
            Graphics object consisting of 123 graphics primitives
            sage: Projection(polytopes.twenty_four_cell()).stereographic([2,0,0,0])
            The projection of a polyhedron into 3 dimensions
        """
    def schlegel(self, facet=None, position=None):
        """
        Return the Schlegel projection.

        * The facet is orthonormally transformed into its affine hull.

        * The position specifies a point coming out of the barycenter of the
          facet from which the other vertices will be projected into the facet.

        INPUT:

        - ``facet`` -- a PolyhedronFace; the facet into which the Schlegel
          diagram is created. The default is the first facet.

        - ``position`` -- a positive number. Determines a relative distance
          from the barycenter of ``facet``. A value close to 0 will place the
          projection point close to the facet and a large value further away.
          If the given value is too large, an error is returned.
          If no position is given, it takes the midpoint of the possible
          point of views along a line spanned by the barycenter of the facet
          and a valid point outside the facet.

        EXAMPLES::

            sage: cube4 = polytopes.hypercube(4)
            sage: from sage.geometry.polyhedron.plot import Projection
            sage: Projection(cube4).schlegel()
            The projection of a polyhedron into 3 dimensions
            sage: _.plot()                                                              # needs sage.plot
            Graphics3d Object

        The 4-cube with a truncated vertex seen into the resulting tetrahedron
        facet::

            sage: tcube4 = cube4.face_truncation(cube4.faces(0)[0])
            sage: tcube4.facets()[4]
            A 3-dimensional face of a Polyhedron in QQ^4 defined as the convex hull of 4 vertices
            sage: into_tetra = Projection(tcube4).schlegel(tcube4.facets()[4])          # needs sage.symbolic
            sage: into_tetra.plot()                                                     # needs sage.plot sage.symbolic
            Graphics3d Object

        Taking a larger value for the position changes the image::

            sage: into_tetra_far = Projection(tcube4).schlegel(tcube4.facets()[4], 4)   # needs sage.symbolic
            sage: into_tetra_far.plot()                                                 # needs sage.plot sage.symbolic
            Graphics3d Object

        A value which is too large or negative give a projection point that
        sees more than one facet resulting in a error::

            sage: Projection(tcube4).schlegel(tcube4.facets()[4], 5)
            Traceback (most recent call last):
            ...
            ValueError: the chosen position is too large
            sage: Projection(tcube4).schlegel(tcube4.facets()[4], -1)
            Traceback (most recent call last):
            ...
            ValueError: 'position' should be a positive number
        """
    def coord_index_of(self, v):
        """
        Convert a coordinate vector to its internal index.

        EXAMPLES::

            sage: p = polytopes.hypercube(3)
            sage: proj = p.projection()
            sage: proj.coord_index_of(vector((1,1,1)))
            2
        """
    def coord_indices_of(self, v_list):
        """
        Convert list of coordinate vectors to the corresponding list
        of internal indices.

        EXAMPLES::

            sage: p = polytopes.hypercube(3)
            sage: proj = p.projection()
            sage: proj.coord_indices_of([vector((1,1,1)), vector((1,-1,1))])
            [2, 3]
        """
    def coordinates_of(self, coord_index_list):
        """
        Given a list of indices, return the projected coordinates.

        EXAMPLES::

            sage: p = polytopes.simplex(4, project=True).projection()
            sage: p.coordinates_of([1])
            [[-0.7071067812, 0.4082482905, 0.2886751346, 0.2236067977]]
        """
    def render_points_1d(self, **kwds):
        """
        Return the points of a polyhedron in 1d.

        INPUT:

        - ``**kwds`` -- options passed through to
          :func:`~sage.plot.point.point2d`

        OUTPUT: a 2-d graphics object

        EXAMPLES::

            sage: cube1 = polytopes.hypercube(1)
            sage: proj = cube1.projection()
            sage: points = proj.render_points_1d()                                      # needs sage.plot
            sage: points._objects                                                       # needs sage.plot
            [Point set defined by 2 point(s)]
        """
    def render_line_1d(self, **kwds):
        """
        Return the line of a polyhedron in 1d.

        INPUT:

        - ``**kwds`` -- options passed through to
          :func:`~sage.plot.line.line2d`

        OUTPUT: a 2-d graphics object

        EXAMPLES::

            sage: outline = polytopes.hypercube(1).projection().render_line_1d()        # needs sage.plot
            sage: outline._objects[0]                                                   # needs sage.plot
            Line defined by 2 points
        """
    def render_points_2d(self, **kwds):
        """
        Return the points of a polyhedron in 2d.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: hex = polytopes.regular_polygon(6)
            sage: proj = hex.projection()
            sage: hex_points = proj.render_points_2d()                                  # needs sage.plot
            sage: hex_points._objects                                                   # needs sage.plot
            [Point set defined by 6 point(s)]
        """
    def render_outline_2d(self, **kwds):
        """
        Return the outline (edges) of a polyhedron in 2d.

        EXAMPLES::

            sage: penta = polytopes.regular_polygon(5)                                  # needs sage.rings.number_field
            sage: outline = penta.projection().render_outline_2d()                      # needs sage.plot sage.rings.number_field
            sage: outline._objects[0]                                                   # needs sage.plot sage.rings.number_field
            Line defined by 2 points
        """
    def render_fill_2d(self, **kwds):
        """
        Return the filled interior (a polygon) of a polyhedron in 2d.

        EXAMPLES::

            sage: cps = [i^3 for i in srange(-2, 2, 1/5)]
            sage: p = Polyhedron(vertices=[[(t^2-1)/(t^2+1), 2*t/(t^2+1)] for t in cps])
            sage: proj = p.projection()
            sage: filled_poly = proj.render_fill_2d()                                   # needs sage.plot
            sage: filled_poly.axes_width()                                              # needs sage.plot
            0.8
        """
    def render_vertices_3d(self, **kwds):
        """
        Return the 3d rendering of the vertices.

        EXAMPLES::

            sage: p = polytopes.cross_polytope(3)
            sage: proj = p.projection()
            sage: verts = proj.render_vertices_3d()                                     # needs sage.plot
            sage: verts.bounding_box()                                                  # needs sage.plot
            ((-1.0, -1.0, -1.0), (1.0, 1.0, 1.0))
        """
    def render_wireframe_3d(self, **kwds):
        """
        Return the 3d wireframe rendering.

        EXAMPLES::

            sage: cube = polytopes.hypercube(3)
            sage: cube_proj = cube.projection()
            sage: wire = cube_proj.render_wireframe_3d()                                # needs sage.plot
            sage: print(wire.tachyon().split('\\n')[77])  # for testing                  # needs sage.plot
            FCylinder base 1.0 1.0 -1.0 apex -1.0 1.0 -1.0 rad 0.005 texture...
        """
    def render_solid_3d(self, **kwds):
        """
        Return solid 3d rendering of a 3d polytope.

        EXAMPLES::

            sage: p = polytopes.hypercube(3).projection()
            sage: p_solid = p.render_solid_3d(opacity=.7)                               # needs sage.plot
            sage: type(p_solid)                                                         # needs sage.plot
            <class 'sage.plot.plot3d.index_face_set.IndexFaceSet'>
        """
    def render_0d(self, point_opts=None, line_opts=None, polygon_opts=None):
        """
        Return 0d rendering of the projection of a polyhedron into
        2-dimensional ambient space.

        INPUT:

        See
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.plot`.

        OUTPUT: a 2-d graphics object

        EXAMPLES::

            sage: print(Polyhedron([]).projection().render_0d().description())          # needs sage.plot
            <BLANKLINE>
            sage: P = Polyhedron(ieqs=[(1,)])
            sage: print(P.projection().render_0d().description())                       # needs sage.plot
            Point set defined by 1 point(s):    [(0.0, 0.0)]
        """
    def render_1d(self, point_opts=None, line_opts=None, polygon_opts=None):
        """
        Return 1d rendering of the projection of a polyhedron into
        2-dimensional ambient space.

        INPUT:

        See
        :meth:`~sage.geometry.polyhedron.base.Polyhedron_base.plot`.

        OUTPUT: a 2-d graphics object

        EXAMPLES::

            sage: Polyhedron([(0,), (1,)]).projection().render_1d()                     # needs sage.plot
            Graphics object consisting of 2 graphics primitives
        """
    def render_2d(self, point_opts=None, line_opts=None, polygon_opts=None):
        """
        Return 2d rendering of the projection of a polyhedron into
        2-dimensional ambient space.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[[1,1]], rays=[[1,1]])
            sage: q1 = p1.projection()
            sage: p2 = Polyhedron(vertices=[[1,0], [0,1], [0,0]])
            sage: q2 = p2.projection()
            sage: p3 = Polyhedron(vertices=[[1,2]])
            sage: q3 = p3.projection()
            sage: p4 = Polyhedron(vertices=[[2,0]], rays=[[1,-1]], lines=[[1,1]])
            sage: q4 = p4.projection()
            sage: q1.plot() + q2.plot() + q3.plot() + q4.plot()                         # needs sage.plot
            Graphics object consisting of 18 graphics primitives
        """
    def render_3d(self, point_opts=None, line_opts=None, polygon_opts=None):
        """
        Return 3d rendering of a polyhedron projected into
        3-dimensional ambient space.

        EXAMPLES::

            sage: p1 = Polyhedron(vertices=[[1,1,1]], rays=[[1,1,1]])
            sage: p2 = Polyhedron(vertices=[[2,0,0], [0,2,0], [0,0,2]])
            sage: p3 = Polyhedron(vertices=[[1,0,0], [0,1,0], [0,0,1]],
            ....:                 rays=[[-1,-1,-1]])
            sage: (p1.projection().plot() + p2.projection().plot()                      # needs sage.plot
            ....:   + p3.projection().plot())
            Graphics3d Object

        It correctly handles various degenerate cases::

            sage: # needs sage.plot
            sage: Polyhedron(lines=[[1,0,0], [0,1,0], [0,0,1]]).plot()  # whole space
            Graphics3d Object
            sage: Polyhedron(vertices=[[1,1,1]], rays=[[1,0,0]],
            ....:            lines=[[0,1,0], [0,0,1]]).plot()           # half space
            Graphics3d Object
            sage: Polyhedron(lines=[[0,1,0], [0,0,1]],
            ....:            vertices=[[1,1,1]]).plot()      # R^2 in R^3
            Graphics3d Object
            sage: Polyhedron(rays=[[0,1,0], [0,0,1]],        # quadrant wedge in R^2
            ....:            lines=[[1,0,0]]).plot()
            Graphics3d Object
            sage: Polyhedron(rays=[[0,1,0]],                 # upper half plane in R^3
            ....:            lines=[[1,0,0]]).plot()
            Graphics3d Object
            sage: Polyhedron(lines=[[1,0,0]]).plot()         # R^1 in R^2
            Graphics3d Object
            sage: Polyhedron(rays=[[0,1,0]]).plot()          # Half-line in R^3
            Graphics3d Object
            sage: Polyhedron(vertices=[[1,1,1]]).plot()      # point in R^3
            Graphics3d Object

        The origin is not included, if it is not in the polyhedron (:issue:`23555`)::

            sage: Q = Polyhedron([[100],[101]])
            sage: P = Q*Q*Q; P
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices
            sage: p = P.plot()                                                          # needs sage.plot
            sage: p.bounding_box()                                                      # needs sage.plot
            ((100.0, 100.0, 100.0), (101.0, 101.0, 101.0))

        Plot 3d polytope with rainbow colors::

            sage: polytopes.hypercube(3).plot(polygon='rainbow', alpha=0.4)             # needs sage.plot
            Graphics3d Object
        """
    def tikz(self, view=[0, 0, 1], angle: int = 0, scale: int = 1, edge_color: str = 'blue!95!black', facet_color: str = 'blue!95!black', opacity: float = 0.8, vertex_color: str = 'green', axis: bool = False, output_type: str = 'TikzPicture'):
        """
        Return a tikz picture of ``self`` as a string or as a
        :class:`~sage.misc.latex_standalone.TikzPicture`
        according to a projection ``view`` and an angle ``angle``
        obtained via the threejs viewer.

        INPUT:

        - ``view`` -- list (default: [0,0,1]) representing the rotation axis (see note below)
        - ``angle`` -- integer (default: 0); angle of rotation in degree from 0 to 360 (see note
          below)
        - ``scale`` -- integer (default: 1); the scaling of the tikz picture
        - ``edge_color`` -- string (default: ``'blue!95!black'``); representing colors which tikz
          recognizes
        - ``facet_color`` -- string (default: ``'blue!95!black'``); representing colors which tikz
          recognizes
        - ``vertex_color`` -- string (default: ``'green'``); representing colors which tikz
          recognizes
        - ``opacity`` -- real number (default: 0.8) between 0 and 1 giving the opacity of
          the front facets
        - ``axis`` -- boolean (default: ``False``); draw the axes at the origin or not
        - ``output_type`` -- string (default: ``'TikzPicture'``); valid values
          are ``'LatexExpr'`` and ``'TikzPicture'``,
          whether to return a :class:`LatexExpr` object (which inherits from Python
          :class:`str`) or a :class:`TikzPicture` object from module
          :mod:`sage.misc.latex_standalone`

        OUTPUT: :class:`LatexExpr` object or :class:`TikzPicture` object

        .. NOTE::

            The inputs ``view`` and ``angle`` can be obtained by visualizing it
            using ``.show(aspect_ratio=1)``. This will open an interactive view
            in your default browser, where you can rotate the polytope. Once
            the desired view angle is found, click on the information icon in
            the lower right-hand corner and select *Get Viewpoint*. This will
            copy a string of the form '[x,y,z],angle' to your local clipboard.
            Go back to Sage and type ``Img = P.projection().tikz([x,y,z],angle)``.

            The inputs ``view`` and ``angle`` can also be obtained from the
            viewer Jmol::

                1) Right click on the image
                2) Select ``Console``
                3) Select the tab ``State``
                4) Scroll to the line ``moveto``

            It reads something like::

                moveto 0.0 {x y z angle} Scale

            The ``view`` is then [x,y,z] and ``angle`` is angle.
            The following number is the scale.

            Jmol performs a rotation of ``angle`` degrees along the
            vector [x,y,z] and show the result from the z-axis.

        EXAMPLES::

            sage: # needs sage.plot sage.rings.number_field
            sage: P1 = polytopes.small_rhombicuboctahedron()
            sage: Image1 = P1.projection().tikz([1,3,5], 175, scale=4,
            ....:                               output_type='TikzPicture')
            sage: type(Image1)
            <class 'sage.misc.latex_standalone.TikzPicture'>
            sage: Image1
            \\documentclass[tikz]{standalone}
            \\begin{document}
            \\begin{tikzpicture}%
                    [x={(-0.939161cm, 0.244762cm)},
                    y={(0.097442cm, -0.482887cm)},
                    z={(0.329367cm, 0.840780cm)},
                    scale=4.000000,
            ...
            Use print to see the full content.
            ...
            \\node[vertex] at (-2.41421, 1.00000, -1.00000)     {};
            \\node[vertex] at (-2.41421, -1.00000, 1.00000)     {};
            %%
            %%
            \\end{tikzpicture}
            \\end{document}
            sage: _ = Image1.tex('polytope-tikz1.tex')          # not tested
            sage: _ = Image1.png('polytope-tikz1.png')          # not tested
            sage: _ = Image1.pdf('polytope-tikz1.pdf')          # not tested
            sage: _ = Image1.svg('polytope-tikz1.svg')          # not tested

        A second example::

            sage: P2 = Polyhedron(vertices=[[1, 1], [1, 2], [2, 1]])
            sage: Image2 = P2.projection().tikz(scale=3, edge_color='blue!95!black',
            ....:                               facet_color='orange!95!black', opacity=0.4,
            ....:                               vertex_color='yellow', axis=True,
            ....:                               output_type='TikzPicture')
            sage: Image2
            \\documentclass[tikz]{standalone}
            \\begin{document}
            \\begin{tikzpicture}%
                    [scale=3.000000,
                    back/.style={loosely dotted, thin},
                    edge/.style={color=blue!95!black, thick},
                    facet/.style={fill=orange!95!black,fill opacity=0.400000},
            ...
            Use print to see the full content.
            ...
            \\node[vertex] at (1.00000, 2.00000)     {};
            \\node[vertex] at (2.00000, 1.00000)     {};
            %%
            %%
            \\end{tikzpicture}
            \\end{document}

        The second example using a LatexExpr as output type::

            sage: # needs sage.plot
            sage: Image2 = P2.projection().tikz(scale=3, edge_color='blue!95!black',
            ....:                               facet_color='orange!95!black', opacity=0.4,
            ....:                               vertex_color='yellow', axis=True,
            ....:                               output_type='LatexExpr')
            sage: type(Image2)
            <class 'sage.misc.latex.LatexExpr'>
            sage: print('\\n'.join(Image2.splitlines()[:4]))
            \\begin{tikzpicture}%
                [scale=3.000000,
                back/.style={loosely dotted, thin},
                edge/.style={color=blue!95!black, thick},
            sage: with open('polytope-tikz2.tex', 'w') as f:    # not tested
            ....:     _ = f.write(Image2)

        A third example::

            sage: # needs sage.plot
            sage: P3 = Polyhedron(vertices=[[-1, -1, 2], [-1, 2, -1], [2, -1, -1]]); P3
            A 2-dimensional polyhedron in ZZ^3 defined as the convex hull of 3 vertices
            sage: Image3 = P3.projection().tikz([0.5, -1, -0.1], 55, scale=3,
            ....:                               edge_color='blue!95!black',
            ....:                               facet_color='orange!95!black', opacity=0.7,
            ....:                               vertex_color='yellow', axis=True)
            sage: Image3
            \\documentclass[tikz]{standalone}
            \\begin{document}
            \\begin{tikzpicture}%
                    [x={(0.658184cm, -0.242192cm)},
                    y={(-0.096240cm, 0.912008cm)},
                    z={(-0.746680cm, -0.331036cm)},
                    scale=3.000000,
            ...
            Use print to see the full content.
            ...
            \\node[vertex] at (-1.00000, 2.00000, -1.00000)     {};
            \\node[vertex] at (2.00000, -1.00000, -1.00000)     {};
            %%
            %%
            \\end{tikzpicture}
            \\end{document}
            sage: _ = Image3.tex('polytope-tikz3.tex')          # not tested
            sage: _ = Image3.png('polytope-tikz3.png')          # not tested
            sage: _ = Image3.pdf('polytope-tikz3.pdf')          # not tested
            sage: _ = Image3.svg('polytope-tikz3.svg')          # not tested

        A fourth example::

            sage: P = Polyhedron(vertices=[[1,1,0,0], [1,2,0,0],
            ....:                          [2,1,0,0], [0,0,1,0], [0,0,0,1]]); P
            A 4-dimensional polyhedron in ZZ^4 defined as the convex hull of 5 vertices
            sage: P.projection().tikz(output_type='TikzPicture')
            Traceback (most recent call last):
            ...
            NotImplementedError: The polytope has to live in 2 or 3 dimensions.

        TESTS::

            sage: P = Polyhedron(vertices=[[0,0,0], [1,0,0],
            ....:                          [0,0,1], [0,1,0]])
            sage: P.projection().tikz(output_type='kawai')
            Traceback (most recent call last):
            ...
            ValueError: output_type (='kawai') must be 'LatexExpr' or 'TikzPicture'

        .. TODO::

            Make it possible to draw Schlegel diagram for 4-polytopes. ::

                sage: P = Polyhedron(vertices=[[1,1,0,0], [1,2,0,0],
                ....:                          [2,1,0,0], [0,0,1,0], [0,0,0,1]]); P
                A 4-dimensional polyhedron in ZZ^4 defined as the convex hull of 5 vertices
                sage: P.projection().tikz(output_type='TikzPicture')
                Traceback (most recent call last):
                ...
                NotImplementedError: The polytope has to live in 2 or 3 dimensions.

            Make it possible to draw 3-polytopes living in higher dimension.
        """
