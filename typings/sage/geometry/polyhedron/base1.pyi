from .base0 import Polyhedron_base0 as Polyhedron_base0
from sage.geometry.convex_set import ConvexSet_closed as ConvexSet_closed
from sage.geometry.relative_interior import RelativeInterior as RelativeInterior
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module_element import vector as vector
from sage.structure.element import coerce_binop as coerce_binop
from sage.structure.richcmp import op_NE as op_NE, rich_to_bool as rich_to_bool

class Polyhedron_base1(Polyhedron_base0, ConvexSet_closed):
    """
    Convex set methods for polyhedra,
    but not constructions such as dilation or product.

    See :class:`sage.geometry.polyhedron.base.Polyhedron_base`.

    TESTS::

        sage: from sage.geometry.polyhedron.base1 import Polyhedron_base1
        sage: P = polytopes.cube()
        sage: Q = polytopes.cube()
        sage: Polyhedron_base1.__hash__(P) == Polyhedron_base1.__hash__(Q)
        True
        sage: Polyhedron_base1.__repr__(P)
        'A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices'
        sage: Polyhedron_base1.is_empty(P)
        False
        sage: Polyhedron_base1.is_universe(P)
        False
        sage: Polyhedron_base1.dim(P)
        3
        sage: Polyhedron_base1.ambient_vector_space(P)
        Vector space of dimension 3 over Rational Field
        sage: Polyhedron_base1.ambient_dim(P)
        3
        sage: Polyhedron_base1.an_affine_basis(P)
        [A vertex at (-1, -1, -1),
        A vertex at (1, -1, -1),
        A vertex at (1, -1, 1),
        A vertex at (1, 1, -1)]
        sage: list(Polyhedron_base1._some_elements_(P))
        [(0, 0, 0),
        (1, -1, -1),
        (1, 0, -1),
        (1, 1/2, 0),
        (1, -1/4, 1/2),
        (0, -5/8, 3/4)]
        sage: Polyhedron_base1.contains(P, vector([1, 1, 1]))
        True
        sage: Polyhedron_base1.interior_contains(P, vector([1, 1, 1]))
        False
        sage: Polyhedron_base1.is_relatively_open(P)
        False
        sage: Polyhedron_base1.relative_interior.f(P) == Polyhedron_base1.interior.f(P)
        True
    """
    def __hash__(self):
        """
        TESTS::

            sage: # needs sage.rings.number_field
            sage: K.<a> = QuadraticField(2)
            sage: p = Polyhedron(vertices=[(0, 1, a), (3, a, 5)],
            ....:                rays=[(a, 2, 3), (0, 0, 1)],
            ....:                base_ring=K)
            sage: q = Polyhedron(vertices=[(3, a, 5), (0, 1, a)],
            ....:                rays=[(0, 0, 1), (a, 2, 3)],
            ....:                base_ring=K)
            sage: hash(p) == hash(q)
            True
        """
    def is_empty(self):
        """
        Test whether the polyhedron is the empty polyhedron.

        OUTPUT: boolean

        EXAMPLES::

            sage: P = Polyhedron(vertices=[[1,0,0],[0,1,0],[0,0,1]]);  P
            A 2-dimensional polyhedron in ZZ^3 defined as the convex hull of 3 vertices
            sage: P.is_empty(), P.is_universe()
            (False, False)

            sage: Q = Polyhedron(vertices=());  Q
            The empty polyhedron in ZZ^0
            sage: Q.is_empty(), Q.is_universe()
            (True, False)

            sage: R = Polyhedron(lines=[(1,0),(0,1)]);  R
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: R.is_empty(), R.is_universe()
            (False, True)
        """
    def is_universe(self):
        """
        Test whether the polyhedron is the whole ambient space.

        OUTPUT: boolean

        EXAMPLES::

            sage: P = Polyhedron(vertices=[[1,0,0],[0,1,0],[0,0,1]]);  P
            A 2-dimensional polyhedron in ZZ^3 defined as the convex hull of 3 vertices
            sage: P.is_empty(), P.is_universe()
            (False, False)

            sage: Q = Polyhedron(vertices=());  Q
            The empty polyhedron in ZZ^0
            sage: Q.is_empty(), Q.is_universe()
            (True, False)

            sage: R = Polyhedron(lines=[(1,0),(0,1)]);  R
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex and 2 lines
            sage: R.is_empty(), R.is_universe()
            (False, True)
        """
    def dim(self):
        """
        Return the dimension of the polyhedron.

        OUTPUT: -1 if the polyhedron is empty, otherwise a nonnegative integer

        EXAMPLES::

            sage: simplex = Polyhedron(vertices = [[1,0,0,0],[0,0,0,1],[0,1,0,0],[0,0,1,0]])
            sage: simplex.dim()
            3
            sage: simplex.ambient_dim()
            4

        The empty set is a special case (:issue:`12193`)::

            sage: P1=Polyhedron(vertices=[[1,0,0],[0,1,0],[0,0,1]])
            sage: P2=Polyhedron(vertices=[[2,0,0],[0,2,0],[0,0,2]])
            sage: P12 = P1.intersection(P2)
            sage: P12
            The empty polyhedron in ZZ^3
            sage: P12.dim()
            -1
        """
    dimension = dim
    def Vrepresentation_space(self):
        """
        Return the ambient free module.

        OUTPUT: a free module over the base ring of dimension :meth:`ambient_dim`

        EXAMPLES::

            sage: poly_test = Polyhedron(vertices = [[1,0,0,0],[0,1,0,0]])
            sage: poly_test.Vrepresentation_space()
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
            sage: poly_test.ambient_space() is poly_test.Vrepresentation_space()
            True
        """
    def Hrepresentation_space(self):
        """
        Return the linear space containing the H-representation vectors.

        OUTPUT: a free module over the base ring of dimension :meth:`ambient_dim` + 1

        EXAMPLES::

            sage: poly_test = Polyhedron(vertices = [[1,0,0,0],[0,1,0,0]])
            sage: poly_test.Hrepresentation_space()
            Ambient free module of rank 5 over the principal ideal domain Integer Ring
        """
    ambient_space = Vrepresentation_space
    def ambient_vector_space(self, base_field=None):
        """
        Return the ambient vector space.

        It is the ambient free module (:meth:`Vrepresentation_space`) tensored
        with a field.

        INPUT:

        - ``base_field`` -- a field (default: the fraction field of the base ring)

        EXAMPLES::

            sage: poly_test = Polyhedron(vertices = [[1,0,0,0],[0,1,0,0]])
            sage: poly_test.ambient_vector_space()
            Vector space of dimension 4 over Rational Field
            sage: poly_test.ambient_vector_space() is poly_test.ambient()
            True

            sage: poly_test.ambient_vector_space(AA)                                    # needs sage.rings.number_field
            Vector space of dimension 4 over Algebraic Real Field
            sage: poly_test.ambient_vector_space(RDF)
            Vector space of dimension 4 over Real Double Field
            sage: poly_test.ambient_vector_space(SR)                                    # needs sage.symbolic
            Vector space of dimension 4 over Symbolic Ring
        """
    ambient = ambient_vector_space
    def ambient_dim(self):
        """
        Return the dimension of the ambient space.

        EXAMPLES::

            sage: poly_test = Polyhedron(vertices = [[1,0,0,0],[0,1,0,0]])
            sage: poly_test.ambient_dim()
            4
        """
    def an_affine_basis(self):
        """
        Return points in ``self`` that form a basis for the affine span of ``self``.

        This implementation of the method :meth:`~sage.geometry.convex_set.ConvexSet_base.an_affine_basis`
        for polytopes guarantees the following:

        - All points are vertices.

        - The basis is obtained by considering a maximal chain of faces
          in the face lattice and picking for each cover relation
          one vertex that is in the difference. Thus this method
          is independent of the concrete realization of the polytope.

        For unbounded polyhedra, the result may contain arbitrary points of ``self``,
        not just vertices.

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: P.an_affine_basis()
            [A vertex at (-1, -1, -1),
             A vertex at (1, -1, -1),
             A vertex at (1, -1, 1),
             A vertex at (1, 1, -1)]

            sage: P = polytopes.permutahedron(5)
            sage: P.an_affine_basis()
            [A vertex at (1, 2, 3, 5, 4),
             A vertex at (2, 1, 3, 5, 4),
             A vertex at (1, 3, 2, 5, 4),
             A vertex at (4, 1, 3, 5, 2),
             A vertex at (4, 2, 5, 3, 1)]

        Unbounded polyhedra::

            sage: p = Polyhedron(vertices=[(0, 0)], rays=[(1,0), (0,1)])
            sage: p.an_affine_basis()
            [A vertex at (0, 0), (1, 0), (0, 1)]
            sage: p = Polyhedron(vertices=[(2, 1)], rays=[(1,0), (0,1)])
            sage: p.an_affine_basis()
            [A vertex at (2, 1), (3, 1), (2, 2)]
            sage: p = Polyhedron(vertices=[(2, 1)], rays=[(1,0)], lines=[(0,1)])
            sage: p.an_affine_basis()
            [(2, 1), A vertex at (2, 0), (3, 0)]
        """
    @abstract_method
    def a_maximal_chain(self) -> None:
        """
        Return a maximal chain of the face lattice in increasing order.

        Subclasses must provide an implementation of this method.

        EXAMPLES::

            sage: from sage.geometry.polyhedron.base1 import Polyhedron_base1
            sage: P = polytopes.cube()
            sage: Polyhedron_base1.a_maximal_chain
            <abstract method a_maximal_chain at ...>
        """
    @cached_method
    def representative_point(self):
        '''
        Return a "generic" point.

        .. SEEALSO::

            :meth:`sage.geometry.polyhedron.base.Polyhedron_base.center`.

        OUTPUT:

        A point as a coordinate vector. The point is chosen to be
        interior if possible. If the polyhedron is not
        full-dimensional, the point is in the relative interior. If
        the polyhedron is zero-dimensional, its single point is
        returned.

        EXAMPLES::

            sage: p = Polyhedron(vertices=[(3,2)], rays=[(1,-1)])
            sage: p.representative_point()
            (4, 1)
            sage: p.center()
            (3, 2)

            sage: Polyhedron(vertices=[(3,2)]).representative_point()
            (3, 2)
        '''
    def contains(self, point):
        """
        Test whether the polyhedron contains the given ``point``.

        .. SEEALSO::

            :meth:`interior_contains`, :meth:`relative_interior_contains`.

        INPUT:

        - ``point`` -- coordinates of a point (an iterable)

        OUTPUT: boolean

        EXAMPLES::

            sage: P = Polyhedron(vertices=[[1,1],[1,-1],[0,0]])
            sage: P.contains( [1,0] )
            True
            sage: P.contains( P.center() )  # true for any convex set
            True

        As a shorthand, one may use the usual ``in`` operator::

            sage: P.center() in P
            True
            sage: [-1,-1] in P
            False

        The point need not have coordinates in the same field as the
        polyhedron::

            sage: # needs sage.symbolic
            sage: ray = Polyhedron(vertices=[(0,0)], rays=[(1,0)], base_ring=QQ)
            sage: ray.contains([sqrt(2)/3,0])        # irrational coordinates are ok
            True
            sage: a = var('a')
            sage: ray.contains([a,0])                # a might be negative!
            False
            sage: assume(a>0)
            sage: ray.contains([a,0])
            True
            sage: ray.contains(['hello', 'kitty'])   # no common ring for coordinates
            False

        The empty polyhedron needs extra care, see :issue:`10238`::

            sage: empty = Polyhedron(); empty
            The empty polyhedron in ZZ^0
            sage: empty.contains([])
            False
            sage: empty.contains([0])               # not a point in QQ^0
            False
            sage: full = Polyhedron(vertices=[()]); full
            A 0-dimensional polyhedron in ZZ^0 defined as the convex hull of 1 vertex
            sage: full.contains([])
            True
            sage: full.contains([0])
            False

        TESTS:

        Passing non-iterable objects does not cause an exception, see :issue:`32013`::

            sage: None in Polyhedron(vertices=[(0,0)], rays=[(1,0)], base_ring=QQ)
            False
        """
    __contains__ = contains
    @cached_method
    def interior(self):
        """
        The interior of ``self``.

        OUTPUT:

        - either an empty polyhedron or an instance of
          :class:`~sage.geometry.relative_interior.RelativeInterior`

        EXAMPLES:

        If the polyhedron is full-dimensional, the result is the
        same as that of :meth:`relative_interior`::

            sage: P_full = Polyhedron(vertices=[[0,0],[1,1],[1,-1]])
            sage: P_full.interior()
            Relative interior of
             a 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices

        If the polyhedron is of strictly smaller dimension than the
        ambient space, its interior is empty::

            sage: P_lower = Polyhedron(vertices=[[0,1], [0,-1]])
            sage: P_lower.interior()
            The empty polyhedron in ZZ^2

        TESTS::

            sage: Empty = Polyhedron(ambient_dim=2); Empty
            The empty polyhedron in ZZ^2
            sage: Empty.interior() is Empty
            True
        """
    def interior_contains(self, point):
        """
        Test whether the interior of the polyhedron contains the
        given ``point``.

        .. SEEALSO::

            :meth:`contains`, :meth:`relative_interior_contains`.

        INPUT:

        - ``point`` -- coordinates of a point

        OUTPUT: boolean

        EXAMPLES::

            sage: P = Polyhedron(vertices=[[0,0],[1,1],[1,-1]])
            sage: P.contains( [1,0] )
            True
            sage: P.interior_contains( [1,0] )
            False

        If the polyhedron is of strictly smaller dimension than the
        ambient space, its interior is empty::

            sage: P = Polyhedron(vertices=[[0,1],[0,-1]])
            sage: P.contains( [0,0] )
            True
            sage: P.interior_contains( [0,0] )
            False

        The empty polyhedron needs extra care, see :issue:`10238`::

            sage: empty = Polyhedron(); empty
            The empty polyhedron in ZZ^0
            sage: empty.interior_contains([])
            False
        """
    def is_relatively_open(self):
        """
        Return whether ``self`` is relatively open.

        OUTPUT: boolean

        EXAMPLES::

            sage: P = Polyhedron(vertices=[(1,0), (-1,0)]); P
            A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: P.is_relatively_open()
            False

            sage: P0 = Polyhedron(vertices=[[1, 2]]); P0
            A 0-dimensional polyhedron in ZZ^2 defined as the convex hull of 1 vertex
            sage: P0.is_relatively_open()
            True

            sage: Empty = Polyhedron(ambient_dim=2); Empty
            The empty polyhedron in ZZ^2
            sage: Empty.is_relatively_open()
            True

            sage: Line = Polyhedron(vertices=[(1, 1)], lines=[(1, 0)]); Line
            A 1-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex and 1 line
            sage: Line.is_relatively_open()
            True
        """
    @cached_method
    def relative_interior(self):
        """
        Return the relative interior of ``self``.

        EXAMPLES::

            sage: P = Polyhedron(vertices=[(1,0), (-1,0)])
            sage: ri_P = P.relative_interior(); ri_P
            Relative interior of
             a 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: (0, 0) in ri_P
            True
            sage: (1, 0) in ri_P
            False

            sage: P0 = Polyhedron(vertices=[[1, 2]])
            sage: P0.relative_interior() is P0
            True

            sage: Empty = Polyhedron(ambient_dim=2)
            sage: Empty.relative_interior() is Empty
            True

            sage: Line = Polyhedron(vertices=[(1, 1)], lines=[(1, 0)])
            sage: Line.relative_interior() is Line
            True
        """
    def relative_interior_contains(self, point):
        """
        Test whether the relative interior of the polyhedron
        contains the given ``point``.

        .. SEEALSO::

            :meth:`contains`, :meth:`interior_contains`.

        INPUT:

        - ``point`` -- coordinates of a point

        OUTPUT: boolean

        EXAMPLES::

            sage: P = Polyhedron(vertices=[(1,0), (-1,0)])
            sage: P.contains( (0,0) )
            True
            sage: P.interior_contains( (0,0) )
            False
            sage: P.relative_interior_contains( (0,0) )
            True
            sage: P.relative_interior_contains( (1,0) )
            False

        The empty polyhedron needs extra care, see :issue:`10238`::

            sage: empty = Polyhedron(); empty
            The empty polyhedron in ZZ^0
            sage: empty.relative_interior_contains([])
            False
        """
