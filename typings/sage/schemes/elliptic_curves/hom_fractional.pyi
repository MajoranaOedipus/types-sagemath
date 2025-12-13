from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.elliptic_curves.hom import EllipticCurveHom as EllipticCurveHom, compare_via_evaluation as compare_via_evaluation
from sage.structure.richcmp import op_EQ as op_EQ
from sage.structure.sequence import Sequence as Sequence

class EllipticCurveHom_fractional(EllipticCurveHom):
    """
    This class represents a (symbolic) quotient of an isogeny divided by an integer.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.hom_fractional import EllipticCurveHom_fractional
        sage: phi = EllipticCurve([1,1]).scalar_multiplication(-2)
        sage: EllipticCurveHom_fractional(phi, 2)
        Fractional elliptic-curve morphism of degree 1:
          Numerator:   Scalar-multiplication endomorphism [-2]
                         of Elliptic Curve defined by y^2 = x^3 + x + 1 over Rational Field
          Denominator: 2
        sage: EllipticCurveHom_fractional(phi, 3)
        Traceback (most recent call last):
        ...
        ValueError: Scalar-multiplication endomorphism [-2]
          of Elliptic Curve defined by y^2 = x^3 + x + 1 over Rational Field
          is not divisible by 3
    """
    def __init__(self, phi, d, *, check: bool = True) -> None:
        """
        Construct a (symbolic) quotient of an isogeny divided by an integer.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_fractional import EllipticCurveHom_fractional
            sage: phi = EllipticCurve(GF(11), [1,1]).scalar_multiplication(-3)
            sage: EllipticCurveHom_fractional(phi, 3)
            Fractional elliptic-curve morphism of degree 1:
              Numerator:   Scalar-multiplication endomorphism [-3]
                             of Elliptic Curve defined by y^2 = x^3 + x + 1 over Finite Field of size 11
              Denominator: 3
        """
    @cached_method
    def to_isogeny_chain(self):
        """
        Convert this fractional elliptic-curve morphism into a (non-fractional)
        :class:`~sage.schemes.elliptic_curves.hom_composite.EllipticCurveHom_composite`
        object representing the same morphism.

        EXAMPLES::

            sage: p = 419
            sage: E = EllipticCurve(GF(p^2), [1,0])
            sage: iota = E.automorphisms()[2]   # sqrt(-1)
            sage: pi = E.frobenius_isogeny()    # sqrt(-p)
            sage: endo = (iota + pi) / 2
            sage: endo.degree()
            105
            sage: endo.to_isogeny_chain()
            Composite morphism of degree 105 = 1*3*5*7:
              From: Elliptic Curve defined by y^2 = x^3 + x over Finite Field in z2 of size 419^2
              To:   Elliptic Curve defined by y^2 = x^3 + x over Finite Field in z2 of size 419^2
            sage: endo.to_isogeny_chain() == endo
            True
        """
    def rational_maps(self):
        """
        Return the pair of explicit rational maps defining this fractional isogeny.

        EXAMPLES::

            sage: E = EllipticCurve(GF(419), [1,0])
            sage: phi = E.isogeny(E(185, 73)); phi.rational_maps()
            ((x^5 + 189*x^4 + 9*x^3 + 114*x^2 + 11*x + 206)/(x^4 + 189*x^3 - 105*x^2 - 171*x - 155),
             (x^6*y + 74*x^5*y - 127*x^4*y + 148*x^3*y + 182*x^2*y + 115*x*y + 43*y)/(x^6 + 74*x^5 - 13*x^4 + x^3 - 88*x^2 - 157*x - 179))
            sage: ((phi + phi) / 2).rational_maps()
            ((x^5 + 189*x^4 + 9*x^3 + 114*x^2 + 11*x + 206)/(x^4 + 189*x^3 - 105*x^2 - 171*x - 155),
             (x^6*y + 74*x^5*y - 127*x^4*y + 148*x^3*y + 182*x^2*y + 115*x*y + 43*y)/(x^6 + 74*x^5 - 13*x^4 + x^3 - 88*x^2 - 157*x - 179))
        """
    def x_rational_map(self):
        """
        Return the `x`-coordinate rational map of this fractional isogeny.

        EXAMPLES::

            sage: E = EllipticCurve(GF(419), [1,0])
            sage: phi = E.isogeny(E(185, 73)); phi.x_rational_map()
            (x^5 + 189*x^4 + 9*x^3 + 114*x^2 + 11*x + 206)/(x^4 + 189*x^3 + 314*x^2 + 248*x + 264)
            sage: ((phi + phi) / 2).x_rational_map()
            (x^5 + 189*x^4 + 9*x^3 + 114*x^2 + 11*x + 206)/(x^4 + 189*x^3 + 314*x^2 + 248*x + 264)
        """
    def kernel_polynomial(self):
        """
        Return the kernel polynomial of this fractional isogeny.

        EXAMPLES::

            sage: E = EllipticCurve(GF(419), [1,0])
            sage: phi = E.isogeny(E(185, 73)); phi.kernel_polynomial()
            x^2 + 304*x + 39
            sage: ((phi + phi) / 2).kernel_polynomial()
            x^2 + 304*x + 39
        """
    @cached_method
    def dual(self):
        """
        Return the dual of this fractional isogeny.

        EXAMPLES::

            sage: E = EllipticCurve(GF(419), [1,0])
            sage: phi = E.isogeny(E(185, 73))
            sage: ((phi + phi) / 2).dual() == phi.dual()
            True
        """
    def formal(self, *args):
        """
        Return the formal isogeny corresponding to this fractional
        isogeny as a power series in the variable `t=-x/y` on the
        domain curve.

        EXAMPLES::

            sage: E = EllipticCurve(GF(419), [-1,0])
            sage: pi = E.frobenius_isogeny()
            sage: ((1 + pi) / 2).formal()
            210*t + 26*t^5 + 254*t^9 + 227*t^13 + 36*t^17 + 74*t^21 + O(t^23)
        """
    def scaling_factor(self):
        """
        Return the Weierstrass scaling factor associated to this
        fractional isogeny.

        The scaling factor is the constant `u` (in the base field)
        such that `\\varphi^* \\omega_2 = u \\omega_1`, where
        `\\varphi: E_1\\to E_2` is this morphism and `\\omega_i` are
        the standard Weierstrass differentials on `E_i` defined by
        `\\mathrm dx/(2y+a_1x+a_3)`.

        EXAMPLES::

            sage: E = EllipticCurve(GF(419), [-1,0])
            sage: pi = E.frobenius_isogeny()
            sage: ((1 + pi) / 2).scaling_factor()
            210
        """
    def inseparable_degree(self):
        """
        Return the inseparable degree of this morphism.

        EXAMPLES::

            sage: E = EllipticCurve(GF(419), [-1,0])
            sage: pi = E.frobenius_isogeny()
            sage: ((1 + pi) / 2).inseparable_degree()
            1
            sage: E = EllipticCurve(GF(419), [-1,0])
            sage: pi = E.frobenius_isogeny()
            sage: ((3*pi - pi) / 2).inseparable_degree()
            419
        """
