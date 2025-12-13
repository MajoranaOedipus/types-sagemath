from .eis_series_cython import eisenstein_series_poly as eisenstein_series_poly
from sage.libs.flint.fmpz_poly_sage import Fmpz_poly as Fmpz_poly
from sage.misc.verbose import verbose as verbose
from sage.rings.finite_rings.integer_mod_ring import Integers as Integers
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.all import Sequence as Sequence

def victor_miller_basis(k, prec: int = 10, cusp_only: bool = False, var: str = 'q'):
    """
    Compute and return the Victor Miller basis for modular forms of
    weight `k` and level 1 to precision `O(q^{prec})`.  If
    ``cusp_only`` is True, return only a basis for the cuspidal
    subspace.

    INPUT:

    - ``k`` -- integer

    - ``prec`` -- (default: 10) a positive integer

    - ``cusp_only`` -- boolean (default: ``False``)

    - ``var`` -- string (default: ``'q'``)

    OUTPUT: a sequence whose entries are power series in ``ZZ[[var]]``

    EXAMPLES::

        sage: victor_miller_basis(1, 6)
        []
        sage: victor_miller_basis(0, 6)
        [1 + O(q^6)]
        sage: victor_miller_basis(2, 6)
        []
        sage: victor_miller_basis(4, 6)
        [1 + 240*q + 2160*q^2 + 6720*q^3 + 17520*q^4 + 30240*q^5 + O(q^6)]

        sage: victor_miller_basis(6, 6, var='w')
        [1 - 504*w - 16632*w^2 - 122976*w^3 - 532728*w^4 - 1575504*w^5 + O(w^6)]

        sage: victor_miller_basis(6, 6)
        [1 - 504*q - 16632*q^2 - 122976*q^3 - 532728*q^4 - 1575504*q^5 + O(q^6)]
        sage: victor_miller_basis(12, 6)
        [1 + 196560*q^2 + 16773120*q^3 + 398034000*q^4 + 4629381120*q^5 + O(q^6),
         q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)]

        sage: victor_miller_basis(12, 6, cusp_only=True)
        [q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 + O(q^6)]
        sage: victor_miller_basis(24, 6, cusp_only=True)
        [q + 195660*q^3 + 12080128*q^4 + 44656110*q^5 + O(q^6),
         q^2 - 48*q^3 + 1080*q^4 - 15040*q^5 + O(q^6)]
        sage: victor_miller_basis(24, 6)
        [1 + 52416000*q^3 + 39007332000*q^4 + 6609020221440*q^5 + O(q^6),
         q + 195660*q^3 + 12080128*q^4 + 44656110*q^5 + O(q^6),
         q^2 - 48*q^3 + 1080*q^4 - 15040*q^5 + O(q^6)]
        sage: victor_miller_basis(32, 6)
        [1 + 2611200*q^3 + 19524758400*q^4 + 19715347537920*q^5 + O(q^6),
         q + 50220*q^3 + 87866368*q^4 + 18647219790*q^5 + O(q^6),
         q^2 + 432*q^3 + 39960*q^4 - 1418560*q^5 + O(q^6)]

        sage: victor_miller_basis(40,200)[1:] == victor_miller_basis(40,200,cusp_only=True)
        True
        sage: victor_miller_basis(200,40)[1:] == victor_miller_basis(200,40,cusp_only=True)
        True

    AUTHORS:

    - William Stein, Craig Citro: original code

    - Martin Raum (2009-08-02): use FLINT for polynomial arithmetic (instead of NTL)
    """
def delta_qexp(prec: int = 10, var: str = 'q', K=...):
    """
    Return the `q`-expansion of the weight 12 cusp form `\\Delta` as a power
    series with coefficients in the ring K (`= \\ZZ` by default).

    INPUT:

    - ``prec`` -- integer (default: 10); the absolute precision of the output
      (must be positive)

    - ``var`` -- string (default: ``'q'``); variable name

    - ``K`` -- ring (default: `\\ZZ`); base ring of answer

    OUTPUT: a power series over K in the variable ``var``

    ALGORITHM:

    Compute the theta series

    .. MATH::

        \\sum_{n \\ge 0} (-1)^n (2n+1) q^{n(n+1)/2},

    a very simple explicit modular form whose 8th power is `\\Delta`. Then
    compute the 8th power. All computations are done over `\\ZZ` or `\\ZZ`
    modulo `N` depending on the characteristic of the given coefficient
    ring `K`, and coerced into `K` afterwards.

    EXAMPLES::

        sage: delta_qexp(7)
        q - 24*q^2 + 252*q^3 - 1472*q^4 + 4830*q^5 - 6048*q^6 + O(q^7)
        sage: delta_qexp(7,'z')
        z - 24*z^2 + 252*z^3 - 1472*z^4 + 4830*z^5 - 6048*z^6 + O(z^7)
        sage: delta_qexp(-3)
        Traceback (most recent call last):
        ...
        ValueError: prec must be positive
        sage: delta_qexp(20, K = GF(3))
        q + q^4 + 2*q^7 + 2*q^13 + q^16 + 2*q^19 + O(q^20)
        sage: delta_qexp(20, K = GF(3^5, 'a'))
        q + q^4 + 2*q^7 + 2*q^13 + q^16 + 2*q^19 + O(q^20)
        sage: delta_qexp(10, K = IntegerModRing(60))
        q + 36*q^2 + 12*q^3 + 28*q^4 + 30*q^5 + 12*q^6 + 56*q^7 + 57*q^9 + O(q^10)

    TESTS:

    Test algorithm with modular arithmetic (see also :issue:`11804`)::

        sage: delta_qexp(10^4).change_ring(GF(13)) == delta_qexp(10^4, K=GF(13))
        True
        sage: delta_qexp(1000).change_ring(IntegerModRing(5^100)) == delta_qexp(1000, K=IntegerModRing(5^100))
        True

    AUTHORS:

    - William Stein: original code

    - David Harvey (2007-05): sped up first squaring step

    - Martin Raum (2009-08-02): use FLINT for polynomial arithmetic (instead of NTL)
    """
