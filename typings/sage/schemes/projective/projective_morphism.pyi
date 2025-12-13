from sage.arith.functions import lcm as lcm
from sage.categories.fields import Fields as Fields
from sage.categories.finite_fields import FiniteFields as FiniteFields
from sage.categories.homset import End as End, Hom as Hom
from sage.categories.number_fields import NumberFields as NumberFields
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.quotient_ring import QuotientRing_generic as QuotientRing_generic
from sage.rings.rational_field import QQ as QQ
from sage.schemes.generic.morphism import SchemeMorphism_polynomial as SchemeMorphism_polynomial

class SchemeMorphism_polynomial_projective_space(SchemeMorphism_polynomial):
    """
    A morphism of schemes determined by rational functions that define
    what the morphism does on points in the ambient projective space.

    EXAMPLES::

        sage: R.<x,y> = QQ[]
        sage: P1 = ProjectiveSpace(R)
        sage: H = P1.Hom(P1)
        sage: H([y,2*x])
        Scheme endomorphism of Projective Space of dimension 1 over Rational Field
          Defn: Defined on coordinates by sending (x : y) to
                (y : 2*x)

    An example of a morphism between projective plane curves (see :issue:`10297`)::

        sage: # needs sage.schemes
        sage: P2.<x,y,z> = ProjectiveSpace(QQ, 2)
        sage: f = x^3 + y^3 + 60*z^3
        sage: g = y^2*z - (x^3 - 6400*z^3/3)
        sage: C = Curve(f)
        sage: E = Curve(g)
        sage: xbar,ybar,zbar = C.coordinate_ring().gens()
        sage: H = C.Hom(E)
        sage: H([zbar, xbar - ybar, -(xbar+ybar)/80])
        Scheme morphism:
          From: Projective Plane Curve over Rational Field defined by x^3 + y^3 + 60*z^3
          To:   Projective Plane Curve over Rational Field defined by -x^3 + y^2*z + 6400/3*z^3
          Defn: Defined on coordinates by sending (x : y : z) to
                (z : x - y : -1/80*x - 1/80*y)

    A more complicated example::

        sage: P2.<x,y,z> = ProjectiveSpace(2, QQ)
        sage: P1 = P2.subscheme(x - y)
        sage: H12 = P1.Hom(P2)
        sage: H12([x^2, x*z, z^2])
        Scheme morphism:
          From: Closed subscheme of Projective Space of dimension 2 over Rational Field
                defined by: x - y
          To:   Projective Space of dimension 2 over Rational Field
          Defn: Defined on coordinates by sending (x : y : z) to (x^2 : x*z : z^2)

    We illustrate some error checking::

        sage: R.<x,y> = QQ[]
        sage: P1 = ProjectiveSpace(R)
        sage: H = P1.Hom(P1)
        sage: f = H([x - y, x*y])
        Traceback (most recent call last):
        ...
        ValueError: polys (=[x - y, x*y]) must be of the same degree

        sage: H([x - 1, x*y + x])
        Traceback (most recent call last):
        ...
        ValueError: polys (=[x - 1, x*y + x]) must be homogeneous

        sage: H([exp(x), exp(y)])                                                       # needs sage.symbolic
        Traceback (most recent call last):
        ...
        TypeError: polys (=[e^x, e^y]) must be elements of
        Multivariate Polynomial Ring in x, y over Rational Field

    We can also compute the forward image of subschemes through
    elimination. In particular, let `X = V(h_1,\\ldots, h_t)` and define the ideal
    `I = (h_1,\\ldots,h_t,y_0-f_0(\\bar{x}), \\ldots, y_n-f_n(\\bar{x}))`.
    Then the elimination ideal `I_{n+1} = I \\cap K[y_0,\\ldots,y_n]` is a homogeneous
    ideal and `f(X) = V(I_{n+1})`::

        sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
        sage: H = End(P)
        sage: f = H([(x-2*y)^2, (x-2*z)^2, x^2])
        sage: X = P.subscheme(y-z)
        sage: f(f(f(X)))                                                                # needs sage.libs.singular
        Closed subscheme of Projective Space of dimension 2 over Rational Field
         defined by:
          y - z

    ::

        sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
        sage: H = End(P)
        sage: f = H([(x-2*y)^2, (x-2*z)^2, (x-2*w)^2, x^2])
        sage: f(P.subscheme([x,y,z]))                                                   # needs sage.libs.singular
        Closed subscheme of Projective Space of dimension 3 over Rational Field
         defined by:
          w,
          y,
          x
    """
    def __init__(self, parent, polys, check: bool = True) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: P1.<x,y> = ProjectiveSpace(QQ,1)
            sage: H = P1.Hom(P1)
            sage: H([y,2*x])
            Scheme endomorphism of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to
                    (y : 2*x)

        ::

            sage: R.<t> = PolynomialRing(QQ)
            sage: P.<x,y,z> = ProjectiveSpace(R, 2)
            sage: X = P.subscheme([x])
            sage: H = End(X)
            sage: H([x^2, t*y^2, x*z])
            Scheme endomorphism of Closed subscheme of Projective Space of dimension 2
             over Univariate Polynomial Ring in t over Rational Field defined by: x
              Defn: Defined on coordinates by sending (x : y : z) to
                    (x^2 : t*y^2 : x*z)

        When elements of the quotient ring is used, they are reduced::

            sage: # needs sage.rings.real_mpfr
            sage: P.<x,y,z> = ProjectiveSpace(CC, 2)
            sage: X = P.subscheme([x - y])
            sage: u,v,w = X.coordinate_ring().gens()                                    # needs sage.libs.singular
            sage: H = End(X)
            sage: H([u^2, v^2, w*u])                                                    # needs sage.libs.singular
            Scheme endomorphism of Closed subscheme of Projective Space of dimension 2
             over Complex Field with 53 bits of precision defined by: x - y
              Defn: Defined on coordinates by sending (x : y : z) to
                    (y^2 : y^2 : y*z)
        """
    def __call__(self, x, check: bool = True):
        """
        Compute the forward image of the point or subscheme ``x`` by this map.

        For subschemes, the forward image is computed through elimination.
        In particular, let `X = V(h_1,\\ldots, h_t)` and define the ideal
        `I = (h_1,\\ldots,h_t,y_0-f_0(\\bar{x}), \\ldots, y_n-f_n(\\bar{x}))`.
        Then the elimination ideal `I_{n+1} = I \\cap K[y_0,\\ldots,y_n]` is a homogeneous
        ideal and `self(X) = V(I_{n+1})`.

        The input boolean ``check`` can be set to false when fast iteration of
        points is desired. It bypasses all input checking and passes ``x`` straight
        to the fast evaluation of points function.

        INPUT:

        - ``x`` -- a point or subscheme in domain of this map

        - ``check`` -- boolean; if ``False`` assume that ``x`` is a point

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = End(P)
            sage: f = H([x^2 + y^2, y^2, z^2 + y*z])
            sage: f(P([1,1,1]))
            (1 : 1/2 : 1)

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: P1.<u,v> = ProjectiveSpace(QQ, 1)
            sage: H = End(P1)
            sage: f = H([u^2, v^2])
            sage: f(PS([0,1,1]))
            Traceback (most recent call last):
            ...
            TypeError: (0 : 1 : 1) fails to convert into the map's domain Projective Space of
            dimension 1 over Rational Field, but a `pushforward` method is not properly implemented

        ::

            sage: PS.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P1.<u,v> = ProjectiveSpace(QQ, 1)
            sage: H = End(P1)
            sage: f = H([u^2, v^2])
            sage: f([0,1])
            (0 : 1)
            sage: f(PS([0,1]))
            (0 : 1)

        ::

            sage: PS.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: H = End(PS)
            sage: f = H([y^2, x^2, w^2, z^2])
            sage: X = PS.subscheme([z^2 + y*w])
            sage: f(X)                                                                  # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 3 over Rational Field
            defined by:
              x*z - w^2

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: P1.<u,v> = ProjectiveSpace(ZZ, 1)
            sage: H = End(PS)
            sage: f = H([x^2, y^2, z^2])
            sage: X = P1.subscheme([u - v])
            sage: f(X)                                                                  # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            TypeError: subscheme must be in ambient space of domain of map

        ::

            sage: PS.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: P1.<u,v> = ProjectiveSpace(ZZ, 1)
            sage: H = End(P1)
            sage: f = H([u^2, v^2])
            sage: f([u - v])                                                            # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 1 over Integer Ring defined by:
              u - v
            sage: X = PS.subscheme([x - z])
            sage: f([x - z])
            Traceback (most recent call last):
            ...
            TypeError: [x - z] fails to convert into the map's domain Projective Space of
            dimension 1 over Integer Ring, but a `pushforward` method is not properly implemented

        TESTS:

        Check that :issue:`32209` is fixed::

            sage: S.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: T.<u,v> = ProjectiveSpace(ZZ, 1)
            sage: h = T.hom([u^2 + v^2, u*v], S); h
            Scheme morphism:
              From: Projective Space of dimension 1 over Integer Ring
              To:   Projective Space of dimension 1 over Integer Ring
              Defn: Defined on coordinates by sending (u : v) to
                    (u^2 + v^2 : u*v)

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: P = T(F)(1, a)
            sage: h(P)                                                                  # needs sage.libs.singular
            (1 : 1)
            sage: h(P).domain()
            Spectrum of Finite Field in a of size 2^2
            sage: h.change_ring(F)(P)
            (1 : 1)
        """
    def __eq__(self, right):
        """
        Test the equality of two projective morphisms.

        INPUT:

        - ``right`` -- a map on projective space

        OUTPUT:

        ``True`` if ``self`` and ``right`` define the same projective map.
        ``False`` otherwise.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = Hom(P, P)
            sage: f = H([x^2 - 2*x*y + z*x, z^2 - y^2, 5*z*y])
            sage: g = H([x^2, y^2, z^2])
            sage: f == g
            False

        ::

            sage: # needs sage.rings.real_mpfr
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P2.<u,v> = ProjectiveSpace(CC, 1)
            sage: H = End(P)
            sage: H2 = End(P2)
            sage: f = H([x^2 - 2*x*y, y^2])
            sage: g = H2([u^2 - 2*u*v, v^2])
            sage: f == g
            False

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = End(P)
            sage: f = H([x^2 - 2*x*y, y^2])
            sage: g = H([x^2*y - 2*x*y^2, y^3])
            sage: f == g
            True
        """
    def __ne__(self, right):
        """
        Test the inequality of two projective morphisms.

        INPUT:

        - ``right`` -- a map on projective space

        OUTPUT:

        ``True`` if ``self`` and ``right`` define different projective maps.
        ``False`` otherwise.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([x^3 - 2*x^2*y, 5*x*y^2])
            sage: g = f.change_ring(GF(7))
            sage: f != g
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = Hom(P, P)
            sage: f = H([x^2 - 2*x*y + z*x, z^2 - y^2, 5*z*y])
            sage: f != f
            False
        """
    def as_dynamical_system(self):
        """
        Return this endomorphism as a :class:`DynamicalSystem_projective`.

        OUTPUT: :class:`DynamicalSystem_projective`

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: H = End(P)
            sage: f = H([x^2, y^2, z^2])
            sage: type(f.as_dynamical_system())                                         # needs sage.schemes
            <class 'sage.dynamics.arithmetic_dynamics.projective_ds.DynamicalSystem_projective'>

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = End(P)
            sage: f = H([x^2 - y^2, y^2])
            sage: type(f.as_dynamical_system())                                         # needs sage.schemes
            <class 'sage.dynamics.arithmetic_dynamics.projective_ds.DynamicalSystem_projective_field'>

        ::

            sage: P.<x,y> = ProjectiveSpace(GF(5), 1)
            sage: H = End(P)
            sage: f = H([x^2, y^2])
            sage: type(f.as_dynamical_system())                                         # needs sage.schemes
            <class 'sage.dynamics.arithmetic_dynamics.projective_ds.DynamicalSystem_projective_finite_field'>

        ::

            sage: P.<x,y> = ProjectiveSpace(RR, 1)
            sage: f = DynamicalSystem([x^2 + y^2, y^2], P)                              # needs sage.schemes
            sage: g = f.as_dynamical_system()                                           # needs sage.schemes
            sage: g is f                                                                # needs sage.schemes
            True
        """
    def scale_by(self, t) -> None:
        """
        Scale each coordinate by a factor of ``t``.

        A :exc:`TypeError` occurs if the point is not in the coordinate ring
        of the parent after scaling.

        INPUT:

        - ``t`` -- a ring element

        OUTPUT: none

        EXAMPLES::

            sage: A.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(A, A)
            sage: f = H([x^3 - 2*x*y^2, x^2*y])
            sage: f.scale_by(1/x)
            sage: f
            Scheme endomorphism of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to (x^2 - 2*y^2 : x*y)

        ::

            sage: R.<t> = PolynomialRing(QQ)
            sage: P.<x,y> = ProjectiveSpace(R, 1)
            sage: H = Hom(P,P)
            sage: f = H([3/5*x^2, 6*y^2])
            sage: f.scale_by(5/3*t); f
            Scheme endomorphism of Projective Space of dimension 1 over
             Univariate Polynomial Ring in t over Rational Field
              Defn: Defined on coordinates by sending (x : y) to (t*x^2 : 10*t*y^2)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: H = Hom(X, X)
            sage: f = H([x^2, y^2, z^2])
            sage: f.scale_by(x - y); f                                                  # needs sage.libs.singular
            Scheme endomorphism of Closed subscheme of Projective Space of dimension 2
             over Finite Field of size 7 defined by: x^2 - y^2
              Defn: Defined on coordinates by sending (x : y : z) to
                    (x*y^2 - y^3 : x*y^2 - y^3 : x*z^2 - y*z^2)
        """
    def normalize_coordinates(self, **kwds) -> None:
        """
        Ensures that this morphism has integral coefficients.
        If the coordinate ring has a GCD, then it ensures that the
        coefficients have no common factor.

        It also makes the leading coefficients of the first polynomial
        positive (if positive has meaning in the coordinate ring).
        This is done in place.

        When ``ideal`` or ``valuation`` is specified, normalization occurs
        with respect to the absolute value defined by the ``ideal`` or
        ``valuation``. That is, the coefficients are scaled such that
        one coefficient has absolute value 1 while the others have
        absolute value less than or equal to 1.
        Only supported when the base ring is a number field.

        INPUT: keyword arguments:

        - ``ideal`` -- (optional) a prime ideal of the base ring of this
          morphism

        - ``valuation`` -- (optional) a valuation of the base ring of this
          morphism

        OUTPUT: none

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([5/4*x^3, 5*x*y^2])
            sage: f.normalize_coordinates(); f
            Scheme endomorphism of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to (x^2 : 4*y^2)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(7), 2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: H = Hom(X, X)
            sage: f = H([x^3 + x*y^2, x*y^2, x*z^2])
            sage: f.normalize_coordinates(); f                                          # needs sage.libs.singular
            Scheme endomorphism of Closed subscheme of Projective Space of dimension 2
             over Finite Field of size 7 defined by: x^2 - y^2
              Defn: Defined on coordinates by sending (x : y : z) to (2*y^2 : y^2 : z^2)

        ::

            sage: R.<a,b> = QQ[]
            sage: P.<x,y,z> = ProjectiveSpace(R, 2)
            sage: H = End(P)
            sage: f = H([a*(x*z + y^2)*x^2, a*b*(x*z + y^2)*y^2, a*(x*z + y^2)*z^2])
            sage: f.normalize_coordinates(); f
            Scheme endomorphism of Projective Space of dimension 2 over
             Multivariate Polynomial Ring in a, b over Rational Field
              Defn: Defined on coordinates by sending (x : y : z) to (x^2 : b*y^2 : z^2)

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(5)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem([w*x^2 + (1/5*w)*y^2, w*y^2])
            sage: f.normalize_coordinates(); f
            Dynamical System of Projective Space of dimension 1 over Number Field in w
             with defining polynomial x^2 - 5 with w = 2.236067977499790?
              Defn: Defined on coordinates by sending (x : y) to (5*x^2 + y^2 : 5*y^2)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<t> = PolynomialRing(ZZ)
            sage: K.<b> = NumberField(t^3 - 11)
            sage: a = 7/(b - 1)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([a*y^2 - (a*y - x)^2, y^2])
            sage: f.normalize_coordinates(); f
            Dynamical System of Projective Space of dimension 1 over
             Number Field in b with defining polynomial t^3 - 11
              Defn: Defined on coordinates by sending (x : y) to
                    (-100*x^2 + (140*b^2 + 140*b + 140)*x*y + (-77*b^2 - 567*b - 1057)*y^2
                     : 100*y^2)

        We can used ``ideal`` to scale with respect to a norm defined by an ideal::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem_projective([2*x^3, 2*x^2*y + 4*x*y^2])
            sage: f.normalize_coordinates(ideal=2); f
            Dynamical System of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to (x^3 : x^2*y + 2*x*y^2)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<w> = QQ[]
            sage: A.<a> = NumberField(w^2 + 1)
            sage: P.<x,y,z> = ProjectiveSpace(A, 2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: H = Hom(X, X)
            sage: f = H([(a+1)*x^3 + 2*x*y^2, 4*x*y^2, 8*x*z^2])
            sage: f.normalize_coordinates(ideal=A.prime_above(2)); f
            Scheme endomorphism of Closed subscheme of Projective Space of dimension 2 over
             Number Field in a with defining polynomial w^2 + 1 defined by: x^2 - y^2
              Defn: Defined on coordinates by sending (x : y : z) to
                    ((-a + 2)*x*y^2 : (-2*a + 2)*x*y^2 : (-4*a + 4)*x*z^2)

        We can pass in a valuation to ``valuation``::

            sage: g = H([(a+1)*x^3 + 2*x*y^2, 4*x*y^2, 8*x*z^2])                        # needs sage.rings.number_field
            sage: g.normalize_coordinates(valuation=A.valuation(A.prime_above(2)))      # needs sage.rings.number_field
            sage: g == f                                                                # needs sage.rings.number_field
            True

        ::

            sage: P.<x,y> = ProjectiveSpace(Qp(3), 1)                                   # needs sage.rings.padics
            sage: f = DynamicalSystem_projective([3*x^2 + 6*y^2, 9*x*y])                # needs sage.rings.padics
            sage: f.normalize_coordinates(); f                                          # needs sage.rings.padics
            Dynamical System of Projective Space of dimension 1 over
             3-adic Field with capped relative precision 20
              Defn: Defined on coordinates by sending (x : y) to
                    (x^2 + (2 + O(3^20))*y^2 : (3 + O(3^21))*x*y)

        Check that #35797 is fixed::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ[]
            sage: K.<a> = NumberField(3*x^2 + 1)
            sage: P.<z,w> = ProjectiveSpace(K, 1)
            sage: f = DynamicalSystem_projective([a*(z^2 + w^2), z*w])
            sage: f.normalize_coordinates(); f
            Dynamical System of Projective Space of dimension 1 over Number Field in a with defining polynomial 3*x^2 + 1
              Defn: Defined on coordinates by sending (z : w) to
                    (z^2 + w^2 : (-3*a)*z*w)

        ::

            sage: R.<a,b> = QQ[]
            sage: P.<x,y,z> = ProjectiveSpace(FractionField(R), 2)
            sage: H = End(P)
            sage: f = H([a/b*(x*z + y^2)*x^2, a*b*(x*z + y^2)*y^2, a*(x*z + y^2)*z^2])
            sage: f.normalize_coordinates(); f
            Scheme endomorphism of Projective Space of dimension 2 over Fraction
            Field of Multivariate Polynomial Ring in a, b over Rational Field
            Defn: Defined on coordinates by sending (x : y : z) to
                (x^2 : (b^2)*y^2 : b*z^2)
        """
    def degree(self):
        """
        Return the degree of this map.

        The degree is defined as the degree of the homogeneous
        polynomials that are the coordinates of this map.

        OUTPUT: positive integer

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([x^2 + y^2, y^2])
            sage: f.degree()
            2

        ::

            sage: # needs sage.rings.real_mpfr
            sage: P.<x,y,z> = ProjectiveSpace(CC, 2)
            sage: H = Hom(P, P)
            sage: f = H([x^3 + y^3, y^2*z, z*x*y])
            sage: f.degree()
            3

        ::

            sage: R.<t> = PolynomialRing(QQ)
            sage: P.<x,y,z> = ProjectiveSpace(R, 2)
            sage: H = Hom(P, P)
            sage: f = H([x^2 + t*y^2, (2-t)*y^2, z^2])
            sage: f.degree()
            2

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: H = Hom(X, X)
            sage: f = H([x^2, y^2, z^2])
            sage: f.degree()
            2
        """
    def dehomogenize(self, n):
        """
        Return the standard dehomogenization at the ``n[0]`` coordinate for the domain
        and the ``n[1]`` coordinate for the codomain.

        Note that the new function is defined over the fraction field
        of the base ring of this map.

        INPUT:

        - ``n`` -- tuple of nonnegative integers; if ``n`` is an integer, then
          the two values of the tuple are assumed to be the same

        OUTPUT: :class:`SchemeMorphism_polynomial_affine_space`

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(ZZ, 1)
            sage: H = Hom(P, P)
            sage: f = H([x^2 + y^2, y^2])
            sage: f.dehomogenize(0)
            Scheme endomorphism of Affine Space of dimension 1 over Integer Ring
              Defn: Defined on coordinates by sending (y) to (y^2/(y^2 + 1))

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([x^2 - y^2, y^2])
            sage: f.dehomogenize((0,1))
            Scheme morphism:
              From: Affine Space of dimension 1 over Rational Field
              To:   Affine Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (y) to ((-y^2 + 1)/y^2)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = Hom(P, P)
            sage: f = H([x^2 + y^2, y^2 - z^2, 2*z^2])
            sage: f.dehomogenize(2)
            Scheme endomorphism of Affine Space of dimension 2 over Rational Field
              Defn: Defined on coordinates by sending (x, y) to
                    (1/2*x^2 + 1/2*y^2, 1/2*y^2 - 1/2)

        ::

            sage: R.<t> = PolynomialRing(QQ)
            sage: P.<x,y,z> = ProjectiveSpace(FractionField(R),2)
            sage: H = Hom(P,P)
            sage: f = H([x^2 + t*y^2, t*y^2 - z^2, t*z^2])
            sage: f.dehomogenize(2)
            Scheme endomorphism of Affine Space of dimension 2 over Fraction Field
             of Univariate Polynomial Ring in t over Rational Field
              Defn: Defined on coordinates by sending (x, y) to
                    (1/t*x^2 + y^2, y^2 - 1/t)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: X = P.subscheme(x^2 - y^2)
            sage: H = Hom(X, X)
            sage: f = H([x^2, y^2, x*z])
            sage: f.dehomogenize(2)                                                     # needs sage.libs.singular
            Scheme endomorphism of Closed subscheme of Affine Space of dimension 2
             over Integer Ring defined by: x^2 - y^2
              Defn: Defined on coordinates by sending (x, y) to (x, y^2/x)

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = End(P)
            sage: f = H([x^2 - 2*x*y, y^2])
            sage: f.dehomogenize(0).homogenize(0) == f
            True

        ::

            sage: # needs sage.rings.number_field
            sage: K.<w> = QuadraticField(3)
            sage: O = K.ring_of_integers()
            sage: P.<x,y> = ProjectiveSpace(O, 1)
            sage: H = End(P)
            sage: f = H([x^2 - O(w)*y^2, y^2])
            sage: f.dehomogenize(1)
            Scheme endomorphism of Affine Space of dimension 1 over
             Maximal Order generated by w in Number Field in w with defining polynomial x^2 - 3
              with w = 1.732050807568878?
              Defn: Defined on coordinates by sending (x) to (x^2 - w)

        ::

            sage: P1.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P2.<u,v,w> = ProjectiveSpace(QQ, 2)
            sage: H = Hom(P2, P1)
            sage: f = H([u*w, v^2 + w^2])
            sage: f.dehomogenize((2,1))
            Scheme morphism:
              From: Affine Space of dimension 2 over Rational Field
              To:   Affine Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (u, v) to (u/(v^2 + 1))
        """
    @cached_method
    def is_morphism(self):
        """
        Return ``True`` if this map is a morphism.

        The map is a morphism if and only if the ideal generated by
        the defining polynomials is the unit ideal
        (no common zeros of the defining polynomials).

        OUTPUT: boolean

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([x^2 + y^2, y^2])
            sage: f.is_morphism()                                                       # needs sage.libs.singular
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(RR, 2)
            sage: H = Hom(P, P)
            sage: f = H([x*z - y*z, x^2 - y^2, z^2])
            sage: f.is_morphism()                                                       # needs sage.libs.singular
            False

        ::

            sage: R.<t> = PolynomialRing(GF(5))
            sage: P.<x,y,z> = ProjectiveSpace(R, 2)
            sage: H = Hom(P, P)
            sage: f = H([x*z - t*y^2, x^2 - y^2, t*z^2])
            sage: f.is_morphism()                                                       # needs sage.libs.singular
            True

        Map that is not morphism on projective space, but is over a subscheme::

            sage: P.<x,y,z> = ProjectiveSpace(RR, 2)
            sage: X = P.subscheme([x*y + y*z])
            sage: H = Hom(X, X)
            sage: f = H([x*z - y*z, x^2 - y^2, z^2])
            sage: f.is_morphism()                                                       # needs sage.libs.singular
            True
        """
    def global_height(self, prec=None):
        """
        Return the global height of the coefficients as a projective point.

        INPUT:

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([1/1331*x^2 + 1/4000*y^2, 210*x*y]);
            sage: f.global_height()                                                     # needs sage.symbolic
            20.8348429892146

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([1/1331*x^2 + 1/4000*y^2, 210*x*y]);
            sage: f.global_height(prec=11)                                              # needs sage.symbolic
            20.8

        ::

            sage: P.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: H = Hom(P, P)
            sage: f = H([4*x^2 + 100*y^2, 210*x*y, 10000*z^2]);
            sage: f.global_height()                                                     # needs sage.symbolic
            8.51719319141624

        ::

            sage: # needs sage.rings.number_field
            sage: R.<z> = PolynomialRing(QQ)
            sage: K.<w> = NumberField(z^2 - 2)
            sage: O = K.maximal_order()
            sage: P.<x,y> = ProjectiveSpace(O, 1)
            sage: H = Hom(P, P)
            sage: f = H([2*x^2 + 3*O(w)*y^2, O(w)*y^2])
            sage: f.global_height()
            1.09861228866811

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: P.<x,y> = ProjectiveSpace(QQbar, 1)
            sage: P2.<u,v,w> = ProjectiveSpace(QQbar, 2)
            sage: H = Hom(P, P2)
            sage: f = H([x^2 + QQbar(I)*x*y + 3*y^2, y^2, QQbar(sqrt(5))*x*y])
            sage: f.global_height()
            1.09861228866811

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: A.<z,w> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, A)
            sage: f = H([1/1331*x^2 + 4000*y*z, y^2])
            sage: f.global_height()                                                     # needs sage.symbolic
            15.4877354584971

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([1/25*x^2 + 25/3*x*y + y^2, 1*y^2])
            sage: exp(f.global_height())                                                # needs sage.symbolic
            625.000000000000

        Scaling should not change the result::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: f = DynamicalSystem([1/25*x^2 + 25/3*x*y + y^2, 1*y^2])
            sage: f.global_height()                                                     # needs sage.symbolic
            6.43775164973640
            sage: c = 10000
            sage: f.scale_by(c)
            sage: f.global_height()                                                     # needs sage.symbolic
            6.43775164973640
        """
    def local_height(self, v, prec=None):
        """
        Return the maximum of the local height of the coefficients in any
        of the coordinate functions of this map.

        INPUT:

        - ``v`` -- a prime or prime ideal of the base ring

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([1/1331*x^2 + 1/4000*y^2, 210*x*y])
            sage: f.local_height(1331)                                                  # needs sage.rings.real_mpfr
            7.19368581839511

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([1/1331*x^2 + 1/4000*y^2, 210*x*y])
            sage: f.local_height(1331, prec=2)                                          # needs sage.rings.real_mpfr
            8.0

        This function does not automatically normalize::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = Hom(P, P)
            sage: f = H([4*x^2 + 3/100*y^2, 8/210*x*y, 1/10000*z^2])
            sage: f.local_height(2)                                                     # needs sage.rings.real_mpfr
            2.77258872223978
            sage: f.normalize_coordinates()                                             # needs sage.libs.singular
            sage: f.local_height(2)                                                     # needs sage.libs.singular
            0.000000000000000

        ::

            sage: # needs sage.rings.number_field
            sage: R.<z> = PolynomialRing(QQ)
            sage: K.<w> = NumberField(z^2 - 2)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: H = Hom(P, P)
            sage: f = H([2*x^2 + w/3*y^2, 1/w*y^2])
            sage: f.local_height(K.ideal(3))
            1.09861228866811
        """
    def local_height_arch(self, i, prec=None):
        """
        Return the maximum of the local height at the ``i``-th infinite place of the coefficients in any
        of the coordinate functions of this map.

        INPUT:

        - ``i`` -- integer

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([1/1331*x^2 + 1/4000*y^2, 210*x*y])
            sage: f.local_height_arch(0)                                                # needs sage.rings.real_mpfr
            5.34710753071747

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = Hom(P, P)
            sage: f = H([1/1331*x^2 + 1/4000*y^2, 210*x*y])
            sage: f.local_height_arch(0, prec=5)                                        # needs sage.rings.real_mpfr
            5.2

        ::

            sage: # needs sage.rings.number_field
            sage: R.<z> = PolynomialRing(QQ)
            sage: K.<w> = NumberField(z^2 - 2)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: H = Hom(P, P)
            sage: f = H([2*x^2 + w/3*y^2, 1/w*y^2])
            sage: f.local_height_arch(1)
            0.6931471805599453094172321214582
        """
    def wronskian_ideal(self):
        """
        Return the ideal generated by the critical point locus.

        This is the vanishing of the maximal minors of the Jacobian matrix.
        Not implemented for subvarieties.

        OUTPUT: an ideal in the coordinate ring of the domain of this map

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<w> = NumberField(x^2 + 11)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: H = End(P)
            sage: f = H([x^2 - w*y^2, w*y^2])
            sage: f.wronskian_ideal()
            Ideal ((4*w)*x*y) of Multivariate Polynomial Ring in x, y
             over Number Field in w with defining polynomial x^2 + 11

        ::

            sage: # needs sage.rings.number_field
            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P2.<u,v,t> = ProjectiveSpace(K, 2)
            sage: H = Hom(P, P2)
            sage: f = H([x^2 - 2*y^2, y^2, x*y])
            sage: f.wronskian_ideal()
            Ideal (4*x*y, 2*x^2 + 4*y^2, -2*y^2) of
             Multivariate Polynomial Ring in x, y over Rational Field
        """

class SchemeMorphism_polynomial_projective_space_field(SchemeMorphism_polynomial_projective_space):
    def rational_preimages(self, Q, k: int = 1):
        """
        Determine all of the rational `k`-th preimages of ``Q`` by this map.

        Given a rational point ``Q`` in the domain of this map, return all the rational points ``P``
        in the domain with `f^k(P)==Q`. In other words, the set of `k`-th preimages of ``Q``.
        The map must be defined over a number field and be an endomorphism for `k > 1`.

        If ``Q`` is a subscheme, then return the subscheme that maps to ``Q`` by this map.
        In particular, `f^{-k}(V(h_1,\\ldots,h_t)) = V(h_1 \\circ f^k, \\ldots, h_t \\circ f^k)`.

        INPUT:

        - ``Q`` -- a rational point or subscheme in the domain of this map

        - ``k`` -- positive integer

        OUTPUT: a list of rational points or a subscheme in the domain of this map

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = End(P)
            sage: f = H([16*x^2 - 29*y^2, 16*y^2])
            sage: f.rational_preimages(P(-1, 4))                                        # needs sage.libs.singular
            [(-5/4 : 1), (5/4 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = End(P)
            sage: f = H([76*x^2 - 180*x*y + 45*y^2 + 14*x*z + 45*y*z - 90*z^2,
            ....:        67*x^2 - 180*x*y - 157*x*z + 90*y*z,
            ....:        -90*z^2])
            sage: f.rational_preimages(P(-9, -4, 1))                                    # needs sage.libs.singular
            [(0 : 4 : 1)]

        A non-periodic example ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = End(P)
            sage: f = H([x^2 + y^2, 2*x*y])
            sage: f.rational_preimages(P(17, 15))                                       # needs sage.libs.singular
            [(3/5 : 1), (5/3 : 1)]

        ::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: H = End(P)
            sage: f = H([x^2 - 2*y*w - 3*w^2, -2*x^2 + y^2 - 2*x*z + 4*y*w + 3*w^2,
            ....:        x^2 - y^2 + 2*x*z + z^2 - 2*y*w - w^2,
            ....:        w^2])
            sage: f.rational_preimages(P(0, -1, 0, 1))                                  # needs sage.libs.singular
            []

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = End(P)
            sage: f = H([x^2 + y^2, 2*x*y])
            sage: f.rational_preimages([CC.0, 1])                                       # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            TypeError: point must be in codomain of self

        A number field example ::

            sage: # needs sage.rings.number_field
            sage: z = QQ['z'].0
            sage: K.<a> = NumberField(z^2 - 2)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: H = End(P)
            sage: f = H([x^2 + y^2, y^2])
            sage: f.rational_preimages(P(3, 1))                                         # needs sage.libs.singular
            [(-a : 1), (a : 1)]

        ::

            sage: # needs sage.rings.number_field
            sage: z = QQ['z'].0
            sage: K.<a> = NumberField(z^2 - 2)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: X = P.subscheme([x^2 - z^2])
            sage: H = End(X)
            sage: f= H([x^2 - z^2, a*y^2, z^2 - x^2])
            sage: f.rational_preimages(X([1, 2, -1]))                                   # needs sage.libs.singular
            []

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme([x^2 - z^2])
            sage: H = End(X)
            sage: f = H([x^2-z^2, y^2, z^2-x^2])
            sage: f.rational_preimages(X([0, 1, 0]))                                    # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x^2 - z^2,
              -x^2 + z^2,
              0,
              -x^2 + z^2

        ::

            sage: P.<x, y> = ProjectiveSpace(QQ, 1)
            sage: H = End(P)
            sage: f = H([x^2 - y^2, y^2])
            sage: f.rational_preimages(P.subscheme([x]))                                # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 1 over Rational Field
             defined by: x^2 - y^2

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: H = End(P)
            sage: f = H([x^2 - 29/16*y^2, y^2])
            sage: f.rational_preimages(P(5/4, 1), k=4)                                  # needs sage.libs.singular
            [(-3/4 : 1), (3/4 : 1), (-7/4 : 1), (7/4 : 1)]

        ::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P2.<u,v,w> = ProjectiveSpace(QQ, 2)
            sage: H = Hom(P, P2)
            sage: f = H([x^2, y^2, x^2-y^2])
            sage: f.rational_preimages(P2(1, 1, 0))                                     # needs sage.libs.singular
            [(-1 : 1), (1 : 1)]
        """
    def base_indeterminacy_locus(self):
        """
        Return the base indeterminacy locus of this map.

        The base indeterminacy locus is the set of points in projective space
        at which all of the defining polynomials of the rational map
        simultaneously vanish.

        OUTPUT: a subscheme of the domain of the map

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = End(P)
            sage: f = H([x*z - y*z, x^2 - y^2, z^2])
            sage: f.base_indeterminacy_locus()
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x*z - y*z,
              x^2 - y^2,
              z^2

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = End(P)
            sage: f = H([x^2, y^2, z^2])
            sage: f.base_indeterminacy_locus()
            Closed subscheme of Projective Space of dimension 2 over Rational Field
             defined by:
              x^2,
              y^2,
              z^2

        ::

            sage: P1.<x,y,z> = ProjectiveSpace(RR, 2)
            sage: P2.<t,u,v,w> = ProjectiveSpace(RR, 3)
            sage: H = Hom(P1, P2)
            sage: h = H([y^3*z^3, x^3*z^3, y^3*z^3, x^2*y^2*z^2])
            sage: h.base_indeterminacy_locus()                                          # needs sage.rings.real_mpfr
            Closed subscheme of Projective Space of dimension 2 over
             Real Field with 53 bits of precision defined by:
              y^3*z^3,
              x^3*z^3,
              y^3*z^3,
              x^2*y^2*z^2

        If defining polynomials are not normalized, output scheme will not be normalized::

            sage: P.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: H = End(P)
            sage: f = H([x*x^2,x*y^2,x*z^2])
            sage: f.base_indeterminacy_locus()
            Closed subscheme of Projective Space of dimension 2 over Rational Field
             defined by:
              x^3,
              x*y^2,
              x*z^2
        """
    def indeterminacy_locus(self):
        """
        Return the indeterminacy locus of this map as a rational map on the domain.

        The indeterminacy locus is the intersection of all the base indeterminacy
        locuses of maps that define the same rational map as by this map.

        OUTPUT: a subscheme of the domain of the map

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = End(P)
            sage: f = H([x^2, y^2, z^2])
            sage: f.indeterminacy_locus()                                               # needs sage.libs.singular
            ... DeprecationWarning: The meaning of indeterminacy_locus() has changed.
            Read the docstring. See https://github.com/sagemath/sage/issues/29145 for details.
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              z,
              y,
              x

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = End(P)
            sage: f = H([x*z - y*z, x^2 - y^2, z^2])
            sage: f.indeterminacy_locus()                                               # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              z,
              x^2 - y^2

        There is related :meth:`base_indeterminacy_locus()` method. This
        computes the indeterminacy locus only from the defining polynomials of
        the map::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = End(P)
            sage: f = H([x*z - y*z, x^2 - y^2, z^2])
            sage: f.base_indeterminacy_locus()
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x*z - y*z,
              x^2 - y^2,
              z^2
        """
    def indeterminacy_points(self, F=None, base: bool = False):
        """
        Return the points in the indeterminacy locus of this map.

        If the dimension of the indeterminacy locus is not zero, an error is raised.

        INPUT:

        - ``F`` -- a field; if not given, the base ring of the domain is assumed

        - ``base`` -- if ``True``, the base indeterminacy locus is used

        OUTPUT: indeterminacy points of the map defined over ``F``

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = End(P)
            sage: f = H([x*z - y*z, x^2 - y^2, z^2])
            sage: f.indeterminacy_points()                                              # needs sage.libs.singular
            ... DeprecationWarning: The meaning of indeterminacy_locus() has changed.
            Read the docstring. See https://github.com/sagemath/sage/issues/29145 for details.
            [(-1 : 1 : 0), (1 : 1 : 0)]

        ::

            sage: P1.<x,y,z> = ProjectiveSpace(RR, 2)
            sage: P2.<t,u,v,w> = ProjectiveSpace(RR, 3)
            sage: H = Hom(P1, P2)
            sage: h = H([x + y, y, z + y, y])
            sage: set_verbose(None)
            sage: h.indeterminacy_points(base=True)                                     # needs sage.libs.singular
            []
            sage: g = H([y^3*z^3, x^3*z^3, y^3*z^3, x^2*y^2*z^2])
            sage: g.indeterminacy_points(base=True)                                     # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ValueError: indeterminacy scheme is not dimension 0

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: H = End(P)
            sage: f = H([x^2 + y^2, x*z, x^2 + y^2])
            sage: f.indeterminacy_points()                                              # needs sage.libs.singular
            [(0 : 0 : 1)]

            sage: R.<t> = QQ[]
            sage: K.<a> = NumberField(t^2 + 1)                                          # needs sage.rings.number_field
            sage: f.indeterminacy_points(F=K)                                           # needs sage.libs.singular sage.rings.number_field
            [(-a : 1 : 0), (0 : 0 : 1), (a : 1 : 0)]
            sage: set_verbose(None)
            sage: f.indeterminacy_points(F=QQbar, base=True)                            # needs sage.libs.singular sage.rings.number_field
            [(-1*I : 1 : 0), (0 : 0 : 1), (1*I : 1 : 0)]

        ::

            sage: set_verbose(None)
            sage: K.<t> = FunctionField(QQ)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: H = End(P)
            sage: f = H([x^2 - t^2*y^2, y^2 - z^2, x^2 - t^2*z^2])
            sage: f.indeterminacy_points(base=True)                                     # needs sage.libs.singular
            [(-t : -1 : 1), (-t : 1 : 1), (t : -1 : 1), (t : 1 : 1)]

        ::

            sage: # needs sage.rings.padics
            sage: set_verbose(None)
            sage: P.<x,y,z> = ProjectiveSpace(Qp(3), 2)
            sage: H = End(P)
            sage: f = H([x^2 - 7*y^2, y^2 - z^2, x^2 - 7*z^2])
            sage: f.indeterminacy_points(base=True)                                     # needs sage.libs.singular
            [(2 + 3 + 3^2 + 2*3^3 + 2*3^5 + 2*3^6 + 3^8
                + 3^9 + 2*3^11 + 3^15 + 2*3^16 + 3^18 + O(3^20) : 1 + O(3^20) : 1 + O(3^20)),
             (2 + 3 + 3^2 + 2*3^3 + 2*3^5 + 2*3^6 + 3^8 + 3^9 + 2*3^11 + 3^15
                + 2*3^16 + 3^18 + O(3^20) : 2 + 2*3 + 2*3^2 + 2*3^3 + 2*3^4 + 2*3^5
                + 2*3^6 + 2*3^7 + 2*3^8 + 2*3^9 + 2*3^10 + 2*3^11 + 2*3^12 + 2*3^13
                + 2*3^14 + 2*3^15 + 2*3^16 + 2*3^17 + 2*3^18 + 2*3^19 + O(3^20) : 1 + O(3^20)),
             (1 + 3 + 3^2 + 2*3^4 + 2*3^7 + 3^8 + 3^9 + 2*3^10 + 2*3^12 + 2*3^13
                + 2*3^14 + 3^15 + 2*3^17 + 3^18 + 2*3^19 + O(3^20) : 1 + O(3^20) : 1 + O(3^20)),
             (1 + 3 + 3^2 + 2*3^4 + 2*3^7 + 3^8 + 3^9 + 2*3^10 + 2*3^12 + 2*3^13
                + 2*3^14 + 3^15 + 2*3^17 + 3^18 + 2*3^19 + O(3^20) : 2 + 2*3 + 2*3^2
                + 2*3^3 + 2*3^4 + 2*3^5 + 2*3^6 + 2*3^7 + 2*3^8 + 2*3^9 + 2*3^10 + 2*3^11
                + 2*3^12 + 2*3^13 + 2*3^14 + 2*3^15 + 2*3^16 + 2*3^17 + 2*3^18 + 2*3^19
                + O(3^20) : 1 + O(3^20))]
        """
    def reduce_base_field(self):
        """
        Return this map defined over the field of definition of the coefficients.

        The base field of the map could be strictly larger than
        the field where all of the coefficients are defined. This function
        reduces the base field to the minimal possible. This can be done when
        the base ring is a number field, QQbar, a finite field, or algebraic
        closure of a finite field.

        OUTPUT: a scheme morphism

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<t> = GF(3^4)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: P2.<a,b,c> = ProjectiveSpace(K, 2)
            sage: H = End(P)
            sage: H2 = Hom(P, P2)
            sage: H3 = Hom(P2, P)
            sage: f = H([x^2 + (2*t^3 + 2*t^2 + 1)*y^2, y^2])
            sage: f.reduce_base_field()                                                 # needs sage.libs.singular sage.modules
            Scheme endomorphism of Projective Space of dimension 1
             over Finite Field in t2 of size 3^2
              Defn: Defined on coordinates by sending (x : y) to (x^2 + t2*y^2 : y^2)
            sage: f2 = H2([x^2 + 5*y^2, y^2, 2*x*y])
            sage: f2.reduce_base_field()                                                # needs sage.libs.singular sage.modules
            Scheme morphism:
              From: Projective Space of dimension 1 over Finite Field of size 3
              To:   Projective Space of dimension 2 over Finite Field of size 3
              Defn: Defined on coordinates by sending (x : y) to (x^2 - y^2 : y^2 : -x*y)
            sage: f3 = H3([a^2 + t*b^2, c^2])
            sage: f3.reduce_base_field()                                                # needs sage.libs.singular sage.modules
            Scheme morphism:
              From: Projective Space of dimension 2 over Finite Field in t of size 3^4
              To:   Projective Space of dimension 1 over Finite Field in t of size 3^4
              Defn: Defined on coordinates by sending (a : b : c) to (a^2 + t*b^2 : c^2)

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = CyclotomicField(4)
            sage: P.<x,y> = ProjectiveSpace(K, 1)
            sage: H = End(P)
            sage: f = H([x^2 + 2*y^2, y^2])
            sage: f.reduce_base_field()                                                 # needs sage.libs.singular
            Scheme endomorphism of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y) to (x^2 + 2*y^2 : y^2)

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<v> = GF(5)
            sage: L = K.algebraic_closure()
            sage: P.<x,y> = ProjectiveSpace(L, 1)
            sage: H = End(P)
            sage: f = H([(L.gen(2))*x^2 + L.gen(4)*y^2, x*y])
            sage: f.reduce_base_field()                                                 # needs sage.libs.singular
            Scheme endomorphism of Projective Space of dimension 1
             over Finite Field in z4 of size 5^4
              Defn: Defined on coordinates by sending (x : y) to
                    ((z4^3 + z4^2 + z4 - 2)*x^2 + z4*y^2 : x*y)
            sage: f = DynamicalSystem_projective([L.gen(3)*x^2 + L.gen(2)*y^2, x*y])    # needs sage.schemes
            sage: f.reduce_base_field()                                                 # needs sage.libs.singular sage.schemes
            Dynamical System of Projective Space of dimension 1
             over Finite Field in z6 of size 5^6
              Defn: Defined on coordinates by sending (x : y) to
                    ((-z6^5 + z6^4 - z6^3 - z6^2 - 2*z6 - 2)*x^2
                     + (z6^5 - 2*z6^4 + z6^2 - z6 + 1)*y^2 : x*y)

        TESTS::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(3).algebraic_closure()
            sage: P.<x,y> = ProjectiveSpace(F, 1)
            sage: H = Hom(P, P)
            sage: f = H([x^2 + y^2, y^2])
            sage: f.reduce_base_field()                                                 # needs sage.libs.singular
            Scheme endomorphism of Projective Space of dimension 1 over Finite Field of size 3
              Defn: Defined on coordinates by sending (x : y) to
                    (x^2 + y^2 : y^2)
        """
    def image(self):
        """
        Return the scheme-theoretic image of the morphism.

        OUTPUT: a subscheme of the ambient space of the codomain

        EXAMPLES::

            sage: P2.<x0,x1,x2> = ProjectiveSpace(QQ, 2)
            sage: f = P2.hom([x0^3, x0^2*x1, x0*x1^2], P2)
            sage: f.image()                                                             # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x1^2 - x0*x2
            sage: f = P2.hom([x0 - x1, x0 - x2, x1 - x2], P2)
            sage: f.image()                                                             # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x0 - x1 + x2

        ::

            sage: P2.<x0,x1,x2> = ProjectiveSpace(QQ, 2)
            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: f = P2.hom([1, x0/x1], A2)
            sage: f.image()                                                             # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              -x + 1
        """

class SchemeMorphism_polynomial_projective_space_finite_field(SchemeMorphism_polynomial_projective_space_field): ...

class SchemeMorphism_polynomial_projective_subscheme_field(SchemeMorphism_polynomial_projective_space_field):
    """
    Morphisms from subschemes of projective spaces defined over fields.
    """
    def __call__(self, x):
        """
        Apply this morphism to the point ``x``.

        INPUT:

        - ``x`` -- a point in the domain of definition

        OUTPUT: the image of the point ``x`` under the morphism

        TESTS::

            sage: # needs sage.libs.pari sage.schemes
            sage: R.<x,y,z> = QQ[]
            sage: C = Curve(7*x^2 + 2*y*z + z^2)
            sage: f, g = C.parametrization()
            sage: g([0, -1, 2])
            (1 : 0)
            sage: f([1, 0])
            (0 : -1/2 : 1)
            sage: _ == C([0, -1, 2])
            True
        """
    def __eq__(self, other):
        """
        EXAMPLES::

            sage: R.<x,y,z> = QQ[]

            sage: # needs sage.libs.pari sage.schemes
            sage: C = Curve(7*x^2 + 2*y*z + z^2)  # conic
            sage: f, g = C.parametrization()
            sage: f*g == C.identity_morphism()
            True

            sage: # needs sage.schemes
            sage: C = Curve(x^2 + y^2 - z^2)
            sage: P.<u, v> = ProjectiveSpace(QQ, 1)
            sage: f = C.hom([x + z, y], P)
            sage: g = C.hom([y, z - x], P)
            sage: f == g
            True
            sage: h = C.hom([z, x - y], P)
            sage: f == h
            False
        """
    @cached_method
    def representatives(self):
        """
        Return all maps representing the same rational map as by this map.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P2.subscheme(0)
            sage: f = X.hom([x^2*y, x^2*z, x*y*z], P2)
            sage: f.representatives()                                                   # needs sage.libs.singular
            [Scheme morphism:
               From: Closed subscheme of Projective Space of dimension 2
                     over Rational Field defined by: 0
               To:   Projective Space of dimension 2 over Rational Field
               Defn: Defined on coordinates by sending (x : y : z) to (x*y : x*z : y*z)]

        ::

            sage: P2.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: P1.<a,b> = ProjectiveSpace(QQ, 1)
            sage: X = P2.subscheme([x^2 - y^2 - y*z])
            sage: f = X.hom([x, y], P1)
            sage: f.representatives()                                                   # needs sage.libs.singular
            [Scheme morphism:
               From: Closed subscheme of Projective Space of dimension 2
                     over Rational Field defined by: x^2 - y^2 - y*z
               To:   Projective Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x : y : z) to (y + z : x),
             Scheme morphism:
               From: Closed subscheme of Projective Space of dimension 2
                     over Rational Field defined by: x^2 - y^2 - y*z
               To:   Projective Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x : y : z) to (x : y)]
            sage: g = _[0]                                                              # needs sage.libs.singular
            sage: g.representatives()                                                   # needs sage.libs.singular
            [Scheme morphism:
               From: Closed subscheme of Projective Space of dimension 2
                     over Rational Field defined by: x^2 - y^2 - y*z
               To:   Projective Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x : y : z) to (y + z : x),
             Scheme morphism:
               From: Closed subscheme of Projective Space of dimension 2
                     over Rational Field defined by: x^2 - y^2 - y*z
               To:   Projective Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x : y : z) to (x : y)]

        ::

            sage: P2.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P2.subscheme([x^2 - y^2 - y*z])
            sage: A1.<a> = AffineSpace(QQ, 1)
            sage: g = X.hom([y/x], A1)
            sage: g.representatives()                                                   # needs sage.libs.singular
            [Scheme morphism:
               From: Closed subscheme of Projective Space of dimension 2
                     over Rational Field defined by: x^2 - y^2 - y*z
               To:   Affine Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x : y : z) to (x/(y + z)),
             Scheme morphism:
               From: Closed subscheme of Projective Space of dimension 2
                     over Rational Field defined by: x^2 - y^2 - y*z
               To:   Affine Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x : y : z) to (y/x)]
            sage: g0, g1 = _                                                            # needs sage.libs.singular
            sage: emb = A1.projective_embedding(0)
            sage: emb*g0                                                                # needs sage.libs.singular
            Scheme morphism:
              From: Closed subscheme of Projective Space of dimension 2
                    over Rational Field defined by: x^2 - y^2 - y*z
              To:   Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y : z) to (y + z : x)
            sage: emb*g1                                                                # needs sage.libs.singular
            Scheme morphism:
              From: Closed subscheme of Projective Space of dimension 2
                    over Rational Field defined by: x^2 - y^2 - y*z
              To:   Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x : y : z) to (x : y)

        ALGORITHM:

        The algorithm is from Proposition 1.1 in [Sim2004]_.
        """
    def indeterminacy_locus(self):
        """
        Return the indeterminacy locus of this map.

        The map defines a rational map on the domain. The output is the
        subscheme of the domain on which the rational map is not defined by any
        representative of the rational map. See :meth:`representatives()`.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P2.<x0,x1,x2> = ProjectiveSpace(QQ, 2)
            sage: X = P2.subscheme(0)
            sage: f = X.hom([x1,x0], P)
            sage: L = f.indeterminacy_locus()                                           # needs sage.libs.singular
            sage: L.rational_points()                                                   # needs sage.libs.singular
            [(0 : 0 : 1)]

        ::

            sage: P2.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: P1.<a,b> = ProjectiveSpace(QQ, 1)
            sage: X = P2.subscheme([x^2 - y^2 - y*z])
            sage: f = X.hom([x,y], P1)
            sage: f.indeterminacy_locus()                                               # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              z,
              y,
              x

        ::

            sage: P3.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: P2.<a,b,c> = ProjectiveSpace(QQ, 2)
            sage: X = P3.subscheme(x^2 - w*y - x*z)
            sage: f = X.hom([x*y, y*z, z*x], P2)
            sage: L = f.indeterminacy_locus()                                           # needs sage.libs.singular
            sage: L.dimension()                                                         # needs sage.libs.singular
            0
            sage: L.degree()                                                            # needs sage.libs.singular
            2
            sage: L.rational_points()                                                   # needs sage.libs.singular
            [(0 : 0 : 0 : 1), (0 : 1 : 0 : 0)]

        ::

            sage: P3.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: A2.<a,b> = AffineSpace(QQ, 2)
            sage: X = P3.subscheme(x^2 - w*y - x*z)
            sage: f = X.hom([x/z, y/x], A2)
            sage: L = f.indeterminacy_locus()                                           # needs sage.libs.singular
            sage: L.rational_points()                                                   # needs sage.libs.singular
            [(0 : 0 : 0 : 1), (0 : 1 : 0 : 0)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: X = P.subscheme(x - y)
            sage: H = End(X)
            sage: f = H([x^2 - 4*y^2, y^2 - z^2, 4*z^2 - x^2])
            sage: Z = f.indeterminacy_locus(); Z                                        # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              z,
              y,
              x
        """
    def is_morphism(self):
        """
        Return ``True`` if the map is defined everywhere on the domain.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: P1.<a,b> = ProjectiveSpace(QQ, 1)
            sage: X = P2.subscheme([x^2 - y^2 - y*z])
            sage: f = X.hom([x,y], P1)
            sage: f.is_morphism()                                                       # needs sage.libs.singular
            True
        """
    def image(self):
        """
        Return the scheme-theoretic image of the morphism.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P2.<x0,x1,x2> = ProjectiveSpace(QQ, 2)
            sage: X = P2.subscheme(0)
            sage: f = X.hom([x1,x0], P)
            sage: f.image()                                                             # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 1 over Rational Field defined by:
              (no polynomials)

        ::

            sage: P2.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: X = P2.subscheme([z^3 - x*y^2 + y^3])
            sage: f = X.hom([x*z, x*y, x^2 + y*z], P2)
            sage: f.image()                                                             # needs sage.libs.singular
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x^6 + 2*x^3*y^3 + x*y^5 + y^6 - x^3*y^2*z - y^5*z
        """
    @cached_method
    def graph(self):
        """
        Return the graph of this morphism.

        The graph is a subscheme of the product of the ambient spaces of the
        domain and the codomain. If the ambient space of the codomain is an
        affine space, it is first embedded into a projective space.

        EXAMPLES:

        We get the standard quadratic curve as the graph of a quadratic function
        of an affine line. ::

            sage: A1.<x> = AffineSpace(1, QQ)
            sage: X = A1.subscheme(0)  # affine line
            sage: phi = X.hom([x^2], A1)
            sage: mor = phi.homogenize(0)                                               # needs sage.libs.singular
            sage: G = mor.graph(); G                                                    # needs sage.libs.singular
            Closed subscheme of Product of projective spaces P^1 x P^1
              over Rational Field defined by: x1^2*x2 - x0^2*x3
            sage: G.affine_patch([0, 0])                                                # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2
              over Rational Field defined by: x0^2 - x1
        """
    @cached_method
    def projective_degrees(self):
        """
        Return the projective degrees of this rational map.

        EXAMPLES::

            sage: # needs sage.schemes
            sage: k = GF(11)
            sage: E = EllipticCurve(k, [1,1])
            sage: Q = E(6, 5)
            sage: phi = E.scalar_multiplication(2)
            sage: mor = phi.as_morphism()
            sage: mor.projective_degrees()
            (12, 3)
        """
    def degree(self):
        """
        Return the degree of this rational map.

        EXAMPLES::

            sage: # needs sage.schemes
            sage: k = GF(11)
            sage: E = EllipticCurve(k, [1,1])
            sage: Q = E(6, 5)
            sage: phi = E.scalar_multiplication(2)
            sage: mor = phi.as_morphism()
            sage: mor.degree()
            4
        """
