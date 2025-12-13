from .constructor import EllipticCurve as EllipticCurve
from .ell_finite_field import EllipticCurve_finite_field as EllipticCurve_finite_field
from .hom import EllipticCurveHom as EllipticCurveHom, compare_via_evaluation as compare_via_evaluation
from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.misc_c import prod as prod
from sage.rings.generic import ProductTree as ProductTree, prod_with_derivative as prod_with_derivative
from sage.rings.integer import Integer as Integer
from sage.structure.richcmp import op_EQ as op_EQ
from sage.structure.sequence import Sequence as Sequence

class _VeluBoundObj:
    """
    Helper object to define the point in which isogeny
    computation should start using square-roor Velu formulae
    instead of Velu.

    EXAMPLES ::

        sage: from sage.schemes.elliptic_curves.hom_velusqrt import _velu_sqrt_bound
        sage: _velu_sqrt_bound.get()
        1000
        sage: _velu_sqrt_bound.set(50)
        sage: _velu_sqrt_bound.get()
        50
    """
    bound: Incomplete
    def __init__(self) -> None: ...
    def set(self, b) -> None: ...
    def get(self): ...

class FastEllipticPolynomial:
    """
    A class to represent and evaluate an *elliptic polynomial*,
    and optionally its derivative, in essentially square-root time.

    The elliptic polynomials computed by this class are of the form

    .. MATH::

        h_S(Z) = \\prod_{i\\in S} (Z - x(Q + [i]P))

    where `P` is a point of odd order `n \\geq 5` and `Q` is either ``None``,
    in which case it is assumed to be `\\infty`, or an arbitrary point which is
    not a multiple of `P`.

    The index set `S` is chosen as follows:

    - If `Q` is given, then `S = \\{0,1,2,3,...,n-1\\}`.

    - If `Q` is omitted, then `S = \\{1,3,5,...,n-2\\}`. Note that in this case,
      `h_{\\{1,2,3,...,n-1\\}}` can be computed as `h_S^2` since `n` is odd.

    INPUT:

    - ``E`` -- an elliptic curve in short Weierstraß form
    - ``n`` -- an odd integer `\\geq 5`
    - ``P`` -- a point on `E`
    - ``Q`` -- a point on `E`, or ``None``

    ALGORITHM: [BDLS2020]_, Algorithm 2

    .. NOTE::

        Currently only implemented for short Weierstraß curves.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.hom_velusqrt import FastEllipticPolynomial
        sage: E = EllipticCurve(GF(71), [5,5])
        sage: P = E(4, 35)
        sage: hP = FastEllipticPolynomial(E, P.order(), P); hP
        Fast elliptic polynomial prod(Z - x(i*P) for i in range(1,n,2)) with n = 19, P = (4 : 35 : 1)
        sage: hP(7)
        19
        sage: prod(7 - (i*P).x() for i in range(1,P.order(),2))
        19

    Passing `Q` changes the index set::

        sage: Q = E(0, 17)
        sage: hPQ = FastEllipticPolynomial(E, P.order(), P, Q)
        sage: hPQ(7)
        58
        sage: prod(7 - (Q+i*P).x() for i in range(P.order()))
        58

    The call syntax has an optional keyword argument ``derivative``, which
    will make the function return the pair `(h_S(\\alpha), h_S'(\\alpha))`
    instead of just `h_S(\\alpha)`::

        sage: hP(7, derivative=True)
        (19, 15)
        sage: R.<Z> = E.base_field()[]
        sage: HP = prod(Z - (i*P).x() for i in range(1,P.order(),2))
        sage: HP
        Z^9 + 16*Z^8 + 57*Z^7 + 6*Z^6 + 45*Z^5 + 31*Z^4 + 46*Z^3 + 10*Z^2 + 28*Z + 41
        sage: HP(7)
        19
        sage: HP.derivative()(7)
        15

    ::

        sage: hPQ(7, derivative=True)
        (58, 62)
        sage: R.<Z> = E.base_field()[]
        sage: HPQ = prod(Z - (Q+i*P).x() for i in range(P.order()))
        sage: HPQ
        Z^19 + 53*Z^18 + 67*Z^17 + 39*Z^16 + 56*Z^15 + 32*Z^14 + 44*Z^13 + 6*Z^12 + 27*Z^11 + 29*Z^10 + 38*Z^9 + 48*Z^8 + 38*Z^7 + 43*Z^6 + 21*Z^5 + 25*Z^4 + 33*Z^3 + 49*Z^2 + 60*Z
        sage: HPQ(7)
        58
        sage: HPQ.derivative()(7)
        62

    The input can be an element of any algebra over the base ring::

        sage: R.<T> = GF(71)[]
        sage: S.<t> = R.quotient(T^2)
        sage: hP(7 + t)
        15*t + 19
    """
    base: Incomplete
    hItree: Incomplete
    EJparts: Incomplete
    DeltaIJ: Incomplete
    hK: Incomplete
    dhK: Incomplete
    def __init__(self, E, n, P, Q=None) -> None:
        """
        Initialize this elliptic polynomial and precompute some
        input-independent data required for evaluation.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_velusqrt import FastEllipticPolynomial
            sage: E = EllipticCurve(GF(71), [5,5])
            sage: P = E(0, 17)
            sage: FastEllipticPolynomial(E, P.order(), P)
            Fast elliptic polynomial prod(Z - x(i*P) for i in range(1,n,2)) with n = 57, P = (0 : 17 : 1)
        """
    def __call__(self, alpha, *, derivative: bool = False):
        """
        Evaluate this elliptic polynomial at a point `\\alpha`,
        and if ``derivative`` is set to ``True`` also return
        the evaluation of the derivative at `\\alpha`.

        INPUT:

        - ``alpha`` -- an element of any algebra over the base ring
        - ``derivative`` -- boolean (default: ``False``)

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_velusqrt import FastEllipticPolynomial
            sage: E = EllipticCurve(GF(71), [5,5])
            sage: P = E(4, 35)
            sage: hP = FastEllipticPolynomial(E, P.order(), P); hP
            Fast elliptic polynomial prod(Z - x(i*P) for i in range(1,n,2)) with n = 19, P = (4 : 35 : 1)
            sage: hP(7)
            19
            sage: hP(7, derivative=True)
            (19, 15)
        """

class EllipticCurveHom_velusqrt(EllipticCurveHom):
    """
    This class implements separable odd-degree isogenies of elliptic
    curves over finite fields using the square-root Vélu algorithm.

    The complexity is `\\tilde O(\\sqrt{\\ell})` base-field operations,
    where `\\ell` is the degree.

    REFERENCES: [BDLS2020]_

    INPUT:

    - ``E`` -- an elliptic curve over a finite field
    - ``P`` -- a point on `E` of odd order `\\geq 9`
    - ``codomain`` -- codomain elliptic curve (optional)
    - ``model`` -- string (optional); input to
      :meth:`~sage.schemes.elliptic_curves.ell_field.compute_model`
    - ``Q`` -- a point on `E` outside `\\langle P\\rangle`, or ``None``

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.hom_velusqrt import EllipticCurveHom_velusqrt
        sage: F.<t> = GF(10009^3)
        sage: E = EllipticCurve(F, [t,t])
        sage: K = E(2154*t^2 + 5711*t + 2899, 7340*t^2 + 4653*t + 6935)
        sage: phi = EllipticCurveHom_velusqrt(E, K); phi
        Elliptic-curve isogeny (using square-root Vélu) of degree 601:
          From: Elliptic Curve defined by y^2 = x^3 + t*x + t over Finite Field in t of size 10009^3
          To:   Elliptic Curve defined by y^2 = x^3 + (263*t^2+3173*t+4759)*x + (3898*t^2+6111*t+9443) over Finite Field in t of size 10009^3
        sage: phi(K)
        (0 : 1 : 0)
        sage: P = E(2, 3163*t^2 + 7293*t + 5999)
        sage: phi(P)
        (6085*t^2 + 855*t + 8720 : 8078*t^2 + 9889*t + 6030 : 1)
        sage: Q = E(6, 5575*t^2 + 6607*t + 9991)
        sage: phi(Q)
        (626*t^2 + 9749*t + 1291 : 5931*t^2 + 8549*t + 3111 : 1)
        sage: phi(P + Q)
        (983*t^2 + 4894*t + 4072 : 5047*t^2 + 9325*t + 336 : 1)
        sage: phi(P) + phi(Q)
        (983*t^2 + 4894*t + 4072 : 5047*t^2 + 9325*t + 336 : 1)

    TESTS:

    Check on a random example that the isogeny is a well-defined
    group homomorphism with the correct kernel::

        sage: from sage.schemes.elliptic_curves.hom_velusqrt import _random_example_for_testing
        sage: E, K = _random_example_for_testing()
        sage: phi = EllipticCurveHom_velusqrt(E, K)
        sage: not phi(K)
        True
        sage: not phi(randrange(2^99) * K)
        True
        sage: P = E.random_point()
        sage: phi(P) in phi.codomain()
        True
        sage: Q = E.random_point()
        sage: phi(Q) in phi.codomain()
        True
        sage: phi(P + Q) == phi(P) + phi(Q)
        True

    Check that the isogeny preserves the field of definition::

        sage: Sequence(K).universe() == phi.domain().base_field()
        True
        sage: phi.codomain().base_field() == phi.domain().base_field()
        True

    Check that the isogeny affects the Weil pairing in the correct way::

        sage: m = lcm(P.order(), Q.order())
        sage: e1 = P.weil_pairing(Q, m)
        sage: e2 = phi(P).weil_pairing(phi(Q), m)
        sage: e2 == e1^phi.degree()
        True

    Check that the isogeny matches (up to isomorphism) the one from
    :class:`~sage.schemes.elliptic_curves.ell_curve_isogeny.EllipticCurveIsogeny`::

        sage: psi = EllipticCurveIsogeny(E, K)
        sage: check = lambda iso: all(iso(psi(Q)) == phi(Q) for Q in E.gens())
        sage: any(map(check, psi.codomain().isomorphisms(phi.codomain())))
        True

    .. SEEALSO::

        :class:`~sage.schemes.elliptic_curves.ell_curve_isogeny.EllipticCurveIsogeny`
    """
    def __init__(self, E, P, *, codomain=None, model=None, Q=None) -> None:
        """
        Initialize this square-root Vélu isogeny from a kernel point of odd order.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.hom_velusqrt import EllipticCurveHom_velusqrt
            sage: E = EllipticCurve(GF(71), [5,5])
            sage: P = E(-2, 22)
            sage: EllipticCurveHom_velusqrt(E, P)
            Elliptic-curve isogeny (using square-root Vélu) of degree 19:
              From: Elliptic Curve defined by y^2 = x^3 + 5*x + 5 over Finite Field of size 71
              To:   Elliptic Curve defined by y^2 = x^3 + 13*x + 11 over Finite Field of size 71

        ::

            sage: E.<P> = EllipticCurve(GF(419), [1,0])
            sage: K = 4*P
            sage: EllipticCurveHom_velusqrt(E, K)
            Elliptic-curve isogeny (using square-root Vélu) of degree 105:
              From: Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 419
              To:   Elliptic Curve defined by y^2 = x^3 + 301*x + 86 over Finite Field of size 419
            sage: E2 = EllipticCurve(GF(419), [0,6,0,385,42])
            sage: EllipticCurveHom_velusqrt(E, K, codomain=E2)
            Elliptic-curve isogeny (using square-root Vélu) of degree 105:
              From: Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 419
              To:   Elliptic Curve defined by y^2 = x^3 + 6*x^2 + 385*x + 42 over Finite Field of size 419
            sage: EllipticCurveHom_velusqrt(E, K, model='montgomery')
            Elliptic-curve isogeny (using square-root Vélu) of degree 105:
              From: Elliptic Curve defined by y^2 = x^3 + x over Finite Field of size 419
              To:   Elliptic Curve defined by y^2 = x^3 + 6*x^2 + x over Finite Field of size 419

        Note that the implementation in fact also works in almost all
        cases when the degree is `5` or `7`. The reason we restrict to
        degrees `\\geq 9` is that (only!) when trying to compute a
        `7`-isogeny from a rational point on an elliptic curve defined
        over `\\GF{3}`, the point `Q` required in the formulas has to be
        defined over a cubic extension rather than an at most quadratic
        extension, which can result in the constructed isogeny being
        irrational. See :issue:`34467`. The assertion in the following
        example currently fails if the minimum degree is lowered::

            sage: E = EllipticCurve(GF(3), [2,1])
            sage: P, = E.gens()
            sage: P.order()
            7
            sage: psi = E.isogeny(P)
            sage: phi = E.isogeny(P, algorithm='velusqrt')              # not tested
            sage: phi._Q.base_ring()                                    # not tested
            Finite Field in z3 of size 3^3
            sage: assert phi.codomain().is_isomorphic(psi.codomain())   # not tested
        """
    @cached_method
    def kernel_polynomial(self):
        """
        Return the kernel polynomial of this square-root Vélu isogeny.

        .. NOTE::

            The data returned by this method has size linear in the degree.

        EXAMPLES::

            sage: E = EllipticCurve(GF(65537^2,'a'), [5,5])
            sage: K = E.cardinality()//31 * E.gens()[0]
            sage: phi = E.isogeny(K, algorithm='velusqrt')
            sage: h = phi.kernel_polynomial(); h
            x^15 + 21562*x^14 + 8571*x^13 + 20029*x^12 + 1775*x^11 + 60402*x^10 + 17481*x^9 + 46543*x^8 + 46519*x^7 + 18590*x^6 + 36554*x^5 + 36499*x^4 + 48857*x^3 + 3066*x^2 + 23264*x + 53937
            sage: h == E.isogeny(K).kernel_polynomial()
            True
            sage: h(K.x())
            0

        TESTS::

            sage: phi.kernel_polynomial().parent()
            Univariate Polynomial Ring in x over Finite Field in a of size 65537^2
        """
    @cached_method
    def dual(self):
        """
        Return the dual of this square-root Vélu
        isogeny as an :class:`EllipticCurveHom`.

        .. NOTE::

            The dual is computed by :class:`EllipticCurveIsogeny`,
            hence it does not benefit from the square-root Vélu speedup.

        EXAMPLES::

            sage: E = EllipticCurve(GF(101^2), [1, 1, 1, 1, 1])
            sage: K = E.cardinality() // 11 * E.gens()[0]
            sage: phi = E.isogeny(K, algorithm='velusqrt'); phi
            Elliptic-curve isogeny (using square-root Vélu) of degree 11:
              From: Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 + x + 1 over Finite Field in z2 of size 101^2
              To:   Elliptic Curve defined by y^2 = x^3 + 39*x + 40 over Finite Field in z2 of size 101^2
            sage: phi.dual()
            Isogeny of degree 11 from Elliptic Curve defined by y^2 = x^3 + 39*x + 40 over Finite Field in z2 of size 101^2 to Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 + x + 1 over Finite Field in z2 of size 101^2
            sage: phi.dual() * phi == phi.domain().scalar_multiplication(11)
            True
            sage: phi * phi.dual() == phi.codomain().scalar_multiplication(11)
            True
        """
    @cached_method
    def rational_maps(self):
        """
        Return the pair of explicit rational maps of this square-root Vélu isogeny
        as fractions of bivariate polynomials in `x` and `y`.

        .. NOTE::

            The data returned by this method has size linear in the degree.

        EXAMPLES::

            sage: E = EllipticCurve(GF(101^2), [1, 1, 1, 1, 1])
            sage: K = (E.cardinality() // 11) * E.gens()[0]
            sage: phi = E.isogeny(K, algorithm='velusqrt'); phi
            Elliptic-curve isogeny (using square-root Vélu) of degree 11:
              From: Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 + x + 1 over Finite Field in z2 of size 101^2
              To:   Elliptic Curve defined by y^2 = x^3 + 39*x + 40 over Finite Field in z2 of size 101^2
            sage: phi.rational_maps()
            ((-17*x^11 - 34*x^10 - 36*x^9 + ... - 29*x^2 - 25*x - 25)/(x^10 + 10*x^9 + 19*x^8 - ... + x^2 + 47*x + 24),
             (-3*x^16 - 6*x^15*y - 48*x^15 + ... - 49*x - 9*y + 46)/(x^15 + 15*x^14 - 35*x^13 - ... + 3*x^2 - 45*x + 47))

        TESTS::

            sage: phi.rational_maps()[0].parent()
            Fraction Field of Multivariate Polynomial Ring in x, y over Finite Field in z2 of size 101^2
            sage: phi.rational_maps()[1].parent()
            Fraction Field of Multivariate Polynomial Ring in x, y over Finite Field in z2 of size 101^2
        """
    @cached_method
    def x_rational_map(self):
        """
        Return the `x`-coordinate rational map of
        this square-root Vélu isogeny
        as a univariate rational function in `x`.

        .. NOTE::

            The data returned by this method has size linear in the degree.

        EXAMPLES::

            sage: E = EllipticCurve(GF(101^2), [1, 1, 1, 1, 1])
            sage: K = (E.cardinality() // 11) * E.gens()[0]
            sage: phi = E.isogeny(K, algorithm='velusqrt'); phi
            Elliptic-curve isogeny (using square-root Vélu) of degree 11:
              From: Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 + x + 1 over Finite Field in z2 of size 101^2
              To:   Elliptic Curve defined by y^2 = x^3 + 39*x + 40 over Finite Field in z2 of size 101^2
            sage: phi.x_rational_map()
            (84*x^11 + 67*x^10 + 65*x^9 + ... + 72*x^2 + 76*x + 76)/(x^10 + 10*x^9 + 19*x^8 + ... + x^2 + 47*x + 24)
            sage: phi.x_rational_map() == phi.rational_maps()[0]
            True

        TESTS::

            sage: phi.x_rational_map().parent()
            Fraction Field of Univariate Polynomial Ring in x over Finite Field in z2 of size 101^2
        """
    def scaling_factor(self):
        """
        Return the Weierstrass scaling factor associated to this
        square-root Vélu isogeny.

        The scaling factor is the constant `u` (in the base field)
        such that `\\varphi^* \\omega_2 = u \\omega_1`, where
        `\\varphi: E_1\\to E_2` is this isogeny and `\\omega_i` are
        the standard Weierstrass differentials on `E_i` defined by
        `\\mathrm dx/(2y+a_1x+a_3)`.

        EXAMPLES::

            sage: E = EllipticCurve(GF(101^2), [1, 1, 1, 1, 1])
            sage: K = (E.cardinality() // 11) * E.gens()[0]
            sage: phi = E.isogeny(K, algorithm='velusqrt', model='montgomery'); phi
            Elliptic-curve isogeny (using square-root Vélu) of degree 11:
              From: Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 + x + 1 over Finite Field in z2 of size 101^2
              To:   Elliptic Curve defined by y^2 = x^3 + 61*x^2 + x over Finite Field in z2 of size 101^2
            sage: phi.scaling_factor()
            55
            sage: phi.scaling_factor() == phi.formal()[1]
            True
        """
    def inseparable_degree(self):
        """
        Return the inseparable degree of this square-root Vélu
        isogeny.

        Since :class:`EllipticCurveHom_velusqrt` only implements
        separable isogenies, this method always returns one.

        TESTS::

            sage: from sage.schemes.elliptic_curves.hom_velusqrt import EllipticCurveHom_velusqrt
            sage: EllipticCurveHom_velusqrt.inseparable_degree(None)
            1
        """
