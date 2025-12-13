from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.schemes.elliptic_curves.constructor import EllipticCurve as EllipticCurve
from sage.schemes.elliptic_curves.ell_curve_isogeny import EllipticCurveIsogeny as EllipticCurveIsogeny
from sage.schemes.elliptic_curves.ell_generic import EllipticCurve_generic as EllipticCurve_generic
from sage.schemes.elliptic_curves.hom import EllipticCurveHom as EllipticCurveHom, find_post_isomorphism as find_post_isomorphism
from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite as EllipticCurveHom_composite
from sage.schemes.elliptic_curves.hom_scalar import EllipticCurveHom_scalar as EllipticCurveHom_scalar
from sage.structure.sequence import Sequence as Sequence

class EllipticCurveHom_frobenius(EllipticCurveHom):
    def __init__(self, E, power: int = 1) -> None:
        """
        Construct a Frobenius isogeny on a given curve with a given
        power of the base-ring characteristic.

        Writing `n` for the parameter ``power`` (default: `1`), the
        isogeny is defined by `(x,y) \\to (x^{p^n}, y^{p^n})` where
        `p` is the characteristic of the base ring.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_frobenius import EllipticCurveHom_frobenius
            sage: E = EllipticCurve(j=GF(11^2).gen())
            sage: EllipticCurveHom_frobenius(E)
            Frobenius isogeny of degree 11:
              From: Elliptic Curve defined by y^2 = x^3 + (2*z2+6)*x + (8*z2+8) over Finite Field in z2 of size 11^2
              To:   Elliptic Curve defined by y^2 = x^3 + (9*z2+3)*x + (3*z2+7) over Finite Field in z2 of size 11^2
            sage: EllipticCurveHom_frobenius(E, 2)
            Frobenius endomorphism of degree 121 = 11^2:
              From: Elliptic Curve defined by y^2 = x^3 + (2*z2+6)*x + (8*z2+8) over Finite Field in z2 of size 11^2
              To:   Elliptic Curve defined by y^2 = x^3 + (2*z2+6)*x + (8*z2+8) over Finite Field in z2 of size 11^2

        TESTS::

            sage: EllipticCurveHom_frobenius(EllipticCurve('11a1'))
            Traceback (most recent call last):
            ...
            ValueError: Frobenius isogenies do not exist in characteristic zero

        ::

            sage: EllipticCurveHom_frobenius(E, -1)
            Traceback (most recent call last):
            ...
            ValueError: negative powers of Frobenius are not isogenies
        """
    def rational_maps(self):
        """
        Return the explicit rational maps defining this Frobenius
        isogeny as (sparse) bivariate rational maps in `x` and `y`.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_frobenius import EllipticCurveHom_frobenius
            sage: E = EllipticCurve(GF(11), [1,1])
            sage: pi = EllipticCurveHom_frobenius(E, 4)
            sage: pi.rational_maps()
            (x^14641, y^14641)

        TESTS:

        See :issue:`34811`::

            sage: pi.rational_maps()[0].parent()
            Fraction Field of Multivariate Polynomial Ring in x, y over Finite Field of size 11
            sage: pi.rational_maps()[1].parent()
            Fraction Field of Multivariate Polynomial Ring in x, y over Finite Field of size 11
        """
    def x_rational_map(self):
        """
        Return the `x`-coordinate rational map of this Frobenius
        isogeny as a (sparse) univariate rational map in `x`.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_frobenius import EllipticCurveHom_frobenius
            sage: E = EllipticCurve(GF(11), [1,1])
            sage: pi = EllipticCurveHom_frobenius(E, 4)
            sage: pi.x_rational_map()
            x^14641

        TESTS:

        See :issue:`34811`::

            sage: pi.x_rational_map().parent()
            Fraction Field of Sparse Univariate Polynomial Ring in x over Finite Field of size 11
        """
    def scaling_factor(self):
        """
        Return the Weierstrass scaling factor associated to this
        Frobenius morphism.

        The scaling factor is the constant `u` (in the base field)
        such that `\\varphi^* \\omega_2 = u \\omega_1`, where
        `\\varphi: E_1\\to E_2` is this morphism and `\\omega_i` are
        the standard Weierstrass differentials on `E_i` defined by
        `\\mathrm dx/(2y+a_1x+a_3)`.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_frobenius import EllipticCurveHom_frobenius
            sage: E = EllipticCurve(GF(11), [1,1])
            sage: pi = EllipticCurveHom_frobenius(E)
            sage: pi.formal()
            t^11 + O(t^33)
            sage: pi.scaling_factor()
            0
            sage: pi = EllipticCurveHom_frobenius(E, 3)
            sage: pi.formal()
            t^1331 + O(t^1353)
            sage: pi.scaling_factor()
            0
            sage: pi = EllipticCurveHom_frobenius(E, 0)
            sage: pi == E.scalar_multiplication(1)
            True
            sage: pi.scaling_factor()
            1

        The scaling factor lives in the base ring::

            sage: pi.scaling_factor().parent()
            Finite Field of size 11

        ALGORITHM: Inseparable isogenies of degree `>1` have scaling
        factor `0`.
        """
    def kernel_polynomial(self):
        """
        Return the kernel polynomial of this Frobenius isogeny
        as a polynomial in `x`. This method always returns `1`.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_frobenius import EllipticCurveHom_frobenius
            sage: E = EllipticCurve(GF(11), [1,1])
            sage: pi = EllipticCurveHom_frobenius(E, 5)
            sage: pi.kernel_polynomial()
            1
        """
    @cached_method
    def dual(self):
        """
        Compute the dual of this Frobenius isogeny.

        This method returns an :class:`EllipticCurveHom` object.

        EXAMPLES:

        An ordinary example::

            sage: from sage.schemes.elliptic_curves.hom_scalar import EllipticCurveHom_scalar
            sage: from sage.schemes.elliptic_curves.hom_frobenius import EllipticCurveHom_frobenius
            sage: E = EllipticCurve(GF(31), [0,1])
            sage: f = EllipticCurveHom_frobenius(E)
            sage: f.dual() * f == EllipticCurveHom_scalar(f.domain(), 31)
            True
            sage: f * f.dual() == EllipticCurveHom_scalar(f.codomain(), 31)
            True

        A supersingular example::

            sage: E = EllipticCurve(GF(31), [1,0])
            sage: f = EllipticCurveHom_frobenius(E)
            sage: f.dual() * f == EllipticCurveHom_scalar(f.domain(), 31)
            True
            sage: f * f.dual() == EllipticCurveHom_scalar(f.codomain(), 31)
            True

        TESTS:

        Some random testing (including small characteristic)::

            sage: p = random_prime(50)
            sage: q = p**randrange(1,10)
            sage: n = randrange(20)
            sage: while True:
            ....:     try:
            ....:         E = EllipticCurve([GF(q).random_element() for _ in range(5)])
            ....:         break
            ....:     except ArithmeticError:
            ....:         pass
            sage: f = EllipticCurveHom_frobenius(E, n)
            sage: f.dual() * f == EllipticCurveHom_scalar(E, p**n)
            True
            sage: f * f.dual() == EllipticCurveHom_scalar(f.codomain(), p**n)
            True
            sage: f.dual().dual() == f  # known bug -- broken in characteristic 2,3
            True
            sage: p in (2,3) or f.dual().dual() == f
            True

        ALGORITHM:

        - For supersingular curves, the dual of Frobenius is again purely
          inseparable, so we start out with a Frobenius isogeny of equal
          degree in the opposite direction.

        - For ordinary curves, we immediately reduce to the case of prime
          degree. The kernel of the dual is the unique subgroup of size `p`,
          which we compute from the `p`-division polynomial.

        In both cases, we then search for the correct post-isomorphism
        using :meth:`find_post_isomorphism`.
        """
    def inseparable_degree(self):
        """
        Return the inseparable degree of this Frobenius isogeny.

        Since this class implements only purely inseparable isogenies,
        the inseparable degree equals the degree.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_frobenius import EllipticCurveHom_frobenius
            sage: E = EllipticCurve(GF(11), [1,1])
            sage: pi = EllipticCurveHom_frobenius(E, 4)
            sage: pi.inseparable_degree()
            14641
            sage: pi.inseparable_degree() == pi.degree()
            True
        """
