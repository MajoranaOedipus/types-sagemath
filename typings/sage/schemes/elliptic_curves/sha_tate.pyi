import sage.arith.all as arith
from _typeshed import Incomplete
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.verbose import verbose as verbose
from sage.modules.free_module_element import vector as vector
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import Q as Q
from sage.rings.real_mpfi import RIF as RIF
from sage.rings.real_mpfr import RealField as RealField
from sage.structure.sage_object import SageObject as SageObject

factor = arith.factor
valuation = arith.valuation

class Sha(SageObject):
    """
    The Tate-Shafarevich group associated to an elliptic curve.

    If `E` is an elliptic curve over a global field `K`, the Tate-Shafarevich
    group is the subgroup of elements in `H^1(K,E)` which map to zero under
    every global-to-local restriction map `H^1(K,E) \\to H^1(K_v,E)`, one for
    each place `v` of `K`.

    EXAMPLES::

        sage: E = EllipticCurve('571a1')
        sage: E._set_gens([])   # curve has rank 0, but non-trivial Sha[2]
        sage: S = E.sha()
        sage: S.bound_kato()
        [2]
        sage: S.bound_kolyvagin()
        ([2], 1)
        sage: S.an_padic(7,3)
        4 + O(7^5)
        sage: S.an()
        4
        sage: S.an_numerical()
        4.00000000000000

        sage: E = EllipticCurve('389a')
        sage: S = E.sha(); S
        Tate-Shafarevich group for the
         Elliptic Curve defined by y^2 + y = x^3 + x^2 - 2*x over Rational Field
        sage: S.an_numerical()
        1.00000000000000
        sage: S.p_primary_bound(5)  # long time
        0
        sage: S.an_padic(5)         # long time
        1 + O(5)
        sage: S.an_padic(5,prec=4)  # very long time
        1 + O(5^3)
    """
    E: Incomplete
    Emin: Incomplete
    def __init__(self, E) -> None:
        """
        The Tate-Shafarevich group associated to an elliptic curve.

        INPUT:

        - ``E`` -- an elliptic curve over `\\QQ`

        EXAMPLES::

            sage: E = EllipticCurve('11a1')
            sage: S = E.sha()
            sage: S
            Tate-Shafarevich group for the
             Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field

            sage: S == loads(dumps(S))
            True
        """
    def __eq__(self, other):
        """
        Compare two Tate-Shafarevich groups by simply comparing the
        elliptic curves.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: S = E.sha()
            sage: S == S
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: E = EllipticCurve('37a1')
            sage: S = E.sha()
            sage: S != S
            False
        """
    def an_numerical(self, prec=None, use_database: bool = True, proof=None):
        """
        Return the numerical analytic order of `Sha`, which is
        a floating point number in all cases.

        INPUT:

        - ``prec`` -- integer (default: 53); bits precision -- used
          for the `L`-series computation, period,  regulator, etc.
        - ``use_database`` -- whether the rank and generators should
          be looked up in the database if possible. Default is ``True``
        - ``proof`` -- boolean or ``None`` (default: ``None``, see proof.[tab] or
          sage.structure.proof) proof option passed
          onto regulator and rank computation.

        .. NOTE::

            See also the :meth:`an` command, which will return a
            provably correct integer when the rank is 0 or 1.

        .. WARNING::

            If the curve's generators are not known, computing
            them may be very time-consuming.  Also, computation of the
            `L`-series derivative will be time-consuming for large rank and
            large conductor, and the computation time for this may
            increase substantially at greater precision.  However, use of
            very low precision less than about 10 can cause the underlying
            PARI library functions to fail.

        EXAMPLES::

            sage: EllipticCurve('11a').sha().an_numerical()
            1.00000000000000
            sage: EllipticCurve('37a').sha().an_numerical()
            1.00000000000000
            sage: EllipticCurve('389a').sha().an_numerical()
            1.00000000000000
            sage: EllipticCurve('66b3').sha().an_numerical()
            4.00000000000000
            sage: EllipticCurve('5077a').sha().an_numerical()
            1.00000000000000

        A rank 4 curve::

            sage: EllipticCurve([1, -1, 0, -79, 289]).sha().an_numerical()  # long time (3s on sage.math, 2011)
            1.00000000000000

        A rank 5 curve::

            sage: EllipticCurve([0, 0, 1, -79, 342]).sha().an_numerical(prec=10, proof=False)  # long time (22s on sage.math, 2011)
            1.0

        See :issue:`1115`::

            sage: sha = EllipticCurve('37a1').sha()
            sage: [sha.an_numerical(prec) for prec in range(40,100,10)]  # long time (3s on sage.math, 2013)
            [1.0000000000,
             1.0000000000000,
             1.0000000000000000,
             1.0000000000000000000,
             1.0000000000000000000000,
             1.0000000000000000000000000]
        """
    def an(self, use_database: bool = False, descent_second_limit: int = 12):
        '''
        Return the Birch and Swinnerton-Dyer conjectural order of `Sha`
        as a provably correct integer, unless the analytic rank is > 1,
        in which case this function returns a numerical value.

        INPUT:

        - ``use_database`` -- boolean (default: ``False``); if ``True``, try
          to use any databases installed to lookup the analytic order of
          `Sha`, if possible.  The order of `Sha` is computed if it cannot
          be looked up.

        - ``descent_second_limit`` -- integer (default: 12); limit to use on
          point searching for the quartic twist in the hard case

        This result is proved correct if the order of vanishing is 0
        and the Manin constant is <= 2.

        If the optional parameter ``use_database`` is ``True`` (default:
        ``False``), this function returns the analytic order of `Sha` as
        listed in Cremona\'s tables, if this curve appears in Cremona\'s
        tables.

        NOTE:

        If you come across the following error::

            sage: E = EllipticCurve([0, 0, 1, -34874, -2506691])
            sage: E.sha().an()
            Traceback (most recent call last):
            ...
            RuntimeError: Unable to compute the rank, hence generators, with certainty
            (lower bound=0, generators found=()).  This could be because Sha(E/Q)[2] is
            nontrivial. Try increasing descent_second_limit then trying this command again.

        You can increase the ``descent_second_limit`` (in the above example,
        set to the default, 12) option to try again::

            sage: E.sha().an(descent_second_limit=16)  # long time (2s on sage.math, 2011)
            1

        EXAMPLES::

            sage: E = EllipticCurve([0, -1, 1, -10, -20])   # 11A  = X_0(11)
            sage: E.sha().an()
            1
            sage: E = EllipticCurve([0, -1, 1, 0, 0])       # X_1(11)
            sage: E.sha().an()
            1

            sage: EllipticCurve(\'14a4\').sha().an()
            1
            sage: EllipticCurve(\'14a4\').sha().an(use_database=True)   # will be faster if you have large Cremona database installed
            1

        The smallest conductor curve with nontrivial `Sha`::

            sage: E = EllipticCurve([1,1,1,-352,-2689])     # 66b3
            sage: E.sha().an()
            4

        The four optimal quotients with nontrivial `Sha` and conductor <= 1000::

            sage: E = EllipticCurve([0, -1, 1, -929, -10595])       # 571A
            sage: E.sha().an()
            4
            sage: E = EllipticCurve([1, 1, 0, -1154, -15345])       # 681B
            sage: E.sha().an()
            9
            sage: E = EllipticCurve([0, -1, 0, -900, -10098])       # 960D
            sage: E.sha().an()
            4
            sage: E = EllipticCurve([0, 1, 0, -20, -42])            # 960N
            sage: E.sha().an()
            4

        The smallest conductor curve of rank > 1::

            sage: E = EllipticCurve([0, 1, 1, -2, 0])       # 389A (rank 2)
            sage: E.sha().an()
            1.00000000000000

        The following are examples that require computation of the Mordell-
        Weil group and regulator::

            sage: E = EllipticCurve([0, 0, 1, -1, 0])                     # 37A  (rank 1)
            sage: E.sha().an()
            1

            sage: E = EllipticCurve("1610f3")
            sage: E.sha().an()
            4

        In this case the input curve is not minimal, and if this function did
        not transform it to be minimal, it would give nonsense::

            sage: E = EllipticCurve([0, -432*6^2])
            sage: E.sha().an()
            1

        See :issue:`10096`: this used to give the wrong result 6.0000
        before since the minimal model was not used::

            sage: E = EllipticCurve([1215*1216, 0]) # non-minimal model
            sage: E.sha().an()  # long time (2s on sage.math, 2011)
            1.00000000000000
            sage: E.minimal_model().sha().an()  # long time (1s on sage.math, 2011)
            1.00000000000000
        '''
    def an_padic(self, p, prec: int = 0, use_twists: bool = True):
        """
        Return the conjectural order of `Sha(E/\\QQ)`,
        according to the `p`-adic analogue of the Birch
        and Swinnerton-Dyer conjecture as formulated
        in [MTT1986]_ and [BP1993]_.

        INPUT:

        - ``p`` -- a prime > 3

        - ``prec`` -- (optional) the precision used in the computation of the
          `p`-adic L-Series

        - ``use_twists`` -- boolean (default: ``True``); if ``True`` the algorithm may
          change to a quadratic twist with minimal conductor to do the modular
          symbol computations rather than using the modular symbols of the
          curve itself. If ``False`` it forces the computation using the
          modular symbols of the curve itself.

        OUTPUT: `p`-adic number - that conjecturally equals `\\# Sha(E/\\QQ)`.

        If ``prec`` is set to zero (default) then the precision is set so that
        at least the first `p`-adic digit of conjectural `\\# Sha(E/\\QQ)` is
        determined.

        EXAMPLES:

        Good ordinary examples::

            sage: EllipticCurve('11a1').sha().an_padic(5)    # rank 0
            1 + O(5^22)
            sage: EllipticCurve('43a1').sha().an_padic(5)    # rank 1
            1 + O(5)
            sage: EllipticCurve('389a1').sha().an_padic(5,4) # rank 2, long time (2s on sage.math, 2011)
            1 + O(5^3)
            sage: EllipticCurve('858k2').sha().an_padic(7)   # rank 0, non trivial sha, long time (10s on sage.math, 2011)
            7^2 + O(7^24)
            sage: EllipticCurve('300b2').sha().an_padic(3)   # 9 elements in sha, long time (2s on sage.math, 2011)
            3^2 + O(3^24)
            sage: EllipticCurve('300b2').sha().an_padic(7, prec=6)  # long time
            2 + 7 + O(7^8)

        Exceptional cases::

            sage: EllipticCurve('11a1').sha().an_padic(11) # rank 0
            1 + O(11^22)
            sage: EllipticCurve('130a1').sha().an_padic(5) # rank 1
            1 + O(5)

        Non-split, but rank 0 case (:issue:`7331`)::

            sage: EllipticCurve('270b1').sha().an_padic(5) # rank 0, long time (2s on sage.math, 2011)
            1 + O(5^22)

        The output has the correct sign::

            sage: EllipticCurve('123a1').sha().an_padic(41) # rank 1, long time (3s on sage.math, 2011)
            1 + O(41)

        Supersingular cases::

            sage: EllipticCurve('34a1').sha().an_padic(5) # rank 0
            1 + O(5^22)
            sage: EllipticCurve('53a1').sha().an_padic(5) # rank 1, long time (11s on sage.math, 2011)
            1 + O(5)

        Cases that use a twist to a lower conductor::

            sage: EllipticCurve('99a1').sha().an_padic(5)
            1 + O(5)
            sage: EllipticCurve('240d3').sha().an_padic(5)  # sha has 4 elements here
            4 + O(5)
            sage: EllipticCurve('448c5').sha().an_padic(7, prec=4, use_twists=False)  # long time (2s on sage.math, 2011)
            2 + 7 + O(7^6)
            sage: EllipticCurve([-19,34]).sha().an_padic(5)  # see trac #6455, long time (4s on sage.math, 2011)
            1 + O(5)

        Test for :issue:`15737`::

            sage: E = EllipticCurve([-100,0])
            sage: s = E.sha()
            sage: s.an_padic(13)
            1 + O(13^20)
        """
    def p_primary_order(self, p):
        '''
        Return the order of the `p`-primary part of the Tate-Shafarevich
        group.

        This uses the result of Skinner and Urban [SU2014]_ on the
        main conjecture in Iwasawa theory. In particular the elliptic
        curve must have good ordinary reduction at `p`, the residual
        Galois representation must be surjective. Furthermore there must
        be an auxiliary prime `\\ell` dividing the conductor of the curve
        exactly once such that the residual representation is ramified
        at `p`.

        INPUT:

        - ``p`` -- an odd prime

        OUTPUT:

        - ``e`` -- nonnegative integer such that `p^e` is the
          order of the `p`-primary order if the conditions are satisfied
          and raises a :exc:`ValueError` otherwise.

        EXAMPLES::

            sage: E = EllipticCurve("389a1")  # rank 2
            sage: E.sha().p_primary_order(5)
            0
            sage: E = EllipticCurve("11a1")
            sage: E.sha().p_primary_order(7)
            0
            sage: E.sha().p_primary_order(5)
            Traceback (most recent call last):
            ...
            ValueError: The order is not provably known using Skinner-Urban.
            Try running p_primary_bound to get a bound.
        '''
    def p_primary_bound(self, p):
        '''
        Return a provable upper bound for the order of the
        `p`-primary part `Sha(E)(p)` of the Tate-Shafarevich group.

        INPUT:

        - ``p`` -- a prime > 2

        OUTPUT:

        - ``e`` -- nonnegative integer such that `p^e` is an upper
          bound for the order of `Sha(E)(p)`

        In particular, if this algorithm does not fail, then it proves
        that the `p`-primary part of `Sha` is finite. This works also
        for curves of rank > 1.

        Note also that this bound is sharp if one assumes the main conjecture
        of Iwasawa theory of elliptic curves. One may use the method
        ``p_primary_order`` for checking if the extra conditions hold under
        which the main conjecture is known by the work of Skinner and Urban.
        This then returns the provable `p`-primary part of the Tate-Shafarevich
        group.

        Currently the algorithm is only implemented when the following
        conditions are verified:

        - The `p`-adic Galois representation must be surjective or
          must have its image contained in a Borel subgroup.

        - The reduction at `p` is not allowed to be additive.

        - If the reduction at `p` is non-split multiplicative, then
          the rank must be 0.

        - If `p = 3`, then the reduction at 3 must be good ordinary or
          split multiplicative, and the rank must be 0.

        ALGORITHM:

        The algorithm is described in [SW2013]_. The results for the
        reducible case can be found in [Wu2004]_. The main ingredient is
        Kato\'s result on the main conjecture in Iwasawa theory.

        EXAMPLES::

            sage: e = EllipticCurve(\'11a3\')
            sage: e.sha().p_primary_bound(3)
            0
            sage: e.sha().p_primary_bound(5)
            0
            sage: e.sha().p_primary_bound(7)
            0
            sage: e.sha().p_primary_bound(11)
            0
            sage: e.sha().p_primary_bound(13)
            0

            sage: e = EllipticCurve(\'389a1\')
            sage: e.sha().p_primary_bound(5)
            0
            sage: e.sha().p_primary_bound(7)
            0
            sage: e.sha().p_primary_bound(11)
            0
            sage: e.sha().p_primary_bound(13)
            0

            sage: e = EllipticCurve(\'858k2\')
            sage: e.sha().p_primary_bound(3)  # long time (10s on sage.math, 2011)
            0

        Some checks for :issue:`6406` and :issue:`16959`::

            sage: e.sha().p_primary_bound(7)  # long time
            2

            sage: E = EllipticCurve(\'608b1\')
            sage: E.sha().p_primary_bound(5)
            Traceback (most recent call last):
            ...
            ValueError: The p-adic Galois representation is not surjective or reducible.
            Current knowledge about Euler systems does not provide an upper bound
            in this case. Try an_padic for a conjectural bound.

            sage: E.sha().an_padic(5)           # long time
            1 + O(5^22)

            sage: E = EllipticCurve("5040bi1")
            sage: E.sha().p_primary_bound(5)    # long time
            0
        '''
    def two_selmer_bound(self):
        """
        Return the 2-rank, i.e. the `\\GF{2}`-dimension
        of the 2-torsion part of `Sha`, provided we can determine the
        rank of `E`.

        EXAMPLES::

            sage: sh = EllipticCurve('571a1').sha()
            sage: sh.two_selmer_bound()
            2
            sage: sh.an()
            4

            sage: sh = EllipticCurve('66a1').sha()
            sage: sh.two_selmer_bound()
            0
            sage: sh.an()
            1

            sage: sh = EllipticCurve('960d1').sha()
            sage: sh.two_selmer_bound()
            2
            sage: sh.an()
            4
        """
    def bound_kolyvagin(self, D: int = 0, regulator=None, ignore_nonsurj_hypothesis: bool = False):
        '''
        Given a fundamental discriminant `D \\neq -3,-4` that satisfies the
        Heegner hypothesis for `E`, return a list of primes so that
        Kolyvagin\'s theorem (as in Gross\'s paper) implies that any
        prime divisor of `Sha` is in this list.

        INPUT:

        - ``D`` -- (optional) a fundamental discriminant < -4 that satisfies
          the Heegner hypothesis for `E`; if not given, use the first such `D`
        - ``regulator`` -- (optional) regulator of `E(K)`; if not given, will
          be computed (which could take a long time)
        - ``ignore_nonsurj_hypothesis`` -- (default: ``False``);
          if ``True``, then gives the bound coming from Heegner point
          index, but without any hypothesis on surjectivity
          of the mod-`p` representation

        OUTPUT:

        - ``list`` -- list of primes such that if `p` divides `Sha(E/K)`, then
          `p` is in this list, unless `E/K` has complex multiplication or
          analytic rank greater than 2 (in which case we return 0)

        - ``index`` -- the odd part of the index of the Heegner point in the full
          group of `K`-rational points on `E` (if `E` has CM, returns 0)

        REMARKS:

        1)      We do not have to assume that the Manin constant is 1
                (or a power of 2).  If the Manin constant were
                divisible by a prime, that prime would get included in
                the list of bad primes.

        2)      We assume the Gross-Zagier theorem is true under the
                hypothesis that `gcd(N,D) = 1`, instead of the stronger
                hypothesis `gcd(2\\cdot N,D)=1` that is in the original
                Gross-Zagier paper.  That Gross-Zagier is true when
                `gcd(N,D)=1` is "well-known" to the experts, but does not
                seem to written up well in the literature.

        3)      Correctness of the computation is guaranteed using
                interval arithmetic, under the assumption that the
                regulator, square root, and period lattice are
                computed to precision at least `10^{-10}`, i.e., they are
                correct up to addition or a real number with absolute
                value less than `10^{-10}`.

        EXAMPLES::

            sage: E = EllipticCurve(\'37a\')
            sage: E.sha().bound_kolyvagin()
            ([2], 1)
            sage: E = EllipticCurve(\'141a\')
            sage: E.sha().an()
            1
            sage: E.sha().bound_kolyvagin()
            ([2, 7], 49)

        We get no information when the curve has rank 2.::

            sage: E = EllipticCurve(\'389a\')
            sage: E.sha().bound_kolyvagin()
            (0, 0)
            sage: E = EllipticCurve(\'681b\')
            sage: E.sha().an()
            9
            sage: E.sha().bound_kolyvagin()
            ([2, 3], 9)
        '''
    def bound_kato(self):
        """
        Return a list of primes `p` such that the theorems of Kato's [Kat2004]_
        and others (e.g., as explained in a thesis of Grigor Grigorov [Gri2005]_)
        imply that if `p` divides  the order of `Sha(E/\\QQ)` then `p` is in
        the list.

        If `L(E,1) = 0`, then this function gives no information, so
        it returns ``False``.

        THEOREM: Suppose `L(E,1) \\neq 0` and `p \\neq 2` is a prime such
        that

        - `E` does not have additive reduction at `p`,
        - either the `p`-adic representation is surjective or has its
          image contained in a Borel subgroup.

        Then `{ord}_p(\\#Sha(E))` is bounded from above by the `p`-adic valuation of  `L(E,1)\\cdot\\#E(\\QQ)_{tor}^2 / (\\Omega_E \\cdot \\prod c_v)`.

        If the `L`-series vanishes, the method ``p_primary_bound`` can be used instead.

        EXAMPLES::

            sage: E = EllipticCurve([0, -1, 1, -10, -20])   # 11A  = X_0(11)
            sage: E.sha().bound_kato()
            [2]
            sage: E = EllipticCurve([0, -1, 1, 0, 0])       # X_1(11)
            sage: E.sha().bound_kato()
            [2]
            sage: E = EllipticCurve([1,1,1,-352,-2689])     # 66B3
            sage: E.sha().bound_kato()
            [2]

        For the following curve one really has that 25 divides the
        order of `Sha` (by [GJPST2009]_)::

            sage: E = EllipticCurve([1, -1, 0, -332311, -73733731])   # 1058D1
            sage: E.sha().bound_kato()                        # long time (about 1 second)
            [2, 5, 23]
            sage: E.galois_representation().non_surjective()  # long time (about 1 second)
            []

        For this one, `Sha` is divisible by 7::

            sage: E = EllipticCurve([0, 0, 0, -4062871, -3152083138])   # 3364C1
            sage: E.sha().bound_kato()                        # long time (< 10 seconds)
            [2, 7, 29]

        No information about curves of rank > 0::

            sage: E = EllipticCurve([0, 0, 1, -1, 0])       # 37A  (rank 1)
            sage: E.sha().bound_kato()
            False
        """
    def bound(self):
        """
        Compute a provably correct bound on the order of the Tate-Shafarevich
        group of this curve.

        The bound is either ``False`` (no bound) or a list ``B`` of primes
        such that any prime divisor of the order of `Sha` is in this list.

        EXAMPLES::

            sage: EllipticCurve('37a').sha().bound()
            ([2], 1)
        """
