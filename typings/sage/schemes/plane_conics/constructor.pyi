from .con_field import ProjectiveConic_field as ProjectiveConic_field
from .con_finite_field import ProjectiveConic_finite_field as ProjectiveConic_finite_field
from .con_number_field import ProjectiveConic_number_field as ProjectiveConic_number_field
from .con_rational_field import ProjectiveConic_rational_field as ProjectiveConic_rational_field
from .con_rational_function_field import ProjectiveConic_rational_function_field as ProjectiveConic_rational_function_field
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.matrix.constructor import matrix as matrix
from sage.modules.free_module_element import vector as vector
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.fraction_field import FractionField_generic as FractionField_generic
from sage.rings.number_field.number_field_base import NumberField as NumberField
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import RationalField as RationalField
from sage.schemes.affine.affine_point import SchemeMorphism_point_affine as SchemeMorphism_point_affine
from sage.schemes.projective.projective_point import SchemeMorphism_point_projective_field as SchemeMorphism_point_projective_field
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace
from sage.structure.all import Sequence as Sequence
from sage.structure.element import Matrix as Matrix

def Conic(base_field, F=None, names=None, unique: bool = True):
    """
    Return the plane projective conic curve defined by ``F``
    over ``base_field``.

    The input form ``Conic(F, names=None)`` is also accepted,
    in which case the fraction field of the base ring of ``F``
    is used as base field.

    INPUT:

    - ``base_field`` -- the base field of the conic

    - ``names`` -- list, tuple, or comma separated string
      of three variable names specifying the names
      of the coordinate functions of the ambient
      space `\\Bold{P}^3`. If not specified or read
      off from ``F``, then this defaults to ``'x,y,z'``.

    - ``F`` -- a polynomial, list, matrix, ternary quadratic form,
      or list or tuple of 5 points in the plane.

                   If ``F`` is a polynomial or quadratic form,
                   then the output is the curve in the projective plane
                   defined by ``F = 0``.

                   If ``F`` is a polynomial, then it must be a polynomial
                   of degree at most 2 in 2 variables, or a homogeneous
                   polynomial in of degree 2 in 3 variables.

                   If ``F`` is a matrix, then the output is the zero locus
                   of `(x,y,z) F (x,y,z)^t`.

                   If ``F`` is a list of coefficients, then it has
                   length 3 or 6 and gives the coefficients of
                   the monomials `x^2, y^2, z^2` or all 6 monomials
                   `x^2, xy, xz, y^2, yz, z^2` in lexicographic order.

                   If ``F`` is a list of 5 points in the plane, then the output
                   is a conic through those points.

    - ``unique`` -- used only if ``F`` is a list of points in the plane;
      if the conic through the points is not unique, then
      raise :exc:`ValueError` if and only if ``unique`` is ``True``

    OUTPUT: a plane projective conic curve defined by ``F`` over a field

    EXAMPLES:

    Conic curves given by polynomials ::

        sage: X,Y,Z = QQ['X,Y,Z'].gens()
        sage: Conic(X^2 - X*Y + Y^2 - Z^2)
        Projective Conic Curve over Rational Field defined by X^2 - X*Y + Y^2 - Z^2
        sage: x,y = GF(7)['x,y'].gens()
        sage: Conic(x^2 - x + 2*y^2 - 3, 'U,V,W')
        Projective Conic Curve over Finite Field of size 7
         defined by U^2 + 2*V^2 - U*W - 3*W^2

    Conic curves given by matrices ::

        sage: Conic(matrix(QQ, [[1, 2, 0], [4, 0, 0], [7, 0, 9]]), 'x,y,z')
        Projective Conic Curve over Rational Field defined by x^2 + 6*x*y + 7*x*z + 9*z^2

        sage: x,y,z = GF(11)['x,y,z'].gens()
        sage: C = Conic(x^2 + y^2 - 2*z^2); C
        Projective Conic Curve over Finite Field of size 11 defined by x^2 + y^2 - 2*z^2
        sage: Conic(C.symmetric_matrix(), 'x,y,z')
        Projective Conic Curve over Finite Field of size 11 defined by x^2 + y^2 - 2*z^2

    Conics given by coefficients ::

        sage: Conic(QQ, [1,2,3])
        Projective Conic Curve over Rational Field defined by x^2 + 2*y^2 + 3*z^2
        sage: Conic(GF(7), [1,2,3,4,5,6], 'X')
        Projective Conic Curve over Finite Field of size 7
        defined by X0^2 + 2*X0*X1 - 3*X1^2 + 3*X0*X2 - 2*X1*X2 - X2^2

    The conic through a set of points ::

        sage: C = Conic(QQ, [[10,2],[3,4],[-7,6],[7,8],[9,10]]); C
        Projective Conic Curve over Rational Field
         defined by x^2 + 13/4*x*y - 17/4*y^2 - 35/2*x*z + 91/4*y*z - 37/2*z^2
        sage: C.rational_point()
        (10 : 2 : 1)
        sage: C.point([3,4])
        (3 : 4 : 1)

        sage: a = AffineSpace(GF(13), 2)
        sage: Conic([a([x,x^2]) for x in range(5)])
        Projective Conic Curve over Finite Field of size 13 defined by x^2 - y*z
    """
