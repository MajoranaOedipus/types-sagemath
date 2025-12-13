from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.libs.ntl.ntl_ZZ import unpickle_class_args as unpickle_class_args
from sage.libs.ntl.ntl_ZZ_pContext import ntl_ZZ_pContext as ntl_ZZ_pContext
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class ntl_ZZ_pX:
    """ntl_ZZ_pX(v=None, modulus=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 66)

    The class \\class{ZZ_pX} implements polynomial arithmetic modulo `p`.

    Polynomial arithmetic is implemented using the FFT, combined with
    the Chinese Remainder Theorem.  A more detailed description of the
    techniques used here can be found in [Shoup, J. Symbolic
    Comp. 20:363-397, 1995].

    Small degree polynomials are multiplied either with classical
    or Karatsuba algorithms."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, v=..., modulus=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 80)

                EXAMPLES::

                    sage: c = ntl.ZZ_pContext(ntl.ZZ(20))
                    sage: f = ntl.ZZ_pX([1,2,5,-9], c)
                    sage: f
                    [1 2 5 11]
                    sage: g = ntl.ZZ_pX([0,0,0], c); g
                    []
                    sage: g[10]=5
                    sage: g
                    [0 0 0 0 0 0 0 0 0 0 5]
                    sage: g[10]
                    5
        """
    @overload
    def charpoly_mod(self, ntl_ZZ_pXmodulus) -> Any:
        """ntl_ZZ_pX.charpoly_mod(self, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1387)

        Return the characteristic polynomial of this polynomial modulo
        the modulus.  The modulus must be monic of degree bigger than
        ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,0,3],c)
            sage: mod = ntl.ZZ_pX([-5,2,0,0,1],c)
            sage: f.charpoly_mod(mod)
            [11 1 8 14 1]"""
    @overload
    def charpoly_mod(self, mod) -> Any:
        """ntl_ZZ_pX.charpoly_mod(self, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1387)

        Return the characteristic polynomial of this polynomial modulo
        the modulus.  The modulus must be monic of degree bigger than
        ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,0,3],c)
            sage: mod = ntl.ZZ_pX([-5,2,0,0,1],c)
            sage: f.charpoly_mod(mod)
            [11 1 8 14 1]"""
    @overload
    def clear(self) -> Any:
        """ntl_ZZ_pX.clear(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1433)

        Reset this polynomial to 0.  Changes this polynomial in place.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3],c)
            sage: f
            [1 2 3]
            sage: f.clear()
            sage: f
            []"""
    @overload
    def clear(self) -> Any:
        """ntl_ZZ_pX.clear(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1433)

        Reset this polynomial to 0.  Changes this polynomial in place.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3],c)
            sage: f
            [1 2 3]
            sage: f.clear()
            sage: f
            []"""
    def compose_mod(self, ntl_ZZ_pXother, ntl_ZZ_pXmodulus) -> Any:
        """ntl_ZZ_pX.compose_mod(self, ntl_ZZ_pX other, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1475)

        Compute `f(g) \\bmod h`.

        To be precise about the order fo compostion, given ``self``, ``other``
        and ``modulus`` as `f(x)`, `g(x)` and `h(x)` compute `f(g(x)) \\bmod h(x)`.

        INPUT:

        - ``other`` -- a polynomial `g(x)`
        - ``modulus`` -- a polynomial `h(x)`

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3],c)
            sage: g = ntl.ZZ_pX([3,2,1],c)
            sage: h = ntl.ZZ_pX([1,0,1],c)
            sage: f.compose_mod(g, h)
            [5 11]

        AUTHORS:

        - Giacomo Pope (2024-08) initial implementation"""
    @overload
    def constant_term(self) -> Any:
        """ntl_ZZ_pX.constant_term(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 855)

        Return the constant coefficient of this polynomial.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([3,6,9],c)
            sage: f.constant_term()
            3
            sage: f = ntl.ZZ_pX([],c)
            sage: f.constant_term()
            0"""
    @overload
    def constant_term(self) -> Any:
        """ntl_ZZ_pX.constant_term(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 855)

        Return the constant coefficient of this polynomial.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([3,6,9],c)
            sage: f.constant_term()
            3
            sage: f = ntl.ZZ_pX([],c)
            sage: f.constant_term()
            0"""
    @overload
    def constant_term(self) -> Any:
        """ntl_ZZ_pX.constant_term(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 855)

        Return the constant coefficient of this polynomial.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([3,6,9],c)
            sage: f.constant_term()
            3
            sage: f = ntl.ZZ_pX([],c)
            sage: f.constant_term()
            0"""
    def convert_to_modulus(self, ntl_ZZ_pContext_classc) -> Any:
        """ntl_ZZ_pX.convert_to_modulus(self, ntl_ZZ_pContext_class c)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 918)

        Return a new ntl_ZZ_pX which is the same as self, but considered modulo a different p.

        In order for this to make mathematical sense, c.p should divide self.c.p
        (in which case ``self`` is reduced modulo c.p) or self.c.p should divide c.p
        (in which case ``self`` is lifted to something modulo c.p congruent to ``self`` modulo self.c.p)

        EXAMPLES::

            sage: a = ntl.ZZ_pX([412,181,991],5^4)
            sage: a
            [412 181 366]
            sage: b = ntl.ZZ_pX([198,333,91],5^4)
            sage: ap = a.convert_to_modulus(ntl.ZZ_pContext(5^2))
            sage: bp = b.convert_to_modulus(ntl.ZZ_pContext(5^2))
            sage: ap
            [12 6 16]
            sage: bp
            [23 8 16]
            sage: ap*bp
            [1 9 8 24 6]
            sage: (a*b).convert_to_modulus(ntl.ZZ_pContext(5^2))
            [1 9 8 24 6]"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZ_pX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 811)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([5,0,1],c)
            sage: f.degree()
            2
            sage: f = ntl.ZZ_pX(range(100),c)
            sage: f.degree()
            99
            sage: f = ntl.ZZ_pX([], c)
            sage: f.degree()
            -1
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZ_pX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 811)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([5,0,1],c)
            sage: f.degree()
            2
            sage: f = ntl.ZZ_pX(range(100),c)
            sage: f.degree()
            99
            sage: f = ntl.ZZ_pX([], c)
            sage: f.degree()
            -1
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZ_pX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 811)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([5,0,1],c)
            sage: f.degree()
            2
            sage: f = ntl.ZZ_pX(range(100),c)
            sage: f.degree()
            99
            sage: f = ntl.ZZ_pX([], c)
            sage: f.degree()
            -1
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZ_pX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 811)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([5,0,1],c)
            sage: f.degree()
            2
            sage: f = ntl.ZZ_pX(range(100),c)
            sage: f.degree()
            99
            sage: f = ntl.ZZ_pX([], c)
            sage: f.degree()
            -1
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZ_pX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 811)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([5,0,1],c)
            sage: f.degree()
            2
            sage: f = ntl.ZZ_pX(range(100),c)
            sage: f.degree()
            99
            sage: f = ntl.ZZ_pX([], c)
            sage: f.degree()
            -1
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.degree()
            0"""
    @overload
    def derivative(self) -> Any:
        """ntl_ZZ_pX.derivative(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 949)

        Return the derivative of this polynomial.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,7,0,13],c)
            sage: f.derivative()
            [7 0 19]"""
    @overload
    def derivative(self) -> Any:
        """ntl_ZZ_pX.derivative(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 949)

        Return the derivative of this polynomial.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,7,0,13],c)
            sage: f.derivative()
            [7 0 19]"""
    def discriminant(self) -> Any:
        """ntl_ZZ_pX.discriminant(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1363)

        Return the discriminant of a=self, which is by definition
        $$
                (-1)^{m(m-1)/2} {\\mbox{\\tt resultant}}(a, a')/lc(a),
        $$
        where m = deg(a), and lc(a) is the leading coefficient of a.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(ntl.ZZ(17))
            sage: f = ntl.ZZ_pX([1,2,0,3],c)
            sage: f.discriminant()
            1"""
    @overload
    def factor(self, verbose=...) -> Any:
        """ntl_ZZ_pX.factor(self, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 966)

        Return the factorization of ``self``. Assumes ``self`` is
        monic.

        NOTE: The roots are returned in a random order.

        EXAMPLES:

        These computations use pseudo-random numbers, so we set the
        seed for reproducible testing. ::

            sage: set_random_seed(12)
            sage: ntl.ZZ_pX([-1,0,0,0,0,1],5).factor()
            [([4 1], 5)]
            sage: ls = ntl.ZZ_pX([-1,0,0,0,1],5).factor()
            sage: ls
            [([4 1], 1), ([2 1], 1), ([1 1], 1), ([3 1], 1)]
            sage: prod( [ x[0] for x in ls ] )
            [4 0 0 0 1]
            sage: ntl.ZZ_pX([3,7,0,1], 31).factor()
            [([3 7 0 1], 1)]
            sage: ntl.ZZ_pX([3,7,1,8], 28).factor()
            Traceback (most recent call last):
            ...
            ValueError: self must be monic."""
    @overload
    def factor(self) -> Any:
        """ntl_ZZ_pX.factor(self, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 966)

        Return the factorization of ``self``. Assumes ``self`` is
        monic.

        NOTE: The roots are returned in a random order.

        EXAMPLES:

        These computations use pseudo-random numbers, so we set the
        seed for reproducible testing. ::

            sage: set_random_seed(12)
            sage: ntl.ZZ_pX([-1,0,0,0,0,1],5).factor()
            [([4 1], 5)]
            sage: ls = ntl.ZZ_pX([-1,0,0,0,1],5).factor()
            sage: ls
            [([4 1], 1), ([2 1], 1), ([1 1], 1), ([3 1], 1)]
            sage: prod( [ x[0] for x in ls ] )
            [4 0 0 0 1]
            sage: ntl.ZZ_pX([3,7,0,1], 31).factor()
            [([3 7 0 1], 1)]
            sage: ntl.ZZ_pX([3,7,1,8], 28).factor()
            Traceback (most recent call last):
            ...
            ValueError: self must be monic."""
    @overload
    def factor(self) -> Any:
        """ntl_ZZ_pX.factor(self, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 966)

        Return the factorization of ``self``. Assumes ``self`` is
        monic.

        NOTE: The roots are returned in a random order.

        EXAMPLES:

        These computations use pseudo-random numbers, so we set the
        seed for reproducible testing. ::

            sage: set_random_seed(12)
            sage: ntl.ZZ_pX([-1,0,0,0,0,1],5).factor()
            [([4 1], 5)]
            sage: ls = ntl.ZZ_pX([-1,0,0,0,1],5).factor()
            sage: ls
            [([4 1], 1), ([2 1], 1), ([1 1], 1), ([3 1], 1)]
            sage: prod( [ x[0] for x in ls ] )
            [4 0 0 0 1]
            sage: ntl.ZZ_pX([3,7,0,1], 31).factor()
            [([3 7 0 1], 1)]
            sage: ntl.ZZ_pX([3,7,1,8], 28).factor()
            Traceback (most recent call last):
            ...
            ValueError: self must be monic."""
    @overload
    def factor(self) -> Any:
        """ntl_ZZ_pX.factor(self, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 966)

        Return the factorization of ``self``. Assumes ``self`` is
        monic.

        NOTE: The roots are returned in a random order.

        EXAMPLES:

        These computations use pseudo-random numbers, so we set the
        seed for reproducible testing. ::

            sage: set_random_seed(12)
            sage: ntl.ZZ_pX([-1,0,0,0,0,1],5).factor()
            [([4 1], 5)]
            sage: ls = ntl.ZZ_pX([-1,0,0,0,1],5).factor()
            sage: ls
            [([4 1], 1), ([2 1], 1), ([1 1], 1), ([3 1], 1)]
            sage: prod( [ x[0] for x in ls ] )
            [4 0 0 0 1]
            sage: ntl.ZZ_pX([3,7,0,1], 31).factor()
            [([3 7 0 1], 1)]
            sage: ntl.ZZ_pX([3,7,1,8], 28).factor()
            Traceback (most recent call last):
            ...
            ValueError: self must be monic."""
    @overload
    def factor(self) -> Any:
        """ntl_ZZ_pX.factor(self, verbose=False)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 966)

        Return the factorization of ``self``. Assumes ``self`` is
        monic.

        NOTE: The roots are returned in a random order.

        EXAMPLES:

        These computations use pseudo-random numbers, so we set the
        seed for reproducible testing. ::

            sage: set_random_seed(12)
            sage: ntl.ZZ_pX([-1,0,0,0,0,1],5).factor()
            [([4 1], 5)]
            sage: ls = ntl.ZZ_pX([-1,0,0,0,1],5).factor()
            sage: ls
            [([4 1], 1), ([2 1], 1), ([1 1], 1), ([3 1], 1)]
            sage: prod( [ x[0] for x in ls ] )
            [4 0 0 0 1]
            sage: ntl.ZZ_pX([3,7,0,1], 31).factor()
            [([3 7 0 1], 1)]
            sage: ntl.ZZ_pX([3,7,1,8], 28).factor()
            Traceback (most recent call last):
            ...
            ValueError: self must be monic."""
    @overload
    def gcd(self, ntl_ZZ_pXother) -> Any:
        """ntl_ZZ_pX.gcd(self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 753)

        Return the gcd d = gcd(a, b), where by convention the leading coefficient
        of d is >= 0.  We uses a multi-modular algorithm.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3],c) * ntl.ZZ_pX([4,5],c)**2
            sage: g = ntl.ZZ_pX([1,1,1],c)**3 * ntl.ZZ_pX([1,2,3],c)
            sage: f.gcd(g)
            [6 12 1]
            sage: g.gcd(f)
            [6 12 1]"""
    @overload
    def gcd(self, a, b) -> Any:
        """ntl_ZZ_pX.gcd(self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 753)

        Return the gcd d = gcd(a, b), where by convention the leading coefficient
        of d is >= 0.  We uses a multi-modular algorithm.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3],c) * ntl.ZZ_pX([4,5],c)**2
            sage: g = ntl.ZZ_pX([1,1,1],c)**3 * ntl.ZZ_pX([1,2,3],c)
            sage: f.gcd(g)
            [6 12 1]
            sage: g.gcd(f)
            [6 12 1]"""
    @overload
    def gcd(self, g) -> Any:
        """ntl_ZZ_pX.gcd(self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 753)

        Return the gcd d = gcd(a, b), where by convention the leading coefficient
        of d is >= 0.  We uses a multi-modular algorithm.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3],c) * ntl.ZZ_pX([4,5],c)**2
            sage: g = ntl.ZZ_pX([1,1,1],c)**3 * ntl.ZZ_pX([1,2,3],c)
            sage: f.gcd(g)
            [6 12 1]
            sage: g.gcd(f)
            [6 12 1]"""
    @overload
    def gcd(self, f) -> Any:
        """ntl_ZZ_pX.gcd(self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 753)

        Return the gcd d = gcd(a, b), where by convention the leading coefficient
        of d is >= 0.  We uses a multi-modular algorithm.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3],c) * ntl.ZZ_pX([4,5],c)**2
            sage: g = ntl.ZZ_pX([1,1,1],c)**3 * ntl.ZZ_pX([1,2,3],c)
            sage: f.gcd(g)
            [6 12 1]
            sage: g.gcd(f)
            [6 12 1]"""
    @overload
    def get_modulus_context(self) -> Any:
        """ntl_ZZ_pX.get_modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 194)

        Return the modulus for ``self``.

        EXAMPLES::

            sage: x = ntl.ZZ_pX([0,5,3],17)
            sage: c = x.get_modulus_context()
            sage: y = ntl.ZZ_pX([5],c)
            sage: x+y
            [5 5 3]"""
    @overload
    def get_modulus_context(self) -> Any:
        """ntl_ZZ_pX.get_modulus_context(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 194)

        Return the modulus for ``self``.

        EXAMPLES::

            sage: x = ntl.ZZ_pX([0,5,3],17)
            sage: c = x.get_modulus_context()
            sage: y = ntl.ZZ_pX([5],c)
            sage: x+y
            [5 5 3]"""
    def invert_and_truncate(self, longm) -> Any:
        """ntl_ZZ_pX.invert_and_truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1161)

        Compute and return the inverse of ``self`` modulo `x^m`.

        The constant term of ``self`` must be a unit.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,3,4,5,6,7],c)
            sage: f.invert_and_truncate(20)
            [1 18 1 0 0 0 0 8 17 2 13 0 0 0 4 0 17 10 9]
            sage: g = f.invert_and_truncate(20)
            sage: g * f
            [1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 8 4 4 3]"""
    def invmod(self, ntl_ZZ_pXmodulus) -> Any:
        """ntl_ZZ_pX.invmod(self, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1185)

        Return the inverse of ``self`` modulo the modulus using NTL's InvMod."""
    def invmod_newton(self, ntl_ZZ_pXmodulus) -> Any:
        """ntl_ZZ_pX.invmod_newton(self, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1195)

        Return the inverse of ``self`` modulo the modulus using Newton lifting.
        Only works if modulo a power of a prime, and if modulus is either
        unramified or Eisenstein."""
    @overload
    def is_monic(self) -> Any:
        """ntl_ZZ_pX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 634)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([2,0,0,1],c)
            sage: f.is_monic()
            True
            sage: g = f.reverse()
            sage: g.is_monic()
            False
            sage: g
            [1 0 0 2]
            sage: f = ntl.ZZ_pX([1,2,0,3,0,2],c)
            sage: f.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """ntl_ZZ_pX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 634)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([2,0,0,1],c)
            sage: f.is_monic()
            True
            sage: g = f.reverse()
            sage: g.is_monic()
            False
            sage: g
            [1 0 0 2]
            sage: f = ntl.ZZ_pX([1,2,0,3,0,2],c)
            sage: f.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """ntl_ZZ_pX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 634)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([2,0,0,1],c)
            sage: f.is_monic()
            True
            sage: g = f.reverse()
            sage: g.is_monic()
            False
            sage: g
            [1 0 0 2]
            sage: f = ntl.ZZ_pX([1,2,0,3,0,2],c)
            sage: f.is_monic()
            False"""
    @overload
    def is_monic(self) -> Any:
        """ntl_ZZ_pX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 634)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([2,0,0,1],c)
            sage: f.is_monic()
            True
            sage: g = f.reverse()
            sage: g.is_monic()
            False
            sage: g
            [1 0 0 2]
            sage: f = ntl.ZZ_pX([1,2,0,3,0,2],c)
            sage: f.is_monic()
            False"""
    @overload
    def is_one(self) -> Any:
        """ntl_ZZ_pX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 617)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,1],c)
            sage: f.is_one()
            False
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """ntl_ZZ_pX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 617)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,1],c)
            sage: f.is_one()
            False
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """ntl_ZZ_pX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 617)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,1],c)
            sage: f.is_one()
            False
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.is_one()
            True"""
    @overload
    def is_x(self) -> Any:
        '''ntl_ZZ_pX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 898)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([],c)
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.ZZ_pX([0,1],c)
            sage: f.is_x()
            True
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.is_x()
            False'''
    @overload
    def is_x(self) -> Any:
        '''ntl_ZZ_pX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 898)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([],c)
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.ZZ_pX([0,1],c)
            sage: f.is_x()
            True
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.is_x()
            False'''
    @overload
    def is_x(self) -> Any:
        '''ntl_ZZ_pX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 898)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([],c)
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.ZZ_pX([0,1],c)
            sage: f.is_x()
            True
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.is_x()
            False'''
    @overload
    def is_x(self) -> Any:
        '''ntl_ZZ_pX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 898)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([],c)
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.ZZ_pX([0,1],c)
            sage: f.is_x()
            True
            sage: f = ntl.ZZ_pX([1],c)
            sage: f.is_x()
            False'''
    @overload
    def is_zero(self) -> Any:
        """ntl_ZZ_pX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 598)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([0,0,0,20],c)
            sage: f.is_zero()
            True
            sage: f = ntl.ZZ_pX([0,0,1],c)
            sage: f
            [0 0 1]
            sage: f.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """ntl_ZZ_pX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 598)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([0,0,0,20],c)
            sage: f.is_zero()
            True
            sage: f = ntl.ZZ_pX([0,0,1],c)
            sage: f
            [0 0 1]
            sage: f.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """ntl_ZZ_pX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 598)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([0,0,0,20],c)
            sage: f.is_zero()
            True
            sage: f = ntl.ZZ_pX([0,0,1],c)
            sage: f
            [0 0 1]
            sage: f.is_zero()
            False"""
    @overload
    def leading_coefficient(self) -> Any:
        """ntl_ZZ_pX.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 835)

        Return the leading coefficient of this polynomial.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([3,6,9],c)
            sage: f.leading_coefficient()
            9
            sage: f = ntl.ZZ_pX([],c)
            sage: f.leading_coefficient()
            0"""
    @overload
    def leading_coefficient(self) -> Any:
        """ntl_ZZ_pX.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 835)

        Return the leading coefficient of this polynomial.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([3,6,9],c)
            sage: f.leading_coefficient()
            9
            sage: f = ntl.ZZ_pX([],c)
            sage: f.leading_coefficient()
            0"""
    @overload
    def leading_coefficient(self) -> Any:
        """ntl_ZZ_pX.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 835)

        Return the leading coefficient of this polynomial.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([3,6,9],c)
            sage: f.leading_coefficient()
            9
            sage: f = ntl.ZZ_pX([],c)
            sage: f.leading_coefficient()
            0"""
    def left_shift(self, longn) -> Any:
        """ntl_ZZ_pX.left_shift(self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 674)

        Return the polynomial obtained by shifting all coefficients of
        this polynomial to the left n positions.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([2,0,0,1],c)
            sage: f
            [2 0 0 1]
            sage: f.left_shift(2)
            [0 0 2 0 0 1]
            sage: f.left_shift(5)
            [0 0 0 0 0 2 0 0 1]

        A negative left shift is a right shift.
            sage: f.left_shift(-2)
            [0 1]"""
    @overload
    def linear_roots(self) -> Any:
        """ntl_ZZ_pX.linear_roots(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1017)

        Assumes that input is monic, and has deg(f) roots.
        Returns the list of roots.

        NOTE: This function will go into an infinite loop if you
        give it a polynomial without deg(f) linear factors. Note
        also that the result is not deterministic, i.e. the
        order of the roots returned is random.

        EXAMPLES::

            sage: ntl.ZZ_pX([-1,0,0,0,0,1],5).linear_roots()
            [1, 1, 1, 1, 1]
            sage: roots = ntl.ZZ_pX([-1,0,0,0,1],5).linear_roots()
            sage: [ ntl.ZZ_p(i,5) in roots for i in [1..4] ]
            [True, True, True, True]
            sage: ntl.ZZ_pX([3,7,1,8], 28).linear_roots()
            Traceback (most recent call last):
            ...
            ValueError: self must be monic."""
    @overload
    def linear_roots(self) -> Any:
        """ntl_ZZ_pX.linear_roots(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1017)

        Assumes that input is monic, and has deg(f) roots.
        Returns the list of roots.

        NOTE: This function will go into an infinite loop if you
        give it a polynomial without deg(f) linear factors. Note
        also that the result is not deterministic, i.e. the
        order of the roots returned is random.

        EXAMPLES::

            sage: ntl.ZZ_pX([-1,0,0,0,0,1],5).linear_roots()
            [1, 1, 1, 1, 1]
            sage: roots = ntl.ZZ_pX([-1,0,0,0,1],5).linear_roots()
            sage: [ ntl.ZZ_p(i,5) in roots for i in [1..4] ]
            [True, True, True, True]
            sage: ntl.ZZ_pX([3,7,1,8], 28).linear_roots()
            Traceback (most recent call last):
            ...
            ValueError: self must be monic."""
    @overload
    def linear_roots(self) -> Any:
        """ntl_ZZ_pX.linear_roots(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1017)

        Assumes that input is monic, and has deg(f) roots.
        Returns the list of roots.

        NOTE: This function will go into an infinite loop if you
        give it a polynomial without deg(f) linear factors. Note
        also that the result is not deterministic, i.e. the
        order of the roots returned is random.

        EXAMPLES::

            sage: ntl.ZZ_pX([-1,0,0,0,0,1],5).linear_roots()
            [1, 1, 1, 1, 1]
            sage: roots = ntl.ZZ_pX([-1,0,0,0,1],5).linear_roots()
            sage: [ ntl.ZZ_p(i,5) in roots for i in [1..4] ]
            [True, True, True, True]
            sage: ntl.ZZ_pX([3,7,1,8], 28).linear_roots()
            Traceback (most recent call last):
            ...
            ValueError: self must be monic."""
    @overload
    def linear_roots(self) -> Any:
        """ntl_ZZ_pX.linear_roots(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1017)

        Assumes that input is monic, and has deg(f) roots.
        Returns the list of roots.

        NOTE: This function will go into an infinite loop if you
        give it a polynomial without deg(f) linear factors. Note
        also that the result is not deterministic, i.e. the
        order of the roots returned is random.

        EXAMPLES::

            sage: ntl.ZZ_pX([-1,0,0,0,0,1],5).linear_roots()
            [1, 1, 1, 1, 1]
            sage: roots = ntl.ZZ_pX([-1,0,0,0,1],5).linear_roots()
            sage: [ ntl.ZZ_p(i,5) in roots for i in [1..4] ]
            [True, True, True, True]
            sage: ntl.ZZ_pX([3,7,1,8], 28).linear_roots()
            Traceback (most recent call last):
            ...
            ValueError: self must be monic."""
    @overload
    def list(self) -> Any:
        """ntl_ZZ_pX.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 306)

        Return list of entries as a list of ntl_ZZ_p.

        EXAMPLES::

            sage: x = ntl.ZZ_pX([1,3,5],11)
            sage: x.list()
            [1, 3, 5]
            sage: type(x.list()[0])
            <class 'sage.libs.ntl.ntl_ZZ_p.ntl_ZZ_p'>"""
    @overload
    def list(self) -> Any:
        """ntl_ZZ_pX.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 306)

        Return list of entries as a list of ntl_ZZ_p.

        EXAMPLES::

            sage: x = ntl.ZZ_pX([1,3,5],11)
            sage: x.list()
            [1, 3, 5]
            sage: type(x.list()[0])
            <class 'sage.libs.ntl.ntl_ZZ_p.ntl_ZZ_p'>"""
    @overload
    def list(self) -> Any:
        """ntl_ZZ_pX.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 306)

        Return list of entries as a list of ntl_ZZ_p.

        EXAMPLES::

            sage: x = ntl.ZZ_pX([1,3,5],11)
            sage: x.list()
            [1, 3, 5]
            sage: type(x.list()[0])
            <class 'sage.libs.ntl.ntl_ZZ_p.ntl_ZZ_p'>"""
    @overload
    def minpoly_mod(self, ntl_ZZ_pXmodulus) -> Any:
        """ntl_ZZ_pX.minpoly_mod(self, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1407)

        Return the minimal polynomial of this polynomial modulo the
        modulus.  The modulus must be monic of degree bigger than
        ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([0,0,1],c)
            sage: g = f*f
            sage: f.charpoly_mod(g)
            [0 0 0 0 1]

        However, since `f^2 = 0` modulo `g`, its minimal polynomial
        is of degree `2`::

            sage: f.minpoly_mod(g)
            [0 0 1]"""
    @overload
    def minpoly_mod(self, g) -> Any:
        """ntl_ZZ_pX.minpoly_mod(self, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1407)

        Return the minimal polynomial of this polynomial modulo the
        modulus.  The modulus must be monic of degree bigger than
        ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([0,0,1],c)
            sage: g = f*f
            sage: f.charpoly_mod(g)
            [0 0 0 0 1]

        However, since `f^2 = 0` modulo `g`, its minimal polynomial
        is of degree `2`::

            sage: f.minpoly_mod(g)
            [0 0 1]"""
    def multiply_and_truncate(self, ntl_ZZ_pXother, longm) -> Any:
        """ntl_ZZ_pX.multiply_and_truncate(self, ntl_ZZ_pX other, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1118)

        Return self*other but with terms of degree >= m removed.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,3,4,5],c)
            sage: g = ntl.ZZ_pX([10],c)
            sage: f.multiply_and_truncate(g, 2)
            [10]
            sage: g.multiply_and_truncate(f, 2)
            [10]"""
    @overload
    def multiply_mod(self, ntl_ZZ_pXother, ntl_ZZ_pXmodulus) -> Any:
        """ntl_ZZ_pX.multiply_mod(self, ntl_ZZ_pX other, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1240)

        Return ``self*other % modulus``.  The modulus must be monic with
        ``deg(modulus) > 0``, and ``self`` and ``other`` must have smaller degree.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(ntl.ZZ(20))
            sage: modulus = ntl.ZZ_pX([1,2,0,1],c)    # must be monic
            sage: g = ntl.ZZ_pX([-1,0,1],c)
            sage: h = ntl.ZZ_pX([3,7,13],c)
            sage: h.multiply_mod(g, modulus)
            [10 6 4]"""
    @overload
    def multiply_mod(self, g, modulus) -> Any:
        """ntl_ZZ_pX.multiply_mod(self, ntl_ZZ_pX other, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1240)

        Return ``self*other % modulus``.  The modulus must be monic with
        ``deg(modulus) > 0``, and ``self`` and ``other`` must have smaller degree.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(ntl.ZZ(20))
            sage: modulus = ntl.ZZ_pX([1,2,0,1],c)    # must be monic
            sage: g = ntl.ZZ_pX([-1,0,1],c)
            sage: h = ntl.ZZ_pX([3,7,13],c)
            sage: h.multiply_mod(g, modulus)
            [10 6 4]"""
    @overload
    def norm_mod(self, ntl_ZZ_pXmodulus) -> Any:
        """ntl_ZZ_pX.norm_mod(self, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1336)

        Return the norm of this polynomial modulo the modulus.  The
        modulus must be monic, and of positive degree strictly greater
        than the degree of ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,0,3],c)
            sage: mod = ntl.ZZ_pX([-5,2,0,0,1],c)
            sage: f.norm_mod(mod)
            11

        The norm is the constant term of the characteristic polynomial::

            sage: f.charpoly_mod(mod)
            [11 1 8 14 1]"""
    @overload
    def norm_mod(self, mod) -> Any:
        """ntl_ZZ_pX.norm_mod(self, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1336)

        Return the norm of this polynomial modulo the modulus.  The
        modulus must be monic, and of positive degree strictly greater
        than the degree of ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,0,3],c)
            sage: mod = ntl.ZZ_pX([-5,2,0,0,1],c)
            sage: f.norm_mod(mod)
            11

        The norm is the constant term of the characteristic polynomial::

            sage: f.charpoly_mod(mod)
            [11 1 8 14 1]"""
    def preallocate_space(self, longn) -> Any:
        """ntl_ZZ_pX.preallocate_space(self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1450)

        Pre-allocate spaces for n coefficients.  The polynomial that f
        represents is unchanged.  This is useful if you know you'll be
        setting coefficients up to n, so memory isn't re-allocated as
        the polynomial grows.  (You might save a millisecond with this
        function.)

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3],c)
            sage: f.preallocate_space(20)
            sage: f
            [1 2 3]
            sage: f[10]=5  # no new memory is allocated
            sage: f
            [1 2 3 0 0 0 0 0 0 0 5]"""
    @overload
    def quo_rem(self, ntl_ZZ_pXother) -> Any:
        """ntl_ZZ_pX.quo_rem(self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 450)

        Return the unique integral `q` and `r` such that ``self = q*other +
        r``, if they exist.  Otherwise raises an Exception.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX(range(10), c); g = ntl.ZZ_pX([-1,0,1], c)
            sage: q, r = f.quo_rem(g)
            sage: q, r
            ([3 7 1 4 14 16 8 9], [3 8])
            sage: q*g + r == f
            True"""
    @overload
    def quo_rem(self, g) -> Any:
        """ntl_ZZ_pX.quo_rem(self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 450)

        Return the unique integral `q` and `r` such that ``self = q*other +
        r``, if they exist.  Otherwise raises an Exception.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX(range(10), c); g = ntl.ZZ_pX([-1,0,1], c)
            sage: q, r = f.quo_rem(g)
            sage: q, r
            ([3 7 1 4 14 16 8 9], [3 8])
            sage: q*g + r == f
            True"""
    @overload
    def resultant(self, ntl_ZZ_pXother) -> Any:
        """ntl_ZZ_pX.resultant(self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1316)

        Return the resultant of ``self`` and ``other``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([17,0,1,1],c)
            sage: g = ntl.ZZ_pX([34,-17,18,2],c)
            sage: f.resultant(g)
            0"""
    @overload
    def resultant(self, g) -> Any:
        """ntl_ZZ_pX.resultant(self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1316)

        Return the resultant of ``self`` and ``other``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([17,0,1,1],c)
            sage: g = ntl.ZZ_pX([34,-17,18,2],c)
            sage: f.resultant(g)
            0"""
    @overload
    def reverse(self, hi=...) -> Any:
        """ntl_ZZ_pX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1062)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,3,4,5],c)
            sage: f.reverse()
            [5 4 3 2 1]
            sage: f.reverse(hi=10)
            [0 0 0 0 0 0 5 4 3 2 1]
            sage: f.reverse(hi=2)
            [3 2 1]
            sage: f.reverse(hi=-2)
            []"""
    @overload
    def reverse(self) -> Any:
        """ntl_ZZ_pX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1062)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,3,4,5],c)
            sage: f.reverse()
            [5 4 3 2 1]
            sage: f.reverse(hi=10)
            [0 0 0 0 0 0 5 4 3 2 1]
            sage: f.reverse(hi=2)
            [3 2 1]
            sage: f.reverse(hi=-2)
            []"""
    @overload
    def reverse(self, hi=...) -> Any:
        """ntl_ZZ_pX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1062)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,3,4,5],c)
            sage: f.reverse()
            [5 4 3 2 1]
            sage: f.reverse(hi=10)
            [0 0 0 0 0 0 5 4 3 2 1]
            sage: f.reverse(hi=2)
            [3 2 1]
            sage: f.reverse(hi=-2)
            []"""
    @overload
    def reverse(self, hi=...) -> Any:
        """ntl_ZZ_pX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1062)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,3,4,5],c)
            sage: f.reverse()
            [5 4 3 2 1]
            sage: f.reverse(hi=10)
            [0 0 0 0 0 0 5 4 3 2 1]
            sage: f.reverse(hi=2)
            [3 2 1]
            sage: f.reverse(hi=-2)
            []"""
    @overload
    def reverse(self, hi=...) -> Any:
        """ntl_ZZ_pX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1062)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,3,4,5],c)
            sage: f.reverse()
            [5 4 3 2 1]
            sage: f.reverse(hi=10)
            [0 0 0 0 0 0 5 4 3 2 1]
            sage: f.reverse(hi=2)
            [3 2 1]
            sage: f.reverse(hi=-2)
            []"""
    def right_shift(self, longn) -> Any:
        """ntl_ZZ_pX.right_shift(self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 701)

        Return the polynomial obtained by shifting all coefficients of
        this polynomial to the right n positions.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([2,0,0,1],c)
            sage: f
            [2 0 0 1]
            sage: f.right_shift(2)
            [0 1]
            sage: f.right_shift(5)
            []
            sage: f.right_shift(-2)
            [0 0 2 0 0 1]"""
    @overload
    def set_x(self) -> Any:
        '''ntl_ZZ_pX.set_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 873)

        Set this polynomial to the monomial "x".

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([],c)
            sage: f.set_x()
            sage: f
            [0 1]
            sage: g = ntl.ZZ_pX([0,1],c)
            sage: f == g
            True

        Though f and g are equal, they are not the same objects in memory::

            sage: f is g
            False'''
    @overload
    def set_x(self) -> Any:
        '''ntl_ZZ_pX.set_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 873)

        Set this polynomial to the monomial "x".

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([],c)
            sage: f.set_x()
            sage: f
            [0 1]
            sage: g = ntl.ZZ_pX([0,1],c)
            sage: f == g
            True

        Though f and g are equal, they are not the same objects in memory::

            sage: f is g
            False'''
    def square(self) -> Any:
        """ntl_ZZ_pX.square(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 475)

        Return f*f.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([-1,0,1], c)
            sage: f*f
            [1 0 15 0 1]"""
    def square_and_truncate(self, longm) -> Any:
        """ntl_ZZ_pX.square_and_truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1140)

        Return self*self but with terms of degree >= m removed.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,3,4,5],c)
            sage: f.square_and_truncate(4)
            [1 4 10]
            sage: (f*f).truncate(4)
            [1 4 10]"""
    @overload
    def trace_list(self) -> Any:
        """ntl_ZZ_pX.trace_list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1282)

        Return the list of traces of the powers `x^i` of the
        monomial x modulo this polynomial for i = 0, ..., deg(f)-1.

        This polynomial must be monic.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,0,3,0,1],c)
            sage: f.trace_list()
            [5, 0, 14, 0, 10]

        The input polynomial must be monic or a :exc:`ValueError` is raised::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,0,3,0,2],c)
            sage: f.trace_list()
            Traceback (most recent call last):
            ...
            ValueError: polynomial must be monic."""
    @overload
    def trace_list(self) -> Any:
        """ntl_ZZ_pX.trace_list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1282)

        Return the list of traces of the powers `x^i` of the
        monomial x modulo this polynomial for i = 0, ..., deg(f)-1.

        This polynomial must be monic.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,0,3,0,1],c)
            sage: f.trace_list()
            [5, 0, 14, 0, 10]

        The input polynomial must be monic or a :exc:`ValueError` is raised::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,0,3,0,2],c)
            sage: f.trace_list()
            Traceback (most recent call last):
            ...
            ValueError: polynomial must be monic."""
    @overload
    def trace_list(self) -> Any:
        """ntl_ZZ_pX.trace_list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1282)

        Return the list of traces of the powers `x^i` of the
        monomial x modulo this polynomial for i = 0, ..., deg(f)-1.

        This polynomial must be monic.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,0,3,0,1],c)
            sage: f.trace_list()
            [5, 0, 14, 0, 10]

        The input polynomial must be monic or a :exc:`ValueError` is raised::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,0,3,0,2],c)
            sage: f.trace_list()
            Traceback (most recent call last):
            ...
            ValueError: polynomial must be monic."""
    @overload
    def trace_mod(self, ntl_ZZ_pXmodulus) -> Any:
        """ntl_ZZ_pX.trace_mod(self, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1260)

        Return the trace of this polynomial modulus the modulus.
        The modulus must be monic, and of positive degree bigger
        than the degree of ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,0,3],c)
            sage: mod = ntl.ZZ_pX([5,3,-1,1,1],c)
            sage: f.trace_mod(mod)
            3"""
    @overload
    def trace_mod(self, mod) -> Any:
        """ntl_ZZ_pX.trace_mod(self, ntl_ZZ_pX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1260)

        Return the trace of this polynomial modulus the modulus.
        The modulus must be monic, and of positive degree bigger
        than the degree of ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,0,3],c)
            sage: mod = ntl.ZZ_pX([5,3,-1,1,1],c)
            sage: f.trace_mod(mod)
            3"""
    def truncate(self, longm) -> Any:
        """ntl_ZZ_pX.truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1088)

        Return the truncation of this polynomial obtained by
        removing all terms of degree >= m.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,2,3,4,5],c)
            sage: f.truncate(3)
            [1 2 3]
            sage: f.truncate(8)
            [1 2 3 4 5]
            sage: f.truncate(1)
            [1]
            sage: f.truncate(0)
            []
            sage: f.truncate(-1)
            []
            sage: f.truncate(-5)
            []"""
    @overload
    def xgcd(self, ntl_ZZ_pXother, plain=...) -> Any:
        """ntl_ZZ_pX.xgcd(self, ntl_ZZ_pX other, plain=True)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 775)

        Return `r`, `s`, `t` such that ``r = s*self + t*other``.

        Here r is the resultant of a and b; if r != 0, then this
        function computes s and t such that: a*s + b*t = r; otherwise
        s and t are both 0.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3],c) * ntl.ZZ_pX([4,5],c)**2
            sage: g = ntl.ZZ_pX([1,1,1],c)**3 * ntl.ZZ_pX([1,2,3],c)
            sage: f.xgcd(g)   # nothing since they are not coprime
            ([6 12 1], [15 13 6 8 7 9], [4 13])

        In this example the input quadratic polynomials have a common
        root modulo 13::

            sage: f = ntl.ZZ_pX([5,0,1],c)
            sage: g = ntl.ZZ_pX([18,0,1],c)
            sage: f.xgcd(g)
            ([1], [13], [4])
    """
    @overload
    def xgcd(self, g) -> Any:
        """ntl_ZZ_pX.xgcd(self, ntl_ZZ_pX other, plain=True)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 775)

        Return `r`, `s`, `t` such that ``r = s*self + t*other``.

        Here r is the resultant of a and b; if r != 0, then this
        function computes s and t such that: a*s + b*t = r; otherwise
        s and t are both 0.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3],c) * ntl.ZZ_pX([4,5],c)**2
            sage: g = ntl.ZZ_pX([1,1,1],c)**3 * ntl.ZZ_pX([1,2,3],c)
            sage: f.xgcd(g)   # nothing since they are not coprime
            ([6 12 1], [15 13 6 8 7 9], [4 13])

        In this example the input quadratic polynomials have a common
        root modulo 13::

            sage: f = ntl.ZZ_pX([5,0,1],c)
            sage: g = ntl.ZZ_pX([18,0,1],c)
            sage: f.xgcd(g)
            ([1], [13], [4])
    """
    @overload
    def xgcd(self, g) -> Any:
        """ntl_ZZ_pX.xgcd(self, ntl_ZZ_pX other, plain=True)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 775)

        Return `r`, `s`, `t` such that ``r = s*self + t*other``.

        Here r is the resultant of a and b; if r != 0, then this
        function computes s and t such that: a*s + b*t = r; otherwise
        s and t are both 0.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3],c) * ntl.ZZ_pX([4,5],c)**2
            sage: g = ntl.ZZ_pX([1,1,1],c)**3 * ntl.ZZ_pX([1,2,3],c)
            sage: f.xgcd(g)   # nothing since they are not coprime
            ([6 12 1], [15 13 6 8 7 9], [4 13])

        In this example the input quadratic polynomials have a common
        root modulo 13::

            sage: f = ntl.ZZ_pX([5,0,1],c)
            sage: g = ntl.ZZ_pX([18,0,1],c)
            sage: f.xgcd(g)
            ([1], [13], [4])
    """
    def __add__(self, ntl_ZZ_pXself, ntl_ZZ_pXother) -> Any:
        """ntl_ZZ_pX.__add__(ntl_ZZ_pX self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 323)

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: ntl.ZZ_pX(range(5),c) + ntl.ZZ_pX(range(6),c)
            [0 2 4 6 8 5]"""
    def __copy__(self) -> Any:
        """ntl_ZZ_pX.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 174)

        Return a copy of ``self``.

        EXAMPLES::

            sage: x = ntl.ZZ_pX([0,5,-3],11)
            sage: y = copy(x)
            sage: x == y
            True
            sage: x is y
            False
            sage: x[0] = 4; y
            [0 5 8]"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, longi) -> Any:
        """ntl_ZZ_pX.__getitem__(self, long i)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 249)

        Return the `i`-th entry of ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: x = ntl.ZZ_pX([2, 3, 4], c)
            sage: x[1]
            3"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mod__(self, ntl_ZZ_pXself, ntl_ZZ_pXother) -> Any:
        """ntl_ZZ_pX.__mod__(ntl_ZZ_pX self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 415)

        Given polynomials a, b in ZZ_p[X], if p is prime, then there exist polynomials q, r
        in ZZ_p[X] such that a = b*q + r, deg(r) < deg(b).  This
        function returns r.

        If p is not prime this function may raise a :exc:`RuntimeError`
        due to division by a noninvertible element of ZZ_p.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(ntl.ZZ(17))
            sage: f = ntl.ZZ_pX([2,4,6], c); g = ntl.ZZ_pX([2], c)
            sage: f % g   # 0
            []
            sage: f = ntl.ZZ_pX(range(10), c); g = ntl.ZZ_pX([-1,0,1], c)
            sage: f % g
            [3 8]

            sage: c = ntl.ZZ_pContext(ntl.ZZ(16))
            sage: f = ntl.ZZ_pX([2,4,6], c); g = ntl.ZZ_pX([2], c)
            sage: f % g
            Traceback (most recent call last):
            ...
            NTLError: ZZ_p: division by non-invertible element"""
    def __mul__(self, ntl_ZZ_pXself, ntl_ZZ_pXother) -> Any:
        """ntl_ZZ_pX.__mul__(ntl_ZZ_pX self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 357)

        EXAMPLES::

            sage: c1 = ntl.ZZ_pContext(20)
            sage: alpha = ntl.ZZ_pX(range(5), c1)
            sage: beta = ntl.ZZ_pX(range(6), c1)
            sage: alpha * beta
            [0 0 1 4 10 0 10 14 11]
            sage: c2 = ntl.ZZ_pContext(ntl.ZZ(5))  # we can mix up the moduli
            sage: x = ntl.ZZ_pX([2, 3, 4], c2)
            sage: x^2
            [4 2 0 4 1]
            sage: alpha * beta  # back to the first one and the ntl modulus gets reset correctly
            [0 0 1 4 10 0 10 14 11]"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_ZZ_pX.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 658)

        Return the negative of ``self``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([2,0,0,1],c)
            sage: -f
            [18 0 0 19]"""
    def __pow__(self, n, modulus) -> Any:
        """ntl_ZZ_pX.__pow__(self, n, modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 493)

        Return the ``n``-th nonnegative power of ``self``.

        If ``modulus`` is not ``None``, the exponentiation is performed
        modulo the polynomial ``modulus``.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: g = ntl.ZZ_pX([-1,0,1],c)
            sage: g**10
            [1 0 10 0 5 0 0 0 10 0 8 0 10 0 0 0 5 0 10 0 1]

            sage: x = ntl.ZZ_pX([0,1],c)
            sage: x**10
            [0 0 0 0 0 0 0 0 0 0 1]

        Modular exponentiation::

            sage: c = ntl.ZZ_pContext(20)
            sage: f = ntl.ZZ_pX([1,0,1],c)
            sage: m = ntl.ZZ_pX([1,0,0,0,0,1],c)
            sage: pow(f, 123**45, m)
            [1 19 3 0 3]

        Modular exponentiation of ``x``::

            sage: f = ntl.ZZ_pX([0,1],c)
            sage: f.is_x()
            True
            sage: m = ntl.ZZ_pX([1,1,0,0,0,1],c)
            sage: pow(f, 123**45, m)
            [15 5 5 11]"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_ZZ_pX.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 148)

        TESTS::

            sage: f = ntl.ZZ_pX([1,2,3,7], 5); f
            [1 2 3 2]
            sage: loads(dumps(f)) == f
            True"""
    def __rmod__(self, other):
        """Return value%self."""
    def __rmul__(self, other):
        """Return value*self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rsub__(self, other):
        """Return value-self."""
    def __rtruediv__(self, other):
        """Return value/self."""
    def __setitem__(self, longi, a) -> Any:
        """ntl_ZZ_pX.__setitem__(self, long i, a)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 208)

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(23)
            sage: x = ntl.ZZ_pX([2, 3, 4], c)
            sage: x[1] = 5
            sage: x
            [2 5 4]"""
    def __sub__(self, ntl_ZZ_pXself, ntl_ZZ_pXother) -> Any:
        """ntl_ZZ_pX.__sub__(ntl_ZZ_pX self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 340)

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(20)
            sage: ntl.ZZ_pX(range(5),c) - ntl.ZZ_pX(range(6),c)
            [0 0 0 0 0 15]"""
    def __truediv__(self, ntl_ZZ_pXself, ntl_ZZ_pXother) -> Any:
        """ntl_ZZ_pX.__truediv__(ntl_ZZ_pX self, ntl_ZZ_pX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 382)

        Compute quotient ``self / other``, if the quotient is a polynomial.
        Otherwise an Exception is raised.

        EXAMPLES::

            sage: c = ntl.ZZ_pContext(17)
            sage: f = ntl.ZZ_pX([1,2,3], c) * ntl.ZZ_pX([4,5], c)**2
            sage: g = ntl.ZZ_pX([4,5], c)
            sage: f/g
            [4 13 5 15]
            sage: ntl.ZZ_pX([1,2,3],c) * ntl.ZZ_pX([4,5],c)
            [4 13 5 15]

            sage: f = ntl.ZZ_pX(range(10), c); g = ntl.ZZ_pX([-1,0,1], c)
            sage: f/g
            Traceback (most recent call last):
            ...
            ArithmeticError: self (=[0 1 2 3 4 5 6 7 8 9]) is not divisible by other (=[16 0 1])"""

class ntl_ZZ_pX_Modulus:
    """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1515)

        Thin holder for ZZ_pX_Moduli.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def degree(self) -> Any:
        """ntl_ZZ_pX_Modulus.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZ_pX.pyx (starting at line 1526)"""
