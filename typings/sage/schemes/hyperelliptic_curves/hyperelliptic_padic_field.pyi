from . import hyperelliptic_generic as hyperelliptic_generic
from sage.matrix.constructor import matrix as matrix
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.modules.free_module_element import vector as vector
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ, RationalField as RationalField
from sage.rings.real_mpfr import RR as RR
from sage.schemes.curves.projective_curve import ProjectivePlaneCurve_field as ProjectivePlaneCurve_field

class HyperellipticCurve_padic_field(hyperelliptic_generic.HyperellipticCurve_generic, ProjectivePlaneCurve_field):
    def local_analytic_interpolation(self, P, Q):
        """
        For points `P`, `Q` in the same residue disc,
        this constructs an interpolation from `P` to `Q`
        (in homogeneous coordinates) in a power series in
        the local parameter `t`, with precision equal to
        the `p`-adic precision of the underlying ring.

        INPUT:

        - ``P``, ``Q`` -- points on ``self`` in the same residue disc

        OUTPUT:

        Returns a point `X(t) = ( x(t) : y(t) : z(t) )` such that:

        (1) `X(0) = P` and `X(1) = Q` if `P, Q` are not in the infinite disc
        (2) `X(P[0]^g/P[1]) = P` and `X(Q[0]^g/Q[1]) = Q` if `P, Q` are in the infinite disc

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,8)
            sage: HK = H.change_ring(K)

        A non-Weierstrass disc::

            sage: P = HK(0,3)
            sage: Q = HK(5, 3 + 3*5^2 + 2*5^3 + 3*5^4 + 2*5^5 + 2*5^6 + 3*5^7 + O(5^8))
            sage: x,y,z, = HK.local_analytic_interpolation(P,Q)
            sage: x(0) == P[0], x(1) == Q[0], y(0) == P[1], y.polynomial()(1) == Q[1]
            (True, True, True, True)

        A finite Weierstrass disc::

            sage: P = HK.lift_x(1 + 2*5^2)
            sage: Q = HK.lift_x(1 + 3*5^2)
            sage: x,y,z = HK.local_analytic_interpolation(P,Q)
            sage: x(0) == P[0], x.polynomial()(1) == Q[0], y(0) == P[1], y(1) == Q[1]
            (True, True, True, True)

        The infinite disc::

            sage: P = HK.lift_x(5^-2)
            sage: Q = HK.lift_x(4*5^-2)
            sage: x,y,z = HK.local_analytic_interpolation(P,Q)
            sage: x = x/z
            sage: y = y/z
            sage: x(P[0]/P[1]) == P[0]
            True
            sage: x(Q[0]/Q[1]) == Q[0]
            True
            sage: y(P[0]/P[1]) == P[1]
            True
            sage: y(Q[0]/Q[1]) == Q[1]
            True

        An error if points are not in the same disc::

            sage: x,y,z = HK.local_analytic_interpolation(P,HK(1,0))
            Traceback (most recent call last):
            ...
            ValueError: (5^-2 + O(5^6) : 4*5^-3 + 4*5^-2 + 4*5^-1 + 4 + 4*5 + 3*5^3 + 5^4 + O(5^5) : 1 + O(5^8)) and (1 + O(5^8) : 0 : 1 + O(5^8)) are not in the same residue disc

        TESTS:

        Check that :issue:`26005` is fixed::

            sage: L = Qp(5, 100)
            sage: HL = H.change_ring(L)
            sage: P = HL.lift_x(1 + 2*5^2)
            sage: Q = HL.lift_x(1 + 3*5^2)
            sage: x,y,z=HL.local_analytic_interpolation(P, Q)
            sage: x.polynomial().degree()
            98

        AUTHORS:

        - Robert Bradshaw (2007-03)
        - Jennifer Balakrishnan (2010-02)
        """
    def weierstrass_points(self):
        """
        Return the Weierstrass points of ``self`` defined over
        ``self.base_ring()``, that is, the point at infinity and those points
        in the support of the divisor of `y`.

        EXAMPLES::

            sage: K = pAdicField(11, 5)
            sage: x = polygen(K)
            sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
            sage: C.weierstrass_points()
            [(0 : 1 + O(11^5) : 0), (7 + 10*11 + 4*11^3 + O(11^5) : 0 : 1 + O(11^5))]
        """
    def is_in_weierstrass_disc(self, P):
        """
        Check if `P` is in a Weierstrass disc.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,8)
            sage: HK = H.change_ring(K)
            sage: P = HK(0,3)
            sage: HK.is_in_weierstrass_disc(P)
            False
            sage: Q = HK(0,1,0)
            sage: HK.is_in_weierstrass_disc(Q)
            True
            sage: S = HK(1,0)
            sage: HK.is_in_weierstrass_disc(S)
            True
            sage: T = HK.lift_x(1+3*5^2); T
            (1 + 3*5^2 + O(5^8) : 3*5 + 4*5^2 + 5^4 + 3*5^5 + 5^6 + O(5^7) : 1 + O(5^8))
            sage: HK.is_in_weierstrass_disc(T)
            True

        AUTHOR:

        - Jennifer Balakrishnan (2010-02)
        """
    def is_weierstrass(self, P):
        """
        Check if `P` is a Weierstrass point (i.e., fixed by the hyperelliptic
        involution).

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,8)
            sage: HK = H.change_ring(K)
            sage: P = HK(0,3)
            sage: HK.is_weierstrass(P)
            False
            sage: Q = HK(0,1,0)
            sage: HK.is_weierstrass(Q)
            True
            sage: S = HK(1,0)
            sage: HK.is_weierstrass(S)
            True
            sage: T = HK.lift_x(1+3*5^2); T
            (1 + 3*5^2 + O(5^8) : 3*5 + 4*5^2 + 5^4 + 3*5^5 + 5^6 + O(5^7) : 1 + O(5^8))
            sage: HK.is_weierstrass(T)
            False

        AUTHOR:

        - Jennifer Balakrishnan (2010-02)
        """
    def find_char_zero_weier_point(self, Q):
        """
        Given `Q` a point on ``self`` in a Weierstrass disc, finds the
        center of the Weierstrass disc (if defined over ``self.base_ring()``).

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,8)
            sage: HK = H.change_ring(K)
            sage: P = HK.lift_x(1 + 2*5^2)
            sage: Q = HK.lift_x(5^-2)
            sage: S = HK(1,0)
            sage: T = HK(0,1,0)
            sage: HK.find_char_zero_weier_point(P)
            (1 + O(5^8) : 0 : 1 + O(5^8))
            sage: HK.find_char_zero_weier_point(Q)
            (0 : 1 + O(5^8) : 0)
            sage: HK.find_char_zero_weier_point(S)
            (1 + O(5^8) : 0 : 1 + O(5^8))
            sage: HK.find_char_zero_weier_point(T)
            (0 : 1 + O(5^8) : 0)

        AUTHOR:

        - Jennifer Balakrishnan
        """
    def residue_disc(self, P):
        """
        Give the residue disc of `P`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,8)
            sage: HK = H.change_ring(K)
            sage: P = HK.lift_x(1 + 2*5^2)
            sage: HK.residue_disc(P)
            (1 : 0 : 1)
            sage: Q = HK(0,3)
            sage: HK.residue_disc(Q)
            (0 : 3 : 1)
            sage: S = HK.lift_x(5^-2)
            sage: HK.residue_disc(S)
            (0 : 1 : 0)
            sage: T = HK(0,1,0)
            sage: HK.residue_disc(T)
            (0 : 1 : 0)

        AUTHOR:

        - Jennifer Balakrishnan
        """
    def is_same_disc(self, P, Q):
        """
        Check if `P,Q` are in same residue disc.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,8)
            sage: HK = H.change_ring(K)
            sage: P = HK.lift_x(1 + 2*5^2)
            sage: Q = HK.lift_x(5^-2)
            sage: S = HK(1,0)
            sage: HK.is_same_disc(P,Q)
            False
            sage: HK.is_same_disc(P,S)
            True
            sage: HK.is_same_disc(Q,S)
            False
        """
    def tiny_integrals(self, F, P, Q):
        """
        Evaluate the integrals of `f_i dx/2y` from `P` to `Q` for each `f_i` in `F`
        by formally integrating a power series in a local parameter `t`

        `P` and `Q` MUST be in the same residue disc for this result to make sense.

        INPUT:

        - ``F`` -- list of functions `f_i`
        - ``P`` -- point on ``self``
        - ``Q`` -- point on ``self`` (in the same residue disc as `P`)

        OUTPUT: the integrals `\\int_P^Q f_i dx/2y`

        EXAMPLES::

            sage: K = pAdicField(17, 5)
            sage: E = EllipticCurve(K, [-31/3, -2501/108]) # 11a
            sage: P = E(K(14/3), K(11/2))
            sage: TP = E.teichmuller(P);
            sage: x,y = E.monsky_washnitzer_gens()
            sage: E.tiny_integrals([1,x],P, TP) == E.tiny_integrals_on_basis(P,TP)
            True

        ::

            sage: K = pAdicField(11, 5)
            sage: x = polygen(K)
            sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
            sage: P = C.lift_x(11^(-2))
            sage: Q = C.lift_x(3*11^(-2))
            sage: C.tiny_integrals([1],P,Q)
            (5*11^3 + 7*11^4 + 2*11^5 + 6*11^6 + 11^7 + O(11^8))

        Note that this fails if the points are not in the same residue disc::

            sage: S = C(0,1/4)
            sage: C.tiny_integrals([1,x,x^2,x^3],P,S)
            Traceback (most recent call last):
            ...
            ValueError: (11^-2 + O(11^3) : 11^-5 + 8*11^-2 + O(11^0) : 1 + O(11^5)) and (0 : 3 + 8*11 + 2*11^2 + 8*11^3 + 2*11^4 + O(11^5) : 1 + O(11^5)) are not in the same residue disc
        """
    def tiny_integrals_on_basis(self, P, Q):
        """
        Evaluate the integrals `\\{\\int_P^Q x^i dx/2y \\}_{i=0}^{2g-1}`
        by formally integrating a power series in a local parameter `t`.
        `P` and `Q` MUST be in the same residue disc for this result to make sense.

        INPUT:

        - ``P`` -- point on ``self``
        - ``Q`` -- point on ``self`` (in the same residue disc as `P`)

        OUTPUT: the integrals `\\{\\int_P^Q x^i dx/2y \\}_{i=0}^{2g-1}`

        EXAMPLES::

            sage: K = pAdicField(17, 5)
            sage: E = EllipticCurve(K, [-31/3, -2501/108]) # 11a
            sage: P = E(K(14/3), K(11/2))
            sage: TP = E.teichmuller(P);
            sage: E.tiny_integrals_on_basis(P, TP)
            (17 + 14*17^2 + 17^3 + 8*17^4 + O(17^5), 16*17 + 5*17^2 + 8*17^3 + 14*17^4 + O(17^5))

        ::

            sage: K = pAdicField(11, 5)
            sage: x = polygen(K)
            sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
            sage: P = C.lift_x(11^(-2))
            sage: Q = C.lift_x(3*11^(-2))
            sage: C.tiny_integrals_on_basis(P,Q)
            (5*11^3 + 7*11^4 + 2*11^5 + 6*11^6 + 11^7 + O(11^8), 10*11 + 2*11^3 + 3*11^4 + 5*11^5 + O(11^6), 5*11^-1 + 8 + 4*11 + 10*11^2 + 7*11^3 + O(11^4), 2*11^-3 + 11^-2 + 11^-1 + 10 + 8*11 + O(11^2))


        Note that this fails if the points are not in the same residue disc::

            sage: S = C(0,1/4)
            sage: C.tiny_integrals_on_basis(P,S)
            Traceback (most recent call last):
            ...
            ValueError: (11^-2 + O(11^3) : 11^-5 + 8*11^-2 + O(11^0) : 1 + O(11^5)) and (0 : 3 + 8*11 + 2*11^2 + 8*11^3 + 2*11^4 + O(11^5) : 1 + O(11^5)) are not in the same residue disc
        """
    def teichmuller(self, P):
        """
        Find a Teichm\\:uller point in the same residue class of `P`.

        Because this lift of frobenius acts as `x \\mapsto x^p`,
        take the Teichmuller lift of `x` and then find a matching `y`
        from that.

        EXAMPLES::

            sage: K = pAdicField(7, 5)
            sage: E = EllipticCurve(K, [-31/3, -2501/108]) # 11a
            sage: P = E(K(14/3), K(11/2))
            sage: E.frobenius(P) == P
            False
            sage: TP = E.teichmuller(P); TP
            (0 : 2 + 3*7 + 3*7^2 + 3*7^4 + O(7^5) : 1 + O(7^5))
            sage: E.frobenius(TP) == TP
            True
            sage: (TP[0] - P[0]).valuation() > 0, (TP[1] - P[1]).valuation() > 0
            (True, True)
        """
    def coleman_integrals_on_basis(self, P, Q, algorithm=None):
        """
        Compute the Coleman integrals `\\{\\int_P^Q x^i dx/2y \\}_{i=0}^{2g-1}`.

        INPUT:

        - ``P`` -- point on ``self``
        - ``Q`` -- point on ``self``
        - ``algorithm`` -- ``None`` (default, uses Frobenius) or teichmuller
          (uses Teichmuller points)

        OUTPUT: the Coleman integrals `\\{\\int_P^Q x^i dx/2y \\}_{i=0}^{2g-1}`

        EXAMPLES::

            sage: K = pAdicField(11, 5)
            sage: x = polygen(K)
            sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
            sage: P = C.lift_x(2)
            sage: Q = C.lift_x(3)
            sage: C.coleman_integrals_on_basis(P, Q)
            (9*11^2 + 7*11^3 + 5*11^4 + O(11^5), 11 + 3*11^2 + 7*11^3 + 11^4 + O(11^5), 10*11 + 11^2 + 5*11^3 + 5*11^4 + O(11^5), 3 + 9*11^2 + 6*11^3 + 11^4 + O(11^5))
            sage: C.coleman_integrals_on_basis(P, Q, algorithm='teichmuller')
            (9*11^2 + 7*11^3 + 5*11^4 + O(11^5), 11 + 3*11^2 + 7*11^3 + 11^4 + O(11^5), 10*11 + 11^2 + 5*11^3 + 5*11^4 + O(11^5), 3 + 9*11^2 + 6*11^3 + 11^4 + O(11^5))

        ::

            sage: K = pAdicField(11,5)
            sage: x = polygen(K)
            sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
            sage: P = C(11^-2, 10*11^-5 + 10*11^-4 + 10*11^-3 + 2*11^-2 + 10*11^-1)
            sage: Q = C(3*11^-2, 11^-5 + 11^-3 + 10*11^-2 + 7*11^-1)
            sage: C.coleman_integrals_on_basis(P, Q)
            (6*11^3 + 3*11^4 + 8*11^5 + 4*11^6 + 9*11^7 + O(11^8), 11 + 10*11^2 + 8*11^3 + 7*11^4 + 5*11^5 + O(11^6), 6*11^-1 + 2 + 6*11 + 3*11^3 + O(11^4), 9*11^-3 + 9*11^-2 + 9*11^-1 + 2*11 + O(11^2))

        ::

            sage: R = C(0,1/4)
            sage: a = C.coleman_integrals_on_basis(P,R)  # long time (7s on sage.math, 2011)
            sage: b = C.coleman_integrals_on_basis(R,Q)  # long time (9s on sage.math, 2011)
            sage: c = C.coleman_integrals_on_basis(P,Q)  # long time
            sage: a+b == c  # long time
            True

        ::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,8)
            sage: HK = H.change_ring(K)
            sage: S = HK(1,0)
            sage: P = HK(0,3)
            sage: T = HK(0,1,0)
            sage: Q = HK.lift_x(5^-2)
            sage: R = HK.lift_x(4*5^-2)
            sage: HK.coleman_integrals_on_basis(S,P)
            (2*5^2 + 5^4 + 5^5 + 3*5^6 + 3*5^7 + 2*5^8 + O(5^9), 5 + 2*5^2 + 4*5^3 + 2*5^4 + 3*5^6 + 4*5^7 + 2*5^8 + O(5^9))
            sage: HK.coleman_integrals_on_basis(T,P)
            (2*5^2 + 5^4 + 5^5 + 3*5^6 + 3*5^7 + 2*5^8 + O(5^9), 5 + 2*5^2 + 4*5^3 + 2*5^4 + 3*5^6 + 4*5^7 + 2*5^8 + O(5^9))
            sage: HK.coleman_integrals_on_basis(P,S) == -HK.coleman_integrals_on_basis(S,P)
            True
            sage: HK.coleman_integrals_on_basis(S,Q)
            (5 + O(5^4), 4*5^-1 + 4 + 4*5 + 4*5^2 + O(5^3))
            sage: HK.coleman_integrals_on_basis(Q,R)
            (5 + 2*5^2 + 2*5^3 + 2*5^4 + 3*5^5 + 3*5^6 + 3*5^7 + 5^8 + O(5^9), 3*5^-1 + 2*5^4 + 5^5 + 2*5^6 + O(5^7))
            sage: HK.coleman_integrals_on_basis(S,R) == HK.coleman_integrals_on_basis(S,Q) + HK.coleman_integrals_on_basis(Q,R)
            True
            sage: HK.coleman_integrals_on_basis(T,T)
            (0, 0)
            sage: HK.coleman_integrals_on_basis(S,T)
            (0, 0)

        AUTHORS:

        - Robert Bradshaw (2007-03): non-Weierstrass points
        - Jennifer Balakrishnan and Robert Bradshaw (2010-02): Weierstrass points
        """
    coleman_integrals_on_basis_hyperelliptic = coleman_integrals_on_basis
    def coleman_integral(self, w, P, Q, algorithm: str = 'None'):
        """
        Return the Coleman integral `\\int_P^Q w`.

        INPUT:

        - ``w`` -- differential (if one of P,Q is Weierstrass, w must be odd)
        - ``P`` -- point on ``self``
        - ``Q`` -- point on ``self``
        - ``algorithm`` -- ``None`` (default, uses Frobenius) or teichmuller
          (uses Teichmuller points)

        OUTPUT: the Coleman integral `\\int_P^Q w`

        EXAMPLES:

        Example of Leprevost from Kiran Kedlaya
        The first two should be zero as `(P-Q) = 30(P-Q)` in the Jacobian
        and `dx/2y` and `x dx/2y` are holomorphic. ::

            sage: K = pAdicField(11, 6)
            sage: x = polygen(K)
            sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
            sage: P = C(-1, 1); P1 = C(-1, -1)
            sage: Q = C(0, 1/4); Q1 = C(0, -1/4)
            sage: x, y = C.monsky_washnitzer_gens()
            sage: w = C.invariant_differential()
            sage: w.coleman_integral(P, Q)
            O(11^6)
            sage: C.coleman_integral(x*w, P, Q)
            O(11^6)
            sage: C.coleman_integral(x^2*w, P, Q)
            7*11 + 6*11^2 + 3*11^3 + 11^4 + 5*11^5 + O(11^6)

        ::

            sage: p = 71; m = 4
            sage: K = pAdicField(p, m)
            sage: x = polygen(K)
            sage: C = HyperellipticCurve(x^5 + 33/16*x^4 + 3/4*x^3 + 3/8*x^2 - 1/4*x + 1/16)
            sage: P = C(-1, 1); P1 = C(-1, -1)
            sage: Q = C(0, 1/4); Q1 = C(0, -1/4)
            sage: x, y = C.monsky_washnitzer_gens()
            sage: w = C.invariant_differential()
            sage: w.integrate(P, Q), (x*w).integrate(P, Q)
            (O(71^4), O(71^4))
            sage: R, R1 = C.lift_x(4, all=True)
            sage: w.integrate(P, R)
            50*71 + 3*71^2 + 43*71^3 + O(71^4)
            sage: w.integrate(P, R) + w.integrate(P1, R1)
            O(71^4)

        A simple example, integrating dx::

            sage: R.<x> = QQ['x']
            sage: E= HyperellipticCurve(x^3-4*x+4)
            sage: K = Qp(5,10)
            sage: EK = E.change_ring(K)
            sage: P = EK(2, 2)
            sage: Q = EK.teichmuller(P)
            sage: x, y = EK.monsky_washnitzer_gens()
            sage: EK.coleman_integral(x.diff(), P, Q)
            5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + 2*5^6 + 3*5^7 + 3*5^9 + O(5^10)
            sage: Q[0] - P[0]
            5 + 2*5^2 + 5^3 + 3*5^4 + 4*5^5 + 2*5^6 + 3*5^7 + 3*5^9 + O(5^10)

        Yet another example::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x*(x-1)*(x+9))
            sage: K = Qp(7,10)
            sage: HK = H.change_ring(K)
            sage: import sage.schemes.hyperelliptic_curves.monsky_washnitzer as mw
            sage: M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(HK)
            sage: w = HK.invariant_differential()
            sage: x,y = HK.monsky_washnitzer_gens()
            sage: f = forms[0]
            sage: S = HK(9,36)
            sage: Q = HK.teichmuller(S)
            sage: P = HK(-1,4)
            sage: b = x*w*w._coeff.parent()(f)
            sage: HK.coleman_integral(b,P,Q)
            7 + 7^2 + 4*7^3 + 5*7^4 + 3*7^5 + 7^6 + 5*7^7 + 3*7^8 + 4*7^9 + 4*7^10 + O(7^11)

        ::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3+1)
            sage: K = Qp(5,8)
            sage: HK = H.change_ring(K)
            sage: w = HK.invariant_differential()
            sage: P = HK(0,1)
            sage: Q = HK(5, 1 + 3*5^3 + 2*5^4 + 2*5^5 + 3*5^7)
            sage: x,y = HK.monsky_washnitzer_gens()
            sage: (2*y*w).coleman_integral(P,Q)
            5 + O(5^9)
            sage: xloc,yloc,zloc = HK.local_analytic_interpolation(P,Q)
            sage: I2 = (xloc.derivative()/(2*yloc)).integral()
            sage: I2.polynomial()(1) - I2(0)
            3*5 + 2*5^2 + 2*5^3 + 5^4 + 4*5^6 + 5^7 + O(5^9)
            sage: HK.coleman_integral(w,P,Q)
            3*5 + 2*5^2 + 2*5^3 + 5^4 + 4*5^6 + 5^7 + O(5^9)

        Integrals involving Weierstrass points::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,8)
            sage: HK = H.change_ring(K)
            sage: S = HK(1,0)
            sage: P = HK(0,3)
            sage: negP = HK(0,-3)
            sage: T = HK(0,1,0)
            sage: w = HK.invariant_differential()
            sage: x,y = HK.monsky_washnitzer_gens()
            sage: HK.coleman_integral(w*x^3,S,T)
            0
            sage: HK.coleman_integral(w*x^3,T,S)
            0
            sage: HK.coleman_integral(w,S,P)
            2*5^2 + 5^4 + 5^5 + 3*5^6 + 3*5^7 + 2*5^8 + O(5^9)
            sage: HK.coleman_integral(w,T,P)
            2*5^2 + 5^4 + 5^5 + 3*5^6 + 3*5^7 + 2*5^8 + O(5^9)
            sage: HK.coleman_integral(w*x^3,T,P)
            5^2 + 2*5^3 + 3*5^6 + 3*5^7 + O(5^8)
            sage: HK.coleman_integral(w*x^3,S,P)
            5^2 + 2*5^3 + 3*5^6 + 3*5^7 + O(5^8)
            sage: HK.coleman_integral(w, P, negP, algorithm='teichmuller')
            5^2 + 4*5^3 + 2*5^4 + 2*5^5 + 3*5^6 + 2*5^7 + 4*5^8 + O(5^9)
            sage: HK.coleman_integral(w, P, negP)
            5^2 + 4*5^3 + 2*5^4 + 2*5^5 + 3*5^6 + 2*5^7 + 4*5^8 + O(5^9)

        AUTHORS:

        - Robert Bradshaw (2007-03)
        - Kiran Kedlaya (2008-05)
        - Jennifer Balakrishnan (2010-02)
        """
    def frobenius(self, P=None):
        """
        Return the `p`-th power lift of Frobenius of `P`.

        EXAMPLES::

            sage: K = Qp(11, 5)
            sage: R.<x> = K[]
            sage: E = HyperellipticCurve(x^5 - 21*x - 20)
            sage: P = E.lift_x(2)
            sage: E.frobenius(P)
            (2 + 10*11 + 5*11^2 + 11^3 + O(11^5) : 6 + 11 + 8*11^2 + 8*11^3 + 10*11^4 + O(11^5) : 1 + O(11^5))
            sage: Q = E.teichmuller(P); Q
            (2 + 10*11 + 4*11^2 + 9*11^3 + 11^4 + O(11^5) : 6 + 11 + 4*11^2 + 9*11^3 + 4*11^4 + O(11^5) : 1 + O(11^5))
            sage: E.frobenius(Q)
            (2 + 10*11 + 4*11^2 + 9*11^3 + 11^4 + O(11^5) : 6 + 11 + 4*11^2 + 9*11^3 + 4*11^4 + O(11^5) : 1 + O(11^5))

        ::

            sage: R.<x> = QQ[]
            sage: H = HyperellipticCurve(x^5-23*x^3+18*x^2+40*x)
            sage: Q = H(0,0)
            sage: u,v = H.local_coord(Q,prec=100)
            sage: K = Qp(11,5)
            sage: L.<a> = K.extension(x^20-11)
            sage: HL = H.change_ring(L)
            sage: S = HL(u(a),v(a))
            sage: HL.frobenius(S)
            (8*a^22 + 10*a^42 + 4*a^44 + 2*a^46 + 9*a^48 + 8*a^50 + a^52 + 7*a^54 +
            7*a^56 + 5*a^58 + 9*a^62 + 5*a^64 + a^66 + 6*a^68 + a^70 + 6*a^74 +
            2*a^76 + 2*a^78 + 4*a^82 + 5*a^84 + 2*a^86 + 7*a^88 + a^90 + 6*a^92 +
            a^96 + 5*a^98 + 2*a^102 + 2*a^106 + 6*a^108 + 8*a^110 + 3*a^112 +
            a^114 + 8*a^116 + 10*a^118 + 3*a^120 + O(a^122) :
            a^11 + 7*a^33 + 7*a^35 + 4*a^37 + 6*a^39 + 9*a^41 + 8*a^43 + 8*a^45 +
            a^47 + 7*a^51 + 4*a^53 + 5*a^55 + a^57 + 7*a^59 + 5*a^61 + 9*a^63 +
            4*a^65 + 10*a^69 + 3*a^71 + 2*a^73 + 9*a^75 + 10*a^77 + 6*a^79 +
            10*a^81 + 7*a^85 + a^87 + 4*a^89 + 8*a^91 + a^93 + 8*a^95 + 2*a^97 +
            7*a^99 + a^101 + 3*a^103 + 6*a^105 + 7*a^107 + 4*a^109 + O(a^111) :
            1 + O(a^100))

        AUTHORS:

        - Robert Bradshaw and Jennifer Balakrishnan (2010-02)
        """
    def newton_sqrt(self, f, x0, prec):
        """
        Take the square root of the power series `f` by Newton's method.

        NOTE:

        this function should eventually be moved to `p`-adic power series ring

        INPUT:

        - ``f`` -- power series with coefficients in `\\QQ_p` or an extension
        - ``x0`` -- seeds the Newton iteration
        - ``prec`` -- precision

        OUTPUT: the square root of `f`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^5-23*x^3+18*x^2+40*x)
            sage: Q = H(0,0)
            sage: u,v = H.local_coord(Q,prec=100)
            sage: K = Qp(11,5)
            sage: HK = H.change_ring(K)
            sage: L.<a> = K.extension(x^20-11)
            sage: HL = H.change_ring(L)
            sage: S = HL(u(a),v(a))
            sage: f = H.hyperelliptic_polynomials()[0]
            sage: y = HK.newton_sqrt( f(u(a)^11), a^11,5)
            sage: y^2 - f(u(a)^11)
            O(a^122)

        AUTHOR:

        - Jennifer Balakrishnan
        """
    def curve_over_ram_extn(self, deg):
        """
        Return ``self`` over `\\QQ_p(p^(1/deg))`.

        INPUT:

        - ``deg`` -- the degree of the ramified extension

        OUTPUT: ``self`` over `\\QQ_p(p^(1/deg))`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^5-23*x^3+18*x^2+40*x)
            sage: K = Qp(11,5)
            sage: HK = H.change_ring(K)
            sage: HL = HK.curve_over_ram_extn(2)
            sage: HL
            Hyperelliptic Curve over 11-adic Eisenstein Extension Field in a defined by x^2 - 11 defined by (1 + O(a^10))*y^2 = (1 + O(a^10))*x^5 + (10 + 8*a^2 + 10*a^4 + 10*a^6 + 10*a^8 + O(a^10))*x^3 + (7 + a^2 + O(a^10))*x^2 + (7 + 3*a^2 + O(a^10))*x

        AUTHOR:

        - Jennifer Balakrishnan
        """
    def get_boundary_point(self, curve_over_extn, P):
        """
        Given ``self`` over an extension field, find a point in the disc of `P`
        near the boundary.

        INPUT:

        - ``curve_over_extn`` -- ``self`` over a totally ramified extension
        - ``P`` -- Weierstrass point

        OUTPUT: a point in the disc of `P` near the boundary

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(3,6)
            sage: HK = H.change_ring(K)
            sage: P = HK(1,0)
            sage: J.<a> = K.extension(x^30-3)
            sage: HJ  = H.change_ring(J)
            sage: S = HK.get_boundary_point(HJ,P)
            sage: S
            (1 + 2*a^2 + 2*a^6 + 2*a^18 + a^32 + a^34 + a^36 + 2*a^38 + 2*a^40 + a^42 + 2*a^44 + a^48 + 2*a^50 + 2*a^52 + a^54 + a^56 + 2*a^60 + 2*a^62 + a^70 + 2*a^72 + a^76 + 2*a^78 + a^82 + a^88 + a^96 + 2*a^98 + 2*a^102 + a^104 + 2*a^106 + a^108 + 2*a^110 + a^112 + 2*a^116 + a^126 + 2*a^130 + 2*a^132 + a^144 + 2*a^148 + 2*a^150 + a^152 + 2*a^154 + a^162 + a^164 + a^166 + a^168 + a^170 + a^176 + a^178 + O(a^180) : a + O(a^180) : 1 + O(a^180))

        AUTHOR:

        - Jennifer Balakrishnan
        """
    def P_to_S(self, P, S):
        """
        Given a finite Weierstrass point `P` and a point `S` in the same disc,
        compute the Coleman integrals `\\{\\int_P^S x^i dx/2y \\}_{i=0}^{2g-1}`.

        INPUT:

        - ``P`` -- finite Weierstrass point
        - ``S`` -- point in disc of `P`

        OUTPUT: Coleman integrals `\\{\\int_P^S x^i dx/2y \\}_{i=0}^{2g-1}`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,4)
            sage: HK = H.change_ring(K)
            sage: P = HK(1,0)
            sage: HJ = HK.curve_over_ram_extn(10)
            sage: S = HK.get_boundary_point(HJ,P)
            sage: HK.P_to_S(P, S)
            (2*a + 4*a^3 + 2*a^11 + 4*a^13 + 2*a^17 + 2*a^19 + a^21 + 4*a^23 + a^25 + 2*a^27 + 2*a^29 + 3*a^31 + 4*a^33 + O(a^35), a^-5 + 2*a + 2*a^3 + a^7 + 3*a^11 + a^13 + 3*a^15 + 3*a^17 + 2*a^19 + 4*a^21 + 4*a^23 + 4*a^25 + 2*a^27 + a^29 + a^31 + O(a^33))

        AUTHOR:

        - Jennifer Balakrishnan
        """
    def coleman_integral_P_to_S(self, w, P, S):
        """
        Given a finite Weierstrass point `P` and a point `S`
        in the same disc, compute the Coleman integral `\\int_P^S w`.

        INPUT:

        - ``w`` -- differential
        - ``P`` -- Weierstrass point
        - ``S`` -- point in the same disc of `P` (S is defined over an extension
          of `\\QQ_p`; coordinates of S are given in terms of uniformizer `a`)

        OUTPUT: Coleman integral `\\int_P^S w` in terms of `a`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,4)
            sage: HK = H.change_ring(K)
            sage: P = HK(1,0)
            sage: J.<a> = K.extension(x^10-5)
            sage: HJ  = H.change_ring(J)
            sage: S = HK.get_boundary_point(HJ,P)
            sage: x,y = HK.monsky_washnitzer_gens()
            sage: S[0]-P[0] == HK.coleman_integral_P_to_S(x.diff(),P,S)
            True
            sage: HK.coleman_integral_P_to_S(HK.invariant_differential(),P,S) == HK.P_to_S(P,S)[0]
            True

        AUTHOR:

        - Jennifer Balakrishnan
        """
    def S_to_Q(self, S, Q):
        """
        Given `S` a point on ``self`` over an extension field, compute the
        Coleman integrals `\\{\\int_S^Q x^i dx/2y \\}_{i=0}^{2g-1}`.

        **one should be able to feed `S,Q` into coleman_integral,
        but currently that segfaults**

        INPUT:

        - ``S`` -- a point with coordinates in an extension of `\\QQ_p` (with unif. a)
        - ``Q`` -- a non-Weierstrass point defined over `\\QQ_p`

        OUTPUT:

        The Coleman integrals `\\{\\int_S^Q x^i dx/2y \\}_{i=0}^{2g-1}` in terms of `a`.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,6)
            sage: HK = H.change_ring(K)
            sage: J.<a> = K.extension(x^20-5)
            sage: HJ  = H.change_ring(J)
            sage: w = HK.invariant_differential()
            sage: x,y = HK.monsky_washnitzer_gens()
            sage: P = HK(1,0)
            sage: Q = HK(0,3)
            sage: S = HK.get_boundary_point(HJ,P)
            sage: P_to_S = HK.P_to_S(P,S)
            sage: S_to_Q = HJ.S_to_Q(S,Q)
            sage: P_to_S + S_to_Q
            (2*a^40 + a^80 + a^100 + O(a^105), a^20 + 2*a^40 + 4*a^60 + 2*a^80 + O(a^103))
            sage: HK.coleman_integrals_on_basis(P,Q)
            (2*5^2 + 5^4 + 5^5 + 3*5^6 + O(5^7), 5 + 2*5^2 + 4*5^3 + 2*5^4 + 5^6 + O(5^7))

        AUTHOR:

        - Jennifer Balakrishnan
        """
    def coleman_integral_S_to_Q(self, w, S, Q):
        """
        Compute the Coleman integral `\\int_S^Q w`.

        **one should be able to feed `S,Q` into coleman_integral,
        but currently that segfaults**

        INPUT:

        - ``w`` -- a differential
        - ``S`` -- a point with coordinates in an extension of `\\QQ_p`
        - ``Q`` -- a non-Weierstrass point defined over `\\QQ_p`

        OUTPUT: the Coleman integral `\\int_S^Q w`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,6)
            sage: HK = H.change_ring(K)
            sage: J.<a> = K.extension(x^20-5)
            sage: HJ  = H.change_ring(J)
            sage: x,y = HK.monsky_washnitzer_gens()
            sage: P = HK(1,0)
            sage: Q = HK(0,3)
            sage: S = HK.get_boundary_point(HJ,P)
            sage: P_to_S = HK.coleman_integral_P_to_S(y.diff(),P,S)
            sage: S_to_Q = HJ.coleman_integral_S_to_Q(y.diff(),S,Q)
            sage: P_to_S  + S_to_Q
            3 + O(a^119)
            sage: HK.coleman_integral(y.diff(),P,Q)
            3 + O(5^6)

        AUTHOR:

        - Jennifer Balakrishnan
        """
    def coleman_integral_from_weierstrass_via_boundary(self, w, P, Q, d):
        """
        Compute the Coleman integral `\\int_P^Q w` via a boundary point
        in the disc of `P`, defined over a degree `d` extension

        INPUT:

        - ``w`` -- a differential
        - ``P`` -- a Weierstrass point
        - ``Q`` -- a non-Weierstrass point
        - ``d`` -- degree of extension where coordinates of boundary point lie

        OUTPUT:

        the Coleman integral `\\int_P^Q w`, written in terms of the uniformizer
        `a` of the degree `d` extension

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3-10*x+9)
            sage: K = Qp(5,6)
            sage: HK = H.change_ring(K)
            sage: P = HK(1,0)
            sage: Q = HK(0,3)
            sage: x,y = HK.monsky_washnitzer_gens()
            sage: HK.coleman_integral_from_weierstrass_via_boundary(y.diff(),P,Q,20)
            3 + O(a^119)
            sage: HK.coleman_integral(y.diff(),P,Q)
            3 + O(5^6)
            sage: w = HK.invariant_differential()
            sage: HK.coleman_integral_from_weierstrass_via_boundary(w,P,Q,20)
            2*a^40 + a^80 + a^100 + O(a^105)
            sage: HK.coleman_integral(w,P,Q)
            2*5^2 + 5^4 + 5^5 + 3*5^6 + O(5^7)

        AUTHOR:

        - Jennifer Balakrishnan
        """
