from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.sets.set import Set as Set
from sage.structure.element import Element as Element
from sage.structure.richcmp import richcmp as richcmp

def triangulation_render_2d(triangulation, **kwds):
    """
    Return a graphical representation of a 2-d triangulation.

    INPUT:

    - ``triangulation`` -- a :class:`Triangulation`

    - ``**kwds`` -- keywords that are passed on to the graphics primitives

    OUTPUT: a 2-d graphics object

    EXAMPLES::

        sage: points = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
        sage: triang = points.triangulate()
        sage: triang.plot(axes=False, aspect_ratio=1)   # indirect doctest              # needs sage.plot
        Graphics object consisting of 12 graphics primitives
    """
def triangulation_render_3d(triangulation, **kwds):
    """
    Return a graphical representation of a 3-d triangulation.

    INPUT:

    - ``triangulation`` -- a :class:`Triangulation`

    - ``**kwds`` -- keywords that are  passed on to the graphics primitives

    OUTPUT: a 3-d graphics object

    EXAMPLES::

        sage: p = [[0,-1,-1],[0,0,1],[0,1,0], [1,-1,-1],[1,0,1],[1,1,0]]
        sage: points = PointConfiguration(p)
        sage: triang = points.triangulate()
        sage: triang.plot(axes=False)     # indirect doctest                            # needs sage.plot
        Graphics3d Object
    """

class Triangulation(Element):
    """
    A triangulation of a
    :class:`~sage.geometry.triangulation.point_configuration.PointConfiguration`.

    .. WARNING::

        You should never create :class:`Triangulation` objects
        manually. See
        :meth:`~sage.geometry.triangulation.point_configuration.PointConfiguration.triangulate`
        and
        :meth:`~sage.geometry.triangulation.point_configuration.PointConfiguration.triangulations`
        to triangulate point configurations.
    """
    def __init__(self, triangulation, parent, check: bool = True) -> None:
        """
        The constructor of a ``Triangulation`` object.

        Note that an internal reference to the underlying ``PointConfiguration`` is
        kept.

        INPUT:

        - ``parent`` -- a
          :class:`~sage.geometry.triangulation.point_configuration.PointConfiguration`

        - ``triangulation`` -- an iterable of integers or an iterable of
          iterables (e.g. a list of lists), specifying the maximal simplices
          of the triangulation. In the first case, each integer specifies a simplex
          by the correspondence :meth:`PointConfiguration.simplex_to_int`. In the second
          case, a simplex is specified by listing the indices of the included points.

        - ``check`` -- boolean; whether to perform checks that the
          triangulation is, indeed, a triangulation of the point
          configuration

        NOTE:

        Passing ``check=False`` allows you to create triangulations of
        subsets of the points of the configuration, see
        :meth:`~sage.geometry.triangulation.point_configuration.PointConfiguration.bistellar_flips`.

        EXAMPLES::

            sage: p = [[0,1],[0,0],[1,0]]
            sage: points = PointConfiguration(p)
            sage: from sage.geometry.triangulation.point_configuration import Triangulation
            sage: Triangulation([(0,1,2)], points)
            (<0,1,2>)
            sage: Triangulation([1], points)
            (<0,1,2>)
        """
    def point_configuration(self):
        """
        Return the point configuration underlying the triangulation.

        EXAMPLES::

            sage: pconfig = PointConfiguration([[0,0],[0,1],[1,0]])
            sage: pconfig
            A point configuration in affine 2-space over Integer Ring
            consisting of 3 points. The triangulations of this point
            configuration are assumed to be connected, not necessarily
            fine, not necessarily regular.
            sage: triangulation = pconfig.triangulate()
            sage: triangulation
            (<0,1,2>)
            sage: triangulation.point_configuration()
            A point configuration in affine 2-space over Integer Ring
            consisting of 3 points. The triangulations of this point
            configuration are assumed to be connected, not necessarily
            fine, not necessarily regular.
            sage: pconfig == triangulation.point_configuration()
            True
        """
    def __iter__(self):
        """
        Iterate through the simplices of the triangulation.

        EXAMPLES::

            sage: PointConfiguration.set_engine('internal')   # to make doctests independent of TOPCOM
            sage: pc = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: triangulation = pc.triangulate()
            sage: iter = triangulation.__iter__()
            sage: next(iter)
            (1, 3, 4)
            sage: next(iter)
            (2, 3, 4)
            sage: next(iter)
            Traceback (most recent call last):
            ...
            StopIteration
        """
    def __getitem__(self, i):
        """
        Access the point indices of the `i`-th simplex of the triangulation.

        INPUT:

        - ``i`` -- integer; the index of a simplex

        OUTPUT:

        A tuple of integers. The vertex indices of the `i`-th simplex.

        EXAMPLES::

            sage: PointConfiguration.set_engine('internal')   # to make doctests independent of TOPCOM
            sage: pc = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: triangulation = pc.triangulate()
            sage: triangulation[1]
            (2, 3, 4)
        """
    def __len__(self) -> int:
        """
        Return the length of the triangulation.

        TESTS::

            sage: PointConfiguration.set_engine('internal')   # to make doctests independent of TOPCOM
            sage: pc = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: triangulation = next(pc.triangulations())
            sage: triangulation.__len__()
            2
            sage: len(triangulation)    # equivalent
            2
        """
    def plot(self, **kwds):
        """
        Produce a graphical representation of the triangulation.

        EXAMPLES::

            sage: p = PointConfiguration([[0,0],[0,1],[1,0],[1,1],[-1,-1]])
            sage: triangulation = p.triangulate()
            sage: triangulation
            (<1,3,4>, <2,3,4>)
            sage: triangulation.plot(axes=False)                                        # needs sage.plot
            Graphics object consisting of 12 graphics primitives
        """
    def gkz_phi(self):
        """
        Calculate the GKZ phi vector of the triangulation.

        The phi vector is a vector of length equals to the number of
        points in the point configuration. For a fixed triangulation
        `T`, the entry corresponding to the `i`-th point `p_i` is

        .. MATH::

            \\phi_T(p_i) = \\sum_{t\\in T, t\\owns p_i} Vol(t)

        that is, the total volume of all simplices containing `p_i`.
        See also [GKZ1994]_ page 220 equation 1.4.

        OUTPUT: the phi vector of self

        EXAMPLES::

            sage: p = PointConfiguration([[0,0],[1,0],[2,1],[1,2],[0,1]])
            sage: p.triangulate().gkz_phi()
            (3, 1, 5, 2, 4)
            sage: p.lexicographic_triangulation().gkz_phi()
            (1, 3, 4, 2, 5)
        """
    def enumerate_simplices(self):
        """
        Return the enumerated simplices.

        OUTPUT: a tuple of integers that uniquely specifies the triangulation

        EXAMPLES::

            sage: pc = PointConfiguration(matrix([
            ....:    [ 0, 0, 0, 0, 0, 2, 4,-1, 1, 1, 0, 0, 1, 0],
            ....:    [ 0, 0, 0, 1, 0, 0,-1, 0, 0, 0, 0, 0, 0, 0],
            ....:    [ 0, 2, 0, 0, 0, 0,-1, 0, 1, 0, 1, 0, 0, 1],
            ....:    [ 0, 1, 1, 0, 0, 1, 0,-2, 1, 0, 0,-1, 1, 1],
            ....:    [ 0, 0, 0, 0, 1, 0,-1, 0, 0, 0, 0, 0, 0, 0]
            ....: ]).columns())
            sage: triangulation = pc.lexicographic_triangulation()
            sage: triangulation.enumerate_simplices()
            (1678, 1688, 1769, 1779, 1895, 1905, 2112, 2143, 2234, 2360, 2555, 2580,
             2610, 2626, 2650, 2652, 2654, 2661, 2663, 2667, 2685, 2755, 2757, 2759,
             2766, 2768, 2772, 2811, 2881, 2883, 2885, 2892, 2894, 2898)

        You can recreate the triangulation from this list by passing
        it to the constructor::

            sage: from sage.geometry.triangulation.point_configuration import Triangulation
            sage: Triangulation([1678, 1688, 1769, 1779, 1895, 1905, 2112, 2143,
            ....:  2234, 2360, 2555, 2580, 2610, 2626, 2650, 2652, 2654, 2661, 2663,
            ....:  2667, 2685, 2755, 2757, 2759, 2766, 2768, 2772, 2811, 2881, 2883,
            ....:  2885, 2892, 2894, 2898], pc)
            (<1,3,4,7,10,13>, <1,3,4,8,10,13>, <1,3,6,7,10,13>, <1,3,6,8,10,13>,
             <1,4,6,7,10,13>, <1,4,6,8,10,13>, <2,3,4,6,7,12>, <2,3,4,7,12,13>,
             <2,3,6,7,12,13>, <2,4,6,7,12,13>, <3,4,5,6,9,12>, <3,4,5,8,9,12>,
             <3,4,6,7,11,12>, <3,4,6,9,11,12>, <3,4,7,10,11,13>, <3,4,7,11,12,13>,
             <3,4,8,9,10,12>, <3,4,8,10,12,13>, <3,4,9,10,11,12>, <3,4,10,11,12,13>,
             <3,5,6,8,9,12>, <3,6,7,10,11,13>, <3,6,7,11,12,13>, <3,6,8,9,10,12>,
             <3,6,8,10,12,13>, <3,6,9,10,11,12>, <3,6,10,11,12,13>, <4,5,6,8,9,12>,
             <4,6,7,10,11,13>, <4,6,7,11,12,13>, <4,6,8,9,10,12>, <4,6,8,10,12,13>,
             <4,6,9,10,11,12>, <4,6,10,11,12,13>)
        """
    def fan(self, origin=None):
        """
        Construct the fan of cones over the simplices of the triangulation.

        INPUT:

        - ``origin`` -- ``None`` (default) or coordinates of a
          point. The common apex of all cones of the fan. If ``None``,
          the triangulation must be a star triangulation and the
          distinguished central point is used as the origin.

        OUTPUT:

        A :class:`~sage.geometry.fan.RationalPolyhedralFan`. The
        coordinates of the points are shifted so that the apex of the
        fan is the origin of the coordinate system.

        .. NOTE:: If the set of cones over the simplices is not a fan, a
            suitable exception is raised.

        EXAMPLES::

            sage: pc = PointConfiguration([(0,0), (1,0), (0,1), (-1,-1)], star=0, fine=True)
            sage: triangulation = pc.triangulate()
            sage: fan = triangulation.fan(); fan
            Rational polyhedral fan in 2-d lattice N
            sage: fan.is_equivalent(toric_varieties.P2().fan())                         # needs palp sage.graphs
            True

        Toric diagrams (the `\\ZZ_5` hyperconifold)::

            sage: vertices=[(0, 1, 0), (0, 3, 1), (0, 2, 3), (0, 0, 2)]
            sage: interior=[(0, 1, 1), (0, 1, 2), (0, 2, 1), (0, 2, 2)]
            sage: points = vertices + interior
            sage: pc = PointConfiguration(points, fine=True)
            sage: triangulation = pc.triangulate()
            sage: fan = triangulation.fan((-1,0,0)); fan
            Rational polyhedral fan in 3-d lattice N
            sage: fan.rays()
            N(1, 1, 0),
            N(1, 3, 1),
            N(1, 2, 3),
            N(1, 0, 2),
            N(1, 1, 1),
            N(1, 1, 2),
            N(1, 2, 1),
            N(1, 2, 2)
            in 3-d lattice N
        """
    @cached_method
    def simplicial_complex(self):
        """
        Return ``self`` as an (abstract) simplicial complex.

        OUTPUT: a :class:`~sage.topology.simplicial_complex.SimplicialComplex`

        EXAMPLES::

            sage: p = polytopes.cuboctahedron()
            sage: sc = p.triangulate(engine='internal').simplicial_complex(); sc        # needs sage.graphs
            Simplicial complex with 12 vertices and 16 facets

        Any convex set is contractable, so its reduced homology groups vanish::

            sage: sc.homology()                                                         # needs sage.graphs
            {0: 0, 1: 0, 2: 0, 3: 0}
        """
    @cached_method
    def boundary(self):
        """
        Return the boundary of the triangulation.

        OUTPUT:

        The outward-facing boundary simplices (of dimension `d-1`) of
        the `d`-dimensional triangulation as a set. Each boundary is
        returned by a tuple of point indices.

        EXAMPLES::

            sage: triangulation = polytopes.cube().triangulate(engine='internal')
            sage: triangulation
            (<0,1,2,7>, <0,1,5,7>, <0,2,3,7>, <0,3,4,7>, <0,4,5,7>, <1,5,6,7>)
            sage: triangulation.boundary()
            frozenset({(0, 1, 2),
                       (0, 1, 5),
                       (0, 2, 3),
                       (0, 3, 4),
                       (0, 4, 5),
                       (1, 2, 7),
                       (1, 5, 6),
                       (1, 6, 7),
                       (2, 3, 7),
                       (3, 4, 7),
                       (4, 5, 7),
                       (5, 6, 7)})
            sage: triangulation.interior_facets()
            frozenset({(0, 1, 7), (0, 2, 7), (0, 3, 7), (0, 4, 7), (0, 5, 7), (1, 5, 7)})
        """
    @cached_method
    def boundary_simplicial_complex(self):
        """
        Return the boundary of ``self`` as an (abstract) simplicial complex.

        OUTPUT: a :class:`~sage.topology.simplicial_complex.SimplicialComplex`

        EXAMPLES::

            sage: p = polytopes.cuboctahedron()
            sage: triangulation = p.triangulate(engine='internal')
            sage: bd_sc = triangulation.boundary_simplicial_complex(); bd_sc            # needs sage.graphs
            Simplicial complex with 12 vertices and 20 facets

        The boundary of every convex set is a topological sphere, so it has
        spherical homology::

            sage: bd_sc.homology()                                                      # needs sage.graphs
            {0: 0, 1: 0, 2: Z}

        It is a subcomplex of ``self`` as a :meth:`simplicial_complex`::

            sage: sc = triangulation.simplicial_complex()                               # needs sage.graphs
            sage: all(f in sc for f in bd_sc.maximal_faces())                           # needs sage.graphs
            True
        """
    @cached_method
    def interior_facets(self):
        """
        Return the interior facets of the triangulation.

        OUTPUT:

        The inward-facing boundary simplices (of dimension `d-1`) of
        the `d`-dimensional triangulation as a set. Each boundary is
        returned by a tuple of point indices.

        EXAMPLES::

            sage: triangulation = polytopes.cube().triangulate(engine='internal')
            sage: triangulation
            (<0,1,2,7>, <0,1,5,7>, <0,2,3,7>, <0,3,4,7>, <0,4,5,7>, <1,5,6,7>)
            sage: triangulation.boundary()
            frozenset({(0, 1, 2),
                       (0, 1, 5),
                       (0, 2, 3),
                       (0, 3, 4),
                       (0, 4, 5),
                       (1, 2, 7),
                       (1, 5, 6),
                       (1, 6, 7),
                       (2, 3, 7),
                       (3, 4, 7),
                       (4, 5, 7),
                       (5, 6, 7)})
            sage: triangulation.interior_facets()
            frozenset({(0, 1, 7), (0, 2, 7), (0, 3, 7), (0, 4, 7), (0, 5, 7), (1, 5, 7)})
        """
    def polyhedral_complex(self, **kwds):
        """
        Return ``self`` as a :class:`~sage.geometry.polyhedral_complex.PolyhedralComplex`.

        OUTPUT:

        A :class:`~sage.geometry.polyhedral_complex.PolyhedralComplex` whose maximal cells
        are the simplices of the triangulation.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: pc = PointConfiguration(P.vertices())
            sage: T = pc.placing_triangulation(); T
            (<0,1,2,7>, <0,1,5,7>, <0,2,3,7>, <0,3,4,7>, <0,4,5,7>, <1,5,6,7>)
            sage: C = T.polyhedral_complex(); C                                         # needs sage.graphs
            Polyhedral complex with 6 maximal cells
            sage: [P.vertices_list() for P in C.maximal_cells_sorted()]                 # needs sage.graphs
            [[[-1, -1, -1], [-1, -1, 1], [-1, 1, 1], [1, -1, -1]],
             [[-1, -1, -1], [-1, 1, -1], [-1, 1, 1], [1, 1, -1]],
             [[-1, -1, -1], [-1, 1, 1], [1, -1, -1], [1, 1, -1]],
             [[-1, -1, 1], [-1, 1, 1], [1, -1, -1], [1, -1, 1]],
             [[-1, 1, 1], [1, -1, -1], [1, -1, 1], [1, 1, 1]],
             [[-1, 1, 1], [1, -1, -1], [1, 1, -1], [1, 1, 1]]]
        """
    def boundary_polyhedral_complex(self, **kwds):
        """
        Return the boundary of ``self`` as a :class:`~sage.geometry.polyhedral_complex.PolyhedralComplex`.

        OUTPUT:

        A :class:`~sage.geometry.polyhedral_complex.PolyhedralComplex` whose maximal cells
        are the simplices of the boundary of ``self``.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: pc = PointConfiguration(P.vertices())
            sage: T = pc.placing_triangulation(); T
            (<0,1,2,7>, <0,1,5,7>, <0,2,3,7>, <0,3,4,7>, <0,4,5,7>, <1,5,6,7>)
            sage: bd_C = T.boundary_polyhedral_complex(); bd_C                          # needs sage.graphs
            Polyhedral complex with 12 maximal cells
            sage: [P.vertices_list() for P in bd_C.maximal_cells_sorted()]              # needs sage.graphs
            [[[-1, -1, -1], [-1, -1, 1], [-1, 1, 1]],
             [[-1, -1, -1], [-1, -1, 1], [1, -1, -1]],
             [[-1, -1, -1], [-1, 1, -1], [-1, 1, 1]],
             [[-1, -1, -1], [-1, 1, -1], [1, 1, -1]],
             [[-1, -1, -1], [1, -1, -1], [1, 1, -1]],
             [[-1, -1, 1], [-1, 1, 1], [1, -1, 1]],
             [[-1, -1, 1], [1, -1, -1], [1, -1, 1]],
             [[-1, 1, -1], [-1, 1, 1], [1, 1, -1]],
             [[-1, 1, 1], [1, -1, 1], [1, 1, 1]],
             [[-1, 1, 1], [1, 1, -1], [1, 1, 1]],
             [[1, -1, -1], [1, -1, 1], [1, 1, 1]],
             [[1, -1, -1], [1, 1, -1], [1, 1, 1]]]

        It is a subcomplex of ``self`` as a :meth:`polyhedral_complex`::

            sage: C = T.polyhedral_complex()                                            # needs sage.graphs
            sage: bd_C.is_subcomplex(C)                                                 # needs sage.graphs
            True
        """
    @cached_method
    def normal_cone(self):
        '''
        Return the (closure of the) normal cone of the triangulation.

        Recall that a regular triangulation is one that equals the
        "crease lines" of a convex piecewise-linear function. This
        support function is not unique, for example, you can scale it
        by a positive constant. The set of all piecewise-linear
        functions with fixed creases forms an open cone. This cone can
        be interpreted as the cone of normal vectors at a point of the
        secondary polytope, which is why we call it normal cone. See
        [GKZ1994]_ Section 7.1 for details.

        OUTPUT:

        The closure of the normal cone. The `i`-th entry equals the
        value of the piecewise-linear function at the `i`-th point of
        the configuration.

        For an irregular triangulation, the normal cone is empty. In
        this case, a single point (the origin) is returned.

        EXAMPLES::

            sage: triangulation = polytopes.hypercube(2).triangulate(engine=\'internal\')
            sage: triangulation
            (<0,1,3>, <1,2,3>)
            sage: N = triangulation.normal_cone();  N
            4-d cone in 4-d lattice
            sage: N.rays()
            ( 0,  0,  0, -1),
            ( 0,  0,  1,  1),
            ( 0,  0, -1, -1),
            ( 1,  0,  0,  1),
            (-1,  0,  0, -1),
            ( 0,  1,  0, -1),
            ( 0, -1,  0,  1)
            in Ambient free module of rank 4
            over the principal ideal domain Integer Ring
            sage: N.dual().rays()
            (1, -1, 1, -1)
            in Ambient free module of rank 4
            over the principal ideal domain Integer Ring

        TESTS::

            sage: polytopes.simplex(2).triangulate().normal_cone()
            3-d cone in 3-d lattice
            sage: _.dual().is_trivial()
            True
        '''
    def adjacency_graph(self):
        """
        Return a graph showing which simplices are adjacent in the triangulation.

        OUTPUT:

        A graph consisting of vertices referring to the simplices in the
        triangulation, and edges showing which simplices are adjacent to each
        other.

        .. SEEALSO::

            * To obtain the triangulation's 1-skeleton, use
              :meth:`SimplicialComplex.graph` through
              ``MyTriangulation.simplicial_complex().graph()``.

        AUTHORS:

        * Stephen Farley (2013-08-10): initial version

        EXAMPLES::

            sage: p = PointConfiguration([[1,0,0], [0,1,0], [0,0,1], [-1,0,1],
            ....:                         [1,0,-1], [-1,0,0], [0,-1,0], [0,0,-1]])
            sage: t = p.triangulate()
            sage: t.adjacency_graph()                                                   # needs sage.graphs
            Graph on 8 vertices
        """
