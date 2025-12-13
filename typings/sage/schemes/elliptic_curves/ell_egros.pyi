from .constructor import EllipticCurve as EllipticCurve, EllipticCurve_from_j as EllipticCurve_from_j
from sage.misc.mrange import xmrange as xmrange
from sage.rings.rational_field import QQ as QQ

def is_possible_j(j, S=[]):
    """
    Test if the rational `j` is a possible `j`-invariant of an
    elliptic curve with good reduction outside `S`.

    .. NOTE::

        The condition used is necessary but not sufficient unless S
        contains both 2 and 3.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_egros import is_possible_j
        sage: is_possible_j(0,[])
        False
        sage: is_possible_j(1728,[])
        True
        sage: is_possible_j(-4096/11,[11])
        True
    """
def curve_key(E1):
    """
    Comparison key for elliptic curves over `\\QQ`.

    The key is a tuple:

    - if the curve is in the database: (conductor, 0, label, number)

    - otherwise: (conductor, 1, a_invariants)

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_egros import curve_key
        sage: E = EllipticCurve_from_j(1728)
        sage: curve_key(E)
        (32, 0, 0, 2)
        sage: E = EllipticCurve_from_j(1729)
        sage: curve_key(E)
        (2989441, 1, (1, 0, 0, -36, -1))
    """
def egros_from_j_1728(S=[]):
    """
    Given a list of primes S, returns a list of elliptic curves over `\\QQ`
    with j-invariant 1728 and good reduction outside S, by checking
    all relevant quartic twists.

    INPUT:

    - ``S`` -- list of primes (default: empty list)

    .. NOTE::

        Primality of elements of S is not checked, and the output
        is undefined if S is not a list or contains non-primes.

    OUTPUT:

    A sorted list of all elliptic curves defined over `\\QQ` with
    `j`-invariant equal to `1728` and with good reduction at
    all primes outside the list ``S``.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_egros import egros_from_j_1728
        sage: egros_from_j_1728([])
        []
        sage: egros_from_j_1728([3])
        []
        sage: [e.cremona_label() for e in egros_from_j_1728([2])]
        ['32a1', '32a2', '64a1', '64a4', '256b1', '256b2', '256c1', '256c2']
    """
def egros_from_j_0(S=[]):
    """
    Given a list of primes S, returns a list of elliptic curves over `\\QQ`
    with j-invariant 0 and good reduction outside S, by checking all
    relevant sextic twists.

    INPUT:

    - ``S`` -- list of primes (default: empty list)

    .. NOTE::

        Primality of elements of S is not checked, and the output
        is undefined if S is not a list or contains non-primes.

    OUTPUT:

    A sorted list of all elliptic curves defined over `\\QQ` with
    `j`-invariant equal to `0` and with good reduction at
    all primes outside the list ``S``.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_egros import egros_from_j_0
        sage: egros_from_j_0([])
        []
        sage: egros_from_j_0([2])
        []
        sage: [e.label() for e in egros_from_j_0([3])]
        ['27a1', '27a3', '243a1', '243a2', '243b1', '243b2']
        sage: len(egros_from_j_0([2,3,5]))  # long time (8s on sage.math, 2013)
        432
    """
def egros_from_j(j, S=[]):
    """
    Given a rational j and a list of primes S, returns a list of
    elliptic curves over `\\QQ` with j-invariant j and good reduction
    outside S, by checking all relevant quadratic twists.

    INPUT:

    - ``j`` -- a rational number

    - ``S`` -- list of primes (default: empty list)

    .. NOTE::

        Primality of elements of S is not checked, and the output
        is undefined if S is not a list or contains non-primes.

    OUTPUT:

    A sorted list of all elliptic curves defined over `\\QQ` with
    `j`-invariant equal to `j` and with good reduction at
    all primes outside the list ``S``.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_egros import egros_from_j
        sage: [e.label() for e in egros_from_j(0,[3])]
        ['27a1', '27a3', '243a1', '243a2', '243b1', '243b2']
        sage: [e.label() for e in egros_from_j(1728,[2])]
        ['32a1', '32a2', '64a1', '64a4', '256b1', '256b2', '256c1', '256c2']
        sage: elist=egros_from_j(-4096/11,[11])
        sage: [e.label() for e in elist]
        ['11a3', '121d1']
    """
def egros_from_jlist(jlist, S=[]):
    """
    Given a list of rational j and a list of primes S, returns a list
    of elliptic curves over `\\QQ` with j-invariant in the list and good
    reduction outside S.

    INPUT:

    - ``j`` -- list of rational numbers

    - ``S`` -- list of primes (default: empty list)

    .. NOTE::

        Primality of elements of S is not checked, and the output
        is undefined if S is not a list or contains non-primes.

    OUTPUT:

    A sorted list of all elliptic curves defined over `\\QQ` with
    `j`-invariant in the list ``jlist`` and with good reduction at
    all primes outside the list ``S``.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_egros import egros_get_j, egros_from_jlist
        sage: jlist=egros_get_j([3])
        sage: elist=egros_from_jlist(jlist,[3])
        sage: [e.label() for e in elist]
        ['27a1', '27a2', '27a3', '27a4', '243a1', '243a2', '243b1', '243b2']
        sage: [e.ainvs() for e in elist]
        [(0, 0, 1, 0, -7),
        (0, 0, 1, -270, -1708),
        (0, 0, 1, 0, 0),
        (0, 0, 1, -30, 63),
        (0, 0, 1, 0, -1),
        (0, 0, 1, 0, 20),
        (0, 0, 1, 0, 2),
        (0, 0, 1, 0, -61)]
    """
def egros_get_j(S=[], proof=None, verbose: bool = False):
    """
    Return a list of rational `j` such that all elliptic curves
    defined over `\\QQ` with good reduction outside `S` have
    `j`-invariant in the list, sorted by height.

    INPUT:

    - ``S`` -- list of primes (default: empty list)

    - ``proof`` -- boolean (default: ``True``); the MW basis for
      auxiliary curves will be computed with this proof flag

    - ``verbose`` -- boolean (default: ``False``); if ``True``, some
      details of the computation will be output

    .. NOTE::

        Proof flag: The algorithm used requires determining all
        S-integral points on several auxiliary curves, which in turn
        requires the computation of their generators.  This is not
        always possible (even in theory) using current knowledge.

        The value of this flag is passed to the function which
        computes generators of various auxiliary elliptic curves, in
        order to find their S-integral points.  Set to ``False`` if the
        default (``True``) causes warning messages, but note that you can
        then not rely on the set of invariants returned being
        complete.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.ell_egros import egros_get_j
        sage: egros_get_j([])
        [1728]
        sage: egros_get_j([2])  # long time (3s on sage.math, 2013)
        [128, 432, -864, 1728, 3375/2, -3456, 6912, 8000, 10976, -35937/4, 287496, -784446336, -189613868625/128]
        sage: egros_get_j([3])  # long time (3s on sage.math, 2013)
        [0, -576, 1536, 1728, -5184, -13824, 21952/9, -41472, 140608/3, -12288000]
        sage: jlist=egros_get_j([2,3]); len(jlist) # long time (30s)
        83
    """
