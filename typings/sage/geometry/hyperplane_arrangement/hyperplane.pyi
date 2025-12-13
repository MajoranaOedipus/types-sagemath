from sage.geometry.linear_expression import LinearExpression as LinearExpression, LinearExpressionModule as LinearExpressionModule
from sage.misc.cachefunc import cached_method as cached_method

class Hyperplane(LinearExpression):
    """
    A hyperplane.

    You should always use :class:`AmbientVectorSpace` to construct
    instances of this class.

    INPUT:

    - ``parent`` -- the parent :class:`AmbientVectorSpace`

    - ``coefficients`` -- a vector of coefficients of the linear variables

    - ``constant`` -- the constant term for the linear expression

    EXAMPLES::

        sage: H.<x,y> = HyperplaneArrangements(QQ)
        sage: x+y-1
        Hyperplane x + y - 1

        sage: ambient = H.ambient_space()
        sage: ambient._element_constructor_(x+y-1)
        Hyperplane x + y - 1

    For technical reasons, we must allow the degenerate cases of
    an empty space and of a full space::

        sage: 0*x
        Hyperplane 0*x + 0*y + 0
        sage: 0*x + 1
        Hyperplane 0*x + 0*y + 1
        sage: x + 0 == x + ambient(0)    # because coercion requires them
        True
    """
    def __init__(self, parent, coefficients, constant) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: x.change_ring(RR)
            Hyperplane 1.00000000000000*x + 0.000000000000000*y + 0.000000000000000
            sage: TestSuite(x+y-1).run()
        """
    def normal(self):
        """
        Return the normal vector.

        OUTPUT: a vector over the base ring

        EXAMPLES::

            sage: H.<x, y, z> = HyperplaneArrangements(QQ)
            sage: x.normal()
            (1, 0, 0)
            sage: x.A(), x.b()
            ((1, 0, 0), 0)
            sage: (x + 2*y + 3*z + 4).normal()
            (1, 2, 3)
        """
    def __contains__(self, q) -> bool:
        """
        Test whether the point ``q`` is in the hyperplane.

        INPUT:

        - ``q`` -- point (as a vector, list, or tuple)

        OUTPUT: boolean

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: h = x + y + z - 1
            sage: (1/3, 1/3, 1/3) in h
            True
            sage: (0,0,0) in h
            False
        """
    @cached_method
    def polyhedron(self, **kwds):
        """
        Return the hyperplane as a polyhedron.

        OUTPUT: a :func:`~sage.geometry.polyhedron.constructor.Polyhedron` instance

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: h = x + 2*y + 3*z - 4
            sage: P = h.polyhedron();  P
            A 2-dimensional polyhedron in QQ^3 defined as the convex hull of 1 vertex and 2 lines
            sage: P.Hrepresentation()
            (An equation (1, 2, 3) x - 4 == 0,)
            sage: P.Vrepresentation()
            (A line in the direction (0, 3, -2),
             A line in the direction (3, 0, -1),
             A vertex at (0, 0, 4/3))
        """
    @cached_method
    def linear_part(self):
        """
        The linear part of the affine space.

        OUTPUT:

        Vector subspace of the ambient vector space, parallel to the
        hyperplane.

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: h = x + 2*y + 3*z - 1
            sage: h.linear_part()
            Vector space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [   1    0 -1/3]
            [   0    1 -2/3]
        """
    def linear_part_projection(self, point):
        """
        Orthogonal projection onto the linear part.

        INPUT:

        - ``point`` -- vector of the ambient space, or anything that
          can be converted into one; not necessarily on the
          hyperplane

        OUTPUT:

        Coordinate vector of the projection of ``point`` with respect
        to the basis of :meth:`linear_part`. In particular, the length
        of this vector is one less than the ambient space
        dimension.

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: h = x + 2*y + 3*z - 4
            sage: h.linear_part()
            Vector space of degree 3 and dimension 2 over Rational Field
            Basis matrix:
            [   1    0 -1/3]
            [   0    1 -2/3]
            sage: p1 = h.linear_part_projection(0);  p1
            (0, 0)
            sage: p2 = h.linear_part_projection([3,4,5]);  p2
            (8/7, 2/7)
            sage: h.linear_part().basis()
            [(1, 0, -1/3), (0, 1, -2/3)]
            sage: p3 = h.linear_part_projection([1,1,1]);  p3
            (4/7, 1/7)
        """
    @cached_method
    def point(self):
        """
        Return the point closest to the origin.

        OUTPUT:

        A vector of the ambient vector space. The closest point to the
        origin in the `L^2`-norm.

        In finite characteristic a random point will be returned if
        the norm of the hyperplane normal vector is zero.

        EXAMPLES::


            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: h = x + 2*y + 3*z - 4
            sage: h.point()
            (2/7, 4/7, 6/7)
            sage: h.point() in h
            True

            sage: # needs sage.rings.finite_rings
            sage: H.<x,y,z> = HyperplaneArrangements(GF(3))
            sage: h = 2*x + y + z + 1
            sage: h.point()
            (1, 0, 0)
            sage: h.point().base_ring()
            Finite Field of size 3

            sage: H.<x,y,z> = HyperplaneArrangements(GF(3))
            sage: h = x + y + z + 1
            sage: h.point()
            (2, 0, 0)
        """
    def dimension(self):
        """
        The dimension of the hyperplane.

        OUTPUT: integer

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: h = x + y + z - 1
            sage: h.dimension()
            2
        """
    def intersection(self, other):
        """
        The intersection of ``self`` with ``other``.

        INPUT:

        - ``other`` -- a hyperplane, a polyhedron, or something that
          defines a polyhedron

        OUTPUT: a polyhedron

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: h = x + y + z - 1
            sage: h.intersection(x - y)
            A 1-dimensional polyhedron in QQ^3 defined as the convex hull of 1 vertex and 1 line
            sage: h.intersection(polytopes.cube())
            A 2-dimensional polyhedron in QQ^3 defined as the convex hull of 3 vertices
        """
    def orthogonal_projection(self, point):
        """
        Return the orthogonal projection of a point.

        INPUT:

        - ``point`` -- vector of the ambient space, or anything that
          can be converted into one; not necessarily on the
          hyperplane

        OUTPUT:

        A vector in the ambient vector space that lies on the
        hyperplane.

        In finite characteristic, a :exc:`ValueError` is raised if the
        the norm of the hyperplane normal is zero.

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: h = x + 2*y + 3*z - 4
            sage: p1 = h.orthogonal_projection(0);  p1
            (2/7, 4/7, 6/7)
            sage: p1 in h
            True
            sage: p2 = h.orthogonal_projection([3,4,5]);  p2
            (10/7, 6/7, 2/7)
            sage: p1 in h
            True
            sage: p3 = h.orthogonal_projection([1,1,1]);  p3
            (6/7, 5/7, 4/7)
            sage: p3 in h
            True
        """
    def primitive(self, signed: bool = True):
        """
        Return hyperplane defined by primitive equation.

        INPUT:

        - ``signed`` -- boolean (default: ``True``); whether
          to preserve the overall sign

        OUTPUT:

        Hyperplane whose linear expression has common factors and
        denominators cleared. That is, the same hyperplane (with the
        same sign) but defined by a rescaled equation. Note that
        different linear expressions must define different hyperplanes
        as comparison is used in caching.

        If ``signed``, the overall rescaling is by a positive constant
        only.

        EXAMPLES::

            sage: H.<x,y> = HyperplaneArrangements(QQ)
            sage: h = -1/3*x + 1/2*y - 1;  h
            Hyperplane -1/3*x + 1/2*y - 1
            sage: h.primitive()
            Hyperplane -2*x + 3*y - 6
            sage: h == h.primitive()
            False
            sage: (4*x + 8).primitive()
            Hyperplane x + 0*y + 2

            sage: (4*x - y - 8).primitive(signed=True)   # default
            Hyperplane 4*x - y - 8
            sage: (4*x - y - 8).primitive(signed=False)
            Hyperplane -4*x + y + 8

        TESTS:

        Check that :issue:`30078` is fixed::

            sage: # needs sage.rings.number_field
            sage: R.<sqrt2> = QuadraticField(2)
            sage: H.<x,y> = HyperplaneArrangements(base_ring=R)
            sage: B = H([1,1,0], [2,2,0], [sqrt2,sqrt2,0])
            sage: B
            Arrangement <x + 1>

        Check that :issue:`30749` is fixed::

            sage: # needs sage.rings.number_field
            sage: tau = (1+AA(5).sqrt()) / 2
            sage: ncn = [[2*tau+1,2*tau,tau],[2*tau+2,2*tau+1,tau+1]]
            sage: ncn += [[tau+1,tau+1,tau],[2*tau,2*tau,tau],[tau+1,tau+1,1]]
            sage: ncn += [[1,1,1],[1,1,0],[0,1,0],[1,0,0],[tau+1,tau,tau]]
            sage: H = HyperplaneArrangements(AA,names='xyz')
            sage: A = H([[0]+v for v in ncn])
            sage: A.n_regions()
            60
        """
    def plot(self, **kwds):
        """
        Plot the hyperplane.

        OUTPUT: a graphics object

        EXAMPLES::

            sage: L.<x, y> = HyperplaneArrangements(QQ)
            sage: (x + y - 2).plot()                                                    # needs sage.plot
            Graphics object consisting of 2 graphics primitives
        """
    def __or__(self, other):
        """
        Construct hyperplane arrangement from bitwise or.

        EXAMPLES::

            sage: L.<x, y> = HyperplaneArrangements(QQ)
            sage: x | y + 1
            Arrangement <y + 1 | x>
            sage: x | [(0,1), 1]
            Arrangement <y + 1 | x>

        TESTS::

            sage: (x | y).parent() is L
            True
        """
    def to_symmetric_space(self):
        """
        Return ``self`` considered as an element in the corresponding
        symmetric space.

        EXAMPLES::

            sage: L.<x, y> = HyperplaneArrangements(QQ)
            sage: h = -1/3*x + 1/2*y
            sage: h.to_symmetric_space()
            -1/3*x + 1/2*y

            sage: hp = -1/3*x + 1/2*y - 1
            sage: hp.to_symmetric_space()
            Traceback (most recent call last):
            ...
            ValueError: the hyperplane must pass through the origin
        """

class AmbientVectorSpace(LinearExpressionModule):
    """
    The ambient space for hyperplanes.

    This class is the parent for the :class:`Hyperplane` instances.

    TESTS::

        sage: from sage.geometry.hyperplane_arrangement.hyperplane import AmbientVectorSpace
        sage: V = AmbientVectorSpace(QQ, ('x', 'y'))
        sage: V.change_ring(QQ) is V
        True
    """
    Element = Hyperplane
    def dimension(self):
        """
        Return the ambient space dimension.

        OUTPUT: integer

        EXAMPLES::

            sage: M.<x,y> = HyperplaneArrangements(QQ)
            sage: x.parent().dimension()
            2
            sage: x.parent() is M.ambient_space()
            True
            sage: x.dimension()
            1
        """
    def change_ring(self, base_ring):
        """
        Return a ambient vector space with a changed base ring.

        INPUT:

        - ``base_ring`` -- a ring; the new base ring

        OUTPUT: a new :class:`AmbientVectorSpace`

        EXAMPLES::

            sage: M.<y> = HyperplaneArrangements(QQ)
            sage: V = M.ambient_space()
            sage: V.change_ring(RR)
            1-dimensional linear space over Real Field with 53 bits of precision with coordinate y

        TESTS::

            sage: V.change_ring(QQ) is V
            True
        """
    def symmetric_space(self):
        """
        Construct the symmetric space of ``self``.

        Consider a hyperplane arrangement `A` in the vector space
        `V = k^n`, for some field `k`. The symmetric space is the
        symmetric algebra `S(V^*)` as the polynomial ring
        `k[x_1, x_2, \\ldots, x_n]` where `(x_1, x_2, \\ldots, x_n)` is
        a basis for `V`.

        EXAMPLES::

            sage: H.<x,y,z> = HyperplaneArrangements(QQ)
            sage: A = H.ambient_space()
            sage: A.symmetric_space()
            Multivariate Polynomial Ring in x, y, z over Rational Field
        """
