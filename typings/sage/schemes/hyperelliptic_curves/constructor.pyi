from .hyperelliptic_finite_field import HyperellipticCurve_finite_field as HyperellipticCurve_finite_field
from .hyperelliptic_g2 import HyperellipticCurve_g2 as HyperellipticCurve_g2
from .hyperelliptic_generic import HyperellipticCurve_generic as HyperellipticCurve_generic
from .hyperelliptic_padic_field import HyperellipticCurve_padic_field as HyperellipticCurve_padic_field
from .hyperelliptic_rational_field import HyperellipticCurve_rational_field as HyperellipticCurve_rational_field
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.rational_field import RationalField as RationalField
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace
from sage.structure.dynamic_class import dynamic_class as dynamic_class

def HyperellipticCurve(f, h: int = 0, names=None, PP=None, check_squarefree: bool = True):
    '''
    Return the hyperelliptic curve `y^2 + h y = f`, for
    univariate polynomials `h` and `f`. If `h`
    is not given, then it defaults to 0.

    INPUT:

    - ``f`` -- univariate polynomial

    - ``h`` -- (optional) univariate polynomial

    - ``names`` -- (default: ``["x","y"]``) names for the coordinate functions

    - ``check_squarefree`` -- boolean (default: ``True``); test if the input
      defines a hyperelliptic curve when f is homogenized to degree `2g+2` and
      h to degree `g+1` for some `g`

    .. WARNING::

        When setting ``check_squarefree=False`` or using a base ring that is
        not a field, the output curves are not to be trusted. For example, the
        output of ``is_singular`` is always ``False``, without this being
        properly tested in that case.

    .. NOTE::

        The words "hyperelliptic curve" are normally only used for curves of
        genus at least two, but this class allows more general smooth double
        covers of the projective line (conics and elliptic curves), even though
        the class is not meant for those and some outputs may be incorrect.

    EXAMPLES:

    Basic examples::

        sage: R.<x> = QQ[]
        sage: HyperellipticCurve(x^5 + x + 1)
        Hyperelliptic Curve over Rational Field defined by y^2 = x^5 + x + 1
        sage: HyperellipticCurve(x^19 + x + 1, x - 2)
        Hyperelliptic Curve over Rational Field defined by y^2 + (x - 2)*y = x^19 + x + 1

        sage: k.<a> = GF(9); R.<x> = k[]                                                # needs sage.rings.finite_rings
        sage: HyperellipticCurve(x^3 + x - 1, x+a)                                      # needs sage.rings.finite_rings
        Hyperelliptic Curve over Finite Field in a of size 3^2
         defined by y^2 + (x + a)*y = x^3 + x + 2

    Characteristic two::

        sage: # needs sage.rings.finite_rings
        sage: P.<x> = GF(8, \'a\')[]
        sage: HyperellipticCurve(x^7 + 1, x)
        Hyperelliptic Curve over Finite Field in a of size 2^3
         defined by y^2 + x*y = x^7 + 1
        sage: HyperellipticCurve(x^8 + x^7 + 1, x^4 + 1)
        Hyperelliptic Curve over Finite Field in a of size 2^3
         defined by y^2 + (x^4 + 1)*y = x^8 + x^7 + 1
        sage: HyperellipticCurve(x^8 + 1, x)
        Traceback (most recent call last):
        ...
        ValueError: not a hyperelliptic curve: highly singular at infinity
        sage: HyperellipticCurve(x^8 + x^7 + 1, x^4)
        Traceback (most recent call last):
        ...
        ValueError: not a hyperelliptic curve: singularity in the provided affine patch

        sage: F.<t> = PowerSeriesRing(FiniteField(2))
        sage: P.<x> = PolynomialRing(FractionField(F))
        sage: HyperellipticCurve(x^5 + t, x)
        Hyperelliptic Curve over Laurent Series Ring in t over Finite Field of size 2
         defined by y^2 + x*y = x^5 + t

    We can change the names of the variables in the output::

        sage: k.<a> = GF(9); R.<x> = k[]                                                # needs sage.rings.finite_rings
        sage: HyperellipticCurve(x^3 + x - 1, x + a, names=[\'X\',\'Y\'])                   # needs sage.rings.finite_rings
        Hyperelliptic Curve over Finite Field in a of size 3^2
         defined by Y^2 + (X + a)*Y = X^3 + X + 2

    This class also allows curves of genus zero or one, which are strictly
    speaking not hyperelliptic::

        sage: P.<x> = QQ[]
        sage: HyperellipticCurve(x^2 + 1)
        Hyperelliptic Curve over Rational Field defined by y^2 = x^2 + 1
        sage: HyperellipticCurve(x^4 - 1)
        Hyperelliptic Curve over Rational Field defined by y^2 = x^4 - 1
        sage: HyperellipticCurve(x^3 + 2*x + 2)
        Hyperelliptic Curve over Rational Field defined by y^2 = x^3 + 2*x + 2

    Double roots::

        sage: P.<x> = GF(7)[]
        sage: HyperellipticCurve((x^3-x+2)^2*(x^6-1))
        Traceback (most recent call last):
        ...
        ValueError: not a hyperelliptic curve: singularity in the provided affine patch

        sage: HyperellipticCurve((x^3-x+2)^2*(x^6-1), check_squarefree=False)
        Hyperelliptic Curve over Finite Field of size 7 defined by
         y^2 = x^12 + 5*x^10 + 4*x^9 + x^8 + 3*x^7 + 3*x^6 + 2*x^4 + 3*x^3 + 6*x^2 + 4*x + 3

    The input for a (smooth) hyperelliptic curve of genus `g` should not
    contain polynomials of degree greater than `2g+2`. In the following
    example, the hyperelliptic curve has genus 2 and there exists a model
    `y^2 = F` of degree 6, so the model `y^2 + yh = f` of degree 200 is not
    allowed.::

        sage: P.<x> = QQ[]
        sage: h = x^100
        sage: F = x^6 + 1
        sage: f = F - h^2/4
        sage: HyperellipticCurve(f, h)
        Traceback (most recent call last):
        ...
        ValueError: not a hyperelliptic curve: highly singular at infinity

        sage: HyperellipticCurve(F)
        Hyperelliptic Curve over Rational Field defined by y^2 = x^6 + 1

    An example with a singularity over an inseparable extension of the
    base field::

        sage: F.<t> = GF(5)[]
        sage: P.<x> = F[]
        sage: HyperellipticCurve(x^5 + t)
        Traceback (most recent call last):
        ...
        ValueError: not a hyperelliptic curve: singularity in the provided affine patch

    Input with integer coefficients creates objects with the integers
    as base ring, but only checks smoothness over `\\QQ`, not over Spec(`\\ZZ`).
    In other words, it is checked that the discriminant is nonzero, but it is
    not checked whether the discriminant is a unit in `\\ZZ^*`.::

        sage: P.<x> = ZZ[]
        sage: HyperellipticCurve(3*x^7 + 6*x + 6)
        Hyperelliptic Curve over Integer Ring defined by y^2 = 3*x^7 + 6*x + 6

    TESTS:

    Check that `f` can be a constant (see :issue:`15516`)::

        sage: R.<u> = PolynomialRing(Rationals())
        sage: HyperellipticCurve(-12, u^4 + 7)
        Hyperelliptic Curve over Rational Field defined by y^2 + (x^4 + 7)*y = -12

    Check that two curves with the same class name have the same class type::

        sage: # needs sage.rings.finite_rings
        sage: R.<t> = PolynomialRing(GF(next_prime(10^9)))
        sage: C = HyperellipticCurve(t^5 + t + 1)
        sage: C2 = HyperellipticCurve(t^5 + 3*t + 1)
        sage: type(C2) == type(C)
        True

    Check that the inheritance is correct::

        sage: # needs sage.rings.finite_rings
        sage: R.<t> = PolynomialRing(GF(next_prime(10^9)))
        sage: C = HyperellipticCurve(t^5 + t + 1)
        sage: type(C).mro()
        [<class \'sage.schemes.hyperelliptic_curves.constructor.HyperellipticCurve_g2_FiniteField_with_category\'>,
         <class \'sage.schemes.hyperelliptic_curves.constructor.HyperellipticCurve_g2_FiniteField\'>,
         <class \'sage.schemes.hyperelliptic_curves.hyperelliptic_g2.HyperellipticCurve_g2\'>,
         <class \'sage.schemes.hyperelliptic_curves.hyperelliptic_finite_field.HyperellipticCurve_finite_field\'>,
         <class \'sage.schemes.hyperelliptic_curves.hyperelliptic_generic.HyperellipticCurve_generic\'>,
        ...]
    '''
