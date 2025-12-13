from _typeshed import Incomplete
from collections.abc import Generator
from sage.arith.misc import legendre_symbol as legendre_symbol, primes as primes
from sage.misc.functional import cyclotomic_polynomial as cyclotomic_polynomial
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.modules.free_module import VectorSpace as VectorSpace
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.infinity import Infinity as Infinity
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.sets.set import Set as Set
from sage.structure.sage_object import SageObject as SageObject

class GaloisRepresentation(SageObject):
    """
    The compatible family of Galois representation
    attached to an elliptic curve over a number field.

    Given an elliptic curve `E` over a number field `K`
    and a rational prime number `p`, the `p^n`-torsion
    `E[p^n]` points of `E` is a representation of the
    absolute Galois group `G_K` of `K`. As `n` varies
    we obtain the Tate module `T_p E` which is
    a representation of `G_K` on a free `\\ZZ_p`-module
    of rank `2`. As `p` varies the representations
    are compatible.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K = NumberField(x**2 + 1, 'a')
        sage: E = EllipticCurve('11a1').change_ring(K)
        sage: rho = E.galois_representation()
        sage: rho
        Compatible family of Galois representations associated to the Elliptic Curve
         defined by y^2 + y = x^3 + (-1)*x^2 + (-10)*x + (-20)
         over Number Field in a with defining polynomial x^2 + 1
    """
    E: Incomplete
    def __init__(self, E) -> None:
        """
        See ``GaloisRepresentation`` for documentation.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x**2 + 1, 'a')
            sage: E = EllipticCurve('11a1').change_ring(K)
            sage: rho = E.galois_representation()
            sage: rho
            Compatible family of Galois representations associated to the Elliptic Curve
             defined by y^2 + y = x^3 + (-1)*x^2 + (-10)*x + (-20)
             over Number Field in a with defining polynomial x^2 + 1
            sage: loads(rho.dumps()) == rho
            True
        """
    def __eq__(self, other):
        """
        Compare two Galois representations.

        We define two compatible families of representations attached
        to elliptic curves to be equal if the curves are isomorphic.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x**2 + 1, 'a'); a = K.gen()
            sage: rho1 = EllipticCurve_from_j(1 + a).galois_representation()
            sage: rho2 = EllipticCurve_from_j(2 + a).galois_representation()
            sage: rho1 == rho1
            True
            sage: rho1 == rho2
            False
            sage: rho1 == 42
            False
        """
    def elliptic_curve(self):
        """
        Return the elliptic curve associated to this representation.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x**2 + 1, 'a'); a = K.gen()
            sage: E = EllipticCurve_from_j(a)
            sage: rho = E.galois_representation()
            sage: rho.elliptic_curve() == E
            True
        """
    def non_surjective(self, A: int = 100):
        """
        Return a list of primes `p` including all primes for which the mod-`p`
        representation might not be surjective.

        INPUT:

        - ``A`` -- integer; a bound on the number of traces of Frobenius to use
          while trying to prove surjectivity

        OUTPUT:

        A list of primes where mod-`p` representation is very likely not
        surjective. At any prime not in this list, the representation is
        definitely surjective. If `E` has CM, the list ``[0]`` is returned.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x**2 - 29, 'a'); a = K.gen()
            sage: E = EllipticCurve([1, 0, ((5 + a)/2)**2, 0, 0])
            sage: rho = E.galois_representation()
            sage: rho.non_surjective() # See Section 5.10 of [Ser1972].  # long time
            [3, 5, 29]
            sage: K = NumberField(x**2 + 3, 'a'); a = K.gen()
            sage: E = EllipticCurve([0, -1, 1, -10, -20]).change_ring(K) # X_0(11)
            sage: rho = E.galois_representation()
            sage: rho.non_surjective()  # long time (4s on sage.math, 2014)
            [3, 5]
            sage: K = NumberField(x**2 + 1, 'a'); a = K.gen()
            sage: E = EllipticCurve_from_j(1728).change_ring(K) # CM
            sage: rho = E.galois_representation()
            sage: rho.non_surjective()
            [0]
            sage: K = NumberField(x**2 - 5, 'a'); a = K.gen()
            sage: E = EllipticCurve_from_j(146329141248*a - 327201914880) # CM
            sage: rho = E.galois_representation()
            sage: rho.non_surjective() # long time (3s on sage.math, 2014)
            [0]

        TESTS:

        An example which failed until fixed at :issue:`19229`::

            sage: K.<a> = NumberField(x^2-x+1)
            sage: E = EllipticCurve([a+1,1,1,0,0])
            sage: rho = E.galois_representation()
            sage: rho.non_surjective()
            [2, 3]
        """
    def is_surjective(self, p, A: int = 100):
        """
        Return ``True`` if the mod-p representation is (provably)
        surjective onto `Aut(E[p]) = GL_2(\\GF{p})`.  Return
        ``False`` if it is (probably) not.

        INPUT:

        - ``p`` -- prime number

        - ``A`` -- integer; a bound on the number of traces of Frobenius to use
          while trying to prove surjectivity

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x**2 - 29, 'a'); a = K.gen()
            sage: E = EllipticCurve([1, 0, ((5 + a)/2)**2, 0, 0])
            sage: rho = E.galois_representation()
            sage: rho.is_surjective(29) # Cyclotomic character not surjective.
            False
            sage: rho.is_surjective(7) # See Section 5.10 of [Ser1972].
            True

        If `E` is defined over `\\QQ`, then the exceptional primes for `E_{/K}`
        are the same as the exceptional primes for `E`, except for those primes
        that are ramified in `K/\\QQ` or are less than `[K:\\QQ]`::

            sage: K = NumberField(x**2 + 11, 'a')
            sage: E = EllipticCurve([2, 14])
            sage: rhoQQ = E.galois_representation()
            sage: rhoK = E.change_ring(K).galois_representation()
            sage: rhoQQ.is_surjective(2) == rhoK.is_surjective(2)
            False
            sage: rhoQQ.is_surjective(3) == rhoK.is_surjective(3)
            True
            sage: rhoQQ.is_surjective(5) == rhoK.is_surjective(5)
            True

        For CM curves, the mod-p representation is never surjective::

            sage: K.<a> = NumberField(x^2 - x + 1)
            sage: E = EllipticCurve([0,0,0,0,a])
            sage: E.has_cm()
            True
            sage: rho = E.galois_representation()
            sage: any(rho.is_surjective(p) for p in [2,3,5,7])
            False
        """
    def isogeny_bound(self, A: int = 100):
        """
        Return a list of primes `p` including all primes for which
        the image of the mod-`p` representation is contained in a
        Borel.

        .. NOTE::

            For the actual list of primes `p` at which the
            representation is reducible see :meth:`reducible_primes()`.

        INPUT:

        - ``A`` -- integer; a bound on the number of traces of Frobenius to
          use while trying to prove the mod-`p` representation is not contained
          in a Borel

        OUTPUT:

        A list of primes which contains (but may not be equal to) all `p` for
        which the image of the mod-`p` representation is contained in a Borel
        subgroup.  At any prime not in this list, the image is definitely not
        contained in a Borel. If E has `CM` defined over `K`, the list ``[0]``
        is returned.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x**2 - 29, 'a'); a = K.gen()
            sage: E = EllipticCurve([1, 0, ((5 + a)/2)**2, 0, 0])
            sage: rho = E.galois_representation()
            sage: rho.isogeny_bound() # See Section 5.10 of [Ser1972].  # long time
            [3, 5]
            sage: K = NumberField(x**2 + 1, 'a')
            sage: E = EllipticCurve_from_j(K(1728))             # CM over K
            sage: E.galois_representation().isogeny_bound()
            [0]
            sage: E = EllipticCurve_from_j(K(0))                # CM NOT over K
            sage: E.galois_representation().isogeny_bound()     # long time
            [2, 3]
            sage: E = EllipticCurve_from_j(K(2268945/128))      # c.f. [Sut2012]
            sage: rho = E.galois_representation()
            sage: rho.isogeny_bound()  # No 7-isogeny, but...   # long time
            [7]

        For curves with rational CM, there are infinitely many primes
        `p` for which the mod-`p` representation is reducible, and [0]
        is returned::

            sage: K.<a> = NumberField(x^2 - x + 1)
            sage: E = EllipticCurve([0,0,0,0,a])
            sage: E.has_rational_cm()
            True
            sage: rho = E.galois_representation()
            sage: rho.isogeny_bound()
            [0]

        An example (an elliptic curve with everywhere good reduction
        over an imaginary quadratic field with quite large
        discriminant), which failed until fixed at :issue:`21776`::

            sage: K.<a> = NumberField(x^2 - x + 112941801)
            sage: E = EllipticCurve([a+1,a-1,a,-23163076*a + 266044005933275,57560769602038*a - 836483958630700313803])
            sage: E.conductor().norm()
            1
            sage: GR = E.galois_representation()
            sage: GR.isogeny_bound()
            []
        """
    def reducible_primes(self):
        """
        Return a list of primes `p` for which the mod-`p`
        representation is reducible, or [0] for CM curves.

        OUTPUT:

        A list of those primes `p` for which the mod-`p` representation is
        contained in a Borel subgroup, i.e. is reducible.  If E has CM
        *defined over K*, the list ``[0]`` is returned (in this case the
        representation is reducible for infinitely many primes).

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K = NumberField(x**2 - 29, 'a'); a = K.gen()
            sage: E = EllipticCurve([1, 0, ((5 + a)/2)**2, 0, 0])
            sage: rho = E.galois_representation()
            sage: rho.reducible_primes() # See Section 5.10 of [Ser1972].  # long time
            [3, 5]

            sage: K = NumberField(x**2 + 1, 'a')
            sage: E = EllipticCurve_from_j(K(1728))             # CM over K
            sage: E.galois_representation().reducible_primes()
            [0]
            sage: E = EllipticCurve_from_j(K(0))                # CM but NOT over K
            sage: E.galois_representation().reducible_primes()  # long time
            [2, 3]
            sage: E = EllipticCurve_from_j(K(2268945/128))      # c.f. [Sut2012]
            sage: rho = E.galois_representation()
            sage: rho.isogeny_bound()  # No 7-isogeny, but...   # long time
            [7]
            sage: rho.reducible_primes()                        # long time
            []

        For curves with rational CM, there are infinitely many primes
        `p` for which the mod-`p` representation is reducible, and [0]
        is returned::

            sage: K.<a> = NumberField(x^2 - x + 1)
            sage: E = EllipticCurve([0,0,0,0,a])
            sage: E.has_rational_cm()
            True
            sage: rho = E.galois_representation()
            sage: rho.reducible_primes()
            [0]
        """

def Frobenius_filter(E, L, patience: int = 100):
    """
    Determine which primes in L might have an image contained in a
    Borel subgroup, by checking of traces of Frobenius.

    .. NOTE::

        This function will sometimes return primes for which the image
        is not contained in a Borel subgroup.  This issue cannot always
        be fixed by increasing patience as it may be a result of a
        failure of a local-global principle for isogenies.

    INPUT:

    - ``E`` -- :class:`EllipticCurve` over a number field

    - ``L`` -- list of prime numbers

    - ``patience`` -- positive integer (default: 100) bounding the number of
      traces of Frobenius to use while trying to prove irreducibility

    OUTPUT:

    The list of all primes `\\ell` in L for which the mod `\\ell` image might be
    contained in a Borel subgroup of `GL_2(\\mathbf{F}_{\\ell})`.

    EXAMPLES::

        sage: E = EllipticCurve('11a1') # has a 5-isogeny
        sage: sage.schemes.elliptic_curves.gal_reps_number_field.Frobenius_filter(E,primes(40))  # long time
        [5]

    Example to show that the output may contain primes where the
    representation is in fact reducible.  Over `\\QQ` the following is
    essentially the unique such example by [Sut2012]_::

        sage: E = EllipticCurve_from_j(2268945/128)
        sage: sage.schemes.elliptic_curves.gal_reps_number_field.Frobenius_filter(E, [7, 11])  # long time
        [7]

    This curve does possess a 7-isogeny modulo every prime of good
    reduction, but has no rational 7-isogeny::

        sage: E.isogenies_prime_degree(7)
        []

    A number field example::

        sage: K.<i> = QuadraticField(-1)
        sage: E = EllipticCurve([1+i, -i, i, -399-240*i,  2627+2869*i])
        sage: sage.schemes.elliptic_curves.gal_reps_number_field.Frobenius_filter(E, primes(20))  # long time
        [2, 3]

    Here the curve really does possess isogenies of degrees 2 and 3::

        sage: [len(E.isogenies_prime_degree(l)) for l in [2,3]]
        [1, 1]
    """
def deg_one_primes_iter(K, principal_only: bool = False) -> Generator[Incomplete]:
    """
    Return an iterator over degree 1 primes of ``K``.

    INPUT:

    - ``K`` -- a number field
    - ``principal_only`` -- boolean; if ``True``, only yield principal primes

    OUTPUT:

    An iterator over degree 1 primes of `K` up to the given norm,
    optionally yielding only principal primes.

    EXAMPLES::

        sage: K.<a> = QuadraticField(-5)
        sage: from sage.schemes.elliptic_curves.gal_reps_number_field import deg_one_primes_iter
        sage: it = deg_one_primes_iter(K)
        sage: [next(it) for _ in range(6)]
        [Fractional ideal (2, a + 1),
         Fractional ideal (3, a + 1),
         Fractional ideal (3, a + 2),
         Fractional ideal (-a),
         Fractional ideal (7, a + 3),
         Fractional ideal (7, a + 4)]
        sage: it = deg_one_primes_iter(K, True)
        sage: [next(it) for _ in range(6)]
        [Fractional ideal (-a),
         Fractional ideal (2*a - 3),
         Fractional ideal (-2*a - 3),
         Fractional ideal (a + 6),
         Fractional ideal (a - 6),
         Fractional ideal (3*a - 4)]
    """
def Billerey_P_l(E, l):
    """
    Return Billerey's `P_l^*` as defined in [Bil2011]_, equation (9).

    INPUT:

    - ``E`` -- an elliptic curve over a number field `K`, given by a
      global integral model

    - ``l`` -- a rational prime

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K = NumberField(x**2 - 29, 'a'); a = K.gen()
        sage: E = EllipticCurve([1, 0, ((5 + a)/2)**2, 0, 0])
        sage: from sage.schemes.elliptic_curves.gal_reps_number_field import Billerey_P_l
        sage: [Billerey_P_l(E,l) for l in primes(10)]
        [x^2 + 8143*x + 16777216,
         x^2 + 451358*x + 282429536481,
         x^4 - 664299076*x^3 + 205155493652343750*x^2 - 39595310449600219726562500*x + 3552713678800500929355621337890625,
         x^4 - 207302404*x^3 - 377423798538689366394*x^2 - 39715249826471656586987520004*x + 36703368217294125441230211032033660188801]
    """
def Billerey_B_l(E, l, B: int = 0):
    """
    Return Billerey's `B_l`, adapted from the definition in [Bil2011]_, after (9).

    INPUT:

    - ``E`` -- an elliptic curve over a number field `K`, given by a
      global integral model

    - ``l`` -- integer; a rational prime

    - ``B`` -- integer; 0 or LCM of previous `B_l` the prime-to-B part of this
      `B_l` is ignored

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K = NumberField(x**2 - 29, 'a'); a = K.gen()
        sage: E = EllipticCurve([1, 0, ((5 + a)/2)**2, 0, 0])
        sage: from sage.schemes.elliptic_curves.gal_reps_number_field import Billerey_B_l
        sage: [Billerey_B_l(E,l) for l in primes(15)]
        [1123077552537600,
         227279663773903886745600,
         0,
         0,
         269247154818492941287713746693964214802283882086400,
         0]
    """
def Billerey_R_q(E, q, B: int = 0):
    """
    Return Billerey's `R_q`, adapted from the definition in [Bil2011]_, Theorem 2.8.

    INPUT:

    - ``E`` -- an elliptic curve over a number field `K`, given by a
      global integral model

    - ``q`` -- a prime ideal of `K`

    - ``B`` -- integer; 0 or LCM of previous `R_q` the prime-to-B part of this
      `R_q` is ignored

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K = NumberField(x**2 - 29, 'a'); a = K.gen()
        sage: E = EllipticCurve([1, 0, ((5 + a)/2)**2, 0, 0])
        sage: from sage.schemes.elliptic_curves.gal_reps_number_field import Billerey_R_q
        sage: [Billerey_R_q(E,K.prime_above(l)) for l in primes(10)]
        [1123077552537600,
        227279663773903886745600,
        51956919562116960000000000000000,
        252485933820556361829926400000000]
    """
def Billerey_B_bound(E, max_l: int = 200, num_l: int = 8, small_prime_bound: int = 0, debug: bool = False):
    """
    Compute Billerey's bound `B`.

    We compute `B_l` for `l` up to ``max_l`` (at most) until ``num_l``
    nonzero values are found (at most).  Return the list of primes
    dividing all `B_l` computed, excluding those dividing 6 or
    ramified or of bad reduction or less than small_prime_bound.  If
    no nonzero values are found return ``[0]``.

    INPUT:

    - ``E`` -- an elliptic curve over a number field `K`, given by a
      global integral model

    - ``max_l`` -- integer (default: 200); maximum size of primes l to check

    - ``num_l`` integer (default: 8); maximum number of primes l to check

    - ``small_prime_bound`` -- integer (default: 0); remove primes less
      than this from the output

    - ``debug`` -- boolean (default: ``False``); if ``True`` prints details

    .. NOTE::

        The purpose of the small_prime_bound is that it is faster to
        deal with these using the local test; by ignoring them here,
        we enable the algorithm to terminate sooner when there are no
        large reducible primes, which is always the case in practice.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K = NumberField(x**2 - 29, 'a'); a = K.gen()
        sage: E = EllipticCurve([1, 0, ((5 + a)/2)**2, 0, 0])
        sage: from sage.schemes.elliptic_curves.gal_reps_number_field import Billerey_B_bound
        sage: Billerey_B_bound(E)
        [5]

    If we do not use enough primes `l`, extraneous primes will be
    included which are not reducible primes::

        sage: Billerey_B_bound(E, num_l=6)
        [5, 7]

    Similarly if we do not use large enough primes `l`::

        sage: Billerey_B_bound(E, max_l=50, num_l=8)
        [5, 7]
        sage: Billerey_B_bound(E, max_l=100, num_l=8)
        [5]

    This curve does have a rational 5-isogeny::

        sage: len(E.isogenies_prime_degree(5))
        1
    """
def Billerey_R_bound(E, max_l: int = 200, num_l: int = 8, small_prime_bound=None, debug: bool = False):
    """
    Compute Billerey's bound `R`.

    We compute `R_q` for `q` dividing primes `\\ell` up to ``max_l``
    (at most) until ``num_l`` nonzero values are found (at most).
    Return the list of primes dividing all ``R_q`` computed, excluding
    those dividing 6 or ramified or of bad reduction or less than
    small_prime_bound.  If no nonzero values are found return ``[0]``.

    INPUT:

    - ``E`` -- an elliptic curve over a number field `K`, given by a
      global integral model

    - ``max_l`` -- integer (default: 200); maximum size of rational primes
      l for which the primes q above l are checked

    - ``num_l`` -- integer (default: 8); maximum number of rational primes
      l for which the primes q above l are checked

    - ``small_prime_bound`` -- integer (default: 0); remove primes less
      than this from the output

    - ``debug`` -- boolean (default: ``False``); if ``True`` prints details

    .. NOTE::

        The purpose of the ``small_prime_bound`` is that it is faster to
        deal with these using the local test; by ignoring them here,
        we enable the algorithm to terminate sooner when there are no
        large reducible primes, which is always the case in practice.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K = NumberField(x**2 - 29, 'a'); a = K.gen()
        sage: E = EllipticCurve([1, 0, ((5 + a)/2)**2, 0, 0])
        sage: from sage.schemes.elliptic_curves.gal_reps_number_field import Billerey_R_bound
        sage: Billerey_R_bound(E)
        [5]

    We may get no bound at all if we do not use enough primes::

        sage: Billerey_R_bound(E, max_l=2, debug=False)
        [0]

    Or we may get a bound but not a good one if we do not use enough primes::

        sage: Billerey_R_bound(E, num_l=1, debug=False)
        [5, 17, 67, 157]

    In this case two primes is enough to restrict the set of possible
    reducible primes to just `\\{5\\}`.  This curve does have a rational 5-isogeny::

        sage: Billerey_R_bound(E, num_l=2, debug=False)
        [5]
        sage: len(E.isogenies_prime_degree(5))
        1
    """
def reducible_primes_Billerey(E, num_l=None, max_l=None, verbose: bool = False):
    """
    Return a finite set of primes `\\ell` containing all those for which
    `E` has a `K`-rational ell-isogeny, where `K` is the base field of
    `E`: i.e., the mod-`\\ell` representation is irreducible for all
    `\\ell` outside the set returned.

    INPUT:

    - ``E`` -- an elliptic curve defined over a number field `K`

    - ``max_l`` -- integer or ``None`` (default); the maximum prime
      `\\ell` to use for the B-bound and R-bound.  If ``None``, a
      default value will be used.

    - ``num_l`` -- integer or ``None`` (default); the number of primes
      `\\ell` to use for the B-bound and R-bound.  If ``None``, a
      default value will be used.

    .. NOTE::

        If ``E`` has CM then [0] is returned.  In this case use the
        function
        sage.schemes.elliptic_curves.isogeny_class.possible_isogeny_degrees

    We first compute Billeray's B_bound using at most ``num_l`` primes
    of size up to ``max_l``.  If that fails we compute Billeray's
    R_bound using at most ``num_q`` primes of size up to ``max_q``.

    Provided that one of these methods succeeds in producing a finite
    list of primes we check these using a local condition, and finally
    test that the primes returned actually are reducible.  Otherwise
    we return ``[0]``.

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.gal_reps_number_field import reducible_primes_Billerey
        sage: x = polygen(ZZ, 'x')
        sage: K = NumberField(x**2 - 29, 'a'); a = K.gen()
        sage: E = EllipticCurve([1, 0, ((5 + a)/2)**2, 0, 0])
        sage: reducible_primes_Billerey(E)  # long time
        [3, 5]
        sage: K = NumberField(x**2 + 1, 'a')
        sage: E = EllipticCurve_from_j(K(1728)) # CM over K
        sage: reducible_primes_Billerey(E)  # long time
        [0]
        sage: E = EllipticCurve_from_j(K(0)) # CM but NOT over K
        sage: reducible_primes_Billerey(E)  # long time
        [2, 3]

    An example where a prime is not reducible but passes the test::

        sage: E = EllipticCurve_from_j(K(2268945/128)).global_minimal_model() # c.f. [Sut2012]
        sage: reducible_primes_Billerey(E)  # long time
        [7]

    TESTS:

    Test that this function works with non-integral models (see :issue:`34174`)::

        sage: K.<a> = QuadraticField(4569)
        sage: j = 46969655/32768
        sage: E = EllipticCurve(j=K(j))
        sage: EK = E.change_ring(K)
        sage: C = EK.isogeny_class(minimal_models=False)    # long time
        sage: len(C)                                        # long time
        4
    """
def reducible_primes_naive(E, max_l=None, num_P=None, verbose: bool = False):
    """
    Return locally reducible primes `\\ell` up to ``max_l``.

    The list of primes `\\ell` returned consists of all those up to
    ``max_l`` such that `E` mod `P` has an `\\ell`-isogeny, where `K`
    is the base field of `E`, for ``num_P`` primes `P` of `K`.  In
    most cases `E` then has a `K`-rational `\\ell`-isogeny, but there
    are rare exceptions.

    INPUT:

    - ``E`` -- an elliptic curve defined over a number field `K`

    - ``max_l`` -- integer or ``None`` (default); the maximum prime
      `\\ell` to test

    - ``num_P`` -- integer or ``None`` (default); the number of primes
      `P` of `K` to use in testing each `\\ell`

    EXAMPLES::

        sage: from sage.schemes.elliptic_curves.gal_reps_number_field import reducible_primes_naive
        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^4 - 5*x^2 + 3)
        sage: E = EllipticCurve(K, [a^2 - 2, -a^2 + 3, a^2 - 2, -50*a^2 + 35, 95*a^2 - 67])
        sage: reducible_primes_naive(E,num_P=10)
        [2, 5, 53, 173, 197, 241, 293, 317, 409, 557, 601, 653, 677, 769, 773, 797]
        sage: reducible_primes_naive(E,num_P=15)
        [2, 5, 197, 557, 653, 769]
        sage: reducible_primes_naive(E,num_P=20)
        [2, 5]
        sage: reducible_primes_naive(E)  # long time
        [2, 5]
        sage: [phi.degree() for phi in E.isogenies_prime_degree()]  # long time
        [2, 2, 2, 5]
    """
