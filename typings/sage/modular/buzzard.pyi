from _typeshed import Incomplete
from sage.env import SAGE_EXTCODE as SAGE_EXTCODE
from sage.libs.pari import pari as pari

buzzard_dir: Incomplete

def buzzard_tpslopes(p, N, kmax):
    """
    Return a vector of length kmax, whose `k`-th entry
    (`0 \\leq k \\leq k_{max}`) is the conjectural sequence
    of valuations of eigenvalues of `T_p` on forms of level
    `N`, weight `k`, and trivial character.

    This conjecture is due to Kevin Buzzard, and is only made assuming
    that `p` does not divide `N` and if `p` is
    `\\Gamma_0(N)`-regular.

    EXAMPLES::

        sage: from sage.modular.buzzard import buzzard_tpslopes
        sage: c = buzzard_tpslopes(2,1,50)
        ...
        sage: c[50]
        [4, 8, 13]

    Hence Buzzard would conjecture that the `2`-adic valuations
    of the eigenvalues of `T_2` on cusp forms of level 1 and
    weight `50` are `[4,8,13]`, which indeed they are,
    as one can verify by an explicit computation using, e.g., modular
    symbols::

        sage: M = ModularSymbols(1,50, sign=1).cuspidal_submodule()
        sage: T = M.hecke_operator(2)
        sage: f = T.charpoly('x')
        sage: f.newton_slopes(2)
        [13, 8, 4]

    AUTHORS:

    - Kevin Buzzard: several PARI/GP scripts

    - William Stein (2006-03-17): small Sage wrapper of Buzzard's scripts
    """
