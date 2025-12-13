import _cython_3_2_1
import sage.rings.polynomial.polynomial_element
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

make_PolynomialRealDense: _cython_3_2_1.cython_function_or_method

class PolynomialRealDense(sage.rings.polynomial.polynomial_element.Polynomial):
    """PolynomialRealDense(Parent parent, x=0, check=None, bool is_gen=False, construct=None)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 49)


    TESTS::

        sage: f = RR['x'].random_element()
        sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
        sage: isinstance(f, PolynomialRealDense)
        True"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, Parentparent, x=..., check=..., boolis_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 74)

                EXAMPLES::

                    sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
                    sage: PolynomialRealDense(RR['x'], [1, int(2), RR(3), 4/1, pi])             # needs sage.symbolic
                    3.14159265358979*x^4 + 4.00000000000000*x^3 + 3.00000000000000*x^2 + 2.00000000000000*x + 1.00000000000000
                    sage: PolynomialRealDense(RR['x'], None)
                    0

                TESTS:

                Check that errors and interrupts are handled properly (see :issue:`10100`)::

                    sage: a = var('a')                                                          # needs sage.symbolic
                    sage: PolynomialRealDense(RR['x'], [1,a])                                   # needs sage.symbolic
                    Traceback (most recent call last):
                    ...
                    TypeError: cannot evaluate symbolic expression to a numeric value
                    sage: R.<x> = SR[]                                                          # needs sage.symbolic
                    sage: (x-a).change_ring(RR)                                                 # needs sage.symbolic
                    Traceback (most recent call last):
                    ...
                    TypeError: cannot evaluate symbolic expression to a numeric value
                    sage: sig_on_count()
                    0

                Test that we don't clean up uninitialized coefficients (:issue:`9826`)::

                    sage: k.<a> = GF(7^3)                                                       # needs sage.rings.finite_rings
                    sage: P.<x> = PolynomialRing(k)                                             # needs sage.rings.finite_rings
                    sage: (a*x).complex_roots()                                                 # needs sage.rings.finite_rings
                    Traceback (most recent call last):
                    ...
                    TypeError: unable to convert 'a' to a real number

                Check that :issue:`17190` is fixed::

                    sage: RR['x']({})
                    0
        """
    @overload
    def change_ring(self, R) -> Any:
        """PolynomialRealDense.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 753)

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [-2, 0, 1.5])
            sage: f.change_ring(QQ)
            3/2*x^2 - 2
            sage: f.change_ring(RealField(10))
            1.5*x^2 - 2.0
            sage: f.change_ring(RealField(100))
            1.5000000000000000000000000000*x^2 - 2.0000000000000000000000000000"""
    @overload
    def change_ring(self, QQ) -> Any:
        """PolynomialRealDense.change_ring(self, R)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 753)

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [-2, 0, 1.5])
            sage: f.change_ring(QQ)
            3/2*x^2 - 2
            sage: f.change_ring(RealField(10))
            1.5*x^2 - 2.0
            sage: f.change_ring(RealField(100))
            1.5000000000000000000000000000*x^2 - 2.0000000000000000000000000000"""
    @overload
    def degree(self) -> Any:
        """PolynomialRealDense.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 240)

        Return the degree of the polynomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [1, 2, 3]); f
            3.00000000000000*x^2 + 2.00000000000000*x + 1.00000000000000
            sage: f.degree()
            2

        TESTS::

            sage: type(f.degree())
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def degree(self) -> Any:
        """PolynomialRealDense.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 240)

        Return the degree of the polynomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [1, 2, 3]); f
            3.00000000000000*x^2 + 2.00000000000000*x + 1.00000000000000
            sage: f.degree()
            2

        TESTS::

            sage: type(f.degree())
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def degree(self) -> Any:
        """PolynomialRealDense.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 240)

        Return the degree of the polynomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [1, 2, 3]); f
            3.00000000000000*x^2 + 2.00000000000000*x + 1.00000000000000
            sage: f.degree()
            2

        TESTS::

            sage: type(f.degree())
            <class 'sage.rings.integer.Integer'>"""
    @overload
    def integral(self) -> Any:
        """PolynomialRealDense.integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 544)

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [3, pi, 1])                          # needs sage.symbolic
            sage: f.integral()                                                          # needs sage.symbolic
            0.333333333333333*x^3 + 1.57079632679490*x^2 + 3.00000000000000*x"""
    @overload
    def integral(self) -> Any:
        """PolynomialRealDense.integral(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 544)

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [3, pi, 1])                          # needs sage.symbolic
            sage: f.integral()                                                          # needs sage.symbolic
            0.333333333333333*x^3 + 1.57079632679490*x^2 + 3.00000000000000*x"""
    @overload
    def list(self, boolcopy=...) -> list:
        """PolynomialRealDense.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 353)

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [1, 0, -2]); f
            -2.00000000000000*x^2 + 1.00000000000000
            sage: f.list()
            [1.00000000000000, 0.000000000000000, -2.00000000000000]"""
    @overload
    def list(self) -> Any:
        """PolynomialRealDense.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 353)

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [1, 0, -2]); f
            -2.00000000000000*x^2 + 1.00000000000000
            sage: f.list()
            [1.00000000000000, 0.000000000000000, -2.00000000000000]"""
    @overload
    def quo_rem(self, PolynomialRealDenseother) -> Any:
        """PolynomialRealDense.quo_rem(self, PolynomialRealDense other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 604)

        Return the quotient with remainder of ``self`` by ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [-2, 0, 1])
            sage: g = PolynomialRealDense(RR['x'], [5, 1])
            sage: q, r = f.quo_rem(g)
            sage: q
            x - 5.00000000000000
            sage: r
            23.0000000000000
            sage: q*g + r == f
            True
            sage: fg = f*g
            sage: fg.quo_rem(f)
            (x + 5.00000000000000, 0)
            sage: fg.quo_rem(g)
            (x^2 - 2.00000000000000, 0)

            sage: # needs sage.symbolic
            sage: f = PolynomialRealDense(RR['x'], range(5))
            sage: g = PolynomialRealDense(RR['x'], [pi,3000,4])
            sage: q, r = f.quo_rem(g)
            sage: g*q + r == f
            True

        TESTS:

        Check that :issue:`18467` is fixed::

            sage: S.<x> = RR[]
            sage: z = S.zero()
            sage: z.degree()
            -1
            sage: q, r = z.quo_rem(x)
            sage: q.degree()
            -1"""
    @overload
    def quo_rem(self, g) -> Any:
        """PolynomialRealDense.quo_rem(self, PolynomialRealDense other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 604)

        Return the quotient with remainder of ``self`` by ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [-2, 0, 1])
            sage: g = PolynomialRealDense(RR['x'], [5, 1])
            sage: q, r = f.quo_rem(g)
            sage: q
            x - 5.00000000000000
            sage: r
            23.0000000000000
            sage: q*g + r == f
            True
            sage: fg = f*g
            sage: fg.quo_rem(f)
            (x + 5.00000000000000, 0)
            sage: fg.quo_rem(g)
            (x^2 - 2.00000000000000, 0)

            sage: # needs sage.symbolic
            sage: f = PolynomialRealDense(RR['x'], range(5))
            sage: g = PolynomialRealDense(RR['x'], [pi,3000,4])
            sage: q, r = f.quo_rem(g)
            sage: g*q + r == f
            True

        TESTS:

        Check that :issue:`18467` is fixed::

            sage: S.<x> = RR[]
            sage: z = S.zero()
            sage: z.degree()
            -1
            sage: q, r = z.quo_rem(x)
            sage: q.degree()
            -1"""
    @overload
    def quo_rem(self, f) -> Any:
        """PolynomialRealDense.quo_rem(self, PolynomialRealDense other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 604)

        Return the quotient with remainder of ``self`` by ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [-2, 0, 1])
            sage: g = PolynomialRealDense(RR['x'], [5, 1])
            sage: q, r = f.quo_rem(g)
            sage: q
            x - 5.00000000000000
            sage: r
            23.0000000000000
            sage: q*g + r == f
            True
            sage: fg = f*g
            sage: fg.quo_rem(f)
            (x + 5.00000000000000, 0)
            sage: fg.quo_rem(g)
            (x^2 - 2.00000000000000, 0)

            sage: # needs sage.symbolic
            sage: f = PolynomialRealDense(RR['x'], range(5))
            sage: g = PolynomialRealDense(RR['x'], [pi,3000,4])
            sage: q, r = f.quo_rem(g)
            sage: g*q + r == f
            True

        TESTS:

        Check that :issue:`18467` is fixed::

            sage: S.<x> = RR[]
            sage: z = S.zero()
            sage: z.degree()
            -1
            sage: q, r = z.quo_rem(x)
            sage: q.degree()
            -1"""
    @overload
    def quo_rem(self, g) -> Any:
        """PolynomialRealDense.quo_rem(self, PolynomialRealDense other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 604)

        Return the quotient with remainder of ``self`` by ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [-2, 0, 1])
            sage: g = PolynomialRealDense(RR['x'], [5, 1])
            sage: q, r = f.quo_rem(g)
            sage: q
            x - 5.00000000000000
            sage: r
            23.0000000000000
            sage: q*g + r == f
            True
            sage: fg = f*g
            sage: fg.quo_rem(f)
            (x + 5.00000000000000, 0)
            sage: fg.quo_rem(g)
            (x^2 - 2.00000000000000, 0)

            sage: # needs sage.symbolic
            sage: f = PolynomialRealDense(RR['x'], range(5))
            sage: g = PolynomialRealDense(RR['x'], [pi,3000,4])
            sage: q, r = f.quo_rem(g)
            sage: g*q + r == f
            True

        TESTS:

        Check that :issue:`18467` is fixed::

            sage: S.<x> = RR[]
            sage: z = S.zero()
            sage: z.degree()
            -1
            sage: q, r = z.quo_rem(x)
            sage: q.degree()
            -1"""
    @overload
    def quo_rem(self, g) -> Any:
        """PolynomialRealDense.quo_rem(self, PolynomialRealDense other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 604)

        Return the quotient with remainder of ``self`` by ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [-2, 0, 1])
            sage: g = PolynomialRealDense(RR['x'], [5, 1])
            sage: q, r = f.quo_rem(g)
            sage: q
            x - 5.00000000000000
            sage: r
            23.0000000000000
            sage: q*g + r == f
            True
            sage: fg = f*g
            sage: fg.quo_rem(f)
            (x + 5.00000000000000, 0)
            sage: fg.quo_rem(g)
            (x^2 - 2.00000000000000, 0)

            sage: # needs sage.symbolic
            sage: f = PolynomialRealDense(RR['x'], range(5))
            sage: g = PolynomialRealDense(RR['x'], [pi,3000,4])
            sage: q, r = f.quo_rem(g)
            sage: g*q + r == f
            True

        TESTS:

        Check that :issue:`18467` is fixed::

            sage: S.<x> = RR[]
            sage: z = S.zero()
            sage: z.degree()
            -1
            sage: q, r = z.quo_rem(x)
            sage: q.degree()
            -1"""
    @overload
    def quo_rem(self, x) -> Any:
        """PolynomialRealDense.quo_rem(self, PolynomialRealDense other)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 604)

        Return the quotient with remainder of ``self`` by ``other``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [-2, 0, 1])
            sage: g = PolynomialRealDense(RR['x'], [5, 1])
            sage: q, r = f.quo_rem(g)
            sage: q
            x - 5.00000000000000
            sage: r
            23.0000000000000
            sage: q*g + r == f
            True
            sage: fg = f*g
            sage: fg.quo_rem(f)
            (x + 5.00000000000000, 0)
            sage: fg.quo_rem(g)
            (x^2 - 2.00000000000000, 0)

            sage: # needs sage.symbolic
            sage: f = PolynomialRealDense(RR['x'], range(5))
            sage: g = PolynomialRealDense(RR['x'], [pi,3000,4])
            sage: q, r = f.quo_rem(g)
            sage: g*q + r == f
            True

        TESTS:

        Check that :issue:`18467` is fixed::

            sage: S.<x> = RR[]
            sage: z = S.zero()
            sage: z.degree()
            -1
            sage: q, r = z.quo_rem(x)
            sage: q.degree()
            -1"""
    @overload
    def reverse(self, degree=...) -> Any:
        """PolynomialRealDense.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 560)

        Return reverse of the input polynomial thought as a polynomial of
        degree ``degree``.

        If `f` is a degree-`d` polynomial, its reverse is `x^d f(1/x)`.

        INPUT:

        - ``degree`` -- ``None`` or an integer; if specified, truncate or zero
          pad the list of coefficients to this degree before reversing it

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: f = RR['x']([-3, pi, 0, 1])
            sage: f.reverse()
            -3.00000000000000*x^3 + 3.14159265358979*x^2 + 1.00000000000000
            sage: f.reverse(2)
            -3.00000000000000*x^2 + 3.14159265358979*x
            sage: f.reverse(5)
            -3.00000000000000*x^5 + 3.14159265358979*x^4 + x^2

        TESTS:

        We check that this implementation is compatible with the generic one::

            sage: all(f.reverse(d) == Polynomial.reverse(f, d)                          # needs sage.symbolic
            ....:     for d in [None, 0, 1, 2, 3, 4, 5])
            True"""
    @overload
    def reverse(self) -> Any:
        """PolynomialRealDense.reverse(self, degree=None)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 560)

        Return reverse of the input polynomial thought as a polynomial of
        degree ``degree``.

        If `f` is a degree-`d` polynomial, its reverse is `x^d f(1/x)`.

        INPUT:

        - ``degree`` -- ``None`` or an integer; if specified, truncate or zero
          pad the list of coefficients to this degree before reversing it

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: f = RR['x']([-3, pi, 0, 1])
            sage: f.reverse()
            -3.00000000000000*x^3 + 3.14159265358979*x^2 + 1.00000000000000
            sage: f.reverse(2)
            -3.00000000000000*x^2 + 3.14159265358979*x
            sage: f.reverse(5)
            -3.00000000000000*x^5 + 3.14159265358979*x^4 + x^2

        TESTS:

        We check that this implementation is compatible with the generic one::

            sage: all(f.reverse(d) == Polynomial.reverse(f, d)                          # needs sage.symbolic
            ....:     for d in [None, 0, 1, 2, 3, 4, 5])
            True"""
    def shift(self, Py_ssize_tn) -> Any:
        """PolynomialRealDense.shift(self, Py_ssize_t n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 312)

        Return this polynomial multiplied by the power `x^n`. If `n`
        is negative, terms below `x^n` will be discarded. Does not
        change this polynomial.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [1, 2, 3]); f
            3.00000000000000*x^2 + 2.00000000000000*x + 1.00000000000000
            sage: f.shift(10)
            3.00000000000000*x^12 + 2.00000000000000*x^11 + x^10
            sage: f.shift(-1)
            3.00000000000000*x + 2.00000000000000
            sage: f.shift(-10)
            0

        TESTS::

            sage: f = RR['x'](0)
            sage: f.shift(3).is_zero()
            True
            sage: f.shift(-3).is_zero()
            True"""
    def truncate(self, longn) -> Polynomial:
        """PolynomialRealDense.truncate(self, long n) -> Polynomial

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 259)

        Return the polynomial of degree `< n` which is equivalent to ``self``
        modulo `x^n`.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RealField(10)['x'], [1, 2, 4, 8])
            sage: f.truncate(3)
            4.0*x^2 + 2.0*x + 1.0
            sage: f.truncate(100)
            8.0*x^3 + 4.0*x^2 + 2.0*x + 1.0
            sage: f.truncate(1)
            1.0
            sage: f.truncate(0)
            0"""
    def truncate_abs(self, RealNumberbound) -> Any:
        """PolynomialRealDense.truncate_abs(self, RealNumber bound)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 288)

        Truncate all high order coefficients below ``bound``.

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RealField(10)['x'], [10^-k for k in range(10)])
            sage: f
            1.0e-9*x^9 + 1.0e-8*x^8 + 1.0e-7*x^7 + 1.0e-6*x^6 + 0.000010*x^5
             + 0.00010*x^4 + 0.0010*x^3 + 0.010*x^2 + 0.10*x + 1.0
            sage: f.truncate_abs(0.5e-6)
            1.0e-6*x^6 + 0.000010*x^5 + 0.00010*x^4 + 0.0010*x^3 + 0.010*x^2 + 0.10*x + 1.0
            sage: f.truncate_abs(10.0)
            0
            sage: f.truncate_abs(1e-100) == f
            True"""
    def __call__(self, *args, **kwds) -> Any:
        """PolynomialRealDense.__call__(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 676)

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [-2, 0, 1])
            sage: f(10)
            98.0000000000000
            sage: f(CC.0)
            -3.00000000000000
            sage: f(2.0000000000000000000000000000000000000000000)
            2.00000000000000
            sage: f(RealField(10)(2))
            2.0
            sage: f(pi)                                                                 # needs sage.symbolic
            1.00000000000000*pi^2 - 2.00000000000000


            sage: f = PolynomialRealDense(RR['x'], range(5))
            sage: f(1)
            10.0000000000000
            sage: f(-1)
            2.00000000000000
            sage: f(0)
            0.000000000000000
            sage: f = PolynomialRealDense(RR['x'])
            sage: f(12)
            0.000000000000000

        TESTS::

            sage: R.<x> = RR[]  # Issue #17311
            sage: (x^2+1)(x=5)
            26.0000000000000"""
    def __neg__(self) -> Any:
        """PolynomialRealDense.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 372)

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [-2,0,1])
            sage: -f
            -x^2 + 2.00000000000000"""
    def __reduce__(self) -> Any:
        """PolynomialRealDense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_real_mpfr_dense.pyx (starting at line 175)

        EXAMPLES::

            sage: from sage.rings.polynomial.polynomial_real_mpfr_dense import PolynomialRealDense
            sage: f = PolynomialRealDense(RR['x'], [-2, 0, 1])
            sage: loads(dumps(f)) == f
            True"""
