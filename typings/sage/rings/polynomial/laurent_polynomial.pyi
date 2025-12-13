import sage.structure.element
from sage.misc.derivative import multi_derivative as multi_derivative
from sage.rings.infinity import minus_infinity as minus_infinity
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic as PolynomialRing_generic
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.factorization import Factorization as Factorization
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class LaurentPolynomial(sage.structure.element.CommutativeAlgebraElement):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 21)

        Base class for Laurent polynomials.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def change_ring(self, R) -> Any:
        """LaurentPolynomial.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 169)

        Return a copy of this Laurent polynomial, with coefficients in ``R``.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: a = x^2 + 3*x^3 + 5*x^-1
            sage: a.change_ring(GF(3))
            2*x^-1 + x^2

        Check that :issue:`22277` is fixed::

            sage: # needs sage.modules
            sage: R.<x, y> = LaurentPolynomialRing(QQ)
            sage: a = 2*x^2 + 3*x^3 + 4*x^-1
            sage: a.change_ring(GF(3))
            -x^2 + x^-1"""
    def dict(self, *args, **kwargs):
        """LaurentPolynomial.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 221)

        Abstract ``dict`` method.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
            sage: LaurentPolynomial.monomial_coefficients(x)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def hamming_weight(self) -> Any:
        """LaurentPolynomial.hamming_weight(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 205)

        Return the hamming weight of ``self``.

        The hamming weight is number of nonzero coefficients and
        also known as the weight or sparsity.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: f = x^3 - 1
            sage: f.hamming_weight()
            2"""
    @overload
    def hamming_weight(self) -> Any:
        """LaurentPolynomial.hamming_weight(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 205)

        Return the hamming weight of ``self``.

        The hamming weight is number of nonzero coefficients and
        also known as the weight or sparsity.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: f = x^3 - 1
            sage: f.hamming_weight()
            2"""
    @overload
    def map_coefficients(self, f, new_base_ring=...) -> Any:
        """LaurentPolynomial.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 238)

        Apply ``f`` to the coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        polynomial will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behavior.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(9)
            sage: R.<x> = LaurentPolynomialRing(k)
            sage: f = x*a + a
            sage: f.map_coefficients(lambda a: a + 1)
            (a + 1) + (a + 1)*x
            sage: R.<x,y> = LaurentPolynomialRing(k, 2)                                 # needs sage.modules
            sage: f = x*a + 2*x^3*y*a + a                                               # needs sage.modules
            sage: f.map_coefficients(lambda a: a + 1)                                   # needs sage.modules
            (2*a + 1)*x^3*y + (a + 1)*x + a + 1

        Examples with different base ring::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: R.<r> = GF(9); S.<s> = GF(81)
            sage: h = Hom(R, S)[0]; h
            Ring morphism:
              From: Finite Field in r of size 3^2
              To:   Finite Field in s of size 3^4
              Defn: r |--> 2*s^3 + 2*s^2 + 1
            sage: T.<X,Y> = LaurentPolynomialRing(R, 2)
            sage: f = r*X + Y
            sage: g = f.map_coefficients(h); g
            (2*s^3 + 2*s^2 + 1)*X + Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in s of size 3^4
            sage: h = lambda x: x.trace()
            sage: g = f.map_coefficients(h); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in r of size 3^2
            sage: g = f.map_coefficients(h, new_base_ring=GF(3)); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y over Finite Field of size 3"""
    @overload
    def map_coefficients(self, lambdaa) -> Any:
        """LaurentPolynomial.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 238)

        Apply ``f`` to the coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        polynomial will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behavior.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(9)
            sage: R.<x> = LaurentPolynomialRing(k)
            sage: f = x*a + a
            sage: f.map_coefficients(lambda a: a + 1)
            (a + 1) + (a + 1)*x
            sage: R.<x,y> = LaurentPolynomialRing(k, 2)                                 # needs sage.modules
            sage: f = x*a + 2*x^3*y*a + a                                               # needs sage.modules
            sage: f.map_coefficients(lambda a: a + 1)                                   # needs sage.modules
            (2*a + 1)*x^3*y + (a + 1)*x + a + 1

        Examples with different base ring::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: R.<r> = GF(9); S.<s> = GF(81)
            sage: h = Hom(R, S)[0]; h
            Ring morphism:
              From: Finite Field in r of size 3^2
              To:   Finite Field in s of size 3^4
              Defn: r |--> 2*s^3 + 2*s^2 + 1
            sage: T.<X,Y> = LaurentPolynomialRing(R, 2)
            sage: f = r*X + Y
            sage: g = f.map_coefficients(h); g
            (2*s^3 + 2*s^2 + 1)*X + Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in s of size 3^4
            sage: h = lambda x: x.trace()
            sage: g = f.map_coefficients(h); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in r of size 3^2
            sage: g = f.map_coefficients(h, new_base_ring=GF(3)); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y over Finite Field of size 3"""
    @overload
    def map_coefficients(self, lambdaa) -> Any:
        """LaurentPolynomial.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 238)

        Apply ``f`` to the coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        polynomial will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behavior.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(9)
            sage: R.<x> = LaurentPolynomialRing(k)
            sage: f = x*a + a
            sage: f.map_coefficients(lambda a: a + 1)
            (a + 1) + (a + 1)*x
            sage: R.<x,y> = LaurentPolynomialRing(k, 2)                                 # needs sage.modules
            sage: f = x*a + 2*x^3*y*a + a                                               # needs sage.modules
            sage: f.map_coefficients(lambda a: a + 1)                                   # needs sage.modules
            (2*a + 1)*x^3*y + (a + 1)*x + a + 1

        Examples with different base ring::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: R.<r> = GF(9); S.<s> = GF(81)
            sage: h = Hom(R, S)[0]; h
            Ring morphism:
              From: Finite Field in r of size 3^2
              To:   Finite Field in s of size 3^4
              Defn: r |--> 2*s^3 + 2*s^2 + 1
            sage: T.<X,Y> = LaurentPolynomialRing(R, 2)
            sage: f = r*X + Y
            sage: g = f.map_coefficients(h); g
            (2*s^3 + 2*s^2 + 1)*X + Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in s of size 3^4
            sage: h = lambda x: x.trace()
            sage: g = f.map_coefficients(h); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in r of size 3^2
            sage: g = f.map_coefficients(h, new_base_ring=GF(3)); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y over Finite Field of size 3"""
    @overload
    def map_coefficients(self, h) -> Any:
        """LaurentPolynomial.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 238)

        Apply ``f`` to the coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        polynomial will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behavior.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(9)
            sage: R.<x> = LaurentPolynomialRing(k)
            sage: f = x*a + a
            sage: f.map_coefficients(lambda a: a + 1)
            (a + 1) + (a + 1)*x
            sage: R.<x,y> = LaurentPolynomialRing(k, 2)                                 # needs sage.modules
            sage: f = x*a + 2*x^3*y*a + a                                               # needs sage.modules
            sage: f.map_coefficients(lambda a: a + 1)                                   # needs sage.modules
            (2*a + 1)*x^3*y + (a + 1)*x + a + 1

        Examples with different base ring::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: R.<r> = GF(9); S.<s> = GF(81)
            sage: h = Hom(R, S)[0]; h
            Ring morphism:
              From: Finite Field in r of size 3^2
              To:   Finite Field in s of size 3^4
              Defn: r |--> 2*s^3 + 2*s^2 + 1
            sage: T.<X,Y> = LaurentPolynomialRing(R, 2)
            sage: f = r*X + Y
            sage: g = f.map_coefficients(h); g
            (2*s^3 + 2*s^2 + 1)*X + Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in s of size 3^4
            sage: h = lambda x: x.trace()
            sage: g = f.map_coefficients(h); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in r of size 3^2
            sage: g = f.map_coefficients(h, new_base_ring=GF(3)); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y over Finite Field of size 3"""
    @overload
    def map_coefficients(self, h) -> Any:
        """LaurentPolynomial.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 238)

        Apply ``f`` to the coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        polynomial will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behavior.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(9)
            sage: R.<x> = LaurentPolynomialRing(k)
            sage: f = x*a + a
            sage: f.map_coefficients(lambda a: a + 1)
            (a + 1) + (a + 1)*x
            sage: R.<x,y> = LaurentPolynomialRing(k, 2)                                 # needs sage.modules
            sage: f = x*a + 2*x^3*y*a + a                                               # needs sage.modules
            sage: f.map_coefficients(lambda a: a + 1)                                   # needs sage.modules
            (2*a + 1)*x^3*y + (a + 1)*x + a + 1

        Examples with different base ring::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: R.<r> = GF(9); S.<s> = GF(81)
            sage: h = Hom(R, S)[0]; h
            Ring morphism:
              From: Finite Field in r of size 3^2
              To:   Finite Field in s of size 3^4
              Defn: r |--> 2*s^3 + 2*s^2 + 1
            sage: T.<X,Y> = LaurentPolynomialRing(R, 2)
            sage: f = r*X + Y
            sage: g = f.map_coefficients(h); g
            (2*s^3 + 2*s^2 + 1)*X + Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in s of size 3^4
            sage: h = lambda x: x.trace()
            sage: g = f.map_coefficients(h); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in r of size 3^2
            sage: g = f.map_coefficients(h, new_base_ring=GF(3)); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y over Finite Field of size 3"""
    @overload
    def map_coefficients(self, h, new_base_ring=...) -> Any:
        """LaurentPolynomial.map_coefficients(self, f, new_base_ring=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 238)

        Apply ``f`` to the coefficients of ``self``.

        If ``f`` is a :class:`sage.categories.map.Map`, then the resulting
        polynomial will be defined over the codomain of ``f``. Otherwise, the
        resulting polynomial will be over the same ring as ``self``. Set
        ``new_base_ring`` to override this behavior.

        INPUT:

        - ``f`` -- a callable that will be applied to the coefficients of ``self``

        - ``new_base_ring`` -- (optional) if given, the resulting polynomial
          will be defined over this ring

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k.<a> = GF(9)
            sage: R.<x> = LaurentPolynomialRing(k)
            sage: f = x*a + a
            sage: f.map_coefficients(lambda a: a + 1)
            (a + 1) + (a + 1)*x
            sage: R.<x,y> = LaurentPolynomialRing(k, 2)                                 # needs sage.modules
            sage: f = x*a + 2*x^3*y*a + a                                               # needs sage.modules
            sage: f.map_coefficients(lambda a: a + 1)                                   # needs sage.modules
            (2*a + 1)*x^3*y + (a + 1)*x + a + 1

        Examples with different base ring::

            sage: # needs sage.modules sage.rings.finite_rings
            sage: R.<r> = GF(9); S.<s> = GF(81)
            sage: h = Hom(R, S)[0]; h
            Ring morphism:
              From: Finite Field in r of size 3^2
              To:   Finite Field in s of size 3^4
              Defn: r |--> 2*s^3 + 2*s^2 + 1
            sage: T.<X,Y> = LaurentPolynomialRing(R, 2)
            sage: f = r*X + Y
            sage: g = f.map_coefficients(h); g
            (2*s^3 + 2*s^2 + 1)*X + Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in s of size 3^4
            sage: h = lambda x: x.trace()
            sage: g = f.map_coefficients(h); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y
             over Finite Field in r of size 3^2
            sage: g = f.map_coefficients(h, new_base_ring=GF(3)); g
            X - Y
            sage: g.parent()
            Multivariate Laurent Polynomial Ring in X, Y over Finite Field of size 3"""
    @overload
    def monomial_coefficients(self) -> dict:
        """LaurentPolynomial.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 221)

        Abstract ``dict`` method.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
            sage: LaurentPolynomial.monomial_coefficients(x)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def monomial_coefficients(self, x) -> Any:
        """LaurentPolynomial.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 221)

        Abstract ``dict`` method.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
            sage: LaurentPolynomial.monomial_coefficients(x)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def number_of_terms(self) -> long:
        """LaurentPolynomial.number_of_terms(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 190)

        Abstract method for number of terms

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
            sage: LaurentPolynomial.number_of_terms(x)
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def number_of_terms(self, x) -> Any:
        """LaurentPolynomial.number_of_terms(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 190)

        Abstract method for number of terms

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
            sage: LaurentPolynomial.number_of_terms(x)
            Traceback (most recent call last):
            ...
            NotImplementedError"""

class LaurentPolynomial_univariate(LaurentPolynomial):
    """LaurentPolynomial_univariate(parent, f, n=0)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 303)

    A univariate Laurent polynomial in the form of `t^n \\cdot f`
    where `f` is a polynomial in `t`.

    INPUT:

    - ``parent`` -- a Laurent polynomial ring

    - ``f`` -- a polynomial (or something that can be coerced to one)

    - ``n`` -- integer (default: 0)

    AUTHORS:

    - Tom Boothby (2011) copied this class almost verbatim from
      ``laurent_series_ring_element.pyx``, so most of the credit goes to
      William Stein, David Joyner, and Robert Bradshaw
    - Travis Scrimshaw (09-2013): Cleaned-up and added a few extra methods"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, f, n=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 324)

                Create the Laurent polynomial `t^n \\cdot f`.

                EXAMPLES::

                    sage: R.<q> = LaurentPolynomialRing(ZZ)
                    sage: R([1,2,3])
                    1 + 2*q + 3*q^2
                    sage: TestSuite(q^-3 + 3*q + 2).run()

                ::

                    sage: # needs sage.rings.padics
                    sage: S.<s> = LaurentPolynomialRing(GF(5))
                    sage: T.<t> = PolynomialRing(pAdicRing(5))
                    sage: S(t)
                    s
                    sage: parent(S(t))
                    Univariate Laurent Polynomial Ring in s over Finite Field of size 5
                    sage: parent(S(t)[1])
                    Finite Field of size 5

                ::

                    sage: R({})
                    0
        """
    @overload
    def coefficients(self) -> Any:
        """LaurentPolynomial_univariate.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 867)

        Return the nonzero coefficients of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3
            sage: f.coefficients()
            [-5, 1, 1, -10/3]"""
    @overload
    def coefficients(self) -> Any:
        """LaurentPolynomial_univariate.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 867)

        Return the nonzero coefficients of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3
            sage: f.coefficients()
            [-5, 1, 1, -10/3]"""
    @overload
    def constant_coefficient(self) -> Any:
        """LaurentPolynomial_univariate.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2118)

        Return the coefficient of the constant term of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = 3*t^-2 - t^-1 + 3 + t^2
            sage: f.constant_coefficient()
            3
            sage: g = -2*t^-2 + t^-1 + 3*t
            sage: g.constant_coefficient()
            0"""
    @overload
    def constant_coefficient(self) -> Any:
        """LaurentPolynomial_univariate.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2118)

        Return the coefficient of the constant term of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = 3*t^-2 - t^-1 + 3 + t^2
            sage: f.constant_coefficient()
            3
            sage: g = -2*t^-2 + t^-1 + 3*t
            sage: g.constant_coefficient()
            0"""
    @overload
    def constant_coefficient(self) -> Any:
        """LaurentPolynomial_univariate.constant_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2118)

        Return the coefficient of the constant term of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = 3*t^-2 - t^-1 + 3 + t^2
            sage: f.constant_coefficient()
            3
            sage: g = -2*t^-2 + t^-1 + 3*t
            sage: g.constant_coefficient()
            0"""
    @overload
    def degree(self) -> Any:
        """LaurentPolynomial_univariate.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1026)

        Return the degree of ``self``.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: g = x^2 - x^4
            sage: g.degree()
            4
            sage: g = -10/x^5 + x^2 - x^7
            sage: g.degree()
            7

        The zero polynomial is defined to have degree `-\\infty`::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: R.zero().degree()
            -Infinity"""
    @overload
    def degree(self) -> Any:
        """LaurentPolynomial_univariate.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1026)

        Return the degree of ``self``.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: g = x^2 - x^4
            sage: g.degree()
            4
            sage: g = -10/x^5 + x^2 - x^7
            sage: g.degree()
            7

        The zero polynomial is defined to have degree `-\\infty`::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: R.zero().degree()
            -Infinity"""
    @overload
    def degree(self) -> Any:
        """LaurentPolynomial_univariate.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1026)

        Return the degree of ``self``.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: g = x^2 - x^4
            sage: g.degree()
            4
            sage: g = -10/x^5 + x^2 - x^7
            sage: g.degree()
            7

        The zero polynomial is defined to have degree `-\\infty`::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: R.zero().degree()
            -Infinity"""
    @overload
    def derivative(self, *args) -> Any:
        """LaurentPolynomial_univariate.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1851)

        The formal derivative of this Laurent polynomial, with respect
        to variables supplied in args.

        Multiple variables and iteration counts may be supplied. See
        documentation for the global :func:`derivative` function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentPolynomialRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x"""
    @overload
    def derivative(self) -> Any:
        """LaurentPolynomial_univariate.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1851)

        The formal derivative of this Laurent polynomial, with respect
        to variables supplied in args.

        Multiple variables and iteration counts may be supplied. See
        documentation for the global :func:`derivative` function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentPolynomialRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x"""
    @overload
    def derivative(self, x) -> Any:
        """LaurentPolynomial_univariate.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1851)

        The formal derivative of this Laurent polynomial, with respect
        to variables supplied in args.

        Multiple variables and iteration counts may be supplied. See
        documentation for the global :func:`derivative` function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentPolynomialRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x"""
    @overload
    def derivative(self) -> Any:
        """LaurentPolynomial_univariate.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1851)

        The formal derivative of this Laurent polynomial, with respect
        to variables supplied in args.

        Multiple variables and iteration counts may be supplied. See
        documentation for the global :func:`derivative` function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentPolynomialRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x"""
    @overload
    def derivative(self, x) -> Any:
        """LaurentPolynomial_univariate.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1851)

        The formal derivative of this Laurent polynomial, with respect
        to variables supplied in args.

        Multiple variables and iteration counts may be supplied. See
        documentation for the global :func:`derivative` function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentPolynomialRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x"""
    @overload
    def derivative(self, t) -> Any:
        """LaurentPolynomial_univariate.derivative(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1851)

        The formal derivative of this Laurent polynomial, with respect
        to variables supplied in args.

        Multiple variables and iteration counts may be supplied. See
        documentation for the global :func:`derivative` function for more
        details.

        .. SEEALSO::

           :meth:`_derivative`

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: g = 1/x^10 - x + x^2 - x^4
            sage: g.derivative()
            -10*x^-11 - 1 + 2*x - 4*x^3
            sage: g.derivative(x)
            -10*x^-11 - 1 + 2*x - 4*x^3

        ::

            sage: R.<t> = PolynomialRing(ZZ)
            sage: S.<x> = LaurentPolynomialRing(R)
            sage: f = 2*t/x + (3*t^2 + 6*t)*x
            sage: f.derivative()
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(x)
            -2*t*x^-2 + (3*t^2 + 6*t)
            sage: f.derivative(t)
            2*x^-1 + (6*t + 6)*x"""
    def dict(self) -> Any:
        """LaurentPolynomial_univariate.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 844)

        Return a dictionary representing ``self``.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: Q.<t> = LaurentPolynomialRing(R)
            sage: f = (x^3 + y/t^3)^3 + t^2; f
            y^3*t^-9 + 3*x^3*y^2*t^-6 + 3*x^6*y*t^-3 + x^9 + t^2
            sage: f.monomial_coefficients()
            {-9: y^3, -6: 3*x^3*y^2, -3: 3*x^6*y, 0: x^9, 2: 1}

        ``dict`` is an alias::

            sage: f.dict()
            {-9: y^3, -6: 3*x^3*y^2, -3: 3*x^6*y, 0: x^9, 2: 1}"""
    @overload
    def divides(self, other) -> Any:
        """LaurentPolynomial_univariate.divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2156)

        Return ``True`` if ``self`` divides ``other``.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: (2*x**-1 + 1).divides(4*x**-2 - 1)
            True
            sage: (2*x + 1).divides(4*x**2 + 1)
            False
            sage: (2*x + x**-1).divides(R(0))
            True
            sage: R(0).divides(2*x ** -1 + 1)
            False
            sage: R(0).divides(R(0))
            True
            sage: R.<x> = LaurentPolynomialRing(Zmod(6))
            sage: p = 4*x + 3*x^-1
            sage: q = 5*x^2 + x + 2*x^-2
            sage: p.divides(q)
            False

            sage: R.<x,y> = GF(2)[]
            sage: S.<z> = LaurentPolynomialRing(R)
            sage: p = (x+y+1) * z**-1 + x*y
            sage: q = (y^2-x^2) * z**-2 + z + x-y
            sage: p.divides(q), p.divides(p*q)                                          # needs sage.libs.singular
            (False, True)"""
    @overload
    def divides(self, q) -> Any:
        """LaurentPolynomial_univariate.divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2156)

        Return ``True`` if ``self`` divides ``other``.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: (2*x**-1 + 1).divides(4*x**-2 - 1)
            True
            sage: (2*x + 1).divides(4*x**2 + 1)
            False
            sage: (2*x + x**-1).divides(R(0))
            True
            sage: R(0).divides(2*x ** -1 + 1)
            False
            sage: R(0).divides(R(0))
            True
            sage: R.<x> = LaurentPolynomialRing(Zmod(6))
            sage: p = 4*x + 3*x^-1
            sage: q = 5*x^2 + x + 2*x^-2
            sage: p.divides(q)
            False

            sage: R.<x,y> = GF(2)[]
            sage: S.<z> = LaurentPolynomialRing(R)
            sage: p = (x+y+1) * z**-1 + x*y
            sage: q = (y^2-x^2) * z**-2 + z + x-y
            sage: p.divides(q), p.divides(p*q)                                          # needs sage.libs.singular
            (False, True)"""
    @overload
    def euclidean_degree(self) -> Any:
        """LaurentPolynomial_univariate.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1491)

        Return the degree of ``self`` as an element of an Euclidean domain.

        This is the Euclidean degree of the underlying polynomial.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: (x^-5 + x^2).euclidean_degree()
            7

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: (x^-5 + x^2).euclidean_degree()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def euclidean_degree(self) -> Any:
        """LaurentPolynomial_univariate.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1491)

        Return the degree of ``self`` as an element of an Euclidean domain.

        This is the Euclidean degree of the underlying polynomial.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: (x^-5 + x^2).euclidean_degree()
            7

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: (x^-5 + x^2).euclidean_degree()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def euclidean_degree(self) -> Any:
        """LaurentPolynomial_univariate.euclidean_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1491)

        Return the degree of ``self`` as an element of an Euclidean domain.

        This is the Euclidean degree of the underlying polynomial.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: (x^-5 + x^2).euclidean_degree()
            7

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: (x^-5 + x^2).euclidean_degree()
            Traceback (most recent call last):
            ...
            NotImplementedError"""
    @overload
    def exponents(self) -> Any:
        """LaurentPolynomial_univariate.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 880)

        Return the exponents appearing in ``self`` with nonzero coefficients.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3
            sage: f.exponents()
            [-2, 1, 2, 3]"""
    @overload
    def exponents(self) -> Any:
        """LaurentPolynomial_univariate.exponents(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 880)

        Return the exponents appearing in ``self`` with nonzero coefficients.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3
            sage: f.exponents()
            [-2, 1, 2, 3]"""
    @overload
    def factor(self) -> Any:
        """LaurentPolynomial_univariate.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2066)

        Return a Laurent monomial (the unit part of the factorization) and
        a factored polynomial.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(ZZ)
            sage: f = 4*t^-7 + 3*t^3 + 2*t^4 + t^-6
            sage: f.factor()                                                            # needs sage.libs.pari
            (t^-7) * (4 + t + 3*t^10 + 2*t^11)"""
    @overload
    def factor(self) -> Any:
        """LaurentPolynomial_univariate.factor(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2066)

        Return a Laurent monomial (the unit part of the factorization) and
        a factored polynomial.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(ZZ)
            sage: f = 4*t^-7 + 3*t^3 + 2*t^4 + t^-6
            sage: f.factor()                                                            # needs sage.libs.pari
            (t^-7) * (4 + t + 3*t^10 + 2*t^11)"""
    def gcd(self, right) -> Any:
        """LaurentPolynomial_univariate.gcd(self, right)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1467)

        Return the gcd of ``self`` with ``right`` where the common divisor
        ``d`` makes both ``self`` and ``right`` into polynomials with
        the lowest possible degree.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: t.gcd(2)
            1
            sage: gcd(t^-2 + 1, t^-4 + 3*t^-1)
            t^-4
            sage: gcd((t^-2 + t)*(t + t^-1), (t^5 + t^8)*(1 + t^-2))
            t^-3 + t^-1 + 1 + t^2"""
    @overload
    def integral(self) -> Any:
        """LaurentPolynomial_univariate.integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1959)

        The formal integral of this Laurent series with 0 constant term.

        EXAMPLES:

        The integral may or may not be defined if the base ring
        is not a field.

        ::

            sage: t = LaurentPolynomialRing(ZZ, 't').0
            sage: f = 2*t^-3 + 3*t^2
            sage: f.integral()
            -t^-2 + t^3

        ::

            sage: f = t^3
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: coefficients of integral cannot be coerced into the base ring

        The integral of `1/t` is `\\log(t)`, which is not given by a
        Laurent polynomial::

            sage: t = LaurentPolynomialRing(ZZ,'t').0
            sage: f = -1/t^3 - 31/t
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: the integral of is not a Laurent polynomial, since t^-1 has nonzero coefficient

        Another example with just one negative coefficient::

            sage: A.<t> = LaurentPolynomialRing(QQ)
            sage: f = -2*t^(-4)
            sage: f.integral()
            2/3*t^-3
            sage: f.integral().derivative() == f
            True"""
    @overload
    def integral(self) -> Any:
        """LaurentPolynomial_univariate.integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1959)

        The formal integral of this Laurent series with 0 constant term.

        EXAMPLES:

        The integral may or may not be defined if the base ring
        is not a field.

        ::

            sage: t = LaurentPolynomialRing(ZZ, 't').0
            sage: f = 2*t^-3 + 3*t^2
            sage: f.integral()
            -t^-2 + t^3

        ::

            sage: f = t^3
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: coefficients of integral cannot be coerced into the base ring

        The integral of `1/t` is `\\log(t)`, which is not given by a
        Laurent polynomial::

            sage: t = LaurentPolynomialRing(ZZ,'t').0
            sage: f = -1/t^3 - 31/t
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: the integral of is not a Laurent polynomial, since t^-1 has nonzero coefficient

        Another example with just one negative coefficient::

            sage: A.<t> = LaurentPolynomialRing(QQ)
            sage: f = -2*t^(-4)
            sage: f.integral()
            2/3*t^-3
            sage: f.integral().derivative() == f
            True"""
    @overload
    def integral(self) -> Any:
        """LaurentPolynomial_univariate.integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1959)

        The formal integral of this Laurent series with 0 constant term.

        EXAMPLES:

        The integral may or may not be defined if the base ring
        is not a field.

        ::

            sage: t = LaurentPolynomialRing(ZZ, 't').0
            sage: f = 2*t^-3 + 3*t^2
            sage: f.integral()
            -t^-2 + t^3

        ::

            sage: f = t^3
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: coefficients of integral cannot be coerced into the base ring

        The integral of `1/t` is `\\log(t)`, which is not given by a
        Laurent polynomial::

            sage: t = LaurentPolynomialRing(ZZ,'t').0
            sage: f = -1/t^3 - 31/t
            sage: f.integral()
            Traceback (most recent call last):
            ...
            ArithmeticError: the integral of is not a Laurent polynomial, since t^-1 has nonzero coefficient

        Another example with just one negative coefficient::

            sage: A.<t> = LaurentPolynomialRing(QQ)
            sage: f = -2*t^(-4)
            sage: f.integral()
            2/3*t^-3
            sage: f.integral().derivative() == f
            True"""
    def inverse_mod(self, a, m) -> Any:
        """LaurentPolynomial_univariate.inverse_mod(a, m)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1402)

        Invert the polynomial ``a`` with respect to ``m``, or raise a :exc:`ValueError`
        if no such inverse exists.

        The parameter ``m`` may be either a single polynomial or an ideal
        (for consistency with :meth:`inverse_mod` in other rings).

        ALGORITHM: Solve the system `as + mt = 1`, returning `s` as the inverse
        of `a` mod `m`.

        EXAMPLES::

            sage: S.<t> = LaurentPolynomialRing(QQ)
            sage: f = inverse_mod(t^-2 + 1, t^-3 + 1); f
            1/2*t^2 - 1/2*t^3 - 1/2*t^4
            sage: f * (t^-2 + 1) + (1/2*t^4 + 1/2*t^3) * (t^-3 + 1)
            1"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LaurentPolynomial_univariate.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1330)

        Return the inverse of ``self`` if a unit.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t^-2).inverse_of_unit()
            t^2
            sage: (t + 2).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: element is not a unit"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LaurentPolynomial_univariate.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1330)

        Return the inverse of ``self`` if a unit.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t^-2).inverse_of_unit()
            t^2
            sage: (t + 2).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: element is not a unit"""
    @overload
    def inverse_of_unit(self) -> Any:
        """LaurentPolynomial_univariate.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1330)

        Return the inverse of ``self`` if a unit.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t^-2).inverse_of_unit()
            t^2
            sage: (t + 2).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: element is not a unit"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_univariate.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1736)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: x.is_constant()
            False
            sage: R.one().is_constant()
            True
            sage: (x^-2).is_constant()
            False
            sage: (x^2).is_constant()
            False
            sage: (x^-2 + 2).is_constant()
            False
            sage: R(0).is_constant()
            True
            sage: R(42).is_constant()
            True
            sage: x.is_constant()
            False
            sage: (1/x).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_univariate.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1736)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: x.is_constant()
            False
            sage: R.one().is_constant()
            True
            sage: (x^-2).is_constant()
            False
            sage: (x^2).is_constant()
            False
            sage: (x^-2 + 2).is_constant()
            False
            sage: R(0).is_constant()
            True
            sage: R(42).is_constant()
            True
            sage: x.is_constant()
            False
            sage: (1/x).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_univariate.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1736)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: x.is_constant()
            False
            sage: R.one().is_constant()
            True
            sage: (x^-2).is_constant()
            False
            sage: (x^2).is_constant()
            False
            sage: (x^-2 + 2).is_constant()
            False
            sage: R(0).is_constant()
            True
            sage: R(42).is_constant()
            True
            sage: x.is_constant()
            False
            sage: (1/x).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_univariate.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1736)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: x.is_constant()
            False
            sage: R.one().is_constant()
            True
            sage: (x^-2).is_constant()
            False
            sage: (x^2).is_constant()
            False
            sage: (x^-2 + 2).is_constant()
            False
            sage: R(0).is_constant()
            True
            sage: R(42).is_constant()
            True
            sage: x.is_constant()
            False
            sage: (1/x).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_univariate.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1736)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: x.is_constant()
            False
            sage: R.one().is_constant()
            True
            sage: (x^-2).is_constant()
            False
            sage: (x^2).is_constant()
            False
            sage: (x^-2 + 2).is_constant()
            False
            sage: R(0).is_constant()
            True
            sage: R(42).is_constant()
            True
            sage: x.is_constant()
            False
            sage: (1/x).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_univariate.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1736)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: x.is_constant()
            False
            sage: R.one().is_constant()
            True
            sage: (x^-2).is_constant()
            False
            sage: (x^2).is_constant()
            False
            sage: (x^-2 + 2).is_constant()
            False
            sage: R(0).is_constant()
            True
            sage: R(42).is_constant()
            True
            sage: x.is_constant()
            False
            sage: (1/x).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_univariate.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1736)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: x.is_constant()
            False
            sage: R.one().is_constant()
            True
            sage: (x^-2).is_constant()
            False
            sage: (x^2).is_constant()
            False
            sage: (x^-2 + 2).is_constant()
            False
            sage: R(0).is_constant()
            True
            sage: R(42).is_constant()
            True
            sage: x.is_constant()
            False
            sage: (1/x).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_univariate.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1736)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: x.is_constant()
            False
            sage: R.one().is_constant()
            True
            sage: (x^-2).is_constant()
            False
            sage: (x^2).is_constant()
            False
            sage: (x^-2 + 2).is_constant()
            False
            sage: R(0).is_constant()
            True
            sage: R(42).is_constant()
            True
            sage: x.is_constant()
            False
            sage: (1/x).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_univariate.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1736)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: x.is_constant()
            False
            sage: R.one().is_constant()
            True
            sage: (x^-2).is_constant()
            False
            sage: (x^2).is_constant()
            False
            sage: (x^-2 + 2).is_constant()
            False
            sage: R(0).is_constant()
            True
            sage: R(42).is_constant()
            True
            sage: x.is_constant()
            False
            sage: (1/x).is_constant()
            False"""
    @overload
    def is_constant(self) -> Any:
        """LaurentPolynomial_univariate.is_constant(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1736)

        Return whether this Laurent polynomial is constant.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: x.is_constant()
            False
            sage: R.one().is_constant()
            True
            sage: (x^-2).is_constant()
            False
            sage: (x^2).is_constant()
            False
            sage: (x^-2 + 2).is_constant()
            False
            sage: R(0).is_constant()
            True
            sage: R(42).is_constant()
            True
            sage: x.is_constant()
            False
            sage: (1/x).is_constant()
            False"""
    @overload
    def is_monomial(self) -> Any:
        """LaurentPolynomial_univariate.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1118)

        Return ``True`` if ``self`` is a monomial; that is, if ``self``
        is `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentPolynomialRing(QQ)
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
        """LaurentPolynomial_univariate.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1118)

        Return ``True`` if ``self`` is a monomial; that is, if ``self``
        is `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentPolynomialRing(QQ)
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
        """LaurentPolynomial_univariate.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1118)

        Return ``True`` if ``self`` is a monomial; that is, if ``self``
        is `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentPolynomialRing(QQ)
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
        """LaurentPolynomial_univariate.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1118)

        Return ``True`` if ``self`` is a monomial; that is, if ``self``
        is `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentPolynomialRing(QQ)
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
        """LaurentPolynomial_univariate.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1118)

        Return ``True`` if ``self`` is a monomial; that is, if ``self``
        is `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentPolynomialRing(QQ)
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
        """LaurentPolynomial_univariate.is_monomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1118)

        Return ``True`` if ``self`` is a monomial; that is, if ``self``
        is `x^n` for some integer `n`.

        EXAMPLES::

            sage: k.<z> = LaurentPolynomialRing(QQ)
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
        """LaurentPolynomial_univariate.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1764)

        Return whether this Laurent polynomial is a square.

        If ``root`` is set to ``True`` then return a pair made of the
        boolean answer together with ``None`` or a square root.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)

            sage: R.one().is_square()
            True
            sage: R(2).is_square()
            False

            sage: t.is_square()
            False
            sage: (t**-2).is_square()
            True

        Usage of the ``root`` option::

            sage: p = (1 + t^-1 - 2*t^3)
            sage: p.is_square(root=True)
            (False, None)
            sage: (p**2).is_square(root=True)
            (True, -t^-1 - 1 + 2*t^3)

        The answer is dependent of the base ring::

            sage: # needs sage.rings.number_field
            sage: S.<u> = LaurentPolynomialRing(QQbar)
            sage: (2 + 4*t + 2*t^2).is_square()
            False
            sage: (2 + 4*u + 2*u^2).is_square()
            True

        TESTS::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t - t).is_square(True)
            (True, 0)

            sage: for _ in range(10):
            ....:     p = t ** randint(-15,15) * sum(QQ.random_element() * t**n for n in range(randint(5,10)))
            ....:     ans, r = (p**2).is_square(root=True)
            ....:     assert ans
            ....:     assert r*r == p*p"""
    @overload
    def is_square(self) -> Any:
        """LaurentPolynomial_univariate.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1764)

        Return whether this Laurent polynomial is a square.

        If ``root`` is set to ``True`` then return a pair made of the
        boolean answer together with ``None`` or a square root.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)

            sage: R.one().is_square()
            True
            sage: R(2).is_square()
            False

            sage: t.is_square()
            False
            sage: (t**-2).is_square()
            True

        Usage of the ``root`` option::

            sage: p = (1 + t^-1 - 2*t^3)
            sage: p.is_square(root=True)
            (False, None)
            sage: (p**2).is_square(root=True)
            (True, -t^-1 - 1 + 2*t^3)

        The answer is dependent of the base ring::

            sage: # needs sage.rings.number_field
            sage: S.<u> = LaurentPolynomialRing(QQbar)
            sage: (2 + 4*t + 2*t^2).is_square()
            False
            sage: (2 + 4*u + 2*u^2).is_square()
            True

        TESTS::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t - t).is_square(True)
            (True, 0)

            sage: for _ in range(10):
            ....:     p = t ** randint(-15,15) * sum(QQ.random_element() * t**n for n in range(randint(5,10)))
            ....:     ans, r = (p**2).is_square(root=True)
            ....:     assert ans
            ....:     assert r*r == p*p"""
    @overload
    def is_square(self) -> Any:
        """LaurentPolynomial_univariate.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1764)

        Return whether this Laurent polynomial is a square.

        If ``root`` is set to ``True`` then return a pair made of the
        boolean answer together with ``None`` or a square root.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)

            sage: R.one().is_square()
            True
            sage: R(2).is_square()
            False

            sage: t.is_square()
            False
            sage: (t**-2).is_square()
            True

        Usage of the ``root`` option::

            sage: p = (1 + t^-1 - 2*t^3)
            sage: p.is_square(root=True)
            (False, None)
            sage: (p**2).is_square(root=True)
            (True, -t^-1 - 1 + 2*t^3)

        The answer is dependent of the base ring::

            sage: # needs sage.rings.number_field
            sage: S.<u> = LaurentPolynomialRing(QQbar)
            sage: (2 + 4*t + 2*t^2).is_square()
            False
            sage: (2 + 4*u + 2*u^2).is_square()
            True

        TESTS::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t - t).is_square(True)
            (True, 0)

            sage: for _ in range(10):
            ....:     p = t ** randint(-15,15) * sum(QQ.random_element() * t**n for n in range(randint(5,10)))
            ....:     ans, r = (p**2).is_square(root=True)
            ....:     assert ans
            ....:     assert r*r == p*p"""
    @overload
    def is_square(self) -> Any:
        """LaurentPolynomial_univariate.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1764)

        Return whether this Laurent polynomial is a square.

        If ``root`` is set to ``True`` then return a pair made of the
        boolean answer together with ``None`` or a square root.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)

            sage: R.one().is_square()
            True
            sage: R(2).is_square()
            False

            sage: t.is_square()
            False
            sage: (t**-2).is_square()
            True

        Usage of the ``root`` option::

            sage: p = (1 + t^-1 - 2*t^3)
            sage: p.is_square(root=True)
            (False, None)
            sage: (p**2).is_square(root=True)
            (True, -t^-1 - 1 + 2*t^3)

        The answer is dependent of the base ring::

            sage: # needs sage.rings.number_field
            sage: S.<u> = LaurentPolynomialRing(QQbar)
            sage: (2 + 4*t + 2*t^2).is_square()
            False
            sage: (2 + 4*u + 2*u^2).is_square()
            True

        TESTS::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t - t).is_square(True)
            (True, 0)

            sage: for _ in range(10):
            ....:     p = t ** randint(-15,15) * sum(QQ.random_element() * t**n for n in range(randint(5,10)))
            ....:     ans, r = (p**2).is_square(root=True)
            ....:     assert ans
            ....:     assert r*r == p*p"""
    @overload
    def is_square(self) -> Any:
        """LaurentPolynomial_univariate.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1764)

        Return whether this Laurent polynomial is a square.

        If ``root`` is set to ``True`` then return a pair made of the
        boolean answer together with ``None`` or a square root.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)

            sage: R.one().is_square()
            True
            sage: R(2).is_square()
            False

            sage: t.is_square()
            False
            sage: (t**-2).is_square()
            True

        Usage of the ``root`` option::

            sage: p = (1 + t^-1 - 2*t^3)
            sage: p.is_square(root=True)
            (False, None)
            sage: (p**2).is_square(root=True)
            (True, -t^-1 - 1 + 2*t^3)

        The answer is dependent of the base ring::

            sage: # needs sage.rings.number_field
            sage: S.<u> = LaurentPolynomialRing(QQbar)
            sage: (2 + 4*t + 2*t^2).is_square()
            False
            sage: (2 + 4*u + 2*u^2).is_square()
            True

        TESTS::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t - t).is_square(True)
            (True, 0)

            sage: for _ in range(10):
            ....:     p = t ** randint(-15,15) * sum(QQ.random_element() * t**n for n in range(randint(5,10)))
            ....:     ans, r = (p**2).is_square(root=True)
            ....:     assert ans
            ....:     assert r*r == p*p"""
    @overload
    def is_square(self, root=...) -> Any:
        """LaurentPolynomial_univariate.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1764)

        Return whether this Laurent polynomial is a square.

        If ``root`` is set to ``True`` then return a pair made of the
        boolean answer together with ``None`` or a square root.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)

            sage: R.one().is_square()
            True
            sage: R(2).is_square()
            False

            sage: t.is_square()
            False
            sage: (t**-2).is_square()
            True

        Usage of the ``root`` option::

            sage: p = (1 + t^-1 - 2*t^3)
            sage: p.is_square(root=True)
            (False, None)
            sage: (p**2).is_square(root=True)
            (True, -t^-1 - 1 + 2*t^3)

        The answer is dependent of the base ring::

            sage: # needs sage.rings.number_field
            sage: S.<u> = LaurentPolynomialRing(QQbar)
            sage: (2 + 4*t + 2*t^2).is_square()
            False
            sage: (2 + 4*u + 2*u^2).is_square()
            True

        TESTS::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t - t).is_square(True)
            (True, 0)

            sage: for _ in range(10):
            ....:     p = t ** randint(-15,15) * sum(QQ.random_element() * t**n for n in range(randint(5,10)))
            ....:     ans, r = (p**2).is_square(root=True)
            ....:     assert ans
            ....:     assert r*r == p*p"""
    @overload
    def is_square(self, root=...) -> Any:
        """LaurentPolynomial_univariate.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1764)

        Return whether this Laurent polynomial is a square.

        If ``root`` is set to ``True`` then return a pair made of the
        boolean answer together with ``None`` or a square root.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)

            sage: R.one().is_square()
            True
            sage: R(2).is_square()
            False

            sage: t.is_square()
            False
            sage: (t**-2).is_square()
            True

        Usage of the ``root`` option::

            sage: p = (1 + t^-1 - 2*t^3)
            sage: p.is_square(root=True)
            (False, None)
            sage: (p**2).is_square(root=True)
            (True, -t^-1 - 1 + 2*t^3)

        The answer is dependent of the base ring::

            sage: # needs sage.rings.number_field
            sage: S.<u> = LaurentPolynomialRing(QQbar)
            sage: (2 + 4*t + 2*t^2).is_square()
            False
            sage: (2 + 4*u + 2*u^2).is_square()
            True

        TESTS::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t - t).is_square(True)
            (True, 0)

            sage: for _ in range(10):
            ....:     p = t ** randint(-15,15) * sum(QQ.random_element() * t**n for n in range(randint(5,10)))
            ....:     ans, r = (p**2).is_square(root=True)
            ....:     assert ans
            ....:     assert r*r == p*p"""
    @overload
    def is_square(self) -> Any:
        """LaurentPolynomial_univariate.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1764)

        Return whether this Laurent polynomial is a square.

        If ``root`` is set to ``True`` then return a pair made of the
        boolean answer together with ``None`` or a square root.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)

            sage: R.one().is_square()
            True
            sage: R(2).is_square()
            False

            sage: t.is_square()
            False
            sage: (t**-2).is_square()
            True

        Usage of the ``root`` option::

            sage: p = (1 + t^-1 - 2*t^3)
            sage: p.is_square(root=True)
            (False, None)
            sage: (p**2).is_square(root=True)
            (True, -t^-1 - 1 + 2*t^3)

        The answer is dependent of the base ring::

            sage: # needs sage.rings.number_field
            sage: S.<u> = LaurentPolynomialRing(QQbar)
            sage: (2 + 4*t + 2*t^2).is_square()
            False
            sage: (2 + 4*u + 2*u^2).is_square()
            True

        TESTS::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t - t).is_square(True)
            (True, 0)

            sage: for _ in range(10):
            ....:     p = t ** randint(-15,15) * sum(QQ.random_element() * t**n for n in range(randint(5,10)))
            ....:     ans, r = (p**2).is_square(root=True)
            ....:     assert ans
            ....:     assert r*r == p*p"""
    @overload
    def is_square(self) -> Any:
        """LaurentPolynomial_univariate.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1764)

        Return whether this Laurent polynomial is a square.

        If ``root`` is set to ``True`` then return a pair made of the
        boolean answer together with ``None`` or a square root.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)

            sage: R.one().is_square()
            True
            sage: R(2).is_square()
            False

            sage: t.is_square()
            False
            sage: (t**-2).is_square()
            True

        Usage of the ``root`` option::

            sage: p = (1 + t^-1 - 2*t^3)
            sage: p.is_square(root=True)
            (False, None)
            sage: (p**2).is_square(root=True)
            (True, -t^-1 - 1 + 2*t^3)

        The answer is dependent of the base ring::

            sage: # needs sage.rings.number_field
            sage: S.<u> = LaurentPolynomialRing(QQbar)
            sage: (2 + 4*t + 2*t^2).is_square()
            False
            sage: (2 + 4*u + 2*u^2).is_square()
            True

        TESTS::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t - t).is_square(True)
            (True, 0)

            sage: for _ in range(10):
            ....:     p = t ** randint(-15,15) * sum(QQ.random_element() * t**n for n in range(randint(5,10)))
            ....:     ans, r = (p**2).is_square(root=True)
            ....:     assert ans
            ....:     assert r*r == p*p"""
    @overload
    def is_square(self, _True) -> Any:
        """LaurentPolynomial_univariate.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1764)

        Return whether this Laurent polynomial is a square.

        If ``root`` is set to ``True`` then return a pair made of the
        boolean answer together with ``None`` or a square root.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)

            sage: R.one().is_square()
            True
            sage: R(2).is_square()
            False

            sage: t.is_square()
            False
            sage: (t**-2).is_square()
            True

        Usage of the ``root`` option::

            sage: p = (1 + t^-1 - 2*t^3)
            sage: p.is_square(root=True)
            (False, None)
            sage: (p**2).is_square(root=True)
            (True, -t^-1 - 1 + 2*t^3)

        The answer is dependent of the base ring::

            sage: # needs sage.rings.number_field
            sage: S.<u> = LaurentPolynomialRing(QQbar)
            sage: (2 + 4*t + 2*t^2).is_square()
            False
            sage: (2 + 4*u + 2*u^2).is_square()
            True

        TESTS::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t - t).is_square(True)
            (True, 0)

            sage: for _ in range(10):
            ....:     p = t ** randint(-15,15) * sum(QQ.random_element() * t**n for n in range(randint(5,10)))
            ....:     ans, r = (p**2).is_square(root=True)
            ....:     assert ans
            ....:     assert r*r == p*p"""
    @overload
    def is_square(self, root=...) -> Any:
        """LaurentPolynomial_univariate.is_square(self, root=False)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1764)

        Return whether this Laurent polynomial is a square.

        If ``root`` is set to ``True`` then return a pair made of the
        boolean answer together with ``None`` or a square root.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)

            sage: R.one().is_square()
            True
            sage: R(2).is_square()
            False

            sage: t.is_square()
            False
            sage: (t**-2).is_square()
            True

        Usage of the ``root`` option::

            sage: p = (1 + t^-1 - 2*t^3)
            sage: p.is_square(root=True)
            (False, None)
            sage: (p**2).is_square(root=True)
            (True, -t^-1 - 1 + 2*t^3)

        The answer is dependent of the base ring::

            sage: # needs sage.rings.number_field
            sage: S.<u> = LaurentPolynomialRing(QQbar)
            sage: (2 + 4*t + 2*t^2).is_square()
            False
            sage: (2 + 4*u + 2*u^2).is_square()
            True

        TESTS::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t - t).is_square(True)
            (True, 0)

            sage: for _ in range(10):
            ....:     p = t ** randint(-15,15) * sum(QQ.random_element() * t**n for n in range(randint(5,10)))
            ....:     ans, r = (p**2).is_square(root=True)
            ....:     assert ans
            ....:     assert r*r == p*p"""
    @overload
    def is_unit(self) -> Any:
        '''LaurentPolynomial_univariate.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 441)

        Return ``True`` if this Laurent polynomial is a unit in this ring.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (2 + t).is_unit()
            False
            sage: f = 2*t
            sage: f.is_unit()
            True
            sage: 1/f
            1/2*t^-1
            sage: R(0).is_unit()
            False
            sage: R.<s> = LaurentPolynomialRing(ZZ)
            sage: g = 2*s
            sage: g.is_unit()
            False
            sage: 1/g
            1/2*s^-1

        ALGORITHM: A Laurent polynomial is a unit if and only if its "unit
        part" is a unit.'''
    @overload
    def is_unit(self) -> Any:
        '''LaurentPolynomial_univariate.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 441)

        Return ``True`` if this Laurent polynomial is a unit in this ring.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (2 + t).is_unit()
            False
            sage: f = 2*t
            sage: f.is_unit()
            True
            sage: 1/f
            1/2*t^-1
            sage: R(0).is_unit()
            False
            sage: R.<s> = LaurentPolynomialRing(ZZ)
            sage: g = 2*s
            sage: g.is_unit()
            False
            sage: 1/g
            1/2*s^-1

        ALGORITHM: A Laurent polynomial is a unit if and only if its "unit
        part" is a unit.'''
    @overload
    def is_unit(self) -> Any:
        '''LaurentPolynomial_univariate.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 441)

        Return ``True`` if this Laurent polynomial is a unit in this ring.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (2 + t).is_unit()
            False
            sage: f = 2*t
            sage: f.is_unit()
            True
            sage: 1/f
            1/2*t^-1
            sage: R(0).is_unit()
            False
            sage: R.<s> = LaurentPolynomialRing(ZZ)
            sage: g = 2*s
            sage: g.is_unit()
            False
            sage: 1/g
            1/2*s^-1

        ALGORITHM: A Laurent polynomial is a unit if and only if its "unit
        part" is a unit.'''
    @overload
    def is_unit(self) -> Any:
        '''LaurentPolynomial_univariate.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 441)

        Return ``True`` if this Laurent polynomial is a unit in this ring.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (2 + t).is_unit()
            False
            sage: f = 2*t
            sage: f.is_unit()
            True
            sage: 1/f
            1/2*t^-1
            sage: R(0).is_unit()
            False
            sage: R.<s> = LaurentPolynomialRing(ZZ)
            sage: g = 2*s
            sage: g.is_unit()
            False
            sage: 1/g
            1/2*s^-1

        ALGORITHM: A Laurent polynomial is a unit if and only if its "unit
        part" is a unit.'''
    @overload
    def is_unit(self) -> Any:
        '''LaurentPolynomial_univariate.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 441)

        Return ``True`` if this Laurent polynomial is a unit in this ring.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (2 + t).is_unit()
            False
            sage: f = 2*t
            sage: f.is_unit()
            True
            sage: 1/f
            1/2*t^-1
            sage: R(0).is_unit()
            False
            sage: R.<s> = LaurentPolynomialRing(ZZ)
            sage: g = 2*s
            sage: g.is_unit()
            False
            sage: 1/g
            1/2*s^-1

        ALGORITHM: A Laurent polynomial is a unit if and only if its "unit
        part" is a unit.'''
    @overload
    def is_zero(self) -> Any:
        """LaurentPolynomial_univariate.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 469)

        Return ``1`` if ``self`` is 0, else return ``0``.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x + x^2 + 3*x^4
            sage: f.is_zero()
            0
            sage: z = 0*f
            sage: z.is_zero()
            1"""
    @overload
    def is_zero(self) -> Any:
        """LaurentPolynomial_univariate.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 469)

        Return ``1`` if ``self`` is 0, else return ``0``.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x + x^2 + 3*x^4
            sage: f.is_zero()
            0
            sage: z = 0*f
            sage: z.is_zero()
            1"""
    @overload
    def is_zero(self) -> Any:
        """LaurentPolynomial_univariate.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 469)

        Return ``1`` if ``self`` is 0, else return ``0``.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x + x^2 + 3*x^4
            sage: f.is_zero()
            0
            sage: z = 0*f
            sage: z.is_zero()
            1"""
    @overload
    def monomial_coefficients(self) -> dict:
        """LaurentPolynomial_univariate.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 844)

        Return a dictionary representing ``self``.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: Q.<t> = LaurentPolynomialRing(R)
            sage: f = (x^3 + y/t^3)^3 + t^2; f
            y^3*t^-9 + 3*x^3*y^2*t^-6 + 3*x^6*y*t^-3 + x^9 + t^2
            sage: f.monomial_coefficients()
            {-9: y^3, -6: 3*x^3*y^2, -3: 3*x^6*y, 0: x^9, 2: 1}

        ``dict`` is an alias::

            sage: f.dict()
            {-9: y^3, -6: 3*x^3*y^2, -3: 3*x^6*y, 0: x^9, 2: 1}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """LaurentPolynomial_univariate.monomial_coefficients(self) -> dict

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 844)

        Return a dictionary representing ``self``.

        EXAMPLES::

            sage: R.<x,y> = ZZ[]
            sage: Q.<t> = LaurentPolynomialRing(R)
            sage: f = (x^3 + y/t^3)^3 + t^2; f
            y^3*t^-9 + 3*x^3*y^2*t^-6 + 3*x^6*y*t^-3 + x^9 + t^2
            sage: f.monomial_coefficients()
            {-9: y^3, -6: 3*x^3*y^2, -3: 3*x^6*y, 0: x^9, 2: 1}

        ``dict`` is an alias::

            sage: f.dict()
            {-9: y^3, -6: 3*x^3*y^2, -3: 3*x^6*y, 0: x^9, 2: 1}"""
    @overload
    def monomial_reduction(self) -> Any:
        """LaurentPolynomial_univariate.monomial_reduction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1717)

        Return the decomposition as a polynomial and a power of the variable.
        Constructed for compatibility with the multivariate case.

        OUTPUT:

        A tuple ``(u, t^n)`` where ``u`` is the underlying polynomial and ``n``
        is the power of the exponent shift.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: f.monomial_reduction()
            (3*x^5 + x^3 + 1, x^-1)"""
    @overload
    def monomial_reduction(self) -> Any:
        """LaurentPolynomial_univariate.monomial_reduction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1717)

        Return the decomposition as a polynomial and a power of the variable.
        Constructed for compatibility with the multivariate case.

        OUTPUT:

        A tuple ``(u, t^n)`` where ``u`` is the underlying polynomial and ``n``
        is the power of the exponent shift.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: f.monomial_reduction()
            (3*x^5 + x^3 + 1, x^-1)"""
    @overload
    def number_of_terms(self) -> long:
        """LaurentPolynomial_univariate.number_of_terms(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 772)

        Return the number of nonzero coefficients of ``self``.

        Also called weight, hamming weight or sparsity.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: f = x^3 - 1
            sage: f.number_of_terms()
            2
            sage: R(0).number_of_terms()
            0
            sage: f = (x+1)^100
            sage: f.number_of_terms()
            101

        The method :meth:`hamming_weight` is an alias::

            sage: f.hamming_weight()
            101"""
    @overload
    def number_of_terms(self) -> Any:
        """LaurentPolynomial_univariate.number_of_terms(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 772)

        Return the number of nonzero coefficients of ``self``.

        Also called weight, hamming weight or sparsity.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: f = x^3 - 1
            sage: f.number_of_terms()
            2
            sage: R(0).number_of_terms()
            0
            sage: f = (x+1)^100
            sage: f.number_of_terms()
            101

        The method :meth:`hamming_weight` is an alias::

            sage: f.hamming_weight()
            101"""
    @overload
    def number_of_terms(self) -> Any:
        """LaurentPolynomial_univariate.number_of_terms(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 772)

        Return the number of nonzero coefficients of ``self``.

        Also called weight, hamming weight or sparsity.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: f = x^3 - 1
            sage: f.number_of_terms()
            2
            sage: R(0).number_of_terms()
            0
            sage: f = (x+1)^100
            sage: f.number_of_terms()
            101

        The method :meth:`hamming_weight` is an alias::

            sage: f.hamming_weight()
            101"""
    @overload
    def number_of_terms(self) -> Any:
        """LaurentPolynomial_univariate.number_of_terms(self) -> long

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 772)

        Return the number of nonzero coefficients of ``self``.

        Also called weight, hamming weight or sparsity.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: f = x^3 - 1
            sage: f.number_of_terms()
            2
            sage: R(0).number_of_terms()
            0
            sage: f = (x+1)^100
            sage: f.number_of_terms()
            101

        The method :meth:`hamming_weight` is an alias::

            sage: f.hamming_weight()
            101"""
    @overload
    def polynomial_construction(self) -> Any:
        """LaurentPolynomial_univariate.polynomial_construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1698)

        Return the polynomial and the shift in power used to construct the
        Laurent polynomial `t^n u`.

        OUTPUT:

        A tuple ``(u, n)`` where ``u`` is the underlying polynomial and ``n``
        is the power of the exponent shift.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: f.polynomial_construction()
            (3*x^5 + x^3 + 1, -1)"""
    @overload
    def polynomial_construction(self) -> Any:
        """LaurentPolynomial_univariate.polynomial_construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1698)

        Return the polynomial and the shift in power used to construct the
        Laurent polynomial `t^n u`.

        OUTPUT:

        A tuple ``(u, n)`` where ``u`` is the underlying polynomial and ``n``
        is the power of the exponent shift.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: f.polynomial_construction()
            (3*x^5 + x^3 + 1, -1)"""
    @overload
    def quo_rem(self, other) -> Any:
        """LaurentPolynomial_univariate.quo_rem(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1511)

        Divide ``self`` by ``other`` and return a quotient ``q``
        and a remainder ``r`` such that ``self == q * other + r``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t^-3 - t^3).quo_rem(t^-1 - t)
            (t^-2 + 1 + t^2, 0)
            sage: (t^-2 + 3 + t).quo_rem(t^-4)
            (t^2 + 3*t^4 + t^5, 0)

            sage: num = t^-2 + t
            sage: den = t^-2 + 1
            sage: q, r = num.quo_rem(den)
            sage: num == q * den + r
            True

        TESTS:

        Check that :issue:`34330` is fixed::

            sage: num = t^-2 + 3 + t
            sage: den = t^-4 + t
            sage: q, r = num.quo_rem(den); q, r
            (0, t^-2 + 3 + t)
            sage: num == q * den + r
            True

            sage: num = 2*t^-4 + t^-3 + t^-2 + 2*t + 2*t^2
            sage: q, r = num.quo_rem(den); q, r
            (2 + 2*t, -t^-3 + t^-2)
            sage: num == q * den + r
            True"""
    @overload
    def quo_rem(self, den) -> Any:
        """LaurentPolynomial_univariate.quo_rem(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1511)

        Divide ``self`` by ``other`` and return a quotient ``q``
        and a remainder ``r`` such that ``self == q * other + r``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t^-3 - t^3).quo_rem(t^-1 - t)
            (t^-2 + 1 + t^2, 0)
            sage: (t^-2 + 3 + t).quo_rem(t^-4)
            (t^2 + 3*t^4 + t^5, 0)

            sage: num = t^-2 + t
            sage: den = t^-2 + 1
            sage: q, r = num.quo_rem(den)
            sage: num == q * den + r
            True

        TESTS:

        Check that :issue:`34330` is fixed::

            sage: num = t^-2 + 3 + t
            sage: den = t^-4 + t
            sage: q, r = num.quo_rem(den); q, r
            (0, t^-2 + 3 + t)
            sage: num == q * den + r
            True

            sage: num = 2*t^-4 + t^-3 + t^-2 + 2*t + 2*t^2
            sage: q, r = num.quo_rem(den); q, r
            (2 + 2*t, -t^-3 + t^-2)
            sage: num == q * den + r
            True"""
    @overload
    def quo_rem(self, den) -> Any:
        """LaurentPolynomial_univariate.quo_rem(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1511)

        Divide ``self`` by ``other`` and return a quotient ``q``
        and a remainder ``r`` such that ``self == q * other + r``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t^-3 - t^3).quo_rem(t^-1 - t)
            (t^-2 + 1 + t^2, 0)
            sage: (t^-2 + 3 + t).quo_rem(t^-4)
            (t^2 + 3*t^4 + t^5, 0)

            sage: num = t^-2 + t
            sage: den = t^-2 + 1
            sage: q, r = num.quo_rem(den)
            sage: num == q * den + r
            True

        TESTS:

        Check that :issue:`34330` is fixed::

            sage: num = t^-2 + 3 + t
            sage: den = t^-4 + t
            sage: q, r = num.quo_rem(den); q, r
            (0, t^-2 + 3 + t)
            sage: num == q * den + r
            True

            sage: num = 2*t^-4 + t^-3 + t^-2 + 2*t + 2*t^2
            sage: q, r = num.quo_rem(den); q, r
            (2 + 2*t, -t^-3 + t^-2)
            sage: num == q * den + r
            True"""
    @overload
    def quo_rem(self, den) -> Any:
        """LaurentPolynomial_univariate.quo_rem(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1511)

        Divide ``self`` by ``other`` and return a quotient ``q``
        and a remainder ``r`` such that ``self == q * other + r``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: (t^-3 - t^3).quo_rem(t^-1 - t)
            (t^-2 + 1 + t^2, 0)
            sage: (t^-2 + 3 + t).quo_rem(t^-4)
            (t^2 + 3*t^4 + t^5, 0)

            sage: num = t^-2 + t
            sage: den = t^-2 + 1
            sage: q, r = num.quo_rem(den)
            sage: num == q * den + r
            True

        TESTS:

        Check that :issue:`34330` is fixed::

            sage: num = t^-2 + 3 + t
            sage: den = t^-4 + t
            sage: q, r = num.quo_rem(den); q, r
            (0, t^-2 + 3 + t)
            sage: num == q * den + r
            True

            sage: num = 2*t^-4 + t^-3 + t^-2 + 2*t + 2*t^2
            sage: q, r = num.quo_rem(den); q, r
            (2 + 2*t, -t^-3 + t^-2)
            sage: num == q * den + r
            True"""
    @overload
    def residue(self) -> Any:
        """LaurentPolynomial_univariate.residue(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2098)

        Return the residue of ``self``.

        The residue is the coefficient of `t^-1`.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = 3*t^-2 - t^-1 + 3 + t^2
            sage: f.residue()
            -1
            sage: g = -2*t^-2 + 4 + 3*t
            sage: g.residue()
            0
            sage: f.residue().parent()
            Rational Field"""
    @overload
    def residue(self) -> Any:
        """LaurentPolynomial_univariate.residue(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2098)

        Return the residue of ``self``.

        The residue is the coefficient of `t^-1`.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = 3*t^-2 - t^-1 + 3 + t^2
            sage: f.residue()
            -1
            sage: g = -2*t^-2 + 4 + 3*t
            sage: g.residue()
            0
            sage: f.residue().parent()
            Rational Field"""
    @overload
    def residue(self) -> Any:
        """LaurentPolynomial_univariate.residue(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2098)

        Return the residue of ``self``.

        The residue is the coefficient of `t^-1`.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = 3*t^-2 - t^-1 + 3 + t^2
            sage: f.residue()
            -1
            sage: g = -2*t^-2 + 4 + 3*t
            sage: g.residue()
            0
            sage: f.residue().parent()
            Rational Field"""
    @overload
    def residue(self) -> Any:
        """LaurentPolynomial_univariate.residue(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2098)

        Return the residue of ``self``.

        The residue is the coefficient of `t^-1`.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = 3*t^-2 - t^-1 + 3 + t^2
            sage: f.residue()
            -1
            sage: g = -2*t^-2 + 4 + 3*t
            sage: g.residue()
            0
            sage: f.residue().parent()
            Rational Field"""
    def shift(self, k) -> Any:
        """LaurentPolynomial_univariate.shift(self, k)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1210)

        Return this Laurent polynomial multiplied by the power `t^n`.
        Does not change this polynomial.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ['y'])
            sage: f = (t+t^-1)^4; f
            t^-4 + 4*t^-2 + 6 + 4*t^2 + t^4
            sage: f.shift(10)
            t^6 + 4*t^8 + 6*t^10 + 4*t^12 + t^14
            sage: f >> 10
            t^-14 + 4*t^-12 + 6*t^-10 + 4*t^-8 + t^-6
            sage: f << 4
            1 + 4*t^2 + 6*t^4 + 4*t^6 + t^8"""
    def truncate(self, n) -> Any:
        """LaurentPolynomial_univariate.truncate(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1643)

        Return a polynomial with degree at most `n-1` whose `j`-th coefficients
        agree with ``self`` for all `j < n`.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x^12 + x^3 + x^5 + x^9
            sage: f.truncate(10)
            x^-12 + x^3 + x^5 + x^9
            sage: f.truncate(5)
            x^-12 + x^3
            sage: f.truncate(-16)
            0"""
    @overload
    def valuation(self, p=...) -> Any:
        """LaurentPolynomial_univariate.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1624)

        Return the valuation of ``self``.

        The valuation of a Laurent polynomial `t^n u` is `n` plus the
        valuation of `u`.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: g = 1 - x + x^2 - x^4
            sage: f.valuation()
            -1
            sage: g.valuation()
            0"""
    @overload
    def valuation(self) -> Any:
        """LaurentPolynomial_univariate.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1624)

        Return the valuation of ``self``.

        The valuation of a Laurent polynomial `t^n u` is `n` plus the
        valuation of `u`.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: g = 1 - x + x^2 - x^4
            sage: f.valuation()
            -1
            sage: g.valuation()
            0"""
    @overload
    def valuation(self) -> Any:
        """LaurentPolynomial_univariate.valuation(self, p=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1624)

        Return the valuation of ``self``.

        The valuation of a Laurent polynomial `t^n u` is `n` plus the
        valuation of `u`.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(ZZ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: g = 1 - x + x^2 - x^4
            sage: f.valuation()
            -1
            sage: g.valuation()
            0"""
    @overload
    def variable_name(self) -> Any:
        """LaurentPolynomial_univariate.variable_name(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1668)

        Return the name of variable of ``self`` as a string.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: f.variable_name()
            'x'"""
    @overload
    def variable_name(self) -> Any:
        """LaurentPolynomial_univariate.variable_name(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1668)

        Return the name of variable of ``self`` as a string.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: f.variable_name()
            'x'"""
    @overload
    def variables(self) -> Any:
        """LaurentPolynomial_univariate.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1681)

        Return the tuple of variables occurring in this Laurent polynomial.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: f.variables()
            (x,)
            sage: R.one().variables()
            ()"""
    @overload
    def variables(self) -> Any:
        """LaurentPolynomial_univariate.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1681)

        Return the tuple of variables occurring in this Laurent polynomial.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: f.variables()
            (x,)
            sage: R.one().variables()
            ()"""
    @overload
    def variables(self) -> Any:
        """LaurentPolynomial_univariate.variables(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1681)

        Return the tuple of variables occurring in this Laurent polynomial.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: f.variables()
            (x,)
            sage: R.one().variables()
            ()"""
    def xgcd(self, other) -> Any:
        """LaurentPolynomial_univariate.xgcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1348)

        Extended :meth:`gcd` for univariate Laurent polynomial rings over a field.

        OUTPUT:

        A triple ``(g, p, q)`` such that ``g`` is the :meth:`gcd` of
        ``self`` (`= a`) and ``other`` (`= b`), and ``p`` and ``q`` are
        cofactors satisfying the Bezout identity

        .. MATH::

            g = p \\cdot a + q \\cdot b.

        EXAMPLES::

            sage: S.<t> = LaurentPolynomialRing(QQ)
            sage: a = t^-2 + 1
            sage: b = t^-3 + 1
            sage: g, p, q = a.xgcd(b); (g, p, q)
            (t^-3, 1/2*t^-1 - 1/2 - 1/2*t, 1/2 + 1/2*t)
            sage: g == p * a + q * b
            True
            sage: g == a.gcd(b)
            True
            sage: t.xgcd(t)
            (t, 0, 1)
            sage: t.xgcd(5)
            (1, 0, 1/5)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *x, **kwds) -> Any:
        """LaurentPolynomial_univariate.__call__(self, *x, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 2024)

        Compute value of this Laurent polynomial at ``x``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(ZZ)
            sage: f = t^(-2) + t^2
            sage: f(2)
            17/4
            sage: f(-1)
            2
            sage: f(1/3)
            82/9
            sage: f(t=-1)
            2
            sage: f(x=-1)
            t^-2 + t^2
            sage: f()
            t^-2 + t^2
            sage: f(1,2)
            Traceback (most recent call last):
            ...
            TypeError: number of arguments does not match number of
             variables in parent"""
    def __copy__(self) -> Any:
        """LaurentPolynomial_univariate.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1829)

        Return a copy of ``self``.

        EXAMPLES::

            sage: R.<x> = LaurentPolynomialRing(QQ)
            sage: f = 1/x + x^2 + 3*x^4
            sage: cf = copy(f)
            sage: cf == f
            True
            sage: cf is not f
            True"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, i) -> Any:
        """LaurentPolynomial_univariate.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 720)

        Return the `i`-th coefficient of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = -5/t^(10) + t + t^2 - 10/3*t^3; f
            -5*t^-10 + t + t^2 - 10/3*t^3
            sage: f[-10]
            -5
            sage: f[1]
            1
            sage: f[3]
            -10/3
            sage: f[-9]
            0
            sage: f = -5/t^(10) + 1/3 + t + t^2 - 10/3*t^3; f
            -5*t^-10 + 1/3 + t + t^2 - 10/3*t^3

        Slicing can be used to truncate Laurent polynomials::

            sage: f[:3]
            -5*t^-10 + 1/3 + t + t^2

        Any other kind of slicing is an error, see :issue:`18940`::

            sage: f[-10:2]
            Traceback (most recent call last):
            ...
            IndexError: polynomial slicing with a start is not defined

            sage: f[-14:5:2]
            Traceback (most recent call last):
            ...
            IndexError: polynomial slicing with a step is not defined"""
    def __hash__(self) -> Any:
        '''LaurentPolynomial_univariate.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 673)

        Return the hash of ``self``.

        TESTS::

            sage: R = LaurentPolynomialRing(QQ, \'t\')

            sage: assert hash(R.zero()) == 0
            sage: assert hash(R.one()) == 1
            sage: assert hash(QQ[\'t\'].gen()) == hash(R.gen())

            sage: for _ in range(20):
            ....:     p = QQ.random_element()
            ....:     assert hash(R(p)) == hash(p), "p = {}".format(p)

            sage: S.<t> = QQ[]
            sage: for _ in range(20):
            ....:     p = S.random_element()
            ....:     assert hash(R(p)) == hash(p), "p = {}".format(p)
            ....:     assert hash(R(t*p)) == hash(t*p), "p = {}".format(p)

        Check that :issue:`21272` is fixed::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: hash(R.zero()) == hash(t - t)
            True'''
    def __invert__(self) -> Any:
        """LaurentPolynomial_univariate.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1293)

        Return the inverse of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: i = ~(t^-2); i
            t^2
            sage: i.parent() is R
            True
            sage: i = ~(2*t^2); i
            1/2*t^-2
            sage: i.parent() is R
            True
            sage: i = ~(t^-2 + 2 + t^2); i
            t^2/(t^4 + 2*t^2 + 1)
            sage: i.parent()
            Fraction Field of Univariate Polynomial Ring in t over Rational Field"""
    def __iter__(self) -> Any:
        """LaurentPolynomial_univariate.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 797)

        Iterate through the coefficients from the first nonzero one to the
        last nonzero one.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = -5/t^(2) + t + t^2 - 10/3*t^3; f
            -5*t^-2 + t + t^2 - 10/3*t^3
            sage: for a in f: print(a)
            -5
            0
            0
            1
            1
            -10/3"""
    def __lshift__(self, LaurentPolynomial_univariateself, k) -> Any:
        """LaurentPolynomial_univariate.__lshift__(LaurentPolynomial_univariate self, k)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1234)

        Return the left shift of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = (t+t^-1)^4; f
            t^-4 + 4*t^-2 + 6 + 4*t^2 + t^4
            sage: f << 4
            1 + 4*t^2 + 6*t^4 + 4*t^6 + t^8"""
    def __neg__(self) -> Any:
        """LaurentPolynomial_univariate.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1051)

        Return the negative of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(ZZ)
            sage: -(1+t^5)
            -1 - t^5"""
    def __pow__(self, _self, r, mod) -> Any:
        """LaurentPolynomial_univariate.__pow__(_self, r, mod)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1139)

        EXAMPLES::

            sage: x = LaurentPolynomialRing(QQ,'x').0
            sage: f = x + x^2 + 3*x^4
            sage: g = 1/x^10 - x
            sage: f^3
            x^3 + 3*x^4 + 3*x^5 + 10*x^6 + 18*x^7 + 9*x^8 + 27*x^9 + 27*x^10 + 27*x^12
            sage: g^4
            x^-40 - 4*x^-29 + 6*x^-18 - 4*x^-7 + x^4

            sage: R.<x> = LaurentPolynomialRing(Zmod(6))
            sage: x^-2
            x^-2
            sage: (5*x^2)^-4
            x^-8
            sage: (5*x^-4)^-3
            5*x^12

        Check that using third argument raises an error::

            sage: L.<x> = LaurentPolynomialRing(R)
            sage: pow(x, 2, x)
            Traceback (most recent call last):
            ...
            NotImplementedError: pow() with a modulus is not implemented for this ring"""
    def __reduce__(self) -> Any:
        """LaurentPolynomial_univariate.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 372)

        Used in pickling.

        EXAMPLES::

            sage: R.<q> = LaurentPolynomialRing(ZZ)
            sage: elt = q^-3 + 2 + q
            sage: loads(dumps(elt)) == elt
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, LaurentPolynomial_univariateself, k) -> Any:
        """LaurentPolynomial_univariate.__rshift__(LaurentPolynomial_univariate self, k)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 1253)

        Return the right shift of ``self``.

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = (t+t^-1)^4; f
            t^-4 + 4*t^-2 + 6 + 4*t^2 + t^4
            sage: f >> 10
            t^-14 + 4*t^-12 + 6*t^-10 + 4*t^-8 + t^-6"""
    def __setitem__(self, n, value) -> Any:
        """LaurentPolynomial_univariate.__setitem__(self, n, value)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/laurent_polynomial.pyx (starting at line 893)

        EXAMPLES::

            sage: R.<t> = LaurentPolynomialRing(QQ)
            sage: f = t^2 + t^-3
            sage: f[2] = 5
            Traceback (most recent call last):
            ...
            IndexError: Laurent polynomials are immutable"""
