import _cython_3_2_1
import sage as sage
import sage.rings.finite_rings.element_base
from sage.interfaces.abc import GapElement as GapElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract as IntegerMod_abstract
from sage.rings.polynomial.multi_polynomial import MPolynomial as MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial as Polynomial
from sage.rings.rational import Rational as Rational
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

unpickle_FiniteFieldElement_pari_ffelt: _cython_3_2_1.cython_function_or_method

class FiniteFieldElement_pari_ffelt(sage.rings.finite_rings.element_base.FinitePolyExtElement):
    '''FiniteFieldElement_pari_ffelt(parent, x)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 89)

    An element of a finite field implemented using PARI.

    EXAMPLES::

        sage: K = FiniteField(10007^10, \'a\', impl=\'pari_ffelt\')
        sage: a = K.gen(); a
        a
        sage: type(a)
        <class \'sage.rings.finite_rings.element_pari_ffelt.FiniteFieldElement_pari_ffelt\'>

    TESTS::

        sage: n = 63
        sage: m = 3
        sage: K.<a> = GF(2^n, impl=\'pari_ffelt\')
        sage: f = conway_polynomial(2, n)
        sage: f(a) == 0
        True
        sage: e = (2^n - 1) / (2^m - 1)
        sage: conway_polynomial(2, m)(a^e) == 0
        True

        sage: K.<a> = FiniteField(2^16, impl=\'pari_ffelt\')
        sage: K(0).is_zero()
        True
        sage: (a - a).is_zero()
        True
        sage: a - a
        0
        sage: a == a
        True
        sage: a - a == 0
        True
        sage: a - a == K(0)
        True
        sage: TestSuite(a).run()

    Test creating elements from basic Python types::

        sage: K.<a> = FiniteField(7^20, impl=\'pari_ffelt\')
        sage: K(int(8))
        1

    ::

        sage: k = FiniteField(3^4, \'a\', impl=\'pari_ffelt\')
        sage: b = k(5) # indirect doctest
        sage: b.parent()
        Finite Field in a of size 3^4
        sage: a = k.gen()
        sage: k(a + 2)
        a + 2

    Univariate polynomials coerce into finite fields by evaluating
    the polynomial at the field\'s generator::

        sage: R.<x> = QQ[]
        sage: k.<a> = FiniteField(5^2, \'a\', impl=\'pari_ffelt\')
        sage: k(R(2/3))
        4
        sage: k(x^2)
        a + 3

        sage: R.<x> = GF(5)[]
        sage: k(x^3-2*x+1)
        2*a + 4

        sage: x = polygen(QQ)
        sage: k(x^25)
        a

        sage: Q.<q> = FiniteField(5^7, \'q\', impl=\'pari_ffelt\')
        sage: L = GF(5)
        sage: LL.<xx> = L[]
        sage: Q(xx^2 + 2*xx + 4)
        q^2 + 2*q + 4

        sage: k = FiniteField(3^11, \'t\', impl=\'pari_ffelt\')
        sage: k.polynomial()
        t^11 + 2*t^2 + 1
        sage: P = k.polynomial_ring()
        sage: k(P.0^11)
        t^2 + 2

    An element can be specified by its vector of coordinates with
    respect to the basis consisting of powers of the generator:

        sage: k = FiniteField(3^11, \'t\', impl=\'pari_ffelt\')
        sage: V = k.vector_space(map=False)
        sage: V
        Vector space of dimension 11 over Finite Field of size 3
        sage: v = V([0,1,2,0,1,2,0,1,2,0,1])
        sage: k(v)
        t^10 + 2*t^8 + t^7 + 2*t^5 + t^4 + 2*t^2 + t

    Multivariate polynomials only coerce if constant::

        sage: k = FiniteField(5^2, \'a\', impl=\'pari_ffelt\')
        sage: R = k[\'x,y,z\']; R
        Multivariate Polynomial Ring in x, y, z over Finite Field in a of size 5^2
        sage: k(R(2))
        2
        sage: R = QQ[\'x,y,z\']
        sage: k(R(1/5))
        Traceback (most recent call last):
        ...
        ZeroDivisionError: inverse of Mod(0, 5) does not exist

    Gap elements can also be coerced into finite fields::

        sage: F = FiniteField(2^3, \'a\', impl=\'pari_ffelt\')
        sage: a = F.multiplicative_generator(); a
        a
        sage: b = gap(a^3); b                                                           # needs sage.libs.gap
        Z(2^3)^3
        sage: F(b)
        a + 1
        sage: a^3
        a + 1

        sage: a = GF(13)(gap(\'0*Z(13)\')); a                                             # needs sage.libs.gap
        0
        sage: a.parent()
        Finite Field of size 13

        sage: F = FiniteField(2^4, \'a\', impl=\'pari_ffelt\')
        sage: F(gap(\'Z(16)^3\'))                                                         # needs sage.libs.gap
        a^3
        sage: F(gap(\'Z(16)^2\'))                                                         # needs sage.libs.gap
        a^2

    You can also call a finite extension field with a string
    to produce an element of that field, like this::

        sage: k = GF(2^8, \'a\')
        sage: k(\'a^200\')
        a^4 + a^3 + a^2

    This is especially useful for conversion from Singular etc.

    TESTS::

        sage: k = FiniteField(3^2, \'a\', impl=\'pari_ffelt\')
        sage: a = k(11); a
        2
        sage: a.parent()
        Finite Field in a of size 3^2
        sage: V = k.vector_space(map=False); v = V((1,2))
        sage: k(v)
        2*a + 1

    We create elements using a list and verify that :issue:`10486` has
    been fixed::

        sage: k = FiniteField(3^11, \'t\', impl=\'pari_ffelt\')
        sage: x = k([1,0,2,1]); x
        t^3 + 2*t^2 + 1
        sage: x + x + x
        0
        sage: pari(x)
        t^3 + 2*t^2 + 1

    If the list is longer than the degree, we just get the result
    modulo the modulus::

        sage: from sage.rings.finite_rings.finite_field_pari_ffelt import FiniteField_pari_ffelt
        sage: R.<a> = PolynomialRing(GF(5))
        sage: k = FiniteField_pari_ffelt(5, a^2 - 2, \'t\')
        sage: x = k([0,0,0,1]); x
        2*t
        sage: pari(x)
        2*t

    When initializing from a list, the elements are first coerced
    to the prime field (:issue:`11685`)::

        sage: k = FiniteField(3^11, \'t\', impl=\'pari_ffelt\')
        sage: k([ 0, 1/2 ])
        2*t
        sage: k([ 0, 1/2, 0, 0, 0, 0, 0, 0, 0, -1, 0 ])
        2*t^9 + 2*t
        sage: k([ k(0), k(1) ])
        t
        sage: k([ GF(3)(2), GF(3^5,\'u\')(1) ])
        t + 2
        sage: R.<x> = PolynomialRing(k)
        sage: k([ x/x ])
        1
        sage: k([ R(-1), x/x ])
        t + 2
        sage: k([ R(-1), R(0), 0 ])
        2

    Check that zeros are created correctly (:issue:`11685`)::

        sage: K = FiniteField(3^11, \'t\', impl=\'pari_ffelt\'); a = K.0
        sage: v = 0; pari(K(v))
        0
        sage: v = Mod(0,3); pari(K(v))
        0
        sage: v = pari(0); pari(K(v))
        0
        sage: v = pari("Mod(0,3)"); pari(K(v))
        0
        sage: v = []; pari(K(v))
        0
        sage: v = [0]; pari(K(v))
        0
        sage: v = [0,0]; pari(K(v))
        0
        sage: v = pari("Pol(0)"); pari(K(v))
        0
        sage: v = pari("Mod(0, %s)"%K.modulus()); pari(K(v))
        0
        sage: v = pari("Mod(Pol(0), %s)"%K.modulus()); pari(K(v))
        0
        sage: v = K(1) - K(1); pari(K(v))
        0
        sage: v = K([1]) - K([1]); pari(K(v))
        0
        sage: v = a - a; pari(K(v))
        0
        sage: v = K(1)*0; pari(K(v))
        0
        sage: v = K([1])*K([0]); pari(K(v))
        0
        sage: v = a*0; pari(K(v))
        0'''
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, x) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 321)

                Initialise ``self`` with the given ``parent`` and value
                converted from ``x``.

                This is called when constructing elements from Python.

                TESTS::

                    sage: from sage.rings.finite_rings.element_pari_ffelt import FiniteFieldElement_pari_ffelt
                    sage: K = FiniteField(101^2, 'a', impl='pari_ffelt')
                    sage: x = FiniteFieldElement_pari_ffelt(K, 'a + 1')
                    sage: x
                    a + 1
        """
    def charpoly(self, var=...) -> Any:
        """FiniteFieldElement_pari_ffelt.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 973)

        Return the characteristic polynomial of ``self``.

        INPUT:

        - ``var`` -- string (default: ``'x'``); variable name to use

        EXAMPLES::

            sage: R.<x> = PolynomialRing(FiniteField(3))
            sage: F.<a> = FiniteField(3^2, modulus=x^2 + 1, impl='pari_ffelt')
            sage: a.charpoly('y')
            y^2 + 1"""
    def frobenius(self, *args, **kwargs):
        """FiniteFieldElement_pari_ffelt.pth_power(self, int k=1)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 861)

        Return the `(p^k)`-th power of ``self``, where `p` is the
        characteristic of the field.

        INPUT:

        - ``k`` -- integer (default: 1); must fit in a C ``int``

        Note that if `k` is negative, then this computes the appropriate root.

        TESTS::

            sage: # needs sage.modules
            sage: F.<a> = GF(13^64, impl='pari_ffelt'); F
            Finite Field in a of size 13^64
            sage: x = F.random_element()
            sage: x.pth_power(0) == x
            True
            sage: x.pth_power(1) == x**13
            True
            sage: x.pth_power(2) == x**(13**2)
            True
            sage: x.pth_power(-1)**13 == x
            True

            sage: # needs sage.modules
            sage: F.<a> = GF(127^16, impl='pari_ffelt'); F
            Finite Field in a of size 127^16
            sage: x = F.random_element()
            sage: x.pth_power(0) == x
            True
            sage: x.pth_power(1) == x**127
            True
            sage: x.pth_power(2) == x**(127**2)
            True
            sage: x.pth_power(-1)**127 == x
            True"""
    @overload
    def is_one(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 741)

        Return ``True`` if ``self`` equals 1.

        EXAMPLES::

            sage: F.<a> = FiniteField(5^3, impl='pari_ffelt')
            sage: a.is_one()
            False
            sage: (a/a).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 741)

        Return ``True`` if ``self`` equals 1.

        EXAMPLES::

            sage: F.<a> = FiniteField(5^3, impl='pari_ffelt')
            sage: a.is_one()
            False
            sage: (a/a).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 741)

        Return ``True`` if ``self`` equals 1.

        EXAMPLES::

            sage: F.<a> = FiniteField(5^3, impl='pari_ffelt')
            sage: a.is_one()
            False
            sage: (a/a).is_one()
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 992)

        Return ``True`` if and only if ``self`` is a square in the
        finite field.

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: a.is_square()
            False
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(2^2, impl='pari_ffelt')
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt')
            sage: (a**2).is_square()
            True
            sage: a.is_square()
            False
            sage: k(0).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 992)

        Return ``True`` if and only if ``self`` is a square in the
        finite field.

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: a.is_square()
            False
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(2^2, impl='pari_ffelt')
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt')
            sage: (a**2).is_square()
            True
            sage: a.is_square()
            False
            sage: k(0).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 992)

        Return ``True`` if and only if ``self`` is a square in the
        finite field.

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: a.is_square()
            False
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(2^2, impl='pari_ffelt')
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt')
            sage: (a**2).is_square()
            True
            sage: a.is_square()
            False
            sage: k(0).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 992)

        Return ``True`` if and only if ``self`` is a square in the
        finite field.

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: a.is_square()
            False
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(2^2, impl='pari_ffelt')
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt')
            sage: (a**2).is_square()
            True
            sage: a.is_square()
            False
            sage: k(0).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 992)

        Return ``True`` if and only if ``self`` is a square in the
        finite field.

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: a.is_square()
            False
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(2^2, impl='pari_ffelt')
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt')
            sage: (a**2).is_square()
            True
            sage: a.is_square()
            False
            sage: k(0).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 992)

        Return ``True`` if and only if ``self`` is a square in the
        finite field.

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: a.is_square()
            False
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(2^2, impl='pari_ffelt')
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt')
            sage: (a**2).is_square()
            True
            sage: a.is_square()
            False
            sage: k(0).is_square()
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 992)

        Return ``True`` if and only if ``self`` is a square in the
        finite field.

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: a.is_square()
            False
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(2^2, impl='pari_ffelt')
            sage: (a**2).is_square()
            True

            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt')
            sage: (a**2).is_square()
            True
            sage: a.is_square()
            False
            sage: k(0).is_square()
            True"""
    @overload
    def is_unit(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 755)

        Return ``True`` if ``self`` is nonzero.

        EXAMPLES::

            sage: F.<a> = FiniteField(5^3, impl='pari_ffelt')
            sage: a.is_unit()
            True"""
    @overload
    def is_unit(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 755)

        Return ``True`` if ``self`` is nonzero.

        EXAMPLES::

            sage: F.<a> = FiniteField(5^3, impl='pari_ffelt')
            sage: a.is_unit()
            True"""
    @overload
    def is_zero(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 727)

        Return ``True`` if ``self`` equals 0.

        EXAMPLES::

            sage: F.<a> = FiniteField(5^3, impl='pari_ffelt')
            sage: a.is_zero()
            False
            sage: (a - a).is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 727)

        Return ``True`` if ``self`` equals 0.

        EXAMPLES::

            sage: F.<a> = FiniteField(5^3, impl='pari_ffelt')
            sage: a.is_zero()
            False
            sage: (a - a).is_zero()
            True"""
    @overload
    def is_zero(self) -> Any:
        """FiniteFieldElement_pari_ffelt.is_zero(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 727)

        Return ``True`` if ``self`` equals 0.

        EXAMPLES::

            sage: F.<a> = FiniteField(5^3, impl='pari_ffelt')
            sage: a.is_zero()
            False
            sage: (a - a).is_zero()
            True"""
    @overload
    def lift(self) -> Any:
        """FiniteFieldElement_pari_ffelt.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1228)

        If ``self`` is an element of the prime field, return a lift of
        this element to an integer.

        EXAMPLES::

            sage: k = FiniteField(next_prime(10^10)^2, 'u', impl='pari_ffelt')
            sage: a = k(17)/k(19)
            sage: b = a.lift(); b
            7894736858
            sage: b.parent()
            Integer Ring"""
    @overload
    def lift(self) -> Any:
        """FiniteFieldElement_pari_ffelt.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1228)

        If ``self`` is an element of the prime field, return a lift of
        this element to an integer.

        EXAMPLES::

            sage: k = FiniteField(next_prime(10^10)^2, 'u', impl='pari_ffelt')
            sage: a = k(17)/k(19)
            sage: b = a.lift(); b
            7894736858
            sage: b.parent()
            Integer Ring"""
    @overload
    def log(self, base, order=..., check=...) -> Any:
        """FiniteFieldElement_pari_ffelt.log(self, base, order=None, *, check=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1100)

        Return a discrete logarithm of ``self`` with respect to the
        given base.

        INPUT:

        - ``base`` -- nonzero field element
        - ``order`` -- integer (optional), the order of the base
        - ``check`` -- boolean (default: ``False``); if set,
          test whether the given ``order`` is correct

        OUTPUT:

        An integer `x` such that ``self`` equals ``base`` raised to
        the power `x`.  If no such `x` exists, a :exc:`ValueError` is
        raised.

        EXAMPLES::

            sage: F.<g> = FiniteField(2^10, impl='pari_ffelt')
            sage: b = g; a = g^37
            sage: a.log(b)
            37
            sage: b^37; a
            g^8 + g^7 + g^4 + g + 1
            g^8 + g^7 + g^4 + g + 1

        ::

            sage: F.<a> = FiniteField(5^2, impl='pari_ffelt')
            sage: F(-1).log(F(2))
            2
            sage: F(1).log(a)
            0

        ::

            sage: p = 2^127-1
            sage: F.<t> = GF((p, 3))
            sage: elt = F.random_element()^(p^2+p+1)
            sage: (elt^2).log(elt, p-1)
            2

        Passing the ``order`` argument can lead to huge speedups when
        factoring the order of the entire unit group is expensive but
        the order of the base element is much smaller::

            sage: %timeit (elt^2).log(elt)       # not tested
            6.18 s ± 85 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
            sage: %timeit (elt^2).log(elt, p-1)  # not tested
            147 ms ± 1.39 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

        Some cases where the logarithm is not defined or does not exist::

            sage: F.<a> = GF(3^10, impl='pari_ffelt')
            sage: a.log(-1)
            Traceback (most recent call last):
            ...
            ArithmeticError: element a does not lie in group generated by 2
            sage: a.log(0)
            Traceback (most recent call last):
            ...
            ArithmeticError: discrete logarithm with base 0 is not defined
            sage: F(0).log(1)
            Traceback (most recent call last):
            ...
            ArithmeticError: discrete logarithm of 0 is not defined

        TESTS:

        An example for ``check=True``::

            sage: a = GF(101^5).primitive_element()
            sage: a.log(a, 10510100500, check=True)
            1
            sage: a.log(a, 5255050250, check=True)
            Traceback (most recent call last):
            ...
            ValueError: element does not have the provided order"""
    @overload
    def log(self, b) -> Any:
        """FiniteFieldElement_pari_ffelt.log(self, base, order=None, *, check=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1100)

        Return a discrete logarithm of ``self`` with respect to the
        given base.

        INPUT:

        - ``base`` -- nonzero field element
        - ``order`` -- integer (optional), the order of the base
        - ``check`` -- boolean (default: ``False``); if set,
          test whether the given ``order`` is correct

        OUTPUT:

        An integer `x` such that ``self`` equals ``base`` raised to
        the power `x`.  If no such `x` exists, a :exc:`ValueError` is
        raised.

        EXAMPLES::

            sage: F.<g> = FiniteField(2^10, impl='pari_ffelt')
            sage: b = g; a = g^37
            sage: a.log(b)
            37
            sage: b^37; a
            g^8 + g^7 + g^4 + g + 1
            g^8 + g^7 + g^4 + g + 1

        ::

            sage: F.<a> = FiniteField(5^2, impl='pari_ffelt')
            sage: F(-1).log(F(2))
            2
            sage: F(1).log(a)
            0

        ::

            sage: p = 2^127-1
            sage: F.<t> = GF((p, 3))
            sage: elt = F.random_element()^(p^2+p+1)
            sage: (elt^2).log(elt, p-1)
            2

        Passing the ``order`` argument can lead to huge speedups when
        factoring the order of the entire unit group is expensive but
        the order of the base element is much smaller::

            sage: %timeit (elt^2).log(elt)       # not tested
            6.18 s ± 85 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
            sage: %timeit (elt^2).log(elt, p-1)  # not tested
            147 ms ± 1.39 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

        Some cases where the logarithm is not defined or does not exist::

            sage: F.<a> = GF(3^10, impl='pari_ffelt')
            sage: a.log(-1)
            Traceback (most recent call last):
            ...
            ArithmeticError: element a does not lie in group generated by 2
            sage: a.log(0)
            Traceback (most recent call last):
            ...
            ArithmeticError: discrete logarithm with base 0 is not defined
            sage: F(0).log(1)
            Traceback (most recent call last):
            ...
            ArithmeticError: discrete logarithm of 0 is not defined

        TESTS:

        An example for ``check=True``::

            sage: a = GF(101^5).primitive_element()
            sage: a.log(a, 10510100500, check=True)
            1
            sage: a.log(a, 5255050250, check=True)
            Traceback (most recent call last):
            ...
            ValueError: element does not have the provided order"""
    @overload
    def log(self, a) -> Any:
        """FiniteFieldElement_pari_ffelt.log(self, base, order=None, *, check=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1100)

        Return a discrete logarithm of ``self`` with respect to the
        given base.

        INPUT:

        - ``base`` -- nonzero field element
        - ``order`` -- integer (optional), the order of the base
        - ``check`` -- boolean (default: ``False``); if set,
          test whether the given ``order`` is correct

        OUTPUT:

        An integer `x` such that ``self`` equals ``base`` raised to
        the power `x`.  If no such `x` exists, a :exc:`ValueError` is
        raised.

        EXAMPLES::

            sage: F.<g> = FiniteField(2^10, impl='pari_ffelt')
            sage: b = g; a = g^37
            sage: a.log(b)
            37
            sage: b^37; a
            g^8 + g^7 + g^4 + g + 1
            g^8 + g^7 + g^4 + g + 1

        ::

            sage: F.<a> = FiniteField(5^2, impl='pari_ffelt')
            sage: F(-1).log(F(2))
            2
            sage: F(1).log(a)
            0

        ::

            sage: p = 2^127-1
            sage: F.<t> = GF((p, 3))
            sage: elt = F.random_element()^(p^2+p+1)
            sage: (elt^2).log(elt, p-1)
            2

        Passing the ``order`` argument can lead to huge speedups when
        factoring the order of the entire unit group is expensive but
        the order of the base element is much smaller::

            sage: %timeit (elt^2).log(elt)       # not tested
            6.18 s ± 85 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
            sage: %timeit (elt^2).log(elt, p-1)  # not tested
            147 ms ± 1.39 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

        Some cases where the logarithm is not defined or does not exist::

            sage: F.<a> = GF(3^10, impl='pari_ffelt')
            sage: a.log(-1)
            Traceback (most recent call last):
            ...
            ArithmeticError: element a does not lie in group generated by 2
            sage: a.log(0)
            Traceback (most recent call last):
            ...
            ArithmeticError: discrete logarithm with base 0 is not defined
            sage: F(0).log(1)
            Traceback (most recent call last):
            ...
            ArithmeticError: discrete logarithm of 0 is not defined

        TESTS:

        An example for ``check=True``::

            sage: a = GF(101^5).primitive_element()
            sage: a.log(a, 10510100500, check=True)
            1
            sage: a.log(a, 5255050250, check=True)
            Traceback (most recent call last):
            ...
            ValueError: element does not have the provided order"""
    @overload
    def log(self, elt) -> Any:
        """FiniteFieldElement_pari_ffelt.log(self, base, order=None, *, check=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1100)

        Return a discrete logarithm of ``self`` with respect to the
        given base.

        INPUT:

        - ``base`` -- nonzero field element
        - ``order`` -- integer (optional), the order of the base
        - ``check`` -- boolean (default: ``False``); if set,
          test whether the given ``order`` is correct

        OUTPUT:

        An integer `x` such that ``self`` equals ``base`` raised to
        the power `x`.  If no such `x` exists, a :exc:`ValueError` is
        raised.

        EXAMPLES::

            sage: F.<g> = FiniteField(2^10, impl='pari_ffelt')
            sage: b = g; a = g^37
            sage: a.log(b)
            37
            sage: b^37; a
            g^8 + g^7 + g^4 + g + 1
            g^8 + g^7 + g^4 + g + 1

        ::

            sage: F.<a> = FiniteField(5^2, impl='pari_ffelt')
            sage: F(-1).log(F(2))
            2
            sage: F(1).log(a)
            0

        ::

            sage: p = 2^127-1
            sage: F.<t> = GF((p, 3))
            sage: elt = F.random_element()^(p^2+p+1)
            sage: (elt^2).log(elt, p-1)
            2

        Passing the ``order`` argument can lead to huge speedups when
        factoring the order of the entire unit group is expensive but
        the order of the base element is much smaller::

            sage: %timeit (elt^2).log(elt)       # not tested
            6.18 s ± 85 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
            sage: %timeit (elt^2).log(elt, p-1)  # not tested
            147 ms ± 1.39 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

        Some cases where the logarithm is not defined or does not exist::

            sage: F.<a> = GF(3^10, impl='pari_ffelt')
            sage: a.log(-1)
            Traceback (most recent call last):
            ...
            ArithmeticError: element a does not lie in group generated by 2
            sage: a.log(0)
            Traceback (most recent call last):
            ...
            ArithmeticError: discrete logarithm with base 0 is not defined
            sage: F(0).log(1)
            Traceback (most recent call last):
            ...
            ArithmeticError: discrete logarithm of 0 is not defined

        TESTS:

        An example for ``check=True``::

            sage: a = GF(101^5).primitive_element()
            sage: a.log(a, 10510100500, check=True)
            1
            sage: a.log(a, 5255050250, check=True)
            Traceback (most recent call last):
            ...
            ValueError: element does not have the provided order"""
    def minpoly(self, var=...) -> Any:
        """FiniteFieldElement_pari_ffelt.minpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 954)

        Return the minimal polynomial of ``self``.

        INPUT:

        - ``var`` -- string (default: ``'x'``); variable name to use

        EXAMPLES::

            sage: R.<x> = PolynomialRing(FiniteField(3))
            sage: F.<a> = FiniteField(3^2, modulus=x^2 + 1, impl='pari_ffelt')
            sage: a.minpoly('y')
            y^2 + 1"""
    @overload
    def multiplicative_order(self) -> Any:
        """FiniteFieldElement_pari_ffelt.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1209)

        Return the order of ``self`` in the multiplicative group.

        EXAMPLES::

            sage: a = FiniteField(5^3, 'a', impl='pari_ffelt').0
            sage: a.multiplicative_order()
            124
            sage: a**124
            1"""
    @overload
    def multiplicative_order(self) -> Any:
        """FiniteFieldElement_pari_ffelt.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1209)

        Return the order of ``self`` in the multiplicative group.

        EXAMPLES::

            sage: a = FiniteField(5^3, 'a', impl='pari_ffelt').0
            sage: a.multiplicative_order()
            124
            sage: a**124
            1"""
    @overload
    def polynomial(self, name=...) -> Any:
        """FiniteFieldElement_pari_ffelt.polynomial(self, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 918)

        Return the unique representative of ``self`` as a polynomial
        over the prime field whose degree is less than the degree of
        the finite field over its prime field.

        INPUT:

        - ``name`` -- (optional) variable name

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: pol = a.polynomial()
            sage: pol
            a
            sage: parent(pol)
            Univariate Polynomial Ring in a over Finite Field of size 3

        ::

            sage: k = FiniteField(3^4, 'alpha', impl='pari_ffelt')
            sage: a = k.gen()
            sage: a.polynomial()
            alpha
            sage: (a**2 + 1).polynomial('beta')
            beta^2 + 1
            sage: (a**2 + 1).polynomial().parent()
            Univariate Polynomial Ring in alpha over Finite Field of size 3
            sage: (a**2 + 1).polynomial('beta').parent()
            Univariate Polynomial Ring in beta over Finite Field of size 3"""
    @overload
    def polynomial(self) -> Any:
        """FiniteFieldElement_pari_ffelt.polynomial(self, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 918)

        Return the unique representative of ``self`` as a polynomial
        over the prime field whose degree is less than the degree of
        the finite field over its prime field.

        INPUT:

        - ``name`` -- (optional) variable name

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: pol = a.polynomial()
            sage: pol
            a
            sage: parent(pol)
            Univariate Polynomial Ring in a over Finite Field of size 3

        ::

            sage: k = FiniteField(3^4, 'alpha', impl='pari_ffelt')
            sage: a = k.gen()
            sage: a.polynomial()
            alpha
            sage: (a**2 + 1).polynomial('beta')
            beta^2 + 1
            sage: (a**2 + 1).polynomial().parent()
            Univariate Polynomial Ring in alpha over Finite Field of size 3
            sage: (a**2 + 1).polynomial('beta').parent()
            Univariate Polynomial Ring in beta over Finite Field of size 3"""
    @overload
    def polynomial(self) -> Any:
        """FiniteFieldElement_pari_ffelt.polynomial(self, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 918)

        Return the unique representative of ``self`` as a polynomial
        over the prime field whose degree is less than the degree of
        the finite field over its prime field.

        INPUT:

        - ``name`` -- (optional) variable name

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: pol = a.polynomial()
            sage: pol
            a
            sage: parent(pol)
            Univariate Polynomial Ring in a over Finite Field of size 3

        ::

            sage: k = FiniteField(3^4, 'alpha', impl='pari_ffelt')
            sage: a = k.gen()
            sage: a.polynomial()
            alpha
            sage: (a**2 + 1).polynomial('beta')
            beta^2 + 1
            sage: (a**2 + 1).polynomial().parent()
            Univariate Polynomial Ring in alpha over Finite Field of size 3
            sage: (a**2 + 1).polynomial('beta').parent()
            Univariate Polynomial Ring in beta over Finite Field of size 3"""
    @overload
    def polynomial(self) -> Any:
        """FiniteFieldElement_pari_ffelt.polynomial(self, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 918)

        Return the unique representative of ``self`` as a polynomial
        over the prime field whose degree is less than the degree of
        the finite field over its prime field.

        INPUT:

        - ``name`` -- (optional) variable name

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: pol = a.polynomial()
            sage: pol
            a
            sage: parent(pol)
            Univariate Polynomial Ring in a over Finite Field of size 3

        ::

            sage: k = FiniteField(3^4, 'alpha', impl='pari_ffelt')
            sage: a = k.gen()
            sage: a.polynomial()
            alpha
            sage: (a**2 + 1).polynomial('beta')
            beta^2 + 1
            sage: (a**2 + 1).polynomial().parent()
            Univariate Polynomial Ring in alpha over Finite Field of size 3
            sage: (a**2 + 1).polynomial('beta').parent()
            Univariate Polynomial Ring in beta over Finite Field of size 3"""
    def pth_power(self, intk=...) -> Any:
        """FiniteFieldElement_pari_ffelt.pth_power(self, int k=1)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 861)

        Return the `(p^k)`-th power of ``self``, where `p` is the
        characteristic of the field.

        INPUT:

        - ``k`` -- integer (default: 1); must fit in a C ``int``

        Note that if `k` is negative, then this computes the appropriate root.

        TESTS::

            sage: # needs sage.modules
            sage: F.<a> = GF(13^64, impl='pari_ffelt'); F
            Finite Field in a of size 13^64
            sage: x = F.random_element()
            sage: x.pth_power(0) == x
            True
            sage: x.pth_power(1) == x**13
            True
            sage: x.pth_power(2) == x**(13**2)
            True
            sage: x.pth_power(-1)**13 == x
            True

            sage: # needs sage.modules
            sage: F.<a> = GF(127^16, impl='pari_ffelt'); F
            Finite Field in a of size 127^16
            sage: x = F.random_element()
            sage: x.pth_power(0) == x
            True
            sage: x.pth_power(1) == x**127
            True
            sage: x.pth_power(2) == x**(127**2)
            True
            sage: x.pth_power(-1)**127 == x
            True"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """FiniteFieldElement_pari_ffelt.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1023)

        Return a square root of ``self``, if it exists.

        INPUT:

        - ``extend`` -- boolean (default: ``False``)

           .. WARNING::

               This option is not implemented.

        - ``all`` -- boolean (default: ``False``)

        OUTPUT:

        A square root of ``self``, if it exists.  If ``all`` is
        ``True``, a list containing all square roots of ``self``
        (of length zero, one or two) is returned instead.

        If ``extend`` is ``True``, a square root is chosen in an
        extension field if necessary.  If ``extend`` is ``False``, a
        :exc:`ValueError` is raised if the element is not a square in the
        base field.

        .. WARNING::

           The ``extend`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a', impl='pari_ffelt')
            sage: F(2).sqrt()
            4
            sage: F(3).sqrt() in (2*F.gen() + 6, 5*F.gen() + 1)
            True
            sage: F(3).sqrt()**2
            3
            sage: F(4).sqrt(all=True)
            [2, 5]

            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: element is not a square
            sage: K(3).sqrt(all=True)
            []

            sage: K.<a> = GF(3^17, impl='pari_ffelt')
            sage: (a^3 - a - 1).sqrt()
            a^16 + 2*a^15 + a^13 + 2*a^12 + a^10 + 2*a^9 + 2*a^8 + a^7 + a^6 + 2*a^5 + a^4 + 2*a^2 + 2*a + 2"""
    @overload
    def sqrt(self) -> Any:
        """FiniteFieldElement_pari_ffelt.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1023)

        Return a square root of ``self``, if it exists.

        INPUT:

        - ``extend`` -- boolean (default: ``False``)

           .. WARNING::

               This option is not implemented.

        - ``all`` -- boolean (default: ``False``)

        OUTPUT:

        A square root of ``self``, if it exists.  If ``all`` is
        ``True``, a list containing all square roots of ``self``
        (of length zero, one or two) is returned instead.

        If ``extend`` is ``True``, a square root is chosen in an
        extension field if necessary.  If ``extend`` is ``False``, a
        :exc:`ValueError` is raised if the element is not a square in the
        base field.

        .. WARNING::

           The ``extend`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a', impl='pari_ffelt')
            sage: F(2).sqrt()
            4
            sage: F(3).sqrt() in (2*F.gen() + 6, 5*F.gen() + 1)
            True
            sage: F(3).sqrt()**2
            3
            sage: F(4).sqrt(all=True)
            [2, 5]

            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: element is not a square
            sage: K(3).sqrt(all=True)
            []

            sage: K.<a> = GF(3^17, impl='pari_ffelt')
            sage: (a^3 - a - 1).sqrt()
            a^16 + 2*a^15 + a^13 + 2*a^12 + a^10 + 2*a^9 + 2*a^8 + a^7 + a^6 + 2*a^5 + a^4 + 2*a^2 + 2*a + 2"""
    @overload
    def sqrt(self) -> Any:
        """FiniteFieldElement_pari_ffelt.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1023)

        Return a square root of ``self``, if it exists.

        INPUT:

        - ``extend`` -- boolean (default: ``False``)

           .. WARNING::

               This option is not implemented.

        - ``all`` -- boolean (default: ``False``)

        OUTPUT:

        A square root of ``self``, if it exists.  If ``all`` is
        ``True``, a list containing all square roots of ``self``
        (of length zero, one or two) is returned instead.

        If ``extend`` is ``True``, a square root is chosen in an
        extension field if necessary.  If ``extend`` is ``False``, a
        :exc:`ValueError` is raised if the element is not a square in the
        base field.

        .. WARNING::

           The ``extend`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a', impl='pari_ffelt')
            sage: F(2).sqrt()
            4
            sage: F(3).sqrt() in (2*F.gen() + 6, 5*F.gen() + 1)
            True
            sage: F(3).sqrt()**2
            3
            sage: F(4).sqrt(all=True)
            [2, 5]

            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: element is not a square
            sage: K(3).sqrt(all=True)
            []

            sage: K.<a> = GF(3^17, impl='pari_ffelt')
            sage: (a^3 - a - 1).sqrt()
            a^16 + 2*a^15 + a^13 + 2*a^12 + a^10 + 2*a^9 + 2*a^8 + a^7 + a^6 + 2*a^5 + a^4 + 2*a^2 + 2*a + 2"""
    @overload
    def sqrt(self) -> Any:
        """FiniteFieldElement_pari_ffelt.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1023)

        Return a square root of ``self``, if it exists.

        INPUT:

        - ``extend`` -- boolean (default: ``False``)

           .. WARNING::

               This option is not implemented.

        - ``all`` -- boolean (default: ``False``)

        OUTPUT:

        A square root of ``self``, if it exists.  If ``all`` is
        ``True``, a list containing all square roots of ``self``
        (of length zero, one or two) is returned instead.

        If ``extend`` is ``True``, a square root is chosen in an
        extension field if necessary.  If ``extend`` is ``False``, a
        :exc:`ValueError` is raised if the element is not a square in the
        base field.

        .. WARNING::

           The ``extend`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a', impl='pari_ffelt')
            sage: F(2).sqrt()
            4
            sage: F(3).sqrt() in (2*F.gen() + 6, 5*F.gen() + 1)
            True
            sage: F(3).sqrt()**2
            3
            sage: F(4).sqrt(all=True)
            [2, 5]

            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: element is not a square
            sage: K(3).sqrt(all=True)
            []

            sage: K.<a> = GF(3^17, impl='pari_ffelt')
            sage: (a^3 - a - 1).sqrt()
            a^16 + 2*a^15 + a^13 + 2*a^12 + a^10 + 2*a^9 + 2*a^8 + a^7 + a^6 + 2*a^5 + a^4 + 2*a^2 + 2*a + 2"""
    @overload
    def sqrt(self, all=...) -> Any:
        """FiniteFieldElement_pari_ffelt.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1023)

        Return a square root of ``self``, if it exists.

        INPUT:

        - ``extend`` -- boolean (default: ``False``)

           .. WARNING::

               This option is not implemented.

        - ``all`` -- boolean (default: ``False``)

        OUTPUT:

        A square root of ``self``, if it exists.  If ``all`` is
        ``True``, a list containing all square roots of ``self``
        (of length zero, one or two) is returned instead.

        If ``extend`` is ``True``, a square root is chosen in an
        extension field if necessary.  If ``extend`` is ``False``, a
        :exc:`ValueError` is raised if the element is not a square in the
        base field.

        .. WARNING::

           The ``extend`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a', impl='pari_ffelt')
            sage: F(2).sqrt()
            4
            sage: F(3).sqrt() in (2*F.gen() + 6, 5*F.gen() + 1)
            True
            sage: F(3).sqrt()**2
            3
            sage: F(4).sqrt(all=True)
            [2, 5]

            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: element is not a square
            sage: K(3).sqrt(all=True)
            []

            sage: K.<a> = GF(3^17, impl='pari_ffelt')
            sage: (a^3 - a - 1).sqrt()
            a^16 + 2*a^15 + a^13 + 2*a^12 + a^10 + 2*a^9 + 2*a^8 + a^7 + a^6 + 2*a^5 + a^4 + 2*a^2 + 2*a + 2"""
    @overload
    def sqrt(self) -> Any:
        """FiniteFieldElement_pari_ffelt.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1023)

        Return a square root of ``self``, if it exists.

        INPUT:

        - ``extend`` -- boolean (default: ``False``)

           .. WARNING::

               This option is not implemented.

        - ``all`` -- boolean (default: ``False``)

        OUTPUT:

        A square root of ``self``, if it exists.  If ``all`` is
        ``True``, a list containing all square roots of ``self``
        (of length zero, one or two) is returned instead.

        If ``extend`` is ``True``, a square root is chosen in an
        extension field if necessary.  If ``extend`` is ``False``, a
        :exc:`ValueError` is raised if the element is not a square in the
        base field.

        .. WARNING::

           The ``extend`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a', impl='pari_ffelt')
            sage: F(2).sqrt()
            4
            sage: F(3).sqrt() in (2*F.gen() + 6, 5*F.gen() + 1)
            True
            sage: F(3).sqrt()**2
            3
            sage: F(4).sqrt(all=True)
            [2, 5]

            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: element is not a square
            sage: K(3).sqrt(all=True)
            []

            sage: K.<a> = GF(3^17, impl='pari_ffelt')
            sage: (a^3 - a - 1).sqrt()
            a^16 + 2*a^15 + a^13 + 2*a^12 + a^10 + 2*a^9 + 2*a^8 + a^7 + a^6 + 2*a^5 + a^4 + 2*a^2 + 2*a + 2"""
    @overload
    def sqrt(self, all=...) -> Any:
        """FiniteFieldElement_pari_ffelt.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1023)

        Return a square root of ``self``, if it exists.

        INPUT:

        - ``extend`` -- boolean (default: ``False``)

           .. WARNING::

               This option is not implemented.

        - ``all`` -- boolean (default: ``False``)

        OUTPUT:

        A square root of ``self``, if it exists.  If ``all`` is
        ``True``, a list containing all square roots of ``self``
        (of length zero, one or two) is returned instead.

        If ``extend`` is ``True``, a square root is chosen in an
        extension field if necessary.  If ``extend`` is ``False``, a
        :exc:`ValueError` is raised if the element is not a square in the
        base field.

        .. WARNING::

           The ``extend`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a', impl='pari_ffelt')
            sage: F(2).sqrt()
            4
            sage: F(3).sqrt() in (2*F.gen() + 6, 5*F.gen() + 1)
            True
            sage: F(3).sqrt()**2
            3
            sage: F(4).sqrt(all=True)
            [2, 5]

            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: element is not a square
            sage: K(3).sqrt(all=True)
            []

            sage: K.<a> = GF(3^17, impl='pari_ffelt')
            sage: (a^3 - a - 1).sqrt()
            a^16 + 2*a^15 + a^13 + 2*a^12 + a^10 + 2*a^9 + 2*a^8 + a^7 + a^6 + 2*a^5 + a^4 + 2*a^2 + 2*a + 2"""
    @overload
    def sqrt(self) -> Any:
        """FiniteFieldElement_pari_ffelt.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1023)

        Return a square root of ``self``, if it exists.

        INPUT:

        - ``extend`` -- boolean (default: ``False``)

           .. WARNING::

               This option is not implemented.

        - ``all`` -- boolean (default: ``False``)

        OUTPUT:

        A square root of ``self``, if it exists.  If ``all`` is
        ``True``, a list containing all square roots of ``self``
        (of length zero, one or two) is returned instead.

        If ``extend`` is ``True``, a square root is chosen in an
        extension field if necessary.  If ``extend`` is ``False``, a
        :exc:`ValueError` is raised if the element is not a square in the
        base field.

        .. WARNING::

           The ``extend`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a', impl='pari_ffelt')
            sage: F(2).sqrt()
            4
            sage: F(3).sqrt() in (2*F.gen() + 6, 5*F.gen() + 1)
            True
            sage: F(3).sqrt()**2
            3
            sage: F(4).sqrt(all=True)
            [2, 5]

            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: element is not a square
            sage: K(3).sqrt(all=True)
            []

            sage: K.<a> = GF(3^17, impl='pari_ffelt')
            sage: (a^3 - a - 1).sqrt()
            a^16 + 2*a^15 + a^13 + 2*a^12 + a^10 + 2*a^9 + 2*a^8 + a^7 + a^6 + 2*a^5 + a^4 + 2*a^2 + 2*a + 2"""
    def __bool__(self) -> bool:
        """FiniteFieldElement_pari_ffelt.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 755)

        Return ``True`` if ``self`` is nonzero.

        EXAMPLES::

            sage: F.<a> = FiniteField(5^3, impl='pari_ffelt')
            sage: a.is_unit()
            True"""
    def __copy__(self) -> Any:
        """FiniteFieldElement_pari_ffelt.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 570)

        TESTS::

            sage: k.<a> = FiniteField(3^3, impl='pari_ffelt')
            sage: a
            a
            sage: b = copy(a); b
            a
            sage: a is b
            True"""
    def __deepcopy__(self, memo) -> Any:
        """FiniteFieldElement_pari_ffelt.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 585)

        TESTS::

            sage: k.<a> = FiniteField(3^3, impl='pari_ffelt')
            sage: a
            a
            sage: b = deepcopy(a); b
            a
            sage: a is b
            True"""
    def __float__(self) -> Any:
        """FiniteFieldElement_pari_ffelt.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1284)

        Lift to a python float, if possible.

        EXAMPLES::

            sage: k.<a> = GF(3^17, impl='pari_ffelt')
            sage: b = k(2)
            sage: float(b)
            2.0"""
    def __hash__(self) -> Any:
        """FiniteFieldElement_pari_ffelt.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 544)

        Return the hash of ``self``.  This is by definition equal to
        the hash of ``self.polynomial()``.

        EXAMPLES::

            sage: k.<a> = GF(3^15, impl='pari_ffelt')
            sage: R = GF(3)['a']; aa = R.gen()
            sage: hash(a^2 + 1) == hash(aa^2 + 1)
            True"""
    def __int__(self) -> Any:
        """FiniteFieldElement_pari_ffelt.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1267)

        Lift to a python int, if possible.

        EXAMPLES::

            sage: k.<a> = GF(3^17, impl='pari_ffelt')
            sage: b = k(2)
            sage: int(b)
            2
            sage: int(a)
            Traceback (most recent call last):
            ...
            ValueError: element is not in the prime field"""
    def __invert__(self) -> Any:
        """FiniteFieldElement_pari_ffelt.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 796)

        Return the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: k.<a> = FiniteField(3^2, impl='pari_ffelt')
            sage: ~a
            a + 2
            sage: (a+1)*a
            2*a + 1
            sage: ~((2*a)/a)
            2"""
    def __neg__(self) -> Any:
        """FiniteFieldElement_pari_ffelt.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 781)

        Negation.

        EXAMPLES::

            sage: k.<a> = GF(3^17, impl='pari_ffelt')
            sage: -a
            2*a"""
    @overload
    def __pari__(self, var=...) -> Any:
        """FiniteFieldElement_pari_ffelt.__pari__(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1297)

        Return a PARI object representing ``self``.

        EXAMPLES::

            sage: k.<a> = FiniteField(3^3, impl='pari_ffelt')
            sage: b = a**2 + 2*a + 1
            sage: b.__pari__()
            a^2 + 2*a + 1"""
    @overload
    def __pari__(self) -> Any:
        """FiniteFieldElement_pari_ffelt.__pari__(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 1297)

        Return a PARI object representing ``self``.

        EXAMPLES::

            sage: k.<a> = FiniteField(3^3, impl='pari_ffelt')
            sage: b = a**2 + 2*a + 1
            sage: b.__pari__()
            a^2 + 2*a + 1"""
    def __pos__(self) -> Any:
        """FiniteFieldElement_pari_ffelt.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 769)

        Unitary positive operator...

        EXAMPLES::

            sage: k.<a> = GF(3^17, impl='pari_ffelt')
            sage: +a
            a"""
    def __pow__(self, FiniteFieldElement_pari_ffeltself, exp, other) -> Any:
        """FiniteFieldElement_pari_ffelt.__pow__(FiniteFieldElement_pari_ffelt self, exp, other)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 817)

        Exponentiation.

        TESTS::

            sage: K.<a> = GF(5^10, impl='pari_ffelt')
            sage: n = (2*a)/a
            sage: n^-15
            2

        Large exponents are not a problem::

            sage: e = 3^10000
            sage: a^e
            2*a^9 + a^5 + 4*a^4 + 4*a^3 + a^2 + 3*a
            sage: a^(e % (5^10 - 1))
            2*a^9 + a^5 + 4*a^4 + 4*a^3 + a^2 + 3*a

        The exponent is converted to an integer (see :issue:`16540`)::

            sage: q = 11^23
            sage: F.<a> = FiniteField(q)
            sage: a^Mod(1, q - 1)
            a

        .. WARNING::

            For efficiency reasons, we do not verify that the
            exponentiation is well defined before converting the
            exponent to an integer.  This means that ``a^Mod(1, n)``
            returns `a` even if `n` is not a multiple of the
            multiplicative order of `a`."""
    def __reduce__(self) -> Any:
        """FiniteFieldElement_pari_ffelt.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_pari_ffelt.pyx (starting at line 558)

        For pickling.

        TESTS::

            sage: K.<a> = FiniteField(10007^10, impl='pari_ffelt')
            sage: loads(a.dumps()) == a
            True"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
