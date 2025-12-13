from sage.categories.fields import Fields as Fields
from sage.categories.number_fields import NumberFields as NumberFields
from sage.misc.verbose import verbose as verbose
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import RationalField as RationalField
from sage.schemes.generic.homset import SchemeHomset_generic as SchemeHomset_generic, SchemeHomset_points as SchemeHomset_points

class SchemeHomset_points_spec(SchemeHomset_generic):
    """
    Set of rational points of an affine variety.

    INPUT:

    See :class:`SchemeHomset_generic`.

    EXAMPLES::

        sage: from sage.schemes.affine.affine_homset import SchemeHomset_points_spec
        sage: SchemeHomset_points_spec(Spec(QQ), Spec(QQ))
        Set of rational points of Spectrum of Rational Field
    """

class SchemeHomset_polynomial_affine_space(SchemeHomset_generic):
    """
    Set of morphisms between affine spaces defined by polynomials.

    EXAMPLES::

        sage: A.<x,y> = AffineSpace(2, QQ)
        sage: Hom(A, A)
        Set of morphisms
          From: Affine Space of dimension 2 over Rational Field
          To:   Affine Space of dimension 2 over Rational Field
    """
    def identity(self):
        """
        The identity morphism of this homset.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(2, QQ)
            sage: I = A.identity_morphism()
            sage: I.parent()
            Set of morphisms
              From: Affine Space of dimension 2 over Rational Field
              To:   Affine Space of dimension 2 over Rational Field
            sage: _.identity() == I
            True
        """

class SchemeHomset_points_affine(SchemeHomset_points):
    """
    Set of rational points of an affine variety.

    INPUT:

    See :class:`SchemeHomset_generic`.

    EXAMPLES::

        sage: from sage.schemes.affine.affine_homset import SchemeHomset_points_affine
        sage: SchemeHomset_points_affine(Spec(QQ), AffineSpace(ZZ,2))
        Set of rational points of Affine Space of dimension 2 over Rational Field
    """
    def points(self, **kwds):
        """
        Return some or all rational points of an affine scheme.

        For dimension 0 subschemes points are determined through a groebner
        basis calculation. For schemes or subschemes with dimension greater than 1
        points are determined through enumeration up to the specified bound.

        Over a finite field, all points are returned. Over an infinite field, all points satisfying the bound
        are returned. For a zero-dimensional subscheme, all points are returned regardless of whether the field
        is infinite or not.

        For number fields, this uses the
        Doyle-Krumm algorithm 4 (algorithm 5 for imaginary quadratic) for
        computing algebraic numbers up to a given height [DK2013]_.

        The algorithm requires floating point arithmetic, so the user is
        allowed to specify the precision for such calculations.
        Additionally, due to floating point issues, points
        slightly larger than the bound may be returned. This can be controlled
        by lowering the tolerance.


        INPUT: keyword arguments:

        - ``bound`` -- real number (default: 0). The bound for the
          height of the coordinates. Only used for subschemes with
          dimension at least 1.

        - ``zero_tolerance`` -- positive real number (default: 10^(-10)).
          For numerically inexact fields, points are on the subscheme if they
          satisfy the equations to within tolerance.

        - ``tolerance`` -- a rational number in (0,1] used in Doyle-Krumm
          algorithm-4 for enumeration over number fields

        - ``precision`` -- the precision to use for computing the elements of
          bounded height of number fields

        OUTPUT: list of rational points of a affine scheme

        .. WARNING::

           For numerically inexact fields such as ComplexField or RealField the
           list of points returned is very likely to be incomplete. It may also
           contain repeated points due to tolerance.

        EXAMPLES: The bug reported at #11526 is fixed::

            sage: A2 = AffineSpace(ZZ, 2)
            sage: F = GF(3)
            sage: A2(F).points()
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

        ::

            sage: A.<x,y> = ZZ[]
            sage: I = A.ideal(x^2 - y^2 - 1)
            sage: V = AffineSpace(ZZ, 2)
            sage: X = V.subscheme(I)
            sage: M = X(ZZ)
            sage: M.points(bound=1)
            [(-1, 0), (1, 0)]

        ::

            sage: u = QQ['u'].0
            sage: K.<v> = NumberField(u^2 + 3)                                          # needs sage.rings.number_field
            sage: A.<x,y> = AffineSpace(K, 2)                                           # needs sage.rings.number_field
            sage: len(A(K).points(bound=2))                                             # needs sage.rings.number_field
            1849

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: E = A.subscheme([x^2 + y^2 - 1, y^2 - x^3 + x^2 + x - 1])
            sage: E(A.base_ring()).points()                                             # needs sage.libs.singular
            [(-1, 0), (0, -1), (0, 1), (1, 0)]

        ::

            sage: A.<x,y> = AffineSpace(CC, 2)                                          # needs sage.rings.real_mpfr
            sage: E = A.subscheme([y^3 - x^3 - x^2, x*y])
            sage: E(A.base_ring()).points()                                             # needs sage.libs.singular sage.rings.real_mpfr
            verbose 0 (...: affine_homset.py, points)
            Warning: computations in the numerical fields are inexact;points
            may be computed partially or incorrectly.
            [(-1.00000000000000, 0.000000000000000),
             (0.000000000000000, 0.000000000000000)]

        ::

            sage: A.<x1,x2> = AffineSpace(CDF, 2)                                       # needs sage.rings.complex_double
            sage: E = A.subscheme([x1^2 + x2^2 + x1*x2, x1 + x2])                       # needs sage.libs.singular sage.rings.complex_double
            sage: E(A.base_ring()).points()                                             # needs sage.libs.singular sage.rings.complex_double
            verbose 0 (...: affine_homset.py, points)
            Warning: computations in the numerical fields are inexact;points
            may be computed partially or incorrectly.
            [(0.0, 0.0)]
        """
    def numerical_points(self, F=None, **kwds):
        """
        Return some or all numerical approximations of rational points of an affine scheme.

        This is for dimension 0 subschemes only and the points are determined
        through a groebner calculation over the base ring and then numerically
        approximating the roots of the resulting polynomials. If the base ring
        is a number field, the embedding into ``F`` must be known.

        INPUT:

        - ``F`` -- numerical ring

        kwds:

        - ``zero_tolerance`` -- positive real number (default: 10^(-10)).
          For numerically inexact fields, points are on the subscheme if they
          satisfy the equations to within tolerance.

        OUTPUT: list of points in the ambient space

        .. WARNING::

           For numerically inexact fields the list of points returned may contain repeated
           or be missing points due to tolerance.

        EXAMPLES::

            sage: # needs sage.libs.singular sage.rings.number_field
            sage: K.<v> = QuadraticField(3)
            sage: A.<x,y> = AffineSpace(K, 2)
            sage: X = A.subscheme([x^3 - v^2*y, y - v*x^2 + 3])
            sage: L = X(K).numerical_points(F=RR); L  # abs tol 1e-14
            [(-1.18738247880014, -0.558021142104134),
             (1.57693558184861, 1.30713548084184),
             (4.80659931965815, 37.0162574656220)]
            sage: L[0].codomain()
            Affine Space of dimension 2 over Real Field with 53 bits of precision

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: X = A.subscheme([y^2 - x^2 - 3*x, x^2 - 10*y])
            sage: len(X(QQ).numerical_points(F=ComplexField(100)))                      # needs sage.libs.singular
            4

        ::

            sage: A.<x1, x2> = AffineSpace(QQ, 2)
            sage: E = A.subscheme([30*x1^100 + 1000*x2^2 + 2000*x1*x2 + 1, x1 + x2])
            sage: len(E(A.base_ring()).numerical_points(F=CDF, zero_tolerance=1e-9))    # needs sage.libs.singular
            100

        TESTS::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: X = A.subscheme([y^2 - x^2 - 3*x, x^2 - 10*y])
            sage: X(QQ).numerical_points(F=QQ)
            Traceback (most recent call last):
            ...
            TypeError: F must be a numerical field

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: X = A.subscheme([y^2 - x^2 - 3*x, x^2 - 10*y])
            sage: X(QQ).numerical_points(F=CC, zero_tolerance=-1)                       # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ValueError: tolerance must be positive
        """
