import _cython_3_2_1
import sage as sage
import sage.rings.finite_rings.element_base
from sage.interfaces.abc import GapElement as GapElement
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

__pyx_capi__: dict
unpickle_Cache_givaro: _cython_3_2_1.cython_function_or_method
unpickle_FiniteField_givaroElement: _cython_3_2_1.cython_function_or_method

class Cache_givaro(sage.rings.finite_rings.element_base.Cache_base):
    """Cache_givaro(parent, unsigned int p, unsigned int k, modulus, repr='poly', cache=False)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    repr: repr
    def __init__(self, parent, unsignedintp, unsignedintk, modulus, repr=..., cache=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 109)

                Finite Field.

                These are implemented using Zech logs and the
                cardinality must be less than `2^{16}`. By default Conway polynomials
                are used as minimal polynomial.

                INPUT:

                - ``q`` -- `p^n` (must be prime power)

                - ``name`` -- variable used for poly_repr (default: ``'a'``)

                - ``modulus`` -- a polynomial to use as modulus

                - ``repr`` -- (default: ``'poly'``) controls the way elements are printed
                  to the user:

                  - 'log': repr is :meth:`~FiniteField_givaroElement.log_repr()`
                  - 'int': repr is :meth:`~FiniteField_givaroElement.int_repr()`
                  - 'poly': repr is :meth:`~FiniteField_givaroElement.poly_repr()`

                - ``cache`` -- boolean (default: ``False``); if ``True`` a cache of all
                  elements of this field is created. Thus, arithmetic does not
                  create new elements which speeds calculations up. Also, if many
                  elements are needed during a calculation this cache reduces the
                  memory requirement as at most :meth:`order()` elements are created.

                OUTPUT: Givaro finite field with characteristic `p` and cardinality `p^n`

                EXAMPLES:

                By default Conway polynomials are used::

                    sage: k.<a> = GF(2**8)
                    sage: -a ^ k.degree()
                    a^4 + a^3 + a^2 + 1
                    sage: f = k.modulus(); f
                    x^8 + x^4 + x^3 + x^2 + 1

                You may enforce a modulus::

                    sage: P.<x> = PolynomialRing(GF(2))
                    sage: f = x^8 + x^4 + x^3 + x + 1 # Rijndael polynomial
                    sage: k.<a> = GF(2^8, modulus=f)
                    sage: k.modulus()
                    x^8 + x^4 + x^3 + x + 1
                    sage: a^(2^8)
                    a

                You may enforce a random modulus::

                    sage: k = GF(3**5, 'a', modulus='random')
                    sage: k.modulus() # random polynomial
                    x^5 + 2*x^4 + 2*x^3 + x^2 + 2

                For binary fields, you may ask for a minimal weight polynomial::

                    sage: k = GF(2**10, 'a', modulus='minimal_weight')
                    sage: k.modulus()
                    x^10 + x^3 + 1
        """
    def a_times_b_minus_c(self, FiniteField_givaroElementa, FiniteField_givaroElementb, FiniteField_givaroElementc) -> Any:
        """Cache_givaro.a_times_b_minus_c(self, FiniteField_givaroElement a, FiniteField_givaroElement b, FiniteField_givaroElement c)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 695)

        Return ``a*b - c``.

        INPUT:

        - ``a``, ``b``, ``c`` -- :class:`FiniteField_givaroElement`

        EXAMPLES::

            sage: k.<a> = GF(3**3)
            sage: k._cache.a_times_b_minus_c(a,a,k(1))
            a^2 + 2"""
    def a_times_b_plus_c(self, FiniteField_givaroElementa, FiniteField_givaroElementb, FiniteField_givaroElementc) -> Any:
        """Cache_givaro.a_times_b_plus_c(self, FiniteField_givaroElement a, FiniteField_givaroElement b, FiniteField_givaroElement c)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 671)

        Return ``a*b + c``.

        This is faster than multiplying ``a`` and ``b``
        first and adding ``c`` to the result.

        INPUT:

        - ``a``, ``b``, ``c`` -- :class:`FiniteField_givaroElement`

        EXAMPLES::

            sage: k.<a> = GF(2**8)
            sage: k._cache.a_times_b_plus_c(a,a,k(1))
            a^2 + 1"""
    def c_minus_a_times_b(self, FiniteField_givaroElementa, FiniteField_givaroElementb, FiniteField_givaroElementc) -> Any:
        """Cache_givaro.c_minus_a_times_b(self, FiniteField_givaroElement a, FiniteField_givaroElement b, FiniteField_givaroElement c)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 716)

        Return ``c - a*b``.

        INPUT:

        - ``a``, ``b``, ``c`` -- :class:`FiniteField_givaroElement`

        EXAMPLES::

            sage: k.<a> = GF(3**3)
            sage: k._cache.c_minus_a_times_b(a,a,k(1))
            2*a^2 + 1"""
    @overload
    def characteristic(self) -> int:
        """Cache_givaro.characteristic(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 227)

        Return the characteristic of this field.

        EXAMPLES::

            sage: p = GF(19^3,'a')._cache.characteristic(); p
            19"""
    @overload
    def characteristic(self) -> Any:
        """Cache_givaro.characteristic(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 227)

        Return the characteristic of this field.

        EXAMPLES::

            sage: p = GF(19^3,'a')._cache.characteristic(); p
            19"""
    def element_from_data(self, e) -> FiniteField_givaroElement:
        """Cache_givaro.element_from_data(self, e) -> FiniteField_givaroElement

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 296)

        Coerces several data types to ``self``.

        INPUT:

        - ``e`` -- data to coerce in

        EXAMPLES::

            sage: k = GF(3^8, 'a')
            sage: type(k)
            <class 'sage.rings.finite_rings.finite_field_givaro.FiniteField_givaro_with_category'>
            sage: e = k.vector_space(map=False).gen(1); e
            (0, 1, 0, 0, 0, 0, 0, 0)
            sage: k(e) #indirect doctest
            a

        TESTS:

        Check coercion of large integers::

            sage: k(-5^13)
            1
            sage: k(2^31)
            2
            sage: k(int(10^19))
            1
            sage: k(2^63)
            2
            sage: k(2^100)
            1
            sage: k(int(2^100))
            1
            sage: k(-2^100)
            2

        Check coercion of incompatible fields::

            sage: x=GF(7).random_element()
            sage: k(x)
            Traceback (most recent call last):
            ...
            TypeError: unable to coerce from a finite field other than the prime subfield

        For more examples, see
        ``finite_field_givaro.FiniteField_givaro._element_constructor_``"""
    def exponent(self) -> int:
        """Cache_givaro.exponent(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 262)

        Return the degree of this field over `\\GF{p}`.

        EXAMPLES::

            sage: K.<a> = GF(9); K._cache.exponent()
            2"""
    def fetch_int(self, number) -> FiniteField_givaroElement:
        """Cache_givaro.fetch_int(self, number) -> FiniteField_givaroElement

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 547)

        Given an integer ``n`` return a finite field element in ``self``
        which equals ``n`` under the condition that :meth:`gen()` is set to
        :meth:`characteristic()`.

        EXAMPLES::

            sage: k.<a> = GF(2^8)
            sage: k._cache.fetch_int(8)
            a^3
            sage: e = k._cache.fetch_int(151); e
            a^7 + a^4 + a^2 + a + 1
            sage: 2^7 + 2^4 + 2^2 + 2 + 1
            151"""
    @overload
    def gen(self) -> FiniteField_givaroElement:
        """Cache_givaro.gen(self) -> FiniteField_givaroElement

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 471)

        Return a generator of the field.

        EXAMPLES::

            sage: K.<a> = GF(625)
            sage: K._cache.gen()
            a"""
    @overload
    def gen(self) -> Any:
        """Cache_givaro.gen(self) -> FiniteField_givaroElement

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 471)

        Return a generator of the field.

        EXAMPLES::

            sage: K.<a> = GF(625)
            sage: K._cache.gen()
            a"""
    def int_to_log(self, intn) -> int:
        """Cache_givaro.int_to_log(self, int n) -> int

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 519)

        Given an integer `n` this method returns `i` where `i` satisfies
        `g^i = n \\mod p` where `g` is the generator and `p` is the
        characteristic of ``self``.

        INPUT:

        - ``n`` -- integer representation of a finite field element

        OUTPUT: log representation of ``n``

        EXAMPLES::

            sage: k = GF(7**3, 'a')
            sage: k._cache.int_to_log(4)
            228
            sage: k._cache.int_to_log(3)
            57
            sage: k.gen()^57
            3"""
    def log_to_int(self, intn) -> int:
        """Cache_givaro.log_to_int(self, int n) -> int

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 488)

        Given an integer `n` this method returns `i` where `i`
        satisfies `g^n = i` where `g` is the generator of ``self``; the
        result is interpreted as an integer.

        INPUT:

        - ``n`` -- log representation of a finite field element

        OUTPUT: integer representation of a finite field element

        EXAMPLES::

            sage: k = GF(2**8, 'a')
            sage: k._cache.log_to_int(4)
            16
            sage: k._cache.log_to_int(20)
            180"""
    @overload
    def order(self) -> Any:
        """Cache_givaro.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 238)

        Return the order of this field.

        EXAMPLES::

            sage: K.<a> = GF(9)
            sage: K._cache.order()
            9"""
    @overload
    def order(self) -> Any:
        """Cache_givaro.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 238)

        Return the order of this field.

        EXAMPLES::

            sage: K.<a> = GF(9)
            sage: K._cache.order()
            9"""
    @overload
    def order_c(self) -> int:
        """Cache_givaro.order_c(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 250)

        Return the order of this field.

        EXAMPLES::

            sage: K.<a> = GF(9)
            sage: K._cache.order_c()
            9"""
    @overload
    def order_c(self) -> Any:
        """Cache_givaro.order_c(self) -> int

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 250)

        Return the order of this field.

        EXAMPLES::

            sage: K.<a> = GF(9)
            sage: K._cache.order_c()
            9"""
    @overload
    def random_element(self, *args, **kwds) -> Any:
        """Cache_givaro.random_element(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 273)

        Return a random element of ``self``.

        EXAMPLES::

            sage: k = GF(23**3, 'a')
            sage: e = k._cache.random_element()
            sage: e.parent() is k
            True
            sage: type(e)
            <class 'sage.rings.finite_rings.element_givaro.FiniteField_givaroElement'>

            sage: P.<x> = PowerSeriesRing(GF(3^3, 'a'))
            sage: P.random_element(5).parent() is P
            True"""
    @overload
    def random_element(self) -> Any:
        """Cache_givaro.random_element(self, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 273)

        Return a random element of ``self``.

        EXAMPLES::

            sage: k = GF(23**3, 'a')
            sage: e = k._cache.random_element()
            sage: e.parent() is k
            True
            sage: type(e)
            <class 'sage.rings.finite_rings.element_givaro.FiniteField_givaroElement'>

            sage: P.<x> = PowerSeriesRing(GF(3^3, 'a'))
            sage: P.random_element(5).parent() is P
            True"""
    def __reduce__(self) -> Any:
        """Cache_givaro.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 737)

        For pickling.

        TESTS::

            sage: k.<a> = GF(3^8)
            sage: TestSuite(a).run()"""

class FiniteField_givaroElement(sage.rings.finite_rings.element_base.FinitePolyExtElement):
    """FiniteField_givaroElement(parent)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 837)

    An element of a (Givaro) finite field."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 842)

                Initialize an element in parent. It's much better to use
                parent(<value>) or any specialized method of parent
                like gen() instead. In general do not call this
                constructor directly.

                Alternatively you may provide a value which is directly
                assigned to this element. So the value must represent the
                log_g of the value you wish to assign.

                INPUT:

                - ``parent`` -- base field

                OUTPUT: a finite field element

                EXAMPLES::

                    sage: k.<a> = GF(5^2)
                    sage: from sage.rings.finite_rings.element_givaro import FiniteField_givaroElement
                    sage: FiniteField_givaroElement(k)
                    0
        """
    @overload
    def is_one(self) -> Any:
        """FiniteField_givaroElement.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 921)

        Return ``True`` if ``self == k(1)``.

        EXAMPLES::

            sage: k.<a> = GF(3^4); k
            Finite Field in a of size 3^4
            sage: a.is_one()
            False
            sage: k(1).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """FiniteField_givaroElement.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 921)

        Return ``True`` if ``self == k(1)``.

        EXAMPLES::

            sage: k.<a> = GF(3^4); k
            Finite Field in a of size 3^4
            sage: a.is_one()
            False
            sage: k(1).is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """FiniteField_givaroElement.is_one(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 921)

        Return ``True`` if ``self == k(1)``.

        EXAMPLES::

            sage: k.<a> = GF(3^4); k
            Finite Field in a of size 3^4
            sage: a.is_one()
            False
            sage: k(1).is_one()
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteField_givaroElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 956)

        Return ``True`` if ``self`` is a square in ``self.parent()``.

        ALGORITHM:

        Elements are stored as powers of generators, so we simply check
        to see if it is an even power of a generator.

        EXAMPLES::

            sage: k.<a> = GF(9); k
            Finite Field in a of size 3^2
            sage: a.is_square()
            False
            sage: v = set([x^2 for x in k])
            sage: [x.is_square() for x in v]
            [True, True, True, True, True]
            sage: [x.is_square() for x in k if not x in v]
            [False, False, False, False]

        TESTS::

            sage: K = GF(27, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(25, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(16, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteField_givaroElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 956)

        Return ``True`` if ``self`` is a square in ``self.parent()``.

        ALGORITHM:

        Elements are stored as powers of generators, so we simply check
        to see if it is an even power of a generator.

        EXAMPLES::

            sage: k.<a> = GF(9); k
            Finite Field in a of size 3^2
            sage: a.is_square()
            False
            sage: v = set([x^2 for x in k])
            sage: [x.is_square() for x in v]
            [True, True, True, True, True]
            sage: [x.is_square() for x in k if not x in v]
            [False, False, False, False]

        TESTS::

            sage: K = GF(27, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(25, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(16, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteField_givaroElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 956)

        Return ``True`` if ``self`` is a square in ``self.parent()``.

        ALGORITHM:

        Elements are stored as powers of generators, so we simply check
        to see if it is an even power of a generator.

        EXAMPLES::

            sage: k.<a> = GF(9); k
            Finite Field in a of size 3^2
            sage: a.is_square()
            False
            sage: v = set([x^2 for x in k])
            sage: [x.is_square() for x in v]
            [True, True, True, True, True]
            sage: [x.is_square() for x in k if not x in v]
            [False, False, False, False]

        TESTS::

            sage: K = GF(27, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(25, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(16, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteField_givaroElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 956)

        Return ``True`` if ``self`` is a square in ``self.parent()``.

        ALGORITHM:

        Elements are stored as powers of generators, so we simply check
        to see if it is an even power of a generator.

        EXAMPLES::

            sage: k.<a> = GF(9); k
            Finite Field in a of size 3^2
            sage: a.is_square()
            False
            sage: v = set([x^2 for x in k])
            sage: [x.is_square() for x in v]
            [True, True, True, True, True]
            sage: [x.is_square() for x in k if not x in v]
            [False, False, False, False]

        TESTS::

            sage: K = GF(27, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(25, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(16, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteField_givaroElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 956)

        Return ``True`` if ``self`` is a square in ``self.parent()``.

        ALGORITHM:

        Elements are stored as powers of generators, so we simply check
        to see if it is an even power of a generator.

        EXAMPLES::

            sage: k.<a> = GF(9); k
            Finite Field in a of size 3^2
            sage: a.is_square()
            False
            sage: v = set([x^2 for x in k])
            sage: [x.is_square() for x in v]
            [True, True, True, True, True]
            sage: [x.is_square() for x in k if not x in v]
            [False, False, False, False]

        TESTS::

            sage: K = GF(27, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(25, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(16, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteField_givaroElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 956)

        Return ``True`` if ``self`` is a square in ``self.parent()``.

        ALGORITHM:

        Elements are stored as powers of generators, so we simply check
        to see if it is an even power of a generator.

        EXAMPLES::

            sage: k.<a> = GF(9); k
            Finite Field in a of size 3^2
            sage: a.is_square()
            False
            sage: v = set([x^2 for x in k])
            sage: [x.is_square() for x in v]
            [True, True, True, True, True]
            sage: [x.is_square() for x in k if not x in v]
            [False, False, False, False]

        TESTS::

            sage: K = GF(27, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(25, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(16, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True"""
    @overload
    def is_square(self) -> Any:
        """FiniteField_givaroElement.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 956)

        Return ``True`` if ``self`` is a square in ``self.parent()``.

        ALGORITHM:

        Elements are stored as powers of generators, so we simply check
        to see if it is an even power of a generator.

        EXAMPLES::

            sage: k.<a> = GF(9); k
            Finite Field in a of size 3^2
            sage: a.is_square()
            False
            sage: v = set([x^2 for x in k])
            sage: [x.is_square() for x in v]
            [True, True, True, True, True]
            sage: [x.is_square() for x in k if not x in v]
            [False, False, False, False]

        TESTS::

            sage: K = GF(27, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(25, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True
            sage: K = GF(16, 'a')
            sage: set([a*a for a in K]) == set([a for a in K if a.is_square()])
            True"""
    @overload
    def is_unit(self) -> Any:
        """FiniteField_givaroElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 936)

        Return ``True`` if ``self`` is nonzero, so it is a unit as an element of
        the finite field.

        EXAMPLES::

            sage: k.<a> = GF(3^4); k
            Finite Field in a of size 3^4
            sage: a.is_unit()
            True
            sage: k(0).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """FiniteField_givaroElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 936)

        Return ``True`` if ``self`` is nonzero, so it is a unit as an element of
        the finite field.

        EXAMPLES::

            sage: k.<a> = GF(3^4); k
            Finite Field in a of size 3^4
            sage: a.is_unit()
            True
            sage: k(0).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """FiniteField_givaroElement.is_unit(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 936)

        Return ``True`` if ``self`` is nonzero, so it is a unit as an element of
        the finite field.

        EXAMPLES::

            sage: k.<a> = GF(3^4); k
            Finite Field in a of size 3^4
            sage: a.is_unit()
            True
            sage: k(0).is_unit()
            False"""
    def log(self, base, order=..., check=...) -> Any:
        """FiniteField_givaroElement.log(self, base, order=None, *, check=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1402)

        Return the log to the base `b` of ``self``, i.e., an integer `n`
        such that `b^n =` ``self``.

        INPUT:

        - ``base`` -- non-zero field element
        - ``order`` -- integer (optional), multiple of order of ``base``
        - ``check`` -- boolean (default: ``False``): If set,
          test whether the given ``order`` is correct.

        .. WARNING::

            TODO -- This is currently implemented by solving the discrete
            log problem -- which shouldn't be needed because of how finite field
            elements are represented.

        EXAMPLES::

            sage: k.<b> = GF(5^2); k
            Finite Field in b of size 5^2
            sage: a = b^7
            sage: a.log(b)
            7

        TESTS:

        An example for ``check=True``::

            sage: F.<t> = GF(3^5, impl='givaro')
            sage: t.log(t, 3^4, check=True)
            Traceback (most recent call last):
            ...
            ValueError: 81 is not a multiple of the order of the base"""
    @overload
    def multiplicative_order(self) -> Any:
        """FiniteField_givaroElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1560)

        Return the multiplicative order of this field element.

        EXAMPLES::

            sage: S.<b> = GF(5^2); S
            Finite Field in b of size 5^2
            sage: b.multiplicative_order()
            24
            sage: (b^6).multiplicative_order()
            4"""
    @overload
    def multiplicative_order(self) -> Any:
        """FiniteField_givaroElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1560)

        Return the multiplicative order of this field element.

        EXAMPLES::

            sage: S.<b> = GF(5^2); S
            Finite Field in b of size 5^2
            sage: b.multiplicative_order()
            24
            sage: (b^6).multiplicative_order()
            4"""
    @overload
    def multiplicative_order(self) -> Any:
        """FiniteField_givaroElement.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1560)

        Return the multiplicative order of this field element.

        EXAMPLES::

            sage: S.<b> = GF(5^2); S
            Finite Field in b of size 5^2
            sage: b.multiplicative_order()
            24
            sage: (b^6).multiplicative_order()
            4"""
    @overload
    def polynomial(self, name=...) -> Any:
        """FiniteField_givaroElement.polynomial(self, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1487)

        Return ``self`` viewed as a polynomial over
        ``self.parent().prime_subfield()``.

        EXAMPLES::

            sage: k.<b> = GF(5^2); k
            Finite Field in b of size 5^2
            sage: f = (b^2+1).polynomial(); f
            b + 4
            sage: type(f)
            <class 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
            sage: parent(f)
            Univariate Polynomial Ring in b over Finite Field of size 5"""
    @overload
    def polynomial(self) -> Any:
        """FiniteField_givaroElement.polynomial(self, name=None)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1487)

        Return ``self`` viewed as a polynomial over
        ``self.parent().prime_subfield()``.

        EXAMPLES::

            sage: k.<b> = GF(5^2); k
            Finite Field in b of size 5^2
            sage: f = (b^2+1).polynomial(); f
            b + 4
            sage: type(f)
            <class 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
            sage: parent(f)
            Univariate Polynomial Ring in b over Finite Field of size 5"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """FiniteField_givaroElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 997)

        Return a square root of this finite field element in its
        parent, if there is one.  Otherwise, raise a :exc:`ValueError`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise,
          raise a :exc:`ValueError` if the root is not in the base ring.

          .. WARNING::

              this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

            The ``extend`` option is not implemented (yet).

        ALGORITHM:

        ``self`` is stored as `a^k` for some generator `a`.
        Return `a^{k/2}` for even `k`.

        EXAMPLES::

            sage: k.<a> = GF(7^2)
            sage: k(2).sqrt()
            3
            sage: k(3).sqrt()
            2*a + 6
            sage: k(3).sqrt()**2
            3
            sage: k(4).sqrt()
            2
            sage: k.<a> = GF(7^3)
            sage: k(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square.

        TESTS::

            sage: K = GF(49, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(27, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(8, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K.<a> = FiniteField(9)
            sage: a.sqrt(extend = False, all = True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """FiniteField_givaroElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 997)

        Return a square root of this finite field element in its
        parent, if there is one.  Otherwise, raise a :exc:`ValueError`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise,
          raise a :exc:`ValueError` if the root is not in the base ring.

          .. WARNING::

              this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

            The ``extend`` option is not implemented (yet).

        ALGORITHM:

        ``self`` is stored as `a^k` for some generator `a`.
        Return `a^{k/2}` for even `k`.

        EXAMPLES::

            sage: k.<a> = GF(7^2)
            sage: k(2).sqrt()
            3
            sage: k(3).sqrt()
            2*a + 6
            sage: k(3).sqrt()**2
            3
            sage: k(4).sqrt()
            2
            sage: k.<a> = GF(7^3)
            sage: k(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square.

        TESTS::

            sage: K = GF(49, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(27, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(8, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K.<a> = FiniteField(9)
            sage: a.sqrt(extend = False, all = True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """FiniteField_givaroElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 997)

        Return a square root of this finite field element in its
        parent, if there is one.  Otherwise, raise a :exc:`ValueError`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise,
          raise a :exc:`ValueError` if the root is not in the base ring.

          .. WARNING::

              this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

            The ``extend`` option is not implemented (yet).

        ALGORITHM:

        ``self`` is stored as `a^k` for some generator `a`.
        Return `a^{k/2}` for even `k`.

        EXAMPLES::

            sage: k.<a> = GF(7^2)
            sage: k(2).sqrt()
            3
            sage: k(3).sqrt()
            2*a + 6
            sage: k(3).sqrt()**2
            3
            sage: k(4).sqrt()
            2
            sage: k.<a> = GF(7^3)
            sage: k(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square.

        TESTS::

            sage: K = GF(49, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(27, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(8, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K.<a> = FiniteField(9)
            sage: a.sqrt(extend = False, all = True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """FiniteField_givaroElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 997)

        Return a square root of this finite field element in its
        parent, if there is one.  Otherwise, raise a :exc:`ValueError`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise,
          raise a :exc:`ValueError` if the root is not in the base ring.

          .. WARNING::

              this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

            The ``extend`` option is not implemented (yet).

        ALGORITHM:

        ``self`` is stored as `a^k` for some generator `a`.
        Return `a^{k/2}` for even `k`.

        EXAMPLES::

            sage: k.<a> = GF(7^2)
            sage: k(2).sqrt()
            3
            sage: k(3).sqrt()
            2*a + 6
            sage: k(3).sqrt()**2
            3
            sage: k(4).sqrt()
            2
            sage: k.<a> = GF(7^3)
            sage: k(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square.

        TESTS::

            sage: K = GF(49, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(27, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(8, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K.<a> = FiniteField(9)
            sage: a.sqrt(extend = False, all = True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """FiniteField_givaroElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 997)

        Return a square root of this finite field element in its
        parent, if there is one.  Otherwise, raise a :exc:`ValueError`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise,
          raise a :exc:`ValueError` if the root is not in the base ring.

          .. WARNING::

              this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

            The ``extend`` option is not implemented (yet).

        ALGORITHM:

        ``self`` is stored as `a^k` for some generator `a`.
        Return `a^{k/2}` for even `k`.

        EXAMPLES::

            sage: k.<a> = GF(7^2)
            sage: k(2).sqrt()
            3
            sage: k(3).sqrt()
            2*a + 6
            sage: k(3).sqrt()**2
            3
            sage: k(4).sqrt()
            2
            sage: k.<a> = GF(7^3)
            sage: k(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square.

        TESTS::

            sage: K = GF(49, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(27, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(8, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K.<a> = FiniteField(9)
            sage: a.sqrt(extend = False, all = True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """FiniteField_givaroElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 997)

        Return a square root of this finite field element in its
        parent, if there is one.  Otherwise, raise a :exc:`ValueError`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise,
          raise a :exc:`ValueError` if the root is not in the base ring.

          .. WARNING::

              this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

            The ``extend`` option is not implemented (yet).

        ALGORITHM:

        ``self`` is stored as `a^k` for some generator `a`.
        Return `a^{k/2}` for even `k`.

        EXAMPLES::

            sage: k.<a> = GF(7^2)
            sage: k(2).sqrt()
            3
            sage: k(3).sqrt()
            2*a + 6
            sage: k(3).sqrt()**2
            3
            sage: k(4).sqrt()
            2
            sage: k.<a> = GF(7^3)
            sage: k(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square.

        TESTS::

            sage: K = GF(49, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(27, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(8, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K.<a> = FiniteField(9)
            sage: a.sqrt(extend = False, all = True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """FiniteField_givaroElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 997)

        Return a square root of this finite field element in its
        parent, if there is one.  Otherwise, raise a :exc:`ValueError`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise,
          raise a :exc:`ValueError` if the root is not in the base ring.

          .. WARNING::

              this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

            The ``extend`` option is not implemented (yet).

        ALGORITHM:

        ``self`` is stored as `a^k` for some generator `a`.
        Return `a^{k/2}` for even `k`.

        EXAMPLES::

            sage: k.<a> = GF(7^2)
            sage: k(2).sqrt()
            3
            sage: k(3).sqrt()
            2*a + 6
            sage: k(3).sqrt()**2
            3
            sage: k(4).sqrt()
            2
            sage: k.<a> = GF(7^3)
            sage: k(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square.

        TESTS::

            sage: K = GF(49, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(27, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(8, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K.<a> = FiniteField(9)
            sage: a.sqrt(extend = False, all = True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """FiniteField_givaroElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 997)

        Return a square root of this finite field element in its
        parent, if there is one.  Otherwise, raise a :exc:`ValueError`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise,
          raise a :exc:`ValueError` if the root is not in the base ring.

          .. WARNING::

              this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

            The ``extend`` option is not implemented (yet).

        ALGORITHM:

        ``self`` is stored as `a^k` for some generator `a`.
        Return `a^{k/2}` for even `k`.

        EXAMPLES::

            sage: k.<a> = GF(7^2)
            sage: k(2).sqrt()
            3
            sage: k(3).sqrt()
            2*a + 6
            sage: k(3).sqrt()**2
            3
            sage: k(4).sqrt()
            2
            sage: k.<a> = GF(7^3)
            sage: k(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square.

        TESTS::

            sage: K = GF(49, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(27, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(8, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K.<a> = FiniteField(9)
            sage: a.sqrt(extend = False, all = True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """FiniteField_givaroElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 997)

        Return a square root of this finite field element in its
        parent, if there is one.  Otherwise, raise a :exc:`ValueError`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise,
          raise a :exc:`ValueError` if the root is not in the base ring.

          .. WARNING::

              this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

            The ``extend`` option is not implemented (yet).

        ALGORITHM:

        ``self`` is stored as `a^k` for some generator `a`.
        Return `a^{k/2}` for even `k`.

        EXAMPLES::

            sage: k.<a> = GF(7^2)
            sage: k(2).sqrt()
            3
            sage: k(3).sqrt()
            2*a + 6
            sage: k(3).sqrt()**2
            3
            sage: k(4).sqrt()
            2
            sage: k.<a> = GF(7^3)
            sage: k(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square.

        TESTS::

            sage: K = GF(49, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(27, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(8, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K.<a> = FiniteField(9)
            sage: a.sqrt(extend = False, all = True)
            []"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """FiniteField_givaroElement.sqrt(self, extend=False, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 997)

        Return a square root of this finite field element in its
        parent, if there is one.  Otherwise, raise a :exc:`ValueError`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise,
          raise a :exc:`ValueError` if the root is not in the base ring.

          .. WARNING::

              this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          square roots of ``self``, instead of just one

        .. WARNING::

            The ``extend`` option is not implemented (yet).

        ALGORITHM:

        ``self`` is stored as `a^k` for some generator `a`.
        Return `a^{k/2}` for even `k`.

        EXAMPLES::

            sage: k.<a> = GF(7^2)
            sage: k(2).sqrt()
            3
            sage: k(3).sqrt()
            2*a + 6
            sage: k(3).sqrt()**2
            3
            sage: k(4).sqrt()
            2
            sage: k.<a> = GF(7^3)
            sage: k(3).sqrt()
            Traceback (most recent call last):
            ...
            ValueError: must be a perfect square.

        TESTS::

            sage: K = GF(49, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(27, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K = GF(8, 'a')
            sage: all(a.sqrt()*a.sqrt() == a for a in K if a.is_square())
            True
            sage: K.<a> = FiniteField(9)
            sage: a.sqrt(extend = False, all = True)
            []"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """FiniteField_givaroElement.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1593)

        Return a copy of this element.  Actually just returns ``self``, since
        finite field elements are immutable.

        EXAMPLES::

            sage: S.<b> = GF(5^2); S
            Finite Field in b of size 5^2
            sage: c = copy(b); c
            b
            sage: c is b
            True
            sage: copy(5r) == 5r
            True"""
    def __deepcopy__(self, memo) -> Any:
        """FiniteField_givaroElement.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1611)

        EXAMPLES::

            sage: S.<b> = GF(5^2); S
            Finite Field in b of size 5^2
            sage: c = deepcopy(b); c
            b
            sage: c is b
            True"""
    def __hash__(self) -> Any:
        """FiniteField_givaroElement.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1663)

        Return the hash of this finite field element.  We hash the parent
        and the underlying integer representation of this element.

        EXAMPLES::

            sage: S.<a> = GF(5^3); S
            Finite Field in a of size 5^3
            sage: hash(a)
            5"""
    def __int__(self) -> Any:
        """FiniteField_givaroElement.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1309)

        Return the int representation of ``self``.  When ``self`` is in the
        prime subfield, the integer returned is equal to ``self``, otherwise
        an error is raised.

        EXAMPLES::

            sage: k.<b> = GF(5^2); k
            Finite Field in b of size 5^2
            sage: int(k(4))
            4
            sage: int(b)
            Traceback (most recent call last):
            ...
            TypeError: Cannot coerce element to an integer."""
    def __invert__(self) -> Any:
        """FiniteField_givaroElement.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1160)

        Return the multiplicative inverse of an element.

        EXAMPLES::

            sage: k.<a> = GF(9); k
            Finite Field in a of size 3^2
            sage: ~a
            a + 2
            sage: ~a*a
            1

        TESTS:

        Check that trying to invert zero raises an error
        (see :issue:`12217`)::

            sage: F = GF(25, 'a')
            sage: z = F(0)
            sage: ~z
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero in finite field"""
    def __neg__(self) -> Any:
        """FiniteField_givaroElement.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1144)

        Negative of an element.

        EXAMPLES::

            sage: k.<a> = GF(9); k
            Finite Field in a of size 3^2
            sage: -a
            2*a"""
    def __pow__(self, FiniteField_givaroElementself, exp, other) -> Any:
        """FiniteField_givaroElement.__pow__(FiniteField_givaroElement self, exp, other)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1191)

        EXAMPLES::

            sage: K.<a> = GF(3^3, 'a')
            sage: a^3 == a*a*a
            True
            sage: b = a+1
            sage: b^5 == b^2 * b^3
            True
            sage: b^(-1) == 1/b
            True
            sage: b = K(-1)
            sage: b^2 == 1
            True

        TESTS:

        The following checks that :issue:`7923` is resolved::

            sage: K.<a> = GF(3^10)
            sage: b = a^9 + a^7 + 2*a^6 + a^4 + a^3 + 2*a^2 + a + 2
            sage: b^(71*7381) == (b^71)^7381
            True

        We define ``0^0`` to be unity, :issue:`13897`::

            sage: K.<a> = GF(3^10)
            sage: K(0)^0
            1

        The value returned from ``0^0`` should belong to our ring::

            sage: K.<a> = GF(3^10)
            sage: type(K(0)^0) == type(K(0))
            True

        ALGORITHM:

        Givaro objects are stored as integers `i` such that ``self`` `= a^i`,
        where `a` is a generator of `K` (though not necessarily the one
        returned by ``K.gens()``).  Now it is trivial to compute
        `(a^i)^e = a^{i \\cdot e}`, and reducing the exponent
        mod the multiplicative order of `K`.

        AUTHOR:

        - Robert Bradshaw"""
    def __reduce__(self) -> Any:
        """FiniteField_givaroElement.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 1728)

        Used for supporting pickling of finite field elements.

        EXAMPLES::

            sage: k = GF(2**8, 'a')
            sage: e = k.random_element()
            sage: TestSuite(e).run() # indirect doctest"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class FiniteField_givaro_iterator:
    """FiniteField_givaro_iterator(Cache_givaro cache)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 770)

    Iterator over :class:`FiniteField_givaro` elements.  We iterate
    multiplicatively, as powers of a fixed internal generator.

    EXAMPLES::

        sage: for x in GF(2^2,'a'): print(x)
        0
        a
        a + 1
        1"""
    def __init__(self, Cache_givarocache) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 784)

                EXAMPLES::

                    sage: k.<a> = GF(3^4)
                    sage: i = iter(k) # indirect doctest
                    sage: i
                    Iterator over Finite Field in a of size 3^4
        """
    def __iter__(self) -> Any:
        """FiniteField_givaro_iterator.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 826)

        EXAMPLES::

            sage: K.<a> = GF(4)
            sage: K.list() # indirect doctest
            [0, a, a + 1, 1]"""
    def __next__(self) -> Any:
        """FiniteField_givaro_iterator.__next__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/element_givaro.pyx (starting at line 796)

        EXAMPLES::

            sage: k.<a> = GF(3^4)
            sage: i = iter(k) # indirect doctest
            sage: next(i)
            0
            sage: next(i)
            a"""
