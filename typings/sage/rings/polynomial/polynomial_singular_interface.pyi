from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.function_field.function_field_rational import RationalFunctionField as RationalFunctionField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field_base import NumberField as NumberField
from sage.rings.rational_field import RationalField as RationalField

class PolynomialRing_singular_repr:
    """
    Implement methods to convert polynomial rings to Singular.

    This class is a base class for all univariate and multivariate
    polynomial rings which support conversion from and to Singular
    rings.
    """

def can_convert_to_singular(R):
    """
    Return ``True`` if this ring's base field or ring can be
    represented in Singular, and the polynomial ring has at
    least one generator.

    The following base rings are supported: finite fields,
    rationals, number fields, and real and complex fields.

    EXAMPLES::

        sage: from sage.rings.polynomial.polynomial_singular_interface import can_convert_to_singular
        sage: can_convert_to_singular(PolynomialRing(QQ, names=['x']))
        True
        sage: can_convert_to_singular(PolynomialRing(ZZ, names=['x']))
        True

        sage: can_convert_to_singular(PolynomialRing(QQ, names=[]))
        False

    TESTS:

    Avoid non absolute number fields (see :issue:`23535`)::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a,b> = NumberField([x^2 - 2, x^2 - 5])                                 # needs sage.rings.number_field
        sage: can_convert_to_singular(K['s,t'])                                         # needs sage.rings.number_field
        False

    Check for :issue:`33319`::

        sage: # needs sage.rings.finite_rings
        sage: R.<x,y> = GF((2^31-1)^3)[]
        sage: R._has_singular
        True
        sage: R.<x,y> = GF((2^31+11)^2)[]
        sage: R._has_singular
        False
        sage: R.<x,y> = GF(10^20 - 11)[]
        sage: R._has_singular
        True

        sage: R.<x,y> = Zmod(10^20 + 1)[]
        sage: R._has_singular
        True

    Check that :issue:`39106` is fixed::

        sage: s = SymmetricFunctions(QQ).s()
        sage: R.<x> = PolynomialRing(s.fraction_field())
        sage: can_convert_to_singular(R)
        False
        sage: R.<x, y> = PolynomialRing(s.fraction_field())
        sage: can_convert_to_singular(R)
        False
    """

class Polynomial_singular_repr:
    """
    Implement coercion of polynomials to Singular polynomials.

    This class is a base class for all (univariate and multivariate)
    polynomial classes which support conversion from and to
    Singular polynomials.

    Due to the incompatibility of Python extension classes and multiple inheritance,
    this just defers to module-level functions.
    """
