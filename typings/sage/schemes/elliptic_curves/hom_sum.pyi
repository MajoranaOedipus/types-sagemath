from sage.arith.misc import gcd as gcd
from sage.groups.generic import discrete_log as discrete_log, order_from_multiple as order_from_multiple
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring import polygen as polygen
from sage.schemes.elliptic_curves.ell_field import point_of_order as point_of_order
from sage.schemes.elliptic_curves.hom import EllipticCurveHom as EllipticCurveHom, compare_via_evaluation as compare_via_evaluation
from sage.sets.primes import Primes as Primes
from sage.structure.sequence import Sequence as Sequence

class EllipticCurveHom_sum(EllipticCurveHom):
    def __init__(self, phis, domain=None, codomain=None) -> None:
        """
        Construct a sum morphism of elliptic curves from its summands.
        (For empty sums, the domain and codomain curves must be given.)

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_sum import EllipticCurveHom_sum
            sage: E = EllipticCurve(GF(101), [5,5])
            sage: phi = E.isogenies_prime_degree(7)[0]
            sage: EllipticCurveHom_sum([phi, phi])
            Sum morphism:
              From: Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field of size 101
              To:   Elliptic Curve defined by y^2 = x^3 + 12*x + 98 over Finite Field of size 101
              Via:  (Isogeny of degree 7 from Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field of size 101 to Elliptic Curve defined by y^2 = x^3 + 12*x + 98 over Finite Field of size 101, Isogeny of degree 7 from Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field of size 101 to Elliptic Curve defined by y^2 = x^3 + 12*x + 98 over Finite Field of size 101)

        The zero morphism can be constructed even between non-isogenous curves::

            sage: E1 = EllipticCurve(GF(101), [5,5])
            sage: E2 = EllipticCurve(GF(101), [7,7])
            sage: E1.is_isogenous(E2)
            False
            sage: EllipticCurveHom_sum([], E1, E2)
            Sum morphism:
              From: Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field of size 101
              To:   Elliptic Curve defined by y^2 = x^3 + 7*x + 7 over Finite Field of size 101
              Via:  ()
        """
    def summands(self):
        """
        Return the individual summands making up this sum morphism.

        EXAMPLES::

            sage: E = EllipticCurve(j=5)
            sage: m2 = E.scalar_multiplication(2)
            sage: m3 = E.scalar_multiplication(3)
            sage: m2 + m3
            Sum morphism:
              From: Elliptic Curve defined by y^2 + x*y = x^3 + x^2 + 180*x + 17255 over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y = x^3 + x^2 + 180*x + 17255 over Rational Field
              Via:  (Scalar-multiplication endomorphism [2] of Elliptic Curve defined by y^2 + x*y = x^3 + x^2 + 180*x + 17255 over Rational Field, Scalar-multiplication endomorphism [3] of Elliptic Curve defined by y^2 + x*y = x^3 + x^2 + 180*x + 17255 over Rational Field)
        """
    @cached_method
    def to_isogeny_chain(self):
        """
        Convert this formal sum of elliptic-curve morphisms into a
        :class:`~sage.schemes.elliptic_curves.hom_composite.EllipticCurveHom_composite`
        object representing the same morphism.

        EXAMPLES::

            sage: E = EllipticCurve(GF(101), [5,5])
            sage: phi = E.isogenies_prime_degree(7)[0]
            sage: (phi + phi).to_isogeny_chain()
            Composite morphism of degree 28 = 4*1*7:
              From: Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field of size 101
              To:   Elliptic Curve defined by y^2 = x^3 + 12*x + 98 over Finite Field of size 101

        ::

            sage: p = 419
            sage: E = EllipticCurve(GF(p^2), [1,0])
            sage: iota = E.automorphisms()[2]   # sqrt(-1)
            sage: pi = E.frobenius_isogeny()    # sqrt(-p)
            sage: endo = iota + pi
            sage: endo.degree()
            420
            sage: endo.to_isogeny_chain()
            Composite morphism of degree 420 = 4*1*3*5*7:
              From: Elliptic Curve defined by y^2 = x^3 + x over Finite Field in z2 of size 419^2
              To:   Elliptic Curve defined by y^2 = x^3 + x over Finite Field in z2 of size 419^2

        The decomposition is impossible for the constant zero map::

             sage: endo = iota*pi + pi*iota
             sage: endo.degree()
             0
             sage: endo.to_isogeny_chain()
             Traceback (most recent call last):
             ...
             ValueError: zero morphism cannot be written as a composition of isogenies

        Isomorphisms are supported as well::

            sage: E = EllipticCurve(j=5); E
            Elliptic Curve defined by y^2 + x*y = x^3 + x^2 + 180*x + 17255 over Rational Field
            sage: m2 = E.scalar_multiplication(2)
            sage: m3 = E.scalar_multiplication(3)
            sage: (m2 - m3).to_isogeny_chain()
            Composite morphism of degree 1 = 1^2:
              From: Elliptic Curve defined by y^2 + x*y = x^3 + x^2 + 180*x + 17255 over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y = x^3 + x^2 + 180*x + 17255 over Rational Field
            sage: (m2 - m3).rational_maps()
            (x, -x - y)
        """
    def degree(self):
        """
        Return the degree of this sum morphism.

        EXAMPLES::

            sage: E = EllipticCurve(GF(101), [5,5])
            sage: phi = E.isogenies_prime_degree(7)[0]
            sage: (phi + phi).degree()
            28

        This method yields a simple toy point-counting algorithm::

            sage: E = EllipticCurve(GF(101), [5,5])
            sage: m1 = E.scalar_multiplication(1)
            sage: pi = E.frobenius_endomorphism()
            sage: (pi - m1).degree()
            119
            sage: E.count_points()
            119

        ALGORITHM: Essentially Schoof's algorithm; see :meth:`_compute_degree`.
        """
    def rational_maps(self):
        """
        Return the rational maps of this sum morphism.

        EXAMPLES::

            sage: E = EllipticCurve(GF(101), [5,5])
            sage: phi = E.isogenies_prime_degree(7)[0]
            sage: (phi + phi).rational_maps()
            ((5*x^28 + 43*x^27 + 26*x^26 - ... + 7*x^2 - 23*x + 38)/(23*x^27 + 16*x^26 + 9*x^25 + ... - 43*x^2 - 22*x + 37),
             (42*x^42*y - 44*x^41*y - 22*x^40*y + ... - 26*x^2*y - 50*x*y - 18*y)/(-24*x^42 - 47*x^41 - 12*x^40 + ... + 18*x^2 - 48*x + 18))

        ALGORITHM: :meth:`to_isogeny_chain`.
        """
    def x_rational_map(self):
        """
        Return the `x`-coordinate rational map of this sum morphism.

        EXAMPLES::

            sage: E = EllipticCurve(GF(101), [5,5])
            sage: phi = E.isogenies_prime_degree(7)[0]
            sage: (phi + phi).x_rational_map()
            (9*x^28 + 37*x^27 + 67*x^26 + ... + 53*x^2 + 100*x + 28)/(x^27 + 49*x^26 + 97*x^25 + ... + 64*x^2 + 21*x + 6)

        ALGORITHM: :meth:`to_isogeny_chain`.
        """
    def kernel_polynomial(self):
        """
        Return the kernel polynomial of this sum morphism.

        EXAMPLES::

            sage: E = EllipticCurve(GF(101), [5,5])
            sage: phi = E.isogenies_prime_degree(7)[0]
            sage: (phi + phi).kernel_polynomial()
            x^15 + 75*x^14 + 16*x^13 + 59*x^12 + 28*x^11 + 60*x^10 + 69*x^9 + 79*x^8 + 79*x^7 + 52*x^6 + 35*x^5 + 11*x^4 + 37*x^3 + 69*x^2 + 66*x + 63

        ::

            sage: E = EllipticCurve(GF(11), [5,5])
            sage: pi = E.frobenius_endomorphism()
            sage: m1 = E.scalar_multiplication(1)
            sage: (pi - m1).kernel_polynomial()
            x^9 + 7*x^8 + 2*x^7 + 4*x^6 + 10*x^4 + 4*x^3 + 9*x^2 + 7*x

        ALGORITHM: :meth:`to_isogeny_chain`.
        """
    def scaling_factor(self):
        """
        Return the Weierstrass scaling factor associated to this
        sum morphism.

        The scaling factor is the constant `u` (in the base field)
        such that `\\varphi^* \\omega_2 = u \\omega_1`, where
        `\\varphi: E_1\\to E_2` is this morphism and `\\omega_i` are
        the standard Weierstrass differentials on `E_i` defined by
        `\\mathrm dx/(2y+a_1x+a_3)`.

        EXAMPLES::

            sage: E = EllipticCurve(GF(101), [5,5])
            sage: phi = E.isogenies_prime_degree(7)[0]
            sage: phi.scaling_factor()
            84
            sage: (phi + phi).scaling_factor()
            67

        ALGORITHM: The scaling factor is additive under addition
        of elliptic-curve morphisms, so we simply add together the
        scaling factors of the :meth:`summands`.
        """
    @cached_method
    def dual(self):
        """
        Return the dual of this sum morphism.

        EXAMPLES::

            sage: E = EllipticCurve(GF(101), [5,5])
            sage: phi = E.isogenies_prime_degree(7)[0]
            sage: (phi + phi).dual()
            Sum morphism:
              From: Elliptic Curve defined by y^2 = x^3 + 12*x + 98 over Finite Field of size 101
              To:   Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field of size 101
              Via:  (Isogeny of degree 7 from Elliptic Curve defined by y^2 = x^3 + 12*x + 98 over Finite Field of size 101 to Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field of size 101, Isogeny of degree 7 from Elliptic Curve defined by y^2 = x^3 + 12*x + 98 over Finite Field of size 101 to Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field of size 101)
            sage: (phi + phi).dual() == phi.dual() + phi.dual()
            True

        ::

            sage: E = EllipticCurve(GF(431^2), [1,0])
            sage: iota = E.automorphisms()[2]
            sage: m2 = E.scalar_multiplication(2)
            sage: endo = m2 + iota
            sage: endo.dual()
            Sum morphism:
              From: Elliptic Curve defined by y^2 = x^3 + x over Finite Field in z2 of size 431^2
              To:   Elliptic Curve defined by y^2 = x^3 + x over Finite Field in z2 of size 431^2
              Via:  (Scalar-multiplication endomorphism [2] of Elliptic Curve defined by y^2 = x^3 + x over Finite Field in z2 of size 431^2, Elliptic-curve endomorphism of Elliptic Curve defined by y^2 = x^3 + x over Finite Field in z2 of size 431^2
              Via:  (u,r,s,t) = (8*z2 + 427, 0, 0, 0))
            sage: endo.dual() == (m2 - iota)
            True

        ALGORITHM: Taking the dual distributes over addition.
        """
    @cached_method
    def inseparable_degree(self):
        """
        Compute the inseparable degree of this sum morphism.

        EXAMPLES::

            sage: E = EllipticCurve(GF(7), [0,1])
            sage: m3 = E.scalar_multiplication(3)
            sage: m3.inseparable_degree()
            1
            sage: m4 = E.scalar_multiplication(4)
            sage: m7 = m3 + m4; m7
            Sum morphism:
              From: Elliptic Curve defined by y^2 = x^3 + 1 over Finite Field of size 7
              To:   Elliptic Curve defined by y^2 = x^3 + 1 over Finite Field of size 7
              Via:  (Scalar-multiplication endomorphism [3] of Elliptic Curve defined by y^2 = x^3 + 1 over Finite Field of size 7, Scalar-multiplication endomorphism [4] of Elliptic Curve defined by y^2 = x^3 + 1 over Finite Field of size 7)
            sage: m7.degree()
            49
            sage: m7.inseparable_degree()
            7

        A supersingular example::

            sage: E = EllipticCurve(GF(7), [1,0])
            sage: m3 = E.scalar_multiplication(3)
            sage: m3.inseparable_degree()
            1
            sage: m4 = E.scalar_multiplication(4)
            sage: m7 = m3 + m4; m7
            Sum morphism:
              From: Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 7
              To:   Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 7
              Via:  (Scalar-multiplication endomorphism [3] of Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 7, Scalar-multiplication endomorphism [4] of Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 7)
            sage: m7.inseparable_degree()
            49
        """
