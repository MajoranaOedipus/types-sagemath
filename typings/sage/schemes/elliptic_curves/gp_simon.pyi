from _typeshed import Incomplete
from sage.env import SAGE_EXTCODE as SAGE_EXTCODE
from sage.libs.pari import pari as pari
from sage.misc.randstate import current_randstate as current_randstate
from sage.misc.superseded import deprecation as deprecation
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.structure.parent_gens import localvars as localvars

simon_dir: Incomplete

def simon_two_descent(E, verbose: int = 0, lim1=None, lim3=None, limtriv=None, maxprob: int = 20, limbigprime: int = 30, known_points=[]):
    """
    Interface to Simon's gp script for two-descent.

    .. NOTE::

        Users should instead run E.simon_two_descent()

    EXAMPLES::

        sage: import sage.schemes.elliptic_curves.gp_simon
        sage: E = EllipticCurve('389a1')
        sage: sage.schemes.elliptic_curves.gp_simon.simon_two_descent(E)
        doctest:warning...:
        DeprecationWarning: please use the 2-descent algorithm over QQ inside pari
        See https://github.com/sagemath/sage/issues/38461 for details.
        (2, 2, [(-3/4 : 7/8 : 1), (5/4 : 5/8 : 1)])

    TESTS::

        sage: # needs sage.rings.number_field
        sage: E = EllipticCurve('37a1').change_ring(QuadraticField(-11,'x'))
        sage: E.simon_two_descent()
        (1, 1, [(0 : 0 : 1)])

    An example with an elliptic curve defined over a relative number field::

        sage: # needs sage.rings.number_field
        sage: F.<a> = QuadraticField(29)
        sage: x = QQ['x'].gen()
        sage: K.<b> = F.extension(x^2-1/2*a+1/2)
        sage: E = EllipticCurve(K,[1, 0, 5/2*a + 27/2, 0, 0])   # long time (about 3 s)
        sage: E.simon_two_descent(lim1=2, limtriv=3)
        (1, 1, ...)

    Check that :issue:`16022` is fixed::

        sage: # needs sage.rings.number_field
        sage: K.<y> = NumberField(x^4 + x^2 - 7)
        sage: E = EllipticCurve(K, [1, 0, 5*y^2 + 16, 0, 0])
        sage: E.simon_two_descent(lim1=2, limtriv=3)            # long time (about 3 s)
        (1, 1, ...)

    An example that checks that :issue:`9322` is fixed (it should take less than a second to run)::

        sage: # needs sage.rings.number_field
        sage: K.<w> = NumberField(x^2 - x - 232)
        sage: E = EllipticCurve([2 - w, 18 + 3*w, 209 + 9*w, 2581 + 175*w, 852 - 55*w])
        sage: E.simon_two_descent()                             # long time
        (0, 2, [])
    """
