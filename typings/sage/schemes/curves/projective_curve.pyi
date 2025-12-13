from .closed_point import IntegralProjectiveCurveClosedPoint as IntegralProjectiveCurveClosedPoint
from .curve import Curve_generic as Curve_generic
from .point import IntegralProjectiveCurvePoint as IntegralProjectiveCurvePoint, IntegralProjectiveCurvePoint_finite_field as IntegralProjectiveCurvePoint_finite_field, IntegralProjectivePlaneCurvePoint as IntegralProjectivePlaneCurvePoint, IntegralProjectivePlaneCurvePoint_finite_field as IntegralProjectivePlaneCurvePoint_finite_field, ProjectiveCurvePoint_field as ProjectiveCurvePoint_field, ProjectivePlaneCurvePoint_field as ProjectivePlaneCurvePoint_field, ProjectivePlaneCurvePoint_finite_field as ProjectivePlaneCurvePoint_finite_field
from _typeshed import Incomplete
from collections.abc import Generator
from sage.categories.fields import Fields as Fields
from sage.categories.homset import End as End, Hom as Hom, hom as hom
from sage.categories.number_fields import NumberFields as NumberFields
from sage.libs.singular.function import get_printlevel as get_printlevel, set_printlevel as set_printlevel, singular_function as singular_function
from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.misc.sage_eval import sage_eval as sage_eval
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.rings.polynomial.multi_polynomial_element import degree_lowest_rational_function as degree_lowest_rational_function
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import RationalField as RationalField
from sage.schemes.projective.projective_space import ProjectiveSpace as ProjectiveSpace, ProjectiveSpace_ring as ProjectiveSpace_ring
from sage.schemes.projective.projective_subscheme import AlgebraicScheme_subscheme_projective as AlgebraicScheme_subscheme_projective, AlgebraicScheme_subscheme_projective_field as AlgebraicScheme_subscheme_projective_field

class ProjectiveCurve(Curve_generic, AlgebraicScheme_subscheme_projective):
    """
    Curves in projective spaces.

    INPUT:

    - ``A`` -- ambient projective space

    - ``X`` -- list of multivariate polynomials; defining equations of the curve

    EXAMPLES::

        sage: P.<x,y,z,w,u> = ProjectiveSpace(GF(7), 4)
        sage: C = Curve([y*u^2 - x^3, z*u^2 - x^3, w*u^2 - x^3, y^3 - x^3], P); C
        Projective Curve over Finite Field of size 7 defined
         by -x^3 + y*u^2, -x^3 + z*u^2, -x^3 + w*u^2, -x^3 + y^3

    ::

        sage: # needs sage.rings.number_field
        sage: K.<u> = CyclotomicField(11)
        sage: P.<x,y,z,w> = ProjectiveSpace(K, 3)
        sage: C = Curve([y*w - u*z^2 - x^2, x*w - 3*u^2*z*w], P); C
        Projective Curve over Cyclotomic Field of order 11 and degree 10 defined
         by -x^2 + (-u)*z^2 + y*w, x*w + (-3*u^2)*z*w
    """
    def __init__(self, A, X, category=None) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve(x*y^2*z^7 - x^10 - x^2*z^8)
            sage: loads(dumps(C)) == C
            True
        """
    def affine_patch(self, i, AA=None):
        """
        Return the `i`-th affine patch of this projective curve.

        INPUT:

        - ``i`` -- affine coordinate chart of the projective ambient space of
          this curve to compute affine patch with respect to

        - ``AA`` -- (default: ``None``) ambient affine space, this is constructed
          if it is not given

        OUTPUT: a curve in affine space

        EXAMPLES::

            sage: P.<x,y,z,w> = ProjectiveSpace(CC, 3)
            sage: C = Curve([y*z - x^2, w^2 - x*y], P)
            sage: C.affine_patch(0)
            Affine Curve over Complex Field with 53 bits of precision defined
             by y*z - 1.00000000000000, w^2 - y

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve(x^3 - x^2*y + y^3 - x^2*z, P)
            sage: C.affine_patch(1)
            Affine Plane Curve over Rational Field defined by x^3 - x^2*z - x^2 + 1

        ::

            sage: A.<x,y> = AffineSpace(QQ, 2)
            sage: P.<u,v,w> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([u^2 - v^2], P)
            sage: C.affine_patch(1, A).ambient_space() == A
            True
        """
    def projection(self, P=None, PS=None):
        """
        Return a projection of this curve into projective space of dimension
        one less than the dimension of the ambient space of this curve.

        This curve must not already be a plane curve. Over finite fields, if
        this curve contains all points in its ambient space, then an error will
        be returned.

        INPUT:

        - ``P`` -- (default: ``None``) a point not on this curve that will be used
          to define the projection map; this is constructed if not specified

        - ``PS`` -- (default: ``None``) the projective space the projected curve
          will be defined in. This space must be defined over the same base ring
          as this curve, and must have dimension one less than that of the
          ambient space of this curve. This space will be constructed if not
          specified.

        OUTPUT: a tuple of

        - a scheme morphism from this curve into a projective space of
          dimension one less than that of the ambient space of this curve

        - the projective curve that is the image of that morphism

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: K.<a> = CyclotomicField(3)
            sage: P.<x,y,z,w> = ProjectiveSpace(K, 3)
            sage: C = Curve([y*w - x^2, z*w^2 - a*x^3], P)
            sage: L.<a,b,c> = ProjectiveSpace(K, 2)
            sage: proj1 = C.projection(PS=L)
            sage: proj1
            (Scheme morphism:
               From: Projective Curve over Cyclotomic Field of order 3 and degree 2
                     defined by -x^2 + y*w, (-a)*x^3 + z*w^2
               To:   Projective Space of dimension 2
                     over Cyclotomic Field of order 3 and degree 2
               Defn: Defined on coordinates by sending (x : y : z : w) to
                     (x : y : -z + w),
             Projective Plane Curve over Cyclotomic Field of order 3 and degree 2
              defined by a^6 + (-a)*a^3*b^3 - a^4*b*c)
            sage: proj1[1].ambient_space() is L
            True
            sage: proj2 = C.projection()
            sage: proj2[1].ambient_space() is L
            False

        ::

            sage: P.<x,y,z,w,a,b,c> = ProjectiveSpace(QQ, 6)
            sage: C = Curve([y - x, z - a - b, w^2 - c^2, z - x - a, x^2 - w*z], P)
            sage: C.projection()
            (Scheme morphism:
               From: Projective Curve over Rational Field
                     defined by -x + y, z - a - b, w^2 - c^2, -x + z - a, x^2 - z*w
               To:   Projective Space of dimension 5 over Rational Field
               Defn: Defined on coordinates by sending (x : y : z : w : a : b : c)
                     to (x : y : -z + w : a : b : c),
             Projective Curve over Rational Field defined by x1 - x4, x0 - x4, x2*x3
              + x3^2 + x2*x4 + 2*x3*x4, x2^2 - x3^2 - 2*x3*x4 + x4^2 - x5^2, x2*x4^2 +
              x3*x4^2 + x4^3 - x3*x5^2 - x4*x5^2, x4^4 - x3^2*x5^2 - 2*x3*x4*x5^2 -
              x4^2*x5^2)

        ::

            sage: P.<x,y,z,w> = ProjectiveSpace(GF(2), 3)
            sage: C = P.curve([(x - y)*(x - z)*(x - w)*(y - z)*(y - w),
            ....:              x*y*z*w*(x + y + z + w)])
            sage: C.projection()
            Traceback (most recent call last):
            ...
            NotImplementedError: this curve contains all points of its ambient space

        ::

            sage: P.<x,y,z,w,u> = ProjectiveSpace(GF(7), 4)
            sage: C = P.curve([x^3 - y*z*u, w^2 - u^2 + 2*x*z, 3*x*w - y^2])
            sage: L.<a,b,c,d> = ProjectiveSpace(GF(7), 3)
            sage: C.projection(PS=L)
            (Scheme morphism:
               From: Projective Curve over Finite Field of size 7
                     defined by x^3 - y*z*u, 2*x*z + w^2 - u^2, -y^2 + 3*x*w
               To:   Projective Space of dimension 3 over Finite Field of size 7
               Defn: Defined on coordinates by sending (x : y : z : w : u) to
                     (x : y : z : w),
             Projective Curve over Finite Field of size 7 defined by b^2 - 3*a*d,
              a^5*b + a*b*c^3*d - 3*b*c^2*d^3, a^6 + a^2*c^3*d - 3*a*c^2*d^3)
            sage: Q.<a,b,c> = ProjectiveSpace(GF(7), 2)
            sage: C.projection(PS=Q)
            Traceback (most recent call last):
            ...
            TypeError: (=Projective Space of dimension 2 over Finite Field of
            size 7) must have dimension (=3)


        ::

            sage: PP.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: C = PP.curve([x^3 - z^2*y, w^2 - z*x])
            sage: Q = PP([1,0,1,1])
            sage: C.projection(P=Q)
            (Scheme morphism:
               From: Projective Curve over Rational Field
                     defined by x^3 - y*z^2, -x*z + w^2
               To:   Projective Space of dimension 2 over Rational Field
               Defn: Defined on coordinates by sending (x : y : z : w) to
                     (y : -x + z : -x + w),
             Projective Plane Curve over Rational Field defined by x0*x1^5 -
              6*x0*x1^4*x2 + 14*x0*x1^3*x2^2 - 16*x0*x1^2*x2^3 + 9*x0*x1*x2^4 -
              2*x0*x2^5 - x2^6)
            sage: LL.<a,b,c> = ProjectiveSpace(QQ, 2)
            sage: Q = PP([0,0,0,1])
            sage: C.projection(PS=LL, P=Q)
            (Scheme morphism:
               From: Projective Curve over Rational Field
                     defined by x^3 - y*z^2, -x*z + w^2
               To:   Projective Space of dimension 2 over Rational Field
               Defn: Defined on coordinates by sending (x : y : z : w) to
                     (x : y : z),
             Projective Plane Curve over Rational Field defined by a^3 - b*c^2)
            sage: Q = PP([0,0,1,0])
            sage: C.projection(P=Q)
            Traceback (most recent call last):
            ...
            TypeError: (=(0 : 0 : 1 : 0)) must be a point not on this curve

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = P.curve(y^2 - x^2 + z^2)
            sage: C.projection()
            Traceback (most recent call last):
            ...
            TypeError: this curve is already a plane curve
        """
    def plane_projection(self, PP=None):
        """
        Return a projection of this curve into a projective plane.

        INPUT:

        - ``PP`` -- (default: ``None``) the projective plane the projected curve
          will be defined in. This space must be defined over the same base field
          as this curve, and must have dimension two. This space is constructed
          if not specified.

        OUTPUT: a tuple of

        - a scheme morphism from this curve into a projective plane

        - the projective curve that is the image of that morphism

        EXAMPLES::

            sage: P.<x,y,z,w,u,v> = ProjectiveSpace(QQ, 5)
            sage: C = P.curve([x*u - z*v, w - y, w*y - x^2, y^3*u*2*z - w^4*w])
            sage: L.<a,b,c> = ProjectiveSpace(QQ, 2)
            sage: proj1 = C.plane_projection(PP=L)
            sage: proj1
            (Scheme morphism:
               From: Projective Curve over Rational Field
                     defined by x*u - z*v, -y + w, -x^2 + y*w, -w^5 + 2*y^3*z*u
               To:   Projective Space of dimension 2 over Rational Field
               Defn: Defined on coordinates by sending (x : y : z : w : u : v) to
                     (x : -z + u : -z + v),
             Projective Plane Curve over Rational Field defined by a^8 + 6*a^7*b +
              4*a^5*b^3 - 4*a^7*c - 2*a^6*b*c - 4*a^5*b^2*c + 2*a^6*c^2)
            sage: proj1[1].ambient_space() is L
            True
            sage: proj2 = C.projection()
            sage: proj2[1].ambient_space() is L
            False

        ::

            sage: P.<x,y,z,w,u> = ProjectiveSpace(GF(7), 4)
            sage: C = P.curve([x^2 - 6*y^2, w*z*u - y^3 + 4*y^2*z, u^2 - x^2])
            sage: C.plane_projection()
            (Scheme morphism:
               From: Projective Curve over Finite Field of size 7
                     defined by x^2 + y^2, -y^3 - 3*y^2*z + z*w*u, -x^2 + u^2
               To:   Projective Space of dimension 2 over Finite Field of size 7
               Defn: Defined on coordinates by sending (x : y : z : w : u) to
                     (x : z : -y + w),
             Projective Plane Curve over Finite Field of size 7
              defined by x0^10 + 2*x0^8*x1^2 + 2*x0^6*x1^4 - 3*x0^6*x1^3*x2
                         + 2*x0^6*x1^2*x2^2 - 2*x0^4*x1^4*x2^2 + x0^2*x1^4*x2^4)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = P.curve(x^2 - y*z - z^2)
            sage: C.plane_projection()
            Traceback (most recent call last):
            ...
            TypeError: this curve is already a plane curve
        """

class ProjectivePlaneCurve(ProjectiveCurve):
    """
    Curves in projective planes.

    INPUT:

    - ``A`` -- projective plane

    - ``f`` -- homogeneous polynomial in the homogeneous coordinate ring of the plane

    EXAMPLES:

    A projective plane curve defined over an algebraic closure of `\\QQ`::

        sage: # needs sage.rings.number_field
        sage: P.<x,y,z> = ProjectiveSpace(QQbar, 2)
        sage: set_verbose(-1)  # suppress warnings for slow computation
        sage: C = Curve([y*z - x^2 - QQbar.gen()*z^2], P); C
        Projective Plane Curve over Algebraic Field
         defined by -x^2 + y*z + (-I)*z^2

    A projective plane curve defined over a finite field::

        sage: # needs sage.rings.finite_rings
        sage: P.<x,y,z> = ProjectiveSpace(GF(5^2, 'v'), 2)
        sage: C = Curve([y^2*z - x*z^2 - z^3], P); C
        Projective Plane Curve over Finite Field in v of size 5^2
         defined by y^2*z - x*z^2 - z^3
    """
    def __init__(self, A, f, category=None) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve(y^2*z^7 - x^9 - x*z^8)
            sage: loads(dumps(C)) == C
            True
        """
    def divisor_of_function(self, r):
        """
        Return the divisor of a function on a curve.

        INPUT:

        - ``r`` is a rational function on X

        OUTPUT: list; the divisor of r represented as a list of coefficients
        and points. (TODO: This will change to a more structural output in the
        future.)

        EXAMPLES::

            sage: FF = FiniteField(5)
            sage: P2 = ProjectiveSpace(2, FF, names=['x','y','z'])
            sage: R = P2.coordinate_ring()
            sage: x, y, z = R.gens()
            sage: f = y^2*z^7 - x^9 - x*z^8
            sage: C = Curve(f)
            sage: K = FractionField(R)
            sage: r = 1/x
            sage: C.divisor_of_function(r)     # todo: not implemented  !!!!
            [[-1, (0, 0, 1)]]
            sage: r = 1/x^3
            sage: C.divisor_of_function(r)     # todo: not implemented  !!!!
            [[-3, (0, 0, 1)]]
        """
    def local_coordinates(self, pt, n):
        """
        Return local coordinates to precision n at the given point.

        Behaviour is flaky - some choices of `n` are worse than
        others.

        INPUT:

        - ``pt`` -- a rational point on X which is not a point of ramification
          for the projection `(x,y) \\to x`

        - ``n`` -- the number of terms desired

        OUTPUT: `x = x0 + t`, `y = y0` + power series in `t`

        EXAMPLES::

            sage: FF = FiniteField(5)
            sage: P2 = ProjectiveSpace(2, FF, names=['x','y','z'])
            sage: x, y, z = P2.coordinate_ring().gens()
            sage: C = Curve(y^2*z^7 - x^9 - x*z^8)
            sage: pt = C([2,3,1])
            sage: C.local_coordinates(pt,9)     # todo: not implemented  !!!!
            [2 + t,
             3 + 3*t^2 + t^3 + 3*t^4 + 3*t^6 + 3*t^7 + t^8 + 2*t^9 + 3*t^11 + 3*t^12]
        """
    def plot(self, *args, **kwds):
        """
        Plot the real points of an affine patch of this projective
        plane curve.

        INPUT:

        - ``self`` -- an affine plane curve

        - ``patch`` -- (optional) the affine patch to be plotted; if not
          specified, the patch corresponding to the last projective
          coordinate being nonzero

        - ``*args`` -- (optional) tuples (variable, minimum, maximum) for
          plotting dimensions

        - ``**kwds`` -- optional keyword arguments passed on to ``implicit_plot``

        EXAMPLES:

        A cuspidal curve::

            sage: R.<x, y, z> = QQ[]
            sage: C = Curve(x^3 - y^2*z)
            sage: C.plot()                                                              # needs sage.plot
            Graphics object consisting of 1 graphics primitive

        The other affine patches of the same curve::

            sage: # needs sage.plot
            sage: C.plot(patch=0)
            Graphics object consisting of 1 graphics primitive
            sage: C.plot(patch=1)
            Graphics object consisting of 1 graphics primitive

        An elliptic curve::

            sage: # needs sage.plot
            sage: E = EllipticCurve('101a')
            sage: C = Curve(E)
            sage: C.plot()
            Graphics object consisting of 1 graphics primitive
            sage: C.plot(patch=0)
            Graphics object consisting of 1 graphics primitive
            sage: C.plot(patch=1)
            Graphics object consisting of 1 graphics primitive

        A hyperelliptic curve::

            sage: # needs sage.plot
            sage: P.<x> = QQ[]
            sage: f = 4*x^5 - 30*x^3 + 45*x - 22
            sage: C = HyperellipticCurve(f)
            sage: C.plot()
            Graphics object consisting of 1 graphics primitive
            sage: C.plot(patch=0)
            Graphics object consisting of 1 graphics primitive
            sage: C.plot(patch=1)
            Graphics object consisting of 1 graphics primitive
        """
    def is_singular(self, P=None):
        """
        Return whether this curve is singular or not, or if a point ``P`` is
        provided, whether ``P`` is a singular point of this curve.

        INPUT:

        - ``P`` -- (default: ``None``) a point on this curve

        OUTPUT:

        If no point ``P`` is provided, return ``True`` or ``False`` depending
        on whether this curve is singular or not. If a point ``P`` is provided,
        return ``True`` or ``False`` depending on whether ``P`` is or is not a
        singular point of this curve.

        EXAMPLES:

        Over `\\QQ`::

            sage: F = QQ
            sage: P2.<X,Y,Z> = ProjectiveSpace(F, 2)
            sage: C = Curve(X^3 - Y^2*Z)
            sage: C.is_singular()
            True

        Over a finite field::

            sage: F = GF(19)
            sage: P2.<X,Y,Z> = ProjectiveSpace(F, 2)
            sage: C = Curve(X^3 + Y^3 + Z^3)
            sage: C.is_singular()
            False
            sage: D = Curve(X^4 - X*Z^3)
            sage: D.is_singular()
            True
            sage: E = Curve(X^5 + 19*Y^5 + Z^5)
            sage: E.is_singular()
            True
            sage: E = Curve(X^5 + 9*Y^5 + Z^5)
            sage: E.is_singular()
            False

        Over `\\CC`::

            sage: # needs sage.rings.function_field
            sage: F = CC
            sage: P2.<X,Y,Z> = ProjectiveSpace(F, 2)
            sage: C = Curve(X)
            sage: C.is_singular()
            False
            sage: D = Curve(Y^2*Z - X^3)
            sage: D.is_singular()
            True
            sage: E = Curve(Y^2*Z - X^3 + Z^3)
            sage: E.is_singular()
            False

        Showing that :issue:`12187` is fixed::

            sage: F.<X,Y,Z> = GF(2)[]
            sage: G = Curve(X^2 + Y*Z)
            sage: G.is_singular()
            False

        ::

            sage: # needs sage.fings.function_field
            sage: P.<x,y,z> = ProjectiveSpace(CC, 2)
            sage: C = Curve([y^4 - x^3*z], P)
            sage: Q = P([0,0,1])
            sage: C.is_singular()
            True
        """
    def degree(self):
        """
        Return the degree of this projective curve.

        For a plane curve, this is just the degree of its defining polynomial.

        OUTPUT: integer

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = P.curve([y^7 - x^2*z^5 + 7*z^7])
            sage: C.degree()
            7
        """
    def tangents(self, P, factor: bool = True):
        """
        Return the tangents of this projective plane curve at the point ``P``.

        These are found by homogenizing the tangents of an affine patch of this
        curve containing ``P``. The point ``P`` must be a point on this curve.

        INPUT:

        - ``P`` -- a point on this curve

        - ``factor`` -- boolean (default: ``True``); whether to attempt computing the
          polynomials of the individual tangent lines over the base field of this
          curve, or to just return the polynomial corresponding to the union of
          the tangent lines (which requires fewer computations)

        OUTPUT:

        A list of polynomials in the coordinate ring of the ambient space of
        this curve.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: set_verbose(-1)
            sage: P.<x,y,z> = ProjectiveSpace(QQbar, 2)
            sage: C = Curve([x^3*y + 2*x^2*y^2 + x*y^3 + x^3*z
            ....:            + 7*x^2*y*z + 14*x*y^2*z + 9*y^3*z], P)
            sage: Q = P([0,0,1])
            sage: C.tangents(Q)
            [x + 4.147899035704788?*y,
             x + (1.426050482147607? + 0.3689894074818041?*I)*y,
             x + (1.426050482147607? - 0.3689894074818041?*I)*y]
            sage: C.tangents(Q, factor=False)
            [6*x^3 + 42*x^2*y + 84*x*y^2 + 54*y^3]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = P.curve([x^2*y^3*z^4 - y^6*z^3 - 4*x^2*y^4*z^3 - 4*x^4*y^2*z^3
            ....:              + 3*y^7*z^2 + 10*x^2*y^5*z^2 + 9*x^4*y^3*z^2 + 5*x^6*y*z^2
            ....:              - 3*y^8*z - 9*x^2*y^6*z - 11*x^4*y^4*z - 7*x^6*y^2*z
            ....:              - 2*x^8*z + y^9 + 2*x^2*y^7 + 3*x^4*y^5 + 4*x^6*y^3 + 2*x^8*y])
            sage: Q = P([0,1,1])
            sage: C.tangents(Q)
            [-y + z, 3*x^2 - y^2 + 2*y*z - z^2]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = P.curve([z^3*x + y^4 - x^2*z^2])
            sage: Q = P([1,1,1])
            sage: C.tangents(Q)
            Traceback (most recent call last):
            ...
            TypeError: (=(1 : 1 : 1)) is not a point on (=Projective Plane Curve
            over Rational Field defined by y^4 - x^2*z^2 + x*z^3)
        """
    def is_ordinary_singularity(self, P):
        """
        Return whether the singular point ``P`` of this projective plane curve is an ordinary singularity.

        The point ``P`` is an ordinary singularity of this curve if it is a singular point, and
        if the tangents of this curve at ``P`` are distinct.

        INPUT:

        - ``P`` -- a point on this curve

        OUTPUT:

        boolean; ``True`` or ``False`` depending on whether ``P`` is or is not
        an ordinary singularity of this curve, respectively. An error is raised
        if ``P`` is not a singular point of this curve.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([y^2*z^3 - x^5], P)
            sage: Q = P([0,0,1])
            sage: C.is_ordinary_singularity(Q)
            False

        ::

            sage: # needs sage.rings.number_field
            sage: R.<a> = QQ[]
            sage: K.<b> = NumberField(a^2 - 3)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: C = P.curve([x^2*y^3*z^4 - y^6*z^3 - 4*x^2*y^4*z^3 - 4*x^4*y^2*z^3
            ....:              + 3*y^7*z^2 + 10*x^2*y^5*z^2 + 9*x^4*y^3*z^2
            ....:              + 5*x^6*y*z^2 - 3*y^8*z - 9*x^2*y^6*z - 11*x^4*y^4*z
            ....:              - 7*x^6*y^2*z - 2*x^8*z + y^9 + 2*x^2*y^7 + 3*x^4*y^5
            ....:              + 4*x^6*y^3 + 2*x^8*y])
            sage: Q = P([0,1,1])
            sage: C.is_ordinary_singularity(Q)
            True

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = P.curve([z^5 - y^5 + x^5 + x*y^2*z^2])
            sage: Q = P([0,1,1])
            sage: C.is_ordinary_singularity(Q)
            Traceback (most recent call last):
            ...
            TypeError: (=(0 : 1 : 1)) is not a singular point of (=Projective Plane
            Curve over Rational Field defined by x^5 - y^5 + x*y^2*z^2 + z^5)
        """
    def quadratic_transform(self):
        """
        Return a birational map from this curve to the proper transform of this curve with respect to the standard
        Cremona transformation.

        The standard Cremona transformation is the birational automorphism of `\\mathbb{P}^{2}` defined
        `(x : y : z)\\mapsto (yz : xz : xy)`.

        OUTPUT:

        - a scheme morphism representing the restriction of the standard Cremona transformation from this curve
          to the proper transform.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve(x^3*y - z^4 - z^2*x^2, P)
            sage: C.quadratic_transform()
            Scheme morphism:
              From: Projective Plane Curve over Rational Field
                    defined by x^3*y - x^2*z^2 - z^4
              To:   Projective Plane Curve over Rational Field
                    defined by -x^3*y - x*y*z^2 + z^4
              Defn: Defined on coordinates by sending (x : y : z) to
                    (y*z : x*z : x*y)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(17), 2)
            sage: C = P.curve([y^7*z^2 - 16*x^9 + x*y*z^7 + 2*z^9])
            sage: C.quadratic_transform()
            Scheme morphism:
              From: Projective Plane Curve over Finite Field of size 17
                    defined by x^9 + y^7*z^2 + x*y*z^7 + 2*z^9
              To:   Projective Plane Curve over Finite Field of size 17
                    defined by 2*x^9*y^7 + x^8*y^6*z^2 + x^9*z^7 + y^7*z^9
              Defn: Defined on coordinates by sending (x : y : z) to
                    (y*z : x*z : x*y)
        """
    def excellent_position(self, Q):
        """
        Return a transformation of this curve into one in excellent position with respect to the point ``Q``.

        Here excellent position is defined as in [Ful1989]_. A curve `C` of degree `d` containing the point
        `(0 : 0 : 1)` with multiplicity `r` is said to be in excellent position if none of the coordinate lines
        are tangent to `C` at any of the fundamental points `(1 : 0 : 0)`, `(0 : 1 : 0)`, and `(0 : 0 : 1)`, and
        if the two coordinate lines containing `(0 : 0 : 1)` intersect `C` transversally in `d - r` distinct
        non-fundamental points, and if the other coordinate line intersects `C` transversally at `d` distinct,
        non-fundamental points.

        INPUT:

        - ``Q`` -- a point on this curve

        OUTPUT:

        A scheme morphism from this curve to a curve in excellent position that
        is a restriction of a change of coordinates map of the projective plane.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([x*y - z^2], P)
            sage: Q = P([1,1,1])
            sage: C.excellent_position(Q)
            Scheme morphism:
              From: Projective Plane Curve over Rational Field defined by x*y - z^2
              To:   Projective Plane Curve over Rational Field
                    defined by -x^2 - 3*x*y - 4*y^2 - x*z - 3*y*z
              Defn: Defined on coordinates by sending (x : y : z) to
                    (-x + 1/2*y + 1/2*z : -1/2*y + 1/2*z : x + 1/2*y - 1/2*z)

        ::

            sage: # needs sage.rings.number_field
            sage: R.<a> = QQ[]
            sage: K.<b> = NumberField(a^2 - 3)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: C = P.curve([z^2*y^3*x^4 - y^6*x^3 - 4*z^2*y^4*x^3 - 4*z^4*y^2*x^3
            ....:              + 3*y^7*x^2 + 10*z^2*y^5*x^2 + 9*z^4*y^3*x^2
            ....:              + 5*z^6*y*x^2 - 3*y^8*x - 9*z^2*y^6*x - 11*z^4*y^4*x
            ....:              - 7*z^6*y^2*x - 2*z^8*x + y^9 + 2*z^2*y^7 + 3*z^4*y^5
            ....:              + 4*z^6*y^3 + 2*z^8*y])
            sage: Q = P([1,0,0])
            sage: C.excellent_position(Q)
            Scheme morphism:
              From: Projective Plane Curve over Number Field in b
                    with defining polynomial a^2 - 3
                    defined by -x^3*y^6 + 3*x^2*y^7 - 3*x*y^8 + y^9 + x^4*y^3*z^2
                               - 4*x^3*y^4*z^2 + 10*x^2*y^5*z^2 - 9*x*y^6*z^2
                               + 2*y^7*z^2 - 4*x^3*y^2*z^4 + 9*x^2*y^3*z^4
                               - 11*x*y^4*z^4 + 3*y^5*z^4 + 5*x^2*y*z^6
                               - 7*x*y^2*z^6 + 4*y^3*z^6 - 2*x*z^8 + 2*y*z^8
              To:   Projective Plane Curve over Number Field in b
                    with defining polynomial a^2 - 3
                    defined by 900*x^9 - 7410*x^8*y + 29282*x^7*y^2 - 69710*x^6*y^3
                               + 110818*x^5*y^4 - 123178*x^4*y^5 + 96550*x^3*y^6
                               - 52570*x^2*y^7 + 18194*x*y^8 - 3388*y^9 - 1550*x^8*z
                               + 9892*x^7*y*z - 30756*x^6*y^2*z + 58692*x^5*y^3*z
                               - 75600*x^4*y^4*z + 67916*x^3*y^5*z - 42364*x^2*y^6*z
                               + 16844*x*y^7*z - 3586*y^8*z + 786*x^7*z^2
                               - 3958*x^6*y*z^2 + 9746*x^5*y^2*z^2 - 14694*x^4*y^3*z^2
                               + 15174*x^3*y^4*z^2 - 10802*x^2*y^5*z^2
                               + 5014*x*y^6*z^2 - 1266*y^7*z^2 - 144*x^6*z^3
                               + 512*x^5*y*z^3 - 912*x^4*y^2*z^3 + 1024*x^3*y^3*z^3
                               - 816*x^2*y^4*z^3 + 512*x*y^5*z^3 - 176*y^6*z^3
                               + 8*x^5*z^4 - 8*x^4*y*z^4 - 16*x^3*y^2*z^4
                               + 16*x^2*y^3*z^4 + 8*x*y^4*z^4 - 8*y^5*z^4
              Defn: Defined on coordinates by sending (x : y : z) to
                    (1/4*y + 1/2*z : -1/4*y + 1/2*z : x + 1/4*y - 1/2*z)

        ::

            sage: # needs sage.rings.number_field sage.symbolic
            sage: set_verbose(-1)
            sage: a = QQbar(sqrt(2))
            sage: P.<x,y,z> = ProjectiveSpace(QQbar, 2)
            sage: C = Curve([(-1/4*a)*x^3 + (-3/4*a)*x^2*y
            ....:            + (-3/4*a)*x*y^2 + (-1/4*a)*y^3 - 2*x*y*z], P)
            sage: Q = P([0,0,1])
            sage: C.excellent_position(Q)
            Scheme morphism:
              From: Projective Plane Curve over Algebraic Field defined
                    by (-0.3535533905932738?)*x^3 + (-1.060660171779822?)*x^2*y
                       + (-1.060660171779822?)*x*y^2 + (-0.3535533905932738?)*y^3
                       + (-2)*x*y*z
              To:   Projective Plane Curve over Algebraic Field defined
                    by (-2.828427124746190?)*x^3 + (-2)*x^2*y + 2*y^3
                       + (-2)*x^2*z + 2*y^2*z
              Defn: Defined on coordinates by sending (x : y : z) to
                    (1/2*x + 1/2*y : (-1/2)*x + 1/2*y : 1/2*x + (-1/2)*y + z)
        """
    def ordinary_model(self):
        """
        Return a birational map from this curve to a plane curve with only ordinary singularities.

        Currently only implemented over number fields. If not all of the coordinates of the non-ordinary
        singularities of this curve are contained in its base field, then the domain and codomain of the
        map returned will be defined over an extension. This curve must be irreducible.

        OUTPUT:

        - a scheme morphism from this curve to a curve with only ordinary singularities that defines a
          birational map between the two curves.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: set_verbose(-1)
            sage: K = QuadraticField(3)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: C = Curve([x^5 - K.0*y*z^4], P)
            sage: C.ordinary_model()
            Scheme morphism:
              From: Projective Plane Curve over Number Field in a
                    with defining polynomial x^2 - 3 with a = 1.732050807568878?
                    defined by x^5 + (-a)*y*z^4
              To:   Projective Plane Curve over Number Field in a
                    with defining polynomial x^2 - 3 with a = 1.732050807568878?
                    defined by (-a)*x^5*y + (-4*a)*x^4*y^2 + (-6*a)*x^3*y^3
                               + (-4*a)*x^2*y^4 + (-a)*x*y^5 + (-a - 1)*x^5*z
                               + (-4*a + 5)*x^4*y*z + (-6*a - 10)*x^3*y^2*z
                               + (-4*a + 10)*x^2*y^3*z + (-a - 5)*x*y^4*z + y^5*z
              Defn: Defined on coordinates by sending (x : y : z) to
                    (-1/4*x^2 - 1/2*x*y + 1/2*x*z + 1/2*y*z - 1/4*z^2 :
                     1/4*x^2 + 1/2*x*y + 1/2*y*z - 1/4*z^2 :
                     -1/4*x^2 + 1/4*z^2)

        ::

            sage: set_verbose(-1)
            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([y^2*z^2 - x^4 - x^3*z], P)
            sage: D = C.ordinary_model(); D  # long time (2 seconds)
            Scheme morphism:
              From: Projective Plane Curve over Rational Field defined
                    by -x^4 - x^3*z + y^2*z^2
              To:   Projective Plane Curve over Rational Field defined
                    by 4*x^6*y^3 - 24*x^5*y^4 + 36*x^4*y^5 + 8*x^6*y^2*z
                       - 40*x^5*y^3*z + 24*x^4*y^4*z + 72*x^3*y^5*z - 4*x^6*y*z^2
                       + 8*x^5*y^2*z^2 - 56*x^4*y^3*z^2 + 104*x^3*y^4*z^2
                       + 44*x^2*y^5*z^2 + 8*x^6*z^3 - 16*x^5*y*z^3
                       - 24*x^4*y^2*z^3 + 40*x^3*y^3*z^3 + 48*x^2*y^4*z^3
                       + 8*x*y^5*z^3 - 8*x^5*z^4 + 36*x^4*y*z^4 - 56*x^3*y^2*z^4
                       + 20*x^2*y^3*z^4 + 40*x*y^4*z^4 - 16*y^5*z^4
              Defn: Defined on coordinates by sending (x : y : z) to
                    (-3/64*x^4 + 9/64*x^2*y^2 - 3/32*x*y^3 - 1/16*x^3*z
                      - 1/8*x^2*y*z + 1/4*x*y^2*z - 1/16*y^3*z - 1/8*x*y*z^2
                      + 1/16*y^2*z^2 :
                     -1/64*x^4 + 3/64*x^2*y^2 - 1/32*x*y^3 + 1/16*x*y^2*z
                      - 1/16*y^3*z + 1/16*y^2*z^2 :
                     3/64*x^4 - 3/32*x^3*y + 3/64*x^2*y^2 + 1/16*x^3*z
                      - 3/16*x^2*y*z + 1/8*x*y^2*z - 1/8*x*y*z^2 + 1/16*y^2*z^2)
            sage: all(D.codomain().is_ordinary_singularity(Q)  # long time
            ....:     for Q in D.codomain().singular_points())
            True

        ::

            sage: set_verbose(-1)
            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([(x^2 + y^2 - y*z - 2*z^2)*(y*z - x^2 + 2*z^2)*z + y^5], P)
            sage: C.ordinary_model() # long time (5 seconds)
            Scheme morphism:
              From: Projective Plane Curve over Number Field in a
                    with defining polynomial y^2 - 2 defined
                    by y^5 - x^4*z - x^2*y^2*z + 2*x^2*y*z^2 + y^3*z^2
                       + 4*x^2*z^3 + y^2*z^3 - 4*y*z^4 - 4*z^5
              To:   Projective Plane Curve over Number Field in a
                    with defining polynomial y^2 - 2 defined
                    by (-29*a + 1)*x^8*y^6 + (10*a + 158)*x^7*y^7
                       + (-109*a - 31)*x^6*y^8 + (-80*a - 198)*x^8*y^5*z
                       + (531*a + 272)*x^7*y^6*z + (170*a - 718)*x^6*y^7*z
                       + (19*a - 636)*x^5*y^8*z + (-200*a - 628)*x^8*y^4*z^2
                       + (1557*a - 114)*x^7*y^5*z^2 + (2197*a - 2449)*x^6*y^6*z^2
                       + (1223*a - 3800)*x^5*y^7*z^2 + (343*a - 1329)*x^4*y^8*z^2
                       + (-323*a - 809)*x^8*y^3*z^3 + (1630*a - 631)*x^7*y^4*z^3
                       + (4190*a - 3126)*x^6*y^5*z^3 + (3904*a - 7110)*x^5*y^6*z^3
                       + (1789*a - 5161)*x^4*y^7*z^3 + (330*a - 1083)*x^3*y^8*z^3
                       + (-259*a - 524)*x^8*y^2*z^4 + (720*a - 605)*x^7*y^3*z^4
                       + (3082*a - 2011)*x^6*y^4*z^4 + (4548*a - 5462)*x^5*y^5*z^4
                       + (2958*a - 6611)*x^4*y^6*z^4 + (994*a - 2931)*x^3*y^7*z^4
                       + (117*a - 416)*x^2*y^8*z^4 + (-108*a - 184)*x^8*y*z^5
                       + (169*a - 168)*x^7*y^2*z^5 + (831*a - 835)*x^6*y^3*z^5
                       + (2225*a - 1725)*x^5*y^4*z^5 + (1970*a - 3316)*x^4*y^5*z^5
                       + (952*a - 2442)*x^3*y^6*z^5 + (217*a - 725)*x^2*y^7*z^5
                       + (16*a - 77)*x*y^8*z^5 + (-23*a - 35)*x^8*z^6
                       + (43*a + 24)*x^7*y*z^6 + (21*a - 198)*x^6*y^2*z^6
                       + (377*a - 179)*x^5*y^3*z^6 + (458*a - 537)*x^4*y^4*z^6
                       + (288*a - 624)*x^3*y^5*z^6 + (100*a - 299)*x^2*y^6*z^6
                       + (16*a - 67)*x*y^7*z^6 - 5*y^8*z^6
              Defn: Defined on coordinates by sending (x : y : z) to
                    ((-5/128*a - 5/128)*x^4 + (-5/32*a + 5/32)*x^3*y
                      + (-1/16*a + 3/32)*x^2*y^2 + (1/16*a - 1/16)*x*y^3
                      + (1/32*a - 1/32)*y^4 - 1/32*x^3*z + (3/16*a - 5/8)*x^2*y*z
                      + (1/8*a - 5/16)*x*y^2*z + (1/8*a + 5/32)*x^2*z^2
                      + (-3/16*a + 5/16)*x*y*z^2 + (-3/16*a - 1/16)*y^2*z^2
                      + 1/16*x*z^3 + (1/4*a + 1/4)*y*z^3 + (-3/32*a - 5/32)*z^4 :
                     (-5/128*a - 5/128)*x^4 + (5/32*a)*x^3*y
                      + (3/32*a + 3/32)*x^2*y^2 + (-1/16*a)*x*y^3
                      + (-1/32*a - 1/32)*y^4 - 1/32*x^3*z + (-11/32*a)*x^2*y*z
                      + (1/8*a + 5/16)*x*y^2*z + (3/16*a + 1/4)*y^3*z
                      + (1/8*a + 5/32)*x^2*z^2 + (-1/16*a - 3/8)*x*y*z^2
                      + (-3/8*a - 9/16)*y^2*z^2 + 1/16*x*z^3 + (5/16*a + 1/2)*y*z^3
                      + (-3/32*a - 5/32)*z^4 :
                     (1/64*a + 3/128)*x^4 + (-1/32*a - 1/32)*x^3*y
                      + (3/32*a - 9/32)*x^2*y^2 + (1/16*a - 3/16)*x*y^3 - 1/32*y^4
                      + (3/32*a + 1/8)*x^2*y*z + (-1/8*a + 1/8)*x*y^2*z
                      + (-1/16*a)*y^3*z + (-1/16*a - 3/32)*x^2*z^2
                      + (1/16*a + 1/16)*x*y*z^2 + (3/16*a + 3/16)*y^2*z^2
                      + (-3/16*a - 1/4)*y*z^3 + (1/16*a + 3/32)*z^4)
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

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([x^2 - y^2], P)
            sage: D = Curve([x - y], P)
            sage: Q = P([1,1,0])
            sage: C.is_transverse(D, Q)
            False

        ::

            sage: # needs sage.rings.number_field
            sage: K = QuadraticField(-1)
            sage: P.<x,y,z> = ProjectiveSpace(K, 2)
            sage: C = Curve([y^2*z - K.0*x^3], P)
            sage: D = Curve([z*x + y^2], P)
            sage: Q = P([0,0,1])
            sage: C.is_transverse(D, Q)
            False

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([x^2 - 2*y^2 - 2*z^2], P)
            sage: D = Curve([y - z], P)
            sage: Q = P([2,1,1])
            sage: C.is_transverse(D, Q)
            True
        """

class ProjectiveCurve_field(ProjectiveCurve, AlgebraicScheme_subscheme_projective_field):
    """
    Projective curves over fields.
    """
    def __init__(self, A, X, category=None) -> None:
        """
        Initialize.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve(x*y^2*z^7 - x^10 - x^2*z^8)
            sage: loads(dumps(C)) == C
            True

        TESTS::

            sage: P.<x0,x1,x2,x3,x4> = ProjectiveSpace(QQ, 4)
            sage: C = Curve([x0^4 - x1^2*x4^2 - 19*x4^4, x2^4 - x3^2*x4^2 - 23*x4^4])
            Traceback (most recent call last):
            ...
            ValueError: defining equations (=[x0^4 - x1^2*x4^2 - 19*x4^4, x2^4 - x3^2*x4^2 - 23*x4^4])
            define a scheme of dimension 2 != 1
        """
    def arithmetic_genus(self):
        """
        Return the arithmetic genus of this projective curve.

        This is the arithmetic genus `p_a(C)` as defined in [Har1977]_. If `P`
        is the Hilbert polynomial of the defining ideal of this curve, then the
        arithmetic genus of this curve is `1 - P(0)`.

        EXAMPLES::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: C = P.curve([w*z - x^2, w^2 + y^2 + z^2])
            sage: C.arithmetic_genus()
            1

        ::

            sage: P.<x,y,z,w,t> = ProjectiveSpace(GF(7), 4)
            sage: C = P.curve([t^3 - x*y*w, x^3 + y^3 + z^3, z - w])
            sage: C.arithmetic_genus()
            10
        """
    def is_complete_intersection(self):
        """
        Return whether this projective curve is a complete intersection.

        EXAMPLES::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: C = Curve([x*y - z*w, x^2 - y*w, y^2*w - x*z*w], P)
            sage: C.is_complete_intersection()
            False

        ::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: C = Curve([y*w - x^2, z*w^2 - x^3], P)
            sage: C.is_complete_intersection()
            True

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: C = Curve([z^2 - y*w, y*z - x*w, y^2 - x*z], P)
            sage: C.is_complete_intersection()
            False
        """
    def tangent_line(self, p):
        """
        Return the tangent line at the point ``p``.

        INPUT:

        - ``p`` -- a rational point of the curve

        EXAMPLES::

            sage: P.<x,y,z,w> = ProjectiveSpace(QQ, 3)
            sage: C = Curve([x*y - z*w, x^2 - y*w, y^2*w - x*z*w], P)
            sage: p = C(1,1,1,1)
            sage: C.tangent_line(p)
            Projective Curve over Rational Field
             defined by -2*x + y + w, -3*x + z + 2*w
        """

class ProjectivePlaneCurve_field(ProjectivePlaneCurve, ProjectiveCurve_field):
    """
    Projective plane curves over fields.
    """
    def arithmetic_genus(self):
        """
        Return the arithmetic genus of this projective curve.

        This is the arithmetic genus `p_a(C)` as defined in [Har1977]_.

        For an irreducible projective plane curve of degree `d`, this is simply
        `(d - 1)(d - 2)/2`. It need *not* equal the geometric genus (the genus
        of the normalization of the curve).

        EXAMPLES::

            sage: x,y,z = PolynomialRing(GF(5), 3, 'xyz').gens()
            sage: C = Curve(y^2*z^7 - x^9 - x*z^8); C
            Projective Plane Curve over Finite Field of size 5
             defined by -x^9 + y^2*z^7 - x*z^8
            sage: C.arithmetic_genus()
            28
            sage: C.genus()  # geometric
            4

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([y^3*x - x^2*y*z - 7*z^4])
            sage: C.arithmetic_genus()
            3
        """
    def fundamental_group(self):
        """
        Return a presentation of the fundamental group of the complement
        of ``self``.

        .. NOTE::

            The curve must be defined over the rationals or a number field
            with an embedding over `\\QQbar`.

        .. NOTE::

           This functionality requires the ``sirocco`` package to be installed.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = P.curve(x^2*z - y^3)
            sage: C.fundamental_group()                                 # needs sirocco
            Finitely presented group < x0 | x0^3 >
            sage: g = P.curve(z*(x^2*z - y^3)).fundamental_group()      # needs sirocco
            sage: g.sorted_presentation()                               # needs sirocco
            Finitely presented group < x0, x1 | x1^-1*x0^-1*x1^-1*x0*x1*x0 >

        In the case of number fields, they need to have an embedding
        into the algebraic field::

            sage: # needs sage.rings.number_field
            sage: a = QQ[x](x^2 + 5).roots(QQbar)[0][0]
            sage: a
            -2.236067977499790?*I
            sage: F = NumberField(a.minpoly(), 'a', embedding=a)
            sage: P.<x,y,z> = ProjectiveSpace(F, 2)
            sage: F.inject_variables()
            Defining a
            sage: C = P.curve(x^2 + a * y^2)
            sage: C.fundamental_group()                         # needs sirocco
            Finitely presented group < x0 |  >

        TESTS::

            sage: F.<x0, x1> = FreeGroup()
            sage: G = F / [x1^-1*(x1^-1*x0^-1*x1*x0^-1)^2, (x1^-1*x0^-1)^2*x1^-1*(x0*x1)^2*x0]
            sage: G.order()
            320
            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = P.curve(z^2*y^3 - z*(33*x*z+2*x^2+8*z^2)*y^2
            ....:             + (21*z^2+21*x*z-x^2)*(z^2+11*x*z-x^2)*y
            ....:             + (x-18*z)*(z^2+11*x*z-x^2)^2)
            sage: G0 = C.fundamental_group()                    # needs sirocco
            sage: G.is_isomorphic(G0)                           # needs sirocco
            True
            sage: C = P.curve(z)
            sage: C.fundamental_group()                         # needs sirocco
            Finitely presented group <  |  >
        """
    def rational_parameterization(self):
        """
        Return a rational parameterization of this curve.

        This curve must have rational coefficients and be absolutely irreducible (i.e. irreducible
        over the algebraic closure of the rational field). The curve must also be rational (have
        geometric genus zero).

        The rational parameterization may have coefficients in a quadratic extension of the rational
        field.

        OUTPUT: a birational map between `\\mathbb{P}^{1}` and this curve, given as a scheme morphism

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([y^2*z - x^3], P)
            sage: C.rational_parameterization()
            Scheme morphism:
              From: Projective Space of dimension 1 over Rational Field
              To:   Projective Plane Curve over Rational Field
                    defined by -x^3 + y^2*z
              Defn: Defined on coordinates by sending (s : t) to
                    (s^2*t : s^3 : t^3)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([x^3 - 4*y*z^2 + x*z^2 - x*y*z], P)
            sage: C.rational_parameterization()
            Scheme morphism:
              From: Projective Space of dimension 1 over Rational Field
              To:   Projective Plane Curve over Rational Field
                    defined by x^3 - x*y*z + x*z^2 - 4*y*z^2
              Defn: Defined on coordinates by sending (s : t) to
                    (4*s^2*t + s*t^2 : s^2*t + t^3 : 4*s^3 + s^2*t)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve([x^2 + y^2 + z^2], P)
            sage: C.rational_parameterization()
            Scheme morphism:
              From: Projective Space of dimension 1 over Number Field in a
                    with defining polynomial a^2 + 1
              To:   Projective Plane Curve over Number Field in a
                    with defining polynomial a^2 + 1 defined by x^2 + y^2 + z^2
              Defn: Defined on coordinates by sending (s : t) to
                    ((-a)*s^2 + (-a)*t^2 : s^2 - t^2 : 2*s*t)
        """
    def riemann_surface(self, **kwargs):
        """
        Return the complex Riemann surface determined by this curve.

        OUTPUT: a :class:`~sage.schemes.riemann_surfaces.riemann_surface.RiemannSurface` object

        EXAMPLES::

            sage: R.<x,y,z> = QQ[]
            sage: C = Curve(x^3 + 3*y^3 + 5*z^3)
            sage: C.riemann_surface()
            Riemann surface defined by polynomial f = x^3 + 3*y^3 + 5 = 0,
            with 53 bits of precision
        """

class ProjectivePlaneCurve_finite_field(ProjectivePlaneCurve_field):
    """
    Projective plane curves over finite fields
    """
    def rational_points_iterator(self) -> Generator[Incomplete]:
        """
        Return a generator object for the rational points on this curve.

        INPUT:

        - ``self`` -- a projective curve

        OUTPUT: a generator of all the rational points on the curve defined over its base field

        EXAMPLES::

            sage: F = GF(37)
            sage: P2.<X,Y,Z> = ProjectiveSpace(F, 2)
            sage: C = Curve(X^7 + Y*X*Z^5*55 + Y^7*12)
            sage: len(list(C.rational_points_iterator()))
            37

        ::

            sage: F = GF(2)
            sage: P2.<X,Y,Z> = ProjectiveSpace(F, 2)
            sage: C = Curve(X*Y*Z)
            sage: a = C.rational_points_iterator()
            sage: next(a)
            (1 : 0 : 0)
            sage: next(a)
            (0 : 1 : 0)
            sage: next(a)
            (1 : 1 : 0)
            sage: next(a)
            (0 : 0 : 1)
            sage: next(a)
            (1 : 0 : 1)
            sage: next(a)
            (0 : 1 : 1)
            sage: next(a)
            Traceback (most recent call last):
            ...
            StopIteration

        ::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(3^2,'a')
            sage: P2.<X,Y,Z> = ProjectiveSpace(F, 2)
            sage: C = Curve(X^3 + 5*Y^2*Z - 33*X*Y*X)
            sage: b = C.rational_points_iterator()
            sage: next(b)
            (0 : 1 : 0)
            sage: next(b)
            (0 : 0 : 1)
            sage: next(b)
            (2*a + 2 : a : 1)
            sage: next(b)
            (2 : a + 1 : 1)
            sage: next(b)
            (a + 1 : 2*a + 1 : 1)
            sage: next(b)
            (1 : 2 : 1)
            sage: next(b)
            (2*a + 2 : 2*a : 1)
            sage: next(b)
            (2 : 2*a + 2 : 1)
            sage: next(b)
            (a + 1 : a + 2 : 1)
            sage: next(b)
            (1 : 1 : 1)
            sage: next(b)
            Traceback (most recent call last):
            ...
            StopIteration
        """
    def riemann_roch_basis(self, D):
        """
        Return a basis for the Riemann-Roch space corresponding to `D`.

        This uses Singular's Brill-Noether implementation.

        INPUT:

        - ``D`` -- a divisor

        OUTPUT: list of function field elements that form a basis of the
        Riemann-Roch space

        EXAMPLES::

            sage: R.<x,y,z> = GF(2)[]
            sage: f = x^3*y + y^3*z + x*z^3
            sage: C = Curve(f); pts = C.rational_points()
            sage: D = C.divisor([ (4, pts[0]), (4, pts[2]) ])
            sage: C.riemann_roch_basis(D)
            [x/y, 1, z/y, z^2/y^2, z/x, z^2/(x*y)]

        ::

            sage: R.<x,y,z> = GF(5)[]
            sage: f = x^7 + y^7 + z^7
            sage: C = Curve(f); pts = C.rational_points()
            sage: D = C.divisor([ (3, pts[0]), (-1,pts[1]), (10, pts[5]) ])
            sage: C.riemann_roch_basis(D)
            [(-2*x + y)/(x + y), (-x + z)/(x + y)]

        .. NOTE::

            Currently this only works over prime field and divisors
            supported on rational points.
        """
    def rational_points(self, algorithm: str = 'enum', sort: bool = True):
        """
        Return the rational points on this curve.

        INPUT:

        - ``algorithm`` -- one of

           - ``'enum'`` -- straightforward enumeration

           - ``'bn'`` -- via Singular's brnoeth package

        - ``sort`` -- boolean (default: ``True``); whether the output
          points should be sorted.  If ``False``, the order of the output
          is non-deterministic.

        OUTPUT: list of all the rational points on the curve, possibly sorted

        .. NOTE::

           The Brill-Noether package does not always work (i.e., the 'bn'
           algorithm. When it fails a :exc:`RuntimeError` exception is raised.

        EXAMPLES::

            sage: x, y, z = PolynomialRing(GF(5), 3, 'xyz').gens()
            sage: f = y^2*z^7 - x^9 - x*z^8
            sage: C = Curve(f); C
            Projective Plane Curve over Finite Field of size 5
             defined by -x^9 + y^2*z^7 - x*z^8
            sage: C.rational_points()
            [(0 : 0 : 1), (0 : 1 : 0), (2 : 2 : 1), (2 : 3 : 1),
             (3 : 1 : 1), (3 : 4 : 1)]
            sage: C = Curve(x - y + z)
            sage: C.rational_points()
            [(0 : 1 : 1), (1 : 1 : 0), (1 : 2 : 1), (2 : 3 : 1),
             (3 : 4 : 1), (4 : 0 : 1)]
            sage: C = Curve(x*z + z^2)
            sage: C.rational_points('all')
            [(0 : 1 : 0), (1 : 0 : 0), (1 : 1 : 0), (2 : 1 : 0),
             (3 : 1 : 0), (4 : 0 : 1), (4 : 1 : 0), (4 : 1 : 1),
             (4 : 2 : 1), (4 : 3 : 1), (4 : 4 : 1)]

        ::

            sage: F = GF(7)
            sage: P2.<X,Y,Z> = ProjectiveSpace(F, 2)
            sage: C = Curve(X^3 + Y^3 - Z^3)
            sage: C.rational_points()
            [(0 : 1 : 1), (0 : 2 : 1), (0 : 4 : 1), (1 : 0 : 1), (2 : 0 : 1),
            (3 : 1 : 0), (4 : 0 : 1), (5 : 1 : 0), (6 : 1 : 0)]

        ::

            sage: F = GF(1237)
            sage: P2.<X,Y,Z> = ProjectiveSpace(F, 2)
            sage: C = Curve(X^7 + 7*Y^6*Z + Z^4*X^2*Y*89)
            sage: len(C.rational_points())
            1237

        ::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(2^6,'a')
            sage: P2.<X,Y,Z> = ProjectiveSpace(F, 2)
            sage: C = Curve(X^5 + 11*X*Y*Z^3 + X^2*Y^3 - 13*Y^2*Z^3)
            sage: len(C.rational_points())
            104

        ::

            sage: R.<x,y,z> = GF(2)[]
            sage: f = x^3*y + y^3*z + x*z^3
            sage: C = Curve(f); pts = C.rational_points()
            sage: pts
            [(0 : 0 : 1), (0 : 1 : 0), (1 : 0 : 0)]
        """

class IntegralProjectiveCurve(ProjectiveCurve_field):
    """
    Integral projective curve.
    """
    def __init__(self, A, f) -> None:
        """
        Initialize.

        TESTS::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: C = Curve(y^2*z^7 - x^9 - x*z^8)
            sage: loads(dumps(C)) == C
            True
        """
    def function_field(self):
        """
        Return the function field of this curve.

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve(x^2 + y^2 + z^2, P)
            sage: C.function_field()
            Function field in z defined by z^2 + y^2 + 1

        ::

            sage: # needs sage.rings.finite_rings
            sage: P.<x,y,z> = ProjectiveSpace(GF(4), 2)
            sage: C = Curve(x^5 + y^5 + x*y*z^3 + z^5)
            sage: C.function_field()
            Function field in z defined by z^5 + y*z^3 + y^5 + 1
        """
    def __call__(self, *args):
        """
        Return a rational point, a pointset or a function depending on ``args``.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: P.<x,y,z> = ProjectiveSpace(GF(4), 2)
            sage: C = Curve(x^5 + y^5 + x*y*z^3 + z^5)
            sage: C(1,1,1)
            (1 : 1 : 1)
            sage: C(y/z)
            (y/(y^5 + 1))*z^4 + (y^2/(y^5 + 1))*z^2
            sage: C(GF(4^2))
            Set of rational points of Closed subscheme of Projective Space of
             dimension 2 over Finite Field in z4 of size 2^4 defined by:
              x^5 + y^5 + x*y*z^3 + z^5
        """
    def function(self, f):
        """
        Return the function field element corresponding to ``f``.

        INPUT:

        - ``f`` -- a fraction of homogeneous polynomials of the coordinate ring
          of the ambient space of the curve

        OUTPUT: an element of the function field

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: P.<x,y,z> = ProjectiveSpace(GF(4), 2)
            sage: C = Curve(x^5 + y^5 + x*y*z^3 + z^5)
            sage: f = C.function(x/y); f
            1/y
            sage: f.divisor()
            Place (1/y, 1/y^2*z^2 + z2/y*z + 1)
             + Place (1/y, 1/y^2*z^2 + ((z2 + 1)/y)*z + 1)
             + Place (1/y, 1/y*z + 1)
             - Place (y, z^2 + z2*z + 1)
             - Place (y, z^2 + (z2 + 1)*z + 1)
             - Place (y, z + 1)
        """
    def coordinate_functions(self, i=None):
        """
        Return the coordinate functions for the ``i``-th affine patch.

        If ``i`` is ``None``, return the homogeneous coordinate functions.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: P.<x,y,z> = ProjectiveSpace(GF(4), 2)
            sage: C = Curve(x^5 + y^5 + x*y*z^3 + z^5)
            sage: C.coordinate_functions(0)
            (y, z)
            sage: C.coordinate_functions(1)
            (1/y, 1/y*z)
        """
    def pull_from_function_field(self, f):
        """
        Return the fraction corresponding to ``f``.

        INPUT:

        - ``f`` -- an element of the function field

        OUTPUT:

        A fraction of homogeneous polynomials in the coordinate ring of the
        ambient space of the curve.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: P.<x,y,z> = ProjectiveSpace(GF(4), 2)
            sage: C = Curve(x^5 + y^5 + x*y*z^3 + z^5)
            sage: F = C.function_field()
            sage: C.pull_from_function_field(F.gen())
            z/x
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

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve(y^2*z - x^3, P)
            sage: C.singular_closed_points()
            [Point (x, y)]

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: C = Curve(y^2*z^7 - x^9 - x*z^8)
            sage: C.singular_closed_points()
            [Point (x, z)]
        """
    @cached_method
    def place_to_closed_point(self, place):
        """
        Return the closed point at the place.

        INPUT:

        - ``place`` -- a place of the function field of the curve

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: C = Curve(y^2*z^7 - x^9 - x*z^8)
            sage: pls = C.places()
            sage: C.place_to_closed_point(pls[-1])
            Point (x - 2*z, y - 2*z)
            sage: pls2 = C.places(2)
            sage: C.place_to_closed_point(pls2[0])
            Point (y^2 + y*z + z^2, x + y)
        """
    def places_on(self, point):
        """
        Return the places on the closed point.

        INPUT:

        - ``point`` -- a closed point of the curve

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(QQ, 2)
            sage: C = Curve(x*y*z^4 - x^6 - y^6)
            sage: C.singular_closed_points()
            [Point (x, y)]
            sage: p, = _
            sage: C.places_on(p)
            [Place (1/y, 1/y^2*z, 1/y^3*z^2, 1/y^4*z^3),
             Place (y, y*z, y*z^2, y*z^3)]
            sage: pl1, pl2 =_
            sage: C.place_to_closed_point(pl1)
            Point (x, y)
            sage: C.place_to_closed_point(pl2)
            Point (x, y)

        ::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: C = Curve(x^2*z - y^3)
            sage: [C.places_on(p) for p in C.closed_points()]
            [[Place (1/y)],
             [Place (y)],
             [Place (y + 1)],
             [Place (y + 2)],
             [Place (y + 3)],
             [Place (y + 4)]]
        """
    def jacobian(self, model, base_div=None):
        """
        Return the Jacobian of this curve.

        INPUT:

        - ``model`` -- model to use for arithmetic

        - ``base_div`` -- an effective divisor for the model

        The degree of the base divisor should satisfy certain degree condition
        corresponding to the model used. The following table lists these
        conditions. Let `g` be the geometric genus of the curve.

        - ``hess``: ideal-based arithmetic; requires base divisor of degree `g`

        - ``km_large``: Khuri-Makdisi's large model; requires base divisor of
          degree at least `2g + 1`

        - ``km_medium``: Khuri-Makdisi's medium model; requires base divisor of
          degree at least `2g + 1`

        - ``km_small``: Khuri-Makdisi's small model requires base divisor of
          degree at least `g + 1`

        We assume the curve (or its function field) has a rational place. If a
        base divisor is not given, one is chosen using a rational place.

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(GF(5), 2)
            sage: C = Curve(y^2*(x^3 - 1) - (x^3 - 2)).projective_closure()
            sage: J = C.jacobian(model='hess'); J
            Jacobian of Projective Plane Curve over Finite Field of size 5
             defined by 2*x0^5 - x0^2*x1^3 - x0^3*x2^2 + x1^3*x2^2 (Hess model)
            sage: J.base_divisor().degree() == C.genus()
            True
        """

class IntegralProjectiveCurve_finite_field(IntegralProjectiveCurve):
    """
    Integral projective curve over a finite field.

    INPUT:

    - ``A`` -- an ambient projective space

    - ``f`` -- homogeneous polynomials defining the curve

    EXAMPLES::

        sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
        sage: C = Curve(y^2*z^7 - x^9 - x*z^8)
        sage: C.function_field()
        Function field in z defined by z^8 + 4*y^2*z^7 + 1
        sage: C.closed_points()
        [Point (x, z),
         Point (x, y),
         Point (x - 2*z, y + 2*z),
         Point (x + 2*z, y + z),
         Point (x + 2*z, y - z),
         Point (x - 2*z, y - 2*z)]
    """
    def places(self, degree: int = 1):
        """
        Return all places on the curve of the ``degree``.

        INPUT:

        - ``degree`` -- positive integer

        EXAMPLES::

            sage: P.<x,y,z> = ProjectiveSpace(GF(5), 2)
            sage: C = Curve(x^2*z - y^3)
            sage: C.places()
            [Place (1/y),
             Place (y),
             Place (y + 1),
             Place (y + 2),
             Place (y + 3),
             Place (y + 4)]
            sage: C.places(2)
            [Place (y^2 + 2),
             Place (y^2 + 3),
             Place (y^2 + y + 1),
             Place (y^2 + y + 2),
             Place (y^2 + 2*y + 3),
             Place (y^2 + 2*y + 4),
             Place (y^2 + 3*y + 3),
             Place (y^2 + 3*y + 4),
             Place (y^2 + 4*y + 1),
             Place (y^2 + 4*y + 2)]
        """
    def closed_points(self, degree: int = 1):
        """
        Return a list of closed points of ``degree`` of the curve.

        INPUT:

        - ``degree`` -- positive integer

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(GF(9),2)
            sage: C = Curve(y^2 - x^5 - x^4 - 2*x^3 - 2*x-2)
            sage: Cp = C.projective_closure()
            sage: Cp.closed_points()
            [Point (x0, x1),
             Point (x0 + (-z2 - 1)*x2, x1),
             Point (x0 + (z2 + 1)*x2, x1),
             Point (x0 + z2*x2, x1 + (z2 - 1)*x2),
             Point (x0 + (-z2)*x2, x1 + (-z2 + 1)*x2),
             Point (x0 + (-z2 - 1)*x2, x1 + (-z2 - 1)*x2),
             Point (x0 + (z2 + 1)*x2, x1 + (z2 + 1)*x2),
             Point (x0 + (z2 - 1)*x2, x1 + z2*x2),
             Point (x0 + (-z2 + 1)*x2, x1 + (-z2)*x2),
             Point (x0 + x2, x1 - x2),
             Point (x0 - x2, x1 + x2)]
        """
    @cached_method
    def L_polynomial(self, name: str = 't'):
        """
        Return the L-polynomial of this possibly singular curve.

        INPUT:

        - ``name`` -- (default: ``t``) name of the variable of the polynomial

        EXAMPLES::

            sage: A.<x,y> = AffineSpace(GF(3), 2)
            sage: C = Curve(y^2 - x^5 - x^4 - 2*x^3 - 2*x - 2)
            sage: Cbar = C.projective_closure()
            sage: Cbar.L_polynomial()
            9*t^4 - 3*t^3 + t^2 - t + 1
        """
    def number_of_rational_points(self, r: int = 1):
        """
        Return the number of rational points of the curve with
        constant field extended by degree ``r``.

        INPUT:

        - ``r`` -- positive integer (default: `1`)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<x,y> = AffineSpace(GF(3), 2)
            sage: C = Curve(y^2 - x^5 - x^4 - 2*x^3 - 2*x - 2)
            sage: Cbar = C.projective_closure()
            sage: Cbar.number_of_rational_points(3)
            21
            sage: D = Cbar.change_ring(Cbar.base_ring().extension(3))
            sage: D.base_ring()
            Finite Field in z3 of size 3^3
            sage: len(D.closed_points())
            21
        """

class IntegralProjectivePlaneCurve(IntegralProjectiveCurve, ProjectivePlaneCurve_field): ...
class IntegralProjectivePlaneCurve_finite_field(IntegralProjectiveCurve_finite_field, ProjectivePlaneCurve_finite_field):
    """
    Integral projective plane curve over a finite field.

    INPUT:

    - ``A`` -- ambient projective plane

    - ``f`` -- a homogeneous equation that defines the curve

    EXAMPLES::

        sage: # needs sage.rings.finite_rings
        sage: A.<x,y> = AffineSpace(GF(9), 2)
        sage: C = Curve(y^2 - x^5 - x^4 - 2*x^3 - 2*x - 2)
        sage: Cb = C.projective_closure()
        sage: Cb.singular_closed_points()
        [Point (x0, x1)]
        sage: Cb.function_field()
        Function field in y defined by y^2 + 2*x^5 + 2*x^4 + x^3 + x + 1
    """

def Hasse_bounds(q, genus: int = 1):
    """
    Return the Hasse-Weil bounds for the cardinality of a nonsingular
    curve defined over `\\GF{q}` of given ``genus``.

    INPUT:

    - ``q`` -- integer; a prime power

    - ``genus`` -- nonnegative integer (default: 1)

    OUTPUT: tuple; the Hasse bounds (lb,ub) for the cardinality of a curve of
    genus ``genus`` defined over `\\GF{q}`

    EXAMPLES::

        sage: Hasse_bounds(2)
        (1, 5)
        sage: Hasse_bounds(next_prime(10^30))                                           # needs sage.libs.pari
        (999999999999998000000000000058, 1000000000000002000000000000058)
    """
