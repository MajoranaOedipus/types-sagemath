from sage.arith.misc import kronecker as kronecker, legendre_symbol as legendre_symbol, prime_divisors as prime_divisors
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.functional import squarefree_part as squarefree_part
from sage.misc.misc_c import prod as prod
from sage.misc.mrange import mrange as mrange
from sage.quadratic_forms.special_values import gamma__exact as gamma__exact, quadratic_L_function__exact as quadratic_L_function__exact, zeta__exact as zeta__exact
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

def mass__by_Siegel_densities(self, odd_algorithm: str = 'Pall', even_algorithm: str = 'Watson'):
    '''
    Return the mass of transformations (det 1 and -1).

    .. WARNING::

        This is broken right now...

    INPUT:

    - ``odd_algorithm`` -- algorithm to be used when `p>2`; ``\'Pall\'`` (only
      one choice for now)
    - ``even_algorithm`` -- algorithm to be used when `p=2`; either
      ``\'Kitaoka\'`` or ``\'Watson\'`` (the default)

    REFERENCES:

    - Nipp\'s Book "Tables of Quaternary Quadratic Forms".
    - Papers of Pall (only for `p>2`) and Watson (for `p=2` -- tricky!).
    - Siegel, Milnor-Hussemoller, Conway-Sloane Paper IV, Kitoaka (all of which
      have problems...)

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1,1])
        sage: m = Q.mass__by_Siegel_densities(); m                                      # needs sage.symbolic
        1/384
        sage: m - (2^Q.dim() * factorial(Q.dim()))^(-1)                                 # needs sage.symbolic
        0

    ::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: m = Q.mass__by_Siegel_densities(); m                                      # needs sage.symbolic
        1/48
        sage: m - (2^Q.dim() * factorial(Q.dim()))^(-1)                                 # needs sage.symbolic
        0
    '''
def Pall_mass_density_at_odd_prime(self, p):
    '''
    Return the local representation density of a form (for
    representing itself) defined over `\\ZZ`, at some prime `p>2`.

    REFERENCES:

    Pall\'s article "The Weight of a Genus of Positive n-ary Quadratic Forms"
    appearing in Proc. Symp. Pure Math. VIII (1965), pp95--105.

    INPUT:

    - ``p`` -- a prime number > 2

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = QuadraticForm(ZZ, 3, [1,0,0,1,0,1])
        sage: Q.Pall_mass_density_at_odd_prime(3)
        [(0, Quadratic form in 3 variables over Integer Ring with coefficients:
        [ 1 0 0 ]
        [ * 1 0 ]
        [ * * 1 ])] [(0, 3, 8)] [8/9] 8/9
        8/9
    '''
def Watson_mass_at_2(self):
    '''
    Return the local mass of the quadratic form when `p=2`, according
    to Watson\'s Theorem 1 of "The 2-adic density of a quadratic form"
    in Mathematika 23 (1976), pp 94--106.

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.Watson_mass_at_2()  # WARNING:  WE NEED TO CHECK THIS CAREFULLY!        # needs sage.symbolic
        384
    '''
def Kitaoka_mass_at_2(self):
    '''
    Return the local mass of the quadratic form when `p=2`, according
    to Theorem 5.6.3 on pp108--9 of Kitaoka\'s Book "The Arithmetic of
    Quadratic Forms".

    OUTPUT: a rational number > 0

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.Kitaoka_mass_at_2()   # WARNING:  WE NEED TO CHECK THIS CAREFULLY!
        1/2
    '''
def mass_at_two_by_counting_mod_power(self, k):
    """
    Compute the local mass at `p=2` assuming that it's stable (mod `2^k`).

    .. NOTE::

        This is **way** too slow to be useful, even when `k=1`.

    .. TODO::

        Remove this routine, or try to compile it!

    INPUT:

    - ``k`` -- integer `\\geq 1`

    OUTPUT: a rational number

    EXAMPLES::

        sage: Q = DiagonalQuadraticForm(ZZ, [1,1,1])
        sage: Q.mass_at_two_by_counting_mod_power(1)
        4
    """
