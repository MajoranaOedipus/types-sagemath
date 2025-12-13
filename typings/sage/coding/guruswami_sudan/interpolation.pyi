from sage.arith.misc import binomial as binomial
from sage.matrix.constructor import matrix as matrix
from sage.misc.misc_c import prod as prod

def gs_interpolation_linalg(points, tau, parameters, wy):
    """
    Compute an interpolation polynomial `Q(x,y)` for the Guruswami-Sudan algorithm
    by solving a linear system of equations.

    `Q` is a bivariate polynomial over the field of the points, such that the
    polynomial has a zero of multiplicity at least `s` at each of the points,
    where `s` is the multiplicity parameter. Furthermore, its ``(1,
    wy)``-weighted degree should be less than
    ``_interpolation_max_weighted_deg(n, tau, wy)``, where ``n`` is the number
    of points

    INPUT:

    - ``points`` -- list of tuples ``(xi, yi)`` such that we seek ``Q`` with
      ``(xi,yi)`` being a root of ``Q`` with multiplicity ``s``

    - ``tau`` -- integer; the number of errors one wants to decode

    - ``parameters`` -- (default: ``None``) a pair of integers, where:

      - the first integer is the multiplicity parameter of Guruswami-Sudan
        algorithm and
      - the second integer is the list size parameter.

    - ``wy`` -- integer; the `y`-weight, where we seek `Q` of low
      ``(1, wy)``-weighted degree

    EXAMPLES:

    The following parameters arise from Guruswami-Sudan decoding of an [6,2,5]
    GRS code over F(11) with multiplicity 2 and list size 4::

        sage: from sage.coding.guruswami_sudan.interpolation import gs_interpolation_linalg
        sage: F = GF(11)
        sage: points = [(F(x), F(y))
        ....:           for (x, y) in [(0, 5), (1, 1), (2, 4), (3, 6), (4, 3), (5, 3)]]
        sage: tau = 3
        sage: params = (2, 4)
        sage: wy = 1
        sage: Q = gs_interpolation_linalg(points, tau, params, wy); Q
        4*x^5 - 4*x^4*y - 2*x^2*y^3 - x*y^4 + 3*x^4 - 4*x^2*y^2 + 5*y^4 - x^3 + x^2*y
         + 5*x*y^2 - 5*y^3 + 3*x*y - 2*y^2 + x - 4*y + 1

    We verify that the interpolation polynomial has a zero of multiplicity at least 2 in each point::

        sage: all( Q(x=a, y=b).is_zero() for (a,b) in points )
        True
        sage: x,y = Q.parent().gens()
        sage: dQdx = Q.derivative(x)
        sage: all( dQdx(x=a, y=b).is_zero() for (a,b) in points )
        True
        sage: dQdy = Q.derivative(y)
        sage: all( dQdy(x=a, y=b).is_zero() for (a,b) in points )
        True
    """
def lee_osullivan_module(points, parameters, wy):
    """
    Return the analytically straight-forward basis for the `\\GF{q}[x]` module
    containing all interpolation polynomials, as according to Lee and
    O'Sullivan.

    The module is constructed in the following way: Let `R(x)` be the Lagrange
    interpolation polynomial through the sought interpolation points `(x_i,
    y_i)`, i.e. `R(x_i) = y_i`. Let `G(x) = \\prod_{i=1}^n (x-x_i)`. Then the
    `i`-th row of the basis matrix of the module is the coefficient-vector of
    the following polynomial in `\\GF{q}[x][y]`:

        `P_i(x,y) = G(x)^{[i-s]} (y - R(x))^{i - [i-s]} y^{[i-s]}` ,

    where `[a]` for real `a` is `a` when `a > 0` and 0 otherwise. It is easily
    seen that `P_i(x,y)` is an interpolation polynomial, i.e. it is zero with
    multiplicity at least `s` on each of the points `(x_i, y_i)`.


    INPUT:

    - ``points`` -- list of tuples ``(xi, yi)`` such that we seek `Q` with
      ``(xi,yi)`` being a root of `Q` with multiplicity `s`

    - ``parameters`` -- (default: ``None``) a pair of integers, where:

      - the first integer is the multiplicity parameter `s` of Guruswami-Sudan
        algorithm and
      - the second integer is the list size parameter.

    - ``wy`` -- integer; the `y`-weight, where we seek `Q` of low
      ``(1,wy)`` weighted degree

    EXAMPLES::

        sage: from sage.coding.guruswami_sudan.interpolation import lee_osullivan_module
        sage: F = GF(11)
        sage: points = [(F(0), F(2)), (F(1), F(5)), (F(2), F(0)), (F(3), F(4)),
        ....:           (F(4), F(9)), (F(5), F(1)), (F(6), F(9)), (F(7), F(10))]
        sage: params = (1, 1)
        sage: wy = 1
        sage: lee_osullivan_module(points, params, wy)
        [x^8 + 5*x^7 + 3*x^6 + 9*x^5 + 4*x^4 + 2*x^3 + 9*x   0]
        [ 10*x^7 + 4*x^6 + 9*x^4 + 7*x^3 + 2*x^2 + 9*x + 9   1]
    """
def gs_interpolation_lee_osullivan(points, tau, parameters, wy):
    """
    Return an interpolation polynomial Q(x,y) for the given input using the
    module-based algorithm of Lee and O'Sullivan.

    This algorithm constructs an explicit `(\\ell+1) \\times (\\ell+1)` polynomial
    matrix whose rows span the `\\GF q[x]` module of all interpolation
    polynomials. It then runs a row reduction algorithm to find a low-shifted
    degree vector in this row space, corresponding to a low weighted-degree
    interpolation polynomial.

    INPUT:

    - ``points`` -- list of tuples ``(xi, yi)`` such that we seek ``Q`` with
      ``(xi,yi)`` being a root of ``Q`` with multiplicity ``s``

    - ``tau`` -- integer; the number of errors one wants to decode

    - ``parameters`` -- (default: ``None``) a pair of integers, where:

      - the first integer is the multiplicity parameter of Guruswami-Sudan
        algorithm and
      - the second integer is the list size parameter.

    - ``wy`` -- integer; the `y`-weight, where we seek ``Q`` of low
      ``(1,wy)`` weighted degree

    EXAMPLES::

        sage: from sage.coding.guruswami_sudan.interpolation import gs_interpolation_lee_osullivan
        sage: F = GF(11)
        sage: points = [(F(0), F(2)), (F(1), F(5)), (F(2), F(0)), (F(3), F(4)),
        ....:           (F(4), F(9)), (F(5), F(1)), (F(6), F(9)), (F(7), F(10))]
        sage: tau = 1
        sage: params = (1, 1)
        sage: wy = 1
        sage: Q = gs_interpolation_lee_osullivan(points, tau, params, wy)
        sage: Q / Q.lc()  # make monic
        x^3*y + 2*x^3 - x^2*y + 5*x^2 + 5*x*y - 5*x + 2*y - 4
    """
