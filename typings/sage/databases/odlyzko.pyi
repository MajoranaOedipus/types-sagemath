from sage.env import SAGE_SHARE as SAGE_SHARE
from sage.misc.persist import load as load

def zeta_zeros():
    """
    List of the imaginary parts of the first 2,001,052 zeros of the
    Riemann zeta function, accurate to within 4e-9.

    REFERENCES:

    - http://www.dtc.umn.edu/~odlyzko/zeta_tables/index.html

    EXAMPLES:

    The following example shows the imaginary part of the 13th
    nontrivial zero of the Riemann zeta function::

        sage: # optional - database_odlyzko_zeta
        sage: zz = zeta_zeros()
        sage: zz[12]
        59.347044003
        sage: len(zz)
        2001052
    """
