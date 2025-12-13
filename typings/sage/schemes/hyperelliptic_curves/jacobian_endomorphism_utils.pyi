from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.fast_arith import prime_range as prime_range
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ

def satisfies_coefficient_condition(g, p) -> bool:
    """
    This is the coefficient condition in the definition of Omega_K'
    on page 912 of the published version of paper.

    EXAMPLES::

        sage: from sage.schemes.hyperelliptic_curves.jacobian_endomorphism_utils import satisfies_coefficient_condition
        sage: R.<x> = ZZ[]
        sage: f = x^4 + x^3 + 17*x^2 + 5*x
        sage: satisfies_coefficient_condition(f,17)
        False
        sage: f = x^4 + x^3 + 17*x^2 + 23*x + 23^2
        sage: satisfies_coefficient_condition(f,23)
        True
    """
def get_is_geom_field(f, C, bad_primes, B: int = 200):
    """
    Determine whether the geometric endomorphism algebra is a field.

    This is Algorithm 4.10 in [Lom2019]_. The computation done here
    may allow one to immediately conclude that the geometric endomorphism
    ring is trivial (i.e. the integer ring); this information is output
    in a second boolean to avoid unnecessary subsequent computation.

    An additional optimisation comes from Part (2) of Theorem 4.8 in
    [Lom2019]_, from which we can conclude that the endomorphism ring
    is geometrically trivial, and from Proposition 4.7 in loc. cit. from
    which we can rule out potential QM.

    INPUT:

    - ``f`` -- a polynomial defining the hyperelliptic curve

    - ``C`` -- the hyperelliptic curve

    - ``bad_primes`` -- the list of odd primes of bad reduction

    - ``B`` -- (default: 200) the bound which appears in the statement of
      the algorithm from [Lom2019]_

    OUTPUT:

    Pair of booleans (bool1, bool2). `bool1` indicates if the
    geometric endomorphism algebra is a field; `bool2` indicates if the
    geometric endomorphism algebra is the field of rational numbers.

    WARNING:

    There is a very small chance that this algorithm return ``False`` when in
    fact it is ``True``. In this case, as explained in the discussion
    immediately preceding Algorithm 4.15 of [Lom2019]_, this can be established
    by increasing the optional `B` parameter. Mathematically, this algorithm
    gives the correct answer only in the limit as `B \\to \\infty`, although in
    practice `B = 200` was sufficient to correctly verify every single entry
    in the LMFDB. However, strictly speaking, a ``False`` returned by this
    function is not provably ``False``.

    EXAMPLES:

    This is LMFDB curve 940693.a.960693.1::

        sage: from sage.schemes.hyperelliptic_curves.jacobian_endomorphism_utils import get_is_geom_field
        sage: R.<x> = QQ[]
        sage: f = 4*x^6 - 12*x^5 + 20*x^3 - 8*x^2 - 4*x + 1
        sage: C = HyperellipticCurve(f)
        sage: get_is_geom_field(f,C,[13,269])
        (False, False)

    This is LMFDB curve 3125.a.3125.1::

        sage: f = 4*x^5 + 1
        sage: C = HyperellipticCurve(f)
        sage: get_is_geom_field(f,C,[5])
        (True, False)

    This is LMFDB curve 277.a.277.2::

        sage: f = 4*x^6 - 36*x^4 + 56*x^3 - 76*x^2 + 44*x - 23
        sage: C = HyperellipticCurve(f)
        sage: get_is_geom_field(f,C,[277])
        (True, True)
    """
def is_geom_trivial_when_field(C, bad_primes, B: int = 200):
    """
    Determine if the geometric endomorphism ring is trivial assuming the
    geometric endomorphism algebra is a field.

    This is Algorithm 4.15 in [Lom2019]_.

    INPUT:

    - ``C`` -- the hyperelliptic curve

    - ``bad_primes`` -- the list of odd primes of bad reduction

    - ``B`` -- (default: 200) the bound which appears in the statement of
      the algorithm from [Lom2019]_

    OUTPUT:

    Boolean indicating whether or not the geometric endomorphism
    algebra is the field of rational numbers.

    WARNING:

    There is a very small chance that this algorithm returns ``False`` when in
    fact it is ``True``. In this case, as explained in the discussion
    immediately preceding Algorithm 4.15 of [Lom2019]_, this can be established
    by increasing the optional `B` parameter. Mathematically, this algorithm
    gives the correct answer only in the limit as `B \\to \\infty`, although in
    practice `B = 200` was sufficient to correctly verify every single entry
    in the LMFDB. However, strictly speaking, a ``False`` returned by this
    function is not provably ``False``.

    EXAMPLES:

    This is LMFDB curve 461.a.461.2::

        sage: from sage.schemes.hyperelliptic_curves.jacobian_endomorphism_utils import is_geom_trivial_when_field
        sage: R.<x> = QQ[]
        sage: f = 4*x^5 - 4*x^4 - 156*x^3 + 40*x^2 + 1088*x - 1223
        sage: C = HyperellipticCurve(f)
        sage: is_geom_trivial_when_field(C,[461])
        True

    This is LMFDB curve 4489.a.4489.1::

        sage: f = x^6 + 4*x^5 + 2*x^4 + 2*x^3 + x^2 - 2*x + 1
        sage: C = HyperellipticCurve(f)
        sage: is_geom_trivial_when_field(C,[67])
        False
    """
