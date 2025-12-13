from .constructor import EllipticCurve as EllipticCurve, EllipticCurve_from_j as EllipticCurve_from_j
from sage.groups.generic import order_from_bounds as order_from_bounds
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.polynomial.polynomial_ring import polygen as polygen
from sage.schemes.curves.projective_curve import Hasse_bounds as Hasse_bounds

def cardinality_exhaustive(self):
    """
    Return the cardinality of ``self`` over the base field.

    This simply adds up the number of points with each x-coordinate:
    only used for small field sizes!

    EXAMPLES::

        sage: p = next_prime(10^3)
        sage: E = EllipticCurve(GF(p), [3,4])
        sage: E.cardinality_exhaustive()
        1020
        sage: E = EllipticCurve(GF(3^4,'a'), [1,1])
        sage: E.cardinality_exhaustive()
        64
    """
def cardinality_bsgs(self, verbose: bool = False):
    '''
    Return the cardinality of ``self`` over the base field.

    ALGORITHM: A variant of "Mestre\'s trick" extended to all finite
    fields by Cremona and Sutherland, 2008.

    .. NOTE::

        1. The Mestre-Schoof-Cremona-Sutherland algorithm may fail for
           a small finite number of curves over `F_q` for `q` at most 49, so
           for `q<50` we use an exhaustive count.

        2. Quadratic twists are not implemented in characteristic 2
           when `j=0 (=1728)`; but this case is treated separately.

    EXAMPLES::

        sage: p = next_prime(10^3)
        sage: E = EllipticCurve(GF(p), [3,4])
        sage: E.cardinality_bsgs()
        1020
        sage: E = EllipticCurve(GF(3^4,\'a\'), [1,1])
        sage: E.cardinality_bsgs()
        64
        sage: F.<a> = GF(101^3,\'a\')
        sage: E = EllipticCurve([2*a^2 + 48*a + 27, 89*a^2 + 76*a + 24])
        sage: E.cardinality_bsgs()
        1031352
    '''
