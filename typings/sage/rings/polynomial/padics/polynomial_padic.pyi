from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.structure.factorization import Factorization as Factorization

class Polynomial_padic(Polynomial):
    def __init__(self, parent, x=None, check: bool = True, is_gen: bool = False, construct: bool = False) -> None: ...
    def content(self):
        """
        Compute the content of this polynomial.

        OUTPUT:

        If this is the zero polynomial, return the constant coefficient.
        Otherwise, since the content is only defined up to a unit, return the
        content as `\\pi^k` with maximal precision where `k` is the minimal
        valuation of any of the coefficients.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: K = Zp(13,7)
            sage: R.<t> = K[]
            sage: f = 13^7*t^3 + K(169,4)*t - 13^4
            sage: f.content()
            13^2 + O(13^9)
            sage: R(0).content()
            0
            sage: f = R(K(0,3)); f
            O(13^3)
            sage: f.content()
            O(13^3)

            sage: # needs sage.libs.ntl
            sage: P.<x> = ZZ[]
            sage: f = x + 2
            sage: f.content()
            1
            sage: fp = f.change_ring(pAdicRing(2, 10))
            sage: fp
            (1 + O(2^10))*x + 2 + O(2^11)
            sage: fp.content()
            1 + O(2^10)
            sage: (2*fp).content()
            2 + O(2^11)

        Over a field it would be sufficient to return only zero or one, as the
        content is only defined up to multiplication with a unit. However, we
        return `\\pi^k` where `k` is the minimal valuation of any coefficient::

            sage: # needs sage.libs.ntl
            sage: K = Qp(13,7)
            sage: R.<t> = K[]
            sage: f = 13^7*t^3 + K(169,4)*t - 13^-4
            sage: f.content()
            13^-4 + O(13^3)
            sage: f = R.zero()
            sage: f.content()
            0
            sage: f = R(K(0,3))
            sage: f.content()
            O(13^3)
            sage: f = 13*t^3 + K(0,1)*t
            sage: f.content()
            13 + O(13^8)
        """
    def factor(self):
        '''
        Return the factorization of this polynomial.

        EXAMPLES::

            sage: # needs sage.libs.ntl
            sage: R.<t> = PolynomialRing(Qp(3, 3, print_mode=\'terse\', print_pos=False))
            sage: pol = t^8 - 1
            sage: for p,e in pol.factor():
            ....:     print("{} {}".format(e, p))
            1 (1 + O(3^3))*t + 1 + O(3^3)
            1 (1 + O(3^3))*t - 1 + O(3^3)
            1 (1 + O(3^3))*t^2 + (5 + O(3^3))*t - 1 + O(3^3)
            1 (1 + O(3^3))*t^2 + (-5 + O(3^3))*t - 1 + O(3^3)
            1 (1 + O(3^3))*t^2 + O(3^3)*t + 1 + O(3^3)
            sage: R.<t> = PolynomialRing(Qp(5, 6, print_mode=\'terse\', print_pos=False))
            sage: pol = 100 * (5*t - 1) * (t - 5); pol
            (500 + O(5^9))*t^2 + (-2600 + O(5^8))*t + 500 + O(5^9)
            sage: pol.factor()
            (500 + O(5^9)) * ((1 + O(5^5))*t - 1/5 + O(5^5)) * ((1 + O(5^6))*t - 5 + O(5^6))
            sage: pol.factor().value()
            (500 + O(5^8))*t^2 + (-2600 + O(5^8))*t + 500 + O(5^8)

        The same factorization over `\\ZZ_p`. In this case, the "unit"
        part is a `p`-adic unit and the power of `p` is considered to be
        a factor::

            sage: # needs sage.libs.ntl
            sage: R.<t> = PolynomialRing(Zp(5, 6, print_mode=\'terse\', print_pos=False))
            sage: pol = 100 * (5*t - 1) * (t - 5); pol
            (500 + O(5^9))*t^2 + (-2600 + O(5^8))*t + 500 + O(5^9)
            sage: pol.factor()
            (4 + O(5^6)) * (5 + O(5^7))^2 * ((1 + O(5^6))*t - 5 + O(5^6)) * ((5 + O(5^6))*t - 1 + O(5^6))
            sage: pol.factor().value()
            (500 + O(5^8))*t^2 + (-2600 + O(5^8))*t + 500 + O(5^8)

        In the following example, the discriminant is zero, so the `p`-adic
        factorization is not well defined::

            sage: factor(t^2)                                                           # needs sage.libs.ntl
            Traceback (most recent call last):
            ...
            PrecisionError: p-adic factorization not well-defined since
            the discriminant is zero up to the requestion p-adic precision

        An example of factoring a constant polynomial (see :issue:`26669`)::

            sage: R.<x> = Qp(5)[]                                                       # needs sage.libs.ntl
            sage: R(2).factor()                                                         # needs sage.libs.ntl
            2 + O(5^20)

        More examples over `\\ZZ_p`::

            sage: R.<w> = PolynomialRing(Zp(5, prec=6, type=\'capped-abs\', print_mode=\'val-unit\'))
            sage: f = w^5 - 1
            sage: f.factor()                                                            # needs sage.libs.ntl
            ((1 + O(5^6))*w + 3124 + O(5^6))
            * ((1 + O(5^6))*w^4 + (12501 + O(5^6))*w^3 + (9376 + O(5^6))*w^2
                 + (6251 + O(5^6))*w + 3126 + O(5^6))

        See :issue:`4038`::

            sage: # needs sage.libs.ntl sage.schemes
            sage: E = EllipticCurve(\'37a1\')
            sage: K = Qp(7,10)
            sage: EK = E.base_extend(K)
            sage: g = EK.division_polynomial_0(3)
            sage: g.factor()
            (3 + O(7^10))
            * ((1 + O(7^10))*x
                 + 1 + 2*7 + 4*7^2 + 2*7^3 + 5*7^4 + 7^5 + 5*7^6 + 3*7^7 + 5*7^8 + 3*7^9 + O(7^10))
            * ((1 + O(7^10))*x^3
                 + (6 + 4*7 + 2*7^2 + 4*7^3 + 7^4 + 5*7^5
                      + 7^6 + 3*7^7 + 7^8 + 3*7^9 + O(7^10))*x^2
                 + (6 + 3*7 + 5*7^2 + 2*7^4 + 7^5 + 7^6 + 2*7^8 + 3*7^9 + O(7^10))*x
                 + 2 + 5*7 + 4*7^2 + 2*7^3 + 6*7^4 + 3*7^5 + 7^6 + 4*7^7 + O(7^10))

        TESTS:

        Check that :issue:`13293` is fixed::

            sage: R.<T> = Qp(3)[]                                                       # needs sage.libs.ntl
            sage: f = 1926*T^2 + 312*T + 387                                            # needs sage.libs.ntl
            sage: f.factor()                                                            # needs sage.libs.ntl
            (3^2 + 2*3^3 + 2*3^4 + 3^5 + 2*3^6 + O(3^22)) * ((1 + O(3^19))*T + 2*3^-1 + 3 + 3^2 + 2*3^5 + 2*3^6 + 2*3^7 + 3^8 + 3^9 + 2*3^11 + 3^15 + 3^17 + O(3^19)) * ((1 + O(3^20))*T + 2*3 + 3^2 + 3^3 + 3^5 + 2*3^6 + 2*3^7 + 3^8 + 3^10 + 3^11 + 2*3^12 + 2*3^14 + 2*3^15 + 2*3^17 + 2*3^18 + O(3^20))

        Check that :issue:`24065` is fixed::

            sage: R = Zp(2, type=\'fixed-mod\', prec=3)
            sage: P.<x> = R[]
            sage: ((1 + 2)*x + (1 + 2)*x^2).factor()
            (1 + 2) * (x + 1) * x
        '''
    def root_field(self, names, check_irreducible: bool = True, **kwds):
        """
        Return the `p`-adic extension field generated by the roots of the irreducible
        polynomial ``self``.

        INPUT:

        - ``names`` -- name of the generator of the extension

        - ``check_irreducible`` -- check whether the polynomial is irreducible

        - ``kwds`` -- see :meth:`sage.rings.padics.padic_generic.pAdicGeneric.extension`

        EXAMPLES::

            sage: R.<x> = Qp(3,5,print_mode='digits')[]                                 # needs sage.libs.ntl
            sage: f = x^2 - 3                                                           # needs sage.libs.ntl
            sage: f.root_field('x')                                                     # needs sage.libs.ntl
            3-adic Eisenstein Extension Field in x defined by x^2 - 3

        ::

            sage: R.<x> = Qp(5,5,print_mode='digits')[]                                 # needs sage.libs.ntl
            sage: f = x^2 - 3                                                           # needs sage.libs.ntl
            sage: f.root_field('x', print_mode='bars')                                  # needs sage.libs.ntl
            5-adic Unramified Extension Field in x defined by x^2 - 3

        ::

            sage: R.<x> = Qp(11,5,print_mode='digits')[]                                # needs sage.libs.ntl
            sage: f = x^2 - 3                                                           # needs sage.libs.ntl
            sage: f.root_field('x', print_mode='bars')                                  # needs sage.libs.ntl
            Traceback (most recent call last):
            ...
            ValueError: polynomial must be irreducible
        """
