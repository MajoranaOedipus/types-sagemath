from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import integer_floor as integer_floor
from sage.categories.morphism import Morphism as Morphism
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.finite_rings import finite_field_base as finite_field_base
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field import number_field_base as number_field_base
from sage.structure.richcmp import op_EQ as op_EQ, op_NE as op_NE, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal

class EllipticCurveHom(Morphism):
    """
    Base class for elliptic-curve morphisms.
    """
    def __init__(self, *args, **kwds) -> None:
        """
        Constructor for elliptic-curve morphisms.

        EXAMPLES::

            sage: E = EllipticCurve(GF(257^2), [5,5])
            sage: P = E.lift_x(1)
            sage: E.isogeny(P)                        # indirect doctest
            Isogeny of degree 127 from Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field in z2 of size 257^2 to Elliptic Curve defined by y^2 = x^3 + 151*x + 22 over Finite Field in z2 of size 257^2
            sage: E.isogeny(P, algorithm='factored')  # indirect doctest
            Composite morphism of degree 127:
              From: Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field in z2 of size 257^2
              To:   Elliptic Curve defined by y^2 = x^3 + 151*x + 22 over Finite Field in z2 of size 257^2
            sage: E.isogeny(P, algorithm='velusqrt')  # indirect doctest
            Elliptic-curve isogeny (using square-root Vélu) of degree 127:
              From: Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field in z2 of size 257^2
              To:   Elliptic Curve defined by y^2 = x^3 + 119*x + 231 over Finite Field in z2 of size 257^2
            sage: E.montgomery_model(morphism=True)   # indirect doctest
            (Elliptic Curve defined by y^2 = x^3 + (199*z2+73)*x^2 + x over Finite Field in z2 of size 257^2,
             Elliptic-curve morphism:
               From: Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field in z2 of size 257^2
               To:   Elliptic Curve defined by y^2 = x^3 + (199*z2+73)*x^2 + x over Finite Field in z2 of size 257^2
               Via:  (u,r,s,t) = (88*z2 + 253, 208*z2 + 90, 0, 0))
        """
    def degree(self):
        """
        Return the degree of this elliptic-curve morphism.

        EXAMPLES::

            sage: E = EllipticCurve(QQ, [0,0,0,1,0])
            sage: phi = EllipticCurveIsogeny(E, E((0,0)))
            sage: phi.degree()
            2
            sage: phi = EllipticCurveIsogeny(E, [0,1,0,1])
            sage: phi.degree()
            4

            sage: E = EllipticCurve(GF(31), [1,0,0,1,2])
            sage: phi = EllipticCurveIsogeny(E, [17, 1])
            sage: phi.degree()
            3

        Degrees are multiplicative, so the degree of a composite isogeny
        is the product of the degrees of the individual factors::

            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: E = EllipticCurve(GF(419), [1,0])
            sage: P, = E.gens()
            sage: phi = EllipticCurveHom_composite(E, P+P)
            sage: phi.degree()
            210
            sage: phi.degree() == prod(f.degree() for f in phi.factors())
            True

        Isomorphisms always have degree `1` by definition::

            sage: E1 = EllipticCurve([1,2,3,4,5])
            sage: E2 = EllipticCurve_from_j(E1.j_invariant())
            sage: E1.isomorphism_to(E2).degree()
            1

        TESTS::

            sage: from sage.schemes.elliptic_curves.hom import EllipticCurveHom
            sage: EllipticCurveHom.degree(None)
            Traceback (most recent call last):
            ...
            NotImplementedError: ...
        """
    @cached_method
    def trace(self):
        """
        Return the trace of this elliptic-curve morphism, which must
        be an endomorphism.

        ALGORITHM: :func:`compute_trace_generic`

        EXAMPLES::

            sage: E = EllipticCurve(QQ, [42, 42])
            sage: m5 = E.scalar_multiplication(5)
            sage: m5.trace()
            10

        ::

            sage: E = EllipticCurve(GF(71^2), [45, 45])
            sage: P = E.lift_x(27)
            sage: P.order()
            71
            sage: tau = E.isogeny(P, codomain=E)
            sage: tau.trace()
            -1

        TESTS:

        Make sure the cached value of the trace is not accidentally
        copied on composition with automorphisms::

            sage: aut = E.automorphisms()[1]  # [-1]
            sage: (aut * tau).trace()
            1

        It also works for more complicated :class:`EllipticCurveHom`
        children::

            sage: tau = E.isogeny(P, codomain=E, algorithm='velusqrt')
            sage: tau.trace()
            -1

        Check that negation commutes with taking the trace::

            sage: (-tau).trace()
            1
        """
    def characteristic_polynomial(self):
        """
        Return the characteristic polynomial of this elliptic-curve
        morphism, which must be an endomorphism.

        .. SEEALSO::

            - :meth:`degree`
            - :meth:`trace`

        EXAMPLES::

            sage: E = EllipticCurve(QQ, [42, 42])
            sage: m5 = E.scalar_multiplication(5)
            sage: m5.characteristic_polynomial()
            x^2 - 10*x + 25

        ::

            sage: E = EllipticCurve(GF(71), [42, 42])
            sage: pi = E.frobenius_endomorphism()
            sage: pi.characteristic_polynomial()
            x^2 - 8*x + 71
            sage: E.frobenius().charpoly()
            x^2 - 8*x + 71

        TESTS::

            sage: m5.characteristic_polynomial().parent()
            Univariate Polynomial Ring in x over Integer Ring
            sage: pi.characteristic_polynomial().parent()
            Univariate Polynomial Ring in x over Integer Ring
        """
    def kernel_polynomial(self) -> None:
        """
        Return the kernel polynomial of this elliptic-curve morphism.

        Implemented by child classes. For examples, see:

        - :meth:`EllipticCurveIsogeny.kernel_polynomial`
        - :meth:`sage.schemes.elliptic_curves.weierstrass_morphism.WeierstrassIsomorphism.kernel_polynomial`
        - :meth:`sage.schemes.elliptic_curves.hom_composite.EllipticCurveHom_composite.kernel_polynomial`
        - :meth:`sage.schemes.elliptic_curves.hom_sum.EllipticCurveHom_sum.kernel_polynomial`
        - :meth:`sage.schemes.elliptic_curves.hom_scalar.EllipticCurveHom_scalar.kernel_polynomial`
        - :meth:`sage.schemes.elliptic_curves.hom_frobenius.EllipticCurveHom_frobenius.kernel_polynomial`
        - :meth:`sage.schemes.elliptic_curves.hom_velusqrt.EllipticCurveHom_velusqrt.kernel_polynomial`
        - :meth:`sage.schemes.elliptic_curves.hom_fractional.EllipticCurveHom_fractional.kernel_polynomial`

        TESTS::

            sage: from sage.schemes.elliptic_curves.hom import EllipticCurveHom
            sage: EllipticCurveHom.kernel_polynomial(None)
            Traceback (most recent call last):
            ...
            NotImplementedError: ...
        """
    def kernel_points(self) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator over the points in the kernel of this
        elliptic-curve morphism.

        EXAMPLES::

            sage: E.<P, Q> = EllipticCurve(GF(5^2), [1, 2, 3, 3, 1])
            sage: f = E.isogeny([P*3, Q*3])
            sage: set(f.kernel_points())
            {(0 : 1 : 0), (4 : 4 : 1), (2*z2 + 4 : 4*z2 + 4 : 1), (3*z2 + 1 : z2 + 3 : 1)}

        In the inseparable case::

            sage: E = EllipticCurve(GF(23), [1,1])
            sage: set(E.scalar_multiplication(23).kernel_points())
            {(0 : 1 : 0)}

        Check that the result is consistent with
        :meth:`~sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_field.division_points`::

            sage: set(E.scalar_multiplication(4).kernel_points()) == set(E(0).division_points(4))
            True
        """
    def dual(self) -> None:
        """
        Return the dual of this elliptic-curve morphism.

        Implemented by child classes. For examples, see:

        - :meth:`EllipticCurveIsogeny.dual`
        - :meth:`sage.schemes.elliptic_curves.weierstrass_morphism.WeierstrassIsomorphism.dual`
        - :meth:`sage.schemes.elliptic_curves.hom_composite.EllipticCurveHom_composite.dual`
        - :meth:`sage.schemes.elliptic_curves.hom_sum.EllipticCurveHom_sum.dual`
        - :meth:`sage.schemes.elliptic_curves.hom_scalar.EllipticCurveHom_scalar.dual`
        - :meth:`sage.schemes.elliptic_curves.hom_frobenius.EllipticCurveHom_frobenius.dual`
        - :meth:`sage.schemes.elliptic_curves.hom_velusqrt.EllipticCurveHom_velusqrt.dual`
        - :meth:`sage.schemes.elliptic_curves.hom_fractional.EllipticCurveHom_fractional.dual`

        TESTS::

            sage: from sage.schemes.elliptic_curves.hom import EllipticCurveHom
            sage: EllipticCurveHom.dual(None)
            Traceback (most recent call last):
            ...
            NotImplementedError: ...
        """
    def rational_maps(self) -> None:
        """
        Return the pair of explicit rational maps defining this
        elliptic-curve morphism as fractions of bivariate
        polynomials in `x` and `y`.

        Implemented by child classes. For examples, see:

        - :meth:`EllipticCurveIsogeny.rational_maps`
        - :meth:`sage.schemes.elliptic_curves.weierstrass_morphism.WeierstrassIsomorphism.rational_maps`
        - :meth:`sage.schemes.elliptic_curves.hom_composite.EllipticCurveHom_composite.rational_maps`
        - :meth:`sage.schemes.elliptic_curves.hom_sum.EllipticCurveHom_sum.rational_maps`
        - :meth:`sage.schemes.elliptic_curves.hom_scalar.EllipticCurveHom_scalar.rational_maps`
        - :meth:`sage.schemes.elliptic_curves.hom_frobenius.EllipticCurveHom_frobenius.rational_maps`
        - :meth:`sage.schemes.elliptic_curves.hom_velusqrt.EllipticCurveHom_velusqrt.rational_maps`
        - :meth:`sage.schemes.elliptic_curves.hom_fractional.EllipticCurveHom_fractional.rational_maps`

        TESTS::

            sage: from sage.schemes.elliptic_curves.hom import EllipticCurveHom
            sage: EllipticCurveHom.rational_maps(None)
            Traceback (most recent call last):
            ...
            NotImplementedError: ...
        """
    def x_rational_map(self) -> None:
        """
        Return the `x`-coordinate rational map of this elliptic-curve
        morphism as a univariate rational expression in `x`.

        Implemented by child classes. For examples, see:

        - :meth:`EllipticCurveIsogeny.x_rational_map`
        - :meth:`sage.schemes.elliptic_curves.weierstrass_morphism.WeierstrassIsomorphism.x_rational_map`
        - :meth:`sage.schemes.elliptic_curves.hom_composite.EllipticCurveHom_composite.x_rational_map`
        - :meth:`sage.schemes.elliptic_curves.hom_sum.EllipticCurveHom_sum.x_rational_map`
        - :meth:`sage.schemes.elliptic_curves.hom_scalar.EllipticCurveHom_scalar.x_rational_map`
        - :meth:`sage.schemes.elliptic_curves.hom_frobenius.EllipticCurveHom_frobenius.x_rational_map`
        - :meth:`sage.schemes.elliptic_curves.hom_velusqrt.EllipticCurveHom_velusqrt.x_rational_map`
        - :meth:`sage.schemes.elliptic_curves.hom_fractional.EllipticCurveHom_fractional.x_rational_map`

        TESTS::

            sage: from sage.schemes.elliptic_curves.hom import EllipticCurveHom
            sage: EllipticCurveHom.x_rational_map(None)
            Traceback (most recent call last):
            ...
            NotImplementedError: ...
        """
    def inverse_image(self, Q, /, *, all: bool = False):
        """
        Return an arbitrary element ``P`` in the domain such that
        ``self(P) == Q``, or raise ``ValueError`` if no such
        element exists.

        INPUT:

        - ``Q`` -- a point
        - ``all`` -- if true, returns an iterator over all points
          in the inverse image

        EXAMPLES::

            sage: E.<P, Q> = EllipticCurve(GF(5^2), [1, 2, 3, 3, 1])
            sage: f = E.isogeny([P*3])
            sage: f(f.inverse_image(f(Q))) == f(Q)
            True
            sage: E.scalar_multiplication(-1).inverse_image(P) == -P
            True
            sage: f.inverse_image(f.codomain().0)
            Traceback (most recent call last):
            ...
            ValueError: ...
            sage: len(list(f.inverse_image(f(Q), all=True)))
            2

        Check that the result is consistent with
        :meth:`~sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_field.division_points`::

            sage: E = EllipticCurve('37a'); E
            Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
            sage: P = E(0, -1)
            sage: (P * 5).division_points(5)
            [(0 : -1 : 1)]
            sage: E.scalar_multiplication(5).inverse_image(P * 5)
            (0 : -1 : 1)

        Points from wrong curves cannot be passed in::

            sage: f.inverse_image(Q)
            Traceback (most recent call last):
            ...
            TypeError: input must be a point in the codomain

        TESTS::

            sage: f.inverse_image(E.zero())
            Traceback (most recent call last):
            ...
            TypeError: input must be a point in the codomain
            sage: f.inverse_image(f.codomain().zero())
            (0 : 1 : 0)

        You can give a tuple as input::

            sage: f.inverse_image((0, 2))  # random
            (2 : 3*z2 + 1 : 1)
            sage: f(f.inverse_image((0, 2)))
            (0 : 2 : 1)

        Stress test::

            sage: # long time
            ....: for p in primes(2, 12):
            ....:     for a in range(p):
            ....:         for b in range(p):
            ....:             try: E = EllipticCurve(GF(p), [a, b]); P = E.0
            ....:             except: continue  # maybe singular curve or E.0 doesn't exist
            ....:             for n in P.order().divisors():
            ....:                 f = E.isogeny(P*n)
            ....:                 for R in E:
            ....:                     Q = f(R)
            ....:                     assert f(f.inverse_image(Q)) == Q
            ....:                 for Q in f.codomain():
            ....:                     try:
            ....:                         ignore = f.inverse_image(Q)
            ....:                     except ValueError:  # no inverse image found
            ....:                         continue
        """
    def scaling_factor(self) -> None:
        """
        Return the Weierstrass scaling factor associated to this
        elliptic-curve morphism.

        The scaling factor is the constant `u` (in the base field)
        such that `\\varphi^* \\omega_2 = u \\omega_1`, where
        `\\varphi: E_1\\to E_2` is this morphism and `\\omega_i` are
        the standard Weierstrass differentials on `E_i` defined by
        `\\mathrm dx/(2y+a_1x+a_3)`.

        Implemented by child classes. For examples, see:

        - :meth:`EllipticCurveIsogeny.scaling_factor`
        - :meth:`sage.schemes.elliptic_curves.weierstrass_morphism.WeierstrassIsomorphism.scaling_factor`
        - :meth:`sage.schemes.elliptic_curves.hom_composite.EllipticCurveHom_composite.scaling_factor`
        - :meth:`sage.schemes.elliptic_curves.hom_sum.EllipticCurveHom_sum.scaling_factor`
        - :meth:`sage.schemes.elliptic_curves.hom_scalar.EllipticCurveHom_scalar.scaling_factor`
        - :meth:`sage.schemes.elliptic_curves.hom_velusqrt.EllipticCurveHom_velusqrt.scaling_factor`
        - :meth:`sage.schemes.elliptic_curves.hom_fractional.EllipticCurveHom_fractional.scaling_factor`

        TESTS::

            sage: from sage.schemes.elliptic_curves.hom import EllipticCurveHom
            sage: EllipticCurveHom.scaling_factor(None)
            Traceback (most recent call last):
            ...
            NotImplementedError: ...
        """
    def formal(self, prec: int = 20):
        """
        Return the formal isogeny associated to this elliptic-curve
        morphism as a power series in the variable `t=-x/y` on the
        domain curve.

        INPUT:

        - ``prec`` -- (default: 20) the precision with which the
          computations in the formal group are carried out

        EXAMPLES::

            sage: E = EllipticCurve(GF(13),[1,7])
            sage: phi = E.isogeny(E(10,4))
            sage: phi.formal()
            t + 12*t^13 + 2*t^17 + 8*t^19 + 2*t^21 + O(t^23)

        ::

            sage: E = EllipticCurve([0,1])
            sage: phi = E.isogeny(E(2,3))
            sage: phi.formal(prec=10)
            t + 54*t^5 + 255*t^7 + 2430*t^9 + 19278*t^11 + O(t^13)

        ::

            sage: E = EllipticCurve('11a2')
            sage: R.<x> = QQ[]
            sage: phi = E.isogeny(x^2 + 101*x + 12751/5)
            sage: phi.formal(prec=7)
            t - 2724/5*t^5 + 209046/5*t^7 - 4767/5*t^8 + 29200946/5*t^9 + O(t^10)
        """
    def is_normalized(self):
        """
        Determine whether this morphism is a normalized isogeny.

        .. NOTE::

            An isogeny `\\varphi\\colon E_1\\to E_2` between two given
            Weierstrass equations is said to be *normalized* if the
            `\\varphi^*(\\omega_2) = \\omega_1`, where `\\omega_1` and
            `\\omega_2` are the invariant differentials on `E_1` and
            `E_2` corresponding to the given equation.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
            sage: E = EllipticCurve(GF(7), [0,0,0,1,0])
            sage: R.<x> = GF(7)[]
            sage: phi = EllipticCurveIsogeny(E, x)
            sage: phi.is_normalized()
            True
            sage: isom = WeierstrassIsomorphism(phi.codomain(), (3, 0, 0, 0))
            sage: phi = isom * phi
            sage: phi.is_normalized()
            False
            sage: isom = WeierstrassIsomorphism(phi.codomain(), (5, 0, 0, 0))
            sage: phi = isom * phi
            sage: phi.is_normalized()
            True
            sage: isom = WeierstrassIsomorphism(phi.codomain(), (1, 1, 1, 1))
            sage: phi = isom * phi
            sage: phi.is_normalized()
            True

        ::

            sage: F = GF(2^5, 'alpha'); alpha = F.gen()
            sage: E = EllipticCurve(F, [1,0,1,1,1])
            sage: R.<x> = F[]
            sage: phi = EllipticCurveIsogeny(E, x+1)
            sage: isom = WeierstrassIsomorphism(phi.codomain(), (alpha, 0, 0, 0))
            sage: phi.is_normalized()
            True
            sage: phi = isom * phi
            sage: phi.is_normalized()
            False
            sage: isom = WeierstrassIsomorphism(phi.codomain(), (1/alpha, 0, 0, 0))
            sage: phi = isom * phi
            sage: phi.is_normalized()
            True
            sage: isom = WeierstrassIsomorphism(phi.codomain(), (1, 1, 1, 1))
            sage: phi = isom * phi
            sage: phi.is_normalized()
            True

        ::

            sage: E = EllipticCurve('11a1')
            sage: R.<x> = QQ[]
            sage: f = x^3 - x^2 - 10*x - 79/4
            sage: phi = EllipticCurveIsogeny(E, f)
            sage: isom = WeierstrassIsomorphism(phi.codomain(), (2, 0, 0, 0))
            sage: phi.is_normalized()
            True
            sage: phi = isom * phi
            sage: phi.is_normalized()
            False
            sage: isom = WeierstrassIsomorphism(phi.codomain(), (1/2, 0, 0, 0))
            sage: phi = isom * phi
            sage: phi.is_normalized()
            True
            sage: isom = WeierstrassIsomorphism(phi.codomain(), (1, 1, 1, 1))
            sage: phi = isom * phi
            sage: phi.is_normalized()
            True

        ALGORITHM: We check if :meth:`scaling_factor` returns `1`.
        """
    def inseparable_degree(self) -> None:
        """
        Return the inseparable degree of this isogeny.

        Implemented by child classes. For examples, see:

        - :meth:`EllipticCurveIsogeny.inseparable_degree`
        - :meth:`sage.schemes.elliptic_curves.weierstrass_morphism.WeierstrassIsomorphism.inseparable_degree`
        - :meth:`sage.schemes.elliptic_curves.hom_composite.EllipticCurveHom_composite.inseparable_degree`
        - :meth:`sage.schemes.elliptic_curves.hom_sum.EllipticCurveHom_sum.inseparable_degree`
        - :meth:`sage.schemes.elliptic_curves.hom_scalar.EllipticCurveHom_scalar.inseparable_degree`
        - :meth:`sage.schemes.elliptic_curves.hom_frobenius.EllipticCurveHom_frobenius.inseparable_degree`
        - :meth:`sage.schemes.elliptic_curves.hom_velusqrt.EllipticCurveHom_velusqrt.inseparable_degree`
        - :meth:`sage.schemes.elliptic_curves.hom_fractional.EllipticCurveHom_fractional.inseparable_degree`

        TESTS::

            sage: from sage.schemes.elliptic_curves.hom import EllipticCurveHom
            sage: EllipticCurveHom.inseparable_degree(None)
            Traceback (most recent call last):
            ...
            NotImplementedError: ...
        """
    def separable_degree(self):
        """
        Return the separable degree of this isogeny.

        The separable degree is the result of dividing the :meth:`degree`
        by the :meth:`inseparable_degree`.

        EXAMPLES::

            sage: E = EllipticCurve(GF(11), [5,5])
            sage: E.is_supersingular()
            False
            sage: E.scalar_multiplication(-77).separable_degree()
            539
            sage: E = EllipticCurve(GF(11), [5,0])
            sage: E.is_supersingular()
            True
            sage: E.scalar_multiplication(-77).separable_degree()
            49
        """
    def is_separable(self):
        """
        Determine whether or not this morphism is a separable isogeny.

        EXAMPLES::

            sage: E = EllipticCurve(GF(17), [0,0,0,3,0])
            sage: phi = EllipticCurveIsogeny(E,  E((0,0)))
            sage: phi.is_separable()
            True

        ::

            sage: E = EllipticCurve('11a1')
            sage: phi = EllipticCurveIsogeny(E, E.torsion_points())
            sage: phi.is_separable()
            True

        ::

            sage: E = EllipticCurve(GF(31337), [0,1])                                   # needs sage.rings.finite_rings
            sage: {f.is_separable() for f in E.automorphisms()}                         # needs sage.rings.finite_rings
            {True}

        ::

            sage: # needs sage.rings.finite_rings
            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: E = EllipticCurve(GF(7^2), [3,2])
            sage: P = E.lift_x(1)
            sage: phi = EllipticCurveHom_composite(E, P); phi
            Composite morphism of degree 7:
              From: Elliptic Curve defined by y^2 = x^3 + 3*x + 2 over Finite Field in z2 of size 7^2
              To:   Elliptic Curve defined by y^2 = x^3 + 3*x + 2 over Finite Field in z2 of size 7^2
            sage: phi.is_separable()
            True

        ::

            sage: E = EllipticCurve(GF(11), [4,4])
            sage: E.scalar_multiplication(11).is_separable()
            False
            sage: E.scalar_multiplication(-11).is_separable()
            False
            sage: E.scalar_multiplication(777).is_separable()
            True
            sage: E.scalar_multiplication(-1).is_separable()
            True
            sage: E.scalar_multiplication(77).is_separable()
            False
            sage: E.scalar_multiplication(121).is_separable()
            False

        ::

            sage: from sage.schemes.elliptic_curves.hom_frobenius import EllipticCurveHom_frobenius
            sage: E = EllipticCurve(GF(11), [1,1])
            sage: pi = EllipticCurveHom_frobenius(E)
            sage: pi.degree()
            11
            sage: pi.is_separable()
            False
            sage: pi = EllipticCurveHom_frobenius(E, 0)
            sage: pi.degree()
            1
            sage: pi.is_separable()
            True

        ::

            sage: E = EllipticCurve(GF(17), [0,0,0,3,0])
            sage: phi = E.isogeny(E((1,2)), algorithm='velusqrt')
            sage: phi.is_separable()
            True
        """
    def is_surjective(self):
        """
        Determine whether or not this morphism is surjective.

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: R.<x> = QQ[]
            sage: f = x^2 + x - 29/5
            sage: phi = EllipticCurveIsogeny(E, f)
            sage: phi.is_surjective()
            True

        ::

            sage: E = EllipticCurve(GF(7), [0,0,0,1,0])
            sage: phi = EllipticCurveIsogeny(E,  E((0,0)))
            sage: phi.is_surjective()
            True

        ::

            sage: F = GF(2^5, 'omega')
            sage: E = EllipticCurve(j=F(0))
            sage: R.<x> = F[]
            sage: phi = EllipticCurveIsogeny(E, x)
            sage: phi.is_surjective()
            True
        """
    def is_injective(self):
        """
        Determine whether or not this morphism has trivial kernel.

        The kernel is trivial if and only if this morphism is a
        purely inseparable isogeny.

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: R.<x> = QQ[]
            sage: f = x^2 + x - 29/5
            sage: phi = EllipticCurveIsogeny(E, f)
            sage: phi.is_injective()
            False
            sage: phi = EllipticCurveIsogeny(E, R(1))
            sage: phi.is_injective()
            True

        ::

            sage: F = GF(7)
            sage: E = EllipticCurve(j=F(0))
            sage: phi = EllipticCurveIsogeny(E, [ E((0,-1)), E((0,1))])
            sage: phi.is_injective()
            False
            sage: phi = EllipticCurveIsogeny(E, E(0))
            sage: phi.is_injective()
            True

        ::

            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: E = EllipticCurve([1,0])
            sage: phi = EllipticCurveHom_composite(E, E(0,0))
            sage: phi.is_injective()
            False
            sage: E = EllipticCurve_from_j(GF(3).algebraic_closure()(0))
            sage: nu = EllipticCurveHom_composite.from_factors(E.automorphisms())
            sage: nu
            Composite morphism of degree 1 = 1^12:
              From: Elliptic Curve defined by y^2 = x^3 + x
                    over Algebraic closure of Finite Field of size 3
              To:   Elliptic Curve defined by y^2 = x^3 + x
                    over Algebraic closure of Finite Field of size 3
            sage: nu.is_injective()
            True

        ::

            sage: E = EllipticCurve(GF(23), [1,0])
            sage: E.scalar_multiplication(4).is_injective()
            False
            sage: E.scalar_multiplication(5).is_injective()
            False
            sage: E.scalar_multiplication(1).is_injective()
            True
            sage: E.scalar_multiplication(-1).is_injective()
            True
            sage: E.scalar_multiplication(23).is_injective()
            True
            sage: E.scalar_multiplication(-23).is_injective()
            True
            sage: E.scalar_multiplication(0).is_injective()
            False

        ::

            sage: from sage.schemes.elliptic_curves.hom_frobenius import EllipticCurveHom_frobenius
            sage: E = EllipticCurve(GF(11), [1,1])
            sage: pi = EllipticCurveHom_frobenius(E, 5)
            sage: pi.is_injective()
            True
        """
    def is_zero(self):
        """
        Check whether this elliptic-curve morphism is the zero map.

        EXAMPLES::

            sage: E = EllipticCurve(j=GF(7)(0))
            sage: phi = EllipticCurveIsogeny(E, [E(0,1), E(0,-1)])
            sage: phi.is_zero()
            False
        """
    def __neg__(self):
        """
        Return the negative of this elliptic-curve morphism. In other
        words, return `[-1]\\circ\\varphi` where `\\varphi` is ``self``
        and `[-1]` is the negation automorphism on the codomain curve.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom import EllipticCurveHom
            sage: E = EllipticCurve(GF(1019), [5,5])
            sage: phi = E.isogeny(E.lift_x(73))
            sage: f,g = phi.rational_maps()
            sage: psi = EllipticCurveHom.__neg__(phi)
            sage: psi.rational_maps() == (f, -g)
            True
        """
    @cached_method
    def __hash__(self):
        """
        Return a hash value for this elliptic-curve morphism.

        ALGORITHM:

        Hash a tuple containing the domain, codomain, and kernel
        polynomial of this morphism. (The base field is factored
        into the computation as part of the (co)domain hashes.)

        EXAMPLES::

            sage: E = EllipticCurve(QQ, [0,0,0,1,0])
            sage: phi_v = EllipticCurveIsogeny(E, E((0,0)))
            sage: phi_k = EllipticCurveIsogeny(E, [0,1])
            sage: phi_k.__hash__() == phi_v.__hash__()
            True
            sage: E_F17 = EllipticCurve(GF(17), [0,0,0,1,1])
            sage: phi_p = EllipticCurveIsogeny(E_F17, E_F17([0,1]))
            sage: phi_p.__hash__() == phi_v.__hash__()
            False

        ::

            sage: E = EllipticCurve('49a3')
            sage: R.<X> = QQ[]
            sage: EllipticCurveIsogeny(E,X^3-13*X^2-58*X+503,check=False)
            Isogeny of degree 7 from Elliptic Curve defined by y^2 + x*y = x^3 - x^2 - 107*x + 552 over Rational Field to Elliptic Curve defined by y^2 + x*y = x^3 - x^2 - 5252*x - 178837 over Rational Field
        """
    def as_morphism(self):
        """
        Return ``self`` as a morphism of projective schemes.

        EXAMPLES::

            sage: k = GF(11)
            sage: E = EllipticCurve(k, [1,1])
            sage: Q = E(6,5)
            sage: phi = E.isogeny(Q)
            sage: mor = phi.as_morphism()
            sage: mor.domain() == E
            True
            sage: mor.codomain() == phi.codomain()
            True
            sage: mor(Q) == phi(Q)
            True

        TESTS::

            sage: mor(0*Q)
            (0 : 1 : 0)
            sage: mor(1*Q)
            (0 : 1 : 0)
        """
    def matrix_on_subgroup(self, domain_gens, codomain_gens=None):
        """
        Return the matrix by which this isogeny acts on the
        `n`-torsion subgroup with respect to the given bases.

        INPUT:

        - ``domain_gens`` -- basis `(P,Q)` of some `n`-torsion
          subgroup on the domain of this elliptic-curve morphism

        - ``codomain_gens`` -- basis `(R,S)` of the `n`-torsion
          on the codomain of this morphism, or (default) ``None``
          if ``self`` is an endomorphism

        OUTPUT:

        A `2\\times 2` matrix `M` over `\\ZZ/n`, such that the
        image of any point `[a]P + [b]Q` under this morphism
        equals `[c]R + [d]S` where `(c\\ d)^T = (a\\ b) M`.

        EXAMPLES::

            sage: F.<i> = GF(419^2, modulus=[1,0,1])
            sage: E = EllipticCurve(F, [1,0])
            sage: P = E(3, 176*i)
            sage: Q = E(i+7, 67*i+48)
            sage: P.weil_pairing(Q, 420).multiplicative_order()
            420
            sage: iota = E.automorphisms()[2]; iota
            Elliptic-curve endomorphism of Elliptic Curve defined by y^2 = x^3 + x over Finite Field in i of size 419^2
              Via:  (u,r,s,t) = (i, 0, 0, 0)
            sage: iota^2 == E.scalar_multiplication(-1)
            True
            sage: mat = iota.matrix_on_subgroup((P,Q)); mat
            [301 386]
            [ 83 119]
            sage: mat.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Ring of integers modulo 420
            sage: iota(P) == 301*P + 386*Q
            True
            sage: iota(Q) == 83*P + 119*Q
            True
            sage: a,b = 123, 456
            sage: c,d = vector((a,b)) * mat; (c,d)
            (111, 102)
            sage: iota(a*P + b*Q) == c*P + d*Q
            True

        One important application of this is to compute generators of
        the kernel subgroup of an isogeny, when the `n`-torsion subgroup
        containing the kernel is accessible::

            sage: K = E(83*i-16, 9*i-147)
            sage: K.order()
            7
            sage: phi = E.isogeny(K)
            sage: R,S = phi.codomain().gens()
            sage: mat = phi.matrix_on_subgroup((P,Q), (R,S))
            sage: mat  # random -- depends on R,S
            [124 263]
            [115 141]
            sage: kermat = mat.left_kernel_matrix(); kermat
            [300  60]
            sage: ker = [ZZ(v[0])*P + ZZ(v[1])*Q for v in kermat]
            sage: {phi(T) for T in ker}
            {(0 : 1 : 0)}
            sage: phi == E.isogeny(ker)
            True

        We can also compute the matrix of a Frobenius endomorphism
        (:class:`~sage.schemes.elliptic_curves.hom_frobenius.EllipticCurveHom_frobenius`)
        on a large enough subgroup to verify point-counting results::

            sage: F.<a> = GF((101, 36))
            sage: E = EllipticCurve(GF(101), [1,1])
            sage: EE = E.change_ring(F)
            sage: P,Q = EE.torsion_basis(37)
            sage: pi = EE.frobenius_isogeny()
            sage: M = pi.matrix_on_subgroup((P,Q))
            sage: M.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Ring of integers modulo 37
            sage: M.trace()
            34
            sage: E.trace_of_frobenius()
            -3

        .. SEEALSO::

            To compute a basis of the `n`-torsion, you may use
            :meth:`~sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field.torsion_basis`.
        """
    def __truediv__(self, other):
        """
        Internal helper function to provide the `\\phi/d` syntax
        for dividing an isogeny by an integer.

        To divide an isogeny by another isogeny (on the left or
        right), use :meth:`divide_left` or :meth:`divide_right`.

        EXAMPLES::

            sage: E = EllipticCurve(GF(419), [-1, 0])
            sage: (E.frobenius_isogeny() + 1) / 2
            Fractional elliptic-curve morphism of degree 105:
              Numerator:   Sum morphism:
                From: Elliptic Curve defined by y^2 = x^3 + 418*x over Finite Field of size 419
                To:   Elliptic Curve defined by y^2 = x^3 + 418*x over Finite Field of size 419
                Via:  (Frobenius endomorphism of degree 419:
                         From: Elliptic Curve defined by y^2 = x^3 + 418*x over Finite Field of size 419
                         To:   Elliptic Curve defined by y^2 = x^3 + 418*x over Finite Field of size 419,
                       Scalar-multiplication endomorphism [1]
                         of Elliptic Curve defined by y^2 = x^3 + 418*x over Finite Field of size 419)
              Denominator: 2
        """
    def divide_left(self, psi):
        """
        Return an isogeny `\\chi` such that `\\psi\\circ\\chi = \\varphi`,
        where `\\varphi` is this isogeny, if such a `\\chi` exists.

        EXAMPLES::

            sage: E = EllipticCurve('54.b2')
            sage: K = next(T for T in E.torsion_points() if T.order() == 9)
            sage: phi, psi = E.isogeny(K).factors()
            sage: chain = psi * phi; chain
            Composite morphism of degree 9 = 3^2:
              From: Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - 14*x + 29 over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - 2324*x - 43091 over Rational Field
            sage: chain.divide_right(phi)
            Fractional elliptic-curve morphism of degree 3:
              Numerator:   Composite morphism of degree 27 = 3^3:
              From: Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 + 106*x - 323 over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - 2324*x - 43091 over Rational Field
              Denominator: 3
            sage: chain.divide_right(phi) == psi
            True
        """
    def divide_right(self, psi):
        """
        Return an isogeny `\\chi` such that `\\chi\\circ\\psi = \\varphi`,
        where `\\varphi` is this isogeny, if such a `\\chi` exists.

        EXAMPLES::

            sage: E = EllipticCurve('54.b2')
            sage: K = next(T for T in E.torsion_points() if T.order() == 9)
            sage: phi, psi = E.isogeny(K).factors()
            sage: chain = psi * phi; chain
            Composite morphism of degree 9 = 3^2:
              From: Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - 14*x + 29 over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - 2324*x - 43091 over Rational Field
            sage: chain.divide_left(psi)
            Fractional elliptic-curve morphism of degree 3:
              Numerator:   Composite morphism of degree 27 = 3^3:
              From: Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 - 14*x + 29 over Rational Field
              To:   Elliptic Curve defined by y^2 + x*y + y = x^3 - x^2 + 106*x - 323 over Rational Field
              Denominator: 3
            sage: chain.divide_left(psi) == phi
            True
        """

def compare_via_evaluation(left, right):
    """
    Test if two elliptic-curve morphisms are equal by evaluating
    them at enough points.

    INPUT:

    - ``left``, ``right`` -- :class:`EllipticCurveHom` objects

    ALGORITHM:

    We use the fact that two isogenies of equal degree `d` must be
    the same if and only if they behave identically on more than
    `4d` points. (It suffices to check this on a few points that
    generate a large enough subgroup.)

    If the domain curve does not have sufficiently many rational
    points, the base field is extended first: Taking an extension
    of degree `O(\\log(d))` suffices.

    EXAMPLES::

        sage: E = EllipticCurve(GF(83), [1,0])
        sage: phi = E.isogeny(12*E.0, model='montgomery'); phi
        Isogeny of degree 7 from Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 83 to Elliptic Curve defined by y^2 = x^3 + 70*x^2 + x over Finite Field of size 83
        sage: psi = phi.dual(); psi
        Isogeny of degree 7 from Elliptic Curve defined by y^2 = x^3 + 70*x^2 + x over Finite Field of size 83 to Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 83
        sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
        sage: mu = EllipticCurveHom_composite.from_factors([phi, psi])
        sage: from sage.schemes.elliptic_curves.hom import compare_via_evaluation
        sage: compare_via_evaluation(mu, E.scalar_multiplication(7))
        True

    .. SEEALSO::

        - :meth:`sage.schemes.elliptic_curves.hom_composite.EllipticCurveHom_composite._richcmp_`
    """
def find_post_isomorphism(phi, psi):
    """
    Given two isogenies `\\phi: E\\to E'` and `\\psi: E\\to E''`
    which are equal up to post-isomorphism defined over the
    same field, find that isomorphism.

    In other words, this function computes an isomorphism
    `\\alpha: E'\\to E''` such that `\\alpha\\circ\\phi = \\psi`.

    ALGORITHM:

    Start with a list of all isomorphisms `E'\\to E''`. Then
    repeatedly evaluate `\\phi` and `\\psi` at random points
    `P` to filter the list for isomorphisms `\\alpha` with
    `\\alpha(\\phi(P)) = \\psi(P)`. Once only one candidate is
    left, return it. Periodically extend the base field to
    avoid getting stuck (say, if all candidate isomorphisms
    act the same on all rational points).

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.hom import find_post_isomorphism
        sage: E = EllipticCurve(GF(7^2), [1,0])
        sage: f = E.scalar_multiplication(1)
        sage: g = choice(E.automorphisms())
        sage: find_post_isomorphism(f, g) == g
        True

    ::

        sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
        sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
        sage: x = polygen(ZZ, 'x')
        sage: F.<i> = GF(883^2, modulus=x^2+1)
        sage: E = EllipticCurve(F, [1,0])
        sage: P = E.lift_x(117)
        sage: Q = E.lift_x(774)
        sage: w = WeierstrassIsomorphism(E, [i,0,0,0])
        sage: phi = EllipticCurveHom_composite(E, [P,w(Q)]) * w
        sage: psi = EllipticCurveHom_composite(E, [Q,w(P)])
        sage: phi.kernel_polynomial() == psi.kernel_polynomial()
        True
        sage: find_post_isomorphism(phi, psi)
        Elliptic-curve morphism:
          From: Elliptic Curve defined by y^2 = x^3 + 320*x + 482 over Finite Field in i of size 883^2
          To:   Elliptic Curve defined by y^2 = x^3 + 320*x + 401 over Finite Field in i of size 883^2
          Via:  (u,r,s,t) = (882*i, 0, 0, 0)
    """
def compute_trace_generic(phi):
    """
    Compute the trace of the given elliptic-curve endomorphism.

    ALGORITHM: Simple variant of Schoof's algorithm.
    For enough small primes `\\ell`, we find an order-`\\ell` point `P`
    on `E` and use a discrete-logarithm calculation to find the unique
    scalar `t_\\ell \\in \\{0,...,\\ell-1\\}` such that
    `\\varphi^2(P)+[\\deg(\\varphi)]P = [t_\\ell]\\varphi(P)`.
    Then `t_\\ell` equals the trace of `\\varphi` modulo `\\ell`, which
    can therefore be recovered using the Chinese remainder theorem.

    EXAMPLES:

    It works over finite fields::

        sage: from sage.schemes.elliptic_curves.hom import compute_trace_generic
        sage: E = EllipticCurve(GF(31337), [1,1])
        sage: compute_trace_generic(E.frobenius_endomorphism())
        314

    It works over `\\QQ`::

        sage: from sage.schemes.elliptic_curves.hom import compute_trace_generic
        sage: E = EllipticCurve(QQ, [1,2,3,4,5])
        sage: dbl = E.scalar_multiplication(2)
        sage: compute_trace_generic(dbl)
        4

    It works over number fields (for a CM curve)::

        sage: from sage.schemes.elliptic_curves.hom import compute_trace_generic
        sage: x = polygen(QQ)
        sage: K.<t> = NumberField(5*x^2 - 2*x + 1)
        sage: E = EllipticCurve(K, [1,0])
        sage: phi = E.isogeny([t,0,1], codomain=E)  # phi = 2 + i
        sage: compute_trace_generic(phi)
        4

    TESTS:

    Check on random elliptic curves over finite fields that
    the result for Frobenius matches
    :meth:`~sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field.trace_of_frobenius`::

        sage: from sage.schemes.elliptic_curves.hom import compute_trace_generic
        sage: p = random_prime(10^3)
        sage: e = randrange(1, ceil(log(10^5,p)))
        sage: F.<t> = GF((p, e))
        sage: E = choice(EllipticCurve(j=F.random_element()).twists())
        sage: pi = E.frobenius_endomorphism()
        sage: compute_trace_generic(pi) == E.trace_of_frobenius()
        True

    Check that the nonexistence of `p`-torsion for supersingular curves
    does not cause trouble::

        sage: from sage.schemes.elliptic_curves.hom import compute_trace_generic
        sage: E = EllipticCurve(GF(5), [0,1])
        sage: E.division_polynomial(5)
        4
        sage: m7 = E.scalar_multiplication(7)
        sage: compute_trace_generic(-m7)
        -14
    """
