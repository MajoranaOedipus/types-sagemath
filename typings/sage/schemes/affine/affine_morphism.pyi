from sage.categories.fields import Fields as Fields
from sage.categories.homset import End as End, Hom as Hom
from sage.categories.number_fields import NumberFields as NumberFields
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.misc_c import prod as prod
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.schemes.generic.morphism import SchemeMorphism_polynomial as SchemeMorphism_polynomial

class SchemeMorphism_polynomial_affine_space(SchemeMorphism_polynomial):
    """
    A morphism of schemes determined by rational functions.

    EXAMPLES::

        sage: RA.<x,y> = QQ[]
        sage: A2 = AffineSpace(RA)
        sage: RP.<u,v,w> = QQ[]
        sage: P2 = ProjectiveSpace(RP)
        sage: H = A2.Hom(P2)
        sage: f = H([x, y, 1])
        sage: f
        Scheme morphism:
          From: Affine Space of dimension 2 over Rational Field
          To:   Projective Space of dimension 2 over Rational Field
          Defn: Defined on coordinates by sending (x, y) to (x : y : 1)
    """
    def __init__(self, parent, polys, check: bool = True) -> None:
        """
        Initialize.

        INPUT:

        - ``parent`` -- Hom

        - ``polys`` -- list or tuple of polynomials or rational functions

        - ``check`` -- boolean

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(ZZ, 2)
            sage: H = Hom(A, A)
            sage: H([3/5*x^2, y^2/(2*x^2)])
            Scheme endomorphism of Affine Space of dimension 2 over Integer Ring
              Defn: Defined on coordinates by sending (x, y) to
                    (3*x^2/5, y^2/(2*x^2))

        ::

            sage: A.<x,y> = AffineSpace(ZZ, 2)
            sage: H = Hom(A, A)
            sage: H([3*x^2/(5*y), y^2/(2*x^2)])
            Scheme endomorphism of Affine Space of dimension 2 over Integer Ring
              Defn: Defined on coordinates by sending (x, y) to
                    (3*x^2/(5*y), y^2/(2*x^2))

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: H = Hom(A, A)
            sage: H([3/2*x^2, y^2])
            Scheme endomorphism of Affine Space of dimension 2 over Rational Field
              Defn: Defined on coordinates by sending (x, y) to (3/2*x^2, y^2)

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: X = A.subscheme([x - y^2])
            sage: H = Hom(X, X)
            sage: H([9/4*x^2, 3/2*y])
            Scheme endomorphism of Closed subscheme of Affine Space of dimension 2
             over Rational Field defined by: -y^2 + x
              Defn: Defined on coordinates by sending (x, y) to (9/4*x^2, 3/2*y)

            sage: P.<x,y,z> = ProjectiveSpace(ZZ, 2)
            sage: H = Hom(P, P)
            sage: f = H([5*x^3 + 3*x*y^2-y^3, 3*z^3 + y*x^2, x^3-z^3])
            sage: f.dehomogenize(2)
            Scheme endomorphism of Affine Space of dimension 2 over Integer Ring
              Defn: Defined on coordinates by sending (x, y) to
                    ((5*x^3 + 3*x*y^2 - y^3)/(x^3 - 1), (x^2*y + 3)/(x^3 - 1))

        If you pass in quotient ring elements, they are reduced::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: X = A.subscheme([x - y])
            sage: H = Hom(X, X)
            sage: u,v,w = X.coordinate_ring().gens()                                    # needs sage.libs.singular
            sage: H([u, v, u + v])                                                      # needs sage.libs.singular
            Scheme endomorphism of Closed subscheme of Affine Space of dimension 3
             over Rational Field defined by: x - y
              Defn: Defined on coordinates by sending (x, y, z) to (y, y, 2*y)

        You must use the ambient space variables to create rational functions::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: X = A.subscheme([x^2 - y^2])
            sage: H = Hom(X, X)
            sage: u,v,w = X.coordinate_ring().gens()                                    # needs sage.libs.singular
            sage: H([u, v, (u+1)/v])                                                    # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: Division failed. The numerator is not a multiple of the denominator.
            sage: H([x, y, (x+1)/y])
            Scheme endomorphism of Closed subscheme of Affine Space of dimension 3
             over Rational Field defined by:
              x^2 - y^2
              Defn: Defined on coordinates by sending (x, y, z) to
                    (x, y, (x + 1)/y)

            ::

            sage: R.<t> = PolynomialRing(QQ)
            sage: A.<x,y,z> = AffineSpace(R, 3)
            sage: X = A.subscheme(x^2 - y^2)
            sage: H = End(X)
            sage: H([x^2/(t*y), t*y^2, x*z])
            Scheme endomorphism of Closed subscheme of Affine Space of dimension 3
             over Univariate Polynomial Ring in t over Rational Field defined by:
              x^2 - y^2
              Defn: Defined on coordinates by sending (x, y, z) to
                    (x^2/(t*y), t*y^2, x*z)
        """
    def __call__(self, x, check: bool = True):
        """
        Evaluate affine morphism at point described by ``x``.

        EXAMPLES::

            sage: P.<x,y,z> = AffineSpace(QQ, 3)
            sage: H = Hom(P, P)
            sage: f = H([x^2 + y^2, y^2, z^2 + y*z])
            sage: f(P([1, 1, 1]))
            (2, 1, 2)

        TESTS:

        Check that :issue:`32209` is fixed::

            sage: S.<x,y> = AffineSpace(ZZ, 2)
            sage: T.<u,v> = AffineSpace(ZZ, 2)
            sage: h = T.hom([u + v, u*v], S); h
            Scheme morphism:
              From: Affine Space of dimension 2 over Integer Ring
              To:   Affine Space of dimension 2 over Integer Ring
              Defn: Defined on coordinates by sending (u, v) to
                    (u + v, u*v)

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(4)
            sage: P = T(F)(1, a)
            sage: h(P)
            (a + 1, a)
            sage: h(P).domain()
            Spectrum of Finite Field in a of size 2^2
            sage: h.change_ring(F)(P)
            (a + 1, a)
        """
    def __eq__(self, right):
        """
        Test the equality of two affine maps.

        INPUT:

        - ``right`` -- a map on affine space

        OUTPUT: ``True`` if the two affine maps define the same map

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: A2.<u,v> = AffineSpace(QQ, 2)
            sage: H = End(A)
            sage: H2 = End(A2)
            sage: f = H([x^2 - 2*x*y, y/(x+1)])
            sage: g = H2([u^3 - v, v^2])
            sage: f == g
            False

        ::

            sage: # needs sage.rings.real_mpfr
            sage: A.<x,y,z> = AffineSpace(CC, 3)
            sage: H = End(A)
            sage: f = H([x^2 - CC.0*x*y + z*x, 1/z^2 - y^2, 5*x])
            sage: f == f
            True
        """
    def __ne__(self, right):
        """
        Test the inequality of two affine maps.

        INPUT:

        - ``right`` -- a map on affine space

        OUTPUT: ``True`` if the two affine maps define the same map

        EXAMPLES::

            sage: # needs sage.rings.real_mpfr
            sage: A.<x,y> = AffineSpace(RR, 2)
            sage: H = End(A)
            sage: f = H([x^2 - y, y^2])
            sage: g = H([x^3 - x*y, x*y^2])
            sage: f != g
            True
            sage: f != f
            False
        """
    def homogenize(self, n):
        """
        Return the homogenization of this map.

        If it's domain is a subscheme, the domain of the homogenized map is the
        projective embedding of the domain. The domain and codomain can be
        homogenized at different coordinates: ``n[0]`` for the domain and
        ``n[1]`` for the codomain.

        INPUT:

        - ``n`` -- tuple of nonnegative integers; if ``n`` is an integer,
          then the two values of the tuple are assumed to be the same

        OUTPUT: a morphism from the projective embedding of the domain of this map

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(ZZ, 2)
            sage: H = Hom(A, A)
            sage: f = H([(x^2-2)/x^5, y^2])
            sage: f.homogenize(2)
            Scheme endomorphism of Projective Space of dimension 2 over Integer Ring
              Defn: Defined on coordinates by sending (x0 : x1 : x2) to
                    (x0^2*x2^5 - 2*x2^7 : x0^5*x1^2 : x0^5*x2^2)

        ::

            sage: # needs sage.rings.real_mpfr
            sage: A.<x,y> = AffineSpace(CC, 2)
            sage: H = Hom(A, A)
            sage: f = H([(x^2-2)/(x*y), y^2 - x])
            sage: f.homogenize((2, 0))
            Scheme endomorphism of Projective Space of dimension 2
             over Complex Field with 53 bits of precision
              Defn: Defined on coordinates by sending (x0 : x1 : x2) to
                    (x0*x1*x2^2 : x0^2*x2^2 + (-2.00000000000000)*x2^4 : x0*x1^3 - x0^2*x1*x2)

        ::

            sage: A.<x,y> = AffineSpace(ZZ, 2)
            sage: X = A.subscheme([x - y^2])
            sage: H = Hom(X, X)
            sage: f = H([9*y^2, 3*y])
            sage: f.homogenize(2)                                                       # needs sage.libs.singular
            Scheme endomorphism of Closed subscheme of Projective Space
             of dimension 2 over Integer Ring defined by: x1^2 - x0*x2
              Defn: Defined on coordinates by sending (x0 : x1 : x2) to
                    (9*x1^2 : 3*x1*x2 : x2^2)

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: A.<x,y> = AffineSpace(R, 2)
            sage: H = Hom(A, A)
            sage: f = H([(x^2-2)/y, y^2 - x])
            sage: f.homogenize((2, 0))
            Scheme endomorphism of Projective Space of dimension 2
             over Univariate Polynomial Ring in t over Integer Ring
              Defn: Defined on coordinates by sending (x0 : x1 : x2) to
                    (x1*x2^2 : x0^2*x2 + (-2)*x2^3 : x1^3 - x0*x1*x2)

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: H = End(A)
            sage: f = H([x^2 - 1])
            sage: f.homogenize((1, 0))
            Scheme endomorphism of Projective Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x0 : x1) to
                    (x1^2 : x0^2 - x1^2)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<a> = PolynomialRing(QQbar)
            sage: A.<x,y> = AffineSpace(R, 2)
            sage: H = End(A)
            sage: f = H([QQbar(sqrt(2))*x*y, a*x^2])                                    # needs sage.symbolic
            sage: f.homogenize(2)                                                       # needs sage.libs.singular sage.symbolic
            Scheme endomorphism of Projective Space of dimension 2
             over Univariate Polynomial Ring in a over Algebraic Field
              Defn: Defined on coordinates by sending (x0 : x1 : x2) to
                    (1.414213562373095?*x0*x1 : a*x0^2 : x2^2)

        ::

            sage: P.<x,y,z> = AffineSpace(QQ, 3)
            sage: H = End(P)
            sage: f = H([x^2 - 2*x*y + z*x, z^2 -y^2 , 5*z*y])
            sage: f.homogenize(2).dehomogenize(2) == f
            True

        ::

            sage: K.<c> = FunctionField(QQ)
            sage: A.<x> = AffineSpace(K, 1)
            sage: f = Hom(A, A)([x^2 + c])
            sage: f.homogenize(1)
            Scheme endomorphism of Projective Space of dimension 1
             over Rational function field in c over Rational Field
              Defn: Defined on coordinates by sending (x0 : x1) to
                    (x0^2 + c*x1^2 : x1^2)

        ::

            sage: # needs sage.rings.number_field
            sage: A.<z> = AffineSpace(QQbar, 1)
            sage: H = End(A)
            sage: f = H([2*z / (z^2 + 2*z + 3)])
            sage: f.homogenize(1)
            Scheme endomorphism of Projective Space of dimension 1
             over Algebraic Field
              Defn: Defined on coordinates by sending (x0 : x1) to
                    (2*x0*x1 : x0^2 + 2*x0*x1 + 3*x1^2)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<c,d> = QQbar[]
            sage: A.<x> = AffineSpace(R, 1)
            sage: H = Hom(A, A)
            sage: F = H([d*x^2 + c])
            sage: F.homogenize(1)
            Scheme endomorphism of Projective Space of dimension 1
             over Multivariate Polynomial Ring in c, d over Algebraic Field
              Defn: Defined on coordinates by sending (x0 : x1) to
                    (d*x0^2 + c*x1^2 : x1^2)

        TESTS::

            sage: A2.<u,v> = AffineSpace(QQ, 2)
            sage: P2.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: f = A2.hom([u, v, u*v], P2)
            sage: g = f.homogenize(0)
            sage: i = A2.projective_embedding(0, g.domain())
            sage: g*i == f
            True
            sage: g = f.homogenize(1)
            sage: i = A2.projective_embedding(1, g.domain())
            sage: g*i == f
            True
            sage: g = f.homogenize(2)
            sage: i = A2.projective_embedding(2, g.domain())
            sage: g*i == f
            True
        """
    def as_dynamical_system(self):
        """
        Return this endomorphism as a :class:`DynamicalSystem_affine`.

        OUTPUT: :class:`DynamicalSystem_affine`

        EXAMPLES::

            sage: A.<x,y,z> = AffineSpace(ZZ, 3)
            sage: H = End(A)
            sage: f = H([x^2, y^2, z^2])
            sage: type(f.as_dynamical_system())                                         # needs sage.schemes
            <class 'sage.dynamics.arithmetic_dynamics.affine_ds.DynamicalSystem_affine'>

        ::

            sage: A.<x,y> = AffineSpace(ZZ, 2)
            sage: H = End(A)
            sage: f = H([x^2 - y^2, y^2])
            sage: type(f.as_dynamical_system())                                         # needs sage.schemes
            <class 'sage.dynamics.arithmetic_dynamics.affine_ds.DynamicalSystem_affine'>

        ::

            sage: A.<x> = AffineSpace(GF(5), 1)
            sage: H = End(A)
            sage: f = H([x^2])
            sage: type(f.as_dynamical_system())                                         # needs sage.schemes
            <class 'sage.dynamics.arithmetic_dynamics.affine_ds.DynamicalSystem_affine_finite_field'>

        ::

            sage: P.<x,y> = AffineSpace(RR, 2)
            sage: f = DynamicalSystem([x^2 + y^2, y^2], P)                              # needs sage.schemes
            sage: g = f.as_dynamical_system()                                           # needs sage.schemes
            sage: g is f                                                                # needs sage.schemes
            True
        """
    def global_height(self, prec=None):
        """
        Take the height of the homogenization, and return the global height of
        the coefficients as a projective point.

        INPUT:

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: H = Hom(A, A)
            sage: f = H([1/1331*x^2 + 4000])
            sage: f.global_height()                                                     # needs sage.symbolic
            15.4877354584971

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQ)
            sage: k.<w> = NumberField(x^2 + 5)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: H = Hom(A, A)
            sage: f = H([13*w*x^2 + 4*y, 1/w*y^2])
            sage: f.global_height(prec=2)
            4.0

        ::

            sage: A.<x> = AffineSpace(ZZ, 1)
            sage: H = Hom(A, A)
            sage: f = H([7*x^2 + 1513])
            sage: f.global_height()                                                     # needs sage.symbolic
            7.32184971378836

        ::

            sage: A.<x> = AffineSpace(QQ, 1)
            sage: B.<y,z> = AffineSpace(QQ, 2)
            sage: H = Hom(A, B)
            sage: f = H([1/3*x^2 + 10, 7*x^3])
            sage: f.global_height()                                                     # needs sage.symbolic
            3.40119738166216

        ::

            sage: P.<x,y> = AffineSpace(QQ, 2)
            sage: A.<z> = AffineSpace(QQ, 1)
            sage: H = Hom(P, A)
            sage: f = H([1/1331*x^2 + 4000*y])
            sage: f.global_height()                                                     # needs sage.symbolic
            15.4877354584971
        """
    def local_height(self, v, prec=None):
        """
        Return the maximum of the local heights of the coefficients in any
        of the coordinate functions of this map.

        INPUT:

        - ``v`` -- a prime or prime ideal of the base ring

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y> = AffineSpace(QQ, 2)
            sage: H = Hom(P, P)
            sage: f = H([1/1331*x^2 + 1/4000*y^2, 210*x*y])
            sage: f.local_height(1331)                                                  # needs sage.rings.real_mpfr
            7.19368581839511

        ::

            sage: P.<x,y,z> = AffineSpace(QQ, 3)
            sage: H = Hom(P, P)
            sage: f = H([4*x^2 + 3/100*y^2, 8/210*x*y, 1/10000*z^2])
            sage: f.local_height(2)                                                     # needs sage.rings.real_mpfr
            2.77258872223978

        ::

            sage: P.<x,y,z> = AffineSpace(QQ, 3)
            sage: H = Hom(P, P)
            sage: f = H([4*x^2 + 3/100*y^2, 8/210*x*y, 1/10000*z^2])
            sage: f.local_height(2, prec=2)                                             # needs sage.rings.real_mpfr
            3.0

        ::

            sage: # needs sage.rings.number_field
            sage: R.<z> = PolynomialRing(QQ)
            sage: K.<w> = NumberField(z^2 - 2)
            sage: P.<x,y> = AffineSpace(K, 2)
            sage: H = Hom(P, P)
            sage: f = H([2*x^2 + w/3*y^2, 1/w*y^2])
            sage: f.local_height(K.ideal(3))
            1.09861228866811
        """
    def local_height_arch(self, i, prec=None):
        """
        Return the maximum of the local height at the ``i``-th infinite place
        of the coefficients in any of the coordinate functions of this map.

        INPUT:

        - ``i`` -- integer

        - ``prec`` -- desired floating point precision (default:
          default RealField precision)

        OUTPUT: a real number

        EXAMPLES::

            sage: P.<x,y> = AffineSpace(QQ, 2)
            sage: H = Hom(P, P)
            sage: f = H([1/1331*x^2 + 1/4000*y^2, 210*x*y]);
            sage: f.local_height_arch(0)                                                # needs sage.rings.real_mpfr
            5.34710753071747

        ::

            sage: P.<x,y> = AffineSpace(QQ, 2)
            sage: H = Hom(P, P)
            sage: f = H([1/1331*x^2 + 1/4000*y^2, 210*x*y]);
            sage: f.local_height_arch(0, prec=5)                                        # needs sage.rings.real_mpfr
            5.2

        ::

            sage: # needs sage.rings.number_field
            sage: R.<z> = PolynomialRing(QQ)
            sage: K.<w> = NumberField(z^2 - 2)
            sage: P.<x,y> = AffineSpace(K, 2)
            sage: H = Hom(P, P)
            sage: f = H([2*x^2 + w/3*y^2, 1/w*y^2])
            sage: f.local_height_arch(1)
            0.6931471805599453094172321214582
        """
    def jacobian(self):
        """
        Return the Jacobian matrix of partial derivative of this map.

        The `(i, j)` entry of the Jacobian matrix is the partial derivative
        ``diff(functions[i], variables[j])``.

        OUTPUT: matrix with coordinates in the coordinate ring of the map

        EXAMPLES::

            sage: A.<z> = AffineSpace(QQ, 1)
            sage: H = End(A)
            sage: f = H([z^2 - 3/4])
            sage: f.jacobian()                                                          # needs sage.modules
            [2*z]

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: H = End(A)
            sage: f = H([x^3 - 25*x + 12*y, 5*y^2*x - 53*y + 24])
            sage: f.jacobian()                                                          # needs sage.modules
            [ 3*x^2 - 25          12]
            [      5*y^2 10*x*y - 53]

        ::

            sage: A.<x,y> = AffineSpace(ZZ, 2)
            sage: H = End(A)
            sage: f = H([(x^2 - x*y)/(1+y), (5+y)/(2+x)])
            sage: f.jacobian()                                                          # needs sage.modules
            [         (2*x - y)/(y + 1) (-x^2 - x)/(y^2 + 2*y + 1)]
            [  (-y - 5)/(x^2 + 4*x + 4)                  1/(x + 2)]
        """
    def degree(self):
        """
        Return the degree of the affine morphism.

        EXAMPLES::

            sage: R.<x> = AffineSpace(QQ, 1)
            sage: H = Hom(R, R)
            sage: f = H([x^7])
            sage: f.degree()
            7

        ::

            sage: R.<x,y,z> = AffineSpace(QQ, 3)
            sage: H = Hom(R, R)
            sage: f = H([x^3, y^2 + 5, z^4 + y])
            sage: f.degree()
            4
        """

class SchemeMorphism_polynomial_affine_space_field(SchemeMorphism_polynomial_affine_space):
    @cached_method
    def weil_restriction(self):
        """
        Compute the Weil restriction of this morphism over some extension field.

        If the field is a finite field, then this computes
        the Weil restriction to the prime subfield.

        A Weil restriction of scalars - denoted `Res_{L/k}` - is a
        functor which, for any finite extension of fields `L/k` and
        any algebraic variety `X` over `L`, produces another
        corresponding variety `Res_{L/k}(X)`, defined over `k`. It is
        useful for reducing questions about varieties over large
        fields to questions about more complicated varieties over
        smaller fields. Since it is a functor it also applied to morphisms.
        In particular, the functor applied to a morphism gives the equivalent
        morphism from the Weil restriction of the domain to the Weil restriction
        of the codomain.

        OUTPUT: scheme morphism on the Weil restrictions of the domain
                and codomain of the map.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K.<v> = QuadraticField(5)
            sage: A.<x,y> = AffineSpace(K, 2)
            sage: H = End(A)
            sage: f = H([x^2 - y^2, y^2])
            sage: f.weil_restriction()                                                  # needs sage.libs.singular
            Scheme endomorphism of Affine Space of dimension 4 over Rational Field
              Defn: Defined on coordinates by sending (z0, z1, z2, z3) to
                    (z0^2 + 5*z1^2 - z2^2 - 5*z3^2, 2*z0*z1 - 2*z2*z3, z2^2 + 5*z3^2, 2*z2*z3)

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = QuadraticField(5)
            sage: PS.<x,y> = AffineSpace(K, 2)
            sage: H = Hom(PS, PS)
            sage: f = H([x, y])
            sage: F = f.weil_restriction()
            sage: P = PS(2, 1)
            sage: Q = P.weil_restriction()
            sage: f(P).weil_restriction() == F(Q)                                       # needs sage.libs.singular
            True
        """
    def reduce_base_field(self):
        """
        Return this map defined over the field of definition of the coefficients.

        The base field of the map could be strictly larger than the field where
        all of the coefficients are defined. This function reduces the base
        field to the minimal possible. This can be done when the base ring is a
        number field, QQbar, a finite field, or algebraic closure of a finite
        field.

        OUTPUT: a scheme morphism

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<t> = GF(5^4)
            sage: A.<x> = AffineSpace(K, 1)
            sage: A2.<a,b> = AffineSpace(K, 2)
            sage: H = End(A)
            sage: H2 = Hom(A, A2)
            sage: H3 = Hom(A2, A)
            sage: f = H([x^2 + 2*(t^3 + t^2 + t + 3)])
            sage: f.reduce_base_field()
            Scheme endomorphism of Affine Space of dimension 1
             over Finite Field in t2 of size 5^2
              Defn: Defined on coordinates by sending (x) to (x^2 + (2*t2))
            sage: f2 = H2([x^2 + 4, 2*x])
            sage: f2.reduce_base_field()
            Scheme morphism:
              From: Affine Space of dimension 1 over Finite Field of size 5
              To:   Affine Space of dimension 2 over Finite Field of size 5
              Defn: Defined on coordinates by sending (x) to (x^2 - 1, 2*x)
            sage: f3 = H3([a^2 + t*b])
            sage: f3.reduce_base_field()
            Scheme morphism:
              From: Affine Space of dimension 2 over Finite Field in t of size 5^4
              To:   Affine Space of dimension 1 over Finite Field in t of size 5^4
              Defn: Defined on coordinates by sending (a, b) to (a^2 + t*b)

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = CyclotomicField(4)
            sage: A.<x> = AffineSpace(K, 1)
            sage: H = End(A)
            sage: f = H([x^2 + v])
            sage: g = f.reduce_base_field(); g
            Scheme endomorphism of Affine Space of dimension 1
             over Cyclotomic Field of order 4 and degree 2
              Defn: Defined on coordinates by sending (x) to (x^2 + v)
            sage: g.base_ring() is K
            True

        ::

            sage: # needs sage.rings.number_field
            sage: A.<x> = AffineSpace(QQbar, 1)
            sage: H = End(A)
            sage: f = H([(QQbar(sqrt(2))*x^2 + 1/QQbar(sqrt(3))) / (5*x)])              # needs sage.symbolic
            sage: f.reduce_base_field()                                                 # needs sage.symbolic
            Scheme endomorphism of Affine Space of dimension 1 over Number Field in a
             with defining polynomial y^4 - 4*y^2 + 1 with a = ...?
              Defn: Defined on coordinates by sending (x) to
                    (((a^3 - 3*a)*x^2 + (-1/3*a^2 + 2/3))/(5*x))

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQ)
            sage: A.<x> = AffineSpace(QQbar, 1)
            sage: H = End(A)
            sage: f = H([QQbar(3^(1/3))*x^2 + QQbar(sqrt(-2))])                         # needs sage.symbolic
            sage: f.reduce_base_field()                                                 # needs sage.symbolic
            Scheme endomorphism of Affine Space of dimension 1 over Number Field in a with defining polynomial y^6 + 6*y^4 - 6*y^3 + 12*y^2 + 36*y + 17 with a = 1.442249570307409? - 1.414213562373095?*I
              Defn: Defined on coordinates by sending (x) to
                    ((-48/269*a^5 + 27/269*a^4 - 320/269*a^3 + 468/269*a^2 - 772/269*a
                    - 1092/269)*x^2 + (-48/269*a^5 + 27/269*a^4 - 320/269*a^3 + 468/269*a^2
                    - 1041/269*a - 1092/269))

        ::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQ)
            sage: K.<a> = NumberField(x^3 - x + 1,
            ....:                     embedding=(x^3 + x + 1).roots(ring=CC)[0][0])
            sage: A.<x> = AffineSpace(K, 1)
            sage: A2.<u,v> = AffineSpace(K, 2)
            sage: H = Hom(A, A2)
            sage: f = H([x^2 + a*x + 3, 5*x])
            sage: f.reduce_base_field()
            Scheme morphism:
              From: Affine Space of dimension 1 over Number Field in a with
                    defining polynomial x^3 - x + 1 with a = -1.324717957244746?
              To:   Affine Space of dimension 2 over Number Field in a with
                    defining polynomial x^3 - x + 1 with a = -1.324717957244746?
              Defn: Defined on coordinates by sending (x) to (x^2 + a*x + 3, 5*x)

        ::

            sage: # needs sage.rings.number_field
            sage: K.<v> = QuadraticField(2)
            sage: A.<x> = AffineSpace(K, 1)
            sage: H = End(A)
            sage: f = H([3*x^2 + x + 1])
            sage: f.reduce_base_field()
            Scheme endomorphism of Affine Space of dimension 1 over Rational Field
              Defn: Defined on coordinates by sending (x) to (3*x^2 + x + 1)

        ::

            sage: # needs sage.rings.finite_rings
            sage: K.<t> = GF(5^6)
            sage: A.<x> = AffineSpace(K, 1)
            sage: H = End(A)
            sage: f = H([x^2 + x*(t^3 + 2*t^2 + 4*t) + (t^5 + 3*t^4 + t^2 + 4*t)])
            sage: f.reduce_base_field()
            Scheme endomorphism of Affine Space of dimension 1
             over Finite Field in t of size 5^6
              Defn: Defined on coordinates by sending (x) to
                    (x^2 + (t^3 + 2*t^2 - t)*x + (t^5 - 2*t^4 + t^2 - t))
        """
    def indeterminacy_locus(self):
        """
        Return the indeterminacy locus of this map as a rational map on the domain.

        The indeterminacy locus is the intersection of all the base indeterminacy
        locuses of maps that define the same rational map as by this map.

        OUTPUT: a subscheme of the domain of the map

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: H = End(A)
            sage: f = H([x - y, x^2 - y^2])
            sage: f.indeterminacy_locus()                                               # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              1

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: f = A.hom([x, x/y], A)
            sage: f.indeterminacy_locus()                                               # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              y
        """
    def indeterminacy_points(self, F=None):
        """
        Return the points in the indeterminacy locus of this map.

        If the dimension of the indeterminacy locus is not zero, an error is raised.

        INPUT:

        - ``F`` -- a field; if not given, the base ring of the domain is assumed

        OUTPUT: indeterminacy points of the map defined over ``F``

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: H = End(A)
            sage: f = H([x - y, x^2 - y^2])
            sage: f.indeterminacy_points()                                              # needs sage.libs.singular
            []

        ::

            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: P2.<x0,x1,x2> = ProjectiveSpace(QQ, 2)
            sage: f = A2.hom([x*y, y, x], P2)
            sage: f.indeterminacy_points()                                              # needs sage.libs.singular
            [(0, 0)]
        """
    def image(self):
        """
        Return the scheme-theoretic image of the morphism.

        OUTPUT: a subscheme of the ambient space of the codomain

        EXAMPLES::

            sage: # needs sage.libs.singular
            sage: A1.<w> = AffineSpace(QQ, 1)
            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: f = A2.hom([x + y], A1)
            sage: f.image()
            Closed subscheme of Affine Space of dimension 1 over Rational Field defined by:
              (no polynomials)
            sage: f = A2.hom([x, x], A2)
            sage: f.image()
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x - y
            sage: f = A2.hom([x^2, x^3], A2)
            sage: f.image()
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x^3 - y^2
            sage: P2.<x0,x1,x2> = ProjectiveSpace(QQ, 2)
            sage: f = A2.hom([x, x^2, x^3], P2)
            sage: f.image()
            Closed subscheme of Projective Space of dimension 2 over Rational Field defined by:
              x1^2 - x0*x2
        """

class SchemeMorphism_polynomial_affine_space_finite_field(SchemeMorphism_polynomial_affine_space_field): ...

class SchemeMorphism_polynomial_affine_subscheme_field(SchemeMorphism_polynomial_affine_space_field):
    """
    Morphisms from subschemes of affine spaces defined over fields.
    """
    @cached_method
    def representatives(self):
        """
        Return all maps representing the same rational map as by this map.

        EXAMPLES::

            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: X = A2.subscheme(0)
            sage: f = X.hom([x, x/y], A2)
            sage: f.representatives()                                                   # needs sage.libs.singular
            [Scheme morphism:
               From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                     defined by: 0
               To:   Affine Space of dimension 2 over Rational Field
               Defn: Defined on coordinates by sending (x, y) to (x, x/y)]

        ::

            sage: # needs sage.libs.singular
            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: A1.<a> = AffineSpace(QQ, 1)
            sage: X = A2.subscheme([x^2 - y^2 - y])
            sage: f = X.hom([x/y], A1)
            sage: f.representatives()
            [Scheme morphism:
               From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                     defined by: x^2 - y^2 - y
               To:   Affine Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x, y) to (x/y),
             Scheme morphism:
               From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                     defined by: x^2 - y^2 - y
               To:   Affine Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x, y) to ((y + 1)/x)]
            sage: g = _[1]
            sage: g.representatives()
            [Scheme morphism:
               From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                     defined by: x^2 - y^2 - y
               To:   Affine Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x, y) to (x/y),
             Scheme morphism:
               From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                     defined by: x^2 - y^2 - y
               To:   Affine Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x, y) to ((y + 1)/x)]

        ::

            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: P1.<a,b> = ProjectiveSpace(QQ, 1)
            sage: X = A2.subscheme([x^2 - y^2 - y])
            sage: f = X.hom([x, y], P1)
            sage: f.representatives()                                                   # needs sage.libs.singular
            [Scheme morphism:
               From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                     defined by: x^2 - y^2 - y
               To:   Projective Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x, y) to
                     (x : y),
             Scheme morphism:
               From: Closed subscheme of Affine Space of dimension 2 over Rational Field
                     defined by: x^2 - y^2 - y
               To:   Projective Space of dimension 1 over Rational Field
               Defn: Defined on coordinates by sending (x, y) to (y + 1 : x)]
        """
    def indeterminacy_locus(self):
        """
        Return the indeterminacy locus of this map.

        The map defines a rational map on the domain. The output is the
        subscheme of the domain on which the rational map is not defined by any
        representative of the rational map. See :meth:`representatives()`.

        EXAMPLES::

            sage: A2.<x1,x2> = AffineSpace(QQ, 2)
            sage: X = A2.subscheme(0)
            sage: A1.<x> = AffineSpace(QQ, 1)
            sage: f = X.hom([x1/x2], A1)
            sage: f.indeterminacy_locus()                                               # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              x2

        ::

            sage: A2.<x1,x2> = AffineSpace(QQ, 2)
            sage: X = A2.subscheme(0)
            sage: P1.<a,b> = ProjectiveSpace(QQ, 1)
            sage: f = X.hom([x1,x2], P1)
            sage: L = f.indeterminacy_locus()                                           # needs sage.libs.singular
            sage: L.rational_points()                                                   # needs sage.libs.singular
            [(0, 0)]

        ::

            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: X = A2.subscheme([x^2 - y^2 - y])
            sage: A1.<a> = AffineSpace(QQ, 1)
            sage: f = X.hom([x/y], A1)
            sage: f.indeterminacy_locus()                                               # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              y,
              x

        ::

            sage: A3.<x,y,z> = AffineSpace(QQ, 3)
            sage: X = A3.subscheme(x^2 - y*z - x)
            sage: A2.<a,b> = AffineSpace(QQ, 2)
            sage: f = X.hom([y, y/x], A2)
            sage: L = f.indeterminacy_locus(); L                                        # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 3 over Rational Field defined by:
              x,
              y*z
            sage: L.dimension()                                                         # needs sage.libs.singular
            1
        """
    def is_morphism(self):
        """
        Return ``True`` if the map is defined everywhere on the domain.

        EXAMPLES::

            sage: P2.<x,y,z> = ProjectiveSpace(QQ,2)
            sage: P1.<a,b> = ProjectiveSpace(QQ,1)
            sage: X = P2.subscheme([x^2 - y^2 - y*z])
            sage: f = X.hom([x,y], P1)
            sage: f.is_morphism()                                                       # needs sage.libs.singular
            True
        """
    def image(self):
        """
        Return the scheme-theoretic image of the morphism.

        OUTPUT: a subscheme of the ambient space of the codomain

        EXAMPLES::

            sage: A1.<w> = AffineSpace(QQ, 1)
            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: X = A2.subscheme(0)
            sage: f = X.hom([x + y], A1)
            sage: f.image()                                                             # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 1 over Rational Field defined by:
              (no polynomials)

        ::

            sage: A2.<x,y> = AffineSpace(QQ, 2)
            sage: X = A2.subscheme([x*y^2 - y^3 - 1])
            sage: f = X.hom([y, y/x], A2)
            sage: f.image()                                                             # needs sage.libs.singular
            Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
              -x^3*y + x^3 - y
        """
