from sage.categories.fields import Fields as Fields
from sage.categories.number_fields import NumberFields as NumberFields
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.misc.verbose import verbose as verbose
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import RationalField as RationalField
from sage.schemes.generic.algebraic_scheme import AlgebraicScheme_subscheme as AlgebraicScheme_subscheme
from sage.schemes.generic.homset import SchemeHomset_generic as SchemeHomset_generic, SchemeHomset_points as SchemeHomset_points

class SchemeHomset_points_projective_field(SchemeHomset_points):
    """
    Set of rational points of a projective variety over a field.

    INPUT:

    See :class:`SchemeHomset_generic`.

    EXAMPLES::

        sage: from sage.schemes.projective.projective_homset import SchemeHomset_points_projective_field
        sage: SchemeHomset_points_projective_field(Spec(QQ), ProjectiveSpace(QQ,2))
        Set of rational points of Projective Space of dimension 2 over Rational Field
    """
    def points(self, **kwds):
        """
        Return some or all rational points of a projective scheme.

        For dimension 0 subschemes points are determined through a groebner
        basis calculation. For schemes or subschemes with dimension greater than 1
        points are determined through enumeration up to the specified bound.

        INPUT: keyword arguments:

        - ``bound`` -- real number (default: 0); the bound for the coordinates
          for subschemes with dimension at least 1

        - ``precision`` -- integer (default: 53); the precision to use to
          compute the elements of bounded height for number fields

        - ``point_tolerance`` -- positive real number (default: `10^{-10}`);
          for numerically inexact fields, two points are considered the same
          if their coordinates are within tolerance

        - ``zero_tolerance`` -- positive real number (default: `10^{-10}`);
          for numerically inexact fields, points are on the subscheme if they
          satisfy the equations to within tolerance

        - ``tolerance`` -- a rational number in (0,1] used in Doyle-Krumm
          algorithm-4 for enumeration over number fields

        OUTPUT: list of rational points of a projective scheme

        .. WARNING::

            For numerically inexact fields such as ComplexField or RealField the
            list of points returned is very likely to be incomplete. It may also
            contain repeated points due to tolerances.

        EXAMPLES::

            sage: P.<x,y> = ProjectiveSpace(QQ, 1)
            sage: P(QQ).points(bound=4)
            [(-4 : 1), (-3 : 1), (-2 : 1), (-3/2 : 1), (-4/3 : 1), (-1 : 1),
             (-3/4 : 1), (-2/3 : 1), (-1/2 : 1), (-1/3 : 1), (-1/4 : 1), (0 : 1),
             (1/4 : 1), (1/3 : 1), (1/2 : 1), (2/3 : 1), (3/4 : 1), (1 : 0), (1 : 1),
             (4/3 : 1), (3/2 : 1), (2 : 1), (3 : 1), (4 : 1)]

        ::

            sage: u = QQ['u'].0
            sage: K.<v> = NumberField(u^2 + 3)                                          # needs sage.rings.number_field
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)                                     # needs sage.rings.number_field
            sage: len(P(K).points(bound=1.8))                                           # needs sage.rings.number_field
            309

        ::

            sage: P1 = ProjectiveSpace(GF(2), 1)
            sage: F.<a> = GF(4, 'a')                                                    # needs sage.rings.finite_rings
            sage: P1(F).points()                                                        # needs sage.libs.singular sage.rings.finite_rings
            [(0 : 1), (1 : 0), (1 : 1), (a : 1), (a + 1 : 1)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: E = P.subscheme([(y^3-y*z^2) - (x^3-x*z^2), (y^3-y*z^2) + (x^3-x*z^2)])
            sage: E(P.base_ring()).points()                                             # needs sage.libs.singular
            [(-1 : -1 : 1), (-1 : 0 : 1), (-1 : 1 : 1), (0 : -1 : 1), (0 : 0 : 1),
             (0 : 1 : 1), (1 : -1 : 1), (1 : 0 : 1), (1 : 1 : 1)]

        ::

            sage: # needs sage.rings.real_mpfr
            sage: P.<x,y,z> = ProjectiveSpace(CC, 2)
            sage: E = P.subscheme([y^3 - x^3 - x*z^2, x*y*z])
            sage: L = E(P.base_ring()).points(); sorted(L, key=str)                     # needs sage.libs.singular
            verbose 0 (...: projective_homset.py, points) Warning: computations in
            the numerical fields are inexact;points may be computed partially or incorrectly.
            [(-0.500000000000000 + 0.866025403784439*I : 1.00000000000000 : 0.000000000000000),
             (-0.500000000000000 - 0.866025403784439*I : 1.00000000000000 : 0.000000000000000),
             (-1.00000000000000*I : 0.000000000000000 : 1.00000000000000),
             (0.000000000000000 : 0.000000000000000 : 1.00000000000000),
             (1.00000000000000 : 1.00000000000000 : 0.000000000000000),
             (1.00000000000000*I : 0.000000000000000 : 1.00000000000000)]
            sage: L[0].codomain()                                                       # needs sage.libs.singular
            Projective Space of dimension 2 over Complex Field with 53 bits of precision

        ::

            sage: # needs sage.rings.complex_double
            sage: P.<x,y,z> = ProjectiveSpace(CDF, 2)
            sage: E = P.subscheme([y^2 + x^2 + z^2, x*y*z])
            sage: len(E(P.base_ring()).points())                                        # needs sage.libs.singular
            verbose 0 (...: projective_homset.py, points) Warning: computations in
            the numerical fields are inexact;points may be computed partially or incorrectly.
            6
        """
    def numerical_points(self, F=None, **kwds):
        """
        Return some or all numerical approximations of rational points of a projective scheme.

        This is for dimension 0 subschemes only and the points are determined
        through a groebner calculation over the base ring and then numerically
        approximating the roots of the resulting polynomials. If the base ring
        is a number field, the embedding into ``F`` must be known.

        INPUT:

        - ``F`` -- numerical ring

        kwds:

        - ``point_tolerance`` -- positive real number (default: `10^{-10}`).
          For numerically inexact fields, two points are considered the same
          if their coordinates are within tolerance.

        - ``zero_tolerance`` -- positive real number (default: `10^{-10}`).
          For numerically inexact fields, points are on the subscheme if they
          satisfy the equations to within tolerance.

        OUTPUT: list of points in the ambient space

        .. WARNING::

           For numerically inexact fields the list of points returned may contain repeated
           or be missing points due to tolerance.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: E = P.subscheme([y^3 - x^3 - x*z^2, x*y*z])
            sage: L = E(QQ).numerical_points(F=RR); L                                   # needs sage.libs.singular
            [(0.000000000000000 : 0.000000000000000 : 1.00000000000000),
             (1.00000000000000 : 1.00000000000000 : 0.000000000000000)]
            sage: L[0].codomain()                                                       # needs sage.libs.singular
            Projective Space of dimension 2 over Real Field with 53 bits of precision

        ::

            sage: S.<a> = QQ[]
            sage: K.<v> = NumberField(a^5 - 7, embedding=CC(7)**(1/5))                  # needs sage.rings.number_field
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)                                     # needs sage.rings.number_field
            sage: X = P.subscheme([x^2 - v^2*z^2, y - v*z])                             # needs sage.rings.number_field
            sage: len(X(K).numerical_points(F=CDF))                                     # needs sage.libs.singular sage.rings.number_field
            2

        ::

            sage: P.<x1, x2, x3> = ProjectiveSpace(QQ, 2)
            sage: E = P.subscheme([3000*x1^50 + 9875643*x2^2*x3^48 + 12334545*x2^50, x1 + x2])
            sage: len(E(P.base_ring()).numerical_points(F=CDF, zero_tolerance=1e-6))    # needs sage.libs.singular
            49

        TESTS::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: E = P.subscheme([y^3 - x^3 - x*z^2, x*y*z])
            sage: E(QQ).numerical_points(F=CDF, point_tolerance=-1)                     # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ValueError: tolerance must be positive

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: E = P.subscheme([y^3 - x^3 - x*z^2, x*y*z])
            sage: E(QQ).numerical_points(F=CC, zero_tolerance=-1)                       # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ValueError: tolerance must be positive

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: E = P.subscheme([y^3 - x^3 - x*z^2, x*y*z])
            sage: E(QQ).numerical_points(F=QQbar)                                       # needs sage.rings.number_field
            Traceback (most recent call last):
            ...
            TypeError: F must be a numerical field
        """

class SchemeHomset_points_projective_ring(SchemeHomset_points):
    """
    Set of rational points of a projective variety over a commutative ring.

    INPUT:

    See :class:`SchemeHomset_generic`.

    EXAMPLES::

        sage: from sage.schemes.projective.projective_homset import SchemeHomset_points_projective_ring
        sage: SchemeHomset_points_projective_ring(Spec(ZZ), ProjectiveSpace(ZZ,2))
        Set of rational points of Projective Space of dimension 2 over Integer Ring
    """
    def points(self, B: int = 0):
        """
        Return some or all rational points of a projective scheme.

        INPUT:

        - ``B`` -- integer (default: 0); the bound for the coordinates

        EXAMPLES::

            sage: from sage.schemes.projective.projective_homset import SchemeHomset_points_projective_ring
            sage: H = SchemeHomset_points_projective_ring(Spec(ZZ), ProjectiveSpace(ZZ, 2))
            sage: H.points(3)
            [(0 : 0 : 1), (0 : 1 : -3), (0 : 1 : -2), (0 : 1 : -1), (0 : 1 : 0), (0 : 1 : 1),
             (0 : 1 : 2), (0 : 1 : 3), (0 : 2 : -3), (0 : 2 : -1), (0 : 2 : 1), (0 : 2 : 3),
             (0 : 3 : -2), (0 : 3 : -1), (0 : 3 : 1), (0 : 3 : 2), (1 : -3 : -3),
             (1 : -3 : -2), (1 : -3 : -1), (1 : -3 : 0), (1 : -3 : 1), (1 : -3 : 2),
             (1 : -3 : 3), (1 : -2 : -3), (1 : -2 : -2), (1 : -2 : -1), (1 : -2 : 0),
             (1 : -2 : 1), (1 : -2 : 2), (1 : -2 : 3), (1 : -1 : -3), (1 : -1 : -2),
             (1 : -1 : -1), (1 : -1 : 0), (1 : -1 : 1), (1 : -1 : 2), (1 : -1 : 3),
             (1 : 0 : -3), (1 : 0 : -2), (1 : 0 : -1), (1 : 0 : 0), (1 : 0 : 1), (1 : 0 : 2),
             (1 : 0 : 3), (1 : 1 : -3), (1 : 1 : -2), (1 : 1 : -1), (1 : 1 : 0), (1 : 1 : 1),
             (1 : 1 : 2), (1 : 1 : 3), (1 : 2 : -3), (1 : 2 : -2), (1 : 2 : -1), (1 : 2 : 0),
             (1 : 2 : 1), (1 : 2 : 2), (1 : 2 : 3), (1 : 3 : -3), (1 : 3 : -2), (1 : 3 : -1),
             (1 : 3 : 0), (1 : 3 : 1), (1 : 3 : 2), (1 : 3 : 3), (2 : -3 : -3),
             (2 : -3 : -2), (2 : -3 : -1), (2 : -3 : 0), (2 : -3 : 1), (2 : -3 : 2),
             (2 : -3 : 3), (2 : -2 : -3), (2 : -2 : -1), (2 : -2 : 1), (2 : -2 : 3),
             (2 : -1 : -3), (2 : -1 : -2), (2 : -1 : -1), (2 : -1 : 0), (2 : -1 : 1),
             (2 : -1 : 2), (2 : -1 : 3), (2 : 0 : -3), (2 : 0 : -1), (2 : 0 : 1),
             (2 : 0 : 3), (2 : 1 : -3), (2 : 1 : -2), (2 : 1 : -1), (2 : 1 : 0), (2 : 1 : 1),
             (2 : 1 : 2), (2 : 1 : 3), (2 : 2 : -3), (2 : 2 : -1), (2 : 2 : 1), (2 : 2 : 3),
             (2 : 3 : -3), (2 : 3 : -2), (2 : 3 : -1), (2 : 3 : 0), (2 : 3 : 1), (2 : 3 : 2),
             (2 : 3 : 3), (3 : -3 : -2), (3 : -3 : -1), (3 : -3 : 1), (3 : -3 : 2),
             (3 : -2 : -3), (3 : -2 : -2), (3 : -2 : -1), (3 : -2 : 0), (3 : -2 : 1),
             (3 : -2 : 2), (3 : -2 : 3), (3 : -1 : -3), (3 : -1 : -2), (3 : -1 : -1),
             (3 : -1 : 0), (3 : -1 : 1), (3 : -1 : 2), (3 : -1 : 3), (3 : 0 : -2),
             (3 : 0 : -1), (3 : 0 : 1), (3 : 0 : 2), (3 : 1 : -3), (3 : 1 : -2),
             (3 : 1 : -1), (3 : 1 : 0), (3 : 1 : 1), (3 : 1 : 2), (3 : 1 : 3), (3 : 2 : -3),
             (3 : 2 : -2), (3 : 2 : -1), (3 : 2 : 0), (3 : 2 : 1), (3 : 2 : 2), (3 : 2 : 3),
             (3 : 3 : -2), (3 : 3 : -1), (3 : 3 : 1), (3 : 3 : 2)]
        """

class SchemeHomset_polynomial_projective_space(SchemeHomset_generic):
    """
    Set of morphisms of a projective space.

    EXAMPLES::

        sage: P.<x,y,z> = ProjectiveSpace(2, QQ)
        sage: Hom(P, P)
        Set of morphisms
          From: Projective Space of dimension 2 over Rational Field
          To:   Projective Space of dimension 2 over Rational Field
    """
    def identity(self):
        """
        Return the identity morphism of this hom-set.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(2, QQ)
            sage: Hom(P, P)
            Set of morphisms
              From: Projective Space of dimension 2 over Rational Field
              To:   Projective Space of dimension 2 over Rational Field
            sage: _.identity()
            Scheme endomorphism of Projective Space of dimension 2 over Rational Field
              Defn: Identity map
        """

class SchemeHomset_points_abelian_variety_field(SchemeHomset_points_projective_field):
    """
    Set of rational points of an Abelian variety.

    INPUT:

    See :class:`SchemeHomset_generic`.

    TESTS:

    The bug reported at :issue:`1785` is fixed::

        sage: # needs sage.rings.number_field sage.schemes
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 + x - (3^3-3))
        sage: E = EllipticCurve('37a')
        sage: X = E(K)
        sage: X
        Abelian group of points on
         Elliptic Curve defined by y^2 + y = x^3 + (-1)*x
          over Number Field in a with defining polynomial x^2 + x - 24
        sage: P = X([3,a])
        sage: P
        (3 : a : 1)
        sage: P in E
        False
        sage: P in E.base_extend(K)
        True
        sage: P in X.codomain()
        False
        sage: P in X.extended_codomain()
        True

    Check for :issue:`11982`::

        sage: P2.<x,y,z> = ProjectiveSpace(QQ,2)
        sage: d = 7
        sage: C = Curve(x^3 + y^3 - d*z^3)                                              # needs sage.schemes
        sage: E = EllipticCurve([0,-432*d^2])                                           # needs sage.schemes
        sage: transformation = [(36*d*z-y)/(72*d), (36*d*z+y)/(72*d), x/(12*d)]
        sage: phi = E.hom(transformation, C); phi                                       # needs sage.schemes
        Scheme morphism:
          From: Elliptic Curve defined by y^2 = x^3 - 21168 over Rational Field
          To:   Projective Plane Curve over Rational Field defined by x^3 + y^3 - 7*z^3
          Defn: Defined on coordinates by sending (x : y : z) to
                (-1/504*y + 1/2*z : 1/504*y + 1/2*z : 1/84*x)
    """
    def base_extend(self, R):
        """
        Extend the base ring.

        This is currently not implemented except for the trivial case
        ``R==ZZ``.

        INPUT:

        - ``R`` -- a ring

        EXAMPLES::

            sage: # needs sage.schemes
            sage: E = EllipticCurve('37a')
            sage: Hom = E.point_homset();  Hom
            Abelian group of points on Elliptic Curve defined
             by y^2 + y = x^3 - x over Rational Field
            sage: Hom.base_ring()
            Rational Field
            sage: Hom.base_extend(QQ)
            Traceback (most recent call last):
            ...
            NotImplementedError: Abelian variety point sets are not
            implemented as modules over rings other than ZZ
        """
    def zero(self):
        """
        Return the neutral element in this group of points.

        EXAMPLES::

            sage: S = EllipticCurve(GF(5), [1,1]).point_homset()
            sage: S.zero()
            (0 : 1 : 0)
            sage: S = EllipticCurve(Zmod(15), [1,1]).point_homset()
            sage: S.zero()
            (0 : 1 : 0)
        """
