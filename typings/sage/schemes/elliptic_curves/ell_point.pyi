from sage.libs.pari import pari as pari
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.finite_rings.integer_mod import Mod as Mod
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.quotient_ring import QuotientRing_generic as QuotientRing_generic
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RR as RR, RealField as RealField
from sage.schemes.curves.projective_curve import Hasse_bounds as Hasse_bounds
from sage.schemes.elliptic_curves.constructor import EllipticCurve as EllipticCurve
from sage.schemes.projective.projective_point import SchemeMorphism_point_abelian_variety_field as SchemeMorphism_point_abelian_variety_field, SchemeMorphism_point_projective_ring as SchemeMorphism_point_projective_ring
from sage.structure.coerce_actions import IntegerMulAction as IntegerMulAction
from sage.structure.element import AdditiveGroupElement as AdditiveGroupElement
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.sequence import Sequence as Sequence

class EllipticCurvePoint(AdditiveGroupElement, SchemeMorphism_point_projective_ring):
    """
    A point on an elliptic curve.
    """
    def __init__(self, *args, **kwds) -> None:
        """
        Initialize this elliptic-curve point.

        EXAMPLES::

            sage: E = EllipticCurve(Zmod(77), [1,1,1,1,1])
            sage: E(0)
            (0 : 1 : 0)
            sage: E(3, 9)
            (3 : 9 : 1)
            sage: E(6, 18, 2)
            (3 : 9 : 1)
            sage: E(66, 23, 22)
            (33 : 50 : 11)
        """
    def curve(self):
        """
        Return the curve that this point is on.

        This is a synonym for :meth:`scheme`.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: P = E([-1, 1])
            sage: P.curve()
            Elliptic Curve defined by y^2 + y = x^3 + x^2 - 2*x over Rational Field

            sage: E = EllipticCurve(QQ, [1, 1])
            sage: P = E(0, 1)
            sage: P.scheme()
            Elliptic Curve defined by y^2 = x^3 + x + 1 over Rational Field
            sage: P.scheme() == P.curve()
            True
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - 3,'a')                                      # needs sage.rings.number_field
            sage: P = E.base_extend(K)(1, a)                                            # needs sage.rings.number_field
            sage: P.scheme()                                                            # needs sage.rings.number_field
            Elliptic Curve defined by y^2 = x^3 + x + 1 over
             Number Field in a with defining polynomial x^2 - 3
        """
    def __bool__(self) -> bool:
        """
        Test whether this elliptic-curve point equals the neutral
        element of the group (i.e., the point at infinity).

        EXAMPLES::

            sage: E = EllipticCurve(GF(7), [1,1])
            sage: bool(E(0))
            False
            sage: bool(E.lift_x(2))
            True

        sage:

            sage: E = EllipticCurve(Zmod(77), [1,1,1,1,1])
            sage: bool(E(0))
            False
            sage: P = E(66, 23, 22); P
            (33 : 50 : 11)
            sage: bool(P)
            True
        """

class EllipticCurvePoint_field(EllipticCurvePoint, SchemeMorphism_point_abelian_variety_field):
    """
    A point on an elliptic curve over a field.  The point has coordinates
    in the base field.

    EXAMPLES::

        sage: E = EllipticCurve('37a')
        sage: E([0,0])
        (0 : 0 : 1)
        sage: E(0,0)               # brackets are optional
        (0 : 0 : 1)
        sage: E([GF(5)(0), 0])     # entries are coerced
        (0 : 0 : 1)

        sage: E(0.000, 0)
        (0 : 0 : 1)

        sage: E(1,0,0)
        Traceback (most recent call last):
        ...
        TypeError: Coordinates [1, 0, 0] do not define a point on
        Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field

    ::

        sage: E = EllipticCurve([0,0,1,-1,0])
        sage: S = E(QQ); S
        Abelian group of points on
         Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: K.<i> = NumberField(x^2 + 1)
        sage: E = EllipticCurve(K, [0,1,0,-160,308])
        sage: P = E(26, -120)
        sage: Q = E(2+12*i, -36+48*i)
        sage: P.order() == Q.order() == 4       # long time
        True
        sage: 2*P == 2*Q
        False

    ::

        sage: K.<t> = FractionField(PolynomialRing(QQ,'t'))
        sage: E = EllipticCurve([0,0,0,0,t^2])
        sage: P = E(0,t)
        sage: P, 2*P, 3*P
        ((0 : t : 1), (0 : -t : 1), (0 : 1 : 0))

    TESTS::

        sage: loads(S.dumps()) == S
        True
        sage: E = EllipticCurve('37a')
        sage: P = E(0,0); P
        (0 : 0 : 1)
        sage: loads(P.dumps()) == P
        True
        sage: T = 100*P
        sage: loads(T.dumps()) == T
        True

    Test pickling an elliptic curve that has known points on it::

        sage: e = EllipticCurve([0, 0, 1, -1, 0]); g = e.gens(); loads(dumps(e)) == e
        True

    Test that the refactoring from :issue:`14711` did preserve the behaviour
    of domain and codomain::

        sage: E = EllipticCurve(QQ,[1,1])
        sage: P = E(0,1)
        sage: P.domain()
        Spectrum of Rational Field
        sage: K.<a> = NumberField(x^2 - 3, 'a')                                         # needs sage.rings.number_field
        sage: P = E.base_extend(K)(1,a)                                                 # needs sage.rings.number_field
        sage: P.domain()                                                                # needs sage.rings.number_field
        Spectrum of Number Field in a with defining polynomial x^2 - 3
        sage: P.codomain()                                                              # needs sage.rings.number_field
        Elliptic Curve defined by y^2 = x^3 + x + 1
         over Number Field in a with defining polynomial x^2 - 3
        sage: P.codomain() == P.curve()                                                 # needs sage.rings.number_field
        True
    """
    def __init__(self, curve, v, check: bool = True) -> None:
        """
        Constructor for a point on an elliptic curve.

        INPUT:

        - ``curve`` -- an elliptic curve
        - ``v`` -- data determining a point (another point, the integer
          0, or a tuple of coordinates)

        EXAMPLES::

            sage: E = EllipticCurve('43a')
            sage: P = E([2, -4, 2]); P
            (1 : -2 : 1)
            sage: P == E([1,-2])
            True
            sage: P = E(0); P
            (0 : 1 : 0)
            sage: P=E(2, -4, 2); P
            (1 : -2 : 1)
        """
    def __getitem__(self, n):
        """
        Return the n'th coordinate of this point.

        EXAMPLES::

            sage: E = EllipticCurve('42a')
            sage: P = E([-17, -51, 17])
            sage: [P[i] for i in [2,1,0]]
            [1, -3, -1]
        """
    def __iter__(self):
        """
        Return the coordinates of this point as a list.

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: list(E([0,0]))
            [0, 0, 1]
        """
    def __tuple__(self):
        """
        Return the coordinates of this point as a tuple.

        EXAMPLES::

            sage: E = EllipticCurve('44a')
            sage: P = E([1, -2, 1])
            sage: P.__tuple__()
            (1, -2, 1)
        """
    def __pari__(self):
        """
        Convert this point to PARI format.

        EXAMPLES::

            sage: E = EllipticCurve([0,0,0,3,0])
            sage: O = E(0)
            sage: P = E.point([1,2])
            sage: O.__pari__()
            [0]
            sage: P.__pari__()
            [1, 2]

        The following implicitly calls O.__pari__() and P.__pari__()::

            sage: pari(E).elladd(O,P)
            [1, 2]

        TESTS:

        Try the same over a finite field::

            sage: E = EllipticCurve(GF(11), [0,0,0,3,0])
            sage: O = E(0)
            sage: P = E.point([1,2])
            sage: O.__pari__()
            [0]
            sage: P.__pari__()
            [Mod(1, 11), Mod(2, 11)]

        We no longer need to explicitly call ``pari(O)`` and ``pari(P)``
        after :issue:`11868`::

            sage: pari(E).elladd(O, P)
            [Mod(1, 11), Mod(2, 11)]
        """
    def order(self):
        """
        Return the order of this point on the elliptic curve.

        If the point is zero, returns 1, otherwise raise a
        :exc:`NotImplementedError`.

        For curves over number fields and finite fields, see below.

        .. NOTE::

            :meth:`additive_order` is a synonym for :meth:`order`

        EXAMPLES::

            sage: K.<t> = FractionField(PolynomialRing(QQ,'t'))
            sage: E = EllipticCurve([0, 0, 0, -t^2, 0])
            sage: P = E(t,0)
            sage: P.order()
            Traceback (most recent call last):
            ...
            NotImplementedError: Computation of order of a point not implemented
            over general fields.
            sage: E(0).additive_order()
            1
            sage: E(0).order() == 1
            True
        """
    additive_order = order
    def __bool__(self) -> bool:
        """
        Return ``True`` if this is not the zero point on the curve.

        EXAMPLES::

            sage: E = EllipticCurve('37a')
            sage: P = E(0); P
            (0 : 1 : 0)
            sage: P.is_zero()
            True
            sage: P = E.gens()[0]
            sage: P.is_zero()
            False
        """
    def has_order(self, n) -> bool:
        """
        Test if this point has order exactly `n`.

        INPUT:

        - ``n`` -- integer or its :class:`~sage.structure.factorization.Factorization`

        ALGORITHM:

        Compare a cached order if available, otherwise use :func:`sage.groups.generic.has_order`.

        EXAMPLES::

            sage: E = EllipticCurve('26b1')
            sage: P = E(1, 0)
            sage: P.has_order(7)
            True
            sage: P._order
            7
            sage: P.has_order(7)
            True

        It also works with a :class:`~sage.structure.factorization.Factorization` object::

            sage: E = EllipticCurve(GF(419), [1,0])
            sage: P = E(-33, 8)
            sage: P.has_order(factor(21))
            True
            sage: P._order
            21
            sage: P.has_order(factor(21))
            True

        This method can be much faster than computing the order and comparing::

            sage: # not tested -- timings are different each time
            sage: p = 4 * prod(primes(3,377)) * 587 - 1
            sage: E = EllipticCurve(GF(p), [1,0])
            sage: %timeit P = E.random_point(); P.set_order(multiple=p+1)
            72.4 ms ± 773 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
            sage: %timeit P = E.random_point(); P.has_order(p+1)
            32.8 ms ± 3.12 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
            sage: fac = factor(p+1)
            sage: %timeit P = E.random_point(); P.has_order(fac)
            30.6 ms ± 3.48 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

        The order is cached once it has been confirmed once, and the cache is
        shared with :meth:`order`::

            sage: # not tested -- timings are different each time
            sage: P, = E.gens()
            sage: delattr(P, '_order')
            sage: %time P.has_order(p+1)
            CPU times: user 83.6 ms, sys: 30 µs, total: 83.6 ms
            Wall time: 83.8 ms
            True
            sage: %time P.has_order(p+1)
            CPU times: user 31 µs, sys: 2 µs, total: 33 µs
            Wall time: 37.9 µs
            True
            sage: %time P.order()
            CPU times: user 11 µs, sys: 0 ns, total: 11 µs
            Wall time: 16 µs
            5326738796327623094747867617954605554069371494832722337612446642054009560026576537626892113026381253624626941643949444792662881241621373288942880288065660
            sage: delattr(P, '_order')
            sage: %time P.has_order(fac)
            CPU times: user 68.6 ms, sys: 17 µs, total: 68.7 ms
            Wall time: 68.7 ms
            True
            sage: %time P.has_order(fac)
            CPU times: user 92 µs, sys: 0 ns, total: 92 µs
            Wall time: 97.5 µs
            True
            sage: %time P.order()
            CPU times: user 10 µs, sys: 1e+03 ns, total: 11 µs
            Wall time: 14.5 µs
            5326738796327623094747867617954605554069371494832722337612446642054009560026576537626892113026381253624626941643949444792662881241621373288942880288065660

        TESTS::

            sage: E = EllipticCurve([1,2,3,4,5])
            sage: E(0).has_order(1)
            True
            sage: E(0).has_order(Factorization([]))
            True
        """
    def has_finite_order(self) -> bool:
        """
        Return ``True`` if this point has finite additive order as an
        element of the group of points on this curve.

        For fields other than number fields and finite fields, this is
        NotImplemented unless self.is_zero().

        EXAMPLES::

            sage: K.<t> = FractionField(PolynomialRing(QQ,'t'))
            sage: E = EllipticCurve([0, 0, 0, -t^2, 0])
            sage: P = E(0)
            sage: P.has_finite_order()
            True
            sage: P = E(t,0)
            sage: P.has_finite_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: Computation of order of a point not implemented
            over general fields.
            sage: (2*P).is_zero()
            True
        """
    is_finite_order = has_finite_order
    def has_infinite_order(self) -> bool:
        """
        Return ``True`` if this point has infinite additive order as an element
        of the group of points on this curve.

        For fields other than number fields and finite fields, this is
        NotImplemented unless ``self.is_zero()``.

        EXAMPLES::

            sage: K.<t> = FractionField(PolynomialRing(QQ,'t'))
            sage: E = EllipticCurve([0, 0, 0, -t^2, 0])
            sage: P = E(0)
            sage: P.has_infinite_order()
            False
            sage: P = E(t,0)
            sage: P.has_infinite_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: Computation of order of a point not implemented over general fields.
            sage: (2*P).is_zero()
            True
        """
    def plot(self, **args):
        """
        Plot this point on an elliptic curve.

        INPUT:

        - ``**args`` -- all arguments get passed directly onto the point
          plotting function

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: P = E([-1,1])
            sage: P.plot(pointsize=30, rgbcolor=(1,0,0))                                # needs sage.plot
            Graphics object consisting of 1 graphics primitive
        """
    def xy(self):
        """
        Return the `x` and `y` coordinates of this point, as a 2-tuple.
        If this is the point at infinity, a :exc:`ZeroDivisionError` is raised.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: P = E([-1,1])
            sage: P.xy()
            (-1, 1)
            sage: Q = E(0); Q
            (0 : 1 : 0)
            sage: Q.xy()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero
        """
    def x(self):
        """
        Return the `x` coordinate of this point, as an element of the base field.
        If this is the point at infinity, a :exc:`ZeroDivisionError` is raised.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: P = E([-1,1])
            sage: P.x()
            -1
            sage: Q = E(0); Q
            (0 : 1 : 0)
            sage: Q.x()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero
        """
    def y(self):
        """
        Return the `y` coordinate of this point, as an element of the base field.
        If this is the point at infinity, a :exc:`ZeroDivisionError` is raised.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: P = E([-1,1])
            sage: P.y()
            1
            sage: Q = E(0); Q
            (0 : 1 : 0)
            sage: Q.y()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero
        """
    def is_divisible_by(self, m):
        """
        Return ``True`` if there exists a point `Q` defined over the same
        field as ``self`` such that `mQ` == ``self``.

        INPUT:

        - ``m`` -- positive integer

        OUTPUT:

        boolean; ``True`` if there is a solution, else False.

        .. WARNING::

            This function usually triggers the computation of the
            `m`-th division polynomial of the associated elliptic
            curve, which will be expensive if `m` is large, though it
            will be cached for subsequent calls with the same `m`.

        EXAMPLES::

            sage: E = EllipticCurve('389a')
            sage: Q = 5*E(0,0); Q
            (-2739/1444 : -77033/54872 : 1)
            sage: Q.is_divisible_by(4)
            False
            sage: Q.is_divisible_by(5)
            True

        A finite field example::

            sage: E = EllipticCurve(GF(101), [23,34])
            sage: E.cardinality().factor()
            2 * 53
            sage: Set([T.order() for T in E.points()])
            {1, 106, 2, 53}
            sage: len([T for T in E.points() if T.is_divisible_by(2)])
            53
            sage: len([T for T in E.points() if T.is_divisible_by(3)])
            106

        TESTS:

        This shows that the bug reported at :issue:`10076` is fixed::

            sage: # needs sage.rings.number_field
            sage: K = QuadraticField(8,'a')
            sage: E = EllipticCurve([K(0),0,0,-1,0])
            sage: P = E([-1,0])
            sage: P.is_divisible_by(2)
            False
            sage: P.division_points(2)
            []

        Note that it is not sufficient to test that
        ``self.division_points(m,poly_only=True)`` has roots::

            sage: P.division_points(2, poly_only=True).roots()                          # needs sage.rings.number_field
            [(1/2*a - 1, 1), (-1/2*a - 1, 1)]

            sage: # needs sage.rings.number_field
            sage: tor = E.torsion_points(); len(tor)
            8
            sage: [T.order() for T in tor]
            [1, 2, 4, 4, 2, 2, 4, 4]
            sage: all(T.is_divisible_by(3) for T in tor)
            True
            sage: sorted(T for T in tor if T.is_divisible_by(2))
            [(0 : 1 : 0), (1 : 0 : 1)]
            sage: sorted(Set([2*T for T in tor]))
            [(0 : 1 : 0), (1 : 0 : 1)]
        """
    def division_points(self, m, poly_only: bool = False):
        """
        Return a list of all points `Q` such that `mQ=P` where `P` = ``self``.

        Only points on the elliptic curve containing ``self`` and defined
        over the base field are included.

        INPUT:

        - ``m`` -- positive integer

        - ``poly_only`` -- boolean (default: ``False``); if ``True`` return
          polynomial whose roots give all possible `x`-coordinates of
          `m`-th roots of ``self``

        OUTPUT: a (possibly empty) list of solutions `Q` to `mQ=P`,
        where `P` = ``self``

        .. SEEALSO ::

            :meth:`~sage.schemes.elliptic_curves.hom.EllipticCurveHom.inverse_image`

        EXAMPLES:

        We find the five 5-torsion points on an elliptic curve::

            sage: E = EllipticCurve('11a'); E
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: P = E(0); P
            (0 : 1 : 0)
            sage: P.division_points(5)
            [(0 : 1 : 0), (5 : -6 : 1), (5 : 5 : 1), (16 : -61 : 1), (16 : 60 : 1)]

        Note above that 0 is included since [5]*0 = 0.

        We create a curve of rank 1 with no torsion and do a consistency check::

            sage: E = EllipticCurve('11a').quadratic_twist(-7)
            sage: Q = E([44,-270])
            sage: (4*Q).division_points(4)
            [(44 : -270 : 1)]

        We create a curve over a non-prime finite field with group of
        order `18`::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF((5,2))
            sage: E = EllipticCurve(k, [1,2+a,3,4*a,2])
            sage: P = E([3, 3*a+4])
            sage: factor(E.order())
            2 * 3^2
            sage: P.order()
            9

        We find the `1`-division points as a consistency check -- there
        is just one, of course::

            sage: P.division_points(1)                                                  # needs sage.rings.finite_rings
            [(3 : 3*a + 4 : 1)]

        The point `P` has order coprime to 2 but divisible by 3, so::

            sage: P.division_points(2)                                                  # needs sage.rings.finite_rings
            [(2*a + 1 : 3*a + 4 : 1), (3*a + 1 : a : 1)]

        We check that each of the 2-division points works as claimed::

            sage: [2*Q for Q in P.division_points(2)]                                   # needs sage.rings.finite_rings
            [(3 : 3*a + 4 : 1), (3 : 3*a + 4 : 1)]

        Some other checks::

            sage: P.division_points(3)                                                  # needs sage.rings.finite_rings
            []
            sage: P.division_points(4)                                                  # needs sage.rings.finite_rings
            [(0 : 3*a + 2 : 1), (1 : 0 : 1)]
            sage: P.division_points(5)                                                  # needs sage.rings.finite_rings
            [(1 : 1 : 1)]

        An example over a number field (see :issue:`3383`)::

            sage: # needs sage.rings.number_field
            sage: E = EllipticCurve('19a1')
            sage: x = polygen(ZZ, 'x')
            sage: K.<t> = NumberField(x^9 - 3*x^8 - 4*x^7 + 16*x^6 - 3*x^5
            ....:                     - 21*x^4 + 5*x^3 + 7*x^2 - 7*x + 1)
            sage: EK = E.base_extend(K)
            sage: E(0).division_points(3)
            [(0 : 1 : 0), (5 : -10 : 1), (5 : 9 : 1)]
            sage: EK(0).division_points(3)
            [(0 : 1 : 0), (5 : 9 : 1), (5 : -10 : 1)]
            sage: E(0).division_points(9)
            [(0 : 1 : 0), (5 : -10 : 1), (5 : 9 : 1)]
            sage: EK(0).division_points(9)
            [(0 : 1 : 0), (5 : 9 : 1), (5 : -10 : 1), (-150/121*t^8 + 414/121*t^7 + 1481/242*t^6 - 2382/121*t^5 - 103/242*t^4 + 629/22*t^3 - 367/242*t^2 - 1307/121*t + 625/121 : 35/484*t^8 - 133/242*t^7 + 445/242*t^6 - 799/242*t^5 + 373/484*t^4 + 113/22*t^3 - 2355/484*t^2 - 753/242*t + 1165/484 : 1), (-150/121*t^8 + 414/121*t^7 + 1481/242*t^6 - 2382/121*t^5 - 103/242*t^4 + 629/22*t^3 - 367/242*t^2 - 1307/121*t + 625/121 : -35/484*t^8 + 133/242*t^7 - 445/242*t^6 + 799/242*t^5 - 373/484*t^4 - 113/22*t^3 + 2355/484*t^2 + 753/242*t - 1649/484 : 1), (-1383/484*t^8 + 970/121*t^7 + 3159/242*t^6 - 5211/121*t^5 + 37/484*t^4 + 654/11*t^3 - 909/484*t^2 - 4831/242*t + 6791/484 : 927/121*t^8 - 5209/242*t^7 - 8187/242*t^6 + 27975/242*t^5 - 1147/242*t^4 - 1729/11*t^3 + 1566/121*t^2 + 12873/242*t - 10871/242 : 1), (-1383/484*t^8 + 970/121*t^7 + 3159/242*t^6 - 5211/121*t^5 + 37/484*t^4 + 654/11*t^3 - 909/484*t^2 - 4831/242*t + 6791/484 : -927/121*t^8 + 5209/242*t^7 + 8187/242*t^6 - 27975/242*t^5 + 1147/242*t^4 + 1729/11*t^3 - 1566/121*t^2 - 12873/242*t + 10629/242 : 1), (-4793/484*t^8 + 6791/242*t^7 + 10727/242*t^6 - 18301/121*t^5 + 2347/484*t^4 + 2293/11*t^3 - 7311/484*t^2 - 17239/242*t + 26767/484 : 30847/484*t^8 - 21789/121*t^7 - 34605/121*t^6 + 117164/121*t^5 - 10633/484*t^4 - 29437/22*t^3 + 39725/484*t^2 + 55428/121*t - 176909/484 : 1), (-4793/484*t^8 + 6791/242*t^7 + 10727/242*t^6 - 18301/121*t^5 + 2347/484*t^4 + 2293/11*t^3 - 7311/484*t^2 - 17239/242*t + 26767/484 : -30847/484*t^8 + 21789/121*t^7 + 34605/121*t^6 - 117164/121*t^5 + 10633/484*t^4 + 29437/22*t^3 - 39725/484*t^2 - 55428/121*t + 176425/484 : 1)]

        TESTS:

        Check that :issue:`24844` is fixed::

            sage: # needs sage.rings.finite_rings
            sage: p = next_prime(1000000)
            sage: E = EllipticCurve(GF(p), 123, 456)
            sage: pts = E(0).division_points(3)
            sage: P = pts[1]; P
            (389063 : 124244 : 1)
            sage: P._order
            3

        When we successfully divide a point known to have infinite
        order, the points returned know that they also have infinite
        order::

            sage: E = EllipticCurve([0,0,1,-1,0])
            sage: P = E(-1,0)
            sage: P.order()
            +Infinity
            sage: pts = P.division_points(3);  len(pts)
            1
            sage: [(Q,Q._order) for Q in pts]
            [((0 : -1 : 1), +Infinity)]

        When we successfully divide a point of known finite order `n`,
        the points returned know that they also have finite order `nk`
        for some divisor `k` of `m`::

          sage: E = EllipticCurve([1, 0, 1, -19, 26])
          sage: [(Q,Q._order) for Q in E(0).division_points(12)]
          [((0 : 1 : 0), 1),
           ((-5 : 2 : 1), 2),
           ((-2 : -7 : 1), 6),
           ((-2 : 8 : 1), 6),
           ((1 : -4 : 1), 6),
           ((1 : 2 : 1), 6),
           ((7/4 : -11/8 : 1), 2),
           ((3 : -2 : 1), 2),
           ((4 : -7 : 1), 3),
           ((4 : 2 : 1), 3),
           ((13 : -52 : 1), 6),
           ((13 : 38 : 1), 6)]
          sage: P = E(4,-7)
          sage: P.order()
          3
          sage: [(Q,Q._order) for Q in P.division_points(4)]
          [((-2 : -7 : 1), 6), ((1 : 2 : 1), 6), ((4 : -7 : 1), 3), ((13 : 38 : 1), 6)]

        Check for :issue:`38796`::

            sage: E = EllipticCurve(GF(127), [1,1])
            sage: P = E(72, 24)
            sage: [-1*Q for Q in P.division_points(-1)]
            [(72 : 24 : 1)]
        """
    def set_order(self, value=None, *, multiple=None, check: bool = True) -> None:
        """
        Set the cached order of this point (i.e., the value of
        ``self._order``) to the given ``value``.

        Alternatively, when ``multiple`` is given, this method will
        first run :func:`~sage.groups.generic.order_from_multiple`
        to determine the exact order from the given multiple of the
        point order, then cache the result.

        Use this when you know a priori the order of this point, or
        a multiple of the order, to avoid a potentially expensive
        order calculation.

        INPUT:

        - ``value`` -- positive integer
        - ``multiple`` -- positive integer; mutually exclusive with ``value``

        OUTPUT: none

        EXAMPLES:

        This example illustrates basic usage.

        ::

            sage: E = EllipticCurve(GF(7), [0, 1])  # This curve has order 12
            sage: G = E(5, 0)
            sage: G.set_order(2)
            sage: 2*G
            (0 : 1 : 0)
            sage: G = E(0, 6)
            sage: G.set_order(multiple=12)
            sage: G._order
            3

        We now give a more interesting case, the NIST-P521 curve. Its
        order is too big to calculate with Sage, and takes a long time
        using other packages, so it is very useful here.

        ::

            sage: # needs sage.rings.finite_rings
            sage: p = 2^521 - 1
            sage: prev_proof_state = proof.arithmetic()
            sage: proof.arithmetic(False)  # turn off primality checking
            sage: F = GF(p)
            sage: A = p - 3
            sage: B = 1093849038073734274511112390766805569936207598951683748994586394495953116150735016013708737573759623248592132296706313309438452531591012912142327488478985984
            sage: q = 6864797660130609714981900799081393217269435300143305409394463459185543183397655394245057746333217197532963996371363321113864768612440380340372808892707005449
            sage: E = EllipticCurve([F(A), F(B)])
            sage: G = E.random_point()
            sage: G.set_order(q)
            sage: G.order() * G  # This takes practically no time.
            (0 : 1 : 0)
            sage: proof.arithmetic(prev_proof_state) # restore state

        Using ``.set_order()`` with a ``multiple=`` argument can
        be used to compute a point's order *significantly* faster
        than calling :meth:`order` if the point is already known
        to be `m`-torsion::

            sage: F.<a> = GF((10007, 23))
            sage: E = EllipticCurve(F, [9,9])
            sage: n = E.order()
            sage: m = 5 * 47 * 139 * 1427 * 2027 * 4831 * 275449 * 29523031
            sage: assert m.divides(n)
            sage: P = n/m * E.lift_x(6747+a)
            sage: assert m * P == 0
            sage: P.set_order(multiple=m)   # compute exact order
            sage: factor(m // P.order())    # order is now cached
            47 * 139

        The algorithm used internally for this functionality is
        :meth:`~sage.groups.generic.order_from_multiple`.
        Indeed, simply calling :meth:`order` on ``P`` would take
        much longer since factoring ``n`` is fairly expensive::

            sage: n == m * 6670822796985115651 * 441770032618665681677 * 9289973478285634606114927
            True

        It is an error to pass a ``value`` equal to `0`::

            sage: # needs sage.rings.finite_rings
            sage: E = EllipticCurve(GF(7), [0, 1])  # This curve has order 12
            sage: G = E.random_point()
            sage: G.set_order(0)
            Traceback (most recent call last):
            ...
            ValueError: Value 0 illegal for point order
            sage: G.set_order(1000)
            Traceback (most recent call last):
            ...
            ValueError: Value 1000 illegal: outside max Hasse bound

        It is also very likely an error to pass a value which is not the actual
        order of this point. How unlikely is determined by the factorization of
        the actual order, and the actual group structure::

            sage: E = EllipticCurve(GF(7), [0, 1])  # This curve has order 12
            sage: G = E(5, 0)   # G has order 2
            sage: G.set_order(11)
            Traceback (most recent call last):
            ...
            ValueError: Value 11 illegal: 11 * (5 : 0 : 1) is not the identity

        However, ``set_order`` can be fooled. For instance, the order
        can be set to a multiple the actual order::

            sage: E = EllipticCurve(GF(7), [0, 1])  # This curve has order 12
            sage: G = E(5, 0)   # G has order 2
            sage: G.set_order(8)
            sage: G.order()
            8

        TESTS:

        Check that some invalid inputs are caught::

            sage: E = EllipticCurve(GF(101), [5,5])
            sage: P = E.lift_x(11)
            sage: P.set_order(17, multiple=119)
            Traceback (most recent call last):
            ...
            ValueError: cannot pass both value and multiple
            sage: P.set_order(17)
            sage: P.set_order(multiple=119+1)
            Traceback (most recent call last):
            ...
            ValueError: previously cached order 17 does not divide given multiple 120
            sage: P.set_order(119)
            Traceback (most recent call last):
            ...
            ValueError: value 119 contradicts previously cached order 17

        AUTHORS:

        - Mariah Lenox (2011-02-16)
        - Lorenz Panny (2022): add ``multiple=`` option
        """
    def weil_pairing(self, Q, n, algorithm=None):
        """
        Compute the Weil pairing of this point with another point `Q`
        on the same curve.

        INPUT:

        - ``Q`` -- another point on the same curve as ``self``

        - ``n`` -- integer `n` such that `nP = nQ = (0:1:0)`, where
          `P` is ``self``

        - ``algorithm`` -- (default: ``None``) choices are ``'pari'``
          and ``'sage'``. PARI is usually significantly faster, but it
          only works over finite fields. When ``None`` is given, a
          suitable algorithm is chosen automatically.

        OUTPUT: an `n`-th root of unity in the base field of the curve

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF((2,5))
            sage: E = EllipticCurve(F, [0,0,1,1,1])
            sage: P = E(a^4 + 1, a^3)
            sage: Fx.<b> = GF((2, 4*5))
            sage: Ex = EllipticCurve(Fx, [0,0,1,1,1])
            sage: phi = Hom(F, Fx)(F.gen().minpoly().roots(Fx)[0][0])
            sage: Px = Ex(phi(P.x()), phi(P.y()))
            sage: O = Ex(0)
            sage: Qx = Ex(b^19 + b^18 + b^16 + b^12 + b^10 + b^9 + b^8 + b^5 + b^3 + 1,
            ....:         b^18 + b^13 + b^10 + b^8 + b^5 + b^4 + b^3 + b)
            sage: Px.weil_pairing(Qx, 41) == b^19 + b^15 + b^9 + b^8 + b^6 + b^4 + b^3 + b^2 + 1
            True
            sage: Px.weil_pairing(17*Px, 41) == Fx(1)
            True
            sage: Px.weil_pairing(O, 41) == Fx(1)
            True

        An error is raised if either point is not `n`-torsion::

            sage: Px.weil_pairing(O, 40)                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: points must both be n-torsion

        A larger example (see :issue:`4964`)::

            sage: # needs sage.rings.finite_rings
            sage: P, Q = EllipticCurve(GF((19,4),'a'), [-1,0]).gens()
            sage: P.order(), Q.order()
            (360, 360)
            sage: z = P.weil_pairing(Q, 360)
            sage: z.multiplicative_order()
            360

        Another larger example::

            sage: F = GF(65537^2, modulus=[3,-1,1], name='a')
            sage: F.inject_variables()
            Defining a
            sage: E = EllipticCurve(F, [0,1])
            sage: P = E(22, 28891)
            sage: Q = E(-93, 2728*a + 64173)
            sage: P.weil_pairing(Q, 7282, algorithm='sage')
            53278*a + 36700

        An example over a number field::

            sage: # needs sage.rings.number_field
            sage: E = EllipticCurve('11a1').change_ring(CyclotomicField(5))
            sage: P, Q = E.torsion_subgroup().gens()
            sage: P, Q = (P.element(), Q.element())
            sage: (P.order(), Q.order())
            (5, 5)
            sage: P.weil_pairing(Q, 5)
            zeta5^2
            sage: Q.weil_pairing(P, 5)
            zeta5^3

        TESTS:

        Check that the original Sage implementation still works and
        that the result coincides with the PARI implementation::

            sage: # needs sage.rings.finite_rings
            sage: GF(65537^2).inject_variables()
            Defining z2
            sage: E = EllipticCurve(GF(65537^2), [0,1])
            sage: R, S = E.torsion_basis(7282)
            sage: a, b = ZZ.random_element(), ZZ.random_element()
            sage: P = a*R + b*S
            sage: c, d = ZZ.random_element(), ZZ.random_element()
            sage: Q = c*R + d*S
            sage: P.weil_pairing(Q, 7282, algorithm='sage') == P.weil_pairing(Q, 7282, algorithm='pari')
            True

        Passing an unknown ``algorithm=`` argument should fail::

            sage: P.weil_pairing(Q, 7282, algorithm='_invalid_')                        # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: unknown algorithm

        ALGORITHM:

        - For ``algorithm='pari'``: :pari:`ellweilpairing`.

        - For ``algorithm='sage'``:
          Implemented using Proposition 8 in [Mil2004]_.  The value 1 is
          returned for linearly dependent input points.  This condition
          is caught via a :exc:`ZeroDivisionError`, since the use of a
          discrete logarithm test for linear dependence is much too slow
          for large `n`.

        AUTHORS:

        - David Hansen (2009-01-25)
        - Lorenz Panny (2022): ``algorithm='pari'``
        """
    def tate_pairing(self, Q, n, k, q=None):
        '''
        Return Tate pairing of `n`-torsion point `P = self` and point `Q`.

        The value returned is `f_{n,P}(Q)^e` where `f_{n,P}` is a function with
        divisor `n[P]-n[O].`. This is also known as the "modified Tate
        pairing". It is a well-defined bilinear map.

        INPUT:

        - ``P=self`` -- elliptic curve point having order `n`

        - ``Q`` -- elliptic curve point on same curve as `P` (can be any order)

        - ``n`` -- positive integer; order of `P`

        - ``k`` -- positive integer; embedding degree

        - ``q`` -- positive integer; size of base field (the "big"
          field is `GF(q^k)`. `q` needs to be set only if its value
          cannot be deduced.)

        OUTPUT:

        An `n`-th root of unity in the base field ``self.curve().base_field()``.

        EXAMPLES:

        A simple example, pairing a point with itself, and pairing a point with
        another rational point::

            sage: p = 103; A = 1; B = 18; E = EllipticCurve(GF(p), [A, B])
            sage: P = E(33, 91); n = P.order(); n
            19
            sage: k = GF(n)(p).multiplicative_order(); k
            6
            sage: P.tate_pairing(P, n, k)
            1
            sage: Q = E(87, 51)
            sage: P.tate_pairing(Q, n, k)
            1
            sage: set_random_seed(35)
            sage: P.tate_pairing(P, n, k)
            1

        We now let `Q` be a point on the same curve as above, but defined over
        the pairing extension field, and we also demonstrate the bilinearity of
        the pairing::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF((p,k))
            sage: EK = E.base_extend(K); P = EK(P)
            sage: Qx = 69*a^5 + 96*a^4 + 22*a^3 + 86*a^2 + 6*a + 35
            sage: Qy = 34*a^5 + 24*a^4 + 16*a^3 + 41*a^2 + 4*a + 40
            sage: Q = EK(Qx, Qy);

        Multiply by cofactor so Q has order n::

            sage: # needs sage.rings.finite_rings
            sage: h = 551269674; Q = h*Q
            sage: P = EK(P); P.tate_pairing(Q, n, k)
            24*a^5 + 34*a^4 + 3*a^3 + 69*a^2 + 86*a + 45
            sage: s = Integer(randrange(1,n))
            sage: ans1 = (s*P).tate_pairing(Q, n, k)
            sage: ans2 = P.tate_pairing(s*Q, n, k)
            sage: ans3 = P.tate_pairing(Q, n, k)^s
            sage: ans1 == ans2 == ans3
            True
            sage: (ans1 != 1) and (ans1^n == 1)
            True

        Here is an example of using the Tate pairing to compute the Weil
        pairing (using the same data as above)::

            sage: # needs sage.rings.finite_rings
            sage: e = Integer((p^k-1)/n); e
            62844857712
            sage: P.weil_pairing(Q, n)^e
            94*a^5 + 99*a^4 + 29*a^3 + 45*a^2 + 57*a + 34
            sage: P.tate_pairing(Q, n, k) == P._miller_(Q, n)^e
            True
            sage: Q.tate_pairing(P, n, k) == Q._miller_(P, n)^e
            True
            sage: P.tate_pairing(Q, n, k)/Q.tate_pairing(P, n, k)
            94*a^5 + 99*a^4 + 29*a^3 + 45*a^2 + 57*a + 34

        An example where we have to pass the base field size (and we again have
        agreement with the Weil pairing)::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF((2,5))
            sage: E = EllipticCurve(F, [0,0,1,1,1])
            sage: P = E(a^4 + 1, a^3)
            sage: Fx.<b> = GF((2,4*5))
            sage: Ex = EllipticCurve(Fx,[0,0,1,1,1])
            sage: phi = Hom(F, Fx)(F.gen().minpoly().roots(Fx)[0][0])
            sage: Px = Ex(phi(P.x()), phi(P.y()))
            sage: Qx = Ex(b^19 + b^18 + b^16 + b^12 + b^10 + b^9 + b^8 + b^5 + b^3 + 1,
            ....:         b^18 + b^13 + b^10 + b^8 + b^5 + b^4 + b^3 + b)
            sage: Px.tate_pairing(Qx, n=41, k=4)
            Traceback (most recent call last):
            ...
            ValueError: Unexpected field degree: set keyword argument q equal to
            the size of the base field (big field is GF(q^4)).
            sage: num = Px.tate_pairing(Qx, n=41, k=4, q=32); num
            b^19 + b^14 + b^13 + b^12 + b^6 + b^4 + b^3
            sage: den = Qx.tate_pairing(Px, n=41, k=4, q=32); den
            b^19 + b^17 + b^16 + b^15 + b^14 + b^10 + b^6 + b^2 + 1
            sage: e = Integer((32^4-1)/41); e
            25575
            sage: Px.weil_pairing(Qx, 41)^e == num/den
            True

        An example over a large base field::

            sage: F = GF(65537^2, modulus=[3,46810,1], name=\'z2\')
            sage: F.inject_variables()
            Defining z2
            sage: E = EllipticCurve(F, [0,1])
            sage: P = E(22, 28891)
            sage: Q = E(-93, 40438*z2 + 31573)
            sage: P.tate_pairing(Q, 7282, 2)
            34585*z2 + 4063

        TESTS:

        The point ``P (self)`` must have ``n`` torsion::

            sage: P.tate_pairing(Q, 163, 2)
            Traceback (most recent call last):
            ...
            ValueError: The point P must be n-torsion

        We must have that ``n`` divides ``q^k - 1``, this is only checked when q is supplied::

            sage: P.tate_pairing(Q, 7282, 2, q=123)
            Traceback (most recent call last):
            ...
            ValueError: n does not divide (q^k - 1) for the supplied value of q

        The Tate pairing is only defined for points on curves defined over finite fields::

            sage: E = EllipticCurve([0,1])
            sage: P = E(2,3)
            sage: P.tate_pairing(P, 6, 1)
            Traceback (most recent call last):
            ...
            NotImplementedError: Reduced Tate pairing is currently only implemented for finite fields

        ALGORITHM:

        - :pari:`elltatepairing` computes the
          non-reduced tate pairing and the exponentiation is handled by
          Sage using user input for `k` (and optionally `q`).

        AUTHORS:

        - Mariah Lenox (2011-03-07)
        - Giacomo Pope (2024): Use of PARI for the non-reduced Tate pairing
        '''
    def ate_pairing(self, Q, n, k, t, q=None):
        '''
        Return ate pairing of `n`-torsion points `P` (``=self``) and `Q`.

        Also known as the `n`-th modified ate pairing. `P` is `GF(q)`-rational,
        and `Q` must be an element of `Ker(\\pi-p)`, where `\\pi` is the
        `q`-frobenius map (and hence `Q` is `GF(q^k)`-rational).

        INPUT:

        - ``P`` (``=self``) -- a point of order `n`, in `ker(\\pi-1)`, where
          `\\pi` is the `q`-Frobenius map (e.g., `P` is `q`-rational)

        - ``Q`` -- a point of order `n` in `ker(\\pi-q)`

        - ``n`` -- the order of `P` and `Q`

        - ``k`` -- the embedding degree

        - ``t`` -- the trace of Frobenius of the curve over `GF(q)`

        - ``q`` -- (default: ``None``) the size of base field (the "big"
          field is `GF(q^k)`). `q` needs to be set only if its value
          cannot be deduced.

        OUTPUT:

        FiniteFieldElement in `GF(q^k)` -- the ate pairing of `P` and `Q`.

        EXAMPLES:

        An example with embedding degree 6::

            sage: # needs sage.rings.finite_rings
            sage: p = 7549; A = 0; B = 1; n = 157; k = 6; t = 14
            sage: F = GF(p); E = EllipticCurve(F, [A, B])
            sage: R.<x> = F[]; K.<a> = GF((p,k), modulus=x^k+2)
            sage: EK = E.base_extend(K)
            sage: P = EK(3050, 5371); Q = EK(6908*a^4, 3231*a^3)
            sage: P.ate_pairing(Q, n, k, t)
            6708*a^5 + 4230*a^4 + 4350*a^3 + 2064*a^2 + 4022*a + 6733
            sage: s = Integer(randrange(1, n))
            sage: (s*P).ate_pairing(Q, n, k, t) == P.ate_pairing(s*Q, n, k, t)
            True
            sage: P.ate_pairing(s*Q, n, k, t) == P.ate_pairing(Q, n, k, t)^s
            True

        Another example with embedding degree 7 and positive trace::

            sage: # needs sage.rings.finite_rings
            sage: p = 2213; A = 1; B = 49; n = 1093; k = 7; t = 28
            sage: F = GF(p); E = EllipticCurve(F, [A, B])
            sage: R.<x> = F[]; K.<a> = GF((p,k), modulus=x^k+2)
            sage: EK = E.base_extend(K)
            sage: P = EK(1583, 1734)
            sage: Qx = 1729*a^6+1767*a^5+245*a^4+980*a^3+1592*a^2+1883*a+722
            sage: Qy = 1299*a^6+1877*a^5+1030*a^4+1513*a^3+1457*a^2+309*a+1636
            sage: Q = EK(Qx, Qy)
            sage: P.ate_pairing(Q, n, k, t)
            1665*a^6 + 1538*a^5 + 1979*a^4 + 239*a^3 + 2134*a^2 + 2151*a + 654
            sage: s = Integer(randrange(1, n))
            sage: (s*P).ate_pairing(Q, n, k, t) == P.ate_pairing(s*Q, n, k, t)
            True
            sage: P.ate_pairing(s*Q, n, k, t) == P.ate_pairing(Q, n, k, t)^s
            True

        Another example with embedding degree 7 and negative trace::

            sage: # needs sage.rings.finite_rings
            sage: p = 2017; A = 1; B = 30; n = 29; k = 7; t = -70
            sage: F = GF(p); E = EllipticCurve(F, [A, B])
            sage: R.<x> = F[]; K.<a> = GF((p,k), modulus=x^k+2)
            sage: EK = E.base_extend(K)
            sage: P = EK(369, 716)
            sage: Qx = 1226*a^6+1778*a^5+660*a^4+1791*a^3+1750*a^2+867*a+770
            sage: Qy = 1764*a^6+198*a^5+1206*a^4+406*a^3+1200*a^2+273*a+1712
            sage: Q = EK(Qx, Qy)
            sage: P.ate_pairing(Q, n, k, t)
            1794*a^6 + 1161*a^5 + 576*a^4 + 488*a^3 + 1950*a^2 + 1905*a + 1315
            sage: s = Integer(randrange(1, n))
            sage: (s*P).ate_pairing(Q, n, k, t) == P.ate_pairing(s*Q, n, k, t)
            True
            sage: P.ate_pairing(s*Q, n, k, t) == P.ate_pairing(Q, n, k, t)^s
            True

        Using the same data, we show that the ate pairing is a power of the
        Tate pairing (see [HSV2006]_ end of section 3.1)::

            sage: # needs sage.rings.finite_rings
            sage: c = (k*p^(k-1)).mod(n); T = t - 1
            sage: N = gcd(T^k - 1, p^k - 1)
            sage: s = Integer(N/n)
            sage: L = Integer((T^k - 1)/N)
            sage: M = (L*s*c.inverse_mod(n)).mod(n)
            sage: P.ate_pairing(Q, n, k, t) == Q.tate_pairing(P, n, k)^M
            True

        An example where we have to pass the base field size (and we again have
        agreement with the Tate pairing). Note that though `Px` is not
        `F`-rational, (it is the homomorphic image of an `F`-rational point) it
        is nonetheless in `ker(\\pi-1)`, and so is a legitimate input::

            sage: # needs sage.rings.finite_rings
            sage: q = 2^5; F.<a> = GF(q)
            sage: n = 41; k = 4; t = -8
            sage: E = EllipticCurve(F,[0,0,1,1,1])
            sage: P = E(a^4 + 1, a^3)
            sage: Fx.<b> = GF(q^k)
            sage: Ex = EllipticCurve(Fx, [0,0,1,1,1])
            sage: phi = Hom(F, Fx)(F.gen().minpoly().roots(Fx)[0][0])
            sage: Px = Ex(phi(P.x()), phi(P.y()))
            sage: Qx = Ex(b^19+b^18+b^16+b^12+b^10+b^9+b^8+b^5+b^3+1,
            ....:         b^18+b^13+b^10+b^8+b^5+b^4+b^3+b)
            sage: Qx = Ex(Qx[0]^q, Qx[1]^q) - Qx  # ensure Qx is in ker(pi - q)
            sage: Px.ate_pairing(Qx, n, k, t)
            Traceback (most recent call last):
            ...
            ValueError: Unexpected field degree: set keyword argument q equal to
            the size of the base field (big field is GF(q^4)).
            sage: Px.ate_pairing(Qx, n, k, t, q)
            b^19 + b^18 + b^17 + b^16 + b^15 + b^14 + b^13 + b^12
            + b^11 + b^9 + b^8 + b^5 + b^4 + b^2 + b + 1
            sage: s = Integer(randrange(1, n))
            sage: (s*Px).ate_pairing(Qx, n, k, t, q) == Px.ate_pairing(s*Qx, n, k, t, q)
            True
            sage: Px.ate_pairing(s*Qx, n, k, t, q) == Px.ate_pairing(Qx, n, k, t, q)^s
            True
            sage: c = (k*q^(k-1)).mod(n); T = t - 1
            sage: N = gcd(T^k - 1, q^k - 1)
            sage: s = Integer(N/n)
            sage: L = Integer((T^k - 1)/N)
            sage: M = (L*s*c.inverse_mod(n)).mod(n)
            sage: Px.ate_pairing(Qx, n, k, t, q) == Qx.tate_pairing(Px, n, k, q)^M
            True

        It is an error if `Q` is not in the kernel of `\\pi - p`, where `\\pi` is
        the Frobenius automorphism::

            sage: # needs sage.rings.finite_rings
            sage: p = 29; A = 1; B = 0; n = 5; k = 2; t = 10
            sage: F = GF(p); R.<x> = F[]
            sage: E = EllipticCurve(F, [A, B]);
            sage: K.<a> = GF((p,k), modulus=x^k+2); EK = E.base_extend(K)
            sage: P = EK(13, 8); Q = EK(13, 21)
            sage: P.ate_pairing(Q, n, k, t)
            Traceback (most recent call last):
            ...
            ValueError: Point (13 : 21 : 1) not in Ker(pi - q)

        It is also an error if `P` is not in the kernel os `\\pi - 1`::

            sage: # needs sage.rings.finite_rings
            sage: p = 29; A = 1; B = 0; n = 5; k = 2; t = 10
            sage: F = GF(p); R.<x> = F[]
            sage: E = EllipticCurve(F, [A, B]);
            sage: K.<a> = GF((p,k), modulus=x^k+2); EK = E.base_extend(K)
            sage: P = EK(14, 10*a); Q = EK(13, 21)
            sage: P.ate_pairing(Q, n, k, t)
            Traceback (most recent call last):
            ...
            ValueError: This point (14 : 10*a : 1) is not in Ker(pi - 1)

        .. NOTE::

            First defined in the paper of [HSV2006]_, the ate pairing
            can be computationally effective in those cases when the
            trace of the curve over the base field is significantly
            smaller than the expected value. This implementation is
            simply Miller\'s algorithm followed by a naive
            exponentiation, and makes no claims towards efficiency.

        AUTHORS:

        - Mariah Lenox (2011-03-08)
        '''
    def point_of_jacobian_of_curve(self):
        """
        Return the point in the Jacobian of the curve.

        The Jacobian is the one attached to the projective curve associated
        with this elliptic curve.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF((5,2))
            sage: E = EllipticCurve(k,[1,0]); E
            Elliptic Curve defined by y^2 = x^3 + x over Finite Field in a of size 5^2
            sage: E.order()
            32
            sage: P = E([a, 2*a + 4])
            sage: P
            (a : 2*a + 4 : 1)
            sage: P.order()
            8
            sage: p = P.point_of_jacobian_of_curve()
            sage: p
            [Place (x + 4*a, y + 3*a + 1)]
            sage: p.order()
            8
            sage: Q = 3*P
            sage: q = Q.point_of_jacobian_of_curve()
            sage: q == 3*p
            True
            sage: G = p.parent()
            sage: G.order()
            32
            sage: G
            Group of rational points of Jacobian over Finite Field in a of size 5^2 (Hess model)
            sage: J = G.parent(); J
            Jacobian of Projective Plane Curve over Finite Field in a of size 5^2
             defined by x^2*y + y^3 - x*z^2 (Hess model)
            sage: J.curve() == E.affine_patch(2).projective_closure()
            True
        """

class EllipticCurvePoint_number_field(EllipticCurvePoint_field):
    """
    A point on an elliptic curve over a number field.

    Most of the functionality is derived from the parent class
    :class:`EllipticCurvePoint_field`.  In addition we have support for
    orders, heights, reduction modulo primes, and elliptic logarithms.

    EXAMPLES::

        sage: E = EllipticCurve('37a')
        sage: E([0,0])
        (0 : 0 : 1)
        sage: E(0,0)               # brackets are optional
        (0 : 0 : 1)
        sage: E([GF(5)(0), 0])     # entries are coerced
        (0 : 0 : 1)

        sage: E(0.000, 0)
        (0 : 0 : 1)

        sage: E(1,0,0)
        Traceback (most recent call last):
        ...
        TypeError: Coordinates [1, 0, 0] do not define a point on
        Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field

    ::

        sage: E = EllipticCurve([0,0,1,-1,0])
        sage: S = E(QQ); S
        Abelian group of points on
        Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field

    TESTS::

        sage: loads(S.dumps()) == S
        True
        sage: P = E(0,0); P
        (0 : 0 : 1)
        sage: loads(P.dumps()) == P
        True
        sage: T = 100*P
        sage: loads(T.dumps()) == T
        True

    Test pickling an elliptic curve that has known points on it::

        sage: e = EllipticCurve([0, 0, 1, -1, 0]); g = e.gens(); loads(dumps(e)) == e
        True
    """
    def order(self):
        """
        Return the order of this point on the elliptic curve.

        If the point has infinite order, returns +Infinity.  For
        curves defined over `\\QQ`, we call PARI; over other
        number fields we implement the function here.

        .. NOTE::

            :meth:`additive_order` is a synonym for :meth:`order`

        EXAMPLES::

            sage: E = EllipticCurve([0,0,1,-1,0])
            sage: P = E([0,0]); P
            (0 : 0 : 1)
            sage: P.order()
            +Infinity

        ::

            sage: E = EllipticCurve([0,1])
            sage: P = E([-1,0])
            sage: P.order()
            2
            sage: P.additive_order()
            2
        """
    additive_order = order
    def has_finite_order(self) -> bool:
        """
        Return ``True`` iff this point has finite order on the elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([0,0,1,-1,0])
            sage: P = E([0,0]); P
            (0 : 0 : 1)
            sage: P.has_finite_order()
            False

        ::

            sage: E = EllipticCurve([0,1])
            sage: P = E([-1,0])
            sage: P.has_finite_order()
            True
        """
    def has_infinite_order(self) -> bool:
        """
        Return ``True`` iff this point has infinite order on the elliptic curve.

        EXAMPLES::

            sage: E = EllipticCurve([0,0,1,-1,0])
            sage: P = E([0,0]); P
            (0 : 0 : 1)
            sage: P.has_infinite_order()
            True

        ::

            sage: E = EllipticCurve([0,1])
            sage: P = E([-1,0])
            sage: P.has_infinite_order()
            False
        """
    def is_on_identity_component(self, embedding=None):
        """
        Return ``True`` iff this point is on the identity component of
        its curve with respect to a given (real or complex) embedding.

        INPUT:

        - ``self`` -- a point on a curve over any ordered field (e.g. `\\QQ`)

        - ``embedding`` -- an embedding from the base_field of the
          point's curve into `\\RR` or `\\CC`; if ``None`` (the
          default) it uses the first embedding of the base_field into
          `\\RR` if any, else the first embedding into `\\CC`.

        OUTPUT:

        boolean; ``True`` iff the point is on the identity component of
        the curve.  (If the point is zero then the result is ``True``.)

        EXAMPLES:

        For `K=\\QQ` there is no need to specify an embedding::

            sage: E = EllipticCurve('5077a1')
            sage: [E.lift_x(x).is_on_identity_component() for x in srange(-3,5)]
            [False, False, False, False, False, True, True, True]

        An example over a field with two real embeddings::

            sage: # needs sage.rings.number_field
            sage: L.<a> = QuadraticField(2)
            sage: E = EllipticCurve(L, [0,1,0,a,a])
            sage: P = E(-1,0)
            sage: [P.is_on_identity_component(e) for e in L.embeddings(RR)]
            [False, True]

        We can check this as follows::

            sage: # needs sage.rings.number_field
            sage: [e(E.discriminant()) > 0 for e in L.embeddings(RR)]
            [True, False]
            sage: e = L.embeddings(RR)[0]
            sage: E1 = EllipticCurve(RR, [e(ai) for ai in E.ainvs()])
            sage: e1, e2, e3 = E1.two_division_polynomial().roots(RR,
            ....:                                                 multiplicities=False)
            sage: e1 < e2 < e3 and e(P[0]) < e3
            True
        """
    def has_good_reduction(self, P=None) -> bool:
        """
        Return ``True`` iff this point has good reduction modulo a prime.

        INPUT:

        - ``P`` -- a prime of the base_field of the point's curve, or
          ``None`` (default)

        OUTPUT:

        boolean; if a prime `P` of the base field is specified, returns
        ``True`` iff the point has good reduction at `P`; otherwise,
        return ``True`` if the point has god reduction at all primes in
        the support of the discriminant of this model.

        EXAMPLES::

            sage: E = EllipticCurve('990e1')
            sage: P = E.gen(0); P
            (15 : 51 : 1)
            sage: [E.has_good_reduction(p) for p in [2,3,5,7]]
            [False, False, False, True]
            sage: [P.has_good_reduction(p) for p in [2,3,5,7]]
            [True, False, True, True]
            sage: [E.tamagawa_exponent(p) for p in [2,3,5,7]]
            [2, 2, 1, 1]
            sage: [(2*P).has_good_reduction(p) for p in [2,3,5,7]]
            [True, True, True, True]
            sage: P.has_good_reduction()
            False
            sage: (2*P).has_good_reduction()
            True
            sage: (3*P).has_good_reduction()
            False

        ::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: E = EllipticCurve(K, [0,1,0,-160,308])
            sage: P = E(26, -120)
            sage: E.discriminant().support()
            [Fractional ideal (i - 1),
             Fractional ideal (2*i - 1),
             Fractional ideal (-2*i - 1),
             Fractional ideal (3)]
            sage: [E.tamagawa_exponent(p) for p in E.discriminant().support()]
            [1, 4, 4, 4]
            sage: P.has_good_reduction()
            False
            sage: (2*P).has_good_reduction()
            False
            sage: (4*P).has_good_reduction()
            True

        TESTS:

        An example showing that :issue:`8498` is fixed::

            sage: E = EllipticCurve('11a1')
            sage: K.<t> = NumberField(x^2 + 47)                                         # needs sage.rings.number_field
            sage: EK = E.base_extend(K)                                                 # needs sage.rings.number_field
            sage: T = EK(5, 5)                                                          # needs sage.rings.number_field
            sage: P = EK(-2, -1/2*t - 1/2)                                              # needs sage.rings.number_field
            sage: p = K.ideal(11)                                                       # needs sage.rings.number_field
            sage: T.has_good_reduction(p)                                               # needs sage.rings.number_field
            False
            sage: P.has_good_reduction(p)                                               # needs sage.rings.number_field
            True
        """
    def reduction(self, p):
        """
        This finds the reduction of a point `P` on the elliptic curve
        modulo the prime `p`.

        INPUT:

        - ``self`` -- a point on an elliptic curve

        - ``p`` -- a prime number

        OUTPUT: the point reduced to be a point on the elliptic curve modulo `p`

        EXAMPLES::

            sage: E = EllipticCurve([1,2,3,4,0])
            sage: P = E(0,0)
            sage: P.reduction(5)
            (0 : 0 : 1)
            sage: Q = E(98,931)
            sage: Q.reduction(5)
            (3 : 1 : 1)
            sage: Q.reduction(5).curve() == E.reduction(5)
            True

        ::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: F.<a> = NumberField(x^2 + 5)
            sage: E = EllipticCurve(F, [1,2,3,4,0])
            sage: Q = E(98, 931)
            sage: Q.reduction(a)
            (3 : 1 : 1)
            sage: Q.reduction(11)
            (10 : 7 : 1)

        ::

            sage: # needs sage.rings.number_field
            sage: F.<a> = NumberField(x^3 + x^2 + 1)
            sage: E = EllipticCurve(F, [a,2])
            sage: P = E(a, 1)
            sage: P.reduction(F.ideal(5))
            (abar : 1 : 1)
            sage: P.reduction(F.ideal(a^2 - 4*a - 2))
            (abar : 1 : 1)
        """
    def height(self, precision=None, normalised: bool = True, algorithm: str = 'pari'):
        """Return the Néron-Tate canonical height of the point.

        INPUT:

        - ``self`` -- a point on an elliptic curve over a number field `K`

        - ``precision`` -- positive integer, or ``None`` (default). The
          precision in bits of the result. If ``None``, the default real
          precision is used.

        - ``normalised`` -- boolean. If ``True`` (default), the height is
          normalised to be invariant under extension of `K`. If ``False``,
          return this normalised height multiplied by the degree of `K`.

        - ``algorithm`` -- string; either ``'pari'`` (default) or ``'sage'``.
          If ``'pari'`` and the base field is `\\QQ`, use the PARI library
          function; otherwise use the Sage implementation.

        OUTPUT:

        The rational number 0, or a nonnegative real number.

        There are two normalisations used in the literature, one of
        which is double the other. We use the larger of the two, which
        is the one appropriate for the BSD conjecture. This is
        consistent with [Cre1997]_ and double that of [Sil2009]_.

        See :wikipedia:`Néron-Tate height`.

        .. NOTE::

            The correct height to use for the regulator in the BSD
            formula is the non-normalised height.

        EXAMPLES::

            sage: E = EllipticCurve('11a'); E
            Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
            sage: P = E([5,5]); P
            (5 : 5 : 1)
            sage: P.height()
            0
            sage: Q = 5*P
            sage: Q.height()
            0

        ::

            sage: E = EllipticCurve('37a'); E
            Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
            sage: P = E([0,0])
            sage: P.height()
            0.0511114082399688
            sage: P.order()
            +Infinity
            sage: E.regulator()
            0.0511114082399688...

            sage: def naive_height(P):
            ....:     return log(RR(max(abs(P[0].numerator()), abs(P[0].denominator()))))
            sage: for n in [1..10]:
            ....:     print(naive_height(2^n*P)/4^n)
            0.000000000000000
            0.0433216987849966
            0.0502949347635656
            0.0511006335618645
            0.0511007834799612
            0.0511013666152466
            0.0511034199907743
            0.0511106492906471
            0.0511114081541082
            0.0511114081541180

        ::

            sage: E = EllipticCurve('4602a1'); E
            Elliptic Curve defined by y^2 + x*y  = x^3 + x^2 - 37746035*x - 89296920339
            over Rational Field
            sage: x = 77985922458974949246858229195945103471590
            sage: y = 19575260230015313702261379022151675961965157108920263594545223
            sage: d = 2254020761884782243
            sage: E([ x / d^2,  y / d^3 ]).height()
            86.7406561381275

        ::

            sage: E = EllipticCurve([17, -60, -120, 0, 0]); E
            Elliptic Curve defined by y^2 + 17*x*y - 120*y = x^3 - 60*x^2 over Rational Field
            sage: E([30, -90]).height()
            0

            sage: E = EllipticCurve('389a1'); E
            Elliptic Curve defined by y^2 + y = x^3 + x^2 - 2*x over Rational Field
            sage: P, Q = E(-1,1), E(0,-1)
            sage: P.height(precision=100)
            0.68666708330558658572355210295
            sage: (3*Q).height(precision=100)/Q.height(precision=100)
            9.0000000000000000000000000000
            sage: _.parent()
            Real Field with 100 bits of precision

        Canonical heights over number fields are implemented as well::

            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(x^3 - 2)                                          # needs sage.rings.number_field
            sage: E = EllipticCurve([a, 4]); E                                          # needs sage.rings.number_field
            Elliptic Curve defined by y^2 = x^3 + a*x + 4
             over Number Field in a with defining polynomial x^3 - 2
            sage: P = E((0,2))                                                          # needs sage.rings.number_field
            sage: P.height()                                                            # needs sage.rings.number_field
            0.810463096585925
            sage: P.height(precision=100)                                               # needs sage.rings.number_field
            0.81046309658592536863991810577
            sage: P.height(precision=200)                                               # needs sage.rings.number_field
            0.81046309658592536863991810576865158896130286417155832378086
            sage: (2*P).height() / P.height()                                           # needs sage.rings.number_field
            4.00000000000000
            sage: (100*P).height() / P.height()                                         # needs sage.rings.number_field
            10000.0000000000

        Setting ``normalised=False`` multiplies the height by the degree of `K`::

            sage: E = EllipticCurve('37a')
            sage: P = E([0,0])
            sage: P.height()
            0.0511114082399688
            sage: P.height(normalised=False)
            0.0511114082399688
            sage: K.<z> = CyclotomicField(5)                                            # needs sage.rings.number_field
            sage: EK = E.change_ring(K)                                                 # needs sage.rings.number_field
            sage: PK = EK([0,0])                                                        # needs sage.rings.number_field
            sage: PK.height()                                                           # needs sage.rings.number_field
            0.0511114082399688
            sage: PK.height(normalised=False)                                           # needs sage.rings.number_field
            0.204445632959875

        Some consistency checks::

            sage: E = EllipticCurve('5077a1')
            sage: P = E([-2,3,1])
            sage: P.height()
            1.36857250535393

            sage: EK = E.change_ring(QuadraticField(-3,'a'))                            # needs sage.rings.number_field
            sage: PK = EK([-2,3,1])                                                     # needs sage.rings.number_field
            sage: PK.height()                                                           # needs sage.rings.number_field
            1.36857250535393

            sage: # needs sage.rings.number_field
            sage: K.<i> = NumberField(x^2 + 1)
            sage: E = EllipticCurve(K, [0,0,4,6*i,0])
            sage: Q = E.lift_x(-9/4); Q
            (-9/4 : 27/8*i - 4 : 1)
            sage: Q.height()
            2.69518560017909
            sage: (15*Q).height() / Q.height()
            225.000000000000

            sage: E = EllipticCurve('37a')
            sage: P = E([0,-1])
            sage: P.height()
            0.0511114082399688
            sage: K.<a> = QuadraticField(-7)                                            # needs sage.rings.number_field
            sage: ED = E.quadratic_twist(-7)                                            # needs sage.rings.number_field
            sage: Q = E.isomorphism_to(ED.change_ring(K))(P); Q                         # needs sage.rings.number_field
            (0 : -7/2*a - 1/2 : 1)
            sage: Q.height()                                                            # needs sage.rings.number_field
            0.0511114082399688
            sage: Q.height(precision=100)                                               # needs sage.rings.number_field
            0.051111408239968840235886099757

        An example to show that the bug at :issue:`5252` is fixed::

            sage: E = EllipticCurve([1, -1, 1, -2063758701246626370773726978, 32838647793306133075103747085833809114881])
            sage: P = E([-30987785091199, 258909576181697016447])
            sage: P.height()
            25.8603170675462
            sage: P.height(precision=100)
            25.860317067546190743868840741
            sage: P.height(precision=250)
            25.860317067546190743868840740735110323098872903844416215577171041783572513
            sage: P.height(precision=500)
            25.8603170675461907438688407407351103230988729038444162155771710417835725129551130570889813281792157278507639909972112856019190236125362914195452321720

            sage: P.height(precision=100) == P.non_archimedean_local_height(prec=100)+P.archimedean_local_height(prec=100)
            True

        An example to show that the bug at :issue:`8319` is fixed (correct height when the curve is not minimal)::

            sage: E = EllipticCurve([-5580472329446114952805505804593498080000,-157339733785368110382973689903536054787700497223306368000000])
            sage: xP = 204885147732879546487576840131729064308289385547094673627174585676211859152978311600/23625501907057948132262217188983681204856907657753178415430361
            sage: P = E.lift_x(xP)
            sage: P.height()
            157.432598516754
            sage: Q = 2*P
            sage: Q.height() # long time (4s)
            629.730394067016
            sage: Q.height()-4*P.height() # long time
            0.000000000000000

        An example to show that the bug at :issue:`12509` is fixed (precision issues)::

            sage: # needs sage.rings.number_field
            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^2 - x - 1)
            sage: v = [0, a + 1, 1, 28665*a - 46382, 2797026*a - 4525688]
            sage: E = EllipticCurve(v)
            sage: P = E([72*a - 509/5,  -682/25*a - 434/25])
            sage: P.height()
            1.38877711688727
            sage: (2*P).height()/P.height()
            4.00000000000000
            sage: (2*P).height(precision=100)/P.height(precision=100)
            4.0000000000000000000000000000
            sage: (2*P).height(precision=1000)/P.height(precision=1000)
            4.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

        This shows that the bug reported at :issue:`13951` has been fixed::

            sage: E = EllipticCurve([0,17])
            sage: P1 = E(2,5)
            sage: P1.height()
            1.06248137652528
            sage: F = E.change_ring(QuadraticField(-3, 'a'))                            # needs sage.rings.number_field
            sage: P2 = F([2,5])                                                         # needs sage.rings.number_field
            sage: P2.height()                                                           # needs sage.rings.number_field
            1.06248137652528

        This shows that the bug reported at :issue:`36834` (incorrect
        value when the model is not integral) has been fixed::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(x^2 - 84131656042917)
            sage: E = EllipticCurve(K, [0, 0, 0, -5482707841/48, -244634179112639/864])
            sage: P = E(349189/12, 1/2*a)
            sage: P.height()
            10.4560438181991
            sage: [(n*P).height()/P.height() for n in [2,3,4,5]]
            [4.00000000000000, 9.00000000000000, 16.0000000000000, 25.0000000000000]

        """
    def archimedean_local_height(self, v=None, prec=None, weighted: bool = False):
        """
        Compute the local height of ``self`` at the archimedean place `v`.

        INPUT:

        - ``self`` -- a point on an elliptic curve over a number field `K`

        - ``v`` -- a real or complex embedding of K, or None (default).
          If `v` is a real or complex embedding, return the local
          height of ``self`` at `v`. If `v` is None, return the total
          archimedean contribution to the global height.

        - ``prec`` -- integer or ``None`` (default). The precision of the
          computation. If ``None``, the precision is deduced from `v`

        - ``weighted`` -- boolean. If ``False`` (default), the height is
          normalised to be invariant under extension of `K`. If ``True``,
          return this normalised height multiplied by the local degree
          if `v` is a single place, or by the degree of `K` if `v` is ``None``.

        OUTPUT:

        A real number. The normalisation is twice that in Silverman's
        paper [Sil1988]_. Note that this local height depends on the
        model of the curve.

        ALGORITHM:

        See [Sil1988]_, Section 4.

        EXAMPLES:

        Examples 1, 2, and 3 from [Sil1988]_::

            sage: # needs sage.rings.number_field
            sage: K.<a> = QuadraticField(-2)
            sage: E = EllipticCurve(K, [0,-1,1,0,0]); E
            Elliptic Curve defined by y^2 + y = x^3 + (-1)*x^2 over Number Field
             in a with defining polynomial x^2 + 2 with a = 1.414213562373095?*I
            sage: P = E.lift_x(2 + a); P
            (a + 2 : -2*a - 2 : 1)
            sage: P.archimedean_local_height(K.places(prec=170)[0]) / 2
            0.45754773287523276736211210741423654346576029814695

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: E = EllipticCurve(K, [0,0,4,6*i,0]); E
            Elliptic Curve defined by y^2 + 4*y = x^3 + 6*i*x
             over Number Field in i with defining polynomial x^2 + 1
            sage: P = E((0,0))
            sage: P.archimedean_local_height(K.places()[0]) / 2
            0.510184995162373

            sage: Q = E.lift_x(-9/4); Q                                                 # needs sage.rings.number_field
            (-9/4 : 27/8*i - 4 : 1)
            sage: Q.archimedean_local_height(K.places()[0]) / 2                         # needs sage.rings.number_field
            0.654445619529600

        An example over the rational numbers::

            sage: E = EllipticCurve([0, 0, 0, -36, 0])
            sage: P = E([-3, 9])
            sage: P.archimedean_local_height()
            1.98723816350773

        Local heights of torsion points can be nonzero (unlike the
        global height)::

            sage: # needs sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: E = EllipticCurve([0, 0, 0, K(1), 0])
            sage: P = E(i, 0)
            sage: P.archimedean_local_height()
            0.346573590279973

        TESTS:

        See :issue:`12509`::

            sage: # needs sage.rings.number_field
            sage: x = polygen(QQ)
            sage: K.<a> = NumberField(x^2 - x - 1)
            sage: v = [0, a + 1, 1, 28665*a - 46382, 2797026*a - 4525688]
            sage: E = EllipticCurve(v)
            sage: P = E([72*a - 509/5,  -682/25*a - 434/25])
            sage: P.archimedean_local_height()
            -0.220660795546828

        See :issue:`19276`::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(x^2 - x - 104)
            sage: E = EllipticCurve([1, a - 1, 1, -816765673272*a - 7931030674178, 1478955604013312315*a + 14361086227143654561])
            sage: P = E(5393511/49*a + 52372721/49 , -33896210324/343*a - 329141996591/343 )
            sage: P.height()
            0.974232017827741

        See :issue:`29966`::

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(x^3 - x^2 - 6*x + 2)
            sage: E = EllipticCurve([1, -a^2 + 2*a + 4, 0, -6056450500590472699700624*a^2 - 11239394326797569935861742*a + 4241549693833829432516231,
            ....:                    1904879037869682826729875958079326124520*a^2 + 3535022146945771697732350459284777382011*a - 1334055169621036218710397707677347972626])
            sage: P = E([1033399668533*a^2 + 1917754693229*a - 723726883800 , 12536493059202326563*a^2 + 23264879148900575548*a - 8779756111574815918 , 1])
            sage: P.height()
            0.297318833424763
            sage: (2*P).height() / P.height()
            4.00000000000000
            sage: P.height(200)
            0.29731883342476341806143743594519935578696537745294661858984
            sage: (2*P).height(200) / P.height(200)
            4.0000000000000000000000000000000000000000000000000000000000
        """
    def non_archimedean_local_height(self, v=None, prec=None, weighted: bool = False, is_minimal=None):
        """
        Compute the local height of ``self`` at non-archimedean places.

        INPUT:

        - ``self`` -- a point on an elliptic curve over a number field `K`

        - ``v`` -- a non-archimedean place of `K`, or ``None`` (default).
          If `v` is a non-archimedean place, return the local height
          of ``self`` at `v`. If `v` is ``None``, return the total
          non-archimedean contribution to the global height.

        - ``prec`` -- integer; or ``None`` (default). The precision of the
          computation. If ``None``, the height is returned symbolically

        - ``weighted`` -- boolean. If ``False`` (default), the height is
          normalised to be invariant under extension of `K`. If ``True``,
          return this normalised height multiplied by the local degree
          if `v` is a single place, or by the degree of `K` if `v` is ``None``.

        - ``is_minimal`` -- boolean, or ``None`` (default). Ignored
          when ``v`` is ``None`` (default) or ``True``.  Otherwise,
          when the place ``v`` is specified: if ``True``, the model is
          assumed to be both locally integral and a local minimal
          model; if ``None`` (default) or ``False``, a local minimal
          model is computed and the computation is done on that model.

        OUTPUT:

        A real number. The normalisation is twice that in Silverman's
        paper [Sil1988]_. Note that this local height depends on the
        model of the curve.

        ALGORITHM:

        See [Sil1988]_, Section 5.

        EXAMPLES:

        Examples 2 and 3 from [Sil1988]_::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<i> = NumberField(x^2 + 1)
            sage: E = EllipticCurve(K, [0,0,4,6*i,0]); E
            Elliptic Curve defined by y^2 + 4*y = x^3 + 6*i*x
             over Number Field in i with defining polynomial x^2 + 1
            sage: P = E((0,0))
            sage: P.non_archimedean_local_height(K.ideal(i+1))
            -1/2*log(2)
            sage: P.non_archimedean_local_height(K.ideal(3))
            0
            sage: P.non_archimedean_local_height(K.ideal(1-2*i))
            0

            sage: # needs sage.rings.number_field
            sage: Q = E.lift_x(-9/4); Q
            (-9/4 : 27/8*i - 4 : 1)
            sage: Q.non_archimedean_local_height(K.ideal(1+i))
            2*log(2)
            sage: Q.non_archimedean_local_height(K.ideal(3))
            0
            sage: Q.non_archimedean_local_height(K.ideal(1-2*i))
            0
            sage: Q.non_archimedean_local_height()
            2*log(2)

        An example over the rational numbers::

            sage: E = EllipticCurve([0, 0, 0, -36, 0])
            sage: P = E([-3, 9])
            sage: P.non_archimedean_local_height()
            -log(3)

        Local heights of torsion points can be nonzero (unlike the
        global height)::

            sage: # needs sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: E = EllipticCurve([0, 0, 0, K(1), 0])
            sage: P = E(i, 0)
            sage: P.non_archimedean_local_height()
            -1/2*log(2)

        TESTS::

            sage: Q.non_archimedean_local_height(prec=100)                              # needs sage.rings.number_field
            1.3862943611198906188344642429
            sage: (3*Q).non_archimedean_local_height()                                  # needs sage.rings.number_field
            1/2*log(75923153929839865104)

            sage: # needs sage.rings.number_field
            sage: F.<a> = NumberField(x^4 + 2*x^3 + 19*x^2 + 18*x + 288)
            sage: F.ring_of_integers().basis()
            [1, 5/6*a^3 + 1/6*a, 1/6*a^3 + 1/6*a^2, a^3]
            sage: F.class_number()
            12
            sage: E = EllipticCurve('37a').change_ring(F)
            sage: P = E((-a^2/6 - a/6 - 1, a)); P
            (-1/6*a^2 - 1/6*a - 1 : a : 1)
            sage: P[0].is_integral()
            True
            sage: P.non_archimedean_local_height()
            0

        This shows that the bug reported at :issue:`13951` has been fixed::

            sage: E = EllipticCurve([0,17])
            sage: P = E(2,5)
            sage: P.non_archimedean_local_height(2)
            -2/3*log(2)

        This shows that the bug reported at :issue:`36834` (incorrect
        value when the model is not integral) has been fixed::

            sage: # needs sage.rings.number_field
            sage: K.<a> = QuadraticField(84131656042917)
            sage: E = EllipticCurve(K, [0, 0, 0, -5482707841/48, -244634179112639/864])
            sage: P = E(349189/12, 1/2*a)
            sage: h = P.non_archimedean_local_height()
            sage: h
            1/2*log(144) - log(3) - 2*log(2)
            sage: h.numerator().simplify_log()
            0

        """
    def elliptic_logarithm(self, embedding=None, precision: int = 100, algorithm: str = 'pari'):
        '''
        Return the elliptic logarithm of this elliptic curve point.

        An embedding of the base field into `\\RR` or `\\CC` (with
        arbitrary precision) may be given; otherwise the first real
        embedding is used (with the specified precision) if any, else
        the first complex embedding.

        INPUT:

        - ``embedding`` -- an embedding of the base field into `\\RR` or `\\CC`

        - ``precision`` -- a positive integer (default: 100) setting the
          number of bits of precision for the computation

        - ``algorithm`` -- either ``\'pari\'`` (default: for real embeddings)
          to use PARI\'s :pari:`ellpointtoz`, or ``\'sage\'`` for a native
          implementation.  Ignored for complex embeddings.

        ALGORITHM:

        See [Coh1993]_ for the case of real embeddings,
        and Cremona, J.E. and Thongjunthug, T. 2010 for the complex
        case.

        AUTHORS:

        - Michael Mardaus (2008-07),
        - Tobias Nagel (2008-07) -- original version from [Coh1993]_.
        - John Cremona (2008-07) -- revision following eclib code.
        - John Cremona (2010-03) -- implementation for complex embeddings.

        EXAMPLES::

            sage: E = EllipticCurve(\'389a\')
            sage: E.discriminant() > 0
            True
            sage: P = E([-1,1])
            sage: P.is_on_identity_component ()
            False
            sage: P.elliptic_logarithm (precision=96)
            0.4793482501902193161295330101 + 0.985868850775824102211203849...*I
            sage: Q = E([3,5])
            sage: Q.is_on_identity_component()
            True
            sage: Q.elliptic_logarithm (precision=96)
            1.931128271542559442488585220

        An example with negative discriminant, and a torsion point::

            sage: E = EllipticCurve(\'11a1\')
            sage: E.discriminant() < 0
            True
            sage: P = E([16,-61])
            sage: P.elliptic_logarithm(precision=70)
            0.25384186085591068434
            sage: E.period_lattice().real_period(prec=70) / P.elliptic_logarithm(precision=70)
            5.0000000000000000000

        A larger example.  The default algorithm uses PARI and makes
        sure the result has the requested precision::

            sage: E = EllipticCurve([1, 0, 1, -85357462, 303528987048]) #18074g1
            sage: P = E([4458713781401/835903744, -64466909836503771/24167649046528, 1])
            sage: P.elliptic_logarithm()  # 100 bits
            0.27656204014107061464076203097

        The native algorithm ``\'sage\'`` used to have trouble with
        precision in this example, but no longer::

            sage: P.elliptic_logarithm(algorithm=\'sage\')  # 100 bits
            0.27656204014107061464076203097

        This shows that the bug reported at :issue:`4901` has been fixed::

            sage: E = EllipticCurve("4390c2")
            sage: P = E(683762969925/44944,-565388972095220019/9528128)
            sage: P.elliptic_logarithm()
            0.00025638725886520225353198932529
            sage: P.elliptic_logarithm(precision=64)
            0.000256387258865202254
            sage: P.elliptic_logarithm(precision=65)
            0.0002563872588652022535
            sage: P.elliptic_logarithm(precision=128)
            0.00025638725886520225353198932528666427412
            sage: P.elliptic_logarithm(precision=129)
            0.00025638725886520225353198932528666427412
            sage: P.elliptic_logarithm(precision=256)
            0.0002563872588652022535319893252866642741168388008346370015005142128009610936373
            sage: P.elliptic_logarithm(precision=257)
            0.00025638725886520225353198932528666427411683880083463700150051421280096109363730

        Examples over number fields::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, \'x\')
            sage: K.<a> = NumberField(x^3 - 2)
            sage: embs = K.embeddings(CC)
            sage: E = EllipticCurve([0,1,0,a,a])
            sage: Ls = [E.period_lattice(e) for e in embs]
            sage: [L.real_flag for L in Ls]
            [0, 0, -1]
            sage: P = E(-1,0)  # order 2
            sage: [L.elliptic_logarithm(P) for L in Ls]
            [-1.73964256006716 - 1.07861534489191*I,
             -0.363756518406398 - 1.50699412135253*I, 1.90726488608927]

            sage: # needs sage.rings.number_field
            sage: E = EllipticCurve([-a^2 - a - 1, a^2 + a])
            sage: Ls = [E.period_lattice(e) for e in embs]
            sage: pts = [E(2*a^2 - a - 1 , -2*a^2 - 2*a + 6 ),
            ....:        E(-2/3*a^2 - 1/3 , -4/3*a - 2/3 ),
            ....:        E(5/4*a^2 - 1/2*a , -a^2 - 1/4*a + 9/4 ),
            ....:        E(2*a^2 + 3*a + 4 , -7*a^2 - 10*a - 12 )]
            sage: [[L.elliptic_logarithm(P) for P in pts] for L in Ls]
            [[0.250819591818930 - 0.411963479992219*I, -0.290994550611374 - 1.37239400324105*I,
              -0.693473752205595 - 2.45028458830342*I, -0.151659609775291 - 1.48985406505459*I],
             [1.33444787667954 - 1.50889756650544*I, 0.792633734249234 - 0.548467043256610*I,
              0.390154532655013 + 0.529423541805758*I, 0.931968675085317 - 0.431006981443071*I],
             [1.14758249500109 + 0.853389664016075*I, 2.59823462472518 + 0.853389664016075*I,
              1.75372176444709, 0.303069634723001]]

        ::

            sage: # needs sage.rings.number_field
            sage: K.<i> = QuadraticField(-1)
            sage: E = EllipticCurve([0,0,0,9*i-10,21-i])
            sage: emb = K.embeddings(CC)[1]
            sage: L = E.period_lattice(emb)
            sage: P = E(2-i, 4+2*i)
            sage: L.elliptic_logarithm(P, prec=100)
            0.70448375537782208460499649302 - 0.79246725643650979858266018068*I
        '''
    def padic_elliptic_logarithm(self, p, absprec: int = 20):
        """
        Compute the `p`-adic elliptic logarithm of this point.

        INPUT:

        - ``p`` -- integer; a prime

        - ``absprec`` -- integer (default: 20); the initial `p`-adic absolute
          precision of the computation

        OUTPUT:

        The `p`-adic elliptic logarithm of self, with precision ``absprec``.

        AUTHORS:

        - Tobias Nagel
        - Michael Mardaus
        - John Cremona

        ALGORITHM:

        For points in the formal group (i.e. not integral at `p`) we
        take the ``log()`` function from the formal groups module and
        evaluate it at `-x/y`.  Otherwise we first multiply the point
        to get into the formal group, and divide the result
        afterwards.

        .. TODO::

            See comments at :issue:`4805`.  Currently the absolute
            precision of the result may be less than the given value
            of absprec, and error-handling is imperfect.

        EXAMPLES::

            sage: E = EllipticCurve([0,1,1,-2,0])
            sage: E(0).padic_elliptic_logarithm(3)                                      # needs sage.rings.padics
            0
            sage: P = E(0, 0)                                                           # needs sage.rings.padics
            sage: P.padic_elliptic_logarithm(3)                                         # needs sage.rings.padics
            2 + 2*3 + 3^3 + 2*3^7 + 3^8 + 3^9 + 3^11 + 3^15 + 2*3^17 + 3^18 + O(3^19)
            sage: P.padic_elliptic_logarithm(3).lift()                                  # needs sage.rings.padics
            660257522
            sage: P = E(-11/9, 28/27)                                                   # needs sage.rings.padics
            sage: [(2*P).padic_elliptic_logarithm(p)/P.padic_elliptic_logarithm(p) for p in prime_range(20)]  # long time, needs sage.rings.padics
            [2 + O(2^19), 2 + O(3^20), 2 + O(5^19), 2 + O(7^19), 2 + O(11^19), 2 + O(13^19), 2 + O(17^19), 2 + O(19^19)]
            sage: [(3*P).padic_elliptic_logarithm(p)/P.padic_elliptic_logarithm(p) for p in prime_range(12)]  # long time, needs sage.rings.padics
            [1 + 2 + O(2^19), 3 + 3^20 + O(3^21), 3 + O(5^19), 3 + O(7^19), 3 + O(11^19)]
            sage: [(5*P).padic_elliptic_logarithm(p)/P.padic_elliptic_logarithm(p) for p in prime_range(12)]  # long time, needs sage.rings.padics
            [1 + 2^2 + O(2^19), 2 + 3 + O(3^20), 5 + O(5^19), 5 + O(7^19), 5 + O(11^19)]

        An example which arose during reviewing :issue:`4741`::

            sage: E = EllipticCurve('794a1')
            sage: P = E(-1,2)
            sage: P.padic_elliptic_logarithm(2)  # default precision=20                 # needs sage.rings.padics
            2^4 + 2^5 + 2^6 + 2^8 + 2^9 + 2^13 + 2^14 + 2^15 + O(2^16)
            sage: P.padic_elliptic_logarithm(2, absprec=30)                             # needs sage.rings.padics
            2^4 + 2^5 + 2^6 + 2^8 + 2^9 + 2^13 + 2^14 + 2^15 + 2^22 + 2^23 + 2^24 + O(2^26)
            sage: P.padic_elliptic_logarithm(2, absprec=40)                             # needs sage.rings.padics
            2^4 + 2^5 + 2^6 + 2^8 + 2^9 + 2^13 + 2^14 + 2^15 + 2^22 + 2^23 + 2^24
            + 2^28 + 2^29 + 2^31 + 2^34 + O(2^35)
        """

class EllipticCurvePoint_finite_field(EllipticCurvePoint_field):
    """
    Class for elliptic curve points over finite fields.
    """
    def log(self, base):
        """
        Return the discrete logarithm of this point to the given ``base``.
        In other words, return an integer `x` such that `xP = Q` where
        `P` is ``base`` and `Q` is this point.

        If ``base`` is a list or tuple of two points, then this function
        solves a two-dimensional discrete logarithm: Given `(P_1,P_2)` in
        ``base``, it returns a tuple of integers `(x,y)` such that
        `[x]P_1 + [y]P_2 = Q`, where `Q` is this point.

        A :exc:`ValueError` is raised if there is no solution.

        ALGORITHM:

        To compute the actual logarithm, :pari:`elllog` is called.

        However, ``elllog()`` does not guarantee termination if `Q`
        is not a multiple of `P`, so we first need to check subgroup
        membership. This is done as follows:

        - Let `n` denote the order of `P`. First check that `nQ` equals
          the point at infinity (and hence the order of `Q` divides `n`).

        - If the curve order `\\#E` has been cached, check whether
          `\\gcd(n^2, \\#E) = n`. If this holds, the curve has cyclic
          `n`-torsion, hence all points whose order divides `n` must be
          multiples of `P` and we are done.

        - Otherwise (if this test is inconclusive), check that the Weil
          pairing of `P` and `Q` is trivial.

        For anomalous curves with `\\#E = p`, the
        :meth:`padic_elliptic_logarithm` function is called.

        For two-dimensional logarithms, we first compute the Weil pairings
        of `Q` with `P_1` and `P_2` and their logarithms relative to the
        pairing of `P_1` and `P_2`; this allows reading off `x` and `y`
        modulo the part of the order where `P_1` and `P_2` are independent.
        Modulo the remaining part of the order the logarithm ends up being
        effectively one-dimensional, so we can reduce the problem to the
        basic one-dimensional case and finally recombine the results.

        INPUT:

        - ``base`` -- another point or sequence of two points on the same
          curve as ``self``

        OUTPUT:

        (integer) -- The discrete logarithm of `Q` with respect to `P`,
        which is an integer `x` with `0\\le x<\\mathrm{ord}(P)` such that
        `xP=Q`, if one exists. In the case of two points `P_1,P_2`, two
        integers `x,y` with `0\\le x<\\mathrm{ord}(P_1)` and
        `0\\le y<\\mathrm{ord}(P_2)` such that `[x]P_1 + [y]P_2 = Q`.

        AUTHORS:

        - John Cremona. Adapted to use generic functions 2008-04-05.
        - Lorenz Panny (2022): switch to PARI.
        - Lorenz Panny (2024): the two-dimensional case.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF((3,6),'a')
            sage: a = F.gen()
            sage: E = EllipticCurve([0,1,1,a,a])
            sage: E.cardinality()
            762
            sage: P = E.gens()[0]
            sage: Q = 400*P
            sage: Q.log(P)
            400

        ::

            sage: # needs sage.rings.finite_rings
            sage: F = GF((5, 60), 'a')
            sage: E = EllipticCurve(F, [1, 1])
            sage: E.abelian_group()
            Additive abelian group isomorphic to Z/194301464603136995341424045476456938000 + Z/4464 embedded in Abelian group of points on Elliptic Curve defined by y^2 = x^3 + x + 1 over Finite Field in a of size 5^60
            sage: P, Q = E.gens()  # cached generators from .abelian_group()
            sage: T = 1234567890987654321*P + 1337*Q
            sage: T.log([P, Q])
            (1234567890987654321, 1337)

        TESTS:

        Some random testing::

            sage: # needs sage.rings.finite_rings
            sage: sz = randint(8,32)
            sage: e = randint(1,3)
            sage: p = random_prime(ceil(2**(sz/e)))
            sage: E = EllipticCurve(j=GF((p,e),'a').random_element())
            sage: P = E.random_point()
            sage: Q = randrange(2**999) * P
            sage: x = Q.log(P)
            sage: x*P == Q
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: sz = randint(16,24)
            sage: e = randint(1,6)
            sage: p = random_prime(ceil(2**(sz/e)))
            sage: E = EllipticCurve(j=GF((p,e),'a').random_element())
            sage: E = choice(E.twists())
            sage: P = E.random_point()
            sage: Q = E.random_point()
            sage: T = randrange(2^99) * P + randrange(2^99) * Q
            sage: x, y = T.log([P, Q])
            sage: 0 <= x < P.order()
            True
            sage: 0 <= y < Q.order()
            True
            sage: T == x*P + y*Q
            True
        """
    def discrete_log(self, Q):
        """
        Legacy version of :meth:`log` with its arguments swapped.

        Note that this method uses the opposite argument ordering
        of all other logarithm methods in Sage; see :issue:`37150`.

        EXAMPLES::

            sage: E = EllipticCurve(j=GF(101)(5))
            sage: P, = E.gens()
            sage: (2*P).log(P)
            2
            sage: (2*P).discrete_log(P)
            doctest:warning ...
            DeprecationWarning: The syntax P.discrete_log(Q) ... Please update your code. ...
            45
            sage: P.discrete_log(2*P)
            2
        """
    def padic_elliptic_logarithm(self, Q, p):
        """
        Return the discrete logarithm of `Q` to base `P` = ``self``,
        that is, an integer `x` such that `xP = Q` only for anomalous curves.

        ALGORITHM:

        Discrete logarithm computed as in [Sma1999]_ with a loop to avoid
        the canonical lift.

        INPUT:

        - ``Q`` -- point; another point on the same curve as ``self``
        - ``p`` -- integer; a prime equal to the order of the curve

        OUTPUT:

        (integer) -- The discrete logarithm of `Q` with respect to `P`,
        which is an integer `x` with `0\\le x<\\mathrm{ord}(P)` such that
        `xP=Q`.

        AUTHORS:

        - Sylvain Pelissier (2022) based on Samuel Neves code_.

        .. _code: https://crypto.stackexchange.com/questions/70454/why-smarts-attack-doesnt-work-on-this-ecdlp/70508#70508

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: p = 235322474717419
            sage: b = 8856682
            sage: E = EllipticCurve(GF(p), [0, b])
            sage: P = E(200673830421813, 57025307876612)
            sage: Q = E(40345734829479, 211738132651297)
            sage: x = P.padic_elliptic_logarithm(Q, p)                                  # needs sage.rings.padics
            sage: x * P == Q                                                            # needs sage.rings.padics
            True

        TESTS:

        Some testing::

            sage: # needs sage.rings.finite_rings
            sage: a = 49850651047495986645822557378918223
            sage: b = 21049438014429831351540675253466229
            sage: p = 54283205379427155782089046839411711
            sage: E = EllipticCurve(GF(p), [a, b])
            sage: P = E.random_point()
            sage: Q = randrange(0, p-1) * P
            sage: x = P.padic_elliptic_logarithm(Q, p)                                  # needs sage.rings.padics
            sage: x*P == Q                                                              # needs sage.rings.padics
            True
        """
    def has_finite_order(self) -> bool:
        """
        Return ``True`` if this point has finite additive order as an element
        of the group of points on this curve.

        Since the base field is finite, the answer will always be ``True``.

        EXAMPLES::

            sage: E = EllipticCurve(GF(7), [1,3])
            sage: P = E.points()[3]
            sage: P.has_finite_order()
            True
        """
    def order(self):
        """
        Return the order of this point on the elliptic curve.

        ALGORITHM: Use PARI function :pari:`ellorder`.

        .. NOTE::

            :meth:`additive_order` is a synonym for :meth:`order`

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF((5,5))
            sage: E = EllipticCurve(k,[2,4]); E
            Elliptic Curve defined by y^2 = x^3 + 2*x + 4 over Finite Field in a of size 5^5
            sage: P = E(3*a^4 + 3*a, 2*a + 1)
            sage: P.order()
            3227
            sage: Q = E(0,2)
            sage: Q.order()
            7
            sage: Q.additive_order()
            7

        ::

            sage: # needs sage.rings.finite_rings
            sage: p = next_prime(2^150)
            sage: E = EllipticCurve(GF(p), [1,1])
            sage: P = E(831623307675610677632782670796608848711856078,
            ....:       42295786042873366706573292533588638217232964)
            sage: P.order()
            1427247692705959881058262545272474300628281448
            sage: P.order() == E.cardinality()
            True

        The next example has `j(E)=0`::

            sage: # needs sage.rings.finite_rings
            sage: p = 33554501
            sage: F.<u> = GF((p,2))
            sage: E = EllipticCurve(F, [0,1])
            sage: E.j_invariant()
            0
            sage: P = E.random_point()
            sage: P.order()  # random
            16777251

        Similarly when `j(E)=1728`::

            sage: # needs sage.rings.finite_rings
            sage: p = 33554473
            sage: F.<u> = GF((p,2))
            sage: E = EllipticCurve(F, [1,0])
            sage: E.j_invariant()
            1728
            sage: P = E.random_point()
            sage: P.order()  # random
            46912611635760

        TESTS:

        Check that the order actually gets cached (:issue:`32786`)::

            sage: # needs sage.rings.finite_rings
            sage: E = EllipticCurve(GF(31337), [42,1])
            sage: P = E.lift_x(1)
            sage: hasattr(P, '_order')
            False
            sage: P.order()
            15649
            sage: P._order
            15649

        The curve order should also get cached as a side effect
        of computing a point order::

            sage: E._order                                                              # needs sage.rings.finite_rings
            31298
        """
    additive_order = order
