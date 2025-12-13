from .quartic_generic import QuarticCurve_generic as QuarticCurve_generic
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace, ProjectiveSpace_ring as ProjectiveSpace_ring

def QuarticCurve(F, PP=None, check: bool = False):
    """
    Return the quartic curve defined by the polynomial ``F``.

    INPUT:

    - ``F`` -- a polynomial in three variables, homogeneous of degree 4

    - ``PP`` -- a projective plane (default: ``None``)

    - ``check`` -- whether to check for smoothness or not (default: ``False``)

    EXAMPLES::

        sage: x,y,z = PolynomialRing(QQ, ['x','y','z']).gens()
        sage: QuarticCurve(x**4 + y**4 + z**4)
        Quartic Curve over Rational Field defined by x^4 + y^4 + z^4

    TESTS::

        sage: QuarticCurve(x**3 + y**3)
        Traceback (most recent call last):
        ...
        ValueError: Argument F (=x^3 + y^3) must be a homogeneous polynomial of degree 4

        sage: QuarticCurve(x**4 + y**4 + z**3)
        Traceback (most recent call last):
        ...
        ValueError: Argument F (=x^4 + y^4 + z^3) must be a homogeneous polynomial of degree 4

        sage: x,y=PolynomialRing(QQ,['x','y']).gens()
        sage: QuarticCurve(x**4 + y**4)
        Traceback (most recent call last):
        ...
        ValueError: Argument F (=x^4 + y^4) must be a polynomial in 3 variables
    """
