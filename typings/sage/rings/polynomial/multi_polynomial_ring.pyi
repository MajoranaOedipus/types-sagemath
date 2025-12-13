from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base as MPolynomialRing_base, is_MPolynomialRing as is_MPolynomialRing
from sage.rings.polynomial.polydict import ETuple as ETuple, PolyDict as PolyDict
from sage.rings.polynomial.polynomial_singular_interface import PolynomialRing_singular_repr as PolynomialRing_singular_repr
from sage.rings.polynomial.term_order import TermOrder as TermOrder
from sage.structure.element import Element as Element

class MPolynomialRing_macaulay2_repr:
    """
    A mixin class for polynomial rings that support conversion to Macaulay2.
    """

class MPolynomialRing_polydict(MPolynomialRing_macaulay2_repr, PolynomialRing_singular_repr, MPolynomialRing_base):
    """
    Multivariable polynomial ring.

    EXAMPLES::

        sage: R = PolynomialRing(Integers(12), 'x', 5); R
        Multivariate Polynomial Ring in x0, x1, x2, x3, x4 over Ring of integers modulo 12
        sage: loads(R.dumps()) == R
        True
    """
    def __init__(self, base_ring, n, names, order) -> None: ...
    def __eq__(self, other):
        """
        Check whether ``self`` is equal to ``other``.

        EXAMPLES::

            sage: R = PolynomialRing(Integers(10), 'x', 4)
            sage: loads(R.dumps()) == R
            True
        """
    def __ne__(self, other):
        """
        Check whether ``self`` is not equal to ``other``.

        EXAMPLES::

            sage: R = PolynomialRing(Integers(8), 'x', 3)
            sage: loads(R.dumps()) != R
            False
        """
    def __hash__(self):
        """
        Compute the hash of ``self``.

        EXAMPLES::

            sage: h = hash(PolynomialRing(Integers(8), 'x', 3))
        """
    def monomial_quotient(self, f, g, coeff: bool = False):
        """
        Return ``f/g``, where both ``f`` and ``g`` are treated as monomials.

        Coefficients are ignored by default.

        INPUT:

        - ``f`` -- monomial

        - ``g`` -- monomial

        - ``coeff`` -- divide coefficients as well (default: ``False``)

        OUTPUT: monomial

        EXAMPLES::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
            sage: P.<x,y,z> = MPolynomialRing_polydict_domain(QQ, 3, order='degrevlex')
            sage: P.monomial_quotient(3/2*x*y, x)
            y

        ::

            sage: P.monomial_quotient(3/2*x*y, 2*x, coeff=True)
            3/4*y

        TESTS::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
            sage: R.<x,y,z> = MPolynomialRing_polydict_domain(QQ,3, order='degrevlex')
            sage: P.<x,y,z> = MPolynomialRing_polydict_domain(QQ,3, order='degrevlex')
            sage: P.monomial_quotient(x*y, x)
            y

        ::

            sage: P.monomial_quotient(x*y, R.gen())
            y

        ::

            sage: P.monomial_quotient(P(0), P(1))
            0

        ::

            sage: P.monomial_quotient(P(1), P(0))
            Traceback (most recent call last):
            ...
            ZeroDivisionError

        ::

            sage: P.monomial_quotient(P(3/2), P(2/3), coeff=True)
            9/4

        ::

            sage: P.monomial_quotient(x, y) # Note the wrong result
            x*y^-1

        ::

            sage: P.monomial_quotient(x, P(1))
            x

        .. NOTE::

            Assumes that the head term of f is a multiple of the head
            term of g and return the multiplicant m. If this rule is
            violated, funny things may happen.
        """
    def monomial_lcm(self, f, g):
        """
        LCM for monomials. Coefficients are ignored.

        INPUT:

        - ``f`` -- monomial

        - ``g`` -- monomial

        OUTPUT: monomial

        EXAMPLES::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
            sage: P.<x,y,z> = MPolynomialRing_polydict_domain(QQ,3, order='degrevlex')
            sage: P.monomial_lcm(3/2*x*y, x)
            x*y

        TESTS::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
            sage: R.<x,y,z> = MPolynomialRing_polydict_domain(QQ,3, order='degrevlex')
            sage: P.<x,y,z> = MPolynomialRing_polydict_domain(QQ,3, order='degrevlex')
            sage: P.monomial_lcm(x*y, R.gen())
            x*y

        ::

            sage: P.monomial_lcm(P(3/2), P(2/3))
            1

        ::

            sage: P.monomial_lcm(x, P(1))
            x
        """
    def monomial_reduce(self, f, G):
        """
        Try to find a ``g`` in ``G`` where ``g.lm()`` divides ``f``.

        If found, ``(flt,g)`` is returned, ``(0,0)`` otherwise, where
        ``flt`` is ``f/g.lm()``. It is assumed that ``G`` is iterable and contains
        ONLY elements in this ring.

        INPUT:

        - ``f`` -- monomial

        - ``G`` -- list/set of mpolynomials

        EXAMPLES::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
            sage: P.<x,y,z>=MPolynomialRing_polydict_domain(QQ,3, order='degrevlex')
            sage: f = x*y^2
            sage: G = [3/2*x^3 + y^2 + 1/2, 1/4*x*y + 2/7, P(1/2)]
            sage: P.monomial_reduce(f,G)
            (y, 1/4*x*y + 2/7)

        ::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
            sage: P.<x,y,z> = MPolynomialRing_polydict_domain(Zmod(23432),3, order='degrevlex')
            sage: f = x*y^2
            sage: G = [3*x^3 + y^2 + 2, 4*x*y + 7, P(2)]
            sage: P.monomial_reduce(f,G)
            (y, 4*x*y + 7)

        TESTS::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
            sage: P.<x,y,z>=MPolynomialRing_polydict_domain(QQ,3, order='degrevlex')
            sage: f = x*y^2
            sage: G = [3/2*x^3 + y^2 + 1/2, 1/4*x*y + 2/7, P(1/2)]

        ::

            sage: P.monomial_reduce(P(0),G)
            (0, 0)

        ::

            sage: P.monomial_reduce(f,[P(0)])
            (0, 0)
        """
    def monomial_divides(self, a, b):
        """
        Return ``False`` if ``a`` does not divide ``b`` and ``True`` otherwise.

        INPUT:

        - ``a`` -- monomial

        - ``b`` -- monomial

        OUTPUT: boolean

        EXAMPLES::

            sage: P.<x,y,z> = PolynomialRing(ZZ,3, order='degrevlex')
            sage: P.monomial_divides(x*y*z, x^3*y^2*z^4)
            True
            sage: P.monomial_divides(x^3*y^2*z^4, x*y*z)
            False

        TESTS::

            sage: P.<x,y,z> = PolynomialRing(ZZ,3, order='degrevlex')
            sage: P.monomial_divides(P(1), P(0))
            True
            sage: P.monomial_divides(P(1), x)
            True
        """
    def monomial_pairwise_prime(self, h, g):
        """
        Return ``True`` if ``h`` and ``g`` are pairwise prime.

        Both are treated as monomials.

        INPUT:

        - ``h`` -- monomial

        - ``g`` -- monomial

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
            sage: P.<x,y,z> = MPolynomialRing_polydict_domain(QQ,3, order='degrevlex')
            sage: P.monomial_pairwise_prime(x^2*z^3, y^4)
            True

        ::

            sage: P.monomial_pairwise_prime(1/2*x^3*y^2, 3/4*y^3)
            False

        TESTS::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
            sage: P.<x,y,z> = MPolynomialRing_polydict_domain(QQ,3, order='degrevlex')
            sage: Q.<x,y,z> = MPolynomialRing_polydict_domain(QQ,3, order='degrevlex')
            sage: P.monomial_pairwise_prime(x^2*z^3, Q('y^4'))
            True

        ::

            sage: P.monomial_pairwise_prime(1/2*x^3*y^2, Q(0))
            True

        ::

            sage: P.monomial_pairwise_prime(P(1/2),x)
            False
        """
    def monomial_all_divisors(self, t):
        """
        Return a list of all monomials that divide ``t``, coefficients are
        ignored.

        INPUT:

        - ``t`` -- a monomial

        OUTPUT: list of monomials

        EXAMPLES::

            sage: from sage.rings.polynomial.multi_polynomial_ring import MPolynomialRing_polydict_domain
            sage: P.<x,y,z> = MPolynomialRing_polydict_domain(QQ,3, order='degrevlex')
            sage: P.monomial_all_divisors(x^2*z^3)
            [x, x^2, z, x*z, x^2*z, z^2, x*z^2, x^2*z^2, z^3, x*z^3, x^2*z^3]

        ALGORITHM: addwithcarry idea by Toon Segers
        """
    def sum(self, terms):
        """
        Return a sum of elements of this multipolynomial ring.

        This is method is much faster than the Python builtin :func:`sum`.

        EXAMPLES::

            sage: R = QQ['x']
            sage: S = R['y, z']
            sage: x = R.gen()
            sage: y, z = S.gens()
            sage: S.sum([x*y, 2*x^2*z - 2*x*y, 1 + y + z])
            (-x + 1)*y + (2*x^2 + 1)*z + 1

        Comparison with builtin :func:`sum`::

            sage: sum([x*y, 2*x^2*z - 2*x*y, 1 + y + z])
            (-x + 1)*y + (2*x^2 + 1)*z + 1
        """

class MPolynomialRing_polydict_domain(MPolynomialRing_polydict):
    def __init__(self, base_ring, n, names, order) -> None: ...
    def is_field(self, proof: bool = True): ...
