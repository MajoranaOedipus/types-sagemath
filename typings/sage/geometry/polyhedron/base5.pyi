from .base4 import Polyhedron_base4 as Polyhedron_base4
from sage.matrix.constructor import matrix as matrix
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import Matrix as Matrix, Vector as Vector, coerce_binop as coerce_binop

class Polyhedron_base5(Polyhedron_base4):
    """
    Methods constructing new polyhedra
    except for affine hull and affine hull projection.

    See :class:`sage.geometry.polyhedron.base.Polyhedron_base`.

    TESTS::

        sage: from sage.geometry.polyhedron.base5 import Polyhedron_base5
        sage: P = polytopes.cube()
        sage: Q = polytopes.cross_polytope(3)

    Unary operations::

        sage: Polyhedron_base5.__neg__(P)
        A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices
        sage: Polyhedron_base5.polar(P)
        A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 6 vertices
        sage: Polyhedron_base5.pyramid(P)
        A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 9 vertices
        sage: Polyhedron_base5.bipyramid(P)
        A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 10 vertices
        sage: Polyhedron_base5.prism(P)
        A 4-dimensional polyhedron in ZZ^4 defined as the convex hull of 16 vertices
        sage: Polyhedron_base5.truncation(P)
        A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 24 vertices
        sage: Polyhedron_base5.lawrence_polytope(P)
        A 11-dimensional polyhedron in ZZ^11 defined as the convex hull of 16 vertices

    Binary operations::

        sage: Polyhedron_base5.minkowski_sum(P, Q)
        A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 24 vertices
        sage: Polyhedron_base5.minkowski_difference(P, Q)
        A 0-dimensional polyhedron in QQ^3 defined as the convex hull of 1 vertex
        sage: Polyhedron_base5.product(P, Q)
        A 6-dimensional polyhedron in ZZ^6 defined as the convex hull of 48 vertices
        sage: Polyhedron_base5.join(P, Q)
        A 7-dimensional polyhedron in ZZ^7 defined as the convex hull of 14 vertices
        sage: Polyhedron_base5.subdirect_sum(P, Q)
        A 6-dimensional polyhedron in ZZ^6 defined as the convex hull of 14 vertices
        sage: Polyhedron_base5.direct_sum(P, Q)
        A 6-dimensional polyhedron in QQ^6 defined as the convex hull of 14 vertices
        sage: Polyhedron_base5.convex_hull(P, Q)
        A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices
        sage: Polyhedron_base5.intersection(P, Q)
        A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 6 vertices

    Actions::

        sage: Polyhedron_base5.translation(P, vector([1, 1, 1]))
        A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices
        sage: Polyhedron_base5.dilation(P, 2)
        A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices
        sage: Polyhedron_base5.__truediv__(P, 2)
        A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 8 vertices
        sage: Polyhedron_base5.linear_transformation(P, matrix([[2, 1, 2], [1, 2, 4], [3, 1, 2]]))
        A 2-dimensional polyhedron in ZZ^3 defined as the convex hull of 4 vertices

    Methods using a face::

        sage: Polyhedron_base5.face_truncation(P, P.facets()[0])
        A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 8 vertices
        sage: Polyhedron_base5.stack(P, P.facets()[0])
        A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 9 vertices
        sage: Polyhedron_base5.wedge(P, P.facets()[0])
        A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 12 vertices
        sage: Polyhedron_base5.face_split(P, P.faces(2)[0])
        A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 10 vertices

    Methods using a vertex or vector::

        sage: Polyhedron_base5.lawrence_extension(P, P.vertices()[0])
        A 4-dimensional polyhedron in ZZ^4 defined as the convex hull of 9 vertices
        sage: Polyhedron_base5.one_point_suspension(P, P.vertices()[0])
        A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 9 vertices
    """
    def __neg__(self):
        """
        Negation of a polytope is defined as inverting the coordinates.

        EXAMPLES::

            sage: t = polytopes.simplex(3,project=False);  t.vertices()
            (A vertex at (0, 0, 0, 1), A vertex at (0, 0, 1, 0),
             A vertex at (0, 1, 0, 0), A vertex at (1, 0, 0, 0))
            sage: neg_ = -t
            sage: neg_.vertices()
            (A vertex at (-1, 0, 0, 0), A vertex at (0, -1, 0, 0),
             A vertex at (0, 0, -1, 0), A vertex at (0, 0, 0, -1))

        TESTS::

            sage: p = Polyhedron(ieqs=[[1,1,0]])
            sage: p.rays()
            (A ray in the direction (1, 0),)
            sage: pneg = p.__neg__()
            sage: pneg.rays()
            (A ray in the direction (-1, 0),)
        """
    def polar(self, in_affine_span: bool = False):
        """
        Return the polar (dual) polytope.

        The original vertices are translated so that their barycenter
        is at the origin, and then the vertices are used as the
        coefficients in the polar inequalities.

        The polytope must be full-dimensional, unless ``in_affine_span`` is ``True``.
        If ``in_affine_span`` is ``True``, then the operation will be performed in the
        linear/affine span of the polyhedron (after translation).

        EXAMPLES::

            sage: p = Polyhedron(vertices=[[0,0,1], [0,1,0], [1,0,0], [0,0,0], [1,1,1]],
            ....:                base_ring=QQ); p
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 5 vertices
            sage: p.polar()
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 6 vertices

            sage: cube = polytopes.hypercube(3)
            sage: octahedron = polytopes.cross_polytope(3)
            sage: cube_dual = cube.polar()
            sage: octahedron == cube_dual
            True

        ``in_affine_span`` somewhat ignores equations, performing the polar in the
        spanned subspace (after translating barycenter to origin)::

            sage: P = polytopes.simplex(3, base_ring=QQ)
            sage: P.polar(in_affine_span=True)
            A 3-dimensional polyhedron in QQ^4 defined as the convex hull of 4 vertices

        Embedding the polytope in a higher dimension, commutes with polar in this case::

            sage: point = Polyhedron([[0]])
            sage: P = polytopes.cube().change_ring(QQ)
            sage: (P*point).polar(in_affine_span=True) == P.polar()*point
            True

        TESTS:

        Check that :issue:`25081` is fixed::

            sage: C = polytopes.hypercube(4,backend='cdd')
            sage: C.polar().backend()
            'cdd'

        Check that :issue:`28850` is fixed::

            sage: P = polytopes.simplex(3, base_ring=QQ)
            sage: P.polar()
            Traceback (most recent call last):
            ...
            ValueError: not full-dimensional; try with 'in_affine_span=True'

        Check that the double description is set up correctly::

            sage: P = Polyhedron([[1,0],[0,1],[-1,-1]], backend='field')
            sage: Q = P.change_ring(QQ, backend='ppl')
            sage: P.polar() == Q.polar()
            True

            sage: P = polytopes.simplex(4, backend='field')
            sage: Q = P.change_ring(QQ, backend='ppl')
            sage: P.polar(in_affine_span=True) == Q.polar(in_affine_span=True)
            True

        Check that it works, even when the equations are not orthogonal to each other::

            sage: P = polytopes.cube()*Polyhedron([[0,0,0]])
            sage: P = P.change_ring(QQ)

            sage: from sage.geometry.polyhedron.backend_field import Polyhedron_field
            sage: from sage.geometry.polyhedron.parent import Polyhedra_field
            sage: parent = Polyhedra_field(QQ, 6, 'field')
            sage: equations = [[0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, -1, 1, -1], [0, 0, 0, 0, 1, -1, -1]]
            sage: Q = Polyhedron_field(parent, [P.vertices(), [], []], [P.inequalities(), equations],
            ....:                      Vrep_minimal=True, Hrep_minimal=True)
            sage: Q == P
            True
            sage: Q.polar(in_affine_span=True) == P.polar(in_affine_span=True)
            True
        """
    def pyramid(self):
        """
        Return a polyhedron that is a pyramid over the original.

        EXAMPLES::

            sage: square = polytopes.hypercube(2);  square
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 4 vertices
            sage: egyptian_pyramid = square.pyramid();  egyptian_pyramid
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 5 vertices
            sage: egyptian_pyramid.n_vertices()
            5
            sage: for v in egyptian_pyramid.vertex_generator(): print(v)
            A vertex at (0, -1, -1)
            A vertex at (0, -1, 1)
            A vertex at (0, 1, -1)
            A vertex at (0, 1, 1)
            A vertex at (1, 0, 0)

        TESTS::

            sage: polytopes.simplex(backend='cdd').pyramid().backend()
            'cdd'
        """
    def bipyramid(self):
        """
        Return a polyhedron that is a bipyramid over the original.

        EXAMPLES::

            sage: octahedron = polytopes.cross_polytope(3)
            sage: cross_poly_4d = octahedron.bipyramid()
            sage: cross_poly_4d.n_vertices()
            8
            sage: q = [list(v) for v in cross_poly_4d.vertex_generator()]; q
            [[-1, 0, 0, 0],
             [0, -1, 0, 0],
             [0, 0, -1, 0],
             [0, 0, 0, -1],
             [0, 0, 0, 1],
             [0, 0, 1, 0],
             [0, 1, 0, 0],
             [1, 0, 0, 0]]

        Now check that bipyramids of cross-polytopes are cross-polytopes::

            sage: q2 = [list(v) for v in polytopes.cross_polytope(4).vertex_generator()]
            sage: [v in q2 for v in q]
            [True, True, True, True, True, True, True, True]

        TESTS::

            sage: polytopes.simplex(backend='cdd').bipyramid().backend()
            'cdd'
        """
    def prism(self):
        """
        Return a prism of the original polyhedron.

        EXAMPLES::

            sage: square = polytopes.hypercube(2)
            sage: cube = square.prism()
            sage: cube
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices
            sage: hypercube = cube.prism()
            sage: hypercube.n_vertices()
            16

        TESTS::

            sage: polytopes.simplex(backend='cdd').prism().backend()
            'cdd'
        """
    def truncation(self, cut_frac=None):
        """
        Return a new polyhedron formed from two points on each edge
        between two vertices.

        INPUT:

        - ``cut_frac`` -- integer; how deeply to cut into the edge
          Default is `\\frac{1}{3}`

        OUTPUT: a Polyhedron object, truncated as described above

        EXAMPLES::

            sage: cube = polytopes.hypercube(3)
            sage: trunc_cube = cube.truncation()
            sage: trunc_cube.n_vertices()
            24
            sage: trunc_cube.n_inequalities()
            14

        TESTS::

            sage: polytopes.simplex(backend='field').truncation().backend()
            'field'
        """
    def lawrence_polytope(self):
        """
        Return the Lawrence polytope of ``self``.

        Let `P` be a `d`-polytope in `\\RR^r` with `n` vertices. The Lawrence
        polytope of `P` is the polytope whose vertices are the columns of the
        following `(r+n)`-by-`2n` matrix.

        .. MATH::

            \\begin{pmatrix}
             V      &   V    \\\\\n             I_n    &   2I_n
            \\end{pmatrix},

        where `V` is the `r`-by-`n` vertices matrix of `P`.

        EXAMPLES::

            sage: P = polytopes.octahedron()
            sage: L = P.lawrence_polytope(); L
            A 9-dimensional polyhedron in ZZ^9 defined as the convex hull of 12 vertices
            sage: V = P.vertices_list()
            sage: for i, v in enumerate(V):
            ....:     v = v + i*[0]
            ....:     P = P.lawrence_extension(v)
            sage: P == L
            True

        REFERENCES:

            For more information, see Section 6.6 of [Zie2007]_.
        """
    def deformation_cone(self):
        """
        Return the deformation cone of ``self``.

        Let `P` be a `d`-polytope in `\\RR^r` with `n` facets. The deformation
        cone is a polyhedron in `\\RR^n` whose points are the right-hand side `b`
        in `Ax\\leq b` where `A` is the matrix of facet normals of ``self``, so
        that the resulting polytope has a normal fan which is a coarsening of
        the normal fan of ``self``.

        EXAMPLES:

        Let's examine the deformation cone of the square with one truncated
        vertex::

            sage: tc = Polyhedron([(1, -1), (1/3, 1), (1, 1/3), (-1, 1), (-1, -1)])
            sage: dc = tc.deformation_cone()
            sage: dc.an_element()
            (2, 1, 1, 0, 0)
            sage: [_.A() for _ in tc.Hrepresentation()]
            [(1, 0), (0, 1), (0, -1), (-3, -3), (-1, 0)]
            sage: P = Polyhedron(rays=[(1, 0, 2), (0, 1, 1), (0, -1, 1), (-3, -3, 0), (-1, 0, 0)])
            sage: P.rays()
            (A ray in the direction (-1, -1, 0),
             A ray in the direction (-1, 0, 0),
             A ray in the direction (0, -1, 1),
             A ray in the direction (0, 1, 1),
             A ray in the direction (1, 0, 2))

        Now, let's compute the deformation cone of the pyramid over a square
        and verify that it is not full dimensional::

            sage: py = Polyhedron([(0, -1, -1), (0, -1, 1), (0, 1, -1), (0, 1, 1), (1, 0, 0)])
            sage: dc_py = py.deformation_cone(); dc_py
            A 4-dimensional polyhedron in QQ^5 defined as the convex hull of 1 vertex, 1 ray, 3 lines
            sage: [ineq.b() for ineq in py.Hrepresentation()]
            [0, 1, 1, 1, 1]
            sage: r = dc_py.rays()[0]
            sage: l1,l2,l3 = dc_py.lines()
            sage: r.vector()-l1.vector()/2-l2.vector()-l3.vector()/2
            (0, 1, 1, 1, 1)

        .. SEEALSO::

            :meth:`~sage.schemes.toric.variety.Kaehler_cone`

        REFERENCES:

        For more information, see Section 5.4 of [DLRS2010]_ and Section
        2.2 of [ACEP2020].
        """
    @coerce_binop
    def minkowski_sum(self, other):
        """
        Return the Minkowski sum.

        Minkowski addition of two subsets of a vector space is defined
        as

        .. MATH::

            X \\oplus Y =
            \\bigcup_{y\\in Y} (X+y) =
            \\bigcup_{x\\in X, y\\in Y} (x+y)

        See :meth:`minkowski_difference` for a partial inverse operation.

        INPUT:

        - ``other`` -- a :class:`~sage.geometry.polyhedron.base.Polyhedron_base`

        OUTPUT: the Minkowski sum of ``self`` and ``other``

        EXAMPLES::

            sage: X = polytopes.hypercube(3)
            sage: Y = Polyhedron(vertices=[(0,0,0), (0,0,1/2), (0,1/2,0), (1/2,0,0)])
            sage: X+Y
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 13 vertices

            sage: four_cube = polytopes.hypercube(4)
            sage: four_simplex = Polyhedron(vertices=[[0, 0, 0, 1], [0, 0, 1, 0],
            ....:                                     [0, 1, 0, 0], [1, 0, 0, 0]])
            sage: four_cube + four_simplex
            A 4-dimensional polyhedron in ZZ^4 defined as the convex hull of 36 vertices
            sage: four_cube.minkowski_sum(four_simplex) == four_cube + four_simplex
            True

            sage: poly_spam = Polyhedron([[3,4,5,2], [1,0,0,1], [0,0,0,0],
            ....:                         [0,4,3,2], [-3,-3,-3,-3]], base_ring=ZZ)
            sage: poly_eggs = Polyhedron([[5,4,5,4], [-4,5,-4,5],
            ....:                         [4,-5,4,-5], [0,0,0,0]], base_ring=QQ)
            sage: poly_spam + poly_spam + poly_eggs
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 12 vertices
        """
    @coerce_binop
    def minkowski_difference(self, other):
        '''
        Return the Minkowski difference.

        Minkowski subtraction can equivalently be defined via
        Minkowski addition (see :meth:`minkowski_sum`) or as
        set-theoretic intersection via

        .. MATH::

            X \\ominus Y =
            (X^c \\oplus Y)^c =
            \\bigcap_{y\\in Y} (X-y)

        where superscript-"c" means the complement in the ambient
        vector space. The Minkowski difference of convex sets is
        convex, and the difference of polyhedra is again a
        polyhedron. We only consider the case of polyhedra in the
        following. Note that it is not quite the inverse of
        addition. In fact:

        * `(X+Y)-Y = X` for any polyhedra `X`, `Y`.

        * `(X-Y)+Y \\subseteq X`

        * `(X-Y)+Y = X` if and only if Y is a Minkowski summand of X.

        INPUT:

        - ``other`` -- a :class:`~sage.geometry.polyhedron.base.Polyhedron_base`

        OUTPUT:

        The Minkowski difference of ``self`` and ``other``. Also known
        as Minkowski subtraction of ``other`` from ``self``.

        EXAMPLES::

            sage: X = polytopes.hypercube(3)
            sage: Y = Polyhedron(vertices=[(0,0,0), (0,0,1), (0,1,0), (1,0,0)]) / 2
            sage: (X+Y)-Y == X
            True
            sage: (X-Y)+Y < X
            True

        The polyhedra need not be full-dimensional::

            sage: X2 = Polyhedron(vertices=[(-1,-1,0), (1,-1,0), (-1,1,0), (1,1,0)])
            sage: Y2 = Polyhedron(vertices=[(0,0,0), (0,1,0), (1,0,0)]) / 2
            sage: (X2+Y2)-Y2 == X2
            True
            sage: (X2-Y2)+Y2 < X2
            True

        Minus sign is really an alias for :meth:`minkowski_difference`
        ::

            sage: four_cube = polytopes.hypercube(4)
            sage: four_simplex = Polyhedron(vertices=[[0, 0, 0, 1], [0, 0, 1, 0],
            ....:                                     [0, 1, 0, 0], [1, 0, 0, 0]])
            sage: four_cube - four_simplex
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 16 vertices
            sage: four_cube.minkowski_difference(four_simplex) == four_cube - four_simplex
            True

        Coercion of the base ring works::

            sage: poly_spam = Polyhedron([[3,4,5,2], [1,0,0,1], [0,0,0,0],
            ....:                         [0,4,3,2], [-3,-3,-3,-3]], base_ring=ZZ)
            sage: poly_eggs = Polyhedron([[5,4,5,4], [-4,5,-4,5],
            ....:                         [4,-5,4,-5], [0,0,0,0]], base_ring=QQ) / 100
            sage: poly_spam - poly_eggs
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 5 vertices

        TESTS::

            sage: X = polytopes.hypercube(2)
            sage: Y = Polyhedron(vertices=[(1,1)])
            sage: (X-Y).Vrepresentation()
            (A vertex at (0, -2), A vertex at (0, 0), A vertex at (-2, 0), A vertex at (-2, -2))

            sage: Y = Polyhedron(vertices=[(1,1), (0,0)])
            sage: (X-Y).Vrepresentation()
            (A vertex at (0, -1), A vertex at (0, 0), A vertex at (-1, 0), A vertex at (-1, -1))

            sage: X = X + Y   # now Y is a Minkowski summand of X
            sage: (X+Y)-Y == X
            True
            sage: (X-Y)+Y == X
            True

        Testing that :issue:`28506` is fixed::

            sage: Q = Polyhedron([[1,0],[0,1]])
            sage: S = Polyhedron([[0,0],[1,2]])
            sage: S.minkowski_difference(Q)
            A 1-dimensional polyhedron in QQ^2 defined as the convex hull of 2 vertices
        '''
    def __sub__(self, other):
        """
        Implement minus binary operation.

        Polyhedra are not a ring with respect to dilatation and
        Minkowski sum, for example `X\\oplus(-1)*Y \\not= X\\ominus Y`.

        INPUT:

        - ``other`` -- a translation vector or a polyhedron

        OUTPUT:

        Either translation by the negative of the given vector or
        Minkowski subtraction by the given polyhedron.

        EXAMPLES::

            sage: X = polytopes.hypercube(2)
            sage: v = vector([1,1])
            sage: (X - v/2).Vrepresentation()
            (A vertex at (-3/2, -3/2), A vertex at (-3/2, 1/2),
             A vertex at (1/2, -3/2), A vertex at (1/2, 1/2))
            sage: (X-v)+v == X
            True

            sage: Y = Polyhedron(vertices=[(1/2,0), (0,1/2)])
            sage: (X-Y).Vrepresentation()
            (A vertex at (1/2, -1), A vertex at (1/2, 1/2),
             A vertex at (-1, 1/2), A vertex at (-1, -1))
            sage: (X+Y)-Y == X
            True
        """
    def product(self, other):
        """
        Return the Cartesian product.

        INPUT:

        - ``other`` -- a :class:`~sage.geometry.polyhedron.base.Polyhedron_base`

        OUTPUT:

        The Cartesian product of ``self`` and ``other`` with a
        suitable base ring to encompass the two.

        EXAMPLES::

            sage: P1 = Polyhedron([[0], [1]], base_ring=ZZ)
            sage: P2 = Polyhedron([[0], [1]], base_ring=QQ)
            sage: P1.product(P2)
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices

        The Cartesian product is the product in the semiring of polyhedra::

            sage: P1 * P1
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 4 vertices
            sage: P1 * P2
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices
            sage: P2 * P2
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices
            sage: 2 * P1
            A 1-dimensional polyhedron in ZZ^1 defined as the convex hull of 2 vertices
            sage: P1 * 2.0
            A 1-dimensional polyhedron in RDF^1 defined as the convex hull of 2 vertices

        An alias is :meth:`cartesian_product`::

            sage: P1.cartesian_product(P2) == P1.product(P2)
            True

        TESTS:

        Check that :issue:`15253` is fixed::

            sage: polytopes.hypercube(1) * polytopes.hypercube(2)
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 8 vertices
        """
    cartesian_product = product
    def join(self, other):
        """
        Return the join of ``self`` and ``other``.

        The join of two polyhedra is obtained by first placing the two objects in
        two non-intersecting affine subspaces `V`, and `W` whose affine hull is
        the whole ambient space, and finally by taking the convex hull of their
        union. The dimension of the join is the sum of the dimensions of the
        two polyhedron plus 1.

        INPUT:

        - ``other`` -- a polyhedron

        EXAMPLES::

            sage: P1 = Polyhedron([[0],[1]], base_ring=ZZ)
            sage: P2 = Polyhedron([[0],[1]], base_ring=QQ)
            sage: P1.join(P2)
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 4 vertices
            sage: P1.join(P1)
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 4 vertices
            sage: P2.join(P2)
            A 3-dimensional polyhedron in QQ^3 defined as the convex hull of 4 vertices

        An unbounded example::

            sage: R1 = Polyhedron(rays=[[1]])
            sage: R1.join(R1)
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 2 vertices and 2 rays

        TESTS::

            sage: C = polytopes.hypercube(5)
            sage: S = Polyhedron([[1]])
            sage: C.join(S).is_combinatorially_isomorphic(C.pyramid())                  # needs sage.graphs
            True

            sage: P = polytopes.simplex(backend='cdd')
            sage: Q = polytopes.simplex(backend='ppl')
            sage: P.join(Q).backend()
            'cdd'
            sage: Q.join(P).backend()
            'ppl'

        Check that the double description is set up correctly::

            sage: P = polytopes.cross_polytope(4)
            sage: P1 = polytopes.cross_polytope(4, backend='field')
            sage: P.join(P) == P1.join(P1)
            True

            sage: P = 4*polytopes.hypercube(4)
            sage: P1 = 4*polytopes.hypercube(4, backend='field')
            sage: P.join(P) == P1.join(P1)
            True

            sage: P = polytopes.permutahedron(4)
            sage: P1 = polytopes.permutahedron(4, backend='field')
            sage: P.join(P) == P1.join(P1)
            True
        """
    def subdirect_sum(self, other):
        """
        Return the subdirect sum of ``self`` and ``other``.

        The subdirect sum of two polyhedron is a projection of the join of the
        two polytopes. It is obtained by placing the two objects in orthogonal subspaces
        intersecting at the origin.

        INPUT:

        - ``other`` -- a :class:`~sage.geometry.polyhedron.base.Polyhedron_base`

        EXAMPLES::

            sage: P1 = Polyhedron([[1], [2]], base_ring=ZZ)
            sage: P2 = Polyhedron([[3], [4]], base_ring=QQ)
            sage: sds = P1.subdirect_sum(P2); sds
            A 2-dimensional polyhedron in QQ^2
             defined as the convex hull of 4 vertices
            sage: sds.vertices()
            (A vertex at (0, 3),
             A vertex at (0, 4),
             A vertex at (1, 0),
             A vertex at (2, 0))

        .. SEEALSO::

            :meth:`join`
            :meth:`direct_sum`

        TESTS::

            sage: P = polytopes.simplex(backend='cdd')
            sage: Q = polytopes.simplex(backend='ppl')
            sage: P.subdirect_sum(Q).backend()
            'cdd'
            sage: Q.subdirect_sum(P).backend()
            'ppl'
        """
    def direct_sum(self, other):
        """
        Return the direct sum of ``self`` and ``other``.

        The direct sum of two polyhedron is the subdirect sum of the two, when
        they have the origin in their interior. To avoid checking if the origin
        is contained in both, we place the affine subspace containing ``other``
        at the center of ``self``.

        INPUT:

        - ``other`` -- a :class:`~sage.geometry.polyhedron.base.Polyhedron_base`

        EXAMPLES::

            sage: P1 = Polyhedron([[1], [2]], base_ring=ZZ)
            sage: P2 = Polyhedron([[3], [4]], base_ring=QQ)
            sage: ds = P1.direct_sum(P2);ds
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 4 vertices
            sage: ds.vertices()
            (A vertex at (1, 0),
             A vertex at (2, 0),
             A vertex at (3/2, -1/2),
             A vertex at (3/2, 1/2))

        .. SEEALSO::

            :meth:`join`
            :meth:`subdirect_sum`

        TESTS:

        Check that the backend is preserved::

            sage: P = polytopes.simplex(backend='cdd')
            sage: Q = polytopes.simplex(backend='ppl')
            sage: P.direct_sum(Q).backend()
            'cdd'
            sage: Q.direct_sum(P).backend()
            'ppl'

        Check that :issue:`28506` is fixed::

            sage: s2 = polytopes.simplex(2)
            sage: s3 = polytopes.simplex(3)
            sage: s2.direct_sum(s3)
            A 5-dimensional polyhedron in QQ^7 defined as the convex hull of 7 vertices
        """
    @coerce_binop
    def convex_hull(self, other):
        """
        Return the convex hull of the set-theoretic union of the two
        polyhedra.

        INPUT:

        - ``other`` -- a :class:`Polyhedron`

        OUTPUT: the convex hull

        EXAMPLES::

            sage: a_simplex = polytopes.simplex(3, project=True)
            sage: verts = a_simplex.vertices()
            sage: verts = [[x[0]*3/5 + x[1]*4/5, -x[0]*4/5 + x[1]*3/5, x[2]] for x in verts]
            sage: another_simplex = Polyhedron(vertices=verts)
            sage: simplex_union = a_simplex.convex_hull(another_simplex)
            sage: simplex_union.n_vertices()
            7
        """
    @coerce_binop
    def intersection(self, other):
        """
        Return the intersection of one polyhedron with another.

        INPUT:

        - ``other`` -- a :class:`Polyhedron`

        OUTPUT: the intersection

        Note that the intersection of two `\\ZZ`-polyhedra might not be
        a `\\ZZ`-polyhedron. In this case, a `\\QQ`-polyhedron is
        returned.

        EXAMPLES::

            sage: cube = polytopes.hypercube(3)
            sage: oct = polytopes.cross_polytope(3)
            sage: cube.intersection(oct*2)
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 12 vertices

        As a shorthand, one may use::

            sage: cube & oct*2
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 12 vertices

        The intersection of two `\\ZZ`-polyhedra is not necessarily a `\\ZZ`-polyhedron::

            sage: P = Polyhedron([(0,0),(1,1)], base_ring=ZZ)
            sage: P.intersection(P)
            A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: Q = Polyhedron([(0,1),(1,0)], base_ring=ZZ)
            sage: P.intersection(Q)
            A 0-dimensional polyhedron in QQ^2 defined as the convex hull of 1 vertex
            sage: _.Vrepresentation()
            (A vertex at (1/2, 1/2),)

        TESTS:

        Check that :issue:`19012` is fixed::

            sage: # needs sage.rings.number_field
            sage: K.<a> = QuadraticField(5)
            sage: P = Polyhedron([[0, 0], [0, a], [1, 1]])
            sage: Q = Polyhedron(ieqs=[[-1, a, 1]])
            sage: P.intersection(Q)
            A 2-dimensional polyhedron in
             (Number Field in a with defining polynomial x^2 - 5 with a = 2.236067977499790?)^2
             defined as the convex hull of 4 vertices
        """
    __and__ = intersection
    def translation(self, displacement):
        """
        Return the translated polyhedron.

        INPUT:

        - ``displacement`` -- a displacement vector or a list/tuple of
          coordinates that determines a displacement vector

        OUTPUT: the translated polyhedron

        .. SEEALSO:: :meth:`linear_transformation`, :meth:`dilation`

        EXAMPLES::

            sage: P = Polyhedron([[0,0], [1,0], [0,1]], base_ring=ZZ)
            sage: P.translation([2,1])
            A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
            sage: P.translation(vector(QQ, [2,1]))
            A 2-dimensional polyhedron in QQ^2 defined as the convex hull of 3 vertices

        TESTS::

            sage: P = Polyhedron([[0,0], [1,0], [0,1]], base_ring=ZZ, backend='field')
            sage: P.translation([2,1]).backend()
            'field'

        Check that precomputed data is set up correctly::

            sage: P = polytopes.permutahedron(4)*Polyhedron(lines=[[1]])
            sage: Q = P.change_ring(P.base_ring(), backend='field')
            sage: P + vector([1,2,3,4,5]) == Q + vector([1,2,3,4,5])
            True
            sage: P + vector([1,2,3,4,5/2]) == Q + vector([1,2,3,4,5/2])
            True
        """
    def dilation(self, scalar):
        """
        Return the dilated (uniformly stretched) polyhedron.

        INPUT:

        - ``scalar`` -- a scalar, not necessarily in :meth:`base_ring`

        OUTPUT:

        The polyhedron dilated by that scalar, possibly coerced to a
        bigger base ring.

        .. SEEALSO:: :meth:`linear_transformation`, :meth:`translation`

        EXAMPLES::

            sage: p = Polyhedron(vertices=[[t,t^2,t^3] for t in srange(2,6)])
            sage: next(p.vertex_generator())
            A vertex at (2, 4, 8)
            sage: p2 = p.dilation(2)
            sage: next(p2.vertex_generator())
            A vertex at (4, 8, 16)
            sage: p.dilation(2) == p * 2
            True

        TESTS:

        Dilation of empty polyhedra works, see :issue:`14987`::

            sage: p = Polyhedron(ambient_dim=2); p
            The empty polyhedron in ZZ^2
            sage: p.dilation(3)
            The empty polyhedron in ZZ^2

            sage: p = Polyhedron(vertices=[(1,1)], rays=[(1,0)], lines=[(0,1)])
            sage: (-p).rays()
            (A ray in the direction (-1, 0),)
            sage: (-p).lines()
            (A line in the direction (0, 1),)

            sage: (0*p).rays()
            ()
            sage: (0*p).lines()
            ()
        """
    def __truediv__(self, scalar):
        """
        Divide by a scalar factor.

        See :meth:`dilation` for details.

        EXAMPLES::

            sage: p = Polyhedron(vertices = [[t,t^2,t^3] for t in srange(2,4)])
            sage: (p/5).Vrepresentation()
            (A vertex at (2/5, 4/5, 8/5), A vertex at (3/5, 9/5, 27/5))
            sage: (p/int(5)).Vrepresentation()
            (A vertex at (0.4, 0.8, 1.6), A vertex at (0.6, 1.8, 5.4))
        """
    def linear_transformation(self, linear_transf, new_base_ring=None):
        """
        Return the linear transformation of ``self``.

        INPUT:

        - ``linear_transf`` -- a matrix, not necessarily in :meth:`base_ring`
        - ``new_base_ring`` -- ring (optional); specify the new base ring;
          may avoid coercion failure

        OUTPUT:

        The polyhedron transformed by that matrix, possibly coerced to a
        bigger base ring.

        .. SEEALSO:: :meth:`dilation`, :meth:`translation`

        EXAMPLES::

            sage: b3 = polytopes.Birkhoff_polytope(3)
            sage: proj_mat = matrix([[0,1,0,0,0,0,0,0,0], [0,0,0,1,0,0,0,0,0],
            ....:                    [0,0,0,0,0,1,0,0,0], [0,0,0,0,0,0,0,1,0]])
            sage: b3_proj = proj_mat * b3; b3_proj
            A 3-dimensional polyhedron in ZZ^4 defined as the convex hull of 5 vertices

            sage: # needs sage.rings.number_field
            sage: square = polytopes.regular_polygon(4)
            sage: square.vertices_list()
            [[0, -1], [1, 0], [-1, 0], [0, 1]]
            sage: transf = matrix([[1,1], [0,1]])
            sage: sheared = transf * square
            sage: sheared.vertices_list()
            [[-1, -1], [1, 0], [-1, 0], [1, 1]]
            sage: sheared == square.linear_transformation(transf)
            True

        Specifying the new base ring may avoid coercion failure::

            sage: # needs sage.rings.number_field
            sage: K.<sqrt2> = QuadraticField(2)
            sage: L.<sqrt3> = QuadraticField(3)
            sage: P = polytopes.cube()*sqrt2
            sage: M = matrix([[sqrt3, 0, 0], [0, sqrt3, 0], [0, 0, 1]])
            sage: P.linear_transformation(M, new_base_ring=K.composite_fields(L)[0])
            A 3-dimensional polyhedron in
             (Number Field in sqrt2sqrt3 with defining polynomial x^4 - 10*x^2 + 1
              with sqrt2sqrt3 = 0.3178372451957823?)^3
             defined as the convex hull of 8 vertices

        Linear transformation without specified new base ring fails in this case::

            sage: M*P                                                                   # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
            'Full MatrixSpace of 3 by 3 dense matrices over Number Field in sqrt3
            with defining polynomial x^2 - 3 with sqrt3 = 1.732050807568878?' and
            'Full MatrixSpace of 3 by 8 dense matrices over Number Field in sqrt2
            with defining polynomial x^2 - 2 with sqrt2 = 1.414213562373095?'

        TESTS:

        One can scale by a scalar as follows::

            sage: P = polytopes.cube()
            sage: P2 = P.linear_transformation(2); P2
            A 3-dimensional polyhedron in QQ^3 defined as
            the convex hull of 8 vertices
            sage: P2.volume()
            64

        Linear transformation respects backend::

            sage: P = polytopes.simplex(backend='field')
            sage: t = matrix([[1,1,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]])
            sage: P.linear_transformation(t).backend()
            'field'

        Check that coercion works::

            sage: (1.0 * proj_mat) * b3
            A 3-dimensional polyhedron in RDF^4 defined as the convex hull of 5 vertices
            sage: (1/1 * proj_mat) * b3
            A 3-dimensional polyhedron in QQ^4 defined as the convex hull of 5 vertices
            sage: (AA(2).sqrt() * proj_mat) * b3                                        # needs sage.rings.number_field
            A 3-dimensional polyhedron in AA^4 defined as the convex hull of 5 vertices

        Check that zero-matrices act correctly::

            sage: Matrix([]) * b3
            A 0-dimensional polyhedron in ZZ^0 defined as the convex hull of 1 vertex
            sage: Matrix([[0 for _ in range(9)]]) * b3
            A 0-dimensional polyhedron in ZZ^1 defined as the convex hull of 1 vertex
            sage: Matrix([[0 for _ in range(9)] for _ in range(4)]) * b3
            A 0-dimensional polyhedron in ZZ^4 defined as the convex hull of 1 vertex
            sage: Matrix([[0 for _ in range(8)]]) * b3
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
            'Full MatrixSpace of 1 by 8 dense matrices over Integer Ring' and
            'Full MatrixSpace of 9 by 6 dense matrices over Integer Ring'
            sage: Matrix(ZZ, []) * b3
            A 0-dimensional polyhedron in ZZ^0 defined as the convex hull of 1 vertex
            sage: Matrix(ZZ, [[],[]]) * b3
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for *:
            'Full MatrixSpace of 2 by 0 dense matrices over Integer Ring' and
            'Full MatrixSpace of 9 by 6 dense matrices over Integer Ring'

        Check that the precomputed double description is correct::

            sage: P = polytopes.permutahedron(4)
            sage: Q = P.change_ring(QQ, backend='field')
            sage: P.affine_hull_projection() == Q.affine_hull_projection()
            True

            sage: M = matrix([[1, 2, 3, 4], [2, 3, 4, 5], [0, 0, 5, 1], [0, 2, 0, 3]])
            sage: M*P == M*Q
            True

            sage: M = matrix([[1, 2, 3, 4], [2, 3, 4, 5], [0, 0, 5, 1], [0, 2, 0, 3], [0, 1, 0, -3]])
            sage: M*P == M*Q
            True
        """
    def face_truncation(self, face, linear_coefficients=None, cut_frac=None):
        """
        Return a new polyhedron formed by truncating a face by an hyperplane.

        By default, the normal vector of the hyperplane used to truncate the
        polyhedron is obtained by taking the barycenter vector of the cone
        corresponding to the truncated face in the normal fan of the
        polyhedron. It is possible to change the direction using the option
        ``linear_coefficients``.

        To determine how deep the truncation is done, the method uses the
        parameter ``cut_frac``. By default it is equal to `\\frac{1}{3}`. Once
        the normal vector of the cutting hyperplane is chosen, the vertices of
        polyhedron are evaluated according to the corresponding linear
        function. The parameter `\\frac{1}{3}` means that the cutting
        hyperplane is placed `\\frac{1}{3}` of the way from the vertices of the
        truncated face to the next evaluated vertex.

        INPUT:

        - ``face`` -- a :class:`~sage.geometry.polyhedron.face.PolyhedronFace`
        - ``linear_coefficients`` -- tuple of integer. Specifies the coefficient
          of the normal vector of the cutting hyperplane used to truncate the
          face.
          The default direction is determined using the normal fan of the
          polyhedron.
        - ``cut_frac`` -- number between 0 and 1. Determines where the
          hyperplane cuts the polyhedron. A value close to 0 cuts very close
          to the face, whereas a value close to 1 cuts very close to the next
          vertex (according to the normal vector of the cutting hyperplane).
          Default is `\\frac{1}{3}`.

        OUTPUT: a Polyhedron object, truncated as described above

        EXAMPLES::

            sage: Cube = polytopes.hypercube(3)
            sage: vertex_trunc1 = Cube.face_truncation(Cube.faces(0)[0])
            sage: vertex_trunc1.f_vector()
            (1, 10, 15, 7, 1)
            sage: tuple(f.ambient_V_indices() for f in vertex_trunc1.faces(2))
            ((4, 5, 6, 7, 9),
             (0, 3, 4, 8, 9),
             (0, 1, 6, 7, 8),
             (7, 8, 9),
             (2, 3, 4, 5),
             (1, 2, 5, 6),
             (0, 1, 2, 3))
            sage: vertex_trunc1.vertices()
            (A vertex at (1, -1, -1),
             A vertex at (1, 1, -1),
             A vertex at (1, 1, 1),
             A vertex at (1, -1, 1),
             A vertex at (-1, -1, 1),
             A vertex at (-1, 1, 1),
             A vertex at (-1, 1, -1),
             A vertex at (-1, -1/3, -1),
             A vertex at (-1/3, -1, -1),
             A vertex at (-1, -1, -1/3))
            sage: vertex_trunc2 = Cube.face_truncation(Cube.faces(0)[0], cut_frac=1/2)
            sage: vertex_trunc2.f_vector()
            (1, 10, 15, 7, 1)
            sage: tuple(f.ambient_V_indices() for f in vertex_trunc2.faces(2))
            ((4, 5, 6, 7, 9),
             (0, 3, 4, 8, 9),
             (0, 1, 6, 7, 8),
             (7, 8, 9),
             (2, 3, 4, 5),
             (1, 2, 5, 6),
             (0, 1, 2, 3))
            sage: vertex_trunc2.vertices()
            (A vertex at (1, -1, -1),
             A vertex at (1, 1, -1),
             A vertex at (1, 1, 1),
             A vertex at (1, -1, 1),
             A vertex at (-1, -1, 1),
             A vertex at (-1, 1, 1),
             A vertex at (-1, 1, -1),
             A vertex at (-1, 0, -1),
             A vertex at (0, -1, -1),
             A vertex at (-1, -1, 0))
            sage: vertex_trunc3 = Cube.face_truncation(Cube.faces(0)[0], cut_frac=0.3)
            sage: vertex_trunc3.vertices()
            (A vertex at (-1.0, -1.0, 1.0),
             A vertex at (-1.0, 1.0, -1.0),
             A vertex at (-1.0, 1.0, 1.0),
             A vertex at (1.0, 1.0, -1.0),
             A vertex at (1.0, 1.0, 1.0),
             A vertex at (1.0, -1.0, 1.0),
             A vertex at (1.0, -1.0, -1.0),
             A vertex at (-0.4, -1.0, -1.0),
             A vertex at (-1.0, -0.4, -1.0),
             A vertex at (-1.0, -1.0, -0.4))
            sage: edge_trunc = Cube.face_truncation(Cube.faces(1)[11])
            sage: edge_trunc.f_vector()
            (1, 10, 15, 7, 1)
            sage: tuple(f.ambient_V_indices() for f in edge_trunc.faces(2))
            ((0, 5, 6, 7),
             (1, 4, 5, 6, 8),
             (6, 7, 8, 9),
             (0, 2, 3, 7, 9),
             (1, 2, 8, 9),
             (0, 3, 4, 5),
             (1, 2, 3, 4))
             sage: face_trunc = Cube.face_truncation(Cube.faces(2)[2])
             sage: face_trunc.vertices()
             (A vertex at (1, -1, -1),
              A vertex at (1, 1, -1),
              A vertex at (1, 1, 1),
              A vertex at (1, -1, 1),
              A vertex at (-1/3, -1, 1),
              A vertex at (-1/3, 1, 1),
              A vertex at (-1/3, 1, -1),
              A vertex at (-1/3, -1, -1))
             sage: face_trunc.face_lattice().is_isomorphic(Cube.face_lattice())         # needs sage.combinat sage.graphs
             True

        TESTS:

        Testing that the backend is preserved::

            sage: Cube = polytopes.cube(backend='field')
            sage: face_trunc = Cube.face_truncation(Cube.faces(2)[0])
            sage: face_trunc.backend()
            'field'

        Testing that :issue:`28506` is fixed::

            sage: P = polytopes.twenty_four_cell()
            sage: P = P.dilation(6)
            sage: P = P.change_ring(ZZ)
            sage: P.face_truncation(P.faces(2)[0], cut_frac=1)
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 27 vertices
        """
    def stack(self, face, position=None):
        """
        Return a new polyhedron formed by stacking onto a ``face``. Stacking a
        face adds a new vertex located slightly outside of the designated face.

        INPUT:

        - ``face`` -- a PolyhedronFace

        - ``position`` -- a positive number. Determines a relative distance
          from the barycenter of ``face``. A value close to 0 will place the
          new vertex close to the face and a large value further away. Default
          is `1`. If the given value is too large, an error is returned.

        OUTPUT: a Polyhedron object

        EXAMPLES::

            sage: cube = polytopes.cube()
            sage: square_face = cube.facets()[2]
            sage: stacked_square = cube.stack(square_face)
            sage: stacked_square.f_vector()
            (1, 9, 16, 9, 1)

            sage: edge_face = cube.faces(1)[3]
            sage: stacked_edge = cube.stack(edge_face)
            sage: stacked_edge.f_vector()
            (1, 9, 17, 10, 1)

            sage: cube.stack(cube.faces(0)[0])
            Traceback (most recent call last):
            ...
            ValueError: cannot stack onto a vertex

            sage: stacked_square_half = cube.stack(square_face, position=1/2)
            sage: stacked_square_half.f_vector()
            (1, 9, 16, 9, 1)
            sage: stacked_square_large = cube.stack(square_face, position=10)

            sage: # needs sage.rings.number_field
            sage: hexaprism = polytopes.regular_polygon(6).prism()
            sage: hexaprism.f_vector()
            (1, 12, 18, 8, 1)
            sage: square_face = hexaprism.faces(2)[2]
            sage: stacked_hexaprism = hexaprism.stack(square_face)
            sage: stacked_hexaprism.f_vector()
            (1, 13, 22, 11, 1)

            sage: hexaprism.stack(square_face, position=4)                              # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            ValueError: the chosen position is too large

            sage: s = polytopes.simplex(7)
            sage: f = s.faces(3)[69]
            sage: sf = s.stack(f); sf
            A 7-dimensional polyhedron in QQ^8 defined as the convex hull of 9 vertices
            sage: sf.vertices()
            (A vertex at (-4, -4, -4, -4, 17/4, 17/4, 17/4, 17/4),
             A vertex at (0, 0, 0, 0, 0, 0, 0, 1),
             A vertex at (0, 0, 0, 0, 0, 0, 1, 0),
             A vertex at (0, 0, 0, 0, 0, 1, 0, 0),
             A vertex at (0, 0, 0, 0, 1, 0, 0, 0),
             A vertex at (0, 0, 0, 1, 0, 0, 0, 0),
             A vertex at (0, 0, 1, 0, 0, 0, 0, 0),
             A vertex at (0, 1, 0, 0, 0, 0, 0, 0),
             A vertex at (1, 0, 0, 0, 0, 0, 0, 0))

        It is possible to stack on unbounded faces::

            sage: Q = Polyhedron(vertices=[[0,1], [1,0]], rays=[[1,1]])
            sage: E = Q.faces(1)
            sage: Q.stack(E[0],1/2).Vrepresentation()
            (A vertex at (0, 1),
             A vertex at (1, 0),
             A ray in the direction (1, 1),
             A vertex at (2, 0))
            sage: Q.stack(E[1],1/2).Vrepresentation()
            (A vertex at (0, 1),
             A vertex at (0, 2),
             A vertex at (1, 0),
             A ray in the direction (1, 1))
            sage: Q.stack(E[2],1/2).Vrepresentation()
            (A vertex at (0, 0),
             A vertex at (0, 1),
             A vertex at (1, 0),
             A ray in the direction (1, 1))

        Stacking requires a proper face::

            sage: Q.stack(Q.faces(2)[0])
            Traceback (most recent call last):
            ...
            ValueError: can only stack on proper face

        TESTS:

        Checking that the backend is preserved::

            sage: Cube = polytopes.cube(backend='field')
            sage: stack = Cube.stack(Cube.faces(2)[0])
            sage: stack.backend()
            'field'

        Taking the stacking vertex too far with the parameter ``position``
        may result in a failure to produce the desired
        (combinatorial type of) polytope.
        The interval of permitted values is always open.
        This is the smallest unpermitted value::

            sage: P = polytopes.octahedron()
            sage: P.stack(P.faces(2)[0], position=4)
            Traceback (most recent call last):
            ...
            ValueError: the chosen position is too large

        Testing that :issue:`29057` is fixed::

            sage: P = polytopes.cross_polytope(4)
            sage: P.stack(P.faces(3)[0])
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 9 vertices
        """
    def wedge(self, face, width: int = 1):
        """
        Return the wedge over a ``face`` of the polytope ``self``.

        The wedge over a face `F` of a polytope `P` with width `w \\not= 0`
        is defined as:

        .. MATH::

            (P \\times \\mathbb{R}) \\cap \\{a^\\top x + |w x_{d+1}| \\leq b\\}

        where `\\{x | a^\\top x = b\\}` is a supporting hyperplane defining `F`.

        INPUT:

        - ``face`` -- a PolyhedronFace of ``self``, the face which we take
          the wedge over
        - ``width`` -- a nonzero number (default: ``1``);
          specifies how wide the wedge will be

        OUTPUT:

        A (bounded) polyhedron

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: P_4 = polytopes.regular_polygon(4)
            sage: W1 = P_4.wedge(P_4.faces(1)[0]); W1
            A 3-dimensional polyhedron in AA^3 defined as the convex hull of 6 vertices
            sage: triangular_prism = polytopes.regular_polygon(3).prism()
            sage: W1.is_combinatorially_isomorphic(triangular_prism)                    # needs sage.graphs
            True

            sage: Q = polytopes.hypersimplex(4,2)
            sage: W2 = Q.wedge(Q.faces(2)[7]); W2
            A 4-dimensional polyhedron in QQ^5 defined as the convex hull of 9 vertices
            sage: W2.vertices()
            (A vertex at (1, 1, 0, 0, 1),
             A vertex at (1, 1, 0, 0, -1),
             A vertex at (1, 0, 1, 0, 1),
             A vertex at (1, 0, 1, 0, -1),
             A vertex at (1, 0, 0, 1, 1),
             A vertex at (1, 0, 0, 1, -1),
             A vertex at (0, 0, 1, 1, 0),
             A vertex at (0, 1, 1, 0, 0),
             A vertex at (0, 1, 0, 1, 0))

            sage: W3 = Q.wedge(Q.faces(1)[11]); W3
            A 4-dimensional polyhedron in QQ^5 defined as the convex hull of 10 vertices
            sage: W3.vertices()
            (A vertex at (1, 1, 0, 0, -2),
             A vertex at (1, 1, 0, 0, 2),
             A vertex at (1, 0, 1, 0, -2),
             A vertex at (1, 0, 1, 0, 2),
             A vertex at (1, 0, 0, 1, 1),
             A vertex at (1, 0, 0, 1, -1),
             A vertex at (0, 1, 0, 1, 0),
             A vertex at (0, 1, 1, 0, 1),
             A vertex at (0, 0, 1, 1, 0),
             A vertex at (0, 1, 1, 0, -1))

            sage: C_3_7 = polytopes.cyclic_polytope(3,7)
            sage: P_6 = polytopes.regular_polygon(6)                                    # needs sage.rings.number_field
            sage: W4 = P_6.wedge(P_6.faces(1)[0])                                       # needs sage.rings.number_field
            sage: W4.is_combinatorially_isomorphic(C_3_7.polar())                       # needs sage.graphs sage.rings.number_field
            True

        REFERENCES:

        For more information, see Chapter 15 of [HoDaCG17]_.

        TESTS:

        The backend should be preserved as long as the value of width permits.
        The base_ring will change to the field of fractions of the current
        base_ring, unless ``width`` forces a different ring. ::

            sage: P = polytopes.cyclic_polytope(3,7, base_ring=ZZ, backend='field')
            sage: W1 = P.wedge(P.faces(2)[0]); W1.base_ring(); W1.backend()
            Rational Field
            'field'
            sage: W2 = P.wedge(P.faces(2)[0], width=5/2); W2.base_ring(); W2.backend()
            Rational Field
            'field'
            sage: W2 = P.wedge(P.faces(2)[9], width=4/2); W2.base_ring(); W2.backend()
            Rational Field
            'field'
            sage: W2.vertices()
            (A vertex at (3, 9, 27, -1/2),
             A vertex at (4, 16, 64, -2),
             A vertex at (6, 36, 216, -10),
             A vertex at (5, 25, 125, -5),
             A vertex at (2, 4, 8, 0),
             A vertex at (1, 1, 1, 0),
             A vertex at (0, 0, 0, 0),
             A vertex at (3, 9, 27, 1/2),
             A vertex at (4, 16, 64, 2),
             A vertex at (6, 36, 216, 10),
             A vertex at (5, 25, 125, 5))
            sage: W2 = P.wedge(P.faces(2)[2], width=1.0); W2.base_ring(); W2.backend()
            Real Double Field
            'cdd'
        """
    def face_split(self, face):
        """
        Return the face splitting of the face ``face``.

        Splitting a face correspond to the bipyramid (see :meth:`bipyramid`)
        of ``self`` where the two new vertices are placed above and below
        the center of ``face`` instead of the center of the whole polyhedron.
        The two new vertices are placed in the new dimension at height `-1` and
        `1`.

        INPUT:

        - ``face`` -- a PolyhedronFace or a Vertex

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: pentagon  = polytopes.regular_polygon(5)
            sage: f = pentagon.faces(1)[0]
            sage: fsplit_pentagon = pentagon.face_split(f)
            sage: fsplit_pentagon.f_vector()
            (1, 7, 14, 9, 1)

        TESTS:

        Check that :issue:`28668` is fixed::

            sage: P = polytopes.octahedron()
            sage: P.face_split(P.faces(2)[0])
            A 4-dimensional polyhedron in QQ^4 defined as the convex hull of 8 vertices

        .. SEEALSO::

            :meth:`one_point_suspension`
        """
    def lawrence_extension(self, v):
        """
        Return the Lawrence extension of ``self`` on the point ``v``.

        Let `P` be a polytope and `v` be a vertex of `P` or a point outside
        `P`. The Lawrence extension of `P` on `v` is the convex hull of
        `(v,1),(v,2)` and `(u,0)` for all vertices `u` in `P` other than `v`
        if `v` is a vertex.

        INPUT:

        - ``v`` -- a vertex of ``self`` or a point outside it

        EXAMPLES::

            sage: P = polytopes.cube()
            sage: P.lawrence_extension(P.vertices()[0])
            A 4-dimensional polyhedron in ZZ^4 defined as the convex hull of 9 vertices
            sage: P.lawrence_extension([-1,-1,-1])
            A 4-dimensional polyhedron in ZZ^4 defined as the convex hull of 9 vertices

        REFERENCES:

            For more information, see Section 6.6 of [Zie2007]_.
        """
    def one_point_suspension(self, vertex):
        """
        Return the one-point suspension of ``self`` by splitting the vertex
        ``vertex``.

        The resulting polyhedron has one more vertex and its dimension
        increases by one.

        INPUT:

        - ``vertex`` -- a Vertex of ``self``

        EXAMPLES::

            sage: cube = polytopes.cube()
            sage: v = cube.vertices()[0]
            sage: ops_cube = cube.one_point_suspension(v)
            sage: ops_cube.f_vector()
            (1, 9, 24, 24, 9, 1)

            sage: # needs sage.rings.number_field
            sage: pentagon  = polytopes.regular_polygon(5)
            sage: v = pentagon.vertices()[0]
            sage: ops_pentagon = pentagon.one_point_suspension(v)
            sage: ops_pentagon.f_vector()
            (1, 6, 12, 8, 1)

        It works with a polyhedral face as well::

            sage: vv = cube.faces(0)[1]
            sage: ops_cube2 = cube.one_point_suspension(vv)
            sage: ops_cube == ops_cube2
            True

        .. SEEALSO::

            :meth:`face_split`

        TESTS::

            sage: e = cube.faces(1)[0]
            sage: cube.one_point_suspension(e)
            Traceback (most recent call last):
            ...
            TypeError: the vertex
            A 1-dimensional face of a Polyhedron in ZZ^3 defined as the convex hull of 2 vertices
            should be a Vertex or PolyhedronFace of dimension 0
        """
