from _typeshed import Incomplete
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.misc.cachefunc import cached_function as cached_function, cached_method as cached_method
from sage.misc.latex import latex as latex
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import parent as parent

class PlotOptions:
    """
    A class for plotting options for root lattice realizations.

    .. SEEALSO::

        - :meth:`RootLatticeRealizations.ParentMethods.plot()
          <sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ParentMethods.plot>`
          for a description of the plotting options
        - :ref:`sage.combinat.root_system.plot` for a tutorial on root
          system plotting
    """
    space: Incomplete
    labels: Incomplete
    affine: Incomplete
    level: Incomplete
    origin_projected: Incomplete
    dimension: Incomplete
    bounding_box: Incomplete
    def __init__(self, space, projection: bool = True, bounding_box: int = 3, color=..., labels: bool = True, level=None, affine=None, arrowsize: int = 5) -> None:
        """
        TESTS::

            sage: L = RootSystem(['B',2,1]).weight_space()
            sage: options = L.plot_parse_options()
            sage: options.dimension
            2
            sage: options._projections
            [Weight space over the Rational Field of the Root system of type ['B', 2],
             <bound method RootLatticeRealizations.ParentMethods._plot_projection
              of Weight space over the Rational Field of the Root system of type ['B', 2]>]

            sage: L = RootSystem(['B',2,1]).ambient_space()
            sage: options = L.plot_parse_options()
            sage: options.dimension
            2
            sage: options._projections
            [Ambient space of the Root system of type ['B', 2],
             <bound method RootLatticeRealizations.ParentMethods._plot_projection
              of Ambient space of the Root system of type ['B', 2]>]

            sage: options = L.plot_parse_options(affine=True)
            sage: options.dimension
            2
            sage: options._projections
            [Ambient space of the Root system of type ['B', 2],
             <bound method RootLatticeRealizations.ParentMethods._plot_projection
              of Ambient space of the Root system of type ['B', 2]>]

            sage: options = L.plot_parse_options(affine=False)
            sage: options._projections
            [<bound method AmbientSpace._plot_projection
              of Ambient space of the Root system of type ['B', 2, 1]>]
            sage: options.dimension
            3

            sage: options = L.plot_parse_options(affine=False,
            ....:                                projection='barycentric')
            sage: options._projections
            [<bound method RootLatticeRealizations.ParentMethods._plot_projection_barycentric
              of Ambient space of the Root system of type ['B', 2, 1]>]
            sage: options.dimension
            3
        """
    @cached_method
    def in_bounding_box(self, x):
        '''
        Return whether ``x`` is in the bounding box.

        INPUT:

        - ``x`` -- an element of the root lattice realization

        This method is currently one of the bottlenecks, and therefore
        cached.

        EXAMPLES::

            sage: L = RootSystem(["A",2,1]).ambient_space()
            sage: options = L.plot_parse_options()
            sage: alpha = L.simple_roots()
            sage: options.in_bounding_box(alpha[1])
            True
            sage: options.in_bounding_box(3*alpha[1])
            False
        '''
    def text(self, label, position, rgbcolor=(0, 0, 0)):
        '''
        Return text widget with label ``label`` at position ``position``.

        INPUT:

        - ``label`` -- string or Sage object upon which latex will be called

        - ``position`` -- a position

        - ``rgbcolor`` -- the color as an RGB tuple

        EXAMPLES::

            sage: L = RootSystem(["A",2]).root_lattice()
            sage: options = L.plot_parse_options()
            sage: list(options.text("coucou", [0,1]))
            [Text \'coucou\' at the point (0.0,1.0)]
            sage: list(options.text(L.simple_root(1), [0,1]))
            [Text \'$\\alpha_{1}$\' at the point (0.0,1.0)]
            sage: list(options.text(L.simple_root(2), [1,0], rgbcolor=(1,0.5,0)))
            [Text \'$\\alpha_{2}$\' at the point (1.0,0.0)]

            sage: options = L.plot_parse_options(labels=False)
            sage: options.text("coucou", [0,1])
            0

            sage: options = RootSystem(["B",3]).root_lattice().plot_parse_options()
            sage: print(options.text("coucou", [0,1,2]).x3d_str())
            <Transform translation=\'0 1 2\'>
            <Shape><Text string=\'coucou\' solid=\'true\'/><Appearance><Material diffuseColor=\'0.0 0.0 0.0\' shininess=\'1.0\' specularColor=\'0.0 0.0 0.0\'/></Appearance></Shape>
            <BLANKLINE>
            </Transform>
        '''
    def index_of_object(self, i):
        '''
        Try to return the node of the Dynkin diagram indexing the object `i`.

        OUTPUT: a node of the Dynkin diagram or ``None``

        EXAMPLES::

            sage: L = RootSystem(["A",3]).root_lattice()
            sage: alpha = L.simple_roots()
            sage: omega = RootSystem(["A",3]).weight_lattice().fundamental_weights()
            sage: options = L.plot_parse_options(labels=False)
            sage: options.index_of_object(3)
            3
            sage: options.index_of_object(alpha[1])
            1
            sage: options.index_of_object(omega[2])
            2
            sage: options.index_of_object(omega[2]+omega[3])
            sage: options.index_of_object(30)
            sage: options.index_of_object("bla")
        '''
    def thickness(self, i):
        '''
        Return the thickness to be used for lines indexed by `i`.

        INPUT:

        - ``i`` -- an index

        .. SEEALSO:: :meth:`index_of_object`

        EXAMPLES::

            sage: L = RootSystem(["A",2,1]).root_lattice()
            sage: options = L.plot_parse_options(labels=False)
            sage: alpha = L.simple_roots()
            sage: options.thickness(0)
            2
            sage: options.thickness(1)
            1
            sage: options.thickness(2)
            1
            sage: for alpha in L.simple_roots():
            ....:     print("{} {}".format(alpha, options.thickness(alpha)))
            alpha[0] 2
            alpha[1] 1
            alpha[2] 1
        '''
    def color(self, i):
        '''
        Return the color to be used for objects indexed by `i`.

        INPUT:

        - ``i`` -- an index

        .. SEEALSO:: :meth:`index_of_object`

        EXAMPLES::

            sage: L = RootSystem(["A",2]).root_lattice()
            sage: options = L.plot_parse_options(labels=False)
            sage: alpha = L.simple_roots()
            sage: options.color(1)
            \'blue\'
            sage: options.color(2)
            \'red\'
            sage: for alpha in L.roots():
            ....:     print("{} {}".format(alpha, options.color(alpha)))
            alpha[1]             blue
            alpha[2]             red
            alpha[1] + alpha[2]  black
            -alpha[1]            black
            -alpha[2]            black
            -alpha[1] - alpha[2] black
        '''
    def projection(self, v):
        '''
        Return the projection of ``v``.

        INPUT:

        - ``x`` -- an element of the root lattice realization

        OUTPUT: an immutable vector with integer or rational coefficients

        EXAMPLES::

            sage: L = RootSystem(["A",2,1]).ambient_space()
            sage: options = L.plot_parse_options()
            sage: options.projection(L.rho())
            (0, 989/571)

            sage: options = L.plot_parse_options(projection=False)
            sage: options.projection(L.rho())
            (2, 1, 0)
        '''
    def intersection_at_level_1(self, x):
        '''
        Return ``x`` scaled at the appropriate level, if level is set;
        otherwise return ``x``.

        INPUT:

        - ``x`` -- an element of the root lattice realization

        EXAMPLES::

            sage: L = RootSystem(["A",2,1]).weight_space()
            sage: options = L.plot_parse_options()
            sage: options.intersection_at_level_1(L.rho())
            1/3*Lambda[0] + 1/3*Lambda[1] + 1/3*Lambda[2]

            sage: options = L.plot_parse_options(affine=False, level=2)
            sage: options.intersection_at_level_1(L.rho())
            2/3*Lambda[0] + 2/3*Lambda[1] + 2/3*Lambda[2]

        When ``level`` is not set, ``x`` is returned::

            sage: options = L.plot_parse_options(affine=False)
            sage: options.intersection_at_level_1(L.rho())
            Lambda[0] + Lambda[1] + Lambda[2]
        '''
    def empty(self, *args):
        '''
        Return an empty plot.

        EXAMPLES::

            sage: L = RootSystem(["A",2]).root_lattice()
            sage: options = L.plot_parse_options(labels=True)

        This currently returns ``int(0)``::

            sage: options.empty()
            0

        This is not a plot, so may cause some corner cases. On the
        other hand, `0` behaves as a fast neutral element, which is
        important given the typical idioms used in the plotting code::

            sage: p = point([0,0])
            sage: p + options.empty() is p
            True
        '''
    def finalize(self, G):
        '''
        Finalize a root system plot.

        INPUT:

        - ``G`` -- a root system plot or ``0``

        This sets the aspect ratio to 1 and remove the axes. This
        should be called by all the user-level plotting methods of
        root systems. This will become mostly obsolete when
        customization options won\'t be lost anymore upon addition of
        graphics objects and there will be a proper empty object for
        2D and 3D plots.

        EXAMPLES::

            sage: L = RootSystem(["B",2,1]).ambient_space()
            sage: options = L.plot_parse_options()
            sage: p = L.plot_roots(plot_options=options)
            sage: p += L.plot_coroots(plot_options=options)
            sage: p.axes()
            True
            sage: p = options.finalize(p)
            sage: p.axes()
            False
            sage: p.aspect_ratio()
            1.0

            sage: options = L.plot_parse_options(affine=False)
            sage: p = L.plot_roots(plot_options=options)
            sage: p += point([[1,1,0]])
            sage: p = options.finalize(p)
            sage: p.aspect_ratio()
            [1.0, 1.0, 1.0]

        If the input is ``0``, this returns an empty graphics object::

            sage: type(options.finalize(0))
            <class \'sage.plot.plot3d.base.Graphics3dGroup\'>

            sage: options = L.plot_parse_options()
            sage: type(options.finalize(0))
            <class \'sage.plot.graphics.Graphics\'>
            sage: list(options.finalize(0))
            []
        '''
    def family_of_vectors(self, vectors):
        '''
        Return a plot of a family of vectors.

        INPUT:

        - ``vectors`` -- family or vectors in ``self``

        The vectors are labelled by their index.

        EXAMPLES::

            sage: L = RootSystem(["A",2]).root_lattice()
            sage: options = L.plot_parse_options()
            sage: alpha = L.simple_roots()
            sage: p = options.family_of_vectors(alpha); p
            Graphics object consisting of 4 graphics primitives
            sage: list(p)
            [Arrow from (0.0,0.0) to (1.0,0.0),
             Text \'$1$\' at the point (1.05,0.0),
             Arrow from (0.0,0.0) to (0.0,1.0),
             Text \'$2$\' at the point (0.0,1.05)]

        Handling of colors and labels::

            sage: def color(i):
            ....:     return "purple" if i==1 else None
            sage: options = L.plot_parse_options(labels=False, color=color)
            sage: p = options.family_of_vectors(alpha)
            sage: list(p)
            [Arrow from (0.0,0.0) to (1.0,0.0)]
            sage: p[0].options()[\'rgbcolor\']
            \'purple\'

        Matplotlib emits a warning for arrows of length 0 and draws
        nothing anyway. So we do not draw them at all::

            sage: L = RootSystem(["A",2,1]).ambient_space()
            sage: options = L.plot_parse_options()
            sage: Lambda = L.fundamental_weights()
            sage: p = options.family_of_vectors(Lambda); p
            Graphics object consisting of 5 graphics primitives
            sage: list(p)
            [Text \'$0$\' at the point (0.0,0.0),
             Arrow from (0.0,0.0) to (0.5,0.86602451838...),
             Text \'$1$\' at the point (0.525,0.909325744308...),
             Arrow from (0.0,0.0) to (-0.5,0.86602451838...),
             Text \'$2$\' at the point (-0.525,0.909325744308...)]
        '''
    def cone(self, rays=[], lines=[], color: str = 'black', thickness: int = 1, alpha: int = 1, wireframe: bool = False, label=None, draw_degenerate: bool = True, as_polyhedron: bool = False):
        '''
        Return the cone generated by the given rays and lines.

        INPUT:

        - ``rays``, ``lines`` -- lists of elements of the root lattice
          realization (default: ``[]``)

        - ``color`` -- a color (default: ``\'black\'``)

        - ``alpha`` -- a number in the interval `[0, 1]` (default: `1`)
          the desired transparency

        - ``label`` -- an object to be used as the label for this cone
          The label itself will be constructed by calling
          :func:`~sage.misc.latex.latex` or :func:`repr` on the
          object depending on the graphics backend.

        - ``draw_degenerate`` -- boolean (default: ``True``)
          whether to draw cones with a degenerate intersection with
          the bounding box

        - ``as_polyhedron`` -- boolean (default: ``False``)
          whether to return the result as a polyhedron, without
          clipping it to the bounding box, and without making a plot
          out of it (for testing purposes)

        OUTPUT: a graphic object, a polyhedron, or ``0``

        EXAMPLES::

            sage: L = RootSystem(["A",2]).root_lattice()
            sage: options = L.plot_parse_options()
            sage: alpha = L.simple_roots()
            sage: p = options.cone(rays=[alpha[1]], lines=[alpha[2]],
            ....:                  color=\'green\', label=2); p
            Graphics object consisting of 2 graphics primitives
            sage: list(p)
            [Polygon defined by 4 points,
             Text \'$2$\' at the point (3.15...,3.15...)]
            sage: options.cone(rays=[alpha[1]], lines=[alpha[2]],
            ....:              color=\'green\', label=2, as_polyhedron=True)
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex, 1 ray, 1 line

        An empty result, being outside of the bounding box::

            sage: options = L.plot_parse_options(labels=True,
            ....:                                bounding_box=[[-10,-9]]*2)
            sage: options.cone(rays=[alpha[1]], lines=[alpha[2]],
            ....:              color=\'green\', label=2)
            0

        Test that the options are properly passed down::

            sage: L = RootSystem(["A",2]).root_lattice()
            sage: options = L.plot_parse_options()
            sage: p = options.cone(rays=[alpha[1] + alpha[2]],
            ....:                  color=\'green\', label=2, thickness=4, alpha=.5)
            sage: list(p)
            [Line defined by 2 points, Text \'$2$\' at the point (3.15...,3.15...)]
            sage: sorted(p[0].options().items())
            [(\'alpha\', 0.500000000000000), (\'legend_color\', None),
             (\'legend_label\', None), (\'rgbcolor\', \'green\'), (\'thickness\', 4),
             (\'zorder\', 1)]

        This method is tested indirectly but extensively by the
        various plot methods of root lattice realizations.
        '''
    def reflection_hyperplane(self, coroot, as_polyhedron: bool = False):
        '''
        Return a plot of the reflection hyperplane indexed by this coroot.

        - ``coroot`` -- a coroot

        EXAMPLES::

            sage: L = RootSystem(["B",2]).weight_space()
            sage: alphacheck = L.simple_coroots()
            sage: options = L.plot_parse_options()
            sage: H = options.reflection_hyperplane(alphacheck[1]); H
            Graphics object consisting of 2 graphics primitives

        TESTS::

            sage: print(H.description())
            Text \'$H_{\\alpha^\\vee_{1}}$\' at the point (0.0,3.15...)
            Line defined by 2 points: [(0.0, 3.0), (0.0, -3.0)]

        ::

            sage: L = RootSystem(["A",3,1]).ambient_space()
            sage: alphacheck = L.simple_coroots()
            sage: options = L.plot_parse_options()
            sage: H = options.reflection_hyperplane(alphacheck[1],
            ....:                                   as_polyhedron=True); H
            A 2-dimensional polyhedron in QQ^3 defined as the convex hull of 1 vertex and 2 lines
            sage: H.lines()
            (A line in the direction (0, 0, 1), A line in the direction (0, 1, 0))
            sage: H.vertices()
            (A vertex at (0, 0, 0),)

        ::

            sage: all(options.reflection_hyperplane(c, as_polyhedron=True).dim() == 2
            ....:     for c in alphacheck)
            True


        .. TODO::

            Display the periodic orientation by adding a `+` and
            a `-` sign close to the label. Typically by using
            the associated root to shift a bit from the vertex
            upon which the hyperplane label is attached.
        '''

@cached_function
def barycentric_projection_matrix(n, angle: int = 0):
    """
    Return a family of `n+1` vectors evenly spaced in a real vector space of dimension `n`.

    Those vectors are of norm `1`, the scalar product between any two
    vector is `1/n`, thus the distance between two tips is constant.

    The family is built recursively and uniquely determined by the
    following property: the last vector is `(0,\\dots,0,-1)`, and the
    projection of the first `n` vectors in dimension `n-1`, after
    appropriate rescaling to norm `1`, retrieves the family for `n-1`.

    OUTPUT:

    A matrix with `n+1` columns of height `n` with rational or
    symbolic coefficients.

    EXAMPLES:

    One vector in dimension `0`::

        sage: from sage.combinat.root_system.root_lattice_realizations import barycentric_projection_matrix
        sage: m = barycentric_projection_matrix(0); m
        []
        sage: matrix(QQ,0,1).nrows()
        0
        sage: matrix(QQ,0,1).ncols()
        1

    Two vectors in dimension 1::

        sage: barycentric_projection_matrix(1)
        [ 1 -1]

    Three vectors in dimension 2::

        sage: barycentric_projection_matrix(2)
        [ 1/2*sqrt(3) -1/2*sqrt(3)            0]
        [         1/2          1/2           -1]

    Four vectors in dimension 3::

        sage: m = barycentric_projection_matrix(3); m
        [ 1/3*sqrt(3)*sqrt(2) -1/3*sqrt(3)*sqrt(2)                    0                    0]
        [         1/3*sqrt(2)          1/3*sqrt(2)         -2/3*sqrt(2)                    0]
        [                 1/3                  1/3                  1/3                   -1]

    The columns give four vectors that sum up to zero::

        sage: sum(m.columns())
        (0, 0, 0)

    and have regular mutual angles::

        sage: m.transpose()*m
        [   1 -1/3 -1/3 -1/3]
        [-1/3    1 -1/3 -1/3]
        [-1/3 -1/3    1 -1/3]
        [-1/3 -1/3 -1/3    1]

    Here is a plot of them::

        sage: sum(arrow((0,0,0),x) for x in m.columns())
        Graphics3d Object

    For 2D drawings of root systems, it is desirable to rotate the
    result to match with the usual conventions::

        sage: barycentric_projection_matrix(2, angle=2*pi/3)
        [         1/2           -1          1/2]
        [ 1/2*sqrt(3)            0 -1/2*sqrt(3)]

    TESTS::

        sage: for n in range(1, 7):
        ....:     m = barycentric_projection_matrix(n)
        ....:     assert sum(m.columns()).is_zero()
        ....:     assert matrix(QQ, n+1,n+1, lambda i,j: 1 if i==j else -1/n) == m.transpose()*m
    """
