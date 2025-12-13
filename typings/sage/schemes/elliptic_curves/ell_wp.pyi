from sage.rings.laurent_series_ring import LaurentSeriesRing as LaurentSeriesRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing

def weierstrass_p(E, prec: int = 20, algorithm=None):
    """
    Compute the Weierstrass `\\wp`-function on an elliptic curve.

    INPUT:

    - ``E`` -- an elliptic curve

    - ``prec`` -- precision

    - ``algorithm`` -- string or ``None`` (default: ``None``);
      a choice of algorithm among ``'pari'``, ``'fast'``, ``'quadratic'``,
      or ``None`` to let this function determine the best algorithm to use

    OUTPUT:

    a Laurent series in one variable `z` with coefficients in the base
    field `k` of `E`.

    EXAMPLES::

        sage: E = EllipticCurve('11a1')
        sage: E.weierstrass_p(prec=10)
        z^-2 + 31/15*z^2 + 2501/756*z^4 + 961/675*z^6 + 77531/41580*z^8 + O(z^10)
        sage: E.weierstrass_p(prec=8)
        z^-2 + 31/15*z^2 + 2501/756*z^4 + 961/675*z^6 + O(z^8)
        sage: Esh = E.short_weierstrass_model()
        sage: Esh.weierstrass_p(prec=8)
        z^-2 + 13392/5*z^2 + 1080432/7*z^4 + 59781888/25*z^6 + O(z^8)

        sage: E.weierstrass_p(prec=8, algorithm='pari')
        z^-2 + 31/15*z^2 + 2501/756*z^4 + 961/675*z^6 + O(z^8)
        sage: E.weierstrass_p(prec=8, algorithm='quadratic')
        z^-2 + 31/15*z^2 + 2501/756*z^4 + 961/675*z^6 + O(z^8)

        sage: k = GF(11)
        sage: E = EllipticCurve(k, [1,1])
        sage: E.weierstrass_p(prec=6, algorithm='fast')
        z^-2 + 2*z^2 + 3*z^4 + O(z^6)
        sage: E.weierstrass_p(prec=7, algorithm='fast')
        Traceback (most recent call last):
        ...
        ValueError: for computing the Weierstrass p-function via the fast algorithm,
        the characteristic (11) of the underlying field must be greater than prec + 4 = 11
        sage: E.weierstrass_p(prec=8)
        z^-2 + 2*z^2 + 3*z^4 + 5*z^6 + O(z^8)
        sage: E.weierstrass_p(prec=8, algorithm='quadratic')
        z^-2 + 2*z^2 + 3*z^4 + 5*z^6 + O(z^8)
        sage: E.weierstrass_p(prec=8, algorithm='pari')
        z^-2 + 2*z^2 + 3*z^4 + 5*z^6 + O(z^8)
        sage: E.weierstrass_p(prec=9)
        Traceback (most recent call last):
        ...
        NotImplementedError: currently no algorithms for computing the Weierstrass
        p-function for that characteristic / precision pair is implemented.
        Lower the precision below char(k) - 2
        sage: E.weierstrass_p(prec=9, algorithm='quadratic')
        Traceback (most recent call last):
        ...
        ValueError: for computing the Weierstrass p-function via the quadratic
        algorithm, the characteristic (11) of the underlying field must be greater
        than prec + 2 = 11
        sage: E.weierstrass_p(prec=9, algorithm='pari')
        Traceback (most recent call last):
        ...
        ValueError: for computing the Weierstrass p-function via pari, the
        characteristic (11) of the underlying field must be greater than prec + 2 = 11

    TESTS::

        sage: E.weierstrass_p(prec=4, algorithm='foo')
        Traceback (most recent call last):
        ...
        ValueError: unknown algorithm for computing the Weierstrass p-function
    """
def compute_wp_pari(E, prec):
    """
    Compute the Weierstrass `\\wp`-function with the ``ellwp`` function
    from PARI.

    EXAMPLES::

        sage: E = EllipticCurve([0,1])
        sage: from sage.schemes.elliptic_curves.ell_wp import compute_wp_pari
        sage: compute_wp_pari(E, prec=20)
        z^-2 - 1/7*z^4 + 1/637*z^10 - 1/84721*z^16 + O(z^20)
        sage: compute_wp_pari(E, prec=30)
        z^-2 - 1/7*z^4 + 1/637*z^10 - 1/84721*z^16
        + 3/38548055*z^22 - 4/8364927935*z^28 + O(z^30)
    """
def compute_wp_quadratic(k, A, B, prec):
    """
    Compute the truncated Weierstrass function of an elliptic curve
    defined by short Weierstrass model: `y^2 = x^3 + Ax + B`. Uses an
    algorithm that is of complexity `O(prec^2)`.

    Let p be the characteristic of the underlying field. Then we must
    have either p = 0, or p > prec + 2.

    INPUT:

    - ``k`` -- the field of definition of the curve
    - ``A`` -- and
    - ``B`` -- the coefficients of the elliptic curve
    - ``prec`` -- the precision to which we compute the series

    OUTPUT:

    A Laurent series approximating the Weierstrass `\\wp`-function to precision ``prec``.

    ALGORITHM:

    This function uses the algorithm described in section 3.2 of [BMSS2006]_.

    EXAMPLES::

        sage: E = EllipticCurve([7,0])
        sage: E.weierstrass_p(prec=10, algorithm='quadratic')
        z^-2 - 7/5*z^2 + 49/75*z^6 + O(z^10)

        sage: E = EllipticCurve(GF(103), [1,2])
        sage: E.weierstrass_p(algorithm='quadratic')
        z^-2 + 41*z^2 + 88*z^4 + 11*z^6 + 57*z^8 + 55*z^10 + 73*z^12
         + 11*z^14 + 17*z^16 + 50*z^18 + O(z^20)

        sage: from sage.schemes.elliptic_curves.ell_wp import compute_wp_quadratic
        sage: compute_wp_quadratic(E.base_ring(), E.a4(), E.a6(), prec=10)
        z^-2 + 41*z^2 + 88*z^4 + 11*z^6 + 57*z^8 + O(z^10)
    """
def compute_wp_fast(k, A, B, m):
    """
    Compute the Weierstrass function of an elliptic curve defined by short Weierstrass model:
    `y^2 = x^3 + Ax + B`. It does this with as fast as polynomial of degree `m` can be multiplied
    together in the base ring, i.e. `O(M(n))` in the notation of [BMSS2006]_.

    Let `p` be the characteristic of the underlying field: Then we must have either `p=0`, or `p > m + 3`.

    INPUT:

    - ``k`` -- the base field of the curve
    - ``A`` -- and
    - ``B`` -- as the coefficients of the short Weierstrass model `y^2 = x^3 +Ax +B`, and
    - ``m`` -- the precision to which the function is computed to

    OUTPUT: the Weierstrass `\\wp` function as a Laurent series to precision `m`

    ALGORITHM:

    This function uses the algorithm described in section 3.3 of
    [BMSS2006]_.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_wp import compute_wp_fast
        sage: compute_wp_fast(QQ, 1, 8, 7)
        z^-2 - 1/5*z^2 - 8/7*z^4 + 1/75*z^6 + O(z^7)

        sage: k = GF(37)
        sage: compute_wp_fast(k, k(1), k(8), 5)
        z^-2 + 22*z^2 + 20*z^4 + O(z^5)
    """
def solve_linear_differential_system(a, b, c, alpha):
    """
    Solve a system of linear differential equations: `af' + bf = c` and `f'(0) = \\alpha`
    where `a`, `b`, and `c` are power series in one variable and `\\alpha` is a constant in the coefficient ring.

    ALGORITHM:

    due to Brent and Kung '78.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_wp import solve_linear_differential_system
        sage: k = GF(17)
        sage: R.<x> = PowerSeriesRing(k)
        sage: a = 1 + x + O(x^7); b = x + O(x^7); c = 1 + x^3 + O(x^7); alpha = k(3)
        sage: f = solve_linear_differential_system(a, b, c, alpha)
        sage: f
        3 + x + 15*x^2 + x^3 + 10*x^5 + 3*x^6 + 13*x^7 + O(x^8)
        sage: a*f.derivative() + b*f - c
        O(x^7)
        sage: f(0) == alpha
        True
    """
