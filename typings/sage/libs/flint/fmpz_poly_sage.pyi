import sage.structure.sage_object
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, overload

__pyx_capi__: dict

class Fmpz_poly(sage.structure.sage_object.SageObject):
    """Fmpz_poly(v)"""
    def __init__(self, v) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 38)

                Construct a new fmpz_poly from a sequence, constant coefficient,
                or string (in the same format as it prints).

                EXAMPLES::

                    sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
                    sage: Fmpz_poly([1,2,3])
                    3  1 2 3
                    sage: Fmpz_poly(5)
                    1  5
                    sage: Fmpz_poly(str(Fmpz_poly([3,5,7])))
                    3  3 5 7
        """
    @overload
    def degree(self) -> Any:
        """Fmpz_poly.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 126)

        The degree of ``self``.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,2,3]); f
            3  1 2 3
            sage: f.degree()
            2
            sage: Fmpz_poly(range(1000)).degree()
            999
            sage: Fmpz_poly([2,0]).degree()
            0"""
    @overload
    def degree(self) -> Any:
        """Fmpz_poly.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 126)

        The degree of ``self``.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,2,3]); f
            3  1 2 3
            sage: f.degree()
            2
            sage: Fmpz_poly(range(1000)).degree()
            999
            sage: Fmpz_poly([2,0]).degree()
            0"""
    @overload
    def degree(self) -> Any:
        """Fmpz_poly.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 126)

        The degree of ``self``.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,2,3]); f
            3  1 2 3
            sage: f.degree()
            2
            sage: Fmpz_poly(range(1000)).degree()
            999
            sage: Fmpz_poly([2,0]).degree()
            0"""
    @overload
    def degree(self) -> Any:
        """Fmpz_poly.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 126)

        The degree of ``self``.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,2,3]); f
            3  1 2 3
            sage: f.degree()
            2
            sage: Fmpz_poly(range(1000)).degree()
            999
            sage: Fmpz_poly([2,0]).degree()
            0"""
    @overload
    def derivative(self) -> Any:
        """Fmpz_poly.derivative(self)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 385)

        Return the derivative of ``self``.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,2,6])
            sage: f.derivative().list() == [2, 12]
            True"""
    @overload
    def derivative(self) -> Any:
        """Fmpz_poly.derivative(self)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 385)

        Return the derivative of ``self``.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,2,6])
            sage: f.derivative().list() == [2, 12]
            True"""
    @overload
    def div_rem(self, Fmpz_polyother) -> Any:
        """Fmpz_poly.div_rem(self, Fmpz_poly other)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 310)

        Return ``self / other, self % other``.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,3,4,5])
            sage: g = f^23
            sage: g.div_rem(f)[1]
            0
            sage: g.div_rem(f)[0] - f^22
            0
            sage: f = Fmpz_poly([1..10])
            sage: g = Fmpz_poly([1,3,5])
            sage: q, r = f.div_rem(g)
            sage: q*f+r
            17  1 2 3 4 4 4 10 11 17 18 22 26 30 23 26 18 20
            sage: g
            3  1 3 5
            sage: q*g+r
            10  1 2 3 4 5 6 7 8 9 10"""
    @overload
    def div_rem(self, f) -> Any:
        """Fmpz_poly.div_rem(self, Fmpz_poly other)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 310)

        Return ``self / other, self % other``.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,3,4,5])
            sage: g = f^23
            sage: g.div_rem(f)[1]
            0
            sage: g.div_rem(f)[0] - f^22
            0
            sage: f = Fmpz_poly([1..10])
            sage: g = Fmpz_poly([1,3,5])
            sage: q, r = f.div_rem(g)
            sage: q*f+r
            17  1 2 3 4 4 4 10 11 17 18 22 26 30 23 26 18 20
            sage: g
            3  1 3 5
            sage: q*g+r
            10  1 2 3 4 5 6 7 8 9 10"""
    @overload
    def div_rem(self, f) -> Any:
        """Fmpz_poly.div_rem(self, Fmpz_poly other)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 310)

        Return ``self / other, self % other``.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,3,4,5])
            sage: g = f^23
            sage: g.div_rem(f)[1]
            0
            sage: g.div_rem(f)[0] - f^22
            0
            sage: f = Fmpz_poly([1..10])
            sage: g = Fmpz_poly([1,3,5])
            sage: q, r = f.div_rem(g)
            sage: q*f+r
            17  1 2 3 4 4 4 10 11 17 18 22 26 30 23 26 18 20
            sage: g
            3  1 3 5
            sage: q*g+r
            10  1 2 3 4 5 6 7 8 9 10"""
    @overload
    def div_rem(self, g) -> Any:
        """Fmpz_poly.div_rem(self, Fmpz_poly other)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 310)

        Return ``self / other, self % other``.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,3,4,5])
            sage: g = f^23
            sage: g.div_rem(f)[1]
            0
            sage: g.div_rem(f)[0] - f^22
            0
            sage: f = Fmpz_poly([1..10])
            sage: g = Fmpz_poly([1,3,5])
            sage: q, r = f.div_rem(g)
            sage: q*f+r
            17  1 2 3 4 4 4 10 11 17 18 22 26 30 23 26 18 20
            sage: g
            3  1 3 5
            sage: q*g+r
            10  1 2 3 4 5 6 7 8 9 10"""
    def left_shift(self, unsignedlongn) -> Any:
        """Fmpz_poly.left_shift(self, unsigned long n)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 338)

        Left shift ``self`` by `n`.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,2])
            sage: f.left_shift(1).list() == [0,1,2]
            True"""
    @overload
    def list(self) -> Any:
        """Fmpz_poly.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 144)

        Return ``self`` as a list of coefficients, lowest terms first.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([2,1,0,-1])
            sage: f.list()
            [2, 1, 0, -1]"""
    @overload
    def list(self) -> Any:
        """Fmpz_poly.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 144)

        Return ``self`` as a list of coefficients, lowest terms first.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([2,1,0,-1])
            sage: f.list()
            [2, 1, 0, -1]"""
    def pow_truncate(self, exp, n) -> Any:
        """Fmpz_poly.pow_truncate(self, exp, n)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 267)

        Return ``self`` raised to the power of ``exp`` mod `x^n`.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,2])
            sage: f.pow_truncate(10,3)
            3  1 20 180
            sage: f.pow_truncate(1000,3)
            3  1 2000 1998000"""
    def pseudo_div(self, Fmpz_polyother) -> Any:
        """Fmpz_poly.pseudo_div(self, Fmpz_poly other)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 372)"""
    def pseudo_div_rem(self, Fmpz_polyother) -> Any:
        """Fmpz_poly.pseudo_div_rem(self, Fmpz_poly other)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 378)"""
    def right_shift(self, unsignedlongn) -> Any:
        """Fmpz_poly.right_shift(self, unsigned long n)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 355)

        Right shift ``self`` by `n`.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,2])
            sage: f.right_shift(1).list() == [2]
            True"""
    def truncate(self, n) -> Any:
        """Fmpz_poly.truncate(self, n)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 407)

        Return the truncation of ``self`` at degree `n`.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,1])
            sage: g = f**10; g
            11  1 10 45 120 210 252 210 120 45 10 1
            sage: g.truncate(5)
            5  1 10 45 120 210"""
    def __add__(self, left, right) -> Any:
        """Fmpz_poly.__add__(left, right)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 157)

        Add together two Flint polynomials.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: Fmpz_poly([1,2,3]) + Fmpz_poly(range(6))
            6  1 3 5 3 4 5"""
    def __copy__(self) -> Any:
        """Fmpz_poly.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 402)"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __floordiv__(self, left, right) -> Any:
        """Fmpz_poly.__floordiv__(left, right)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 289)

        Return left // right, truncated.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([3,4,5])
            sage: g = f^5; g
            11  243 1620 6345 16560 32190 47224 53650 46000 29375 12500 3125
            sage: g // f
            9  81 432 1404 2928 4486 4880 3900 2000 625
            sage: f^4
            9  81 432 1404 2928 4486 4880 3900 2000 625"""
    def __getitem__(self, i) -> Any:
        """Fmpz_poly.__getitem__(self, i)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 94)

        Return the `i`-th item of self, which is the coefficient of the `x^i` term.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly(range(100))
            sage: f[13]
            13
            sage: f[200]
            0"""
    def __mul__(self, left, right) -> Any:
        """Fmpz_poly.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 203)

        Return the product of left and right.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([0,1]); g = Fmpz_poly([2,3,4])
            sage: f*g
            4  0 2 3 4
            sage: f = Fmpz_poly([1,0,-1]); g = Fmpz_poly([2,3,4])
            sage: f*g
            5  2 3 2 -3 -4

            Scalar multiplication
            sage: f * 3
            3  3 0 -3
            sage: f * 5r
            3  5 0 -5"""
    def __neg__(self) -> Any:
        """Fmpz_poly.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 189)

        Return the negative of ``self``.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: -Fmpz_poly([2,10,2,3,18,-5])
            6  -2 -10 -2 -3 -18 5"""
    def __pow__(self, n, dummy) -> Any:
        """Fmpz_poly.__pow__(self, n, dummy)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 239)

        Return ``self`` raised to the power of `n`.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly([1,1])
            sage: f**6
            7  1 6 15 20 15 6 1
            sage: f = Fmpz_poly([2])
            sage: f^150
            1  1427247692705959881058285969449495136382746624
            sage: 2^150
            1427247692705959881058285969449495136382746624

            sage: f**(3/2)
            Traceback (most recent call last):
            ...
            TypeError: unable to convert rational 3/2 to an integer"""
    def __radd__(self, other):
        """Return value+self."""
    def __rfloordiv__(self, other):
        """Return value//self."""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __setitem__(self, i, value) -> Any:
        """Fmpz_poly.__setitem__(self, i, value)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 75)

        Set the `i`-th item of self, which is the coefficient of the `x^i` term.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: f = Fmpz_poly(range(10))
            sage: f[7] = 100; f
            10  0 1 2 3 4 5 6 100 8 9
            sage: f[2] = 10**100000
            sage: f[2] == 10**100000
            True"""
    def __sub__(self, left, right) -> Any:
        """Fmpz_poly.__sub__(left, right)

        File: /build/sagemath/src/sage/src/sage/libs/flint/fmpz_poly_sage.pyx (starting at line 173)

        Subtract two Flint polynomials.

        EXAMPLES::

            sage: from sage.libs.flint.fmpz_poly_sage import Fmpz_poly
            sage: Fmpz_poly([10,2,3]) - Fmpz_poly([4,-2,1])
            3  6 4 2"""
