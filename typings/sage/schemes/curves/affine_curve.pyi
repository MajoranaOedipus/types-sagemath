from .closed_point import IntegralAffineCurveClosedPoint as IntegralAffineCurveClosedPoint
from .curve import Curve_generic as Curve_generic
from .point import AffineCurvePoint_field as AffineCurvePoint_field, AffinePlaneCurvePoint_field as AffinePlaneCurvePoint_field, AffinePlaneCurvePoint_finite_field as AffinePlaneCurvePoint_finite_field, IntegralAffineCurvePoint as IntegralAffineCurvePoint, IntegralAffineCurvePoint_finite_field as IntegralAffineCurvePoint_finite_field, IntegralAffinePlaneCurvePoint as IntegralAffinePlaneCurvePoint, IntegralAffinePlaneCurvePoint_finite_field as IntegralAffinePlaneCurvePoint_finite_field
from sage.arith.misc import binomial as binomial
from sage.categories.fields import Fields as Fields
from sage.categories.finite_fields import FiniteFields as FiniteFields
from sage.categories.homset import End as End, Hom as Hom, hom as hom
from sage.categories.number_fields import NumberFields as NumberFields
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import infinity as infinity
from sage.rings.polynomial.multi_polynomial_element import degree_lowest_rational_function as degree_lowest_rational_function
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import RationalField as RationalField
from sage.schemes.affine.affine_space import AffineSpace as AffineSpace, AffineSpace_generic as AffineSpace_generic
from sage.schemes.affine.affine_subscheme import AlgebraicScheme_subscheme_affine as AlgebraicScheme_subscheme_affine, AlgebraicScheme_subscheme_affine_field as AlgebraicScheme_subscheme_affine_field

class AffineCurve(Curve_generic, AlgebraicScheme_subscheme_affine):
    """
    Affine curves.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: R.<v> = QQ[]
        sage: K.<u> = NumberField(v^2 + 3)
        sage: A.<x,y,z> = AffineSpace(K, 3)
        sage: C = Curve([z - u*x^2, y^2], A); C
        Affine Curve over Number Field in u with defining polynomial v^2 + 3
        defined by (-u)*x^2 + z, y^2

    ::

        sage: A.<x,y,z> = AffineSpace(GF(7), 3)
        sage: C = Curve([x^2 - z, z - 8*x], A); C
        Affine Curve over Finite Field of size 7 defined by x^2 - z, -x + z
    """
    def __init__(self, A, X) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<v> = QQ[]
            sage: K.<u> = NumberField(v^2 + 3)
            sage: A.<x,y,z> = AffineSpace(K, 3)
            sage: C = Curve([z - u*x^2, y^2], A); C
            Affine Curve over Number Field in u with defining polynomial v^2 + 3
            defined by (-u)*x^2 + z, y^2

        ::

            sage: A.<x,y,z> = AffineSpace(GF(7), 3)
            sage: C = Curve([x^2 - z, z - 8*x], A); C
            Affine Curve over Finite Field of size 7 defined by x^2 - z, -x + z
        """
    def projective_closure(self, i: int = 0, PP=None):
        """
        Return the projective closure of this affine curve.

        INPUT:

        - ``i`` -- (default: 0) the index of the affine coordinate chart of the
          projective space that the affine ambient space of this curve embeds into

        - ``PP`` -- (default: ``None``) ambient projective space to compute the
          projective closure in; this is constructed if it is not given

        OUTPUT: a curve in projective space

        EXAMPLES::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: C = Curve([y-x^2,z-x^3], A)
            sage: C.projective_closure()
            Projective Curve over Rational Field defined by x1^2 - x0*x2,
            x1*x2 - x0*x3, x2^2 - x1*x3

        ::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: C = Curve([y - x^2, z - x^3], A)
            sage: C.projective_closure()
            Projective Curve over Rational Field defined by
            x1^2 - x0*x2, x1*x2 - x0*x3, x2^2 - x1*x3

        ::

            sage: A.<x,y> = AffineSpace(CC, 2)
            sage: C = Curve(y - x^3 + x - 1, A)
            sage: C.projective_closure(1)
            Projective Plane Curve over Complex Field with 53 bits of precision defined by
            x0^3 - x0*x1^2 + x1^3 - x1^2*x2

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: P.<u,v,w> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([y - x^2], A)
            sage: C.projective_closure(1, P).ambient_space() == P
            True
        """

class AffinePlaneCurve(AffineCurve):
    """
    Affine plane curves.
    """
    def __init__(self, A, f) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([x^3 - y^2], A); C
            Affine Plane Curve over Rational Field defined by x^3 - y^2

        ::

            sage: A.<x,y> = AffineSpace(CC, 2)
            sage: C = Curve([y^2 + x^2], A); C
            Affine Plane Curve over Complex Field with 53 bits of precision defined
            by x^2 + y^2
        """
    def divisor_of_function(self, r):
        """
        Return the divisor of a function on a curve.

        INPUT:

        - ``r`` -- a rational function on X

        OUTPUT:

        - ``list`` -- the divisor of r represented as a list of coefficients
          and points. (TODO: This will change to a more structural output in
          the future.)

        EXAMPLES::

            sage: F = GF(5)
            sage: P2 = AffineSpace(2, F, names='xy')
            sage: R = P2.coordinate_ring()
            sage: x, y = R.gens()
            sage: f = y^2 - x^9 - x
            sage: C = Curve(f)
            sage: K = FractionField(R)
            sage: r = 1/x
            sage: C.divisor_of_function(r)      # not implemented (broken)
                  [[-1, (0, 0, 1)]]
            sage: r = 1/x^3
            sage: C.divisor_of_function(r)      # not implemented (broken)
                  [[-3, (0, 0, 1)]]
        """
    def local_coordinates(self, pt, n):
        """
        Return local coordinates to precision n at the given point.

        Behaviour is flaky - some choices of `n` are worst that
        others.


        INPUT:

        - ``pt`` -- an F-rational point on X which is not a
          point of ramification for the projection (x,y) - x

        - ``n`` -- the number of terms desired

        OUTPUT: x = x0 + t y = y0 + power series in t

        EXAMPLES::

            sage: F = GF(5)
            sage: pt = (2,3)
            sage: R = PolynomialRing(F, 2, names = ['x','y'])
            sage: x,y = R.gens()
            sage: f = y^2 - x^9 - x
            sage: C = Curve(f)
            sage: C.local_coordinates(pt, 9)
            [t + 2, -2*t^12 - 2*t^11 + 2*t^9 + t^8 - 2*t^7 - 2*t^6 - 2*t^4 + t^3 - 2*t^2 - 2]
        """
    def plot(self, *args, **kwds):
        """
        Plot the real points on this affine plane curve.

        INPUT:

        - ``*args`` -- (optional) tuples (variable, minimum, maximum) for
          plotting dimensions

        - ``**kwds`` -- optional keyword arguments passed on to ``implicit_plot``

        EXAMPLES:

        A cuspidal curve::

            sage: R.<x, y> = QQ[]
            sage: C = Curve(x^3 - y^2)
            sage: C.plot()                                      # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        A 5-nodal curve of degree 11.  This example also illustrates
        some of the optional arguments::

            sage: # needs sage.plot
            sage: R.<x, y> = ZZ[]
            sage: C = Curve(32*x^2 - 2097152*y^11 + 1441792*y^9
            ....:            - 360448*y^7 + 39424*y^5 - 1760*y^3 + 22*y - 1)
            sage: C.plot((x, -1, 1), (y, -1, 1), plot_points=400)
            Graphics object consisting of 1 graphics primitive

        A line over `\\mathbf{RR}`::

            sage: # needs sage.symbolic sage.plot
            sage: R.<x, y> = RR[]
            sage: C = Curve(R(y - sqrt(2)*x))
            sage: C.plot()
            Graphics object consisting of 1 graphics primitive
        """
    def is_transverse(self, C, P):
        """
        Return whether the intersection of this curve with the curve ``C`` at the point ``P`` is transverse.

        The intersection at ``P`` is transverse if ``P`` is a nonsingular point of both curves, and if the
        tangents of the curves at ``P`` are distinct.

        INPUT:

        - ``C`` -- a curve in the ambient space of this curve

        - ``P`` -- a point in the intersection of both curves

        OUTPUT: boolean

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([x^2 + y^2 - 1], A)
            sage: D = Curve([x - 1], A)
            sage: Q = A([1,0])
            sage: C.is_transverse(D, Q)
            False

        ::

            sage: # needs sage.rings.number_field
            sage: R.<a> = QQ[]
            sage: K.<b> = NumberField(a^3 + 2)
            sage: A.<x,y> = AffineSpace(K, 2)
            sage: C = A.curve([x*y])
            sage: D = A.curve([y - b*x])
            sage: Q = A([0,0])
            sage: C.is_transverse(D, Q)
            False

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([y - x^3], A)
            sage: D = Curve([y + x], A)
            sage: Q = A([0,0])
            sage: C.is_transverse(D, Q)
            True
        """
    def multiplicity(self, P):
        """
        Return the multiplicity of this affine plane curve at the point ``P``.

        In the special case of affine plane curves, the multiplicity of an affine
        plane curve at the point (0,0) can be computed as the minimum of the degrees
        of the homogeneous components of its defining polynomial. To compute the
        multiplicity of a different point, a linear change of coordinates is used.

        This curve must be defined over a field. An error if raised if ``P`` is
        not a point on this curve.

        INPUT:

        - ``P`` -- a point in the ambient space of this curve

        OUTPUT: integer

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([y^2 - x^3], A)
            sage: Q1 = A([1,1])
            sage: C.multiplicity(Q1)
            1
            sage: Q2 = A([0,0])
            sage: C.multiplicity(Q2)
            2

        ::

            sage: # needs sage.rings.number_field
            sage: A.<x,y> = AffineSpace(QQbar,2)
            sage: C = Curve([-x^7 + (-7)*x^6 + y^6 + (-21)*x^5 + 12*y^5
            ....:            + (-35)*x^4 + 60*y^4 + (-35)*x^3 + 160*y^3
            ....:            + (-21)*x^2 + 240*y^2 + (-7)*x + 192*y + 63], A)
            sage: Q = A([-1,-2])
            sage: C.multiplicity(Q)
            6

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = A.curve([y^3 - x^3 + x^6])
            sage: Q = A([1,1])
            sage: C.multiplicity(Q)
            Traceback (most recent call last):
            ...
            TypeError: (=(1, 1)) is not a point on (=Affine Plane Curve over
            Rational Field defined by x^6 - x^3 + y^3)
        """
    def tangents(self, P, factor: bool = True):
        """
        Return the tangents of this affine plane curve at the point ``P``.

        The point ``P`` must be a point on this curve.

        INPUT:

        - ``P`` -- a point on this curve

        - ``factor`` -- boolean (default: ``True``); whether to attempt computing the
          polynomials of the individual tangent lines over the base field of this
          curve, or to just return the polynomial corresponding to the union of
          the tangent lines (which requires fewer computations)

        OUTPUT: list of polynomials in the coordinate ring of the ambient space

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: set_verbose(-1)
            sage: A.<x,y> = AffineSpace(QQbar, 2)
            sage: C = Curve([x^5*y^3 + 2*x^4*y^4 + x^3*y^5 + 3*x^4*y^3
            ....:            + 6*x^3*y^4 + 3*x^2*y^5 + 3*x^3*y^3
            ....:            + 6*x^2*y^4 + 3*x*y^5 + x^5 + 10*x^4*y
            ....:            + 40*x^3*y^2 + 81*x^2*y^3 + 82*x*y^4 + 33*y^5], A)
            sage: Q = A([0,0])
            sage: C.tangents(Q)
            [x + 3.425299577684700?*y,
             x + (1.949159013086856? + 1.179307909383728?*I)*y,
             x + (1.949159013086856? - 1.179307909383728?*I)*y,
             x + (1.338191198070795? + 0.2560234251008043?*I)*y,
             x + (1.338191198070795? - 0.2560234251008043?*I)*y]
            sage: C.tangents(Q, factor=False)
            [120*x^5 + 1200*x^4*y + 4800*x^3*y^2 + 9720*x^2*y^3 + 9840*x*y^4 + 3960*y^5]

        ::

            sage: # needs sage.rings.number_field
            sage: R.<a> = QQ[]
            sage: K.<b> = NumberField(a^2 - 3)
            sage: A.<x,y> = AffineSpace(K, 2)
            sage: C = Curve([(x^2 + y^2 - 2*x)^2 - x^2 - y^2], A)
            sage: Q = A([0,0])
            sage: C.tangents(Q)
            [x + (-1/3*b)*y, x + (1/3*b)*y]

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = A.curve([y^2 - x^3 - x^2])
            sage: Q = A([0,0])
            sage: C.tangents(Q)
            [x - y, x + y]

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = A.curve([y*x - x^4 + 2*x^2])
            sage: Q = A([1,1])
            sage: C.tangents(Q)
            Traceback (most recent call last):
            ...
            TypeError: (=(1, 1)) is not a point on (=Affine Plane Curve over
            Rational Field defined by -x^4 + 2*x^2 + x*y)
        """
    def is_ordinary_singularity(self, P):
        """
        Return whether the singular point ``P`` of this affine plane curve is
        an ordinary singularity.

        The point ``P`` is an ordinary singularity of this curve if it is a
        singular point, and if the tangents of this curve at ``P`` are
        distinct.

        INPUT:

        - ``P`` -- a point on this curve

        OUTPUT:

        ``True`` or ``False`` depending on whether ``P`` is or is not an ordinary
        singularity of this curve, respectively. An error is raised if ``P`` is
        not a singular point of this curve.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([y^2 - x^3], A)
            sage: Q = A([0,0])
            sage: C.is_ordinary_singularity(Q)
            False

        ::

            sage: # needs sage.rings.number_field
            sage: R.<a> = QQ[]
            sage: K.<b> = NumberField(a^2 - 3)
            sage: A.<x,y> = AffineSpace(K, 2)
            sage: C = Curve([(x^2 + y^2 - 2*x)^2 - x^2 - y^2], A)
            sage: Q = A([0,0])
            sage: C.is_ordinary_singularity(Q)
            True

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = A.curve([x^2*y - y^2*x + y^2 + x^3])
            sage: Q = A([-1,-1])
            sage: C.is_ordinary_singularity(Q)
            Traceback (most recent call last):
            ...
            TypeError: (=(-1, -1)) is not a singular point of (=Affine Plane Curve
            over Rational Field defined by x^3 + x^2*y - x*y^2 + y^2)
        """
    def rational_parameterization(self):
        """
        Return a rational parameterization of this curve.

        This curve must have rational coefficients and be absolutely irreducible (i.e. irreducible
        over the algebraic closure of the rational field). The curve must also be rational (have
        geometric genus zero).

        The rational parameterization may have coefficients in a quadratic extension of the rational
        field.

        OUTPUT: a birational map between `\\mathbb{A}^{1}` and this curve, given
        as a scheme morphism

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([y^2 - x], A)
            sage: C.rational_parameterization()
            Scheme morphism:
              From: Affine Space of dimension 1 over Rational Field
              To:   Affine Plane Curve over Rational Field defined by y^2 - x
              Defn: Defined on coordinates by sending (t) to
                    (t^2, t)

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([(x^2 + y^2 - 2*x)^2 - x^2 - y^2], A)
            sage: C.rational_parameterization()
            Scheme morphism:
              From: Affine Space of dimension 1 over Rational Field
              To:   Affine Plane Curve over Rational Field defined by x^4 +
            2*x^2*y^2 + y^4 - 4*x^3 - 4*x*y^2 + 3*x^2 - y^2
              Defn: Defined on coordinates by sending (t) to
                    ((-12*t^4 + 6*t^3 + 4*t^2 - 2*t)/(-25*t^4 + 40*t^3 - 26*t^2 +
            8*t - 1), (-9*t^4 + 12*t^3 - 4*t + 1)/(-25*t^4 + 40*t^3 - 26*t^2 + 8*t - 1))

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([x^2 + y^2 + 7], A)
            sage: C.rational_parameterization()
            Scheme morphism:
              From: Affine Space of dimension 1 over Number Field in a with defining polynomial a^2 + 7
              To:   Affine Plane Curve over Number Field in a with defining
            polynomial a^2 + 7 defined by x^2 + y^2 + 7
              Defn: Defined on coordinates by sending (t) to
                    ((-7*t^2 + 7)/((-a)*t^2 + (-a)), 14*t/((-a)*t^2 + (-a)))
        """

class AffineCurve_field(AffineCurve, AlgebraicScheme_subscheme_affine_field):
    """
    Affine curves over fields.
    """
    def __init__(self, A, X) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<v> = QQ[]
            sage: K.<u> = NumberField(v^2 + 3)
            sage: A.<x,y,z> = AffineSpace(K, 3)
            sage: C = Curve([z - u*x^2, y^2], A); C
            Affine Curve over Number Field in u with defining polynomial v^2 + 3
            defined by (-u)*x^2 + z, y^2

        ::

            sage: A.<x,y,z> = AffineSpace(GF(7), 3)
            sage: C = Curve([x^2 - z, z - 8*x], A); C
            Affine Curve over Finite Field of size 7 defined by x^2 - z, -x + z

        TESTS::

            sage: K.<x,y,z,t> = QQ[]
            sage: t1 = x^2*z^2 + y*t
            sage: t2 = y*z^2 + x^2*t
            sage: C = Curve([x^4 - y^2 - 19, z^4 - t^2 - 23, t1^2 - t2^2 - 19*23])
            Traceback (most recent call last):
            ...
            ValueError: defining equations (=[x^4 - y^2 - 19, z^4 - t^2 - 23,
            x^4*z^4 - y^2*z^4 - x^4*t^2 + y^2*t^2 - 437]) define a scheme of dimension 2 != 1
        """
    def projection(self, indices, AS=None):
        """
        Return the projection of this curve onto the coordinates specified by
        ``indices``.

        INPUT:

        - ``indices`` -- list or tuple of distinct integers specifying the
          indices of the coordinates to use in the projection. Can also be a list
          or tuple consisting of variables of the coordinate ring of the ambient
          space of this curve. If integers are used to specify the coordinates, 0
          denotes the first coordinate. The length of ``indices`` must be between
          two and one less than the dimension of the ambient space of this curve,
          inclusive.

        - ``AS`` -- (default: ``None``) the affine space the projected curve will
          be defined in. This space must be defined over the same base field as
          this curve, and must have dimension equal to the length of ``indices``.
          This space is constructed if not specified.

        OUTPUT: a tuple of

        - a scheme morphism from this curve to affine space of dimension equal
          to the number of coordinates specified in ``indices``

        - the affine subscheme that is the image of that morphism. If the image
          is a curve, the second element of the tuple will be a curve.

        EXAMPLES::

            sage: A.<x,y,z> = AffineSpace(QQ, 3)
            sage: C = Curve([y^7 - x^2 + x^3 - 2*z, z^2 - x^7 - y^2], A)
            sage: C.projection([0,1])
            (Scheme morphism:
               From: Affine Curve over Rational Field
                     defined by y^7 + x^3 - x^2 - 2*z, -x^7 - y^2 + z^2
               To:   Affine Space of dimension 2 over Rational Field
               Defn: Defined on coordinates by sending (x, y, z) to
                     (x, y),
             Affine Plane Curve over Rational Field defined by x1^14 + 2*x0^3*x1^7 -
            2*x0^2*x1^7 - 4*x0^7 + x0^6 - 2*x0^5 + x0^4 - 4*x1^2)
            sage: C.projection([0,1,3,4])
            Traceback (most recent call last):
            ...
            ValueError: (=[0, 1, 3, 4]) must be a list or tuple of length between 2
            and (=2), inclusive

        ::

            sage: A.<x,y,z,w> = AffineSpace(QQ, 4)
            sage: C = Curve([x - 2, y - 3, z - 1], A)
            sage: B.<a,b,c> = AffineSpace(QQ, 3)
            sage: C.projection([0,1,2], AS=B)
            (Scheme morphism:
               From: Affine Curve over Rational Field defined by x - 2, y - 3, z - 1
               To:   Affine Space of dimension 3 over Rational Field
               Defn: Defined on coordinates by sending (x, y, z, w) to
                     (x, y, z),
             Closed subscheme of Affine Space of dimension 3 over Rational Field defined by:
               c - 1,
               b - 3,
               a - 2)

        ::

            sage: A.<x,y,z,w,u> = AffineSpace(GF(11), 5)
            sage: C = Curve([x^3 - 5*y*z + u^2, x - y^2 + 3*z^2,
            ....:            w^2 + 2*u^3*y, y - u^2 + z*x], A)
            sage: B.<a,b,c> = AffineSpace(GF(11), 3)
            sage: proj1 = C.projection([1,2,4], AS=B); proj1
            (Scheme morphism:
               From: Affine Curve over Finite Field of size 11 defined by x^3 -
                     5*y*z + u^2, -y^2 + 3*z^2 + x, 2*y*u^3 + w^2, x*z - u^2 + y
               To:   Affine Space of dimension 3 over Finite Field of size 11
               Defn: Defined on coordinates by sending (x, y, z, w, u) to
                     (y, z, u),
             Affine Curve over Finite Field of size 11 defined by a^2*b - 3*b^3 -
            c^2 + a, c^6 - 5*a*b^4 + b^3*c^2 - 3*a*c^4 + 3*a^2*c^2 - a^3, a^2*c^4 -
            3*b^2*c^4 - 2*a^3*c^2 - 5*a*b^2*c^2 + a^4 - 5*a*b^3 + 2*b^4 + b^2*c^2 -
            3*b*c^2 + 3*a*b, a^4*c^2 + 2*b^4*c^2 - a^5 - 2*a*b^4 + 5*b*c^4 + a*b*c^2
            - 5*a*b^2 + 4*b^3 + b*c^2 + 5*c^2 - 5*a, a^6 - 5*b^6 - 5*b^3*c^2 +
            5*a*b^3 + 2*c^4 - 4*a*c^2 + 2*a^2 - 5*a*b + c^2)
            sage: proj1[1].ambient_space() is B
            True
            sage: proj2 = C.projection([1,2,4])
            sage: proj2[1].ambient_space() is B
            False
            sage: C.projection([1,2,3,5], AS=B)
            Traceback (most recent call last):
            ...
            TypeError: (=Affine Space of dimension 3 over Finite Field of size 11)
            must have dimension (=4)

        ::

            sage: A.<x,y,z,w> = AffineSpace(QQ, 4)
            sage: C = A.curve([x*y - z^3, x*z - w^3, w^2 - x^3])
            sage: C.projection([y,z])
            (Scheme morphism:
               From: Affine Curve over Rational Field defined by
                     -z^3 + x*y, -w^3 + x*z, -x^3 + w^2
               To:   Affine Space of dimension 2 over Rational Field
               Defn: Defined on coordinates by sending (x, y, z, w) to (y, z),
             Affine Plane Curve over Rational Field defined by x1^23 - x0^7*x1^4)
            sage: B.<x,y,z> = AffineSpace(QQ, 3)
            sage: C.projection([x,y,z], AS=B)
            (Scheme morphism:
               From: Affine Curve over Rational Field defined by
                     -z^3 + x*y, -w^3 + x*z, -x^3 + w^2
               To:   Affine Space of dimension 3 over Rational Field
               Defn: Defined on coordinates by sending (x, y, z, w) to
                     (x, y, z),
             Affine Curve over Rational Field defined by
             z^3 - x*y, x^8 - x*z^2, x^7*z^2 - x*y*z)
            sage: C.projection([y,z,z])
            Traceback (most recent call last):
            ...
            ValueError: (=[y, z, z]) must be a list or tuple of distinct indices or
            variables
        """
    def plane_projection(self, AP=None):
        """
        Return a projection of this curve into an affine plane so that the
        image of the projection is a plane curve.

        INPUT:

        - ``AP`` -- (default: ``None``) the affine plane to project this curve
          into. This space must be defined over the same base field as this
          curve, and must have dimension two. This space will be constructed if
          not specified.

        OUTPUT: a tuple of

        - a scheme morphism from this curve into an affine plane

        - the plane curve that defines the image of that morphism

        EXAMPLES::

            sage: A.<x,y,z,w> = AffineSpace(QQ, 4)
            sage: C = Curve([x^2 - y*z*w, z^3 - w, w + x*y - 3*z^3], A)
            sage: C.plane_projection()
            (Scheme morphism:
              From: Affine Curve over Rational Field defined by
                    -y*z*w + x^2, z^3 - w, -3*z^3 + x*y + w
              To:   Affine Space of dimension 2 over Rational Field
              Defn: Defined on coordinates by sending (x, y, z, w) to (x, y),
             Affine Plane Curve over Rational Field defined by
             x0^2*x1^7 - 16*x0^4)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<a> = QQ[]
            sage: K.<b> = NumberField(a^2 + 2)
            sage: A.<x,y,z> = AffineSpace(K, 3)
            sage: C = A.curve([x - b, y - 2])
            sage: B.<a,b> = AffineSpace(K, 2)
            sage: proj1 = C.plane_projection(AP=B)
            sage: proj1
            (Scheme morphism:
               From: Affine Curve over Number Field in b
                     with defining polynomial a^2 + 2 defined by x + (-b), y - 2
               To:   Affine Space of dimension 2 over Number Field in b
                     with defining polynomial a^2 + 2
               Defn: Defined on coordinates by sending (x, y, z) to
                     (x, z),
             Affine Plane Curve over Number Field in b
             with defining polynomial a^2 + 2 defined by a + (-b))
            sage: proj1[1].ambient_space() is B
            True
            sage: proj2 = C.plane_projection()
            sage: proj2[1].ambient_space() is B
            False
        """
    def blowup(self, P=None):
        """
        Return the blow up of this affine curve at the point ``P``.

        The blow up is described by affine charts. This curve must be irreducible.

        INPUT:

        - ``P`` -- (default: ``None``) a point on this curve at which to blow up;
          if ``None``, then ``P`` is taken to be the origin

        OUTPUT: a tuple of

        - a tuple of curves in affine space of the same dimension as the
          ambient space of this curve, which define the blow up in each affine
          chart.

        - a tuple of tuples such that the j-th element of the i-th tuple is the
          transition map from the i-th affine patch to the j-th affine patch.

        - a tuple consisting of the restrictions of the projection map from the
          blow up back to the original curve, restricted to each affine patch.
          There the i-th element will be the projection from the i-th affine patch.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([y^2 - x^3], A)
            sage: C.blowup()
            ((Affine Plane Curve over Rational Field defined by s1^2 - x,
              Affine Plane Curve over Rational Field defined by y*s0^3 - 1),
            ([Scheme endomorphism of Affine Plane Curve over Rational Field
               defined by s1^2 - x
                Defn: Defined on coordinates by sending (x, s1) to (x, s1),
              Scheme morphism:
                From: Affine Plane Curve over Rational Field defined by s1^2 - x
                To:   Affine Plane Curve over Rational Field defined by y*s0^3 - 1
                Defn: Defined on coordinates by sending (x, s1) to (x*s1, 1/s1)],
             [Scheme morphism:
                From: Affine Plane Curve over Rational Field defined by y*s0^3 - 1
                To:   Affine Plane Curve over Rational Field defined by s1^2 - x
                Defn: Defined on coordinates by sending (y, s0) to (y*s0, 1/s0),
              Scheme endomorphism of Affine Plane Curve over Rational Field
               defined by y*s0^3 - 1
                Defn: Defined on coordinates by sending (y, s0) to (y, s0)]),
            (Scheme morphism:
               From: Affine Plane Curve over Rational Field defined by s1^2 - x
               To:   Affine Plane Curve over Rational Field defined by -x^3 + y^2
               Defn: Defined on coordinates by sending (x, s1) to (x, x*s1),
             Scheme morphism:
               From: Affine Plane Curve over Rational Field defined by y*s0^3 - 1
               To:   Affine Plane Curve over Rational Field defined by -x^3 + y^2
               Defn: Defined on coordinates by sending (y, s0) to (y*s0, y)))

        ::

            sage: # needs sage.rings.number_field
            sage: K.<a> = QuadraticField(2)
            sage: A.<x,y,z> = AffineSpace(K, 3)
            sage: C = Curve([y^2 - a*x^5, x - z], A)
            sage: B = C.blowup()
            sage: B[0]
            (Affine Curve over Number Field in a with defining polynomial x^2 - 2
              with a = 1.414213562373095? defined by s2 - 1, 2*x^3 + (-a)*s1^2,
             Affine Curve over Number Field in a with defining polynomial x^2 - 2
              with a = 1.414213562373095? defined by s0 - s2, 2*y^3*s2^5 + (-a),
             Affine Curve over Number Field in a with defining polynomial x^2 - 2
              with a = 1.414213562373095? defined by s0 - 1, 2*z^3 + (-a)*s1^2)
            sage: B[1][0][2]
            Scheme morphism:
              From: Affine Curve over Number Field in a
                    with defining polynomial x^2 - 2 with a = 1.414213562373095?
                    defined by s2 - 1, 2*x^3 + (-a)*s1^2
              To:   Affine Curve over Number Field in a
                    with defining polynomial x^2 - 2 with a = 1.414213562373095?
                    defined by s0 - 1, 2*z^3 + (-a)*s1^2
              Defn: Defined on coordinates by sending (x, s1, s2) to
                    (x*s2, 1/s2, s1/s2)
            sage: B[1][2][0]
            Scheme morphism:
              From: Affine Curve over Number Field in a
                    with defining polynomial x^2 - 2 with a = 1.414213562373095?
                    defined by s0 - 1, 2*z^3 + (-a)*s1^2
              To:   Affine Curve over Number Field in a
                    with defining polynomial x^2 - 2 with a = 1.414213562373095?
                    defined by s2 - 1, 2*x^3 + (-a)*s1^2
              Defn: Defined on coordinates by sending (z, s0, s1) to
                    (z*s0, s1/s0, 1/s0)
            sage: B[2]
            (Scheme morphism:
               From: Affine Curve over Number Field in a
                     with defining polynomial x^2 - 2 with a = 1.414213562373095?
                     defined by s2 - 1, 2*x^3 + (-a)*s1^2
               To:   Affine Curve over Number Field in a
                     with defining polynomial x^2 - 2 with a = 1.414213562373095?
                     defined by (-a)*x^5 + y^2, x - z
               Defn: Defined on coordinates by sending (x, s1, s2) to
                     (x, x*s1, x*s2),
             Scheme morphism:
               From: Affine Curve over Number Field in a
                     with defining polynomial x^2 - 2 with a = 1.414213562373095?
                     defined by s0 - s2, 2*y^3*s2^5 + (-a)
               To:   Affine Curve over Number Field in a
                     with defining polynomial x^2 - 2 with a = 1.414213562373095?
                     defined by (-a)*x^5 + y^2, x - z
               Defn: Defined on coordinates by sending (y, s0, s2) to
                     (y*s0, y, y*s2),
             Scheme morphism:
               From: Affine Curve over Number Field in a
                     with defining polynomial x^2 - 2 with a = 1.414213562373095?
                     defined by s0 - 1, 2*z^3 + (-a)*s1^2
               To:   Affine Curve over Number Field in a
                     with defining polynomial x^2 - 2 with a = 1.414213562373095?
                     defined by (-a)*x^5 + y^2, x - z
               Defn: Defined on coordinates by sending (z, s0, s1) to
                     (z*s0, z*s1, z))

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = A.curve((y - 3/2)^3 - (x + 2)^5 - (x + 2)^6)
            sage: Q = A([-2,3/2])
            sage: C.blowup(Q)
            ((Affine Plane Curve over Rational Field
               defined by x^3 - s1^3 + 7*x^2 + 16*x + 12,
              Affine Plane Curve over Rational Field
               defined by 8*y^3*s0^6 - 36*y^2*s0^6 + 8*y^2*s0^5
                          + 54*y*s0^6 - 24*y*s0^5 - 27*s0^6 + 18*s0^5 - 8),
             ([Scheme endomorphism of Affine Plane Curve over Rational Field
                defined by x^3 - s1^3 + 7*x^2 + 16*x + 12
                 Defn: Defined on coordinates by sending (x, s1) to (x, s1),
               Scheme morphism:
                 From: Affine Plane Curve over Rational Field
                       defined by x^3 - s1^3 + 7*x^2 + 16*x + 12
                 To:   Affine Plane Curve over Rational Field
                       defined by 8*y^3*s0^6 - 36*y^2*s0^6 + 8*y^2*s0^5
                                  + 54*y*s0^6 - 24*y*s0^5 - 27*s0^6 + 18*s0^5 - 8
                 Defn: Defined on coordinates by sending (x, s1) to
                       (x*s1 + 2*s1 + 3/2, 1/s1)],
              [Scheme morphism:
                 From: Affine Plane Curve over Rational Field
                       defined by 8*y^3*s0^6 - 36*y^2*s0^6 + 8*y^2*s0^5
                                  + 54*y*s0^6 - 24*y*s0^5 - 27*s0^6 + 18*s0^5 - 8
                 To:   Affine Plane Curve over Rational Field
                       defined by x^3 - s1^3 + 7*x^2 + 16*x + 12
                 Defn: Defined on coordinates by sending (y, s0) to
                       (y*s0 - 3/2*s0 - 2, 1/s0),
               Scheme endomorphism of Affine Plane Curve over Rational Field
                defined by 8*y^3*s0^6 - 36*y^2*s0^6 + 8*y^2*s0^5 + 54*y*s0^6
                           - 24*y*s0^5 - 27*s0^6 + 18*s0^5 - 8
                 Defn: Defined on coordinates by sending (y, s0) to (y, s0)]),
             (Scheme morphism:
                From: Affine Plane Curve over Rational Field
                      defined by x^3 - s1^3 + 7*x^2 + 16*x + 12
                To:   Affine Plane Curve over Rational Field
                      defined by -x^6 - 13*x^5 - 70*x^4 - 200*x^3 + y^3
                                 - 320*x^2 - 9/2*y^2 - 272*x + 27/4*y - 795/8
                Defn: Defined on coordinates by sending (x, s1) to
                      (x, x*s1 + 2*s1 + 3/2),
              Scheme morphism:
                From: Affine Plane Curve over Rational Field
                      defined by 8*y^3*s0^6 - 36*y^2*s0^6 + 8*y^2*s0^5
                                 + 54*y*s0^6 - 24*y*s0^5 - 27*s0^6 + 18*s0^5 - 8
                To:   Affine Plane Curve over Rational Field
                      defined by -x^6 - 13*x^5 - 70*x^4 - 200*x^3 + y^3
                                 - 320*x^2 - 9/2*y^2 - 272*x + 27/4*y - 795/8
                Defn: Defined on coordinates by sending (y, s0) to
                      (y*s0 - 3/2*s0 - 2, y)))

        ::

            sage: A.<x,y,z,w> = AffineSpace(QQ, 4)
            sage: C = A.curve([((x + 1)^2 + y^2)^3 - 4*(x + 1)^2*y^2, y - z, w - 4])
            sage: Q = C([-1,0,0,4])
            sage: B = C.blowup(Q)
            sage: B[0]
            (Affine Curve over Rational Field defined by s3, s1 - s2,
              x^2*s2^6 + 2*x*s2^6 + 3*x^2*s2^4 + s2^6 + 6*x*s2^4
              + 3*x^2*s2^2 + 3*s2^4 + 6*x*s2^2 + x^2 - s2^2 + 2*x + 1,
             Affine Curve over Rational Field defined by s3, s2 - 1,
              y^2*s0^6 + 3*y^2*s0^4 + 3*y^2*s0^2 + y^2 - 4*s0^2,
             Affine Curve over Rational Field defined by s3, s1 - 1,
              z^2*s0^6 + 3*z^2*s0^4 + 3*z^2*s0^2 + z^2 - 4*s0^2,
             Closed subscheme of Affine Space of dimension 4 over Rational Field
              defined by: 1)
            sage: Q = A([6,2,3,1])
            sage: B = C.blowup(Q)
            Traceback (most recent call last):
            ...
            TypeError: (=(6, 2, 3, 1)) must be a point on this curve

        ::

            sage: # needs sage.rings.number_field
            sage: A.<x,y> = AffineSpace(QuadraticField(-1), 2)
            sage: C = A.curve([y^2 + x^2])
            sage: C.blowup()
            Traceback (most recent call last):
            ...
            TypeError: this curve must be irreducible
        """
    def resolution_of_singularities(self, extend: bool = False):
        """
        Return a nonsingular model for this affine curve created by blowing up
        its singular points.

        The nonsingular model is given as a collection of affine patches that
        cover it. If ``extend`` is ``False`` and if the base field is a number
        field, or if the base field is a finite field, the model returned may
        have singularities with coordinates not contained in the base field. An
        error is returned if this curve is already nonsingular, or if it has no
        singular points over its base field. This curve must be irreducible,
        and must be defined over a number field or finite field.

        INPUT:

        - ``extend`` -- boolean (default: ``False``); specifies whether to
          extend the base field when necessary to find all singular points when
          this curve is defined over a number field. If ``extend`` is
          ``False``, then only singularities with coordinates in the base field
          of this curve will be resolved. However, setting ``extend`` to
          ``True`` will slow down computations.

        OUTPUT: a tuple of

        - a tuple of curves in affine space of the same dimension as the
          ambient space of this curve, which represent affine patches of the
          resolution of singularities.

        - a tuple of tuples such that the j-th element of the i-th tuple is the
          transition map from the i-th patch to the j-th patch.

        - a tuple consisting of birational maps from the patches back to the
          original curve that were created by composing the projection maps
          generated from the blow up computations. There the i-th element will
          be a map from the i-th patch.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([y^2 - x^3], A)
            sage: C.resolution_of_singularities()
            ((Affine Plane Curve over Rational Field defined by s1^2 - x,
              Affine Plane Curve over Rational Field defined by y*s0^3 - 1),
             ((Scheme endomorphism of Affine Plane Curve over Rational Field
                defined by s1^2 - x
                 Defn: Defined on coordinates by sending (x, s1) to (x, s1),
               Scheme morphism:
                 From: Affine Plane Curve over Rational Field defined by s1^2 - x
                 To:   Affine Plane Curve over Rational Field defined by y*s0^3 - 1
                 Defn: Defined on coordinates by sending (x, s1) to (x*s1, 1/s1)),
              (Scheme morphism:
                 From: Affine Plane Curve over Rational Field defined by y*s0^3 - 1
                 To:   Affine Plane Curve over Rational Field defined by s1^2 - x
                 Defn: Defined on coordinates by sending (y, s0) to (y*s0, 1/s0),
               Scheme endomorphism of Affine Plane Curve over Rational Field
                defined by y*s0^3 - 1
                 Defn: Defined on coordinates by sending (y, s0) to (y, s0))),
             (Scheme morphism:
                From: Affine Plane Curve over Rational Field defined by s1^2 - x
                To:   Affine Plane Curve over Rational Field defined by -x^3 + y^2
                Defn: Defined on coordinates by sending (x, s1) to (x, x*s1),
              Scheme morphism:
                From: Affine Plane Curve over Rational Field defined by y*s0^3 - 1
                To:   Affine Plane Curve over Rational Field defined by -x^3 + y^2
                Defn: Defined on coordinates by sending (y, s0) to (y*s0, y)))

        ::

            sage: # needs sage.rings.number_field
            sage: set_verbose(-1)
            sage: K.<a> = QuadraticField(3)
            sage: A.<x,y> = AffineSpace(K, 2)
            sage: C = A.curve(x^4 + 2*x^2 + a*y^3 + 1)
            sage: C.resolution_of_singularities(extend=True)[0]         # long time (2 s)
            (Affine Plane Curve over Number Field in a0
              with defining polynomial y^4 - 4*y^2 + 16
              defined by 24*x^2*ss1^3 + 24*ss1^3 + (a0^3 - 8*a0),
             Affine Plane Curve over Number Field in a0
              with defining polynomial y^4 - 4*y^2 + 16
              defined by 24*s1^2*ss0 + (a0^3 - 8*a0)*ss0^2 + (-6*a0^3)*s1,
             Affine Plane Curve over Number Field in a0
              with defining polynomial y^4 - 4*y^2 + 16
              defined by 8*y^2*s0^4 + (4*a0^3)*y*s0^3 - 32*s0^2 + (a0^3 - 8*a0)*y)

        ::

            sage: A.<x,y,z> = AffineSpace(GF(5), 3)
            sage: C = Curve([y - x^3, (z - 2)^2 - y^3 - x^3], A)
            sage: R = C.resolution_of_singularities()
            sage: R[0]
            (Affine Curve over Finite Field of size 5
              defined by x^2 - s1, s1^4 - x*s2^2 + s1, x*s1^3 - s2^2 + x,
             Affine Curve over Finite Field of size 5
              defined by y*s2^2 - y^2 - 1, s2^4 - s0^3 - y^2 - 2, y*s0^3 - s2^2 + y,
             Affine Curve over Finite Field of size 5
              defined by s0^3*s1 + z*s1^3 + s1^4 - 2*s1^3 - 1,
                         z*s0^3 + z*s1^3 - 2*s0^3 - 2*s1^3 - 1,
                         z^2*s1^3 + z*s1^3 - s1^3 - z + s1 + 2)

        ::

            sage: A.<x,y,z,w> = AffineSpace(QQ, 4)
            sage: C = A.curve([((x - 2)^2 + y^2)^2 - (x - 2)^2 - y^2 + (x - 2)^3,
            ....:              z - y - 7, w - 4])
            sage: B = C.resolution_of_singularities()
            sage: B[0]
            (Affine Curve over Rational Field defined by s3, s1 - s2,
              x^2*s2^4 - 4*x*s2^4 + 2*x^2*s2^2 + 4*s2^4 - 8*x*s2^2
              + x^2 + 7*s2^2 - 3*x + 1,
             Affine Curve over Rational Field defined by s3, s2 - 1,
              y^2*s0^4 + 2*y^2*s0^2 + y*s0^3 + y^2 - s0^2 - 1,
             Affine Curve over Rational Field defined by s3, s1 - 1,
              z^2*s0^4 - 14*z*s0^4 + 2*z^2*s0^2 + z*s0^3 + 49*s0^4
              - 28*z*s0^2 - 7*s0^3 + z^2 + 97*s0^2 - 14*z + 48,
             Closed subscheme of Affine Space of dimension 4 over Rational Field
              defined by: 1)

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve([y - x^2 + 1], A)
            sage: C.resolution_of_singularities()
            Traceback (most recent call last):
            ...
            TypeError: this curve is already nonsingular

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = A.curve([(x^2 + y^2 - y - 2)*(y - x^2 + 2) + y^3])
            sage: C.resolution_of_singularities()
            Traceback (most recent call last):
            ...
            TypeError: this curve has no singular points over its base field. If
            working over a number field use extend=True
        """
    def tangent_line(self, p):
        """
        Return the tangent line at the point ``p``.

        INPUT:

        - ``p`` -- a rational point of the curve

        EXAMPLES::

            sage: A3.<x,y,z> = AffineSpace(3, QQ)
            sage: C = Curve([x + y + z, x^2 - y^2*z^2 + z^3])
            sage: p = C(0,0,0)
            sage: C.tangent_line(p)
            Traceback (most recent call last):
            ...
            ValueError: the curve is not smooth at (0, 0, 0)
            sage: p = C(1,0,-1)
            sage: C.tangent_line(p)
            Affine Curve over Rational Field defined by x + y + z, 2*x + 3*z + 1

        We check that the tangent line at ``p`` is the tangent space at ``p``,
        translated to ``p``. ::

            sage: Tp = C.tangent_space(p)
            sage: Tp
            Closed subscheme of Affine Space of dimension 3 over Rational Field
             defined by: x + y + z, 2*x + 3*z
            sage: phi = A3.translation(A3.origin(), p)
            sage: T = phi * Tp.embedding_morphism()
            sage: T.image()
            Closed subscheme of Affine Space of dimension 3 over Rational Field
             defined by: -2*y + z + 1, x + y + z
            sage: _ == C.tangent_line(p)
            True
        """

class AffinePlaneCurve_field(AffinePlaneCurve, AffineCurve_field):
    """
    Affine plane curves over fields.
    """
    def has_vertical_asymptote(self) -> bool:
        """
        Check if the curve is not a line and has vertical asymptotes.

        EXAMPLES::

            sage: A2.<x,y> = AffineSpace(2, QQ)
            sage: Curve(x).has_vertical_asymptote()
            False
            sage: Curve(y^2 * x + x + y).has_vertical_asymptote()
            True
        """
    def is_vertical_line(self) -> bool:
        """
        Check if the curve is a vertical line.

        EXAMPLES::

            sage: A2.<x, y> = AffineSpace(2, QQ)
            sage: Curve(x - 1).is_vertical_line()
            True
            sage: Curve(x - y).is_vertical_line()
            False
            sage: Curve(y^2 * x + x + y).is_vertical_line()
            False
        """
    @cached_method
    def fundamental_group(self, simplified: bool = True, puiseux: bool = True):
        """
        Return a presentation of the fundamental group of the complement
        of ``self``.

        INPUT:

        - ``simplified`` -- boolean (default: ``True``); to simplify the presentation

        - ``puiseux`` -- boolean (default: ``True``); to decide if the
          presentation is constructed in the classical way or using Puiseux
          shortcut

        OUTPUT:

        A presentation with generators `x_1, \\dots, x_d` and relations. If ``puiseux``
        is ``False`` the relations are `(x_j\\cdot \\tau)\\cdot x_j^{-1}` for `1\\leq j<d`
        and `tau` a braid in the braid monodromy; finally the presentation
        is simplified. If ``puiseux`` is ``True``, each
        `tau` is decomposed as `\\alpha^{-1}\\cdot\\beta\\cdot\\alpha`, where `\\beta` is
        a positive braid; the relations are `((x_j\\cdot \\beta)\\cdot x_j^{-1})\\cdot \\alpha`
        where `j` is an integer of the ``Tietze`` word of `\\beta`. This presentation
        is not simplified by default since it represents the homotopy type of
        the complement of the curve.

        .. NOTE::

            The curve must be defined over the rationals or a number field
            with an embedding over `\\QQbar`. This functionality requires
            the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: # needs sirocco
            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = A.curve(y^2 - x^3 - x^2)
            sage: C.fundamental_group(puiseux=False)
            Finitely presented group < x0 |  >
            sage: bm = C.braid_monodromy()
            sage: g = C.fundamental_group(simplified=False)
            sage: g.sorted_presentation()
            Finitely presented group < x0, x1 | x1^-1*x0^-1*x1*x0, x1^-1*x0 >
            sage: g.simplified()
            Finitely presented group < x0 |  >

        In the case of number fields, they need to have an embedding
        to the algebraic field::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ)
            sage: a = QQ[x](x^2 + 5).roots(QQbar)[0][0]
            sage: F = NumberField(a.minpoly(), 'a', embedding=a)
            sage: F.inject_variables()
            Defining a
            sage: A.<x,y> = AffineSpace(F, 2)
            sage: C = A.curve(y^2 - a*x^3 - x^2)
            sage: C.fundamental_group()                     # needs sirocco
            Finitely presented group < x0 |  >
            sage: C = A.curve(x * (x - 1))
            sage: C.fundamental_group()                     # needs sirocco
            Finitely presented group < x0, x1 |  >
        """
    @cached_method
    def braid_monodromy(self):
        """
        Compute the braid monodromy of a projection of the curve.

        OUTPUT:

        A list of braids. The braids correspond to paths based in the same point;
        each of this paths is the conjugated of a loop around one of the points
        in the discriminant of the projection of ``self``.

        .. NOTE::

            The projection over the `x` axis is used if there are no vertical asymptotes.
            Otherwise, a linear change of variables is done to fall into the previous case.

        .. NOTE::

            This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = A.curve((x^2-y^3)*(x+3*y-5))
            sage: C.braid_monodromy()                                   # needs sirocco
            [s1*s0*(s1*s2)^2*s0*s2^2*s0^-1*(s2^-1*s1^-1)^2*s0^-1*s1^-1,
             s1*s0*(s1*s2)^2*(s0*s2^-1*s1*s2*s1*s2^-1)^2*(s2^-1*s1^-1)^2*s0^-1*s1^-1,
             s1*s0*(s1*s2)^2*s2*s1^-1*s2^-1*s1^-1*s0^-1*s1^-1,
             s1*s0*s2*s0^-1*s2*s1^-1]
            sage: T.<t> = QQ[]
            sage: K.<a> = NumberField(t^3 + 2, 'a')
            sage: A.<x, y> = AffineSpace(K, 2)
            sage: Curve(y^2 + a * x).braid_monodromy()
            Traceback (most recent call last):
            ...
            NotImplementedError: the base field must have an embedding to the algebraic field
        """
    def riemann_surface(self, **kwargs):
        """
        Return the complex Riemann surface determined by this curve.

        OUTPUT: a :class:`~sage.schemes.riemann_surfaces.riemann_surface.RiemannSurface` object

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: C = Curve(x^3 + 3*y^3 + 5)
            sage: C.riemann_surface()
            Riemann surface defined by polynomial f = x^3 + 3*y^3 + 5 = 0,
             with 53 bits of precision
        """

class AffinePlaneCurve_finite_field(AffinePlaneCurve_field):
    """
    Affine plane curves over finite fields.
    """
    def riemann_roch_basis(self, D):
        '''
        Return a basis of the Riemann-Roch space of the divisor ``D``.

        This interfaces with Singular\'s Brill-Noether command.

        This curve is assumed to be a plane curve defined by a polynomial
        equation `f(x,y) = 0` over a prime finite field `F = GF(p)` in 2
        variables `x,y` representing a curve `X: f(x,y) = 0` having `n`
        `F`-rational points (see the Sage function ``places_on_curve``)

        INPUT:

        - ``D`` -- an `n`-tuple of integers `(d_1, ..., d_n)` representing the
          divisor `Div = d_1P_1 + \\dots + d_nP_n`, where `X(F) = \\{P_1, \\dots,
          P_n\\}`.  The ordering is that dictated by ``places_on_curve``.

        OUTPUT: a basis of `L(Div)`.

        EXAMPLES::

            sage: R = PolynomialRing(GF(5), 2, names=["x","y"])
            sage: x, y = R.gens()
            sage: f = y^2 - x^9 - x
            sage: C = Curve(f)
            sage: D = [6,0,0,0,0,0]
            sage: C.riemann_roch_basis(D)
            [1, (-x*z^5 + y^2*z^4)/x^6, (-x*z^6 + y^2*z^5)/x^7, (-x*z^7 + y^2*z^6)/x^8]
        '''
    def rational_points(self, algorithm: str = 'enum'):
        """
        Return sorted list of all rational points on this curve.

        INPUT:

        - ``algorithm`` -- possible choices:

           +  ``'enum'`` -- use *very* naive point enumeration to find all
              rational points on this curve over a finite field.

           +  ``'bn'`` -- via Singular's Brill-Noether package.

           +  ``'all'`` -- use all implemented algorithms and verify that they
              give the same answer, then return it

        .. NOTE::

           The Brill-Noether package does not always work. When it fails, a
           :exc:`RuntimeError` exception is raised.

        EXAMPLES::

            sage: x, y = (GF(5)['x,y']).gens()
            sage: f = y^2 - x^9 - x
            sage: C = Curve(f); C
            Affine Plane Curve over Finite Field of size 5 defined by -x^9 + y^2 - x
            sage: C.rational_points(algorithm='bn')
            [(0, 0), (2, 2), (2, 3), (3, 1), (3, 4)]
            sage: C = Curve(x - y + 1)
            sage: C.rational_points()
            [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]

        We compare Brill-Noether and enumeration::

            sage: x, y = (GF(17)['x,y']).gens()
            sage: C = Curve(x^2 + y^5 + x*y - 19)
            sage: v = C.rational_points(algorithm='bn')
            sage: w = C.rational_points(algorithm='enum')
            sage: len(v)
            20
            sage: v == w
            True

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(2, GF(9,'a'))
            sage: C = Curve(x^2 + y^2 - 1); C
            Affine Plane Curve over Finite Field in a of size 3^2
             defined by x^2 + y^2 - 1
            sage: C.rational_points()
            [(0, 1), (0, 2), (1, 0), (2, 0), (a + 1, a + 1),
             (a + 1, 2*a + 2), (2*a + 2, a + 1), (2*a + 2, 2*a + 2)]
        """

class IntegralAffineCurve(AffineCurve_field):
    """
    Base class for integral affine curves.
    """
    def function_field(self):
        """
        Return the function field of the curve.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve(x^3 - y^2 - x^4 - y^4)
            sage: C.function_field()
            Function field in y defined by y^4 + y^2 + x^4 - x^3

        ::

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(GF(8), 2)
            sage: C = Curve(x^5 + y^5 + x*y + 1)
            sage: C.function_field()
            Function field in y defined by y^5 + x*y + x^5 + 1
        """
    def __call__(self, *args):
        """
        Return a rational point, a pointset or a function depending on ``args``.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(GF(8), 2)
            sage: C = Curve(x^5 + y^5 + x*y + 1)
            sage: C(1,1)
            (1, 1)
            sage: C(x/y)
            (x/(x^5 + 1))*y^4 + x^2/(x^5 + 1)
            sage: C(GF(8^2))
            Set of rational points of Closed subscheme of Affine Space of dimension 2
            over Finite Field in z6 of size 2^6 defined by: x^5 + y^5 + x*y + 1

        ::

            sage: A.<x,y,z> = AffineSpace(GF(11), 3)
            sage: C = Curve([x*z - y^2, y - z^2, x - y*z], A)
            sage: C([0,0,0])
            (0, 0, 0)
            sage: C(y)
            z^2
            sage: C(A.coordinate_ring()(y))
            z^2
        """
    def function(self, f):
        """
        Return the function field element coerced from ``f``.

        INPUT:

        - ``f`` -- an element of the fraction field of the coordinate ring of
          the ambient space or the coordinate ring of the curve

        OUTPUT: an element of the function field of this curve

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(GF(8), 2)
            sage: C = Curve(x^5 + y^5 + x*y + 1)
            sage: f = C.function(x/y)
            sage: f
            (x/(x^5 + 1))*y^4 + x^2/(x^5 + 1)
            sage: df = f.differential(); df
            ((1/(x^10 + 1))*y^4 + x^6/(x^10 + 1)) d(x)
            sage: df.divisor()                  # long time
            2*Place (1/x, 1/x^4*y^4 + 1/x^3*y^3 + 1/x^2*y^2 + 1/x*y + 1)
             + 2*Place (1/x, 1/x*y + 1)
             - 2*Place (x + 1, y)
             - 2*Place (x^4 + x^3 + x^2 + x + 1, y)
        """
    def coordinate_functions(self):
        """
        Return the coordinate functions.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(GF(8), 2)
            sage: C = Curve(x^5 + y^5 + x*y + 1)
            sage: x, y = C.coordinate_functions()
            sage: x^5 + y^5 + x*y + 1
            0
        """
    def pull_from_function_field(self, f):
        """
        Return the fraction corresponding to ``f``.

        INPUT:

        - ``f`` -- an element of the function field

        OUTPUT:

        A fraction of polynomials in the coordinate ring of the ambient space
        of the curve.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(GF(8), 2)
            sage: C = Curve(x^5 + y^5 + x*y + 1)
            sage: F = C.function_field()
            sage: C.pull_from_function_field(F.gen())
            y
            sage: C.pull_from_function_field(F.one())
            1
            sage: C.pull_from_function_field(F.zero())
            0
            sage: f1 = F.gen()
            sage: f2 = F.base_ring().gen()
            sage: C.function(C.pull_from_function_field(f1)) == f1
            True
            sage: C.function(C.pull_from_function_field(f2)) == f2
            True
        """
    def singular_closed_points(self):
        """
        Return the singular closed points of the curve.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(GF(7^2), 2)
            sage: C = Curve(x^2 - x^4 - y^4)
            sage: C.singular_closed_points()
            [Point (x, y)]

        ::

            sage: A.<x,y,z> = AffineSpace(GF(11), 3)
            sage: C = Curve([x*z - y^2, y - z^2, x - y*z], A)
            sage: C.singular_closed_points()
            []
        """
    @cached_method
    def place_to_closed_point(self, place):
        """
        Return the closed point on the place.

        INPUT:

        - ``place`` -- a place of the function field of the curve

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(GF(4), 2)
            sage: C = Curve(x^5 + y^5 + x*y + 1)
            sage: F = C.function_field()
            sage: pls = F.places(1)
            sage: C.place_to_closed_point(pls[-1])
            Point (x + 1, y + 1)
            sage: C.place_to_closed_point(pls[-2])
            Point (x + 1, y + 1)
        """
    def places_at_infinity(self):
        """
        Return the places of the curve at infinity.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve(x^3 - y^2 - x^4 - y^4)
            sage: C.places_at_infinity()
            [Place (1/x, 1/x^2*y, 1/x^3*y^2, 1/x^4*y^3)]

        ::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(9)
            sage: A2.<x,y> = AffineSpace(F, 2)
            sage: C = A2.curve(y^3 + y - x^4)
            sage: C.places_at_infinity()
            [Place (1/x, 1/x^3*y^2)]

        ::

            sage: A.<x,y,z> = AffineSpace(GF(11), 3)
            sage: C = Curve([x*z - y^2, y - z^2, x - y*z], A)
            sage: C.places_at_infinity()
            [Place (1/x, 1/x*z^2)]
        """
    def places_on(self, point):
        """
        Return the places on the closed point.

        INPUT:

        - ``point`` -- a closed point of the curve

        OUTPUT: list of the places of the function field of the curve

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve(x^3 - y^2 - x^4 - y^4)
            sage: C.singular_closed_points()
            [Point (x, y)]
            sage: p, = _
            sage: C.places_on(p)
            [Place (x, y, y^2, 1/x*y^3 + 1/x*y)]

        ::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(9)
            sage: A.<x,y> = AffineSpace(k, 2)
            sage: C = Curve(y^2 - x^5 - x^4 - 2*x^3 - 2*x - 2)
            sage: pts = C.closed_points()
            sage: pts
            [Point (x, y + (a + 1)),
             Point (x, y + (-a - 1)),
             Point (x + (a + 1), y + (a - 1)),
             Point (x + (a + 1), y + (-a + 1)),
             Point (x - 1, y + (a + 1)),
             Point (x - 1, y + (-a - 1)),
             Point (x + (-a - 1), y + a),
             Point (x + (-a - 1), y + (-a)),
             Point (x + 1, y + 1),
             Point (x + 1, y - 1)]
            sage: p1, p2, p3 = pts[:3]
            sage: C.places_on(p1)
            [Place (x, y + a + 1)]
            sage: C.places_on(p2)
            [Place (x, y + 2*a + 2)]
            sage: C.places_on(p3)
            [Place (x + a + 1, y + a + 2)]

        ::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(8)
            sage: P.<x,y,z> = ProjectiveSpace(F, 2)
            sage: Cp = Curve(x^3*y + y^3*z + x*z^3)
            sage: C = Cp.affine_patch(0)
        """
    def parametric_representation(self, place, name=None):
        """
        Return a power series representation of the branch of the
        curve given by ``place``.

        INPUT:

        - ``place`` -- a place on the curve

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: C = Curve(x^2 + y^2 -1)
            sage: p = C(0,1)
            sage: p.closed_point()
            Point (x, y - 1)
            sage: pl = _.place()
            sage: C.parametric_representation(pl)
            (s + ..., 1 - 1/2*s^2 - 1/8*s^4 - 1/16*s^6 + ...)

        ::

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(GF(7^2), 2)
            sage: C = Curve(x^2 - x^4 - y^4)
            sage: p, = C.singular_closed_points()
            sage: b1, b2 = p.places()
            sage: xs, ys = C.parametric_representation(b1)
            sage: f = xs^2 - xs^4 - ys^4
            sage: [f.coefficient(i) for i in range(5)]
            [0, 0, 0, 0, 0]
            sage: xs, ys = C.parametric_representation(b2)
            sage: f = xs^2 - xs^4 - ys^4
            sage: [f.coefficient(i) for i in range(5)]
            [0, 0, 0, 0, 0]
        """

class IntegralAffineCurve_finite_field(IntegralAffineCurve):
    """
    Integral affine curves.

    INPUT:

    - ``A`` -- an ambient space in which the curve lives

    - ``X`` -- list of polynomials that define the curve

    EXAMPLES::

        sage: A.<x,y,z> = AffineSpace(GF(11), 3)
        sage: C = Curve([x*z - y^2, y - z^2, x - y*z], A); C
        Affine Curve over Finite Field of size 11
         defined by -y^2 + x*z, -z^2 + y, -y*z + x
        sage: C.function_field()
        Function field in z defined by z^3 + 10*x
    """
    def places(self, degree: int = 1):
        """
        Return all places on the curve of the ``degree``.

        INPUT:

        - ``degree`` -- positive integer

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(9)
            sage: A2.<x,y> = AffineSpace(F, 2)
            sage: C = A2.curve(y^3 + y - x^4)
            sage: C.places()
            [Place (1/x, 1/x^3*y^2),
             Place (x, y),
             Place (x, y + z2 + 1),
             Place (x, y + 2*z2 + 2),
             Place (x + z2, y + 2),
             Place (x + z2, y + z2),
             Place (x + z2, y + 2*z2 + 1),
             Place (x + z2 + 1, y + 1),
             Place (x + z2 + 1, y + z2 + 2),
             Place (x + z2 + 1, y + 2*z2),
             Place (x + 2*z2 + 1, y + 2),
             Place (x + 2*z2 + 1, y + z2),
             Place (x + 2*z2 + 1, y + 2*z2 + 1),
             Place (x + 2, y + 1),
             Place (x + 2, y + z2 + 2),
             Place (x + 2, y + 2*z2),
             Place (x + 2*z2, y + 2),
             Place (x + 2*z2, y + z2),
             Place (x + 2*z2, y + 2*z2 + 1),
             Place (x + 2*z2 + 2, y + 1),
             Place (x + 2*z2 + 2, y + z2 + 2),
             Place (x + 2*z2 + 2, y + 2*z2),
             Place (x + z2 + 2, y + 2),
             Place (x + z2 + 2, y + z2),
             Place (x + z2 + 2, y + 2*z2 + 1),
             Place (x + 1, y + 1),
             Place (x + 1, y + z2 + 2),
             Place (x + 1, y + 2*z2)]
        """
    def closed_points(self, degree: int = 1):
        """
        Return a list of the closed points of ``degree`` of the curve.

        INPUT:

        - ``degree`` -- positive integer

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(GF(7), 2)
            sage: C = Curve(x^2 - x^4 - y^4)
            sage: C.closed_points()
            [Point (x, y),
             Point (x + 1, y),
             Point (x + 2, y + 2),
             Point (x + 2, y - 2),
             Point (x - 2, y + 2),
             Point (x - 2, y - 2),
             Point (x - 1, y)]
        """

class IntegralAffinePlaneCurve(IntegralAffineCurve, AffinePlaneCurve_field): ...
class IntegralAffinePlaneCurve_finite_field(AffinePlaneCurve_finite_field, IntegralAffineCurve_finite_field):
    """
    Integral affine plane curve over a finite field.

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: A.<x,y> = AffineSpace(GF(8), 2)
        sage: C = Curve(x^5 + y^5 + x*y + 1); C
        Affine Plane Curve over Finite Field in z3 of size 2^3
         defined by x^5 + y^5 + x*y + 1
        sage: C.function_field()
        Function field in y defined by y^5 + x*y + x^5 + 1
    """
