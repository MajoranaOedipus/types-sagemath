from sage.rings.polynomial.pbori.pbori import Polynomial as Polynomial, ReductionStrategy as ReductionStrategy

def interred(l, completely: bool = False):
    """
    Compute a new generating system (g1, ...,gn),
    spanning the same ideal modulo field equations.

    The system is interreduced: For i!=j:
    gi.lead() does not divide any leading term of gj.

    If completely is set to ``True``, then also terms in the
    tail are not reducible by other polynomials.
    """
