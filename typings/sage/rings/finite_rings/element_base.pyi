import _cython_3_2_1
import sage.structure.element
import sage.structure.sage_object
from sage.categories.category import ZZ as ZZ
from sage.rings.integer import Integer as Integer
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

is_FiniteFieldElement: _cython_3_2_1.cython_function_or_method

class Cache_base(sage.structure.sage_object.SageObject):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def fetch_int(self, number) -> FinitePolyExtElement:
        """Cache_base.fetch_int(self, number) -> FinitePolyExtElement

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 1160)

        Given an integer less than `p^n` with base `2`
        representation `a_0 + a_1 \\cdot 2 + \\cdots + a_k 2^k`, this returns
        `a_0 + a_1 x + \\cdots + a_k x^k`, where `x` is the
        generator of this finite field.

        EXAMPLES::

            sage: k.<a> = GF(2^48)
            sage: k._cache.fetch_int(2^33 + 2 + 1)                                      # needs sage.libs.ntl
            a^33 + a + 1"""

class FinitePolyExtElement(FiniteRingElement):
    """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 193)

        Elements represented as polynomials modulo a given ideal.

        TESTS::

            sage: k.<a> = GF(64)
            sage: TestSuite(a).run()
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def additive_order(self) -> Any:
        """FinitePolyExtElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 742)

        Return the additive order of this finite field element.

        EXAMPLES::

            sage: k.<a> = FiniteField(2^12, 'a')
            sage: b = a^3 + a + 1
            sage: b.additive_order()
            2
            sage: k(0).additive_order()
            1"""
    @overload
    def additive_order(self) -> Any:
        """FinitePolyExtElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 742)

        Return the additive order of this finite field element.

        EXAMPLES::

            sage: k.<a> = FiniteField(2^12, 'a')
            sage: b = a^3 + a + 1
            sage: b.additive_order()
            2
            sage: k(0).additive_order()
            1"""
    @overload
    def additive_order(self) -> Any:
        """FinitePolyExtElement.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 742)

        Return the additive order of this finite field element.

        EXAMPLES::

            sage: k.<a> = FiniteField(2^12, 'a')
            sage: b = a^3 + a + 1
            sage: b.additive_order()
            2
            sage: k(0).additive_order()
            1"""
    def charpoly(self, var=..., algorithm=...) -> Any:
        '''FinitePolyExtElement.charpoly(self, var=\'x\', algorithm=\'pari\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 611)

        Return the characteristic polynomial of ``self`` as a polynomial with given variable.

        INPUT:

        - ``var`` -- string (default: ``\'x\'``)

        - ``algorithm`` -- string (default: ``\'pari\'``):

          - ``\'pari\'`` -- use pari\'s charpoly

          - ``\'matrix\'`` -- return the charpoly computed from the matrix of
            left multiplication by ``self``

        The result is not cached.

        EXAMPLES::

            sage: from sage.rings.finite_rings.element_base import FinitePolyExtElement
            sage: k.<a> = FiniteField(19^2)
            sage: parent(a)
            Finite Field in a of size 19^2
            sage: b = a**20
            sage: p = FinitePolyExtElement.charpoly(b, "x", algorithm=\'pari\')
            sage: q = FinitePolyExtElement.charpoly(b, "x", algorithm=\'matrix\')         # needs sage.modules
            sage: q == p                                                                # needs sage.modules
            True
            sage: p
            x^2 + 15*x + 4
            sage: factor(p)
            (x + 17)^2
            sage: b.minpoly(\'x\')
            x + 17'''
    @overload
    def conjugate(self) -> Any:
        """FinitePolyExtElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 1023)

        This methods returns the result of the Frobenius morphism
        in the case where the field is a quadratic extension, say
        `GF(q^2)`, where `q=p^k` is a prime power and `p` the
        characteristic of the field.

        OUTPUT:

        Instance of this class representing the image under
        the Frobenius morphisms.

        EXAMPLES::

            sage: F.<a> = GF(16)
            sage: b = a.conjugate(); b
            a + 1
            sage: a == b.conjugate()
            True

            sage: F.<a> = GF(27)
            sage: a.conjugate()
            Traceback (most recent call last):
            ...
            TypeError: cardinality of the field must be a square number

        TESTS:

        Check that :issue:`26761` is fixed::

            sage: # needs sage.libs.gap
            sage: G32 = GU(3,2)
            sage: g1, g2 = G32.gens()
            sage: m1 = g1.matrix()
            sage: m1.is_unitary()
            True
            sage: G32(m1) == g1
            True"""
    @overload
    def conjugate(self) -> Any:
        """FinitePolyExtElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 1023)

        This methods returns the result of the Frobenius morphism
        in the case where the field is a quadratic extension, say
        `GF(q^2)`, where `q=p^k` is a prime power and `p` the
        characteristic of the field.

        OUTPUT:

        Instance of this class representing the image under
        the Frobenius morphisms.

        EXAMPLES::

            sage: F.<a> = GF(16)
            sage: b = a.conjugate(); b
            a + 1
            sage: a == b.conjugate()
            True

            sage: F.<a> = GF(27)
            sage: a.conjugate()
            Traceback (most recent call last):
            ...
            TypeError: cardinality of the field must be a square number

        TESTS:

        Check that :issue:`26761` is fixed::

            sage: # needs sage.libs.gap
            sage: G32 = GU(3,2)
            sage: g1, g2 = G32.gens()
            sage: m1 = g1.matrix()
            sage: m1.is_unitary()
            True
            sage: G32(m1) == g1
            True"""
    @overload
    def conjugate(self) -> Any:
        """FinitePolyExtElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 1023)

        This methods returns the result of the Frobenius morphism
        in the case where the field is a quadratic extension, say
        `GF(q^2)`, where `q=p^k` is a prime power and `p` the
        characteristic of the field.

        OUTPUT:

        Instance of this class representing the image under
        the Frobenius morphisms.

        EXAMPLES::

            sage: F.<a> = GF(16)
            sage: b = a.conjugate(); b
            a + 1
            sage: a == b.conjugate()
            True

            sage: F.<a> = GF(27)
            sage: a.conjugate()
            Traceback (most recent call last):
            ...
            TypeError: cardinality of the field must be a square number

        TESTS:

        Check that :issue:`26761` is fixed::

            sage: # needs sage.libs.gap
            sage: G32 = GU(3,2)
            sage: g1, g2 = G32.gens()
            sage: m1 = g1.matrix()
            sage: m1.is_unitary()
            True
            sage: G32(m1) == g1
            True"""
    @overload
    def conjugate(self) -> Any:
        """FinitePolyExtElement.conjugate(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 1023)

        This methods returns the result of the Frobenius morphism
        in the case where the field is a quadratic extension, say
        `GF(q^2)`, where `q=p^k` is a prime power and `p` the
        characteristic of the field.

        OUTPUT:

        Instance of this class representing the image under
        the Frobenius morphisms.

        EXAMPLES::

            sage: F.<a> = GF(16)
            sage: b = a.conjugate(); b
            a + 1
            sage: a == b.conjugate()
            True

            sage: F.<a> = GF(27)
            sage: a.conjugate()
            Traceback (most recent call last):
            ...
            TypeError: cardinality of the field must be a square number

        TESTS:

        Check that :issue:`26761` is fixed::

            sage: # needs sage.libs.gap
            sage: G32 = GU(3,2)
            sage: g1, g2 = G32.gens()
            sage: m1 = g1.matrix()
            sage: m1.is_unitary()
            True
            sage: G32(m1) == g1
            True"""
    def frobenius(self, *args, **kwargs):
        """FinitePolyExtElement.pth_power(self, int k=1)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 967)

        Return the `(p^k)`-th power of self, where `p` is the
        characteristic of the field.

        INPUT:

        - ``k`` -- integer (default: 1, must fit in C int type)

        Note that if `k` is negative, then this computes the appropriate root.

        EXAMPLES::

            sage: F.<a> = GF(29^2)
            sage: z = a^2 + 5*a + 1
            sage: z.pth_power()
            19*a + 20
            sage: z.pth_power(10)
            10*a + 28
            sage: z.pth_power(-10) == z
            True
            sage: F.<b> = GF(2^12)
            sage: y = b^3 + b + 1
            sage: y == (y.pth_power(-3))^(2^3)
            True
            sage: y.pth_power(2)
            b^7 + b^6 + b^5 + b^4 + b^3 + b"""
    @overload
    def is_square(self) -> Any:
        """FinitePolyExtElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 759)

        Return ``True`` if and only if this element is a perfect square.

        EXAMPLES::

            sage: k.<a> = FiniteField(9, impl='givaro', modulus='primitive')            # needs sage.libs.linbox
            sage: a.is_square()                                                         # needs sage.libs.linbox
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.linbox
            True
            sage: k.<a> = FiniteField(4, impl='ntl', modulus='primitive')               # needs sage.libs.ntl
            sage: (a**2).is_square()                                                    # needs sage.libs.ntl
            True
            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt', modulus='primitive')     # needs sage.libs.pari
            sage: a.is_square()                                                         # needs sage.libs.pari
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.pari
            True

        ::

            sage: k(0).is_square()                                                      # needs sage.libs.linbox
            True"""
    @overload
    def is_square(self) -> Any:
        """FinitePolyExtElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 759)

        Return ``True`` if and only if this element is a perfect square.

        EXAMPLES::

            sage: k.<a> = FiniteField(9, impl='givaro', modulus='primitive')            # needs sage.libs.linbox
            sage: a.is_square()                                                         # needs sage.libs.linbox
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.linbox
            True
            sage: k.<a> = FiniteField(4, impl='ntl', modulus='primitive')               # needs sage.libs.ntl
            sage: (a**2).is_square()                                                    # needs sage.libs.ntl
            True
            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt', modulus='primitive')     # needs sage.libs.pari
            sage: a.is_square()                                                         # needs sage.libs.pari
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.pari
            True

        ::

            sage: k(0).is_square()                                                      # needs sage.libs.linbox
            True"""
    @overload
    def is_square(self) -> Any:
        """FinitePolyExtElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 759)

        Return ``True`` if and only if this element is a perfect square.

        EXAMPLES::

            sage: k.<a> = FiniteField(9, impl='givaro', modulus='primitive')            # needs sage.libs.linbox
            sage: a.is_square()                                                         # needs sage.libs.linbox
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.linbox
            True
            sage: k.<a> = FiniteField(4, impl='ntl', modulus='primitive')               # needs sage.libs.ntl
            sage: (a**2).is_square()                                                    # needs sage.libs.ntl
            True
            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt', modulus='primitive')     # needs sage.libs.pari
            sage: a.is_square()                                                         # needs sage.libs.pari
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.pari
            True

        ::

            sage: k(0).is_square()                                                      # needs sage.libs.linbox
            True"""
    @overload
    def is_square(self) -> Any:
        """FinitePolyExtElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 759)

        Return ``True`` if and only if this element is a perfect square.

        EXAMPLES::

            sage: k.<a> = FiniteField(9, impl='givaro', modulus='primitive')            # needs sage.libs.linbox
            sage: a.is_square()                                                         # needs sage.libs.linbox
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.linbox
            True
            sage: k.<a> = FiniteField(4, impl='ntl', modulus='primitive')               # needs sage.libs.ntl
            sage: (a**2).is_square()                                                    # needs sage.libs.ntl
            True
            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt', modulus='primitive')     # needs sage.libs.pari
            sage: a.is_square()                                                         # needs sage.libs.pari
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.pari
            True

        ::

            sage: k(0).is_square()                                                      # needs sage.libs.linbox
            True"""
    @overload
    def is_square(self) -> Any:
        """FinitePolyExtElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 759)

        Return ``True`` if and only if this element is a perfect square.

        EXAMPLES::

            sage: k.<a> = FiniteField(9, impl='givaro', modulus='primitive')            # needs sage.libs.linbox
            sage: a.is_square()                                                         # needs sage.libs.linbox
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.linbox
            True
            sage: k.<a> = FiniteField(4, impl='ntl', modulus='primitive')               # needs sage.libs.ntl
            sage: (a**2).is_square()                                                    # needs sage.libs.ntl
            True
            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt', modulus='primitive')     # needs sage.libs.pari
            sage: a.is_square()                                                         # needs sage.libs.pari
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.pari
            True

        ::

            sage: k(0).is_square()                                                      # needs sage.libs.linbox
            True"""
    @overload
    def is_square(self) -> Any:
        """FinitePolyExtElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 759)

        Return ``True`` if and only if this element is a perfect square.

        EXAMPLES::

            sage: k.<a> = FiniteField(9, impl='givaro', modulus='primitive')            # needs sage.libs.linbox
            sage: a.is_square()                                                         # needs sage.libs.linbox
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.linbox
            True
            sage: k.<a> = FiniteField(4, impl='ntl', modulus='primitive')               # needs sage.libs.ntl
            sage: (a**2).is_square()                                                    # needs sage.libs.ntl
            True
            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt', modulus='primitive')     # needs sage.libs.pari
            sage: a.is_square()                                                         # needs sage.libs.pari
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.pari
            True

        ::

            sage: k(0).is_square()                                                      # needs sage.libs.linbox
            True"""
    @overload
    def is_square(self) -> Any:
        """FinitePolyExtElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 759)

        Return ``True`` if and only if this element is a perfect square.

        EXAMPLES::

            sage: k.<a> = FiniteField(9, impl='givaro', modulus='primitive')            # needs sage.libs.linbox
            sage: a.is_square()                                                         # needs sage.libs.linbox
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.linbox
            True
            sage: k.<a> = FiniteField(4, impl='ntl', modulus='primitive')               # needs sage.libs.ntl
            sage: (a**2).is_square()                                                    # needs sage.libs.ntl
            True
            sage: k.<a> = FiniteField(17^5, impl='pari_ffelt', modulus='primitive')     # needs sage.libs.pari
            sage: a.is_square()                                                         # needs sage.libs.pari
            False
            sage: (a**2).is_square()                                                    # needs sage.libs.pari
            True

        ::

            sage: k(0).is_square()                                                      # needs sage.libs.linbox
            True"""
    @overload
    def list(self) -> Any:
        """FinitePolyExtElement.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 331)

        Return the list of coefficients (in little-endian) of this
        finite field element when written as a polynomial in the
        generator.

        Equivalent to calling ``list()`` on this element.

        EXAMPLES::

            sage: x = polygen(GF(71))
            sage: F.<u> = GF(71^7, modulus=x^7 + x + 1)
            sage: a = 3 + u + 3*u^2 + 3*u^3 + 7*u^4
            sage: a.list()
            [3, 1, 3, 3, 7, 0, 0]
            sage: a.list() == list(a) == [a[i] for i in range(F.degree())]
            True

        The coefficients returned are those of a fully reduced
        representative of the finite field element::

            sage: b = u^777
            sage: b.list()
            [9, 69, 4, 27, 40, 10, 56]
            sage: (u.polynomial()^777).list()
            [0, 0, 0, 0, ..., 0, 1]

        TESTS::

            sage: # needs sage.modules
            sage: R.<x> = GF(17)[]
            sage: F.<t> = GF(17^60)
            sage: a = F.random_element()
            sage: a == R(a.list())(t)
            True
            sage: list(a) == a.list()
            True"""
    @overload
    def list(self) -> Any:
        """FinitePolyExtElement.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 331)

        Return the list of coefficients (in little-endian) of this
        finite field element when written as a polynomial in the
        generator.

        Equivalent to calling ``list()`` on this element.

        EXAMPLES::

            sage: x = polygen(GF(71))
            sage: F.<u> = GF(71^7, modulus=x^7 + x + 1)
            sage: a = 3 + u + 3*u^2 + 3*u^3 + 7*u^4
            sage: a.list()
            [3, 1, 3, 3, 7, 0, 0]
            sage: a.list() == list(a) == [a[i] for i in range(F.degree())]
            True

        The coefficients returned are those of a fully reduced
        representative of the finite field element::

            sage: b = u^777
            sage: b.list()
            [9, 69, 4, 27, 40, 10, 56]
            sage: (u.polynomial()^777).list()
            [0, 0, 0, 0, ..., 0, 1]

        TESTS::

            sage: # needs sage.modules
            sage: R.<x> = GF(17)[]
            sage: F.<t> = GF(17^60)
            sage: a = F.random_element()
            sage: a == R(a.list())(t)
            True
            sage: list(a) == a.list()
            True"""
    @overload
    def list(self) -> Any:
        """FinitePolyExtElement.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 331)

        Return the list of coefficients (in little-endian) of this
        finite field element when written as a polynomial in the
        generator.

        Equivalent to calling ``list()`` on this element.

        EXAMPLES::

            sage: x = polygen(GF(71))
            sage: F.<u> = GF(71^7, modulus=x^7 + x + 1)
            sage: a = 3 + u + 3*u^2 + 3*u^3 + 7*u^4
            sage: a.list()
            [3, 1, 3, 3, 7, 0, 0]
            sage: a.list() == list(a) == [a[i] for i in range(F.degree())]
            True

        The coefficients returned are those of a fully reduced
        representative of the finite field element::

            sage: b = u^777
            sage: b.list()
            [9, 69, 4, 27, 40, 10, 56]
            sage: (u.polynomial()^777).list()
            [0, 0, 0, 0, ..., 0, 1]

        TESTS::

            sage: # needs sage.modules
            sage: R.<x> = GF(17)[]
            sage: F.<t> = GF(17^60)
            sage: a = F.random_element()
            sage: a == R(a.list())(t)
            True
            sage: list(a) == a.list()
            True"""
    @overload
    def list(self, a) -> Any:
        """FinitePolyExtElement.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 331)

        Return the list of coefficients (in little-endian) of this
        finite field element when written as a polynomial in the
        generator.

        Equivalent to calling ``list()`` on this element.

        EXAMPLES::

            sage: x = polygen(GF(71))
            sage: F.<u> = GF(71^7, modulus=x^7 + x + 1)
            sage: a = 3 + u + 3*u^2 + 3*u^3 + 7*u^4
            sage: a.list()
            [3, 1, 3, 3, 7, 0, 0]
            sage: a.list() == list(a) == [a[i] for i in range(F.degree())]
            True

        The coefficients returned are those of a fully reduced
        representative of the finite field element::

            sage: b = u^777
            sage: b.list()
            [9, 69, 4, 27, 40, 10, 56]
            sage: (u.polynomial()^777).list()
            [0, 0, 0, 0, ..., 0, 1]

        TESTS::

            sage: # needs sage.modules
            sage: R.<x> = GF(17)[]
            sage: F.<t> = GF(17^60)
            sage: a = F.random_element()
            sage: a == R(a.list())(t)
            True
            sage: list(a) == a.list()
            True"""
    @overload
    def list(self) -> Any:
        """FinitePolyExtElement.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 331)

        Return the list of coefficients (in little-endian) of this
        finite field element when written as a polynomial in the
        generator.

        Equivalent to calling ``list()`` on this element.

        EXAMPLES::

            sage: x = polygen(GF(71))
            sage: F.<u> = GF(71^7, modulus=x^7 + x + 1)
            sage: a = 3 + u + 3*u^2 + 3*u^3 + 7*u^4
            sage: a.list()
            [3, 1, 3, 3, 7, 0, 0]
            sage: a.list() == list(a) == [a[i] for i in range(F.degree())]
            True

        The coefficients returned are those of a fully reduced
        representative of the finite field element::

            sage: b = u^777
            sage: b.list()
            [9, 69, 4, 27, 40, 10, 56]
            sage: (u.polynomial()^777).list()
            [0, 0, 0, 0, ..., 0, 1]

        TESTS::

            sage: # needs sage.modules
            sage: R.<x> = GF(17)[]
            sage: F.<t> = GF(17^60)
            sage: a = F.random_element()
            sage: a == R(a.list())(t)
            True
            sage: list(a) == a.list()
            True"""
    @overload
    def list(self) -> Any:
        """FinitePolyExtElement.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 331)

        Return the list of coefficients (in little-endian) of this
        finite field element when written as a polynomial in the
        generator.

        Equivalent to calling ``list()`` on this element.

        EXAMPLES::

            sage: x = polygen(GF(71))
            sage: F.<u> = GF(71^7, modulus=x^7 + x + 1)
            sage: a = 3 + u + 3*u^2 + 3*u^3 + 7*u^4
            sage: a.list()
            [3, 1, 3, 3, 7, 0, 0]
            sage: a.list() == list(a) == [a[i] for i in range(F.degree())]
            True

        The coefficients returned are those of a fully reduced
        representative of the finite field element::

            sage: b = u^777
            sage: b.list()
            [9, 69, 4, 27, 40, 10, 56]
            sage: (u.polynomial()^777).list()
            [0, 0, 0, 0, ..., 0, 1]

        TESTS::

            sage: # needs sage.modules
            sage: R.<x> = GF(17)[]
            sage: F.<t> = GF(17^60)
            sage: a = F.random_element()
            sage: a == R(a.list())(t)
            True
            sage: list(a) == a.list()
            True"""
    @overload
    def list(self) -> Any:
        """FinitePolyExtElement.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 331)

        Return the list of coefficients (in little-endian) of this
        finite field element when written as a polynomial in the
        generator.

        Equivalent to calling ``list()`` on this element.

        EXAMPLES::

            sage: x = polygen(GF(71))
            sage: F.<u> = GF(71^7, modulus=x^7 + x + 1)
            sage: a = 3 + u + 3*u^2 + 3*u^3 + 7*u^4
            sage: a.list()
            [3, 1, 3, 3, 7, 0, 0]
            sage: a.list() == list(a) == [a[i] for i in range(F.degree())]
            True

        The coefficients returned are those of a fully reduced
        representative of the finite field element::

            sage: b = u^777
            sage: b.list()
            [9, 69, 4, 27, 40, 10, 56]
            sage: (u.polynomial()^777).list()
            [0, 0, 0, 0, ..., 0, 1]

        TESTS::

            sage: # needs sage.modules
            sage: R.<x> = GF(17)[]
            sage: F.<t> = GF(17^60)
            sage: a = F.random_element()
            sage: a == R(a.list())(t)
            True
            sage: list(a) == a.list()
            True"""
    @overload
    def list(self, a) -> Any:
        """FinitePolyExtElement.list(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 331)

        Return the list of coefficients (in little-endian) of this
        finite field element when written as a polynomial in the
        generator.

        Equivalent to calling ``list()`` on this element.

        EXAMPLES::

            sage: x = polygen(GF(71))
            sage: F.<u> = GF(71^7, modulus=x^7 + x + 1)
            sage: a = 3 + u + 3*u^2 + 3*u^3 + 7*u^4
            sage: a.list()
            [3, 1, 3, 3, 7, 0, 0]
            sage: a.list() == list(a) == [a[i] for i in range(F.degree())]
            True

        The coefficients returned are those of a fully reduced
        representative of the finite field element::

            sage: b = u^777
            sage: b.list()
            [9, 69, 4, 27, 40, 10, 56]
            sage: (u.polynomial()^777).list()
            [0, 0, 0, 0, ..., 0, 1]

        TESTS::

            sage: # needs sage.modules
            sage: R.<x> = GF(17)[]
            sage: F.<t> = GF(17^60)
            sage: a = F.random_element()
            sage: a == R(a.list())(t)
            True
            sage: list(a) == a.list()
            True"""
    def matrix(self, reverse=...) -> Any:
        """FinitePolyExtElement.matrix(self, reverse=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 472)

        Return the matrix of left multiplication by the element on
        the power basis `1, x, x^2, \\ldots, x^{d-1}` for the field
        extension.

        Thus the \\emph{columns} of this matrix give the images
        of each of the `x^i`.

        INPUT:

        - ``reverse`` -- if ``True``, act on vectors in reversed order

        EXAMPLES::

            sage: # needs sage.modules
            sage: k.<a> = GF(2^4)
            sage: b = k.random_element()
            sage: vector(a*b) == a.matrix() * vector(b)
            True
            sage: (a*b)._vector_(reverse=True) == a.matrix(reverse=True) * b._vector_(reverse=True)
            True"""
    def minimal_polynomial(self, var=...) -> Any:
        '''FinitePolyExtElement.minimal_polynomial(self, var=\'x\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 275)

        Return the minimal polynomial of this element
        (over the corresponding prime subfield).

        EXAMPLES::

            sage: k.<a> = FiniteField(3^4)
            sage: parent(a)
            Finite Field in a of size 3^4
            sage: b=a**20;p=charpoly(b,"y");p
            y^4 + 2*y^2 + 1
            sage: factor(p)
            (y^2 + 1)^2
            sage: b.minimal_polynomial(\'y\')
            y^2 + 1'''
    def minpoly(self, var=..., algorithm=...) -> Any:
        '''FinitePolyExtElement.minpoly(self, var=\'x\', algorithm=\'pari\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 228)

        Return the minimal polynomial of this element
        (over the corresponding prime subfield).

        INPUT:

        - ``var`` -- string (default: ``\'x\'``)

        - ``algorithm`` -- string (default: ``\'pari\'``):

          - ``\'pari\'`` -- use pari\'s minpoly

          - ``\'matrix\'`` -- return the minpoly computed from the matrix of
            left multiplication by self

        EXAMPLES::

            sage: from sage.rings.finite_rings.element_base import FinitePolyExtElement
            sage: k.<a> = FiniteField(19^2)
            sage: parent(a)
            Finite Field in a of size 19^2
            sage: b=a**20
            sage: p=FinitePolyExtElement.minpoly(b,"x", algorithm=\'pari\')
            sage: q=FinitePolyExtElement.minpoly(b,"x", algorithm=\'matrix\')
            sage: q == p
            True
            sage: p
            x + 17'''
    @overload
    def multiplicative_order(self) -> Any:
        """FinitePolyExtElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 711)

        Return the multiplicative order of this field element.

        EXAMPLES::

            sage: S.<a> = GF(5^3); S
            Finite Field in a of size 5^3
            sage: a.multiplicative_order()
            124
            sage: (a^8).multiplicative_order()
            31
            sage: S(0).multiplicative_order()
            Traceback (most recent call last):
            ...
            ArithmeticError: Multiplicative order of 0 not defined."""
    @overload
    def multiplicative_order(self) -> Any:
        """FinitePolyExtElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 711)

        Return the multiplicative order of this field element.

        EXAMPLES::

            sage: S.<a> = GF(5^3); S
            Finite Field in a of size 5^3
            sage: a.multiplicative_order()
            124
            sage: (a^8).multiplicative_order()
            31
            sage: S(0).multiplicative_order()
            Traceback (most recent call last):
            ...
            ArithmeticError: Multiplicative order of 0 not defined."""
    @overload
    def multiplicative_order(self) -> Any:
        """FinitePolyExtElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 711)

        Return the multiplicative order of this field element.

        EXAMPLES::

            sage: S.<a> = GF(5^3); S
            Finite Field in a of size 5^3
            sage: a.multiplicative_order()
            124
            sage: (a^8).multiplicative_order()
            31
            sage: S(0).multiplicative_order()
            Traceback (most recent call last):
            ...
            ArithmeticError: Multiplicative order of 0 not defined."""
    @overload
    def multiplicative_order(self) -> Any:
        """FinitePolyExtElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 711)

        Return the multiplicative order of this field element.

        EXAMPLES::

            sage: S.<a> = GF(5^3); S
            Finite Field in a of size 5^3
            sage: a.multiplicative_order()
            124
            sage: (a^8).multiplicative_order()
            31
            sage: S(0).multiplicative_order()
            Traceback (most recent call last):
            ...
            ArithmeticError: Multiplicative order of 0 not defined."""
    @overload
    def norm(self) -> Any:
        """FinitePolyExtElement.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 656)

        Return the norm of ``self`` down to the prime subfield.

        This is the product of the Galois conjugates of ``self``.

        EXAMPLES::

            sage: S.<b> = GF(5^2); S
            Finite Field in b of size 5^2
            sage: b.norm()
            2
            sage: b.charpoly('t')
            t^2 + 4*t + 2

        Next we consider a cubic extension::

            sage: S.<a> = GF(5^3); S
            Finite Field in a of size 5^3
            sage: a.norm()
            2
            sage: a.charpoly('t')
            t^3 + 3*t + 3
            sage: a * a^5 * (a^25)
            2"""
    @overload
    def norm(self) -> Any:
        """FinitePolyExtElement.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 656)

        Return the norm of ``self`` down to the prime subfield.

        This is the product of the Galois conjugates of ``self``.

        EXAMPLES::

            sage: S.<b> = GF(5^2); S
            Finite Field in b of size 5^2
            sage: b.norm()
            2
            sage: b.charpoly('t')
            t^2 + 4*t + 2

        Next we consider a cubic extension::

            sage: S.<a> = GF(5^3); S
            Finite Field in a of size 5^3
            sage: a.norm()
            2
            sage: a.charpoly('t')
            t^3 + 3*t + 3
            sage: a * a^5 * (a^25)
            2"""
    @overload
    def norm(self) -> Any:
        """FinitePolyExtElement.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 656)

        Return the norm of ``self`` down to the prime subfield.

        This is the product of the Galois conjugates of ``self``.

        EXAMPLES::

            sage: S.<b> = GF(5^2); S
            Finite Field in b of size 5^2
            sage: b.norm()
            2
            sage: b.charpoly('t')
            t^2 + 4*t + 2

        Next we consider a cubic extension::

            sage: S.<a> = GF(5^3); S
            Finite Field in a of size 5^3
            sage: a.norm()
            2
            sage: a.charpoly('t')
            t^3 + 3*t + 3
            sage: a * a^5 * (a^25)
            2"""
    def nth_root(self, n, extend=..., all=..., algorithm=..., cunningham=...) -> Any:
        """FinitePolyExtElement.nth_root(self, n, extend=False, all=False, algorithm=None, cunningham=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 846)

        Return an `n`-th root of ``self``.

        INPUT:

        - ``n`` -- integer `\\geq 1`

        - ``extend`` -- boolean (default: ``False``); if ``True``, return an
          `n`-th root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the root is not in the base ring.  Warning:
          this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all `n`-th
          roots of ``self``, instead of just one

        - ``algorithm`` -- string (default: ``None``); ``'Johnston'`` is the
          only currently supported option.  For IntegerMod elements, the problem
          is reduced to the prime modulus case using CRT and `p`-adic logs,
          and then this algorithm used.

        OUTPUT:

        If ``self`` has an `n`-th root, returns one (if ``all`` is ``False``) or a
        list of all of them (if ``all`` is ``True``).
        Otherwise, raises a :exc:`ValueError` (if ``extend`` is ``False``)
        or a :exc:`NotImplementedError` (if ``extend`` is ``True``).

        .. warning::

           The ``extend`` option is not implemented (yet).

        EXAMPLES::

            sage: K = GF(31)
            sage: a = K(22)
            sage: K(22).nth_root(7)
            13
            sage: K(25).nth_root(5)
            5
            sage: K(23).nth_root(3)
            29

            sage: K.<a> = GF(625)
            sage: (3*a^2+a+1).nth_root(13)**13
            3*a^2 + a + 1

            sage: k.<a> = GF(29^2)
            sage: b = a^2 + 5*a + 1
            sage: b.nth_root(11)
            3*a + 20
            sage: b.nth_root(5)
            Traceback (most recent call last):
            ...
            ValueError: no nth root
            sage: b.nth_root(5, all = True)
            []
            sage: b.nth_root(3, all = True)
            [14*a + 18, 10*a + 13, 5*a + 27]

            sage: k.<a> = GF(29^5)
            sage: b = a^2 + 5*a + 1
            sage: b.nth_root(5)
            19*a^4 + 2*a^3 + 2*a^2 + 16*a + 3
            sage: b.nth_root(7)
            Traceback (most recent call last):
            ...
            ValueError: no nth root
            sage: b.nth_root(4, all=True)
            []

        TESTS::

            sage: for p in [2,3,5,7,11]:  # long time, random because of PARI warnings
            ....:     for n in [2,5,10]:
            ....:         q = p^n
            ....:         K.<a> = GF(q)
            ....:         for r in (q-1).divisors():
            ....:             if r == 1: continue
            ....:             x = K.random_element()
            ....:             y = x^r
            ....:             assert y.nth_root(r)^r == y
            ....:             assert (y^41).nth_root(41*r)^(41*r) == y^41
            ....:             assert (y^307).nth_root(307*r)^(307*r) == y^307
            sage: k.<a> = GF(4)
            sage: a.nth_root(0,all=True)
            []
            sage: k(1).nth_root(0,all=True)
            [a, a + 1, 1]

        ALGORITHM:

        The default is currently an algorithm described in [Joh1999]_.

        AUTHOR:

        - David Roe (2010-02-13)"""
    @overload
    def pth_power(self, intk=...) -> Any:
        """FinitePolyExtElement.pth_power(self, int k=1)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 967)

        Return the `(p^k)`-th power of self, where `p` is the
        characteristic of the field.

        INPUT:

        - ``k`` -- integer (default: 1, must fit in C int type)

        Note that if `k` is negative, then this computes the appropriate root.

        EXAMPLES::

            sage: F.<a> = GF(29^2)
            sage: z = a^2 + 5*a + 1
            sage: z.pth_power()
            19*a + 20
            sage: z.pth_power(10)
            10*a + 28
            sage: z.pth_power(-10) == z
            True
            sage: F.<b> = GF(2^12)
            sage: y = b^3 + b + 1
            sage: y == (y.pth_power(-3))^(2^3)
            True
            sage: y.pth_power(2)
            b^7 + b^6 + b^5 + b^4 + b^3 + b"""
    @overload
    def pth_power(self) -> Any:
        """FinitePolyExtElement.pth_power(self, int k=1)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 967)

        Return the `(p^k)`-th power of self, where `p` is the
        characteristic of the field.

        INPUT:

        - ``k`` -- integer (default: 1, must fit in C int type)

        Note that if `k` is negative, then this computes the appropriate root.

        EXAMPLES::

            sage: F.<a> = GF(29^2)
            sage: z = a^2 + 5*a + 1
            sage: z.pth_power()
            19*a + 20
            sage: z.pth_power(10)
            10*a + 28
            sage: z.pth_power(-10) == z
            True
            sage: F.<b> = GF(2^12)
            sage: y = b^3 + b + 1
            sage: y == (y.pth_power(-3))^(2^3)
            True
            sage: y.pth_power(2)
            b^7 + b^6 + b^5 + b^4 + b^3 + b"""
    def pth_root(self, intk=...) -> Any:
        """FinitePolyExtElement.pth_root(self, int k=1)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 1001)

        Return the `(p^k)`-th root of self, where `p` is the characteristic
        of the field.

        INPUT:

        - ``k`` -- integer (default: 1, must fit in C int type)

        Note that if `k` is negative, then this computes the appropriate power.

        EXAMPLES::

            sage: F.<b> = GF(2^12)
            sage: y = b^3 + b + 1
            sage: y == (y.pth_root(3))^(2^3)
            True
            sage: y.pth_root(2)
            b^11 + b^10 + b^9 + b^7 + b^5 + b^4 + b^2 + b"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """FinitePolyExtElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 834)

        See :meth:`square_root`.

        EXAMPLES::

            sage: k.<a> = GF(3^17)
            sage: (a^3 - a - 1).sqrt()
            a^16 + 2*a^15 + a^13 + 2*a^12 + a^10 + 2*a^9 + 2*a^8 + a^7 + a^6 + 2*a^5 + a^4 + 2*a^2 + 2*a + 2"""
    @overload
    def sqrt(self) -> Any:
        """FinitePolyExtElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 834)

        See :meth:`square_root`.

        EXAMPLES::

            sage: k.<a> = GF(3^17)
            sage: (a^3 - a - 1).sqrt()
            a^16 + 2*a^15 + a^13 + 2*a^12 + a^10 + 2*a^9 + 2*a^8 + a^7 + a^6 + 2*a^5 + a^4 + 2*a^2 + 2*a + 2"""
    @overload
    def square_root(self, extend=..., all=...) -> Any:
        """FinitePolyExtElement.square_root(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 791)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the root is not in the base ring.

           .. WARNING::

               This option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

           The ``'extend'`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a')
            sage: F(2).square_root()
            4
            sage: F(3).square_root()
            2*a + 6
            sage: F(3).square_root()**2
            3
            sage: F(4).square_root()
            2
            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).square_root()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square."""
    @overload
    def square_root(self) -> Any:
        """FinitePolyExtElement.square_root(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 791)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the root is not in the base ring.

           .. WARNING::

               This option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

           The ``'extend'`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a')
            sage: F(2).square_root()
            4
            sage: F(3).square_root()
            2*a + 6
            sage: F(3).square_root()**2
            3
            sage: F(4).square_root()
            2
            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).square_root()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square."""
    @overload
    def square_root(self) -> Any:
        """FinitePolyExtElement.square_root(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 791)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the root is not in the base ring.

           .. WARNING::

               This option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

           The ``'extend'`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a')
            sage: F(2).square_root()
            4
            sage: F(3).square_root()
            2*a + 6
            sage: F(3).square_root()**2
            3
            sage: F(4).square_root()
            2
            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).square_root()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square."""
    @overload
    def square_root(self) -> Any:
        """FinitePolyExtElement.square_root(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 791)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the root is not in the base ring.

           .. WARNING::

               This option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

           The ``'extend'`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a')
            sage: F(2).square_root()
            4
            sage: F(3).square_root()
            2*a + 6
            sage: F(3).square_root()**2
            3
            sage: F(4).square_root()
            2
            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).square_root()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square."""
    @overload
    def square_root(self) -> Any:
        """FinitePolyExtElement.square_root(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 791)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the root is not in the base ring.

           .. WARNING::

               This option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

           The ``'extend'`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a')
            sage: F(2).square_root()
            4
            sage: F(3).square_root()
            2*a + 6
            sage: F(3).square_root()**2
            3
            sage: F(4).square_root()
            2
            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).square_root()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square."""
    @overload
    def square_root(self) -> Any:
        """FinitePolyExtElement.square_root(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 791)

        The square root function.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the root is not in the base ring.

           .. WARNING::

               This option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

           The ``'extend'`` option is not implemented (yet).

        EXAMPLES::

            sage: F = FiniteField(7^2, 'a')
            sage: F(2).square_root()
            4
            sage: F(3).square_root()
            2*a + 6
            sage: F(3).square_root()**2
            3
            sage: F(4).square_root()
            2
            sage: K = FiniteField(7^3, 'alpha', impl='pari_ffelt')
            sage: K(3).square_root()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square."""
    @overload
    def to_bytes(self, byteorder=...) -> Any:
        """FinitePolyExtElement.to_bytes(self, byteorder='big')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 1130)

        Return an array of bytes representing an integer.

        Internally relies on the python ``int.to_bytes()`` method.
        Length of byte array is determined from the field's order.

        INPUT:

        - ``byteorder`` -- string (default: ``'big'``); determines the byte order of
          the output; can only be ``'big'`` or ``'little'``

        EXAMPLES::

            sage: F.<z5> = GF(3^5)
            sage: a = z5^4 + 2*z5^3 + 1
            sage: a.to_bytes()
            b'\\x88'

        ::

            sage: F.<z3> = GF(163^3)
            sage: a = 136*z3^2 + 10*z3 + 125
            sage: a.to_bytes()
            b'7)\\xa3'"""
    @overload
    def to_bytes(self) -> Any:
        """FinitePolyExtElement.to_bytes(self, byteorder='big')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 1130)

        Return an array of bytes representing an integer.

        Internally relies on the python ``int.to_bytes()`` method.
        Length of byte array is determined from the field's order.

        INPUT:

        - ``byteorder`` -- string (default: ``'big'``); determines the byte order of
          the output; can only be ``'big'`` or ``'little'``

        EXAMPLES::

            sage: F.<z5> = GF(3^5)
            sage: a = z5^4 + 2*z5^3 + 1
            sage: a.to_bytes()
            b'\\x88'

        ::

            sage: F.<z3> = GF(163^3)
            sage: a = 136*z3^2 + 10*z3 + 125
            sage: a.to_bytes()
            b'7)\\xa3'"""
    def to_integer(self, reverse=...) -> Any:
        """FinitePolyExtElement.to_integer(self, reverse=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 1069)

        Return an integer representation of this finite field element
        obtained by lifting its representative polynomial to `\\ZZ` and
        evaluating it at the characteristic `p`.

        If ``reverse`` is set to ``True`` (default: ``False``),
        the list of coefficients is reversed prior to evaluation.

        Inverse of :meth:`sage.rings.finite_rings.finite_field_base.FiniteField.from_integer`.

        EXAMPLES::

            sage: F.<t> = GF(7^5)
            sage: F(5).to_integer()
            5
            sage: t.to_integer()
            7
            sage: (t^2).to_integer()
            49
            sage: (t^2+1).to_integer()
            50
            sage: (t^2+t+1).to_integer()
            57

        ::

            sage: F.<t> = GF(2^8)
            sage: u = F.from_integer(0xd1)
            sage: bin(u.to_integer(False))
            '0b11010001'
            sage: bin(u.to_integer(True))
            '0b10001011'

        TESTS::

            sage: # needs sage.modules
            sage: p = random_prime(2^99)
            sage: k = randrange(2,10)
            sage: F.<t> = GF((p, k))
            sage: rev = bool(randrange(2))
            sage: u = F.random_element()
            sage: 0 <= u.to_integer(rev) < F.cardinality()
            True
            sage: F.from_integer(u.to_integer(rev), rev) == u
            True
            sage: n = randrange(F.cardinality())
            sage: F.from_integer(n, rev).to_integer(rev) == n
            True"""
    @overload
    def trace(self) -> Any:
        """FinitePolyExtElement.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 686)

        Return the trace of this element, which is the sum of the
        Galois conjugates.

        EXAMPLES::

            sage: S.<a> = GF(5^3); S
            Finite Field in a of size 5^3
            sage: a.trace()
            0
            sage: a.charpoly('t')
            t^3 + 3*t + 3
            sage: a + a^5 + a^25
            0
            sage: z = a^2 + a + 1
            sage: z.trace()
            2
            sage: z.charpoly('t')
            t^3 + 3*t^2 + 2*t + 2
            sage: z + z^5 + z^25
            2"""
    @overload
    def trace(self) -> Any:
        """FinitePolyExtElement.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 686)

        Return the trace of this element, which is the sum of the
        Galois conjugates.

        EXAMPLES::

            sage: S.<a> = GF(5^3); S
            Finite Field in a of size 5^3
            sage: a.trace()
            0
            sage: a.charpoly('t')
            t^3 + 3*t + 3
            sage: a + a^5 + a^25
            0
            sage: z = a^2 + a + 1
            sage: z.trace()
            2
            sage: z.charpoly('t')
            t^3 + 3*t^2 + 2*t + 2
            sage: z + z^5 + z^25
            2"""
    @overload
    def trace(self) -> Any:
        """FinitePolyExtElement.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 686)

        Return the trace of this element, which is the sum of the
        Galois conjugates.

        EXAMPLES::

            sage: S.<a> = GF(5^3); S
            Finite Field in a of size 5^3
            sage: a.trace()
            0
            sage: a.charpoly('t')
            t^3 + 3*t + 3
            sage: a + a^5 + a^25
            0
            sage: z = a^2 + a + 1
            sage: z.trace()
            2
            sage: z.charpoly('t')
            t^3 + 3*t^2 + 2*t + 2
            sage: z + z^5 + z^25
            2"""
    def __getitem__(self, n) -> Any:
        """FinitePolyExtElement.__getitem__(self, n)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 294)

        Return the `n`-th coefficient of this finite field element when
        written as a polynomial in the generator.

        EXAMPLES::

            sage: x = polygen(GF(19))
            sage: F.<i> = GF(19^2, modulus=x^2+1)
            sage: a = 5 + 7*i
            sage: a[0]
            5
            sage: a[1]
            7

        ::

            sage: b = F(11)
            sage: b[0]
            11
            sage: b[1]
            0

        TESTS::

            sage: # needs sage.modules
            sage: F,t = GF(random_prime(99)^randrange(2,99), 't').objgen()
            sage: a = F.random_element()
            sage: all(a[i] == a.polynomial()[i] for i in range(F.degree()))
            True
            sage: a == sum(a[i]*t^i for i in range(F.degree()))
            True"""
    def __iter__(self) -> Any:
        """FinitePolyExtElement.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 371)

        Return an iterator over the coefficients of this finite field
        element, in the same order as :meth:`list`.

        EXAMPLES::

            sage: x = polygen(GF(19))
            sage: F.<i> = GF(19^2, modulus=x^2+1)
            sage: a = 5 + 7*i
            sage: it = iter(a)
            sage: next(it)
            5
            sage: next(it)
            7
            sage: next(it)
            Traceback (most recent call last):
            ...
            StopIteration
            sage: list(a)   # implicit doctest
            [5, 7]
            sage: tuple(a)  # implicit doctest
            (5, 7)
            sage: b = F(11)
            sage: list(b)   # implicit doctest
            [11, 0]
            sage: tuple(b)  # implicit doctest
            (11, 0)
            sage: list(b.polynomial())
            [11]

        TESTS::

            sage: # needs sage.modules
            sage: F = GF(random_prime(333)^randrange(111,999),'t')
            sage: a = F.random_element()
            sage: list(a) == a.list()  # implicit doctest
            True

        ::

            sage: # needs sage.modules
            sage: F.<t> = GF(17^60)
            sage: a = F.random_element()
            sage: a == sum(c*t^i for i,c in enumerate(a))  # implicit doctest
            True

        ::

            sage: # needs sage.modules
            sage: F.<t> = GF((2^127 - 1)^10, 't')
            sage: a = F.random_element()
            sage: a == sum(c*t^i for i,c in enumerate(a))  # implicit doctest
            True"""
    @overload
    def __pari__(self, var=...) -> Any:
        """FinitePolyExtElement.__pari__(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 532)

        Return PARI representation of this finite field element.

        INPUT:

        - ``var`` -- (default: ``None``) optional variable string

        EXAMPLES::

            sage: k.<a> = GF(5^3)
            sage: a.__pari__()
            a
            sage: a.__pari__('b')
            b
            sage: t = 3*a^2 + 2*a + 4
            sage: t_string = t._pari_init_('y')
            sage: t_string
            'Mod(Mod(3, 5)*y^2 + Mod(2, 5)*y + Mod(4, 5), Mod(1, 5)*y^3 + Mod(3, 5)*y + Mod(3, 5))'
            sage: type(t_string)
            <... 'str'>
            sage: t_element = t.__pari__('b')
            sage: t_element
            3*b^2 + 2*b + 4
            sage: type(t_element)
            <class 'cypari2.gen.Gen'>"""
    @overload
    def __pari__(self) -> Any:
        """FinitePolyExtElement.__pari__(self, var=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 532)

        Return PARI representation of this finite field element.

        INPUT:

        - ``var`` -- (default: ``None``) optional variable string

        EXAMPLES::

            sage: k.<a> = GF(5^3)
            sage: a.__pari__()
            a
            sage: a.__pari__('b')
            b
            sage: t = 3*a^2 + 2*a + 4
            sage: t_string = t._pari_init_('y')
            sage: t_string
            'Mod(Mod(3, 5)*y^2 + Mod(2, 5)*y + Mod(4, 5), Mod(1, 5)*y^3 + Mod(3, 5)*y + Mod(3, 5))'
            sage: type(t_string)
            <... 'str'>
            sage: t_element = t.__pari__('b')
            sage: t_element
            3*b^2 + 2*b + 4
            sage: type(t_element)
            <class 'cypari2.gen.Gen'>"""

class FiniteRingElement(sage.structure.element.CommutativeRingElement):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def canonical_associate(self) -> Any:
        """FiniteRingElement.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 168)

        Return a canonical associate.

        Implemented here because not all finite field elements inherit from FieldElement.

        EXAMPLES::

            sage: GF(7)(1).canonical_associate()
            (1, 1)
            sage: GF(7)(3).canonical_associate()
            (1, 3)
            sage: GF(7)(0).canonical_associate()
            (0, 1)
            sage: IntegerModRing(15)(7).canonical_associate()
            NotImplemented"""
    @overload
    def canonical_associate(self) -> Any:
        """FiniteRingElement.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 168)

        Return a canonical associate.

        Implemented here because not all finite field elements inherit from FieldElement.

        EXAMPLES::

            sage: GF(7)(1).canonical_associate()
            (1, 1)
            sage: GF(7)(3).canonical_associate()
            (1, 3)
            sage: GF(7)(0).canonical_associate()
            (0, 1)
            sage: IntegerModRing(15)(7).canonical_associate()
            NotImplemented"""
    @overload
    def canonical_associate(self) -> Any:
        """FiniteRingElement.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 168)

        Return a canonical associate.

        Implemented here because not all finite field elements inherit from FieldElement.

        EXAMPLES::

            sage: GF(7)(1).canonical_associate()
            (1, 1)
            sage: GF(7)(3).canonical_associate()
            (1, 3)
            sage: GF(7)(0).canonical_associate()
            (0, 1)
            sage: IntegerModRing(15)(7).canonical_associate()
            NotImplemented"""
    @overload
    def canonical_associate(self) -> Any:
        """FiniteRingElement.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 168)

        Return a canonical associate.

        Implemented here because not all finite field elements inherit from FieldElement.

        EXAMPLES::

            sage: GF(7)(1).canonical_associate()
            (1, 1)
            sage: GF(7)(3).canonical_associate()
            (1, 3)
            sage: GF(7)(0).canonical_associate()
            (0, 1)
            sage: IntegerModRing(15)(7).canonical_associate()
            NotImplemented"""
    @overload
    def canonical_associate(self) -> Any:
        """FiniteRingElement.canonical_associate(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 168)

        Return a canonical associate.

        Implemented here because not all finite field elements inherit from FieldElement.

        EXAMPLES::

            sage: GF(7)(1).canonical_associate()
            (1, 1)
            sage: GF(7)(3).canonical_associate()
            (1, 3)
            sage: GF(7)(0).canonical_associate()
            (0, 1)
            sage: IntegerModRing(15)(7).canonical_associate()
            NotImplemented"""
    @overload
    def to_bytes(self, byteorder=...) -> Any:
        '''FiniteRingElement.to_bytes(self, byteorder=\'big\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 144)

        Return an array of bytes representing an integer.

        Internally relies on the python ``int.to_bytes()`` method.
        Length of byte array is determined from the field\'s order.

        INPUT:

        - ``byteorder`` -- string (default: ``\'big\'``); determines the byte order of
          ``input_bytes``; can only be ``\'big\'`` or ``\'little\'``

        EXAMPLES::

            sage: F = GF(65537)
            sage: a = F(8726)
            sage: a.to_bytes()
            b\'\\x00"\\x16\'
            sage: a.to_bytes(byteorder=\'little\')
            b\'\\x16"\\x00\''''
    @overload
    def to_bytes(self) -> Any:
        '''FiniteRingElement.to_bytes(self, byteorder=\'big\')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_base.pyx (starting at line 144)

        Return an array of bytes representing an integer.

        Internally relies on the python ``int.to_bytes()`` method.
        Length of byte array is determined from the field\'s order.

        INPUT:

        - ``byteorder`` -- string (default: ``\'big\'``); determines the byte order of
          ``input_bytes``; can only be ``\'big\'`` or ``\'little\'``

        EXAMPLES::

            sage: F = GF(65537)
            sage: a = F(8726)
            sage: a.to_bytes()
            b\'\\x00"\\x16\'
            sage: a.to_bytes(byteorder=\'little\')
            b\'\\x16"\\x00\''''
