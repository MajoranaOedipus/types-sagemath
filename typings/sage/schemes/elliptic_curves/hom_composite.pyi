from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import prod as prod
from sage.misc.cachefunc import cached_method as cached_method
from sage.schemes.elliptic_curves.ell_curve_isogeny import EllipticCurveIsogeny as EllipticCurveIsogeny
from sage.schemes.elliptic_curves.ell_generic import EllipticCurve_generic as EllipticCurve_generic
from sage.schemes.elliptic_curves.hom import EllipticCurveHom as EllipticCurveHom, compare_via_evaluation as compare_via_evaluation
from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism as WeierstrassIsomorphism, identity_morphism as identity_morphism
from sage.structure.richcmp import op_EQ as op_EQ
from sage.structure.sequence import Sequence as Sequence

class EllipticCurveHom_composite(EllipticCurveHom):
    def __init__(self, E, kernel, codomain=None, model=None, velu_sqrt_bound=None) -> None:
        """
        Construct a composite isogeny with given kernel (and optionally,
        prescribed codomain curve). The isogeny is decomposed into steps
        of prime degree.

        The ``codomain`` and ``model`` parameters have the same meaning
        as for :class:`EllipticCurveIsogeny`.

        The optional parameter ``velu_sqrt_bound`` prescribes the point
        in which the computation of a single isogeny should be performed
        using square root Velu instead of simple Velu. If not provided,
        the system default is used (see
        :class:`EllipticCurve_field.isogeny` for a more detailed
        discussion.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: E = EllipticCurve(GF(419), [1,0])                                     # needs sage.rings.finite_rings
            sage: EllipticCurveHom_composite(E, E.lift_x(23))                           # needs sage.rings.finite_rings
            Composite morphism of degree 105 = 3*5*7:
              From: Elliptic Curve defined by y^2 = x^3 + x
                    over Finite Field of size 419
              To:   Elliptic Curve defined by y^2 = x^3 + 373*x + 126
                    over Finite Field of size 419

        The given kernel generators need not be independent::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^2 - x - 5)
            sage: E = EllipticCurve('210.b6').change_ring(K)
            sage: E.torsion_subgroup()
            Torsion Subgroup isomorphic to Z/12 + Z/2 associated to the Elliptic Curve
             defined by y^2 + x*y + y = x^3 + (-578)*x + 2756
              over Number Field in a with defining polynomial x^2 - x - 5
            sage: EllipticCurveHom_composite(E, E.torsion_points())
            Composite morphism of degree 24 = 2^3*3:
              From: Elliptic Curve defined by y^2 + x*y + y = x^3 + (-578)*x + 2756
                    over Number Field in a with defining polynomial x^2 - x - 5
              To:   Elliptic Curve defined by
                    y^2 + x*y + y = x^3 + (-89915533/16)*x + (-328200928141/64)
                    over Number Field in a with defining polynomial x^2 - x - 5

        TESTS::

            sage: E = EllipticCurve(GF(19), [1,0])
            sage: P = E.random_point()
            sage: psi = EllipticCurveHom_composite(E, P)
            sage: psi   # random
            Composite morphism of degree 10 = 2*5:
              From: Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 19
              To:   Elliptic Curve defined by y^2 = x^3 + 14*x over Finite Field of size 19

        ::

            sage: EllipticCurveHom_composite(E, E.lift_x(3), codomain=E)
            Composite morphism of degree 20 = 2^2*5:
              From: Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 19
              To:   Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 19

        ::

            sage: # needs sage.rings.finite_rings
            sage: E = EllipticCurve(GF((2^127-1)^2), [1,0])
            sage: K = 2^30 * E.random_point()
            sage: psi = EllipticCurveHom_composite(E, K, model='montgomery')
            sage: psi.codomain().a_invariants()
            (0, ..., 0, 1, 0)
        """
    @classmethod
    def from_factors(cls, maps, E=None, strict: bool = True):
        """
        This method constructs a :class:`EllipticCurveHom_composite`
        object encapsulating a given sequence of compatible isogenies.

        The isogenies are composed in left-to-right order, i.e., the
        resulting composite map equals `f_{n-1} \\circ \\dots \\circ f_0`
        where `f_i` denotes ``maps[i]``.

        INPUT:

        - ``maps`` -- sequence of :class:`EllipticCurveHom` objects
        - ``E`` -- (optional) the domain elliptic curve
        - ``strict`` -- boolean (default: ``True``); if ``True``,
          always return an :class:`EllipticCurveHom_composite` object,
          else may return another :class:`EllipticCurveHom` type

        OUTPUT: the composite of ``maps``

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: E = EllipticCurve(GF(43), [1,0])
            sage: P, = E.gens()
            sage: phi = EllipticCurveHom_composite(E, P)
            sage: psi = EllipticCurveHom_composite.from_factors(phi.factors())
            sage: psi == phi
            True

        TESTS::

            sage: E = EllipticCurve('4730k1')
            sage: EllipticCurveHom_composite.from_factors([], E) == E.scalar_multiplication(1)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: E = EllipticCurve(GF(419), [1,0])
            sage: P, = E.gens()
            sage: phi = EllipticCurveHom_composite(E, P)
            sage: EllipticCurveHom_composite.from_factors(phi.factors()) == phi
            True
        """
    def factors(self):
        """
        Return the factors of this composite isogeny as a tuple.

        The isogenies are returned in left-to-right order, i.e.,
        the returned tuple `(f_1,...,f_n)` corresponds to the map
        `f_n \\circ \\dots \\circ f_1`.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: E = EllipticCurve(GF(43), [1,0])
            sage: P, = E.gens()
            sage: phi = EllipticCurveHom_composite(E, P)
            sage: phi.factors()
            (Isogeny of degree 2
              from Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 43
                to Elliptic Curve defined by y^2 = x^3 + 39*x over Finite Field of size 43,
             Isogeny of degree 2
              from Elliptic Curve defined by y^2 = x^3 + 39*x over Finite Field of size 43
                to Elliptic Curve defined by y^2 = x^3 + 42*x + 26 over Finite Field of size 43,
             Isogeny of degree 11
              from Elliptic Curve defined by y^2 = x^3 + 42*x + 26 over Finite Field of size 43
                to Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 43)
        """
    def rational_maps(self):
        """
        Return the pair of explicit rational maps defining this composite
        isogeny.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: E = EllipticCurve(GF(65537), [1,2,3,4,5])
            sage: P = E.lift_x(7321)
            sage: phi = EllipticCurveHom_composite(E, P)
            sage: phi.rational_maps()
            ((x^9 + 27463*x^8 + 21204*x^7 - 5750*x^6 + 1610*x^5 + 14440*x^4
              + 26605*x^3 - 15569*x^2 - 3341*x + 1267)/(x^8 + 27463*x^7 + 26871*x^6
              + 5999*x^5 - 20194*x^4 - 6310*x^3 + 24366*x^2 - 20905*x - 13867),
             (x^12*y + 8426*x^11*y + 5667*x^11 + 27612*x^10*y + 26124*x^10 + 9688*x^9*y
              - 22715*x^9 + 19864*x^8*y + 498*x^8 + 22466*x^7*y - 14036*x^7 + 8070*x^6*y
              + 19955*x^6 - 20765*x^5*y - 12481*x^5 + 12672*x^4*y + 24142*x^4 - 23695*x^3*y
              + 26667*x^3 + 23780*x^2*y + 17864*x^2 + 15053*x*y - 30118*x + 17539*y
              - 23609)/(x^12 + 8426*x^11 + 21945*x^10 - 22587*x^9 + 22094*x^8 + 14603*x^7
              - 26255*x^6 + 11171*x^5 - 16508*x^4 - 14435*x^3 - 2170*x^2 + 29081*x - 19009))

        TESTS::

            sage: f = phi.codomain().defining_polynomial()                              # needs sage.rings.finite_rings
            sage: g = E.defining_polynomial().subs({2:1})                               # needs sage.rings.finite_rings
            sage: f(*phi.rational_maps(), 1) % g                                        # needs sage.rings.finite_rings
            0

        ::

            sage: phi.rational_maps()[0].parent()                                       # needs sage.rings.finite_rings
            Fraction Field of
             Multivariate Polynomial Ring in x, y over Finite Field of size 65537
            sage: phi.rational_maps()[1].parent()                                       # needs sage.rings.finite_rings
            Fraction Field of
             Multivariate Polynomial Ring in x, y over Finite Field of size 65537
        """
    def x_rational_map(self):
        """
        Return the `x`-coordinate rational map of this composite isogeny.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: E = EllipticCurve(GF(65537), [1,2,3,4,5])
            sage: P = E.lift_x(7321)
            sage: phi = EllipticCurveHom_composite(E, P)
            sage: phi.x_rational_map() == phi.rational_maps()[0]
            True

        TESTS::

            sage: phi.x_rational_map().parent()                                         # needs sage.rings.finite_rings
            Fraction Field of Univariate Polynomial Ring in x
             over Finite Field of size 65537
        """
    def kernel_polynomial(self):
        """
        Return the kernel polynomial of this composite isogeny.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: E = EllipticCurve(GF(65537), [1,2,3,4,5])
            sage: P = E.lift_x(7321)
            sage: phi = EllipticCurveHom_composite(E, P); phi
            Composite morphism of degree 9 = 3^2:
              From: Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5
                    over Finite Field of size 65537
              To:   Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 28339*x + 59518
                    over Finite Field of size 65537
            sage: phi.kernel_polynomial()
            x^4 + 46500*x^3 + 19556*x^2 + 7643*x + 15952
        """
    @cached_method
    def dual(self):
        """
        Return the dual of this composite isogeny.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: E = EllipticCurve(GF(65537), [1,2,3,4,5])
            sage: P = E.lift_x(7321)
            sage: phi = EllipticCurveHom_composite(E, P); phi
            Composite morphism of degree 9 = 3^2:
              From: Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5
                    over Finite Field of size 65537
              To:   Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 28339*x + 59518
                    over Finite Field of size 65537
            sage: psi = phi.dual(); psi
            Composite morphism of degree 9 = 3^2:
              From: Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 28339*x + 59518
                    over Finite Field of size 65537
              To:   Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5
                    over Finite Field of size 65537
            sage: psi * phi == phi.domain().scalar_multiplication(phi.degree())
            True
            sage: phi * psi == psi.domain().scalar_multiplication(psi.degree())
            True
        """
    def formal(self, prec: int = 20):
        """
        Return the formal isogeny corresponding to this composite
        isogeny as a power series in the variable `t=-x/y` on the
        domain curve.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: E = EllipticCurve(GF(65537), [1,2,3,4,5])
            sage: P = E.lift_x(7321)
            sage: phi = EllipticCurveHom_composite(E, P)
            sage: phi.formal()
            t + 54203*t^5 + 48536*t^6 + 40698*t^7 + 37808*t^8 + 21111*t^9 + 42381*t^10
             + 46688*t^11 + 657*t^12 + 38916*t^13 + 62261*t^14 + 59707*t^15
             + 30767*t^16 + 7248*t^17 + 60287*t^18 + 50451*t^19 + 38305*t^20
             + 12312*t^21 + 31329*t^22 + O(t^23)
            sage: (phi.dual() * phi).formal(prec=5)
            9*t + 65501*t^2 + 65141*t^3 + 59183*t^4 + 21491*t^5 + 8957*t^6
             + 999*t^7 + O(t^8)
        """
    def scaling_factor(self):
        """
        Return the Weierstrass scaling factor associated to this
        composite morphism.

        The scaling factor is the constant `u` (in the base field)
        such that `\\varphi^* \\omega_2 = u \\omega_1`, where
        `\\varphi: E_1\\to E_2` is this morphism and `\\omega_i` are
        the standard Weierstrass differentials on `E_i` defined by
        `\\mathrm dx/(2y+a_1x+a_3)`.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: from sage.schemes.elliptic_curves.weierstrass_morphism import WeierstrassIsomorphism
            sage: E = EllipticCurve(GF(65537), [1,2,3,4,5])
            sage: P = E.lift_x(7321)
            sage: phi = EllipticCurveHom_composite(E, P)
            sage: phi = WeierstrassIsomorphism(phi.codomain(), [7,8,9,10]) * phi
            sage: phi.formal()
            7*t + 65474*t^2 + 511*t^3 + 61316*t^4 + 20548*t^5 + 45511*t^6 + 37285*t^7
             + 48414*t^8 + 9022*t^9 + 24025*t^10 + 35986*t^11 + 55397*t^12 + 25199*t^13
             + 18744*t^14 + 46142*t^15 + 9078*t^16 + 18030*t^17 + 47599*t^18
             + 12158*t^19 + 50630*t^20 + 56449*t^21 + 43320*t^22 + O(t^23)
            sage: phi.scaling_factor()
            7

        ALGORITHM: The scaling factor is multiplicative under
        composition, so we return the product of the individual
        scaling factors associated to each factor.
        """
    def inseparable_degree(self):
        """
        Return the inseparable degree of this morphism.

        Like the degree, the inseparable degree is multiplicative
        under composition, so this method returns the product of
        the inseparable degrees of the factors.

        EXAMPLES::

            sage: E = EllipticCurve(j=GF(11^5).random_element())
            sage: phi = E.frobenius_isogeny(2) * E.scalar_multiplication(77)
            sage: type(phi)
            <class 'sage.schemes.elliptic_curves.hom_composite.EllipticCurveHom_composite'>
            sage: phi.inseparable_degree()
            1331
        """
    def kernel_points(self) -> Generator[Incomplete, Incomplete]:
        """
        Return an iterator over the points in the kernel of this
        elliptic-curve morphism.

        EXAMPLES::

            sage: E.<P, Q> = EllipticCurve(GF(5^2), [1, 2, 3, 3, 1])
            sage: f = E.isogeny([P*3, Q*3])
            sage: f
            Composite morphism of degree 4 = 2^2:
              From: Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 3*x + 1 over Finite Field in z2 of size 5^2
              To:   Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 3*x + 3 over Finite Field in z2 of size 5^2
            sage: set(f.kernel_points())
            {(0 : 1 : 0), (4 : 4 : 1), (2*z2 + 4 : 4*z2 + 4 : 1), (3*z2 + 1 : z2 + 3 : 1)}
        """
    def inverse_image(self, Q, /, *, all: bool = False):
        '''
        Return an arbitrary element ``P`` in the domain such that
        ``self(P) == Q``, or raise ``ValueError`` if no such
        element exists.

        INPUT:

        - ``Q`` -- a point
        - ``all`` -- (boolean) if ``True``, returns an iterator over all points
          in the inverse image

        EXAMPLES::

            sage: E.<P, Q> = EllipticCurve(GF(5^2), [1, 2, 3, 3, 1])
            sage: f = E.isogeny([P*3, Q*3])
            sage: f
            Composite morphism of degree 4 = 2^2:
              From: Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 3*x + 1 over Finite Field in z2 of size 5^2
              To:   Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 3*x + 3 over Finite Field in z2 of size 5^2
            sage: f(f.inverse_image(f(Q))) == f(Q)
            True
            sage: E.scalar_multiplication(-1).inverse_image(P) == -P
            True
            sage: f.inverse_image(f.codomain().0)
            Traceback (most recent call last):
            ...
            ValueError...
            sage: len(list(f.inverse_image(f(Q), all=True)))
            4

        Test a large example. It should finish in a few seconds::

            sage: p = 3 * 2^143 - 1
            sage: GF(p^2).inject_variables()
            Defining z2
            sage: E = EllipticCurve(GF(p^2), [1,0])
            sage: P = E.lift_x(31415926535897932384626433832795028841971 - z2)
            sage: f = E.isogeny(P, algorithm="factored")
            sage: Q = f(E.lift_x(2718281828459045235360287471352662497757 - z2)); Q
            (14253459515090351074737629944491750308703143*z2 + 17548601963968266930680314841240982076784493 : ... : 1)
            sage: f.inverse_image(Q)  # long time
            (...)

        TESTS:

        Normally, a :class:`EllipticCurveHom_composite` has ``len(self._phis) > 1``,
        but if :meth:`from_factors` is called with ``strict=True``, or if the user
        constructs a :class:`EllipticCurveHom_composite` object directly, then it is
        possible to violate this condition. We test for this case::

            sage: E.<P> = EllipticCurve(GF(5), [1, 2])
            sage: from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite
            sage: f = EllipticCurveHom_composite(E, P*2); f
            Composite morphism of degree 2:
              From: Elliptic Curve defined by y^2 = x^3 + x + 2 over Finite Field of size 5
              To:   Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 5
            sage: len(f._phis)
            1
            sage: f(f.inverse_image(f(P))) == f(P)
            True
            sage: set(f.inverse_image(f(P), all=True))
            {(1 : 2 : 1), (1 : 3 : 1)}

        The current implementation guarantees :attr:`_phis` is not empty::

            sage: f = EllipticCurveHom_composite.from_factors((), E); f
            Composite morphism of degree 1:
              From: Elliptic Curve defined by y^2 = x^3 + x + 2 over Finite Field of size 5
              To:   Elliptic Curve defined by y^2 = x^3 + x + 2 over Finite Field of size 5
            sage: len(f._phis)
            1
            sage: f.inverse_image(P) == P
            True
        '''
