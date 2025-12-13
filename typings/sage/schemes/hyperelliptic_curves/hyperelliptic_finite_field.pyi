from . import hyperelliptic_generic as hyperelliptic_generic
from sage.arith.misc import binomial as binomial
from sage.matrix.constructor import identity_matrix as identity_matrix, matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.functional import rank as rank
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.power_series_ring import PowerSeriesRing as PowerSeriesRing
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RR as RR
from sage.schemes.curves.projective_curve import ProjectivePlaneCurve_finite_field as ProjectivePlaneCurve_finite_field

class HyperellipticCurve_finite_field(hyperelliptic_generic.HyperellipticCurve_generic, ProjectivePlaneCurve_finite_field):
    def frobenius_matrix_hypellfrob(self, N=None):
        """
        Compute `p`-adic frobenius matrix to precision `p^N`.
        If `N` not supplied, a default value is selected, which is the
        minimum needed to recover the charpoly unambiguously.

        .. NOTE::

            Implemented using ``hypellfrob``, which means it only works
            over the prime field `GF(p)`, and requires `p > (2g+1)(2N-1)`.

        EXAMPLES::

            sage: R.<t> = PolynomialRing(GF(37))
            sage: H = HyperellipticCurve(t^5 + t + 2)
            sage: H.frobenius_matrix_hypellfrob()
            [1258 + O(37^2)  925 + O(37^2)  132 + O(37^2)  587 + O(37^2)]
            [1147 + O(37^2)  814 + O(37^2)  241 + O(37^2) 1011 + O(37^2)]
            [1258 + O(37^2) 1184 + O(37^2) 1105 + O(37^2)  482 + O(37^2)]
            [1073 + O(37^2)  999 + O(37^2)  772 + O(37^2)  929 + O(37^2)]

        The ``hypellfrob`` program doesn't support non-prime fields::

            sage: K.<z> = GF(37**3)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + z*t^3 + 1)
            sage: H.frobenius_matrix_hypellfrob()
            Traceback (most recent call last):
            ...
            NotImplementedError: Computation of Frobenius matrix only implemented
            for hyperelliptic curves defined over prime fields.

        nor too small characteristic::

            sage: K = GF(7)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + t^3 + 1)
            sage: H.frobenius_matrix_hypellfrob()
            Traceback (most recent call last):
            ...
            ValueError: In the current implementation, p must be greater than (2g+1)(2N-1) = 81
        """
    def frobenius_matrix(self, N=None, algorithm: str = 'hypellfrob'):
        """
        Compute `p`-adic frobenius matrix to precision `p^N`.
        If `N` not supplied, a default value is selected, which is the
        minimum needed to recover the charpoly unambiguously.

        .. NOTE::

            Currently only implemented using ``hypellfrob``,
            which means it only works over the prime field `GF(p)`,
            and requires `p > (2g+1)(2N-1)`.

        EXAMPLES::

            sage: R.<t> = PolynomialRing(GF(37))
            sage: H = HyperellipticCurve(t^5 + t + 2)
            sage: H.frobenius_matrix()
            [1258 + O(37^2)  925 + O(37^2)  132 + O(37^2)  587 + O(37^2)]
            [1147 + O(37^2)  814 + O(37^2)  241 + O(37^2) 1011 + O(37^2)]
            [1258 + O(37^2) 1184 + O(37^2) 1105 + O(37^2)  482 + O(37^2)]
            [1073 + O(37^2)  999 + O(37^2)  772 + O(37^2)  929 + O(37^2)]

        The ``hypellfrob`` program doesn't support non-prime fields::

            sage: K.<z> = GF(37**3)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + z*t^3 + 1)
            sage: H.frobenius_matrix(algorithm='hypellfrob')
            Traceback (most recent call last):
            ...
            NotImplementedError: Computation of Frobenius matrix only implemented
            for hyperelliptic curves defined over prime fields.

        nor too small characteristic::

            sage: K = GF(7)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + t^3 + 1)
            sage: H.frobenius_matrix(algorithm='hypellfrob')
            Traceback (most recent call last):
            ...
            ValueError: In the current implementation, p must be greater than (2g+1)(2N-1) = 81
        """
    def frobenius_polynomial_cardinalities(self, a=None):
        """
        Compute the charpoly of frobenius, as an element of `\\ZZ[x]`,
        by computing the number of points on the curve over `g` extensions
        of the base field where `g` is the genus of the curve.

        .. WARNING::

            This is highly inefficient when the base field or the genus of the
            curve are large.

        EXAMPLES::

            sage: R.<t> = PolynomialRing(GF(37))
            sage: H = HyperellipticCurve(t^5 + t + 2)
            sage: H.frobenius_polynomial_cardinalities()
            x^4 + x^3 - 52*x^2 + 37*x + 1369

        A quadratic twist::

            sage: H = HyperellipticCurve(2*t^5 + 2*t + 4)
            sage: H.frobenius_polynomial_cardinalities()
            x^4 - x^3 - 52*x^2 - 37*x + 1369

        Curve over a non-prime field::

            sage: K.<z> = GF(7**2)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^5 + z*t + z^2)
            sage: H.frobenius_polynomial_cardinalities()
            x^4 + 8*x^3 + 70*x^2 + 392*x + 2401

        This method may actually be useful when ``hypellfrob`` does not work::

            sage: K = GF(7)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + t^3 + 1)
            sage: H.frobenius_polynomial_matrix(algorithm='hypellfrob')
            Traceback (most recent call last):
            ...
            ValueError: In the current implementation, p must be greater than (2g+1)(2N-1) = 81
            sage: H.frobenius_polynomial_cardinalities()
            x^8 - 5*x^7 + 7*x^6 + 36*x^5 - 180*x^4 + 252*x^3 + 343*x^2 - 1715*x + 2401
        """
    def frobenius_polynomial_matrix(self, M=None, algorithm: str = 'hypellfrob'):
        """
        Compute the charpoly of frobenius, as an element of `\\ZZ[x]`,
        by computing the charpoly of the frobenius matrix.

        This is currently only supported when the base field is prime
        and large enough using the ``hypellfrob`` library.

        EXAMPLES::

            sage: R.<t> = PolynomialRing(GF(37))
            sage: H = HyperellipticCurve(t^5 + t + 2)
            sage: H.frobenius_polynomial_matrix()
            x^4 + x^3 - 52*x^2 + 37*x + 1369

        A quadratic twist::

            sage: H = HyperellipticCurve(2*t^5 + 2*t + 4)
            sage: H.frobenius_polynomial_matrix()
            x^4 - x^3 - 52*x^2 - 37*x + 1369

        Curves defined over larger prime fields::

            sage: K = GF(49999)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + t^5 + 1)
            sage: H.frobenius_polynomial_matrix()
            x^8 + 281*x^7 + 55939*x^6 + 14144175*x^5 + 3156455369*x^4 + 707194605825*x^3
            + 139841906155939*x^2 + 35122892542149719*x + 6249500014999800001
            sage: H = HyperellipticCurve(t^15 + t^5 + 1)
            sage: H.frobenius_polynomial_matrix()  # long time, 8s on a Corei7
            x^14 - 76*x^13 + 220846*x^12 - 12984372*x^11 + 24374326657*x^10 - 1203243210304*x^9
            + 1770558798515792*x^8 - 74401511415210496*x^7 + 88526169366991084208*x^6
            - 3007987702642212810304*x^5 + 3046608028331197124223343*x^4
            - 81145833008762983138584372*x^3 + 69007473838551978905211279154*x^2
            - 1187357507124810002849977200076*x + 781140631562281254374947500349999

        This ``hypellfrob`` program doesn't support non-prime fields::

            sage: K.<z> = GF(37**3)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + z*t^3 + 1)
            sage: H.frobenius_polynomial_matrix(algorithm='hypellfrob')
            Traceback (most recent call last):
            ...
            NotImplementedError: Computation of Frobenius matrix only implemented
            for hyperelliptic curves defined over prime fields.
        """
    def frobenius_polynomial_pari(self):
        """
        Compute the charpoly of frobenius, as an element of `\\ZZ[x]`,
        by calling the PARI function ``hyperellcharpoly``.

        EXAMPLES::

            sage: R.<t> = PolynomialRing(GF(37))
            sage: H = HyperellipticCurve(t^5 + t + 2)
            sage: H.frobenius_polynomial_pari()
            x^4 + x^3 - 52*x^2 + 37*x + 1369

        A quadratic twist::

            sage: H = HyperellipticCurve(2*t^5 + 2*t + 4)
            sage: H.frobenius_polynomial_pari()
            x^4 - x^3 - 52*x^2 - 37*x + 1369

        Slightly larger example::

            sage: K = GF(2003)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^7 + 487*t^5 + 9*t + 1)
            sage: H.frobenius_polynomial_pari()
            x^6 - 14*x^5 + 1512*x^4 - 66290*x^3 + 3028536*x^2 - 56168126*x + 8036054027

        Curves defined over a non-prime field are supported as well::

            sage: K.<a> = GF(7^2)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^5 + a*t + 1)
            sage: H.frobenius_polynomial_pari()
            x^4 + 4*x^3 + 84*x^2 + 196*x + 2401

            sage: K.<z> = GF(23**3)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^3 + z*t + 4)
            sage: H.frobenius_polynomial_pari()
            x^2 - 15*x + 12167

        Over prime fields of odd characteristic, `h` may be nonzero::

            sage: K = GF(101)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^5 + 27*t + 3, t)
            sage: H.frobenius_polynomial_pari()
            x^4 + 2*x^3 - 58*x^2 + 202*x + 10201

        TESTS:

        Check that :issue:`28789` is fixed::

            sage: P.<x> = PolynomialRing(GF(3))
            sage: u = x^10 + x^9 + x^8 + x
            sage: C = HyperellipticCurve(u)
            sage: C.frobenius_polynomial_pari()
            x^8 + 2*x^7 + 6*x^6 + 9*x^5 + 18*x^4 + 27*x^3 + 54*x^2 + 54*x + 81
        """
    @cached_method
    def frobenius_polynomial(self):
        """
        Compute the charpoly of frobenius, as an element of `\\ZZ[x]`.

        EXAMPLES::

            sage: R.<t> = PolynomialRing(GF(37))
            sage: H = HyperellipticCurve(t^5 + t + 2)
            sage: H.frobenius_polynomial()
            x^4 + x^3 - 52*x^2 + 37*x + 1369

        A quadratic twist::

            sage: H = HyperellipticCurve(2*t^5 + 2*t + 4)
            sage: H.frobenius_polynomial()
            x^4 - x^3 - 52*x^2 - 37*x + 1369

        Slightly larger example::

            sage: K = GF(2003)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^7 + 487*t^5 + 9*t + 1)
            sage: H.frobenius_polynomial()
            x^6 - 14*x^5 + 1512*x^4 - 66290*x^3 + 3028536*x^2 - 56168126*x + 8036054027

        Curves defined over a non-prime field of odd characteristic,
        or an odd prime field which is too small compared to the genus,
        are supported via PARI::

            sage: K.<z> = GF(23**3)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^3 + z*t + 4)
            sage: H.frobenius_polynomial()
            x^2 - 15*x + 12167

            sage: K.<z> = GF(3**3)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^5 + z*t + z**3)
            sage: H.frobenius_polynomial()
            x^4 - 3*x^3 + 10*x^2 - 81*x + 729

        Over prime fields of odd characteristic, `h` may be nonzero::

            sage: K = GF(101)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^5 + 27*t + 3, t)
            sage: H.frobenius_polynomial()
            x^4 + 2*x^3 - 58*x^2 + 202*x + 10201

        Over prime fields of odd characteristic, `f` may have even degree::

            sage: H = HyperellipticCurve(t^6 + 27*t + 3)
            sage: H.frobenius_polynomial()
            x^4 + 25*x^3 + 322*x^2 + 2525*x + 10201

        In even characteristic, the naive algorithm could cover all cases
        because we can easily check for squareness in quotient rings of
        polynomial rings over finite fields but these rings unfortunately
        do not support iteration::

            sage: K.<z> = GF(2**5)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^5 + z*t + z**3, t)
            sage: H.frobenius_polynomial()
            x^4 - x^3 + 16*x^2 - 32*x + 1024

        TESTS:

        Check that :issue:`28789` is fixed::

            sage: P.<x> = PolynomialRing(GF(3))
            sage: u = x^10 + x^9 + x^8 + x
            sage: C = HyperellipticCurve(u)
            sage: C.frobenius_polynomial()
            x^8 + 2*x^7 + 6*x^6 + 9*x^5 + 18*x^4 + 27*x^3 + 54*x^2 + 54*x + 81
        """
    def points(self):
        """
        All the points on this hyperelliptic curve.

        EXAMPLES::

            sage: x = polygen(GF(7))
            sage: C = HyperellipticCurve(x^7 - x^2 - 1)
            sage: C.points()
            [(0 : 1 : 0), (2 : 5 : 1), (2 : 2 : 1), (3 : 0 : 1), (4 : 6 : 1),
             (4 : 1 : 1), (5 : 0 : 1), (6 : 5 : 1), (6 : 2 : 1)]

        ::

            sage: x = polygen(GF(121, 'a'))
            sage: C = HyperellipticCurve(x^5 + x - 1, x^2 + 2)
            sage: len(C.points())
            122

        Conics are allowed (the issue reported at :issue:`11800`
        has been resolved)::

            sage: R.<x> = GF(7)[]
            sage: H = HyperellipticCurve(3*x^2 + 5*x + 1)
            sage: H.points()
            [(0 : 6 : 1), (0 : 1 : 1), (1 : 4 : 1), (1 : 3 : 1), (2 : 4 : 1),
             (2 : 3 : 1), (3 : 6 : 1), (3 : 1 : 1)]

        The method currently lists points on the plane projective model, that
        is the closure in `\\mathbb{P}^2` of the curve defined by `y^2+hy=f`.
        This means that one point `(0:1:0)` at infinity is returned if the
        degree of the curve is at least 4 and `\\deg(f)>\\deg(h)+1`. This point
        is a singular point of the plane model. Later implementations may
        consider a smooth model instead since that would be a more relevant
        object. Then, for a curve whose only singularity is at `(0:1:0)`, the
        point at infinity would be replaced by a number of rational points of
        the smooth model. We illustrate this with an example of a genus 2
        hyperelliptic curve::

            sage: R.<x>=GF(11)[]
            sage: H = HyperellipticCurve(x*(x+1)*(x+2)*(x+3)*(x+4)*(x+5))
            sage: H.points()
            [(0 : 1 : 0), (0 : 0 : 1), (1 : 7 : 1), (1 : 4 : 1), (5 : 7 : 1), (5 : 4 : 1),
             (6 : 0 : 1), (7 : 0 : 1), (8 : 0 : 1), (9 : 0 : 1), (10 : 0 : 1)]

        The plane model of the genus 2 hyperelliptic curve in the above example
        is the curve in `\\mathbb{P}^2` defined by `y^2z^4=g(x,z)` where
        `g(x,z)=x(x+z)(x+2z)(x+3z)(x+4z)(x+5z).` This model has one point at
        infinity `(0:1:0)` which is also the only singular point of the plane
        model. In contrast, the hyperelliptic curve is smooth and imbeds via
        the equation `y^2=g(x,z)` into weighted projected space
        `\\mathbb{P}(1,3,1)`. The latter model has two points at infinity:
        `(1:1:0)` and `(1:-1:0)`.
        """
    def count_points_matrix_traces(self, n: int = 1, M=None, N=None):
        """
        Count the number of points on the curve over the first `n` extensions
        of the base field by computing traces of powers of the frobenius
        matrix.
        This requires less `p`-adic precision than computing the charpoly
        of the matrix when `n < g` where `g` is the genus of the curve.

        EXAMPLES::

            sage: K = GF(49999)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^19 + t + 1)
            sage: H.count_points_matrix_traces(3)
            [49491, 2500024375, 124992509154249]

        TESTS:

        Check that :issue:`18831` is fixed::

            sage: R.<t> = PolynomialRing(GF(11))
            sage: H = HyperellipticCurve(t^5 - t + 1)
            sage: H.count_points_matrix_traces()
            Traceback (most recent call last):
            ...
            ValueError: In the current implementation, p must be greater than (2g+1)(2N-1) = 15
        """
    def count_points_frobenius_polynomial(self, n: int = 1, f=None):
        """
        Count the number of points on the curve over the first `n` extensions
        of the base field by computing the frobenius polynomial.

        EXAMPLES::

            sage: K = GF(49999)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^19 + t + 1)

        The following computation takes a long time as the complete
        characteristic polynomial of the frobenius is computed::

            sage: H.count_points_frobenius_polynomial(3) # long time, 20s on a Corei7 (when computed before the following test of course)
            [49491, 2500024375, 124992509154249]

        As the polynomial is cached, further computations of number of points
        are really fast::

            sage: H.count_points_frobenius_polynomial(19) # long time, because of the previous test
            [49491,
            2500024375,
            124992509154249,
            6249500007135192947,
            312468751250758776051811,
            15623125093747382662737313867,
            781140631562281338861289572576257,
            39056250437482500417107992413002794587,
            1952773465623687539373429411200893147181079,
            97636720507718753281169963459063147221761552935,
            4881738388665429945305281187129778704058864736771824,
            244082037694882831835318764490138139735446240036293092851,
            12203857802706446708934102903106811520015567632046432103159713,
            610180686277519628999996211052002771035439565767719719151141201339,
            30508424133189703930370810556389262704405225546438978173388673620145499,
            1525390698235352006814610157008906752699329454643826047826098161898351623931,
            76268009521069364988723693240288328729528917832735078791261015331201838856825193,
            3813324208043947180071195938321176148147244128062172555558715783649006587868272993991,
            190662397077989315056379725720120486231213267083935859751911720230901597698389839098903847]
        """
    def count_points_exhaustive(self, n: int = 1, naive: bool = False):
        """
        Count the number of points on the curve over the first `n` extensions
        of the base field by exhaustive search if `n` if smaller than `g`,
        the genus of the curve, and by computing the frobenius polynomial
        after performing exhaustive search on the first `g` extensions if
        `n > g` (unless ``naive == True``).

        EXAMPLES::

            sage: K = GF(5)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + t^3 + 1)
            sage: H.count_points_exhaustive(n=5)
            [9, 27, 108, 675, 3069]

        When `n > g`, the frobenius polynomial is computed from the numbers
        of points of the curve over the first `g` extension, so that computing
        the number of points on extensions of degree `n > g` is not much more
        expensive than for `n == g`::

            sage: H.count_points_exhaustive(n=15)
            [9,
            27,
            108,
            675,
            3069,
            16302,
            78633,
            389475,
            1954044,
            9768627,
            48814533,
            244072650,
            1220693769,
            6103414827,
            30517927308]

        This behavior can be disabled by passing ``naive=True``::

           sage: H.count_points_exhaustive(n=6, naive=True) # long time, 7s on a Corei7
           [9, 27, 108, 675, 3069, 16302]
        """
    def count_points_hypellfrob(self, n: int = 1, N=None, algorithm=None):
        """
        Count the number of points on the curve over the first `n` extensions
        of the base field using the ``hypellfrob`` program.

        This only supports prime fields of large enough characteristic.

        EXAMPLES::

            sage: K = GF(49999)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^21 + 3*t^5 + 5)
            sage: H.count_points_hypellfrob()
            [49804]
            sage: H.count_points_hypellfrob(2)
            [49804, 2499799038]

            sage: K = GF(2**7-1)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^11 + 3*t^5 + 5)
            sage: H.count_points_hypellfrob()
            [127]
            sage: H.count_points_hypellfrob(n=5)
            [127, 16335, 2045701, 260134299, 33038098487]

            sage: K = GF(2**7-1)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^13 + 3*t^5 + 5)
            sage: H.count_points(n=6)
            [112, 16360, 2045356, 260199160, 33038302802, 4195868633548]

        The base field should be prime::

            sage: K.<z> = GF(19**10)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + (z+1)*t^5 + 1)
            sage: H.count_points_hypellfrob()
            Traceback (most recent call last):
            ...
            ValueError: hypellfrob does not support non-prime fields

        and the characteristic should be large enough::

            sage: K = GF(7)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + t^3 + 1)
            sage: H.count_points_hypellfrob()
            Traceback (most recent call last):
            ...
            ValueError: p=7 should be greater than (2*g+1)(2*N-1)=27
        """
    def count_points(self, n: int = 1):
        """
        Count points over finite fields.

        INPUT:

        - ``n`` -- integer

        OUTPUT:

        An integer. The number of points over `\\GF{q}, \\ldots,
        \\GF{q^n}` on a hyperelliptic curve over a finite field `\\GF{q}`.

        .. WARNING::

           This is currently using exhaustive search for hyperelliptic curves
           over non-prime fields, which can be awfully slow.

        EXAMPLES::

            sage: P.<x> = PolynomialRing(GF(3))
            sage: C = HyperellipticCurve(x^3+x^2+1)
            sage: C.count_points(4)
            [6, 12, 18, 96]
            sage: C.base_extend(GF(9,'a')).count_points(2)
            [12, 96]

            sage: K = GF(2**31-1)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^5 + 3*t + 5)
            sage: H.count_points() # long time, 2.4 sec on a Corei7
            [2147464821]
            sage: H.count_points(n=2) # long time, 30s on a Corei7
            [2147464821, 4611686018988310237]

            sage: K = GF(2**7-1)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^13 + 3*t^5 + 5)
            sage: H.count_points(n=6)
            [112, 16360, 2045356, 260199160, 33038302802, 4195868633548]

            sage: P.<x> = PolynomialRing(GF(3))
            sage: H = HyperellipticCurve(x^3+x^2+1)
            sage: C1 = H.count_points(4); C1
            [6, 12, 18, 96]
            sage: C2 = sage.schemes.generic.scheme.Scheme.count_points(H,4); C2 # long time, 2s on a Corei7
            [6, 12, 18, 96]
            sage: C1 == C2 # long time, because we need C2 to be defined
            True

            sage: P.<x> = PolynomialRing(GF(9,'a'))
            sage: H = HyperellipticCurve(x^5+x^2+1)
            sage: H.count_points(5)
            [18, 78, 738, 6366, 60018]

            sage: F.<a> = GF(4); P.<x> = F[]
            sage: H = HyperellipticCurve(x^5+a*x^2+1, x+a+1)
            sage: H.count_points(6)
            [2, 24, 74, 256, 1082, 4272]

        This example shows that :issue:`20391` is resolved::

            sage: x = polygen(GF(4099))
            sage: H = HyperellipticCurve(x^6 + x + 1)
            sage: H.count_points(1)
            [4106]
        """
    def cardinality_exhaustive(self, extension_degree: int = 1, algorithm=None):
        """
        Count points on a single extension of the base field
        by enumerating over x and solving the resulting quadratic
        equation for y.

        EXAMPLES::

            sage: K.<a> = GF(9, 'a')
            sage: x = polygen(K)
            sage: C = HyperellipticCurve(x^7 - 1, x^2 + a)
            sage: C.cardinality_exhaustive()
            7

            sage: K = GF(next_prime(1<<10))
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^7 + 3*t^5 + 5)
            sage: H.cardinality_exhaustive()
            1025

            sage: P.<x> = PolynomialRing(GF(9,'a'))
            sage: H = HyperellipticCurve(x^5+x^2+1)
            sage: H.count_points(5)
            [18, 78, 738, 6366, 60018]

            sage: F.<a> = GF(4); P.<x> = F[]
            sage: H = HyperellipticCurve(x^5+a*x^2+1, x+a+1)
            sage: H.count_points(6)
            [2, 24, 74, 256, 1082, 4272]

        TESTS:

        Check for :issue:`19122`::

            sage: x = polygen(GF(19), 'x')
            sage: f = 15*x^4 + 7*x^3 + 3*x^2 + 7*x + 18
            sage: HyperellipticCurve(f).cardinality_exhaustive(1)
            19

        Points at infinity on general curves of genus 1 are counted
        correctly (see :issue:`21195`)::

            sage: S.<z> = PolynomialRing(ZZ)
            sage: C = HyperellipticCurve(-z^2 + z, z^2)
            sage: C.base_extend(GF(2)).count_points_exhaustive()
            [5]
            sage: C.base_extend(GF(3)).count_points_exhaustive()
            [5]
        """
    def cardinality_hypellfrob(self, extension_degree: int = 1, algorithm=None):
        """
        Count points on a single extension of the base field
        using the ``hypellfrob`` program.

        EXAMPLES::

            sage: K = GF(next_prime(1<<10))
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^7 + 3*t^5 + 5)
            sage: H.cardinality_hypellfrob()
            1025

            sage: K = GF(49999)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^7 + 3*t^5 + 5)
            sage: H.cardinality_hypellfrob()
            50162
            sage: H.cardinality_hypellfrob(3)
            124992471088310
        """
    @cached_method
    def cardinality(self, extension_degree: int = 1):
        """
        Count points on a single extension of the base field.

        EXAMPLES::

            sage: K = GF(101)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + 3*t^5 + 5)
            sage: H.cardinality()
            106
            sage: H.cardinality(15)
            1160968955369992567076405831000
            sage: H.cardinality(100)
            270481382942152609326719471080753083367793838278100277689020104911710151430673927943945601434674459120495370826289654897190781715493352266982697064575800553229661690000887425442240414673923744999504000

            sage: K = GF(37)
            sage: R.<t> = PolynomialRing(K)
            sage: H = HyperellipticCurve(t^9 + 3*t^5 + 5)
            sage: H.cardinality()
            40
            sage: H.cardinality(2)
            1408
            sage: H.cardinality(3)
            50116

        The following example shows that :issue:`20391` has been resolved::

            sage: F=GF(23)
            sage: x=polygen(F)
            sage: C=HyperellipticCurve(x^8+1)
            sage: C.cardinality()
            24
        """
    def zeta_function(self):
        """
        Compute the zeta function of the hyperelliptic curve.

        EXAMPLES::

            sage: F = GF(2); R.<t> = F[]
            sage: H = HyperellipticCurve(t^9 + t, t^4)
            sage: H.zeta_function()
            (16*x^8 + 8*x^7 + 8*x^6 + 4*x^5 + 6*x^4 + 2*x^3 + 2*x^2 + x + 1)/(2*x^2 - 3*x + 1)

            sage: F.<a> = GF(4); R.<t> = F[]
            sage: H = HyperellipticCurve(t^5 + t^3 + t^2 + t + 1, t^2 + t + 1)
            sage: H.zeta_function()
            (16*x^4 + 8*x^3 + x^2 + 2*x + 1)/(4*x^2 - 5*x + 1)

            sage: F.<a> = GF(9); R.<t> = F[]
            sage: H = HyperellipticCurve(t^5 + a*t)
            sage: H.zeta_function()
            (81*x^4 + 72*x^3 + 32*x^2 + 8*x + 1)/(9*x^2 - 10*x + 1)

            sage: R.<t> = PolynomialRing(GF(37))
            sage: H = HyperellipticCurve(t^5 + t + 2)
            sage: H.zeta_function()
            (1369*x^4 + 37*x^3 - 52*x^2 + x + 1)/(37*x^2 - 38*x + 1)

        A quadratic twist::

            sage: R.<t> = PolynomialRing(GF(37))
            sage: H = HyperellipticCurve(2*t^5 + 2*t + 4)
            sage: H.zeta_function()
            (1369*x^4 - 37*x^3 - 52*x^2 - x + 1)/(37*x^2 - 38*x + 1)
        """
    def Cartier_matrix(self):
        """
        INPUT:

        - ``self`` -- Hyperelliptic Curve of the form `y^2 = f(x)` over a
          finite field, `\\GF{q}`

        OUTPUT:

        The matrix `M = (c_{pi-j})`, where `c_i` are the coefficients of
        `f(x)^{(p-1)/2} = \\sum c_i x^i`.

        REFERENCES:

        N. Yui. On the Jacobian varieties of hyperelliptic curves over fields of characteristic `p > 2`.

        EXAMPLES::

            sage: K.<x> = GF(9,'x')[]
            sage: C = HyperellipticCurve(x^7 - 1, 0)
            sage: C.Cartier_matrix()
            [0 0 2]
            [0 0 0]
            [0 1 0]

            sage: K.<x> = GF(49, 'x')[]
            sage: C = HyperellipticCurve(x^5 + 1, 0)
            sage: C.Cartier_matrix()
            [0 3]
            [0 0]

            sage: P.<x> = GF(9, 'a')[]
            sage: E = HyperellipticCurve(x^29 + 1, 0)
            sage: E.Cartier_matrix()
            [0 0 1 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 1 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 1 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 1 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [1 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 1 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 1 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 1 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 1 0]

        TESTS::

            sage: K.<x>=GF(2,'x')[]
            sage: C=HyperellipticCurve(x^7-1,x)
            sage: C.Cartier_matrix()
            Traceback (most recent call last):
            ...
            ValueError: p must be odd

            sage: K.<x>=GF(5,'x')[]
            sage: C=HyperellipticCurve(x^7-1,4)
            sage: C.Cartier_matrix()
            Traceback (most recent call last):
            ...
            ValueError: E must be of the form y^2 = f(x)

            sage: K.<x>=GF(5,'x')[]
            sage: C=HyperellipticCurve(x^8-1,0)
            sage: C.Cartier_matrix()
            Traceback (most recent call last):
            ...
            ValueError: In this implementation the degree of f must be odd

            sage: K.<x>=GF(5,'x')[]
            sage: C=HyperellipticCurve(x^5+1,0,check_squarefree=False)
            sage: C.Cartier_matrix()
            Traceback (most recent call last):
            ...
            ValueError: curve is not smooth
        """
    def Hasse_Witt(self):
        """
        INPUT:

        - ``self`` -- Hyperelliptic Curve of the form `y^2 = f(x)` over a
          finite field, `\\GF{q}`

        OUTPUT:

        The matrix `N = M M^p \\dots M^{p^{g-1}}` where `M = c_{pi-j}`, and
        `f(x)^{(p-1)/2} = \\sum c_i x^i`.

        Reference-N. Yui. On the Jacobian varieties of hyperelliptic curves over fields of characteristic `p > 2`.

        EXAMPLES::

            sage: K.<x> = GF(9, 'x')[]
            sage: C = HyperellipticCurve(x^7 - 1, 0)
            sage: C.Hasse_Witt()
            [0 0 0]
            [0 0 0]
            [0 0 0]

            sage: K.<x> = GF(49, 'x')[]
            sage: C = HyperellipticCurve(x^5 + 1, 0)
            sage: C.Hasse_Witt()
            [0 0]
            [0 0]

            sage: P.<x> = GF(9, 'a')[]
            sage: E = HyperellipticCurve(x^29 + 1, 0)
            sage: E.Hasse_Witt()
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0 0 0 0 0 0 0]
        """
    def a_number(self):
        """
        INPUT:

        - ``self`` -- Hyperelliptic Curve of the form `y^2 = f(x)` over a
          finite field, `\\GF{q}`

        OUTPUT: a-number

        EXAMPLES::

            sage: K.<x> = GF(49, 'x')[]
            sage: C = HyperellipticCurve(x^5 + 1, 0)
            sage: C.a_number()
            1

            sage: K.<x> = GF(9, 'x')[]
            sage: C = HyperellipticCurve(x^7 - 1, 0)
            sage: C.a_number()
            1

            sage: P.<x> = GF(9, 'a')[]
            sage: E = HyperellipticCurve(x^29 + 1, 0)
            sage: E.a_number()
            5
        """
    def p_rank(self):
        """
        INPUT:

        - ``self`` -- Hyperelliptic Curve of the form `y^2 = f(x)` over a
          finite field, `\\GF{q}`

        OUTPUT: p-rank

        EXAMPLES::

            sage: K.<x> = GF(49, 'x')[]
            sage: C = HyperellipticCurve(x^5 + 1, 0)
            sage: C.p_rank()
            0

            sage: K.<x> = GF(9, 'x')[]
            sage: C = HyperellipticCurve(x^7 - 1, 0)
            sage: C.p_rank()
            0

            sage: P.<x> = GF(9, 'a')[]
            sage: E = HyperellipticCurve(x^29 + 1, 0)
            sage: E.p_rank()
            0
        """
