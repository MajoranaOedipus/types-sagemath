from _typeshed import Incomplete
from collections.abc import Generator
from ppl import C_Polyhedron
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.rings.integer import GCD_list as GCD_list, Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ

def LatticePolytope_PPL(*args):
    """
    Construct a new instance of the PPL-based lattice polytope class.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
        sage: LatticePolytope_PPL((0,0), (1,0), (0,1))
        A 2-dimensional lattice polytope in ZZ^2 with 3 vertices

        sage: from ppl import point, Generator_System, C_Polyhedron, Linear_Expression  # needs pplpy
        sage: p = point(Linear_Expression([2,3],0));  p                                 # needs pplpy
        point(2/1, 3/1)
        sage: LatticePolytope_PPL(p)                                                    # needs pplpy
        A 0-dimensional lattice polytope in ZZ^2 with 1 vertex

        sage: P = C_Polyhedron(Generator_System(p));  P                                 # needs pplpy
        A 0-dimensional polyhedron in QQ^2 defined as the convex hull of 1 point
        sage: LatticePolytope_PPL(P)                                                    # needs pplpy
        A 0-dimensional lattice polytope in ZZ^2 with 1 vertex

    A :exc:`TypeError` is raised if the arguments do not specify a lattice polytope::

        sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
        sage: LatticePolytope_PPL((0,0), (1/2,1))                                       # needs pplpy
        Traceback (most recent call last):
        ...
        TypeError: unable to convert rational 1/2 to an integer

        sage: from ppl import point, Generator_System, C_Polyhedron, Linear_Expression  # needs pplpy
        sage: p = point(Linear_Expression([2,3],0), 5);  p                              # needs pplpy
        point(2/5, 3/5)
        sage: LatticePolytope_PPL(p)                                                    # needs pplpy
        Traceback (most recent call last):
         ...
        TypeError: generator is not a lattice polytope generator

        sage: P = C_Polyhedron(Generator_System(p));  P                                 # needs pplpy
        A 0-dimensional polyhedron in QQ^2 defined as the convex hull of 1 point
        sage: LatticePolytope_PPL(P)                                                    # needs pplpy
        Traceback (most recent call last):
        ...
        TypeError: polyhedron has non-integral generators
    """

class LatticePolytope_PPL_class(C_Polyhedron):
    """
    The lattice polytope class.

    You should use :func:`LatticePolytope_PPL` to construct instances.

    EXAMPLES::

        sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
        sage: LatticePolytope_PPL((0,0), (1,0), (0,1))
        A 2-dimensional lattice polytope in ZZ^2 with 3 vertices
    """
    def is_bounded(self):
        """
        Return whether the lattice polytope is compact.

        OUTPUT: always ``True``, since polytopes are by definition compact

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: LatticePolytope_PPL((0,0), (1,0), (0,1)).is_bounded()
            True
        """
    @cached_method
    def n_vertices(self):
        """
        Return the number of vertices.

        OUTPUT: integer; the number of vertices

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: LatticePolytope_PPL((0,0,0), (1,0,0), (0,1,0)).n_vertices()
            3
        """
    @cached_method
    def is_simplex(self):
        """
        Return whether the polyhedron is a simplex.

        OUTPUT:

        Boolean, whether the polyhedron is a simplex (possibly of
        strictly smaller dimension than the ambient space).

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: LatticePolytope_PPL((0,0,0), (1,0,0), (0,1,0)).is_simplex()
            True
        """
    @cached_method
    def bounding_box(self):
        """
        Return the coordinates of a rectangular box containing the non-empty polytope.

        OUTPUT:

        A pair of tuples ``(box_min, box_max)`` where ``box_min`` are
        the coordinates of a point bounding the coordinates of the
        polytope from below and ``box_max`` bounds the coordinates
        from above.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: LatticePolytope_PPL((0,0), (1,0), (0,1)).bounding_box()
            ((0, 0), (1, 1))
        """
    @cached_method
    def n_integral_points(self):
        """
        Return the number of integral points.

        OUTPUT:

        Integer. The number of integral points contained in the
        lattice polytope.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: LatticePolytope_PPL((0,0), (1,0), (0,1)).n_integral_points()
            3
        """
    @cached_method
    def integral_points(self):
        """
        Return the integral points in the polyhedron.

        Uses the naive algorithm (iterate over a rectangular bounding
        box).

        OUTPUT:

        The list of integral points in the polyhedron. If the
        polyhedron is not compact, a :exc:`ValueError` is raised.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: LatticePolytope_PPL((-1,-1), (1,0), (1,1), (0,1)).integral_points()
            ((-1, -1), (0, 0), (0, 1), (1, 0), (1, 1))

            sage: simplex = LatticePolytope_PPL((1,2,3), (2,3,7), (-2,-3,-11))
            sage: simplex.integral_points()
            ((-2, -3, -11), (0, 0, -2), (1, 2, 3), (2, 3, 7))

        The polyhedron need not be full-dimensional::

            sage: simplex = LatticePolytope_PPL((1,2,3,5), (2,3,7,5), (-2,-3,-11,5))
            sage: simplex.integral_points()
            ((-2, -3, -11, 5), (0, 0, -2, 5), (1, 2, 3, 5), (2, 3, 7, 5))

            sage: point = LatticePolytope_PPL((2,3,7))
            sage: point.integral_points()
            ((2, 3, 7),)

            sage: empty = LatticePolytope_PPL()
            sage: empty.integral_points()
            ()

        Here is a simplex where the naive algorithm of running over
        all points in a rectangular bounding box no longer works fast
        enough::

            sage: v = [(1,0,7,-1), (-2,-2,4,-3), (-1,-1,-1,4), (2,9,0,-5), (-2,-1,5,1)]
            sage: simplex = LatticePolytope_PPL(v); simplex
            A 4-dimensional lattice polytope in ZZ^4 with 5 vertices
            sage: len(simplex.integral_points())
            49

        Finally, the 3-d reflexive polytope number 4078::

            sage: v = [(1,0,0), (0,1,0), (0,0,1), (0,0,-1), (0,-2,1),
            ....:      (-1,2,-1), (-1,2,-2), (-1,1,-2), (-1,-1,2), (-1,-3,2)]
            sage: P = LatticePolytope_PPL(*v)
            sage: pts1 = P.integral_points()            # Sage's own code
            sage: pts2 = LatticePolytope(v).points()                                    # needs palp
            sage: for p in pts1: p.set_immutable()
            sage: set(pts1) == set(pts2)                                                # needs palp
            True

            sage: len(Polyhedron(v).integral_points())  # takes about 1 ms
            23
            sage: len(LatticePolytope(v).points())      # takes about 13 ms             # needs palp
            23
            sage: len(LatticePolytope_PPL(*v).integral_points())  # takes about 0.5 ms
            23
        """
    @cached_method
    def integral_points_not_interior_to_facets(self):
        """
        Return the integral points not interior to facets.

        OUTPUT:

        A tuple whose entries are the coordinate vectors of integral
        points not interior to facets (codimension one faces) of the
        lattice polytope.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: square = LatticePolytope_PPL((-1,-1), (-1,1), (1,-1), (1,1))
            sage: square.n_integral_points()
            9
            sage: square.integral_points_not_interior_to_facets()
            ((-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1))
        """
    @cached_method
    def vertices(self):
        """
        Return the vertices as a tuple of `\\ZZ`-vectors.

        OUTPUT:

        A tuple of `\\ZZ`-vectors. Each entry is the coordinate vector
        of an integral points of the lattice polytope.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: p = LatticePolytope_PPL((-9,-6,-1,-1),
            ....:                         (0,0,0,1), (0,0,1,0), (0,1,0,0), (1,0,0,0))
            sage: p.vertices()
            ((-9, -6, -1, -1), (0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0))
            sage: p.minimized_generators()
            Generator_System {point(-9/1, -6/1, -1/1, -1/1), point(0/1, 0/1, 0/1, 1/1),
            point(0/1, 0/1, 1/1, 0/1), point(0/1, 1/1, 0/1, 0/1), point(1/1, 0/1, 0/1, 0/1)}
        """
    def vertices_saturating(self, constraint):
        """
        Return the vertices saturating the constraint.

        INPUT:

        - ``constraint`` -- a constraint (inequality or equation) of
          the polytope

        OUTPUT:

        The tuple of vertices saturating the constraint. The vertices
        are returned as `\\ZZ`-vectors, as in :meth:`vertices`.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: p = LatticePolytope_PPL((0,0), (0,1), (1,0))
            sage: ieq = next(iter(p.constraints()));  ieq
            x0>=0
            sage: p.vertices_saturating(ieq)
            ((0, 0), (0, 1))
        """
    @cached_method
    def is_full_dimensional(self):
        """
        Return whether the lattice polytope is full dimensional.

        OUTPUT: boolean; whether the :meth:`affine_dimension` equals the
        ambient space dimension

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: p = LatticePolytope_PPL((0,0), (0,1))
            sage: p.is_full_dimensional()
            False
            sage: q = LatticePolytope_PPL((0,0), (0,1), (1,0))
            sage: q.is_full_dimensional()
            True
        """
    def fibration_generator(self, dim) -> Generator[Incomplete, None, Incomplete]:
        """
        Generate the lattice polytope fibrations.

        For the purposes of this function, a lattice polytope fiber is
        a sub-lattice polytope. Projecting the plane spanned by the
        subpolytope to a point yields another lattice polytope, the
        base of the fibration.

        INPUT:

        - ``dim`` -- integer; the dimension of the lattice polytope
          fiber

        OUTPUT:

        A generator yielding the distinct lattice polytope fibers of
        given dimension.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: p = LatticePolytope_PPL((-9,-6,-1,-1),
            ....:                         (0,0,0,1), (0,0,1,0), (0,1,0,0), (1,0,0,0))
            sage: list(p.fibration_generator(2))
            [A 2-dimensional lattice polytope in ZZ^4 with 3 vertices]
        """
    def pointsets_mod_automorphism(self, pointsets):
        """
        Return ``pointsets`` modulo the automorphisms of ``self``.

        INPUT:

        - ``polytopes`` -- tuple/list/iterable of subsets of the
          integral points of ``self``

        OUTPUT:

        Representatives of the point sets modulo the
        :meth:`lattice_automorphism_group` of ``self``.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: square = LatticePolytope_PPL((-1,-1), (-1,1), (1,-1), (1,1))
            sage: fibers = [f.vertices() for f in square.fibration_generator(1)]
            sage: square.pointsets_mod_automorphism(fibers)                             # needs sage.graphs sage.groups
            (frozenset({(-1, -1), (1, 1)}), frozenset({(-1, 0), (1, 0)}))

            sage: cell24 = LatticePolytope_PPL(
            ....:     (1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1), (1,-1,-1,1), (0,0,-1,1),
            ....:     (0,-1,0,1), (-1,0,0,1), (1,0,0,-1), (0,1,0,-1), (0,0,1,-1), (-1,1,1,-1),
            ....:     (1,-1,-1,0), (0,0,-1,0), (0,-1,0,0), (-1,0,0,0), (1,-1,0,0), (1,0,-1,0),
            ....:     (0,1,1,-1), (-1,1,1,0), (-1,1,0,0), (-1,0,1,0), (0,-1,-1,1), (0,0,0,-1))
            sage: fibers = [f.vertices() for f in cell24.fibration_generator(2)]
            sage: cell24.pointsets_mod_automorphism(fibers)     # long time             # needs sage.graphs sage.groups
            (frozenset({(-1, 0, 0, 0),
                        (-1, 0, 0, 1),
                        (0, 0, 0, -1),
                        (0, 0, 0, 1),
                        (1, 0, 0, -1),
                        (1, 0, 0, 0)}),
             frozenset({(-1, 0, 0, 0), (-1, 1, 1, 0), (1, -1, -1, 0), (1, 0, 0, 0)}))
        """
    @cached_method
    def ambient_space(self):
        """
        Return the ambient space.

        OUTPUT:

        The free module `\\ZZ^d`, where `d` is the ambient space
        dimension.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: point = LatticePolytope_PPL((1,2,3))
            sage: point.ambient_space()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
        """
    def contains(self, point_coordinates):
        """
        Test whether point is contained in the polytope.

        INPUT:

        - ``point_coordinates`` -- list/tuple/iterable of rational
          numbers; the coordinates of the point

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: line = LatticePolytope_PPL((1,2,3), (-1,-2,-3))
            sage: line.contains([0,0,0])
            True
            sage: line.contains([1,0,0])
            False
        """
    @cached_method
    def contains_origin(self):
        """
        Test whether the polytope contains the origin.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: LatticePolytope_PPL((1,2,3), (-1,-2,-3)).contains_origin()
            True
            sage: LatticePolytope_PPL((1,2,5), (-1,-2,-3)).contains_origin()
            False
        """
    @cached_method
    def affine_space(self):
        """
        Return the affine space spanned by the polytope.

        OUTPUT:

        The free module `\\ZZ^n`, where `n` is the dimension of the
        affine space spanned by the points of the polytope.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: point = LatticePolytope_PPL((1,2,3))
            sage: point.affine_space()
            Free module of degree 3 and rank 0 over Integer Ring
            Echelon basis matrix:
            []
            sage: line = LatticePolytope_PPL((1,1,1), (1,2,3))
            sage: line.affine_space()
            Free module of degree 3 and rank 1 over Integer Ring
            Echelon basis matrix:
            [0 1 2]
        """
    def affine_lattice_polytope(self):
        """
        Return the lattice polytope restricted to
        :meth:`affine_space`.

        OUTPUT:

        A new, full-dimensional lattice polytope.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: poly_4d = LatticePolytope_PPL((-9,-6,0,0), (0,1,0,0), (1,0,0,0));  poly_4d
            A 2-dimensional lattice polytope in ZZ^4 with 3 vertices
            sage: poly_4d.space_dimension()
            4
            sage: poly_2d = poly_4d.affine_lattice_polytope();  poly_2d
            A 2-dimensional lattice polytope in ZZ^2 with 3 vertices
            sage: poly_2d.space_dimension()
            2
        """
    def base_projection(self, fiber):
        """
        The projection that maps the sub-polytope ``fiber`` to a
        single point.

        OUTPUT:

        The quotient module of the ambient space modulo the
        :meth:`affine_space` spanned by the fiber.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: poly = LatticePolytope_PPL((-9,-6,-1,-1),
            ....:                            (0,0,0,1), (0,0,1,0), (0,1,0,0), (1,0,0,0))
            sage: fiber = next(poly.fibration_generator(2))
            sage: poly.base_projection(fiber)
            Finitely generated module V/W over Integer Ring with invariants (0, 0)
        """
    def base_projection_matrix(self, fiber):
        """
        The projection that maps the sub-polytope ``fiber`` to a
        single point.

        OUTPUT:

        An integer matrix that represents the projection to the
        base.

        .. SEEALSO::

            The :meth:`base_projection` yields equivalent information,
            and is easier to use. However, just returning the matrix
            has lower overhead.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: poly = LatticePolytope_PPL((-9,-6,-1,-1),
            ....:                            (0,0,0,1), (0,0,1,0), (0,1,0,0), (1,0,0,0))
            sage: fiber = next(poly.fibration_generator(2))
            sage: poly.base_projection_matrix(fiber)
            [ 0  0 -1  0]
            [ 0  0  0 -1]

        Note that the basis choice in :meth:`base_projection` for the
        quotient is usually different::

            sage: proj = poly.base_projection(fiber)
            sage: proj_matrix = poly.base_projection_matrix(fiber)
            sage: [proj(p) for p in poly.integral_points()]
            [(-1, -1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 1), (1, 0)]
            sage: [proj_matrix*p for p in poly.integral_points()]
            [(1, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, -1), (-1, 0)]
        """
    def base_rays(self, fiber, points):
        """
        Return the primitive lattice vectors that generate the
        direction given by the base projection of points.

        INPUT:

        - ``fiber`` -- a sub-lattice polytope defining the
          :meth:`base_projection`

        - ``points`` -- the points to project to the base

        OUTPUT: a tuple of primitive `\\ZZ`-vectors

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: poly = LatticePolytope_PPL((-9,-6,-1,-1),
            ....:                            (0,0,0,1), (0,0,1,0), (0,1,0,0), (1,0,0,0))
            sage: fiber = next(poly.fibration_generator(2))
            sage: poly.base_rays(fiber, poly.integral_points_not_interior_to_facets())
            ((-1, -1), (0, 1), (1, 0))

            sage: p = LatticePolytope_PPL((1,0), (1,2), (-1,0))
            sage: f = LatticePolytope_PPL((1,0), (-1,0))
            sage: p.base_rays(f, p.integral_points())
            ((1),)
        """
    @cached_method
    def has_IP_property(self) -> bool:
        """
        Whether the lattice polytope has the IP property.

        That is, the polytope is full-dimensional and the origin is a
        interior point not on the boundary.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: LatticePolytope_PPL((-1,-1), (0,1), (1,0)).has_IP_property()
            True
            sage: LatticePolytope_PPL((-1,-1), (1,1)).has_IP_property()
            False
        """
    @cached_method
    def restricted_automorphism_group(self, vertex_labels=None):
        """
        Return the restricted automorphism group.

        First, let the linear automorphism group be the subgroup of
        the Euclidean group `E(d) = GL(d,\\RR) \\ltimes \\RR^d`
        preserving the `d`-dimensional polyhedron. The Euclidean group
        acts in the usual way `\\vec{x}\\mapsto A\\vec{x}+b` on the
        ambient space. The restricted automorphism group is the
        subgroup of the linear automorphism group generated by
        permutations of vertices. If the polytope is full-dimensional,
        it is equal to the full (unrestricted) automorphism group.

        INPUT:

        - ``vertex_labels`` -- tuple or ``None`` (default). The
          labels of the vertices that will be used in the output
          permutation group. By default, the vertices are used
          themselves.

        OUTPUT:

        A
        :class:`PermutationGroup<sage.groups.perm_gps.permgroup.PermutationGroup_generic>`
        acting on the vertices (or the ``vertex_labels``, if
        specified).

        REFERENCES:

        [BSS2009]_

        EXAMPLES::

            sage: # needs sage.graphs sage.groups
            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: Z3square = LatticePolytope_PPL((0,0), (1,2), (2,1), (3,3))
            sage: G1234 = Z3square.restricted_automorphism_group(
            ....:     vertex_labels=(1,2,3,4))
            sage: G1234 == PermutationGroup([[(2,3)], [(1,2),(3,4)]])
            True
            sage: G = Z3square.restricted_automorphism_group()
            sage: G == PermutationGroup([[((1,2),(2,1))], [((0,0),(1,2)),
            ....:                         ((2,1),(3,3))], [((0,0),(3,3))]])
            True
            sage: set(G.domain()) == set(Z3square.vertices())
            True
            sage: (set(tuple(x) for x in G.orbit(Z3square.vertices()[0]))
            ....:   == set([(0, 0), (1, 2), (3, 3), (2, 1)]))
            True
            sage: cell24 = LatticePolytope_PPL(
            ....:     (1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1), (1,-1,-1,1), (0,0,-1,1),
            ....:     (0,-1,0,1), (-1,0,0,1), (1,0,0,-1), (0,1,0,-1), (0,0,1,-1), (-1,1,1,-1),
            ....:     (1,-1,-1,0), (0,0,-1,0), (0,-1,0,0), (-1,0,0,0), (1,-1,0,0), (1,0,-1,0),
            ....:     (0,1,1,-1), (-1,1,1,0), (-1,1,0,0), (-1,0,1,0), (0,-1,-1,1), (0,0,0,-1))
            sage: cell24.restricted_automorphism_group().cardinality()
            1152
        """
    @cached_method
    def lattice_automorphism_group(self, points=None, point_labels=None):
        """
        The integral subgroup of the restricted automorphism group.

        INPUT:

        - ``points`` -- tuple of coordinate vectors or ``None``
          (default). If specified, the points must form complete
          orbits under the lattice automorphism group. If ``None`` all
          vertices are used.

        - ``point_labels`` -- tuple of labels for the ``points`` or
          ``None`` (default). These will be used as labels for the do
          permutation group. If ``None``, the ``points`` will be used
          themselves.

        OUTPUT:

        The integral subgroup of the restricted automorphism group
        acting on the given ``points``, or all vertices if not
        specified.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: Z3square = LatticePolytope_PPL((0,0), (1,2), (2,1), (3,3))
            sage: Z3square.lattice_automorphism_group()                                 # needs sage.graphs sage.groups
            Permutation Group with generators [(), ((1,2),(2,1)),
            ((0,0),(3,3)), ((0,0),(3,3))((1,2),(2,1))]

            sage: G1 = Z3square.lattice_automorphism_group(point_labels=(1,2,3,4))      # needs sage.graphs sage.groups
            sage: G1                                                                    # needs sage.graphs sage.groups
            Permutation Group with generators [(), (2,3), (1,4), (1,4)(2,3)]
            sage: G1.cardinality()                                                      # needs sage.graphs sage.groups
            4

            sage: G2 = Z3square.restricted_automorphism_group(vertex_labels=(1,2,3,4))  # needs sage.graphs sage.groups
            sage: G2 == PermutationGroup([[(2,3)], [(1,2),(3,4)], [(1,4)]])             # needs sage.graphs sage.groups
            True
            sage: G2.cardinality()                                                      # needs sage.graphs sage.groups
            8

            sage: points = Z3square.integral_points(); points
            ((0, 0), (1, 1), (1, 2), (2, 1), (2, 2), (3, 3))
            sage: Z3square.lattice_automorphism_group(points,                           # needs sage.graphs sage.groups
            ....:                                     point_labels=(1,2,3,4,5,6))
            Permutation Group with generators [(), (3,4), (1,6)(2,5), (1,6)(2,5)(3,4)]

        Point labels also work for lattice polytopes that are not
        full-dimensional, see :issue:`16669`::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: lp = LatticePolytope_PPL((1,0,0), (0,1,0), (-1,-1,0))
            sage: lp.lattice_automorphism_group(point_labels=(0,1,2))                   # needs sage.graphs sage.groups
            Permutation Group with generators [(), (1,2), (0,1), (0,1,2), (0,2,1), (0,2)]
        """
    def sub_polytope_generator(self) -> Generator[Incomplete]:
        """
        Generate the maximal lattice sub-polytopes.

        OUTPUT:

        A generator yielding the maximal (with respect to inclusion)
        lattice sub polytopes. That is, each can be gotten as the
        convex hull of the integral points of ``self`` with one vertex
        removed.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: P = LatticePolytope_PPL((1,0,0), (0,1,0), (0,0,1), (-1,-1,-1))
            sage: for p in P.sub_polytope_generator():
            ....:     print(p.vertices())
            ((0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0))
            ((-1, -1, -1), (0, 0, 0), (0, 1, 0), (1, 0, 0))
            ((-1, -1, -1), (0, 0, 0), (0, 0, 1), (1, 0, 0))
            ((-1, -1, -1), (0, 0, 0), (0, 0, 1), (0, 1, 0))
        """
    def embed_in_reflexive_polytope(self, output: str = 'hom'):
        """
        Find an embedding as a sub-polytope of a maximal reflexive
        polytope.

        INPUT:

        - ``hom`` -- string. One of ``'hom'`` (default),
          ``'polytope'``, or ``points``. How the embedding is
          returned. See the output section for details.

        OUTPUT:

        An embedding into a reflexive polytope. Depending on the
        ``output`` option slightly different data is returned.

        - If ``output='hom'``, a map from a reflexive polytope onto
          ``self`` is returned.

        - If ``output='polytope'``, a reflexive polytope that contains
          ``self`` (up to a lattice linear transformation) is
          returned. That is, the domain of the ``output='hom'`` map is
          returned. If the affine span of ``self`` is less or equal
          2-dimensional, the output is one of the following three
          possibilities:

          :func:`~sage.geometry.polyhedron.ppl_lattice_polygon.polar_P2_polytope`,
          :func:`~sage.geometry.polyhedron.ppl_lattice_polygon.polar_P1xP1_polytope`,
          or
          :func:`~sage.geometry.polyhedron.ppl_lattice_polygon.polar_P2_112_polytope`.

        - If ``output='points'``, a dictionary containing the integral
          points of ``self`` as keys and the corresponding integral
          point of the reflexive polytope as value.

        If there is no such embedding, a
        :class:`~sage.geometry.polyhedron.lattice_euclidean_group_element.LatticePolytopeNoEmbeddingError`
        is raised. Even if it exists, the ambient reflexive polytope
        is usually not uniquely determined and a random but fixed
        choice will be returned.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.ppl_lattice_polytope import LatticePolytope_PPL
            sage: polygon = LatticePolytope_PPL((0,0,2,1), (0,1,2,0), (2,3,0,0), (2,0,0,3))
            sage: polygon.embed_in_reflexive_polytope()
            The map A*x+b with
              A=
                [ 1  1]
                [ 0  1]
                [-1 -1]
                [ 1  0]
              b = (-1, 0, 3, 0)
            sage: polygon.embed_in_reflexive_polytope('polytope')
            A 2-dimensional lattice polytope in ZZ^2 with 3 vertices
            sage: polygon.embed_in_reflexive_polytope('points')
            {(0, 0, 2, 1): (1, 0),
             (0, 1, 2, 0): (0, 1),
             (1, 0, 1, 2): (2, 0),
             (1, 1, 1, 1): (1, 1),
             (1, 2, 1, 0): (0, 2),
             (2, 0, 0, 3): (3, 0),
             (2, 1, 0, 2): (2, 1),
             (2, 2, 0, 1): (1, 2),
             (2, 3, 0, 0): (0, 3)}

            sage: LatticePolytope_PPL((0,0), (4,0), (0,4)).embed_in_reflexive_polytope()
            Traceback (most recent call last):
            ...
            LatticePolytopeNoEmbeddingError: not a sub-polytope of a reflexive polygon
        """
