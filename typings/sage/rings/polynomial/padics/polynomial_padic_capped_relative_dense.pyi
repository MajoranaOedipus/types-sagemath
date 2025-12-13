import sage.rings.padics.misc as misc
import sage.rings.padics.precision_error as precision_error
import sage.rings.polynomial.polynomial_element_generic
from _typeshed import Incomplete
from sage.libs.pari import pari as pari
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.fraction_field_element import FractionFieldElement as FractionFieldElement
from sage.rings.infinity import infinity as infinity
from sage.rings.polynomial.padics.polynomial_padic import Polynomial_padic as Polynomial_padic
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial

min = misc.min
ZZ: Incomplete
PrecisionError = precision_error.PrecisionError
Integer: Incomplete
Polynomial_integer_dense: Incomplete
Polynomial_generic_cdv = sage.rings.polynomial.polynomial_element_generic.Polynomial_generic_cdv

class Polynomial_padic_capped_relative_dense(Polynomial_generic_cdv, Polynomial_padic):
    def __init__(self, parent, x=None, check: bool = True, is_gen: bool = False, construct: bool = False, absprec=..., relprec=...) -> None:
        """
        TESTS::

            sage: K = Qp(13,7)
            sage: R.<t> = K[]
            sage: R([K(13), K(1)])
            (1 + O(13^7))*t + 13 + O(13^8)
            sage: T.<t> = ZZ[]
            sage: R(t + 2)
            (1 + O(13^7))*t + 2 + O(13^7)

        Check that :issue:`13620` has been fixed::

            sage: f = R.zero()
            sage: R(f.monomial_coefficients())
            0

        Check that :issue:`29829` has been fixed::

            sage: R.<x> = PolynomialRing(ZZ)
            sage: f = x + 5
            sage: S.<y> = PolynomialRing(Qp(5))
            sage: g2 = S(f)
            sage: 25*g2
            (5^2 + O(5^22))*y + 5^3 + O(5^23)
        """
    def __reduce__(self):
        """
        For pickling.  This function is here because the relative precisions were getting screwed up for some reason.
        """
    def list(self, copy: bool = True):
        """
        Return a list of coefficients of ``self``.

        .. NOTE::

            The length of the list returned may be greater
            than expected since it includes any leading zeros
            that have finite absolute precision.

        EXAMPLES::

            sage: K = Qp(13,7)
            sage: R.<t> = K[]
            sage: a = 2*t^3 + 169*t - 1
            sage: a
            (2 + O(13^7))*t^3 + (13^2 + O(13^9))*t + 12 + 12*13 + 12*13^2 + 12*13^3 + 12*13^4 + 12*13^5 + 12*13^6 + O(13^7)
            sage: a.list()
            [12 + 12*13 + 12*13^2 + 12*13^3 + 12*13^4 + 12*13^5 + 12*13^6 + O(13^7),
             13^2 + O(13^9),
             0,
             2 + O(13^7)]
        """
    def lift(self):
        """
        Return an integer polynomial congruent to this one modulo the
        precision of each coefficient.

        .. NOTE::

            The lift that is returned will not necessarily be the same
            for polynomials with the same coefficients (i.e. same values
            and precisions): it will depend on how the polynomials are
            created.

        EXAMPLES::

            sage: K = Qp(13,7)
            sage: R.<t> = K[]
            sage: a = 13^7*t^3 + K(169,4)*t - 13^4
            sage: a.lift()
            62748517*t^3 + 169*t - 28561
        """
    def __getitem__(self, n):
        """
        Return the `n`-th coefficient of ``self``.

        This returns the coefficient of `x^n` if `n` is an integer,
        and returns the monomials of ``self`` of degree
        in slice `n` if `n` is a slice ``[:k]``.

        EXAMPLES::

            sage: K = Qp(13,7)
            sage: R.<t> = K[]
            sage: a = 13^7*t^3 + K(169,4)*t - 13^4
            sage: a[1]
            13^2 + O(13^4)

        Slices can be used to truncate polynomials::

            sage: a[:2]
            (13^2 + O(13^4))*t + 12*13^4 + 12*13^5 + 12*13^6 + 12*13^7 + 12*13^8 + 12*13^9 + 12*13^10 + O(13^11)

        Any other kind of slicing is an error, see :issue:`18940`::

            sage: a[1:3]
            Traceback (most recent call last):
            ...
            IndexError: polynomial slicing with a start is not defined

            sage: a[1:3:2]
            Traceback (most recent call last):
            ...
            IndexError: polynomial slicing with a step is not defined
        """
    def lshift_coeffs(self, shift, no_list: bool = False):
        """
        Return a new polynomials whose coefficients are multiplied by p^shift.

        EXAMPLES::

            sage: K = Qp(13, 4)
            sage: R.<t> = K[]
            sage: a = t + 52
            sage: a.lshift_coeffs(3)
            (13^3 + O(13^7))*t + 4*13^4 + O(13^8)
        """
    def rshift_coeffs(self, shift, no_list: bool = False):
        """
        Return a new polynomial whose coefficients are `p`-adically
        shifted to the right by ``shift``.

        .. NOTE::

            Type ``Qp(5)(0).__rshift__?`` for more information.

        EXAMPLES::

            sage: K = Zp(13, 4)
            sage: R.<t> = K[]
            sage: a = t^2 + K(13,3)*t + 169; a
            (1 + O(13^4))*t^2 + (13 + O(13^3))*t + 13^2 + O(13^6)
            sage: b = a.rshift_coeffs(1); b
            O(13^3)*t^2 + (1 + O(13^2))*t + 13 + O(13^5)
            sage: b.list()
            [13 + O(13^5), 1 + O(13^2), O(13^3)]
            sage: b = a.rshift_coeffs(2); b
            O(13^2)*t^2 + O(13)*t + 1 + O(13^4)
            sage: b.list()
            [1 + O(13^4), O(13), O(13^2)]
        """
    def __pari__(self, variable=None):
        """
        Return ``self`` as a PARI object.
        """
    def __copy__(self):
        """
        Return a copy of ``self``.
        """
    def degree(self, secure: bool = False):
        """
        Return the degree of ``self``.

        INPUT:

        - ``secure`` -- boolean (default: ``False``)

        If ``secure`` is ``True`` and the degree of this polynomial
        is not determined (because the leading coefficient is
        indistinguishable from 0), an error is raised.

        If ``secure`` is ``False``, the returned value is the largest
        `n` so that the coefficient of `x^n` does not compare equal
        to `0`.

        EXAMPLES::

            sage: K = Qp(3,10)
            sage: R.<T> = K[]
            sage: f = T + 2; f
            (1 + O(3^10))*T + 2 + O(3^10)
            sage: f.degree()
            1
            sage: (f-T).degree()
            0
            sage: (f-T).degree(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: the leading coefficient is indistinguishable from 0

            sage: x = O(3^5)
            sage: li = [3^i * x for i in range(0,5)]; li
            [O(3^5), O(3^6), O(3^7), O(3^8), O(3^9)]
            sage: f = R(li); f
            O(3^9)*T^4 + O(3^8)*T^3 + O(3^7)*T^2 + O(3^6)*T + O(3^5)
            sage: f.degree()
            -1
            sage: f.degree(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: the leading coefficient is indistinguishable from 0
        """
    def prec_degree(self):
        """
        Return the largest `n` so that precision information is
        stored about the coefficient of `x^n`.

        Always greater than or equal to degree.

        EXAMPLES::

            sage: K = Qp(3,10)
            sage: R.<T> = K[]
            sage: f = T + 2; f
            (1 + O(3^10))*T + 2 + O(3^10)
            sage: f.prec_degree()
            1
        """
    def precision_absolute(self, n=None):
        """
        Return absolute precision information about ``self``.

        INPUT:

        - ``self`` -- a `p`-adic polynomial

        - ``n`` -- ``None`` or integer (default: ``None``)

        OUTPUT:

        If ``n`` is ``None``, returns a list of absolute precisions of
        coefficients.  Otherwise, returns the absolute precision of
        the coefficient of `x^n`.

        EXAMPLES::

            sage: K = Qp(3,10)
            sage: R.<T> = K[]
            sage: f = T + 2; f
            (1 + O(3^10))*T + 2 + O(3^10)
            sage: f.precision_absolute()
            [10, 10]
        """
    def precision_relative(self, n=None):
        """
        Return relative precision information about ``self``.

        INPUT:

        - ``self`` -- a `p`-adic polynomial

        - ``n`` -- ``None`` or integer (default: ``None``)

        OUTPUT:

        If ``n`` is ``None``, returns a list of relative precisions of
        coefficients.  Otherwise, returns the relative precision of
        the coefficient of `x^n`.

        EXAMPLES::

            sage: K = Qp(3,10)
            sage: R.<T> = K[]
            sage: f = T + 2; f
            (1 + O(3^10))*T + 2 + O(3^10)
            sage: f.precision_relative()
            [10, 10]
        """
    def valuation_of_coefficient(self, n=None):
        """
        Return valuation information about ``self``'s coefficients.

        INPUT:

        - ``self`` -- a `p`-adic polynomial

        - ``n`` -- ``None`` or integer (default: ``None``)

        OUTPUT:

        If ``n`` is ``None``, returns a list of valuations of coefficients.  Otherwise,
        returns the valuation of the coefficient of `x^n`.

        EXAMPLES::

            sage: K = Qp(3,10)
            sage: R.<T> = K[]
            sage: f = T + 2; f
            (1 + O(3^10))*T + 2 + O(3^10)
            sage: f.valuation_of_coefficient(1)
            0
        """
    def valuation(self, val_of_var=None):
        """
        Return the valuation of ``self``.

        INPUT:

        - ``self`` -- a `p`-adic polynomial

        - ``val_of_var`` -- ``None`` or a rational (default: ``None``)

        OUTPUT:

        If ``val_of_var`` is ``None``, returns the largest power of the
        variable dividing ``self``.  Otherwise, returns the valuation of
        ``self`` where the variable is assigned valuation ``val_of_var``

        EXAMPLES::

            sage: K = Qp(3,10)
            sage: R.<T> = K[]
            sage: f = T + 2; f
            (1 + O(3^10))*T + 2 + O(3^10)
            sage: f.valuation()
            0
        """
    def reverse(self, degree=None):
        """
        Return the reverse of the input polynomial, thought as a polynomial of
        degree ``degree``.

        If `f` is a degree-`d` polynomial, its reverse is `x^d f(1/x)`.

        INPUT:

        - ``degree`` -- ``None`` or integer; if specified, truncate or zero
          pad the list of coefficients to this degree before reversing it

        EXAMPLES::

            sage: K = Qp(13,7)
            sage: R.<t> = K[]
            sage: f = t^3 + 4*t; f
            (1 + O(13^7))*t^3 + (4 + O(13^7))*t
            sage: f.reverse()
            0*t^3 + (4 + O(13^7))*t^2 + 1 + O(13^7)
            sage: f.reverse(3)
            0*t^3 + (4 + O(13^7))*t^2 + 1 + O(13^7)
            sage: f.reverse(2)
            0*t^2 + (4 + O(13^7))*t
            sage: f.reverse(4)
            0*t^4 + (4 + O(13^7))*t^3 + (1 + O(13^7))*t
            sage: f.reverse(6)
            0*t^6 + (4 + O(13^7))*t^5 + (1 + O(13^7))*t^3

        TESTS:

        Check that this implementation is compatible with the generic one::

            sage: all(f.reverse(d) == Polynomial.reverse(f, d)
            ....:     for d in [None,0,1,2,3,4,5])
            True
        """
    def rescale(self, a):
        """
        Return `f(a\\cdot x)`.

        .. TODO::

            Need to write this function for integer polynomials before
            this works.

        EXAMPLES::

            sage: K = Zp(13, 5)
            sage: R.<t> = K[]
            sage: f = t^3 + K(13, 3) * t
            sage: f.rescale(2)  # not implemented
        """
    def quo_rem(self, right, secure: bool = False):
        """
        Return the quotient and remainder in division of ``self`` by ``right``.

        EXAMPLES::

            sage: K = Qp(3,10)
            sage: R.<T> = K[]
            sage: f = T + 2
            sage: g = T**4 + 3*T+22
            sage: g.quo_rem(f)
            ((1 + O(3^10))*T^3 + (1 + 2*3 + 2*3^2 + 2*3^3 + 2*3^4 + 2*3^5 + 2*3^6 + 2*3^7 + 2*3^8 + 2*3^9 + O(3^10))*T^2 + (1 + 3 + O(3^10))*T + 1 + 3 + 2*3^2 + 2*3^3 + 2*3^4 + 2*3^5 + 2*3^6 + 2*3^7 + 2*3^8 + 2*3^9 + O(3^10),
             2 + 3 + 3^3 + O(3^10))

        TESTS:

        Verify that :issue:`15188` has been resolved::

            sage: R.<x> = Qp(3)[]
            sage: x.quo_rem(x)
            (1 + O(3^20), 0)
        """
    def disc(self): ...
    def newton_polygon(self):
        """
        Return the Newton polygon of this polynomial.

        .. NOTE::

            If some coefficients have not enough precision an error is raised.

        OUTPUT: a :class:`NewtonPolygon`

        EXAMPLES::

            sage: K = Qp(2, prec=5)
            sage: P.<x> = K[]
            sage: f = x^4 + 2^3*x^3 + 2^13*x^2 + 2^21*x + 2^37
            sage: f.newton_polygon()                                                    # needs sage.geometry.polyhedron
            Finite Newton polygon with 4 vertices: (0, 37), (1, 21), (3, 3), (4, 0)

            sage: K = Qp(5)
            sage: R.<t> = K[]
            sage: f = 5 + 3*t + t^4 + 25*t^10
            sage: f.newton_polygon()                                                    # needs sage.geometry.polyhedron
            Finite Newton polygon with 4 vertices: (0, 1), (1, 0), (4, 0), (10, 2)

        Here is an example where the computation fails because precision is
        not sufficient::

            sage: g = f + K(0,0)*t^4; g
            (5^2 + O(5^22))*t^10 + O(5^0)*t^4 + (3 + O(5^20))*t + 5 + O(5^21)
            sage: g.newton_polygon()                                                    # needs sage.geometry.polyhedron
            Traceback (most recent call last):
            ...
            PrecisionError: The coefficient of t^4 has not enough precision

        TESTS::

            sage: (5*f).newton_polygon()                                                # needs sage.geometry.polyhedron
            Finite Newton polygon with 4 vertices: (0, 2), (1, 1), (4, 1), (10, 3)

        AUTHOR:

        - Xavier Caruso (2013-03-20)
        """
    def is_eisenstein(self, secure: bool = False):
        """
        Return ``True`` if this polynomial is an Eisenstein polynomial.

        EXAMPLES::

            sage: K = Qp(5)
            sage: R.<t> = K[]
            sage: f = 5 + 5*t + t^4
            sage: f.is_eisenstein()
            True

        TESTS::

            sage: f = R([K(5,1),0,0,1]); f
            (1 + O(5^20))*t^3 + O(5)
            sage: f.is_eisenstein()
            Traceback (most recent call last):
            ...
            PrecisionError: Not enough precision on the constant coefficient

            sage: g = R([5,K(0,0),0,1]); g
            (1 + O(5^20))*t^3 + O(5^0)*t + 5 + O(5^21)
            sage: g.is_eisenstein()
            True
            sage: g.is_eisenstein(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: Not enough precision on the coefficient of t

        AUTHOR:

        - Xavier Caruso (2013-03)
        """
    def newton_slopes(self, repetition: bool = True):
        """
        Return a list of the Newton slopes of this polynomial.

        These are the valuations of the roots of this polynomial.

        If ``repetition`` is ``True``, each slope is repeated a number of
        times equal to its multiplicity. Otherwise it appears only one time.

        INPUT:

        - ``repetition`` -- boolean (default: ``True``)

        OUTPUT: list of rationals

        EXAMPLES::

            sage: K = Qp(5)
            sage: R.<t> = K[]
            sage: f = 5 + 3*t + t^4 + 25*t^10
            sage: f.newton_polygon()                                                    # needs sage.geometry.polyhedron
            Finite Newton polygon with 4 vertices: (0, 1), (1, 0), (4, 0),
            (10, 2)
            sage: f.newton_slopes()                                                     # needs sage.geometry.polyhedron
            [1, 0, 0, 0, -1/3, -1/3, -1/3, -1/3, -1/3, -1/3]

            sage: f.newton_slopes(repetition=False)                                     # needs sage.geometry.polyhedron
            [1, 0, -1/3]

        AUTHOR:

        - Xavier Caruso (2013-03-20)
        """
    def factor_mod(self):
        """
        Return the factorization of ``self`` modulo `p`.
        """

def make_padic_poly(parent, x, version): ...
