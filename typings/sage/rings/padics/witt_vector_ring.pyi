from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.fields import Fields as Fields
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.misc.latex import latex as latex
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.padics.factory import Zp as Zp
from sage.rings.padics.witt_vector import WittVector_finotti as WittVector_finotti, WittVector_phantom as WittVector_phantom, WittVector_pinvertible as WittVector_pinvertible, WittVector_standard as WittVector_standard
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing_base
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.sets.primes import Primes as Primes
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation
from typing import Iterator

def fast_char_p_power(x, n, p=None):
    """
    Return `x^n` assuming that `x` lives in a ring of characteristic `p`.

    If `x` is not an element of a ring of characteristic `p`,
    this throws an error.

    EXAMPLES::

        sage: from sage.rings.padics.witt_vector_ring import fast_char_p_power
        sage: t = GF(1913)(33)
        sage: fast_char_p_power(t, 77)
        1371

    ::

        sage: K.<t> = GF(5^3)
        sage: fast_char_p_power(t, 385)
        4*t^2 + 1
        sage: t^385
        4*t^2 + 1

    ::

        sage: A.<x> = K[]
        sage: fast_char_p_power(x + 1, 10)
        x^10 + 2*x^5 + 1

    ::

        sage: B.<u,v> = K[]
        sage: fast_char_p_power(u + v, 1250)
        u^1250 + 2*u^625*v^625 + v^1250
    """

class WittVectorRing(Parent, UniqueRepresentation):
    """
    Return the appropriate `p`-typical truncated Witt vector ring.

    INPUT:

    - ``coefficient_ring`` -- commutative ring of coefficients

    - ``prec`` -- integer (default: `1`), length of the truncated Witt
      vectors in the ring

    - ``p`` -- a prime number (default: ``None``); when it is not set, it
      defaults to the characteristic of ``coefficient_ring`` when it is prime.

    - ``algorithm`` -- the name of the algorithm to use for the ring laws
      (default: ``None``); when it is not set, the most adequate algorithm
      is chosen

    Available algorithms are:

    - ``standard`` -- the schoolbook algorithm;

    - ``finotti`` -- Finotti's algorithm; it can be used when the coefficient
      ring has characteristic `p`;

    - ``phantom`` -- computes the ring laws using the phantom components
      using a lift of ``coefficient_ring``, assuming that it is either
      `\\mathbb F_q` for a power `q` of `p`, or a polynomial ring on that field;

    - ``p_invertible`` -- uses some optimisations when `p` is invertible
      in the coefficient ring.

    EXAMPLES::

        sage: WittVectorRing(QQ, p=5)
        Ring of truncated 5-typical Witt vectors of length 1 over
        Rational Field

    ::

        sage: WittVectorRing(GF(3))
        Ring of truncated 3-typical Witt vectors of length 1 over
        Finite Field of size 3

    ::

        sage: WittVectorRing(GF(3)['t'])
        Ring of truncated 3-typical Witt vectors of length 1 over
        Univariate Polynomial Ring in t over Finite Field of size 3

    ::

        sage: WittVectorRing(Qp(7), prec=30, p=5)
        Ring of truncated 5-typical Witt vectors of length 30 over
        7-adic Field with capped relative precision 20

    TESTS::

        sage: A = SymmetricGroup(3).algebra(QQ)
        sage: WittVectorRing(A)
        Traceback (most recent call last):
        ...
        TypeError: Symmetric group algebra of order 3 over Rational Field is not a commutative ring

        sage: WittVectorRing(QQ)
        Traceback (most recent call last):
        ...
        ValueError: Rational Field has non-prime characteristic and no prime was supplied

        sage: WittVectorRing(QQ, p=5, algorithm='moon')
        Traceback (most recent call last):
        ...
        ValueError: algorithm must be one of None, 'standard', 'p_invertible', 'finotti', 'phantom'

        sage: W = WittVectorRing(ZZ, p=53)
        sage: type(W)
        <class 'sage.rings.padics.witt_vector_ring.WittVectorRing_standard_with_category'>

        sage: W = WittVectorRing(PolynomialRing(GF(13), 't'))
        sage: type(W)
        <class 'sage.rings.padics.witt_vector_ring.WittVectorRing_phantom_with_category'>

        sage: W = WittVectorRing(PolynomialRing(GF(5), 't,u'))
        sage: type(W)
        <class 'sage.rings.padics.witt_vector_ring.WittVectorRing_finotti_with_category'>
    """
    def __classcall_private__(cls, coefficient_ring, prec: int = 1, p=None, algorithm=None):
        """
        Construct the ring of truncated Witt vectors from the parameters.

        TESTS::

            sage: W = WittVectorRing(QQ, p=5)
            sage: W
            Ring of truncated 5-typical Witt vectors of length 1 over Rational Field
        """
    def __init__(self, coefficient_ring, prec, prime) -> None:
        """
        Initialise ``self``.

        EXAMPLES::

            sage: W = WittVectorRing(PolynomialRing(GF(5), 't'), prec=4); W
            Ring of truncated 5-typical Witt vectors of length 4 over Univariate Polynomial Ring in t over Finite Field of size 5
            sage: type(W)
            <class 'sage.rings.padics.witt_vector_ring.WittVectorRing_phantom_with_category'>

            sage: TestSuite(W).run()
        """
    def __iter__(self) -> Iterator:
        """
        Iterator for truncated Witt vector rings.

        EXAMPLES::

            sage: W = WittVectorRing(GF(3), p=3, prec=2)
            sage: [w for w in W]
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1),
            (2, 2)]
        """
    def cardinality(self):
        """
        Return the cardinality of ``self``.

        EXAMPLES::

            sage: WittVectorRing(GF(17), prec=2).cardinality()
            289
            sage: WittVectorRing(QQ, p=2).cardinality()
            +Infinity
        """
    def characteristic(self):
        """
        Return the characteristic of ``self``.

        EXAMPLES::

            sage: WittVectorRing(GF(25), p=5, prec=3).characteristic()
            125
            sage: WittVectorRing(ZZ, p=2, prec=4).characteristic()
            0
            sage: WittVectorRing(Integers(18), p=3, prec=3).characteristic()
            162
        """
    def coefficient_ring(self):
        """
        Return the coefficient ring of ``self``.

        EXAMPLES::

            sage: W = WittVectorRing(Zp(5), p=5)
            sage: W.coefficient_ring()
            5-adic Ring with capped relative precision 20
        """
    def is_finite(self) -> bool:
        """
        Return whether ``self`` is a finite ring.

        EXAMPLES::

            sage: WittVectorRing(GF(23)).is_finite()
            True
            sage: WittVectorRing(ZZ, p=2).is_finite()
            False
        """
    def precision(self):
        """
        Return the length of the truncated Witt vectors in ``length``.

        EXAMPLES::

            sage: WittVectorRing(GF(9), p=3, prec=3).precision()
            3
        """
    def prime(self):
        """
        Return the prime from which the truncated Witt vector ring has been
        constructed.

        EXAMPLES::

            sage: W = WittVectorRing(GF(81), prec=3)
            sage: W.prime()
            3

            sage: W = WittVectorRing(ZZ, p=7, prec=2)
            sage: W.prime()
            7
        """
    def prod_polynomials(self, variables=None):
        """
        Return the Witt product polynomials.

        INPUT:

        - ``variables`` -- names of the indeterminates (default: ``None``),
          given as a string, or as a list of strings, whose length must be the
          double of the precision of the ring. When nothing is given,
          variables indexed by `X` and `Y` are used.

        EXAMPLES::

            sage: W = WittVectorRing(GF(5), prec=3)
            sage: W.prod_polynomials()
            [X0*Y0,
            X1*Y0^5 + X0^5*Y1,
            -X0^5*X1^4*Y0^20*Y1 - 2*X0^10*X1^3*Y0^15*Y1^2 - 2*X0^15*X1^2*Y0^10*Y1^3 - X0^20*X1*Y0^5*Y1^4 + X2*Y0^25 + X0^25*Y2 + X1^5*Y1^5]

            sage: W = WittVectorRing(ZZ, p=2, prec=2)
            sage: W.prod_polynomials('T0, T1, U0, U1')
            [T0*U0, T1*U0^2 + T0^2*U1 + 2*T1*U1]
        """
    def random_element(self, *args, **kwds):
        """
        Return a random truncated Witt vector.

        Extra arguments are passed to
        the random generator of the coefficient ring.

        EXAMPLES::

            sage: WittVectorRing(GF(27,'t'), prec=2).random_element()  # random
            (z3, 2*z3^2 + 1)

            sage: W = WittVectorRing(PolynomialRing(ZZ,'x'), p=3, prec=3)
            sage: W.random_element(5)  # random
            (x^5 - 2*x^4 - 4*x^3 - 2*x^2 + 1, -x^5 + 2*x^4 - x - 1,
            -x^5 + 7*x^4 + 3*x^3 - 24*x^2 - 1)
        """
    def sum_polynomials(self, variables=None):
        """
        Return the Witt sum polynomials.

        INPUT:

        - ``variables`` -- names of the indeterminates (default: ``None``),
          given as a string, or as a list of strings, whose length must be the
          double of the precision of the ring. When nothing is given,
          variables indexed by `X` and `Y` are used.

        EXAMPLES::

            sage: W = WittVectorRing(GF(5), prec=2)
            sage: W.sum_polynomials(['T0', 'T1', 'U0', 'U1'])
            [T0 + U0, -T0^4*U0 - 2*T0^3*U0^2 - 2*T0^2*U0^3 - T0*U0^4 + T1 + U1]

            sage: W = WittVectorRing(ZZ, p=2, prec=3)
            sage: W.sum_polynomials()
            [X0 + Y0,
            -X0*Y0 + X1 + Y1,
            -X0^3*Y0 - 2*X0^2*Y0^2 - X0*Y0^3 + X0*X1*Y0 + X0*Y0*Y1 - X1*Y1 + X2 + Y2]
        """
    def teichmuller_lift(self, x):
        """
        Return the Teichmüller lift of ``x`` in ``self``.

        This lift is sometimes known as the multiplicative lift of ``x``.

        EXAMPLES::

            sage: WittVectorRing(GF(125,'t'), prec=2).teichmuller_lift(3)
            (3, 0)
        """

class WittVectorRing_finotti(WittVectorRing):
    """
    Child class for truncated Witt vectors using Finotti's algorithm.

    .. WARNING::

        This class should never be called directly, use ``WittVectorRing``
        instead.

    EXAMPLES::

        sage: W = WittVectorRing(GF(49), prec=3, algorithm='finotti')
        sage: W
        Ring of truncated 7-typical Witt vectors of length 3 over Finite Field in z2 of size 7^2

        sage: W = WittVectorRing(ZZ, p=11, prec=3, algorithm='finotti')
        Traceback (most recent call last):
        ...
        ValueError: the 'finotti' algorithm only works for coefficients rings of characteristic p
    """
    Element = WittVector_finotti
    def __init__(self, coefficient_ring, prec, prime) -> None:
        """
        Initialise ``self``.

        EXAMPLES::

            sage: W = WittVectorRing(PowerSeriesRing(GF(3), 't'), p=3, prec=3)
            sage: W
            Ring of truncated 3-typical Witt vectors of length 3 over Power Series Ring in t over Finite Field of size 3
            sage: type(W)
            <class 'sage.rings.padics.witt_vector_ring.WittVectorRing_finotti_with_category'>

            sage: TestSuite(W).run()
        """

class WittVectorRing_phantom(WittVectorRing):
    """
    Child class for truncated Witt vectors using the ``phantom`` algorithm.

    .. WARNING::

        This class should never be called directly, use ``WittVectorRing``
        instead.

    EXAMPLES::

        sage: W = WittVectorRing(GF(19), prec=20)
        sage: W
        Ring of truncated 19-typical Witt vectors of length 20 over Finite Field of size 19

        sage: W = WittVectorRing(QQ, p=23, prec=3, algorithm='phantom')
        Traceback (most recent call last):
        ...
        ValueError: the 'phantom' algorithm only works when the coefficient ring is a finite field of char. p, or a polynomial ring on that field
    """
    Element = WittVector_phantom
    def __init__(self, coefficient_ring, prec, prime) -> None:
        """
        Initialise ``self``.

        EXAMPLES::

            sage: W = WittVectorRing(GF(23,'t'), p=23, prec=2)
            sage: W
            Ring of truncated 23-typical Witt vectors of length 2 over Finite Field of size 23
            sage: type(W)
            <class 'sage.rings.padics.witt_vector_ring.WittVectorRing_phantom_with_category'>

            sage: TestSuite(W).run()
        """

class WittVectorRing_pinvertible(WittVectorRing):
    """
    Child class for truncated Witt vectors using the ``p_invertible`` algorithm.

    .. WARNING::

        This class should never be called directly, use ``WittVectorRing``
        instead.

    EXAMPLES::

        sage: W = WittVectorRing(QQ, p=31, prec=20)
        sage: W
        Ring of truncated 31-typical Witt vectors of length 20 over Rational Field

        sage: W = WittVectorRing(GF(3), prec=3, algorithm='p_invertible')
        Traceback (most recent call last):
        ...
        ValueError: the 'p_invertible' algorithm only works when p is a unit in the ring of coefficients
    """
    Element = WittVector_pinvertible
    def __init__(self, coefficient_ring, prec, prime) -> None:
        """
        Initialise ``self``.

        EXAMPLES::

            sage: W = WittVectorRing(QQ, p=11, prec=3)
            sage: W
            Ring of truncated 11-typical Witt vectors of length 3 over Rational Field
            sage: type(W)
            <class 'sage.rings.padics.witt_vector_ring.WittVectorRing_pinvertible_with_category'>

            sage: TestSuite(W).run()
        """

class WittVectorRing_standard(WittVectorRing):
    """
    Child class for truncated Witt vectors using the ``standard`` algorithm.

    .. WARNING::

        This class should never be called directly, use ``WittVectorRing``
        instead.

    EXAMPLES::

        sage: W = WittVectorRing(GF(3), prec=3, algorithm='standard')
        sage: W
        Ring of truncated 3-typical Witt vectors of length 3 over Finite Field of size 3
    """
    Element = WittVector_standard
    def __init__(self, coefficient_ring, prec, prime) -> None:
        """
        Initialise ``self``.

        EXAMPLES::

            sage: W = WittVectorRing(ZZ, p=5, prec=2)
            sage: W
            Ring of truncated 5-typical Witt vectors of length 2 over Integer Ring
            sage: type(W)
            <class 'sage.rings.padics.witt_vector_ring.WittVectorRing_standard_with_category'>

            sage: TestSuite(W).run()
        """
