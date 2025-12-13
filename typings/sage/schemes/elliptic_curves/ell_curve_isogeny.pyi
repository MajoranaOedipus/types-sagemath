from sage.rings.fraction_field import FractionField as FractionField
from sage.rings.integer import Integer as Integer
from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.schemes.elliptic_curves.constructor import EllipticCurve as EllipticCurve
from sage.schemes.elliptic_curves.ell_generic import EllipticCurve_generic as EllipticCurve_generic
from sage.schemes.elliptic_curves.hom import EllipticCurveHom as EllipticCurveHom
from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism as WeierstrassIsomorphism, baseWI as baseWI, negation_morphism as negation_morphism
from sage.structure.sequence import Sequence as Sequence

def isogeny_codomain_from_kernel(E, kernel):
    """
    Compute the isogeny codomain given a kernel.

    INPUT:

    - ``E`` -- domain elliptic curve

    - ``kernel`` -- either a list of points in the kernel of the isogeny,
                    or a kernel polynomial (specified as either a
                    univariate polynomial or a coefficient list)

    OUTPUT: elliptic curve) The codomain of the separable normalized isogeny
    defined by this kernel.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import isogeny_codomain_from_kernel
        sage: E = EllipticCurve(GF(7), [1,0,1,0,1])
        sage: R.<x> = GF(7)[]
        sage: isogeny_codomain_from_kernel(E, [4,1])
        Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x + 6
         over Finite Field of size 7
        sage: (EllipticCurveIsogeny(E, [4,1]).codomain()
        ....:  == isogeny_codomain_from_kernel(E, [4,1]))
        True
        sage: isogeny_codomain_from_kernel(E, x^3 + x^2 + 4*x + 3)
        Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x + 6
         over Finite Field of size 7
        sage: isogeny_codomain_from_kernel(E, x^3 + 2*x^2 + 4*x + 3)
        Elliptic Curve defined by y^2 + x*y + y = x^3 + 5*x + 2
         over Finite Field of size 7

        sage: # needs sage.rings.finite_rings
        sage: E = EllipticCurve(GF(19), [1,2,3,4,5])
        sage: kernel_list = [E((15,10)), E((10,3)), E((6,5))]
        sage: isogeny_codomain_from_kernel(E, kernel_list)
        Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 3*x + 15
         over Finite Field of size 19
    """
def compute_codomain_formula(E, v, w):
    """
    Compute the codomain curve given parameters `v` and `w` (as in
    Vélu/Kohel/etc. formulas).

    INPUT:

    - ``E`` -- an elliptic curve

    - ``v``, ``w`` -- elements of the base field of ``E``

    OUTPUT:

    The elliptic curve with invariants
    `[a_1,a_2,a_3,a_4-5v,a_6-(a_1^2+4a_2)v-7w]` where
    `E = [a_1,a_2,a_3,a_4,a_6]`.

    EXAMPLES:

    This formula is used by every invocation of the
    :class:`EllipticCurveIsogeny` constructor::

        sage: E = EllipticCurve(GF(19), [1,2,3,4,5])
        sage: phi = EllipticCurveIsogeny(E, E((1,2)) )
        sage: phi.codomain()
        Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 9*x + 13
         over Finite Field of size 19
        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import compute_codomain_formula
        sage: v = phi._EllipticCurveIsogeny__v
        sage: w = phi._EllipticCurveIsogeny__w
        sage: compute_codomain_formula(E, v, w) == phi.codomain()
        True
    """
def compute_vw_kohel_even_deg1(x0, y0, a1, a2, a4):
    """
    Compute Vélu's `(v,w)` using Kohel's formulas for isogenies of
    degree exactly divisible by `2`.

    INPUT:

    - ``x0``, ``y0`` -- coordinates of a 2-torsion point on an elliptic curve `E`

    - ``a1``, ``a2``, ``a4`` -- invariants of `E`

    OUTPUT: Vélu's isogeny parameters `(v,w)`.

    EXAMPLES:

    This function will be implicitly called by the following example::

        sage: E = EllipticCurve(GF(19), [1,2,3,4,5])
        sage: phi = EllipticCurveIsogeny(E, [9,1]); phi
        Isogeny of degree 2
         from Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5
              over Finite Field of size 19
           to Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 9*x + 8
              over Finite Field of size 19
        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import compute_vw_kohel_even_deg1
        sage: a1,a2,a3,a4,a6 = E.a_invariants()
        sage: x0 = -9
        sage: y0 = -(a1*x0 + a3)/2
        sage: compute_vw_kohel_even_deg1(x0, y0, a1, a2, a4)
        (18, 9)
    """
def compute_vw_kohel_even_deg3(b2, b4, s1, s2, s3):
    """
    Compute Vélu's `(v,w)` using Kohel's formulas for isogenies of
    degree divisible by `4`.

    INPUT:

    - ``b2``, ``b4`` -- invariants of an elliptic curve `E`

    - ``s1``, ``s2``, ``s3`` -- signed coefficients of the 2-division
      polynomial of `E`

    OUTPUT: Vélu's isogeny parameters `(v,w)`.

    EXAMPLES:

    This function will be implicitly called by the following example::

        sage: E = EllipticCurve(GF(19), [1,2,3,4,5])
        sage: R.<x> = GF(19)[]
        sage: phi = EllipticCurveIsogeny(E, x^3 + 7*x^2 + 15*x + 12); phi
        Isogeny of degree 4
         from Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5
              over Finite Field of size 19
           to Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 3*x + 15
              over Finite Field of size 19
        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import compute_vw_kohel_even_deg3
        sage: b2,b4 = E.b2(), E.b4()
        sage: s1, s2, s3 = -7, 15, -12
        sage: compute_vw_kohel_even_deg3(b2, b4, s1, s2, s3)
        (4, 7)
    """
def compute_vw_kohel_odd(b2, b4, b6, s1, s2, s3, n):
    """
    Compute Vélu's `(v,w)` using Kohel's formulas for isogenies of odd
    degree.

    INPUT:

    - ``b2``, ``b4``, ``b6`` -- invariants of an elliptic curve `E`

    - ``s1``, ``s2``, ``s3`` -- signed coefficients of lowest powers
      of `x` in the kernel polynomial

    - ``n`` -- integer; the degree

    OUTPUT: Vélu's isogeny parameters `(v,w)`

    EXAMPLES:

    This function will be implicitly called by the following example::

        sage: E = EllipticCurve(GF(19), [18,17,16,15,14])
        sage: R.<x> = GF(19)[]
        sage: phi = EllipticCurveIsogeny(E, x^3 + 14*x^2 + 3*x + 11); phi
        Isogeny of degree 7
         from Elliptic Curve defined by y^2 + 18*x*y + 16*y = x^3 + 17*x^2 + 15*x + 14
              over Finite Field of size 19
           to Elliptic Curve defined by y^2 + 18*x*y + 16*y = x^3 + 17*x^2 + 18*x + 18
              over Finite Field of size 19
        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import compute_vw_kohel_odd
        sage: b2,b4,b6 = E.b2(), E.b4(), E.b6()
        sage: s1,s2,s3 = -14,3,-11
        sage: compute_vw_kohel_odd(b2,b4,b6,s1,s2,s3,3)
        (7, 1)
    """
def compute_codomain_kohel(E, kernel):
    """
    Compute the codomain from the kernel polynomial using Kohel's
    formulas.

    INPUT:

    - ``E`` -- domain elliptic curve

    - ``kernel`` -- polynomial or list; the kernel polynomial, or a
      list of its coefficients

    OUTPUT: elliptic curve; the codomain elliptic curve of the isogeny
    defined by ``kernel``

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import compute_codomain_kohel
        sage: E = EllipticCurve(GF(19), [1,2,3,4,5])
        sage: phi = EllipticCurveIsogeny(E, [9,1])
        sage: phi.codomain() == isogeny_codomain_from_kernel(E, [9,1])
        True
        sage: compute_codomain_kohel(E, [9,1])
        Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 9*x + 8
         over Finite Field of size 19
        sage: R.<x> = GF(19)[]
        sage: E = EllipticCurve(GF(19), [18,17,16,15,14])
        sage: phi = EllipticCurveIsogeny(E, x^3 + 14*x^2 + 3*x + 11)
        sage: phi.codomain() == isogeny_codomain_from_kernel(E, x^3 + 14*x^2 + 3*x + 11)
        True
        sage: compute_codomain_kohel(E, x^3 + 14*x^2 + 3*x + 11)
        Elliptic Curve defined by y^2 + 18*x*y + 16*y = x^3 + 17*x^2 + 18*x + 18
         over Finite Field of size 19
        sage: E = EllipticCurve(GF(19), [1,2,3,4,5])
        sage: phi = EllipticCurveIsogeny(E, x^3 + 7*x^2 + 15*x + 12)
        sage: isogeny_codomain_from_kernel(E, x^3 + 7*x^2 + 15*x + 12) == phi.codomain()
        True
        sage: compute_codomain_kohel(E, x^3 + 7*x^2 + 15*x + 12)
        Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 3*x + 15
         over Finite Field of size 19

    ALGORITHM:

    This function uses the formulas of Section 2.4 of [Koh1996]_.
    """
def two_torsion_part(E, psi):
    """
    Return the greatest common divisor of ``psi`` and the 2-torsion
    polynomial of `E`.

    INPUT:

    - ``E`` -- an elliptic curve

    - ``psi`` -- a univariate polynomial over the base field of ``E``

    OUTPUT: polynomial; the `\\gcd` of ``psi`` and the 2-torsion polynomial of ``E``

    EXAMPLES:

    Every function that computes the kernel polynomial via Kohel's
    formulas will call this function::

        sage: E = EllipticCurve(GF(19), [1,2,3,4,5])
        sage: R.<x> = GF(19)[]
        sage: phi = EllipticCurveIsogeny(E, x + 13)
        sage: isogeny_codomain_from_kernel(E, x + 13) == phi.codomain()
        True
        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import two_torsion_part
        sage: two_torsion_part(E, x + 13)
        x + 13
    """

class EllipticCurveIsogeny(EllipticCurveHom):
    """
    This class implements separable isogenies of elliptic curves.

    Several different algorithms for computing isogenies are
    available.  These include:

    - Vélu's Formulas: Vélu's original formulas for computing
      isogenies.  This algorithm is selected by giving as the
      ``kernel`` parameter a single point, or a list of points,
      generating a finite subgroup.

    - Kohel's Formulas: Kohel's original formulas for computing
      isogenies.  This algorithm is selected by giving as the
      ``kernel`` parameter a monic polynomial (or a coefficient list)
      which will define the kernel of the isogeny.
      Kohel's algorithm is currently only implemented for cyclic
      isogenies, with the exception of `[2]`.

    INPUT:

    - ``E`` -- an elliptic curve; the domain of the isogeny to initialize

    - ``kernel`` -- a kernel; either a point on ``E``, a list of
      points on ``E``, a monic kernel polynomial, or ``None``.
      If initializing from a domain/codomain, this must be ``None``.

    - ``codomain`` -- an elliptic curve (default: ``None``)

      - If ``kernel`` is ``None``, then ``degree`` must be given as well
        and the given ``codomain`` must be the codomain of a cyclic,
        separable, normalized isogeny of the given degree.

      - If ``kernel`` is not ``None``, then this must be isomorphic to
        the codomain of the separable isogeny defined by ``kernel``; in
        this case, the isogeny is post-composed with an isomorphism so
        that the codomain equals the given curve.

    - ``degree`` -- integer (default: ``None``)

      - If ``kernel`` is ``None``, then this is the degree of the isogeny
        from ``E`` to ``codomain``.

      - If ``kernel`` is not ``None``, then this is used to determine
        whether or not to skip a `\\gcd` of the given kernel polynomial
        with the two-torsion polynomial of ``E``.

    - ``model`` -- string (default: ``None``); supported values
      (cf. :func:`~sage.schemes.elliptic_curves.ell_field.compute_model`):

      - ``'minimal'`` -- if ``E`` is a curve over the rationals or
        over a number field, then the codomain is a global minimal
        model where this exists.

      - ``'short_weierstrass'`` -- the codomain is a short Weierstrass curve,
        assuming one exists.

      - ``'montgomery'`` -- the codomain is an (untwisted) Montgomery
        curve, assuming one exists over this field.

    - ``check`` -- boolean (default: ``True``); check whether the input is valid.
      Setting this to ``False`` can lead to significant speedups.

    EXAMPLES:

    A simple example of creating an isogeny of a field of small
    characteristic::

        sage: E = EllipticCurve(GF(7), [0,0,0,1,0])
        sage: phi = EllipticCurveIsogeny(E, E((0,0)) ); phi
        Isogeny of degree 2
         from Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 7
           to Elliptic Curve defined by y^2 = x^3 + 3*x over Finite Field of size 7
        sage: phi.degree() == 2
        True
        sage: phi.kernel_polynomial()
        x
        sage: phi.rational_maps()
        ((x^2 + 1)/x, (x^2*y - y)/x^2)
        sage: phi == loads(dumps(phi))          # known bug
        True

    A more complicated example of a characteristic-2 field::

        sage: # needs sage.rings.finite_rings
        sage: E = EllipticCurve(GF(2^4,'alpha'), [0,0,1,0,1])
        sage: P = E((1,1))
        sage: phi_v = EllipticCurveIsogeny(E, P); phi_v
        Isogeny of degree 3
         from Elliptic Curve defined by y^2 + y = x^3 + 1
              over Finite Field in alpha of size 2^4
           to Elliptic Curve defined by y^2 + y = x^3
              over Finite Field in alpha of size 2^4
        sage: phi_ker_poly = phi_v.kernel_polynomial()
        sage: phi_ker_poly
        x + 1
        sage: phi_k = EllipticCurveIsogeny(E, phi_ker_poly)
        sage: phi_k == phi_v
        True
        sage: phi_k.rational_maps()
        ((x^3 + x + 1)/(x^2 + 1), (x^3*y + x^2*y + x*y + x + y)/(x^3 + x^2 + x + 1))
        sage: phi_v.rational_maps()
        ((x^3 + x + 1)/(x^2 + 1), (x^3*y + x^2*y + x*y + x + y)/(x^3 + x^2 + x + 1))
        sage: phi_k.degree() == phi_v.degree() == 3
        True
        sage: phi_k.is_separable()
        True
        sage: phi_v(E(0))
        (0 : 1 : 0)
        sage: alpha = E.base_field().gen()
        sage: Q = E((0, alpha*(alpha + 1)))
        sage: phi_v(Q)
        (1 : alpha^2 + alpha : 1)
        sage: phi_v(P) == phi_k(P)
        True
        sage: phi_k(P) == phi_v.codomain()(0)
        True

    We can create an isogeny whose kernel equals the full 2-torsion::

        sage: # needs sage.rings.finite_rings
        sage: E = EllipticCurve(GF((3,2)), [0,0,0,1,1])
        sage: ker_poly = E.division_polynomial(2)
        sage: phi = EllipticCurveIsogeny(E, ker_poly); phi
        Isogeny of degree 4
         from Elliptic Curve defined by y^2 = x^3 + x + 1
              over Finite Field in z2 of size 3^2
           to Elliptic Curve defined by y^2 = x^3 + x + 1
              over Finite Field in z2 of size 3^2
        sage: P1,P2,P3 = filter(bool, E(0).division_points(2))
        sage: phi(P1)
        (0 : 1 : 0)
        sage: phi(P2)
        (0 : 1 : 0)
        sage: phi(P3)
        (0 : 1 : 0)
        sage: phi.degree()
        4

    We can also create trivial isogenies with the trivial kernel::

        sage: E = EllipticCurve(GF(17), [11, 11, 4, 12, 10])
        sage: phi_v = EllipticCurveIsogeny(E, E(0))
        sage: phi_v.degree()
        1
        sage: phi_v.rational_maps()
        (x, y)
        sage: E == phi_v.codomain()
        True
        sage: P = E.random_point()
        sage: phi_v(P) == P
        True

        sage: E = EllipticCurve(GF(31), [23, 1, 22, 7, 18])
        sage: phi_k = EllipticCurveIsogeny(E, [1]); phi_k
        Isogeny of degree 1
         from Elliptic Curve defined by y^2 + 23*x*y + 22*y = x^3 + x^2 + 7*x + 18
              over Finite Field of size 31
           to Elliptic Curve defined by y^2 + 23*x*y + 22*y = x^3 + x^2 + 7*x + 18
              over Finite Field of size 31
        sage: phi_k.degree()
        1
        sage: phi_k.rational_maps()
        (x, y)
        sage: phi_k.codomain() == E
        True
        sage: phi_k.kernel_polynomial()
        1
        sage: P = E.random_point(); P == phi_k(P)
        True

    Vélu and Kohel also work in characteristic `0`::

        sage: E = EllipticCurve(QQ, [0,0,0,3,4])
        sage: P_list = E.torsion_points()
        sage: phi = EllipticCurveIsogeny(E, P_list); phi
        Isogeny of degree 2
         from Elliptic Curve defined by y^2 = x^3 + 3*x + 4 over Rational Field
           to Elliptic Curve defined by y^2 = x^3 - 27*x + 46 over Rational Field
        sage: P = E((0,2))
        sage: phi(P)
        (6 : -10 : 1)
        sage: phi_ker_poly = phi.kernel_polynomial()
        sage: phi_ker_poly
        x + 1
        sage: phi_k = EllipticCurveIsogeny(E, phi_ker_poly); phi_k
        Isogeny of degree 2
         from Elliptic Curve defined by y^2 = x^3 + 3*x + 4 over Rational Field
           to Elliptic Curve defined by y^2 = x^3 - 27*x + 46 over Rational Field
        sage: phi_k(P) == phi(P)
        True
        sage: phi_k == phi
        True
        sage: phi_k.degree()
        2
        sage: phi_k.is_separable()
        True

    A more complicated example over the rationals (of odd degree)::

        sage: E = EllipticCurve('11a1')
        sage: P_list = E.torsion_points()
        sage: phi_v = EllipticCurveIsogeny(E, P_list); phi_v
        Isogeny of degree 5
         from Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
           to Elliptic Curve defined by y^2 + y = x^3 - x^2 - 7820*x - 263580 over Rational Field
        sage: P = E((16,-61))
        sage: phi_v(P)
        (0 : 1 : 0)
        sage: ker_poly = phi_v.kernel_polynomial(); ker_poly
        x^2 - 21*x + 80
        sage: phi_k = EllipticCurveIsogeny(E, ker_poly); phi_k
        Isogeny of degree 5
         from Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
           to Elliptic Curve defined by y^2 + y = x^3 - x^2 - 7820*x - 263580 over Rational Field
        sage: phi_k == phi_v
        True
        sage: phi_v(P) == phi_k(P)
        True
        sage: phi_k.is_separable()
        True

    We can also do this same example over the number field defined by
    the irreducible two-torsion polynomial of `E`::

        sage: # needs sage.rings.number_field
        sage: E = EllipticCurve('11a1')
        sage: P_list = E.torsion_points()
        sage: x = polygen(ZZ, 'x')
        sage: K.<alpha> = NumberField(x^3 - 2* x^2 - 40*x - 158)
        sage: EK = E.change_ring(K)
        sage: P_list = [EK(P) for P in P_list]
        sage: phi_v = EllipticCurveIsogeny(EK, P_list); phi_v
        Isogeny of degree 5
         from Elliptic Curve defined by y^2 + y = x^3 + (-1)*x^2 + (-10)*x + (-20)
              over Number Field in alpha with defining polynomial x^3 - 2*x^2 - 40*x - 158
           to Elliptic Curve defined by y^2 + y = x^3 + (-1)*x^2 + (-7820)*x + (-263580)
              over Number Field in alpha with defining polynomial x^3 - 2*x^2 - 40*x - 158
        sage: P = EK((alpha/2,-1/2))
        sage: phi_v(P)
        (122/121*alpha^2 + 1633/242*alpha - 3920/121 : -1/2 : 1)
        sage: ker_poly = phi_v.kernel_polynomial()
        sage: ker_poly
        x^2 - 21*x + 80
        sage: phi_k = EllipticCurveIsogeny(EK, ker_poly); phi_k
        Isogeny of degree 5
         from Elliptic Curve defined by y^2 + y = x^3 + (-1)*x^2 + (-10)*x + (-20)
              over Number Field in alpha with defining polynomial x^3 - 2*x^2 - 40*x - 158
           to Elliptic Curve defined by y^2 + y = x^3 + (-1)*x^2 + (-7820)*x + (-263580)
              over Number Field in alpha with defining polynomial x^3 - 2*x^2 - 40*x - 158
        sage: phi_v == phi_k
        True
        sage: phi_k(P) == phi_v(P)
        True
        sage: phi_k == phi_v
        True
        sage: phi_k.degree()
        5
        sage: phi_v.is_separable()
        True

    The following example shows how to specify an isogeny from domain
    and codomain::

        sage: E = EllipticCurve('11a1')
        sage: R.<x> = QQ[]
        sage: f = x^2 - 21*x + 80
        sage: phi = E.isogeny(f)
        sage: E2 = phi.codomain()
        sage: phi_s = EllipticCurveIsogeny(E, None, E2, 5); phi_s
        Isogeny of degree 5
         from Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
           to Elliptic Curve defined by y^2 + y = x^3 - x^2 - 7820*x - 263580 over Rational Field
        sage: phi_s == phi
        True
        sage: phi_s.rational_maps() == phi.rational_maps()
        True

    However, only cyclic normalized isogenies can be constructed this way.
    The non-cyclic multiplication-by-`3` isogeny won't be found::

        sage: E.isogeny(None, codomain=E, degree=9)
        Traceback (most recent call last):
        ...
        ValueError: the two curves are not linked by a cyclic normalized isogeny of degree 9

    Non-normalized isogeny also won't be found::

        sage: E2.isogeny(None, codomain=E, degree=5)
        Traceback (most recent call last):
        ...
        ValueError: the two curves are not linked by a cyclic normalized isogeny of degree 5
        sage: phihat = phi.dual(); phihat
        Isogeny of degree 5
         from Elliptic Curve defined by y^2 + y = x^3 - x^2 - 7820*x - 263580
              over Rational Field
           to Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
        sage: phihat.is_normalized()
        False

    Here an example of a construction of a endomorphisms with cyclic
    kernel on a CM-curve::

        sage: # needs sage.rings.number_field
        sage: K.<i> = NumberField(x^2 + 1)
        sage: E = EllipticCurve(K, [1,0])
        sage: RK.<X> = K[]
        sage: f = X^2 - 2/5*i + 1/5
        sage: phi= E.isogeny(f)
        sage: isom = phi.codomain().isomorphism_to(E)
        sage: phi = isom * phi
        sage: phi.codomain() == phi.domain()
        True
        sage: phi.rational_maps()
        (((4/25*i + 3/25)*x^5 + (4/5*i - 2/5)*x^3 - x)/(x^4 + (-4/5*i + 2/5)*x^2 + (-4/25*i - 3/25)),
         ((11/125*i + 2/125)*x^6*y + (-23/125*i + 64/125)*x^4*y + (141/125*i + 162/125)*x^2*y + (3/25*i - 4/25)*y)/(x^6 + (-6/5*i + 3/5)*x^4 + (-12/25*i - 9/25)*x^2 + (2/125*i - 11/125)))

    TESTS:

    Domain and codomain tests (see :issue:`12880`)::

        sage: E = EllipticCurve(QQ, [0,0,0,1,0])
        sage: phi = EllipticCurveIsogeny(E, E(0,0))
        sage: phi.domain() == E
        True
        sage: phi.codomain()
        Elliptic Curve defined by y^2 = x^3 - 4*x over Rational Field

        sage: E = EllipticCurve(GF(31), [1,0,0,1,2])
        sage: phi = EllipticCurveIsogeny(E, [17, 1])
        sage: phi.domain()
        Elliptic Curve defined by y^2 + x*y = x^3 + x + 2 over Finite Field of size 31
        sage: phi.codomain()
        Elliptic Curve defined by y^2 + x*y = x^3 + 24*x + 6 over Finite Field of size 31

    Composition tests (see :issue:`16245`, cf. :issue:`34410`)::

        sage: E = EllipticCurve(j=GF(7)(0))
        sage: phi = E.isogeny([E(0), E((0,1)), E((0,-1))]); phi
        Composite morphism of degree 3:
          From: Elliptic Curve defined by y^2 = x^3 + 1 over Finite Field of size 7
          To:   Elliptic Curve defined by y^2 = x^3 + 1 over Finite Field of size 7
        sage: phi2 = phi * phi; phi2
        Composite morphism of degree 9 = 3^2:
          From: Elliptic Curve defined by y^2 = x^3 + 1 over Finite Field of size 7
          To:   Elliptic Curve defined by y^2 = x^3 + 1 over Finite Field of size 7

    Examples over relative number fields used not to work (see :issue:`16779`)::

        sage: # long time, needs sage.rings.number_field
        sage: pol26 = hilbert_class_polynomial(-4*26)
        sage: F = NumberField(pol26,'a')
        sage: pol = F.optimized_representation()[0].polynomial()
        sage: K.<a> = NumberField(pol)
        sage: j = pol26.roots(K)[0][0]
        sage: E = EllipticCurve(j=j)
        sage: L.<b> = K.extension(x^2 + 26)
        sage: EL = E.change_ring(L)
        sage: iso2 = EL.isogenies_prime_degree(2); len(iso2)
        1
        sage: iso3 = EL.isogenies_prime_degree(3); len(iso3)
        2

    Examples over function fields used not to work (see :issue:`11327`)::

        sage: F.<t> = FunctionField(QQ)
        sage: E = EllipticCurve([0,0,0,-t^2,0])
        sage: isogs = E.isogenies_prime_degree(2)
        sage: isogs[0]
        Isogeny of degree 2
         from Elliptic Curve defined by y^2 = x^3 + (-t^2)*x
              over Rational function field in t over Rational Field
           to Elliptic Curve defined by y^2 = x^3 + 4*t^2*x
              over Rational function field in t over Rational Field
        sage: isogs[0].rational_maps()
        ((x^2 - t^2)/x, (x^2*y + t^2*y)/x^2)
        sage: duals = [phi.dual() for phi in isogs]
        sage: duals[0]
        Isogeny of degree 2
         from Elliptic Curve defined by y^2 = x^3 + 4*t^2*x
              over Rational function field in t over Rational Field
           to Elliptic Curve defined by y^2 = x^3 + (-t^2)*x
              over Rational function field in t over Rational Field
        sage: duals[0].rational_maps()
        ((1/4*x^2 + t^2)/x, (1/8*x^2*y + (-1/2*t^2)*y)/x^2)
        sage: duals[0]
        Isogeny of degree 2
         from Elliptic Curve defined by y^2 = x^3 + 4*t^2*x
              over Rational function field in t over Rational Field
           to Elliptic Curve defined by y^2 = x^3 + (-t^2)*x
              over Rational function field in t over Rational Field
    """
    def __init__(self, E, kernel, codomain=None, degree=None, model=None, check: bool = True) -> None:
        """
        Constructor for ``EllipticCurveIsogeny`` class.

        EXAMPLES::

            sage: E = EllipticCurve(GF(2), [0,0,1,0,1])
            sage: phi = EllipticCurveIsogeny(E, [1,1]); phi
            Isogeny of degree 3
             from Elliptic Curve defined by y^2 + y = x^3 + 1 over Finite Field of size 2
               to Elliptic Curve defined by y^2 + y = x^3 over Finite Field of size 2

            sage: E = EllipticCurve(GF(31), [0,0,0,1,0])
            sage: P = E((2,17))
            sage: phi = EllipticCurveIsogeny(E, P); phi
            Isogeny of degree 8
             from Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 31
               to Elliptic Curve defined by y^2 = x^3 + 10*x + 28 over Finite Field of size 31

            sage: E = EllipticCurve('17a1')
            sage: phi = EllipticCurveIsogeny(E, [41/3, -55, -1, -1, 1]); phi
            Isogeny of degree 9
             from Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - x - 14
                  over Rational Field
               to Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - 56*x - 10124
                  over Rational Field

            sage: E = EllipticCurve('37a1')
            sage: triv = EllipticCurveIsogeny(E, E(0)); triv
            Isogeny of degree 1
             from Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
               to Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
            sage: triv.rational_maps()
            (x, y)

            sage: E = EllipticCurve('49a3')
            sage: R.<X> = QQ[]
            sage: EllipticCurveIsogeny(E, X^3 - 13*X^2 - 58*X + 503, check=False)
            Isogeny of degree 7
             from Elliptic Curve defined by y^2 + x*y = x^3 - x^2 - 107*x + 552
                  over Rational Field
               to Elliptic Curve defined by y^2 + x*y = x^3 - x^2 - 5252*x - 178837
                  over Rational Field
        """
    def __getitem__(self, i):
        """
        Return one of the rational-map components.

        .. NOTE::

            Both components are returned as elements of the function
            field `F(x,y)` in two variables over the base field `F`,
            though the first only involves `x`.  To obtain the
            `x`-coordinate function as a rational function in `F(x)`,
            use :meth:`x_rational_map`.

        EXAMPLES::

            sage: E = EllipticCurve(QQ, [0,2,0,1,-1])
            sage: phi = EllipticCurveIsogeny(E, [1])
            sage: phi[0]
            x
            sage: phi[1]
            y

            sage: E = EllipticCurve(GF(17), [0,0,0,3,0])
            sage: phi = EllipticCurveIsogeny(E, E((0,0)))
            sage: phi[0]
            (x^2 + 3)/x
            sage: phi[1]
            (x^2*y - 3*y)/x^2
        """
    def __iter__(self):
        """
        Return an iterator through the rational-map components.

        EXAMPLES::

            sage: E = EllipticCurve(QQ, [0,2,0,1,-1])
            sage: phi = EllipticCurveIsogeny(E, [1])
            sage: for c in phi: print(c)
            x
            y

            sage: E = EllipticCurve(GF(17), [0,0,0,3,0])
            sage: phi = EllipticCurveIsogeny(E, E((0,0)))
            sage: for c in phi: print(c)
            (x^2 + 3)/x
            (x^2*y - 3*y)/x^2
        """
    def __neg__(self):
        """
        Return a copy of the isogeny that has been negated.

        This implements the unary `-` operator.

        EXAMPLES:

        The following examples inherently exercise this function::

            sage: E = EllipticCurve(j=GF(17)(0))
            sage: phi = EllipticCurveIsogeny(E, E((-1,0)) )
            sage: negphi = -phi
            sage: phi(E((0,1))) + negphi(E((0,1))) == 0
            True

            sage: E = EllipticCurve(j=GF(19)(1728))
            sage: R.<x> = GF(19)[]
            sage: phi = EllipticCurveIsogeny(E, x)
            sage: negphi = -phi
            sage: phi(E((3,7))) + negphi(E((3,12))) == phi(2*E((3,7)))
            True
            sage: negphi(E((18,6)))
            (17 : 0 : 1)

            sage: R.<x> = QQ[]
            sage: E = EllipticCurve('17a1')
            sage: R.<x> = QQ[]
            sage: f = x - 11/4
            sage: phi = EllipticCurveIsogeny(E, f)
            sage: negphi = -phi
            sage: phi.rational_maps()[0] == negphi.rational_maps()[0]
            True
            sage: P = E((7,13))
            sage: phi(P) + negphi(P) == 0
            True

            sage: E = EllipticCurve(GF(23), [0,0,0,1,0])
            sage: f = E.torsion_polynomial(3)/3
            sage: phi = EllipticCurveIsogeny(E, f, E)
            sage: phi.rational_maps() == E.multiplication_by_m(3)
            False
            sage: negphi = -phi
            sage: negphi.rational_maps() == E.multiplication_by_m(3)
            True

            sage: E = EllipticCurve(GF(17), [-2, 3, -5, 7, -11])
            sage: R.<x> = GF(17)[]
            sage: f = x+6
            sage: phi = EllipticCurveIsogeny(E, f); phi
            Isogeny of degree 2
             from Elliptic Curve defined by y^2 + 15*x*y + 12*y = x^3 + 3*x^2 + 7*x + 6 over Finite Field of size 17
               to Elliptic Curve defined by y^2 + 15*x*y + 12*y = x^3 + 3*x^2 + 4*x + 8 over Finite Field of size 17
            sage: phi.rational_maps()
            ((x^2 + 6*x + 4)/(x + 6), (x^2*y - 5*x*y + 8*x - 2*y)/(x^2 - 5*x + 2))
            sage: negphi = -phi
            sage: negphi
            Isogeny of degree 2
             from Elliptic Curve defined by y^2 + 15*x*y + 12*y = x^3 + 3*x^2 + 7*x + 6 over Finite Field of size 17
               to Elliptic Curve defined by y^2 + 15*x*y + 12*y = x^3 + 3*x^2 + 4*x + 8 over Finite Field of size 17
            sage: negphi.rational_maps()
            ((x^2 + 6*x + 4)/(x + 6),
             (2*x^3 - x^2*y - 5*x^2 + 5*x*y - 4*x + 2*y + 7)/(x^2 - 5*x + 2))

            sage: E = EllipticCurve('11a1')
            sage: R.<x> = QQ[]
            sage: f = x^2 - 21*x + 80
            sage: phi = EllipticCurveIsogeny(E, f)
            sage: (xmap1, ymap1) = phi.rational_maps()
            sage: negphi = -phi
            sage: (xmap2, ymap2) = negphi.rational_maps()
            sage: xmap1 == xmap2
            True
            sage: ymap1 == -ymap2 - E.a1()*xmap2 - E.a3()
            True

            sage: # needs sage.rings.number_field
            sage: K.<a> = NumberField(x^2 + 1)
            sage: E = EllipticCurve(K, [0,0,0,1,0])
            sage: R.<x> = K[]
            sage: phi = EllipticCurveIsogeny(E, x - a)
            sage: phi.rational_maps()
            ((x^2 + (-a)*x - 2)/(x + (-a)), (x^2*y + (-2*a)*x*y + y)/(x^2 + (-2*a)*x - 1))
            sage: negphi = -phi
            sage: negphi.rational_maps()
            ((x^2 + (-a)*x - 2)/(x + (-a)), (-x^2*y + (2*a)*x*y - y)/(x^2 + (-2*a)*x - 1))
        """
    def rational_maps(self):
        """
        Return the pair of rational maps defining this isogeny.

        .. NOTE::

            Both components are returned as elements of the function
            field `F(x,y)` in two variables over the base field `F`,
            though the first only involves `x`.  To obtain the
            `x`-coordinate function as a rational function in `F(x)`,
            use :meth:`x_rational_map`.

        EXAMPLES::

            sage: E = EllipticCurve(QQ, [0,2,0,1,-1])
            sage: phi = EllipticCurveIsogeny(E, [1])
            sage: phi.rational_maps()
            (x, y)

            sage: E = EllipticCurve(GF(17), [0,0,0,3,0])
            sage: phi = EllipticCurveIsogeny(E, E((0,0)))
            sage: phi.rational_maps()
            ((x^2 + 3)/x, (x^2*y - 3*y)/x^2)
        """
    def x_rational_map(self):
        """
        Return the rational map giving the `x`-coordinate of this isogeny.

        .. NOTE::

            This function returns the `x`-coordinate component of the
            isogeny as a rational function in `F(x)`, where `F` is the
            base field.  To obtain both coordinate functions as
            elements of the function field `F(x,y)` in two variables,
            use :meth:`rational_maps`.

        EXAMPLES::

            sage: E = EllipticCurve(QQ, [0,2,0,1,-1])
            sage: phi = EllipticCurveIsogeny(E, [1])
            sage: phi.x_rational_map()
            x

            sage: E = EllipticCurve(GF(17), [0,0,0,3,0])
            sage: phi = EllipticCurveIsogeny(E, E((0,0)))
            sage: phi.x_rational_map()
            (x^2 + 3)/x
        """
    def scaling_factor(self):
        '''
        Return the Weierstrass scaling factor associated to this
        elliptic-curve isogeny.

        The scaling factor is the constant `u` (in the base field)
        such that `\\varphi^* \\omega_2 = u \\omega_1`, where
        `\\varphi: E_1\\to E_2` is this isogeny and `\\omega_i` are
        the standard Weierstrass differentials on `E_i` defined by
        `\\mathrm dx/(2y+a_1x+a_3)`.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: E = EllipticCurve(GF(257^2), [0,1])
            sage: phi = E.isogeny(E.lift_x(240))
            sage: phi.degree()
            43
            sage: phi.scaling_factor()
            1
            sage: phi.dual().scaling_factor()
            43

        TESTS:

        Check for :issue:`36638`::

            sage: phi.scaling_factor().parent()                                         # needs sage.rings.finite_rings
            Finite Field in z2 of size 257^2

        ALGORITHM: The "inner" isogeny is normalized by construction,
        so we only need to account for the scaling factors of a pre-
        and post-isomorphism.
        '''
    def kernel_polynomial(self):
        """
        Return the kernel polynomial of this isogeny.

        EXAMPLES::

            sage: E = EllipticCurve(QQ, [0,0,0,2,0])
            sage: phi = EllipticCurveIsogeny(E, E((0,0)))
            sage: phi.kernel_polynomial()
            x

            sage: E = EllipticCurve('11a1')
            sage: phi = EllipticCurveIsogeny(E, E.torsion_points())
            sage: phi.kernel_polynomial()
            x^2 - 21*x + 80

            sage: E = EllipticCurve(GF(17), [1,-1,1,-1,1])
            sage: phi = EllipticCurveIsogeny(E, [1])
            sage: phi.kernel_polynomial()
            1

            sage: E = EllipticCurve(GF(31), [0,0,0,3,0])
            sage: phi = EllipticCurveIsogeny(E, [0,3,0,1])
            sage: phi.kernel_polynomial()
            x^3 + 3*x
        """
    def inseparable_degree(self):
        """
        Return the inseparable degree of this isogeny.

        Since this class only implements separable isogenies,
        this method always returns one.

        TESTS::

            sage: EllipticCurveIsogeny.inseparable_degree(None)
            1
        """
    def dual(self):
        """
        Return the isogeny dual to this isogeny.

        .. NOTE::

            If `\\varphi\\colon E \\to E'` is the given isogeny and `n`
            is its degree, then the dual is by definition the unique
            isogeny `\\hat\\varphi\\colon E'\\to E` such that the
            compositions `\\hat\\varphi\\circ\\varphi` and
            `\\varphi\\circ\\hat\\varphi` are the multiplication-by-`n`
            maps on `E` and `E'`, respectively.

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: R.<x> = QQ[]
            sage: f = x^2 - 21*x + 80
            sage: phi = EllipticCurveIsogeny(E, f)
            sage: phi_hat = phi.dual()
            sage: phi_hat.domain() == phi.codomain()
            True
            sage: phi_hat.codomain() == phi.domain()
            True
            sage: (X, Y) = phi.rational_maps()
            sage: (Xhat, Yhat) = phi_hat.rational_maps()
            sage: Xm = Xhat.subs(x=X, y=Y)
            sage: Ym = Yhat.subs(x=X, y=Y)
            sage: (Xm, Ym) == E.multiplication_by_m(5)
            True

            sage: E = EllipticCurve(GF(37), [0,0,0,1,8])
            sage: R.<x> = GF(37)[]
            sage: f = x^3 + x^2 + 28*x + 33
            sage: phi = EllipticCurveIsogeny(E, f)
            sage: phi_hat = phi.dual()
            sage: phi_hat.codomain() == phi.domain()
            True
            sage: phi_hat.domain() == phi.codomain()
            True
            sage: (X, Y) = phi.rational_maps()
            sage: (Xhat, Yhat) = phi_hat.rational_maps()
            sage: Xm = Xhat.subs(x=X, y=Y)
            sage: Ym = Yhat.subs(x=X, y=Y)
            sage: (Xm, Ym) == E.multiplication_by_m(7)
            True

            sage: E = EllipticCurve(GF(31), [0,0,0,1,8])
            sage: R.<x> = GF(31)[]
            sage: f = x^2 + 17*x + 29
            sage: phi = EllipticCurveIsogeny(E, f)
            sage: phi_hat = phi.dual()
            sage: phi_hat.codomain() == phi.domain()
            True
            sage: phi_hat.domain() == phi.codomain()
            True
            sage: (X, Y) = phi.rational_maps()
            sage: (Xhat, Yhat) = phi_hat.rational_maps()
            sage: Xm = Xhat.subs(x=X, y=Y)
            sage: Ym = Yhat.subs(x=X, y=Y)
            sage: (Xm, Ym) == E.multiplication_by_m(5)
            True

        Inseparable duals should be computed correctly::

            sage: # needs sage.rings.finite_rings
            sage: z2 = GF(71^2).gen()
            sage: E = EllipticCurve(j=57*z2+51)
            sage: E.isogeny(3*E.lift_x(0)).dual()
            Composite morphism of degree 71 = 71*1^2:
              From: Elliptic Curve defined by y^2 = x^3 + (32*z2+67)*x + (24*z2+37)
                    over Finite Field in z2 of size 71^2
              To:   Elliptic Curve defined by y^2 = x^3 + (41*z2+56)*x + (18*z2+42)
                    over Finite Field in z2 of size 71^2
            sage: E.isogeny(E.lift_x(0)).dual()
            Composite morphism of degree 213 = 71*3:
              From: Elliptic Curve defined by y^2 = x^3 + (58*z2+31)*x + (34*z2+58)
                    over Finite Field in z2 of size 71^2
              To:   Elliptic Curve defined by y^2 = x^3 + (41*z2+56)*x + (18*z2+42)
                    over Finite Field in z2 of size 71^2

        ...even if pre- or post-isomorphisms are present::

            sage: # needs sage.rings.finite_rings
            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
            sage: phi = E.isogeny(E.lift_x(0))
            sage: pre = ~WeierstrassIsomorphism(phi.domain(), (z2,2,3,4))
            sage: post = WeierstrassIsomorphism(phi.codomain(), (5,6,7,8))
            sage: phi = post * phi * pre
            sage: phi.dual()
            Composite morphism of degree 213 = 71*3:
              From: Elliptic Curve defined
                    by y^2 + 17*x*y + 45*y = x^3 + 30*x^2 + (6*z2+64)*x + (48*z2+65)
                    over Finite Field in z2 of size 71^2
              To:   Elliptic Curve defined
                    by y^2 + (60*z2+22)*x*y + (69*z2+37)*y = x^3 + (32*z2+48)*x^2
                       + (19*z2+58)*x + (56*z2+22)
                    over Finite Field in z2 of size 71^2

        TESTS:

        Test for :issue:`23928`::

            sage: E = EllipticCurve(j=GF(431**2)(4))                                    # needs sage.rings.finite_rings
            sage: phi = E.isogeny(E.lift_x(0))                                          # needs sage.rings.finite_rings
            sage: phi.dual()                                                            # needs sage.rings.finite_rings
            Isogeny of degree 2
             from Elliptic Curve defined by y^2 = x^3 + 427*x over Finite Field in z2 of size 431^2
               to Elliptic Curve defined by y^2 = x^3 + x over Finite Field in z2 of size 431^2

        Test (for :issue:`7096`)::

            sage: E = EllipticCurve('11a1')
            sage: phi = E.isogeny(E(5,5))
            sage: phi.dual().dual() == phi
            True

            sage: k = GF(103)
            sage: E = EllipticCurve(k,[11,11])
            sage: phi = E.isogeny(E(4,4))
            sage: phi
            Isogeny of degree 5
             from Elliptic Curve defined by y^2 = x^3 + 11*x + 11 over Finite Field of size 103
               to Elliptic Curve defined by y^2 = x^3 + 25*x + 80 over Finite Field of size 103
            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
            sage: phi = WeierstrassIsomorphism(phi.codomain(),(5,0,1,2)) * phi
            sage: phi.dual().dual() == phi
            True

            sage: E = EllipticCurve(GF(103),[1,0,0,1,-1])
            sage: phi = E.isogeny(E(60,85))
            sage: phi.dual()
            Isogeny of degree 7
             from Elliptic Curve defined by y^2 + x*y = x^3 + 84*x + 34 over Finite Field of size 103
               to Elliptic Curve defined by y^2 + x*y = x^3 + x + 102 over Finite Field of size 103

        Check that :issue:`17293` is fixed::

            sage: # needs sage.rings.number_field
            sage: k.<s> = QuadraticField(2)
            sage: E = EllipticCurve(k, [-3*s*(4 + 5*s), 2*s*(2 + 14*s + 11*s^2)])
            sage: phi = E.isogenies_prime_degree(3)[0]
            sage: (-phi).dual() == -phi.dual()
            True
            sage: phi._EllipticCurveIsogeny__clear_cached_values()  # forget the dual
            sage: -phi.dual() == (-phi).dual()
            True

        Check that :issue:`37168` is fixed::

            sage: R.<x> = GF(23)[]
            sage: F.<a> = FiniteField(23^2, modulus=x^2-x+1)
            sage: E0 = EllipticCurve(F, (0, 1))
            sage: E1 = EllipticCurve(F, (8, 1))
            sage: phi = E0.isogeny(kernel=E0((a, 0)), codomain=E1)
            sage: phi.dual()
            Isogeny of degree 2
             from Elliptic Curve defined by y^2 = x^3 + 8*x + 1 over Finite Field in a of size 23^2
             to Elliptic Curve defined by y^2 = x^3 + 1 over Finite Field in a of size 23^2
        """

def compute_isogeny_bmss(E1, E2, l):
    """
    Compute the kernel polynomial of the unique normalized isogeny
    of degree ``l`` between ``E1`` and ``E2``.

    Both curves must be given in short Weierstrass form, and the
    characteristic must be either `0` or no smaller than `4l+4`.

    ALGORITHM: [BMSS2006]_, algorithm *fastElkies'*.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import compute_isogeny_bmss
        sage: E1 = EllipticCurve(GF(167), [153, 112])
        sage: E2 = EllipticCurve(GF(167), [56, 40])
        sage: compute_isogeny_bmss(E1, E2, 13)
        x^6 + 139*x^5 + 73*x^4 + 139*x^3 + 120*x^2 + 88*x
    """
def compute_isogeny_stark(E1, E2, ell):
    """
    Return the kernel polynomial of an isogeny of degree ``ell``
    from ``E1`` to ``E2``.

    INPUT:

    - ``E1`` -- domain elliptic curve in short Weierstrass form

    - ``E2`` -- codomain elliptic curve in short Weierstrass form

    - ``ell`` -- the degree of an isogeny from ``E1`` to ``E2``

    OUTPUT: the kernel polynomial of an isogeny from ``E1`` to ``E2``

    .. NOTE::

        If there is no degree-``ell``, cyclic, separable, normalized
        isogeny from ``E1`` to ``E2``, a :exc:`ValueError` will be
        raised.

    ALGORITHM:

    This function uses Stark's algorithm as presented in Section 6.2
    of [BMSS2006]_.

    .. NOTE::

        As published in [BMSS2006]_, the algorithm is incorrect, and a
        correct version (with slightly different notation) can be found
        in [Mo2009]_.  The algorithm originates in [Sta1973]_.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import compute_isogeny_stark, compute_sequence_of_maps

        sage: E = EllipticCurve(GF(97), [1,0,1,1,0])
        sage: R.<x> = GF(97)[]; f = x^5 + 27*x^4 + 61*x^3 + 58*x^2 + 28*x + 21
        sage: phi = EllipticCurveIsogeny(E, f)
        sage: E2 = phi.codomain()
        sage: isom1, isom2, E1pr, E2pr, ker_poly = compute_sequence_of_maps(E, E2, 11)
        sage: compute_isogeny_stark(E1pr, E2pr, 11)
        x^10 + 37*x^9 + 53*x^8 + 66*x^7 + 66*x^6 + 17*x^5 + 57*x^4 + 6*x^3 + 89*x^2 + 53*x + 8

        sage: E = EllipticCurve(GF(37), [0,0,0,1,8])
        sage: R.<x> = GF(37)[]
        sage: f = (x + 14) * (x + 30)
        sage: phi = EllipticCurveIsogeny(E, f)
        sage: E2 = phi.codomain()
        sage: compute_isogeny_stark(E, E2, 5)
        x^4 + 14*x^3 + x^2 + 34*x + 21
        sage: f**2
        x^4 + 14*x^3 + x^2 + 34*x + 21

        sage: E = EllipticCurve(QQ, [0,0,0,1,0])
        sage: R.<x> = QQ[]
        sage: f = x
        sage: phi = EllipticCurveIsogeny(E, f)
        sage: E2 = phi.codomain()
        sage: compute_isogeny_stark(E, E2, 2)
        x

    TESTS:

    Check for :issue:`21883`::

        sage: E1 = EllipticCurve([0,1])
        sage: E2 = EllipticCurve([0,-27])
        sage: E1.isogeny(None, E2, degree=3)
        Isogeny of degree 3 from Elliptic Curve defined by y^2 = x^3 + 1 over Rational Field to Elliptic Curve defined by y^2 = x^3 - 27 over Rational Field
    """
def compute_isogeny_kernel_polynomial(E1, E2, ell, algorithm=None):
    """
    Return the kernel polynomial of a cyclic, separable, normalized
    isogeny of degree ``ell`` from ``E1`` to ``E2``.

    INPUT:

    - ``E1`` -- domain elliptic curve in short Weierstrass form

    - ``E2`` -- codomain elliptic curve in short Weierstrass form

    - ``ell`` -- the degree of an isogeny from ``E1`` to ``E2``

    - ``algorithm`` -- ``None`` (default, choose automatically) or
      ``'bmss'`` (:func:`compute_isogeny_bmss`) or
      ``'stark'`` (:func:`compute_isogeny_stark`)

    OUTPUT: the kernel polynomial of an isogeny from ``E1`` to ``E2``

    .. NOTE::

        If there is no degree-``ell``, cyclic, separable, normalized
        isogeny from ``E1`` to ``E2``, a :exc:`ValueError` will be
        raised.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import compute_isogeny_kernel_polynomial

        sage: E = EllipticCurve(GF(37), [0,0,0,1,8])
        sage: R.<x> = GF(37)[]
        sage: f = (x + 14) * (x + 30)
        sage: phi = EllipticCurveIsogeny(E, f)
        sage: E2 = phi.codomain()
        sage: compute_isogeny_kernel_polynomial(E, E2, 5)
        x^2 + 7*x + 13
        sage: f
        x^2 + 7*x + 13

        sage: # needs sage.rings.number_field
        sage: R.<x> = QQ[]
        sage: K.<i> = NumberField(x^2 + 1)
        sage: E = EllipticCurve(K, [0,0,0,1,0])
        sage: E2 = EllipticCurve(K, [0,0,0,16,0])
        sage: compute_isogeny_kernel_polynomial(E, E2, 4)
        x^3 + x

    TESTS:

    Check that :meth:`Polynomial.radical` is doing the right thing for us::

        sage: E = EllipticCurve(GF(37), [0,0,0,1,8])
        sage: R.<x> = GF(37)[]
        sage: f = (x + 10) * (x + 12) * (x + 16)
        sage: phi = EllipticCurveIsogeny(E, f)
        sage: E2 = phi.codomain()
        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import compute_isogeny_stark
        sage: ker_poly = compute_isogeny_stark(E, E2, 7); ker_poly
        x^6 + 2*x^5 + 20*x^4 + 11*x^3 + 36*x^2 + 35*x + 16
        sage: ker_poly.factor()
        (x + 10)^2 * (x + 12)^2 * (x + 16)^2
        sage: poly = ker_poly.radical(); poly
        x^3 + x^2 + 28*x + 33
        sage: poly.factor()
        (x + 10) * (x + 12) * (x + 16)
    """
def compute_intermediate_curves(E1, E2):
    """
    Return intermediate curves and isomorphisms.

    .. NOTE::

        This is used to compute `\\wp` functions from the short
        Weierstrass model more easily.

    .. WARNING::

        The base field must be of characteristic not equal to `2` or `3`.

    INPUT:

    - ``E1``, ``E2`` -- elliptic curves

    OUTPUT:

    A tuple (``pre_isomorphism``, ``post_isomorphism``,
    ``intermediate_domain``, ``intermediate_codomain``) where:

    - ``intermediate_domain`` is a short Weierstrass curve isomorphic
      to ``E1``;

    - ``intermediate_codomain`` is a short Weierstrass curve isomorphic
      to ``E2``;

    - ``pre_isomorphism`` is a normalized isomorphism from ``E1`` to
      ``intermediate_domain``;

    - ``post_isomorphism`` is a normalized isomorphism from
      ``intermediate_codomain`` to ``E2``.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import compute_intermediate_curves
        sage: E = EllipticCurve(GF(83), [1,0,1,1,0])
        sage: R.<x> = GF(83)[]; f = x + 24
        sage: phi = EllipticCurveIsogeny(E, f)
        sage: E2 = phi.codomain()
        sage: compute_intermediate_curves(E, E2)
        (Elliptic Curve defined by y^2 = x^3 + 62*x + 74 over Finite Field of size 83,
         Elliptic Curve defined by y^2 = x^3 + 65*x + 69 over Finite Field of size 83,
         Elliptic-curve morphism:
          From: Elliptic Curve defined by y^2 + x*y + y = x^3 + x
                over Finite Field of size 83
          To:   Elliptic Curve defined by y^2 = x^3 + 62*x + 74
                over Finite Field of size 83
          Via:  (u,r,s,t) = (1, 76, 41, 3),
         Elliptic-curve morphism:
          From: Elliptic Curve defined by y^2 = x^3 + 65*x + 69
                over Finite Field of size 83
          To:   Elliptic Curve defined by y^2 + x*y + y = x^3 + 4*x + 16
                over Finite Field of size 83
          Via:  (u,r,s,t) = (1, 7, 42, 42))

        sage: # needs sage.rings.number_field
        sage: R.<x> = QQ[]
        sage: K.<i> = NumberField(x^2 + 1)
        sage: E = EllipticCurve(K, [0,0,0,1,0])
        sage: E2 = EllipticCurve(K, [0,0,0,16,0])
        sage: compute_intermediate_curves(E, E2)
        (Elliptic Curve defined by y^2 = x^3 + x
          over Number Field in i with defining polynomial x^2 + 1,
         Elliptic Curve defined by y^2 = x^3 + 16*x
          over Number Field in i with defining polynomial x^2 + 1,
         Elliptic-curve endomorphism of Elliptic Curve defined by y^2 = x^3 + x
          over Number Field in i with defining polynomial x^2 + 1
          Via:  (u,r,s,t) = (1, 0, 0, 0),
         Elliptic-curve endomorphism of Elliptic Curve defined by y^2 = x^3 + 16*x
          over Number Field in i with defining polynomial x^2 + 1
          Via:  (u,r,s,t) = (1, 0, 0, 0))
    """
def compute_sequence_of_maps(E1, E2, ell):
    """
    Return intermediate curves, isomorphisms and kernel polynomial.

    INPUT:

    - ``E1``, ``E2`` -- elliptic curves

    - ``ell`` -- a prime such that there is a degree-``ell`` separable
      normalized isogeny from ``E1`` to ``E2``

    OUTPUT:

    A tuple (``pre_isom``, ``post_isom``, ``E1pr``, ``E2pr``,
    ``ker_poly``) where:

    - ``E1pr`` is an elliptic curve in short Weierstrass form
      isomorphic to ``E1``;

    - ``E2pr`` is an elliptic curve in short Weierstrass form
      isomorphic to ``E2``;

    - ``pre_isom`` is a normalized isomorphism from ``E1`` to ``E1pr``;

    - ``post_isom`` is a normalized isomorphism from ``E2pr`` to ``E2``;

    - ``ker_poly`` is the kernel polynomial of an ``ell``-isogeny from
      ``E1pr`` to ``E2pr``.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import compute_sequence_of_maps
        sage: E = EllipticCurve('11a1')
        sage: R.<x> = QQ[]; f = x^2 - 21*x + 80
        sage: phi = EllipticCurveIsogeny(E, f)
        sage: E2 = phi.codomain()
        sage: compute_sequence_of_maps(E, E2, 5)
        (Elliptic-curve morphism:
          From: Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20
                over Rational Field
          To:   Elliptic Curve defined by y^2 = x^3 - 31/3*x - 2501/108
                over Rational Field
          Via:  (u,r,s,t) = (1, 1/3, 0, -1/2),
         Elliptic-curve morphism:
          From: Elliptic Curve defined by y^2 = x^3 - 23461/3*x - 28748141/108
                over Rational Field
          To:   Elliptic Curve defined by y^2 + y = x^3 - x^2 - 7820*x - 263580
                over Rational Field
          Via:  (u,r,s,t) = (1, -1/3, 0, 1/2),
         Elliptic Curve defined by y^2 = x^3 - 31/3*x - 2501/108 over Rational Field,
         Elliptic Curve defined by y^2 = x^3 - 23461/3*x - 28748141/108 over Rational Field,
         x^2 - 61/3*x + 658/9)

        sage: # needs sage.rings.number_field
        sage: K.<i> = NumberField(x^2 + 1)
        sage: E = EllipticCurve(K, [0,0,0,1,0])
        sage: E2 = EllipticCurve(K, [0,0,0,16,0])
        sage: compute_sequence_of_maps(E, E2, 4)
        (Elliptic-curve endomorphism of Elliptic Curve defined by y^2 = x^3 + x
          over Number Field in i with defining polynomial x^2 + 1
          Via:  (u,r,s,t) = (1, 0, 0, 0),
         Elliptic-curve endomorphism of Elliptic Curve defined by y^2 = x^3 + 16*x
          over Number Field in i with defining polynomial x^2 + 1
          Via:  (u,r,s,t) = (1, 0, 0, 0),
         Elliptic Curve defined by y^2 = x^3 + x
          over Number Field in i with defining polynomial x^2 + 1,
         Elliptic Curve defined by y^2 = x^3 + 16*x
          over Number Field in i with defining polynomial x^2 + 1,
         x^3 + x)

        sage: E = EllipticCurve(GF(97), [1,0,1,1,0])
        sage: R.<x> = GF(97)[]; f = x^5 + 27*x^4 + 61*x^3 + 58*x^2 + 28*x + 21
        sage: phi = EllipticCurveIsogeny(E, f)
        sage: E2 = phi.codomain()
        sage: compute_sequence_of_maps(E, E2, 11)
        (Elliptic-curve morphism:
          From: Elliptic Curve defined by y^2 + x*y + y = x^3 + x
                over Finite Field of size 97
          To:   Elliptic Curve defined by y^2 = x^3 + 52*x + 31
                over Finite Field of size 97
          Via:  (u,r,s,t) = (1, 8, 48, 44),
         Elliptic-curve morphism:
          From: Elliptic Curve defined by y^2 = x^3 + 41*x + 66
                over Finite Field of size 97
          To:   Elliptic Curve defined by y^2 + x*y + y = x^3 + 87*x + 26
                over Finite Field of size 97
          Via:  (u,r,s,t) = (1, 89, 49, 49),
         Elliptic Curve defined by y^2 = x^3 + 52*x + 31 over Finite Field of size 97,
         Elliptic Curve defined by y^2 = x^3 + 41*x + 66 over Finite Field of size 97,
         x^5 + 67*x^4 + 13*x^3 + 35*x^2 + 77*x + 69)
    """
def fill_isogeny_matrix(M):
    """
    Return a filled isogeny matrix giving all degrees from one giving only prime degrees.

    INPUT:

    - ``M`` -- a square symmetric matrix whose off-diagonal `i`, `j`
      entry is either a prime `l` if the `i`-th and `j`-th curves
      have an `l`-isogeny between them, otherwise `0`

    OUTPUT:

    A square matrix with entries `1` on the diagonal, and in
    general the `i`, `j` entry is `d>0` if `d` is the minimal degree
    of an isogeny from the `i`-th to the `j`-th curve.

    EXAMPLES::

        sage: M = Matrix([[0, 2, 3, 3, 0, 0], [2, 0, 0, 0, 3, 3], [3, 0, 0, 0, 2, 0],
        ....:             [3, 0, 0, 0, 0, 2], [0, 3, 2, 0, 0, 0], [0, 3, 0, 2, 0, 0]]); M
        [0 2 3 3 0 0]
        [2 0 0 0 3 3]
        [3 0 0 0 2 0]
        [3 0 0 0 0 2]
        [0 3 2 0 0 0]
        [0 3 0 2 0 0]
        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import fill_isogeny_matrix
        sage: fill_isogeny_matrix(M)
        [ 1  2  3  3  6  6]
        [ 2  1  6  6  3  3]
        [ 3  6  1  9  2 18]
        [ 3  6  9  1 18  2]
        [ 6  3  2 18  1  9]
        [ 6  3 18  2  9  1]
    """
def unfill_isogeny_matrix(M):
    """
    Reverses the action of ``fill_isogeny_matrix``.

    INPUT:

    - ``M`` -- a square symmetric matrix of integers

    OUTPUT:

    A square symmetric matrix obtained from ``M`` by
    replacing non-prime entries with `0`.

    EXAMPLES::

        sage: M = Matrix([[0, 2, 3, 3, 0, 0], [2, 0, 0, 0, 3, 3], [3, 0, 0, 0, 2, 0],
        ....:             [3, 0, 0, 0, 0, 2], [0, 3, 2, 0, 0, 0], [0, 3, 0, 2, 0, 0]]); M
        [0 2 3 3 0 0]
        [2 0 0 0 3 3]
        [3 0 0 0 2 0]
        [3 0 0 0 0 2]
        [0 3 2 0 0 0]
        [0 3 0 2 0 0]
        sage: from sage.schemes.elliptic_curves.ell_curve_isogeny import fill_isogeny_matrix, unfill_isogeny_matrix
        sage: M1 = fill_isogeny_matrix(M); M1
        [ 1  2  3  3  6  6]
        [ 2  1  6  6  3  3]
        [ 3  6  1  9  2 18]
        [ 3  6  9  1 18  2]
        [ 6  3  2 18  1  9]
        [ 6  3 18  2  9  1]
        sage: unfill_isogeny_matrix(M1)
        [0 2 3 3 0 0]
        [2 0 0 0 3 3]
        [3 0 0 0 2 0]
        [3 0 0 0 0 2]
        [0 3 2 0 0 0]
        [0 3 0 2 0 0]
        sage: unfill_isogeny_matrix(M1) == M
        True
    """
