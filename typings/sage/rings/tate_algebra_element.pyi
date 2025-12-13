import sage.structure.element
from sage.categories.category import ZZ as ZZ
from sage.rings.infinity import Infinity as Infinity
from sage.rings.padics.precision_error import PrecisionError as PrecisionError
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class TateAlgebraElement(sage.structure.element.CommutativeAlgebraElement):
    """TateAlgebraElement(parent, x, prec=None, reduce=True)

    File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1022)

    A class for Tate series, elements of Tate algebras.

    EXAMPLES::

        sage: R = Zp(2, prec=10, print_mode='digits')
        sage: A.<x,y> = TateAlgebra(R)
        sage: A(2*x+1)
        ...0000000001 + ...00000000010*x
        sage: A(2*x+1, prec=5)
        ...00001 + ...00010*x + O(2^5 * <x, y>)
        sage: A(2*x+1, prec=20)
        ...0000000001 + ...00000000010*x + O(2^20 * <x, y>)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x, prec=..., reduce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1037)

                Initialize a Tate algebra series.

                TESTS::

                    sage: R = Zp(2, prec=10, print_mode='digits')
                    sage: A.<x,y> = TateAlgebra(R)
                    sage: TestSuite(x).run()
        """
    @overload
    def Spoly(self, other) -> Any:
        """TateAlgebraElement.Spoly(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3382)

        Return the S-polynomial of this series and ``other``.

        INPUT:

        - ``other`` -- a Tate series

        NOTE:

        If `f` and `g` are two Tate series with leading term
        `t_f` and `t_g` respectively, the S-polynomial of `f`
        and `g` is defined by

        .. MATH::

            S(f,g) = \x0c        rac{      ext{lcm}(t_f,t_g)}{t_f}} f - \x0c        rac{      ext{lcm}(t_f,t_g)}{t_g}} g

        By construction the terms in `  ext{lcm}(t_f,t_g)` cancel,
        so that the leading term of `S(f,g)` is strictly smaller
        than `  ext{lcm}(t_f,t_g)`.

        EXAMPLES::

            sage: R = Zp(2, 5, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^3*y + 2*x*y + 4*x^2
            sage: g = 2*x*y^2 + 2*x
            sage: h = f.Spoly(g); h
            ...111110*x^3 + ...0000100*x*y^2 + ...00001000*x^2*y

            sage: h == 2*y*f - x^2*g
            True

        TESTS::

            sage: f.Spoly(0)
            Traceback (most recent call last):
            ...
            ValueError: the S-polynomial of zero is not defined"""
    @overload
    def Spoly(self, g) -> Any:
        """TateAlgebraElement.Spoly(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3382)

        Return the S-polynomial of this series and ``other``.

        INPUT:

        - ``other`` -- a Tate series

        NOTE:

        If `f` and `g` are two Tate series with leading term
        `t_f` and `t_g` respectively, the S-polynomial of `f`
        and `g` is defined by

        .. MATH::

            S(f,g) = \x0c        rac{      ext{lcm}(t_f,t_g)}{t_f}} f - \x0c        rac{      ext{lcm}(t_f,t_g)}{t_g}} g

        By construction the terms in `  ext{lcm}(t_f,t_g)` cancel,
        so that the leading term of `S(f,g)` is strictly smaller
        than `  ext{lcm}(t_f,t_g)`.

        EXAMPLES::

            sage: R = Zp(2, 5, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^3*y + 2*x*y + 4*x^2
            sage: g = 2*x*y^2 + 2*x
            sage: h = f.Spoly(g); h
            ...111110*x^3 + ...0000100*x*y^2 + ...00001000*x^2*y

            sage: h == 2*y*f - x^2*g
            True

        TESTS::

            sage: f.Spoly(0)
            Traceback (most recent call last):
            ...
            ValueError: the S-polynomial of zero is not defined"""
    def add_bigoh(self, n) -> Any:
        """TateAlgebraElement.add_bigoh(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2302)

        Return this series truncated at precision ``n``.

        INPUT:

        - ``n`` -- integer

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 32*x + 64*x^2; f
            ...000000000100000*x + ...0000000001000000*x^2
            sage: f.add_bigoh(5)
            O(2^5 * <x, y>)

            sage: g = f.add_bigoh(6); g
            ...100000*x + O(2^6 * <x, y>)
            sage: g.precision_absolute()
            6"""
    def coefficient(self, exponent) -> Any:
        """TateAlgebraElement.coefficient(self, exponent)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2220)

        Return the coefficient corresponding to the given exponent.

        INPUT:

        - ``exponent`` -- tuple of integers

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='terse')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x^2 + 53*x*y + y^3

            sage: f.coefficient((2,0))   # coeff in x^2
            2 + O(2^11)
            sage: f.coefficient((1,1))   # coeff in x*y
            53 + O(2^10)
            sage: f.coefficient((3,0))   # coeff in x^3
            0

            sage: g = f.add_bigoh(5)
            sage: g.coefficient((2,0))   # coeff in x^2
            2 + O(2^5)
            sage: g.coefficient((1,1))   # coeff in x*y
            21 + O(2^5)
            sage: g.coefficient((3,0))   # coeff in x^3
            O(2^5)"""
    @overload
    def coefficients(self) -> Any:
        """TateAlgebraElement.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2288)

        Return the list of coefficients of this series.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x + 2*x^2
            sage: f.coefficients()
            [...0000000001, ...00000000010]"""
    @overload
    def coefficients(self) -> Any:
        """TateAlgebraElement.coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2288)

        Return the list of coefficients of this series.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x + 2*x^2
            sage: f.coefficients()
            [...0000000001, ...00000000010]"""
    @overload
    def degree(self) -> Any:
        """TateAlgebraElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2991)

        Return the Weierstrass degree of this Tate series.

        .. NOTE::

            The Weierstrass degree is the total degree of the polynomial
            defined by the terms with least valuation in the series.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x*y + 2*x^4 + y; f
            ...0000000001*x*y + ...0000000001*y + ...00000000010*x^4
            sage: f.degree()
            2"""
    @overload
    def degree(self) -> Any:
        """TateAlgebraElement.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2991)

        Return the Weierstrass degree of this Tate series.

        .. NOTE::

            The Weierstrass degree is the total degree of the polynomial
            defined by the terms with least valuation in the series.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x*y + 2*x^4 + y; f
            ...0000000001*x*y + ...0000000001*y + ...00000000010*x^4
            sage: f.degree()
            2"""
    @overload
    def degrees(self) -> Any:
        """TateAlgebraElement.degrees(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3032)

        Return the Weierstrass degrees of this series.

        .. NOTE::

            The Weierstrass degrees are the partial degrees of the polynomial
            defined by the terms with least valuation in the series.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits',prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^2 + y^2 + 2*x^3 + y; f
            ...0000000001*x^2 + ...0000000001*y^2 + ...0000000001*y + ...00000000010*x^3
            sage: f.degrees()
            (2, 2)"""
    @overload
    def degrees(self) -> Any:
        """TateAlgebraElement.degrees(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3032)

        Return the Weierstrass degrees of this series.

        .. NOTE::

            The Weierstrass degrees are the partial degrees of the polynomial
            defined by the terms with least valuation in the series.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits',prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^2 + y^2 + 2*x^3 + y; f
            ...0000000001*x^2 + ...0000000001*y^2 + ...0000000001*y + ...00000000010*x^3
            sage: f.degrees()
            (2, 2)"""
    def dict(self) -> Any:
        """TateAlgebraElement.monomial_coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2197)

        Return a dictionary whose keys are the exponents and whose values
        are the corresponding coefficients of this series.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x^2 + x
            sage: f.monomial_coefficients()
            {(1, 0): ...0000000001, (2, 0): ...00000000010}

        ``dict`` is an alias::

            sage: f.dict()
            {(1, 0): ...0000000001, (2, 0): ...00000000010}"""
    @overload
    def exp(self, prec=...) -> Any:
        """TateAlgebraElement.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2650)

        Return the exponential of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 3*x^2 + 9*y
            sage: f.exp()
            ...0000000001 + ...0000000010*x^2 + ...1111111200*x^6 + ...1111111200*x^4
             + ...0000000100*y + ... + O(3^10 * <x, y>)

            sage: f.exp(prec=3)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(3); g
            ...010*x^2 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp()
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp(prec=10)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = x
            sage: f.exp()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\exp(x)` converges on a smaller disk::

            sage: f.restriction(-1).exp()
            ...0000000001 + ...000000001*x + ...1111111.2*x^3 + ...111112*x^2
             + ... + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 3 * A.random_element(integral=True)
            sage: expf = f.exp()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).exp() == expf(x0, y0)
            True

            sage: expf.log() == f  # long time
            True"""
    @overload
    def exp(self) -> Any:
        """TateAlgebraElement.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2650)

        Return the exponential of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 3*x^2 + 9*y
            sage: f.exp()
            ...0000000001 + ...0000000010*x^2 + ...1111111200*x^6 + ...1111111200*x^4
             + ...0000000100*y + ... + O(3^10 * <x, y>)

            sage: f.exp(prec=3)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(3); g
            ...010*x^2 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp()
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp(prec=10)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = x
            sage: f.exp()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\exp(x)` converges on a smaller disk::

            sage: f.restriction(-1).exp()
            ...0000000001 + ...000000001*x + ...1111111.2*x^3 + ...111112*x^2
             + ... + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 3 * A.random_element(integral=True)
            sage: expf = f.exp()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).exp() == expf(x0, y0)
            True

            sage: expf.log() == f  # long time
            True"""
    @overload
    def exp(self, prec=...) -> Any:
        """TateAlgebraElement.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2650)

        Return the exponential of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 3*x^2 + 9*y
            sage: f.exp()
            ...0000000001 + ...0000000010*x^2 + ...1111111200*x^6 + ...1111111200*x^4
             + ...0000000100*y + ... + O(3^10 * <x, y>)

            sage: f.exp(prec=3)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(3); g
            ...010*x^2 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp()
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp(prec=10)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = x
            sage: f.exp()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\exp(x)` converges on a smaller disk::

            sage: f.restriction(-1).exp()
            ...0000000001 + ...000000001*x + ...1111111.2*x^3 + ...111112*x^2
             + ... + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 3 * A.random_element(integral=True)
            sage: expf = f.exp()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).exp() == expf(x0, y0)
            True

            sage: expf.log() == f  # long time
            True"""
    @overload
    def exp(self) -> Any:
        """TateAlgebraElement.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2650)

        Return the exponential of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 3*x^2 + 9*y
            sage: f.exp()
            ...0000000001 + ...0000000010*x^2 + ...1111111200*x^6 + ...1111111200*x^4
             + ...0000000100*y + ... + O(3^10 * <x, y>)

            sage: f.exp(prec=3)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(3); g
            ...010*x^2 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp()
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp(prec=10)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = x
            sage: f.exp()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\exp(x)` converges on a smaller disk::

            sage: f.restriction(-1).exp()
            ...0000000001 + ...000000001*x + ...1111111.2*x^3 + ...111112*x^2
             + ... + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 3 * A.random_element(integral=True)
            sage: expf = f.exp()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).exp() == expf(x0, y0)
            True

            sage: expf.log() == f  # long time
            True"""
    @overload
    def exp(self, prec=...) -> Any:
        """TateAlgebraElement.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2650)

        Return the exponential of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 3*x^2 + 9*y
            sage: f.exp()
            ...0000000001 + ...0000000010*x^2 + ...1111111200*x^6 + ...1111111200*x^4
             + ...0000000100*y + ... + O(3^10 * <x, y>)

            sage: f.exp(prec=3)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(3); g
            ...010*x^2 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp()
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp(prec=10)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = x
            sage: f.exp()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\exp(x)` converges on a smaller disk::

            sage: f.restriction(-1).exp()
            ...0000000001 + ...000000001*x + ...1111111.2*x^3 + ...111112*x^2
             + ... + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 3 * A.random_element(integral=True)
            sage: expf = f.exp()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).exp() == expf(x0, y0)
            True

            sage: expf.log() == f  # long time
            True"""
    @overload
    def exp(self) -> Any:
        """TateAlgebraElement.exp(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2650)

        Return the exponential of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 3*x^2 + 9*y
            sage: f.exp()
            ...0000000001 + ...0000000010*x^2 + ...1111111200*x^6 + ...1111111200*x^4
             + ...0000000100*y + ... + O(3^10 * <x, y>)

            sage: f.exp(prec=3)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(3); g
            ...010*x^2 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp()
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)
            sage: g.exp(prec=10)
            ...001 + ...010*x^2 + ...200*x^6 + ...200*x^4 + ...100*y + O(3^3 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = x
            sage: f.exp()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\exp(x)` converges on a smaller disk::

            sage: f.restriction(-1).exp()
            ...0000000001 + ...000000001*x + ...1111111.2*x^3 + ...111112*x^2
             + ... + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 3 * A.random_element(integral=True)
            sage: expf = f.exp()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).exp() == expf(x0, y0)
            True

            sage: expf.log() == f  # long time
            True"""
    @overload
    def inverse_of_unit(self, prec=...) -> Any:
        """TateAlgebraElement.inverse_of_unit(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1392)

        Return the inverse of this series if it is invertible.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the precision at which the result is computed, if ``None``,
          the result is truncated according to the cap of the parent

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = A(1); f
            ...0000000001
            sage: f.inverse_of_unit()
            ...0000000001 + O(2^10 * <x, y>)

            sage: f = 2*x + 1; f
            ...0000000001 + ...00000000010*x
            sage: f.inverse_of_unit()
            ...0000000001 + ...1111111110*x + ...0000000100*x^2 + ...1111111000*x^3
             + ...0000010000*x^4 + ...1111100000*x^5 + ...0001000000*x^6
             + ...1110000000*x^7 + ...0100000000*x^8 + ...1000000000*x^9 + O(2^10 * <x, y>)

            sage: f.inverse_of_unit(prec=4)
            ...0001 + ...1110*x + ...0100*x^2 + ...1000*x^3 + O(2^4 * <x, y>)

        If the series is not invertible, an error is raised::

            sage: f = 1 + x; f
            ...0000000001*x + ...0000000001
            sage: f.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ValueError: this series in not invertible"""
    @overload
    def inverse_of_unit(self) -> Any:
        """TateAlgebraElement.inverse_of_unit(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1392)

        Return the inverse of this series if it is invertible.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the precision at which the result is computed, if ``None``,
          the result is truncated according to the cap of the parent

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = A(1); f
            ...0000000001
            sage: f.inverse_of_unit()
            ...0000000001 + O(2^10 * <x, y>)

            sage: f = 2*x + 1; f
            ...0000000001 + ...00000000010*x
            sage: f.inverse_of_unit()
            ...0000000001 + ...1111111110*x + ...0000000100*x^2 + ...1111111000*x^3
             + ...0000010000*x^4 + ...1111100000*x^5 + ...0001000000*x^6
             + ...1110000000*x^7 + ...0100000000*x^8 + ...1000000000*x^9 + O(2^10 * <x, y>)

            sage: f.inverse_of_unit(prec=4)
            ...0001 + ...1110*x + ...0100*x^2 + ...1000*x^3 + O(2^4 * <x, y>)

        If the series is not invertible, an error is raised::

            sage: f = 1 + x; f
            ...0000000001*x + ...0000000001
            sage: f.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ValueError: this series in not invertible"""
    @overload
    def inverse_of_unit(self) -> Any:
        """TateAlgebraElement.inverse_of_unit(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1392)

        Return the inverse of this series if it is invertible.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the precision at which the result is computed, if ``None``,
          the result is truncated according to the cap of the parent

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = A(1); f
            ...0000000001
            sage: f.inverse_of_unit()
            ...0000000001 + O(2^10 * <x, y>)

            sage: f = 2*x + 1; f
            ...0000000001 + ...00000000010*x
            sage: f.inverse_of_unit()
            ...0000000001 + ...1111111110*x + ...0000000100*x^2 + ...1111111000*x^3
             + ...0000010000*x^4 + ...1111100000*x^5 + ...0001000000*x^6
             + ...1110000000*x^7 + ...0100000000*x^8 + ...1000000000*x^9 + O(2^10 * <x, y>)

            sage: f.inverse_of_unit(prec=4)
            ...0001 + ...1110*x + ...0100*x^2 + ...1000*x^3 + O(2^4 * <x, y>)

        If the series is not invertible, an error is raised::

            sage: f = 1 + x; f
            ...0000000001*x + ...0000000001
            sage: f.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ValueError: this series in not invertible"""
    @overload
    def inverse_of_unit(self, prec=...) -> Any:
        """TateAlgebraElement.inverse_of_unit(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1392)

        Return the inverse of this series if it is invertible.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the precision at which the result is computed, if ``None``,
          the result is truncated according to the cap of the parent

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = A(1); f
            ...0000000001
            sage: f.inverse_of_unit()
            ...0000000001 + O(2^10 * <x, y>)

            sage: f = 2*x + 1; f
            ...0000000001 + ...00000000010*x
            sage: f.inverse_of_unit()
            ...0000000001 + ...1111111110*x + ...0000000100*x^2 + ...1111111000*x^3
             + ...0000010000*x^4 + ...1111100000*x^5 + ...0001000000*x^6
             + ...1110000000*x^7 + ...0100000000*x^8 + ...1000000000*x^9 + O(2^10 * <x, y>)

            sage: f.inverse_of_unit(prec=4)
            ...0001 + ...1110*x + ...0100*x^2 + ...1000*x^3 + O(2^4 * <x, y>)

        If the series is not invertible, an error is raised::

            sage: f = 1 + x; f
            ...0000000001*x + ...0000000001
            sage: f.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ValueError: this series in not invertible"""
    @overload
    def inverse_of_unit(self) -> Any:
        """TateAlgebraElement.inverse_of_unit(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1392)

        Return the inverse of this series if it is invertible.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the precision at which the result is computed, if ``None``,
          the result is truncated according to the cap of the parent

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = A(1); f
            ...0000000001
            sage: f.inverse_of_unit()
            ...0000000001 + O(2^10 * <x, y>)

            sage: f = 2*x + 1; f
            ...0000000001 + ...00000000010*x
            sage: f.inverse_of_unit()
            ...0000000001 + ...1111111110*x + ...0000000100*x^2 + ...1111111000*x^3
             + ...0000010000*x^4 + ...1111100000*x^5 + ...0001000000*x^6
             + ...1110000000*x^7 + ...0100000000*x^8 + ...1000000000*x^9 + O(2^10 * <x, y>)

            sage: f.inverse_of_unit(prec=4)
            ...0001 + ...1110*x + ...0100*x^2 + ...1000*x^3 + O(2^4 * <x, y>)

        If the series is not invertible, an error is raised::

            sage: f = 1 + x; f
            ...0000000001*x + ...0000000001
            sage: f.inverse_of_unit()
            Traceback (most recent call last):
            ...
            ValueError: this series in not invertible"""
    @overload
    def is_monic(self) -> Any:
        """TateAlgebraElement.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2945)

        Return ``True`` if this series is monic, in the sense
        that it has valuation 0 and its leading coefficient is
        a power of the uniformizer.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x*y + 2; f
            ...0000000001*x*y + ...00000000010
            sage: f.is_monic()
            True

            sage: g = f.restriction(-1); g
            ...00000000010 + ...0000000001*x*y
            sage: g.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """TateAlgebraElement.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2945)

        Return ``True`` if this series is monic, in the sense
        that it has valuation 0 and its leading coefficient is
        a power of the uniformizer.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x*y + 2; f
            ...0000000001*x*y + ...00000000010
            sage: f.is_monic()
            True

            sage: g = f.restriction(-1); g
            ...00000000010 + ...0000000001*x*y
            sage: g.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """TateAlgebraElement.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2945)

        Return ``True`` if this series is monic, in the sense
        that it has valuation 0 and its leading coefficient is
        a power of the uniformizer.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x*y + 2; f
            ...0000000001*x*y + ...00000000010
            sage: f.is_monic()
            True

            sage: g = f.restriction(-1); g
            ...00000000010 + ...0000000001*x*y
            sage: g.is_monic()
            False"""
    @overload
    def is_unit(self) -> Any:
        """TateAlgebraElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1458)

        Return ``True`` if this series is invertible.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x + 1; f
            ...0000000001 + ...00000000010*x
            sage: f.is_unit()
            True

            sage: f = 1 + x; f
            ...0000000001*x + ...0000000001
            sage: f.is_unit()
            False

        Note that invertibility is tested in the parent of this series::

            sage: f = 4*x + 2
            sage: f.is_unit()
            True

            sage: Ao = A.integer_ring()
            sage: Ao(f).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """TateAlgebraElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1458)

        Return ``True`` if this series is invertible.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x + 1; f
            ...0000000001 + ...00000000010*x
            sage: f.is_unit()
            True

            sage: f = 1 + x; f
            ...0000000001*x + ...0000000001
            sage: f.is_unit()
            False

        Note that invertibility is tested in the parent of this series::

            sage: f = 4*x + 2
            sage: f.is_unit()
            True

            sage: Ao = A.integer_ring()
            sage: Ao(f).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """TateAlgebraElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1458)

        Return ``True`` if this series is invertible.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x + 1; f
            ...0000000001 + ...00000000010*x
            sage: f.is_unit()
            True

            sage: f = 1 + x; f
            ...0000000001*x + ...0000000001
            sage: f.is_unit()
            False

        Note that invertibility is tested in the parent of this series::

            sage: f = 4*x + 2
            sage: f.is_unit()
            True

            sage: Ao = A.integer_ring()
            sage: Ao(f).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """TateAlgebraElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1458)

        Return ``True`` if this series is invertible.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x + 1; f
            ...0000000001 + ...00000000010*x
            sage: f.is_unit()
            True

            sage: f = 1 + x; f
            ...0000000001*x + ...0000000001
            sage: f.is_unit()
            False

        Note that invertibility is tested in the parent of this series::

            sage: f = 4*x + 2
            sage: f.is_unit()
            True

            sage: Ao = A.integer_ring()
            sage: Ao(f).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """TateAlgebraElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1458)

        Return ``True`` if this series is invertible.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x + 1; f
            ...0000000001 + ...00000000010*x
            sage: f.is_unit()
            True

            sage: f = 1 + x; f
            ...0000000001*x + ...0000000001
            sage: f.is_unit()
            False

        Note that invertibility is tested in the parent of this series::

            sage: f = 4*x + 2
            sage: f.is_unit()
            True

            sage: Ao = A.integer_ring()
            sage: Ao(f).is_unit()
            False"""
    @overload
    def is_zero(self, prec=...) -> Any:
        """TateAlgebraElement.is_zero(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2055)

        Return ``True`` if this series is indistinguishable from zero.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``),
          the precision at which the series should be compared to zero

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x + 2*x^2 + x^3; f
            ...0000000001*x^3 + ...0000000001*x + ...00000000010*x^2
            sage: f.is_zero()
            False

            sage: g = f << 4; g
            ...00000000010000*x^3 + ...00000000010000*x + ...000000000100000*x^2
            sage: g.is_zero()
            False
            sage: g.is_zero(5)
            False
            sage: g.is_zero(4)
            True"""
    @overload
    def is_zero(self) -> Any:
        """TateAlgebraElement.is_zero(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2055)

        Return ``True`` if this series is indistinguishable from zero.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``),
          the precision at which the series should be compared to zero

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x + 2*x^2 + x^3; f
            ...0000000001*x^3 + ...0000000001*x + ...00000000010*x^2
            sage: f.is_zero()
            False

            sage: g = f << 4; g
            ...00000000010000*x^3 + ...00000000010000*x + ...000000000100000*x^2
            sage: g.is_zero()
            False
            sage: g.is_zero(5)
            False
            sage: g.is_zero(4)
            True"""
    @overload
    def is_zero(self) -> Any:
        """TateAlgebraElement.is_zero(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2055)

        Return ``True`` if this series is indistinguishable from zero.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``),
          the precision at which the series should be compared to zero

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x + 2*x^2 + x^3; f
            ...0000000001*x^3 + ...0000000001*x + ...00000000010*x^2
            sage: f.is_zero()
            False

            sage: g = f << 4; g
            ...00000000010000*x^3 + ...00000000010000*x + ...000000000100000*x^2
            sage: g.is_zero()
            False
            sage: g.is_zero(5)
            False
            sage: g.is_zero(4)
            True"""
    @overload
    def leading_coefficient(self, secure=...) -> Any:
        """TateAlgebraElement.leading_coefficient(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2827)

        Return the leading coefficient of this series.

        .. NOTE::

            The leading coefficient is the coefficient of the leading term.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='terse')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + 3*x*y + 1; f
            (1 + O(2^10))*x^4 + (3 + O(2^10))*x*y + (1 + O(2^10))
            sage: f.leading_coefficient()
            1 + O(2^10)

            sage: g = f + x^4; g
            (3 + O(2^10))*x*y + (1 + O(2^10)) + (2 + O(2^10))*x^4
            sage: g.leading_coefficient()
            3 + O(2^10)

        .. SEEALSO::

            :meth:`leading_term`, :meth:`leading_monomial`"""
    @overload
    def leading_coefficient(self) -> Any:
        """TateAlgebraElement.leading_coefficient(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2827)

        Return the leading coefficient of this series.

        .. NOTE::

            The leading coefficient is the coefficient of the leading term.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='terse')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + 3*x*y + 1; f
            (1 + O(2^10))*x^4 + (3 + O(2^10))*x*y + (1 + O(2^10))
            sage: f.leading_coefficient()
            1 + O(2^10)

            sage: g = f + x^4; g
            (3 + O(2^10))*x*y + (1 + O(2^10)) + (2 + O(2^10))*x^4
            sage: g.leading_coefficient()
            3 + O(2^10)

        .. SEEALSO::

            :meth:`leading_term`, :meth:`leading_monomial`"""
    @overload
    def leading_coefficient(self) -> Any:
        """TateAlgebraElement.leading_coefficient(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2827)

        Return the leading coefficient of this series.

        .. NOTE::

            The leading coefficient is the coefficient of the leading term.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='terse')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + 3*x*y + 1; f
            (1 + O(2^10))*x^4 + (3 + O(2^10))*x*y + (1 + O(2^10))
            sage: f.leading_coefficient()
            1 + O(2^10)

            sage: g = f + x^4; g
            (3 + O(2^10))*x*y + (1 + O(2^10)) + (2 + O(2^10))*x^4
            sage: g.leading_coefficient()
            3 + O(2^10)

        .. SEEALSO::

            :meth:`leading_term`, :meth:`leading_monomial`"""
    @overload
    def leading_monomial(self, secure=...) -> Any:
        """TateAlgebraElement.leading_monomial(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2862)

        Return the leading coefficient of this series.

        .. NOTE::

            The leading monomial is the monomial of the leading term.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + x*y + 1; f
            ...0000000001*x^4 + ...0000000001*x*y + ...0000000001
            sage: f.leading_monomial()
            ...0000000001*x^4

            sage: g = f + x^4; g
            ...0000000001*x*y + ...0000000001 + ...0000000010*x^4
            sage: g.leading_monomial()
            ...0000000001*x*y

        .. SEEALSO::

            :meth:`leading_term`, :meth:`leading_coefficient`"""
    @overload
    def leading_monomial(self) -> Any:
        """TateAlgebraElement.leading_monomial(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2862)

        Return the leading coefficient of this series.

        .. NOTE::

            The leading monomial is the monomial of the leading term.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + x*y + 1; f
            ...0000000001*x^4 + ...0000000001*x*y + ...0000000001
            sage: f.leading_monomial()
            ...0000000001*x^4

            sage: g = f + x^4; g
            ...0000000001*x*y + ...0000000001 + ...0000000010*x^4
            sage: g.leading_monomial()
            ...0000000001*x*y

        .. SEEALSO::

            :meth:`leading_term`, :meth:`leading_coefficient`"""
    @overload
    def leading_monomial(self) -> Any:
        """TateAlgebraElement.leading_monomial(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2862)

        Return the leading coefficient of this series.

        .. NOTE::

            The leading monomial is the monomial of the leading term.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + x*y + 1; f
            ...0000000001*x^4 + ...0000000001*x*y + ...0000000001
            sage: f.leading_monomial()
            ...0000000001*x^4

            sage: g = f + x^4; g
            ...0000000001*x*y + ...0000000001 + ...0000000010*x^4
            sage: g.leading_monomial()
            ...0000000001*x*y

        .. SEEALSO::

            :meth:`leading_term`, :meth:`leading_coefficient`"""
    @overload
    def leading_term(self, secure=...) -> Any:
        """TateAlgebraElement.leading_term(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2745)

        Return the leading term of this series.

        .. NOTE::

            The order on the terms is defined as follows: first we
            compare the valuation and, in case of equality, we compare
            the monomials with respect to the order given at the
            creation of the parent.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + x*y + 1; f
            ...0000000001*x^4 + ...0000000001*x*y + ...0000000001
            sage: f.leading_term()
            ...0000000001*x^4

            sage: g = f + x^4; g
            ...0000000001*x*y + ...0000000001 + ...0000000010*x^4
            sage: g.leading_monomial()
            ...0000000001*x*y

        Observe that the leading term may change after restriction::

            sage: f.restriction(-1).leading_term()
            ...0000000001

        TESTS::

            sage: f = 1 + 64*x
            sage: f -= R(1, 5)
            sage: f
            ...00000 + ...0000000001000000*x

            sage: f.leading_term()
            ...0000000001000000*x
            sage: f.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

            sage: g = A(0, 10); g
            O(2^10 * <x, y>)
            sage: g.leading_term()
            Traceback (most recent call last):
            ...
            ValueError: zero has no leading term
            sage: g.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

        .. SEEALSO::

            :meth:`leading_coefficient`, :meth:`leading_monomial`"""
    @overload
    def leading_term(self) -> Any:
        """TateAlgebraElement.leading_term(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2745)

        Return the leading term of this series.

        .. NOTE::

            The order on the terms is defined as follows: first we
            compare the valuation and, in case of equality, we compare
            the monomials with respect to the order given at the
            creation of the parent.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + x*y + 1; f
            ...0000000001*x^4 + ...0000000001*x*y + ...0000000001
            sage: f.leading_term()
            ...0000000001*x^4

            sage: g = f + x^4; g
            ...0000000001*x*y + ...0000000001 + ...0000000010*x^4
            sage: g.leading_monomial()
            ...0000000001*x*y

        Observe that the leading term may change after restriction::

            sage: f.restriction(-1).leading_term()
            ...0000000001

        TESTS::

            sage: f = 1 + 64*x
            sage: f -= R(1, 5)
            sage: f
            ...00000 + ...0000000001000000*x

            sage: f.leading_term()
            ...0000000001000000*x
            sage: f.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

            sage: g = A(0, 10); g
            O(2^10 * <x, y>)
            sage: g.leading_term()
            Traceback (most recent call last):
            ...
            ValueError: zero has no leading term
            sage: g.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

        .. SEEALSO::

            :meth:`leading_coefficient`, :meth:`leading_monomial`"""
    @overload
    def leading_term(self) -> Any:
        """TateAlgebraElement.leading_term(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2745)

        Return the leading term of this series.

        .. NOTE::

            The order on the terms is defined as follows: first we
            compare the valuation and, in case of equality, we compare
            the monomials with respect to the order given at the
            creation of the parent.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + x*y + 1; f
            ...0000000001*x^4 + ...0000000001*x*y + ...0000000001
            sage: f.leading_term()
            ...0000000001*x^4

            sage: g = f + x^4; g
            ...0000000001*x*y + ...0000000001 + ...0000000010*x^4
            sage: g.leading_monomial()
            ...0000000001*x*y

        Observe that the leading term may change after restriction::

            sage: f.restriction(-1).leading_term()
            ...0000000001

        TESTS::

            sage: f = 1 + 64*x
            sage: f -= R(1, 5)
            sage: f
            ...00000 + ...0000000001000000*x

            sage: f.leading_term()
            ...0000000001000000*x
            sage: f.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

            sage: g = A(0, 10); g
            O(2^10 * <x, y>)
            sage: g.leading_term()
            Traceback (most recent call last):
            ...
            ValueError: zero has no leading term
            sage: g.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

        .. SEEALSO::

            :meth:`leading_coefficient`, :meth:`leading_monomial`"""
    @overload
    def leading_term(self) -> Any:
        """TateAlgebraElement.leading_term(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2745)

        Return the leading term of this series.

        .. NOTE::

            The order on the terms is defined as follows: first we
            compare the valuation and, in case of equality, we compare
            the monomials with respect to the order given at the
            creation of the parent.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + x*y + 1; f
            ...0000000001*x^4 + ...0000000001*x*y + ...0000000001
            sage: f.leading_term()
            ...0000000001*x^4

            sage: g = f + x^4; g
            ...0000000001*x*y + ...0000000001 + ...0000000010*x^4
            sage: g.leading_monomial()
            ...0000000001*x*y

        Observe that the leading term may change after restriction::

            sage: f.restriction(-1).leading_term()
            ...0000000001

        TESTS::

            sage: f = 1 + 64*x
            sage: f -= R(1, 5)
            sage: f
            ...00000 + ...0000000001000000*x

            sage: f.leading_term()
            ...0000000001000000*x
            sage: f.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

            sage: g = A(0, 10); g
            O(2^10 * <x, y>)
            sage: g.leading_term()
            Traceback (most recent call last):
            ...
            ValueError: zero has no leading term
            sage: g.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

        .. SEEALSO::

            :meth:`leading_coefficient`, :meth:`leading_monomial`"""
    @overload
    def leading_term(self, secure=...) -> Any:
        """TateAlgebraElement.leading_term(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2745)

        Return the leading term of this series.

        .. NOTE::

            The order on the terms is defined as follows: first we
            compare the valuation and, in case of equality, we compare
            the monomials with respect to the order given at the
            creation of the parent.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + x*y + 1; f
            ...0000000001*x^4 + ...0000000001*x*y + ...0000000001
            sage: f.leading_term()
            ...0000000001*x^4

            sage: g = f + x^4; g
            ...0000000001*x*y + ...0000000001 + ...0000000010*x^4
            sage: g.leading_monomial()
            ...0000000001*x*y

        Observe that the leading term may change after restriction::

            sage: f.restriction(-1).leading_term()
            ...0000000001

        TESTS::

            sage: f = 1 + 64*x
            sage: f -= R(1, 5)
            sage: f
            ...00000 + ...0000000001000000*x

            sage: f.leading_term()
            ...0000000001000000*x
            sage: f.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

            sage: g = A(0, 10); g
            O(2^10 * <x, y>)
            sage: g.leading_term()
            Traceback (most recent call last):
            ...
            ValueError: zero has no leading term
            sage: g.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

        .. SEEALSO::

            :meth:`leading_coefficient`, :meth:`leading_monomial`"""
    @overload
    def leading_term(self) -> Any:
        """TateAlgebraElement.leading_term(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2745)

        Return the leading term of this series.

        .. NOTE::

            The order on the terms is defined as follows: first we
            compare the valuation and, in case of equality, we compare
            the monomials with respect to the order given at the
            creation of the parent.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + x*y + 1; f
            ...0000000001*x^4 + ...0000000001*x*y + ...0000000001
            sage: f.leading_term()
            ...0000000001*x^4

            sage: g = f + x^4; g
            ...0000000001*x*y + ...0000000001 + ...0000000010*x^4
            sage: g.leading_monomial()
            ...0000000001*x*y

        Observe that the leading term may change after restriction::

            sage: f.restriction(-1).leading_term()
            ...0000000001

        TESTS::

            sage: f = 1 + 64*x
            sage: f -= R(1, 5)
            sage: f
            ...00000 + ...0000000001000000*x

            sage: f.leading_term()
            ...0000000001000000*x
            sage: f.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

            sage: g = A(0, 10); g
            O(2^10 * <x, y>)
            sage: g.leading_term()
            Traceback (most recent call last):
            ...
            ValueError: zero has no leading term
            sage: g.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

        .. SEEALSO::

            :meth:`leading_coefficient`, :meth:`leading_monomial`"""
    @overload
    def leading_term(self, secure=...) -> Any:
        """TateAlgebraElement.leading_term(self, secure=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2745)

        Return the leading term of this series.

        .. NOTE::

            The order on the terms is defined as follows: first we
            compare the valuation and, in case of equality, we compare
            the monomials with respect to the order given at the
            creation of the parent.

        INPUT:

        - ``secure`` -- boolean (default: ``False``); if ``True``,
          raises an error if the leading term cannot be determined
          due to the existence of terms which are indistinguishable
          from zero. If ``False``, discard silently these terms.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + x*y + 1; f
            ...0000000001*x^4 + ...0000000001*x*y + ...0000000001
            sage: f.leading_term()
            ...0000000001*x^4

            sage: g = f + x^4; g
            ...0000000001*x*y + ...0000000001 + ...0000000010*x^4
            sage: g.leading_monomial()
            ...0000000001*x*y

        Observe that the leading term may change after restriction::

            sage: f.restriction(-1).leading_term()
            ...0000000001

        TESTS::

            sage: f = 1 + 64*x
            sage: f -= R(1, 5)
            sage: f
            ...00000 + ...0000000001000000*x

            sage: f.leading_term()
            ...0000000001000000*x
            sage: f.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

            sage: g = A(0, 10); g
            O(2^10 * <x, y>)
            sage: g.leading_term()
            Traceback (most recent call last):
            ...
            ValueError: zero has no leading term
            sage: g.leading_term(secure=True)
            Traceback (most recent call last):
            ...
            PrecisionError: not enough precision to determine the leading term

        .. SEEALSO::

            :meth:`leading_coefficient`, :meth:`leading_monomial`"""
    @overload
    def lift_to_precision(self, prec=...) -> Any:
        """TateAlgebraElement.lift_to_precision(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2326)

        Return a lift of this series at precision ``prec``.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); if
          ``None``, the cap of the parent is used if it is higher than
          the current precision

        EXAMPLES::

            sage: R = Zp(2, prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = R(1,4)*x*y + R(1,5)*x + R(1,8)*y
            sage: f
            (1 + O(2^4))*x*y + (1 + O(2^5))*x + (1 + O(2^8))*y

        This method lifts the precision of the coefficients::

            sage: f.lift_to_precision()
            (1 + O(2^10))*x*y + (1 + O(2^10))*x + (1 + O(2^10))*y

        and also acts on the global ``O(.)`` of the series::

            sage: g = f.add_bigoh(7)
            sage: g
            (1 + O(2^4))*x*y + (1 + O(2^5))*x + (1 + O(2^7))*y + O(2^7 * <x, y>)
            sage: g.lift_to_precision()
            (1 + O(2^10))*x*y + (1 + O(2^10))*x + (1 + O(2^10))*y + O(2^10 * <x, y>)

            sage: g.lift_to_precision(9)
            (1 + O(2^9))*x*y + (1 + O(2^9))*x + (1 + O(2^9))*y + O(2^9 * <x, y>)

        In the next example, the precision on the coefficient is only lifted
        to ``O(2^10)`` because it is limited by the cap of the underlying
        `p`-adic ring::

            sage: g.lift_to_precision(20)
            (1 + O(2^10))*x*y + (1 + O(2^10))*x + (1 + O(2^10))*y + O(2^20 * <x, y>)"""
    @overload
    def lift_to_precision(self) -> Any:
        """TateAlgebraElement.lift_to_precision(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2326)

        Return a lift of this series at precision ``prec``.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); if
          ``None``, the cap of the parent is used if it is higher than
          the current precision

        EXAMPLES::

            sage: R = Zp(2, prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = R(1,4)*x*y + R(1,5)*x + R(1,8)*y
            sage: f
            (1 + O(2^4))*x*y + (1 + O(2^5))*x + (1 + O(2^8))*y

        This method lifts the precision of the coefficients::

            sage: f.lift_to_precision()
            (1 + O(2^10))*x*y + (1 + O(2^10))*x + (1 + O(2^10))*y

        and also acts on the global ``O(.)`` of the series::

            sage: g = f.add_bigoh(7)
            sage: g
            (1 + O(2^4))*x*y + (1 + O(2^5))*x + (1 + O(2^7))*y + O(2^7 * <x, y>)
            sage: g.lift_to_precision()
            (1 + O(2^10))*x*y + (1 + O(2^10))*x + (1 + O(2^10))*y + O(2^10 * <x, y>)

            sage: g.lift_to_precision(9)
            (1 + O(2^9))*x*y + (1 + O(2^9))*x + (1 + O(2^9))*y + O(2^9 * <x, y>)

        In the next example, the precision on the coefficient is only lifted
        to ``O(2^10)`` because it is limited by the cap of the underlying
        `p`-adic ring::

            sage: g.lift_to_precision(20)
            (1 + O(2^10))*x*y + (1 + O(2^10))*x + (1 + O(2^10))*y + O(2^20 * <x, y>)"""
    @overload
    def lift_to_precision(self) -> Any:
        """TateAlgebraElement.lift_to_precision(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2326)

        Return a lift of this series at precision ``prec``.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); if
          ``None``, the cap of the parent is used if it is higher than
          the current precision

        EXAMPLES::

            sage: R = Zp(2, prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = R(1,4)*x*y + R(1,5)*x + R(1,8)*y
            sage: f
            (1 + O(2^4))*x*y + (1 + O(2^5))*x + (1 + O(2^8))*y

        This method lifts the precision of the coefficients::

            sage: f.lift_to_precision()
            (1 + O(2^10))*x*y + (1 + O(2^10))*x + (1 + O(2^10))*y

        and also acts on the global ``O(.)`` of the series::

            sage: g = f.add_bigoh(7)
            sage: g
            (1 + O(2^4))*x*y + (1 + O(2^5))*x + (1 + O(2^7))*y + O(2^7 * <x, y>)
            sage: g.lift_to_precision()
            (1 + O(2^10))*x*y + (1 + O(2^10))*x + (1 + O(2^10))*y + O(2^10 * <x, y>)

            sage: g.lift_to_precision(9)
            (1 + O(2^9))*x*y + (1 + O(2^9))*x + (1 + O(2^9))*y + O(2^9 * <x, y>)

        In the next example, the precision on the coefficient is only lifted
        to ``O(2^10)`` because it is limited by the cap of the underlying
        `p`-adic ring::

            sage: g.lift_to_precision(20)
            (1 + O(2^10))*x*y + (1 + O(2^10))*x + (1 + O(2^10))*y + O(2^20 * <x, y>)"""
    @overload
    def log(self, prec=...) -> Any:
        """TateAlgebraElement.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2489)

        Return the logarithm of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 3*x + 9*y^2
            sage: f.log()
            ...0000000010*x + ...0000000100*x^3 + ...1111111100*x^2 + ...0000000100*y^2
             + ...2222222000*x*y^2 + ... + O(3^10 * <x, y>)

            sage: f.log(prec=4)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(4); g
            ...0001 + ...0010*x + ...0100*y^2 + O(3^4 * <x, y>)
            sage: g.log()
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)
            sage: g.log(prec=10)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = 1 + x
            sage: f.log()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\log(1+x)` converges on a smaller disk::

            sage: f.restriction(-1).log()
            ...000000001*x + ...0000000.1*x^3 + ...111111*x^2 + ...
             + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 1 + 3 * A.random_element(integral=True)
            sage: logf = f.log()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).log() == logf(x0, y0)
            True

            sage: logf.exp() == f
            True"""
    @overload
    def log(self) -> Any:
        """TateAlgebraElement.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2489)

        Return the logarithm of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 3*x + 9*y^2
            sage: f.log()
            ...0000000010*x + ...0000000100*x^3 + ...1111111100*x^2 + ...0000000100*y^2
             + ...2222222000*x*y^2 + ... + O(3^10 * <x, y>)

            sage: f.log(prec=4)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(4); g
            ...0001 + ...0010*x + ...0100*y^2 + O(3^4 * <x, y>)
            sage: g.log()
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)
            sage: g.log(prec=10)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = 1 + x
            sage: f.log()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\log(1+x)` converges on a smaller disk::

            sage: f.restriction(-1).log()
            ...000000001*x + ...0000000.1*x^3 + ...111111*x^2 + ...
             + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 1 + 3 * A.random_element(integral=True)
            sage: logf = f.log()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).log() == logf(x0, y0)
            True

            sage: logf.exp() == f
            True"""
    @overload
    def log(self, prec=...) -> Any:
        """TateAlgebraElement.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2489)

        Return the logarithm of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 3*x + 9*y^2
            sage: f.log()
            ...0000000010*x + ...0000000100*x^3 + ...1111111100*x^2 + ...0000000100*y^2
             + ...2222222000*x*y^2 + ... + O(3^10 * <x, y>)

            sage: f.log(prec=4)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(4); g
            ...0001 + ...0010*x + ...0100*y^2 + O(3^4 * <x, y>)
            sage: g.log()
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)
            sage: g.log(prec=10)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = 1 + x
            sage: f.log()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\log(1+x)` converges on a smaller disk::

            sage: f.restriction(-1).log()
            ...000000001*x + ...0000000.1*x^3 + ...111111*x^2 + ...
             + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 1 + 3 * A.random_element(integral=True)
            sage: logf = f.log()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).log() == logf(x0, y0)
            True

            sage: logf.exp() == f
            True"""
    @overload
    def log(self) -> Any:
        """TateAlgebraElement.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2489)

        Return the logarithm of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 3*x + 9*y^2
            sage: f.log()
            ...0000000010*x + ...0000000100*x^3 + ...1111111100*x^2 + ...0000000100*y^2
             + ...2222222000*x*y^2 + ... + O(3^10 * <x, y>)

            sage: f.log(prec=4)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(4); g
            ...0001 + ...0010*x + ...0100*y^2 + O(3^4 * <x, y>)
            sage: g.log()
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)
            sage: g.log(prec=10)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = 1 + x
            sage: f.log()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\log(1+x)` converges on a smaller disk::

            sage: f.restriction(-1).log()
            ...000000001*x + ...0000000.1*x^3 + ...111111*x^2 + ...
             + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 1 + 3 * A.random_element(integral=True)
            sage: logf = f.log()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).log() == logf(x0, y0)
            True

            sage: logf.exp() == f
            True"""
    @overload
    def log(self, prec=...) -> Any:
        """TateAlgebraElement.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2489)

        Return the logarithm of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 3*x + 9*y^2
            sage: f.log()
            ...0000000010*x + ...0000000100*x^3 + ...1111111100*x^2 + ...0000000100*y^2
             + ...2222222000*x*y^2 + ... + O(3^10 * <x, y>)

            sage: f.log(prec=4)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(4); g
            ...0001 + ...0010*x + ...0100*y^2 + O(3^4 * <x, y>)
            sage: g.log()
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)
            sage: g.log(prec=10)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = 1 + x
            sage: f.log()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\log(1+x)` converges on a smaller disk::

            sage: f.restriction(-1).log()
            ...000000001*x + ...0000000.1*x^3 + ...111111*x^2 + ...
             + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 1 + 3 * A.random_element(integral=True)
            sage: logf = f.log()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).log() == logf(x0, y0)
            True

            sage: logf.exp() == f
            True"""
    @overload
    def log(self) -> Any:
        """TateAlgebraElement.log(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2489)

        Return the logarithm of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``); the
          absolute precision at which the result is computed, if ``None``
          the cap of the Tate algebra is used

        EXAMPLES::

            sage: R = Zp(3, 10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 3*x + 9*y^2
            sage: f.log()
            ...0000000010*x + ...0000000100*x^3 + ...1111111100*x^2 + ...0000000100*y^2
             + ...2222222000*x*y^2 + ... + O(3^10 * <x, y>)

            sage: f.log(prec=4)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        If the precision on the input is not enough to determine the
        result at precision ``prec``, a result with smaller precision
        is returned::

            sage: g = f.add_bigoh(4); g
            ...0001 + ...0010*x + ...0100*y^2 + O(3^4 * <x, y>)
            sage: g.log()
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)
            sage: g.log(prec=10)
            ...0010*x + ...0100*x^3 + ...1100*x^2 + ...0100*y^2 + ...2000*x*y^2
             + O(3^4 * <x, y>)

        When the input value is outside the domain of convergence, an
        error is raised::

            sage: f = 1 + x
            sage: f.log()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        However `\\log(1+x)` converges on a smaller disk::

            sage: f.restriction(-1).log()
            ...000000001*x + ...0000000.1*x^3 + ...111111*x^2 + ...
             + O(3^10 * <3*x, 3*y>)

        TESTS::

            sage: f = 1 + 3 * A.random_element(integral=True)
            sage: logf = f.log()

            sage: x0 = 3 * R.random_element()
            sage: y0 = 3 * R.random_element()
            sage: f(x0, y0).log() == logf(x0, y0)
            True

            sage: logf.exp() == f
            True"""
    @overload
    def monic(self) -> TateAlgebraElement:
        """TateAlgebraElement.monic(self) -> TateAlgebraElement

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2897)

        Return this series normalized so that it has valuation 0
        and its leading coefficient is a power of the uniformizer.

        EXAMPLES:

        When the log radii of convergence are all zero, the
        leading coefficient of the returned series is `1`::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R, order='lex')
            sage: f = 3*x^2*y^2 + 4*x^2*y^3 + y^5; f
            ...0000000011*x^2*y^2 + ...0000000001*y^5 + ...000000000100*x^2*y^3
            sage: f.monic()
            ...0000000001*x^2*y^2 + ...1010101011*y^5 + ...101010101100*x^2*y^3

        However, when log radii do not vanish, behaviors might
        be different::

            sage: g = f.restriction(-1); g
            ...0000000011*x^2*y^2 + ...0000000001*y^5 + ...000000000100*x^2*y^3
            sage: g.monic()
            ...000000.0001*x^2*y^2 + ...101010.1011*y^5 + ...10101010.11*x^2*y^3
            sage: g.monic().valuation()
            0

        TESTS::

            sage: A(0).monic()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero"""
    @overload
    def monic(self) -> Any:
        """TateAlgebraElement.monic(self) -> TateAlgebraElement

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2897)

        Return this series normalized so that it has valuation 0
        and its leading coefficient is a power of the uniformizer.

        EXAMPLES:

        When the log radii of convergence are all zero, the
        leading coefficient of the returned series is `1`::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R, order='lex')
            sage: f = 3*x^2*y^2 + 4*x^2*y^3 + y^5; f
            ...0000000011*x^2*y^2 + ...0000000001*y^5 + ...000000000100*x^2*y^3
            sage: f.monic()
            ...0000000001*x^2*y^2 + ...1010101011*y^5 + ...101010101100*x^2*y^3

        However, when log radii do not vanish, behaviors might
        be different::

            sage: g = f.restriction(-1); g
            ...0000000011*x^2*y^2 + ...0000000001*y^5 + ...000000000100*x^2*y^3
            sage: g.monic()
            ...000000.0001*x^2*y^2 + ...101010.1011*y^5 + ...10101010.11*x^2*y^3
            sage: g.monic().valuation()
            0

        TESTS::

            sage: A(0).monic()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero"""
    @overload
    def monic(self) -> Any:
        """TateAlgebraElement.monic(self) -> TateAlgebraElement

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2897)

        Return this series normalized so that it has valuation 0
        and its leading coefficient is a power of the uniformizer.

        EXAMPLES:

        When the log radii of convergence are all zero, the
        leading coefficient of the returned series is `1`::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R, order='lex')
            sage: f = 3*x^2*y^2 + 4*x^2*y^3 + y^5; f
            ...0000000011*x^2*y^2 + ...0000000001*y^5 + ...000000000100*x^2*y^3
            sage: f.monic()
            ...0000000001*x^2*y^2 + ...1010101011*y^5 + ...101010101100*x^2*y^3

        However, when log radii do not vanish, behaviors might
        be different::

            sage: g = f.restriction(-1); g
            ...0000000011*x^2*y^2 + ...0000000001*y^5 + ...000000000100*x^2*y^3
            sage: g.monic()
            ...000000.0001*x^2*y^2 + ...101010.1011*y^5 + ...10101010.11*x^2*y^3
            sage: g.monic().valuation()
            0

        TESTS::

            sage: A(0).monic()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero"""
    @overload
    def monic(self) -> Any:
        """TateAlgebraElement.monic(self) -> TateAlgebraElement

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2897)

        Return this series normalized so that it has valuation 0
        and its leading coefficient is a power of the uniformizer.

        EXAMPLES:

        When the log radii of convergence are all zero, the
        leading coefficient of the returned series is `1`::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R, order='lex')
            sage: f = 3*x^2*y^2 + 4*x^2*y^3 + y^5; f
            ...0000000011*x^2*y^2 + ...0000000001*y^5 + ...000000000100*x^2*y^3
            sage: f.monic()
            ...0000000001*x^2*y^2 + ...1010101011*y^5 + ...101010101100*x^2*y^3

        However, when log radii do not vanish, behaviors might
        be different::

            sage: g = f.restriction(-1); g
            ...0000000011*x^2*y^2 + ...0000000001*y^5 + ...000000000100*x^2*y^3
            sage: g.monic()
            ...000000.0001*x^2*y^2 + ...101010.1011*y^5 + ...10101010.11*x^2*y^3
            sage: g.monic().valuation()
            0

        TESTS::

            sage: A(0).monic()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero"""
    @overload
    def monic(self) -> Any:
        """TateAlgebraElement.monic(self) -> TateAlgebraElement

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2897)

        Return this series normalized so that it has valuation 0
        and its leading coefficient is a power of the uniformizer.

        EXAMPLES:

        When the log radii of convergence are all zero, the
        leading coefficient of the returned series is `1`::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R, order='lex')
            sage: f = 3*x^2*y^2 + 4*x^2*y^3 + y^5; f
            ...0000000011*x^2*y^2 + ...0000000001*y^5 + ...000000000100*x^2*y^3
            sage: f.monic()
            ...0000000001*x^2*y^2 + ...1010101011*y^5 + ...101010101100*x^2*y^3

        However, when log radii do not vanish, behaviors might
        be different::

            sage: g = f.restriction(-1); g
            ...0000000011*x^2*y^2 + ...0000000001*y^5 + ...000000000100*x^2*y^3
            sage: g.monic()
            ...000000.0001*x^2*y^2 + ...101010.1011*y^5 + ...10101010.11*x^2*y^3
            sage: g.monic().valuation()
            0

        TESTS::

            sage: A(0).monic()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: rational division by zero"""
    @overload
    def monomial_coefficients(self) -> Any:
        """TateAlgebraElement.monomial_coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2197)

        Return a dictionary whose keys are the exponents and whose values
        are the corresponding coefficients of this series.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x^2 + x
            sage: f.monomial_coefficients()
            {(1, 0): ...0000000001, (2, 0): ...00000000010}

        ``dict`` is an alias::

            sage: f.dict()
            {(1, 0): ...0000000001, (2, 0): ...00000000010}"""
    @overload
    def monomial_coefficients(self) -> Any:
        """TateAlgebraElement.monomial_coefficients(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2197)

        Return a dictionary whose keys are the exponents and whose values
        are the corresponding coefficients of this series.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x^2 + x
            sage: f.monomial_coefficients()
            {(1, 0): ...0000000001, (2, 0): ...00000000010}

        ``dict`` is an alias::

            sage: f.dict()
            {(1, 0): ...0000000001, (2, 0): ...00000000010}"""
    @overload
    def monomials(self) -> Any:
        """TateAlgebraElement.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2183)

        Return a list of the monomials of this series.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x^2 + x
            sage: f.monomials()  # indirect doctest
            [...0000000001*x, ...0000000001*x^2]"""
    @overload
    def monomials(self) -> Any:
        """TateAlgebraElement.monomials(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2183)

        Return a list of the monomials of this series.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x^2 + x
            sage: f.monomials()  # indirect doctest
            [...0000000001*x, ...0000000001*x^2]"""
    def nth_root(self, n=..., prec=...) -> Any:
        """TateAlgebraElement.nth_root(self, n=2, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1666)

        Return the `n`-th root of this series.

        INPUT:

        - ``n`` -- integer (default: `2`)

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the precision at which the result is computed, if ``None``,
          the result is truncated according to the cap of the parent

        .. NOTE::

            The `n`-th root is computed as `\\exp(\\frac 1 n \\log(f))`.

        EXAMPLES::

            sage: R = Zp(3, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 9*x^2 + 9*y^2
            sage: g = f.nth_root(3, prec=3); g
            ...001 + ...010*x^2 + ...010*y^2 + ...200*x^6 + ...200*y^6 + ...200*x^4
             + ...100*x^2*y^2 + ...200*y^4 + O(3^3 * <x, y>)
            sage: g^3 == f
            True

            sage: for n in range(2, 9):
            ....:     if f.nth_root(n)^n != f: raise RuntimeError

        It's possible that `f` has a trivial ``n``-th root (which is analytic on
        the correct domain) but that `\\exp(\\frac 1 n \\log(f))` does not converge.
        In this case, an error is raised::

            sage: f = x^3
            sage: f.nth_root(3)
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence"""
    @overload
    def precision_absolute(self) -> Any:
        """TateAlgebraElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2384)

        Return the maximal precision at which a term of this series is known.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x + 2*x^2; f
            ...0000000001*x + ...00000000010*x^2
            sage: f.precision_absolute()
            +Infinity

            sage: g = f.add_bigoh(5); g
            ...00001*x + ...00010*x^2 + O(2^5 * <x, y>)
            sage: g.precision_absolute()
            5

        The absolute precision may be higher than the precision of some
        individual coefficients::

            sage: g = f.add_bigoh(20); g
            ...0000000001*x + ...00000000010*x^2 + O(2^20 * <x, y>)
            sage: g.precision_absolute()
            20"""
    @overload
    def precision_absolute(self) -> Any:
        """TateAlgebraElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2384)

        Return the maximal precision at which a term of this series is known.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x + 2*x^2; f
            ...0000000001*x + ...00000000010*x^2
            sage: f.precision_absolute()
            +Infinity

            sage: g = f.add_bigoh(5); g
            ...00001*x + ...00010*x^2 + O(2^5 * <x, y>)
            sage: g.precision_absolute()
            5

        The absolute precision may be higher than the precision of some
        individual coefficients::

            sage: g = f.add_bigoh(20); g
            ...0000000001*x + ...00000000010*x^2 + O(2^20 * <x, y>)
            sage: g.precision_absolute()
            20"""
    @overload
    def precision_absolute(self) -> Any:
        """TateAlgebraElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2384)

        Return the maximal precision at which a term of this series is known.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x + 2*x^2; f
            ...0000000001*x + ...00000000010*x^2
            sage: f.precision_absolute()
            +Infinity

            sage: g = f.add_bigoh(5); g
            ...00001*x + ...00010*x^2 + O(2^5 * <x, y>)
            sage: g.precision_absolute()
            5

        The absolute precision may be higher than the precision of some
        individual coefficients::

            sage: g = f.add_bigoh(20); g
            ...0000000001*x + ...00000000010*x^2 + O(2^20 * <x, y>)
            sage: g.precision_absolute()
            20"""
    @overload
    def precision_absolute(self) -> Any:
        """TateAlgebraElement.precision_absolute(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2384)

        Return the maximal precision at which a term of this series is known.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x + 2*x^2; f
            ...0000000001*x + ...00000000010*x^2
            sage: f.precision_absolute()
            +Infinity

            sage: g = f.add_bigoh(5); g
            ...00001*x + ...00010*x^2 + O(2^5 * <x, y>)
            sage: g.precision_absolute()
            5

        The absolute precision may be higher than the precision of some
        individual coefficients::

            sage: g = f.add_bigoh(20); g
            ...0000000001*x + ...00000000010*x^2 + O(2^20 * <x, y>)
            sage: g.precision_absolute()
            20"""
    @overload
    def precision_relative(self) -> Any:
        """TateAlgebraElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2454)

        Return the relative precision of this series.

        The relative precision is defined as the difference
        between the absolute precision and the valuation.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R.fraction_field())
            sage: f = x^4 + 4*x*y + 1; f
            ...0000000001*x^4 + ...0000000001 + ...000000000100*x*y
            sage: f.precision_relative()
            +Infinity

            sage: g = f.add_bigoh(5)
            sage: g.precision_relative()
            5
            sage: g.precision_absolute()
            5
            sage: g.valuation()
            0

            sage: h = g + 1/2 ; h
            ...00001.1 + ...00001*x^4 + ...00100*x*y + O(2^5 * <x, y>)
            sage: h.precision_relative()
            6
            sage: h.precision_absolute()
            5
            sage: h.valuation()
            -1"""
    @overload
    def precision_relative(self) -> Any:
        """TateAlgebraElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2454)

        Return the relative precision of this series.

        The relative precision is defined as the difference
        between the absolute precision and the valuation.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R.fraction_field())
            sage: f = x^4 + 4*x*y + 1; f
            ...0000000001*x^4 + ...0000000001 + ...000000000100*x*y
            sage: f.precision_relative()
            +Infinity

            sage: g = f.add_bigoh(5)
            sage: g.precision_relative()
            5
            sage: g.precision_absolute()
            5
            sage: g.valuation()
            0

            sage: h = g + 1/2 ; h
            ...00001.1 + ...00001*x^4 + ...00100*x*y + O(2^5 * <x, y>)
            sage: h.precision_relative()
            6
            sage: h.precision_absolute()
            5
            sage: h.valuation()
            -1"""
    @overload
    def precision_relative(self) -> Any:
        """TateAlgebraElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2454)

        Return the relative precision of this series.

        The relative precision is defined as the difference
        between the absolute precision and the valuation.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R.fraction_field())
            sage: f = x^4 + 4*x*y + 1; f
            ...0000000001*x^4 + ...0000000001 + ...000000000100*x*y
            sage: f.precision_relative()
            +Infinity

            sage: g = f.add_bigoh(5)
            sage: g.precision_relative()
            5
            sage: g.precision_absolute()
            5
            sage: g.valuation()
            0

            sage: h = g + 1/2 ; h
            ...00001.1 + ...00001*x^4 + ...00100*x*y + O(2^5 * <x, y>)
            sage: h.precision_relative()
            6
            sage: h.precision_absolute()
            5
            sage: h.valuation()
            -1"""
    @overload
    def precision_relative(self) -> Any:
        """TateAlgebraElement.precision_relative(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2454)

        Return the relative precision of this series.

        The relative precision is defined as the difference
        between the absolute precision and the valuation.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R.fraction_field())
            sage: f = x^4 + 4*x*y + 1; f
            ...0000000001*x^4 + ...0000000001 + ...000000000100*x*y
            sage: f.precision_relative()
            +Infinity

            sage: g = f.add_bigoh(5)
            sage: g.precision_relative()
            5
            sage: g.precision_absolute()
            5
            sage: g.valuation()
            0

            sage: h = g + 1/2 ; h
            ...00001.1 + ...00001*x^4 + ...00100*x*y + O(2^5 * <x, y>)
            sage: h.precision_relative()
            6
            sage: h.precision_absolute()
            5
            sage: h.valuation()
            -1"""
    @overload
    def quo_rem(self, divisors) -> Any:
        """TateAlgebraElement.quo_rem(self, divisors)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3249)

        Return the quotient(s) and the remainder of the division of
        this series by ``divisors``.

        INPUT:

        - ``divisors`` -- a series, or a list of series

        NOTE:

        The condition on the remainder is that it has

        - no term which is greater than the leading term of the
          numerator and

        - no term which is divisible by the leading term of one
          divisor.

        EXAMPLES::

            sage: R = Zp(2, 5, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 2*x*y + 3*x^2*y + 4*x*y^2
            sage: g = x^2
            sage: q, r = f.quo_rem(g)
            sage: q
            ...00011*y
            sage: r
            ...00001 + ...00010*x*y + ...00100*x*y^2 + O(2^5 * <x, y>)
            sage: f == g*q + r
            True

        We can also divide by a family of divisors::

            sage: g0 = x^2
            sage: g1 = x*y + 2*x
            sage: q, r = f.quo_rem([g0, g1])
            sage: q
            [...00011*y, ...11010 + ...00100*y]
            sage: r
            ...00001 + ...01100*x + O(2^5 * <x, y>)
            sage: f == g0*q[0] + g1*q[1] + r
            True"""
    @overload
    def quo_rem(self, g) -> Any:
        """TateAlgebraElement.quo_rem(self, divisors)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3249)

        Return the quotient(s) and the remainder of the division of
        this series by ``divisors``.

        INPUT:

        - ``divisors`` -- a series, or a list of series

        NOTE:

        The condition on the remainder is that it has

        - no term which is greater than the leading term of the
          numerator and

        - no term which is divisible by the leading term of one
          divisor.

        EXAMPLES::

            sage: R = Zp(2, 5, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 2*x*y + 3*x^2*y + 4*x*y^2
            sage: g = x^2
            sage: q, r = f.quo_rem(g)
            sage: q
            ...00011*y
            sage: r
            ...00001 + ...00010*x*y + ...00100*x*y^2 + O(2^5 * <x, y>)
            sage: f == g*q + r
            True

        We can also divide by a family of divisors::

            sage: g0 = x^2
            sage: g1 = x*y + 2*x
            sage: q, r = f.quo_rem([g0, g1])
            sage: q
            [...00011*y, ...11010 + ...00100*y]
            sage: r
            ...00001 + ...01100*x + O(2^5 * <x, y>)
            sage: f == g0*q[0] + g1*q[1] + r
            True"""
    @overload
    def reduce(self, I) -> Any:
        """TateAlgebraElement.reduce(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3350)

        Return a canonical representative of this series in the
        quotient of the Tate algebra (in which this series lives)
        by the ideal ``I``.

        EXAMPLES::

            sage: R = Zp(3, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 3*x^2 + 5*x*y^2
            sage: g = 5*x^2*y + 3
            sage: I = A.ideal([f, g])

            sage: f.reduce(I)
            O(3^9 * <x, y>)
            sage: h = (x^2 + 2*y)*f + (x^2*y^3 + 3*x*y^2 + 7)*g + 1
            sage: h.reduce(I)
            ...000000001 + O(3^9 * <x, y>)

        TESTS::

            sage: s = I.random_element(integral=True)
            sage: s.reduce(I).precision_absolute() >= 9
            True

            sage: h = A.random_element()
            sage: (h + s).reduce(I) == h.reduce(I)
            True"""
    @overload
    def reduce(self, I) -> Any:
        """TateAlgebraElement.reduce(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3350)

        Return a canonical representative of this series in the
        quotient of the Tate algebra (in which this series lives)
        by the ideal ``I``.

        EXAMPLES::

            sage: R = Zp(3, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 3*x^2 + 5*x*y^2
            sage: g = 5*x^2*y + 3
            sage: I = A.ideal([f, g])

            sage: f.reduce(I)
            O(3^9 * <x, y>)
            sage: h = (x^2 + 2*y)*f + (x^2*y^3 + 3*x*y^2 + 7)*g + 1
            sage: h.reduce(I)
            ...000000001 + O(3^9 * <x, y>)

        TESTS::

            sage: s = I.random_element(integral=True)
            sage: s.reduce(I).precision_absolute() >= 9
            True

            sage: h = A.random_element()
            sage: (h + s).reduce(I) == h.reduce(I)
            True"""
    @overload
    def reduce(self, I) -> Any:
        """TateAlgebraElement.reduce(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3350)

        Return a canonical representative of this series in the
        quotient of the Tate algebra (in which this series lives)
        by the ideal ``I``.

        EXAMPLES::

            sage: R = Zp(3, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 3*x^2 + 5*x*y^2
            sage: g = 5*x^2*y + 3
            sage: I = A.ideal([f, g])

            sage: f.reduce(I)
            O(3^9 * <x, y>)
            sage: h = (x^2 + 2*y)*f + (x^2*y^3 + 3*x*y^2 + 7)*g + 1
            sage: h.reduce(I)
            ...000000001 + O(3^9 * <x, y>)

        TESTS::

            sage: s = I.random_element(integral=True)
            sage: s.reduce(I).precision_absolute() >= 9
            True

            sage: h = A.random_element()
            sage: (h + s).reduce(I) == h.reduce(I)
            True"""
    @overload
    def reduce(self, I) -> Any:
        """TateAlgebraElement.reduce(self, I)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3350)

        Return a canonical representative of this series in the
        quotient of the Tate algebra (in which this series lives)
        by the ideal ``I``.

        EXAMPLES::

            sage: R = Zp(3, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 3*x^2 + 5*x*y^2
            sage: g = 5*x^2*y + 3
            sage: I = A.ideal([f, g])

            sage: f.reduce(I)
            O(3^9 * <x, y>)
            sage: h = (x^2 + 2*y)*f + (x^2*y^3 + 3*x*y^2 + 7)*g + 1
            sage: h.reduce(I)
            ...000000001 + O(3^9 * <x, y>)

        TESTS::

            sage: s = I.random_element(integral=True)
            sage: s.reduce(I).precision_absolute() >= 9
            True

            sage: h = A.random_element()
            sage: (h + s).reduce(I) == h.reduce(I)
            True"""
    @overload
    def residue(self, n=...) -> Any:
        """TateAlgebraElement.residue(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3052)

        Return this series modulo the ``n``-th power of the uniformizer.

        Note that by definition of Tate series, the output is a polynomial.

        INPUT:

        - ``n`` -- integer (default: `1`)

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^2 + y^2 + 6*x^3 + 3*y
            sage: f.residue()
            x^2 + y^2 + y
            sage: f.residue().parent()
            Multivariate Polynomial Ring in x, y over Finite Field of size 2

            sage: f.residue(2)
            2*x^3 + x^2 + y^2 - y
            sage: f.residue(2).parent()
            Multivariate Polynomial Ring in x, y over Ring of integers modulo 4

        The residue can only be computed for series with nonnegative valuation.

            sage: g = f >> 2; g
            ...00000000.01*x^2 + ...00000000.01*y^2 + ...00000000.11*y + ...000000001.1*x^3
            sage: g.residue()
            Traceback (most recent call last):
            ...
            ValueError: element must have nonnegative valuation in order to compute residue

        The residue is not implemented for series with convergence radius different from 1.

            sage: A.<x,y> = TateAlgebra(R, log_radii=(2,-1))
            sage: f = x^2 + y^2 + 6*x^3 + 3*y
            sage: f.residue()
            Traceback (most recent call last):
            ...
            NotImplementedError: residues are only implemented for radius 1"""
    @overload
    def residue(self) -> Any:
        """TateAlgebraElement.residue(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3052)

        Return this series modulo the ``n``-th power of the uniformizer.

        Note that by definition of Tate series, the output is a polynomial.

        INPUT:

        - ``n`` -- integer (default: `1`)

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^2 + y^2 + 6*x^3 + 3*y
            sage: f.residue()
            x^2 + y^2 + y
            sage: f.residue().parent()
            Multivariate Polynomial Ring in x, y over Finite Field of size 2

            sage: f.residue(2)
            2*x^3 + x^2 + y^2 - y
            sage: f.residue(2).parent()
            Multivariate Polynomial Ring in x, y over Ring of integers modulo 4

        The residue can only be computed for series with nonnegative valuation.

            sage: g = f >> 2; g
            ...00000000.01*x^2 + ...00000000.01*y^2 + ...00000000.11*y + ...000000001.1*x^3
            sage: g.residue()
            Traceback (most recent call last):
            ...
            ValueError: element must have nonnegative valuation in order to compute residue

        The residue is not implemented for series with convergence radius different from 1.

            sage: A.<x,y> = TateAlgebra(R, log_radii=(2,-1))
            sage: f = x^2 + y^2 + 6*x^3 + 3*y
            sage: f.residue()
            Traceback (most recent call last):
            ...
            NotImplementedError: residues are only implemented for radius 1"""
    @overload
    def residue(self) -> Any:
        """TateAlgebraElement.residue(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3052)

        Return this series modulo the ``n``-th power of the uniformizer.

        Note that by definition of Tate series, the output is a polynomial.

        INPUT:

        - ``n`` -- integer (default: `1`)

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^2 + y^2 + 6*x^3 + 3*y
            sage: f.residue()
            x^2 + y^2 + y
            sage: f.residue().parent()
            Multivariate Polynomial Ring in x, y over Finite Field of size 2

            sage: f.residue(2)
            2*x^3 + x^2 + y^2 - y
            sage: f.residue(2).parent()
            Multivariate Polynomial Ring in x, y over Ring of integers modulo 4

        The residue can only be computed for series with nonnegative valuation.

            sage: g = f >> 2; g
            ...00000000.01*x^2 + ...00000000.01*y^2 + ...00000000.11*y + ...000000001.1*x^3
            sage: g.residue()
            Traceback (most recent call last):
            ...
            ValueError: element must have nonnegative valuation in order to compute residue

        The residue is not implemented for series with convergence radius different from 1.

            sage: A.<x,y> = TateAlgebra(R, log_radii=(2,-1))
            sage: f = x^2 + y^2 + 6*x^3 + 3*y
            sage: f.residue()
            Traceback (most recent call last):
            ...
            NotImplementedError: residues are only implemented for radius 1"""
    @overload
    def residue(self) -> Any:
        """TateAlgebraElement.residue(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3052)

        Return this series modulo the ``n``-th power of the uniformizer.

        Note that by definition of Tate series, the output is a polynomial.

        INPUT:

        - ``n`` -- integer (default: `1`)

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^2 + y^2 + 6*x^3 + 3*y
            sage: f.residue()
            x^2 + y^2 + y
            sage: f.residue().parent()
            Multivariate Polynomial Ring in x, y over Finite Field of size 2

            sage: f.residue(2)
            2*x^3 + x^2 + y^2 - y
            sage: f.residue(2).parent()
            Multivariate Polynomial Ring in x, y over Ring of integers modulo 4

        The residue can only be computed for series with nonnegative valuation.

            sage: g = f >> 2; g
            ...00000000.01*x^2 + ...00000000.01*y^2 + ...00000000.11*y + ...000000001.1*x^3
            sage: g.residue()
            Traceback (most recent call last):
            ...
            ValueError: element must have nonnegative valuation in order to compute residue

        The residue is not implemented for series with convergence radius different from 1.

            sage: A.<x,y> = TateAlgebra(R, log_radii=(2,-1))
            sage: f = x^2 + y^2 + 6*x^3 + 3*y
            sage: f.residue()
            Traceback (most recent call last):
            ...
            NotImplementedError: residues are only implemented for radius 1"""
    @overload
    def residue(self) -> Any:
        """TateAlgebraElement.residue(self, n=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3052)

        Return this series modulo the ``n``-th power of the uniformizer.

        Note that by definition of Tate series, the output is a polynomial.

        INPUT:

        - ``n`` -- integer (default: `1`)

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^2 + y^2 + 6*x^3 + 3*y
            sage: f.residue()
            x^2 + y^2 + y
            sage: f.residue().parent()
            Multivariate Polynomial Ring in x, y over Finite Field of size 2

            sage: f.residue(2)
            2*x^3 + x^2 + y^2 - y
            sage: f.residue(2).parent()
            Multivariate Polynomial Ring in x, y over Ring of integers modulo 4

        The residue can only be computed for series with nonnegative valuation.

            sage: g = f >> 2; g
            ...00000000.01*x^2 + ...00000000.01*y^2 + ...00000000.11*y + ...000000001.1*x^3
            sage: g.residue()
            Traceback (most recent call last):
            ...
            ValueError: element must have nonnegative valuation in order to compute residue

        The residue is not implemented for series with convergence radius different from 1.

            sage: A.<x,y> = TateAlgebra(R, log_radii=(2,-1))
            sage: f = x^2 + y^2 + 6*x^3 + 3*y
            sage: f.residue()
            Traceback (most recent call last):
            ...
            NotImplementedError: residues are only implemented for radius 1"""
    def restriction(self, log_radii) -> Any:
        """TateAlgebraElement.restriction(self, log_radii)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2089)

        Return the restriction of this series to a smaller domain.

        INPUT:

        - ``log_radii`` -- integer or a tuple; the log-radii of
          convergence of the smaller domain (see :class:`TateAlgebra`
          for more details)

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x + y^2; f
            ...0000000001*y^2 + ...00000000010*x

            sage: g = f.restriction(-1); g
            ...0000000001*y^2 + ...00000000010*x
            sage: g.parent()
            Tate Algebra in x (val >= 1), y (val >= 1)
             over 2-adic Field with capped relative precision 10

        Note that restricting may change the order of the terms::

            sage: f.restriction([-1,-2])
            ...00000000010*x + ...0000000001*y^2"""
    @overload
    def sqrt(self, prec=...) -> Any:
        """TateAlgebraElement.sqrt(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1627)

        Return the square root of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the precision at which the result is computed, if ``None``,
          the result is truncated according to the cap of the parent

        EXAMPLES::

            sage: R = Zp(3, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 6*x^2 + 9*y^2
            sage: g = f.sqrt(); g
            ...0000000001 + ...0000000010*x^2 + ...1111111100*x^4 + ...1111111200*y^2
             + ...1111112000*x^6 + ...1111111000*x^2*y^2 + ... + O(3^10 * <x, y>)

            sage: f.sqrt(prec=4)
            ...0001 + ...0010*x^2 + ...1100*x^4 + ...1200*y^2 + ...2000*x^6
             + ...1000*x^2*y^2 + O(3^4 * <x, y>)

            sage: g^2 == f
            True

        It's possible that `f` has a trivial square root (which is analytic on
        the correct domain) but that it takes its values outside the domain of
        convergence of the square root function.
        In this case, an error is raised::

            sage: f = x^2
            sage: f.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence"""
    @overload
    def sqrt(self) -> Any:
        """TateAlgebraElement.sqrt(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1627)

        Return the square root of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the precision at which the result is computed, if ``None``,
          the result is truncated according to the cap of the parent

        EXAMPLES::

            sage: R = Zp(3, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 6*x^2 + 9*y^2
            sage: g = f.sqrt(); g
            ...0000000001 + ...0000000010*x^2 + ...1111111100*x^4 + ...1111111200*y^2
             + ...1111112000*x^6 + ...1111111000*x^2*y^2 + ... + O(3^10 * <x, y>)

            sage: f.sqrt(prec=4)
            ...0001 + ...0010*x^2 + ...1100*x^4 + ...1200*y^2 + ...2000*x^6
             + ...1000*x^2*y^2 + O(3^4 * <x, y>)

            sage: g^2 == f
            True

        It's possible that `f` has a trivial square root (which is analytic on
        the correct domain) but that it takes its values outside the domain of
        convergence of the square root function.
        In this case, an error is raised::

            sage: f = x^2
            sage: f.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence"""
    @overload
    def sqrt(self, prec=...) -> Any:
        """TateAlgebraElement.sqrt(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1627)

        Return the square root of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the precision at which the result is computed, if ``None``,
          the result is truncated according to the cap of the parent

        EXAMPLES::

            sage: R = Zp(3, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 6*x^2 + 9*y^2
            sage: g = f.sqrt(); g
            ...0000000001 + ...0000000010*x^2 + ...1111111100*x^4 + ...1111111200*y^2
             + ...1111112000*x^6 + ...1111111000*x^2*y^2 + ... + O(3^10 * <x, y>)

            sage: f.sqrt(prec=4)
            ...0001 + ...0010*x^2 + ...1100*x^4 + ...1200*y^2 + ...2000*x^6
             + ...1000*x^2*y^2 + O(3^4 * <x, y>)

            sage: g^2 == f
            True

        It's possible that `f` has a trivial square root (which is analytic on
        the correct domain) but that it takes its values outside the domain of
        convergence of the square root function.
        In this case, an error is raised::

            sage: f = x^2
            sage: f.sqrt()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence"""
    @overload
    def square_root(self, prec=...) -> Any:
        """TateAlgebraElement.square_root(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1588)

        Return the square root of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the precision at which the result is computed, if ``None``,
          the result is truncated according to the cap of the parent

        EXAMPLES::

            sage: R = Zp(3, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 6*x^2 + 9*y^2
            sage: g = f.sqrt(); g
            ...0000000001 + ...0000000010*x^2 + ...1111111100*x^4 + ...1111111200*y^2
             + ...1111112000*x^6 + ...1111111000*x^2*y^2 + ... + O(3^10 * <x, y>)

            sage: f.square_root(prec=4)
            ...0001 + ...0010*x^2 + ...1100*x^4 + ...1200*y^2 + ...2000*x^6
             + ...1000*x^2*y^2 + O(3^4 * <x, y>)

            sage: g^2 == f
            True

        It's possible that `f` has a trivial square root (which is analytic on
        the correct domain) but that it takes its values outside the domain of
        convergence of the square root function.
        In this case, an error is raised::

            sage: f = x^2
            sage: f.square_root()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence"""
    @overload
    def square_root(self, prec=...) -> Any:
        """TateAlgebraElement.square_root(self, prec=None)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1588)

        Return the square root of this series.

        INPUT:

        - ``prec`` -- integer or ``None`` (default: ``None``);
          the precision at which the result is computed, if ``None``,
          the result is truncated according to the cap of the parent

        EXAMPLES::

            sage: R = Zp(3, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 6*x^2 + 9*y^2
            sage: g = f.sqrt(); g
            ...0000000001 + ...0000000010*x^2 + ...1111111100*x^4 + ...1111111200*y^2
             + ...1111112000*x^6 + ...1111111000*x^2*y^2 + ... + O(3^10 * <x, y>)

            sage: f.square_root(prec=4)
            ...0001 + ...0010*x^2 + ...1100*x^4 + ...1200*y^2 + ...2000*x^6
             + ...1000*x^2*y^2 + O(3^4 * <x, y>)

            sage: g^2 == f
            True

        It's possible that `f` has a trivial square root (which is analytic on
        the correct domain) but that it takes its values outside the domain of
        convergence of the square root function.
        In this case, an error is raised::

            sage: f = x^2
            sage: f.square_root()
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence"""
    @overload
    def terms(self) -> Any:
        """TateAlgebraElement.terms(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2123)

        Return a list of the terms of this series sorted in descending order.

        .. NOTE::

            The order on the terms is defined as follows: first we
            compare the valuation and, in case of equality, we compare
            the monomials with respect to the order given at the
            creation of the parent.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x^2 + x
            sage: f.terms()
            [...0000000001*x, ...00000000010*x^2]"""
    @overload
    def terms(self) -> Any:
        """TateAlgebraElement.terms(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2123)

        Return a list of the terms of this series sorted in descending order.

        .. NOTE::

            The order on the terms is defined as follows: first we
            compare the valuation and, in case of equality, we compare
            the monomials with respect to the order given at the
            creation of the parent.

        EXAMPLES::

            sage: R = Zp(2, prec=10, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x^2 + x
            sage: f.terms()
            [...0000000001*x, ...00000000010*x^2]"""
    @overload
    def valuation(self) -> Any:
        """TateAlgebraElement.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2412)

        Return the valuation of this series.

        .. NOTE::

            The valuation of a series `f` is defined as the minimal
            valuation of `f(x)` for `x` varying in the domain of convergence
            (specified in the parent).

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + 4*x*y + 1; f
            ...0000000001*x^4 + ...0000000001 + ...000000000100*x*y
            sage: f.valuation()
            0

            sage: g = 2*f; g
            ...00000000010*x^4 + ...00000000010 + ...0000000001000*x*y
            sage: g.valuation()
            1

        When the radius of convergence is not 1, the variables themselves
        have a nontrivial valuation::

            sage: A.<x,y> = TateAlgebra(R, log_radii=(1,2))
            sage: x.valuation()
            -1
            sage: y.valuation()
            -2

            sage: f = x^4 + 4*x*y + 1
            sage: f.valuation()
            -4"""
    @overload
    def valuation(self) -> Any:
        """TateAlgebraElement.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2412)

        Return the valuation of this series.

        .. NOTE::

            The valuation of a series `f` is defined as the minimal
            valuation of `f(x)` for `x` varying in the domain of convergence
            (specified in the parent).

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + 4*x*y + 1; f
            ...0000000001*x^4 + ...0000000001 + ...000000000100*x*y
            sage: f.valuation()
            0

            sage: g = 2*f; g
            ...00000000010*x^4 + ...00000000010 + ...0000000001000*x*y
            sage: g.valuation()
            1

        When the radius of convergence is not 1, the variables themselves
        have a nontrivial valuation::

            sage: A.<x,y> = TateAlgebra(R, log_radii=(1,2))
            sage: x.valuation()
            -1
            sage: y.valuation()
            -2

            sage: f = x^4 + 4*x*y + 1
            sage: f.valuation()
            -4"""
    @overload
    def valuation(self) -> Any:
        """TateAlgebraElement.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2412)

        Return the valuation of this series.

        .. NOTE::

            The valuation of a series `f` is defined as the minimal
            valuation of `f(x)` for `x` varying in the domain of convergence
            (specified in the parent).

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + 4*x*y + 1; f
            ...0000000001*x^4 + ...0000000001 + ...000000000100*x*y
            sage: f.valuation()
            0

            sage: g = 2*f; g
            ...00000000010*x^4 + ...00000000010 + ...0000000001000*x*y
            sage: g.valuation()
            1

        When the radius of convergence is not 1, the variables themselves
        have a nontrivial valuation::

            sage: A.<x,y> = TateAlgebra(R, log_radii=(1,2))
            sage: x.valuation()
            -1
            sage: y.valuation()
            -2

            sage: f = x^4 + 4*x*y + 1
            sage: f.valuation()
            -4"""
    @overload
    def valuation(self) -> Any:
        """TateAlgebraElement.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2412)

        Return the valuation of this series.

        .. NOTE::

            The valuation of a series `f` is defined as the minimal
            valuation of `f(x)` for `x` varying in the domain of convergence
            (specified in the parent).

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + 4*x*y + 1; f
            ...0000000001*x^4 + ...0000000001 + ...000000000100*x*y
            sage: f.valuation()
            0

            sage: g = 2*f; g
            ...00000000010*x^4 + ...00000000010 + ...0000000001000*x*y
            sage: g.valuation()
            1

        When the radius of convergence is not 1, the variables themselves
        have a nontrivial valuation::

            sage: A.<x,y> = TateAlgebra(R, log_radii=(1,2))
            sage: x.valuation()
            -1
            sage: y.valuation()
            -2

            sage: f = x^4 + 4*x*y + 1
            sage: f.valuation()
            -4"""
    @overload
    def valuation(self) -> Any:
        """TateAlgebraElement.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2412)

        Return the valuation of this series.

        .. NOTE::

            The valuation of a series `f` is defined as the minimal
            valuation of `f(x)` for `x` varying in the domain of convergence
            (specified in the parent).

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + 4*x*y + 1; f
            ...0000000001*x^4 + ...0000000001 + ...000000000100*x*y
            sage: f.valuation()
            0

            sage: g = 2*f; g
            ...00000000010*x^4 + ...00000000010 + ...0000000001000*x*y
            sage: g.valuation()
            1

        When the radius of convergence is not 1, the variables themselves
        have a nontrivial valuation::

            sage: A.<x,y> = TateAlgebra(R, log_radii=(1,2))
            sage: x.valuation()
            -1
            sage: y.valuation()
            -2

            sage: f = x^4 + 4*x*y + 1
            sage: f.valuation()
            -4"""
    @overload
    def valuation(self) -> Any:
        """TateAlgebraElement.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2412)

        Return the valuation of this series.

        .. NOTE::

            The valuation of a series `f` is defined as the minimal
            valuation of `f(x)` for `x` varying in the domain of convergence
            (specified in the parent).

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^4 + 4*x*y + 1; f
            ...0000000001*x^4 + ...0000000001 + ...000000000100*x*y
            sage: f.valuation()
            0

            sage: g = 2*f; g
            ...00000000010*x^4 + ...00000000010 + ...0000000001000*x*y
            sage: g.valuation()
            1

        When the radius of convergence is not 1, the variables themselves
        have a nontrivial valuation::

            sage: A.<x,y> = TateAlgebra(R, log_radii=(1,2))
            sage: x.valuation()
            -1
            sage: y.valuation()
            -2

            sage: f = x^4 + 4*x*y + 1
            sage: f.valuation()
            -4"""
    @overload
    def weierstrass_degree(self) -> Any:
        """TateAlgebraElement.weierstrass_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2970)

        Return the Weierstrass degree of this Tate series.

        .. NOTE::

            The Weierstrass degree is the total degree of the polynomial
            defined by the terms with least valuation in the series.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x*y + 2*x^4 + y; f
            ...0000000001*x*y + ...0000000001*y + ...00000000010*x^4
            sage: f.weierstrass_degree()
            2"""
    @overload
    def weierstrass_degree(self) -> Any:
        """TateAlgebraElement.weierstrass_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2970)

        Return the Weierstrass degree of this Tate series.

        .. NOTE::

            The Weierstrass degree is the total degree of the polynomial
            defined by the terms with least valuation in the series.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x*y + 2*x^4 + y; f
            ...0000000001*x*y + ...0000000001*y + ...00000000010*x^4
            sage: f.weierstrass_degree()
            2"""
    @overload
    def weierstrass_degrees(self) -> Any:
        """TateAlgebraElement.weierstrass_degrees(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3011)

        Return the Weierstrass degrees of this Tate series.

        .. NOTE::

            The Weierstrass degrees are the partial degrees of the polynomial
            defined by the terms with least valuation in the series.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits',prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^2 + y^2 + 2*x^3 + y; f
            ...0000000001*x^2 + ...0000000001*y^2 + ...0000000001*y + ...00000000010*x^3
            sage: f.weierstrass_degrees()
            (2, 2)"""
    @overload
    def weierstrass_degrees(self) -> Any:
        """TateAlgebraElement.weierstrass_degrees(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3011)

        Return the Weierstrass degrees of this Tate series.

        .. NOTE::

            The Weierstrass degrees are the partial degrees of the polynomial
            defined by the terms with least valuation in the series.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits',prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x^2 + y^2 + 2*x^3 + y; f
            ...0000000001*x^2 + ...0000000001*y^2 + ...0000000001*y + ...00000000010*x^3
            sage: f.weierstrass_degrees()
            (2, 2)"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *args) -> Any:
        """TateAlgebraElement.__call__(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1812)

        Return this term evaluated at ``args``.

        INPUT:

        - ``args`` -- elements

        EXAMPLES::

            sage: R = Zp(2)
            sage: A.<u,v> = TateAlgebra(R, log_radii=[0,-1])
            sage: A
            Tate Algebra in u (val >= 0), v (val >= 1) over 2-adic Field with capped relative precision 20

            sage: f = u^2 + v^2
            sage: f(1, 0)
            1 + O(2^20)

        An error is raised if we ask for the evaluation at one
        point which is outside the domain of convergence::

            sage: f(1, 1)
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        Evaluation at points in extensions is allowed::

            sage: S.<a> = Zq(2^3)
            sage: f(a, 2)
            a^2 + 2^2 + O(2^20)

            sage: x = polygen(ZZ, 'x')
            sage: T.<pi> = S.extension(x^2 - 2)
            sage: f(pi, 2)
            pi^2 + pi^4 + O(pi^42)

            sage: f(pi, pi)
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        This method can also be used to compose Tate series::

            sage: f(u + v, 2*u)
            (1 + 2^2 + O(2^20))*u^2 + (2 + O(2^20))*u*v + (1 + O(2^20))*v^2

        or for partial evaluation::

            sage: f(pi, v)
            (pi^2 + O(pi^42)) + (1 + O(pi^40))*v^2"""
    def __floordiv__(self, divisors) -> Any:
        """TateAlgebraElement.__floordiv__(self, divisors)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3323)

        Return the quotient(s) of the division of this series by
        ``divisors``.

        INPUT:

        - ``divisors`` -- a series, or a list of series

        EXAMPLES::

            sage: R = Zp(2, 5, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 2*x*y + 3*x^2*y + 4*x*y^2
            sage: g = x^2
            sage: f // g
            ...00011*y

        We can also divide by a family of divisors::

            sage: g0 = x^2
            sage: g1 = x*y + 2*x
            sage: f // [g0, g1]
            [...00011*y, ...11010 + ...00100*y]"""
    def __getitem__(self, exponent) -> Any:
        """TateAlgebraElement.__getitem__(self, exponent)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2262)

        Return the coefficient corresponding to the given exponent.

        INPUT:

        - ``exponent`` -- tuple of integers

        TESTS::

            sage: R = Zp(2, prec=10, print_mode='terse')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 2*x^2 + 53*x*y + y^3

            sage: f['hello']
            Traceback (most recent call last):
            ...
            IndexError: hello is not a correct exponent

            sage: f[1,2,3]
            Traceback (most recent call last):
            ...
            IndexError: lengths do not match"""
    def __lshift__(self, n) -> Any:
        """TateAlgebraElement.__lshift__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1977)

        Return the product of this series by the ``n``-th power
        of the uniformizer.

        INPUT:

        - ``n`` -- integer

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits',prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x + 2*x^2 + x^3; f
            ...0000000001*x^3 + ...0000000001*x + ...00000000010*x^2
            sage: f << 2  # indirect doctest
            ...000000000100*x^3 + ...000000000100*x + ...0000000001000*x^2
            sage: f << -1  # indirect doctest
            ...000000000.1*x^3 + ...000000000.1*x + ...0000000001*x^2

        If we're shifting by a negative number of digits over the ring of
        integers of a Tate algebra, the result is truncated -- that is, the
        output is the result of the integer division of the Tate series by
        `\\pi^{-n}` where `\\pi` is a uniformizer.

            sage: Ao = A.integer_ring()
            sage: Ao(f) << -1
            ...0000000001*x^2 + ...000000000*x^3 + ...000000000*x"""
    def __mod__(self, divisors) -> Any:
        """TateAlgebraElement.__mod__(self, divisors)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 3296)

        Return the remainder of the division of this series by
        ``divisors``.

        INPUT:

        - ``divisors`` -- a series, or a list of series

        EXAMPLES::

            sage: R = Zp(2, 5, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = 1 + 2*x*y + 3*x^2*y + 4*x*y^2
            sage: g = x^2
            sage: f % g
            ...00001 + ...00010*x*y + ...00100*x*y^2 + O(2^5 * <x, y>)

        We can also divide by a family of divisors::

            sage: g0 = x^2
            sage: g1 = x*y + 2*x
            sage: f % [g0, g1]
            ...00001 + ...01100*x + O(2^5 * <x, y>)"""
    def __pow__(self, exponent, modulus) -> Any:
        """TateAlgebraElement.__pow__(self, exponent, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1496)

        Return this element raised to the power ``exponent``.

        INPUT:

        - ``exponent`` -- either an integer, a rational number or a
          Tate series

        - ``modulus`` -- discarded

        EXAMPLES::

            sage: R = Zp(3, prec=4, print_mode='digits')
            sage: A.<x,y> = TateAlgebra(R)
            sage: (x + y)^3
            ...0001*x^3 + ...0001*y^3 + ...0010*x^2*y + ...0010*x*y^2

        This function can be used to compute the inverse of a Tate series::

            sage: f = 1 + 6*x^2 + 9*y^2
            sage: f^(-1)
            ...0001 + ...2210*x^2 + ...1100*x^4 + ...2200*y^2 + ...1000*x^6
             + ...1000*x^2*y^2 + O(3^4 * <x, y>)

        or a square root (or more generally an n-th root)::

            sage: g = f^(1/2); g
            ...0001 + ...0010*x^2 + ...1100*x^4 + ...1200*y^2 + ...2000*x^6
             + ...1000*x^2*y^2 + O(3^4 * <x, y>)
            sage: g^2 == f
            True

        When the exponent is not an integer, `f^e` is computed as `\\exp(e \\log(f))`.
        This computation fails if `f` is outside the domain of the logarithm or if
        `e \\log(f)` is outside the domain of convergence of the exponential::

            sage: f^(1/3)
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        The exponent can be a series as well::

            sage: g = f^x; g
            ...0001 + ...0020*x^3 + ...1100*x^9 + ...2200*x^7 + ... + O(3^4 * <x, y>)

            sage: x0 = R.random_element()
            sage: y0 = R.random_element()
            sage: g(x0, y0) == f(x0, y0)^x0
            True

        TESTS::

            sage: f^(x + y) == f^x * f^y
            True
            sage: f^(x*y) == (f^x)^y
            True
            sage: f^(x*y) == (f^y)^x
            True"""
    def __reduce__(self) -> Any:
        """TateAlgebraElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 1143)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: A.<x,y> = TateAlgebra(Zp(2))
            sage: loads(dumps(x)) == x  # indirect doctest
            True"""
    def __rfloordiv__(self, other):
        """Return value//self."""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rmod__(self, other):
        """Return value%self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, n) -> Any:
        """TateAlgebraElement.__rshift__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 2008)

        Return the quotient in the division of this series by
        the ``n``-th power of the uniformizer.

        INPUT:

        - ``n`` -- integer

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits',prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: f = x + 2*x^2 + x^3; f
            ...0000000001*x^3 + ...0000000001*x + ...00000000010*x^2
            sage: f << 2
            ...000000000100*x^3 + ...000000000100*x + ...0000000001000*x^2
            sage: f << -1  # indirect doctest
            ...000000000.1*x^3 + ...000000000.1*x + ...0000000001*x^2

        If we're working over the ring of integers of a Tate algebra, the
        result is truncated -- that is, the output is the result of the integer
        division of the Tate series by `\\pi^n` where `\\pi` is a uniformizer.

            sage: Ao = A.integer_ring()
            sage: Ao(f) << -1
            ...0000000001*x^2 + ...000000000*x^3 + ...000000000*x"""

class TateAlgebraTerm(sage.structure.element.MonoidElement):
    """TateAlgebraTerm(parent, coeff, exponent=None)

    File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 76)

    A class for Tate algebra terms.

    A term in `K\\{X_1,\\dots,X_n\\}` is the product of a coefficient in `K` and a
    monomial in the variables `X_1,\\dots,X_n`.

    Those terms form a partially ordered monoid, with term multiplication and the
    term order of the parent Tate algebra.

    INPUT:

    - ``coeff`` -- an element in the base field

    - ``exponent`` -- tuple of length ``n``

    EXAMPLES::

        sage: R = Zp(2, print_mode='digits', prec=10)
        sage: A.<x,y> = TateAlgebra(R)
        sage: T = A.monoid_of_terms(); T
        Monoid of terms in x (val >= 0), y (val >= 0)
         over 2-adic Field with capped relative precision 10

        sage: T(2*x*y)
        ...00000000010*x*y
        sage: T(0)
        Traceback (most recent call last):
        ...
        TypeError: a term cannot be zero"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, coeff, exponent=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 107)

                Initialize a Tate algebra term.

                INPUT:

                - ``coeff`` -- an element in the base field

                - ``exponent`` -- tuple

                TESTS::

                    sage: R = Zp(2, print_mode='digits', prec=10)
                    sage: A.<x,y> = TateAlgebra(R)
                    sage: T = A.monoid_of_terms()

                    sage: t = T(x)
                    sage: TestSuite(t).run()
        """
    @overload
    def coefficient(self) -> Any:
        """TateAlgebraTerm.coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 271)

        Return the coefficient of this Tate algebra term.

        EXAMPLES::

            sage: R = Zp(2,prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: t = T(2*x*y); t
            (2 + O(2^11))*x*y
            sage: t.coefficient()
            2 + O(2^11)"""
    @overload
    def coefficient(self) -> Any:
        """TateAlgebraTerm.coefficient(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 271)

        Return the coefficient of this Tate algebra term.

        EXAMPLES::

            sage: R = Zp(2,prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: t = T(2*x*y); t
            (2 + O(2^11))*x*y
            sage: t.coefficient()
            2 + O(2^11)"""
    @overload
    def divides(self, other, integral=...) -> Any:
        """TateAlgebraTerm.divides(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 870)

        Return ``True`` if this term divides ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test for
          divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: t.divides(s)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: t.divides(s)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: t.divides(s)
            True
            sage: t.divides(s, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: to.divides(so)
            False
            sage: to.divides(so, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: to.divides(s)
            True"""
    @overload
    def divides(self, s) -> Any:
        """TateAlgebraTerm.divides(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 870)

        Return ``True`` if this term divides ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test for
          divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: t.divides(s)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: t.divides(s)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: t.divides(s)
            True
            sage: t.divides(s, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: to.divides(so)
            False
            sage: to.divides(so, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: to.divides(s)
            True"""
    @overload
    def divides(self, s) -> Any:
        """TateAlgebraTerm.divides(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 870)

        Return ``True`` if this term divides ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test for
          divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: t.divides(s)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: t.divides(s)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: t.divides(s)
            True
            sage: t.divides(s, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: to.divides(so)
            False
            sage: to.divides(so, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: to.divides(s)
            True"""
    @overload
    def divides(self, s) -> Any:
        """TateAlgebraTerm.divides(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 870)

        Return ``True`` if this term divides ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test for
          divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: t.divides(s)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: t.divides(s)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: t.divides(s)
            True
            sage: t.divides(s, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: to.divides(so)
            False
            sage: to.divides(so, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: to.divides(s)
            True"""
    @overload
    def divides(self, s, integral=...) -> Any:
        """TateAlgebraTerm.divides(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 870)

        Return ``True`` if this term divides ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test for
          divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: t.divides(s)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: t.divides(s)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: t.divides(s)
            True
            sage: t.divides(s, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: to.divides(so)
            False
            sage: to.divides(so, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: to.divides(s)
            True"""
    @overload
    def divides(self, so) -> Any:
        """TateAlgebraTerm.divides(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 870)

        Return ``True`` if this term divides ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test for
          divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: t.divides(s)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: t.divides(s)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: t.divides(s)
            True
            sage: t.divides(s, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: to.divides(so)
            False
            sage: to.divides(so, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: to.divides(s)
            True"""
    @overload
    def divides(self, so, integral=...) -> Any:
        """TateAlgebraTerm.divides(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 870)

        Return ``True`` if this term divides ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test for
          divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: t.divides(s)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: t.divides(s)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: t.divides(s)
            True
            sage: t.divides(s, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: to.divides(so)
            False
            sage: to.divides(so, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: to.divides(s)
            True"""
    @overload
    def divides(self, s) -> Any:
        """TateAlgebraTerm.divides(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 870)

        Return ``True`` if this term divides ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test for
          divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: t.divides(s)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: t.divides(s)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: t.divides(s)
            True
            sage: t.divides(s, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: to.divides(so)
            False
            sage: to.divides(so, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: to.divides(s)
            True"""
    @overload
    def exponent(self) -> Any:
        """TateAlgebraTerm.exponent(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 287)

        Return the exponents of this Tate algebra term.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms(); T
            Monoid of terms in x (val >= 0), y (val >= 0)
             over 2-adic Field with capped relative precision 10
            sage: t = T(2,(1,1))
            sage: t.exponent()
            (1, 1)"""
    @overload
    def exponent(self) -> Any:
        """TateAlgebraTerm.exponent(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 287)

        Return the exponents of this Tate algebra term.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms(); T
            Monoid of terms in x (val >= 0), y (val >= 0)
             over 2-adic Field with capped relative precision 10
            sage: t = T(2,(1,1))
            sage: t.exponent()
            (1, 1)"""
    @overload
    def gcd(self, other) -> Any:
        """TateAlgebraTerm.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 679)

        Return the greatest common divisor of this term and ``other``.

        The result is normalized so that:

        - its valuation is equal to the smallest valuation of
          this term and ``other``

        - its coefficient is a power of the uniformizer.

        INPUT:

        - ``other`` -- a Tate term

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(8*x^2*y^2); s
            ...0000000001000*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: s.gcd(t)
            ...000000000100*x*y^2"""
    @overload
    def gcd(self, t) -> Any:
        """TateAlgebraTerm.gcd(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 679)

        Return the greatest common divisor of this term and ``other``.

        The result is normalized so that:

        - its valuation is equal to the smallest valuation of
          this term and ``other``

        - its coefficient is a power of the uniformizer.

        INPUT:

        - ``other`` -- a Tate term

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(8*x^2*y^2); s
            ...0000000001000*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: s.gcd(t)
            ...000000000100*x*y^2"""
    @overload
    def is_coprime_with(self, other) -> Any:
        """TateAlgebraTerm.is_coprime_with(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 623)

        Return ``True`` if this term is coprime with ``other``.

        INPUT:

        - ``other`` -- a Tate term

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: s = T(y^3); s
            ...0000000001*y^3
            sage: s.is_coprime_with(t)
            False
            sage: t.is_coprime_with(s)
            False

            sage: tt = T(3*x^2); tt
            ...0000000011*x^2
            sage: s.is_coprime_with(tt)
            True
            sage: tt.is_coprime_with(s)
            True

        When working over a rational Tate algebra, only the
        monomial part of terms are compared::

            sage: t = T(2*x^2); t
            ...00000000010*x^2
            sage: s = T(4*y^3); s
            ...000000000100*y^3
            sage: s.is_coprime_with(t)
            True

        But coefficients play a role when we are working over
        the ring of integers of the Tate Algebra::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: To(s).is_coprime_with(To(t))
            False"""
    @overload
    def is_coprime_with(self, t) -> Any:
        """TateAlgebraTerm.is_coprime_with(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 623)

        Return ``True`` if this term is coprime with ``other``.

        INPUT:

        - ``other`` -- a Tate term

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: s = T(y^3); s
            ...0000000001*y^3
            sage: s.is_coprime_with(t)
            False
            sage: t.is_coprime_with(s)
            False

            sage: tt = T(3*x^2); tt
            ...0000000011*x^2
            sage: s.is_coprime_with(tt)
            True
            sage: tt.is_coprime_with(s)
            True

        When working over a rational Tate algebra, only the
        monomial part of terms are compared::

            sage: t = T(2*x^2); t
            ...00000000010*x^2
            sage: s = T(4*y^3); s
            ...000000000100*y^3
            sage: s.is_coprime_with(t)
            True

        But coefficients play a role when we are working over
        the ring of integers of the Tate Algebra::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: To(s).is_coprime_with(To(t))
            False"""
    @overload
    def is_coprime_with(self, s) -> Any:
        """TateAlgebraTerm.is_coprime_with(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 623)

        Return ``True`` if this term is coprime with ``other``.

        INPUT:

        - ``other`` -- a Tate term

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: s = T(y^3); s
            ...0000000001*y^3
            sage: s.is_coprime_with(t)
            False
            sage: t.is_coprime_with(s)
            False

            sage: tt = T(3*x^2); tt
            ...0000000011*x^2
            sage: s.is_coprime_with(tt)
            True
            sage: tt.is_coprime_with(s)
            True

        When working over a rational Tate algebra, only the
        monomial part of terms are compared::

            sage: t = T(2*x^2); t
            ...00000000010*x^2
            sage: s = T(4*y^3); s
            ...000000000100*y^3
            sage: s.is_coprime_with(t)
            True

        But coefficients play a role when we are working over
        the ring of integers of the Tate Algebra::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: To(s).is_coprime_with(To(t))
            False"""
    @overload
    def is_coprime_with(self, tt) -> Any:
        """TateAlgebraTerm.is_coprime_with(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 623)

        Return ``True`` if this term is coprime with ``other``.

        INPUT:

        - ``other`` -- a Tate term

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: s = T(y^3); s
            ...0000000001*y^3
            sage: s.is_coprime_with(t)
            False
            sage: t.is_coprime_with(s)
            False

            sage: tt = T(3*x^2); tt
            ...0000000011*x^2
            sage: s.is_coprime_with(tt)
            True
            sage: tt.is_coprime_with(s)
            True

        When working over a rational Tate algebra, only the
        monomial part of terms are compared::

            sage: t = T(2*x^2); t
            ...00000000010*x^2
            sage: s = T(4*y^3); s
            ...000000000100*y^3
            sage: s.is_coprime_with(t)
            True

        But coefficients play a role when we are working over
        the ring of integers of the Tate Algebra::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: To(s).is_coprime_with(To(t))
            False"""
    @overload
    def is_coprime_with(self, s) -> Any:
        """TateAlgebraTerm.is_coprime_with(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 623)

        Return ``True`` if this term is coprime with ``other``.

        INPUT:

        - ``other`` -- a Tate term

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: s = T(y^3); s
            ...0000000001*y^3
            sage: s.is_coprime_with(t)
            False
            sage: t.is_coprime_with(s)
            False

            sage: tt = T(3*x^2); tt
            ...0000000011*x^2
            sage: s.is_coprime_with(tt)
            True
            sage: tt.is_coprime_with(s)
            True

        When working over a rational Tate algebra, only the
        monomial part of terms are compared::

            sage: t = T(2*x^2); t
            ...00000000010*x^2
            sage: s = T(4*y^3); s
            ...000000000100*y^3
            sage: s.is_coprime_with(t)
            True

        But coefficients play a role when we are working over
        the ring of integers of the Tate Algebra::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: To(s).is_coprime_with(To(t))
            False"""
    @overload
    def is_coprime_with(self, t) -> Any:
        """TateAlgebraTerm.is_coprime_with(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 623)

        Return ``True`` if this term is coprime with ``other``.

        INPUT:

        - ``other`` -- a Tate term

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: s = T(y^3); s
            ...0000000001*y^3
            sage: s.is_coprime_with(t)
            False
            sage: t.is_coprime_with(s)
            False

            sage: tt = T(3*x^2); tt
            ...0000000011*x^2
            sage: s.is_coprime_with(tt)
            True
            sage: tt.is_coprime_with(s)
            True

        When working over a rational Tate algebra, only the
        monomial part of terms are compared::

            sage: t = T(2*x^2); t
            ...00000000010*x^2
            sage: s = T(4*y^3); s
            ...000000000100*y^3
            sage: s.is_coprime_with(t)
            True

        But coefficients play a role when we are working over
        the ring of integers of the Tate Algebra::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: To(s).is_coprime_with(To(t))
            False"""
    @overload
    def is_divisible_by(self, other, integral=...) -> Any:
        """TateAlgebraTerm.is_divisible_by(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 813)

        Return ``True`` if this term is divisible by ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test
          for divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: s.is_divisible_by(t)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: s.is_divisible_by(t)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: s.is_divisible_by(t)
            True
            sage: s.is_divisible_by(t, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: so.is_divisible_by(to)
            False
            sage: so.is_divisible_by(to, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: s.is_divisible_by(to)
            True"""
    @overload
    def is_divisible_by(self, t) -> Any:
        """TateAlgebraTerm.is_divisible_by(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 813)

        Return ``True`` if this term is divisible by ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test
          for divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: s.is_divisible_by(t)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: s.is_divisible_by(t)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: s.is_divisible_by(t)
            True
            sage: s.is_divisible_by(t, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: so.is_divisible_by(to)
            False
            sage: so.is_divisible_by(to, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: s.is_divisible_by(to)
            True"""
    @overload
    def is_divisible_by(self, t) -> Any:
        """TateAlgebraTerm.is_divisible_by(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 813)

        Return ``True`` if this term is divisible by ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test
          for divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: s.is_divisible_by(t)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: s.is_divisible_by(t)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: s.is_divisible_by(t)
            True
            sage: s.is_divisible_by(t, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: so.is_divisible_by(to)
            False
            sage: so.is_divisible_by(to, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: s.is_divisible_by(to)
            True"""
    @overload
    def is_divisible_by(self, t) -> Any:
        """TateAlgebraTerm.is_divisible_by(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 813)

        Return ``True`` if this term is divisible by ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test
          for divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: s.is_divisible_by(t)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: s.is_divisible_by(t)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: s.is_divisible_by(t)
            True
            sage: s.is_divisible_by(t, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: so.is_divisible_by(to)
            False
            sage: so.is_divisible_by(to, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: s.is_divisible_by(to)
            True"""
    @overload
    def is_divisible_by(self, t, integral=...) -> Any:
        """TateAlgebraTerm.is_divisible_by(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 813)

        Return ``True`` if this term is divisible by ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test
          for divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: s.is_divisible_by(t)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: s.is_divisible_by(t)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: s.is_divisible_by(t)
            True
            sage: s.is_divisible_by(t, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: so.is_divisible_by(to)
            False
            sage: so.is_divisible_by(to, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: s.is_divisible_by(to)
            True"""
    @overload
    def is_divisible_by(self, to) -> Any:
        """TateAlgebraTerm.is_divisible_by(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 813)

        Return ``True`` if this term is divisible by ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test
          for divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: s.is_divisible_by(t)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: s.is_divisible_by(t)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: s.is_divisible_by(t)
            True
            sage: s.is_divisible_by(t, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: so.is_divisible_by(to)
            False
            sage: so.is_divisible_by(to, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: s.is_divisible_by(to)
            True"""
    @overload
    def is_divisible_by(self, to, integral=...) -> Any:
        """TateAlgebraTerm.is_divisible_by(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 813)

        Return ``True`` if this term is divisible by ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test
          for divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: s.is_divisible_by(t)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: s.is_divisible_by(t)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: s.is_divisible_by(t)
            True
            sage: s.is_divisible_by(t, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: so.is_divisible_by(to)
            False
            sage: so.is_divisible_by(to, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: s.is_divisible_by(to)
            True"""
    @overload
    def is_divisible_by(self, to) -> Any:
        """TateAlgebraTerm.is_divisible_by(self, other, integral=False)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 813)

        Return ``True`` if this term is divisible by ``other``.

        INPUT:

        - ``other`` -- a Tate term

        - ``integral`` -- (default: ``False``) if ``True``, test
          for divisibility in the ring of integers of the Tate algebra

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(4*x^2*y^2); s
            ...000000000100*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: s.is_divisible_by(t)
            False

            sage: t = T(4*x*y^2); t
            ...000000000100*x*y^2
            sage: s.is_divisible_by(t)
            True

            sage: t = T(16); t
            ...00000000010000
            sage: s.is_divisible_by(t)
            True
            sage: s.is_divisible_by(t, integral=True)
            False

        If you are working over the ring of integers of the Tate algebra,
        divisibility is always checked in the ring of integers (even if
        ``integral`` is set to ``False``)::

            sage: Ao = A.integer_ring()
            sage: To = Ao.monoid_of_terms()
            sage: so = To(s)
            sage: to = To(t)
            sage: so.is_divisible_by(to)
            False
            sage: so.is_divisible_by(to, integral=False)
            False

        Be careful that coercion between the Tate algebra and its ring of
        integers can be done silently::

            sage: s.is_divisible_by(to)
            True"""
    def lcm(self, other) -> Any:
        """TateAlgebraTerm.lcm(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 750)

        Return the least common multiple of two Tate terms.

        The result is normalized so that `\\gcd(a,b) \\lcm(a,b) = ab`.

        INPUT:

        - ``other`` -- a Tate term

        EXAMPLES::

        In a Tate algebra over a field:

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(8*x^2*y^2); s
            ...0000000001000*x^2*y^2
            sage: t = T(4*x*y^3); t
            ...000000000100*x*y^3
            sage: s.lcm(t)
            ...0000000001000*x^2*y^3"""
    @overload
    def monic(self) -> TateAlgebraTerm:
        """TateAlgebraTerm.monic(self) -> TateAlgebraTerm

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 457)

        Return this term normalized so that it has valuation 0
        and its coefficient is a power of the uniformizer.

        EXAMPLES:

        When the log radii of convergence are all zero, the
        coefficient of the returned term is `1`. In this case,
        this method does the same thing as :meth:`monomial`::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(3*x^2*y^2); s
            ...0000000011*x^2*y^2
            sage: s.monic()
            ...0000000001*x^2*y^2
            sage: s.monomial()
            ...0000000001*x^2*y^2

        However, when log radii do not vanish, behaviors might
        be different::

            sage: A.<x,y> = TateAlgebra(R, log_radii=1)
            sage: T = A.monoid_of_terms()
            sage: s = T(3*x^2*y^2); s
            ...0000000011*x^2*y^2
            sage: s.monic()
            ...00000000010000*x^2*y^2
            sage: s.monomial()
            ...0000000001*x^2*y^2

        We compare the valuations::

            sage: s.monic().valuation()
            0
            sage: s.monomial().valuation()
            -4"""
    @overload
    def monic(self) -> Any:
        """TateAlgebraTerm.monic(self) -> TateAlgebraTerm

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 457)

        Return this term normalized so that it has valuation 0
        and its coefficient is a power of the uniformizer.

        EXAMPLES:

        When the log radii of convergence are all zero, the
        coefficient of the returned term is `1`. In this case,
        this method does the same thing as :meth:`monomial`::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(3*x^2*y^2); s
            ...0000000011*x^2*y^2
            sage: s.monic()
            ...0000000001*x^2*y^2
            sage: s.monomial()
            ...0000000001*x^2*y^2

        However, when log radii do not vanish, behaviors might
        be different::

            sage: A.<x,y> = TateAlgebra(R, log_radii=1)
            sage: T = A.monoid_of_terms()
            sage: s = T(3*x^2*y^2); s
            ...0000000011*x^2*y^2
            sage: s.monic()
            ...00000000010000*x^2*y^2
            sage: s.monomial()
            ...0000000001*x^2*y^2

        We compare the valuations::

            sage: s.monic().valuation()
            0
            sage: s.monomial().valuation()
            -4"""
    @overload
    def monic(self) -> Any:
        """TateAlgebraTerm.monic(self) -> TateAlgebraTerm

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 457)

        Return this term normalized so that it has valuation 0
        and its coefficient is a power of the uniformizer.

        EXAMPLES:

        When the log radii of convergence are all zero, the
        coefficient of the returned term is `1`. In this case,
        this method does the same thing as :meth:`monomial`::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(3*x^2*y^2); s
            ...0000000011*x^2*y^2
            sage: s.monic()
            ...0000000001*x^2*y^2
            sage: s.monomial()
            ...0000000001*x^2*y^2

        However, when log radii do not vanish, behaviors might
        be different::

            sage: A.<x,y> = TateAlgebra(R, log_radii=1)
            sage: T = A.monoid_of_terms()
            sage: s = T(3*x^2*y^2); s
            ...0000000011*x^2*y^2
            sage: s.monic()
            ...00000000010000*x^2*y^2
            sage: s.monomial()
            ...0000000001*x^2*y^2

        We compare the valuations::

            sage: s.monic().valuation()
            0
            sage: s.monomial().valuation()
            -4"""
    @overload
    def monic(self) -> Any:
        """TateAlgebraTerm.monic(self) -> TateAlgebraTerm

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 457)

        Return this term normalized so that it has valuation 0
        and its coefficient is a power of the uniformizer.

        EXAMPLES:

        When the log radii of convergence are all zero, the
        coefficient of the returned term is `1`. In this case,
        this method does the same thing as :meth:`monomial`::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(3*x^2*y^2); s
            ...0000000011*x^2*y^2
            sage: s.monic()
            ...0000000001*x^2*y^2
            sage: s.monomial()
            ...0000000001*x^2*y^2

        However, when log radii do not vanish, behaviors might
        be different::

            sage: A.<x,y> = TateAlgebra(R, log_radii=1)
            sage: T = A.monoid_of_terms()
            sage: s = T(3*x^2*y^2); s
            ...0000000011*x^2*y^2
            sage: s.monic()
            ...00000000010000*x^2*y^2
            sage: s.monomial()
            ...0000000001*x^2*y^2

        We compare the valuations::

            sage: s.monic().valuation()
            0
            sage: s.monomial().valuation()
            -4"""
    @overload
    def monomial(self) -> TateAlgebraTerm:
        """TateAlgebraTerm.monomial(self) -> TateAlgebraTerm

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 438)

        Return this term divided by its coefficient.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(3*x^2*y^2); s
            ...0000000011*x^2*y^2
            sage: s.monomial()
            ...0000000001*x^2*y^2"""
    @overload
    def monomial(self) -> Any:
        """TateAlgebraTerm.monomial(self) -> TateAlgebraTerm

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 438)

        Return this term divided by its coefficient.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: s = T(3*x^2*y^2); s
            ...0000000011*x^2*y^2
            sage: s.monomial()
            ...0000000001*x^2*y^2"""
    @overload
    def valuation(self) -> Any:
        """TateAlgebraTerm.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 503)

        Return the valuation of this term.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: t.valuation()
            2

        In case of nonzero log radii, the valuations of the variables
        contribute::

            sage: A.<x,y> = TateAlgebra(R, log_radii=1)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: t.valuation()
            -2"""
    @overload
    def valuation(self) -> Any:
        """TateAlgebraTerm.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 503)

        Return the valuation of this term.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: t.valuation()
            2

        In case of nonzero log radii, the valuations of the variables
        contribute::

            sage: A.<x,y> = TateAlgebra(R, log_radii=1)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: t.valuation()
            -2"""
    @overload
    def valuation(self) -> Any:
        """TateAlgebraTerm.valuation(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 503)

        Return the valuation of this term.

        EXAMPLES::

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: t.valuation()
            2

        In case of nonzero log radii, the valuations of the variables
        contribute::

            sage: A.<x,y> = TateAlgebra(R, log_radii=1)
            sage: T = A.monoid_of_terms()
            sage: t = T(4*x^2*y^2); t
            ...000000000100*x^2*y^2
            sage: t.valuation()
            -2"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *args) -> Any:
        """TateAlgebraTerm.__call__(self, *args)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 569)

        Return this term evaluated at ``args``.

        INPUT:

        - ``args`` -- elements

        EXAMPLES::

            sage: R = Zp(2)
            sage: A.<x,y> = TateAlgebra(R)
            sage: M = A.monoid_of_terms()
            sage: t = M(x*y)
            sage: t(1, 2)
            2 + O(2^21)

        An error is raised if we ask for the evaluation at one
        point which is outside the domain of convergence::

            sage: t(1/2, 1)
            Traceback (most recent call last):
            ...
            ValueError: not in the domain of convergence

        TESTS::

            sage: t(1/2, 1, 0)
            Traceback (most recent call last):
            ...
            TypeError: wrong number of arguments

            sage: t(1/2, GF(3)(2))
            Traceback (most recent call last):
            ...
            TypeError: cannot coerce all the elements to the same parent"""
    def __hash__(self) -> Any:
        """TateAlgebraTerm.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 152)

        Return a hash of this term.

            sage: R = Zp(2, print_mode='digits', prec=10)
            sage: A.<x,y> = TateAlgebra(R);
            sage: T = A.monoid_of_terms()
            sage: t = T(x^2)

            sage: hash(t) == hash((t.coefficient(), t.exponent()))
            True"""
    def __reduce__(self) -> Any:
        """TateAlgebraTerm.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/tate_algebra_element.pyx (starting at line 185)

        Return a tuple of a function and data that can be used to unpickle this
        element.

        TESTS::

            sage: A.<x,y> = TateAlgebra(Zp(2))
            sage: t = x.leading_term()
            sage: loads(dumps(t)) == t  # indirect doctest
            True"""
