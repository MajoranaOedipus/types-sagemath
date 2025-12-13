import sage.schemes.curves.projective_curve as plane_curve
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.big_oh import O as O
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.real_mpfr import RR as RR
from sage.structure.category_object import normalize_names as normalize_names

def is_HyperellipticCurve(C):
    """
    EXAMPLES::

        sage: from sage.schemes.hyperelliptic_curves.hyperelliptic_generic import is_HyperellipticCurve
        sage: R.<x> = QQ[]; C = HyperellipticCurve(x^3 + x - 1); C
        Hyperelliptic Curve over Rational Field defined by y^2 = x^3 + x - 1
        sage: is_HyperellipticCurve(C)
        doctest:warning...
        DeprecationWarning: The function is_HyperellipticCurve is deprecated; use 'isinstance(..., HyperellipticCurve_generic)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True
    """

class HyperellipticCurve_generic(plane_curve.ProjectivePlaneCurve):
    """
    TESTS::

        sage: P.<x> = QQ[]
        sage: f0 = 4*x^5 - 30*x^3 + 45*x - 22
        sage: C0 = HyperellipticCurve(f0)
        sage: f1 = x^5 - x^3 + x - 22
        sage: C1 = HyperellipticCurve(f1)
        sage: C0 == C1
        False
        sage: C0 == C0
        True

        sage: P.<x> = QQ[]
        sage: f0 = 4*x^5 - 30*x^3 + 45*x - 22
        sage: C0 = HyperellipticCurve(f0)
        sage: f1 = x^5 - x^3 + x - 22
        sage: C1 = HyperellipticCurve(f1)
        sage: C0 != C1
        True
        sage: C0 != C0
        False

        sage: P.<x> = QQ[]
        sage: f0 = 4*x^5 - 30*x^3 + 45*x - 22
        sage: C0 = HyperellipticCurve(f0)
        sage: f1 = x^5 - x^3 + x - 22
        sage: C1 = HyperellipticCurve(f1)
        sage: Q.<y> = GF(5)[]
        sage: f2 = y^5 - y^3 + y - 22
        sage: C2 = HyperellipticCurve(f2)
        sage: hash(C0) == hash(C0)
        True
        sage: hash(C0) == hash(C1)
        False
        sage: hash(C1) == hash(C2)
        False
    """
    def __init__(self, PP, f, h=None, names=None, genus=None) -> None: ...
    def change_ring(self, R):
        """
        Return this HyperellipticCurve over a new base ring ``R``.

        EXAMPLES::

            sage: # needs sage.rings.padics
            sage: R.<x> = QQ[]
            sage: H = HyperellipticCurve(x^5 - 10*x + 9)
            sage: K = Qp(3, 5)
            sage: L.<a> = K.extension(x^30 - 3)
            sage: HK = H.change_ring(K)
            sage: HL = HK.change_ring(L); HL
            Hyperelliptic Curve
             over 3-adic Eisenstein Extension Field in a defined by x^30 - 3
             defined by (1 + O(a^150))*y^2 = (1 + O(a^150))*x^5
              + (2 + 2*a^30 + a^60 + 2*a^90 + 2*a^120 + O(a^150))*x + a^60 + O(a^210)

            sage: R.<x> = FiniteField(7)[]
            sage: H = HyperellipticCurve(x^8 + x + 5)
            sage: H.base_extend(FiniteField(7^2, 'a'))                                  # needs sage.rings.finite_rings
            Hyperelliptic Curve over Finite Field in a of size 7^2
             defined by y^2 = x^8 + x + 5
        """
    base_extend = change_ring
    def hyperelliptic_polynomials(self, K=None, var: str = 'x'):
        """
        EXAMPLES::

            sage: R.<x> = QQ[]; C = HyperellipticCurve(x^3 + x - 1, x^3/5); C
            Hyperelliptic Curve over Rational Field defined by y^2 + 1/5*x^3*y = x^3 + x - 1
            sage: C.hyperelliptic_polynomials()
            (x^3 + x - 1, 1/5*x^3)
        """
    def is_singular(self):
        """
        Return ``False``, because hyperelliptic curves are smooth projective
        curves, as checked on construction.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: H = HyperellipticCurve(x^5 + 1)
            sage: H.is_singular()
            False

        A hyperelliptic curve with genus at least 2 always has a singularity at
        infinity when viewed as a *plane* projective curve. This can be seen in
        the following example.::

            sage: R.<x> = QQ[]
            sage: H = HyperellipticCurve(x^5 + 2)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(-1)
            sage: H.is_singular()
            False
            sage: from sage.schemes.curves.projective_curve import ProjectivePlaneCurve
            sage: ProjectivePlaneCurve.is_singular(H)
            True
        """
    def is_smooth(self):
        """
        Return ``True``, because hyperelliptic curves are smooth projective
        curves, as checked on construction.

        EXAMPLES::

            sage: R.<x> = GF(13)[]
            sage: H = HyperellipticCurve(x^8 + 1)
            sage: H.is_smooth()
            True

        A hyperelliptic curve with genus at least 2 always has a singularity at
        infinity when viewed as a *plane* projective curve. This can be seen in
        the following example.::

            sage: # needs sage.rings.finite_rings
            sage: R.<x> = GF(27, 'a')[]
            sage: H = HyperellipticCurve(x^10 + 2)
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(-1)
            sage: H.is_smooth()
            True
            sage: from sage.schemes.curves.projective_curve import ProjectivePlaneCurve
            sage: ProjectivePlaneCurve.is_smooth(H)
            False
        """
    def is_x_coord(self, x):
        """
        Return ``True`` if ``x`` is the `x`-coordinate of a point on this curve.

        .. SEEALSO::

            See also :meth:`lift_x` to find the point(s) with a given
            `x`-coordinate.  This function may be useful in cases where
            testing an element of the base field for being a square is
            faster than finding its square root.

        INPUT:

        - ``x`` -- an element of the base ring of the curve

        OUTPUT: boolean stating whether or not `x` is a x-coordinate of a point
        on the curve

        EXAMPLES:

        When `x` is the `x`-coordinate of a rational point on the
        curve, we can request these::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = x^5 + x^3 + 1
            sage: H = HyperellipticCurve(f)
            sage: H.is_x_coord(0)
            True

        There are no rational points with `x`-coordinate 3::

            sage: H.is_x_coord(3)
            False

        The function also handles the case when `h(x)` is not zero::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = x^5 + x^3 + 1
            sage: h = x + 1
            sage: H = HyperellipticCurve(f, h)
            sage: H.is_x_coord(1)
            True

        We can perform these operations over finite fields too::

            sage: # needs sage.rings.finite_rings
            sage: R.<x> = PolynomialRing(GF(163))
            sage: f = x^7 + x + 1
            sage: H = HyperellipticCurve(f)
            sage: H.is_x_coord(13)
            True

        Including the case of characteristic two::

            sage: # needs sage.rings.finite_rings
            sage: F.<z4> = GF(2^4)
            sage: R.<x> = PolynomialRing(F)
            sage: f = x^7 + x^3 + 1
            sage: h = x + 1
            sage: H = HyperellipticCurve(f, h)
            sage: H.is_x_coord(z4^3 + z4^2 + z4)
            True

        AUTHORS:

        - Giacomo Pope (2024): adapted from :meth:`lift_x`

        TESTS:

        The `x`-coordinate must be defined over the base field of the curve::

            sage: p = 11
            sage: F = GF(11)
            sage: F_ext = GF(11^2)
            sage: R.<x> = PolynomialRing(F)
            sage: f = x^7 + x^3 + 1
            sage: H = HyperellipticCurve(f)
            sage: H.is_x_coord(F_ext.gen())
            Traceback (most recent call last):
            ...
            TypeError: x must be coercible into the base ring of the curve
        """
    def lift_x(self, x, all: bool = False):
        """
        Return one or all points with given `x`-coordinate.

        This method is deterministic: It returns the same data each
        time when called again with the same `x`.

        INPUT:

        - ``x`` -- an element of the base ring of the curve

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          (possibly empty) list of all points. If ``False``, return
          just one point, or raise a :exc:`ValueError` if there are none.

        OUTPUT: a point or list of up to two points on this curve

        .. SEEALSO::

            :meth:`is_x_coord`

        AUTHORS:

        - Giacomo Pope (2024): Allowed for the case of characteristic two

        EXAMPLES:

        When `x` is the `x`-coordinate of a rational point on the
        curve, we can request these::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = x^5 + x^3 + 1
            sage: H = HyperellipticCurve(f)
            sage: H.lift_x(0)
            (0 : -1 : 1)
            sage: H.lift_x(4, all=True)
            [(4 : -33 : 1), (4 : 33 : 1)]

        There are no rational points with `x`-coordinate 3::

            sage: H.lift_x(3)
            Traceback (most recent call last):
            ...
            ValueError: No point with x-coordinate 3 on Hyperelliptic Curve over Rational Field defined by y^2 = x^5 + x^3 + 1

        An empty list is returned when there are no points and ``all=True``::

            sage: H.lift_x(3, all=True)
            []

        The function also handles the case when `h(x)` is not zero::

            sage: R.<x> = PolynomialRing(QQ)
            sage: f = x^5 + x^3 + 1
            sage: h = x + 1
            sage: H = HyperellipticCurve(f, h)
            sage: H.lift_x(1)
            (1 : -3 : 1)

        We can perform these operations over finite fields too::

            sage: # needs sage.rings.finite_rings
            sage: R.<x> = PolynomialRing(GF(163))
            sage: f = x^7 + x + 1
            sage: H = HyperellipticCurve(f)
            sage: H.lift_x(13)
            (13 : 41 : 1)

        Including the case of characteristic two::

            sage: # needs sage.rings.finite_rings
            sage: F.<z4> = GF(2^4)
            sage: R.<x> = PolynomialRing(F)
            sage: f = x^7 + x^3 + 1
            sage: h = x + 1
            sage: H = HyperellipticCurve(f, h)
            sage: H.lift_x(z4^3 + z4^2 + z4, all=True)
            [(z4^3 + z4^2 + z4 : z4^2 + z4 + 1 : 1), (z4^3 + z4^2 + z4 : z4^3 : 1)]

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: F1 = GF(11)
            sage: F2 = GF(13)
            sage: R.<x> = PolynomialRing(F1)
            sage: f = x^7 + x^3 + 1
            sage: H = HyperellipticCurve(f)
            sage: H.lift_x(F2.random_element())
            Traceback (most recent call last):
            ...
            ValueError: x must have a common parent with the base ring

        Ensure that :issue:`37097` is fixed::

            sage: # needs sage.rings.finite_rings
            sage: F.<z4> = GF(2^4)
            sage: R.<x> = PolynomialRing(F)
            sage: f = x^7 + x^3 + 1
            sage: h = x + 1
            sage: H = HyperellipticCurve(f, h)
            sage: H.lift_x(z4^3 + z4^2 + z4, all=True)
            [(z4^3 + z4^2 + z4 : z4^2 + z4 + 1 : 1), (z4^3 + z4^2 + z4 : z4^3 : 1)]
        """
    def genus(self): ...
    def jacobian(self): ...
    def odd_degree_model(self):
        '''
        Return an odd degree model of ``self``, or raise :exc:`ValueError` if
        one does not exist over the field of definition.

        EXAMPLES::

            sage: x = QQ[\'x\'].gen()
            sage: H = HyperellipticCurve((x^2 + 2)*(x^2 + 3)*(x^2 + 5)); H
            Hyperelliptic Curve over Rational Field defined by y^2 = x^6 + 10*x^4 + 31*x^2 + 30
            sage: H.odd_degree_model()
            Traceback (most recent call last):
            ...
            ValueError: No odd degree model exists over field of definition

            sage: K2 = QuadraticField(-2, \'a\')                                          # needs sage.rings.number_field
            sage: Hp2 = H.change_ring(K2).odd_degree_model(); Hp2                       # needs sage.rings.number_field
            Hyperelliptic Curve over Number Field in a
             with defining polynomial x^2 + 2 with a = 1.414213562373095?*I
             defined by y^2 = 6*a*x^5 - 29*x^4 - 20*x^2 + 6*a*x + 1

            sage: K3 = QuadraticField(-3, \'b\')                                          # needs sage.rings.number_field
            sage: Hp3 = H.change_ring(QuadraticField(-3, \'b\')).odd_degree_model(); Hp3  # needs sage.rings.number_field
            Hyperelliptic Curve over Number Field in b
             with defining polynomial x^2 + 3 with b = 1.732050807568878?*I
             defined by y^2 = -4*b*x^5 - 14*x^4 - 20*b*x^3 - 35*x^2 + 6*b*x + 1

            Of course, ``Hp2`` and ``Hp3`` are isomorphic over the composite
            extension.  One consequence of this is that odd degree models
            reduced over "different" fields should have the same number of
            points on their reductions.  43 and 67 split completely in the
            compositum, so when we reduce we find:

            sage: # needs sage.rings.number_field
            sage: P2 = K2.factor(43)[0][0]
            sage: P3 = K3.factor(43)[0][0]
            sage: Hp2.change_ring(K2.residue_field(P2)).frobenius_polynomial()
            x^4 - 16*x^3 + 134*x^2 - 688*x + 1849
            sage: Hp3.change_ring(K3.residue_field(P3)).frobenius_polynomial()
            x^4 - 16*x^3 + 134*x^2 - 688*x + 1849

            sage: H.change_ring(GF(43)).odd_degree_model().frobenius_polynomial()       # needs sage.rings.finite_rings
            x^4 - 16*x^3 + 134*x^2 - 688*x + 1849

            sage: # needs sage.rings.number_field
            sage: P2 = K2.factor(67)[0][0]
            sage: P3 = K3.factor(67)[0][0]
            sage: Hp2.change_ring(K2.residue_field(P2)).frobenius_polynomial()
            x^4 - 8*x^3 + 150*x^2 - 536*x + 4489
            sage: Hp3.change_ring(K3.residue_field(P3)).frobenius_polynomial()
            x^4 - 8*x^3 + 150*x^2 - 536*x + 4489

            sage: H.change_ring(GF(67)).odd_degree_model().frobenius_polynomial()       # needs sage.rings.finite_rings
            x^4 - 8*x^3 + 150*x^2 - 536*x + 4489

        TESTS::

            sage: HyperellipticCurve(x^5 + 1, 1).odd_degree_model()
            Traceback (most recent call last):
            ...
            NotImplementedError: odd_degree_model only implemented for curves in Weierstrass form

            sage: HyperellipticCurve(x^5 + 1, names="U, V").odd_degree_model()
            Hyperelliptic Curve over Rational Field defined by V^2 = U^5 + 1
        '''
    def has_odd_degree_model(self) -> bool:
        """
        Return ``True`` if an odd degree model of ``self`` exists over the
        field of definition; ``False`` otherwise.

        Use ``odd_degree_model`` to calculate an odd degree model.

        EXAMPLES::

            sage: x = QQ['x'].0
            sage: HyperellipticCurve(x^5 + x).has_odd_degree_model()
            True
            sage: HyperellipticCurve(x^6 + x).has_odd_degree_model()
            True
            sage: HyperellipticCurve(x^6 + x + 1).has_odd_degree_model()
            False
        """
    def monsky_washnitzer_gens(self): ...
    def invariant_differential(self):
        """
        Return `dx/2y`, as an element of the Monsky-Washnitzer cohomology
        of ``self``.

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: C = HyperellipticCurve(x^5 - 4*x + 4)
            sage: C.invariant_differential()
            1 dx/2y
        """
    def local_coordinates_at_nonweierstrass(self, P, prec: int = 20, name: str = 't'):
        """
        For a non-Weierstrass point `P = (a,b)` on the hyperelliptic
        curve `y^2 = f(x)`, return `(x(t), y(t))` such that `(y(t))^2 = f(x(t))`,
        where `t = x - a` is the local parameter.

        INPUT:

        - ``P = (a, b)`` -- a non-Weierstrass point on ``self``
        - ``prec`` -- desired precision of the local coordinates
        - ``name`` -- gen of the power series ring (default: ``t``)

        OUTPUT:

        `(x(t),y(t))` such that `y(t)^2 = f(x(t))` and `t = x - a`
        is the local parameter at `P`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^5 - 23*x^3 + 18*x^2 + 40*x)
            sage: P = H(1, 6)
            sage: x, y = H.local_coordinates_at_nonweierstrass(P, prec=5)
            sage: x
            1 + t + O(t^5)
            sage: y
            6 + t - 7/2*t^2 - 1/2*t^3 - 25/48*t^4 + O(t^5)
            sage: Q = H(-2, 12)
            sage: x, y = H.local_coordinates_at_nonweierstrass(Q, prec=5)
            sage: x
            -2 + t + O(t^5)
            sage: y
            12 - 19/2*t - 19/32*t^2 + 61/256*t^3 - 5965/24576*t^4 + O(t^5)

        AUTHOR:

        - Jennifer Balakrishnan (2007-12)
        """
    def local_coordinates_at_weierstrass(self, P, prec: int = 20, name: str = 't'):
        """
        For a finite Weierstrass point on the hyperelliptic
        curve `y^2 = f(x)`, returns `(x(t), y(t))` such that
        `(y(t))^2 = f(x(t))`, where `t = y` is the local parameter.

        INPUT:

        - ``P`` -- a finite Weierstrass point on ``self``
        - ``prec`` -- desired precision of the local coordinates
        - ``name`` -- gen of the power series ring (default: `t`)

        OUTPUT:

        `(x(t),y(t))` such that `y(t)^2 = f(x(t))` and `t = y`
        is the local parameter at `P`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^5 - 23*x^3 + 18*x^2 + 40*x)
            sage: A = H(4, 0)
            sage: x, y = H.local_coordinates_at_weierstrass(A, prec=7)
            sage: x
            4 + 1/360*t^2 - 191/23328000*t^4 + 7579/188956800000*t^6 + O(t^7)
            sage: y
            t + O(t^7)
            sage: B = H(-5, 0)
            sage: x, y = H.local_coordinates_at_weierstrass(B, prec=5)
            sage: x
            -5 + 1/1260*t^2 + 887/2000376000*t^4 + O(t^5)
            sage: y
            t + O(t^5)

        AUTHOR:
          - Jennifer Balakrishnan (2007-12)

            - Francis Clarke (2012-08-26)
        """
    def local_coordinates_at_infinity(self, prec: int = 20, name: str = 't'):
        """
        For the genus `g` hyperelliptic curve `y^2 = f(x)`, return
        `(x(t), y(t))` such that `(y(t))^2 = f(x(t))`, where `t = x^g/y` is
        the local parameter at infinity

        INPUT:

        - ``prec`` -- desired precision of the local coordinates
        - ``name`` -- generator of the power series ring (default: ``t``)

        OUTPUT:

        `(x(t),y(t))` such that `y(t)^2 = f(x(t))` and `t = x^g/y`
        is the local parameter at infinity

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^5 - 5*x^2 + 1)
            sage: x, y = H.local_coordinates_at_infinity(10)
            sage: x
            t^-2 + 5*t^4 - t^8 - 50*t^10 + O(t^12)
            sage: y
            t^-5 + 10*t - 2*t^5 - 75*t^7 + 50*t^11 + O(t^12)

        ::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^3 - x + 1)
            sage: x, y = H.local_coordinates_at_infinity(10)
            sage: x
            t^-2 + t^2 - t^4 - t^6 + 3*t^8 + O(t^12)
            sage: y
            t^-3 + t - t^3 - t^5 + 3*t^7 - 10*t^11 + O(t^12)

        AUTHOR:

        - Jennifer Balakrishnan (2007-12)
        """
    def local_coord(self, P, prec: int = 20, name: str = 't'):
        """
        Call the appropriate local_coordinates function.

        INPUT:

        - ``P`` -- a point on ``self``
        - ``prec`` -- desired precision of the local coordinates
        - ``name`` -- generator of the power series ring (default: ``t``)

        OUTPUT:

        `(x(t),y(t))` such that `y(t)^2 = f(x(t))`, where `t`
        is the local parameter at `P`

        EXAMPLES::

            sage: R.<x> = QQ['x']
            sage: H = HyperellipticCurve(x^5 - 23*x^3 + 18*x^2 + 40*x)
            sage: H.local_coord(H(1 ,6), prec=5)
            (1 + t + O(t^5), 6 + t - 7/2*t^2 - 1/2*t^3 - 25/48*t^4 + O(t^5))
            sage: H.local_coord(H(4, 0), prec=7)
            (4 + 1/360*t^2 - 191/23328000*t^4 + 7579/188956800000*t^6 + O(t^7), t + O(t^7))
            sage: H.local_coord(H(0, 1, 0), prec=5)
            (t^-2 + 23*t^2 - 18*t^4 - 569*t^6 + O(t^7),
             t^-5 + 46*t^-1 - 36*t - 609*t^3 + 1656*t^5 + O(t^6))

        AUTHOR:

        - Jennifer Balakrishnan (2007-12)
        """
    def rational_points(self, **kwds):
        """
        Find rational points on the hyperelliptic curve, all arguments are passed
        on to :meth:`sage.schemes.generic.algebraic_scheme.rational_points`.

        EXAMPLES:

        For the LMFDB genus 2 curve `932.a.3728.1 <https://www.lmfdb.org/Genus2Curve/Q/932/a/3728/1>`_::

            sage: R.<x> = PolynomialRing(QQ)
            sage: C = HyperellipticCurve(R([0, -1, 1, 0, 1, -2, 1]), R([1]))
            sage: C.rational_points(bound=8)
            [(-1 : -3 : 1),
            (-1 : 2 : 1),
            (0 : -1 : 1),
            (0 : 0 : 1),
            (0 : 1 : 0),
            (1/2 : -5/8 : 1),
            (1/2 : -3/8 : 1),
            (1 : -1 : 1),
            (1 : 0 : 1)]

        Check that :issue:`29509` is fixed for the LMFDB genus 2 curve
        `169.a.169.1 <https://www.lmfdb.org/Genus2Curve/Q/169/a/169/1>`_::

            sage: C = HyperellipticCurve(R([0, 0, 0, 0, 1, 1]), R([1, 1, 0, 1]))
            sage: C.rational_points(bound=10)
            [(-1 : 0 : 1),
            (-1 : 1 : 1),
            (0 : -1 : 1),
            (0 : 0 : 1),
            (0 : 1 : 0)]

        An example over a number field::

            sage: R.<x> = PolynomialRing(QuadraticField(2))                             # needs sage.rings.number_field
            sage: C = HyperellipticCurve(R([1, 0, 0, 0, 0, 1]))                         # needs sage.rings.number_field
            sage: C.rational_points(bound=2)                                            # needs sage.rings.number_field
            [(-1 : 0 : 1),
             (0 : -1 : 1),
             (0 : 1 : 0),
             (0 : 1 : 1),
             (1 : -a : 1),
             (1 : a : 1)]
        """
