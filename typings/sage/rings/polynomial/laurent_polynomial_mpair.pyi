import sage.rings.polynomial.laurent_polynomial
from sage.misc.derivative import multi_derivative as multi_derivative
from sage.rings.infinity import Infinity as Infinity, minus_infinity as minus_infinity
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.factorization import Factorization as Factorization
from typing import Any, ClassVar, overload

class LaurentPolynomial_mpair(sage.rings.polynomial.laurent_polynomial.LaurentPolynomial):
    """LaurentPolynomial_mpair(parent, x, mon=None, reduce=True)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 22)

    Multivariate Laurent polynomials."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, mon=..., reduce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 27)

                Currently, one can only create LaurentPolynomials out of dictionaries
                and elements of the base ring.

                INPUT:

                - ``parent`` -- a SageMath parent

                - ``x`` -- an element or dictionary or anything the underlying
                  polynomial ring accepts

                - ``mon`` -- (default: ``None``) a tuple specifying the shift
                  in the exponents

                - ``reduce`` -- boolean (default: ``True``)

                EXAMPLES::

                    sage: L.<w,z> = LaurentPolynomialRing(QQ)
                    sage: f = L({(-1,-1):1}); f
                    w^-1*z^-1
                    sage: f = L({(1,1):1}); f
                    w*z
                    sage: f =  L({(-1,-1):1, (1,3):4}); f
                    4*w*z^3 + w^-1*z^-1
                    sage: L(1/2)
                    1/2

                TESTS:

                Check that :issue:`19538` is fixed::

                    sage: R = LaurentPolynomialRing(QQ,'x2,x0')
                    sage: S = LaurentPolynomialRing(QQ,'x',3)
                    sage: f = S.coerce_map_from(R)
                    sage: f(R.gen(0) + R.gen(1)^2)
                    x0^2 + x2
                    sage: _.parent()
                    Multivariate Laurent Polynomial Ring in x0, x1, x2 over Rational Field

                ::

                    sage: from sage.rings.polynomial.laurent_polynomial_mpair import LaurentPolynomial_mpair
                    sage: LaurentPolynomial_mpair(L, {(1,2): 1/42}, mon=(-3, -3))
                    1/42*w^-2*z^-1

                :issue:`22398`::

                    sage: LQ = LaurentPolynomialRing(QQ, 'x0, x1, x2, y0, y1, y2, y3, y4, y5')
                    sage: LZ = LaurentPolynomialRing(ZZ, 'x0, x1, x2, y0, y1, y2, y3, y4, y5')
                    sage: LQ.inject_variables()
                    Defining x0, x1, x2, y0, y1, y2, y3, y4, y5
                    sage: x2^-1*y0*y1*y2*y3*y4*y5 + x1^-1*x2^-1*y0*y1*y3*y4 + x0^-1 in LZ
                    True
                    sage: x2^-1*y0*y1*y2*y3*y4*y5 + x1^-1*x2^-1*y0*y1*y3*y4 + x0^-1*x1^-1*y0*y3 + x0^-1 in LZ
                    True

                Check that input is not modified::

                    sage: LQ.<x,y> = LaurentPolynomialRing(QQ)
                    sage: D = {(-1, 1): 1}
                    sage: k = tuple(D)[0]
                    sage: v = D[k]
                    sage: type(k), type(v)
                    (<... 'tuple'>, <class 'sage.rings.integer.Integer'>)
                    sage: LQ(D)
                    x^-1*y
                    sage: tuple(D)[0] is k
                    True
                    sage: D[k] is v
                    True
        """
    def coefficient(self, mon) -> Any:
        """LaurentPolynomial_mpair.coefficient(self, mon)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 692)

        Return the coefficient of ``mon`` in ``self``, where ``mon`` must
        have the same parent as ``self``.

        The coefficient is defined as follows. If `f` is this polynomial, then
        the coefficient `c_m` is sum:

        .. MATH::

            c_m := \\sum_T \\frac{T}{m}

        where the sum is over terms `T` in `f` that are exactly divisible
        by `m`.

        A monomial `m(x,y)` 'exactly divides' `f(x,y)` if `m(x,y) | f(x,y)`
        and neither `x \\cdot m(x,y)` nor `y \\cdot m(x,y)` divides `f(x,y)`.

        INPUT:

        - ``mon`` -- a monomial

        OUTPUT: element of the parent of ``self``

        .. NOTE::

            To get the constant coefficient, call
            :meth:`constant_coefficient()`.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)

        The coefficient returned is an element of the parent of ``self``; in
        this case, ``P``. ::

            sage: f = 2 * x * y
            sage: c = f.coefficient(x*y); c
            2
            sage: c.parent()
            Multivariate Laurent Polynomial Ring in x, y over Rational Field

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = (y^2 - x^9 - 7*x*y^2 + 5*x*y)*x^-3; f
            -x^6 - 7*x^-2*y^2 + 5*x^-2*y + x^-3*y^2
            sage: f.coefficient(y)
            5*x^-2
            sage: f.coefficient(y^2)
            -7*x^-2 + x^-3
            sage: f.coefficient(x*y)
            0
            sage: f.coefficient(x^-2)
            -7*y^2 + 5*y
            sage: f.coefficient(x^-2*y^2)
            -7
            sage: f.coefficient(1)
            -x^6 - 7*x^-2*y^2 + 5*x^-2*y + x^-3*y^2"""
    @overload
    def coefficients(self) -> Any:
        """LaurentPolynomial_mpair.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 759)

        Return the nonzero coefficients of ``self`` in a list.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ, order='degrevlex')
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.coefficients()
            [4, 3, 2, 1]
            sage: L.<x,y,z> = LaurentPolynomialRing(QQ,order='lex')
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.coefficients()
            [4, 1, 2, 3]"""
    @overload
    def coefficients(self) -> Any:
        """LaurentPolynomial_mpair.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 759)

        Return the nonzero coefficients of ``self`` in a list.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ, order='degrevlex')
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.coefficients()
            [4, 3, 2, 1]
            sage: L.<x,y,z> = LaurentPolynomialRing(QQ,order='lex')
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.coefficients()
            [4, 1, 2, 3]"""
    @overload
    def coefficients(self) -> Any:
        """LaurentPolynomial_mpair.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 759)

        Return the nonzero coefficients of ``self`` in a list.

        The returned list is decreasingly ordered by the term ordering
        of ``self.parent()``.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ, order='degrevlex')
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.coefficients()
            [4, 3, 2, 1]
            sage: L.<x,y,z> = LaurentPolynomialRing(QQ,order='lex')
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.coefficients()
            [4, 1, 2, 3]"""
    @overload
    def constant_coefficient(self) -> Any:
        """LaurentPolynomial_mpair.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 674)

        Return the constant coefficient of ``self``.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = (y^2 - x^9 - 7*x*y^2 + 5*x*y)*x^-3; f
            -x^6 - 7*x^-2*y^2 + 5*x^-2*y + x^-3*y^2
            sage: f.constant_coefficient()
            0
            sage: f = (x^3 + 2*x^-2*y+y^3)*y^-3; f
            x^3*y^-3 + 1 + 2*x^-2*y^-2
            sage: f.constant_coefficient()
            1"""
    @overload
    def constant_coefficient(self) -> Any:
        """LaurentPolynomial_mpair.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 674)

        Return the constant coefficient of ``self``.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = (y^2 - x^9 - 7*x*y^2 + 5*x*y)*x^-3; f
            -x^6 - 7*x^-2*y^2 + 5*x^-2*y + x^-3*y^2
            sage: f.constant_coefficient()
            0
            sage: f = (x^3 + 2*x^-2*y+y^3)*y^-3; f
            x^3*y^-3 + 1 + 2*x^-2*y^-2
            sage: f.constant_coefficient()
            1"""
    @overload
    def constant_coefficient(self) -> Any:
        """LaurentPolynomial_mpair.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 674)

        Return the constant coefficient of ``self``.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = (y^2 - x^9 - 7*x*y^2 + 5*x*y)*x^-3; f
            -x^6 - 7*x^-2*y^2 + 5*x^-2*y + x^-3*y^2
            sage: f.constant_coefficient()
            0
            sage: f = (x^3 + 2*x^-2*y+y^3)*y^-3; f
            x^3*y^-3 + 1 + 2*x^-2*y^-2
            sage: f.constant_coefficient()
            1"""
    @overload
    def degree(self, x=...) -> Any:
        """LaurentPolynomial_mpair.degree(self, x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1171)

        Return the degree of ``self``.

        INPUT:

        - ``x`` -- (default: ``None``) a generator of the parent ring

        OUTPUT:

        If ``x`` is ``None``, return the total degree of ``self``.
        If ``x`` is a given generator of the parent ring,
        the output is the maximum degree of ``x`` in ``self``.

        EXAMPLES::

            sage: R.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.degree()
            6
            sage: f.degree(x)
            7
            sage: f.degree(y)
            1
            sage: f.degree(z)
            0

        The zero polynomial is defined to have degree `-\\infty`::

            sage: R.<x, y, z> = LaurentPolynomialRing(ZZ)
            sage: R.zero().degree()
            -Infinity
            sage: R.zero().degree(x)
            -Infinity
            sage: R.zero().degree(x) == R.zero().degree(y) == R.zero().degree(z)
            True

        TESTS::

            sage: R.<x, y, z> = LaurentPolynomialRing(ZZ)
            sage: f = x + y + z
            sage: f.degree(1)
            Traceback (most recent call last):
            ...
            TypeError: 1 is not a generator of parent"""
    @overload
    def degree(self) -> Any:
        """LaurentPolynomial_mpair.degree(self, x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1171)

        Return the degree of ``self``.

        INPUT:

        - ``x`` -- (default: ``None``) a generator of the parent ring

        OUTPUT:

        If ``x`` is ``None``, return the total degree of ``self``.
        If ``x`` is a given generator of the parent ring,
        the output is the maximum degree of ``x`` in ``self``.

        EXAMPLES::

            sage: R.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.degree()
            6
            sage: f.degree(x)
            7
            sage: f.degree(y)
            1
            sage: f.degree(z)
            0

        The zero polynomial is defined to have degree `-\\infty`::

            sage: R.<x, y, z> = LaurentPolynomialRing(ZZ)
            sage: R.zero().degree()
            -Infinity
            sage: R.zero().degree(x)
            -Infinity
            sage: R.zero().degree(x) == R.zero().degree(y) == R.zero().degree(z)
            True

        TESTS::

            sage: R.<x, y, z> = LaurentPolynomialRing(ZZ)
            sage: f = x + y + z
            sage: f.degree(1)
            Traceback (most recent call last):
            ...
            TypeError: 1 is not a generator of parent"""
    @overload
    def degree(self, x) -> Any:
        """LaurentPolynomial_mpair.degree(self, x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1171)

        Return the degree of ``self``.

        INPUT:

        - ``x`` -- (default: ``None``) a generator of the parent ring

        OUTPUT:

        If ``x`` is ``None``, return the total degree of ``self``.
        If ``x`` is a given generator of the parent ring,
        the output is the maximum degree of ``x`` in ``self``.

        EXAMPLES::

            sage: R.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.degree()
            6
            sage: f.degree(x)
            7
            sage: f.degree(y)
            1
            sage: f.degree(z)
            0

        The zero polynomial is defined to have degree `-\\infty`::

            sage: R.<x, y, z> = LaurentPolynomialRing(ZZ)
            sage: R.zero().degree()
            -Infinity
            sage: R.zero().degree(x)
            -Infinity
            sage: R.zero().degree(x) == R.zero().degree(y) == R.zero().degree(z)
            True

        TESTS::

            sage: R.<x, y, z> = LaurentPolynomialRing(ZZ)
            sage: f = x + y + z
            sage: f.degree(1)
            Traceback (most recent call last):
            ...
            TypeError: 1 is not a generator of parent"""
    @overload
    def degree(self, y) -> Any:
        """LaurentPolynomial_mpair.degree(self, x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1171)

        Return the degree of ``self``.

        INPUT:

        - ``x`` -- (default: ``None``) a generator of the parent ring

        OUTPUT:

        If ``x`` is ``None``, return the total degree of ``self``.
        If ``x`` is a given generator of the parent ring,
        the output is the maximum degree of ``x`` in ``self``.

        EXAMPLES::

            sage: R.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.degree()
            6
            sage: f.degree(x)
            7
            sage: f.degree(y)
            1
            sage: f.degree(z)
            0

        The zero polynomial is defined to have degree `-\\infty`::

            sage: R.<x, y, z> = LaurentPolynomialRing(ZZ)
            sage: R.zero().degree()
            -Infinity
            sage: R.zero().degree(x)
            -Infinity
            sage: R.zero().degree(x) == R.zero().degree(y) == R.zero().degree(z)
            True

        TESTS::

            sage: R.<x, y, z> = LaurentPolynomialRing(ZZ)
            sage: f = x + y + z
            sage: f.degree(1)
            Traceback (most recent call last):
            ...
            TypeError: 1 is not a generator of parent"""
    @overload
    def degree(self, z) -> Any:
        """LaurentPolynomial_mpair.degree(self, x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1171)

        Return the degree of ``self``.

        INPUT:

        - ``x`` -- (default: ``None``) a generator of the parent ring

        OUTPUT:

        If ``x`` is ``None``, return the total degree of ``self``.
        If ``x`` is a given generator of the parent ring,
        the output is the maximum degree of ``x`` in ``self``.

        EXAMPLES::

            sage: R.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.degree()
            6
            sage: f.degree(x)
            7
            sage: f.degree(y)
            1
            sage: f.degree(z)
            0

        The zero polynomial is defined to have degree `-\\infty`::

            sage: R.<x, y, z> = LaurentPolynomialRing(ZZ)
            sage: R.zero().degree()
            -Infinity
            sage: R.zero().degree(x)
            -Infinity
            sage: R.zero().degree(x) == R.zero().degree(y) == R.zero().degree(z)
            True

        TESTS::

            sage: R.<x, y, z> = LaurentPolynomialRing(ZZ)
            sage: f = x + y + z
            sage: f.degree(1)
            Traceback (most recent call last):
            ...
            TypeError: 1 is not a generator of parent"""
    def derivative(self, *args) -> Any:
        """LaurentPolynomial_mpair.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1510)

        The formal derivative of this Laurent polynomial, with respect
        to variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global :func:`derivative` function for more
        details.

        .. SEEALSO::

            :meth:`_derivative`

        EXAMPLES::

            sage: R = LaurentPolynomialRing(ZZ,'x, y')
            sage: x, y = R.gens()
            sage: t = x**4*y + x*y + y + x**(-1) + y**(-3)
            sage: t.derivative(x, x)
            12*x^2*y + 2*x^-3
            sage: t.derivative(y, 2)
            12*y^-5"""
    def dict(self) -> Any:
        """LaurentPolynomial_mpair.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 809)

        Return ``self`` represented as a ``dict``.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: sorted(f.monomial_coefficients().items())
            [((3, 1, 0), 3), ((4, 0, -2), 2), ((6, -7, 0), 1), ((7, 0, -1), 4)]

        ``dict`` is an alias::

            sage: sorted(f.dict().items())
            [((3, 1, 0), 3), ((4, 0, -2), 2), ((6, -7, 0), 1), ((7, 0, -1), 4)]"""
    def diff(self, *args, **kwargs):
        """LaurentPolynomial_mpair.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1510)

        The formal derivative of this Laurent polynomial, with respect
        to variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global :func:`derivative` function for more
        details.

        .. SEEALSO::

            :meth:`_derivative`

        EXAMPLES::

            sage: R = LaurentPolynomialRing(ZZ,'x, y')
            sage: x, y = R.gens()
            sage: t = x**4*y + x*y + y + x**(-1) + y**(-3)
            sage: t.derivative(x, x)
            12*x^2*y + 2*x^-3
            sage: t.derivative(y, 2)
            12*y^-5"""
    def differentiate(self, *args, **kwargs):
        """LaurentPolynomial_mpair.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1510)

        The formal derivative of this Laurent polynomial, with respect
        to variables supplied in args.

        Multiple variables and iteration counts may be supplied; see
        documentation for the global :func:`derivative` function for more
        details.

        .. SEEALSO::

            :meth:`_derivative`

        EXAMPLES::

            sage: R = LaurentPolynomialRing(ZZ,'x, y')
            sage: x, y = R.gens()
            sage: t = x**4*y + x*y + y + x**(-1) + y**(-3)
            sage: t.derivative(x, x)
            12*x^2*y + 2*x^-3
            sage: t.derivative(y, 2)
            12*y^-5"""
    @overload
    def divides(self, other) -> Any:
        """LaurentPolynomial_mpair.divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 2001)

        Check if ``self`` divides ``other``.

        EXAMPLES::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)
            sage: f1 = x^-2*y^3 - 9 - 1/14*x^-1*y - 1/3*x^-1
            sage: h = 3*x^-1 - 3*x^-2*y - 1/2*x^-3*y^2 - x^-3*y + x^-3
            sage: f2 = f1 * h
            sage: f3 = f2 + x * y
            sage: f1.divides(f2)
            True
            sage: f1.divides(f3)
            False
            sage: f1.divides(3)
            False"""
    @overload
    def divides(self, f2) -> Any:
        """LaurentPolynomial_mpair.divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 2001)

        Check if ``self`` divides ``other``.

        EXAMPLES::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)
            sage: f1 = x^-2*y^3 - 9 - 1/14*x^-1*y - 1/3*x^-1
            sage: h = 3*x^-1 - 3*x^-2*y - 1/2*x^-3*y^2 - x^-3*y + x^-3
            sage: f2 = f1 * h
            sage: f3 = f2 + x * y
            sage: f1.divides(f2)
            True
            sage: f1.divides(f3)
            False
            sage: f1.divides(3)
            False"""
    @overload
    def divides(self, f3) -> Any:
        """LaurentPolynomial_mpair.divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 2001)

        Check if ``self`` divides ``other``.

        EXAMPLES::

            sage: R.<x,y> = LaurentPolynomialRing(QQ)
            sage: f1 = x^-2*y^3 - 9 - 1/14*x^-1*y - 1/3*x^-1
            sage: h = 3*x^-1 - 3*x^-2*y - 1/2*x^-3*y^2 - x^-3*y + x^-3
            sage: f2 = f1 * h
            sage: f3 = f2 + x * y
            sage: f1.divides(f2)
            True
            sage: f1.divides(f3)
            False
            sage: f1.divides(3)
            False"""
    @overload
    def exponents(self) -> Any:
        """LaurentPolynomial_mpair.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1156)

        Return a list of the exponents of ``self``.

        EXAMPLES::

            sage: L.<w,z> = LaurentPolynomialRing(QQ)
            sage: a = w^2*z^-1 + 3; a
            w^2*z^-1 + 3
            sage: e = a.exponents()
            sage: e.sort(); e
            [(0, 0), (2, -1)]"""
    @overload
    def exponents(self) -> Any:
        """LaurentPolynomial_mpair.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1156)

        Return a list of the exponents of ``self``.

        EXAMPLES::

            sage: L.<w,z> = LaurentPolynomialRing(QQ)
            sage: a = w^2*z^-1 + 3; a
            w^2*z^-1 + 3
            sage: e = a.exponents()
            sage: e.sort(); e
            [(0, 0), (2, -1)]"""
    @overload
    def factor(self) -> Any:
        """LaurentPolynomial_mpair.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1696)

        Return a Laurent monomial (the unit part of the factorization) and a factored multi-polynomial.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.factor()
            (x^3*y^-7*z^-2) * (4*x^4*y^7*z + 3*y^8*z^2 + 2*x*y^7 + x^3*z^2)

        TESTS:

        Tests for :issue:`29173`::

            sage: L.<a, b> = LaurentPolynomialRing(ZZ, 'a, b')
            sage: (a*b + a + b + 1).factor()
            (b + 1) * (a + 1)
            sage: ((a^-1)*(a*b + a + b + 1)).factor()
            (a^-1) * (b + 1) * (a + 1)
            sage: L(-12).factor()
            -1 * 2^2 * 3"""
    @overload
    def factor(self) -> Any:
        """LaurentPolynomial_mpair.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1696)

        Return a Laurent monomial (the unit part of the factorization) and a factored multi-polynomial.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.factor()
            (x^3*y^-7*z^-2) * (4*x^4*y^7*z + 3*y^8*z^2 + 2*x*y^7 + x^3*z^2)

        TESTS:

        Tests for :issue:`29173`::

            sage: L.<a, b> = LaurentPolynomialRing(ZZ, 'a, b')
            sage: (a*b + a + b + 1).factor()
            (b + 1) * (a + 1)
            sage: ((a^-1)*(a*b + a + b + 1)).factor()
            (a^-1) * (b + 1) * (a + 1)
            sage: L(-12).factor()
            -1 * 2^2 * 3"""
    @overload
    def factor(self) -> Any:
        """LaurentPolynomial_mpair.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1696)

        Return a Laurent monomial (the unit part of the factorization) and a factored multi-polynomial.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.factor()
            (x^3*y^-7*z^-2) * (4*x^4*y^7*z + 3*y^8*z^2 + 2*x*y^7 + x^3*z^2)

        TESTS:

        Tests for :issue:`29173`::

            sage: L.<a, b> = LaurentPolynomialRing(ZZ, 'a, b')
            sage: (a*b + a + b + 1).factor()
            (b + 1) * (a + 1)
            sage: ((a^-1)*(a*b + a + b + 1)).factor()
            (a^-1) * (b + 1) * (a + 1)
            sage: L(-12).factor()
            -1 * 2^2 * 3"""
    @overload
    def factor(self) -> Any:
        """LaurentPolynomial_mpair.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1696)

        Return a Laurent monomial (the unit part of the factorization) and a factored multi-polynomial.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.factor()
            (x^3*y^-7*z^-2) * (4*x^4*y^7*z + 3*y^8*z^2 + 2*x*y^7 + x^3*z^2)

        TESTS:

        Tests for :issue:`29173`::

            sage: L.<a, b> = LaurentPolynomialRing(ZZ, 'a, b')
            sage: (a*b + a + b + 1).factor()
            (b + 1) * (a + 1)
            sage: ((a^-1)*(a*b + a + b + 1)).factor()
            (a^-1) * (b + 1) * (a + 1)
            sage: L(-12).factor()
            -1 * 2^2 * 3"""
    @overload
    def factor(self) -> Any:
        """LaurentPolynomial_mpair.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1696)

        Return a Laurent monomial (the unit part of the factorization) and a factored multi-polynomial.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.factor()
            (x^3*y^-7*z^-2) * (4*x^4*y^7*z + 3*y^8*z^2 + 2*x*y^7 + x^3*z^2)

        TESTS:

        Tests for :issue:`29173`::

            sage: L.<a, b> = LaurentPolynomialRing(ZZ, 'a, b')
            sage: (a*b + a + b + 1).factor()
            (b + 1) * (a + 1)
            sage: ((a^-1)*(a*b + a + b + 1)).factor()
            (a^-1) * (b + 1) * (a + 1)
            sage: L(-12).factor()
            -1 * 2^2 * 3"""
    @overload
    def has_any_inverse(self) -> Any:
        """LaurentPolynomial_mpair.has_any_inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1327)

        Return ``True`` if ``self`` contains any monomials with a negative
        exponent, ``False`` otherwise.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.has_any_inverse()
            True
            sage: g = x^2 + y^2
            sage: g.has_any_inverse()
            False"""
    @overload
    def has_any_inverse(self) -> Any:
        """LaurentPolynomial_mpair.has_any_inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1327)

        Return ``True`` if ``self`` contains any monomials with a negative
        exponent, ``False`` otherwise.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.has_any_inverse()
            True
            sage: g = x^2 + y^2
            sage: g.has_any_inverse()
            False"""
    @overload
    def has_any_inverse(self) -> Any:
        """LaurentPolynomial_mpair.has_any_inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1327)

        Return ``True`` if ``self`` contains any monomials with a negative
        exponent, ``False`` otherwise.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.has_any_inverse()
            True
            sage: g = x^2 + y^2
            sage: g.has_any_inverse()
            False"""
    def has_inverse_of(self, i) -> Any:
        """LaurentPolynomial_mpair.has_inverse_of(self, i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1296)

        INPUT:

        - ``i`` -- the index of a generator of ``self.parent()``

        OUTPUT:

        Return ``True`` if ``self`` contains a monomial including the inverse of
        ``self.parent().gen(i)``, ``False`` otherwise.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.has_inverse_of(0)
            False
            sage: f.has_inverse_of(1)
            True
            sage: f.has_inverse_of(2)
            True"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_mpair.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1473)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: L.<a, b> = LaurentPolynomialRing(QQ)
            sage: L(0).is_constant()
            True
            sage: L(42).is_constant()
            True
            sage: a.is_constant()
            False
            sage: (1/b).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_mpair.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1473)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: L.<a, b> = LaurentPolynomialRing(QQ)
            sage: L(0).is_constant()
            True
            sage: L(42).is_constant()
            True
            sage: a.is_constant()
            False
            sage: (1/b).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_mpair.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1473)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: L.<a, b> = LaurentPolynomialRing(QQ)
            sage: L(0).is_constant()
            True
            sage: L(42).is_constant()
            True
            sage: a.is_constant()
            False
            sage: (1/b).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_mpair.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1473)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: L.<a, b> = LaurentPolynomialRing(QQ)
            sage: L(0).is_constant()
            True
            sage: L(42).is_constant()
            True
            sage: a.is_constant()
            False
            sage: (1/b).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_mpair.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1473)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: L.<a, b> = LaurentPolynomialRing(QQ)
            sage: L(0).is_constant()
            True
            sage: L(42).is_constant()
            True
            sage: a.is_constant()
            False
            sage: (1/b).is_constant()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentPolynomial_mpair.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 940)

        Return ``True`` if ``self`` is a monomial.

        EXAMPLES::

            sage: k.<y,z> = LaurentPolynomialRing(QQ)
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (38*z^-2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentPolynomial_mpair.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 940)

        Return ``True`` if ``self`` is a monomial.

        EXAMPLES::

            sage: k.<y,z> = LaurentPolynomialRing(QQ)
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (38*z^-2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentPolynomial_mpair.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 940)

        Return ``True`` if ``self`` is a monomial.

        EXAMPLES::

            sage: k.<y,z> = LaurentPolynomialRing(QQ)
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (38*z^-2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentPolynomial_mpair.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 940)

        Return ``True`` if ``self`` is a monomial.

        EXAMPLES::

            sage: k.<y,z> = LaurentPolynomialRing(QQ)
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (38*z^-2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentPolynomial_mpair.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 940)

        Return ``True`` if ``self`` is a monomial.

        EXAMPLES::

            sage: k.<y,z> = LaurentPolynomialRing(QQ)
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (38*z^-2909).is_monomial()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentPolynomial_mpair.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 940)

        Return ``True`` if ``self`` is a monomial.

        EXAMPLES::

            sage: k.<y,z> = LaurentPolynomialRing(QQ)
            sage: z.is_monomial()
            True
            sage: k(1).is_monomial()
            True
            sage: (z+1).is_monomial()
            False
            sage: (z^-2909).is_monomial()
            True
            sage: (38*z^-2909).is_monomial()
            False"""
    @overload
    def is_square(self, root=...) -> Any:
        """LaurentPolynomial_mpair.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1743)

        Test whether this Laurent polynomial is a square.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if set to ``True``
          then return a pair ``(True, sqrt)`` with ``sqrt`` a square
          root of this Laurent polynomial when it exists or
          ``(False, None)``

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: p = 1 + x*y + z^-3
            sage: (p**2).is_square()
            True
            sage: (p**2).is_square(root=True)
            (True, x*y + 1 + z^-3)

            sage: x.is_square()
            False
            sage: x.is_square(root=True)
            (False, None)

            sage: (x**-4 * (1 + z)).is_square(root=False)
            False
            sage: (x**-4 * (1 + z)).is_square(root=True)
            (False, None)"""
    @overload
    def is_square(self) -> Any:
        """LaurentPolynomial_mpair.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1743)

        Test whether this Laurent polynomial is a square.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if set to ``True``
          then return a pair ``(True, sqrt)`` with ``sqrt`` a square
          root of this Laurent polynomial when it exists or
          ``(False, None)``

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: p = 1 + x*y + z^-3
            sage: (p**2).is_square()
            True
            sage: (p**2).is_square(root=True)
            (True, x*y + 1 + z^-3)

            sage: x.is_square()
            False
            sage: x.is_square(root=True)
            (False, None)

            sage: (x**-4 * (1 + z)).is_square(root=False)
            False
            sage: (x**-4 * (1 + z)).is_square(root=True)
            (False, None)"""
    @overload
    def is_square(self, root=...) -> Any:
        """LaurentPolynomial_mpair.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1743)

        Test whether this Laurent polynomial is a square.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if set to ``True``
          then return a pair ``(True, sqrt)`` with ``sqrt`` a square
          root of this Laurent polynomial when it exists or
          ``(False, None)``

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: p = 1 + x*y + z^-3
            sage: (p**2).is_square()
            True
            sage: (p**2).is_square(root=True)
            (True, x*y + 1 + z^-3)

            sage: x.is_square()
            False
            sage: x.is_square(root=True)
            (False, None)

            sage: (x**-4 * (1 + z)).is_square(root=False)
            False
            sage: (x**-4 * (1 + z)).is_square(root=True)
            (False, None)"""
    @overload
    def is_square(self) -> Any:
        """LaurentPolynomial_mpair.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1743)

        Test whether this Laurent polynomial is a square.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if set to ``True``
          then return a pair ``(True, sqrt)`` with ``sqrt`` a square
          root of this Laurent polynomial when it exists or
          ``(False, None)``

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: p = 1 + x*y + z^-3
            sage: (p**2).is_square()
            True
            sage: (p**2).is_square(root=True)
            (True, x*y + 1 + z^-3)

            sage: x.is_square()
            False
            sage: x.is_square(root=True)
            (False, None)

            sage: (x**-4 * (1 + z)).is_square(root=False)
            False
            sage: (x**-4 * (1 + z)).is_square(root=True)
            (False, None)"""
    @overload
    def is_square(self, root=...) -> Any:
        """LaurentPolynomial_mpair.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1743)

        Test whether this Laurent polynomial is a square.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if set to ``True``
          then return a pair ``(True, sqrt)`` with ``sqrt`` a square
          root of this Laurent polynomial when it exists or
          ``(False, None)``

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: p = 1 + x*y + z^-3
            sage: (p**2).is_square()
            True
            sage: (p**2).is_square(root=True)
            (True, x*y + 1 + z^-3)

            sage: x.is_square()
            False
            sage: x.is_square(root=True)
            (False, None)

            sage: (x**-4 * (1 + z)).is_square(root=False)
            False
            sage: (x**-4 * (1 + z)).is_square(root=True)
            (False, None)"""
    @overload
    def is_square(self, root=...) -> Any:
        """LaurentPolynomial_mpair.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1743)

        Test whether this Laurent polynomial is a square.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if set to ``True``
          then return a pair ``(True, sqrt)`` with ``sqrt`` a square
          root of this Laurent polynomial when it exists or
          ``(False, None)``

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: p = 1 + x*y + z^-3
            sage: (p**2).is_square()
            True
            sage: (p**2).is_square(root=True)
            (True, x*y + 1 + z^-3)

            sage: x.is_square()
            False
            sage: x.is_square(root=True)
            (False, None)

            sage: (x**-4 * (1 + z)).is_square(root=False)
            False
            sage: (x**-4 * (1 + z)).is_square(root=True)
            (False, None)"""
    @overload
    def is_square(self, root=...) -> Any:
        """LaurentPolynomial_mpair.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1743)

        Test whether this Laurent polynomial is a square.

        INPUT:

        - ``root`` -- boolean (default: ``False``); if set to ``True``
          then return a pair ``(True, sqrt)`` with ``sqrt`` a square
          root of this Laurent polynomial when it exists or
          ``(False, None)``

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: p = 1 + x*y + z^-3
            sage: (p**2).is_square()
            True
            sage: (p**2).is_square(root=True)
            (True, x*y + 1 + z^-3)

            sage: x.is_square()
            False
            sage: x.is_square(root=True)
            (False, None)

            sage: (x**-4 * (1 + z)).is_square(root=False)
            False
            sage: (x**-4 * (1 + z)).is_square(root=True)
            (False, None)"""
    @overload
    def is_unit(self) -> Any:
        """LaurentPolynomial_mpair.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 327)

        Return ``True`` if ``self`` is a unit.

        The ground ring is assumed to be an integral domain.

        This means that the Laurent polynomial is a monomial
        with unit coefficient.

        EXAMPLES::

            sage: L.<x,y> = LaurentPolynomialRing(QQ)
            sage: (x*y/2).is_unit()
            True
            sage: (x + y).is_unit()
            False
            sage: (L.zero()).is_unit()
            False
            sage: (L.one()).is_unit()
            True

            sage: L.<x,y> = LaurentPolynomialRing(ZZ)
            sage: (2*x*y).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """LaurentPolynomial_mpair.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 327)

        Return ``True`` if ``self`` is a unit.

        The ground ring is assumed to be an integral domain.

        This means that the Laurent polynomial is a monomial
        with unit coefficient.

        EXAMPLES::

            sage: L.<x,y> = LaurentPolynomialRing(QQ)
            sage: (x*y/2).is_unit()
            True
            sage: (x + y).is_unit()
            False
            sage: (L.zero()).is_unit()
            False
            sage: (L.one()).is_unit()
            True

            sage: L.<x,y> = LaurentPolynomialRing(ZZ)
            sage: (2*x*y).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """LaurentPolynomial_mpair.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 327)

        Return ``True`` if ``self`` is a unit.

        The ground ring is assumed to be an integral domain.

        This means that the Laurent polynomial is a monomial
        with unit coefficient.

        EXAMPLES::

            sage: L.<x,y> = LaurentPolynomialRing(QQ)
            sage: (x*y/2).is_unit()
            True
            sage: (x + y).is_unit()
            False
            sage: (L.zero()).is_unit()
            False
            sage: (L.one()).is_unit()
            True

            sage: L.<x,y> = LaurentPolynomialRing(ZZ)
            sage: (2*x*y).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """LaurentPolynomial_mpair.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 327)

        Return ``True`` if ``self`` is a unit.

        The ground ring is assumed to be an integral domain.

        This means that the Laurent polynomial is a monomial
        with unit coefficient.

        EXAMPLES::

            sage: L.<x,y> = LaurentPolynomialRing(QQ)
            sage: (x*y/2).is_unit()
            True
            sage: (x + y).is_unit()
            False
            sage: (L.zero()).is_unit()
            False
            sage: (L.one()).is_unit()
            True

            sage: L.<x,y> = LaurentPolynomialRing(ZZ)
            sage: (2*x*y).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """LaurentPolynomial_mpair.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 327)

        Return ``True`` if ``self`` is a unit.

        The ground ring is assumed to be an integral domain.

        This means that the Laurent polynomial is a monomial
        with unit coefficient.

        EXAMPLES::

            sage: L.<x,y> = LaurentPolynomialRing(QQ)
            sage: (x*y/2).is_unit()
            True
            sage: (x + y).is_unit()
            False
            sage: (L.zero()).is_unit()
            False
            sage: (L.one()).is_unit()
            True

            sage: L.<x,y> = LaurentPolynomialRing(ZZ)
            sage: (2*x*y).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """LaurentPolynomial_mpair.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 327)

        Return ``True`` if ``self`` is a unit.

        The ground ring is assumed to be an integral domain.

        This means that the Laurent polynomial is a monomial
        with unit coefficient.

        EXAMPLES::

            sage: L.<x,y> = LaurentPolynomialRing(QQ)
            sage: (x*y/2).is_unit()
            True
            sage: (x + y).is_unit()
            False
            sage: (L.zero()).is_unit()
            False
            sage: (L.one()).is_unit()
            True

            sage: L.<x,y> = LaurentPolynomialRing(ZZ)
            sage: (2*x*y).is_unit()
            False"""
    @overload
    def is_univariate(self) -> Any:
        """LaurentPolynomial_mpair.is_univariate(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1591)

        Return ``True`` if this is a univariate or constant Laurent polynomial,
        and ``False`` otherwise.

        EXAMPLES::

            sage: R.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = (x^3 + y^-3)*z
            sage: f.is_univariate()
            False
            sage: g = f(1, y, 4)
            sage: g.is_univariate()
            True
            sage: R(1).is_univariate()
            True"""
    @overload
    def is_univariate(self) -> Any:
        """LaurentPolynomial_mpair.is_univariate(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1591)

        Return ``True`` if this is a univariate or constant Laurent polynomial,
        and ``False`` otherwise.

        EXAMPLES::

            sage: R.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = (x^3 + y^-3)*z
            sage: f.is_univariate()
            False
            sage: g = f(1, y, 4)
            sage: g.is_univariate()
            True
            sage: R(1).is_univariate()
            True"""
    @overload
    def is_univariate(self) -> Any:
        """LaurentPolynomial_mpair.is_univariate(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1591)

        Return ``True`` if this is a univariate or constant Laurent polynomial,
        and ``False`` otherwise.

        EXAMPLES::

            sage: R.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = (x^3 + y^-3)*z
            sage: f.is_univariate()
            False
            sage: g = f(1, y, 4)
            sage: g.is_univariate()
            True
            sage: R(1).is_univariate()
            True"""
    @overload
    def is_univariate(self) -> Any:
        """LaurentPolynomial_mpair.is_univariate(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1591)

        Return ``True`` if this is a univariate or constant Laurent polynomial,
        and ``False`` otherwise.

        EXAMPLES::

            sage: R.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = (x^3 + y^-3)*z
            sage: f.is_univariate()
            False
            sage: g = f(1, y, 4)
            sage: g.is_univariate()
            True
            sage: R(1).is_univariate()
            True"""
    @overload
    def iterator_exp_coeff(self) -> Any:
        """LaurentPolynomial_mpair.iterator_exp_coeff(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 599)

        Iterate over ``self`` as pairs of (ETuple, coefficient).

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = (y^2 - x^9 - 7*x*y^3 + 5*x*y)*x^-3
            sage: list(f.iterator_exp_coeff())
            [((6, 0), -1), ((-2, 3), -7), ((-2, 1), 5), ((-3, 2), 1)]"""
    @overload
    def iterator_exp_coeff(self) -> Any:
        """LaurentPolynomial_mpair.iterator_exp_coeff(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 599)

        Iterate over ``self`` as pairs of (ETuple, coefficient).

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = (y^2 - x^9 - 7*x*y^3 + 5*x*y)*x^-3
            sage: list(f.iterator_exp_coeff())
            [((6, 0), -1), ((-2, 3), -7), ((-2, 1), 5), ((-3, 2), 1)]"""
    def monomial_coefficient(self, mon) -> Any:
        """LaurentPolynomial_mpair.monomial_coefficient(self, mon)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 626)

        Return the coefficient in the base ring of the monomial ``mon`` in
        ``self``, where ``mon`` must have the same parent as ``self``.

        This function contrasts with the function :meth:`coefficient()`
        which returns the coefficient of a monomial viewing this
        polynomial in a polynomial ring over a base ring having fewer
        variables.

        INPUT:

        - ``mon`` -- a monomial

        .. SEEALSO::

            For coefficients in a base ring of fewer variables, see
            :meth:`coefficient()`.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = (y^2 - x^9 - 7*x*y^3 + 5*x*y)*x^-3
            sage: f.monomial_coefficient(x^-2*y^3)
            -7
            sage: f.monomial_coefficient(x^2)
            0

        TESTS::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = y^2 * x^-2
            sage: f.monomial_coefficient(x + y)
            Traceback (most recent call last):
            ...
            ValueError: not a monomial"""
    @overload
    def monomial_coefficients(self) -> dict:
        """LaurentPolynomial_mpair.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 809)

        Return ``self`` represented as a ``dict``.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: sorted(f.monomial_coefficients().items())
            [((3, 1, 0), 3), ((4, 0, -2), 2), ((6, -7, 0), 1), ((7, 0, -1), 4)]

        ``dict`` is an alias::

            sage: sorted(f.dict().items())
            [((3, 1, 0), 3), ((4, 0, -2), 2), ((6, -7, 0), 1), ((7, 0, -1), 4)]"""
    @overload
    def monomial_coefficients(self) -> Any:
        """LaurentPolynomial_mpair.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 809)

        Return ``self`` represented as a ``dict``.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: sorted(f.monomial_coefficients().items())
            [((3, 1, 0), 3), ((4, 0, -2), 2), ((6, -7, 0), 1), ((7, 0, -1), 4)]

        ``dict`` is an alias::

            sage: sorted(f.dict().items())
            [((3, 1, 0), 3), ((4, 0, -2), 2), ((6, -7, 0), 1), ((7, 0, -1), 4)]"""
    @overload
    def monomial_reduction(self) -> Any:
        """LaurentPolynomial_mpair.monomial_reduction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1667)

        Factor ``self`` into a polynomial and a monomial.

        OUTPUT:

        A tuple ``(p, v)`` where ``p`` is the underlying polynomial and ``v``
        is a monomial.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(QQ)
            sage: f = y / x + x^2 / y + 3 * x^4 * y^-2
            sage: f.monomial_reduction()
            (3*x^5 + x^3*y + y^3, x^-1*y^-2)
            sage: f = y * x + x^2 / y + 3 * x^4 * y^-2
            sage: f.monomial_reduction()
             (3*x^3 + y^3 + x*y, x*y^-2)
            sage: x.monomial_reduction()
            (1, x)
            sage: (y^-1).monomial_reduction()
            (1, y^-1)"""
    @overload
    def monomial_reduction(self) -> Any:
        """LaurentPolynomial_mpair.monomial_reduction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1667)

        Factor ``self`` into a polynomial and a monomial.

        OUTPUT:

        A tuple ``(p, v)`` where ``p`` is the underlying polynomial and ``v``
        is a monomial.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(QQ)
            sage: f = y / x + x^2 / y + 3 * x^4 * y^-2
            sage: f.monomial_reduction()
            (3*x^5 + x^3*y + y^3, x^-1*y^-2)
            sage: f = y * x + x^2 / y + 3 * x^4 * y^-2
            sage: f.monomial_reduction()
             (3*x^3 + y^3 + x*y, x*y^-2)
            sage: x.monomial_reduction()
            (1, x)
            sage: (y^-1).monomial_reduction()
            (1, y^-1)"""
    @overload
    def monomial_reduction(self) -> Any:
        """LaurentPolynomial_mpair.monomial_reduction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1667)

        Factor ``self`` into a polynomial and a monomial.

        OUTPUT:

        A tuple ``(p, v)`` where ``p`` is the underlying polynomial and ``v``
        is a monomial.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(QQ)
            sage: f = y / x + x^2 / y + 3 * x^4 * y^-2
            sage: f.monomial_reduction()
            (3*x^5 + x^3*y + y^3, x^-1*y^-2)
            sage: f = y * x + x^2 / y + 3 * x^4 * y^-2
            sage: f.monomial_reduction()
             (3*x^3 + y^3 + x*y, x*y^-2)
            sage: x.monomial_reduction()
            (1, x)
            sage: (y^-1).monomial_reduction()
            (1, y^-1)"""
    @overload
    def monomial_reduction(self) -> Any:
        """LaurentPolynomial_mpair.monomial_reduction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1667)

        Factor ``self`` into a polynomial and a monomial.

        OUTPUT:

        A tuple ``(p, v)`` where ``p`` is the underlying polynomial and ``v``
        is a monomial.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(QQ)
            sage: f = y / x + x^2 / y + 3 * x^4 * y^-2
            sage: f.monomial_reduction()
            (3*x^5 + x^3*y + y^3, x^-1*y^-2)
            sage: f = y * x + x^2 / y + 3 * x^4 * y^-2
            sage: f.monomial_reduction()
             (3*x^3 + y^3 + x*y, x*y^-2)
            sage: x.monomial_reduction()
            (1, x)
            sage: (y^-1).monomial_reduction()
            (1, y^-1)"""
    @overload
    def monomial_reduction(self) -> Any:
        """LaurentPolynomial_mpair.monomial_reduction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1667)

        Factor ``self`` into a polynomial and a monomial.

        OUTPUT:

        A tuple ``(p, v)`` where ``p`` is the underlying polynomial and ``v``
        is a monomial.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(QQ)
            sage: f = y / x + x^2 / y + 3 * x^4 * y^-2
            sage: f.monomial_reduction()
            (3*x^5 + x^3*y + y^3, x^-1*y^-2)
            sage: f = y * x + x^2 / y + 3 * x^4 * y^-2
            sage: f.monomial_reduction()
             (3*x^3 + y^3 + x*y, x*y^-2)
            sage: x.monomial_reduction()
            (1, x)
            sage: (y^-1).monomial_reduction()
            (1, y^-1)"""
    @overload
    def monomials(self) -> Any:
        """LaurentPolynomial_mpair.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 613)

        Return the list of monomials in ``self``.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = (y^2 - x^9 - 7*x*y^3 + 5*x*y)*x^-3
            sage: sorted(f.monomials())
            [x^-3*y^2, x^-2*y, x^-2*y^3, x^6]"""
    @overload
    def monomials(self) -> Any:
        """LaurentPolynomial_mpair.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 613)

        Return the list of monomials in ``self``.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = (y^2 - x^9 - 7*x*y^3 + 5*x*y)*x^-3
            sage: sorted(f.monomials())
            [x^-3*y^2, x^-2*y, x^-2*y^3, x^6]"""
    @overload
    def number_of_terms(self) -> long:
        """LaurentPolynomial_mpair.number_of_terms(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 402)

        Return the number of nonzero coefficients of ``self``.

        Also called weight, hamming weight or sparsity.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(ZZ)
            sage: f = x^3 - y
            sage: f.number_of_terms()
            2
            sage: R(0).number_of_terms()
            0
            sage: f = (x+1/y)^100
            sage: f.number_of_terms()
            101

        The method :meth:`hamming_weight` is an alias::

            sage: f.hamming_weight()
            101"""
    @overload
    def number_of_terms(self) -> Any:
        """LaurentPolynomial_mpair.number_of_terms(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 402)

        Return the number of nonzero coefficients of ``self``.

        Also called weight, hamming weight or sparsity.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(ZZ)
            sage: f = x^3 - y
            sage: f.number_of_terms()
            2
            sage: R(0).number_of_terms()
            0
            sage: f = (x+1/y)^100
            sage: f.number_of_terms()
            101

        The method :meth:`hamming_weight` is an alias::

            sage: f.hamming_weight()
            101"""
    @overload
    def number_of_terms(self) -> Any:
        """LaurentPolynomial_mpair.number_of_terms(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 402)

        Return the number of nonzero coefficients of ``self``.

        Also called weight, hamming weight or sparsity.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(ZZ)
            sage: f = x^3 - y
            sage: f.number_of_terms()
            2
            sage: R(0).number_of_terms()
            0
            sage: f = (x+1/y)^100
            sage: f.number_of_terms()
            101

        The method :meth:`hamming_weight` is an alias::

            sage: f.hamming_weight()
            101"""
    @overload
    def number_of_terms(self) -> Any:
        """LaurentPolynomial_mpair.number_of_terms(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 402)

        Return the number of nonzero coefficients of ``self``.

        Also called weight, hamming weight or sparsity.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(ZZ)
            sage: f = x^3 - y
            sage: f.number_of_terms()
            2
            sage: R(0).number_of_terms()
            0
            sage: f = (x+1/y)^100
            sage: f.number_of_terms()
            101

        The method :meth:`hamming_weight` is an alias::

            sage: f.hamming_weight()
            101"""
    @overload
    def quo_rem(self, right) -> Any:
        """LaurentPolynomial_mpair.quo_rem(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1068)

        Divide this Laurent polynomial by ``right`` and return a quotient and
        a remainder.

        INPUT:

        - ``right`` -- a Laurent polynomial

        OUTPUT: a pair of Laurent polynomials

        EXAMPLES::

            sage: R.<s, t> = LaurentPolynomialRing(QQ)
            sage: (s^2 - t^2).quo_rem(s - t)                                            # needs sage.libs.singular
            (s + t, 0)
            sage: (s^-2 - t^2).quo_rem(s - t)                                           # needs sage.libs.singular
            (s + t, -s^2 + s^-2)
            sage: (s^-2 - t^2).quo_rem(s^-1 - t)                                        # needs sage.libs.singular
            (t + s^-1, 0)

        TESTS:

        Verify that :issue:`31257` is fixed::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = LaurentPolynomialRing(QQ)
            sage: q, r = (1/x).quo_rem(y)
            sage: q, r
            (x^-1*y^-1, 0)
            sage: q*y + r == 1/x
            True
            sage: q, r = (x^-2 - y^2).quo_rem(x - y)
            sage: q*(x - y) + r == x^-2 - y^2
            True"""
    @overload
    def quo_rem(self, y) -> Any:
        """LaurentPolynomial_mpair.quo_rem(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1068)

        Divide this Laurent polynomial by ``right`` and return a quotient and
        a remainder.

        INPUT:

        - ``right`` -- a Laurent polynomial

        OUTPUT: a pair of Laurent polynomials

        EXAMPLES::

            sage: R.<s, t> = LaurentPolynomialRing(QQ)
            sage: (s^2 - t^2).quo_rem(s - t)                                            # needs sage.libs.singular
            (s + t, 0)
            sage: (s^-2 - t^2).quo_rem(s - t)                                           # needs sage.libs.singular
            (s + t, -s^2 + s^-2)
            sage: (s^-2 - t^2).quo_rem(s^-1 - t)                                        # needs sage.libs.singular
            (t + s^-1, 0)

        TESTS:

        Verify that :issue:`31257` is fixed::

            sage: # needs sage.libs.singular
            sage: R.<x,y> = LaurentPolynomialRing(QQ)
            sage: q, r = (1/x).quo_rem(y)
            sage: q, r
            (x^-1*y^-1, 0)
            sage: q*y + r == 1/x
            True
            sage: q, r = (x^-2 - y^2).quo_rem(x - y)
            sage: q*(x - y) + r == x^-2 - y^2
            True"""
    def rescale_vars(self, dictd, h=..., new_ring=...) -> Any:
        """LaurentPolynomial_mpair.rescale_vars(self, dict d, h=None, new_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1792)

        Rescale variables in a Laurent polynomial.

        INPUT:

        - ``d`` -- a ``dict`` whose keys are the generator indices
          and values are the coefficients; so a pair ``(i, v)``
          means `x_i \\mapsto v x_i`
        - ``h`` -- (optional) a map to be applied to coefficients
          done after rescaling
        - ``new_ring`` -- (optional) a new ring to map the result into

        EXAMPLES::

            sage: L.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: p = x^-2*y + x*y^-2
            sage: p.rescale_vars({0: 2, 1: 3})
            2/9*x*y^-2 + 3/4*x^-2*y
            sage: F = GF(2)
            sage: p.rescale_vars({0: 3, 1: 7}, new_ring=L.change_ring(F))
            x*y^-2 + x^-2*y

        Test for :issue:`30331`::

            sage: F.<z> = CyclotomicField(3)                                            # needs sage.rings.number_field
            sage: p.rescale_vars({0: 2, 1: z}, new_ring=L.change_ring(F))               # needs sage.rings.number_field
            2*z*x*y^-2 + 1/4*z*x^-2*y"""
    @overload
    def subs(self, in_dict=..., **kwds) -> Any:
        """LaurentPolynomial_mpair.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1408)

        Substitute some variables in this Laurent polynomial.

        Variable/value pairs for the substitution may be given
        as a dictionary or via keyword-value pairs. If both are
        present, the latter take precedence.

        INPUT:

        - ``in_dict`` -- dictionary (optional)

        - ``**kwds`` -- keyword arguments

        OUTPUT: a Laurent polynomial

        EXAMPLES::

            sage: L.<x, y, z> = LaurentPolynomialRing(QQ)
            sage: f = x + 2*y + 3*z
            sage: f.subs(x=1)
            2*y + 3*z + 1
            sage: f.subs(y=1)
            x + 3*z + 2
            sage: f.subs(z=1)
            x + 2*y + 3
            sage: f.subs(x=1, y=1, z=1)
            6

            sage: f = x^-1
            sage: f.subs(x=2)
            1/2
            sage: f.subs({x: 2})
            1/2

            sage: f = x + 2*y + 3*z
            sage: f.subs({x: 1, y: 1, z: 1})
            6
            sage: f.substitute(x=1, y=1, z=1)
            6

        TESTS::

            sage: f = x + 2*y + 3*z
            sage: f(q=10)
            x + 2*y + 3*z

            sage: x.subs({x: 2}, x=1)
            1

            sage: f.subs({1: 2}, x=1)
            3*z + 5"""
    @overload
    def subs(self, x=...) -> Any:
        """LaurentPolynomial_mpair.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1408)

        Substitute some variables in this Laurent polynomial.

        Variable/value pairs for the substitution may be given
        as a dictionary or via keyword-value pairs. If both are
        present, the latter take precedence.

        INPUT:

        - ``in_dict`` -- dictionary (optional)

        - ``**kwds`` -- keyword arguments

        OUTPUT: a Laurent polynomial

        EXAMPLES::

            sage: L.<x, y, z> = LaurentPolynomialRing(QQ)
            sage: f = x + 2*y + 3*z
            sage: f.subs(x=1)
            2*y + 3*z + 1
            sage: f.subs(y=1)
            x + 3*z + 2
            sage: f.subs(z=1)
            x + 2*y + 3
            sage: f.subs(x=1, y=1, z=1)
            6

            sage: f = x^-1
            sage: f.subs(x=2)
            1/2
            sage: f.subs({x: 2})
            1/2

            sage: f = x + 2*y + 3*z
            sage: f.subs({x: 1, y: 1, z: 1})
            6
            sage: f.substitute(x=1, y=1, z=1)
            6

        TESTS::

            sage: f = x + 2*y + 3*z
            sage: f(q=10)
            x + 2*y + 3*z

            sage: x.subs({x: 2}, x=1)
            1

            sage: f.subs({1: 2}, x=1)
            3*z + 5"""
    @overload
    def subs(self, y=...) -> Any:
        """LaurentPolynomial_mpair.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1408)

        Substitute some variables in this Laurent polynomial.

        Variable/value pairs for the substitution may be given
        as a dictionary or via keyword-value pairs. If both are
        present, the latter take precedence.

        INPUT:

        - ``in_dict`` -- dictionary (optional)

        - ``**kwds`` -- keyword arguments

        OUTPUT: a Laurent polynomial

        EXAMPLES::

            sage: L.<x, y, z> = LaurentPolynomialRing(QQ)
            sage: f = x + 2*y + 3*z
            sage: f.subs(x=1)
            2*y + 3*z + 1
            sage: f.subs(y=1)
            x + 3*z + 2
            sage: f.subs(z=1)
            x + 2*y + 3
            sage: f.subs(x=1, y=1, z=1)
            6

            sage: f = x^-1
            sage: f.subs(x=2)
            1/2
            sage: f.subs({x: 2})
            1/2

            sage: f = x + 2*y + 3*z
            sage: f.subs({x: 1, y: 1, z: 1})
            6
            sage: f.substitute(x=1, y=1, z=1)
            6

        TESTS::

            sage: f = x + 2*y + 3*z
            sage: f(q=10)
            x + 2*y + 3*z

            sage: x.subs({x: 2}, x=1)
            1

            sage: f.subs({1: 2}, x=1)
            3*z + 5"""
    @overload
    def subs(self, z=...) -> Any:
        """LaurentPolynomial_mpair.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1408)

        Substitute some variables in this Laurent polynomial.

        Variable/value pairs for the substitution may be given
        as a dictionary or via keyword-value pairs. If both are
        present, the latter take precedence.

        INPUT:

        - ``in_dict`` -- dictionary (optional)

        - ``**kwds`` -- keyword arguments

        OUTPUT: a Laurent polynomial

        EXAMPLES::

            sage: L.<x, y, z> = LaurentPolynomialRing(QQ)
            sage: f = x + 2*y + 3*z
            sage: f.subs(x=1)
            2*y + 3*z + 1
            sage: f.subs(y=1)
            x + 3*z + 2
            sage: f.subs(z=1)
            x + 2*y + 3
            sage: f.subs(x=1, y=1, z=1)
            6

            sage: f = x^-1
            sage: f.subs(x=2)
            1/2
            sage: f.subs({x: 2})
            1/2

            sage: f = x + 2*y + 3*z
            sage: f.subs({x: 1, y: 1, z: 1})
            6
            sage: f.substitute(x=1, y=1, z=1)
            6

        TESTS::

            sage: f = x + 2*y + 3*z
            sage: f(q=10)
            x + 2*y + 3*z

            sage: x.subs({x: 2}, x=1)
            1

            sage: f.subs({1: 2}, x=1)
            3*z + 5"""
    @overload
    def subs(self, x=..., y=..., z=...) -> Any:
        """LaurentPolynomial_mpair.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1408)

        Substitute some variables in this Laurent polynomial.

        Variable/value pairs for the substitution may be given
        as a dictionary or via keyword-value pairs. If both are
        present, the latter take precedence.

        INPUT:

        - ``in_dict`` -- dictionary (optional)

        - ``**kwds`` -- keyword arguments

        OUTPUT: a Laurent polynomial

        EXAMPLES::

            sage: L.<x, y, z> = LaurentPolynomialRing(QQ)
            sage: f = x + 2*y + 3*z
            sage: f.subs(x=1)
            2*y + 3*z + 1
            sage: f.subs(y=1)
            x + 3*z + 2
            sage: f.subs(z=1)
            x + 2*y + 3
            sage: f.subs(x=1, y=1, z=1)
            6

            sage: f = x^-1
            sage: f.subs(x=2)
            1/2
            sage: f.subs({x: 2})
            1/2

            sage: f = x + 2*y + 3*z
            sage: f.subs({x: 1, y: 1, z: 1})
            6
            sage: f.substitute(x=1, y=1, z=1)
            6

        TESTS::

            sage: f = x + 2*y + 3*z
            sage: f(q=10)
            x + 2*y + 3*z

            sage: x.subs({x: 2}, x=1)
            1

            sage: f.subs({1: 2}, x=1)
            3*z + 5"""
    @overload
    def subs(self, x=...) -> Any:
        """LaurentPolynomial_mpair.subs(self, in_dict=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1408)

        Substitute some variables in this Laurent polynomial.

        Variable/value pairs for the substitution may be given
        as a dictionary or via keyword-value pairs. If both are
        present, the latter take precedence.

        INPUT:

        - ``in_dict`` -- dictionary (optional)

        - ``**kwds`` -- keyword arguments

        OUTPUT: a Laurent polynomial

        EXAMPLES::

            sage: L.<x, y, z> = LaurentPolynomialRing(QQ)
            sage: f = x + 2*y + 3*z
            sage: f.subs(x=1)
            2*y + 3*z + 1
            sage: f.subs(y=1)
            x + 3*z + 2
            sage: f.subs(z=1)
            x + 2*y + 3
            sage: f.subs(x=1, y=1, z=1)
            6

            sage: f = x^-1
            sage: f.subs(x=2)
            1/2
            sage: f.subs({x: 2})
            1/2

            sage: f = x + 2*y + 3*z
            sage: f.subs({x: 1, y: 1, z: 1})
            6
            sage: f.substitute(x=1, y=1, z=1)
            6

        TESTS::

            sage: f = x + 2*y + 3*z
            sage: f(q=10)
            x + 2*y + 3*z

            sage: x.subs({x: 2}, x=1)
            1

            sage: f.subs({1: 2}, x=1)
            3*z + 5"""
    def toric_coordinate_change(self, M, h=..., new_ring=...) -> Any:
        """LaurentPolynomial_mpair.toric_coordinate_change(self, M, h=None, new_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1859)

        Apply a matrix to the exponents in a Laurent polynomial.

        For efficiency, we implement this directly, rather than as a substitution.

        The optional argument ``h`` is a map to be applied to coefficients.

        EXAMPLES::

            sage: L.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: p = 2*x^2 + y - x*y
            sage: p.toric_coordinate_change(Matrix([[1,-3], [1,1]]))
            2*x^2*y^2 - x^-2*y^2 + x^-3*y
            sage: F = GF(2)
            sage: p.toric_coordinate_change(Matrix([[1,-3], [1,1]]),
            ....:                           new_ring=L.change_ring(F))
            x^-2*y^2 + x^-3*y"""
    def toric_substitute(self, v, v1, a, h=..., new_ring=...) -> Any:
        """LaurentPolynomial_mpair.toric_substitute(self, v, v1, a, h=None, new_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1927)

        Perform a single-variable substitution up to a toric coordinate change.

        The optional argument ``h`` is a map to be applied to coefficients.

        EXAMPLES::

            sage: L.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: p = x + y
            sage: p.toric_substitute((2,3), (-1,1), 2)
            1/2*x^3*y^3 + 2*x^-2*y^-2
            sage: F = GF(5)
            sage: p.toric_substitute((2,3), (-1,1), 2, new_ring=L.change_ring(F))
            3*x^3*y^3 + 2*x^-2*y^-2

        TESTS:

        Tests for :issue:`30331`::

            sage: L.<x,y> = LaurentPolynomialRing(QQ, 2)
            sage: p = x + y
            sage: F.<z> = CyclotomicField(3)                                            # needs sage.rings.number_field
            sage: p.toric_substitute((2,3), (-1,1), z, new_ring=L.change_ring(F))       # needs sage.rings.number_field
            (-z - 1)*x^3*y^3 + z*x^-2*y^-2

            sage: P.<x> = LaurentPolynomialRing(QQ, 1)
            sage: u = x - 1
            sage: v = u.toric_substitute((-1,), (-1,), 1)
            sage: v.is_zero()
            True"""
    @overload
    def univariate_polynomial(self, R=...) -> Any:
        """LaurentPolynomial_mpair.univariate_polynomial(self, R=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1610)

        Return a univariate polynomial associated to this
        multivariate polynomial.

        INPUT:

        - ``R`` -- (default: ``None``) a univariate Laurent polynomial ring

        If this polynomial is not in at most one variable, then a
        :exc:`ValueError` exception is raised.  The new polynomial is over
        the same base ring as the given :class:`LaurentPolynomial` and in the
        variable ``x`` if no ring ``R`` is provided.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(ZZ)
            sage: f = 3*x^2 - 2*y^-1 + 7*x^2*y^2 + 5
            sage: f.univariate_polynomial()
            Traceback (most recent call last):
            ...
            TypeError: polynomial must involve at most one variable
            sage: g = f(10, y); g
            700*y^2 + 305 - 2*y^-1
            sage: h = g.univariate_polynomial(); h
            -2*y^-1 + 305 + 700*y^2
            sage: h.parent()
            Univariate Laurent Polynomial Ring in y over Integer Ring
            sage: g.univariate_polynomial(LaurentPolynomialRing(QQ,'z'))
            -2*z^-1 + 305 + 700*z^2

        Here's an example with a constant multivariate polynomial::

            sage: g = R(1)
            sage: h = g.univariate_polynomial(); h
            1
            sage: h.parent()
            Univariate Laurent Polynomial Ring in x over Integer Ring"""
    @overload
    def univariate_polynomial(self) -> Any:
        """LaurentPolynomial_mpair.univariate_polynomial(self, R=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1610)

        Return a univariate polynomial associated to this
        multivariate polynomial.

        INPUT:

        - ``R`` -- (default: ``None``) a univariate Laurent polynomial ring

        If this polynomial is not in at most one variable, then a
        :exc:`ValueError` exception is raised.  The new polynomial is over
        the same base ring as the given :class:`LaurentPolynomial` and in the
        variable ``x`` if no ring ``R`` is provided.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(ZZ)
            sage: f = 3*x^2 - 2*y^-1 + 7*x^2*y^2 + 5
            sage: f.univariate_polynomial()
            Traceback (most recent call last):
            ...
            TypeError: polynomial must involve at most one variable
            sage: g = f(10, y); g
            700*y^2 + 305 - 2*y^-1
            sage: h = g.univariate_polynomial(); h
            -2*y^-1 + 305 + 700*y^2
            sage: h.parent()
            Univariate Laurent Polynomial Ring in y over Integer Ring
            sage: g.univariate_polynomial(LaurentPolynomialRing(QQ,'z'))
            -2*z^-1 + 305 + 700*z^2

        Here's an example with a constant multivariate polynomial::

            sage: g = R(1)
            sage: h = g.univariate_polynomial(); h
            1
            sage: h.parent()
            Univariate Laurent Polynomial Ring in x over Integer Ring"""
    @overload
    def univariate_polynomial(self) -> Any:
        """LaurentPolynomial_mpair.univariate_polynomial(self, R=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1610)

        Return a univariate polynomial associated to this
        multivariate polynomial.

        INPUT:

        - ``R`` -- (default: ``None``) a univariate Laurent polynomial ring

        If this polynomial is not in at most one variable, then a
        :exc:`ValueError` exception is raised.  The new polynomial is over
        the same base ring as the given :class:`LaurentPolynomial` and in the
        variable ``x`` if no ring ``R`` is provided.

        EXAMPLES::

            sage: R.<x, y> = LaurentPolynomialRing(ZZ)
            sage: f = 3*x^2 - 2*y^-1 + 7*x^2*y^2 + 5
            sage: f.univariate_polynomial()
            Traceback (most recent call last):
            ...
            TypeError: polynomial must involve at most one variable
            sage: g = f(10, y); g
            700*y^2 + 305 - 2*y^-1
            sage: h = g.univariate_polynomial(); h
            -2*y^-1 + 305 + 700*y^2
            sage: h.parent()
            Univariate Laurent Polynomial Ring in y over Integer Ring
            sage: g.univariate_polynomial(LaurentPolynomialRing(QQ,'z'))
            -2*z^-1 + 305 + 700*z^2

        Here's an example with a constant multivariate polynomial::

            sage: g = R(1)
            sage: h = g.univariate_polynomial(); h
            1
            sage: h.parent()
            Univariate Laurent Polynomial Ring in x over Integer Ring"""
    def valuation(self, x=...) -> Any:
        """LaurentPolynomial_mpair.valuation(self, x=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1233)

        Return the valuation of ``self``.

        If ``x`` is ``None``, the returned valuation is the minimal total degree
        of the monomials occurring in ``self``. Geometrically, this is the order
        of vanishing of ``self`` at the generic point of the blow-up of the
        point `(0,0,\\ldots,0)`.

        If ``x`` is not ``None``, then it must be a generator. In that case, the
        minimum degree of that generator occurring in ``self`` is returned.
        Geometrically, this is the order of vanishing of ``self`` at the generic
        point of the curve `x = 0`.

        INPUT:

        - ``x`` -- (optional) a generator; if given, return the valuation
          with respect to this generator

        EXAMPLES::

            sage: R.<x,y> = LaurentPolynomialRing(ZZ)
            sage: f = 2*x^2*y^-3 - 13*x^-1*y^-3 + 2*x^2*y^-5 - 2*x^-3*y^2
            sage: f.valuation()
            -4
            sage: f.valuation(x)
            -3
            sage: f.valuation(y)
            -5
            sage: R.zero().valuation()
            +Infinity

        TESTS:

        If supplied, ``x`` must be a generator::

            sage: R.<x,y> = LaurentPolynomialRing(ZZ)
            sage: f = 1 + x + x^2*y^-1
            sage: f.valuation(1)
            Traceback (most recent call last):
            ...
            TypeError: 1 is not a generator of parent"""
    @overload
    def variables(self, sort=...) -> Any:
        """LaurentPolynomial_mpair.variables(self, sort=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 779)

        Return a tuple of all variables occurring in ``self``.

        INPUT:

        - ``sort`` -- specifies whether the indices shall be sorted

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.variables()
            (z, y, x)
            sage: f.variables(sort=False) #random
            (y, z, x)"""
    @overload
    def variables(self) -> Any:
        """LaurentPolynomial_mpair.variables(self, sort=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 779)

        Return a tuple of all variables occurring in ``self``.

        INPUT:

        - ``sort`` -- specifies whether the indices shall be sorted

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.variables()
            (z, y, x)
            sage: f.variables(sort=False) #random
            (y, z, x)"""
    @overload
    def variables(self, sort=...) -> Any:
        """LaurentPolynomial_mpair.variables(self, sort=True)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 779)

        Return a tuple of all variables occurring in ``self``.

        INPUT:

        - ``sort`` -- specifies whether the indices shall be sorted

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = 4*x^7*z^-1 + 3*x^3*y + 2*x^4*z^-2 + x^6*y^-7
            sage: f.variables()
            (z, y, x)
            sage: f.variables(sort=False) #random
            (y, z, x)"""
    def __call__(self, *x, **kwds) -> Any:
        """LaurentPolynomial_mpair.__call__(self, *x, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 1347)

        Compute value of ``self`` at ``x``.

        EXAMPLES::

            sage: L.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = x + 2*y + 3*z
            sage: f(1,1,1)
            6
            sage: f = x^-1 + y + z
            sage: f(0,1,1)
            Traceback (most recent call last):
            ...
            ZeroDivisionError

        TESTS::

            sage: f = x + 2*y + 3*z
            sage: f(2)
            Traceback (most recent call last):
            ...
            TypeError: number of arguments does not match the number of generators in parent
            sage: f(2,0)
            Traceback (most recent call last):
            ...
            TypeError: number of arguments does not match the number of generators in parent
            sage: f( (1,1,1) )
            6"""
    def __getitem__(self, n) -> Any:
        """LaurentPolynomial_mpair.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 504)

        Return the coefficient of `x^n = x_1^{n_1} \\cdots x_k^{n_k}` where
        `n` is a tuple of length `k` and `k` is the number of variables.

        If the number of inputs is not equal to the number of variables, this
        raises a :exc:`TypeError`.

        EXAMPLES::

            sage: P.<x,y,z> = LaurentPolynomialRing(QQ)
            sage: f = (y^2 - x^9 - 7*x*y^3 + 5*x*y)*x^-3 + x*z; f
            -x^6 + x*z - 7*x^-2*y^3 + 5*x^-2*y + x^-3*y^2
            sage: f[6,0,0]
            -1
            sage: f[-2,3,0]
            -7
            sage: f[-1,4,2]
            0
            sage: f[1,0,1]
            1
            sage: f[6]
            Traceback (most recent call last):
            ...
            TypeError: must have exactly 3 inputs
            sage: f[6,0]
            Traceback (most recent call last):
            ...
            TypeError: must have exactly 3 inputs
            sage: f[6,0,0,0]
            Traceback (most recent call last):
            ...
            TypeError: must have exactly 3 inputs"""
    def __hash__(self) -> Any:
        """LaurentPolynomial_mpair.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 146)

        TESTS:

        Test that the hash is non-constant (see also :issue:`27914`)::

            sage: L.<w,z> = LaurentPolynomialRing(QQ)
            sage: len({hash(w^i*z^j) for i in [-2..2] for j in [-2..2]})
            25

        Check that :issue:`20490` is fixed::

            sage: R.<a,b> = LaurentPolynomialRing(ZZ)
            sage: p = a*~a
            sage: p._fraction_pair()
            (a, a)
            sage: p == R.one()
            True
            sage: hash(p)
            1

        Check that :issue:`23864` is fixed (compatibility with integers, rationals
        and polynomial rings)::

            sage: L = LaurentPolynomialRing(QQ, 'x0,x1,x2')
            sage: hash(L.zero())
            0
            sage: hash(L.one())
            1
            sage: hash(-L.one())
            -2
            sage: hash(L(1/2)) == hash(1/2)
            True

            sage: R = PolynomialRing(QQ, 'x0,x1,x2')
            sage: x0,x1,x2 = R.gens()
            sage: hash(x0) == hash(L(x0))
            True
            sage: hash(1 - 7*x0 + x1*x2) == hash(L(1 - 7*x0 + x1*x2))
            True

        Check that :issue:`27914` is fixed::

            sage: L.<w,z> = LaurentPolynomialRing(QQ)
            sage: Lw = LaurentPolynomialRing(QQ, 'w')
            sage: Lz = LaurentPolynomialRing(QQ, 'z')
            sage: all(hash(w^k) == hash(Lw(w^k))
            ....:     and hash(z^k) == hash(Lz(z^k)) for k in (-5..5))
            True
            sage: p = w^-1 + 2 + w
            sage: hash(p) == hash(Lw(p))
            True"""
    def __invert__(self) -> Any:
        """LaurentPolynomial_mpair.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 427)

        Return the inverse of ``self``.

        This treats monomials specially so they remain Laurent
        polynomials; the inverse of any other polynomial is an element
        of the rational function field.

        TESTS::

            sage: L.<x,y> = LaurentPolynomialRing(ZZ)
            sage: f = ~x
            sage: parent(f)
            Multivariate Laurent Polynomial Ring in x, y over Integer Ring
            sage: parent(f.coefficients()[0]) is parent(f).base_ring()
            True
            sage: g = ~(2*x)
            sage: parent(g)
            Multivariate Laurent Polynomial Ring in x, y over Rational Field
            sage: parent(g.coefficients()[0]) is parent(g).base_ring()
            True"""
    def __iter__(self) -> Any:
        """LaurentPolynomial_mpair.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 551)

        Iterate through all terms by returning a list of the coefficient and
        the corresponding monomial.

        EXAMPLES::

            sage: P.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = (y^2 - x^9 - 7*x*y^3 + 5*x*y)*x^-3
            sage: sorted(f) # indirect doctest
            [(-7, x^-2*y^3), (-1, x^6), (1, x^-3*y^2), (5, x^-2*y)]"""
    def __pow__(self, LaurentPolynomial_mpairself, n, mod) -> Any:
        """LaurentPolynomial_mpair.__pow__(LaurentPolynomial_mpair self, n, mod)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 463)

        EXAMPLES::

            sage: L.<x,y> = LaurentPolynomialRing(QQ)
            sage: f = x + y
            sage: f^2
            x^2 + 2*x*y + y^2
            sage: f^(-1)
            1/(x + y)

        TESTS:

        Check that :issue:`2952` is fixed::

            sage: R.<q> = QQ[]
            sage: L.<x,y,z> = LaurentPolynomialRing(R)
            sage: f = (x+y+z^-1)^2
            sage: f.substitute(z=1)
            x^2 + 2*x*y + y^2 + 2*x + 2*y + 1

        Check that using third argument raises an error::

            sage: L.<x,y,z> = LaurentPolynomialRing(R)
            sage: pow(x + y + z, 2, x)
            Traceback (most recent call last):
            ...
            NotImplementedError: pow() with a modulus is not implemented for this ring"""
    def __reduce__(self) -> Any:
        """LaurentPolynomial_mpair.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial_mpair.pyx (starting at line 132)

        TESTS::

            sage: R = LaurentPolynomialRing(QQ, 2, 'x')
            sage: R.<x1,x2> = LaurentPolynomialRing(QQ)
            sage: loads(dumps(x1)) == x1 # indirect doctest
            True
            sage: z = x1/x2
            sage: loads(dumps(z)) == z
            True"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
