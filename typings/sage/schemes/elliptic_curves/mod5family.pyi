from .constructor import EllipticCurve as EllipticCurve
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ

def mod5family(a, b):
    """
    Formulas for computing the family of elliptic curves with
    congruent mod-5 representation.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.mod5family import mod5family
        sage: mod5family(0,1)
        Elliptic Curve defined by y^2 = x^3 + (t^30+30*t^29+435*t^28+4060*t^27+27405*t^26+142506*t^25+593775*t^24+2035800*t^23+5852925*t^22+14307150*t^21+30045015*t^20+54627300*t^19+86493225*t^18+119759850*t^17+145422675*t^16+155117520*t^15+145422675*t^14+119759850*t^13+86493225*t^12+54627300*t^11+30045015*t^10+14307150*t^9+5852925*t^8+2035800*t^7+593775*t^6+142506*t^5+27405*t^4+4060*t^3+435*t^2+30*t+1) over Fraction Field of Univariate Polynomial Ring in t over Rational Field
    """
