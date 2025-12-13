from sage.categories.morphism import Morphism as Morphism
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.elliptic_curves.ell_generic import EllipticCurve_generic as EllipticCurve_generic
from sage.schemes.generic.homset import SchemeHomset_generic as SchemeHomset_generic

class EllipticCurveHomset(SchemeHomset_generic):
    """
    This class represents the set of all homomorphisms between two fixed
    elliptic curves.

    EXAMPLES::

        sage: E = EllipticCurve(GF(419^2), [1,0])
        sage: E.frobenius_isogeny() in End(E)
        True
        sage: phi = E.isogenies_prime_degree(7)[0]
        sage: phi in End(E)
        False
        sage: phi in Hom(E, phi.codomain())
        True

    Note that domain and codomain are *not* taken up to isomorphism::

        sage: iso = E.isomorphism_to(EllipticCurve(GF(419^2), [2,0]))
        sage: iso in End(E)
        False
    """
    def __init__(self, E1, E2, category=None) -> None:
        """
        Construct the homset for a given pair of elliptic curves
        defined over the same base ring.

        TESTS::

            sage: E = EllipticCurve(GF(101), [1,1])
            sage: H = End(E)
            sage: TestSuite(H).run(skip='_test_elements')

        ::

            sage: E1 = EllipticCurve(GF(101), [1,1])
            sage: E2 = EllipticCurve(GF(101), [4,9])
            sage: H = Hom(E1, E2)
            sage: TestSuite(H).run(skip='_test_elements')

        ::

            sage: E1 = EllipticCurve(j=42)
            sage: E2 = EllipticCurve(j=43)
            sage: Hom(E1, E2)
            Additive group of elliptic-curve morphisms
              From: Elliptic Curve defined by y^2 = x^3 + 5901*x + 1105454 over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y = x^3 + x^2 + 1510*x - 140675 over Rational Field
            sage: Hom(E1, E2) in CommutativeAdditiveGroups()
            True
            sage: Hom(E1, E2) in Rings()
            False
            sage: End(E1) in CommutativeRings()  # not implemented; see note in code below
            True

        ::

            sage: E0 = EllipticCurve(GF(419), [1,0])
            sage: EE0 = E0.change_ring(GF(419^2))
            sage: End(E0) in CommutativeRings()  # not implemented; see note in code below
            True
            sage: End(EE0) in CommutativeRings()
            False
            sage: End(EE0) in Rings()
            True
            sage: E1 = EllipticCurve(GF(419), [1,1])
            sage: EE1 = E1.change_ring(GF(419^2))
            sage: Hom(E0, E1) in CommutativeAdditiveGroups()
            True
            sage: Hom(EE0, EE1) in CommutativeAdditiveGroups()
            True
            sage: Hom(E0, E1) in Rings()
            False
            sage: Hom(EE0, EE1) in Rings()
            False
        """
    def identity(self):
        """
        Return the identity morphism in this elliptic-curve homset
        as an :class:`EllipticCurveHom` object.

        EXAMPLES::

            sage: E = EllipticCurve(j=42)
            sage: End(E).identity()
            Elliptic-curve endomorphism of Elliptic Curve defined by y^2 = x^3 + 5901*x + 1105454 over Rational Field
              Via:  (u,r,s,t) = (1, 0, 0, 0)
            sage: End(E).identity() == E.scalar_multiplication(1)
            True
        """
    def is_commutative(self):
        """
        Assuming this homset is an endomorphism ring, check whether
        it is a commutative ring.

        ALGORITHM: :meth:`EllipticCurve_field.endomorphism_ring_is_commutative`

        EXAMPLES::

            sage: End(EllipticCurve(j=123)).is_commutative()
            True
            sage: End(EllipticCurve(GF(11), [1,0])).is_commutative()
            True
            sage: End(EllipticCurve(GF(11^2), [1,0])).is_commutative()
            False
        """
