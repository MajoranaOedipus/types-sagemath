from sage.rings.invariants.invariant_theory import invariant_theory as invariant_theory
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing

def WeierstrassForm2(polynomial, variables=None, transformation: bool = False):
    """
    Helper function for :func:`~sage.schemes.toric.weierstrass.WeierstrassForm`.

    Currently, only the case of the complete intersection of two
    quadratic equations in `\\mathbb{P}^3` is supported.

    INPUT / OUTPUT: see :func:`~sage.schemes.toric.weierstrass.WeierstrassForm`

    TESTS::

        sage: from sage.schemes.toric.weierstrass_higher import WeierstrassForm2
        sage: R.<w,x,y,z> = QQ[]
        sage: quadratic1 = w^2 + x^2 + y^2
        sage: quadratic2 = z^2 + w*x
        sage: WeierstrassForm2([quadratic1, quadratic2])
        (-1/4, 0)
    """
def WeierstrassForm_P3(quadratic1, quadratic2, variables=None):
    """
    Bring a complete intersection of two quadratics into Weierstrass form.

    Input/output is the same as
    :func:`sage.schemes.toric.weierstrass.WeierstrassForm`, except
    that the two input polynomials must be quadratic polynomials in
    `\\mathbb{P}^3`.

    EXAMPLES::

        sage: from sage.schemes.toric.weierstrass_higher import WeierstrassForm_P3
        sage: R.<w,x,y,z> = QQ[]
        sage: quadratic1 = w^2 + x^2 + y^2
        sage: quadratic2 = z^2 + w*x
        sage: WeierstrassForm_P3(quadratic1, quadratic2)
        (-1/4, 0)

    TESTS::

        sage: R.<w,x,y,z,a0,a1,a2,a3,b0,b1,b2,b3,b4,b5> = QQ[]
        sage: p1 = w^2 + x^2 + y^2 + z^2
        sage: p2 = a0*w^2 + a1*x^2 + a2*y^2 + a3*z^2
        sage: p2 += b0*x*y + b1*x*z + b2*x*w + b3*y*z + b4*y*w + b5*z*w
        sage: a, b = WeierstrassForm_P3(p1, p2, [w,x,y,z])
        sage: a.total_degree(), len(a.coefficients())
        (4, 107)
        sage: b.total_degree(), len(b.coefficients())
        (6, 648)
    """
def WeierstrassMap_P3(quadratic1, quadratic2, variables=None):
    """
    Bring a complete intersection of two quadratics into Weierstrass form.

    Input/output is the same as
    :func:`sage.schemes.toric.weierstrass.WeierstrassForm`, except
    that the two input polynomials must be quadratic polynomials in
    `\\mathbb{P}^3`.

    EXAMPLES::

        sage: from sage.schemes.toric.weierstrass_higher import \\\n        ....:     WeierstrassMap_P3, WeierstrassForm_P3
        sage: R.<w,x,y,z> = QQ[]
        sage: quadratic1 = w^2 + x^2 + y^2
        sage: quadratic2 = z^2 + w*x
        sage: X, Y, Z = WeierstrassMap_P3(quadratic1, quadratic2)
        sage: X
        1/1024*w^8 + 3/256*w^6*x^2 + 19/512*w^4*x^4 + 3/256*w^2*x^6 + 1/1024*x^8
        sage: Y
        1/32768*w^12 - 7/16384*w^10*x^2 - 145/32768*w^8*x^4 - 49/8192*w^6*x^6
        - 145/32768*w^4*x^8 - 7/16384*w^2*x^10 + 1/32768*x^12
        sage: Z
        -1/8*w^2*y*z + 1/8*x^2*y*z

        sage: a, b = WeierstrassForm_P3(quadratic1, quadratic2);  a, b
        (-1/4, 0)

        sage: ideal = R.ideal(quadratic1, quadratic2)
        sage: (-Y^2 + X^3 + a*X*Z^4 + b*Z^6).reduce(ideal)                              # needs sage.libs.singular
        0

    TESTS::

        sage: R.<w,x,y,z,a0,a1,a2,a3> = GF(101)[]
        sage: p1 = w^2 + x^2 + y^2 + z^2
        sage: p2 = a0*w^2 + a1*x^2 + a2*y^2 + a3*z^2
        sage: X, Y, Z = WeierstrassMap_P3(p1, p2, [w,x,y,z])
        sage: X.total_degree(), len(X.coefficients())
        (22, 4164)
        sage: Y.total_degree(), len(Y.coefficients())
        (33, 26912)
        sage: Z.total_degree(), len(Z.coefficients())
        (10, 24)
        sage: Z
        w*x*y*z*a0^3*a1^2*a2 - w*x*y*z*a0^2*a1^3*a2 - w*x*y*z*a0^3*a1*a2^2
        + w*x*y*z*a0*a1^3*a2^2 + w*x*y*z*a0^2*a1*a2^3 - w*x*y*z*a0*a1^2*a2^3
        - w*x*y*z*a0^3*a1^2*a3 + w*x*y*z*a0^2*a1^3*a3 + w*x*y*z*a0^3*a2^2*a3
        - w*x*y*z*a1^3*a2^2*a3 - w*x*y*z*a0^2*a2^3*a3 + w*x*y*z*a1^2*a2^3*a3
        + w*x*y*z*a0^3*a1*a3^2 - w*x*y*z*a0*a1^3*a3^2 - w*x*y*z*a0^3*a2*a3^2
        + w*x*y*z*a1^3*a2*a3^2 + w*x*y*z*a0*a2^3*a3^2 - w*x*y*z*a1*a2^3*a3^2
        - w*x*y*z*a0^2*a1*a3^3 + w*x*y*z*a0*a1^2*a3^3 + w*x*y*z*a0^2*a2*a3^3
        - w*x*y*z*a1^2*a2*a3^3 - w*x*y*z*a0*a2^2*a3^3 + w*x*y*z*a1*a2^2*a3^3
    """
