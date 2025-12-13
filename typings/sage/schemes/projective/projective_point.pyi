from sage.arith.functions import lcm as lcm
from sage.arith.misc import gcd as gcd
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.categories.number_fields import NumberFields as NumberFields
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.abc import Order as Order
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.quotient_ring import QuotientRing_generic as QuotientRing_generic
from sage.rings.rational_field import QQ as QQ
from sage.rings.ring import CommutativeRing as CommutativeRing
from sage.schemes.generic.morphism import SchemeMorphism as SchemeMorphism, SchemeMorphism_point as SchemeMorphism_point
from sage.structure.element import AdditiveGroupElement as AdditiveGroupElement
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp
from sage.structure.sequence import Sequence as Sequence

class SchemeMorphism_point_projective_ring(SchemeMorphism_point):
    """
    A rational point of projective space over a ring.

    INPUT:

    - ``X`` -- a homset of a subscheme of an ambient projective space over a ring `K`

    - ``v`` -- list or tuple of coordinates in `K`

    - ``check`` -- boolean (default: ``True``); whether to check the input for consistency

    EXAMPLES::

        sage: P = ProjectiveSpace(2, ZZ)
        sage: P(2,3,4)
        (2 : 3 : 4)
    """
    def __init__(self, X, v, check: bool = True) -> None:
        """
        The Python constructor.

        EXAMPLES::

            sage: P = ProjectiveSpace(2, QQ)
            sage: P(2, 3/5, 4)
            (1/2 : 3/20 : 1)

        ::

            sage: P = ProjectiveSpace(1, ZZ)
            sage: P([0, 1])
            (0 : 1)

        ::

            sage: P = ProjectiveSpace(1, ZZ)
            sage: P([0, 0, 1])
            Traceback (most recent call last):
            ...
            TypeError: v (=[0, 0, 1]) must have 2 components

        ::

            sage: P = ProjectiveSpace(3, ZZ)
            sage: P(0,0,0,0)
            Traceback (most recent call last):
            ...
            ValueError: [0, 0, 0, 0] does not define a valid projective point since all entries are zero

        ::

            sage: P = ProjectiveSpace(3, Zmod(15))
            sage: P(3,5,9,10)
            (3 : 5 : 9 : 10)

        ::

            sage: P = ProjectiveSpace(3, Zmod(15))
            sage: P(0,5,10,15)
            Traceback (most recent call last):
            ...
            ValueError: [0, 5, 10, 0] does not define a valid projective point since it is a multiple of a zero divisor

        It is possible to avoid the possibly time-consuming checks, but be careful!! ::

            sage: P = ProjectiveSpace(3, QQ)
            sage: P.point([0,0,0,0], check=False)
            (0 : 0 : 0 : 0)

        ::

            sage: P.<x, y, z> = ProjectiveSpace(2, ZZ)
            sage: X = P.subscheme([x^2 - y*z])
            sage: X([2, 2, 2])
            (2 : 2 : 2)

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: P = ProjectiveSpace(1, R.quo(t^2 + 1))                                # needs sage.libs.pari
            sage: P([2*t, 1])                                                           # needs sage.libs.pari
            (2*tbar : 1)

        ::

            sage: P = ProjectiveSpace(ZZ, 1)
            sage: P.point(Infinity)
            (1 : 0)
            sage: P(infinity)
            (1 : 0)

        ::

            sage: P = ProjectiveSpace(ZZ, 2)
            sage: P(Infinity)
            Traceback (most recent call last):
            ...
            ValueError: +Infinity not well defined in dimension > 1
            sage: P.point(infinity)
            Traceback (most recent call last):
            ...
            ValueError: +Infinity not well defined in dimension > 1
        """
    def __hash__(self):
        """
        Compute the hash value of this point.

        If the base ring has a fraction field, normalize the point in
        the fraction field and then hash so that equal points have
        equal hash values. If the base ring is not an integral domain,
        return the hash of the parent.

        OUTPUT: integer

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: hash(P([1, 1])) == hash(P.point([2, 2], False))
            True

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<w> = NumberField(x^2 + 3)
            sage: O = K.maximal_order()
            sage: P.<x,y> = ProjectiveSpace(O, 1)
            sage: hash(P([1 + w, 2])) == hash(P([2, 1 - w]))
            True

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(Zmod(10), 1)
            sage: Q.<x,y> = ProjectiveSpace(Zmod(10), 1)
            sage: hash(P([2, 5])) == hash(Q([2, 5]))
            True
            sage: hash(P([2, 5])) == hash(P([2, 5]))
            True
            sage: hash(P([3, 7])) == hash(P([2, 5]))
            True
        """
    def scale_by(self, t) -> None:
        """
        Scale the coordinates of the point by ``t``.

        A :exc:`TypeError` occurs if the point is not in the
        base_ring of the codomain after scaling.

        INPUT:

        - ``t`` -- a ring element

        OUTPUT: none

        EXAMPLES::

            sage: R.<t> = PolynomialRing(QQ)
            sage: P = ProjectiveSpace(R, 2, 'x')
            sage: p = P([3/5*t^3, 6*t, t])
            sage: p.scale_by(1/t); p
            (3/5*t^2 : 6 : 1)

        ::

            sage: # needs sage.libs.pari
            sage: R.<t> = PolynomialRing(QQ)
            sage: S = R.quo(R.ideal(t^3))
            sage: P.<x,y,z> = ProjectiveSpace(S, 2)
            sage: Q = P(t, 1, 1)
            sage: Q.scale_by(t);Q
            (tbar^2 : tbar : tbar)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ,2)
            sage: Q = P(2, 2, 2)
            sage: Q.scale_by(1/2);Q
            (1 : 1 : 1)
        """
    def normalize_coordinates(self) -> None:
        '''
        Removes the gcd from the coordinates of this point (including `-1`)
        and rescales everything so that the last nonzero entry is as "simple"
        as possible. The notion of "simple" here depends on the base ring;
        concretely, the last nonzero coordinate will be `1` in a field and
        positive over an ordered ring.

        .. WARNING:: The gcd will depend on the base ring.

        OUTPUT: none

        EXAMPLES::

            sage: P = ProjectiveSpace(ZZ, 2, \'x\')
            sage: p = P([-5, -15, -20])
            sage: p.normalize_coordinates(); p
            (1 : 3 : 4)

        ::

            sage: # needs sage.rings.padics
            sage: P = ProjectiveSpace(Zp(7), 2, \'x\')
            sage: p = P([-5, -15, -2])
            sage: p.normalize_coordinates(); p
            (6 + 3*7 + 3*7^2 + 3*7^3 + 3*7^4 + 3*7^5 + 3*7^6 + 3*7^7 + 3*7^8 + 3*7^9 + 3*7^10 + 3*7^11 + 3*7^12 + 3*7^13 + 3*7^14 + 3*7^15 + 3*7^16 + 3*7^17 + 3*7^18 + 3*7^19 + O(7^20) : 4 + 4*7 + 3*7^2 + 3*7^3 + 3*7^4 + 3*7^5 + 3*7^6 + 3*7^7 + 3*7^8 + 3*7^9 + 3*7^10 + 3*7^11 + 3*7^12 + 3*7^13 + 3*7^14 + 3*7^15 + 3*7^16 + 3*7^17 + 3*7^18 + 3*7^19 + O(7^20) : 1 + O(7^20))

        ::

            sage: R.<t> = PolynomialRing(QQ)
            sage: P = ProjectiveSpace(R, 2, \'x\')
            sage: p = P([3/5*t^3, 6*t, t])
            sage: p.normalize_coordinates(); p
            (3/5*t^2 : 6 : 1)

        ::

            sage: P.<x,y> = ProjectiveSpace(Zmod(20), 1)
            sage: Q = P(3, 6)
            sage: Q.normalize_coordinates()
            sage: Q
            (1 : 2)

        Since the base ring is a polynomial ring over a field, only the
        gcd `c` is removed. ::

            sage: R.<c> = PolynomialRing(QQ)
            sage: P = ProjectiveSpace(R, 1)
            sage: Q = P(2*c, 4*c)
            sage: Q.normalize_coordinates(); Q
            (1/2 : 1)

        A polynomial ring over a ring gives the more intuitive result. ::

            sage: R.<c> = PolynomialRing(ZZ)
            sage: P = ProjectiveSpace(R, 1)
            sage: Q = P(2*c, 4*c)
            sage: Q.normalize_coordinates();Q
            (1 : 2)

        ::

            sage: # needs sage.libs.singular
            sage: R.<t> = QQ[]
            sage: S = R.quotient_ring(R.ideal(t^3))
            sage: P.<x,y> = ProjectiveSpace(S, 1)
            sage: Q = P(t + 1, t^2 + t)
            sage: Q.normalize_coordinates()
            sage: Q
            (1 : tbar)
        '''
    def dehomogenize(self, n):
        """
        Dehomogenizes at the `n`-th coordinate.

        INPUT:

        - ``n`` -- nonnegative integer

        OUTPUT: :class:`SchemeMorphism_point_affine`

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: Q = X(23, 23, 46)
            sage: Q.dehomogenize(2)                                                     # needs sage.libs.singular
            (1/2, 1/2)

        ::

            sage: # needs sage.libs.pari
            sage: R.<t> = PolynomialRing(QQ)
            sage: S = R.quo(R.ideal(t^3))
            sage: P.<x,y,z> = ProjectiveSpace(S, 2)
            sage: Q = P(t, 1, 1)
            sage: Q.dehomogenize(1)
            (tbar, 1)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: Q = P(1, 3, 1)
            sage: Q.dehomogenize(0)
            (3, 1)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: Q = P(1, 3, 0)
            sage: Q.dehomogenize(2)
            Traceback (most recent call last):
            ...
            ValueError: can...t dehomogenize at 0 coordinate
        """
    def global_height(self, prec=None):
        """
        Return the absolute logarithmic height of the point.

        INPUT:

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: Q = P.point([4, 4, 1/30])
            sage: Q.global_height()                                                     # needs sage.symbolic
            4.78749174278205

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: Q = P([4, 1, 30])
            sage: Q.global_height()                                                     # needs sage.symbolic
            3.40119738166216

        ::

            sage: R.<x> = PolynomialRing(QQ)
            sage: k.<w> = NumberField(x^2 + 5)                                          # needs sage.rings.number_field
            sage: A = ProjectiveSpace(k, 2, 'z')                                        # needs sage.rings.number_field
            sage: A([3, 5*w + 1, 1]).global_height(prec=100)                            # needs sage.rings.number_field
            2.4181409534757389986565376694

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQbar, 2)                                 # needs sage.rings.number_field
            sage: Q = P([QQbar(sqrt(3)), QQbar(sqrt(-2)), 1])                           # needs sage.rings.number_field sage.symbolic
            sage: Q.global_height()                                                     # needs sage.rings.number_field sage.symbolic
            0.549306144334055

        ::

            sage: # needs sage.rings.number_field
            sage: K = UniversalCyclotomicField()
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: Q = P.point([K(4/3), K.gen(7), K.gen(5)])
            sage: Q.global_height()
            1.38629436111989

        TESTS::

            sage: P = ProjectiveSpace(QQ, 2)
            sage: P(1/1, 2/3, 5/8).global_height()                                      # needs sage.symbolic
            3.17805383034795

            sage: x = polygen(QQ, 'x')
            sage: F.<u> = NumberField(x^3 - 5)                                          # needs sage.rings.number_field
            sage: P = ProjectiveSpace(F, 2)                                             # needs sage.rings.number_field
            sage: P(u, u^2/5, 1).global_height()                                        # needs sage.rings.number_field
            1.07295860828940
        """
    def local_height(self, v, prec=None):
        """
        Return the maximum of the local height of the coordinates of this point.

        INPUT:

        - ``v`` -- a prime or prime ideal of the base ring

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: Q = P.point([4, 4, 1/150], False)
            sage: Q.local_height(5)                                                     # needs sage.rings.real_mpfr
            3.21887582486820

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: Q = P([4, 1, 30])
            sage: Q.local_height(2)                                                     # needs sage.rings.real_mpfr
            0.693147180559945
        """
    def local_height_arch(self, i, prec=None):
        """
        Return the maximum of the local heights at the ``i``-th infinite place of this point.

        INPUT:

        - ``i`` -- integer

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: Q = P.point([4, 4, 1/150], False)
            sage: Q.local_height_arch(0)                                                # needs sage.rings.real_mpfr
            1.38629436111989

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y,z> = ProjectiveSpace(QuadraticField(5, 'w'), 2)
            sage: Q = P.point([4, 1, 30], False)
            sage: Q.local_height_arch(1)
            3.401197381662155375413236691607
        """
    def multiplier(self, f, n, check: bool = True):
        """
        Return the multiplier of this point of period ``n`` by the function ``f``.

        ``f`` must be an endomorphism of projective space.

        INPUT:

        - ``f`` -- a endomorphism of this point's codomain

        - ``n`` -- positive integer; the period of this point

        - ``check`` -- boolean (default: ``True``); check if ``P`` is periodic
          of period ``n``

        OUTPUT:

        - a square matrix of size ``self.codomain().dimension_relative()`` in the
          ``base_ring`` of this point.

        EXAMPLES::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: f = DynamicalSystem_projective([x^2, y^2, 4*w^2, 4*z^2], domain=P)    # needs sage.schemes
            sage: Q = P.point([4, 4, 1, 1], False)
            sage: Q.multiplier(f, 1)                                                    # needs sage.schemes
            [ 2  0 -8]
            [ 0  2 -8]
            [ 0  0 -2]
        """
    def is_preperiodic(self, f, err: float = 0.1, return_period: bool = False):
        """
        Determine if the point is preperiodic with respect to the map ``f``.

        This is implemented for both projective space and subschemes.
        There are two optional keyword arguments:
        ``error_bound`` sets the error_bound used in the canonical height computation
        and ``return_period`` a boolean which controls if the period is returned if the
        point is preperiodic. If ``return_period`` is ``True`` and this point is not
        preperiodic, then `(0,0)` is returned for the period.

        ALGORITHM:

        We know that a point is preperiodic if and only if it has canonical height zero. However,
        we can only compute the canonical height up to numerical precision. This function first computes
        the canonical height of the point to the given error bound. If it is larger than that error bound,
        then it must not be preperiodic. If it is less than the error bound, then we expect preperiodic. In
        this case we begin computing the orbit stopping if either we determine the orbit is finite, or
        the height of the point is large enough that it must be wandering. We can determine the height
        cutoff by computing the height difference constant, i.e., the bound between the height and
        the canonical height of a point (which depends only on the map and not the point itself).
        If the height of the point is larger than the difference bound, then the canonical height
        cannot be zero so the point cannot be preperiodic.

        INPUT:

        - ``f`` -- an endomorphism of this point's codomain

        kwds:

        - ``err`` -- a positive real number (default: 0.1)

        - ``return_period`` -- boolean (default: ``False``)


        OUTPUT:

        - boolean; ``True`` if preperiodic.

        - if ``return_period`` is ``True``, then ``(0,0)`` if wandering, and ``(m,n)``
          if preperiod ``m`` and period ``n``.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([x^3 - 3*x*y^2, y^3], domain=P)        # needs sage.schemes
            sage: Q = P(-1, 1)
            sage: Q.is_preperiodic(f)                                                   # needs sage.libs.singular sage.schemes
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme(z)
            sage: f = DynamicalSystem([x^2 - y^2, y^2, z^2], domain=X)                  # needs sage.schemes
            sage: p = X((-1, 1, 0))
            sage: p.is_preperiodic(f, return_period=True)                               # needs sage.libs.singular sage.schemes
            (0, 2)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ,1)
            sage: f = DynamicalSystem_projective([x^2 - 29/16*y^2, y^2], domain=P)      # needs sage.schemes
            sage: Q = P(1, 4)
            sage: Q.is_preperiodic(f, return_period=True)                               # needs sage.libs.singular sage.schemes
            (1, 3)
            sage: Q = P(1, 1)
            sage: Q.is_preperiodic(f, return_period=True)                               # needs sage.libs.singular sage.schemes
            (0, 0)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<a> = NumberField(x^2 + 1)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([x^5 + 5/4*x*y^4, y^5], domain=P)      # needs sage.schemes
            sage: Q = P([-1/2*a + 1/2, 1])
            sage: Q.is_preperiodic(f)                                                   # needs sage.schemes
            True
            sage: Q = P([a, 1])
            sage: Q.is_preperiodic(f)                                                   # needs sage.schemes
            False

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = DynamicalSystem_projective([                                      # needs sage.schemes
            ....:         -38/45*x^2 + (2*y - 7/45*z)*x + (-1/2*y^2 - 1/2*y*z + z^2),
            ....:         -67/90*x^2 + (2*y + z*157/90)*x - y*z,
            ....:         z^2
            ....:     ], domain=P)
            sage: Q = P([1, 3, 1])
            sage: Q.is_preperiodic(f, return_period=True)                               # needs sage.libs.singular sage.schemes
            (0, 9)

        ::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: f = DynamicalSystem_projective([                                      # needs sage.schemes
            ....:         (-y - w)*x + (-13/30*y^2 + 13/30*w*y + w^2),
            ....:         -1/2*x^2 + (-y + 3/2*w)*x + (-1/3*y^2 + 4/3*w*y),
            ....:         -3/2*z^2 + 5/2*z*w + w^2,
            ....:         w^2
            ....:     ], domain=P)
            sage: Q = P([3,0,4/3,1])
            sage: Q.is_preperiodic(f, return_period=True)                               # needs sage.libs.singular sage.schemes
            (2, 24)

        ::

            sage: # needs sage.rings.number_field sage.schemes sage.symbolic
            sage: from sage.misc.verbose import set_verbose
            sage: set_verbose(-1)
            sage: P.<x,y,z> = ProjectiveSpace(QQbar, 2)
            sage: f = DynamicalSystem_projective([x^2, QQbar(sqrt(-1))*y^2, z^2],
            ....:                                domain=P)
            sage: Q = P([1, 1, 1])
            sage: Q.is_preperiodic(f)
            True

        ::

            sage: # needs sage.rings.number_field sage.schemes sage.symbolic
            sage: set_verbose(-1)
            sage: P.<x,y,z> = ProjectiveSpace(QQbar, 2)
            sage: f = DynamicalSystem_projective([x^2, y^2, z^2], domain=P)
            sage: Q = P([QQbar(sqrt(-1)), 1, 1])
            sage: Q.is_preperiodic(f)
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([16*x^2 - 29*y^2, 16*y^2], domain=P)   # needs sage.schemes
            sage: Q = P(-1,4)
            sage: Q.is_preperiodic(f)                                                   # needs sage.libs.singular sage.schemes
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(3), 2)
            sage: F = DynamicalSystem([x^2 - 2*y^2, y^2, z^2])                          # needs sage.schemes
            sage: Q = P(1, 1, 1)
            sage: Q.is_preperiodic(F, return_period=True)                               # needs sage.schemes
            (1, 1)

        TESTS::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = End(P)
            sage: f = H([16*x^2 - 29*y^2, 16*y^2])
            sage: Q = P(-1,4)
            sage: Q.is_preperiodic(f)
            Traceback (most recent call last):
            ...
            TypeError: map must be a dynamical system

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([16*x^2 - 29*y^2, 16*y^2])             # needs sage.schemes
            sage: Q = P(11,4)
            sage: Q.is_preperiodic(f, err=2)                                            # needs sage.libs.singular sage.schemes
            False
        """

class SchemeMorphism_point_projective_field(SchemeMorphism_point_projective_ring):
    """
    A rational point of projective space over a field.

    INPUT:

    - ``X`` -- a homset of a subscheme of an ambient projective space
      over a field `K`

    - ``v`` -- list or tuple of coordinates in `K`

    - ``check`` -- boolean (default: ``True``); whether to
      check the input for consistency

    EXAMPLES::

        sage: # needs sage.rings.real_mpfr
        sage: P = ProjectiveSpace(3, RR)
        sage: P(2, 3, 4, 5)
        (0.400000000000000 : 0.600000000000000 : 0.800000000000000 : 1.00000000000000)
    """
    def __init__(self, X, v, check: bool = True) -> None:
        """
        The Python constructor.

        See :class:`SchemeMorphism_point_projective_ring` for details.

        This function still normalizes points so that the rightmost nonzero coordinate is 1.
        This is to maintain functionality with current
        implementations of curves in projectives space (plane, conic, elliptic, etc).
        The :class:`SchemeMorphism_point_projective_ring` is for general use.

        EXAMPLES::

            sage: P = ProjectiveSpace(2, QQ)
            sage: P(2, 3/5, 4)
            (1/2 : 3/20 : 1)

        ::

            sage: P = ProjectiveSpace(3, QQ)
            sage: P(0, 0, 0, 0)
            Traceback (most recent call last):
            ...
            ValueError: [0, 0, 0, 0] does not define a valid projective point since all entries are zero

        ::

            sage: P.<x, y, z> = ProjectiveSpace(2, QQ)
            sage: X = P.subscheme([x^2 - y*z])
            sage: X([2, 2, 2])
            (1 : 1 : 1)

        ::

            sage: P = ProjectiveSpace(1, GF(7))
            sage: Q = P([2, 1])
            sage: Q[0].parent()
            Finite Field of size 7

        ::

            sage: P = ProjectiveSpace(QQ, 1)
            sage: P.point(Infinity)
            (1 : 0)
            sage: P(infinity)
            (1 : 0)

        ::

            sage: P = ProjectiveSpace(QQ, 2)
            sage: P(infinity)
            Traceback (most recent call last):
            ...
            ValueError: +Infinity not well defined in dimension > 1
            sage: P.point(infinity)
            Traceback (most recent call last):
            ...
            ValueError: +Infinity not well defined in dimension > 1
        """
    def __hash__(self):
        """
        Compute the hash value of this point.

        OUTPUT: integer

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: hash(P([1/2, 1])) == hash(P.point([1, 2], False))
            True
        """
    def normalize_coordinates(self) -> None:
        """
        Normalize the point so that the last nonzero coordinate is `1`.

        OUTPUT: none

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: Q = P.point([GF(5)(1), GF(5)(3), GF(5)(0)], False); Q
            (1 : 3 : 0)
            sage: Q.normalize_coordinates(); Q
            (2 : 1 : 0)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme(x^2 - y^2);
            sage: Q = X.point([23, 23, 46], False); Q
            (23 : 23 : 46)
            sage: Q.normalize_coordinates(); Q
            (1/2 : 1/2 : 1)
        """
    def clear_denominators(self) -> None:
        """
        Scale by the least common multiple of the denominators.

        OUTPUT: none

        EXAMPLES::

            sage: R.<t> = PolynomialRing(QQ)
            sage: P.<x,y,z> = ProjectiveSpace(FractionField(R), 2)
            sage: Q = P([t, 3/t^2, 1])
            sage: Q.clear_denominators(); Q
            (t^3 : 3 : t^2)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<w> = NumberField(x^2 - 3)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: Q = P([1/w, 3, 0])
            sage: Q.clear_denominators(); Q
            (w : 9 : 0)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: Q = X([1/2, 1/2, 1])
            sage: Q.clear_denominators(); Q
            (1 : 1 : 2)

        ::

            sage: PS.<x,y> = ProjectiveSpace(QQ, 1)
            sage: Q = PS.point([1, 2/3], False); Q
            (1 : 2/3)
            sage: Q.clear_denominators(); Q
            (3 : 2)
        """
    def intersection_multiplicity(self, X):
        """
        Return the intersection multiplicity of the codomain of this point and ``X`` at this point.

        This uses the intersection_multiplicity implementations for projective/affine subschemes. This
        point must be a point of a projective subscheme.

        INPUT:

        - ``X`` -- a subscheme in the same ambient space as that of the codomain of this point

        OUTPUT: integer

        EXAMPLES::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: X = P.subscheme([x*z - y^2])
            sage: Y = P.subscheme([x^3 - y*w^2 + z*w^2, x*y - z*w])
            sage: Q1 = X([1/2, 1/4, 1/8, 1])
            sage: Q1.intersection_multiplicity(Y)                                       # needs sage.libs.singular
            1
            sage: Q2 = X([0,0,0,1])
            sage: Q2.intersection_multiplicity(Y)                                       # needs sage.libs.singular
            5
            sage: Q3 = X([0,0,1,0])
            sage: Q3.intersection_multiplicity(Y)                                       # needs sage.libs.singular
            6

        ::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: X = P.subscheme([x^2 - y^2])
            sage: Q = P([1,1,1,0])
            sage: Q.intersection_multiplicity(X)
            Traceback (most recent call last):
            ...
            TypeError: this point must be a point on a projective subscheme
        """
    def multiplicity(self):
        """
        Return the multiplicity of this point on its codomain.

        Uses the subscheme multiplicity implementation. This point must be a point on
        a projective subscheme.

        OUTPUT: integer

        EXAMPLES::

            sage: P.<x,y,z,w,t> = ProjectiveSpace(QQ, 4)
            sage: X = P.subscheme([y^6 - x^3*w^2*t + t^5*w, x^2 - t^2])
            sage: Q1 = X([1,0,2,1,1])
            sage: Q1.multiplicity()                                                     # needs sage.libs.singular
            1
            sage: Q2 = X([0,0,-2,1,0])
            sage: Q2.multiplicity()                                                     # needs sage.libs.singular
            8
        """
    def as_subscheme(self):
        """
        Return the subscheme associated with this rational point.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: p1 = P2.point([0,0,1]).as_subscheme(); p1
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x, y
            sage: p2 = P2.point([1,1,1]).as_subscheme(); p2
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x - z, y - z
            sage: p1 + p2
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x - y, y^2 - y*z
        """

class SchemeMorphism_point_projective_finite_field(SchemeMorphism_point_projective_field):
    def __hash__(self):
        """
        Return the integer hash of this point.

        OUTPUT: integer

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: hash(P(2, 1, 2))
            41

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: hash(X(1, 1, 2))
            81

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(13), 1)
            sage: hash(P(3, 4))
            17

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(13^3,'t'), 1)                            # needs sage.rings.finite_rings
            sage: hash(P(3, 4))                                                         # needs sage.rings.finite_rings
            2201
        """

class SchemeMorphism_point_abelian_variety_field(AdditiveGroupElement, SchemeMorphism_point_projective_field):
    """
    A rational point of an abelian variety over a field.

    EXAMPLES::

        sage: # needs sage.schemes
        sage: E = EllipticCurve([0,0,1,-1,0])
        sage: origin = E(0)
        sage: origin.domain()
        Spectrum of Rational Field
        sage: origin.codomain()
        Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
    """
