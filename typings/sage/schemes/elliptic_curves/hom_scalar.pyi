from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.schemes.elliptic_curves.ell_generic import EllipticCurve_generic as EllipticCurve_generic
from sage.schemes.elliptic_curves.hom import EllipticCurveHom as EllipticCurveHom
from sage.schemes.elliptic_curves.weierstrass_morphism import negation_morphism as negation_morphism
from sage.structure.richcmp import richcmp as richcmp

class EllipticCurveHom_scalar(EllipticCurveHom):
    def __init__(self, E, m) -> None:
        """
        Construct a scalar-multiplication map on an elliptic curve.

        TESTS::

            sage: from sage.schemes.elliptic_curves.hom_scalar import EllipticCurveHom_scalar
            sage: E = EllipticCurve([1,1])
            sage: EllipticCurveHom_scalar(E, 123)
            Scalar-multiplication endomorphism [123] of Elliptic Curve defined by y^2 = x^3 + x + 1 over Rational Field
        """
    def degree(self):
        """
        Return the degree of this scalar-multiplication morphism.

        The map `[m]` has degree `m^2`.

        EXAMPLES::

            sage: E = EllipticCurve(GF(23), [0,1])
            sage: phi = E.scalar_multiplication(1111111)
            sage: phi.degree()
            1234567654321

        TESTS:

        The degree is still `m^2` even in the inseparable case::

            sage: E = EllipticCurve(GF(23), [1,1])
            sage: E.scalar_multiplication(23).degree()
            529
            sage: E = EllipticCurve(GF(23), [0,1])
            sage: E.scalar_multiplication(23).degree()
            529
        """
    def rational_maps(self):
        """
        Return the pair of explicit rational maps defining this scalar
        multiplication.

        ALGORITHM: :meth:`EllipticCurve_generic.multiplication_by_m`

        EXAMPLES::

            sage: E = EllipticCurve('77a1')
            sage: phi = E.scalar_multiplication(5)
            sage: phi.rational_maps()
            ((x^25 - 200*x^23 - 520*x^22 + ... + 368660*x^2 + 163195*x + 16456)/(25*x^24 + 1240*x^22 + 950*x^21 + ... + 20360*x^2 - 39480*x + 2209),
             (10*x^36*y - 620*x^36 + 3240*x^34*y - ... + 226380480*x + 42986410*y + 20974090)/(1250*x^36 + 93000*x^34 + 71250*x^33 + ... + 138715800*x^2 - 27833400*x + 1038230))
            sage: P = (2,3)
            sage: Q = tuple(r(P) for r in phi.rational_maps()); Q
            (30, 164)
            sage: E(Q) == 5*E(P)
            True

        TESTS::

            sage: {r.parent() for r in phi.rational_maps()}
            {Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field}
        """
    def x_rational_map(self):
        """
        Return the `x`-coordinate rational map of this scalar
        multiplication.

        ALGORITHM: :meth:`EllipticCurve_generic.multiplication_by_m`

        EXAMPLES::

            sage: E = EllipticCurve(GF(65537), [1,2,3,4,5])
            sage: phi = E.scalar_multiplication(7)
            sage: phi.x_rational_map() == phi.rational_maps()[0]
            True

        TESTS::

            sage: phi.x_rational_map().parent()
            Fraction Field of Univariate Polynomial Ring in x over Finite Field of size 65537
        """
    def scaling_factor(self):
        """
        Return the Weierstrass scaling factor associated to this
        scalar multiplication.

        The scaling factor is the constant `u` (in the base field)
        such that `\\varphi^* \\omega_2 = u \\omega_1`, where
        `\\varphi: E_1\\to E_2` is this morphism and `\\omega_i` are
        the standard Weierstrass differentials on `E_i` defined by
        `\\mathrm dx/(2y+a_1x+a_3)`.

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: phi = E.scalar_multiplication(5)
            sage: u = phi.scaling_factor()
            sage: u == phi.formal()[1]
            True
            sage: u == 5
            True

        The scaling factor lives in the base ring::

            sage: E = EllipticCurve(GF(101^2), [5,5])
            sage: phi = E.scalar_multiplication(123)
            sage: phi.scaling_factor()
            22
            sage: phi.scaling_factor().parent()
            Finite Field in z2 of size 101^2

        ALGORITHM: The scaling factor equals the scalar that is being
        multiplied by.
        """
    @cached_method
    def kernel_polynomial(self):
        """
        Return the kernel polynomial of this scalar-multiplication map.
        (When `m=0`, return `0`.)

        EXAMPLES::

            sage: E = EllipticCurve(GF(997), [7,7,7,7,7])
            sage: phi = E.scalar_multiplication(5)
            sage: phi.kernel_polynomial()
            x^12 + 77*x^11 + 380*x^10 + 198*x^9 + 840*x^8 + 376*x^7 + 946*x^6 + 848*x^5 + 246*x^4 + 778*x^3 + 77*x^2 + 518*x + 28

        ::

            sage: E = EllipticCurve(GF(997), [5,6,7,8,9])
            sage: phi = E.scalar_multiplication(11)
            sage: phi.kernel_polynomial()
            x^60 + 245*x^59 + 353*x^58 + 693*x^57 + 499*x^56 + 462*x^55 + 820*x^54 + 962*x^53 + ... + 736*x^7 + 939*x^6 + 429*x^5 + 267*x^4 + 116*x^3 + 770*x^2 + 491*x + 519

        TESTS::

            sage: E = EllipticCurve(j = GF(997^6).random_element())
            sage: m = choice([+1,-1]) * randrange(1,8)
            sage: phi = E.scalar_multiplication(m)
            sage: phi.kernel_polynomial() == phi.x_rational_map().denominator().monic().radical()
            True

        ::

            sage: E.scalar_multiplication(randint(-10,+10)).kernel_polynomial().parent()
            Univariate Polynomial Ring in x over Finite Field in z6 of size 997^6
        """
    def dual(self):
        """
        Return the dual isogeny of this scalar-multiplication map.

        This method simply returns ``self`` as scalars are self-dual.

        EXAMPLES::

            sage: E = EllipticCurve([5,5])
            sage: phi = E.scalar_multiplication(5)
            sage: phi.dual() is phi
            True
        """
    def inseparable_degree(self):
        """
        Return the inseparable degree of this scalar-multiplication map.

        EXAMPLES::

            sage: E = EllipticCurve(GF(7), [0,1])
            sage: E.is_supersingular()
            False
            sage: E.scalar_multiplication(4).inseparable_degree()
            1
            sage: E.scalar_multiplication(-7).inseparable_degree()
            7

        ::

            sage: E = EllipticCurve(GF(7), [1,0])
            sage: E.is_supersingular()
            True
            sage: E.scalar_multiplication(4).inseparable_degree()
            1
            sage: E.scalar_multiplication(-7).inseparable_degree()
            49
        """
    def __neg__(self):
        """
        Negate this scalar-multiplication map, i.e., return `[-m]`
        when this morphism equals `[m]`.

        If rational maps have been computed already, they will be
        reused for the negated morphism.

        EXAMPLES::

            sage: E = EllipticCurve(GF(2^8), [1,0,1,0,1])
            sage: phi = E.scalar_multiplication(23)
            sage: -phi
            Scalar-multiplication endomorphism [-23] of Elliptic Curve defined by y^2 + x*y + y = x^3 + 1 over Finite Field in z8 of size 2^8

        TESTS::

            sage: E = EllipticCurve(GF(79), [7,7])
            sage: phi = E.scalar_multiplication(5)
            sage: _ = phi.rational_maps()
            sage: (-phi)._rational_maps
            ((x^25 + 11*x^23 - 24*x^22 - ... - 7*x^2 + 34*x + 21)/(25*x^24 - 5*x^22 - 23*x^21 - ... - 11*x^2 + 36*x + 21),
             (29*x^36*y + 22*x^34*y - 27*x^33*y - ... + 14*x^2*y - 33*x*y + 37*y)/(9*x^36 + 21*x^34 - 14*x^33 + ... - 26*x^2 + 18*x + 7))
        """
