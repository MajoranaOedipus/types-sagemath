from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.integer_ring import ZZ as ZZ
from sage.structure.sage_object import SageObject as SageObject

def reduce_mod_q(x, amodq):
    """The reduction of ``x`` modulo the prime ideal defined by ``amodq``.

    INPUT:

    - ``x`` -- an element of a  number field `K`

    - ``amodq`` -- an element of `GF(q)` which is a root mod `q` of
      the defining polynomial of `K`.  This defines a degree 1 prime
      ideal `Q=(q,\\alpha-a)` of `K=\\QQ(\\alpha)`, where `a \\bmod q` =
      ``amodq``.

    OUTPUT: the image of ``x`` in the residue field of `K` at the prime `Q`

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.saturation import reduce_mod_q
        sage: x = polygen(QQ)
        sage: pol = x^3 - x^2 - 3*x + 1
        sage: K.<a> = NumberField(pol)
        sage: [(q, [(amodq, reduce_mod_q(1 - a + a^4, amodq))
        ....:       for amodq in sorted(pol.roots(GF(q), multiplicities=False))])
        ....:  for q in primes(50, 70)]
        [(53, []),
         (59, [(36, 28)]),
         (61, [(40, 35)]),
         (67, [(10, 8), (62, 28), (63, 60)])]
    """

class EllipticCurveSaturator(SageObject):
    """
    Class for saturating points on an elliptic curve over a number field.

    INPUT:

    - ``E`` -- an elliptic curve defined over a number field, or `\\QQ`

    - ``verbose`` -- boolean (default: ``False``); verbosity flag

    .. NOTE::

        This function is not normally called directly by users, who
        may access the data via methods of the EllipticCurve
        classes.
    """
    def __init__(self, E, verbose: bool = False) -> None:
        """
        Initialize the saturator.

        INPUT:

        - ``E`` -- an elliptic curve defined over a number field

        - ``verbose`` -- boolean (default: ``False``); verbosity flag
        """
    def add_reductions(self, q) -> None:
        """
        Add reduction data at primes above ``q`` if not already there.

        INPUT:

        - ``q`` -- a prime number not dividing the defining polynomial
          of ``self.__field``

        OUTPUT:

        Returns nothing, but updates self._reductions dictionary for
        key ``q`` to a dict whose keys are the roots of the defining
        polynomial mod ``q`` and values tuples (``nq``, ``Eq``) where
        ``Eq`` is an elliptic curve over `GF(q)` and ``nq`` its
        cardinality.  If ``q`` divides the conductor norm or order
        discriminant nothing is added.

        EXAMPLES:

        Over `\\QQ`::

            sage: from sage.schemes.elliptic_curves.saturation import EllipticCurveSaturator
            sage: E = EllipticCurve('11a1')
            sage: saturator = EllipticCurveSaturator(E)
            sage: saturator._reductions
            {}
            sage: saturator.add_reductions(19)
            sage: saturator._reductions
            {19: {0: (20, Elliptic Curve defined by y^2 + y = x^3 + 18*x^2 + 9*x + 18
                           over Finite Field of size 19)}}

        Over a number field::

            sage: x = polygen(QQ);  K.<a> = NumberField(x^2 + 2)
            sage: E = EllipticCurve(K, [0,1,0,a,a])
            sage: from sage.schemes.elliptic_curves.saturation import EllipticCurveSaturator
            sage: saturator = EllipticCurveSaturator(E)
            sage: for q in primes(20):
            ....:     saturator.add_reductions(q)
            sage: saturator._reductions
            {2:  {},
             3:  {},
             5:  {},
             7:  {},
             11: {3:  (16, Elliptic Curve defined by y^2 = x^3 + x^2 + 3*x + 3
                            over Finite Field of size 11),
                  8:  (8,  Elliptic Curve defined by y^2 = x^3 + x^2 + 8*x + 8
                            over Finite Field of size 11)},
             13: {},
             17: {7:  (20, Elliptic Curve defined by y^2 = x^3 + x^2 + 7*x + 7
                            over Finite Field of size 17),
                  10: (18, Elliptic Curve defined by y^2 = x^3 + x^2 + 10*x + 10
                            over Finite Field of size 17)},
             19: {6:  (16, Elliptic Curve defined by y^2 = x^3 + x^2 + 6*x + 6
                            over Finite Field of size 19),
                  13: (12, Elliptic Curve defined by y^2 = x^3 + x^2 + 13*x + 13
                            over Finite Field of size 19)}}
        """
    def full_p_saturation(self, Plist, p):
        """Full `p`-saturation of ``Plist``.

        INPUT:

        - ``Plist`` -- list of independent points on one elliptic curve

        - ``p`` -- integer; a prime number

        OUTPUT:

        (``newPlist``, ``exponent``) where ``newPlist`` has the same
        length as ``Plist`` and spans the `p`-saturation of the span
        of ``Plist``, which contains that span with index
        ``p**exponent``.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.saturation import EllipticCurveSaturator
            sage: E = EllipticCurve('389a')
            sage: K.<i> = QuadraticField(-1)
            sage: EK = E.change_ring(K)
            sage: P = EK(1 + i, -1 - 2*i)
            sage: saturator = EllipticCurveSaturator(EK, verbose=True)
            sage: saturator.full_p_saturation([8*P], 2)
             --starting full 2-saturation
            Points were not 2-saturated, exponent was 3
            ([(i + 1 : -2*i - 1 : 1)], 3)

            sage: Q = EK(0, 0)
            sage: R = EK(-1, 1)
            sage: saturator = EllipticCurveSaturator(EK, verbose=False)
            sage: saturator.full_p_saturation([P, Q, R], 3)
            ([(i + 1 : -2*i - 1 : 1), (0 : 0 : 1), (-1 : 1 : 1)], 0)

        An example where the points are not 7-saturated and we gain
        index exponent 1.  Running this example with verbose=True
        would show that it uses the code for when the reduction has
        `p`-rank 2 (which occurs for the reduction modulo `(16-5i)`),
        which uses the Weil pairing::

            sage: saturator.full_p_saturation([P, Q + 3*R, Q - 4*R], 7)
            ([(i + 1 : -2*i - 1 : 1),
              (2869/676 : 154413/17576 : 1),
              (-7095/502681 : -366258864/356400829 : 1)], 1)
        """
    def p_saturation(self, Plist, p, sieve: bool = True):
        """Checks whether the list of points is `p`-saturated.

        INPUT:

        - ``Plist`` -- list of independent points on one elliptic curve

        - ``p`` -- integer; a prime number

        - ``sieve`` -- boolean; if ``True``, use a sieve (when there are at
          least 2 points), otherwise test all combinations

        .. NOTE::

            The sieve is much more efficient when the points are
            saturated and the number of points or the prime are large.

        OUTPUT:

        Either ``False`` if the points are `p`-saturated, or (``i``,
        ``newP``) if they are not `p`-saturated, in which case after
        replacing the i'th point with ``newP``, the subgroup generated
        contains that generated by ``Plist`` with index `p`.

        EXAMPLES::

            sage: from sage.schemes.elliptic_curves.saturation import EllipticCurveSaturator
            sage: E = EllipticCurve('389a')
            sage: K.<i> = QuadraticField(-1)
            sage: EK = E.change_ring(K)
            sage: P = EK(1 + i, -1 - 2*i)
            sage: saturator = EllipticCurveSaturator(EK)
            sage: saturator.p_saturation([P], 2)
            False
            sage: saturator.p_saturation([2*P], 2)
            (0, (i + 1 : -2*i - 1 : 1))

            sage: Q = EK(0, 0)
            sage: R = EK(-1, 1)
            sage: saturator.p_saturation([P, Q, R], 3)
            False

        Here we see an example where 19-saturation is proved, with the
        verbose flag set to ``True`` so that we can see what is going on::

            sage: saturator = EllipticCurveSaturator(EK, verbose=True)
            sage: saturator.p_saturation([P, Q, R], 19)
            Using sieve method to saturate...
            E has 19-torsion over Finite Field of size 197, projecting points
            --> [(15 : 168 : 1), (0 : 0 : 1), (196 : 1 : 1)]
            --rank is now 1
            E has 19-torsion over Finite Field of size 197, projecting points
            --> [(184 : 27 : 1), (0 : 0 : 1), (196 : 1 : 1)]
            --rank is now 2
            E has 19-torsion over Finite Field of size 293, projecting points
            --> [(139 : 16 : 1), (0 : 0 : 1), (292 : 1 : 1)]
             --rank is now 3
            Reached full rank: points were 19-saturated
            False

        An example where the points are not 11-saturated::

            sage: saturator = EllipticCurveSaturator(EK, verbose=False)
            sage: res = saturator.p_saturation([P + 5*Q, P - 6*Q, R], 11); res
            (0, (-5783311/14600041*i + 1396143/14600041
                 : 37679338314/55786756661*i + 3813624227/55786756661 : 1))

        That means that the 0'th point may be replaced by the displayed
        point to achieve an index gain of 11::

            sage: saturator.p_saturation([res[1], P - 6*Q, R], 11)
            False

        TESTS:

        See :issue:`27387`::

            sage: K.<a> = NumberField(x^2 - x - 26)
            sage: E = EllipticCurve([a, 1 - a, 0, 93 - 16*a, 3150 - 560*a])
            sage: P = E([65 - 35*a/3, (959*a-5377)/9])
            sage: T = E.torsion_points()[0]
            sage: from sage.schemes.elliptic_curves.saturation import EllipticCurveSaturator
            sage: saturator = EllipticCurveSaturator(E, True)
            sage: saturator.p_saturation([P, T], 2)
            Using sieve method to saturate...
            ...
            -- points were not 2-saturated, gaining index 2
            (1, (0 : 1 : 0))

        A CM example where large sieving primes are needed (LMFDB
        label 2.0.3.1-50625.1-CMb2)::

            sage: K.<a> = NumberField(x^2 - x + 1)
            sage: E = EllipticCurve(K, [0, 0, 1, -750, 7906])
            sage: E.has_rational_cm()
            True
            sage: E.cm_discriminant()
            -27
            sage: points = [E([10, -38]), E([15/49*a + 760/49, 675/343*a - 884/343])]
            sage: E.saturation(points, verbose=True) # long time (17s)
            Computing lower height bound..
            ..done: 7.168735020029907e-06
            p-saturating for primes p < 132
            ...
            Saturating at p=131
            --starting full 131-saturation
            Using sieve method to saturate...
            E has 131-torsion over Finite Field of size 617011, projecting points
            --> [(10 : 616973 : 1), (592083 : 192224 : 1)]
            --rank is now 1
            --rank is now 2
            Reached full rank: points were 131-saturated
            Points were 131-saturated
            --already 131-saturated
            ([(10 : -38 : 1), (15/49*a + 760/49 : 675/343*a - 884/343 : 1)],
            1,
            0.123378097374749)
        """

def p_projections(Eq, Plist, p, debug: bool = False):
    """

    INPUT:

    - ``Eq`` -- an elliptic curve over a finite field

    - ``Plist`` -- list of points on `Eq`

    - ``p`` -- a prime number

    OUTPUT:

    A list of `r\\le2` vectors in `\\GF{p^n}`, the images of the points in
    `G \\otimes \\GF{p}`, where `r` is the number of vectors is the
    `p`-rank of `Eq`.

    ALGORITHM:

    First project onto the `p`-primary part of `Eq`.  If that has
    `p`-rank 1 (i.e. is cyclic), use discrete logs there to define a
    map to `\\GF{p}`, otherwise use the Weil pairing to define two
    independent maps to `\\GF{p}`.

    EXAMPLES:

    This curve has three independent rational points::

        sage: E = EllipticCurve([0,0,1,-7,6])

    We reduce modulo `409` where its order is `3^2\\cdot7^2`; the
    `3`-primary part is non-cyclic while the `7`-primary part is
    cyclic of order `49`::

        sage: F = GF(409)
        sage: EF = E.change_ring(F)
        sage: G = EF.abelian_group()
        sage: G
        Additive abelian group isomorphic to Z/147 + Z/3
         embedded in Abelian group of points on Elliptic Curve
          defined by y^2 + y = x^3 + 402*x + 6 over Finite Field of size 409
        sage: G.order().factor()
        3^2 * 7^2

    We construct three points and project them to the `p`-primary
    parts for `p=2,3,5,7`, yielding 0,2,0,1 vectors of length 3 modulo
    `p` respectively.  The exact vectors output depend on the computed
    generators of `G`::

        sage: Plist = [EF([-2,3]), EF([0,2]), EF([1,0])]
        sage: from sage.schemes.elliptic_curves.saturation import p_projections
        sage: [(p, p_projections(EF, Plist, p)) for p in primes(11)]  # random
        [(2, []), (3, [(0, 2, 2), (2, 2, 1)]), (5, []), (7, [(5, 1, 1)])]
        sage: [(p, len(p_projections(EF, Plist, p))) for p in primes(11)]
        [(2, 0), (3, 2), (5, 0), (7, 1)]
    """
