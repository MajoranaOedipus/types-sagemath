from sage.arith.misc import binomial as binomial, kronecker as kronecker
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.sage_object import SageObject as SageObject

class pAdicLseries(SageObject):
    """
    The `p`-adic `L`-series associated to an overconvergent eigensymbol.

    INPUT:

    - ``symb`` -- an overconvergent eigensymbol
    - ``gamma`` -- topological generator of `1 + p\\ZZ_p`
      (default: `1+p` or 5 if `p=2`)
    - ``quadratic_twist`` -- conductor of quadratic twist `\\chi` (default: 1)
    - ``precision`` -- if ``None`` (default) is specified,
      the correct precision bound is computed and the answer
      is returned modulo that accuracy

    EXAMPLES::

        sage: E = EllipticCurve('37a')
        sage: p = 5
        sage: prec = 4
        sage: L = E.padic_lseries(p, implementation='pollackstevens', precision=prec) # long time
        sage: L[1]                # long time
        1 + 4*5 + 2*5^2 + O(5^3)
        sage: L.series(3)    # long time
        O(5^4) + (1 + 4*5 + 2*5^2 + O(5^3))*T + (3 + O(5^2))*T^2 + O(T^3)

    ::

        sage: from sage.modular.pollack_stevens.padic_lseries import pAdicLseries
        sage: E = EllipticCurve('20a')
        sage: phi = E.pollack_stevens_modular_symbol()
        sage: Phi = phi.p_stabilize_and_lift(3, 4) # long time
        sage: L = pAdicLseries(Phi)                # long time
        sage: L.series(4)                          # long time
        2*3 + O(3^4) + (3 + O(3^2))*T + (2 + O(3))*T^2 + O(3^0)*T^3 + O(T^4)

    An example of a `p`-adic `L`-series associated to a modular
    abelian surface. This is not tested as it takes too long.::

        sage: from sage.modular.pollack_stevens.space import ps_modsym_from_simple_modsym_space
        sage: from sage.modular.pollack_stevens.padic_lseries import pAdicLseries
        sage: A = ModularSymbols(103,2,1).cuspidal_submodule().new_subspace().decomposition()[0]
        sage: p = 19
        sage: prec = 4
        sage: phi = ps_modsym_from_simple_modsym_space(A)
        sage: ap = phi.Tq_eigenvalue(p,prec)
        sage: c1,c2 = phi.completions(p,prec)
        sage: phi1,psi1 = c1
        sage: phi2,psi2 = c2
        sage: phi1p = phi1.p_stabilize_and_lift(p,ap = psi1(ap), M = prec) # not tested - too long
        sage: L1 = pAdicLseries(phi1p)                                     # not tested - too long
        sage: phi2p = phi2.p_stabilize_and_lift(p,ap = psi2(ap), M = prec) # not tested - too long
        sage: L2  = pAdicLseries(phi2p)                                    # not tested - too long
        sage: L1[1]*L2[1]                                                  # not tested - too long
        13 + 9*19 + 18*19^2 + O(19^3)
    """
    def __init__(self, symb, gamma=None, quadratic_twist: int = 1, precision=None) -> None:
        """
        Initialize the class.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.padic_lseries import pAdicLseries
            sage: E = EllipticCurve('11a3')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: p = 11
            sage: prec = 3
            sage: Phi = phi.lift(p, prec,eigensymbol=True) # long time
            sage: L = pAdicLseries(Phi)                    # long time
            sage: L.series(3)                              # long time
            O(11^3) + (2 + 5*11 + O(11^2))*T + (10 + O(11))*T^2 + O(T^3)

            sage: TestSuite(L).run()                       # long time
        """
    def __getitem__(self, n):
        """
        Return the `n`-th coefficient of the `p`-adic `L`-series.

        EXAMPLES::

            sage: E = EllipticCurve('14a5')
            sage: L = E.padic_lseries(7,implementation='pollackstevens',precision=5) # long time
            sage: L[0]                                   # long time
            O(7^5)
            sage: L[1]                                   # long time
            5 + 5*7 + 2*7^2 + 2*7^3 + O(7^4)
        """
    def __eq__(self, other):
        """
        Compare ``self`` and ``other``.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: L = E.padic_lseries(11,implementation='pollackstevens',precision=6) # long time
            sage: L == loads(dumps(L)) # indirect doctest, long time
            True
        """
    def __ne__(self, other):
        """
        Compare ``self`` and ``other``.

        EXAMPLES::

            sage: E = EllipticCurve('11a')
            sage: L = E.padic_lseries(11,implementation='pollackstevens',precision=6) # long time
            sage: L != L  # long time
            False
        """
    def symbol(self):
        """
        Return the overconvergent modular symbol.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.padic_lseries import pAdicLseries
            sage: E = EllipticCurve('21a4')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: Phi = phi.p_stabilize_and_lift(2,5)   # long time
            sage: L = pAdicLseries(Phi)                 # long time
            sage: L.symbol()                              # long time
            Modular symbol of level 42 with values in Space of 2-adic
            distributions with k=0 action and precision cap 15
            sage: L.symbol() is Phi                       # long time
            True
        """
    def prime(self):
        """
        Return the prime `p` as in `p`-adic `L`-series.

        EXAMPLES::

            sage: E = EllipticCurve('19a')
            sage: L = E.padic_lseries(19, implementation='pollackstevens',precision=6) # long time
            sage: L.prime()                   # long time
            19
        """
    def quadratic_twist(self):
        """
        Return the discriminant of the quadratic twist.

        EXAMPLES::

            sage: from sage.modular.pollack_stevens.padic_lseries import pAdicLseries
            sage: E = EllipticCurve('37a')
            sage: phi = E.pollack_stevens_modular_symbol()
            sage: Phi = phi.lift(37,4)
            sage: L = pAdicLseries(Phi, quadratic_twist=-3)
            sage: L.quadratic_twist()
            -3
        """
    def series(self, prec: int = 5):
        '''
        Return the ``prec``-th approximation to the `p`-adic `L`-series
        associated to ``self``, as a power series in `T` (corresponding to
        `\\gamma-1` with `\\gamma` the chosen generator of `1+p\\ZZ_p`).

        INPUT:

        - ``prec`` -- (default: 5) the precision of the power series

        EXAMPLES::

            sage: E = EllipticCurve(\'14a2\')
            sage: p = 3
            sage: prec = 6
            sage: L = E.padic_lseries(p,implementation=\'pollackstevens\',precision=prec) # long time
            sage: L.series(4)          # long time
            2*3 + 3^4 + 3^5 + O(3^6) + (2*3 + 3^2 + O(3^4))*T + (2*3 + O(3^2))*T^2 + (3 + O(3^2))*T^3 + O(T^4)

            sage: E = EllipticCurve("15a3")
            sage: L = E.padic_lseries(5,implementation=\'pollackstevens\',precision=15)  # long time
            sage: L.series(3)            # long time
            O(5^15) + (2 + 4*5^2 + 3*5^3 + 5^5 + 2*5^6 + 3*5^7 + 3*5^8 + 2*5^9 + 2*5^10 + 3*5^11 + 5^12 + O(5^13))*T + (4*5 + 4*5^3 + 3*5^4 + 4*5^5 + 3*5^6 + 2*5^7 + 5^8 + 4*5^9 + 3*5^10 + O(5^11))*T^2 + O(T^3)

            sage: E = EllipticCurve("79a1")
            sage: L = E.padic_lseries(2,implementation=\'pollackstevens\',precision=10) # not tested
            sage: L.series(4)  # not tested
            O(2^9) + (2^3 + O(2^4))*T + O(2^0)*T^2 + (O(2^-3))*T^3 + O(T^4)
        '''
    def interpolation_factor(self, ap, chip: int = 1, psi=None):
        """
        Return the interpolation factor associated to ``self``.
        This is the `p`-adic multiplier that which appears in
        the interpolation formula of the `p`-adic `L`-function. It
        has the form `(1-\\alpha_p^{-1})^2`, where `\\alpha_p` is the
        unit root of `X^2 - \\psi(a_p) \\chi(p) X + p`.

        INPUT:

        - ``ap`` -- the eigenvalue of the Up operator

        - ``chip`` -- the value of the nebentype at `p` (default: 1)

        - ``psi`` -- a twisting character (default: ``None``)

        OUTPUT: a `p`-adic number

        EXAMPLES::

            sage: E = EllipticCurve('19a2')
            sage: L = E.padic_lseries(3,implementation='pollackstevens',precision=6)  # long time
            sage: ap = E.ap(3)               # long time
            sage: L.interpolation_factor(ap) # long time
            3^2 + 3^3 + 2*3^5 + 2*3^6 + O(3^7)

        Comparing against a different implementation::

            sage: L = E.padic_lseries(3)
            sage: (1-1/L.alpha(prec=4))^2
            3^2 + 3^3 + O(3^5)
        """

def log_gamma_binomial(p, gamma, n, M):
    """
    Return the list of coefficients in the power series
    expansion (up to precision `M`) of `\\binom{\\log_p(z)/\\log_p(\\gamma)}{n}`

    INPUT:

    - ``p`` -- prime
    - ``gamma`` -- topological generator, e.g. `1+p`
    - ``n`` -- nonnegative integer
    - ``M`` -- precision

    OUTPUT:

    The list of coefficients in the power series expansion of
    `\\binom{\\log_p(z)/\\log_p(\\gamma)}{n}`

    EXAMPLES::

        sage: from sage.modular.pollack_stevens.padic_lseries import log_gamma_binomial
        sage: log_gamma_binomial(5,1+5,2,4)
        [0, -3/205, 651/84050, -223/42025]
        sage: log_gamma_binomial(5,1+5,3,4)
        [0, 2/205, -223/42025, 95228/25845375]
    """
