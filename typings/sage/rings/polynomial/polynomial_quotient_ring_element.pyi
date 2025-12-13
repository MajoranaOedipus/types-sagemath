import sage.rings.polynomial.polynomial_singular_interface as polynomial_singular_interface
from sage.structure.element import CommutativeRingElement as CommutativeRingElement
from sage.structure.richcmp import richcmp as richcmp

class PolynomialQuotientRingElement(polynomial_singular_interface.Polynomial_singular_repr, CommutativeRingElement):
    """
    Element of a quotient of a polynomial ring.

    EXAMPLES::

        sage: P.<x> = QQ[]
        sage: Q.<xi> = P.quo([(x^2 + 1)])
        sage: xi^2
        -1
        sage: singular(xi)                                                              # needs sage.libs.singular
        xi
        sage: (singular(xi)*singular(xi)).NF('std(0)')                                  # needs sage.libs.singular
        -1
    """
    def __init__(self, parent, polynomial, check: bool = True) -> None:
        """
        Create an element of the quotient of a polynomial ring.

        INPUT:

        - ``parent`` -- a quotient of a polynomial ring

        - ``polynomial`` -- a polynomial

        - ``check`` -- boolean (default: ``True``); whether or not to
          verify that x is a valid element of the polynomial ring and reduced
          (mod the modulus).
        """
    def __hash__(self): ...
    def __reduce__(self):
        """
        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: S.<a> = R.quotient(2*x^3 + 3/2*x -1/3)
            sage: 2 * a^3
            -3/2*a + 1/3
            sage: loads(dumps(2*a^3)) == 2*a^3
            True
        """
    def __pari__(self):
        """
        Pari representation of this quotient element.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: I = R.ideal(x^10)
            sage: S.<xb> = R.quo(I)
            sage: pari(xb)^10
            Mod(0, x^10)
        """
    def __neg__(self): ...
    def __getitem__(self, n): ...
    def __int__(self) -> int:
        """
        Coerce this element to an int if possible.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: S.<a> = R.quotient(x^3 - 2)
            sage: int(S(10))
            10
            sage: int(a)
            Traceback (most recent call last):
            ...
            TypeError: cannot convert nonconstant polynomial
        """
    def is_unit(self):
        """
        Return ``True`` if ``self`` is invertible.

        .. WARNING::

            Only implemented when the base ring is a field.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: S.<y> = R.quotient(x^2 + 2*x + 1)
            sage: (2*y).is_unit()
            True
            sage: (y + 1).is_unit()
            False

        TESTS:

        Raise an exception if the base ring is not a field
        (see :issue:`13303`)::

            sage: Z16x.<x> = Integers(16)[]
            sage: S.<y> =  Z16x.quotient(x^2 + x + 1)
            sage: (2*y).is_unit()
            Traceback (most recent call last):
            ...
            NotImplementedError: The base ring (=Ring of integers modulo 16) is not a field

        Check that :issue:`29469` is fixed::

            sage: S(3).is_unit()
            True
        """
    def __invert__(self):
        """
        Return the inverse of this element.

        EXAMPLES::

            sage: R.<x> = QQ[]
            sage: S.<y> = R.quotient(x^2 + 2*x + 1)
            sage: (2*y)^(-1)
            -1/2*y - 1

        Raises a :exc:`ZeroDivisionError` if this element is not a unit::

            sage: (y+1)^(-1)
            Traceback (most recent call last):
            ...
            ArithmeticError: element is non-invertible

        TESTS:

        An element is not invertible if the base ring is not a field
        (see :issue:`13303`) (the test no longer makes sense when inversion is
        implemented for this particular base ring, need better test)::

            sage: Z16x.<x> = Integers(16)[]
            sage: S.<y> =  Z16x.quotient(x^2 + x + 1)
            sage: (2*y)^(-1)
            Traceback (most recent call last):
            ...
            ArithmeticError: element is non-invertible
            sage: (2*y+1)^(-1)  # this cannot raise ValueError because...
            10*y + 5
            sage: (2*y+1) * (10*y+5)  # the element is in fact invertible
            1

        Check that :issue:`29469` is fixed::

            sage: ~S(3)
            11
        """
    def field_extension(self, names):
        """
        Given a polynomial with base ring a quotient ring, return a
        3-tuple: a number field defined by the same polynomial, a
        homomorphism from its parent to the number field sending the
        generators to one another, and the inverse isomorphism.

        INPUT:

        - ``names`` -- name of generator of output field

        OUTPUT:

        -  field

        -  homomorphism from ``self`` to field

        -  homomorphism from field to ``self``

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: R.<x> = PolynomialRing(QQ)
            sage: S.<alpha> = R.quotient(x^3 - 2)
            sage: F.<a>, f, g = alpha.field_extension()
            sage: F
            Number Field in a with defining polynomial x^3 - 2
            sage: a = F.gen()
            sage: f(alpha)
            a
            sage: g(a)
            alpha

        Over a finite field, the corresponding field extension is not a
        number field::

            sage: # needs sage.rings.finite_rings
            sage: R.<x> = GF(25,'b')['x']
            sage: S.<a> = R.quo(x^3 + 2*x + 1)
            sage: F.<b>, g, h = a.field_extension()
            sage: h(b^2 + 3)
            a^2 + 3
            sage: g(x^2 + 2)
            b^2 + 2

        We do an example involving a relative number field::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ['x']
            sage: K.<a> = NumberField(x^3 - 2)
            sage: S.<X> = K['X']
            sage: Q.<b> = S.quo(X^3 + 2*X + 1)
            sage: F, g, h = b.field_extension('c')

        Another more awkward example::

            sage: # needs sage.rings.number_field
            sage: R.<x> = QQ['x']
            sage: K.<a> = NumberField(x^3 - 2)
            sage: S.<X> = K['X']
            sage: f = (X+a)^3 + 2*(X+a) + 1
            sage: f
            X^3 + 3*a*X^2 + (3*a^2 + 2)*X + 2*a + 3
            sage: Q.<z> = S.quo(f)
            sage: F.<w>, g, h = z.field_extension()
            sage: c = g(z)
            sage: f(c)
            0
            sage: h(g(z))
            z
            sage: g(h(w))
            w

        AUTHORS:

        - Craig Citro (2006-08-06)

        - William Stein (2006-08-06)
        """
    def charpoly(self, var):
        """
        The characteristic polynomial of this element, which is by
        definition the characteristic polynomial of right multiplication by
        this element.

        INPUT:

        - ``var`` -- string; the variable name

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: S.<a> = R.quo(x^3 -389*x^2 + 2*x - 5)
            sage: a.charpoly('X')                                                       # needs sage.modules
            X^3 - 389*X^2 + 2*X - 5
        """
    def fcp(self, var: str = 'x'):
        """
        Return the factorization of the characteristic polynomial of this
        element.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: S.<a> = R.quotient(x^3 -389*x^2 + 2*x - 5)
            sage: a.fcp('x')                                                            # needs sage.modules
            x^3 - 389*x^2 + 2*x - 5
            sage: S(1).fcp('y')                                                         # needs sage.modules
            (y - 1)^3
        """
    def lift(self):
        """
        Return lift of this polynomial quotient ring element to the unique
        equivalent polynomial of degree less than the modulus.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: S.<a> = R.quotient(x^3 - 2)
            sage: b = a^2 - 3
            sage: b
            a^2 - 3
            sage: b.lift()
            x^2 - 3
        """
    def __iter__(self): ...
    def list(self, copy: bool = True):
        """
        Return list of the elements of ``self``, of length the same as the
        degree of the quotient polynomial ring.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: S.<a> = R.quotient(x^3 + 2*x - 5)
            sage: a^10
            -134*a^2 - 35*a + 300
            sage: (a^10).list()
            [300, -35, -134]
        """
    def matrix(self):
        """
        The matrix of right multiplication by this element on the power
        basis for the quotient ring.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: S.<a> = R.quotient(x^3 + 2*x - 5)
            sage: a.matrix()                                                            # needs sage.modules
            [ 0  1  0]
            [ 0  0  1]
            [ 5 -2  0]
        """
    def minpoly(self):
        """
        The minimal polynomial of this element, which is by definition the
        minimal polynomial of the :meth:`matrix` of this element.

        ALGORITHM: Use
        :meth:`~sage.rings.polynomial.polynomial_zz_pex.Polynomial_ZZ_pEX.minpoly_mod`
        if possible, otherwise compute the minimal polynomial of the :meth:`matrix`.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: S.<a> = R.quotient(x^3 + 2*x - 5)
            sage: (a + 123).minpoly()                                                   # needs sage.modules
            x^3 - 369*x^2 + 45389*x - 1861118
            sage: (a + 123).matrix().minpoly()                                          # needs sage.modules
            x^3 - 369*x^2 + 45389*x - 1861118

        One useful application of this function is to compute a minimal
        polynomial of a finite-field element over an intermediate extension,
        rather than the absolute minimal polynomial over the prime field::

            sage: # needs sage.rings.finite_rings
            sage: F2.<i> = GF((431,2), modulus=[1,0,1])
            sage: F6.<u> = F2.extension(3)
            sage: (u + 1).minpoly()                                                     # needs sage.modules
            x^6 + 425*x^5 + 19*x^4 + 125*x^3 + 189*x^2 + 239*x + 302
            sage: ext = F6.over(F2)                                                     # needs sage.modules
            sage: ext(u + 1).minpoly()  # indirect doctest                              # needs sage.modules # random
            x^3 + (396*i + 428)*x^2 + (80*i + 39)*x + 9*i + 178

        TESTS:

        We make sure that the previous example works on random examples::

            sage: # long time, needs sage.rings.finite_rings
            sage: p = random_prime(50)
            sage: K.<u> = GF((p, randrange(1,20)))
            sage: L.<v> = K.extension(randrange(2,20))
            sage: LK = L.over(K)
            sage: a = L.random_element()
            sage: poly = LK(a).minpoly()  # indirect doctest
            sage: poly(a)
            0
            sage: abs_deg = a.minpoly().degree()
            sage: poly.degree() == abs_deg // gcd(abs_deg, K.degree())
            True
        """
    def norm(self):
        """
        The norm of this element, which is the determinant of the matrix of right
        multiplication by this element.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: S.<a> = R.quotient(x^3 - 389*x^2 + 2*x - 5)
            sage: a.norm()                                                              # needs sage.modules
            5
        """
    def trace(self):
        """
        The trace of this element, which is the trace of the matrix of
        right multiplication by this element.

        EXAMPLES::

            sage: R.<x> = PolynomialRing(QQ)
            sage: S.<a> = R.quotient(x^3 - 389*x^2 + 2*x - 5)
            sage: a.trace()                                                             # needs sage.modules
            389
        """
    def rational_reconstruction(self, *args, **kwargs):
        """
        Compute a rational reconstruction of this polynomial quotient
        ring element to its cover ring.

        This method is a thin convenience wrapper around
        :meth:`Polynomial.rational_reconstruction`.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: R.<x> = GF(65537)[]
            sage: m = (x^11 + 25345*x^10 + 10956*x^9 + 13873*x^8 + 23962*x^7
            ....:      + 17496*x^6 + 30348*x^5 + 7440*x^4 + 65438*x^3 + 7676*x^2
            ....:      + 54266*x + 47805)
            sage: f = (20437*x^10 + 62630*x^9 + 63241*x^8 + 12820*x^7 + 42171*x^6
            ....:      + 63091*x^5 + 15288*x^4 + 32516*x^3 + 2181*x^2 + 45236*x + 2447)
            sage: f_mod_m = R.quotient(m)(f)
            sage: f_mod_m.rational_reconstruction()
            (51388*x^5 + 29141*x^4 + 59341*x^3 + 7034*x^2 + 14152*x + 23746,
             x^5 + 15208*x^4 + 19504*x^3 + 20457*x^2 + 11180*x + 28352)
        """
