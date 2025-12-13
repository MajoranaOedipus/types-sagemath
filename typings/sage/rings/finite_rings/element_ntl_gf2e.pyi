import _cython_3_2_1
import cypari2.pari_instance
import sage.rings.finite_rings.element_base
from sage.interfaces.abc import GapElement as GapElement
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.finite_rings.element_pari_ffelt import FiniteFieldElement_pari_ffelt as FiniteFieldElement_pari_ffelt
from sage.rings.finite_rings.finite_field_ntl_gf2e import FiniteField_ntl_gf2e as FiniteField_ntl_gf2e
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

pari: cypari2.pari_instance.Pari
unpickleFiniteField_ntl_gf2eElement: _cython_3_2_1.cython_function_or_method

class Cache_ntl_gf2e(sage.rings.finite_rings.element_base.Cache_base):
    """Cache_ntl_gf2e(parent, Py_ssize_t k, modulus)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 109)

    This class stores information for an NTL finite field in a Cython
    class so that elements can access it quickly.

    It's modeled on
    :class:`~sage.rings.finite_rings.integer_mod.NativeIntStruct`,
    but includes many functions that were previously included in
    the parent (see :issue:`12062`)."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, Py_ssize_tk, modulus) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 141)

                Initialization.

                TESTS::

                    sage: k.<a> = GF(2^8, impl='ntl')
        """
    @overload
    def degree(self) -> Any:
        """Cache_ntl_gf2e.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 232)

        If the field has cardinality `2^n` this method returns `n`.

        EXAMPLES::

            sage: k.<a> = GF(2^64)
            sage: k._cache.degree()
            64"""
    @overload
    def degree(self) -> Any:
        """Cache_ntl_gf2e.degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 232)

        If the field has cardinality `2^n` this method returns `n`.

        EXAMPLES::

            sage: k.<a> = GF(2^64)
            sage: k._cache.degree()
            64"""
    def fetch_int(self, number) -> FiniteField_ntl_gf2eElement:
        """Cache_ntl_gf2e.fetch_int(self, number) -> FiniteField_ntl_gf2eElement

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 380)

        Given an integer less than `p^n` with base `2`
        representation `a_0 + a_1 \\cdot 2 + \\cdots + a_k 2^k`, this returns
        `a_0 + a_1 x + \\cdots + a_k x^k`, where `x` is the
        generator of this finite field.

        INPUT:

        - ``number`` -- integer; of size less than the cardinality

        EXAMPLES::

            sage: k.<a> = GF(2^48)
            sage: k._cache.fetch_int(2^33 + 2 + 1)
            a^33 + a + 1

        TESTS:

        We test that :issue:`17027` is fixed::

            sage: K.<a> = GF(2^16)
            sage: K._cache.fetch_int(0r)
            0"""
    @overload
    def import_data(self, e) -> Any:
        """Cache_ntl_gf2e.import_data(self, e)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 244)

        EXAMPLES::

            sage: k.<a> = GF(2^17)
            sage: V = k.vector_space(map=False)
            sage: v = [1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0]
            sage: k._cache.import_data(v)
            a^13 + a^8 + a^5 + 1
            sage: k._cache.import_data(V(v))
            a^13 + a^8 + a^5 + 1

        TESTS:

        We check that :issue:`12584` is fixed::

            sage: k(2^63)
            0

        We can coerce from PARI finite field implementations::

            sage: K.<a> = GF(2^19, impl='ntl')
            sage: a^20
            a^6 + a^3 + a^2 + a
            sage: M.<c> = GF(2^19, impl='pari_ffelt')
            sage: K(c^20)
            a^6 + a^3 + a^2 + a"""
    @overload
    def import_data(self, v) -> Any:
        """Cache_ntl_gf2e.import_data(self, e)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 244)

        EXAMPLES::

            sage: k.<a> = GF(2^17)
            sage: V = k.vector_space(map=False)
            sage: v = [1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0]
            sage: k._cache.import_data(v)
            a^13 + a^8 + a^5 + 1
            sage: k._cache.import_data(V(v))
            a^13 + a^8 + a^5 + 1

        TESTS:

        We check that :issue:`12584` is fixed::

            sage: k(2^63)
            0

        We can coerce from PARI finite field implementations::

            sage: K.<a> = GF(2^19, impl='ntl')
            sage: a^20
            a^6 + a^3 + a^2 + a
            sage: M.<c> = GF(2^19, impl='pari_ffelt')
            sage: K(c^20)
            a^6 + a^3 + a^2 + a"""
    @overload
    def order(self) -> Any:
        """Cache_ntl_gf2e.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 220)

        Return the cardinality of the field.

        EXAMPLES::

            sage: k.<a> = GF(2^64)
            sage: k._cache.order()
            18446744073709551616"""
    @overload
    def order(self) -> Any:
        """Cache_ntl_gf2e.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 220)

        Return the cardinality of the field.

        EXAMPLES::

            sage: k.<a> = GF(2^64)
            sage: k._cache.order()
            18446744073709551616"""
    @overload
    def polynomial(self) -> Any:
        """Cache_ntl_gf2e.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 437)

        Return the list of 0s and 1s giving the defining polynomial of the
        field.

        EXAMPLES::

            sage: k.<a> = GF(2^20,modulus='minimal_weight')
            sage: k._cache.polynomial()
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]"""
    @overload
    def polynomial(self) -> Any:
        """Cache_ntl_gf2e.polynomial(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 437)

        Return the list of 0s and 1s giving the defining polynomial of the
        field.

        EXAMPLES::

            sage: k.<a> = GF(2^20,modulus='minimal_weight')
            sage: k._cache.polynomial()
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]"""

class FiniteField_ntl_gf2eElement(sage.rings.finite_rings.element_base.FinitePolyExtElement):
    """FiniteField_ntl_gf2eElement(parent=None)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 467)

    An element of an NTL:GF2E finite field."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 472)

                Initialize an element in parent. It's much better to use
                parent(<value>) or any specialized method of parent
                (one,zero,gen) instead. Do not call this constructor directly,
                it doesn't make much sense.

                INPUT:

                - ``parent`` -- base field

                OUTPUT: a finite field element

                EXAMPLES::

                    sage: k.<a> = GF(2^16)
                    sage: from sage.rings.finite_rings.element_ntl_gf2e import FiniteField_ntl_gf2eElement
                    sage: FiniteField_ntl_gf2eElement(k)
                    0
                    sage: k.<a> = GF(2^20)
                    sage: a.parent() is k
                    True
        """
    @overload
    def charpoly(self, var=...) -> Any:
        """FiniteField_ntl_gf2eElement.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 988)

        Return the characteristic polynomial of ``self`` as a polynomial
        in var over the prime subfield.

        INPUT:

        - ``var`` -- string (default: ``'x'``)

        OUTPUT: polynomial

        EXAMPLES::

            sage: k.<a> = GF(2^8, impl='ntl')
            sage: b = a^3 + a
            sage: b.minpoly()
            x^4 + x^3 + x^2 + x + 1
            sage: b.charpoly()
            x^8 + x^6 + x^4 + x^2 + 1
            sage: b.charpoly().factor()
            (x^4 + x^3 + x^2 + x + 1)^2
            sage: b.charpoly('Z')
            Z^8 + Z^6 + Z^4 + Z^2 + 1"""
    @overload
    def charpoly(self) -> Any:
        """FiniteField_ntl_gf2eElement.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 988)

        Return the characteristic polynomial of ``self`` as a polynomial
        in var over the prime subfield.

        INPUT:

        - ``var`` -- string (default: ``'x'``)

        OUTPUT: polynomial

        EXAMPLES::

            sage: k.<a> = GF(2^8, impl='ntl')
            sage: b = a^3 + a
            sage: b.minpoly()
            x^4 + x^3 + x^2 + x + 1
            sage: b.charpoly()
            x^8 + x^6 + x^4 + x^2 + 1
            sage: b.charpoly().factor()
            (x^4 + x^3 + x^2 + x + 1)^2
            sage: b.charpoly('Z')
            Z^8 + Z^6 + Z^4 + Z^2 + 1"""
    @overload
    def charpoly(self) -> Any:
        """FiniteField_ntl_gf2eElement.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 988)

        Return the characteristic polynomial of ``self`` as a polynomial
        in var over the prime subfield.

        INPUT:

        - ``var`` -- string (default: ``'x'``)

        OUTPUT: polynomial

        EXAMPLES::

            sage: k.<a> = GF(2^8, impl='ntl')
            sage: b = a^3 + a
            sage: b.minpoly()
            x^4 + x^3 + x^2 + x + 1
            sage: b.charpoly()
            x^8 + x^6 + x^4 + x^2 + 1
            sage: b.charpoly().factor()
            (x^4 + x^3 + x^2 + x + 1)^2
            sage: b.charpoly('Z')
            Z^8 + Z^6 + Z^4 + Z^2 + 1"""
    @overload
    def is_one(self) -> Any:
        """FiniteField_ntl_gf2eElement.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 576)

        Return ``True`` if ``self == k(1)``.

        Equivalent to ``self != k(0)``.

        EXAMPLES::

            sage: k.<a> = GF(2^20)
            sage: a.is_one() # indirect doctest
            False
            sage: k(1).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """FiniteField_ntl_gf2eElement.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 576)

        Return ``True`` if ``self == k(1)``.

        Equivalent to ``self != k(0)``.

        EXAMPLES::

            sage: k.<a> = GF(2^20)
            sage: a.is_one() # indirect doctest
            False
            sage: k(1).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """FiniteField_ntl_gf2eElement.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 576)

        Return ``True`` if ``self == k(1)``.

        Equivalent to ``self != k(0)``.

        EXAMPLES::

            sage: k.<a> = GF(2^20)
            sage: a.is_one() # indirect doctest
            False
            sage: k(1).is_one()
            True"""
    def is_square(self) -> Any:
        """FiniteField_ntl_gf2eElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 612)

        Return ``True`` as every element in `\\GF{2^n}` is a square.

        EXAMPLES::

            sage: k.<a> = GF(2^18)
            sage: e = k.random_element()
            sage: e.parent() is k
            True
            sage: e.is_square()
            True
            sage: e.sqrt()^2 == e
            True"""
    @overload
    def is_unit(self) -> Any:
        """FiniteField_ntl_gf2eElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 593)

        Return ``True`` if ``self`` is nonzero, so it is a unit as an element
        of the finite field.

        EXAMPLES::

            sage: k.<a> = GF(2^17)
            sage: a.is_unit()
            True
            sage: k(0).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """FiniteField_ntl_gf2eElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 593)

        Return ``True`` if ``self`` is nonzero, so it is a unit as an element
        of the finite field.

        EXAMPLES::

            sage: k.<a> = GF(2^17)
            sage: a.is_unit()
            True
            sage: k(0).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """FiniteField_ntl_gf2eElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 593)

        Return ``True`` if ``self`` is nonzero, so it is a unit as an element
        of the finite field.

        EXAMPLES::

            sage: k.<a> = GF(2^17)
            sage: a.is_unit()
            True
            sage: k(0).is_unit()
            False"""
    @overload
    def log(self, base, order=..., check=...) -> Any:
        """FiniteField_ntl_gf2eElement.log(self, base, order=None, *, check=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1227)

        Compute an integer `x` such that `b^x = a`, where `a` is ``self``
        and `b` is ``base``.

        INPUT:

        - ``base`` -- finite field element
        - ``order`` -- integer (optional), the order of the base
        - ``check`` -- boolean (default: ``False``): If set,
          test whether the given ``order`` is correct.

        OUTPUT:

        Integer `x` such that `a^x = b`, if it exists.
        Raises a :exc:`ValueError` exception if no such `x` exists.

        ALGORITHM: :pari:`fflog`

        EXAMPLES::

            sage: F = FiniteField(2^10, 'a')
            sage: g = F.gen()
            sage: b = g; a = g^37
            sage: a.log(b)
            37
            sage: b^37; a
            a^8 + a^7 + a^4 + a + 1
            a^8 + a^7 + a^4 + a + 1

        Big instances used to take a very long time before :issue:`32842`::

            sage: g = GF(2^61).gen()
            sage: g.log(g^7)
            1976436865040309101

        TESTS:

        Check that non-existence is correctly detected::

            sage: g = GF(2^50).gen()
            sage: (2^50-1) % 1023
            0
            sage: g.log(g^1023)
            Traceback (most recent call last):
            ...
            ValueError: no logarithm of z50 exists to base z50^49 + z50^46 + z50^45 + z50^44 + z50^41 + z50^34 + z50^33 + z50^32 + z50^27 + z50^25 + z50^24 + z50^21 + z50^18 + z50^17 + z50^16 + z50^15 + z50^12 + z50^11 + z50^10 + z50^8 + z50^7 + z50^3 + z50^2

        An example for ``check=True``::

            sage: F.<t> = GF(2^5, impl='ntl')
            sage: t.log(t, 3^4, check=True)
            Traceback (most recent call last):
            ...
            ValueError: base does not have the provided order

        AUTHORS:

        - David Joyner and William Stein (2005-11)
        - Lorenz Panny (2021-11): use PARI's :pari:`fflog` instead of :func:`sage.groups.generic.discrete_log`"""
    @overload
    def log(self, b) -> Any:
        """FiniteField_ntl_gf2eElement.log(self, base, order=None, *, check=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1227)

        Compute an integer `x` such that `b^x = a`, where `a` is ``self``
        and `b` is ``base``.

        INPUT:

        - ``base`` -- finite field element
        - ``order`` -- integer (optional), the order of the base
        - ``check`` -- boolean (default: ``False``): If set,
          test whether the given ``order`` is correct.

        OUTPUT:

        Integer `x` such that `a^x = b`, if it exists.
        Raises a :exc:`ValueError` exception if no such `x` exists.

        ALGORITHM: :pari:`fflog`

        EXAMPLES::

            sage: F = FiniteField(2^10, 'a')
            sage: g = F.gen()
            sage: b = g; a = g^37
            sage: a.log(b)
            37
            sage: b^37; a
            a^8 + a^7 + a^4 + a + 1
            a^8 + a^7 + a^4 + a + 1

        Big instances used to take a very long time before :issue:`32842`::

            sage: g = GF(2^61).gen()
            sage: g.log(g^7)
            1976436865040309101

        TESTS:

        Check that non-existence is correctly detected::

            sage: g = GF(2^50).gen()
            sage: (2^50-1) % 1023
            0
            sage: g.log(g^1023)
            Traceback (most recent call last):
            ...
            ValueError: no logarithm of z50 exists to base z50^49 + z50^46 + z50^45 + z50^44 + z50^41 + z50^34 + z50^33 + z50^32 + z50^27 + z50^25 + z50^24 + z50^21 + z50^18 + z50^17 + z50^16 + z50^15 + z50^12 + z50^11 + z50^10 + z50^8 + z50^7 + z50^3 + z50^2

        An example for ``check=True``::

            sage: F.<t> = GF(2^5, impl='ntl')
            sage: t.log(t, 3^4, check=True)
            Traceback (most recent call last):
            ...
            ValueError: base does not have the provided order

        AUTHORS:

        - David Joyner and William Stein (2005-11)
        - Lorenz Panny (2021-11): use PARI's :pari:`fflog` instead of :func:`sage.groups.generic.discrete_log`"""
    def minpoly(self, var=...) -> Any:
        """FiniteField_ntl_gf2eElement.minpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1017)

        Return the minimal polynomial of ``self``, which is the smallest
        degree polynomial `f \\in \\GF{2}[x]` such that ``f(self) == 0``.

        INPUT:

        - ``var`` -- string (default: ``'x'``)

        OUTPUT: polynomial

        EXAMPLES::

            sage: K.<a> = GF(2^100)
            sage: f = a.minpoly(); f
            x^100 + x^57 + x^56 + x^55 + x^52 + x^48 + x^47 + x^46 + x^45 + x^44 + x^43 + x^41 + x^37 + x^36 + x^35 + x^34 + x^31 + x^30 + x^27 + x^25 + x^24 + x^22 + x^20 + x^19 + x^16 + x^15 + x^11 + x^9 + x^8 + x^6 + x^5 + x^3 + 1
            sage: f(a)
            0
            sage: g = K.random_element()
            sage: g.minpoly()(g)
            0"""
    @overload
    def polynomial(self, name=...) -> Any:
        """FiniteField_ntl_gf2eElement.polynomial(self, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 957)

        Return ``self`` viewed as a polynomial over
        ``self.parent().prime_subfield()``.

        INPUT:

        - ``name`` -- (optional) variable name

        EXAMPLES::

            sage: k.<a> = GF(2^17)
            sage: e = a^15 + a^13 + a^11 + a^10 + a^9 + a^8 + a^7 + a^6 + a^4 + a + 1
            sage: e.polynomial()
            a^15 + a^13 + a^11 + a^10 + a^9 + a^8 + a^7 + a^6 + a^4 + a + 1

            sage: from sage.rings.polynomial.polynomial_element import Polynomial
            sage: isinstance(e.polynomial(), Polynomial)
            True

            sage: e.polynomial('x')
            x^15 + x^13 + x^11 + x^10 + x^9 + x^8 + x^7 + x^6 + x^4 + x + 1"""
    @overload
    def polynomial(self) -> Any:
        """FiniteField_ntl_gf2eElement.polynomial(self, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 957)

        Return ``self`` viewed as a polynomial over
        ``self.parent().prime_subfield()``.

        INPUT:

        - ``name`` -- (optional) variable name

        EXAMPLES::

            sage: k.<a> = GF(2^17)
            sage: e = a^15 + a^13 + a^11 + a^10 + a^9 + a^8 + a^7 + a^6 + a^4 + a + 1
            sage: e.polynomial()
            a^15 + a^13 + a^11 + a^10 + a^9 + a^8 + a^7 + a^6 + a^4 + a + 1

            sage: from sage.rings.polynomial.polynomial_element import Polynomial
            sage: isinstance(e.polynomial(), Polynomial)
            True

            sage: e.polynomial('x')
            x^15 + x^13 + x^11 + x^10 + x^9 + x^8 + x^7 + x^6 + x^4 + x + 1"""
    @overload
    def polynomial(self) -> Any:
        """FiniteField_ntl_gf2eElement.polynomial(self, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 957)

        Return ``self`` viewed as a polynomial over
        ``self.parent().prime_subfield()``.

        INPUT:

        - ``name`` -- (optional) variable name

        EXAMPLES::

            sage: k.<a> = GF(2^17)
            sage: e = a^15 + a^13 + a^11 + a^10 + a^9 + a^8 + a^7 + a^6 + a^4 + a + 1
            sage: e.polynomial()
            a^15 + a^13 + a^11 + a^10 + a^9 + a^8 + a^7 + a^6 + a^4 + a + 1

            sage: from sage.rings.polynomial.polynomial_element import Polynomial
            sage: isinstance(e.polynomial(), Polynomial)
            True

            sage: e.polynomial('x')
            x^15 + x^13 + x^11 + x^10 + x^9 + x^8 + x^7 + x^6 + x^4 + x + 1"""
    @overload
    def sqrt(self, all=..., extend=...) -> Any:
        """FiniteField_ntl_gf2eElement.sqrt(self, all=False, extend=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 629)

        Return a square root of this finite field element in its parent.

        EXAMPLES::

            sage: k.<a> = GF(2^20)
            sage: a.is_square()
            True
            sage: a.sqrt()
            a^19 + a^15 + a^14 + a^12 + a^9 + a^7 + a^4 + a^3 + a + 1
            sage: a.sqrt()^2 == a
            True

        This failed before :issue:`4899`::

            sage: GF(2^16,'a')(1).sqrt()
            1"""
    @overload
    def sqrt(self) -> Any:
        """FiniteField_ntl_gf2eElement.sqrt(self, all=False, extend=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 629)

        Return a square root of this finite field element in its parent.

        EXAMPLES::

            sage: k.<a> = GF(2^20)
            sage: a.is_square()
            True
            sage: a.sqrt()
            a^19 + a^15 + a^14 + a^12 + a^9 + a^7 + a^4 + a^3 + a + 1
            sage: a.sqrt()^2 == a
            True

        This failed before :issue:`4899`::

            sage: GF(2^16,'a')(1).sqrt()
            1"""
    @overload
    def sqrt(self) -> Any:
        """FiniteField_ntl_gf2eElement.sqrt(self, all=False, extend=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 629)

        Return a square root of this finite field element in its parent.

        EXAMPLES::

            sage: k.<a> = GF(2^20)
            sage: a.is_square()
            True
            sage: a.sqrt()
            a^19 + a^15 + a^14 + a^12 + a^9 + a^7 + a^4 + a^3 + a + 1
            sage: a.sqrt()^2 == a
            True

        This failed before :issue:`4899`::

            sage: GF(2^16,'a')(1).sqrt()
            1"""
    @overload
    def sqrt(self) -> Any:
        """FiniteField_ntl_gf2eElement.sqrt(self, all=False, extend=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 629)

        Return a square root of this finite field element in its parent.

        EXAMPLES::

            sage: k.<a> = GF(2^20)
            sage: a.is_square()
            True
            sage: a.sqrt()
            a^19 + a^15 + a^14 + a^12 + a^9 + a^7 + a^4 + a^3 + a + 1
            sage: a.sqrt()^2 == a
            True

        This failed before :issue:`4899`::

            sage: GF(2^16,'a')(1).sqrt()
            1"""
    @overload
    def trace(self) -> Any:
        """FiniteField_ntl_gf2eElement.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1047)

        Return the trace of ``self``.

        EXAMPLES::

            sage: K.<a> = GF(2^25)
            sage: a.trace()
            0
            sage: a.charpoly()
            x^25 + x^8 + x^6 + x^2 + 1
            sage: parent(a.trace())
            Finite Field of size 2

            sage: b = a+1
            sage: b.trace()
            1
            sage: b.charpoly()[1]
            1"""
    @overload
    def trace(self) -> Any:
        """FiniteField_ntl_gf2eElement.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1047)

        Return the trace of ``self``.

        EXAMPLES::

            sage: K.<a> = GF(2^25)
            sage: a.trace()
            0
            sage: a.charpoly()
            x^25 + x^8 + x^6 + x^2 + 1
            sage: parent(a.trace())
            Finite Field of size 2

            sage: b = a+1
            sage: b.trace()
            1
            sage: b.charpoly()[1]
            1"""
    @overload
    def trace(self) -> Any:
        """FiniteField_ntl_gf2eElement.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1047)

        Return the trace of ``self``.

        EXAMPLES::

            sage: K.<a> = GF(2^25)
            sage: a.trace()
            0
            sage: a.charpoly()
            x^25 + x^8 + x^6 + x^2 + 1
            sage: parent(a.trace())
            Finite Field of size 2

            sage: b = a+1
            sage: b.trace()
            1
            sage: b.charpoly()[1]
            1"""
    @overload
    def trace(self) -> Any:
        """FiniteField_ntl_gf2eElement.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1047)

        Return the trace of ``self``.

        EXAMPLES::

            sage: K.<a> = GF(2^25)
            sage: a.trace()
            0
            sage: a.charpoly()
            x^25 + x^8 + x^6 + x^2 + 1
            sage: parent(a.trace())
            Finite Field of size 2

            sage: b = a+1
            sage: b.trace()
            1
            sage: b.charpoly()[1]
            1"""
    @overload
    def weight(self) -> Any:
        """FiniteField_ntl_gf2eElement.weight(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1072)

        Return the number of nonzero coefficients in the polynomial
        representation of ``self``.

        EXAMPLES::

            sage: K.<a> = GF(2^21)
            sage: a.weight()
            1
            sage: (a^5+a^2+1).weight()
            3
            sage: b = 1/(a+1); b
            a^20 + a^19 + a^18 + a^17 + a^16 + a^15 + a^14 + a^13 + a^12 + a^11 + a^10 + a^9 + a^8 + a^7 + a^6 + a^4 + a^3 + a^2
            sage: b.weight()
            18"""
    @overload
    def weight(self) -> Any:
        """FiniteField_ntl_gf2eElement.weight(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1072)

        Return the number of nonzero coefficients in the polynomial
        representation of ``self``.

        EXAMPLES::

            sage: K.<a> = GF(2^21)
            sage: a.weight()
            1
            sage: (a^5+a^2+1).weight()
            3
            sage: b = 1/(a+1); b
            a^20 + a^19 + a^18 + a^17 + a^16 + a^15 + a^14 + a^13 + a^12 + a^11 + a^10 + a^9 + a^8 + a^7 + a^6 + a^4 + a^3 + a^2
            sage: b.weight()
            18"""
    @overload
    def weight(self) -> Any:
        """FiniteField_ntl_gf2eElement.weight(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1072)

        Return the number of nonzero coefficients in the polynomial
        representation of ``self``.

        EXAMPLES::

            sage: K.<a> = GF(2^21)
            sage: a.weight()
            1
            sage: (a^5+a^2+1).weight()
            3
            sage: b = 1/(a+1); b
            a^20 + a^19 + a^18 + a^17 + a^16 + a^15 + a^14 + a^13 + a^12 + a^11 + a^10 + a^9 + a^8 + a^7 + a^6 + a^4 + a^3 + a^2
            sage: b.weight()
            18"""
    @overload
    def weight(self) -> Any:
        """FiniteField_ntl_gf2eElement.weight(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1072)

        Return the number of nonzero coefficients in the polynomial
        representation of ``self``.

        EXAMPLES::

            sage: K.<a> = GF(2^21)
            sage: a.weight()
            1
            sage: (a^5+a^2+1).weight()
            3
            sage: b = 1/(a+1); b
            a^20 + a^19 + a^18 + a^17 + a^16 + a^15 + a^14 + a^13 + a^12 + a^11 + a^10 + a^9 + a^8 + a^7 + a^6 + a^4 + a^3 + a^2
            sage: b.weight()
            18"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """FiniteField_ntl_gf2eElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1111)

        Return a copy of this element.  Actually just returns ``self``, since
        finite field elements are immutable.

        EXAMPLES::

            sage: k.<a> = GF(2^16)
            sage: copy(a) is a
            True"""
    def __deepcopy__(self, memo) -> Any:
        """FiniteField_ntl_gf2eElement.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1124)

        EXAMPLES::

            sage: k.<a> = GF(2^16)
            sage: deepcopy(a) is a
            True"""
    def __hash__(self) -> Any:
        """FiniteField_ntl_gf2eElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1166)

        Return the hash of this finite field element.  We hash the parent
        and the underlying integer representation of this element.

        EXAMPLES::

            sage: k.<a> = GF(2^18)
            sage: {a:1,a:0} # indirect doctest
            {a: 0}"""
    def __int__(self) -> Any:
        """FiniteField_ntl_gf2eElement.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 876)

        Return the int representation of ``self``.  When ``self`` is in the
        prime subfield, the integer returned is equal to ``self`` and
        otherwise raises an error.

        EXAMPLES::

            sage: k.<a> = GF(2^20)
            sage: int(k(0))
            0
            sage: int(k(1))
            1
            sage: int(a)
            Traceback (most recent call last):
            ...
            TypeError: Cannot coerce element to an integer.
            sage: int(a^2 + 1)
            Traceback (most recent call last):
            ...
            TypeError: Cannot coerce element to an integer."""
    def __invert__(self) -> Any:
        """FiniteField_ntl_gf2eElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 741)

        Return the multiplicative inverse of an element.

        EXAMPLES::

            sage: k.<a> = GF(2^16)
            sage: ~a
            a^15 + a^4 + a^2 + a
            sage: a * ~a
            1
            sage: ~k(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero in finite field"""
    def __neg__(self) -> Any:
        """FiniteField_ntl_gf2eElement.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 727)

        Return this element.

        EXAMPLES::

            sage: k.<a> = GF(2^16)
            sage: -a
            a"""
    def __reduce__(self) -> Any:
        """FiniteField_ntl_gf2eElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_ntl_gf2e.pyx (starting at line 1215)

        Used for supporting pickling of finite field elements.

        EXAMPLES::

            sage: k.<a> = GF(2^16)
            sage: loads(dumps(a)) == a
            True"""
