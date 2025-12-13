from sage.misc.functional import sqrt as sqrt
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ

def polynomial_to_list(p, len):
    """
    Return ``p`` as a list of its coefficients of length ``len``.

    INPUT:

    - ``p`` -- a polynomial

    - ``len`` -- integer; if ``len`` is smaller than the degree of ``p``, the
      returned list will be of size degree of ``p``, else it will be of size ``len``

    EXAMPLES::

        sage: from sage.coding.guruswami_sudan.utils import polynomial_to_list
        sage: F.<x> = GF(41)[]
        sage: p = 9*x^2 + 8*x + 37
        sage: polynomial_to_list(p, 4)
        [37, 8, 9, 0]
    """
def johnson_radius(n, d):
    """
    Return the Johnson-radius for the code length `n` and the minimum distance `d`.

    The Johnson radius is defined as `n - \\sqrt(n(n-d))`.

    INPUT:

    - ``n`` -- integer; the length of the code
    - ``d`` -- integer; the minimum distance of the code

    EXAMPLES::

        sage: sage.coding.guruswami_sudan.utils.johnson_radius(250, 181)                # needs sage.symbolic
        -5*sqrt(690) + 250
    """
def ligt(x):
    """
    Return the least integer greater than ``x``.

    EXAMPLES::

        sage: from sage.coding.guruswami_sudan.utils import ligt
        sage: ligt(41)
        42

    It works with any type of numbers (not only integers)::

        sage: ligt(41.041)
        42
    """
def gilt(x):
    """
    Return the greatest integer smaller than ``x``.

    EXAMPLES::

        sage: from sage.coding.guruswami_sudan.utils import gilt
        sage: gilt(43)
        42

    It works with any type of numbers (not only integers)::

        sage: gilt(43.041)
        43
    """
def solve_degree2_to_integer_range(a, b, c):
    """
    Return the greatest integer range `[i_1, i_2]` such that
    `i_1 > x_1` and `i_2 < x_2` where `x_1, x_2` are the two zeroes of the
    equation in `x`: `ax^2+bx+c=0`.

    If there is no real solution to the equation, it returns an empty range
    with negative coefficients.

    INPUT:

    - ``a``, ``b`` and ``c`` -- coefficients of a second degree equation, ``a``
      being the coefficient of the higher degree term

    EXAMPLES::

        sage: from sage.coding.guruswami_sudan.utils import solve_degree2_to_integer_range
        sage: solve_degree2_to_integer_range(1, -5, 1)                                  # needs sage.symbolic
        (1, 4)

    If there is no real solution::

        sage: solve_degree2_to_integer_range(50, 5, 42)
        (-2, -1)
    """
