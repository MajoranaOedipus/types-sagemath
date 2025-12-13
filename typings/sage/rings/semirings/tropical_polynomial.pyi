from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.polynomial.polynomial_element_generic import Polynomial_generic_sparse as Polynomial_generic_sparse
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class TropicalPolynomial(Polynomial_generic_sparse):
    """
    A univariate tropical polynomial.

    A tropical polynomial is a polynomial whose coefficients come from
    a tropical semiring. Tropical polynomial induces a function which is
    piecewise linear, where each segment of the function has a non-negative
    integer slope. Tropical roots (zeros) of polynomial `P(x)` is defined
    as all points `x_0` for which the graph of `P(x)` change its slope.
    The difference in the slopes of the two pieces adjacent to this root
    gives the order of the root.

    The tropical polynomials are implemented with a sparse format by using
    a ``dict`` whose keys are the exponent and values the corresponding
    coefficients. Each coefficient is a tropical number.

    EXAMPLES:

    We construct a tropical polynomial semiring by defining a base
    tropical semiring and then inputting it to :class:`PolynomialRing`::

        sage: T = TropicalSemiring(QQ, use_min=False)
        sage: R.<x> = PolynomialRing(T); R
        Univariate Tropical Polynomial Semiring in x over Rational Field
        sage: R.0
        0*x

    One way to construct an element is to provide a list or tuple of
    coefficients. Another way to define an element is to write a polynomial
    equation with each coefficient converted to the semiring::

        sage: p1 = R([1,4,None,0]); p1
        0*x^3 + 4*x + 1
        sage: p2 = R(1)*x^2 + R(2)*x + R(3); p2
        1*x^2 + 2*x + 3

    We can do some basic arithmetic operations for these tropical polynomials.
    Remember that numbers given have to be in the tropical semiring.
    If not, then it will raise an error::

        sage: p1 + p2
        0*x^3 + 1*x^2 + 4*x + 3
        sage: p1 * p2
        1*x^5 + 2*x^4 + 5*x^3 + 6*x^2 + 7*x + 4
        sage: 2 * p1
        Traceback (most recent call last):
        ...
        ArithmeticError: cannot negate any non-infinite element
        sage: T(2) * p1
        2*x^3 + 6*x + 3
        sage: p1(3)
        Traceback (most recent call last):
        ...
        TypeError: no common canonical parent for objects with parents:
        'Tropical semiring over Rational Field' and 'Integer Ring'
        sage: p1(T(3))
        9

    We can find all tropical roots of a tropical polynomial, counted
    with their multiplicities::

        sage: p1.roots()
        [-3, 2, 2]
        sage: p2.roots()
        [1, 1]

    Even though every tropical polynomials have tropical roots, this does not
    necessarily means it can be factored into its linear factors::

        sage: p1.factor()
        (0) * (0*x^3 + 4*x + 1)
        sage: p2.factor()
        (1) * (0*x + 1)^2

    Every tropical polynomial `p(x)` have a corresponding unique tropical
    polynomial `\\bar{p}(x)` with the same roots that can be factored. We
    call `\\bar{p}(x)` the tropical polynomial split form of `p(x)`::

        sage: p1.split_form()
        0*x^3 + 2*x^2 + 4*x + 1
        sage: p2.split_form()
        1*x^2 + 2*x + 3

    Every tropical polynomial induce a piecewise linear function that can be
    invoked in the following way::

        sage: p1.piecewise_function()
        piecewise(x|-->1 on (-oo, -3], x|-->x + 4 on (-3, 2), x|-->3*x on [2, +oo); x)
        sage: p1.plot()
        Graphics object consisting of 1 graphics primitive

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=False)
        R = PolynomialRing(T, 'x')
        p1 = R([1,4,None,0])
        sphinx_plot(p1.plot())

    ::

        sage: p2.piecewise_function()
        piecewise(x|-->3 on (-oo, 1], x|-->2*x + 1 on (1, +oo); x)
        sage: p2.plot()
        Graphics object consisting of 1 graphics primitive

    .. PLOT::
        :width: 300 px

        T = TropicalSemiring(QQ, use_min=False)
        R = PolynomialRing(T, 'x')
        x = R.gen()
        p2 = R(1)*x**2 + R(2)*x + R(3)
        sphinx_plot(plot(p2, xmin=-1, xmax=3))

    TESTS:

    There is no subtraction for tropical polynomials because element in
    tropical semiring doesn't necessarily have additive inverse::

        sage: -p1
        Traceback (most recent call last):
        ...
        ArithmeticError: cannot negate any non-infinite element
    """
    def roots(self):
        """
        Return the list of all tropical roots of ``self``, counted with
        multiplicity.

        OUTPUT: a list of tropical numbers

        ALGORITHM:

        For each pair of monomials in the polynomial, we find the point
        where their values are equal.  This is the same as solving the
        equation `c_1 + a_1 \\cdot x = c_2 + a_2 \\cdot x` for `x`, where
        `(c_1, a_1)` and `(c_2, a_2)` are the coefficients and exponents
        of monomials.

        The solution to this equation is `x = (c_2-c_1)/(a_1-a_2)`. We
        substitute this `x` to each monomials in polynomial and check if
        the maximum (minimum) is achieved by the previous two monomials.
        If it is, then `x` is the root of tropical polynomial. In this
        case, the order of the root at `x` is the maximum of `|i-j|` for
        all possible pairs `i,j` which realise this maximum (minimum).

        EXAMPLES::

            sage: T = TropicalSemiring(QQ, use_min=True)
            sage: R.<x> = PolynomialRing(T)
            sage: p1 = R([5,4,1,0,2,4,3]); p1
            3*x^6 + 4*x^5 + 2*x^4 + 0*x^3 + 1*x^2 + 4*x + 5
            sage: p1.roots()
            [-1, -1, -1, 1, 2, 2]

        There will be no tropical root for constant polynomial. Additionaly,
        for a monomial, the tropical root is assumed to be the additive
        identity of its base tropical semiring::

            sage: p2 = R(2)
            sage: p2.roots()
            []
            sage: p3 = x^3
            sage: p3.roots()
            [+infinity, +infinity, +infinity]
        """
    def split_form(self):
        """
        Return the tropical polynomial which has the same roots as ``self``
        but which can be reduced to its linear factors.

        If a tropical polynomial has roots at `x_1, x_2, \\ldots, x_n`, then
        its split form is the tropical product of linear terms of the form
        `(x + x_i)` for all `i=1,2,\\ldots,n`.

        OUTPUT: :class:`TropicalPolynomial`

        EXAMPLES::

            sage: T = TropicalSemiring(QQ, use_min=True)
            sage: R.<x> = PolynomialRing(T)
            sage: p1 = R([5,4,1,0,2,4,3]); p1
            3*x^6 + 4*x^5 + 2*x^4 + 0*x^3 + 1*x^2 + 4*x + 5
            sage: p1.split_form()
            3*x^6 + 2*x^5 + 1*x^4 + 0*x^3 + 1*x^2 + 3*x + 5

        ::

            sage: T = TropicalSemiring(QQ, use_min=False)
            sage: R.<x> = PolynomialRing(T)
            sage: p1 = R([5,4,1,0,2,4,3])
            sage: p1.split_form()
            3*x^6 + 4*x^5 + 21/5*x^4 + 22/5*x^3 + 23/5*x^2 + 24/5*x + 5

        TESTS:

        We verify that the roots of tropical polynomial and its split form
        is really the same::

            sage: p1.roots() == p1.split_form().roots()
            True
        """
    def factor(self):
        """
        Return the factorization of ``self`` into its tropical linear factors.

        Note that the factor `x - x_0` in classical algebra gets transformed
        to the factor `x + x_0`, since the root of the tropical polynomial
        `x + x_0` is `x_0` and not `-x_0`. However, not every tropical
        polynomial can be factored.

        OUTPUT: :class:'Factorization'

        EXAMPLES::

            sage: T = TropicalSemiring(QQ, use_min=True)
            sage: R.<x> = PolynomialRing(T)
            sage: p1 = R([6,3,1,0]); p1
            0*x^3 + 1*x^2 + 3*x + 6
            sage: factor(p1)
            (0) * (0*x + 1) * (0*x + 2) * (0*x + 3)

        Such factorization is not always possible::

            sage: p2 = R([4,4,2]); p2
            2*x^2 + 4*x + 4
            sage: p2.factor()
            (2) * (0*x^2 + 2*x + 2)

        TESTS:

        The factorization for a constant::

            sage: p3 = R(3)
            sage: p3.factor()
            (3) * 0
        """
    def piecewise_function(self):
        """
        Return the tropical polynomial function of ``self``.

        The function is a piecewise linear function with the domains are
        divided by the roots. First we convert each term of polynomial to
        its corresponding linear function. Next, we must determine which
        term achieves the minimum (maximum) at each interval.

        OUTPUT: a piecewise function

        EXAMPLES::

            sage: T = TropicalSemiring(QQ, use_min=False)
            sage: R.<x> = PolynomialRing(T)
            sage: p1 = R([4,2,1,3]); p1
            3*x^3 + 1*x^2 + 2*x + 4
            sage: p1.piecewise_function()
            piecewise(x|-->4 on (-oo, 1/3], x|-->3*x + 3 on (1/3, +oo); x)

        A constant tropical polynomial will result in a constant function::

            sage: p2 = R(3)
            sage: p2.piecewise_function()
            3

        A monomial will resulted in a linear function::

            sage: p3 = R(1)*x^3
            sage: p3.piecewise_function()
            3*x + 1
        """
    def plot(self, xmin=None, xmax=None):
        """
        Return the plot of ``self``, which is the tropical polynomial
        function we get from ``self.piecewise_function()``.

        INPUT:

        - ``xmin`` -- (optional) real number
        - ``xmax`` -- (optional) real number

        OUTPUT:

        If ``xmin`` and ``xmax`` is given, then it return a plot of
        piecewise linear function of ``self`` with the axes start from
        ``xmin`` to ``xmax``. Otherwise, the domain will start from the
        the minimum root of ``self`` minus 1 to maximum root of ``self``
        plus 1. If the function of ``self`` is constant or linear, then
        the default domain will be `[-1,1]`.

        EXAMPLES:

        If the tropical semiring use a max-plus algebra, then the graph
        will be of piecewise linear convex function::

            sage: T = TropicalSemiring(QQ, use_min=False)
            sage: R.<x> = PolynomialRing(T)
            sage: p1 = R([4,2,1,3]); p1
            3*x^3 + 1*x^2 + 2*x + 4
            sage: p1.roots()
            [1/3, 1/3, 1/3]
            sage: p1.plot()
            Graphics object consisting of 1 graphics primitive

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ, use_min=False)
            R = PolynomialRing(T, 'x')
            p1 = R([4,2,1,3])
            sphinx_plot(p1.plot())

        A different result will be obtained if the tropical semiring employs
        a min-plus algebra. Rather, a graph of the piecewise linear concave
        function will be obtained::

            sage: T = TropicalSemiring(QQ, use_min=True)
            sage: R.<x> = PolynomialRing(T)
            sage: p1 = R([4,2,1,3])
            sage: p1.roots()
            [-2, 1, 2]
            sage: p1.plot()
            Graphics object consisting of 1 graphics primitive

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ, use_min=True)
            R = PolynomialRing(T, 'x')
            p1 = R([4,2,1,3])
            sphinx_plot(p1.plot())

        TESTS:

        If ``xmin`` or ``xmax`` is given as an input, then the others also
        have to be given. Otherwise it will raise an error::

            sage: plot(p1, 5)
            Traceback (most recent call last):
            ...
            ValueError: expected 2 inputs for xmin and xmax, but got 1

        Error also occurred when ``xmin`` is greater or equal than``xmax``::

            sage: plot(p1, 5, 3)
            Traceback (most recent call last):
            ...
            ValueError: xmin = 5 should be less than xmax = 3
        """

class TropicalPolynomialSemiring(UniqueRepresentation, Parent):
    """
    The semiring of univariate tropical polynomials.

    This is the commutative semiring consisting of finite linear
    combinations of tropical monomials under (tropical)
    addition and multiplication with the identity element
    being `+\\infty` (or `-\\infty` depending on whether the
    base tropical semiring is using min-plus or max-plus algebra).

    EXAMPLES::

        sage: T = TropicalSemiring(QQ)
        sage: R.<x> = PolynomialRing(T)
        sage: f = T(1)*x
        sage: g = T(2)*x
        sage: f + g
        1*x
        sage: f * g
        3*x^2
        sage: f + R.zero() == f
        True
        sage: f * R.zero() == R.zero()
        True
        sage: f * R.one() == f
        True
    """
    @staticmethod
    def __classcall_private__(cls, base_semiring, names):
        """
        Ensures the names parameter is a tuple.

        EXAMPLES::

            sage: from sage.rings.semirings.tropical_polynomial import TropicalPolynomialSemiring
            sage: T = TropicalSemiring(ZZ)
            sage: TPS = TropicalPolynomialSemiring
            sage: TPS(T, 'x') == TPS(T, ('x'))
            True
        """
    def __init__(self, base_semiring, names) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R = PolynomialRing(T, 'x')
            sage: TestSuite(R).run()

        TESTS::

            sage: from sage.rings.semirings.tropical_polynomial import TropicalPolynomialSemiring
            sage: TropicalPolynomialSemiring(ZZ, names='x')
            Traceback (most recent call last):
            ...
            ValueError: Integer Ring is not a tropical semiring
        """
    Element = TropicalPolynomial
    @cached_method
    def one(self):
        """
        Return the multiplicative identity of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R = PolynomialRing(T, 'x')
            sage: R.one()
            0
        """
    @cached_method
    def zero(self):
        """
        Return the additive identity of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R = PolynomialRing(T, 'x')
            sage: R.zero()
            +infinity
        """
    def gen(self, n: int = 0):
        """
        Return the indeterminate generator of ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<abc> = PolynomialRing(T)
            sage: R.gen()
            0*abc

        TESTS::

            sage: R.gen(2)
            Traceback (most recent call last):
            ...
            IndexError: generator n not defined
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators for ``self``.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R.<abc> = PolynomialRing(T)
            sage: R.gens()
            (0*abc,)
        """
    def ngens(self):
        """
        Return the number of generators of ``self``, which is 1
        since it is a univariate polynomial ring.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R = PolynomialRing(T, 'x')
            sage: R.ngens()
            1
        """
    def random_element(self, degree=(-1, 2), monic: bool = False, *args, **kwds):
        """
        Return a random tropical polynomial of given degrees (bounds).

        OUTPUT: :class:`TropicalPolynomial`

        .. SEEALSO::

            :meth:`sage.rings.polynomial.polynomial_ring.PolynomialRing_generic.random_element`

        EXAMPLES:

        Tropical polynomial over an integer with each coefficient bounded
        between ``x`` and ``y``::

            sage: T = TropicalSemiring(ZZ)
            sage: R = PolynomialRing(T, 'x')
            sage: f = R.random_element(8, x=3, y=10)
            sage: f.degree()
            8
            sage: f.parent() is R
            True
            sage: all(a >= T(3) for a in f.coefficients())
            True
            sage: all(a < T(10) for a in f.coefficients())
            True

        If a tuple of two integers is provided for the ``degree`` argument,
        a polynomial is selected with degrees within that range::

            sage: all(R.random_element(degree=(1, 5)).degree() in range(1, 6) for _ in range(10^3))
            True

        Note that the zero polynomial (`\\pm \\infty`) has degree `-1`.
        To include it, set the minimum degree to `-1`::

            sage: while R.random_element(degree=(-1,2), x=-1, y=1) != R.zero():
            ....:     pass

        Monic polynomials are chosen among all monic polynomials with degree
        between the given ``degree`` argument::

            sage: all(R.random_element(degree=(-1, 2), monic=True).is_monic() for _ in range(10^3))
            True
        """
    def is_sparse(self):
        """
        Return ``True`` to indicate that the objects are sparse polynomials.

        EXAMPLES::

            sage: T = TropicalSemiring(QQ)
            sage: R = PolynomialRing(T, 'x')
            sage: R.is_sparse()
            True
        """
    def interpolation(self, points):
        """
        Return a tropical polynomial with its function is a linear
        interpolation of point in ``points`` if possible.

        If there is only one point, then it will give a constant polynomial.
        Because we are using linear interpolation, each point is actually
        a root of the resulted tropical polynomial.

        INPUT:

        - ``points`` -- a list of tuples ``(x, y)``

        OUTPUT: :class:`TropicalPolynomial`

        EXAMPLES::

            sage: T = TropicalSemiring(QQ, use_min=True)
            sage: R = PolynomialRing(T, 'x')
            sage: points = [(-2,-3),(1,3),(2,4)]
            sage: p1 = R.interpolation(points); p1
            1*x^2 + 2*x + 4
            sage: p1.plot()
            Graphics object consisting of 1 graphics primitive

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ, use_min=True)
            R = PolynomialRing(T, 'x')
            points = [(-2,-3),(1,3),(2,4)]
            p1 = R.interpolation(points)
            sphinx_plot(p1.plot())

        ::

            sage: T = TropicalSemiring(QQ, use_min=False)
            sage: R = PolynomialRing(T,'x')
            sage: points = [(0,0),(1,1),(2,4)]
            sage: p1 = R.interpolation(points); p1
            (-2)*x^3 + (-1)*x^2 + 0*x + 0
            sage: p1.plot()
            Graphics object consisting of 1 graphics primitive

        .. PLOT::
            :width: 300 px

            T = TropicalSemiring(QQ, use_min=False)
            R = PolynomialRing(T, 'x')
            points = [(0,0),(1,1),(2,4)]
            p1 = R.interpolation(points)
            sphinx_plot(p1.plot())

        TESTS:

        Every piecewise linear component of tropical polynomial function
        has to have an integer slope::

            sage: T = TropicalSemiring(QQ, use_min=False)
            sage: R = PolynomialRing(T,'x')
            sage: points = [(0,0),(2,3)]
            sage: R.interpolation(points)
            Traceback (most recent call last):
            ...
            ValueError: the slope is not an integer

        For max-plus algebra, the slope of the components has to be
        increasing as we move from left to right. Conversely for min-plus
        algebra, the slope of the components has to be decreasing from
        left to right::

            sage: T = TropicalSemiring(QQ, use_min=False)
            sage: R = PolynomialRing(T,'x')
            sage: points = [(-2,-3),(1,3),(2,4)]
            sage: R.interpolation(points)
            Traceback (most recent call last):
            ...
            ValueError: can not interpolate these points
        """
