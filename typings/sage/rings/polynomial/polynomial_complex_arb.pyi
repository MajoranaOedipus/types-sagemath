import sage.rings.polynomial.polynomial_element
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Polynomial_complex_arb(sage.rings.polynomial.polynomial_element.Polynomial):
    '''Polynomial_complex_arb(parent, x=None, check=True, is_gen=False, construct=False)

    File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 38)

    Wrapper for `FLINT <https://flintlib.org>`_ polynomials of type
    ``acb_poly_t``

    EXAMPLES::

        sage: Pol.<x> = CBF[]
        sage: type(x)
        <class \'sage.rings.polynomial.polynomial_complex_arb.Polynomial_complex_arb\'>

        sage: Pol(), Pol(1), Pol([0,1,2]), Pol({1: pi, 3: i})                           # needs sage.symbolic
        (0,
         1.000000000000000,
         2.000000000000000*x^2 + x,
         I*x^3 + ([3.141592653589793 +/- ...e-16])*x)

        sage: Pol("x - 2/3")
        x + [-0.666666666666667 +/- ...e-16]
        sage: Pol(polygen(QQ))
        x

        sage: all(Pol.has_coerce_map_from(P) for P in
        ....:     (QQ[\'x\'], QuadraticField(-1), RealBallField(100)))
        True
        sage: any(Pol.has_coerce_map_from(P) for P in
        ....:     (QQ[\'y\'], RR, CC, RDF, CDF, RIF, CIF, RealBallField(20)))
        False'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x=..., check=..., is_gen=..., construct=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 97)

                Initialize this polynomial to the specified value.

                TESTS::

                    sage: from sage.rings.polynomial.polynomial_complex_arb import Polynomial_complex_arb
                    sage: Pol = CBF['x']
                    sage: Polynomial_complex_arb(Pol)
                    0
                    sage: Polynomial_complex_arb(Pol, is_gen=True)
                    x
                    sage: Polynomial_complex_arb(Pol, 42, is_gen=True)
                    x
                    sage: Polynomial_complex_arb(Pol, CBF(1))
                    1.000000000000000
                    sage: Polynomial_complex_arb(Pol, [])
                    0
                    sage: Polynomial_complex_arb(Pol, [0])
                    0
                    sage: Polynomial_complex_arb(Pol, [0, 2, 0])
                    2.000000000000000*x
                    sage: Polynomial_complex_arb(Pol, (1,))
                    1.000000000000000
                    sage: Polynomial_complex_arb(Pol, (CBF(i), 1))                              # needs sage.symbolic
                    x + I
                    sage: Polynomial_complex_arb(Pol, polygen(QQ,'y')+2)
                    x + 2.000000000000000
                    sage: Polynomial_complex_arb(Pol, QQ['x'](0))
                    0
                    sage: Polynomial_complex_arb(Pol, {10: pi})                                 # needs sage.symbolic
                    ([3.141592653589793 +/- ...e-16])*x^10
                    sage: Polynomial_complex_arb(Pol, pi)                                       # needs sage.symbolic
                    [3.141592653589793 +/- ...e-16]
        """
    def compose_trunc(self, Polynomialother, longn) -> Any:
        """Polynomial_complex_arb.compose_trunc(self, Polynomial other, long n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 829)

        Return the composition of ``self`` and ``other``, truncated before degree\xa0`n`.

        EXAMPLES::

            sage: Pol.<x> = CBF[]
            sage: Pol.<x> = CBF[]
            sage: pol = x*(x-1)^2
            sage: pol.compose_trunc(x + x^2, 4)
            -3.000000000000000*x^3 - x^2 + x
            sage: pol.compose_trunc(1 + x, 4)
            x^3 + x^2
            sage: pol.compose_trunc(2 + x/3, 2)
            ([1.666666666666667 +/- ...e-16])*x + 2.000000000000000
            sage: pol.compose_trunc(2 + x/3, 0)
            0
            sage: pol.compose_trunc(2 + x/3, -1)
            0"""
    @overload
    def degree(self) -> Any:
        """Polynomial_complex_arb.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 214)

        Return the (apparent) degree of this polynomial.

        EXAMPLES::

            sage: Pol.<x> = CBF[]
            sage: (x^2 + 1).degree()
            2
            sage: pol = (x/3 + 1) - x/3; pol
            ([+/- ...e-16])*x + 1.000000000000000
            sage: pol.degree()
            1
            sage: Pol([1, 0, 0, 0]).degree()
            0"""
    @overload
    def degree(self) -> Any:
        """Polynomial_complex_arb.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 214)

        Return the (apparent) degree of this polynomial.

        EXAMPLES::

            sage: Pol.<x> = CBF[]
            sage: (x^2 + 1).degree()
            2
            sage: pol = (x/3 + 1) - x/3; pol
            ([+/- ...e-16])*x + 1.000000000000000
            sage: pol.degree()
            1
            sage: Pol([1, 0, 0, 0]).degree()
            0"""
    @overload
    def degree(self) -> Any:
        """Polynomial_complex_arb.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 214)

        Return the (apparent) degree of this polynomial.

        EXAMPLES::

            sage: Pol.<x> = CBF[]
            sage: (x^2 + 1).degree()
            2
            sage: pol = (x/3 + 1) - x/3; pol
            ([+/- ...e-16])*x + 1.000000000000000
            sage: pol.degree()
            1
            sage: Pol([1, 0, 0, 0]).degree()
            0"""
    @overload
    def degree(self) -> Any:
        """Polynomial_complex_arb.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 214)

        Return the (apparent) degree of this polynomial.

        EXAMPLES::

            sage: Pol.<x> = CBF[]
            sage: (x^2 + 1).degree()
            2
            sage: pol = (x/3 + 1) - x/3; pol
            ([+/- ...e-16])*x + 1.000000000000000
            sage: pol.degree()
            1
            sage: Pol([1, 0, 0, 0]).degree()
            0"""
    def inverse_series_trunc(self, longn) -> Polynomial:
        """Polynomial_complex_arb.inverse_series_trunc(self, long n) -> Polynomial

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 563)

        Return the power series expansion at\xa00 of the inverse of this
        polynomial, truncated before degree\xa0`n`.

        EXAMPLES::

            sage: Pol.<x> = CBF[]
            sage: (1 - x/3).inverse_series_trunc(3)
            ([0.1111111111111111 +/- ...e-17])*x^2 + ([0.3333333333333333 +/- ...e-17])*x + 1.000000000000000
            sage: x.inverse_series_trunc(1)
            nan
            sage: Pol(0).inverse_series_trunc(2)
            (nan + nan*I)*x + nan + nan*I

        TESTS::

            sage: Pol(0).inverse_series_trunc(-1)
            0"""
    @overload
    def list(self, boolcopy=...) -> list:
        """Polynomial_complex_arb.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 238)

        Return the coefficient list of this polynomial.

        EXAMPLES::

            sage: Pol.<x> = CBF[]
            sage: (x^2/3).list()
            [0, 0, [0.3333333333333333 +/- ...e-17]]
            sage: Pol(0).list()
            []
            sage: Pol([0, 1, RBF(0, rad=.1), 0]).list()
            [0, 1.000000000000000, [+/- 0.101]]"""
    @overload
    def list(self) -> Any:
        """Polynomial_complex_arb.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 238)

        Return the coefficient list of this polynomial.

        EXAMPLES::

            sage: Pol.<x> = CBF[]
            sage: (x^2/3).list()
            [0, 0, [0.3333333333333333 +/- ...e-17]]
            sage: Pol(0).list()
            []
            sage: Pol([0, 1, RBF(0, rad=.1), 0]).list()
            [0, 1.000000000000000, [+/- 0.101]]"""
    @overload
    def list(self) -> Any:
        """Polynomial_complex_arb.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 238)

        Return the coefficient list of this polynomial.

        EXAMPLES::

            sage: Pol.<x> = CBF[]
            sage: (x^2/3).list()
            [0, 0, [0.3333333333333333 +/- ...e-17]]
            sage: Pol(0).list()
            []
            sage: Pol([0, 1, RBF(0, rad=.1), 0]).list()
            [0, 1.000000000000000, [+/- 0.101]]"""
    @overload
    def list(self) -> Any:
        """Polynomial_complex_arb.list(self, bool copy=True) -> list

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 238)

        Return the coefficient list of this polynomial.

        EXAMPLES::

            sage: Pol.<x> = CBF[]
            sage: (x^2/3).list()
            [0, 0, [0.3333333333333333 +/- ...e-17]]
            sage: Pol(0).list()
            []
            sage: Pol([0, 1, RBF(0, rad=.1), 0]).list()
            [0, 1.000000000000000, [+/- 0.101]]"""
    @overload
    def quo_rem(self, divisor) -> Any:
        """Polynomial_complex_arb.quo_rem(self, divisor)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 381)

        Compute the Euclidean division of this ball polynomial by ``divisor``.

        Raises a :exc:`ZeroDivisionError` when the divisor is zero or its leading
        coefficient contains zero. Returns a pair (quotient, remainder)
        otherwise.

        EXAMPLES::

            sage: Pol.<x> = CBF[]

            sage: (x^3/7 - CBF(i)).quo_rem(x + CBF(pi))                                 # needs sage.symbolic
            (([0.1428571428571428 +/- ...e-17])*x^2
               + ([-0.448798950512828 +/- ...e-16])*x
               + [1.409943485869908 +/- ...e-16],
             [-4.42946809718569 +/- ...e-15] - I)

            sage: Pol(0).quo_rem(x + 1)
            (0, 0)

            sage: (x + 1).quo_rem(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ('cannot divide by this polynomial', 0)

            sage: div = (x^2/3 + x + 1) - x^2/3; div
            ([+/- ...e-16])*x^2 + x + 1.000000000000000
            sage: (x + 1).quo_rem(div)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ('cannot divide by this polynomial',
            ([+/- ...e-16])*x^2 + x + 1.000000000000000)"""
    @overload
    def quo_rem(self, div) -> Any:
        """Polynomial_complex_arb.quo_rem(self, divisor)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 381)

        Compute the Euclidean division of this ball polynomial by ``divisor``.

        Raises a :exc:`ZeroDivisionError` when the divisor is zero or its leading
        coefficient contains zero. Returns a pair (quotient, remainder)
        otherwise.

        EXAMPLES::

            sage: Pol.<x> = CBF[]

            sage: (x^3/7 - CBF(i)).quo_rem(x + CBF(pi))                                 # needs sage.symbolic
            (([0.1428571428571428 +/- ...e-17])*x^2
               + ([-0.448798950512828 +/- ...e-16])*x
               + [1.409943485869908 +/- ...e-16],
             [-4.42946809718569 +/- ...e-15] - I)

            sage: Pol(0).quo_rem(x + 1)
            (0, 0)

            sage: (x + 1).quo_rem(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ('cannot divide by this polynomial', 0)

            sage: div = (x^2/3 + x + 1) - x^2/3; div
            ([+/- ...e-16])*x^2 + x + 1.000000000000000
            sage: (x + 1).quo_rem(div)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: ('cannot divide by this polynomial',
            ([+/- ...e-16])*x^2 + x + 1.000000000000000)"""
    def revert_series(self, longn) -> Any:
        """Polynomial_complex_arb.revert_series(self, long n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 878)

        Return a polynomial ``f`` such that
        ``f(self(x)) = self(f(x)) = x mod x^n``.

        EXAMPLES::

            sage: Pol.<x> = CBF[]

            sage: (2*x).revert_series(5)
            0.5000000000000000*x

            sage: (x + x^3/6 + x^5/120).revert_series(6)
            ([0.075000000000000 +/- ...e-17])*x^5 + ([-0.166666666666667 +/- ...e-16])*x^3 + x

            sage: (1 + x).revert_series(6)
            Traceback (most recent call last):
            ...
            ValueError: the constant coefficient must be zero

            sage: (x^2).revert_series(6)
            Traceback (most recent call last):
            ...
            ValueError: the linear term must be nonzero"""
    def truncate(self, longn) -> Polynomial:
        """Polynomial_complex_arb.truncate(self, long n) -> Polynomial

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 430)

        Return the truncation to degree `n - 1` of this polynomial.

        EXAMPLES::

            sage: pol = CBF['x'](range(1,5)); pol
            4.000000000000000*x^3 + 3.000000000000000*x^2 + 2.000000000000000*x + 1.000000000000000
            sage: pol.truncate(2)
            2.000000000000000*x + 1.000000000000000
            sage: pol.truncate(0)
            0
            sage: pol.truncate(-1)
            0

        TESTS::

            sage: pol.truncate(6)
            4.000000000000000*x^3 + 3.000000000000000*x^2 + 2.000000000000000*x + 1.000000000000000
            sage: pol.truncate(4)
            4.000000000000000*x^3 + 3.000000000000000*x^2 + 2.000000000000000*x + 1.000000000000000"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *x, **kwds) -> Any:
        """Polynomial_complex_arb.__call__(self, *x, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 917)

        Evaluate this polynomial.

        EXAMPLES::

            sage: Pol.<x> = CBF[]
            sage: pol = x^2 - 1
            sage: pol(CBF(pi))                                                          # needs sage.symbolic
            [8.86960440108936 +/- ...e-15]
            sage: pol(x^3 + 1)
            x^6 + 2.000000000000000*x^3
            sage: pol(matrix([[1,2],[3,4]]))
            [6.000000000000000 10.00000000000000]
            [15.00000000000000 21.00000000000000]

        TESTS::

            sage: P.<x> = CBF[]
            sage: Q.<y> = CBF[]
            sage: x(y)
            y"""
    def __lshift__(self, val, n) -> Any:
        """Polynomial_complex_arb.__lshift__(val, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 467)

        Shift ``val`` to the left, i.e. multiply it by `x^n`, throwing away
        coefficients if `n < 0`.

        EXAMPLES::

            sage: pol = CBF['x'](range(1,5)); pol
            4.000000000000000*x^3 + 3.000000000000000*x^2 + 2.000000000000000*x + 1.000000000000000
            sage: pol << 2
            4.000000000000000*x^5 + 3.000000000000000*x^4 + 2.000000000000000*x^3 + x^2
            sage: pol << (-2)
            4.000000000000000*x + 3.000000000000000

        TESTS::

            sage: 1 << pol
            Traceback (most recent call last):
            ...
            TypeError: unsupported operands for <<: 1, 4.000000000000000*x^3 + 3.000000000000000*x^2 + 2.000000000000000*x + 1.000000000000000"""
    def __reduce__(self) -> Any:
        """Polynomial_complex_arb.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 194)

        Serialize a polynomial for pickling.

        TESTS::

            sage: # needs sage.symbolic
            sage: Pol.<x> = ComplexBallField(42)[]
            sage: pol = (x + i)/3
            sage: pol2 = loads(dumps(pol))
            sage: pol.degree() == pol2.degree()
            True
            sage: all(a.identical(b) for (a, b) in zip(pol, pol2))
            True"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, val, n) -> Any:
        """Polynomial_complex_arb.__rshift__(val, n)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_complex_arb.pyx (starting at line 500)

        Shift ``val`` to the left, i.e. divide it by `x^n`, throwing away
        coefficients if `n > 0`.

        EXAMPLES::

            sage: pol = CBF['x'](range(1,5)); pol
            4.000000000000000*x^3 + 3.000000000000000*x^2 + 2.000000000000000*x + 1.000000000000000
            sage: pol >> 2
            4.000000000000000*x + 3.000000000000000
            sage: pol >> -2
            4.000000000000000*x^5 + 3.000000000000000*x^4 + 2.000000000000000*x^3 + x^2

        TESTS::

            sage: 1 >> pol
            Traceback (most recent call last):
            ...
            TypeError: unsupported operands for >>: 1, 4.000000000000000*x^3 + 3.000000000000000*x^2 + 2.000000000000000*x + 1.000000000000000"""
