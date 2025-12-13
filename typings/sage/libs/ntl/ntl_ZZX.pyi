from sage.categories.category import ZZ as ZZ
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.libs.ntl.ntl_ZZ import unpickle_class_value as unpickle_class_value
from sage.rings.integer_ring import IntegerRing as IntegerRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.proof.proof import get_flag as get_flag
from typing import Any, ClassVar, overload

one_ZZX: ntl_ZZX
zero_ZZX: ntl_ZZX

class ntl_ZZX:
    '''ntl_ZZX(v=None)

    File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 79)

    The class \\class{ZZX} implements polynomials in `\\Z[X]`, i.e.,
    univariate polynomials with integer coefficients.

    Polynomial multiplication is very fast, and is implemented using
    one of 4 different algorithms:
    \\begin{enumerate}
    \\item\\hspace{1em} Classical
    \\item\\hspace{1em} Karatsuba
    \\item\\hspace{1em} Schoenhage and Strassen --- performs an FFT by working
          modulo a "Fermat number" of appropriate size...
          good for polynomials with huge coefficients
          and moderate degree
    \\item\\hspace{1em} CRT/FFT --- performs an FFT by working modulo several
         small primes.  This is good for polynomials with moderate
         coefficients and huge degree.
    \\end{enumerate}

    The choice of algorithm is somewhat heuristic, and may not always be
    perfect.

    Many thanks to Juergen Gerhard {\\tt
    <jngerhar@plato.uni-paderborn.de>} for pointing out the deficiency
    in the NTL-1.0 ZZX arithmetic, and for contributing the
    Schoenhage/Strassen code.

    Extensive use is made of modular algorithms to enhance performance
    (e.g., the GCD algorithm and many others).'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, v=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 111)

                EXAMPLES::

                    sage: f = ntl.ZZX([1,2,5,-9])
                    sage: f
                    [1 2 5 -9]
                    sage: g = ntl.ZZX([0,0,0]); g
                    []
                    sage: g[10]=5
                    sage: g
                    [0 0 0 0 0 0 0 0 0 0 5]
                    sage: g[10]
                    5
        """
    @overload
    def charpoly_mod(self, ntl_ZZXmodulus, proof=...) -> Any:
        """ntl_ZZX.charpoly_mod(self, ntl_ZZX modulus, proof=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1095)

        Return the characteristic polynomial of this polynomial modulo
        the modulus.  The modulus must be monic of degree bigger than
        ``self``. If proof=False (the default is proof=None, see
        proof.polynomial or sage.structure.proof, but the global
        default is proof=True), then this function may use a
        randomized strategy that errors with probability no more than
        `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,0,3])
            sage: mod = ntl.ZZX([-5,2,0,0,1])
            sage: f.charpoly_mod(mod)
            [-8846 -594 -60 14 1]"""
    @overload
    def charpoly_mod(self, mod) -> Any:
        """ntl_ZZX.charpoly_mod(self, ntl_ZZX modulus, proof=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1095)

        Return the characteristic polynomial of this polynomial modulo
        the modulus.  The modulus must be monic of degree bigger than
        ``self``. If proof=False (the default is proof=None, see
        proof.polynomial or sage.structure.proof, but the global
        default is proof=True), then this function may use a
        randomized strategy that errors with probability no more than
        `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,0,3])
            sage: mod = ntl.ZZX([-5,2,0,0,1])
            sage: f.charpoly_mod(mod)
            [-8846 -594 -60 14 1]"""
    @overload
    def clear(self) -> Any:
        """ntl_ZZX.clear(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1139)

        Reset this polynomial to 0.  Changes this polynomial in place.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3])
            sage: f
            [1 2 3]
            sage: f.clear()
            sage: f
            []"""
    @overload
    def clear(self) -> Any:
        """ntl_ZZX.clear(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1139)

        Reset this polynomial to 0.  Changes this polynomial in place.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3])
            sage: f
            [1 2 3]
            sage: f.clear()
            sage: f
            []"""
    @overload
    def constant_term(self) -> Any:
        """ntl_ZZX.constant_term(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 780)

        Return the constant coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.ZZX([3,6,9])
            sage: f.constant_term()
            3
            sage: f = ntl.ZZX()
            sage: f.constant_term()
            0"""
    @overload
    def constant_term(self) -> Any:
        """ntl_ZZX.constant_term(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 780)

        Return the constant coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.ZZX([3,6,9])
            sage: f.constant_term()
            3
            sage: f = ntl.ZZX()
            sage: f.constant_term()
            0"""
    @overload
    def constant_term(self) -> Any:
        """ntl_ZZX.constant_term(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 780)

        Return the constant coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.ZZX([3,6,9])
            sage: f.constant_term()
            3
            sage: f = ntl.ZZX()
            sage: f.constant_term()
            0"""
    @overload
    def content(self) -> Any:
        """ntl_ZZX.content(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 590)

        Return the content of f, which has sign the same as the
        leading coefficient of f.  Also, our convention is that the
        content of 0 is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([2,0,0,2])
            sage: f.content()
            2
            sage: f = ntl.ZZX([2,0,0,-2])
            sage: f.content()
            -2
            sage: f = ntl.ZZX([6,12,3,9])
            sage: f.content()
            3
            sage: f = ntl.ZZX([])
            sage: f.content()
            0"""
    @overload
    def content(self) -> Any:
        """ntl_ZZX.content(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 590)

        Return the content of f, which has sign the same as the
        leading coefficient of f.  Also, our convention is that the
        content of 0 is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([2,0,0,2])
            sage: f.content()
            2
            sage: f = ntl.ZZX([2,0,0,-2])
            sage: f.content()
            -2
            sage: f = ntl.ZZX([6,12,3,9])
            sage: f.content()
            3
            sage: f = ntl.ZZX([])
            sage: f.content()
            0"""
    @overload
    def content(self) -> Any:
        """ntl_ZZX.content(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 590)

        Return the content of f, which has sign the same as the
        leading coefficient of f.  Also, our convention is that the
        content of 0 is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([2,0,0,2])
            sage: f.content()
            2
            sage: f = ntl.ZZX([2,0,0,-2])
            sage: f.content()
            -2
            sage: f = ntl.ZZX([6,12,3,9])
            sage: f.content()
            3
            sage: f = ntl.ZZX([])
            sage: f.content()
            0"""
    @overload
    def content(self) -> Any:
        """ntl_ZZX.content(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 590)

        Return the content of f, which has sign the same as the
        leading coefficient of f.  Also, our convention is that the
        content of 0 is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([2,0,0,2])
            sage: f.content()
            2
            sage: f = ntl.ZZX([2,0,0,-2])
            sage: f.content()
            -2
            sage: f = ntl.ZZX([6,12,3,9])
            sage: f.content()
            3
            sage: f = ntl.ZZX([])
            sage: f.content()
            0"""
    @overload
    def content(self) -> Any:
        """ntl_ZZX.content(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 590)

        Return the content of f, which has sign the same as the
        leading coefficient of f.  Also, our convention is that the
        content of 0 is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([2,0,0,2])
            sage: f.content()
            2
            sage: f = ntl.ZZX([2,0,0,-2])
            sage: f.content()
            -2
            sage: f = ntl.ZZX([6,12,3,9])
            sage: f.content()
            3
            sage: f = ntl.ZZX([])
            sage: f.content()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 741)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: f = ntl.ZZX([5,0,1])
            sage: f.degree()
            2
            sage: f = ntl.ZZX(list(range(100)))
            sage: f.degree()
            99
            sage: f = ntl.ZZX()
            sage: f.degree()
            -1
            sage: f = ntl.ZZX([1])
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 741)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: f = ntl.ZZX([5,0,1])
            sage: f.degree()
            2
            sage: f = ntl.ZZX(list(range(100)))
            sage: f.degree()
            99
            sage: f = ntl.ZZX()
            sage: f.degree()
            -1
            sage: f = ntl.ZZX([1])
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 741)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: f = ntl.ZZX([5,0,1])
            sage: f.degree()
            2
            sage: f = ntl.ZZX(list(range(100)))
            sage: f.degree()
            99
            sage: f = ntl.ZZX()
            sage: f.degree()
            -1
            sage: f = ntl.ZZX([1])
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 741)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: f = ntl.ZZX([5,0,1])
            sage: f.degree()
            2
            sage: f = ntl.ZZX(list(range(100)))
            sage: f.degree()
            99
            sage: f = ntl.ZZX()
            sage: f.degree()
            -1
            sage: f = ntl.ZZX([1])
            sage: f.degree()
            0"""
    @overload
    def degree(self) -> Any:
        """ntl_ZZX.degree(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 741)

        Return the degree of this polynomial.  The degree of the 0
        polynomial is -1.

        EXAMPLES::

            sage: f = ntl.ZZX([5,0,1])
            sage: f.degree()
            2
            sage: f = ntl.ZZX(list(range(100)))
            sage: f.degree()
            99
            sage: f = ntl.ZZX()
            sage: f.degree()
            -1
            sage: f = ntl.ZZX([1])
            sage: f.degree()
            0"""
    @overload
    def derivative(self) -> Any:
        """ntl_ZZX.derivative(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 837)

        Return the derivative of this polynomial.

        EXAMPLES::

            sage: f = ntl.ZZX([1,7,0,13])
            sage: f.derivative()
            [7 0 39]"""
    @overload
    def derivative(self) -> Any:
        """ntl_ZZX.derivative(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 837)

        Return the derivative of this polynomial.

        EXAMPLES::

            sage: f = ntl.ZZX([1,7,0,13])
            sage: f.derivative()
            [7 0 39]"""
    def discriminant(self, proof=...) -> Any:
        """ntl_ZZX.discriminant(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1066)

        Return the discriminant of self, which is by definition
        $$
                (-1)^{m(m-1)/2} {\\mbox{\\tt resultant}}(a, a')/lc(a),
        $$
        where m = deg(a), and lc(a) is the leading coefficient of a.
        If proof is False (the default is proof=None, see
        proof.polynomial or sage.structure.proof, but the global
        default is proof=True), then this function may use a
        randomized strategy that errors with probability no more than
        `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,0,3])
            sage: f.discriminant()
            -339
            sage: f.discriminant(proof=False)
            -339"""
    @overload
    def gcd(self, ntl_ZZXother) -> Any:
        """ntl_ZZX.gcd(self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 664)

        Return the gcd d = gcd(a, b), where by convention the leading coefficient
        of d is >= 0.  We use a multi-modular algorithm.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3]) * ntl.ZZX([4,5])**2
            sage: g = ntl.ZZX([1,1,1])**3 * ntl.ZZX([1,2,3])
            sage: f.gcd(g)
            [1 2 3]
            sage: g.gcd(f)
            [1 2 3]"""
    @overload
    def gcd(self, a, b) -> Any:
        """ntl_ZZX.gcd(self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 664)

        Return the gcd d = gcd(a, b), where by convention the leading coefficient
        of d is >= 0.  We use a multi-modular algorithm.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3]) * ntl.ZZX([4,5])**2
            sage: g = ntl.ZZX([1,1,1])**3 * ntl.ZZX([1,2,3])
            sage: f.gcd(g)
            [1 2 3]
            sage: g.gcd(f)
            [1 2 3]"""
    @overload
    def gcd(self, g) -> Any:
        """ntl_ZZX.gcd(self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 664)

        Return the gcd d = gcd(a, b), where by convention the leading coefficient
        of d is >= 0.  We use a multi-modular algorithm.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3]) * ntl.ZZX([4,5])**2
            sage: g = ntl.ZZX([1,1,1])**3 * ntl.ZZX([1,2,3])
            sage: f.gcd(g)
            [1 2 3]
            sage: g.gcd(f)
            [1 2 3]"""
    @overload
    def gcd(self, f) -> Any:
        """ntl_ZZX.gcd(self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 664)

        Return the gcd d = gcd(a, b), where by convention the leading coefficient
        of d is >= 0.  We use a multi-modular algorithm.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3]) * ntl.ZZX([4,5])**2
            sage: g = ntl.ZZX([1,1,1])**3 * ntl.ZZX([1,2,3])
            sage: f.gcd(g)
            [1 2 3]
            sage: g.gcd(f)
            [1 2 3]"""
    def getitem_as_int_doctest(self, i) -> Any:
        """ntl_ZZX.getitem_as_int_doctest(self, i)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 257)

        This method exists solely for automated testing of getitem_as_int().

        sage: x = ntl.ZZX([2, 3, 5, -7, 11])
        sage: i = x.getitem_as_int_doctest(3)
        sage: i
         -7
        sage: type(i)
         <... 'int'>
        sage: x.getitem_as_int_doctest(15)
         0"""
    def invert_and_truncate(self, longm) -> Any:
        """ntl_ZZX.invert_and_truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 934)

        Compute and return the inverse of ``self`` modulo `x^m`.
        The constant term of ``self`` must be 1 or -1.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3,4,5,6,7])
            sage: f.invert_and_truncate(20)
            [1 -2 1 0 0 0 0 8 -23 22 -7 0 0 0 64 -240 337 -210 49]
            sage: g = f.invert_and_truncate(20)
            sage: g * f
            [1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -512 1344 -1176 343]"""
    @overload
    def is_monic(self) -> Any:
        """ntl_ZZX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 515)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: f = ntl.ZZX([2,0,0,1])
            sage: f.is_monic()
            True
            sage: g = f.reverse()
            sage: g.is_monic()
            False
            sage: g
            [1 0 0 2]"""
    @overload
    def is_monic(self) -> Any:
        """ntl_ZZX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 515)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: f = ntl.ZZX([2,0,0,1])
            sage: f.is_monic()
            True
            sage: g = f.reverse()
            sage: g.is_monic()
            False
            sage: g
            [1 0 0 2]"""
    @overload
    def is_monic(self) -> Any:
        """ntl_ZZX.is_monic(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 515)

        Return ``True`` exactly if this polynomial is monic.

        EXAMPLES::

            sage: f = ntl.ZZX([2,0,0,1])
            sage: f.is_monic()
            True
            sage: g = f.reverse()
            sage: g.is_monic()
            False
            sage: g
            [1 0 0 2]"""
    @overload
    def is_one(self) -> Any:
        """ntl_ZZX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 500)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: f = ntl.ZZX([1,1])
            sage: f.is_one()
            False
            sage: f = ntl.ZZX([1])
            sage: f.is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """ntl_ZZX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 500)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: f = ntl.ZZX([1,1])
            sage: f.is_one()
            False
            sage: f = ntl.ZZX([1])
            sage: f.is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """ntl_ZZX.is_one(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 500)

        Return ``True`` exactly if this polynomial is 1.

        EXAMPLES::

            sage: f = ntl.ZZX([1,1])
            sage: f.is_one()
            False
            sage: f = ntl.ZZX([1])
            sage: f.is_one()
            True"""
    @overload
    def is_x(self) -> Any:
        '''ntl_ZZX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 818)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: f = ntl.ZZX()
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.ZZX([0,1])
            sage: f.is_x()
            True
            sage: f = ntl.ZZX([1])
            sage: f.is_x()
            False'''
    @overload
    def is_x(self) -> Any:
        '''ntl_ZZX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 818)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: f = ntl.ZZX()
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.ZZX([0,1])
            sage: f.is_x()
            True
            sage: f = ntl.ZZX([1])
            sage: f.is_x()
            False'''
    @overload
    def is_x(self) -> Any:
        '''ntl_ZZX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 818)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: f = ntl.ZZX()
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.ZZX([0,1])
            sage: f.is_x()
            True
            sage: f = ntl.ZZX([1])
            sage: f.is_x()
            False'''
    @overload
    def is_x(self) -> Any:
        '''ntl_ZZX.is_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 818)

        ``True`` if this is the polynomial "x".

        EXAMPLES::

            sage: f = ntl.ZZX()
            sage: f.set_x()
            sage: f.is_x()
            True
            sage: f = ntl.ZZX([0,1])
            sage: f.is_x()
            True
            sage: f = ntl.ZZX([1])
            sage: f.is_x()
            False'''
    @overload
    def is_zero(self) -> Any:
        """ntl_ZZX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 483)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([0,0,0,0])
            sage: f.is_zero()
            True
            sage: f = ntl.ZZX([0,0,1])
            sage: f
            [0 0 1]
            sage: f.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """ntl_ZZX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 483)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([0,0,0,0])
            sage: f.is_zero()
            True
            sage: f = ntl.ZZX([0,0,1])
            sage: f
            [0 0 1]
            sage: f.is_zero()
            False"""
    @overload
    def is_zero(self) -> Any:
        """ntl_ZZX.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 483)

        Return ``True`` exactly if this polynomial is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([0,0,0,0])
            sage: f.is_zero()
            True
            sage: f = ntl.ZZX([0,0,1])
            sage: f
            [0 0 1]
            sage: f.is_zero()
            False"""
    @overload
    def lcm(self, ntl_ZZXother) -> Any:
        """ntl_ZZX.lcm(self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 681)

        Return the least common multiple of ``self`` and ``other``.

        EXAMPLES::

            sage: x1 = ntl.ZZX([-1,0,0,1])
            sage: x2 = ntl.ZZX([-1,0,0,0,0,0,1])
            sage: x1.lcm(x2)
            [-1 0 0 0 0 0 1]"""
    @overload
    def lcm(self, x2) -> Any:
        """ntl_ZZX.lcm(self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 681)

        Return the least common multiple of ``self`` and ``other``.

        EXAMPLES::

            sage: x1 = ntl.ZZX([-1,0,0,1])
            sage: x2 = ntl.ZZX([-1,0,0,0,0,0,1])
            sage: x1.lcm(x2)
            [-1 0 0 0 0 0 1]"""
    @overload
    def leading_coefficient(self) -> Any:
        """ntl_ZZX.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 763)

        Return the leading coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.ZZX([3,6,9])
            sage: f.leading_coefficient()
            9
            sage: f = ntl.ZZX()
            sage: f.leading_coefficient()
            0"""
    @overload
    def leading_coefficient(self) -> Any:
        """ntl_ZZX.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 763)

        Return the leading coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.ZZX([3,6,9])
            sage: f.leading_coefficient()
            9
            sage: f = ntl.ZZX()
            sage: f.leading_coefficient()
            0"""
    @overload
    def leading_coefficient(self) -> Any:
        """ntl_ZZX.leading_coefficient(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 763)

        Return the leading coefficient of this polynomial.

        EXAMPLES::

            sage: f = ntl.ZZX([3,6,9])
            sage: f.leading_coefficient()
            9
            sage: f = ntl.ZZX()
            sage: f.leading_coefficient()
            0"""
    def left_shift(self, longn) -> Any:
        """ntl_ZZX.left_shift(self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 550)

        Return the polynomial obtained by shifting all coefficients of
        this polynomial to the left n positions.

        EXAMPLES::

            sage: f = ntl.ZZX([2,0,0,1])
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
    def list(self) -> Any:
        """ntl_ZZX.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 272)

        Retrieves coefficients as a list of ntl.ZZ Integers.

        EXAMPLES::

            sage: x = ntl.ZZX([129381729371289371237128318293718237, 2, -3, 0, 4])
            sage: L = x.list(); L
            [129381729371289371237128318293718237, 2, -3, 0, 4]
            sage: type(L[0])
            <class 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>
            sage: x = ntl.ZZX()
            sage: L = x.list(); L
            []"""
    @overload
    def list(self) -> Any:
        """ntl_ZZX.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 272)

        Retrieves coefficients as a list of ntl.ZZ Integers.

        EXAMPLES::

            sage: x = ntl.ZZX([129381729371289371237128318293718237, 2, -3, 0, 4])
            sage: L = x.list(); L
            [129381729371289371237128318293718237, 2, -3, 0, 4]
            sage: type(L[0])
            <class 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>
            sage: x = ntl.ZZX()
            sage: L = x.list(); L
            []"""
    @overload
    def list(self) -> Any:
        """ntl_ZZX.list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 272)

        Retrieves coefficients as a list of ntl.ZZ Integers.

        EXAMPLES::

            sage: x = ntl.ZZX([129381729371289371237128318293718237, 2, -3, 0, 4])
            sage: L = x.list(); L
            [129381729371289371237128318293718237, 2, -3, 0, 4]
            sage: type(L[0])
            <class 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>
            sage: x = ntl.ZZX()
            sage: L = x.list(); L
            []"""
    @overload
    def minpoly_mod_noproof(self, ntl_ZZXmodulus) -> Any:
        """ntl_ZZX.minpoly_mod_noproof(self, ntl_ZZX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1116)

        Return the minimal polynomial of this polynomial modulo the
        modulus.  The modulus must be monic of degree bigger than
        ``self``.  In all cases, this function may use a randomized
        strategy that errors with probability no more than `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([0,0,1])
            sage: g = f*f
            sage: f.charpoly_mod(g)
            [0 0 0 0 1]

        However, since `f^2 = 0` modulo `g`, its minimal polynomial
        is of degree `2`::

            sage: f.minpoly_mod_noproof(g)
            [0 0 1]"""
    @overload
    def minpoly_mod_noproof(self, g) -> Any:
        """ntl_ZZX.minpoly_mod_noproof(self, ntl_ZZX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1116)

        Return the minimal polynomial of this polynomial modulo the
        modulus.  The modulus must be monic of degree bigger than
        ``self``.  In all cases, this function may use a randomized
        strategy that errors with probability no more than `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([0,0,1])
            sage: g = f*f
            sage: f.charpoly_mod(g)
            [0 0 0 0 1]

        However, since `f^2 = 0` modulo `g`, its minimal polynomial
        is of degree `2`::

            sage: f.minpoly_mod_noproof(g)
            [0 0 1]"""
    def multiply_and_truncate(self, ntl_ZZXother, longm) -> Any:
        """ntl_ZZX.multiply_and_truncate(self, ntl_ZZX other, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 899)

        Return self*other but with terms of degree >= m removed.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3,4,5])
            sage: g = ntl.ZZX([10])
            sage: f.multiply_and_truncate(g, 2)
            [10 20]
            sage: g.multiply_and_truncate(f, 2)
            [10 20]"""
    @overload
    def multiply_mod(self, ntl_ZZXother, ntl_ZZXmodulus) -> Any:
        """ntl_ZZX.multiply_mod(self, ntl_ZZX other, ntl_ZZX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 956)

        Return ``self*other % modulus``.  The modulus must be monic with
        deg(modulus) > 0, and ``self`` and ``other`` must have smaller degree.

        EXAMPLES::

            sage: modulus = ntl.ZZX([1,2,0,1])    # must be monic
            sage: g = ntl.ZZX([-1,0,1])
            sage: h = ntl.ZZX([3,7,13])
            sage: h.multiply_mod(g, modulus)
            [-10 -34 -36]"""
    @overload
    def multiply_mod(self, g, modulus) -> Any:
        """ntl_ZZX.multiply_mod(self, ntl_ZZX other, ntl_ZZX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 956)

        Return ``self*other % modulus``.  The modulus must be monic with
        deg(modulus) > 0, and ``self`` and ``other`` must have smaller degree.

        EXAMPLES::

            sage: modulus = ntl.ZZX([1,2,0,1])    # must be monic
            sage: g = ntl.ZZX([-1,0,1])
            sage: h = ntl.ZZX([3,7,13])
            sage: h.multiply_mod(g, modulus)
            [-10 -34 -36]"""
    @overload
    def norm_mod(self, ntl_ZZXmodulus, proof=...) -> Any:
        """ntl_ZZX.norm_mod(self, ntl_ZZX modulus, proof=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1039)

        Return the norm of this polynomial modulo the modulus.

        The modulus must be monic, and of positive degree strictly
        greater than the degree of ``self``.  If proof=False (the default
        is proof=None, see proof.polynomial or sage.structure.proof,
        but the global default is proof=True) then it may use a
        randomized strategy that errors with probability no more than
        `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,0,3])
            sage: mod = ntl.ZZX([-5,2,0,0,1])
            sage: f.norm_mod(mod)
            -8846

        The norm is the constant term of the characteristic polynomial::

            sage: f.charpoly_mod(mod)
            [-8846 -594 -60 14 1]"""
    @overload
    def norm_mod(self, mod) -> Any:
        """ntl_ZZX.norm_mod(self, ntl_ZZX modulus, proof=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1039)

        Return the norm of this polynomial modulo the modulus.

        The modulus must be monic, and of positive degree strictly
        greater than the degree of ``self``.  If proof=False (the default
        is proof=None, see proof.polynomial or sage.structure.proof,
        but the global default is proof=True) then it may use a
        randomized strategy that errors with probability no more than
        `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,0,3])
            sage: mod = ntl.ZZX([-5,2,0,0,1])
            sage: f.norm_mod(mod)
            -8846

        The norm is the constant term of the characteristic polynomial::

            sage: f.charpoly_mod(mod)
            [-8846 -594 -60 14 1]"""
    def preallocate_space(self, longn) -> Any:
        """ntl_ZZX.preallocate_space(self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1154)

        Pre-allocate spaces for n coefficients.  The polynomial that f
        represents is unchanged.  This is useful if you know you'll be
        setting coefficients up to n, so memory isn't re-allocated as
        the polynomial grows.  (You might save a millisecond with this
        function.)

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3])
            sage: f.preallocate_space(20)
            sage: f
            [1 2 3]
            sage: f[10]=5  # no new memory is allocated
            sage: f
            [1 2 3 0 0 0 0 0 0 0 5]"""
    @overload
    def primitive_part(self) -> Any:
        """ntl_ZZX.primitive_part(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 615)

        Return the primitive part of f.  Our convention is that the leading
        coefficient of the primitive part is nonnegative, and the primitive
        part of 0 is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([6,12,3,9])
            sage: f.primitive_part()
            [2 4 1 3]
            sage: f
            [6 12 3 9]
            sage: f = ntl.ZZX([6,12,3,-9])
            sage: f
            [6 12 3 -9]
            sage: f.primitive_part()
            [-2 -4 -1 3]
            sage: f = ntl.ZZX()
            sage: f.primitive_part()
            []"""
    @overload
    def primitive_part(self) -> Any:
        """ntl_ZZX.primitive_part(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 615)

        Return the primitive part of f.  Our convention is that the leading
        coefficient of the primitive part is nonnegative, and the primitive
        part of 0 is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([6,12,3,9])
            sage: f.primitive_part()
            [2 4 1 3]
            sage: f
            [6 12 3 9]
            sage: f = ntl.ZZX([6,12,3,-9])
            sage: f
            [6 12 3 -9]
            sage: f.primitive_part()
            [-2 -4 -1 3]
            sage: f = ntl.ZZX()
            sage: f.primitive_part()
            []"""
    @overload
    def primitive_part(self) -> Any:
        """ntl_ZZX.primitive_part(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 615)

        Return the primitive part of f.  Our convention is that the leading
        coefficient of the primitive part is nonnegative, and the primitive
        part of 0 is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([6,12,3,9])
            sage: f.primitive_part()
            [2 4 1 3]
            sage: f
            [6 12 3 9]
            sage: f = ntl.ZZX([6,12,3,-9])
            sage: f
            [6 12 3 -9]
            sage: f.primitive_part()
            [-2 -4 -1 3]
            sage: f = ntl.ZZX()
            sage: f.primitive_part()
            []"""
    @overload
    def primitive_part(self) -> Any:
        """ntl_ZZX.primitive_part(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 615)

        Return the primitive part of f.  Our convention is that the leading
        coefficient of the primitive part is nonnegative, and the primitive
        part of 0 is 0.

        EXAMPLES::

            sage: f = ntl.ZZX([6,12,3,9])
            sage: f.primitive_part()
            [2 4 1 3]
            sage: f
            [6 12 3 9]
            sage: f = ntl.ZZX([6,12,3,-9])
            sage: f
            [6 12 3 -9]
            sage: f.primitive_part()
            [-2 -4 -1 3]
            sage: f = ntl.ZZX()
            sage: f.primitive_part()
            []"""
    def pseudo_quo_rem(self, ntl_ZZXother) -> Any:
        """ntl_ZZX.pseudo_quo_rem(self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 639)

        Perform pseudo-division: computes q and r with deg(r) <
        deg(b), and \\code{LeadCoeff(b)\\^(deg(a)-deg(b)+1) a = b q + r}.
        Only the classical algorithm is used.

        EXAMPLES::

            sage: f = ntl.ZZX([0,1])
            sage: g = ntl.ZZX([1,2,3])
            sage: g.pseudo_quo_rem(f)
            ([2 3], [1])
            sage: f = ntl.ZZX([1,1])
            sage: g.pseudo_quo_rem(f)
            ([-1 3], [2])"""
    @overload
    def quo_rem(self, ntl_ZZXother) -> Any:
        """ntl_ZZX.quo_rem(self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 395)

        Return the unique integral q and r such that ``self = q*other +
        r``, if they exist.  Otherwise raises an Exception.

        EXAMPLES::

           sage: f = ntl.ZZX(list(range(10))); g = ntl.ZZX([-1,0,1])
           sage: q, r = f.quo_rem(g)
           sage: q, r
           ([20 24 18 21 14 16 8 9], [20 25])
           sage: q*g + r == f
           True"""
    @overload
    def quo_rem(self, g) -> Any:
        """ntl_ZZX.quo_rem(self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 395)

        Return the unique integral q and r such that ``self = q*other +
        r``, if they exist.  Otherwise raises an Exception.

        EXAMPLES::

           sage: f = ntl.ZZX(list(range(10))); g = ntl.ZZX([-1,0,1])
           sage: q, r = f.quo_rem(g)
           sage: q, r
           ([20 24 18 21 14 16 8 9], [20 25])
           sage: q*g + r == f
           True"""
    @overload
    def resultant(self, ntl_ZZXother, proof=...) -> Any:
        """ntl_ZZX.resultant(self, ntl_ZZX other, proof=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1017)

        Return the resultant of ``self`` and ``other``.  If proof = False (the
        default is proof=None, see proof.polynomial or sage.structure.proof,
        but the global default is True), then this function may use a
        randomized strategy that errors with probability no more than
        `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([17,0,1,1])
            sage: g = ntl.ZZX([34,-17,18,2])
            sage: f.resultant(g)
            1345873
            sage: f.resultant(g, proof=False)
            1345873"""
    @overload
    def resultant(self, g) -> Any:
        """ntl_ZZX.resultant(self, ntl_ZZX other, proof=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1017)

        Return the resultant of ``self`` and ``other``.  If proof = False (the
        default is proof=None, see proof.polynomial or sage.structure.proof,
        but the global default is True), then this function may use a
        randomized strategy that errors with probability no more than
        `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([17,0,1,1])
            sage: g = ntl.ZZX([34,-17,18,2])
            sage: f.resultant(g)
            1345873
            sage: f.resultant(g, proof=False)
            1345873"""
    @overload
    def resultant(self, g, proof=...) -> Any:
        """ntl_ZZX.resultant(self, ntl_ZZX other, proof=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1017)

        Return the resultant of ``self`` and ``other``.  If proof = False (the
        default is proof=None, see proof.polynomial or sage.structure.proof,
        but the global default is True), then this function may use a
        randomized strategy that errors with probability no more than
        `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([17,0,1,1])
            sage: g = ntl.ZZX([34,-17,18,2])
            sage: f.resultant(g)
            1345873
            sage: f.resultant(g, proof=False)
            1345873"""
    @overload
    def reverse(self, hi=...) -> Any:
        """ntl_ZZX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 849)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3,4,5])
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
        """ntl_ZZX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 849)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3,4,5])
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
        """ntl_ZZX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 849)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3,4,5])
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
        """ntl_ZZX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 849)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3,4,5])
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
        """ntl_ZZX.reverse(self, hi=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 849)

        Return the polynomial obtained by reversing the coefficients
        of this polynomial.  If hi is set then this function behaves
        as if this polynomial has degree hi.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3,4,5])
            sage: f.reverse()
            [5 4 3 2 1]
            sage: f.reverse(hi=10)
            [0 0 0 0 0 0 5 4 3 2 1]
            sage: f.reverse(hi=2)
            [3 2 1]
            sage: f.reverse(hi=-2)
            []"""
    def right_shift(self, longn) -> Any:
        """ntl_ZZX.right_shift(self, long n)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 571)

        Return the polynomial obtained by shifting all coefficients of
        this polynomial to the right n positions.

        EXAMPLES::

            sage: f = ntl.ZZX([2,0,0,1])
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
        '''ntl_ZZX.set_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 797)

        Set this polynomial to the monomial "x".

        EXAMPLES::

            sage: f = ntl.ZZX()
            sage: f.set_x()
            sage: f
            [0 1]
            sage: g = ntl.ZZX([0,1])
            sage: f == g
            True

        Though f and g are equal, they are not the same objects in memory::

            sage: f is g
            False'''
    @overload
    def set_x(self) -> Any:
        '''ntl_ZZX.set_x(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 797)

        Set this polynomial to the monomial "x".

        EXAMPLES::

            sage: f = ntl.ZZX()
            sage: f.set_x()
            sage: f
            [0 1]
            sage: g = ntl.ZZX([0,1])
            sage: f == g
            True

        Though f and g are equal, they are not the same objects in memory::

            sage: f is g
            False'''
    def setitem_from_int_doctest(self, i, value) -> Any:
        """ntl_ZZX.setitem_from_int_doctest(self, i, value)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 211)

        This method exists solely for automated testing of setitem_from_int().

        sage: x = ntl.ZZX([2, 3, 4])
        sage: x.setitem_from_int_doctest(5, 42)
        sage: x
         [2 3 4 0 0 42]"""
    def square(self) -> Any:
        """ntl_ZZX.square(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 418)

        Return f*f.

        EXAMPLES::

            sage: f = ntl.ZZX([-1,0,1])
            sage: f*f
            [1 0 -2 0 1]"""
    def square_and_truncate(self, longm) -> Any:
        """ntl_ZZX.square_and_truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 917)

        Return self*self but with terms of degree >= m removed.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3,4,5])
            sage: f.square_and_truncate(4)
            [1 4 10 20]
            sage: (f*f).truncate(4)
            [1 4 10 20]"""
    @overload
    def squarefree_decomposition(self) -> Any:
        """ntl_ZZX.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1176)

        Return the square-free decomposition of ``self`` (a partial
        factorization into square-free, relatively prime polynomials)
        as a list of 2-tuples, where the first element in each tuple
        is a factor, and the second is its exponent.
        Assumes that ``self`` is primitive.

        EXAMPLES::

            sage: f = ntl.ZZX([0, 1, 2, 1])
            sage: f.squarefree_decomposition()
            [([0 1], 1), ([1 1], 2)]"""
    @overload
    def squarefree_decomposition(self) -> Any:
        """ntl_ZZX.squarefree_decomposition(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 1176)

        Return the square-free decomposition of ``self`` (a partial
        factorization into square-free, relatively prime polynomials)
        as a list of 2-tuples, where the first element in each tuple
        is a factor, and the second is its exponent.
        Assumes that ``self`` is primitive.

        EXAMPLES::

            sage: f = ntl.ZZX([0, 1, 2, 1])
            sage: f.squarefree_decomposition()
            [([0 1], 1), ([1 1], 2)]"""
    @overload
    def trace_list(self) -> Any:
        """ntl_ZZX.trace_list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 988)

        Return the list of traces of the powers `x^i` of the
        monomial x modulo this polynomial for i = 0, ..., deg(f)-1.
        This polynomial must be monic.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,0,3,0,1])
            sage: f.trace_list()
            [5, 0, -6, 0, 10]

        The input polynomial must be monic or a :exc:`ValueError` is raised::

            sage: f = ntl.ZZX([1,2,0,3,0,2])
            sage: f.trace_list()
            Traceback (most recent call last):
            ...
            ValueError: polynomial must be monic."""
    @overload
    def trace_list(self) -> Any:
        """ntl_ZZX.trace_list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 988)

        Return the list of traces of the powers `x^i` of the
        monomial x modulo this polynomial for i = 0, ..., deg(f)-1.
        This polynomial must be monic.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,0,3,0,1])
            sage: f.trace_list()
            [5, 0, -6, 0, 10]

        The input polynomial must be monic or a :exc:`ValueError` is raised::

            sage: f = ntl.ZZX([1,2,0,3,0,2])
            sage: f.trace_list()
            Traceback (most recent call last):
            ...
            ValueError: polynomial must be monic."""
    @overload
    def trace_list(self) -> Any:
        """ntl_ZZX.trace_list(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 988)

        Return the list of traces of the powers `x^i` of the
        monomial x modulo this polynomial for i = 0, ..., deg(f)-1.
        This polynomial must be monic.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,0,3,0,1])
            sage: f.trace_list()
            [5, 0, -6, 0, 10]

        The input polynomial must be monic or a :exc:`ValueError` is raised::

            sage: f = ntl.ZZX([1,2,0,3,0,2])
            sage: f.trace_list()
            Traceback (most recent call last):
            ...
            ValueError: polynomial must be monic."""
    @overload
    def trace_mod(self, ntl_ZZXmodulus) -> Any:
        """ntl_ZZX.trace_mod(self, ntl_ZZX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 972)

        Return the trace of this polynomial modulus the modulus.
        The modulus must be monic, and of positive degree bigger
        than the degree of ``self``.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,0,3])
            sage: mod = ntl.ZZX([5,3,-1,1,1])
            sage: f.trace_mod(mod)
            -37"""
    @overload
    def trace_mod(self, mod) -> Any:
        """ntl_ZZX.trace_mod(self, ntl_ZZX modulus)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 972)

        Return the trace of this polynomial modulus the modulus.
        The modulus must be monic, and of positive degree bigger
        than the degree of ``self``.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,0,3])
            sage: mod = ntl.ZZX([5,3,-1,1,1])
            sage: f.trace_mod(mod)
            -37"""
    def truncate(self, longm) -> Any:
        """ntl_ZZX.truncate(self, long m)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 872)

        Return the truncation of this polynomial obtained by
        removing all terms of degree >= m.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3,4,5])
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
    def xgcd(self, ntl_ZZXother, proof=...) -> Any:
        """ntl_ZZX.xgcd(self, ntl_ZZX other, proof=None)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 695)

        If ``self`` and ``other`` are coprime over the rationals,
        return ``r, s, t`` such that ``r = s*self + t*other``.
        Otherwise return 0.

        This is \\emph{not} the same as the \\sage function on
        polynomials over the integers, since here the return value r
        is always an integer.

        Here r is the resultant of a and b; if r != 0, then this
        function computes s and t such that: a*s + b*t = r; otherwise
        s and t are both 0.  If proof = False (*not* the default),
        then resultant computation may use a randomized strategy that
        errors with probability no more than `2^{-80}`.  The default is
        default is proof=None, see proof.polynomial or sage.structure.proof,
        but the global default is True), then this function may use a
        randomized strategy that errors with probability no more than
        `2^{-80}`.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3]) * ntl.ZZX([4,5])**2
            sage: g = ntl.ZZX([1,1,1])**3 * ntl.ZZX([1,2,3])
            sage: f.xgcd(g)   # nothing since they are not coprime
            (0, [], [])

        In this example the input quadratic polynomials have a common root modulo 13::

            sage: f = ntl.ZZX([5,0,1])
            sage: g = ntl.ZZX([18,0,1])
            sage: f.xgcd(g)
            (169, [-13], [13])"""
    def __add__(self, ntl_ZZXself, ntl_ZZXother) -> Any:
        """ntl_ZZX.__add__(ntl_ZZX self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 290)

        EXAMPLES::

            sage: ntl.ZZX(list(range(5))) + ntl.ZZX(list(range(6)))
            [0 2 4 6 8 5]"""
    def __copy__(self) -> Any:
        """ntl_ZZX.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 168)

        Return a copy of ``self``.

        EXAMPLES::

            sage: x = ntl.ZZX([1,32])
            sage: y = copy(x)
            sage: y == x
            True
            sage: y is x
            False"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __getitem__(self, longi) -> Any:
        """ntl_ZZX.__getitem__(self, long i)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 222)

        Retrieves coefficient number i as an NTL ZZ.

        sage: x = ntl.ZZX([129381729371289371237128318293718237, 2, -3, 0, 4])
        sage: x[0]
         129381729371289371237128318293718237
        sage: type(x[0])
         <class 'sage.libs.ntl.ntl_ZZ.ntl_ZZ'>
        sage: x[1]
         2
        sage: x[2]
         -3
        sage: x[3]
         0
        sage: x[4]
         4
        sage: x[5]
         0"""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __mod__(self, ntl_ZZXself, ntl_ZZXother) -> Any:
        """ntl_ZZX.__mod__(ntl_ZZX self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 368)

        Given polynomials a, b in ZZ[X], there exist polynomials q, r
        in QQ[X] such that a = b*q + r, deg(r) < deg(b).  This
        function returns q if q lies in ZZ[X], and otherwise raises an
        Exception.

        EXAMPLES::

            sage: f = ntl.ZZX([2,4,6]); g = ntl.ZZX([2])
            sage: f % g   # 0
            []

            sage: f = ntl.ZZX(list(range(10))); g = ntl.ZZX([-1,0,1])
            sage: f % g
            [20 25]"""
    def __mul__(self, ntl_ZZXself, ntl_ZZXother) -> Any:
        """ntl_ZZX.__mul__(ntl_ZZX self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 320)

        EXAMPLES::

            sage: ntl.ZZX(list(range(5))) * ntl.ZZX(list(range(6)))
            [0 0 1 4 10 20 30 34 31 20]"""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
    def __neg__(self) -> Any:
        """ntl_ZZX.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 538)

        Return the negative of ``self``.

        EXAMPLES::

            sage: f = ntl.ZZX([2,0,0,1])
            sage: -f
            [-2 0 0 -1]"""
    def __pow__(self, ntl_ZZXself, longn, ignored) -> Any:
        """ntl_ZZX.__pow__(ntl_ZZX self, long n, ignored)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 431)

        Return the `n`-th nonnegative power of ``self``.

        EXAMPLES::

            sage: g = ntl.ZZX([-1,0,1])
            sage: g ^ 10
            [1 0 -10 0 45 0 -120 0 210 0 -252 0 210 0 -120 0 45 0 -10 0 1]
            sage: g ^ 0
            [1]
            sage: g ^ 1
            [-1 0 1]
            sage: g ^ (-1)
            Traceback (most recent call last):
            ...
            ArithmeticError"""
    def __radd__(self, other):
        """Return value+self."""
    def __reduce__(self) -> Any:
        """ntl_ZZX.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 142)

        EXAMPLES::

            sage: from sage.libs.ntl.ntl_ZZX import ntl_ZZX
            sage: f = ntl_ZZX([1,2,0,4])
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
        """ntl_ZZX.__setitem__(self, long i, a)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 183)

        EXAMPLES::

            sage: n=ntl.ZZX([1,2,3])
            sage: n
            [1 2 3]
            sage: n[1] = 4
            sage: n
            [1 4 3]"""
    def __sub__(self, ntl_ZZXself, ntl_ZZXother) -> Any:
        """ntl_ZZX.__sub__(ntl_ZZX self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 305)

        EXAMPLES::

            sage: ntl.ZZX(list(range(5))) - ntl.ZZX(list(range(6)))
            [0 0 0 0 0 -5]"""
    def __truediv__(self, ntl_ZZXself, ntl_ZZXother) -> Any:
        """ntl_ZZX.__truediv__(ntl_ZZX self, ntl_ZZX other)

        File: /build/sagemath/src/sage/src/sage/libs/ntl/ntl_ZZX.pyx (starting at line 337)

        Compute quotient ``self / other``, if the quotient is a polynomial.
        Otherwise an Exception is raised.

        EXAMPLES::

            sage: f = ntl.ZZX([1,2,3]) * ntl.ZZX([4,5])**2
            sage: g = ntl.ZZX([4,5])
            sage: f/g
            [4 13 22 15]
            sage: ntl.ZZX([1,2,3]) * ntl.ZZX([4,5])
            [4 13 22 15]

            sage: f = ntl.ZZX(list(range(10))); g = ntl.ZZX([-1,0,1])
            sage: f/g
            Traceback (most recent call last):
            ...
            ArithmeticError: self (=[0 1 2 3 4 5 6 7 8 9]) is not divisible by other (=[-1 0 1])"""
