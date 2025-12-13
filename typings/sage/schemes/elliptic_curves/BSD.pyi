from _typeshed import Incomplete
from sage.arith.misc import prime_divisors as prime_divisors
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ

class BSD_data:
    """
    Helper class used to keep track of information in proving BSD.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.BSD import BSD_data
        sage: D = BSD_data()
        sage: D.Sha is None
        True
        sage: D.curve=EllipticCurve('11a')
        sage: D.update()
        sage: D.Sha
        Tate-Shafarevich group for the Elliptic Curve
         defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
    """
    curve: Incomplete
    two_tor_rk: Incomplete
    Sha: Incomplete
    sha_an: Incomplete
    N: Incomplete
    rank: Incomplete
    gens: Incomplete
    bounds: Incomplete
    primes: Incomplete
    heegner_indexes: Incomplete
    heegner_index_upper_bound: Incomplete
    N_factorization: Incomplete
    proof: Incomplete
    def __init__(self) -> None: ...
    def update(self) -> None:
        """
        Update some properties from ``curve``.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.BSD import BSD_data
            sage: D = BSD_data()
            sage: D.Sha is None
            True
            sage: D.curve = EllipticCurve('11a')
            sage: D.update()
            sage: D.Sha
            Tate-Shafarevich group for the Elliptic Curve
             defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field
        """

def mwrank_two_descent_work(E, two_tor_rk) -> tuple:
    """
    Prepare the output from mwrank two-descent.

    INPUT:

    - ``E`` -- an elliptic curve

    - ``two_tor_rk`` -- its two-torsion rank

    OUTPUT:

    - a lower bound on the rank

    - an upper bound on the rank

    - a lower bound on the rank of Sha[2]

    - an upper bound on the rank of Sha[2]

    - a list of the generators found

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.BSD import mwrank_two_descent_work
        sage: E = EllipticCurve('14a')
        sage: mwrank_two_descent_work(E, E.two_torsion_rank())
        (0, 0, 0, 0, [])
        sage: E = EllipticCurve('37a')
        sage: mwrank_two_descent_work(E, E.two_torsion_rank())
        (1, 1, 0, 0, [(0 : -1 : 1)])
    """
def pari_two_descent_work(E) -> tuple:
    """
    Prepare the output from pari by two-isogeny.

    INPUT:

    - ``E`` -- an elliptic curve

    OUTPUT: a tuple of 5 elements with the first 4 being integers

    - a lower bound on the rank

    - an upper bound on the rank

    - a lower bound on the rank of Sha[2]

    - an upper bound on the rank of Sha[2]

    - a list of the generators found

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.BSD import pari_two_descent_work
        sage: E = EllipticCurve('14a')
        sage: pari_two_descent_work(E)
        (0, 0, 0, 0, [])
        sage: E = EllipticCurve('37a')
        sage: pari_two_descent_work(E) # random, up to sign
        (1, 1, 0, 0, [(0 : -1 : 1)])
        sage: E = EllipticCurve('210e7')
        sage: pari_two_descent_work(E)
        (0, 2, 0, 2, [])
        sage: E = EllipticCurve('66b3')
        sage: pari_two_descent_work(E)
        (0, 0, 2, 2, [])
    """
def native_two_isogeny_descent_work(E, two_tor_rk) -> tuple:
    """
    Prepare the output from two-descent by two-isogeny.

    INPUT:

    - ``E`` -- an elliptic curve

    - ``two_tor_rk`` -- its two-torsion rank

    OUTPUT:

    - a lower bound on the rank

    - an upper bound on the rank

    - a lower bound on the rank of Sha[2]

    - an upper bound on the rank of Sha[2]

    - a list of the generators found
      (currently ``None``, since we do not store them)

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.BSD import native_two_isogeny_descent_work
        sage: E = EllipticCurve('14a')
        sage: native_two_isogeny_descent_work(E, E.two_torsion_rank())
        (0, 0, 0, 0, None)
        sage: E = EllipticCurve('65a')
        sage: native_two_isogeny_descent_work(E, E.two_torsion_rank())
        (1, 1, 0, 0, None)
    """
def heegner_index_work(E) -> tuple:
    """
    Prepare the input and output for computing the Heegner index.

    INPUT:

    - ``E`` -- an elliptic curve

    OUTPUT:

    - a Heegner index

    - the discriminant used

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.BSD import heegner_index_work
        sage: heegner_index_work(EllipticCurve('14a'))
        (1, -31)
    """
def prove_BSD(E, verbosity: int = 0, two_desc: str = 'mwrank', proof=None, secs_hi: int = 5, return_BSD: bool = False):
    '''
    Attempt to prove the Birch and Swinnerton-Dyer conjectural
    formula for `E`, returning a list of primes `p` for which this
    function fails to prove BSD(E,p).

    Here, BSD(E,p) is the
    statement: "the Birch and Swinnerton-Dyer formula holds up to a
    rational number coprime to `p`."

    INPUT:

    - ``E`` -- an elliptic curve

    - ``verbosity`` -- integer; how much information about the proof to print

      - 0: print nothing
      - 1: print sketch of proof
      - 2: print information about remaining primes

    - ``two_desc`` -- string (default: ``\'mwrank\'``); what to use for the
      two-descent. Options are ``\'mwrank\', \'pari\', \'sage\'``.

    - ``proof`` -- boolean or ``None`` (default: None, see
      proof.elliptic_curve or sage.structure.proof). If ``False``, this
      function just immediately returns the empty list.

    - ``secs_hi`` -- maximum number of seconds to try to compute the
      Heegner index before switching over to trying to compute the
      Heegner index bound. (Rank 0 only!)

    - ``return_BSD`` -- boolean (default: ``False``); whether to return an object
      which contains information to reconstruct a proof

    .. NOTE::

        When printing verbose output, phrases such as "by Mazur" are referring
        to the following list of papers:

    REFERENCES:

    - [Cha2005]_
    - [Jet2008]_
    - [Kat2004]_
    - [Kol1991]_
    - [LW2015]_
    - [LS]_
    - [Maz1978]_
    - [Rub1991]_
    - [SW2013]_
    - [GJPST2009]_

    EXAMPLES::

        sage: EllipticCurve(\'11a\').prove_BSD(verbosity=2)
        p = 2: True by 2-descent
        True for p not in {2, 5} by Kolyvagin.
        Kolyvagin\'s bound for p = 5 applies by Lawson-Wuthrich
        True for p = 5 by Kolyvagin bound
        []

        sage: EllipticCurve(\'14a\').prove_BSD(verbosity=2)
        p = 2: True by 2-descent
        True for p not in {2, 3} by Kolyvagin.
        Kolyvagin\'s bound for p = 3 applies by Lawson-Wuthrich
        True for p = 3 by Kolyvagin bound
        []

        sage: E = EllipticCurve("20a1")
        sage: E.prove_BSD(verbosity=2)
        p = 2: True by 2-descent
        True for p not in {2, 3} by Kolyvagin.
        Kato further implies that #Sha[3] is trivial.
        []

        sage: E = EllipticCurve("50b1")
        sage: E.prove_BSD(verbosity=2)
        p = 2: True by 2-descent
        True for p not in {2, 3, 5} by Kolyvagin.
        Kolyvagin\'s bound for p = 3 applies by Lawson-Wuthrich
        Kolyvagin\'s bound for p = 5 applies by Lawson-Wuthrich
        True for p = 3 by Kolyvagin bound
        True for p = 5 by Kolyvagin bound
        []
        sage: E.prove_BSD(two_desc=\'pari\')
        []

    A rank two curve::

        sage: E = EllipticCurve(\'389a\')

    We know nothing with proof=True::

        sage: E.prove_BSD()
        Set of all prime numbers: 2, 3, 5, 7, ...

    We (think we) know everything with proof=False::

        sage: E.prove_BSD(proof=False)
        []

    A curve of rank 0 and prime conductor::

        sage: E = EllipticCurve(\'19a\')
        sage: E.prove_BSD(verbosity=2)
        p = 2: True by 2-descent
        True for p not in {2, 3} by Kolyvagin.
        Kolyvagin\'s bound for p = 3 applies by Lawson-Wuthrich
        True for p = 3 by Kolyvagin bound
        []

        sage: E = EllipticCurve(\'37a\')
        sage: E.rank()
        1
        sage: E._EllipticCurve_rational_field__rank
        (1, True)
        sage: E.analytic_rank = lambda : 0
        sage: E.prove_BSD()
        Traceback (most recent call last):
        ...
        RuntimeError: It seems that the rank conjecture does not hold for this curve
        (Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field)!
        This may be a counterexample to BSD, but is more likely a bug.

    We test the consistency check for the 2-part of Sha::

        sage: E = EllipticCurve(\'37a\')
        sage: S = E.sha(); S
        Tate-Shafarevich group for the Elliptic Curve defined by y^2 + y = x^3 - x
         over Rational Field
        sage: def foo(use_database):
        ....:  return 4
        sage: S.an = foo
        sage: E.prove_BSD()
        Traceback (most recent call last):
        ...
        RuntimeError: Apparent contradiction: 0 <= rank(sha[2]) <= 0, but ord_2(sha_an) = 2

    An example with a Tamagawa number at 5::

        sage: E = EllipticCurve(\'123a1\')
        sage: E.prove_BSD(verbosity=2)
        p = 2: True by 2-descent
        True for p not in {2, 5} by Kolyvagin.
        Kolyvagin\'s bound for p = 5 applies by Lawson-Wuthrich
        True for p = 5 by Kolyvagin bound
        []

    A curve for which 3 divides the order of the Tate-Shafarevich group::

        sage: E = EllipticCurve(\'681b\')
        sage: E.prove_BSD(verbosity=2)               # long time
        p = 2: True by 2-descent...
        True for p not in {2, 3} by Kolyvagin....
        Remaining primes:
        p = 3: irreducible, surjective, non-split multiplicative
            (0 <= ord_p <= 2)
            ord_p(#Sha_an) = 2
        [3]

    A curve for which we need to use ``heegner_index_bound``::

        sage: E = EllipticCurve(\'198b\')
        sage: E.prove_BSD(verbosity=1, secs_hi=1)
        p = 2: True by 2-descent
        True for p not in {2, 3} by Kolyvagin.
        [3]

    The ``return_BSD`` option gives an object with detailed information
    about the proof::

        sage: E = EllipticCurve(\'26b\')
        sage: B = E.prove_BSD(return_BSD=True)
        sage: B.two_tor_rk
        0
        sage: B.N
        26
        sage: B.gens
        []
        sage: B.primes
        []
        sage: B.heegner_indexes
        {-23: 2}

    TESTS:

    This was fixed by :issue:`8184` and :issue:`7575`::

        sage: EllipticCurve(\'438e1\').prove_BSD(verbosity=1)
        p = 2: True by 2-descent...
        True for p not in {2} by Kolyvagin.
        []

    ::

        sage: E = EllipticCurve(\'960d1\')
        sage: E.prove_BSD(verbosity=1)  # long time (4s on sage.math, 2011)
        p = 2: True by 2-descent
        True for p not in {2} by Kolyvagin.
        []

    ::

        sage: E = EllipticCurve(\'66b3\')
        sage: E.prove_BSD(two_desc="pari",verbosity=1)
        p = 2: True by 2-descent
        True for p not in {2} by Kolyvagin.
        []
    '''
