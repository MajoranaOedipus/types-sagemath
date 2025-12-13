from . import ell_point as ell_point
from .ell_field import EllipticCurve_field as EllipticCurve_field
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.schemes.hyperelliptic_curves.hyperelliptic_padic_field import HyperellipticCurve_padic_field as HyperellipticCurve_padic_field

class EllipticCurve_padic_field(EllipticCurve_field, HyperellipticCurve_padic_field):
    """
    Elliptic curve over a `p`-adic field.

    EXAMPLES::

        sage: Qp = pAdicField(17)
        sage: E = EllipticCurve(Qp,[2,3]); E
        Elliptic Curve defined by y^2  = x^3 + (2+O(17^20))*x + (3+O(17^20))
         over 17-adic Field with capped relative precision 20
        sage: E == loads(dumps(E))
        True
    """
    def frobenius(self, P=None):
        """
        Return the Frobenius as a function on the group of points of
        this elliptic curve.

        EXAMPLES::

            sage: Qp = pAdicField(13)
            sage: E = EllipticCurve(Qp,[1,1])
            sage: type(E.frobenius())
            <... 'function'>
            sage: point = E(0,1)
            sage: E.frobenius(point)
            (0 : 1 + O(13^20) : 1 + O(13^20))

        Check that :issue:`29709` is fixed::

            sage: Qp = pAdicField(13)
            sage: E = EllipticCurve(Qp,[0,0,1,0,1])
            sage: E.frobenius(E(1,1))
            Traceback (most recent call last):
            ...
            NotImplementedError: Curve must be in weierstrass normal form.
            sage: E = EllipticCurve(Qp,[0,1,0,0,1])
            sage: E.frobenius(E(0,1))
            (0 : 1 + O(13^20) : 1 + O(13^20))
        """
