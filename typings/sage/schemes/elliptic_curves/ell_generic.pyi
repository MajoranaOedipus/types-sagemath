import math
import sage.schemes.curves.projective_curve as plane_curve
from . import constructor as constructor, ell_point as ell_point, ell_torsion as ell_torsion, formal_group as formal_group
from sage.arith.functions import lcm as lcm
from sage.arith.misc import valuation as valuation
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.fast_methods import WithEqualityById as WithEqualityById
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.polynomial_element import polynomial_is_variable as polynomial_is_variable
from sage.rings.polynomial.polynomial_quotient_ring_element import PolynomialQuotientRingElement as PolynomialQuotientRingElement
from sage.rings.polynomial.polynomial_ring import polygen as polygen, polygens as polygens
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational import Rational as Rational
from sage.rings.rational_field import RationalField as RationalField
from sage.rings.real_mpfr import RealField as RealField
from sage.schemes.projective.projective_homset import SchemeHomset_points_abelian_variety_field as SchemeHomset_points_abelian_variety_field

sqrt = math.sqrt
exp = math.exp

def is_EllipticCurve(x):
    """
    Utility function to test if ``x`` is an instance of an Elliptic Curve class.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_generic import is_EllipticCurve
        sage: E = EllipticCurve([1,2,3/4,7,19])
        sage: is_EllipticCurve(E)
        doctest:warning...
        DeprecationWarning: The function is_EllipticCurve is deprecated; use 'isinstance(..., EllipticCurve_generic)' instead.
        See https://github.com/sagemath/sage/issues/38022 for details.
        True
        sage: is_EllipticCurve(0)
        False
    """

class EllipticCurve_generic(WithEqualityById, plane_curve.ProjectivePlaneCurve):
    """
    Elliptic curve over a generic base ring.

    EXAMPLES::

        sage: E = EllipticCurve([1,2,3/4,7,19]); E
        Elliptic Curve defined by y^2 + x*y + 3/4*y = x^3 + 2*x^2 + 7*x + 19 over Rational Field
        sage: loads(E.dumps()) == E
        True
        sage: E = EllipticCurve([1,3])
        sage: P = E([-1,1,1])
        sage: -5*P
        (179051/80089 : -91814227/22665187 : 1)
    """
    def __init__(self, K, ainvs, category=None) -> None:
        """
        Construct an elliptic curve from Weierstrass `a`-coefficients.

        INPUT:

        - ``K`` -- a ring

        - ``ainvs`` -- list or tuple `[a_1, a_2, a_3, a_4, a_6]` of
          Weierstrass coefficients

        .. NOTE::

            This class should not be called directly; use
            :class:`sage.constructor.EllipticCurve` to construct
            elliptic curves.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,5]); E
            Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5
            over Rational Field
            sage: E = EllipticCurve(GF(7), [1,2,3,4,5]); E
            Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5
            over Finite Field of size 7

        Constructor from `[a_4,a_6]` sets `a_1=a_2=a_3=0`::

            sage: EllipticCurve([4,5]).ainvs()
            (0, 0, 0, 4, 5)

        The base ring need not be a field::

            sage: EllipticCurve(IntegerModRing(91), [1,2,3,4,5])
            Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5
            over Ring of integers modulo 91
        """
    def assume_base_ring_is_field(self, flag: bool = True) -> None:
        """
        Set a flag to pretend that this elliptic curve is defined over a
        field while doing arithmetic, which is useful in some algorithms.


        .. WARNING::

            The flag affects all points created while the flag is set. Note
            that elliptic curves are unique parents, hence setting this flag
            may break seemingly unrelated parts of Sage.

        .. NOTE::

            This method is a **hack** provided for educational purposes.

        EXAMPLES::

            sage: E = EllipticCurve(Zmod(35), [1,1])
            sage: P = E(-5, 9)
            sage: 4*P
            (23 : 26 : 1)
            sage: 9*P
            (10 : 11 : 5)
            sage: E.assume_base_ring_is_field()
            sage: P = E(-5, 9)
            sage: 4*P
            (23 : 26 : 1)
            sage: 9*P
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Inverse of 5 does not exist (characteristic = 35 = 5*7)
        """
    def __contains__(self, P) -> bool:
        """
        Return ``True`` if and only if P is a point on the elliptic curve.

        P just has to be something that can be coerced to a point.

        EXAMPLES::

            sage: E = EllipticCurve([0, 0, 1, -1, 0])
            sage: (0,0) in E
            True
            sage: (1,3) in E
            False
            sage: E = EllipticCurve([GF(7)(0), 1])
            sage: [0,0] in E
            False
            sage: [0,8] in E
            True
            sage: P = E(0,8)
            sage: P
            (0 : 1 : 1)
            sage: P in E
            True
        """
    def __call__(self, *args, **kwds):
        """
        EXAMPLES::

            sage: E = EllipticCurve([0, 0, 1, -1, 0])

        The point at infinity, which is the 0 element of the group::

            sage: E(0)
            (0 : 1 : 0)

        The origin is a point on our curve::

            sage: P = E([0,0])
            sage: P
            (0 : 0 : 1)

        The curve associated to a point::

            sage: P.curve()
            Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field

        Points can be specified by given a 2-tuple or 3-tuple::

            sage: E([0,0])
            (0 : 0 : 1)
            sage: E([0,1,0])
            (0 : 1 : 0)

        Over a field, points are normalized so the 3rd entry (if nonzero)
        is 1::

            sage: E(105, -69, 125)
            (21/25 : -69/125 : 1)

        We create points on an elliptic curve over a prime finite field::

            sage: E = EllipticCurve([GF(7)(0), 1])
            sage: E([2,3])
            (2 : 3 : 1)
            sage: E([0,0])
            Traceback (most recent call last):
            ...
            TypeError: Coordinates [0, 0, 1] do not define a point
            on Elliptic Curve defined by y^2 = x^3 + 1 over Finite Field of size 7

        We create a point on an elliptic curve over a number field::

            sage: # needs sage.rings.number_field
            sage: x = polygen(RationalField())
            sage: K = NumberField(x**3 + x + 1, 'a'); a = K.gen()
            sage: E = EllipticCurve([a, a])
            sage: E
            Elliptic Curve defined by y^2 = x^3 + a*x + a
            over Number Field in a with defining polynomial x^3 + x + 1
            sage: E = EllipticCurve([K(1), 1])
            sage: E
            Elliptic Curve defined by y^2 = x^3 + x + 1
            over Number Field in a with defining polynomial x^3 + x + 1
            sage: P = E([a,0,1])
            sage: P
            (a : 0 : 1)
            sage: P + P
            (0 : 1 : 0)

        Another example involving `p`-adics::

            sage: E = EllipticCurve('37a1')
            sage: P = E([0,0]); P
            (0 : 0 : 1)
            sage: R = pAdicField(3, 20)                                                 # needs sage.rings.padics
            sage: Ep = E.base_extend(R); Ep                                             # needs sage.rings.padics
            Elliptic Curve defined by
            y^2 + (1+O(3^20))*y = x^3 + (2+2*3+2*3^2+2*3^3+2*3^4+2*3^5+2*3^6+2*3^7+2*3^8+2*3^9+2*3^10+2*3^11+2*3^12+2*3^13+2*3^14+2*3^15+2*3^16+2*3^17+2*3^18+2*3^19+O(3^20))*x
            over 3-adic Field with capped relative precision 20
            sage: Ep(P)                                                                 # needs sage.rings.padics
            (0 : 0 : 1 + O(3^20))

        Constructing points from the torsion subgroup (which is an abstract
        abelian group)::

            sage: E = EllipticCurve('14a1')
            sage: T = E.torsion_subgroup()
            sage: [E(t) for t in T]
            [(0 : 1 : 0),
             (9 : 23 : 1),
             (2 : 2 : 1),
             (1 : -1 : 1),
             (2 : -5 : 1),
             (9 : -33 : 1)]

        ::

            sage: E = EllipticCurve([0,0,0,-49,0])
            sage: T = E.torsion_subgroup()
            sage: [E(t) for t in T]
            [(0 : 1 : 0), (0 : 0 : 1), (-7 : 0 : 1), (7 : 0 : 1)]

        ::

            sage: E = EllipticCurve('37a1')
            sage: T = E.torsion_subgroup()
            sage: [E(t) for t in T]
            [(0 : 1 : 0)]
        """
    def is_x_coord(self, x):
        """
        Return ``True`` if ``x`` is the `x`-coordinate of a point on this curve.

        .. NOTE::

            See also :meth:`lift_x` to find the point(s) with a given
            `x`-coordinate.  This function may be useful in cases where
            testing an element of the base field for being a square is
            faster than finding its square root.

        EXAMPLES::

            sage: E = EllipticCurve('37a'); E
            Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
            sage: E.is_x_coord(1)
            True
            sage: E.is_x_coord(2)
            True

        There are no rational points with x-coordinate 3::

            sage: E.is_x_coord(3)
            False

        However, there are such points in `E(\\RR)`::

            sage: E.change_ring(RR).is_x_coord(3)
            True

        And of course it always works in `E(\\CC)`::

            sage: E.change_ring(RR).is_x_coord(-3)
            False
            sage: E.change_ring(CC).is_x_coord(-3)
            True

        AUTHORS:

        - John Cremona (2008-08-07): adapted from :meth:`lift_x`

        TESTS::

            sage: E = EllipticCurve('5077a1')
            sage: [x for x in srange(-10,10) if E.is_x_coord (x)]
            [-3, -2, -1, 0, 1, 2, 3, 4, 8]

        ::

            sage: F = GF(32,'a')                                                                    # needs sage.rings.finite_rings
            sage: E = EllipticCurve(F,[1,0,0,0,1])                                                  # needs sage.rings.finite_rings
            sage: set(P[0] for P in E.points() if P!=E(0)) == set(x for x in F if E.is_x_coord(x))  # needs sage.rings.finite_rings
            True
        """
    def lift_x(self, x, all: bool = False, extend: bool = False):
        """
        Return one or all points with given `x`-coordinate.

        This method is deterministic: It returns the same data each
        time when called again with the same `x`.

        INPUT:

        - ``x`` -- an element of the base ring of the curve, or of an extension

        - ``all`` -- boolean (default: ``False``); if ``True``, return a
          (possibly empty) list of all points; if ``False``, return just one
          point, or raise a :exc:`ValueError` if there are none.

        - ``extend`` -- boolean (default: ``False``);

          - if ``False``, extend the base if necessary and possible to
            include `x`, and only return point(s) defined over this
            ring, or raise an error when there are none with this
            `x`-coordinate;

          - If ``True``, the base ring will be extended if necessary
            to contain the `y`-coordinates of the point(s) with this
            `x`-coordinate, in addition to a possible base change to
            include `x`.

        OUTPUT:

        A point or list of up to 2 points on this curve, or a
        base-change of this curve to a larger ring.

        .. SEEALSO::

            :meth:`is_x_coord`

        EXAMPLES::

            sage: E = EllipticCurve('37a'); E
            Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
            sage: E.lift_x(1)
            (1 : -1 : 1)
            sage: E.lift_x(2)
            (2 : -3 : 1)
            sage: E.lift_x(1/4, all=True)
            [(1/4 : -5/8 : 1), (1/4 : -3/8 : 1)]

        There are no rational points with `x`-coordinate 3::

            sage: E.lift_x(3)
            Traceback (most recent call last):
            ...
            ValueError: No point with x-coordinate 3
            on Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field

        We can use the ``extend`` parameter to make the necessary
        quadratic extension.  Note that in such cases the returned
        point is a point on a new curve object, the result of changing
        the base ring to the parent of `x`::

            sage: P = E.lift_x(3, extend=True); P                                       # needs sage.rings.number_field
            (3 : -y - 1 : 1)
            sage: P.curve()                                                             # needs sage.rings.number_field
            Elliptic Curve defined by y^2 + y = x^3 + (-1)*x
            over Number Field in y with defining polynomial y^2 + y - 24

        Or we can extend scalars.  There are two such points in `E(\\RR)`::

            sage: E.change_ring(RR).lift_x(3, all=True)
            [(3.00000000000000 : -5.42442890089805 : 1.00000000000000),
             (3.00000000000000 : 4.42442890089805 : 1.00000000000000)]

        And of course it always works in `E(\\CC)`::

            sage: E.change_ring(RR).lift_x(.5, all=True)
            []
            sage: E.change_ring(CC).lift_x(.5)
            (0.500000000000000 : -0.500000000000000 - 0.353553390593274*I : 1.00000000000000)

        In this example we start with a curve defined over `\\QQ`
        which has no rational points with `x=0`, but using
        ``extend = True`` we can construct such a point over a quadratic
        field::

            sage: E = EllipticCurve([0,0,0,0,2]); E
            Elliptic Curve defined by y^2 = x^3 + 2 over Rational Field
            sage: P = E.lift_x(0, extend=True); P                                       # needs sage.rings.number_field
            (0 : -y : 1)
            sage: P.curve()                                                             # needs sage.rings.number_field
            Elliptic Curve defined by y^2 = x^3 + 2
            over Number Field in y with defining polynomial y^2 - 2

        We can perform these operations over finite fields too::

            sage: E = EllipticCurve('37a').change_ring(GF(17)); E
            Elliptic Curve defined by y^2 + y = x^3 + 16*x over Finite Field of size 17
            sage: E.lift_x(7)
            (7 : 5 : 1)
            sage: E.lift_x(3)
            Traceback (most recent call last):
            ...
            ValueError: No point with x-coordinate 3 on
            Elliptic Curve defined by y^2 + y = x^3 + 16*x over Finite Field of size 17

        Note that there is only one lift with `x`-coordinate 10 in
        `E(\\GF{17})`::

            sage: E.lift_x(10, all=True)
            [(10 : 8 : 1)]

        We can lift over more exotic rings too. If the supplied x
        value is in an extension of the base, note that the point
        returned is on the base-extended curve::

            sage: E = EllipticCurve('37a')
            sage: P = E.lift_x(pAdicField(17, 5)(6)); P                                 # needs sage.rings.padics
            (6 + O(17^5) : 14 + O(17^5) : 1 + O(17^5))
            sage: P.curve()                                                             # needs sage.rings.padics
            Elliptic Curve defined by
            y^2 + (1+O(17^5))*y = x^3 + (16+16*17+16*17^2+16*17^3+16*17^4+O(17^5))*x
            over 17-adic Field with capped relative precision 5
            sage: K.<t> = PowerSeriesRing(QQ, 't', 5)
            sage: P = E.lift_x(1 + t); P
            (1 + t : -1 - 2*t + t^2 - 5*t^3 + 21*t^4 + O(t^5) : 1)
            sage: K.<a> = GF(16)                                                        # needs sage.rings.finite_rings
            sage: P = E.change_ring(K).lift_x(a^3); P                                   # needs sage.rings.finite_rings
            (a^3 : a^3 + a : 1)
            sage: P.curve()                                                             # needs sage.rings.finite_rings
            Elliptic Curve defined by y^2 + y = x^3 + x over Finite Field in a of size 2^4

        We can extend the base field to include the associated `y` value(s)::

            sage: E = EllipticCurve([0,0,0,0,2]); E
            Elliptic Curve defined by y^2 = x^3 + 2 over Rational Field
            sage: x = polygen(QQ)
            sage: P = E.lift_x(x, extend=True); P
            (x : -y : 1)

        This point is a generic point on E::

            sage: P.curve()
            Elliptic Curve defined by y^2 = x^3 + 2
            over Univariate Quotient Polynomial Ring in y
            over Fraction Field of Univariate Polynomial Ring in x over Rational Field
            with modulus y^2 - x^3 - 2
            sage: -P
            (x : y : 1)
            sage: 2*P
            ((1/4*x^4 - 4*x)/(x^3 + 2) : ((-1/8*x^6 - 5*x^3 + 4)/(x^6 + 4*x^3 + 4))*y : 1)

        Check that :issue:`30297` is fixed::

            sage: K = Qp(5)                                                             # needs sage.rings.padics
            sage: E = EllipticCurve([K(0), K(1)])                                       # needs sage.rings.padics
            sage: E.lift_x(1, extend=True)                                              # needs sage.rings.padics
            (1 + O(5^20) : y + O(5^20) : 1 + O(5^20))

        AUTHORS:

        - Robert Bradshaw (2007-04-24)
        - John Cremona (2017-11-10)

        TESTS::

            sage: E = EllipticCurve('37a').short_weierstrass_model().change_ring(GF(17))
            sage: E.lift_x(3, all=True)
            []
            sage: E.lift_x(7, all=True)
            [(7 : 3 : 1), (7 : 14 : 1)]

        Check determinism::

            sage: F.<t> = GF((101,3))
            sage: {(t+1).sqrt() for _ in range(1000)}   # both square roots can occur
            {29*t^2 + 56*t + 26, 72*t^2 + 45*t + 75}
            sage: E = EllipticCurve(F, [1,1])
            sage: {E.lift_x(t+1) for _ in range(1000)}  # but .lift_x() uses a fixed one
            {(t + 1 : 39*t^2 + 14*t + 12 : 1)}
        """
    def __getitem__(self, n) -> None:
        """
        Placeholder for standard indexing function.

        EXAMPLES::

            sage: E = EllipticCurve(QQ,[1,1])
            sage: E[2]
            Traceback (most recent call last):
            ...
            NotImplementedError: not implemented.
        """
    def is_on_curve(self, x, y):
        """
        Return ``True`` if `(x,y)` is an affine point on this curve.

        INPUT:

        - ``x``, ``y`` -- elements of the base ring of the curve

        EXAMPLES::

            sage: E = EllipticCurve(QQ,[1,1])
            sage: E.is_on_curve(0,1)
            True
            sage: E.is_on_curve(1,1)
            False
        """
    def is_exact(self):
        """
        Test whether elements of this elliptic curve are represented exactly.

        EXAMPLES::

            sage: EllipticCurve(QQ, [1, 2]).is_exact()
            True
            sage: EllipticCurve(RR, [1, 2]).is_exact()
            False
        """
    def a_invariants(self):
        """
        The `a`-invariants of this elliptic curve, as a tuple.

        OUTPUT:

        (tuple) - a 5-tuple of the `a`-invariants of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,5])
            sage: E.a_invariants()
            (1, 2, 3, 4, 5)

            sage: E = EllipticCurve([0,1]); E
            Elliptic Curve defined by y^2 = x^3 + 1 over Rational Field
            sage: E.a_invariants()
            (0, 0, 0, 0, 1)

            sage: E = EllipticCurve([GF(7)(3),5])
            sage: E.a_invariants()
            (0, 0, 0, 3, 5)

        TESTS::

            sage: E = EllipticCurve([1,0,0,0,1])
            sage: E.a_invariants()[0] = 100000000
            Traceback (most recent call last):
            ...
            TypeError: 'tuple' object does not support item assignment
        """
    ainvs = a_invariants
    def a1(self):
        """
        Return the `a_1` invariant of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,6])
            sage: E.a1()
            1
        """
    def a2(self):
        """
        Return the `a_2` invariant of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,6])
            sage: E.a2()
            2
        """
    def a3(self):
        """
        Return the `a_3` invariant of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,6])
            sage: E.a3()
            3
        """
    def a4(self):
        """
        Return the `a_4` invariant of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,6])
            sage: E.a4()
            4
        """
    def a6(self):
        """
        Return the `a_6` invariant of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,6])
            sage: E.a6()
            6
        """
    @cached_method
    def b_invariants(self):
        """
        Return the `b`-invariants of this elliptic curve, as a tuple.

        OUTPUT:

        (tuple) - a 4-tuple of the `b`-invariants of this elliptic curve.

        This method is cached.

        EXAMPLES::

            sage: E = EllipticCurve([0, -1, 1, -10, -20])
            sage: E.b_invariants()
            (-4, -20, -79, -21)

            sage: E = EllipticCurve([-4,0])
            sage: E.b_invariants()
            (0, -8, 0, -16)

            sage: E = EllipticCurve([1,2,3,4,5])
            sage: E.b_invariants()
            (9, 11, 29, 35)
            sage: E.b2()
            9
            sage: E.b4()
            11
            sage: E.b6()
            29
            sage: E.b8()
            35

        ALGORITHM:

        These are simple functions of the `a`-invariants.

        AUTHORS:

        - William Stein (2005-04-25)
        """
    def b2(self):
        """
        Return the `b_2` invariant of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,5])
            sage: E.b2()
            9
        """
    def b4(self):
        """
        Return the `b_4` invariant of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,5])
            sage: E.b4()
            11
        """
    def b6(self):
        """
        Return the `b_6` invariant of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,5])
            sage: E.b6()
            29
        """
    def b8(self):
        """
        Return the `b_8` invariant of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,5])
            sage: E.b8()
            35
        """
    @cached_method
    def c_invariants(self):
        """
        Return the `c`-invariants of this elliptic curve, as a tuple.

        This method is cached.

        OUTPUT:

        (tuple) - a 2-tuple of the `c`-invariants of the elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([0, -1, 1, -10, -20])
            sage: E.c_invariants()
            (496, 20008)

            sage: E = EllipticCurve([-4,0])
            sage: E.c_invariants()
            (192, 0)

        ALGORITHM:

        These are simple functions of the `a`-invariants.

        AUTHORS:

        - William Stein (2005-04-25)
        """
    def c4(self):
        """
        Return the `c_4` invariant of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([0, -1, 1, -10, -20])
            sage: E.c4()
            496
        """
    def c6(self):
        """
        Return the `c_6` invariant of this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([0, -1, 1, -10, -20])
            sage: E.c6()
            20008
        """
    @cached_method
    def discriminant(self):
        """
        Return the discriminant of this elliptic curve.

        This method is cached.

        EXAMPLES::

            sage: E = EllipticCurve([0,0,1,-1,0])
            sage: E.discriminant()
            37

            sage: E = EllipticCurve([0, -1, 1, -10, -20])
            sage: E.discriminant()
            -161051

            sage: E = EllipticCurve([GF(7)(2),1])
            sage: E.discriminant()
            1
        """
    @cached_method
    def j_invariant(self):
        """
        Return the `j`-invariant of this elliptic curve.

        This method is cached.

        EXAMPLES::

            sage: E = EllipticCurve([0,0,1,-1,0])
            sage: E.j_invariant()
            110592/37

            sage: E = EllipticCurve([0, -1, 1, -10, -20])
            sage: E.j_invariant()
            -122023936/161051

            sage: E = EllipticCurve([-4,0])
            sage: E.j_invariant()
            1728

            sage: E = EllipticCurve([GF(7)(2),1])
            sage: E.j_invariant()
            1
        """
    def base_extend(self, R):
        """
        Return the base extension of ``self`` to `R`.

        INPUT:

        - ``R`` -- either a ring into which the `a`-invariants of
          ``self`` may be converted, or a morphism which may be
          applied to them.

        OUTPUT:

        An elliptic curve over the new ring whose `a`-invariants are
        the images of the `a`-invariants of ``self``.

        EXAMPLES::

            sage: E = EllipticCurve(GF(5), [1,1]); E
            Elliptic Curve defined by y^2 = x^3 + x + 1 over Finite Field of size 5
            sage: E1 = E.base_extend(GF(125,'a')); E1                                   # needs sage.rings.finite_rings
            Elliptic Curve defined by y^2 = x^3 + x + 1 over Finite Field in a of size 5^3

        TESTS:

        Check that we are correctly keeping track of known
        cardinalities when extending the base field::

            sage: # needs sage.rings.finite_rings
            sage: E = EllipticCurve(j=GF(7)(5))
            sage: E.cardinality()
            10
            sage: EE = E.base_extend(GF(7^2))
            sage: EE._order
            60

        Changing to a smaller field should not cache orders::

            sage: EE = EllipticCurve(j=GF(7^3)(6))                                      # needs sage.rings.finite_rings
            sage: hasattr(EE.change_ring(GF(7)), '_order')                              # needs sage.rings.finite_rings
            False

        Changing to a field of different characteristic should
        not cache orders::

            sage: Elift = E.change_ring(QQ)                                             # needs sage.rings.finite_rings
            sage: hasattr(Elift, '_order')                                              # needs sage.rings.finite_rings
            False
        """
    def change_ring(self, R):
        """
        Return the base change of ``self`` to `R`.

        This has the same effect as ``self.base_extend(R)``.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F2 = GF(5^2,'a'); a = F2.gen()
            sage: F4 = GF(5^4,'b'); b = F4.gen()
            sage: roots = a.charpoly().roots(ring=F4, multiplicities=False)
            sage: h = F2.hom([roots[0]], F4)
            sage: E = EllipticCurve(F2, [1,a]); E
            Elliptic Curve defined by y^2 = x^3 + x + a
            over Finite Field in a of size 5^2
            sage: E.change_ring(h)
            Elliptic Curve defined by y^2 = x^3 + x + (4*b^3+4*b^2+4*b+3)
            over Finite Field in b of size 5^4
        """
    def base_ring(self):
        """
        Return the base ring of the elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve(GF(49, 'a'), [3,5])                                 # needs sage.rings.finite_rings
            sage: E.base_ring()                                                         # needs sage.rings.finite_rings
            Finite Field in a of size 7^2

        ::

            sage: E = EllipticCurve([1,1])
            sage: E.base_ring()
            Rational Field

        ::

            sage: E = EllipticCurve(ZZ, [3,5])
            sage: E.base_ring()
            Integer Ring
        """
    def gens(self) -> None:
        """
        Placeholder function to return generators of an elliptic curve.

        .. NOTE::

            This functionality is implemented in certain derived
            classes, such as EllipticCurve_rational_field.

        EXAMPLES::

            sage: R.<a1,a2,a3,a4,a6> = QQ[]
            sage: E = EllipticCurve([a1,a2,a3,a4,a6])
            sage: E.gens()
            Traceback (most recent call last):
            ...
            NotImplementedError: not implemented.
            sage: E = EllipticCurve(QQ, [1,1])
            sage: E.gens()
            [(0 : 1 : 1)]
        """
    def gen(self, i):
        """
        Function returning the i'th generator of this elliptic curve.

        .. NOTE::

            Relies on gens() being implemented.

        EXAMPLES::

            sage: R.<a1,a2,a3,a4,a6> = QQ[]
            sage: E = EllipticCurve([a1,a2,a3,a4,a6])
            sage: E.gen(0)
            Traceback (most recent call last):
            ...
            NotImplementedError: not implemented.
        """
    def rst_transform(self, r, s, t):
        """
        Return the transform of the curve by `(r,s,t)` (with `u=1`).

        INPUT:

        - ``r``, ``s``, ``t`` -- three elements of the base ring

        OUTPUT:

        The elliptic curve obtained from ``self`` by the standard
        Weierstrass transformation `(u,r,s,t)` with `u=1`.

        .. NOTE::

            This is just a special case of
            :meth:`change_weierstrass_model`, with `u=1`.

        EXAMPLES::

            sage: R.<r,s,t> = QQ[]
            sage: E = EllipticCurve([1,2,3,4,5])
            sage: E.rst_transform(r, s, t)
            Elliptic Curve defined by y^2 + (2*s+1)*x*y + (r+2*t+3)*y
            = x^3 + (-s^2+3*r-s+2)*x^2 + (3*r^2-r*s-2*s*t+4*r-3*s-t+4)*x
              + (r^3+2*r^2-r*t-t^2+4*r-3*t+5)
            over Multivariate Polynomial Ring in r, s, t over Rational Field
        """
    def scale_curve(self, u):
        """
        Return the transform of the curve by scale factor `u`.

        INPUT:

        - ``u`` -- an invertible element of the base ring

        OUTPUT:

        The elliptic curve obtained from ``self`` by the standard
        Weierstrass transformation `(u,r,s,t)` with `r=s=t=0`.

        .. NOTE::

            This is just a special case of
            :meth:`change_weierstrass_model`, with `r=s=t=0`.

        EXAMPLES::

            sage: K = Frac(PolynomialRing(QQ, 'u'))
            sage: u = K.gen()
            sage: E = EllipticCurve([1,2,3,4,5])
            sage: E.scale_curve(u)
            Elliptic Curve defined by
            y^2 + u*x*y + 3*u^3*y = x^3 + 2*u^2*x^2 + 4*u^4*x + 5*u^6
            over Fraction Field of Univariate Polynomial Ring in u over Rational Field
        """
    def isomorphism(self, u, r: int = 0, s: int = 0, t: int = 0, *, is_codomain: bool = False):
        """
        Given four values `u,r,s,t` in the base ring of this curve, return
        the :class:`WeierstrassIsomorphism` defined by `u,r,s,t` with this
        curve as its codomain.
        (The value `u` must be a unit; the values `r,s,t` default to zero.)

        Optionally, if the keyword argument ``is_codomain`` is set to ``True``,
        return the isomorphism defined by `u,r,s,t` with this curve as its
        **co**\\domain.

        EXAMPLES::

            sage: E = EllipticCurve([1, 2, 3, 4, 5])
            sage: iso = E.isomorphism(6); iso
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field
              To:   Elliptic Curve defined by y^2 + 1/6*x*y + 1/72*y = x^3 + 1/18*x^2 + 1/324*x + 5/46656 over Rational Field
              Via:  (u,r,s,t) = (6, 0, 0, 0)
            sage: iso.domain() == E
            True
            sage: iso.codomain() == E.scale_curve(1 / 6)
            True

            sage: iso = E.isomorphism(1, 7, 8, 9); iso
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field
              To:   Elliptic Curve defined by y^2 + 17*x*y + 28*y = x^3 - 49*x^2 - 54*x + 303 over Rational Field
              Via:  (u,r,s,t) = (1, 7, 8, 9)
            sage: iso.domain() == E
            True
            sage: iso.codomain() == E.rst_transform(7, 8, 9)
            True

            sage: iso = E.isomorphism(6, 7, 8, 9); iso
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field
              To:   Elliptic Curve defined by y^2 + 17/6*x*y + 7/54*y = x^3 - 49/36*x^2 - 1/24*x + 101/15552 over Rational Field
              Via:  (u,r,s,t) = (6, 7, 8, 9)
            sage: iso.domain() == E
            True
            sage: iso.codomain() == E.rst_transform(7, 8, 9).scale_curve(1 / 6)
            True

        The ``is_codomain`` argument reverses the role of domain and codomain::

            sage: E = EllipticCurve([1, 2, 3, 4, 5])
            sage: iso = E.isomorphism(6, is_codomain=True); iso
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 + 6*x*y + 648*y = x^3 + 72*x^2 + 5184*x + 233280 over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field
              Via:  (u,r,s,t) = (6, 0, 0, 0)
            sage: iso.domain() == E.scale_curve(6)
            True
            sage: iso.codomain() == E
            True

            sage: iso = E.isomorphism(1, 7, 8, 9, is_codomain=True); iso
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 - 15*x*y + 90*y = x^3 - 75*x^2 + 796*x - 2289 over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field
              Via:  (u,r,s,t) = (1, 7, 8, 9)
            sage: iso.domain().rst_transform(7, 8, 9) == E
            True
            sage: iso.codomain() == E
            True

            sage: iso = E.isomorphism(6, 7, 8, 9, is_codomain=True); iso
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 - 10*x*y + 700*y = x^3 + 35*x^2 + 9641*x + 169486 over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field
              Via:  (u,r,s,t) = (6, 7, 8, 9)
            sage: iso.domain().rst_transform(7, 8, 9) == E.scale_curve(6)
            True
            sage: iso.codomain() == E
            True

        .. SEEALSO::

            - :class:`~sage.schemes.elliptic_curves.weierstrass_morphism.WeierstrassIsomorphism`
            - :meth:`rst_transform`
            - :meth:`scale_curve`
        """
    def division_polynomial_0(self, n, x=None):
        '''
        Return the `n`-th torsion (division) polynomial, without
        the 2-torsion factor if `n` is even, as a polynomial in `x`.

        These are the polynomials `g_n` defined in [MT1991]_, but with
        the sign flipped for even `n`, so that the leading coefficient is
        always positive.

        .. NOTE::

            This function is intended for internal use; users should use
            :meth:`division_polynomial`.

        .. SEEALSO::

            - :meth:`division_polynomial`
            - :meth:`_multiple_x_numerator`
            - :meth:`_multiple_x_denominator`

        INPUT:

        - ``n`` -- positive integer, or the special values ``-1`` and ``-2``
          which mean `B_6 = (2y + a_1 x + a_3)^2` and `B_6^2` respectively (in
          the notation of [MT1991]_), or a list of integers

        - ``x`` -- a ring element to use as the "x" variable or ``None``
          (default: ``None``); if ``None``, then a new polynomial ring will
          be constructed over the base ring of the elliptic curve, and its
          generator will be used as ``x``. Note that ``x`` does not need to
          be a generator of a polynomial ring; any ring element is ok. This
          permits fast calculation of the torsion polynomial *evaluated* on
          any element of a ring.

        ALGORITHM:

        Recursion described in [MT1991]_. The recursive
        formulae are evaluated `O(\\log^2 n)` times.

        AUTHORS:

        - David Harvey (2006-09-24): initial version

        - John Cremona (2008-08-26): unified division polynomial code

        EXAMPLES::

            sage: E = EllipticCurve("37a")
            sage: E.division_polynomial_0(1)
            1
            sage: E.division_polynomial_0(2)
            1
            sage: E.division_polynomial_0(3)
            3*x^4 - 6*x^2 + 3*x - 1
            sage: E.division_polynomial_0(4)
            2*x^6 - 10*x^4 + 10*x^3 - 10*x^2 + 2*x + 1
            sage: E.division_polynomial_0(5)
            5*x^12 - 62*x^10 + 95*x^9 - 105*x^8 - 60*x^7 + 285*x^6 - 174*x^5 - 5*x^4 - 5*x^3 + 35*x^2 - 15*x + 2
            sage: E.division_polynomial_0(6)
            3*x^16 - 72*x^14 + 168*x^13 - 364*x^12 + 1120*x^10 - 1144*x^9 + 300*x^8 - 540*x^7 + 1120*x^6 - 588*x^5 - 133*x^4 + 252*x^3 - 114*x^2 + 22*x - 1
            sage: E.division_polynomial_0(7)
            7*x^24 - 308*x^22 + 986*x^21 - 2954*x^20 + 28*x^19 + 17171*x^18 - 23142*x^17 + 511*x^16 - 5012*x^15 + 43804*x^14 - 7140*x^13 - 96950*x^12 + 111356*x^11 - 19516*x^10 - 49707*x^9 + 40054*x^8 - 124*x^7 - 18382*x^6 + 13342*x^5 - 4816*x^4 + 1099*x^3 - 210*x^2 + 35*x - 3
            sage: E.division_polynomial_0(8)
            4*x^30 - 292*x^28 + 1252*x^27 - 5436*x^26 + 2340*x^25 + 39834*x^24 - 79560*x^23 + 51432*x^22 - 142896*x^21 + 451596*x^20 - 212040*x^19 - 1005316*x^18 + 1726416*x^17 - 671160*x^16 - 954924*x^15 + 1119552*x^14 + 313308*x^13 - 1502818*x^12 + 1189908*x^11 - 160152*x^10 - 399176*x^9 + 386142*x^8 - 220128*x^7 + 99558*x^6 - 33528*x^5 + 6042*x^4 + 310*x^3 - 406*x^2 + 78*x - 5

        ::

            sage: E.division_polynomial_0(18) % E.division_polynomial_0(6) == 0
            True

        An example to illustrate the relationship with torsion points::

            sage: F = GF(11)
            sage: E = EllipticCurve(F, [0, 2]); E
            Elliptic Curve defined by y^2  = x^3 + 2 over Finite Field of size 11
            sage: f = E.division_polynomial_0(5); f
            5*x^12 + x^9 + 8*x^6 + 4*x^3 + 7
            sage: f.factor()
            (5) * (x^2 + 5) * (x^2 + 2*x + 5) * (x^2 + 5*x + 7)
             * (x^2 + 7*x + 7) * (x^2 + 9*x + 5) * (x^2 + 10*x + 7)

        This indicates that the `x`-coordinates of all the 5-torsion points of
        `E` are in `\\GF{11^2}`, and therefore the `y`-coordinates are in
        `\\GF{11^4}`::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(11^4, \'a\')
            sage: X = E.change_ring(K)
            sage: f = X.division_polynomial_0(5)
            sage: x_coords = f.roots(multiplicities=False); x_coords
            [10*a^3 + 4*a^2 + 5*a + 6,
             9*a^3 + 8*a^2 + 10*a + 8,
             8*a^3 + a^2 + 4*a + 10,
             8*a^3 + a^2 + 4*a + 8,
             8*a^3 + a^2 + 4*a + 4,
             6*a^3 + 9*a^2 + 3*a + 4,
             5*a^3 + 2*a^2 + 8*a + 7,
             3*a^3 + 10*a^2 + 7*a + 8,
             3*a^3 + 10*a^2 + 7*a + 3,
             3*a^3 + 10*a^2 + 7*a + 1,
             2*a^3 + 3*a^2 + a + 7,
             a^3 + 7*a^2 + 6*a]

        Now we check that these are exactly the `x`-coordinates of the
        5-torsion points of `E`::

            sage: for x in x_coords:                                                    # needs sage.rings.finite_rings
            ....:     assert X.lift_x(x).order() == 5

        The roots of the polynomial are the `x`-coordinates of the points `P`
        such that `mP=0` but `2P\\not=0`::

            sage: E = EllipticCurve(\'14a1\')
            sage: T = E.torsion_subgroup()
            sage: [n*T.0 for n in range(6)]
            [(0 : 1 : 0),
            (9 : 23 : 1),
            (2 : 2 : 1),
            (1 : -1 : 1),
            (2 : -5 : 1),
            (9 : -33 : 1)]
            sage: pol = E.division_polynomial_0(6)
            sage: xlist = pol.roots(multiplicities=False); xlist
            [9, 2, -1/3, -5]
            sage: [E.lift_x(x, all=True) for x in xlist]
            [[(9 : -33 : 1), (9 : 23 : 1)], [(2 : -5 : 1), (2 : 2 : 1)], [], []]

        .. NOTE::

            The point of order 2 and the identity do not appear.
            The points with `x=-1/3` and `x=-5` are not rational.
        '''
    def two_division_polynomial(self, x=None):
        """
        Return the 2-division polynomial of this elliptic curve evaluated
        at ``x``.

        INPUT:

        - ``x`` -- (optional) ring element to use as the `x` variable.
          If ``x`` is ``None``, then a new polynomial ring will be
          constructed over the base ring of the elliptic curve, and
          its generator will be used as ``x``. Note that ``x`` does
          not need to be a generator of a polynomial ring; any ring
          element is acceptable. This permits fast calculation of the
          torsion polynomial *evaluated* on any element of a ring.

        EXAMPLES::

            sage: E = EllipticCurve('5077a1')
            sage: E.two_division_polynomial()
            4*x^3 - 28*x + 25
            sage: E = EllipticCurve(GF(3^2,'a'), [1,1,1,1,1])                           # needs sage.rings.finite_rings
            sage: E.two_division_polynomial()                                           # needs sage.rings.finite_rings
            x^3 + 2*x^2 + 2
            sage: E.two_division_polynomial().roots()                                   # needs sage.rings.finite_rings
            [(2, 1), (2*a, 1), (a + 2, 1)]
        """
    def division_polynomial(self, m, x=None, two_torsion_multiplicity: int = 2, force_evaluate=None):
        """
        Return the `m`-th division polynomial of this elliptic
        curve evaluated at `x`.

        The division polynomial is cached if `x` is ``None``.

        INPUT:

        - ``m`` -- positive integer

        - ``x`` -- (optional) ring element to use as the `x` variable.
          If `x` is ``None`` (omitted), then a new polynomial ring will be
          constructed over the base ring of the elliptic curve, and its
          generator will be used as `x`. Note that `x` does not need to
          be a generator of a polynomial ring; any ring element works. This
          permits fast calculation of the torsion polynomial *evaluated* on
          any element of a ring.

        - ``two_torsion_multiplicity`` -- 0, 1, or 2

          If 0: For even `m` when `x` is ``None``, a univariate polynomial
          over the base ring of the curve is returned, which omits factors
          whose roots are the `x`-coordinates of the `2`-torsion points.
          When `x` is not ``None``, the evaluation of such a polynomial at
          `x` is returned.

          If 2: For even `m` when `x` is ``None``, a univariate polynomial
          over the base ring of the curve is returned, which includes a
          factor of degree 3 whose roots are the `x`-coordinates of the
          `2`-torsion points.
          Similarly, when `x` is not ``None``, the evaluation of such a
          polynomial at `x` is returned.

          If 1: For even `m` when `x` is ``None``, a bivariate polynomial
          over the base ring of the curve is returned, which includes a
          factor `2y+a_1x+a_3` having simple zeros at the `2`-torsion points.
          When `x` is not ``None``, it should be a tuple of length 2, and
          the evaluation of such a polynomial at `x` is returned.

        - ``force_evaluate`` -- (optional) 0, 1, or 2

          By default, this method makes use of previously cached generic
          division polynomials to compute the value of the polynomial at
          a given element `x` whenever it appears beneficial to do so.
          Explicitly setting this flag overrides the default behavior.

          Note that the complexity of evaluating a generic division
          polynomial scales much worse than that of computing the value
          at a point directly (using the recursive formulas), hence
          setting this flag can be detrimental to performance.

          If 0: Do not use cached generic division polynomials.

          If 1: If the generic division polynomial for this `m` has been
          cached before, evaluate it at `x` to compute the result.

          If 2: Compute the value at `x` by evaluating the generic
          division polynomial. If the generic `m`-division polynomial
          has not yet been cached, compute and cache it first.

        EXAMPLES::

            sage: E = EllipticCurve([0,0,1,-1,0])
            sage: E.division_polynomial(1)
            1
            sage: E.division_polynomial(2, two_torsion_multiplicity=0)
            1
            sage: E.division_polynomial(2, two_torsion_multiplicity=1)
            2*y + 1
            sage: E.division_polynomial(2, two_torsion_multiplicity=2)
            4*x^3 - 4*x + 1
            sage: E.division_polynomial(2)
            4*x^3 - 4*x + 1
            sage: [E.division_polynomial(3, two_torsion_multiplicity=i) for i in range(3)]
            [3*x^4 - 6*x^2 + 3*x - 1, 3*x^4 - 6*x^2 + 3*x - 1, 3*x^4 - 6*x^2 + 3*x - 1]
            sage: [type(E.division_polynomial(3, two_torsion_multiplicity=i)) for i in range(3)]
            [<... 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint'>,
             <... 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>,
             <... 'sage.rings.polynomial.polynomial_rational_flint.Polynomial_rational_flint'>]

        ::

            sage: E = EllipticCurve([0, -1, 1, -10, -20])
            sage: R.<z> = PolynomialRing(QQ)
            sage: E.division_polynomial(4, z, 0)
            2*z^6 - 4*z^5 - 100*z^4 - 790*z^3 - 210*z^2 - 1496*z - 5821
            sage: E.division_polynomial(4, z)
            8*z^9 - 24*z^8 - 464*z^7 - 2758*z^6 + 6636*z^5 + 34356*z^4
             + 53510*z^3 + 99714*z^2 + 351024*z + 459859

        This does not work, since when two_torsion_multiplicity is 1, we
        compute a bivariate polynomial, and must evaluate at a tuple of
        length 2::

            sage: E.division_polynomial(4,z,1)
            Traceback (most recent call last):
            ...
            ValueError: x should be a tuple of length 2 (or None)
            when two_torsion_multiplicity is 1
            sage: R.<z,w> = PolynomialRing(QQ, 2)
            sage: E.division_polynomial(4, (z,w), 1).factor()
            (2*w + 1) * (2*z^6 - 4*z^5 - 100*z^4 - 790*z^3 - 210*z^2 - 1496*z - 5821)

        We can also evaluate this bivariate polynomial at a point::

            sage: P = E(5,5)
            sage: E.division_polynomial(4,P,two_torsion_multiplicity=1)
            -1771561

        TESTS:

        Check that :issue:`33164` is fixed::

            sage: E = EllipticCurve('11a3')
            sage: R.<X> = QQ[]
            sage: S.<Y> = R.quotient(X^2)
            sage: E.division_polynomial(5, x=Y)
            -5*Y
            sage: E.division_polynomial(5, x=X)
            5*X^12 - 20*X^11 + 16*X^10 + 95*X^9 - 285*X^8 + 360*X^7 - 255*X^6 + 94*X^5 + 15*X^4 - 45*X^3 + 25*X^2 - 5*X

        Tests for the ``force_evaluate`` argument::

            sage: E.division_polynomial(5, x=Y, force_evaluate=0)
            -5*Y
            sage: E.division_polynomial(5, x=Y, force_evaluate=1)
            -5*Y
            sage: E.division_polynomial(5, x=Y, force_evaluate=2)
            -5*Y
            sage: E._EllipticCurve_generic__divpolys[2]
            {5: 5*x^12 - 20*x^11 + 16*x^10 + 95*x^9 - 285*x^8 + 360*x^7 - 255*x^6 + 94*x^5 + 15*x^4 - 45*x^3 + 25*x^2 - 5*x}
            sage: E._EllipticCurve_generic__divpolys[2][5] += 1  # poison cache
            sage: E.division_polynomial(5, x=Y, force_evaluate=0)
            -5*Y
            sage: E.division_polynomial(5, x=Y, force_evaluate=1)
            -5*Y + 1
            sage: E.division_polynomial(5, x=Y, force_evaluate=2)
            -5*Y + 1
        """
    torsion_polynomial = division_polynomial
    def multiplication_by_m(self, m, x_only: bool = False):
        """
        Return the multiplication-by-`m` map from ``self`` to ``self``.

        The result is a pair of rational functions in two variables
        `x`, `y` (or a rational function in one variable `x` if
        ``x_only`` is ``True``).

        INPUT:

        - ``m`` -- nonzero integer

        - ``x_only`` -- boolean (default: ``False``); if ``True``, return only
          the `x`-coordinate of the map (as a rational function in one variable)

        OUTPUT:

        - a pair `(f(x), g(x,y))`, where `f` and `g` are rational
          functions with the degree of `y` in `g(x,y)` exactly 1,

        - or just `f(x)` if ``x_only`` is ``True``

        .. SEEALSO::

            :meth:`scalar_multiplication` to get a morphism instead.

        .. NOTE::

            - The result is not cached.

            - ``m`` is allowed to be negative (but not 0).

        EXAMPLES::

            sage: E = EllipticCurve([-1,3])

        We verify that multiplication by 1 is just the identity::

            sage: E.multiplication_by_m(1)
            (x, y)

        Multiplication by 2 is more complicated::

            sage: f = E.multiplication_by_m(2)
            sage: f
            ((x^4 + 2*x^2 - 24*x + 1)/(4*x^3 - 4*x + 12),
             (8*x^6*y - 40*x^4*y + 480*x^3*y - 40*x^2*y + 96*x*y - 568*y)/(64*x^6 - 128*x^4 + 384*x^3 + 64*x^2 - 384*x + 576))

        We check that the rational maps agree with :meth:`scalar_multiplication`::

            sage: phi = E.scalar_multiplication(2)
            sage: phi.x_rational_map() == f[0]
            True
            sage: phi.rational_maps() == f
            True

        Grab only the x-coordinate (less work)::

            sage: mx = E.multiplication_by_m(2, x_only=True); mx
            (1/4*x^4 + 1/2*x^2 - 6*x + 1/4)/(x^3 - x + 3)
            sage: mx.parent()
            Fraction Field of Univariate Polynomial Ring in x over Rational Field

        We check that it works on a point::

            sage: P = E([2,3])
            sage: eval = lambda f,P: [fi(P[0],P[1]) for fi in f]
            sage: assert E(eval(f,P)) == 2*P

        We do the same but with multiplication by 3::

            sage: f = E.multiplication_by_m(3)
            sage: assert E(eval(f,P)) == 3*P

        And the same with multiplication by 4::

            sage: f = E.multiplication_by_m(4)
            sage: assert E(eval(f,P)) == 4*P

        And the same with multiplication by -1,-2,-3,-4::

            sage: for m in [-1,-2,-3,-4]:
            ....:     f = E.multiplication_by_m(m)
            ....:     assert E(eval(f,P)) == m*P

        TESTS:

        Verify for this fairly random looking curve and point that
        multiplication by m returns the right result for the first 10
        integers::

            sage: E = EllipticCurve([23,-105])
            sage: P = E([129/4, 1479/8])
            sage: for n in [1..10]:
            ....:     f = E.multiplication_by_m(n)
            ....:     Q = n*P
            ....:     assert Q == E(eval(f,P))
            ....:     f = E.multiplication_by_m(-n)
            ....:     Q = -n*P
            ....:     assert Q == E(eval(f,P))

        The following test shows that :issue:`4364` is indeed fixed::

            sage: # needs sage.rings.finite_rings
            sage: p = next_prime(2^30 - 41)
            sage: a = GF(p)(1)
            sage: b = GF(p)(1)
            sage: E = EllipticCurve([a, b])
            sage: P = E.random_point()
            sage: my_eval = lambda f,P: [fi(P[0],P[1]) for fi in f]
            sage: f = E.multiplication_by_m(2)
            sage: assert(E(eval(f,P)) == 2*P)

        The following test shows that :issue:`6413` is fixed for elliptic curves over finite fields::
            sage: p = 7
            sage: K.<a> = GF(p^2)
            sage: E = EllipticCurve(K, [a + 3, 5 - a])
            sage: k = p^2 * 3
            sage: f, g = E.multiplication_by_m(k)
            sage: for _ in range(100):
            ....:     P = E.random_point()
            ....:     if P * k == 0:
            ....:         continue
            ....:     Qx = f.subs(x=P[0])
            ....:     Qy = g.subs(x=P[0], y=P[1])
            ....:     assert (P * k).xy() == (Qx, Qy)

        However, it still fails for elliptic curves over positive-characteristic fields::

            sage: F.<a> = FunctionField(GF(7))
            sage: E = EllipticCurve(F, [a, 1 / a])
            sage: E.multiplication_by_m(7)
            Traceback (most recent call last):
            ...
            NotImplementedError: multiplication by integer not coprime to p is only implemented for curves over finite fields

        ::

            sage: p = 7
            sage: K.<a> = GF(p^2)
            sage: E = EllipticCurve(j=K.random_element())
            sage: E.multiplication_by_m(p * 2)[0] == E.multiplication_by_m(p * 2, x_only=True)
            True
        """
    def scalar_multiplication(self, m):
        """
        Return the scalar-multiplication map `[m]` on this elliptic
        curve as a
        :class:`sage.schemes.elliptic_curves.hom_scalar.EllipticCurveHom_scalar`
        object.

        EXAMPLES::

            sage: E = EllipticCurve('77a1')
            sage: m = E.scalar_multiplication(-7); m
            Scalar-multiplication endomorphism [-7]
             of Elliptic Curve defined by y^2 + y = x^3 + 2*x over Rational Field
            sage: m.degree()
            49
            sage: P = E(2,3)
            sage: m(P)
            (-26/225 : -2132/3375 : 1)
            sage: m.rational_maps() == E.multiplication_by_m(-7)
            True

        ::

            sage: E = EllipticCurve('11a1')
            sage: E.scalar_multiplication(7)
            Scalar-multiplication endomorphism [7]
             of Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field

        TESTS:

        Tests for :issue:`32490`::

            sage: E = EllipticCurve(QQbar, [1,0])                                       # needs sage.rings.number_field
            sage: E.scalar_multiplication(1).rational_maps()                      # needs sage.rings.number_field
            (x, y)

        ::

            sage: E = EllipticCurve_from_j(GF(31337).random_element())                  # needs sage.rings.finite_rings
            sage: P = E.random_point()                                                  # needs sage.rings.finite_rings
            sage: [E.scalar_multiplication(m)(P) == m*P for m in (1,2,3,5,7,9)]   # needs sage.rings.finite_rings
            [True, True, True, True, True, True]

        ::

            sage: E = EllipticCurve('99.a1')
            sage: E.scalar_multiplication(5)
            Scalar-multiplication endomorphism [5]
             of Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - 17*x + 30 over Rational Field
            sage: E.scalar_multiplication(2).rational_maps()
            ((x^4 + 33*x^2 - 242*x + 363)/(4*x^3 - 3*x^2 - 66*x + 121),
             (-4*x^7 + 8*x^6*y - 28*x^6 - 12*x^5*y - 420*x^5 - 660*x^4*y + 5020*x^4 + 4840*x^3*y - 7568*x^3 - 14520*x^2*y - 42108*x^2 + 20328*x*y + 143264*x - 10648*y - 122452)/(64*x^6 - 96*x^5 - 2076*x^4 + 5456*x^3 + 14520*x^2 - 63888*x + 58564))
        """
    def frobenius_isogeny(self, n: int = 1):
        """
        Return the `n`-power Frobenius isogeny from this curve to
        its Galois conjugate.

        The Frobenius *endo*\\morphism is the special case where `n`
        is divisible by the degree of the base ring of the curve.

        .. SEEALSO::

            :meth:`~sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field.frobenius_endomorphism`

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: z3, = GF(13^3).gens()
            sage: E = EllipticCurve([z3, z3^2])
            sage: E.frobenius_isogeny()
            Frobenius isogeny of degree 13:
              From: Elliptic Curve defined by y^2 = x^3 + z3*x + z3^2
                     over Finite Field in z3 of size 13^3
              To:   Elliptic Curve defined by y^2 = x^3 + (5*z3^2+7*z3+11)*x + (5*z3^2+12*z3+1)
                     over Finite Field in z3 of size 13^3
            sage: E.frobenius_isogeny(3)
            Frobenius endomorphism of degree 2197 = 13^3:
              From: Elliptic Curve defined by y^2 = x^3 + z3*x + z3^2
                     over Finite Field in z3 of size 13^3
              To:   Elliptic Curve defined by y^2 = x^3 + z3*x + z3^2
                     over Finite Field in z3 of size 13^3
        """
    def identity_morphism(self):
        """
        Return the identity endomorphism of this elliptic curve
        as an :class:`EllipticCurveHom` object.

        EXAMPLES::

            sage: E = EllipticCurve(j=42)
            sage: E.identity_morphism()
            Elliptic-curve endomorphism of Elliptic Curve defined by y^2 = x^3 + 5901*x + 1105454 over Rational Field
              Via:  (u,r,s,t) = (1, 0, 0, 0)
            sage: E.identity_morphism() == E.scalar_multiplication(1)
            True
        """
    def isomorphism_to(self, other):
        """
        Given another weierstrass model ``other`` of ``self``, return an
        isomorphism from ``self`` to ``other``.

        INPUT:

        - ``other`` -- an elliptic curve isomorphic to ``self``

        OUTPUT:

        (Weierstrassmorphism) An isomorphism from ``self`` to ``other``.

        .. NOTE::

            If the curves in question are not isomorphic, a :exc:`ValueError`
            is raised.

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: F = E.short_weierstrass_model()
            sage: w = E.isomorphism_to(F); w
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
              To:   Elliptic Curve defined by y^2  = x^3 - 16*x + 16 over Rational Field
              Via:  (u,r,s,t) = (1/2, 0, 0, -1/2)
            sage: P = E(0,-1,1)
            sage: w(P)
            (0 : -4 : 1)
            sage: w(5*P)
            (1 : 1 : 1)
            sage: 5*w(P)
            (1 : 1 : 1)
            sage: 120*w(P) == w(120*P)
            True

        We can also handle injections to different base rings::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^3 - 7)                                          # needs sage.rings.number_field
            sage: E.isomorphism_to(E.change_ring(K))                                    # needs sage.rings.number_field
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
              To:   Elliptic Curve defined by y^2 + y = x^3 + (-1)*x
                     over Number Field in a with defining polynomial x^3 - 7
              Via:  (u,r,s,t) = (1, 0, 0, 0)
        """
    def automorphisms(self, field=None):
        """
        Return the set of isomorphisms from ``self`` to itself (as a list).

        The identity and negation morphisms are guaranteed to appear
        as the first and second entry of the returned list.

        INPUT:

        - ``field`` -- (default: ``None``) a field into which the
          coefficients of the curve may be coerced (by default, uses
          the base field of the curve)

        OUTPUT:

        A list of :class:`~wm.WeierstrassIsomorphism` objects
        consisting of all the isomorphisms from the curve ``self`` to
        itself defined over ``field``.

        EXAMPLES::

            sage: E = EllipticCurve_from_j(QQ(0))  # a curve with j=0 over QQ
            sage: E.automorphisms()
            [Elliptic-curve endomorphism of Elliptic Curve defined by y^2 + y = x^3
              over Rational Field
               Via:  (u,r,s,t) = (1, 0, 0, 0),
             Elliptic-curve endomorphism of Elliptic Curve defined by y^2 + y = x^3
              over Rational Field
               Via:  (u,r,s,t) = (-1, 0, 0, -1)]

        We can also find automorphisms defined over extension fields::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 + 3)  # adjoin roots of unity                 # needs sage.rings.number_field
            sage: E.automorphisms(K)                                                    # needs sage.rings.number_field
            [Elliptic-curve endomorphism of Elliptic Curve defined by y^2 + y = x^3
              over Number Field in a with defining polynomial x^2 + 3
               Via:  (u,r,s,t) = (1, 0, 0, 0),
             Elliptic-curve endomorphism of Elliptic Curve defined by y^2 + y = x^3
              over Number Field in a with defining polynomial x^2 + 3
               Via:  (u,r,s,t) = (-1, 0, 0, -1),
             Elliptic-curve endomorphism of Elliptic Curve defined by y^2 + y = x^3
              over Number Field in a with defining polynomial x^2 + 3
               Via:  (u,r,s,t) = (-1/2*a - 1/2, 0, 0, 0),
             Elliptic-curve endomorphism of Elliptic Curve defined by y^2 + y = x^3
              over Number Field in a with defining polynomial x^2 + 3
               Via:  (u,r,s,t) = (1/2*a + 1/2, 0, 0, -1),
             Elliptic-curve endomorphism of Elliptic Curve defined by y^2 + y = x^3
              over Number Field in a with defining polynomial x^2 + 3
               Via:  (u,r,s,t) = (1/2*a - 1/2, 0, 0, 0),
             Elliptic-curve endomorphism of Elliptic Curve defined by y^2 + y = x^3
              over Number Field in a with defining polynomial x^2 + 3
               Via:  (u,r,s,t) = (-1/2*a + 1/2, 0, 0, -1)]

        ::

            sage: [len(EllipticCurve_from_j(GF(q,'a')(0)).automorphisms())              # needs sage.rings.finite_rings
            ....:  for q in [2,4,3,9,5,25,7,49]]
            [2, 24, 2, 12, 2, 6, 6, 6]

        TESTS:

        Random testing::

            sage: # needs sage.rings.finite_rings
            sage: p = random_prime(100)
            sage: k = randrange(1,30)
            sage: F.<t> = GF((p,k))
            sage: while True:
            ....:     try:
            ....:         E = EllipticCurve(list((F^5).random_element()))
            ....:     except ArithmeticError:
            ....:         continue
            ....:     break
            sage: Aut = E.automorphisms()
            sage: Aut[0] == E.scalar_multiplication(1)
            True
            sage: Aut[1] == E.scalar_multiplication(-1)
            True
            sage: sorted(Aut) == Aut
            True
        """
    def isomorphisms(self, other, field=None):
        """
        Return the set of isomorphisms from ``self`` to ``other`` (as a list).

        INPUT:

        - ``other`` -- another elliptic curve

        - ``field`` -- (default: ``None``) a field into which the
          coefficients of the curves may be coerced (by default, uses
          the base field of the curves)

        OUTPUT:

        A list of :class:`~wm.WeierstrassIsomorphism` objects consisting of all
        the isomorphisms from the curve ``self`` to the curve
        ``other`` defined over ``field``.

        EXAMPLES::

            sage: E = EllipticCurve_from_j(QQ(0)) # a curve with j=0 over QQ
            sage: F = EllipticCurve('27a3') # should be the same one
            sage: E.isomorphisms(F)
            [Elliptic-curve endomorphism of Elliptic Curve defined by y^2 + y = x^3
              over Rational Field
               Via:  (u,r,s,t) = (1, 0, 0, 0),
             Elliptic-curve endomorphism of Elliptic Curve defined by y^2 + y = x^3
              over Rational Field
               Via:  (u,r,s,t) = (-1, 0, 0, -1)]

        We can also find isomorphisms defined over extension fields::

            sage: # needs sage.rings.finite_rings
            sage: E = EllipticCurve(GF(7), [0,0,0,1,1])
            sage: F = EllipticCurve(GF(7), [0,0,0,1,-1])
            sage: E.isomorphisms(F)
            []
            sage: E.isomorphisms(F, GF(49,'a'))
            [Elliptic-curve morphism:
               From: Elliptic Curve defined by y^2 = x^3 + x + 1
                     over Finite Field in a of size 7^2
               To:   Elliptic Curve defined by y^2 = x^3 + x + 6
                     over Finite Field in a of size 7^2
               Via:  (u,r,s,t) = (a + 3, 0, 0, 0),
             Elliptic-curve morphism:
               From: Elliptic Curve defined by y^2 = x^3 + x + 1
                     over Finite Field in a of size 7^2
               To:   Elliptic Curve defined by y^2 = x^3 + x + 6
                     over Finite Field in a of size 7^2
               Via:  (u,r,s,t) = (6*a + 4, 0, 0, 0)]
        """
    def is_isomorphic(self, other, field=None):
        """
        Return whether or not ``self`` is isomorphic to ``other``.

        INPUT:

        - ``other`` -- another elliptic curve

        - ``field`` -- (default: ``None``) a field into which the
          coefficients of the curves may be coerced (by default, uses
          the base field of the curves).

        OUTPUT:

        boolean; ``True`` if there is an isomorphism from curve ``self`` to
        curve ``other`` defined over ``field``.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: F = E.change_weierstrass_model([2,3,4,5]); F
            Elliptic Curve defined by y^2 + 4*x*y + 11/8*y = x^3 - 3/2*x^2 - 13/16*x
            over Rational Field
            sage: E.is_isomorphic(F)
            True
            sage: E.is_isomorphic(F.change_ring(CC))
            False
        """
    def change_weierstrass_model(self, *urst):
        """
        Return a new Weierstrass model of ``self`` under the standard
        transformation `(u,r,s,t)`.

        .. MATH::

             (x,y) \\mapsto (x',y') = (u^2x + r , u^3y + su^2x + t).

        EXAMPLES::

            sage: E = EllipticCurve('15a')
            sage: F1 = E.change_weierstrass_model([1/2,0,0,0]); F1
            Elliptic Curve defined by y^2 + 2*x*y + 8*y = x^3 + 4*x^2 - 160*x - 640
            over Rational Field
            sage: F2 = E.change_weierstrass_model([7,2,1/3,5]); F2
            Elliptic Curve defined by
            y^2 + 5/21*x*y + 13/343*y = x^3 + 59/441*x^2 - 10/7203*x - 58/117649
            over Rational Field
            sage: F1.is_isomorphic(F2)
            True
        """
    def short_weierstrass_model(self, complete_cube: bool = True):
        """
        Return a short Weierstrass model for ``self``.

        INPUT:

        - ``complete_cube`` -- boolean (default: ``True``); for
          meaning, see below

        OUTPUT: an elliptic curve

        If ``complete_cube=True``: Return a model of the form
        `y^2 = x^3 + a*x + b` for this curve. The characteristic
        must not be 2; in characteristic 3, it is only possible if `b_2=0`.

        If ``complete_cube=False``: Return a model of the form
        `y^2 = x^3 + ax^2 + bx + c` for this curve. The
        characteristic must not be 2.

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,5])
            sage: E
            Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field
            sage: F = E.short_weierstrass_model()
            sage: F
            Elliptic Curve defined by y^2  = x^3 + 4941*x + 185166 over Rational Field
            sage: E.is_isomorphic(F)
            True
            sage: F = E.short_weierstrass_model(complete_cube=False)
            sage: F
            Elliptic Curve defined by y^2  = x^3 + 9*x^2 + 88*x + 464 over Rational Field
            sage: E.is_isomorphic(F)
            True

        ::

            sage: E = EllipticCurve(GF(3), [1,2,3,4,5])
            sage: E.short_weierstrass_model(complete_cube=False)
            Elliptic Curve defined by y^2 = x^3 + x + 2 over Finite Field of size 3

        This used to be different see :issue:`3973`::

            sage: E.short_weierstrass_model()
            Elliptic Curve defined by y^2 = x^3 + x + 2 over Finite Field of size 3

        More tests in characteristic 3::

            sage: E = EllipticCurve(GF(3), [0,2,1,2,1])
            sage: E.short_weierstrass_model()
            Traceback (most recent call last):
            ...
            ValueError: short_weierstrass_model(): no short model for Elliptic Curve
            defined by y^2 + y = x^3 + 2*x^2 + 2*x + 1 over Finite Field of size 3
            (characteristic is 3)
            sage: E.short_weierstrass_model(complete_cube=False)
            Elliptic Curve defined by y^2 = x^3 + 2*x^2 + 2*x + 2
            over Finite Field of size 3
            sage: E.short_weierstrass_model(complete_cube=False).is_isomorphic(E)
            True
        """
    def montgomery_model(self, twisted: bool = False, morphism: bool = False):
        """
        Return a (twisted or untwisted) Montgomery model for this
        elliptic curve, if possible.

        A Montgomery curve is a smooth projective curve of the form

        .. MATH::

            BY^2 = X^3 + AX^2 + X.

        The Montgomery curve is called *untwisted* if `B=1`.

        INPUT:

        - ``twisted`` -- boolean (default: ``False``); allow `B \\neq 1`

        - ``morphism`` -- boolean (default: ``False``); also return an
          isomorphism from this curve to the computed Montgomery model

        OUTPUT:

        If ``twisted`` is ``False`` (the default), an
        :class:`EllipticCurve_generic` object encapsulating an untwisted
        Montgomery curve.  Otherwise, a
        :class:`~sage.schemes.curves.projective_curve.ProjectivePlaneCurve`
        object encapsulating a (potentially twisted) Montgomery curve.

        If ``morphism`` is ``True``, this method returns a tuple consisting of
        such a curve together with an isomorphism of suitable type (either
        :class:`~sage.schemes.elliptic_curves.weierstrass_morphism.WeierstrassIsomorphism`
        or
        :class:`~sage.schemes.elliptic_curves.weierstrass_transform.WeierstrassTransformationWithInverse`)
        from this curve to the Montgomery model.

        EXAMPLES::

            sage: E = EllipticCurve(QQbar, '11a1')                                      # needs sage.rings.number_field
            sage: E.montgomery_model()                                                  # needs sage.rings.number_field
            Elliptic Curve defined by y^2 = x^3 + (-1.953522420987248?)*x^2 + x
            over Algebraic Field

        ::

            sage: E = EllipticCurve(GF(431^2), [7,7])                                   # needs sage.rings.finite_rings
            sage: E.montgomery_model()                                                  # needs sage.rings.finite_rings
            Elliptic Curve defined by y^2 = x^3 + (51*z2+190)*x^2 + x
            over Finite Field in z2 of size 431^2

        An isomorphism between the Montgomery and Weierstrass form can
        be obtained using the ``morphism`` parameter::

            sage: E.montgomery_model(morphism=True)                                     # needs sage.rings.finite_rings
            (Elliptic Curve defined by y^2 = x^3 + (51*z2+190)*x^2 + x
              over Finite Field in z2 of size 431^2,
             Elliptic-curve morphism:
               From: Elliptic Curve defined by y^2 = x^3 + 7*x + 7
                     over Finite Field in z2 of size 431^2
               To:   Elliptic Curve defined by y^2 = x^3 + (51*z2+190)*x^2 + x
                     over Finite Field in z2 of size 431^2
               Via:  (u,r,s,t) = (64*z2 + 407, 159, 0, 0))

        Not all elliptic curves have a Montgomery model over their field
        of definition::

            sage: E = EllipticCurve(GF(257), [1,1])
            sage: E.montgomery_model()
            Traceback (most recent call last):
            ...
            ValueError: Elliptic Curve defined by y^2 = x^3 + x + 1
            over Finite Field of size 257 has no Montgomery model

        ::

            sage: E = EllipticCurve(GF(257), [10,10])
            sage: E.montgomery_model()
            Traceback (most recent call last):
            ...
            ValueError: Elliptic Curve defined by y^2 = x^3 + 10*x + 10
            over Finite Field of size 257 has no untwisted Montgomery model

        However, as hinted by the error message, the latter curve does
        admit a *twisted* Montgomery model, which can be computed by
        passing ``twisted=True``::

            sage: E.montgomery_model(twisted=True)
            Projective Plane Curve over Finite Field of size 257
            defined by -x^3 + 8*x^2*z - 127*y^2*z - x*z^2

        Since Sage internally represents elliptic curves as (long) Weierstrass
        curves, which do not feature the Montgomery `B` coefficient, the
        returned curve in this case is merely a
        :class:`~sage.schemes.curves.projective_curve.ProjectivePlaneCurve`
        rather than the usual :class:`EllipticCurve_generic`.

        Arithmetic on curves of this type is not implemented natively,
        but can easily be emulated by mapping back and forth to the
        corresponding Weierstrass curve::

            sage: C, f = E.montgomery_model(twisted=True, morphism=True)
            sage: f
            Scheme morphism:
              From: Elliptic Curve defined by y^2 = x^3 + 10*x + 10
                    over Finite Field of size 257
              To:   Projective Plane Curve over Finite Field of size 257
                    defined by -x^3 + 8*x^2*z - 127*y^2*z - x*z^2
              Defn: Defined on coordinates by sending (x : y : z) to
                    (x + 116*z : -y : -85*z)
            sage: g = f.inverse(); g
            Scheme morphism:
              From: Projective Plane Curve over Finite Field of size 257
                    defined by -x^3 + 8*x^2*z - 127*y^2*z - x*z^2
              To:   Elliptic Curve defined by y^2 = x^3 + 10*x + 10
                    over Finite Field of size 257
              Defn: Defined on coordinates by sending (x : y : z) to
                    (-85*x - 116*z : 85*y : z)
            sage: P = C(70, 8)
            sage: Q = C(17, 17)
            sage: P + Q             # this doesn't work...
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +: ...
            sage: f(g(P) + g(Q))    # ...but this does
            (107 : 168 : 1)

        Using the fact that the Weil pairing satisfies `e(\\psi(P),\\psi(Q)) =
        e(P,Q)^{\\deg\\psi}`, even pairings can be emulated in this way (note
        that isomorphisms have degree `1`)::

            sage: # needs sage.rings.finite_rings
            sage: F.<z2> = GF(257^2)
            sage: C_ = C.change_ring(F)
            sage: g_ = g.change_ring(F)
            sage: g_(P).order()
            12
            sage: T = C_(-7 * z2 - 57, 31 * z2 - 52, 1)
            sage: g_(T).order()
            12
            sage: g_(P).weil_pairing(g_(T), 12)
            15*z2 + 204

        Another alternative is to simply extend the base field enough
        for the curve to have an untwisted Montgomery model::

            sage: C_ = E.change_ring(F).montgomery_model(); C_                          # needs sage.rings.finite_rings
            Elliptic Curve defined by y^2 = x^3 + 249*x^2 + x
            over Finite Field in z2 of size 257^2
            sage: h = C.defining_polynomial().change_ring(F); h                         # needs sage.rings.finite_rings
            -x^3 + 8*x^2*z - 127*y^2*z - x*z^2
            sage: C_.is_isomorphic(EllipticCurve_from_cubic(h).codomain())              # needs sage.rings.finite_rings
            True

        .. SEEALSO::

            The inverse conversion --- computing a Weierstrass model for a
            given Montgomery curve --- can be performed using
            :func:`~sage.schemes.elliptic_curves.constructor.EllipticCurve_from_cubic`.

        ALGORITHM: [CS2018]_, §2.4

        REFERENCES:

        - Original publication: [Mont1987]_, §10.3.1
        - More recent survey article: [CS2018]_
        """
    def plot(self, xmin=None, xmax=None, components: str = 'both', **args):
        """
        Draw a graph of this elliptic curve.

        The plot method is only implemented when there is a natural coercion
        from the base ring of ``self`` to ``RR``. In this case, ``self`` is
        plotted as if it was defined over ``RR``.

        INPUT:

        - ``xmin``, ``xmax`` -- (optional) points will be computed at
          least within this range, but possibly farther

        - ``components`` -- string; one of the following:

          - ``both`` -- (default), scale so that both bounded and
            unbounded components appear

          - ``bounded`` -- scale the plot to show the bounded
            component.  Raises an error if there is only one real
            component.

          - ``unbounded`` -- scale the plot to show the unbounded
            component, including the two flex points

        - ``plot_points`` -- passed to
          :func:`sage.plot.generate_plot_points`

        - ``adaptive_tolerance`` -- passed to
          :func:`sage.plot.generate_plot_points`

        - ``adaptive_recursion`` -- passed to
          :func:`sage.plot.generate_plot_points`

        - ``randomize`` -- passed to
          :func:`sage.plot.generate_plot_points`

        - ``**args`` -- all other options are passed to
          :class:`sage.plot.line.Line`

        EXAMPLES::

            sage: E = EllipticCurve([0, -1])
            sage: plot(E, rgbcolor=hue(0.7))                                            # needs sage.plot
            Graphics object consisting of 1 graphics primitive
            sage: E = EllipticCurve('37a')
            sage: plot(E)                                                               # needs sage.plot
            Graphics object consisting of 2 graphics primitives
            sage: plot(E, xmin=25, xmax=26)                                             # needs sage.plot
            Graphics object consisting of 2 graphics primitives

        With :issue:`12766` we added the components keyword::

            sage: E.real_components()
            2
            sage: E.plot(components='bounded')                                          # needs sage.plot
            Graphics object consisting of 1 graphics primitive
            sage: E.plot(components='unbounded')                                        # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        If there is only one component then specifying
        components='bounded' raises a ValueError::

            sage: E = EllipticCurve('9990be2')
            sage: E.plot(components='bounded')                                          # needs sage.plot
            Traceback (most recent call last):
            ...
            ValueError: no bounded component for this curve

        An elliptic curve defined over the Complex Field can not be plotted::

            sage: E = EllipticCurve(CC, [0,0,1,-1,0])
            sage: E.plot()                                                              # needs sage.plot
            Traceback (most recent call last):
            ...
            NotImplementedError: plotting of curves over Complex Field
            with 53 bits of precision is not implemented yet
        """
    @cached_method
    def formal_group(self):
        '''
        Return the formal group associated to this elliptic curve.

        This method is cached.

        EXAMPLES::

            sage: E = EllipticCurve("37a")
            sage: E.formal_group()
            Formal Group associated to the Elliptic Curve
            defined by y^2 + y = x^3 - x over Rational Field
        '''
    formal = formal_group
    def hyperelliptic_polynomials(self):
        """
        Return a pair of polynomials `g(x)`, `h(x)` such that this elliptic
        curve can be defined by the standard hyperelliptic equation

        .. MATH::

            y^2 + h(x)y = g(x).

        EXAMPLES::

            sage: R.<a1,a2,a3,a4,a6>=QQ[]
            sage: E = EllipticCurve([a1,a2,a3,a4,a6])
            sage: E.hyperelliptic_polynomials()
            (x^3 + a2*x^2 + a4*x + a6, a1*x + a3)
        """
    @cached_method
    def pari_curve(self):
        """
        Return the PARI curve corresponding to this elliptic curve.

        The result is cached.

        EXAMPLES::

            sage: # needs sage.libs.pari
            sage: E = EllipticCurve([RR(0), RR(0), RR(1), RR(-1), RR(0)])
            sage: e = E.pari_curve()
            sage: type(e)
            <... 'cypari2.gen.Gen'>
            sage: e.type()
            't_VEC'
            sage: e.disc()
            37.0000000000000

        Over a finite field::

            sage: EllipticCurve(GF(41), [2,5]).pari_curve()                             # needs sage.libs.pari
            [Mod(0, 41), Mod(0, 41), Mod(0, 41), Mod(2, 41), Mod(5, 41),
             Mod(0, 41), Mod(4, 41), Mod(20, 41), Mod(37, 41), Mod(27, 41),
             Mod(26, 41), Mod(4, 41), Mod(11, 41),
             Vecsmall([3]),
             [41, [9, 31, [6, 0, 0, 0]]], [0, 0, 0, 0]]

        Over a `p`-adic field::

            sage: # needs sage.libs.pari sage.rings.padics
            sage: Qp = pAdicField(5, prec=3)
            sage: E = EllipticCurve(Qp, [3, 4])
            sage: E.pari_curve()
            [0, 0, 0, 3, 4, 0, 6, 16, -9, -144, -3456, -8640, 1728/5,
             Vecsmall([2]), [O(5^3)], [0, 0]]
            sage: E.j_invariant()
            3*5^-1 + O(5)

        Over a number field::

            sage: K.<a> = QuadraticField(2)                                             # needs sage.libs.pari sage.rings.number_field
            sage: E = EllipticCurve([1,a])                                              # needs sage.libs.pari sage.rings.number_field
            sage: E.pari_curve()                                                        # needs sage.libs.pari sage.rings.number_field
            [0, 0, 0, Mod(1, y^2 - 2),
             Mod(y, y^2 - 2), 0, Mod(2, y^2 - 2), Mod(4*y, y^2 - 2),
             Mod(-1, y^2 - 2), Mod(-48, y^2 - 2), Mod(-864*y, y^2 - 2),
             Mod(-928, y^2 - 2), Mod(3456/29, y^2 - 2),
             Vecsmall([5]),
             [[y^2 - 2, [2, 0], 8, 1, [[1, -1.41421356237310; 1, 1.41421356237310],
             [1, -1.41421356237310; 1, 1.41421356237310],
             [16, -23; 16, 23], [2, 0; 0, 4], [4, 0; 0, 2], [2, 0; 0, 1],
             [2, [0, 2; 1, 0]], [2]], [-1.41421356237310, 1.41421356237310],
             [1, y], [1, 0; 0, 1], [1, 0, 0, 2; 0, 1, 1, 0]]], [0, 0, 0, 0, 0]]

        PARI no longer requires that the `j`-invariant has negative `p`-adic valuation::

            sage: E = EllipticCurve(Qp,[1, 1])                                          # needs sage.libs.pari sage.rings.padics
            sage: E.j_invariant()  # the j-invariant is a p-adic integer                # needs sage.libs.pari sage.rings.padics
            2 + 4*5^2 + O(5^3)
            sage: E.pari_curve()                                                        # needs sage.libs.pari sage.rings.padics
            [0, 0, 0, 1, 1, 0, 2, 4, -1, -48, -864, -496, 6912/31,
             Vecsmall([2]), [O(5^3)], [0, 0]]
        """
    def __pari__(self):
        """
        Return the PARI curve corresponding to this elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: pari(E)                                                               # needs sage.libs.pari
            [0, -1, 1, -10, -20, -4, -20, -79, -21, 496, 20008, -161051, -122023936/161051, Vecsmall([1]), [Vecsmall([64, -1])], [0, 0, 0, 0, 0, 0, 0, 0]]

        Over a finite field::

            sage: EllipticCurve(GF(2), [0,0,1,1,1]).__pari__()                          # needs sage.libs.pari
            [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, Vecsmall([4]), [1, [[Vecsmall([0, 1]), Vecsmall([0, 1]), Vecsmall([0, 1])], Vecsmall([0, 1]), [Vecsmall([0, 1]), Vecsmall([0]), Vecsmall([0]), Vecsmall([0])]]], [0, 0, 0, 0]]
        """
