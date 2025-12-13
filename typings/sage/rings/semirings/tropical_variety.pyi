from sage.rings.infinity import infinity as infinity
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class TropicalVariety(UniqueRepresentation, SageObject):
    """
    A tropical variety in `\\RR^n`.

    A tropical variety is defined as a corner locus of tropical polynomial
    function. This means it consist of all points in `\\RR^n` for which
    the minimum (maximum) of the function is attained at least twice.

    We represent the tropical variety as a list of lists, where the
    inner list consist of three parts. The first one is a parametric
    equations for tropical roots. The second one is the condition
    for parameters. The third one is the order of the corresponding
    component.

    INPUT:

    - ``poly`` -- a :class:`TropicalMPolynomial`

    ALGORITHM:

    We need to determine a corner locus of this tropical polynomial
    function, which is all points `(x_1, x_2, \\ldots, x_n)` for which
    the maximum (minimum) is obtained at least twice. First, we convert
    each monomial to its corresponding linear function. Then for each two
    monomials of polynomial, we find the points where their values are
    equal. Since we attempt to solve the equality of two equations in `n`
    variables, the solution set will be described by `n-1` parameters.

    Next, we need to check if the value of previous two monomials at the
    points in solution set is really the maximum (minimum) of function.
    We do this by solving the inequality of the previous monomial with all
    other monomials in the polynomial after substituting the parameter.
    This will give us the condition of parameters. Each of this condition
    is then combined by union operator. If this final condition is not an
    empty set, then it represent one component of tropical root. Then we
    calculate the weight of this particular component by the maximum of
    gcd of the numbers `|i-k|` and `|j-l|` for all pairs `(i,j)` and
    `(k,l)` such that the value of on this component is given by the
    corresponding monomials.

    EXAMPLES:

    We construct a tropical variety in `\\RR^2`, where it is called a
    tropical curve::

        sage: T = TropicalSemiring(QQ, use_min=False)
        sage: R.<x,y> = PolynomialRing(T)
        sage: p1 = R(1)*x + x*y + R(0); p1
        0*x*y + 1*x + 0
        sage: tv = p1.tropical_variety(); tv
        Tropical curve of 0*x*y + 1*x + 0
        sage: tv.components()
        [[(t1, 1), [t1 >= -1], 1], [(-1, t1), [t1 <= 1], 1], [(-t1, t1), [t1 >= 1], 1]]
        sage: tv.vertices()
        {(-1, 1)}
        sage: tv.plot()
        Graphics object consisting of 3 graphics primitives

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=False)
        R = PolynomialRing(T, ('x,y'))
        x, y = R.gen(), R.gen(1)
        p1 = R(1)*x + x*y + R(0)
        sphinx_plot(p1.tropical_variety().plot())

    A slightly different result will be obtained if we use min-plus algebra
    for the base tropical semiring::

        sage: T = TropicalSemiring(QQ, use_min=True)
        sage: R.<x,y> = PolynomialRing(T)
        sage: p1 = R(1)*x + x*y + R(0)
        sage: tv = p1.tropical_variety(); tv
        Tropical curve of 0*x*y + 1*x + 0
        sage: tv.components()
        [[(t1, 1), [t1 <= -1], 1], [(-1, t1), [t1 >= 1], 1], [(-t1, t1), [t1 <= 1], 1]]
        sage: tv.plot()
        Graphics object consisting of 3 graphics primitives

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=True)
        R = PolynomialRing(T, ('x,y'))
        x, y = R.gen(), R.gen(1)
        p1 = R(1)*x + x*y + R(0)
        sphinx_plot(p1.tropical_variety().plot())

    Tropical variety can consist of multiple components with varying orders::

        sage: T = TropicalSemiring(QQ, use_min=False)
        sage: R.<x,y> = PolynomialRing(T)
        sage: p1 = R(7) + T(4)*x + y + R(4)*x*y + R(3)*y^2 + R(-3)*x^2
        sage: tv = p1.tropical_variety(); tv
        Tropical curve of (-3)*x^2 + 4*x*y + 3*y^2 + 4*x + 0*y + 7
        sage: tv.components()
        [[(3, t1), [t1 <= 0], 1],
        [(-t1 + 3, t1), [0 <= t1, t1 <= 2], 1],
        [(t1, 2), [t1 <= 1], 2],
        [(t1, 0), [3 <= t1, t1 <= 7], 1],
        [(7, t1), [t1 <= 0], 1],
        [(t1 - 1, t1), [2 <= t1], 1],
        [(t1 + 7, t1), [0 <= t1], 1]]
        sage: tv.plot()
        Graphics object consisting of 8 graphics primitives

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=False)
        R = PolynomialRing(T, ('x,y'))
        x, y = R.gen(), R.gen(1)
        p1 = R(7) + T(4)*x + y + R(4)*x*y + R(3)*y**2 + R(-3)*x**2
        sphinx_plot(p1.tropical_variety().plot())

    If the tropical polynomial have `n>2` variables, then the result will be
    a tropical hypersurface embedded in a real space `\\RR^n`::

        sage: T = TropicalSemiring(QQ)
        sage: R.<w,x,y,z> = PolynomialRing(T)
        sage: p1 = x*y + R(-1/2)*x*z + R(4)*z^2 + w*x
        sage: tv = p1.tropical_variety(); tv
        Tropical hypersurface of 0*w*x + 0*x*y + (-1/2)*x*z + 4*z^2
        sage: tv.components()
        [[(t1, t2, t3 - 1/2, t3), [t2 - 9/2 <= t3, t3 <= t1 + 1/2, t2 - 5 <= t1], 1],
        [(t1, 2*t2 - t3 + 4, t3, t2), [t3 + 1/2 <= t2, t3 <= t1], 1],
        [(t1, t2, t1, t3), [max(t1 + 1/2, 1/2*t1 + 1/2*t2 - 2) <= t3], 1],
        [(t1, t2 + 9/2, t3, t2), [t2 <= min(t3 + 1/2, t1 + 1/2)], 1],
        [(t1 - 1/2, t2, t3, t1), [t2 - 9/2 <= t1, t1 <= t3 + 1/2, t2 - 5 <= t3], 1],
        [(2*t1 - t2 + 4, t2, t3, t1), [t1 <= min(1/2*t2 + 1/2*t3 - 2, t2 - 9/2)], 1]]
    """
    def __init__(self, poly) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: tv = (x+y).tropical_variety()
            sage: TestSuite(tv).run()

        TESTS::

            sage: from sage.rings.semirings.tropical_variety import TropicalVariety
            sage: R.<x,y> = QQ[]
            sage: p1 = x + y
            sage: TropicalVariety(p1)
            Traceback (most recent call last):
            ...
            ValueError: x + y is not a multivariate tropical polynomial
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<a,x,y,z> = PolynomialRing(T)
            sage: p1 = x*y + R(-1)*x*z
            sage: p1.tropical_variety().dimension()
            4
        """
    def number_of_components(self):
        """
        Return the number of components that make up ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<a,x,y,z> = PolynomialRing(T)
            sage: p1 = x*y*a + x*z + y^2 + a*x + y + z
            sage: p1.tropical_variety().number_of_components()
            13
        """
    def components(self):
        """
        Return all components of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<a,x,y,z> = PolynomialRing(T)
            sage: tv = (a+x+y+z).tropical_variety()
            sage: tv.components()
            [[(t1, t1, t2, t3), [t1 <= min(t3, t2)], 1],
             [(t1, t2, t1, t3), [t1 <= t3, t1 <= t2], 1],
             [(t1, t2, t3, t1), [t1 <= min(t3, t2)], 1],
             [(t1, t2, t2, t3), [t2 <= t3, t2 <= t1], 1],
             [(t1, t2, t3, t2), [t2 <= min(t3, t1)], 1],
             [(t1, t2, t3, t3), [t3 <= min(t1, t2)], 1]]
        """
    def weight_vectors(self):
        """
        Return the weight vectors for each unique intersection of
        components of ``self``.

        Weight vectors are a list of vectors associated with each
        unique intersection of the components of tropical variety.
        Each vector is a normal vector to a component with respect
        to the unique intersection lying within that component.

        Assume ``self`` is a `n`-dimensional tropical variety.
        Suppose `L` is an intersection lying within the components
        `S_1, \\ldots, S_k` with respective weights `w_1, \\ldots, w_k`.
        This `L` is a linear structure in `\\RR^{n-1}` and has `n-1`
        direction vectors `d_1,d_2,\\ldots, d_{n-1}`. Each component
        `S_1, \\ldots, S_k` has a normal vector `n_1, \\ldots, n_k`.
        Then, we scale each normal vector to an integer vector such
        that the greatest common divisor of its elements is 1.

        The weight vector of a component `S_i` with respect to `L`
        can be found by calculating the cross product between direction
        vectors of `L` and normal vector `n_i`.These vectors will
        satisfy the balancing condition `\\sum_{i=1}^k w_k v_k = 0`.

        OUTPUT:

        A tuple of three dictionaries. The first dictionary contains
        equations representing the intersections. The second dictionary
        contains indices of components that contains the intersection.
        The third dictionary contains lists of vectors.

        EXAMPLES:

        Weight vectors of tropical surface::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y,z> = PolynomialRing(T)
            sage: p = x^2 + R(-1)*y + z + R(1)
            sage: tv = p.tropical_variety()
            sage: tv.weight_vectors()
            ({0: ((1/2*u2, u2 + 1, u2), {u2 <= 1}),
              1: ((1/2, 2, u2), {1 <= u2}),
              2: ((1/2, u2, 1), {2 <= u2}),
              3: ((u1, 2, 1), {(1/2) <= u1})},
             {0: [0, 1, 3], 1: [0, 2, 4], 2: [1, 2, 5], 3: [3, 4, 5]},
             {0: [(1, 2, -5/2), (1, -5/2, 2), (-2, 1/2, 1/2)],
              1: [(-1, -2, 0), (0, 2, 0), (1, 0, 0)],
              2: [(1, 0, 2), (0, 0, -2), (-1, 0, 0)],
              3: [(0, 1, 1), (0, 0, -1), (0, -1, 0)]})

        TESTS:

        Checking the balance condition of weight vectors::

            sage: T = TropicalSemiring(QQ)
            sage: R.<a,b,c,d> = PolynomialRing(T)
            sage: f = R.random_element()
            sage: vec = f.tropical_variety().weight_vectors()[2].values()
            sage: all(a == vector([0,0,0,0]) for a in [sum(lst) for lst in vec])  # not tested (:issue:`39663`)
            True
        """

class TropicalSurface(TropicalVariety):
    """
    A tropical surface in `\\RR^3`.

    The tropical surface consists of planar regions and facets, which we
    can call cells. These cells are connected in such a way that they form
    a piecewise linear structure embedded in three-dimensional space. These
    cells meet along edges, where the balancing condition is satisfied.
    This balancing condition ensures that the sum of the outgoing normal
    vectors at each edge is zero, reflecting the equilibrium.

    EXAMPLES::

        sage: T = TropicalSemiring(QQ, use_min=False)
        sage: R.<x,y,z> = PolynomialRing(T)
        sage: p1 = x + y + z + R(0)
        sage: tv = p1.tropical_variety(); tv
        Tropical surface of 0*x + 0*y + 0*z + 0
        sage: tv.components()
        [[(t1, t1, t2), [t2 <= t1, 0 <= t1], 1],
        [(t1, t2, t1), [max(0, t2) <= t1], 1],
        [(0, t1, t2), [t2 <= 0, t1 <= 0], 1],
        [(t1, t2, t2), [max(0, t1) <= t2], 1],
        [(t1, 0, t2), [t2 <= 0, t1 <= 0], 1],
        [(t1, t2, 0), [t1 <= 0, t2 <= 0], 1]]
    """
    def plot(self, color: str = 'random'):
        """
        Return the plot of ``self`` by constructing a polyhedron from
        vertices in ``self.polygon_vertices()``.

        INPUT:

        - ``color`` -- string or tuple that represent a color (default:
          ``random``); ``random`` means each polygon will be assigned
          a different color. If instead a specific ``color`` is provided,
          then all polygon will be given the same color.

        OUTPUT: Graphics3d Object

        EXAMPLES:

        A tropical surface that consist of only one cell::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y,z> = PolynomialRing(T)
            sage: p1 = x + z
            sage: tv = p1.tropical_variety()
            sage: tv.plot()
            Graphics3d Object

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ)
            R = PolynomialRing(T, ('x,y,z'))
            x, y, z = R.gen(), R.gen(1), R.gen(2)
            p1 = x + z
            sphinx_plot(p1.tropical_variety().plot())

        A tropical surface with multiple cells that exhibit complex and
        intriguing geometric structures::

            sage: p2 = x^2 + x + y + z + R(1)
            sage: tv = p2.tropical_variety()
            sage: tv.plot() # long time
            Graphics3d Object

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ)
            R = PolynomialRing(T, ('x,y,z'))
            x, y, z = R.gen(), R.gen(1), R.gen(2)
            p2 = x**2 + x + y + z + R(1)
            sphinx_plot(p2.tropical_variety().plot())
        """

class TropicalCurve(TropicalVariety):
    """
    A tropical curve in `\\RR^2`.

    The tropical curve consists of line segments and half-lines, which we
    call edges. These edges are connected in such a way that they form a
    piecewise linear graph embedded in the plane. These edges meet at
    a vertices, where the balancing condition is satisfied. This balancing
    condition ensures that the sum of the outgoing slopes at each vertex
    is zero, reflecting the equilibrium.

    EXAMPLES:

    We define some tropical curves::

        sage: T = TropicalSemiring(QQ, use_min=False)
        sage: R.<x,y> = PolynomialRing(T)
        sage: p1 = x + y + R(0)
        sage: tv1 = p1.tropical_variety(); tv1
        Tropical curve of 0*x + 0*y + 0
        sage: tv1.components()
        [[(t1, t1), [t1 >= 0], 1], [(0, t1), [t1 <= 0], 1], [(t1, 0), [t1 <= 0], 1]]
        sage: tv1.plot()
        Graphics object consisting of 3 graphics primitives

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=False)
        R = PolynomialRing(T, ('x,y'))
        x, y = R.gen(), R.gen(1)
        p1 = x + y + R(0)
        sphinx_plot(p1.tropical_variety().plot())

    ::

        sage: p2 = R(-2)*x^2 + R(-1)*x + R(1/2)*y + R(1/6)
        sage: tv2 = p2.tropical_variety()
        sage: tv2.components()
        [[(1/2*t1 + 5/4, t1), [(-1/3) <= t1], 1],
         [(13/12, t1), [t1 <= (-1/3)], 2],
         [(t1, -1/3), [t1 <= (13/12)], 1]]
        sage: tv2.plot()
        Graphics object consisting of 4 graphics primitives

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=False)
        R = PolynomialRing(T, ('x,y'))
        x, y = R.gen(), R.gen(1)
        p2 = R(-2)*x**2 + R(-1)*x + R(1/2)*y + R(1/6)
        sphinx_plot(p2.tropical_variety().plot())

    When two tropical polynomials are multiplied, the tropical curve of
    the resulting polynomial is the union of the tropical curves of the
    original polynomials::

        sage: p3 = p1 * p2; p3
        (-2)*x^3 + (-2)*x^2*y + (-1)*x^2 + 1/2*x*y + 1/2*y^2 + 1/6*x + 1/2*y + 1/6
        sage: tv3 = p3.tropical_variety()
        sage: tv3.plot()
        Graphics object consisting of 11 graphics primitives

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=False)
        R = PolynomialRing(T, ('x,y'))
        x, y = R.gen(), R.gen(1)
        p1 = x + y + R(0)
        p2 = R(-2)*x**2 + R(-1)*x + R(1/2)*y + R(1/6)
        p3 = p1 * p2
        sphinx_plot(p3.tropical_variety().plot())
    """
    def vertices(self):
        """
        Return all vertices of ``self``, which is the point where three or
        more edges intersect.

        OUTPUT: a set of `(x,y)` points

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = x + y
            sage: p1.tropical_variety().vertices()
            set()
            sage: p2 = R(-2)*x^2 + R(-1)*x + R(1/2)*y + R(1/6)
            sage: p2.tropical_variety().vertices()
            {(1, -1/2), (7/6, -1/3)}
        """
    def weight_vectors(self):
        """
        Return the weight vectors for all vertices of ``self``.

        Weight vectors are a list of vectors associated with each vertex
        of the curve. Each vector corresponds to an edge emanating from
        that vertex and points in the direction of the edge.

        Suppose `v` is a vertex adjacent to the edges `e_1, \\ldots, e_k`
        with respective weights `w_1, \\ldots, w_k`. Every edge `e_i` is
        contained in a line (component) defined by an equation. Therefore,
        there exists a unique integer vector `v_i = (\\alpha, \\beta)` in
        the direction of `e_i` such that `\\gcd(\\alpha, \\beta)=1`. Then,
        each vertex `v` yield the vectors `w_1 v_1, \\ldots, w_k v_k`.
        These vectors will satisfy the following balancing condition:
        `\\sum_{i=1}^k w_i v_i = 0`.

        OUTPUT:

        A dictionary where the keys represent the vertices, and the values
        are lists of vectors.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = R(-2)*x^2 + R(-1)*x + R(1/2)*y + R(1/6)
            sage: p1.tropical_variety().weight_vectors()
            {(1, -1/2): [(0, 1), (-1, -2), (1, 1)],
             (7/6, -1/3): [(-1, -1), (0, 1), (1, 0)]}

            sage: p2 = R(2)*x^2 + x*y + R(2)*y^2 + x + R(-1)*y + R(3)
            sage: p2.tropical_variety().weight_vectors()
            {(-2, 0): [(-1, -1), (0, 1), (1, 0)],
             (-1, -3): [(-1, -1), (0, 1), (1, 0)],
             (-1, 0): [(-1, 0), (0, -1), (1, 1)],
             (3, 4): [(-1, -1), (0, 1), (1, 0)]}
        """
    def is_smooth(self):
        """
        Return ``True`` if ``self`` is smooth and ``False`` otherwise.

        Suppose `C` is a tropical curve of degree `d`. A tropical curve
        `C` is smooth if the dual subdivision of `C` consists of `d^2`
        triangles each having unit area `1/2`. This is equivalent with
        `C` having `d^2` vertices. These vertices are necessarily
        trivalent (has three adjacent edges).

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = x^2 + x + R(1)
            sage: p1.tropical_variety().is_smooth()
            False
            sage: p2 = R(2)*x^2 + x*y + R(2)*y^2 + x + R(-1)*y + R(3)
            sage: p2.tropical_variety().is_smooth()
            True
        """
    def is_simple(self):
        """
        Return ``True`` if ``self`` is simple and ``False`` otherwise.

        A tropical curve `C` is called simple if each vertex is either
        trivalent or is locally the intersection of two line segments.
        Equivalently, `C` is simple if the corresponding subdivision
        consists only of triangles and parallelograms.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = R(0) + x + y + x*y + x^2*y + x*y^2
            sage: p1.tropical_variety().is_simple()
            False
            sage: p2 = R(2)*x^2 + x*y + R(2)*y^2 + x + R(-1)*y + R(3)
            sage: p2.tropical_variety().is_simple()
            True
        """
    def genus(self):
        """
        Return the genus of ``self``.

        Let `t(C)` be the number of trivalent vertices, and let `r(C)` be
        the number of unbounded edges of `C`. The genus of simple tropical
        curve `C` is defined by the formula:

        .. MATH::

            g(C) = \\frac{1}{2}t(C) - \\frac{1}{2}r(C) + 1.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = x^2 + y^2 + x*y
            sage: p1.tropical_variety().genus()
            1
            sage: p2 = R(2)*x^2 + x*y + R(2)*y^2 + x + R(-1)*y + R(3)
            sage: p2.tropical_variety().genus()
            0

        TESTS::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = R(0) + y + x^2*y + x*y^2
            sage: p1.tropical_variety().genus()
            Traceback (most recent call last):
            ...
            ValueError: Tropical curve of 0*x^2*y + 0*x*y^2 + 0*y + 0 is not simple
        """
    def contribution(self):
        """
        Return the contribution of ``self``.

        The contribution of a simple curve `C` is defined as the product
        of the normalized areas of all triangles in the corresponding
        dual subdivision. We just multiply positive integers attached to
        the trivalent vertices. The contribution of a trivalent vertex
        equals `w_1w_2|\\det(v_1,v_2)|`, with `w_i` are the weights of
        the adjacent edges and `v_i` are their weight vectors. That
        formula is independent of the choice made because of the
        balancing condition `w_1v_1+w_2v_2+w_3v_3=0`.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = R(2)*x^2 + x*y + R(2)*y^2 + x + R(-1)*y + R(3)
            sage: p1.tropical_variety().contribution()
            1
            sage: p2 = R(-1/3)*x^2 + R(1)*x*y + R(1)*y^2 + R(-1/3)*x + R(1/3)
            sage: p2.tropical_variety().contribution()
            16

        TESTS::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = R(0) + x + x^2*y + x*y^2
            sage: p1.tropical_variety().contribution()
            Traceback (most recent call last):
            ...
            ValueError: Tropical curve of 0*x^2*y + 0*x*y^2 + 0*x + 0 is not simple
        """
    def plot(self):
        """
        Return the plot of ``self``.

        Generates a visual representation of the tropical curve in cartesian
        coordinates. The plot shows piecewise-linear segments representing
        each components. The axes are centered around the vertices.

        OUTPUT:

        A Graphics object. The weight of the component will be written if it
        is greater or equal than 2. The weight is written near the vertex.

        EXAMPLES:

        A polynomial with only two terms will give one straight line::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: (y+R(1)).tropical_variety().components()
            [[(t1, 1), [-Infinity < t1, t1 < +Infinity], 1]]
            sage: (y+R(1)).tropical_variety().plot()
            Graphics object consisting of 1 graphics primitive

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ)
            R = PolynomialRing(T, ('x,y'))
            x, y = R.gen(), R.gen(1)
            sphinx_plot((y+R(1)).tropical_variety().plot())

        An intriguing and fascinating tropical curve can be obtained with
        a more complex tropical polynomial::

            sage: p1 = R(1) + R(2)*x + R(3)*y + R(6)*x*y + R(10)*x*y^2
            sage: p1.tropical_variety().components()
            [[(-1, t1), [-2 <= t1], 1],
            [(t1, -2), [-1 <= t1], 1],
            [(t1 + 1, t1), [-4 <= t1, t1 <= -2], 1],
            [(t1, -4), [t1 <= -3], 2],
            [(-t1 - 7, t1), [t1 <= -4], 1]]
            sage: p1.tropical_variety().plot()
            Graphics object consisting of 6 graphics primitives

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ)
            R = PolynomialRing(T, ('x,y'))
            x, y = R.gen(), R.gen(1)
            p1 = R(1) + R(2)*x + R(3)*y + R(6)*x*y + R(10)*x*y**2
            sphinx_plot(p1.tropical_variety().plot())

        Another tropical polynomial with numerous components, resulting
        in a more intricate structure::

            sage: p2 = (x^6 + R(4)*x^4*y^2 + R(2)*x^3*y^3 + R(3)*x^2*y^4
            ....:       + x*y^5 + R(7)*x^2 + R(5)*x*y + R(3)*y^2 + R(2)*x
            ....:       + y + R(10))
            sage: p2.tropical_variety().plot() # long time
            Graphics object consisting of 11 graphics primitives

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ)
            R = PolynomialRing(T, ('x,y'))
            x, y = R.gen(), R.gen(1)
            p2 = (x**6 + R(4)*x**4*y**2 + R(2)*x**3*y**3 + R(3)*x**2*y**4
                  + x*y**5 + R(7)*x**2 + R(5)*x*y + R(3)*y**2 + R(2)*x
                  + y + R(10))
            sphinx_plot(p2.tropical_variety().plot())

        ::

            sage: p3 = (R(8) + R(4)*x + R(2)*y + R(1)*x^2 + x*y + R(1)*y^2
            ....:       + R(2)*x^3 + x^2*y + x*y^2 + R(4)*y^3 + R(8)*x^4
            ....:       + R(4)*x^3*y + x^2*y^2 + R(2)*x*y^3 + y^4)
            sage: p3.tropical_variety().plot() # long time
            Graphics object consisting of 23 graphics primitives

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ)
            R = PolynomialRing(T, ('x,y'))
            x, y = R.gen(), R.gen(1)
            p3 = (R(8) + R(4)*x + R(2)*y + R(1)*x**2 + x*y + R(1)*y**2
                 + R(2)*x**3 + x**2*y + x*y**2 + R(4)*y**3 + R(8)*x**4
                 + R(4)*x**3*y + x**2*y**2 + R(2)*x*y**3 + y**4)
            sphinx_plot(p3.tropical_variety().plot())
        """
