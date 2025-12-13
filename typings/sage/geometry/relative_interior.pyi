from sage.geometry.convex_set import ConvexSet_relatively_open as ConvexSet_relatively_open

class RelativeInterior(ConvexSet_relatively_open):
    """
    The relative interior of a polyhedron or cone.

    This class should not be used directly. Use methods
    :meth:`~sage.geometry.polyhedron.Polyhedron_base.relative_interior`,
    :meth:`~sage.geometry.polyhedron.Polyhedron_base.interior`,
    :meth:`~sage.geometry.cone.ConvexRationalPolyhedralCone.relative_interior`,
    :meth:`~sage.geometry.cone.ConvexRationalPolyhedralCone.interior` instead.

    EXAMPLES::

        sage: segment = Polyhedron([[1, 2], [3, 4]])
        sage: segment.relative_interior()
        Relative interior of
         a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
        sage: octant = Cone([(1,0,0), (0,1,0), (0,0,1)])
        sage: octant.relative_interior()
        Relative interior of 3-d cone in 3-d lattice N
    """
    def __init__(self, polyhedron) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``polyhedron`` -- an instance of :class:`Polyhedron_base` or
          :class:`ConvexRationalPolyhedralCone`

        TESTS::

            sage: P = Polyhedron([[1, 2], [3, 4]])
            sage: from sage.geometry.relative_interior import RelativeInterior
            sage: TestSuite(RelativeInterior(P)).run()
        """
    def __hash__(self):
        """
        TESTS::

            sage: P = Polyhedron([[1, 2], [3, 4]])
            sage: Q = Polyhedron([[3, 4], [1, 2]])
            sage: hash(P.relative_interior()) == hash(Q.relative_interior())
            True
        """
    def __contains__(self, point) -> bool:
        """
        Return whether ``self`` contains ``point``.

        EXAMPLES::

            sage: octant = Cone([(1,0,0), (0,1,0), (0,0,1)])
            sage: ri_octant = octant.relative_interior(); ri_octant
            Relative interior of 3-d cone in 3-d lattice N
            sage: (1, 1, 1) in ri_octant
            True
            sage: (1, 0, 0) in ri_octant
            False
        """
    def ambient(self):
        """
        Return the ambient convex set or space.

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of
             a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: ri_segment.ambient()
            Vector space of dimension 2 over Rational Field
        """
    def ambient_vector_space(self, base_field=None):
        """
        Return the ambient vector space.

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of
             a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: ri_segment.ambient_vector_space()
            Vector space of dimension 2 over Rational Field
        """
    def ambient_dim(self):
        """
        Return the dimension of the ambient space.

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: segment.ambient_dim()
            2
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of
             a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: ri_segment.ambient_dim()
            2
        """
    def an_affine_basis(self):
        """
        Return points that form an affine basis for the affine hull.

        The points are guaranteed to lie in the topological closure of ``self``.

        EXAMPLES::

            sage: segment = Polyhedron([[1, 0], [0, 1]])
            sage: segment.relative_interior().an_affine_basis()
            [A vertex at (1, 0), A vertex at (0, 1)]
        """
    def dim(self):
        """
        Return the dimension of ``self``.

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: segment.dim()
            1
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of
             a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: ri_segment.dim()
            1
        """
    def interior(self):
        """
        Return the interior of ``self``.

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of
             a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: ri_segment.interior()
            The empty polyhedron in ZZ^2

            sage: octant = Cone([(1,0,0), (0,1,0), (0,0,1)])
            sage: ri_octant = octant.relative_interior(); ri_octant
            Relative interior of 3-d cone in 3-d lattice N
            sage: ri_octant.interior() is ri_octant
            True
        """
    def relative_interior(self):
        """
        Return the relative interior of ``self``.

        As ``self`` is already relatively open, this method just returns ``self``.

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of
             a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: ri_segment.relative_interior() is ri_segment
            True
        """
    def closure(self):
        """
        Return the topological closure of ``self``.

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of
             a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: ri_segment.closure() is segment
            True
        """
    def is_universe(self):
        """
        Return whether ``self`` is the whole ambient space.

        OUTPUT: boolean

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of
             a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: ri_segment.is_universe()
            False
        """
    def is_closed(self):
        """
        Return whether ``self`` is closed.

        OUTPUT: boolean

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: ri_segment.is_closed()
            False
        """
    def representative_point(self):
        '''
        Return a "generic" point of ``self``.

        OUTPUT:

        A point in ``self`` (thus, in the relative interior of ``self``) as a coordinate vector.

        EXAMPLES::

            sage: C = Cone([[1, 2, 0], [2, 1, 0]])
            sage: C.relative_interior().representative_point()
            (1, 1, 0)
        '''
    def __eq__(self, other):
        """
        Compare ``self`` and ``other``.

        INPUT:

        - ``other`` -- any object

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of
             a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: segment2 = Polyhedron([[1, 2], [3, 4]], base_ring=AA)                 # needs sage.rings.number_field
            sage: ri_segment2 = segment2.relative_interior(); ri_segment2               # needs sage.rings.number_field
            Relative interior of
             a 1-dimensional polyhedron in AA^2 defined as the convex hull of 2 vertices
            sage: ri_segment == ri_segment2                                             # needs sage.rings.number_field
            True

        TESTS::

            sage: empty = Polyhedron(ambient_dim=2)
            sage: ri_segment == empty
            False
        """
    def __ne__(self, other):
        """
        Compare ``self`` and ``other``.

        INPUT:

        - ``other`` -- any object

        TESTS::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of
             a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: segment2 = Polyhedron([[1, 2], [3, 4]], base_ring=AA)                 # needs sage.rings.number_field
            sage: ri_segment2 = segment2.relative_interior(); ri_segment2               # needs sage.rings.number_field
            Relative interior of
             a 1-dimensional polyhedron in AA^2 defined as the convex hull of 2 vertices
            sage: ri_segment != ri_segment2                                             # needs sage.rings.number_field
            False
        """
    def dilation(self, scalar):
        """
        Return the dilated (uniformly stretched) set.

        INPUT:

        - ``scalar`` -- a scalar

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of a
             1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: A = ri_segment.dilation(2); A
            Relative interior of a
             1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: A.closure().vertices()
            (A vertex at (2, 4), A vertex at (6, 8))
            sage: B = ri_segment.dilation(-1/3); B
            Relative interior of a
             1-dimensional polyhedron in QQ^2 defined as the convex hull of 2 vertices
            sage: B.closure().vertices()
            (A vertex at (-1, -4/3), A vertex at (-1/3, -2/3))
            sage: C = ri_segment.dilation(0); C
            A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: C.vertices()
            (A vertex at (0, 0),)
        """
    def linear_transformation(self, linear_transf, **kwds):
        """
        Return the linear transformation of ``self``.

        By [Roc1970]_, Theorem 6.6, the linear transformation of a relative interior
        is the relative interior of the linear transformation.

        INPUT:

        - ``linear_transf`` -- a matrix
        - ``**kwds`` -- passed to the :meth:`linear_transformation` method of
          the closure of ``self``

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of a
             1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: T = matrix([[1, 1]])
            sage: A = ri_segment.linear_transformation(T); A
            Relative interior of a
             1-dimensional polyhedron in ZZ^1 defined as the convex hull of 2 vertices
            sage: A.closure().vertices()
            (A vertex at (3), A vertex at (7))
        """
    def translation(self, displacement):
        """
        Return the translation of ``self`` by a ``displacement`` vector.

        INPUT:

        - ``displacement`` -- a displacement vector or a list/tuple of
          coordinates that determines a displacement vector

        EXAMPLES::

            sage: segment = Polyhedron([[1, 2], [3, 4]])
            sage: ri_segment = segment.relative_interior(); ri_segment
            Relative interior of a
             1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: t = vector([100, 100])
            sage: ri_segment.translation(t)
            Relative interior of a
             1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: ri_segment.closure().vertices()
            (A vertex at (1, 2), A vertex at (3, 4))
        """
