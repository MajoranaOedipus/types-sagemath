from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.schemes.generic.homset import SchemeHomset_points as SchemeHomset_points
from sage.schemes.hyperelliptic_curves.jacobian_morphism import JacobianMorphism_divisor_class_field as JacobianMorphism_divisor_class_field

class JacobianHomset_divisor_classes(SchemeHomset_points):
    def __init__(self, Y, X, **kwds) -> None: ...
    def __call__(self, P):
        """
        Return a rational point P in the abstract Homset J(K), given:

        0. A point P in J = Jac(C), returning P;

        1. A point P on the curve C such that J = Jac(C), where C is
           an odd degree model, returning [P - oo];

        2. A pair of points (P, Q) on the curve C such that J = Jac(C),
           returning [P-Q];

        3. A list of polynomials (a,b) such that `b^2 + h*b - f = 0 mod a`,
           returning [(a(x),y-b(x))].

        EXAMPLES::

            sage: P.<x> = PolynomialRing(QQ)
            sage: f = x^5 - x + 1; h = x
            sage: C = HyperellipticCurve(f,h,'u,v')
            sage: P = C(0,1,1)
            sage: J = C.jacobian()
            sage: Q = J(QQ)(P)
            sage: for i in range(6): i*Q
            (1)
            (u, v - 1)
            (u^2, v + u - 1)
            (u^2, v + 1)
            (u, v + 1)
            (1)

        ::

            sage: F.<a> = GF(3)
            sage: R.<x> = F[]
            sage: f = x^5 - 1
            sage: C = HyperellipticCurve(f)
            sage: J = C.jacobian()
            sage: X = J(F)
            sage: a = x^2 - x + 1; b = -x + 1; c = x - 1; d = 0
            sage: D1 = X([a,b]); D1
            (x^2 + 2*x + 1, y + x + 2)
            sage: D2 = X([c,d]); D2
            (x + 2, y)
            sage: D1 + D2
            (x^2 + 2*x + 2, y + 2*x + 1)

        TESTS:

        Test :issue:`38459`::

            sage: K.<u> = QQ[]
            sage: C = HyperellipticCurve(u^5 - 1)
            sage: J = C.jacobian()
            sage: J(u - 1, 0)
            (x - 1, y)
        """
    def curve(self): ...
    def value_ring(self):
        """
        Return S for a homset X(T) where T = Spec(S).
        """
    def base_extend(self, R): ...
