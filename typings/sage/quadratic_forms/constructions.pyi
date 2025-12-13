from sage.quadratic_forms.quadratic_form import QuadraticForm as QuadraticForm
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

def BezoutianQuadraticForm(f, g):
    """
    Compute the Bezoutian of two polynomials defined over a common base ring.  This is defined by

    .. MATH::

        {\\rm Bez}(f, g) := \\frac{f(x) g(y) - f(y) g(x)}{y - x}

    and has size defined by the maximum of the degrees of `f` and `g`.

    INPUT:

    - ``f``, ``g`` -- polynomials in `R[x]`, for some ring `R`

    OUTPUT: a quadratic form over `R`

    EXAMPLES::

        sage: R = PolynomialRing(ZZ, 'x')
        sage: f = R([1,2,3])
        sage: g = R([2,5])
        sage: Q = BezoutianQuadraticForm(f, g); Q                                       # needs sage.libs.singular
        Quadratic form in 2 variables over Integer Ring with coefficients:
        [ 1 -12 ]
        [ * -15 ]

    AUTHORS:

    - Fernando Rodriguez-Villegas, Jonathan Hanke -- added on 11/9/2008
    """
def HyperbolicPlane_quadratic_form(R, r: int = 1):
    """
    Construct the direct sum of `r` copies of the quadratic form `xy`
    representing a hyperbolic plane defined over the base ring `R`.

    INPUT:

    - ``R`` -- a ring
    - ``n`` -- integer (default: 1); number of copies

    EXAMPLES::

        sage: HyperbolicPlane_quadratic_form(ZZ)
        Quadratic form in 2 variables over Integer Ring with coefficients:
        [ 0 1 ]
        [ * 0 ]
    """
