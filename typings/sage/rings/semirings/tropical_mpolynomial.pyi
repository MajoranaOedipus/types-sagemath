from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.polynomial.multi_polynomial_element import MPolynomial_polydict as MPolynomial_polydict
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class TropicalMPolynomial(MPolynomial_polydict):
    """
    A multivariate tropical polynomial.

    Let `x_1, x_2, \\ldots, x_n` be indeterminants. A tropical monomial is
    any product of these variables, possibly including repetitions:
    `x_1^{i_1}\\cdots x_n^{i_n}` where `i_j \\in \\{0,1,\\ldots\\}`, for all
    `j\\in \\{1,\\ldots,n\\}`. A multivariate tropical polynomial is a finite
    linear combination of tropical monomials,
    `p(x_1, \\ldots, x_n) = \\sum_{i=1}^n c_i x_1^{i_1}\\cdots x_n^{i_n}`.

    In classical arithmetic, we can rewrite the general form of a tropical
    monomial: `x_1^{i_1}\\cdots x_n^{i_n} \\mapsto i_1 x_1 + \\cdots + i_n x_n`.
    Thus, the tropical polynomial can be viewed as the minimum (maximum) of
    a finite collection of linear functions.

    EXAMPLES:

    Construct a multivariate tropical polynomial semiring in two variables::

        sage: T = TropicalSemiring(QQ, use_min=False)
        sage: R.<a,b> = PolynomialRing(T); R
        Multivariate Tropical Polynomial Semiring in a, b over Rational Field

    Define some multivariate tropical polynomials::

        sage: p1 = R(3)*a*b + a + R(-1)*b; p1
        3*a*b + 0*a + (-1)*b
        sage: p2 = R(1)*a + R(1)*b + R(1)*a*b; p2
        1*a*b + 1*a + 1*b

    Some basic arithmetic operations for multivariate tropical polynomials::

        sage: p1 + p2
        3*a*b + 1*a + 1*b
        sage: p1 * p2
        4*a^2*b^2 + 4*a^2*b + 4*a*b^2 + 1*a^2 + 1*a*b + 0*b^2
        sage: T(2) * p1
        5*a*b + 2*a + 1*b
        sage: p1(T(1),T(2))
        6

    Let us look at the different result for tropical curve and 3d graph
    of tropical polynomial in two variables when different algebra is used.
    First for the min-plus algebra::

        sage: T = TropicalSemiring(QQ, use_min=True)
        sage: R.<a,b> = PolynomialRing(T)
        sage: p1 = R(3)*a*b + a + R(-1)*b
        sage: p1.tropical_variety()
        Tropical curve of 3*a*b + 0*a + (-1)*b
        sage: p1.tropical_variety().plot()
        Graphics object consisting of 3 graphics primitives

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=True)
        R = PolynomialRing(T, ('a,b'))
        a, b = R.gen(), R.gen(1)
        p1 = R(3)*a*b + a + R(-1)*b
        tv1 = p1.tropical_variety()
        sphinx_plot(tv1.plot())

    Tropical polynomial in two variables will induce a function in three
    dimension that consists of a number of surfaces::

        sage: p1.plot3d()
        Graphics3d Object

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=True)
        R = PolynomialRing(T, ('a,b'))
        a, b = R.gen(), R.gen(1)
        p1 = R(3)*a*b + a + R(-1)*b
        sphinx_plot(p1.plot3d())

    If we use a max-plus algebra, we will get a slightly different result::

        sage: T = TropicalSemiring(QQ, use_min=False)
        sage: R.<a,b> = PolynomialRing(T)
        sage: p1 = R(3)*a*b + a + R(-1)*b
        sage: p1.tropical_variety()
        Tropical curve of 3*a*b + 0*a + (-1)*b
        sage: p1.tropical_variety().plot()
        Graphics object consisting of 3 graphics primitives

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=False)
        R = PolynomialRing(T, ('a,b'))
        a, b = R.gen(), R.gen(1)
        p1 = R(3)*a*b + a + R(-1)*b
        tv1 = p1.tropical_variety()
        sphinx_plot(tv1.plot())

    ::

        sage: p1.plot3d()
        Graphics3d Object

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=False)
        R = PolynomialRing(T, ('a,b'))
        a, b = R.gen(), R.gen(1)
        p1 = R(3)*a*b + a + R(-1)*b
        sphinx_plot(p1.plot3d())

    Another way to represent tropical curve is through dual subdivision,
    which is a subdivision of Newton polytope of tropical polynomial::

        sage: p1.newton_polytope()
        A 2-dimensional polyhedron in ZZ^2 defined as the convex hull of 3 vertices
        sage: p1.dual_subdivision()
        Polyhedral complex with 1 maximal cell

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=False)
        R = PolynomialRing(T, ('a,b'))
        a, b = R.gen(), R.gen(1)
        p1 = R(3)*a*b + a + R(-1)*b
        sphinx_plot(p1.dual_subdivision().plot())

    TESTS:

    There is no subtraction defined for tropical polynomials::

        sage: T = TropicalSemiring(QQ)
        sage: R.<a,b> = PolynomialRing(T)
        sage: a - b
        Traceback (most recent call last):
        ...
        ArithmeticError: cannot negate any non-infinite element
    """
    def subs(self, fixed=None, **kwds):
        """
        Fix some given variables in ``self`` and return the changed
        tropical multivariate polynomials.

        .. SEEALSO::

            :meth:`sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict.subs`

        EXAMPLES::

            sage: T = TropicalSemiring(QQ, use_min=False)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = x^2 + y + R(3)
            sage: p1((R(4),y))
            0*y + 8
            sage: p1.subs({x: 4})
            0*y + 8
        """
    def plot3d(self, color: str = 'random'):
        """
        Return the 3d plot of ``self``.

        Only implemented for tropical polynomial in two variables.
        The `x`-`y` axes for this 3d plot is the same as the `x`-`y`
        axes of the corresponding tropical curve.

        OUTPUT: Graphics3d Object

        EXAMPLES:

        A simple tropical polynomial that consist of only one surface::

            sage: T = TropicalSemiring(QQ, use_min=False)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = x^2
            sage: p1.plot3d()
            Graphics3d Object

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ, use_min=False)
            R = PolynomialRing(T, ('x,y'))
            x, y = R.gen(), R.gen(1)
            p1 = x**2
            sphinx_plot(p1.plot3d())

        Tropical polynomials often have graphs that represent a combination
        of multiple surfaces::

            sage: p2 = R(3) + R(2)*x + R(2)*y + R(3)*x*y
            sage: p2.plot3d()
            Graphics3d Object

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ, use_min=False)
            R = PolynomialRing(T, ('x,y'))
            x, y = R.gen(), R.gen(1)
            p2 = R(3) + R(2)*x + R(2)*y + R(3)*x*y
            sphinx_plot(p2.plot3d())

        ::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p3 = R(2)*x^2 + x*y + R(2)*y^2 + x + R(-1)*y + R(3)
            sage: p3.plot3d()
            Graphics3d Object

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ)
            R = PolynomialRing(T, ('x,y'))
            x, y = R.gen(), R.gen(1)
            p3 = R(2)*x**2 + x*y + R(2)*y**2 + x + R(-1)*y + R(3)
            sphinx_plot(p3.plot3d())

        TESTS::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y,z> = PolynomialRing(T)
            sage: p1 = x*y*z + x
            sage: p1.plot3d()
            Traceback (most recent call last):
            ...
            NotImplementedError: can only plot the graph of tropical
            multivariate polynomial in two variables
        """
    def tropical_variety(self):
        """
        Return tropical roots of ``self``.

        In the multivariate case, the roots can be represented by a
        tropical variety. In two dimensions, this is known as a tropical
        curve. For dimensions higher than two, it is referred to as a
        tropical hypersurface.

        OUTPUT: :class:`sage.rings.semirings.tropical_variety.TropicalVariety`

        EXAMPLES:

        Tropical curve for tropical polynomials in two variables::

            sage: T = TropicalSemiring(QQ, use_min=False)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = x + y + R(0); p1
            0*x + 0*y + 0
            sage: p1.tropical_variety()
            Tropical curve of 0*x + 0*y + 0

        Tropical hypersurface for tropical polynomials in more than two
        variables::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y,z> = PolynomialRing(T)
            sage: p1 = R(1)*x*y + R(-1/2)*x*z + R(4)*z^2; p1
            1*x*y + (-1/2)*x*z + 4*z^2
            sage: p1.tropical_variety()
            Tropical surface of 1*x*y + (-1/2)*x*z + 4*z^2
        """
    def newton_polytope(self):
        """
        Return the Newton polytope of ``self``.

        The Newton polytope is the convex hull of all the points
        corresponding to the exponents of the monomials of tropical
        polynomial.

        OUTPUT: :func:`~sage.geometry.polyhedron.constructor.Polyhedron`

        EXAMPLES:

        A Newton polytope for a two-variable tropical polynomial::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = x + y
            sage: p1.newton_polytope()
            A 1-dimensional polyhedron in ZZ^2 defined as the convex hull of 2 vertices
            sage: p1.newton_polytope().Vrepresentation()
            (A vertex at (0, 1), A vertex at (1, 0))
            sage: p1.newton_polytope().Hrepresentation()
            (An equation (1, 1) x - 1 == 0,
             An inequality (0, -1) x + 1 >= 0,
             An inequality (0, 1) x + 0 >= 0)

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ)
            R = PolynomialRing(T, ('x,y'))
            x, y = R.gen(), R.gen(1)
            p1 = x + y
            sphinx_plot(p1.newton_polytope().plot())

        A Newton polytope in three dimension::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y,z> = PolynomialRing(T)
            sage: p1 = x^2 + x*y*z + x + y + z + R(0)
            sage: p1.newton_polytope()
            A 3-dimensional polyhedron in ZZ^3 defined as the convex hull of 5 vertices
            sage: p1.newton_polytope().Vrepresentation()
            (A vertex at (0, 0, 0),
            A vertex at (0, 0, 1),
            A vertex at (0, 1, 0),
            A vertex at (2, 0, 0),
            A vertex at (1, 1, 1))
            sage: p1.newton_polytope().Hrepresentation()
            (An inequality (0, 1, 0) x + 0 >= 0,
             An inequality (0, 0, 1) x + 0 >= 0,
             An inequality (1, 0, 0) x + 0 >= 0,
             An inequality (1, -1, -1) x + 1 >= 0,
             An inequality (-1, -2, 1) x + 2 >= 0,
             An inequality (-1, 1, -2) x + 2 >= 0)

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ)
            R = PolynomialRing(T, ('x,y,z'))
            x, y, z = R.gen(), R.gen(1), R.gen(2)
            p1 = x**2 + x*y*z + x + y + z + R(0)
            sphinx_plot(p1.newton_polytope().plot())
        """
    def dual_subdivision(self):
        '''
        Return the dual subdivision of ``self``.

        Dual subdivision refers to a specific decomposition of the
        Newton polytope of a tropical polynomial. The term "dual" is
        used in the sense that the combinatorial structure of the
        tropical variety is reflected in the dual subdivision.
        Specifically, vertices of the dual subdivision correspond to
        the intersection of multiple components. Edges of the dual
        subdivision correspond to the individual components.

        OUTPUT: :class:`~sage.geometry.polyhedral_complex.PolyhedralComplex`

        EXAMPLES:

        Dual subdivision of a tropical curve::

            sage: T = TropicalSemiring(QQ, use_min=False)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p1 = R(3) + R(2)*x + R(2)*y + R(3)*x*y + x^2 + y^2
            sage: pc = p1.dual_subdivision(); pc
            Polyhedral complex with 4 maximal cells
            sage: [p.Vrepresentation() for p in pc.maximal_cells_sorted()]
            [(A vertex at (0, 0), A vertex at (0, 1), A vertex at (1, 1)),
             (A vertex at (0, 0), A vertex at (1, 0), A vertex at (1, 1)),
             (A vertex at (0, 1), A vertex at (0, 2), A vertex at (1, 1)),
             (A vertex at (1, 0), A vertex at (1, 1), A vertex at (2, 0))]

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ,  use_min=False)
            R = PolynomialRing(T, (\'x,y\'))
            x, y = R.gen(), R.gen(1)
            p1 = R(3) + R(2)*x + R(2)*y + R(3)*x*y + x**2 + y**2
            sphinx_plot(p1.dual_subdivision().plot())

        A subdivision of a pentagonal Newton polytope::

            sage: p2 = R(3) + x^2 + R(-2)*y + R(1/2)*x^2*y + R(2)*x*y^3 + R(-1)*x^3*y^4
            sage: pc = p2.dual_subdivision(); pc
            Polyhedral complex with 5 maximal cells
            sage: [p.Vrepresentation() for p in pc.maximal_cells_sorted()]
            [(A vertex at (0, 0), A vertex at (0, 1), A vertex at (1, 3)),
             (A vertex at (0, 0), A vertex at (1, 3), A vertex at (2, 1)),
             (A vertex at (0, 0), A vertex at (2, 0), A vertex at (2, 1)),
             (A vertex at (1, 3), A vertex at (2, 1), A vertex at (3, 4)),
             (A vertex at (2, 0), A vertex at (2, 1), A vertex at (3, 4))]

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ,  use_min=False)
            R = PolynomialRing(T, (\'x,y\'))
            x, y = R.gen(), R.gen(1)
            p2 = R(3) + x**2 + R(-2)*y + R(1/2)*x**2*y + R(2)*x*y**3 + R(-1)*x**3*y**4
            sphinx_plot(p2.dual_subdivision().plot())

        A subdivision with many faces, not all of which are triangles::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y> = PolynomialRing(T)
            sage: p3 = (R(8) + R(4)*x + R(2)*y + R(1)*x^2 + x*y + R(1)*y^2
            ....:      + R(2)*x^3 + x^2*y + x*y^2 + R(4)*y^3 + R(8)*x^4
            ....:      + R(4)*x^3*y + x^2*y^2 + R(2)*x*y^3 + y^4)
            sage: pc = p3.dual_subdivision(); pc
            Polyhedral complex with 10 maximal cells
            sage: [p.Vrepresentation() for p in pc.maximal_cells_sorted()]
            [(A vertex at (0, 0), A vertex at (0, 1), A vertex at (1, 0)),
             (A vertex at (0, 1), A vertex at (0, 2), A vertex at (1, 1)),
             (A vertex at (0, 1), A vertex at (1, 0), A vertex at (2, 0)),
             (A vertex at (0, 1), A vertex at (1, 1), A vertex at (2, 0)),
             (A vertex at (0, 2), A vertex at (0, 4), A vertex at (1, 1)),
             (A vertex at (0, 4),
              A vertex at (1, 1),
              A vertex at (2, 1),
              A vertex at (2, 2)),
             (A vertex at (1, 1), A vertex at (2, 0), A vertex at (2, 1)),
             (A vertex at (2, 0), A vertex at (2, 1), A vertex at (3, 0)),
             (A vertex at (2, 1), A vertex at (2, 2), A vertex at (3, 0)),
             (A vertex at (2, 2), A vertex at (3, 0), A vertex at (4, 0))]

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ)
            R = PolynomialRing(T, (\'x,y\'))
            x, y = R.gen(), R.gen(1)
            p3 = (R(8) + R(4)*x + R(2)*y + R(1)*x**2 + x*y + R(1)*y**2
                  + R(2)*x**3 + x**2*y + x*y**2 + R(4)*y**3 + R(8)*x**4
                  + R(4)*x**3*y + x**2*y**2 + R(2)*x*y**3 + y**4)
            sphinx_plot(p3.dual_subdivision().plot())

        Dual subdivision of a tropical surface::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y,z> = PolynomialRing(T)
            sage: p1 = x + y + z + x^2 + R(1)
            sage: pc = p1.dual_subdivision(); pc
            Polyhedral complex with 7 maximal cells
            sage: [p.Vrepresentation() for p in pc.maximal_cells_sorted()]
            [(A vertex at (0, 0, 0), A vertex at (0, 0, 1), A vertex at (0, 1, 0)),
             (A vertex at (0, 0, 0), A vertex at (0, 0, 1), A vertex at (1, 0, 0)),
             (A vertex at (0, 0, 0), A vertex at (0, 1, 0), A vertex at (1, 0, 0)),
             (A vertex at (0, 0, 1), A vertex at (0, 1, 0), A vertex at (1, 0, 0)),
             (A vertex at (0, 0, 1), A vertex at (0, 1, 0), A vertex at (2, 0, 0)),
             (A vertex at (0, 0, 1), A vertex at (1, 0, 0), A vertex at (2, 0, 0)),
             (A vertex at (0, 1, 0), A vertex at (1, 0, 0), A vertex at (2, 0, 0))]

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ,  use_min=False)
            R = PolynomialRing(T, (\'x,y,z\'))
            x, y, z = R.gen(), R.gen(1), R.gen(2)
            p1 = x + y + z + x**2 + R(1)
            sphinx_plot(p1.dual_subdivision().plot())

        Dual subdivision of a tropical hypersurface::

            sage: T = TropicalSemiring(QQ)
            sage: R.<a,b,c,d> = PolynomialRing(T)
            sage: p1 = R(2)*a*b + R(3)*a*c + R(-1)*c^2 + R(-1/3)*a*d
            sage: pc = p1.dual_subdivision(); pc
            Polyhedral complex with 4 maximal cells
            sage: [p.Vrepresentation() for p in pc.maximal_cells_sorted()]
            [(A vertex at (0, 0, 2, 0),
             A vertex at (1, 0, 0, 1),
             A vertex at (1, 0, 1, 0)),
            (A vertex at (0, 0, 2, 0),
             A vertex at (1, 0, 0, 1),
             A vertex at (1, 1, 0, 0)),
            (A vertex at (0, 0, 2, 0),
             A vertex at (1, 0, 1, 0),
             A vertex at (1, 1, 0, 0)),
            (A vertex at (1, 0, 0, 1),
             A vertex at (1, 0, 1, 0),
             A vertex at (1, 1, 0, 0))]
        '''

class TropicalMPolynomialSemiring(UniqueRepresentation, Parent):
    """
    The semiring of tropical polynomials in multiple variables.

    This is the commutative semiring consisting of all finite linear
    combinations of tropical monomials under (tropical) addition
    and multiplication with coefficients in a tropical semiring.

    EXAMPLES::

        sage: T = TropicalSemiring(QQ)
        sage: R.<x,y> = PolynomialRing(T)
        sage: f = T(1)*x + T(-1)*y
        sage: g = T(2)*x + T(-2)*y
        sage: f + g
        1*x + (-2)*y
        sage: f * g
        3*x^2 + (-1)*x*y + (-3)*y^2
        sage: f + R.zero() == f
        True
        sage: f * R.zero() == R.zero()
        True
        sage: f * R.one() == f
        True
    """
    def __init__(self, base_semiring, n, names, order) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R = PolynomialRing(T, 5, 'x')
            sage: TestSuite(R).run()
        """
    def term_order(self):
        """
        Return the defined term order of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<x,y,z> = PolynomialRing(T)
            sage: R.term_order()
            Degree reverse lexicographic term order
        """
    Element = TropicalMPolynomial
    @cached_method
    def one(self):
        """
        Return the multiplicative identity of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R = PolynomialRing(T, 'x,y')
            sage: R.one()
            0
        """
    @cached_method
    def zero(self):
        """
        Return the additive identity of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R = PolynomialRing(T, 'x,y')
            sage: R.zero()
            +infinity
        """
    def random_element(self, degree: int = 2, terms=None, choose_degree: bool = False, *args, **kwargs):
        """
        Return a random multivariate tropical polynomial from ``self``.

        OUTPUT: :class:`TropicalMPolynomial`

        .. SEEALSO::

            :meth:`sage.rings.polynomial.multi_polynomial_ring_base.MPolynomialRing_base.random_element`

        EXAMPLES:

        A random polynomial of at most degree `d` and at most `t` terms::

            sage: T = TropicalSemiring(QQ)
            sage: R.<a,b,c> = PolynomialRing(T)
            sage: f = R.random_element(2, 5)
            sage: f.degree() <= 2
            True
            sage: f.parent() is R
            True
            sage: len(list(f)) <= 5
            True

        Choose degrees of monomials randomly first rather than monomials
        uniformly random::

            sage: f = R.random_element(3, 6, choose_degree=True)
            sage: f.degree() <= 3
            True
            sage: f.parent() is R
            True
            sage: len(list(f)) <= 6
            True
        """
    def gen(self, n: int = 0):
        """
        Return the ``n``-th generator of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<a,b,c> = PolynomialRing(T)
            sage: R.gen()
            0*a
            sage: R.gen(2)
            0*c

        TESTS::

            sage: R.gen(3)
            Traceback (most recent call last):
            ...
            IndexError: tuple index out of range
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R = PolynomialRing(T, 5, 'x')
            sage: R.gens()
            (0*x0, 0*x1, 0*x2, 0*x3, 0*x4)
        """
    def ngens(self):
        """
        Return the number of generators of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R = PolynomialRing(T, 10, 'z')
            sage: R.ngens()
            10
        """
