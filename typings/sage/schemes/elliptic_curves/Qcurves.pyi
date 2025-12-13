from sage.rings.polynomial.polynomial_ring import polygen as polygen
from sage.rings.rational_field import QQ as QQ

def is_Q_curve(E, maxp: int = 100, certificate: bool = False, verbose: bool = False):
    '''
    Return whether ``E`` is a `\\QQ`-curve, with optional certificate.

    INPUT:

    - ``E`` -- elliptic curve over a number field

    - ``maxp`` -- integer (default: 100); bound on primes used for checking
      necessary local conditions.  The result will not depend on this,
      but using a larger value may return ``False`` faster.

    - ``certificate`` -- boolean (default: ``False``); if ``True`` then a
      second value is returned giving a certificate for the
      `\\QQ`-curve property

    OUTPUT:

    If ``certificate`` is ``False``: either ``True`` (if `E` is a
    `\\QQ`-curve), or ``False``.

    If ``certificate`` is ``True``: a tuple consisting of a boolean
    flag as before and a certificate, defined as follows:

    - when the flag is ``True``, so `E` is a `\\QQ`-curve:

      - either {\'CM\':`D`} where `D` is a negative discriminant, when
        `E` has potential CM with discriminant `D`;

      - otherwise {\'CM\': `0`, \'core_poly\': `f`, \'rho\': `\\rho`, \'r\':
        `r`, \'N\': `N`}, when `E` is a non-CM `\\QQ`-curve, where the
        core polynomial `f` is an irreducible monic polynomial over
        `QQ` of degree `2^\\rho`, all of whose roots are
        `j`-invariants of curves isogenous to `E`, the core level
        `N` is a square-free integer with `r` prime factors which is
        the LCM of the degrees of the isogenies between these
        conjugates.  For example, if there exists a curve `E\'`
        isogenous to `E` with `j(E\')=j\\in\\QQ`, then the certificate
        is {\'CM\':0, \'r\':0, \'rho\':0, \'core_poly\': x-j, \'N\':1}.

    - when the flag is ``False``, so `E` is not a `\\QQ`-curve, the
      certificate is a prime `p` such that the reductions of `E` at
      the primes dividing `p` are inconsistent with the property of
      being a `\\QQ`-curve.  See the ALGORITHM section for details.

    ALGORITHM:

    See [CrNa2020]_ for details.

    1. If `E` has rational `j`-invariant, or has CM, then return
    ``True``.

    2. Replace `E` by a curve defined over `K=\\QQ(j(E))`. Let `N` be
    the conductor norm.

    3. For all primes `p\\mid N` check that the valuations of `j` at
    all `P\\mid p` are either all negative or all nonnegative; if not,
    return ``False``.

    4. For `p\\le maxp`, `p\\not\\mid N`, check that either `E` is
    ordinary mod `P` for all `P\\mid p`, or `E` is supersingular mod
    `P` for all `P\\mid p`; if neither, return ``False``.  If all are
    ordinary, check that the integers `a_P(E)^2-4N(P)` have the same
    square-free part; if not, return ``False``.

    5. Compute the `K`-isogeny class of `E` using the "heuristic"
    option (which is faster, but not guaranteed to be complete).
    Check whether the set of `j`-invariants of curves in the class of
    `2`-power degree contains a complete Galois orbit.  If so, return
    ``True``.

    6. Otherwise repeat step 4 for more primes, and if still
    undecided, repeat Step 5 without the "heuristic" option, to get
    the complete `K`-isogeny class (which will probably be no bigger
    than before).  Now return ``True`` if the set of `j`-invariants of
    curves in the class contains a complete Galois orbit, otherwise
    return ``False``.

    EXAMPLES:

    A non-CM curve over `\\QQ` and a CM curve over `\\QQ` are both
    trivially `\\QQ`-curves::

        sage: from sage.schemes.elliptic_curves.Qcurves import is_Q_curve
        sage: E = EllipticCurve([1,2,3,4,5])
        sage: flag, cert = is_Q_curve(E, certificate=True)
        sage: flag
        True
        sage: cert
        {\'CM\': 0, \'N\': 1, \'core_poly\': x, \'r\': 0, \'rho\': 0}

        sage: E = EllipticCurve(j=8000)
        sage: flag, cert = is_Q_curve(E, certificate=True)
        sage: flag
        True
        sage: cert
        {\'CM\': -8}

    A non-`\\QQ`-curve over a quartic field.  The local data at bad
    primes above `3` is inconsistent::

        sage: from sage.schemes.elliptic_curves.Qcurves import is_Q_curve
        sage: R.<x> = PolynomialRing(QQ)
        sage: K.<a> = NumberField(R([3, 0, -5, 0, 1]))                                  # needs sage.rings.number_field
        sage: E = EllipticCurve([K([-3,-4,1,1]), K([4,-1,-1,0]), K([-2,0,1,0]),         # needs sage.rings.number_field
        ....:                    K([-621,778,138,-178]), K([9509,2046,-24728,10380])])
        sage: is_Q_curve(E, certificate=True, verbose=True)                             # needs sage.rings.number_field
        Checking whether Elliptic Curve defined by y^2 + (a^3+a^2-4*a-3)*x*y + (a^2-2)*y = x^3 + (-a^2-a+4)*x^2 + (-178*a^3+138*a^2+778*a-621)*x + (10380*a^3-24728*a^2+2046*a+9509) over Number Field in a with defining polynomial x^4 - 5*x^2 + 3 is a Q-curve
        No: inconsistency at the 2 primes dividing 3
        - potentially multiplicative: [True, False]
        (False, 3)

    A non-`\\QQ`-curve over a quadratic field.  The local data at bad
    primes is consistent, but the local test at good primes above `13`
    is not::

        sage: K.<a> = NumberField(R([-10, 0, 1]))                                       # needs sage.rings.number_field
        sage: E = EllipticCurve([K([0,1]), K([-1,-1]), K([0,0]),                        # needs sage.rings.number_field
        ....:                    K([-236,40]), K([-1840,464])])
        sage: is_Q_curve(E, certificate=True, verbose=True)                             # needs sage.rings.number_field
        Checking whether Elliptic Curve defined by y^2 + a*x*y = x^3 + (-a-1)*x^2 + (40*a-236)*x + (464*a-1840) over Number Field in a with defining polynomial x^2 - 10 is a Q-curve
        Applying local tests at good primes above p<=100
        No: inconsistency at the 2 ordinary primes dividing 13
        - Frobenius discriminants mod squares: [-1, -3]
        No: local test at p=13 failed
        (False, 13)

    A quadratic `\\QQ`-curve with CM discriminant `-15` (`j`-invariant not in `\\QQ`)::

        sage: from sage.schemes.elliptic_curves.Qcurves import is_Q_curve
        sage: R.<x> = PolynomialRing(QQ)
        sage: K.<a> = NumberField(R([-1, -1, 1]))                                       # needs sage.rings.number_field
        sage: E = EllipticCurve([K([1,0]), K([-1,0]), K([0,1]), K([0,-2]), K([0,1])])   # needs sage.rings.number_field
        sage: is_Q_curve(E, certificate=True, verbose=True)                             # needs sage.rings.number_field
        Checking whether Elliptic Curve defined by y^2 + x*y + a*y = x^3 + (-1)*x^2 + (-2*a)*x + a over Number Field in a with defining polynomial x^2 - x - 1 is a Q-curve
        Yes: E is CM (discriminant -15)
        (True, {\'CM\': -15})

    An example over `\\QQ(\\sqrt{2},\\sqrt{3})`.  The `j`-invariant is in
    `\\QQ(\\sqrt{6})`, so computations will be done over that field, and
    in fact there is an isogenous curve with rational `j`, so we have
    a so-called rational `\\QQ`-curve::

        sage: # needs sage.rings.number_field
        sage: K.<a> = NumberField(R([1, 0, -4, 0, 1]))
        sage: E = EllipticCurve([K([-2,-4,1,1]), K([0,1,0,0]), K([0,1,0,0]),
        ....:                    K([-4780,9170,1265,-2463]),
        ....:                    K([163923,-316598,-43876,84852])])
        sage: flag, cert = is_Q_curve(E, certificate=True)
        sage: flag
        True
        sage: cert
        {\'CM\': 0, \'N\': 1, \'core_degs\': [1], \'core_poly\': x - 85184/3, \'r\': 0, \'rho\': 0}

    Over the same field, a so-called strict `\\QQ`-curve which is not
    isogenous to one with rational `j`, but whose core field is
    quadratic. In fact the isogeny class over `K` consists of `6`
    curves, four with conjugate quartic `j`-invariants and `2` with
    quadratic conjugate `j`-invariants in `\\QQ(\\sqrt{3})` (but which
    are not base-changes from the quadratic subfield)::

        sage: # needs sage.rings.number_field
        sage: E = EllipticCurve([K([0,-3,0,1]), K([1,4,0,-1]), K([0,0,0,0]),
        ....:                    K([-2,-16,0,4]), K([-19,-32,4,8])])
        sage: flag, cert = is_Q_curve(E, certificate=True)
        sage: flag
        True
        sage: cert
        {\'CM\': 0,
         \'N\': 2,
         \'core_degs\': [1, 2],
         \'core_poly\': x^2 - 840064*x + 1593413632,
         \'r\': 1,
         \'rho\': 1}

    TESTS::

        sage: E = EllipticCurve([GF(5)(t) for t in [2,3,5,7,11]])
        sage: is_Q_curve(E)
        Traceback (most recent call last):
        ...
        TypeError: Elliptic Curve defined by ... must be an elliptic curve
        defined over a number field
    '''
def Step4Test(E, B, oldB: int = 0, verbose: bool = False):
    """
    Apply local Q-curve test to E at all primes up to B.

    INPUT:

    - ``E`` -- elliptic curve defined over a number field

    - ``B`` -- integer; upper bound on primes to test

    - ``oldB`` -- integer (default: 0); lower bound on primes to test

    - ``verbose`` -- boolean (default: ``False``); verbosity flag

    OUTPUT:

    Either (``False``, `p`), if the local test at `p` proves that `E`
    is not a `\\QQ`-curve, or (``True``, `0`) if all local tests at
    primes between ``oldB`` and ``B`` fail to prove that `E` is not a
    `\\QQ`-curve.

    ALGORITHM (see [CrNa2020]_ for details):

    This local test at `p` only applies if `E` has good reduction at
    all of the primes lying above `p` in the base field `K` of `E`.  It
    tests whether (1) `E` is either ordinary at all `P\\mid p`, or
    supersingular at all; (2) if ordinary at all, it tests that the
    squarefree part of `a_P^2-4N(P)` is the same for all `P\\mid p`.

    EXAMPLES:

    A non-`\\QQ`-curve over a quartic field (with LMFDB label
    '4.4.8112.1-12.1-a1') fails this test at `p=13`::

        sage: from sage.schemes.elliptic_curves.Qcurves import Step4Test
        sage: R.<x> = PolynomialRing(QQ)
        sage: K.<a> = NumberField(R([3, 0, -5, 0, 1]))                                  # needs sage.rings.number_field
        sage: E = EllipticCurve([K([-3,-4,1,1]), K([4,-1,-1,0]), K([-2,0,1,0]),         # needs sage.rings.number_field
        ....:                    K([-621,778,138,-178]), K([9509,2046,-24728,10380])])
        sage: Step4Test(E, 100, verbose=True)                                           # needs sage.rings.number_field
        No: inconsistency at the 2 ordinary primes dividing 13
        - Frobenius discriminants mod squares: [-3, -1]
        (False, 13)

    A `\\QQ`-curve over a sextic field (with LMFDB label
    '6.6.1259712.1-64.1-a6') passes this test for all `p<100`::

        sage: from sage.schemes.elliptic_curves.Qcurves import Step4Test
        sage: R.<x> = PolynomialRing(QQ)
        sage: K.<a> = NumberField(R([-3, 0, 9, 0, -6, 0, 1]))                           # needs sage.rings.number_field
        sage: E = EllipticCurve([K([1,-3,0,1,0,0]), K([5,-3,-6,1,1,0]),                 # needs sage.rings.number_field
        ....:                    K([1,-3,0,1,0,0]), K([-139,-129,331,277,-76,-63]),
        ....:                    K([2466,1898,-5916,-4582,1361,1055])])
        sage: Step4Test(E, 100, verbose=True)                                           # needs sage.rings.number_field
        (True, 0)
    """
def conjugacy_test(jlist, verbose: bool = False):
    """
    Test whether a list of algebraic numbers contains a complete
    conjugacy class of 2-power degree.

    INPUT:

    - ``jlist`` -- list of algebraic numbers in the same field

    - ``verbose`` -- boolean (default: ``False``); verbosity flag

    OUTPUT:

    A possibly empty list of irreducible polynomials over `\\QQ` of
    2-power degree all of whose roots are in the list.

    EXAMPLES::

        sage: # needs sage.rings.number_field
        sage: from sage.schemes.elliptic_curves.Qcurves import conjugacy_test
        sage: conjugacy_test([3])
        [x - 3]
        sage: K.<a> = QuadraticField(2)
        sage: conjugacy_test([K(3), a])
        [x - 3]
        sage: conjugacy_test([K(3), 3 + a])
        [x - 3]
        sage: conjugacy_test([3 + a])
        []
        sage: conjugacy_test([3 + a, 3 - a])
        [x^2 - 6*x + 7]
        sage: x = polygen(QQ)
        sage: f = x^3 - 3
        sage: K.<a> = f.splitting_field()
        sage: js = f.roots(K, multiplicities=False)
        sage: conjugacy_test(js)
        []
        sage: f = x^4 - 3
        sage: K.<a> = NumberField(f)
        sage: js = f.roots(K, multiplicities=False)
        sage: conjugacy_test(js)
        []
        sage: K.<a> = f.splitting_field()
        sage: js = f.roots(K, multiplicities=False)
        sage: conjugacy_test(js)
        [x^4 - 3]
    """
