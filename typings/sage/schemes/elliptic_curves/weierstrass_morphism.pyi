from .constructor import EllipticCurve as EllipticCurve
from _typeshed import Incomplete
from sage.rings.integer import Integer as Integer
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.schemes.elliptic_curves.hom import EllipticCurveHom as EllipticCurveHom
from sage.structure.element import get_coercion_model as get_coercion_model
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from sage.structure.sequence import Sequence as Sequence

class baseWI:
    """
    This class implements the basic arithmetic of isomorphisms between
    Weierstrass models of elliptic curves.

    These are specified by lists of the form `[u,r,s,t]` (with `u \\neq 0`)
    which specifies a transformation `(x,y) \\mapsto (x',y')` where

            `(x,y) = (u^2x'+r , u^3y' + su^2x' + t).`

    INPUT:

    - ``u``, ``r``, ``s``, ``t`` -- (default: `1`, `0`, `0`, `0`); standard
      parameters of an isomorphism between Weierstrass models

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.weierstrass_morphism import *
        sage: baseWI()
        (1, 0, 0, 0)
        sage: baseWI(2,3,4,5)
        (2, 3, 4, 5)
        sage: R.<u,r,s,t> = QQ[]
        sage: baseWI(u,r,s,t)
        (u, r, s, t)
    """
    u: Incomplete
    r: Incomplete
    s: Incomplete
    t: Incomplete
    def __init__(self, u: int = 1, r: int = 0, s: int = 0, t: int = 0) -> None:
        """
        Constructor: check for valid parameters (defaults to identity).

        INPUT:

        - ``u``, ``r``, ``s``, ``t`` -- (default: `1`, `0`, `0`, `0`); standard
          parameters of an isomorphism between Weierstrass models

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import *
            sage: baseWI()
            (1, 0, 0, 0)
            sage: baseWI(2,3,4,5)
            (2, 3, 4, 5)
            sage: R.<u,r,s,t> = QQ[]
            sage: baseWI(u,r,s,t)
            (u, r, s, t)
        """
    def tuple(self):
        """
        Return the parameters `u,r,s,t` as a tuple.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import *
            sage: w = baseWI(2,3,4,5)
            sage: w.tuple()
            (2, 3, 4, 5)
        """
    def __mul__(self, other):
        """
        Return the composition of this isomorphism and another.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import *
            sage: baseWI(1,2,3,4)*baseWI(5,6,7,8)
            (5, 56, 22, 858)
            sage: baseWI()*baseWI(1,2,3,4)*baseWI()
            (1, 2, 3, 4)
        """
    def __invert__(self):
        """
        Return the inverse of this isomorphism.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import *
            sage: w = baseWI(2,3,4,5)
            sage: ~w
            (1/2, -3/4, -2, 7/8)
            sage: w*~w
            (1, 0, 0, 0)
            sage: ~w*w
            (1, 0, 0, 0)
            sage: R.<u,r,s,t> = QQ[]
            sage: w = baseWI(u,r,s,t)
            sage: ~w
            (1/u, (-r)/u^2, (-s)/u, (r*s - t)/u^3)
            sage: ~w*w
            (1, 0, 0, 0)
        """
    def is_identity(self):
        """
        Return ``True`` if this is the identity isomorphism.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import *
            sage: w = baseWI(); w.is_identity()
            True
            sage: w = baseWI(2,3,4,5); w.is_identity()
            False
        """
    def __call__(self, EorP):
        """
        Base application of isomorphisms to curves and points.

        A baseWI `w` may be applied to a list `[a1,a2,a3,a4,a6]`
        representing the `a`-invariants of an elliptic curve `E`,
        returning the `a`-invariants of `w(E)`; or to `P=[x,y]` or
        `P=[x,y,z]` representing a point in `\\mathbb{A}^2` or
        `\\mathbb{P}^2`, returning the transformed point.

        INPUT:

        - ``EorP`` -- either an elliptic curve, or a point on an elliptic curve

        OUTPUT: the transformed curve or point

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import *
            sage: E = EllipticCurve([0,0,1,-7,6])
            sage: w = baseWI(2,3,4,5)
            sage: w(E.ainvs())
            [4, -7/4, 11/8, -3/2, -9/32]
            sage: P = E(-2,3)
            sage: w(P.xy())
            [-5/4, 9/4]
            sage: EllipticCurve(w(E.ainvs()))(w(P.xy()))
            (-5/4 : 9/4 : 1)
        """

class WeierstrassIsomorphism(EllipticCurveHom, baseWI):
    """
    Class representing a Weierstrass isomorphism between two elliptic curves.

    INPUT:

    - ``E`` -- an ``EllipticCurve``, or ``None`` (see below)

    - ``urst`` -- a 4-tuple `(u,r,s,t)`, a :class:`baseWI` object,
      or ``None`` (see below)

    - ``F`` -- an ``EllipticCurve``, or ``None`` (see below)

    Given two Elliptic Curves ``E`` and ``F`` (represented by Weierstrass
    models as usual), and a transformation ``urst`` from ``E`` to ``F``,
    construct an isomorphism from ``E`` to ``F``.
    An exception is raised if ``urst(E) != F``.  At most one of ``E``,
    ``F``, ``urst`` can be ``None``.  In this case, the missing input is
    constructed from the others in such a way that ``urst(E) == F`` holds,
    and an exception is raised if this is impossible (typically because
    ``E`` and ``F`` are not isomorphic).

    Users will not usually need to use this class directly, but instead use
    methods such as
    :meth:`~sage.schemes.elliptic_curves.ell_generic.EllipticCurve_generic.isomorphism_to`
    or
    :meth:`~sage.schemes.elliptic_curves.ell_generic.EllipticCurve_generic.isomorphisms`.

    Explicitly, the isomorphism defined by `(u,r,s,t)` maps a point `(x,y)`
    to the point

    .. MATH::

        ((x-r) / u^2, \\; (y - s(x-r) - t) / u^3) .

    If the domain `E` has Weierstrass coefficients `[a_1,a_2,a_3,a_4,a_6]`,
    the codomain `F` is given by

    .. MATH::

        a_1' &= (a_1 + 2s) / u \\\\\n        a_2' &= (a_2 - a_1s + 3r - s^2) / u^2 \\\\\n        a_3' &= (a_3 + a_1r + 2t) / u^3 \\\\\n        a_4' &= (a_4 + 2a_2r - a_1(rs+t) - a_3s + 3r^2 - 2st) / u^4 \\\\\n        a_6' &= (a_6 - a_1rt + a_2r^2 - a_3t + a_4r + r^3 - t^2) / u^6 .

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.weierstrass_morphism import *
        sage: WeierstrassIsomorphism(EllipticCurve([0,1,2,3,4]), (-1,2,3,4))
        Elliptic-curve morphism:
          From: Elliptic Curve defined by y^2 + 2*y = x^3 + x^2 + 3*x + 4 over Rational Field
          To:   Elliptic Curve defined by y^2 - 6*x*y - 10*y = x^3 - 2*x^2 - 11*x - 2 over Rational Field
          Via:  (u,r,s,t) = (-1, 2, 3, 4)
        sage: E = EllipticCurve([0,1,2,3,4])
        sage: F = EllipticCurve(E.cremona_label())
        sage: WeierstrassIsomorphism(E, None, F)
        Elliptic-curve morphism:
          From: Elliptic Curve defined by y^2 + 2*y = x^3 + x^2 + 3*x + 4 over Rational Field
          To:   Elliptic Curve defined by y^2  = x^3 + x^2 + 3*x + 5 over Rational Field
          Via:  (u,r,s,t) = (1, 0, 0, -1)
        sage: w = WeierstrassIsomorphism(None, (1,0,0,-1), F)
        sage: w._domain == E
        True
    """
    def __init__(self, E=None, urst=None, F=None) -> None:
        """
        Constructor for the ``WeierstrassIsomorphism`` class.

        TESTS:

        Check for :issue:`33215`::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
            sage: E = EllipticCurve(GF(71^2), [5,5])                                    # needs sage.rings.finite_rings
            sage: iso = WeierstrassIsomorphism(E, (1,2,3,4))                            # needs sage.rings.finite_rings
            sage: ~iso  # indirect doctest                                              # needs sage.rings.finite_rings
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 + 6*x*y + 8*y = x^3 + 68*x^2 + 64*x + 7 over Finite Field in z2 of size 71^2
              To:   Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field in z2 of size 71^2
              Via:  (u,r,s,t) = (1, 69, 68, 2)

        Test for :issue:`33312`::

            sage: type(iso.degree())                                                    # needs sage.rings.finite_rings
            <class 'sage.rings.integer.Integer'>
        """
    def __invert__(self):
        """
        Return the inverse of this WeierstrassIsomorphism.

        EXAMPLES::

            sage: E = EllipticCurve('5077')
            sage: F = E.change_weierstrass_model([2,3,4,5]); F
            Elliptic Curve defined by y^2 + 4*x*y + 11/8*y = x^3 - 7/4*x^2 - 3/2*x - 9/32 over Rational Field
            sage: w = E.isomorphism_to(F)
            sage: P = E(-2,3,1)
            sage: w(P)
            (-5/4 : 9/4 : 1)
            sage: ~w
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 + 4*x*y + 11/8*y = x^3 - 7/4*x^2 - 3/2*x - 9/32 over Rational Field
              To:   Elliptic Curve defined by y^2 + y = x^3 - 7*x + 6 over Rational Field
              Via:  (u,r,s,t) = (1/2, -3/4, -2, 7/8)
            sage: Q = w(P); Q
            (-5/4 : 9/4 : 1)
            sage: (~w)(Q)
            (-2 : 3 : 1)
        """
    def rational_maps(self):
        """
        Return the pair of rational maps defining this isomorphism.

        EXAMPLES::

            sage: E1 = EllipticCurve([11,22,33,44,55])
            sage: E2 = EllipticCurve_from_j(E1.j_invariant())
            sage: iso = E1.isomorphism_to(E2); iso
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 + 11*x*y + 33*y = x^3 + 22*x^2 + 44*x + 55
                    over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y = x^3 + x^2 - 684*x + 6681
                    over Rational Field
              Via:  (u,r,s,t) = (1, -17, -5, 77)
            sage: iso.rational_maps()
            (x + 17, 5*x + y + 8)
            sage: f = E2.defining_polynomial()(*iso.rational_maps(), 1)
            sage: I = E1.defining_ideal()
            sage: x,y,z = I.ring().gens()
            sage: f in I + Ideal(z-1)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: E = EllipticCurve(GF(65537), [1,1,1,1,1])
            sage: w = E.isomorphism_to(E.short_weierstrass_model())
            sage: f,g = w.rational_maps()
            sage: P = E.random_point()
            sage: w(P).xy() == (f(P.xy()), g(P.xy()))
            True

        TESTS:

        Check for :issue:`34811`::

            sage: iso.rational_maps()[0].parent()
            Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
            sage: iso.rational_maps()[1].parent()
            Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
        """
    def x_rational_map(self):
        """
        Return the `x`-coordinate rational map of this isomorphism.

        EXAMPLES::

            sage: E1 = EllipticCurve([11,22,33,44,55])
            sage: E2 = EllipticCurve_from_j(E1.j_invariant())
            sage: iso = E1.isomorphism_to(E2); iso
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 + 11*x*y + 33*y = x^3 + 22*x^2 + 44*x + 55
                    over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y = x^3 + x^2 - 684*x + 6681
                    over Rational Field
              Via:  (u,r,s,t) = (1, -17, -5, 77)
            sage: iso.x_rational_map()
            x + 17
            sage: iso.x_rational_map() == iso.rational_maps()[0]
            True

        TESTS:

        Check for :issue:`34811`::

            sage: iso.x_rational_map().parent()
            Fraction Field of Univariate Polynomial Ring in x over Rational Field
        """
    def kernel_polynomial(self):
        """
        Return the kernel polynomial of this isomorphism.

        Isomorphisms have trivial kernel by definition, hence this
        method always returns `1`.

        EXAMPLES::

            sage: E1 = EllipticCurve([11,22,33,44,55])
            sage: E2 = EllipticCurve_from_j(E1.j_invariant())
            sage: iso = E1.isomorphism_to(E2)
            sage: iso.kernel_polynomial()
            1
            sage: psi = E1.isogeny(iso.kernel_polynomial(), codomain=E2); psi
            Isogeny of degree 1
             from Elliptic Curve defined by y^2 + 11*x*y + 33*y = x^3 + 22*x^2 + 44*x + 55
                  over Rational Field
               to Elliptic Curve defined by y^2 + x*y = x^3 + x^2 - 684*x + 6681
                  over Rational Field
            sage: psi in {iso, -iso}
            True

        TESTS::

            sage: iso.kernel_polynomial().parent()
            Univariate Polynomial Ring in x over Rational Field
        """
    def dual(self):
        """
        Return the dual isogeny of this isomorphism.

        For isomorphisms, the dual is just the inverse.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
            sage: E = EllipticCurve(QuadraticField(-3), [0,1])                          # needs sage.rings.number_field
            sage: w = WeierstrassIsomorphism(E, (CyclotomicField(3).gen(),0,0,0))       # needs sage.rings.number_field
            sage: (w.dual() * w).rational_maps()                                        # needs sage.rings.number_field
            (x, y)

        ::

            sage: E1 = EllipticCurve([11,22,33,44,55])
            sage: E2 = E1.short_weierstrass_model()
            sage: iso = E1.isomorphism_to(E2)
            sage: iso.dual() == ~iso
            True
        """
    def __neg__(self):
        """
        Return the negative of this isomorphism, i.e., its composition
        with the negation map `[-1]`.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
            sage: E = EllipticCurve([11,22,33,44,55])
            sage: w = WeierstrassIsomorphism(E, (66,77,88,99))
            sage: -w
            Elliptic-curve morphism:
              From: Elliptic Curve defined by y^2 + 11*x*y + 33*y = x^3 + 22*x^2 + 44*x + 55 over Rational Field
              To:   Elliptic Curve defined by y^2 + 17/6*x*y + 49/13068*y = x^3 - 769/396*x^2 - 3397/862488*x + 44863/7513995456
                    over Rational Field
              Via:  (u,r,s,t) = (-66, 77, -99, -979)
            sage: -(-w) == w
            True

        ::

            sage: # needs sage.rings.number_field
            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
            sage: K.<a> = QuadraticField(-3)
            sage: E = EllipticCurve(K, [0,1])
            sage: w = WeierstrassIsomorphism(E, (CyclotomicField(3).gen(),0,0,0))
            sage: w.tuple()
            (1/2*a - 1/2, 0, 0, 0)
            sage: (-w).tuple()
            (-1/2*a + 1/2, 0, 0, 0)
            sage: (-w)^3 == -(w^3)
            True

        ::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism, identity_morphism
            sage: E = EllipticCurve(QuadraticField(-1), [1,0])                          # needs sage.rings.number_field
            sage: t = WeierstrassIsomorphism(E, (i,0,0,0))                              # needs sage.rings.number_field
            sage: -t^2 == identity_morphism(E)                                          # needs sage.rings.number_field
            True
        """
    def scaling_factor(self):
        """
        Return the Weierstrass scaling factor associated to this
        Weierstrass isomorphism.

        The scaling factor is the constant `u` (in the base field)
        such that `\\varphi^* \\omega_2 = u \\omega_1`, where
        `\\varphi: E_1\\to E_2` is this isomorphism and `\\omega_i` are
        the standard Weierstrass differentials on `E_i` defined by
        `\\mathrm dx/(2y+a_1x+a_3)`.

        EXAMPLES::

            sage: E = EllipticCurve(QQbar, [0,1])                                       # needs sage.rings.number_field
            sage: all(f.scaling_factor() == f.formal()[1] for f in E.automorphisms())   # needs sage.rings.number_field
            True

        ALGORITHM: The scaling factor equals the `u` component of
        the tuple `(u,r,s,t)` defining the isomorphism.
        """
    def inseparable_degree(self):
        """
        Return the inseparable degree of this Weierstrass isomorphism.

        For isomorphisms, this method always returns one.

        TESTS::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
            sage: WeierstrassIsomorphism.inseparable_degree(None)
            1
        """
    def is_identity(self):
        """
        Check if this Weierstrass isomorphism is the identity.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
            sage: p = 97
            sage: Fp = GF(p)
            sage: E = EllipticCurve(Fp, [1, 28])
            sage: ws = WeierstrassIsomorphism(E, None, E)
            sage: ws.is_identity()
            False

        ::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
            sage: p = 97
            sage: Fp = GF(p)
            sage: E = EllipticCurve(Fp, [1, 28])
            sage: ws = WeierstrassIsomorphism(E, (1, 0, 0, 0), None)
            sage: ws.is_identity()
            True
        """
    def order(self):
        """
        Compute the order of this Weierstrass isomorphism if it is an automorphism.

        A :exc:`ValueError` is raised if the domain is not equal to the codomain.

        A :exc:`NotImplementedError` is raised if the order of the automorphism is not 1, 2, 3, 4 or 6.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import *
            sage: p = 97
            sage: Fp = GF(p)
            sage: E = EllipticCurve(Fp, [1, 28])
            sage: ws = WeierstrassIsomorphism(E, None, E)
            sage: ws.order()
            2

        TESTS::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import *
            sage: p = 97
            sage: Fp = GF(p)
            sage: E = EllipticCurve(Fp, [1, 28])
            sage: ws = WeierstrassIsomorphism(E, None, E)
            sage: ws.order()
            2
            sage: E1 = EllipticCurve(Fp, [1, 69])
            sage: ws = E.isomorphism_to(E1)
            sage: ws.order()
            Traceback (most recent call last):
            ...
            ValueError: the domain is different from the codomain

        ::

            sage: E = EllipticCurve_from_j(Fp(0))
            sage: ws = WeierstrassIsomorphism(E, (Fp(36), 0, 0, 0), None)
            sage: ws.order()
            6
            sage: ws2 = ws*ws
            sage: ws2.order()
            3
            sage: F2_bar = GF(2).algebraic_closure()
            sage: E = EllipticCurve_from_j(F2_bar(0))
            sage: ws = WeierstrassIsomorphism(E, None, E)
            sage: ws.order()
            3
        """

def identity_morphism(E):
    """
    Given an elliptic curve `E`, return the identity morphism
    on `E` as a :class:`WeierstrassIsomorphism`.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.weierstrass_morphism import identity_morphism
        sage: E = EllipticCurve([5,6,7,8,9])
        sage: id_ = identity_morphism(E)
        sage: id_.rational_maps()
        (x, y)
    """
def negation_morphism(E):
    """
    Given an elliptic curve `E`, return the negation endomorphism
    `[-1]` of `E` as a :class:`WeierstrassIsomorphism`.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.weierstrass_morphism import negation_morphism
        sage: E = EllipticCurve([5,6,7,8,9])
        sage: neg = negation_morphism(E)
        sage: neg.rational_maps()
        (x, -5*x - y - 7)
    """
