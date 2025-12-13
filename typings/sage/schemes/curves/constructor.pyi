from .affine_curve import AffineCurve as AffineCurve, AffineCurve_field as AffineCurve_field, AffinePlaneCurve as AffinePlaneCurve, AffinePlaneCurve_field as AffinePlaneCurve_field, AffinePlaneCurve_finite_field as AffinePlaneCurve_finite_field, IntegralAffineCurve as IntegralAffineCurve, IntegralAffineCurve_finite_field as IntegralAffineCurve_finite_field, IntegralAffinePlaneCurve as IntegralAffinePlaneCurve, IntegralAffinePlaneCurve_finite_field as IntegralAffinePlaneCurve_finite_field
from .projective_curve import IntegralProjectiveCurve as IntegralProjectiveCurve, IntegralProjectiveCurve_finite_field as IntegralProjectiveCurve_finite_field, IntegralProjectivePlaneCurve as IntegralProjectivePlaneCurve, IntegralProjectivePlaneCurve_finite_field as IntegralProjectivePlaneCurve_finite_field, ProjectiveCurve as ProjectiveCurve, ProjectiveCurve_field as ProjectiveCurve_field, ProjectivePlaneCurve as ProjectivePlaneCurve, ProjectivePlaneCurve_field as ProjectivePlaneCurve_field, ProjectivePlaneCurve_finite_field as ProjectivePlaneCurve_finite_field
from sage.categories.fields import Fields as Fields
from sage.categories.number_fields import NumberFields as NumberFields
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.rational_field import QQ as QQ
from sage.schemes.affine.affine_space import AffineSpace as AffineSpace, AffineSpace_generic as AffineSpace_generic
from sage.schemes.generic.algebraic_scheme import AlgebraicScheme as AlgebraicScheme
from sage.schemes.generic.ambient_space import AmbientSpace as AmbientSpace
from sage.schemes.plane_conics.constructor import Conic as Conic
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace, ProjectiveSpace_ring as ProjectiveSpace_ring
from sage.structure.all import Sequence as Sequence

def Curve(F, A=None):
    """
    Return the plane or space curve defined by ``F``, where ``F`` can be either
    a multivariate polynomial, a list or tuple of polynomials, or an algebraic
    scheme.

    If no ambient space is passed in for ``A``, and if ``F`` is not an
    algebraic scheme, a new ambient space is constructed.

    Also not specifying an ambient space will cause the curve to be defined in
    either affine or projective space based on properties of ``F``. In
    particular, if ``F`` contains a nonhomogeneous polynomial, the curve is
    affine, and if ``F`` consists of homogeneous polynomials, then the curve is
    projective.

    INPUT:

    - ``F`` -- a multivariate polynomial, or a list or tuple of polynomials, or an algebraic scheme

    - ``A`` -- (default: ``None``) an ambient space in which to create the curve

    EXAMPLES:

    A projective plane curve::

        sage: x,y,z = QQ['x,y,z'].gens()
        sage: C = Curve(x^3 + y^3 + z^3); C
        Projective Plane Curve over Rational Field defined by x^3 + y^3 + z^3
        sage: C.genus()
        1

    Affine plane curves.  ::

        sage: x,y = GF(7)['x,y'].gens()
        sage: C = Curve(y^2 + x^3 + x^10); C
        Affine Plane Curve over Finite Field of size 7 defined by x^10 + x^3 + y^2
        sage: C.genus()
        0
        sage: x, y = QQ['x,y'].gens()
        sage: Curve(x^3 + y^3 + 1)
        Affine Plane Curve over Rational Field defined by x^3 + y^3 + 1

    A projective space curve.  ::

        sage: x,y,z,w = QQ['x,y,z,w'].gens()
        sage: C = Curve([x^3 + y^3 - z^3 - w^3, x^5 - y*z^4]); C
        Projective Curve over Rational Field defined by x^3 + y^3 - z^3 - w^3, x^5 - y*z^4
        sage: C.genus()
        13

    An affine space curve.  ::

        sage: x,y,z = QQ['x,y,z'].gens()
        sage: C = Curve([y^2 + x^3 + x^10 + z^7,  x^2 + y^2]); C
        Affine Curve over Rational Field defined by x^10 + z^7 + x^3 + y^2, x^2 + y^2
        sage: C.genus()
        47

    We can also make non-reduced non-irreducible curves.  ::

        sage: x,y,z = QQ['x,y,z'].gens()
        sage: Curve((x-y)*(x+y))
        Projective Conic Curve over Rational Field defined by x^2 - y^2
        sage: Curve((x-y)^2*(x+y)^2)
        Projective Plane Curve over Rational Field defined by x^4 - 2*x^2*y^2 + y^4

    A union of curves is a curve.  ::

        sage: x,y,z = QQ['x,y,z'].gens()
        sage: C = Curve(x^3 + y^3 + z^3)
        sage: D = Curve(x^4 + y^4 + z^4)
        sage: C.union(D)
        Projective Plane Curve over Rational Field defined by
        x^7 + x^4*y^3 + x^3*y^4 + y^7 + x^4*z^3 + y^4*z^3 + x^3*z^4 + y^3*z^4 + z^7

    The intersection is not a curve, though it is a scheme.  ::

        sage: X = C.intersection(D); X
        Closed subscheme of Projective Space of dimension 2 over Rational Field
         defined by: x^3 + y^3 + z^3,
                     x^4 + y^4 + z^4

    Note that the intersection has dimension 0.  ::

        sage: X.dimension()
        0
        sage: I = X.defining_ideal(); I
        Ideal (x^3 + y^3 + z^3, x^4 + y^4 + z^4) of
         Multivariate Polynomial Ring in x, y, z over Rational Field

    If only a polynomial in three variables is given, then it must be
    homogeneous such that a projective curve is constructed.  ::

        sage: x,y,z = QQ['x,y,z'].gens()
        sage: Curve(x^2 + y^2)
        Projective Conic Curve over Rational Field defined by x^2 + y^2
        sage: Curve(x^2 + y^2 + z)
        Traceback (most recent call last):
        ...
        TypeError: x^2 + y^2 + z is not a homogeneous polynomial

    An ambient space can be specified to construct a space curve in an affine
    or a projective space.  ::

        sage: A.<x,y,z> = AffineSpace(QQ, 3)
        sage: C = Curve([y - x^2, z - x^3], A)
        sage: C
        Affine Curve over Rational Field defined by -x^2 + y, -x^3 + z
        sage: A == C.ambient_space()
        True

    The defining polynomial must be nonzero unless the ambient space itself is
    of dimension 1. ::

        sage: P1.<x,y> = ProjectiveSpace(1, GF(5))
        sage: S = P1.coordinate_ring()
        sage: Curve(S(0), P1)
        Projective Line over Finite Field of size 5
        sage: Curve(P1)
        Projective Line over Finite Field of size 5

    An affine line::

        sage: A1.<x> = AffineSpace(1, QQ)
        sage: R = A1.coordinate_ring()
        sage: Curve(R(0), A1)
        Affine Line over Rational Field
        sage: Curve(A1)
        Affine Line over Rational Field

    A projective line::

        sage: R.<x> = QQ[]
        sage: N.<a> = NumberField(x^2 + 1)
        sage: P1.<x,y> = ProjectiveSpace(N, 1)
        sage: C = Curve(P1)
        sage: C
        Projective Line over Number Field in a with defining polynomial x^2 + 1
        sage: C.geometric_genus()
        0
        sage: C.arithmetic_genus()
        0
    """
