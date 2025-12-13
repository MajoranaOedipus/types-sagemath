from sage.schemes.elliptic_curves.constructor import EllipticCurve as EllipticCurve

def Jacobian(X, **kwds):
    """
    Return the Jacobian.

    INPUT:

    - ``X`` -- polynomial, algebraic variety, or anything else that
      has a Jacobian elliptic curve

    - ``kwds`` -- optional keyword arguments

    The input ``X`` can be one of the following:

    * A polynomial, see :func:`Jacobian_of_equation` for details.

    * A curve, see :func:`Jacobian_of_curve` for details.

    EXAMPLES::

        sage: R.<u,v,w> = QQ[]
        sage: Jacobian(u^3 + v^3 + w^3)
        Elliptic Curve defined by y^2 = x^3 - 27/4 over Rational Field

        sage: C = Curve(u^3 + v^3 + w^3)
        sage: Jacobian(C)
        Elliptic Curve defined by y^2 = x^3 - 27/4 over Rational Field

        sage: P2.<u,v,w> = ProjectiveSpace(2, QQ)
        sage: C = P2.subscheme(u^3 + v^3 + w^3)
        sage: Jacobian(C)
        Elliptic Curve defined by y^2 = x^3 - 27/4 over Rational Field

        sage: Jacobian(C, morphism=True)
        Scheme morphism:
          From: Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
          u^3 + v^3 + w^3
          To:   Elliptic Curve defined by y^2 = x^3 - 27/4 over Rational Field
          Defn: Defined on coordinates by sending (u : v : w) to
                (-u^4*v^4*w - u^4*v*w^4 - u*v^4*w^4 :
                 1/2*u^6*v^3 - 1/2*u^3*v^6 - 1/2*u^6*w^3 + 1/2*v^6*w^3 + 1/2*u^3*w^6 - 1/2*v^3*w^6 :
                 u^3*v^3*w^3)
    """
def Jacobian_of_curve(curve, morphism: bool = False):
    """
    Return the Jacobian of a genus-one curve.

    INPUT:

    - ``curve`` -- a one-dimensional algebraic variety of genus one

    OUTPUT: its Jacobian elliptic curve

    EXAMPLES::

        sage: R.<u,v,w> = QQ[]
        sage: C = Curve(u^3 + v^3 + w^3)
        sage: Jacobian(C)
        Elliptic Curve defined by y^2 = x^3 - 27/4 over Rational Field
    """
def Jacobian_of_equation(polynomial, variables=None, curve=None):
    """
    Construct the Jacobian of a genus-one curve given by a polynomial.

    INPUT:

    - ``F`` -- a polynomial defining a plane curve of genus one. May
      be homogeneous or inhomogeneous

    - ``variables`` -- list of two or three variables or ``None``
      (default). The inhomogeneous or homogeneous coordinates. By
      default, all variables in the polynomial are used.

    - ``curve`` -- the genus-one curve defined by ``polynomial`` or #
      ``None`` (default). If specified, suitable morphism from the
      jacobian elliptic curve to the curve is returned.

    OUTPUT:

    An elliptic curve in short Weierstrass form isomorphic to the
    curve ``polynomial=0``. If the optional argument ``curve`` is
    specified, a rational multicover from the Jacobian elliptic curve
    to the genus-one curve is returned.

    EXAMPLES::

        sage: R.<a,b,c> = QQ[]
        sage: f = a^3 + b^3 + 60*c^3
        sage: Jacobian(f)
        Elliptic Curve defined by y^2 = x^3 - 24300 over Rational Field
        sage: Jacobian(f.subs(c=1))
        Elliptic Curve defined by y^2 = x^3 - 24300 over Rational Field

    If we specify the domain curve, the birational covering is returned::

        sage: h = Jacobian(f, curve=Curve(f));  h
        Scheme morphism:
          From: Projective Plane Curve over Rational Field defined by a^3 + b^3 + 60*c^3
          To:   Elliptic Curve defined by y^2 = x^3 - 24300 over Rational Field
          Defn: Defined on coordinates by sending (a : b : c) to
                (-216000*a^4*b^4*c - 12960000*a^4*b*c^4 - 12960000*a*b^4*c^4
                 : 108000*a^6*b^3 - 108000*a^3*b^6 - 6480000*a^6*c^3 + 6480000*b^6*c^3
                   + 388800000*a^3*c^6 - 388800000*b^3*c^6
                 : 216000*a^3*b^3*c^3)

        sage: h([1,-1,0])
        (0 : 1 : 0)

    Plugging in the polynomials defining `h` allows us to verify that
    it is indeed a rational morphism to the elliptic curve::

        sage: E = h.codomain()
        sage: E.defining_polynomial()(h.defining_polynomials()).factor()
        (2519424000000000) * c^3 * b^3 * a^3 * (a^3 + b^3 + 60*c^3)
        * (a^9*b^6 + a^6*b^9 - 120*a^9*b^3*c^3 + 900*a^6*b^6*c^3 - 120*a^3*b^9*c^3
           + 3600*a^9*c^6 + 54000*a^6*b^3*c^6 + 54000*a^3*b^6*c^6 + 3600*b^9*c^6
           + 216000*a^6*c^9 - 432000*a^3*b^3*c^9 + 216000*b^6*c^9)

    By specifying the variables, we can also construct an elliptic
    curve over a polynomial ring::

        sage: R.<u,v,t> = QQ[]
        sage: Jacobian(u^3 + v^3 + t, variables=[u,v])
        Elliptic Curve defined by y^2 = x^3 + (-27/4*t^2) over
         Multivariate Polynomial Ring in u, v, t over Rational Field

    TESTS::

        sage: from sage.schemes.elliptic_curves.jacobian import Jacobian_of_equation
        sage: Jacobian_of_equation(f, variables=[a,b,c])
        Elliptic Curve defined by y^2 = x^3 - 24300 over Rational Field
    """
