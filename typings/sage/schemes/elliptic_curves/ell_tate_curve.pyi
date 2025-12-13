from sage.matrix.constructor import matrix as matrix
from sage.misc.functional import denominator as denominator, log as log
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.misc.misc_c import prod as prod
from sage.modular.modform.constructor import CuspForms as CuspForms, EisensteinForms as EisensteinForms
from sage.rings.integer_ring import ZZ as ZZ
from sage.schemes.elliptic_curves.constructor import EllipticCurve as EllipticCurve
from sage.structure.richcmp import richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

class TateCurve(SageObject):
    """
    Tate's `p`-adic uniformisation of an elliptic curve with
    multiplicative reduction.

    .. NOTE::

        Some of the methods of this Tate curve only work when the
        reduction is split multiplicative over `\\QQ_p`.

    EXAMPLES::

        sage: e = EllipticCurve('130a1')
        sage: eq = e.tate_curve(5); eq
        5-adic Tate curve associated to the Elliptic Curve
         defined by y^2 + x*y + y = x^3 - 33*x + 68 over Rational Field
        sage: eq == loads(dumps(eq))
        True

    REFERENCES: [Sil1994]_
    """
    def __init__(self, E, p) -> None:
        """
        INPUT:

        - ``E`` -- an elliptic curve over the rational numbers

        - ``p`` -- a prime where `E` has multiplicative reduction,
          i.e., such that `j(E)` has negative valuation

        EXAMPLES::

            sage: e = EllipticCurve('130a1')
            sage: eq = e.tate_curve(2); eq
            2-adic Tate curve associated to the Elliptic Curve
             defined by y^2 + x*y + y = x^3 - 33*x + 68 over Rational Field
        """
    def __richcmp__(self, other, op):
        """
        Compare ``self`` and ``other``.

        TESTS::

            sage: E = EllipticCurve('35a')
            sage: eq5 = E.tate_curve(5)
            sage: eq7 = E.tate_curve(7)
            sage: eq7 == eq7
            True
            sage: eq7 == eq5
            False
        """
    def original_curve(self):
        """
        Return the elliptic curve the Tate curve was constructed from.

        EXAMPLES::

            sage: eq = EllipticCurve('130a1').tate_curve(5)
            sage: eq.original_curve()
            Elliptic Curve defined by y^2 + x*y + y = x^3 - 33*x + 68
             over Rational Field
        """
    def prime(self):
        """
        Return the residual characteristic `p`.

        EXAMPLES::

            sage: eq = EllipticCurve('130a1').tate_curve(5)
            sage: eq.original_curve()
            Elliptic Curve defined by y^2 + x*y + y = x^3 - 33*x + 68
             over Rational Field
            sage: eq.prime()
            5
        """
    def parameter(self, prec: int = 20):
        """
        Return the Tate parameter `q` such that the curve is isomorphic
        over the algebraic closure of `\\QQ_p` to the curve
        `\\QQ_p^{\\times}/q^{\\ZZ}`.

        INPUT:

        - ``prec`` -- the `p`-adic precision (default: 20)

        EXAMPLES::

            sage: eq = EllipticCurve('130a1').tate_curve(5)
            sage: eq.parameter(prec=5)
            3*5^3 + 3*5^4 + 2*5^5 + 2*5^6 + 3*5^7 + O(5^8)
        """
    def curve(self, prec: int = 20):
        """
        Return the `p`-adic elliptic curve of the form
        `y^2+x y = x^3 + s_4 x+s_6`.

        This curve with split multiplicative reduction is isomorphic
        to the given curve over the algebraic closure of `\\QQ_p`.

        INPUT:

        - ``prec`` -- the `p`-adic precision (default: 20)

        EXAMPLES::

            sage: eq = EllipticCurve('130a1').tate_curve(5)
            sage: eq.curve(prec=5)
            Elliptic Curve defined by y^2 + (1+O(5^5))*x*y =
             x^3 + (2*5^4+5^5+2*5^6+5^7+3*5^8+O(5^9))*x + (2*5^3+5^4+2*5^5+5^7+O(5^8))
             over 5-adic Field with capped relative precision 5
        """
    def E2(self, prec: int = 20):
        """
        Return the value of the `p`-adic Eisenstein series of weight 2
        evaluated on the elliptic curve having split multiplicative
        reduction.

        INPUT:

        - ``prec`` -- the `p`-adic precision (default: 20)

        EXAMPLES::

            sage: eq = EllipticCurve('130a1').tate_curve(5)
            sage: eq.E2(prec=10)
            4 + 2*5^2 + 2*5^3 + 5^4 + 2*5^5 + 5^7 + 5^8 + 2*5^9 + O(5^10)

            sage: T = EllipticCurve('14').tate_curve(7)
            sage: T.E2(30)
            2 + 4*7 + 7^2 + 3*7^3 + 6*7^4 + 5*7^5 + 2*7^6 + 7^7 + 5*7^8 + 6*7^9 + 5*7^10 + 2*7^11 + 6*7^12 + 4*7^13 + 3*7^15 + 5*7^16 + 4*7^17 + 4*7^18 + 2*7^20 + 7^21 + 5*7^22 + 4*7^23 + 4*7^24 + 3*7^25 + 6*7^26 + 3*7^27 + 6*7^28 + O(7^30)
        """
    def is_split(self) -> bool:
        """
        Return ``True`` if the given elliptic curve has split multiplicative reduction.

        EXAMPLES::

            sage: eq = EllipticCurve('130a1').tate_curve(5)
            sage: eq.is_split()
            True

            sage: eq = EllipticCurve('37a1').tate_curve(37)
            sage: eq.is_split()
            False
        """
    def parametrisation_onto_tate_curve(self, u, prec=None):
        """
        Given an element `u` in `\\QQ_p^{\\times}`, this computes its image on the Tate curve
        under the `p`-adic uniformisation of `E`.

        INPUT:

        - ``u`` -- a nonzero `p`-adic number

        - ``prec`` -- the `p`-adic precision; default is the relative precision
          of ``u``, otherwise 20

        EXAMPLES::

            sage: eq = EllipticCurve('130a1').tate_curve(5)
            sage: eq.parametrisation_onto_tate_curve(1+5+5^2+O(5^10), prec=10)
            (5^-2 + 4*5^-1 + 1 + 2*5 + 3*5^2 + 2*5^5 + 3*5^6 + O(5^7)
             : 4*5^-3 + 2*5^-1 + 4 + 2*5 + 3*5^4 + 2*5^5 + O(5^6) : 1 + O(5^10))
            sage: eq.parametrisation_onto_tate_curve(1+5+5^2+O(5^10))
            (5^-2 + 4*5^-1 + 1 + 2*5 + 3*5^2 + 2*5^5 + 3*5^6 + O(5^7)
             : 4*5^-3 + 2*5^-1 + 4 + 2*5 + 3*5^4 + 2*5^5 + O(5^6) : 1 + O(5^10))
            sage: eq.parametrisation_onto_tate_curve(1+5+5^2+O(5^10), prec=20)
            Traceback (most recent call last):
            ...
            ValueError: requested more precision than the precision of u
        """
    def L_invariant(self, prec: int = 20):
        """
        Return the *mysterious* `\\mathcal{L}`-invariant associated
        to an elliptic curve with split multiplicative reduction.

        One instance where this constant appears is in the exceptional
        case of the `p`-adic Birch and Swinnerton-Dyer conjecture as
        formulated in [MTT1986]_. See [Col2004]_ for a detailed discussion.

        INPUT:

        - ``prec`` -- the `p`-adic precision (default: 20)

        EXAMPLES::

            sage: eq = EllipticCurve('130a1').tate_curve(5)
            sage: eq.L_invariant(prec=10)
            5^3 + 4*5^4 + 2*5^5 + 2*5^6 + 2*5^7 + 3*5^8 + 5^9 + O(5^10)
        """
    def lift(self, P, prec: int = 20):
        """
        Given a point `P` in the formal group of the elliptic curve `E` with split multiplicative reduction,
        this produces an element `u` in `\\QQ_p^{\\times}` mapped to the point `P` by the Tate parametrisation.
        The algorithm return the unique such element in `1+p\\ZZ_p`.

        INPUT:

        - ``P`` -- a point on the elliptic curve

        - ``prec`` -- the `p`-adic precision (default: 20)

        EXAMPLES::

            sage: e = EllipticCurve('130a1')
            sage: eq = e.tate_curve(5)
            sage: P = e([-6,10])
            sage: l = eq.lift(12*P, prec=10); l
            1 + 4*5 + 5^3 + 5^4 + 4*5^5 + 5^6 + 5^7 + 4*5^8 + 5^9 + O(5^10)

        Now we map the lift l back and check that it is indeed right.::

            sage: eq.parametrisation_onto_original_curve(l)
            (4*5^-2 + 2*5^-1 + 4*5 + 3*5^3 + 5^4 + 2*5^5 + 4*5^6 + O(5^7)
             : 2*5^-3 + 5^-1 + 4 + 4*5 + 5^2 + 3*5^3 + 4*5^4 + O(5^6) : 1 + O(5^10))
            sage: e5 = e.change_ring(Qp(5,9))
            sage: e5(12*P)
            (4*5^-2 + 2*5^-1 + 4*5 + 3*5^3 + 5^4 + 2*5^5 + 4*5^6 + O(5^7)
             : 2*5^-3 + 5^-1 + 4 + 4*5 + 5^2 + 3*5^3 + 4*5^4 + O(5^6) : 1 + O(5^9))
        """
    def parametrisation_onto_original_curve(self, u, prec=None):
        """
        Given an element `u` in `\\QQ_p^{\\times}`, this computes its image on the original curve
        under the `p`-adic uniformisation of `E`.

        INPUT:

        - ``u`` -- a nonzero `p`-adic number

        - ``prec`` -- the `p`-adic precision; default is the relative precision
          of ``u``, otherwise 20

        EXAMPLES::

            sage: eq = EllipticCurve('130a1').tate_curve(5)
            sage: eq.parametrisation_onto_original_curve(1+5+5^2+O(5^10))
            (4*5^-2 + 4*5^-1 + 4 + 2*5^3 + 3*5^4 + 2*5^6 + O(5^7) :
             3*5^-3 + 5^-2 + 4*5^-1 + 1 + 4*5 + 5^2 + 3*5^5 + O(5^6) :
             1 + O(5^10))
            sage: eq.parametrisation_onto_original_curve(1+5+5^2+O(5^10), prec=20)
            Traceback (most recent call last):
            ...
            ValueError: requested more precision than the precision of u

        Here is how one gets a 4-torsion point on `E` over `\\QQ_5`::

            sage: R = Qp(5,30)
            sage: i = R(-1).sqrt()
            sage: T = eq.parametrisation_onto_original_curve(i, prec=30); T
            (2 + 3*5 + 4*5^2 + 2*5^3 + 5^4 + 4*5^5 + 2*5^7 + 5^8 + 5^9 + 5^12 + 3*5^13 + 3*5^14 + 5^15 + 4*5^17 + 5^18 + 3*5^19 + 2*5^20 + 4*5^21 + 5^22 + 3*5^23 + 3*5^24 + 4*5^25 + 3*5^26 + 3*5^27 + 3*5^28 + 3*5^29 + O(5^30) : 3*5 + 5^2 + 5^4 + 3*5^5 + 3*5^7 + 2*5^8 + 4*5^9 + 5^10 + 2*5^11 + 4*5^13 + 2*5^14 + 4*5^15 + 4*5^16 + 3*5^17 + 2*5^18 + 4*5^20 + 2*5^21 + 2*5^22 + 4*5^23 + 4*5^24 + 4*5^25 + 5^26 + 3*5^27 + 2*5^28 + O(5^30) : 1 + O(5^30))
            sage: 4*T
            (0 : 1 + O(5^30) : 0)
        """
    def padic_height(self, prec: int = 20):
        """
        Return the canonical `p`-adic height function on the original curve.

        INPUT:

        - ``prec`` -- the `p`-adic precision (default: 20)

        OUTPUT: a function that can be evaluated on rational points of `E`

        EXAMPLES::

            sage: e = EllipticCurve('130a1')
            sage: eq = e.tate_curve(5)
            sage: h = eq.padic_height(prec=10)
            sage: P = e.gens()[0]
            sage: h(P)
            2*5^-1 + 1 + 2*5 + 2*5^2 + 3*5^3 + 3*5^6 + 5^7 + O(5^9)

        Check that it is a quadratic function::

            sage: h(3*P)-3^2*h(P)
            O(5^9)
        """
    def padic_regulator(self, prec: int = 20):
        """
        Compute the canonical `p`-adic regulator on the extended
        Mordell-Weil group as in [MTT1986]_
        (with the correction of [Wer1998]_ and sign convention in [SW2013]_.)

        The `p`-adic Birch and Swinnerton-Dyer conjecture predicts
        that this value appears in the formula for the leading term of
        the `p`-adic `L`-function.

        INPUT:

        - ``prec`` -- the `p`-adic precision (default: 20)

        EXAMPLES::

            sage: eq = EllipticCurve('130a1').tate_curve(5)
            sage: eq.padic_regulator()
            2*5^-1 + 1 + 2*5 + 2*5^2 + 3*5^3 + 3*5^6 + 5^7 + 3*5^9 + 3*5^10 + 3*5^12 + 4*5^13 + 3*5^15 + 2*5^16 + 3*5^18 + 4*5^19 +  4*5^20 + 3*5^21 + 4*5^22 + O(5^23)
        """
