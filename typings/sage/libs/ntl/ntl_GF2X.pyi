import _cython_3_2_1
from sage.libs.ntl.ntl_ZZ import unpickle_class_value as unpickle_class_value
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, overload

GF2XHexOutput: _cython_3_2_1.cython_function_or_method

class ntl_GF2X:
    """ntl_GF2X(x=[])

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 88)

    Univariate Polynomials over GF(2) via NTL."""
    def __init__(self, x=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 92)

                Construct a new polynomial over GF(2).

                A value may be passed to this constructor. If you pass a string
                to the constructor please note that byte sequences and the hexadecimal
                notation are little endian.  So e.g. '[0 1]' == '0x2' == x.

                Input types are ntl.ZZ_px, strings, lists of digits, FiniteFieldElements
                from extension fields over GF(2), Polynomials over GF(2), Integers, and finite
                extension fields over GF(2) (uses modulus).

                INPUT:

                - ``x`` -- value to be assigned to this element. See examples.

                OUTPUT: a new ntl.GF2X element

                EXAMPLES::

                    sage: ntl.GF2X(ntl.ZZ_pX([1,1,3],2))
                    [1 1 1]
                    sage: ntl.GF2X('0x1c')
                    [1 0 0 0 0 0 1 1]
                    sage: ntl.GF2X('[1 0 1 0]')
                    [1 0 1]
                    sage: ntl.GF2X([1,0,1,0])
                    [1 0 1]
                    sage: ntl.GF2X(GF(2**8,'a').gen()**20)
                    [0 0 1 0 1 1 0 1]
                    sage: ntl.GF2X(GF(2**8,'a'))
                    [1 0 1 1 1 0 0 0 1]
                    sage: ntl.GF2X(2)
                    [0 1]
                    sage: ntl.GF2X(ntl.GF2(1))
                    [1]

                    sage: R.<x> = GF(2)[]
                    sage: f = x^5+x^2+1
                    sage: ntl.GF2X(f)
                    [1 0 1 0 0 1]
        """
    @overload
    def ConstTerm(self) -> Any:
        """ntl_GF2X.ConstTerm(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 617)

        Return the constant term of ``self``.

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1])
            sage: e.ConstTerm()
            1
            sage: e = ntl.GF2X(0)
            sage: e.ConstTerm()
            0"""
    @overload
    def ConstTerm(self) -> Any:
        """ntl_GF2X.ConstTerm(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 617)

        Return the constant term of ``self``.

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1])
            sage: e.ConstTerm()
            1
            sage: e = ntl.GF2X(0)
            sage: e.ConstTerm()
            0"""
    @overload
    def ConstTerm(self) -> Any:
        """ntl_GF2X.ConstTerm(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 617)

        Return the constant term of ``self``.

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1])
            sage: e.ConstTerm()
            1
            sage: e = ntl.GF2X(0)
            sage: e.ConstTerm()
            0"""
    def DivRem(self, b) -> Any:
        """ntl_GF2X.DivRem(self, b)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 229)

        EXAMPLES::

            sage: a = ntl.GF2X(4)
            sage: a.DivRem( ntl.GF2X(2) )
            ([0 1], [])
            sage: a.DivRem( ntl.GF2X(3) )
            ([1 1], [1])"""
    @overload
    def GCD(self, other) -> Any:
        """ntl_GF2X.GCD(self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 406)

        Return GCD of ``self`` and ``other``.

        INPUT:

        - ``other`` -- ntl.GF2X

        EXAMPLES::

            sage: a = ntl.GF2X(10)
            sage: b = ntl.GF2X(4)
            sage: a.GCD(b)
            [0 1]"""
    @overload
    def GCD(self, b) -> Any:
        """ntl_GF2X.GCD(self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 406)

        Return GCD of ``self`` and ``other``.

        INPUT:

        - ``other`` -- ntl.GF2X

        EXAMPLES::

            sage: a = ntl.GF2X(10)
            sage: b = ntl.GF2X(4)
            sage: a.GCD(b)
            [0 1]"""
    @overload
    def LeadCoeff(self) -> Any:
        """ntl_GF2X.LeadCoeff(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 598)

        Return the leading coefficient of ``self``.

        This is always 1 except when ``self == 0``.

        EXAMPLES::

            sage: e = ntl.GF2X([0,1])
            sage: e.LeadCoeff()
            1
            sage: e = ntl.GF2X(0)
            sage: e.LeadCoeff()
            0"""
    @overload
    def LeadCoeff(self) -> Any:
        """ntl_GF2X.LeadCoeff(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 598)

        Return the leading coefficient of ``self``.

        This is always 1 except when ``self == 0``.

        EXAMPLES::

            sage: e = ntl.GF2X([0,1])
            sage: e.LeadCoeff()
            1
            sage: e = ntl.GF2X(0)
            sage: e.LeadCoeff()
            0"""
    @overload
    def LeadCoeff(self) -> Any:
        """ntl_GF2X.LeadCoeff(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 598)

        Return the leading coefficient of ``self``.

        This is always 1 except when ``self == 0``.

        EXAMPLES::

            sage: e = ntl.GF2X([0,1])
            sage: e.LeadCoeff()
            1
            sage: e = ntl.GF2X(0)
            sage: e.LeadCoeff()
            0"""
    @overload
    def NumBits(self) -> Any:
        """ntl_GF2X.NumBits(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 728)

        Return the number of bits of self, i.e., deg(self) + 1.

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0])
            sage: e.NumBits()
            4"""
    @overload
    def NumBits(self) -> Any:
        """ntl_GF2X.NumBits(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 728)

        Return the number of bits of self, i.e., deg(self) + 1.

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0])
            sage: e.NumBits()
            4"""
    @overload
    def NumBytes(self) -> Any:
        """ntl_GF2X.NumBytes(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 750)

        Return the number of bytes of ``self``, i.e., floor((NumBits(self)+7)/8).

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1])
            sage: e.NumBytes()
            3"""
    @overload
    def NumBytes(self) -> Any:
        """ntl_GF2X.NumBytes(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 750)

        Return the number of bytes of ``self``, i.e., floor((NumBits(self)+7)/8).

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,1,1])
            sage: e.NumBytes()
            3"""
    def SetCoeff(self, inti, a) -> Any:
        """ntl_GF2X.SetCoeff(self, int i, a)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 634)

        Set the value of a coefficient of ``self``.

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1]); e
            [1 0 1]
            sage: e.SetCoeff(1,1)
            sage: e
            [1 1 1]"""
    @overload
    def XGCD(self, other) -> Any:
        """ntl_GF2X.XGCD(self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 429)

        Return the extended gcd of ``self`` and ``other``, i.e., elements r, s, t such that.

            r = s  * self + t  * other.

        INPUT:

        - ``other`` -- ntl.GF2X

        EXAMPLES::

            sage: a = ntl.GF2X(10)
            sage: b = ntl.GF2X(4)
            sage: r,s,t = a.XGCD(b)
            sage: r == a*s + t*b
            True"""
    @overload
    def XGCD(self, b) -> Any:
        """ntl_GF2X.XGCD(self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 429)

        Return the extended gcd of ``self`` and ``other``, i.e., elements r, s, t such that.

            r = s  * self + t  * other.

        INPUT:

        - ``other`` -- ntl.GF2X

        EXAMPLES::

            sage: a = ntl.GF2X(10)
            sage: b = ntl.GF2X(4)
            sage: r,s,t = a.XGCD(b)
            sage: r == a*s + t*b
            True"""
    def bin(self) -> Any:
        """ntl_GF2X.bin(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 486)

        Return binary representation of this element.

        It is the same as setting \\code{ntl.GF2XHexOutput(False)} and
        representing this element afterwards. However it should be
        faster and preserves the HexOutput state as opposed to the above code.

        EXAMPLES::

             sage: e=ntl.GF2X([1,1,0,1,1,1,0,0,1])
             sage: e.bin()
             '[1 1 0 1 1 1 0 0 1]'

        OUTPUT:

        string representing this element in binary digits"""
    def coeff(self, inti) -> Any:
        """ntl_GF2X.coeff(self, int i)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 564)

        Return the coefficient of the monomial `X^i` in ``self``.

        INPUT:

        - ``i`` -- degree of X

        EXAMPLES::

            sage: e = ntl.GF2X([0,1,0,1])
            sage: e.coeff(0)
            0
            sage: e.coeff(1)
            1"""
    @overload
    def deg(self) -> Any:
        """ntl_GF2X.deg(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 457)

        Return the degree of this polynomial.

        EXAMPLES::

            sage: ntl.GF2X([1,0,1,1]).deg()
            3"""
    @overload
    def deg(self) -> Any:
        """ntl_GF2X.deg(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 457)

        Return the degree of this polynomial.

        EXAMPLES::

            sage: ntl.GF2X([1,0,1,1]).deg()
            3"""
    @overload
    def diff(self) -> Any:
        """ntl_GF2X.diff(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 663)

        Differentiate ``self``.

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0])
            sage: e.diff()
            [0 0 1]"""
    @overload
    def diff(self) -> Any:
        """ntl_GF2X.diff(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 663)

        Differentiate ``self``.

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0])
            sage: e.diff()
            [0 0 1]"""
    def hex(self) -> Any:
        """ntl_GF2X.hex(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 510)

        Return a hexadecimal representation of this element.

        It is the same as setting \\code{ntl.GF2XHexOutput(True)} and
        representing this element afterwards. However it should be faster and
        preserves the HexOutput state as opposed to the above code.

        OUTPUT: string representing this element in hexadecimal

        EXAMPLES::

            sage: e = ntl.GF2X([1,1,0,1,1,1,0,0,1])
            sage: e.hex()
            '0xb31'"""
    @overload
    def list(self) -> Any:
        """ntl_GF2X.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 468)

        Represent this element as a list of binary digits.

        EXAMPLES::

             sage: e=ntl.GF2X([0,1,1])
             sage: e.list()
             [0, 1, 1]
             sage: e=ntl.GF2X('0xff')
             sage: e.list()
             [1, 1, 1, 1, 1, 1, 1, 1]

        OUTPUT: list of digits representing the coefficients in this element's
        polynomial representation"""
    @overload
    def list(self) -> Any:
        """ntl_GF2X.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 468)

        Represent this element as a list of binary digits.

        EXAMPLES::

             sage: e=ntl.GF2X([0,1,1])
             sage: e.list()
             [0, 1, 1]
             sage: e=ntl.GF2X('0xff')
             sage: e.list()
             [1, 1, 1, 1, 1, 1, 1, 1]

        OUTPUT: list of digits representing the coefficients in this element's
        polynomial representation"""
    @overload
    def list(self) -> Any:
        """ntl_GF2X.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 468)

        Represent this element as a list of binary digits.

        EXAMPLES::

             sage: e=ntl.GF2X([0,1,1])
             sage: e.list()
             [0, 1, 1]
             sage: e=ntl.GF2X('0xff')
             sage: e.list()
             [1, 1, 1, 1, 1, 1, 1, 1]

        OUTPUT: list of digits representing the coefficients in this element's
        polynomial representation"""
    @overload
    def reverse(self, inthi=...) -> Any:
        """ntl_GF2X.reverse(self, int hi=-2)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 677)

        Return reverse of a[0]..a[hi] (hi >= -1)
        hi defaults to deg(a)

        INPUT:

        - ``hi`` -- bit position until which reverse is requested

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0])
            sage: e.reverse()
            [1 1 0 1]"""
    @overload
    def reverse(self) -> Any:
        """ntl_GF2X.reverse(self, int hi=-2)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 677)

        Return reverse of a[0]..a[hi] (hi >= -1)
        hi defaults to deg(a)

        INPUT:

        - ``hi`` -- bit position until which reverse is requested

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0])
            sage: e.reverse()
            [1 1 0 1]"""
    @overload
    def weight(self) -> Any:
        """ntl_GF2X.weight(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 698)

        Return the number of nonzero coefficients in ``self``.

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0])
            sage: e.weight()
            3"""
    @overload
    def weight(self) -> Any:
        """ntl_GF2X.weight(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 698)

        Return the number of nonzero coefficients in ``self``.

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0])
            sage: e.weight()
            3"""
    def __add__(self, ntl_GF2Xself, other) -> Any:
        """ntl_GF2X.__add__(ntl_GF2X self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 300)

        EXAMPLES::

            sage: f = ntl.GF2X([1,0,1,1]) ; g = ntl.GF2X([0,1,0])
            sage: f + g ## indirect doctest
            [1 1 1 1]"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __floordiv__(self, ntl_GF2Xself, b) -> Any:
        """ntl_GF2X.__floordiv__(ntl_GF2X self, b)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 248)

        EXAMPLES::

            sage: a = ntl.GF2X(4)
            sage: a // ntl.GF2X(2)
            [0 1]
            sage: a // ntl.GF2X(3)
            [1 1]"""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, inti) -> Any:
        """ntl_GF2X.__getitem__(self, int i)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 584)

        EXAMPLES::

            sage: e = ntl.GF2X([0,1,0,1])
            sage: e[0] # indirect doctest
            0
            sage: e[1]
            1"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __hash__(self) -> Any:
        """ntl_GF2X.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 532)"""
    def __int__(self) -> Any:
        """ntl_GF2X.__int__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 710)

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0])
            sage: int(e)
            Traceback (most recent call last):
            ...
            ValueError: cannot convert non-constant polynomial to integer
            sage: e = ntl.GF2X([1])
            sage: int(e)
            1"""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __len__(self) -> Any:
        """ntl_GF2X.__len__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 740)

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1,1,0])
            sage: len(e)
            4"""
    def __lshift__(self, ntl_GF2Xself, inti) -> Any:
        """ntl_GF2X.__lshift__(ntl_GF2X self, int i)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 366)

        Return left shift of ``self`` by i bits ( == multiplication by
        `X^i`).

        INPUT:

        - ``i`` -- offset/power of X

        EXAMPLES::

            sage: a = ntl.GF2X(4); a
            [0 0 1]
            sage: a << 2
            [0 0 0 0 1]"""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mod__(self, ntl_GF2Xself, b) -> Any:
        """ntl_GF2X.__mod__(ntl_GF2X self, b)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 266)

        EXAMPLES::

            sage: a = ntl.GF2X(4)
            sage: a % ntl.GF2X(2)
            []
            sage: a % ntl.GF2X(3)
            [1]"""
    def __mul__(self, ntl_GF2Xself, other) -> Any:
        """ntl_GF2X.__mul__(ntl_GF2X self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 192)

        EXAMPLES::

            sage: f = ntl.GF2X([1,0,1,1]) ; g = ntl.GF2X([0,1])
            sage: f*g ## indirect doctest
            [0 1 0 1 1]"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_GF2X.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 314)

        EXAMPLES::

            sage: f = ntl.GF2X([1,0,1,1])
            sage: -f ## indirect doctest
            [1 0 1 1]
            sage: f == -f
            True"""
    def __pow__(self, ntl_GF2Xself, longe, ignored) -> Any:
        """ntl_GF2X.__pow__(ntl_GF2X self, long e, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 328)

        EXAMPLES::

            sage: f = ntl.GF2X([1,0,1,1]) ; g = ntl.GF2X([0,1,0])
            sage: f**3 ## indirect doctest
            [1 0 1 1 1 0 0 1 1 1]"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_GF2X.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 168)

        EXAMPLES::

            sage: f = ntl.GF2X(ntl.ZZ_pX([1,1,3],2))
            sage: loads(dumps(f)) == f
            True
            sage: f = ntl.GF2X('0x1c')
            sage: loads(dumps(f)) == f
            True"""
    def __rfloordiv__(self, other):
        """Return value//self."""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rmod__(self, other):
        """Return value%self."""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, ntl_GF2Xself, intoffset) -> Any:
        """ntl_GF2X.__rshift__(ntl_GF2X self, int offset)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 386)

        Return right shift of ``self`` by i bits ( == floor division by
        `X^i`).

        INPUT:

        - ``i`` -- offset/power of X

        EXAMPLES::

            sage: a = ntl.GF2X(4); a
            [0 0 1]
            sage: a >> 1
            [0 1]"""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __setitem__(self, inti, a) -> Any:
        """ntl_GF2X.__setitem__(self, int i, a)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 650)

        EXAMPLES::

            sage: e = ntl.GF2X([1,0,1]); e
            [1 0 1]
            sage: e[1] = 1 # indirect doctest
            sage: e
            [1 1 1]"""
    def __sub__(self, ntl_GF2Xself, other) -> Any:
        """ntl_GF2X.__sub__(ntl_GF2X self, other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 284)

        EXAMPLES::

            sage: f = ntl.GF2X([1,0,1,1]) ; g = ntl.GF2X([0,1])
            sage: f - g ## indirect doctest
            [1 1 1 1]
            sage: g - f
            [1 1 1 1]"""
    def __truediv__(self, ntl_GF2Xself, b) -> Any:
        """ntl_GF2X.__truediv__(ntl_GF2X self, b)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_GF2X.pyx (starting at line 206)

        EXAMPLES::

            sage: a = ntl.GF2X(4)
            sage: a / ntl.GF2X(2)
            [0 1]
            sage: a / ntl.GF2X(3)
            Traceback (most recent call last):
            ...
            ArithmeticError: self (=[0 0 1]) is not divisible by b (=[1 1])"""
