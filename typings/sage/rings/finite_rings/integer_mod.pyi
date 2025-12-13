import _cython_3_2_1
import cypari2.pari_instance
import sage as sage
import sage.categories.map
import sage.categories.morphism
import sage.rings.finite_rings.element_base
import sage.rings.integer_ring as integer_ring
import sage.rings.rational as rational
from sage.arith.functions import lcm as lcm
from sage.arith.misc import crt as crt
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.structure.element import coerce_binop as coerce_binop, have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

IntegerMod: _cython_3_2_1.cython_function_or_method
Mod: _cython_3_2_1.cython_function_or_method
__pyx_capi__: dict
is_IntegerMod: _cython_3_2_1.cython_function_or_method
lucas: _cython_3_2_1.cython_function_or_method
lucas_q1: _cython_3_2_1.cython_function_or_method
mod: _cython_3_2_1.cython_function_or_method
pari: cypari2.pari_instance.Pari
square_root_mod_prime: _cython_3_2_1.cython_function_or_method
square_root_mod_prime_power: _cython_3_2_1.cython_function_or_method

class Int_to_IntegerMod(IntegerMod_hom):
    """Int_to_IntegerMod(R)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4541)

    EXAMPLES:

    We make sure it works for every type.

    ::

        sage: from sage.rings.finite_rings.integer_mod import Int_to_IntegerMod
        sage: Rs = [Integers(2**k) for k in range(1,50,10)]
        sage: [type(R(0)) for R in Rs]
        [<class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>,
         <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>,
         <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int64'>,
         <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>,
         <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>]
        sage: fs = [Int_to_IntegerMod(R) for R in Rs]
        sage: [f(-1) for f in fs]
        [1, 2047, 2097151, 2147483647, 2199023255551]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4561)"""
    @overload
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4561)"""

class IntegerMod_abstract(sage.rings.finite_rings.element_base.FiniteRingElement):
    """IntegerMod_abstract(parent, value=None)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, value=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 342)

                EXAMPLES::

                    sage: a = Mod(10, 30^10); a
                    10
                    sage: type(a)
                    <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>
                    sage: loads(a.dumps()) == a
                    True

                TESTS::

                    sage: TestSuite(Zmod(1)).run()
                    sage: TestSuite(Zmod(2)).run()
                    sage: TestSuite(Zmod(3)).run()
                    sage: TestSuite(Zmod(4)).run()
                    sage: TestSuite(Zmod(5)).run()
                    sage: TestSuite(Zmod(6)).run()
                    sage: TestSuite(Zmod(2^10 * 3^5)).run()
                    sage: TestSuite(Zmod(2^30 * 3^50 * 5^20)).run()

                    sage: GF(29)(SR(1/3))                                                       # needs sage.rings.finite_rings sage.symbolic
                    10
                    sage: Integers(30)(QQ['x'](1/7))
                    13
                    sage: Integers(30)(SR(1/4))                                                 # needs sage.symbolic
                    Traceback (most recent call last):
                    ...
                    ZeroDivisionError: inverse of Mod(4, 30) does not exist
        """
    @overload
    def additive_order(self) -> Any:
        """IntegerMod_abstract.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1769)

        Return the additive order of ``self``.

        This is the same as ``self.order()``.

        EXAMPLES::

            sage: Integers(20)(2).additive_order()
            10
            sage: Integers(20)(7).additive_order()
            20
            sage: Integers(90308402384902)(2).additive_order()
            45154201192451"""
    @overload
    def additive_order(self) -> Any:
        """IntegerMod_abstract.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1769)

        Return the additive order of ``self``.

        This is the same as ``self.order()``.

        EXAMPLES::

            sage: Integers(20)(2).additive_order()
            10
            sage: Integers(20)(7).additive_order()
            20
            sage: Integers(90308402384902)(2).additive_order()
            45154201192451"""
    @overload
    def additive_order(self) -> Any:
        """IntegerMod_abstract.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1769)

        Return the additive order of ``self``.

        This is the same as ``self.order()``.

        EXAMPLES::

            sage: Integers(20)(2).additive_order()
            10
            sage: Integers(20)(7).additive_order()
            20
            sage: Integers(90308402384902)(2).additive_order()
            45154201192451"""
    @overload
    def additive_order(self) -> Any:
        """IntegerMod_abstract.additive_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1769)

        Return the additive order of ``self``.

        This is the same as ``self.order()``.

        EXAMPLES::

            sage: Integers(20)(2).additive_order()
            10
            sage: Integers(20)(7).additive_order()
            20
            sage: Integers(90308402384902)(2).additive_order()
            45154201192451"""
    def charpoly(self, var=...) -> Any:
        """IntegerMod_abstract.charpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 900)

        Return the characteristic polynomial of this element.

        EXAMPLES::

            sage: k = GF(3)
            sage: a = k.gen()
            sage: a.charpoly('x')
            x + 2
            sage: a + 2
            0

        AUTHORS:

        - Craig Citro"""
    @overload
    def crt(self, IntegerMod_abstractother) -> Any:
        """IntegerMod_abstract.crt(self, IntegerMod_abstract other)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1695)

        Use the Chinese Remainder Theorem to find an element of the
        integers modulo the product of the moduli that reduces to
        ``self`` and to ``other``. The modulus of
        ``other`` must be coprime to the modulus of
        ``self``.

        EXAMPLES::

            sage: a = mod(3, 5)
            sage: b = mod(2, 7)
            sage: a.crt(b)
            23

        ::

            sage: a = mod(37, 10^8)
            sage: b = mod(9, 3^8)
            sage: a.crt(b)
            125900000037

        ::

            sage: b = mod(0, 1)
            sage: a.crt(b) == a
            True
            sage: a.crt(b).modulus()
            100000000

        TESTS::

            sage: mod(0, 1).crt(mod(4, 2^127))
            4
            sage: mod(4, 2^127).crt(mod(0, 1))
            4
            sage: mod(4, 2^30).crt(mod(0, 1))
            4
            sage: mod(0, 1).crt(mod(4, 2^30))
            4
            sage: mod(0, 1).crt(mod(4, 2^15))
            4
            sage: mod(4, 2^15).crt(mod(0, 1))
            4

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def crt(self, b) -> Any:
        """IntegerMod_abstract.crt(self, IntegerMod_abstract other)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1695)

        Use the Chinese Remainder Theorem to find an element of the
        integers modulo the product of the moduli that reduces to
        ``self`` and to ``other``. The modulus of
        ``other`` must be coprime to the modulus of
        ``self``.

        EXAMPLES::

            sage: a = mod(3, 5)
            sage: b = mod(2, 7)
            sage: a.crt(b)
            23

        ::

            sage: a = mod(37, 10^8)
            sage: b = mod(9, 3^8)
            sage: a.crt(b)
            125900000037

        ::

            sage: b = mod(0, 1)
            sage: a.crt(b) == a
            True
            sage: a.crt(b).modulus()
            100000000

        TESTS::

            sage: mod(0, 1).crt(mod(4, 2^127))
            4
            sage: mod(4, 2^127).crt(mod(0, 1))
            4
            sage: mod(4, 2^30).crt(mod(0, 1))
            4
            sage: mod(0, 1).crt(mod(4, 2^30))
            4
            sage: mod(0, 1).crt(mod(4, 2^15))
            4
            sage: mod(4, 2^15).crt(mod(0, 1))
            4

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def crt(self, b) -> Any:
        """IntegerMod_abstract.crt(self, IntegerMod_abstract other)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1695)

        Use the Chinese Remainder Theorem to find an element of the
        integers modulo the product of the moduli that reduces to
        ``self`` and to ``other``. The modulus of
        ``other`` must be coprime to the modulus of
        ``self``.

        EXAMPLES::

            sage: a = mod(3, 5)
            sage: b = mod(2, 7)
            sage: a.crt(b)
            23

        ::

            sage: a = mod(37, 10^8)
            sage: b = mod(9, 3^8)
            sage: a.crt(b)
            125900000037

        ::

            sage: b = mod(0, 1)
            sage: a.crt(b) == a
            True
            sage: a.crt(b).modulus()
            100000000

        TESTS::

            sage: mod(0, 1).crt(mod(4, 2^127))
            4
            sage: mod(4, 2^127).crt(mod(0, 1))
            4
            sage: mod(4, 2^30).crt(mod(0, 1))
            4
            sage: mod(0, 1).crt(mod(4, 2^30))
            4
            sage: mod(0, 1).crt(mod(4, 2^15))
            4
            sage: mod(4, 2^15).crt(mod(0, 1))
            4

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def crt(self, b) -> Any:
        """IntegerMod_abstract.crt(self, IntegerMod_abstract other)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1695)

        Use the Chinese Remainder Theorem to find an element of the
        integers modulo the product of the moduli that reduces to
        ``self`` and to ``other``. The modulus of
        ``other`` must be coprime to the modulus of
        ``self``.

        EXAMPLES::

            sage: a = mod(3, 5)
            sage: b = mod(2, 7)
            sage: a.crt(b)
            23

        ::

            sage: a = mod(37, 10^8)
            sage: b = mod(9, 3^8)
            sage: a.crt(b)
            125900000037

        ::

            sage: b = mod(0, 1)
            sage: a.crt(b) == a
            True
            sage: a.crt(b).modulus()
            100000000

        TESTS::

            sage: mod(0, 1).crt(mod(4, 2^127))
            4
            sage: mod(4, 2^127).crt(mod(0, 1))
            4
            sage: mod(4, 2^30).crt(mod(0, 1))
            4
            sage: mod(0, 1).crt(mod(4, 2^30))
            4
            sage: mod(0, 1).crt(mod(4, 2^15))
            4
            sage: mod(4, 2^15).crt(mod(0, 1))
            4

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def crt(self, b) -> Any:
        """IntegerMod_abstract.crt(self, IntegerMod_abstract other)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1695)

        Use the Chinese Remainder Theorem to find an element of the
        integers modulo the product of the moduli that reduces to
        ``self`` and to ``other``. The modulus of
        ``other`` must be coprime to the modulus of
        ``self``.

        EXAMPLES::

            sage: a = mod(3, 5)
            sage: b = mod(2, 7)
            sage: a.crt(b)
            23

        ::

            sage: a = mod(37, 10^8)
            sage: b = mod(9, 3^8)
            sage: a.crt(b)
            125900000037

        ::

            sage: b = mod(0, 1)
            sage: a.crt(b) == a
            True
            sage: a.crt(b).modulus()
            100000000

        TESTS::

            sage: mod(0, 1).crt(mod(4, 2^127))
            4
            sage: mod(4, 2^127).crt(mod(0, 1))
            4
            sage: mod(4, 2^30).crt(mod(0, 1))
            4
            sage: mod(0, 1).crt(mod(4, 2^30))
            4
            sage: mod(0, 1).crt(mod(4, 2^15))
            4
            sage: mod(4, 2^15).crt(mod(0, 1))
            4

        AUTHORS:

        - Robert Bradshaw"""
    def divides(self, other) -> Any:
        """IntegerMod_abstract.divides(self, other)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1036)

        Test whether ``self`` divides ``other``.

        EXAMPLES::

            sage: R = Zmod(6)
            sage: R(2).divides(R(4))
            True
            sage: R(4).divides(R(2))
            True
            sage: R(2).divides(R(3))
            False"""
    def generalised_log(self) -> Any:
        """IntegerMod_abstract.generalised_log(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 841)

        Return integers `[n_1, \\ldots, n_d]` such that.

        .. MATH::

            \\prod_{i=1}^d x_i^{n_i} = \\text{self},

        where `x_1, \\dots, x_d` are the generators of the unit group
        returned by ``self.parent().unit_gens()``.

        EXAMPLES::


            sage: m = Mod(3, 1568)
            sage: v = m.generalised_log(); v                                            # needs sage.libs.pari sage.modules
            [1, 3, 1]
            sage: prod([Zmod(1568).unit_gens()[i] ** v[i] for i in [0..2]])             # needs sage.libs.pari sage.modules
            3

        .. SEEALSO::

            The method :meth:`log`.

        .. warning::

            The output is given relative to the set of generators
            obtained by passing ``algorithm='sage'`` to the method
            :meth:`~sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic.unit_gens`
            of the parent (which is the default).  Specifying
            ``algorithm='pari'`` usually yields a different set of
            generators that is incompatible with this method."""
    @overload
    def is_nilpotent(self) -> Any:
        """IntegerMod_abstract.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 512)

        Return ``True`` if ``self`` is nilpotent,
        i.e., some power of ``self`` is zero.

        EXAMPLES::

            sage: a = Integers(90384098234^3)
            sage: factor(a.order())                                                     # needs sage.libs.pari
            2^3 * 191^3 * 236607587^3
            sage: b = a(2*191)
            sage: b.is_nilpotent()
            False
            sage: b = a(2*191*236607587)
            sage: b.is_nilpotent()
            True

        ALGORITHM: Let `m \\geq  \\log_2(n)`, where `n` is
        the modulus. Then `x \\in \\ZZ/n\\ZZ` is
        nilpotent if and only if `x^m = 0`.

        PROOF: This is clear if you reduce to the prime power case, which
        you can do via the Chinese Remainder Theorem.

        We could alternatively factor `n` and check to see if the
        prime divisors of `n` all divide `x`. This is
        asymptotically slower :-)."""
    @overload
    def is_nilpotent(self) -> Any:
        """IntegerMod_abstract.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 512)

        Return ``True`` if ``self`` is nilpotent,
        i.e., some power of ``self`` is zero.

        EXAMPLES::

            sage: a = Integers(90384098234^3)
            sage: factor(a.order())                                                     # needs sage.libs.pari
            2^3 * 191^3 * 236607587^3
            sage: b = a(2*191)
            sage: b.is_nilpotent()
            False
            sage: b = a(2*191*236607587)
            sage: b.is_nilpotent()
            True

        ALGORITHM: Let `m \\geq  \\log_2(n)`, where `n` is
        the modulus. Then `x \\in \\ZZ/n\\ZZ` is
        nilpotent if and only if `x^m = 0`.

        PROOF: This is clear if you reduce to the prime power case, which
        you can do via the Chinese Remainder Theorem.

        We could alternatively factor `n` and check to see if the
        prime divisors of `n` all divide `x`. This is
        asymptotically slower :-)."""
    @overload
    def is_nilpotent(self) -> Any:
        """IntegerMod_abstract.is_nilpotent(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 512)

        Return ``True`` if ``self`` is nilpotent,
        i.e., some power of ``self`` is zero.

        EXAMPLES::

            sage: a = Integers(90384098234^3)
            sage: factor(a.order())                                                     # needs sage.libs.pari
            2^3 * 191^3 * 236607587^3
            sage: b = a(2*191)
            sage: b.is_nilpotent()
            False
            sage: b = a(2*191*236607587)
            sage: b.is_nilpotent()
            True

        ALGORITHM: Let `m \\geq  \\log_2(n)`, where `n` is
        the modulus. Then `x \\in \\ZZ/n\\ZZ` is
        nilpotent if and only if `x^m = 0`.

        PROOF: This is clear if you reduce to the prime power case, which
        you can do via the Chinese Remainder Theorem.

        We could alternatively factor `n` and check to see if the
        prime divisors of `n` all divide `x`. This is
        asymptotically slower :-)."""
    def is_one(self) -> bool:
        """IntegerMod_abstract.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1030)"""
    @overload
    def is_primitive_root(self) -> bool:
        '''IntegerMod_abstract.is_primitive_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1787)

        Determine whether this element generates the group of units modulo n.

        This is only possible if the group of units is cyclic, which occurs if
        n is 2, 4, a power of an odd prime or twice a power of an odd prime.

        EXAMPLES::

            sage: mod(1, 2).is_primitive_root()
            True
            sage: mod(3, 4).is_primitive_root()
            True
            sage: mod(2, 7).is_primitive_root()
            False
            sage: mod(3, 98).is_primitive_root()                                        # needs sage.libs.pari
            True
            sage: mod(11, 1009^2).is_primitive_root()                                   # needs sage.libs.pari
            True

        TESTS::

            sage: for p in prime_range(3,12):                                           # needs sage.libs.pari
            ....:     for k in range(1,4):
            ....:         for even in [1,2]:
            ....:             n = even*p^k
            ....:             phin = euler_phi(n)
            ....:             for _ in range(6):
            ....:                 a = Zmod(n).random_element()
            ....:                 if not a.is_unit(): continue
            ....:                 if a.is_primitive_root().__xor__(a.multiplicative_order()==phin):
            ....:                     print("mod(%s,%s) incorrect" % (a, n))

        `0` is not a primitive root mod `n` (:issue:`23624`) except for `n=0`::

            sage: mod(0, 17).is_primitive_root()
            False
            sage: all(not mod(0, n).is_primitive_root() for n in srange(2, 20))         # needs sage.libs.pari
            True
            sage: mod(0, 1).is_primitive_root()
            True

            sage: all(not mod(p^j, p^k).is_primitive_root()                             # needs sage.libs.pari
            ....:     for p in prime_range(3, 12)
            ....:     for k in srange(1, 4)
            ....:     for j in srange(0, k))
            True'''
    @overload
    def is_primitive_root(self) -> Any:
        '''IntegerMod_abstract.is_primitive_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1787)

        Determine whether this element generates the group of units modulo n.

        This is only possible if the group of units is cyclic, which occurs if
        n is 2, 4, a power of an odd prime or twice a power of an odd prime.

        EXAMPLES::

            sage: mod(1, 2).is_primitive_root()
            True
            sage: mod(3, 4).is_primitive_root()
            True
            sage: mod(2, 7).is_primitive_root()
            False
            sage: mod(3, 98).is_primitive_root()                                        # needs sage.libs.pari
            True
            sage: mod(11, 1009^2).is_primitive_root()                                   # needs sage.libs.pari
            True

        TESTS::

            sage: for p in prime_range(3,12):                                           # needs sage.libs.pari
            ....:     for k in range(1,4):
            ....:         for even in [1,2]:
            ....:             n = even*p^k
            ....:             phin = euler_phi(n)
            ....:             for _ in range(6):
            ....:                 a = Zmod(n).random_element()
            ....:                 if not a.is_unit(): continue
            ....:                 if a.is_primitive_root().__xor__(a.multiplicative_order()==phin):
            ....:                     print("mod(%s,%s) incorrect" % (a, n))

        `0` is not a primitive root mod `n` (:issue:`23624`) except for `n=0`::

            sage: mod(0, 17).is_primitive_root()
            False
            sage: all(not mod(0, n).is_primitive_root() for n in srange(2, 20))         # needs sage.libs.pari
            True
            sage: mod(0, 1).is_primitive_root()
            True

            sage: all(not mod(p^j, p^k).is_primitive_root()                             # needs sage.libs.pari
            ....:     for p in prime_range(3, 12)
            ....:     for k in srange(1, 4)
            ....:     for j in srange(0, k))
            True'''
    @overload
    def is_primitive_root(self) -> Any:
        '''IntegerMod_abstract.is_primitive_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1787)

        Determine whether this element generates the group of units modulo n.

        This is only possible if the group of units is cyclic, which occurs if
        n is 2, 4, a power of an odd prime or twice a power of an odd prime.

        EXAMPLES::

            sage: mod(1, 2).is_primitive_root()
            True
            sage: mod(3, 4).is_primitive_root()
            True
            sage: mod(2, 7).is_primitive_root()
            False
            sage: mod(3, 98).is_primitive_root()                                        # needs sage.libs.pari
            True
            sage: mod(11, 1009^2).is_primitive_root()                                   # needs sage.libs.pari
            True

        TESTS::

            sage: for p in prime_range(3,12):                                           # needs sage.libs.pari
            ....:     for k in range(1,4):
            ....:         for even in [1,2]:
            ....:             n = even*p^k
            ....:             phin = euler_phi(n)
            ....:             for _ in range(6):
            ....:                 a = Zmod(n).random_element()
            ....:                 if not a.is_unit(): continue
            ....:                 if a.is_primitive_root().__xor__(a.multiplicative_order()==phin):
            ....:                     print("mod(%s,%s) incorrect" % (a, n))

        `0` is not a primitive root mod `n` (:issue:`23624`) except for `n=0`::

            sage: mod(0, 17).is_primitive_root()
            False
            sage: all(not mod(0, n).is_primitive_root() for n in srange(2, 20))         # needs sage.libs.pari
            True
            sage: mod(0, 1).is_primitive_root()
            True

            sage: all(not mod(p^j, p^k).is_primitive_root()                             # needs sage.libs.pari
            ....:     for p in prime_range(3, 12)
            ....:     for k in srange(1, 4)
            ....:     for j in srange(0, k))
            True'''
    @overload
    def is_primitive_root(self) -> Any:
        '''IntegerMod_abstract.is_primitive_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1787)

        Determine whether this element generates the group of units modulo n.

        This is only possible if the group of units is cyclic, which occurs if
        n is 2, 4, a power of an odd prime or twice a power of an odd prime.

        EXAMPLES::

            sage: mod(1, 2).is_primitive_root()
            True
            sage: mod(3, 4).is_primitive_root()
            True
            sage: mod(2, 7).is_primitive_root()
            False
            sage: mod(3, 98).is_primitive_root()                                        # needs sage.libs.pari
            True
            sage: mod(11, 1009^2).is_primitive_root()                                   # needs sage.libs.pari
            True

        TESTS::

            sage: for p in prime_range(3,12):                                           # needs sage.libs.pari
            ....:     for k in range(1,4):
            ....:         for even in [1,2]:
            ....:             n = even*p^k
            ....:             phin = euler_phi(n)
            ....:             for _ in range(6):
            ....:                 a = Zmod(n).random_element()
            ....:                 if not a.is_unit(): continue
            ....:                 if a.is_primitive_root().__xor__(a.multiplicative_order()==phin):
            ....:                     print("mod(%s,%s) incorrect" % (a, n))

        `0` is not a primitive root mod `n` (:issue:`23624`) except for `n=0`::

            sage: mod(0, 17).is_primitive_root()
            False
            sage: all(not mod(0, n).is_primitive_root() for n in srange(2, 20))         # needs sage.libs.pari
            True
            sage: mod(0, 1).is_primitive_root()
            True

            sage: all(not mod(p^j, p^k).is_primitive_root()                             # needs sage.libs.pari
            ....:     for p in prime_range(3, 12)
            ....:     for k in srange(1, 4)
            ....:     for j in srange(0, k))
            True'''
    @overload
    def is_primitive_root(self) -> Any:
        '''IntegerMod_abstract.is_primitive_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1787)

        Determine whether this element generates the group of units modulo n.

        This is only possible if the group of units is cyclic, which occurs if
        n is 2, 4, a power of an odd prime or twice a power of an odd prime.

        EXAMPLES::

            sage: mod(1, 2).is_primitive_root()
            True
            sage: mod(3, 4).is_primitive_root()
            True
            sage: mod(2, 7).is_primitive_root()
            False
            sage: mod(3, 98).is_primitive_root()                                        # needs sage.libs.pari
            True
            sage: mod(11, 1009^2).is_primitive_root()                                   # needs sage.libs.pari
            True

        TESTS::

            sage: for p in prime_range(3,12):                                           # needs sage.libs.pari
            ....:     for k in range(1,4):
            ....:         for even in [1,2]:
            ....:             n = even*p^k
            ....:             phin = euler_phi(n)
            ....:             for _ in range(6):
            ....:                 a = Zmod(n).random_element()
            ....:                 if not a.is_unit(): continue
            ....:                 if a.is_primitive_root().__xor__(a.multiplicative_order()==phin):
            ....:                     print("mod(%s,%s) incorrect" % (a, n))

        `0` is not a primitive root mod `n` (:issue:`23624`) except for `n=0`::

            sage: mod(0, 17).is_primitive_root()
            False
            sage: all(not mod(0, n).is_primitive_root() for n in srange(2, 20))         # needs sage.libs.pari
            True
            sage: mod(0, 1).is_primitive_root()
            True

            sage: all(not mod(p^j, p^k).is_primitive_root()                             # needs sage.libs.pari
            ....:     for p in prime_range(3, 12)
            ....:     for k in srange(1, 4)
            ....:     for j in srange(0, k))
            True'''
    @overload
    def is_primitive_root(self) -> Any:
        '''IntegerMod_abstract.is_primitive_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1787)

        Determine whether this element generates the group of units modulo n.

        This is only possible if the group of units is cyclic, which occurs if
        n is 2, 4, a power of an odd prime or twice a power of an odd prime.

        EXAMPLES::

            sage: mod(1, 2).is_primitive_root()
            True
            sage: mod(3, 4).is_primitive_root()
            True
            sage: mod(2, 7).is_primitive_root()
            False
            sage: mod(3, 98).is_primitive_root()                                        # needs sage.libs.pari
            True
            sage: mod(11, 1009^2).is_primitive_root()                                   # needs sage.libs.pari
            True

        TESTS::

            sage: for p in prime_range(3,12):                                           # needs sage.libs.pari
            ....:     for k in range(1,4):
            ....:         for even in [1,2]:
            ....:             n = even*p^k
            ....:             phin = euler_phi(n)
            ....:             for _ in range(6):
            ....:                 a = Zmod(n).random_element()
            ....:                 if not a.is_unit(): continue
            ....:                 if a.is_primitive_root().__xor__(a.multiplicative_order()==phin):
            ....:                     print("mod(%s,%s) incorrect" % (a, n))

        `0` is not a primitive root mod `n` (:issue:`23624`) except for `n=0`::

            sage: mod(0, 17).is_primitive_root()
            False
            sage: all(not mod(0, n).is_primitive_root() for n in srange(2, 20))         # needs sage.libs.pari
            True
            sage: mod(0, 1).is_primitive_root()
            True

            sage: all(not mod(p^j, p^k).is_primitive_root()                             # needs sage.libs.pari
            ....:     for p in prime_range(3, 12)
            ....:     for k in srange(1, 4)
            ....:     for j in srange(0, k))
            True'''
    @overload
    def is_primitive_root(self) -> Any:
        '''IntegerMod_abstract.is_primitive_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1787)

        Determine whether this element generates the group of units modulo n.

        This is only possible if the group of units is cyclic, which occurs if
        n is 2, 4, a power of an odd prime or twice a power of an odd prime.

        EXAMPLES::

            sage: mod(1, 2).is_primitive_root()
            True
            sage: mod(3, 4).is_primitive_root()
            True
            sage: mod(2, 7).is_primitive_root()
            False
            sage: mod(3, 98).is_primitive_root()                                        # needs sage.libs.pari
            True
            sage: mod(11, 1009^2).is_primitive_root()                                   # needs sage.libs.pari
            True

        TESTS::

            sage: for p in prime_range(3,12):                                           # needs sage.libs.pari
            ....:     for k in range(1,4):
            ....:         for even in [1,2]:
            ....:             n = even*p^k
            ....:             phin = euler_phi(n)
            ....:             for _ in range(6):
            ....:                 a = Zmod(n).random_element()
            ....:                 if not a.is_unit(): continue
            ....:                 if a.is_primitive_root().__xor__(a.multiplicative_order()==phin):
            ....:                     print("mod(%s,%s) incorrect" % (a, n))

        `0` is not a primitive root mod `n` (:issue:`23624`) except for `n=0`::

            sage: mod(0, 17).is_primitive_root()
            False
            sage: all(not mod(0, n).is_primitive_root() for n in srange(2, 20))         # needs sage.libs.pari
            True
            sage: mod(0, 1).is_primitive_root()
            True

            sage: all(not mod(p^j, p^k).is_primitive_root()                             # needs sage.libs.pari
            ....:     for p in prime_range(3, 12)
            ....:     for k in srange(1, 4)
            ....:     for j in srange(0, k))
            True'''
    @overload
    def is_primitive_root(self) -> Any:
        '''IntegerMod_abstract.is_primitive_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1787)

        Determine whether this element generates the group of units modulo n.

        This is only possible if the group of units is cyclic, which occurs if
        n is 2, 4, a power of an odd prime or twice a power of an odd prime.

        EXAMPLES::

            sage: mod(1, 2).is_primitive_root()
            True
            sage: mod(3, 4).is_primitive_root()
            True
            sage: mod(2, 7).is_primitive_root()
            False
            sage: mod(3, 98).is_primitive_root()                                        # needs sage.libs.pari
            True
            sage: mod(11, 1009^2).is_primitive_root()                                   # needs sage.libs.pari
            True

        TESTS::

            sage: for p in prime_range(3,12):                                           # needs sage.libs.pari
            ....:     for k in range(1,4):
            ....:         for even in [1,2]:
            ....:             n = even*p^k
            ....:             phin = euler_phi(n)
            ....:             for _ in range(6):
            ....:                 a = Zmod(n).random_element()
            ....:                 if not a.is_unit(): continue
            ....:                 if a.is_primitive_root().__xor__(a.multiplicative_order()==phin):
            ....:                     print("mod(%s,%s) incorrect" % (a, n))

        `0` is not a primitive root mod `n` (:issue:`23624`) except for `n=0`::

            sage: mod(0, 17).is_primitive_root()
            False
            sage: all(not mod(0, n).is_primitive_root() for n in srange(2, 20))         # needs sage.libs.pari
            True
            sage: mod(0, 1).is_primitive_root()
            True

            sage: all(not mod(p^j, p^k).is_primitive_root()                             # needs sage.libs.pari
            ....:     for p in prime_range(3, 12)
            ....:     for k in srange(1, 4)
            ....:     for j in srange(0, k))
            True'''
    @overload
    def is_primitive_root(self) -> Any:
        '''IntegerMod_abstract.is_primitive_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1787)

        Determine whether this element generates the group of units modulo n.

        This is only possible if the group of units is cyclic, which occurs if
        n is 2, 4, a power of an odd prime or twice a power of an odd prime.

        EXAMPLES::

            sage: mod(1, 2).is_primitive_root()
            True
            sage: mod(3, 4).is_primitive_root()
            True
            sage: mod(2, 7).is_primitive_root()
            False
            sage: mod(3, 98).is_primitive_root()                                        # needs sage.libs.pari
            True
            sage: mod(11, 1009^2).is_primitive_root()                                   # needs sage.libs.pari
            True

        TESTS::

            sage: for p in prime_range(3,12):                                           # needs sage.libs.pari
            ....:     for k in range(1,4):
            ....:         for even in [1,2]:
            ....:             n = even*p^k
            ....:             phin = euler_phi(n)
            ....:             for _ in range(6):
            ....:                 a = Zmod(n).random_element()
            ....:                 if not a.is_unit(): continue
            ....:                 if a.is_primitive_root().__xor__(a.multiplicative_order()==phin):
            ....:                     print("mod(%s,%s) incorrect" % (a, n))

        `0` is not a primitive root mod `n` (:issue:`23624`) except for `n=0`::

            sage: mod(0, 17).is_primitive_root()
            False
            sage: all(not mod(0, n).is_primitive_root() for n in srange(2, 20))         # needs sage.libs.pari
            True
            sage: mod(0, 1).is_primitive_root()
            True

            sage: all(not mod(p^j, p^k).is_primitive_root()                             # needs sage.libs.pari
            ....:     for p in prime_range(3, 12)
            ....:     for k in srange(1, 4)
            ....:     for j in srange(0, k))
            True'''
    @overload
    def is_primitive_root(self) -> Any:
        '''IntegerMod_abstract.is_primitive_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1787)

        Determine whether this element generates the group of units modulo n.

        This is only possible if the group of units is cyclic, which occurs if
        n is 2, 4, a power of an odd prime or twice a power of an odd prime.

        EXAMPLES::

            sage: mod(1, 2).is_primitive_root()
            True
            sage: mod(3, 4).is_primitive_root()
            True
            sage: mod(2, 7).is_primitive_root()
            False
            sage: mod(3, 98).is_primitive_root()                                        # needs sage.libs.pari
            True
            sage: mod(11, 1009^2).is_primitive_root()                                   # needs sage.libs.pari
            True

        TESTS::

            sage: for p in prime_range(3,12):                                           # needs sage.libs.pari
            ....:     for k in range(1,4):
            ....:         for even in [1,2]:
            ....:             n = even*p^k
            ....:             phin = euler_phi(n)
            ....:             for _ in range(6):
            ....:                 a = Zmod(n).random_element()
            ....:                 if not a.is_unit(): continue
            ....:                 if a.is_primitive_root().__xor__(a.multiplicative_order()==phin):
            ....:                     print("mod(%s,%s) incorrect" % (a, n))

        `0` is not a primitive root mod `n` (:issue:`23624`) except for `n=0`::

            sage: mod(0, 17).is_primitive_root()
            False
            sage: all(not mod(0, n).is_primitive_root() for n in srange(2, 20))         # needs sage.libs.pari
            True
            sage: mod(0, 1).is_primitive_root()
            True

            sage: all(not mod(p^j, p^k).is_primitive_root()                             # needs sage.libs.pari
            ....:     for p in prime_range(3, 12)
            ....:     for k in srange(1, 4)
            ....:     for j in srange(0, k))
            True'''
    @overload
    def is_primitive_root(self) -> Any:
        '''IntegerMod_abstract.is_primitive_root(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1787)

        Determine whether this element generates the group of units modulo n.

        This is only possible if the group of units is cyclic, which occurs if
        n is 2, 4, a power of an odd prime or twice a power of an odd prime.

        EXAMPLES::

            sage: mod(1, 2).is_primitive_root()
            True
            sage: mod(3, 4).is_primitive_root()
            True
            sage: mod(2, 7).is_primitive_root()
            False
            sage: mod(3, 98).is_primitive_root()                                        # needs sage.libs.pari
            True
            sage: mod(11, 1009^2).is_primitive_root()                                   # needs sage.libs.pari
            True

        TESTS::

            sage: for p in prime_range(3,12):                                           # needs sage.libs.pari
            ....:     for k in range(1,4):
            ....:         for even in [1,2]:
            ....:             n = even*p^k
            ....:             phin = euler_phi(n)
            ....:             for _ in range(6):
            ....:                 a = Zmod(n).random_element()
            ....:                 if not a.is_unit(): continue
            ....:                 if a.is_primitive_root().__xor__(a.multiplicative_order()==phin):
            ....:                     print("mod(%s,%s) incorrect" % (a, n))

        `0` is not a primitive root mod `n` (:issue:`23624`) except for `n=0`::

            sage: mod(0, 17).is_primitive_root()
            False
            sage: all(not mod(0, n).is_primitive_root() for n in srange(2, 20))         # needs sage.libs.pari
            True
            sage: mod(0, 1).is_primitive_root()
            True

            sage: all(not mod(p^j, p^k).is_primitive_root()                             # needs sage.libs.pari
            ....:     for p in prime_range(3, 12)
            ....:     for k in srange(1, 4)
            ....:     for j in srange(0, k))
            True'''
    @overload
    def is_square(self) -> Any:
        """IntegerMod_abstract.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1061)

        EXAMPLES::

            sage: Mod(3, 17).is_square()
            False

            sage: # needs sage.libs.pari
            sage: Mod(9, 17).is_square()
            True
            sage: Mod(9, 17*19^2).is_square()
            True
            sage: Mod(-1, 17^30).is_square()
            True
            sage: Mod(1/9, next_prime(2^40)).is_square()
            True
            sage: Mod(1/25, next_prime(2^90)).is_square()
            True

        TESTS::

            sage: Mod(1/25, 2^8).is_square()                                            # needs sage.libs.pari
            True
            sage: Mod(1/25, 2^40).is_square()                                           # needs sage.libs.pari
            True

            sage: for p,q,r in cartesian_product_iterator([[3,5],[11,13],[17,19]]):  # long time, needs sage.libs.pari
            ....:     for ep,eq,er in cartesian_product_iterator([[0,1,2,3],[0,1,2,3],[0,1,2,3]]):
            ....:         for e2 in [0, 1, 2, 3, 4]:
            ....:             n = p^ep * q^eq * r^er * 2^e2
            ....:             for _ in range(2):
            ....:                 a = Zmod(n).random_element()
            ....:                 if a.is_square().__xor__(a.__pari__().issquare()):
            ....:                     print(a, n)

        ALGORITHM: Calculate the Jacobi symbol
        `(\\mathtt{self}/p)` at each prime `p`
        dividing `n`. It must be 1 or 0 for each prime, and if it
        is 0 mod `p`, where `p^k || n`, then
        `ord_p(\\mathtt{self})` must be even or greater than
        `k`.

        The case `p = 2` is handled separately.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def is_square(self) -> Any:
        """IntegerMod_abstract.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1061)

        EXAMPLES::

            sage: Mod(3, 17).is_square()
            False

            sage: # needs sage.libs.pari
            sage: Mod(9, 17).is_square()
            True
            sage: Mod(9, 17*19^2).is_square()
            True
            sage: Mod(-1, 17^30).is_square()
            True
            sage: Mod(1/9, next_prime(2^40)).is_square()
            True
            sage: Mod(1/25, next_prime(2^90)).is_square()
            True

        TESTS::

            sage: Mod(1/25, 2^8).is_square()                                            # needs sage.libs.pari
            True
            sage: Mod(1/25, 2^40).is_square()                                           # needs sage.libs.pari
            True

            sage: for p,q,r in cartesian_product_iterator([[3,5],[11,13],[17,19]]):  # long time, needs sage.libs.pari
            ....:     for ep,eq,er in cartesian_product_iterator([[0,1,2,3],[0,1,2,3],[0,1,2,3]]):
            ....:         for e2 in [0, 1, 2, 3, 4]:
            ....:             n = p^ep * q^eq * r^er * 2^e2
            ....:             for _ in range(2):
            ....:                 a = Zmod(n).random_element()
            ....:                 if a.is_square().__xor__(a.__pari__().issquare()):
            ....:                     print(a, n)

        ALGORITHM: Calculate the Jacobi symbol
        `(\\mathtt{self}/p)` at each prime `p`
        dividing `n`. It must be 1 or 0 for each prime, and if it
        is 0 mod `p`, where `p^k || n`, then
        `ord_p(\\mathtt{self})` must be even or greater than
        `k`.

        The case `p = 2` is handled separately.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def is_square(self) -> Any:
        """IntegerMod_abstract.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1061)

        EXAMPLES::

            sage: Mod(3, 17).is_square()
            False

            sage: # needs sage.libs.pari
            sage: Mod(9, 17).is_square()
            True
            sage: Mod(9, 17*19^2).is_square()
            True
            sage: Mod(-1, 17^30).is_square()
            True
            sage: Mod(1/9, next_prime(2^40)).is_square()
            True
            sage: Mod(1/25, next_prime(2^90)).is_square()
            True

        TESTS::

            sage: Mod(1/25, 2^8).is_square()                                            # needs sage.libs.pari
            True
            sage: Mod(1/25, 2^40).is_square()                                           # needs sage.libs.pari
            True

            sage: for p,q,r in cartesian_product_iterator([[3,5],[11,13],[17,19]]):  # long time, needs sage.libs.pari
            ....:     for ep,eq,er in cartesian_product_iterator([[0,1,2,3],[0,1,2,3],[0,1,2,3]]):
            ....:         for e2 in [0, 1, 2, 3, 4]:
            ....:             n = p^ep * q^eq * r^er * 2^e2
            ....:             for _ in range(2):
            ....:                 a = Zmod(n).random_element()
            ....:                 if a.is_square().__xor__(a.__pari__().issquare()):
            ....:                     print(a, n)

        ALGORITHM: Calculate the Jacobi symbol
        `(\\mathtt{self}/p)` at each prime `p`
        dividing `n`. It must be 1 or 0 for each prime, and if it
        is 0 mod `p`, where `p^k || n`, then
        `ord_p(\\mathtt{self})` must be even or greater than
        `k`.

        The case `p = 2` is handled separately.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def is_square(self) -> Any:
        """IntegerMod_abstract.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1061)

        EXAMPLES::

            sage: Mod(3, 17).is_square()
            False

            sage: # needs sage.libs.pari
            sage: Mod(9, 17).is_square()
            True
            sage: Mod(9, 17*19^2).is_square()
            True
            sage: Mod(-1, 17^30).is_square()
            True
            sage: Mod(1/9, next_prime(2^40)).is_square()
            True
            sage: Mod(1/25, next_prime(2^90)).is_square()
            True

        TESTS::

            sage: Mod(1/25, 2^8).is_square()                                            # needs sage.libs.pari
            True
            sage: Mod(1/25, 2^40).is_square()                                           # needs sage.libs.pari
            True

            sage: for p,q,r in cartesian_product_iterator([[3,5],[11,13],[17,19]]):  # long time, needs sage.libs.pari
            ....:     for ep,eq,er in cartesian_product_iterator([[0,1,2,3],[0,1,2,3],[0,1,2,3]]):
            ....:         for e2 in [0, 1, 2, 3, 4]:
            ....:             n = p^ep * q^eq * r^er * 2^e2
            ....:             for _ in range(2):
            ....:                 a = Zmod(n).random_element()
            ....:                 if a.is_square().__xor__(a.__pari__().issquare()):
            ....:                     print(a, n)

        ALGORITHM: Calculate the Jacobi symbol
        `(\\mathtt{self}/p)` at each prime `p`
        dividing `n`. It must be 1 or 0 for each prime, and if it
        is 0 mod `p`, where `p^k || n`, then
        `ord_p(\\mathtt{self})` must be even or greater than
        `k`.

        The case `p = 2` is handled separately.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def is_square(self) -> Any:
        """IntegerMod_abstract.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1061)

        EXAMPLES::

            sage: Mod(3, 17).is_square()
            False

            sage: # needs sage.libs.pari
            sage: Mod(9, 17).is_square()
            True
            sage: Mod(9, 17*19^2).is_square()
            True
            sage: Mod(-1, 17^30).is_square()
            True
            sage: Mod(1/9, next_prime(2^40)).is_square()
            True
            sage: Mod(1/25, next_prime(2^90)).is_square()
            True

        TESTS::

            sage: Mod(1/25, 2^8).is_square()                                            # needs sage.libs.pari
            True
            sage: Mod(1/25, 2^40).is_square()                                           # needs sage.libs.pari
            True

            sage: for p,q,r in cartesian_product_iterator([[3,5],[11,13],[17,19]]):  # long time, needs sage.libs.pari
            ....:     for ep,eq,er in cartesian_product_iterator([[0,1,2,3],[0,1,2,3],[0,1,2,3]]):
            ....:         for e2 in [0, 1, 2, 3, 4]:
            ....:             n = p^ep * q^eq * r^er * 2^e2
            ....:             for _ in range(2):
            ....:                 a = Zmod(n).random_element()
            ....:                 if a.is_square().__xor__(a.__pari__().issquare()):
            ....:                     print(a, n)

        ALGORITHM: Calculate the Jacobi symbol
        `(\\mathtt{self}/p)` at each prime `p`
        dividing `n`. It must be 1 or 0 for each prime, and if it
        is 0 mod `p`, where `p^k || n`, then
        `ord_p(\\mathtt{self})` must be even or greater than
        `k`.

        The case `p = 2` is handled separately.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def is_square(self) -> Any:
        """IntegerMod_abstract.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1061)

        EXAMPLES::

            sage: Mod(3, 17).is_square()
            False

            sage: # needs sage.libs.pari
            sage: Mod(9, 17).is_square()
            True
            sage: Mod(9, 17*19^2).is_square()
            True
            sage: Mod(-1, 17^30).is_square()
            True
            sage: Mod(1/9, next_prime(2^40)).is_square()
            True
            sage: Mod(1/25, next_prime(2^90)).is_square()
            True

        TESTS::

            sage: Mod(1/25, 2^8).is_square()                                            # needs sage.libs.pari
            True
            sage: Mod(1/25, 2^40).is_square()                                           # needs sage.libs.pari
            True

            sage: for p,q,r in cartesian_product_iterator([[3,5],[11,13],[17,19]]):  # long time, needs sage.libs.pari
            ....:     for ep,eq,er in cartesian_product_iterator([[0,1,2,3],[0,1,2,3],[0,1,2,3]]):
            ....:         for e2 in [0, 1, 2, 3, 4]:
            ....:             n = p^ep * q^eq * r^er * 2^e2
            ....:             for _ in range(2):
            ....:                 a = Zmod(n).random_element()
            ....:                 if a.is_square().__xor__(a.__pari__().issquare()):
            ....:                     print(a, n)

        ALGORITHM: Calculate the Jacobi symbol
        `(\\mathtt{self}/p)` at each prime `p`
        dividing `n`. It must be 1 or 0 for each prime, and if it
        is 0 mod `p`, where `p^k || n`, then
        `ord_p(\\mathtt{self})` must be even or greater than
        `k`.

        The case `p = 2` is handled separately.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def is_square(self) -> Any:
        """IntegerMod_abstract.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1061)

        EXAMPLES::

            sage: Mod(3, 17).is_square()
            False

            sage: # needs sage.libs.pari
            sage: Mod(9, 17).is_square()
            True
            sage: Mod(9, 17*19^2).is_square()
            True
            sage: Mod(-1, 17^30).is_square()
            True
            sage: Mod(1/9, next_prime(2^40)).is_square()
            True
            sage: Mod(1/25, next_prime(2^90)).is_square()
            True

        TESTS::

            sage: Mod(1/25, 2^8).is_square()                                            # needs sage.libs.pari
            True
            sage: Mod(1/25, 2^40).is_square()                                           # needs sage.libs.pari
            True

            sage: for p,q,r in cartesian_product_iterator([[3,5],[11,13],[17,19]]):  # long time, needs sage.libs.pari
            ....:     for ep,eq,er in cartesian_product_iterator([[0,1,2,3],[0,1,2,3],[0,1,2,3]]):
            ....:         for e2 in [0, 1, 2, 3, 4]:
            ....:             n = p^ep * q^eq * r^er * 2^e2
            ....:             for _ in range(2):
            ....:                 a = Zmod(n).random_element()
            ....:                 if a.is_square().__xor__(a.__pari__().issquare()):
            ....:                     print(a, n)

        ALGORITHM: Calculate the Jacobi symbol
        `(\\mathtt{self}/p)` at each prime `p`
        dividing `n`. It must be 1 or 0 for each prime, and if it
        is 0 mod `p`, where `p^k || n`, then
        `ord_p(\\mathtt{self})` must be even or greater than
        `k`.

        The case `p = 2` is handled separately.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def is_square(self) -> Any:
        """IntegerMod_abstract.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1061)

        EXAMPLES::

            sage: Mod(3, 17).is_square()
            False

            sage: # needs sage.libs.pari
            sage: Mod(9, 17).is_square()
            True
            sage: Mod(9, 17*19^2).is_square()
            True
            sage: Mod(-1, 17^30).is_square()
            True
            sage: Mod(1/9, next_prime(2^40)).is_square()
            True
            sage: Mod(1/25, next_prime(2^90)).is_square()
            True

        TESTS::

            sage: Mod(1/25, 2^8).is_square()                                            # needs sage.libs.pari
            True
            sage: Mod(1/25, 2^40).is_square()                                           # needs sage.libs.pari
            True

            sage: for p,q,r in cartesian_product_iterator([[3,5],[11,13],[17,19]]):  # long time, needs sage.libs.pari
            ....:     for ep,eq,er in cartesian_product_iterator([[0,1,2,3],[0,1,2,3],[0,1,2,3]]):
            ....:         for e2 in [0, 1, 2, 3, 4]:
            ....:             n = p^ep * q^eq * r^er * 2^e2
            ....:             for _ in range(2):
            ....:                 a = Zmod(n).random_element()
            ....:                 if a.is_square().__xor__(a.__pari__().issquare()):
            ....:                     print(a, n)

        ALGORITHM: Calculate the Jacobi symbol
        `(\\mathtt{self}/p)` at each prime `p`
        dividing `n`. It must be 1 or 0 for each prime, and if it
        is 0 mod `p`, where `p^k || n`, then
        `ord_p(\\mathtt{self})` must be even or greater than
        `k`.

        The case `p = 2` is handled separately.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def is_square(self) -> Any:
        """IntegerMod_abstract.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1061)

        EXAMPLES::

            sage: Mod(3, 17).is_square()
            False

            sage: # needs sage.libs.pari
            sage: Mod(9, 17).is_square()
            True
            sage: Mod(9, 17*19^2).is_square()
            True
            sage: Mod(-1, 17^30).is_square()
            True
            sage: Mod(1/9, next_prime(2^40)).is_square()
            True
            sage: Mod(1/25, next_prime(2^90)).is_square()
            True

        TESTS::

            sage: Mod(1/25, 2^8).is_square()                                            # needs sage.libs.pari
            True
            sage: Mod(1/25, 2^40).is_square()                                           # needs sage.libs.pari
            True

            sage: for p,q,r in cartesian_product_iterator([[3,5],[11,13],[17,19]]):  # long time, needs sage.libs.pari
            ....:     for ep,eq,er in cartesian_product_iterator([[0,1,2,3],[0,1,2,3],[0,1,2,3]]):
            ....:         for e2 in [0, 1, 2, 3, 4]:
            ....:             n = p^ep * q^eq * r^er * 2^e2
            ....:             for _ in range(2):
            ....:                 a = Zmod(n).random_element()
            ....:                 if a.is_square().__xor__(a.__pari__().issquare()):
            ....:                     print(a, n)

        ALGORITHM: Calculate the Jacobi symbol
        `(\\mathtt{self}/p)` at each prime `p`
        dividing `n`. It must be 1 or 0 for each prime, and if it
        is 0 mod `p`, where `p^k || n`, then
        `ord_p(\\mathtt{self})` must be even or greater than
        `k`.

        The case `p = 2` is handled separately.

        AUTHORS:

        - Robert Bradshaw"""
    @overload
    def is_square(self) -> Any:
        """IntegerMod_abstract.is_square(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1061)

        EXAMPLES::

            sage: Mod(3, 17).is_square()
            False

            sage: # needs sage.libs.pari
            sage: Mod(9, 17).is_square()
            True
            sage: Mod(9, 17*19^2).is_square()
            True
            sage: Mod(-1, 17^30).is_square()
            True
            sage: Mod(1/9, next_prime(2^40)).is_square()
            True
            sage: Mod(1/25, next_prime(2^90)).is_square()
            True

        TESTS::

            sage: Mod(1/25, 2^8).is_square()                                            # needs sage.libs.pari
            True
            sage: Mod(1/25, 2^40).is_square()                                           # needs sage.libs.pari
            True

            sage: for p,q,r in cartesian_product_iterator([[3,5],[11,13],[17,19]]):  # long time, needs sage.libs.pari
            ....:     for ep,eq,er in cartesian_product_iterator([[0,1,2,3],[0,1,2,3],[0,1,2,3]]):
            ....:         for e2 in [0, 1, 2, 3, 4]:
            ....:             n = p^ep * q^eq * r^er * 2^e2
            ....:             for _ in range(2):
            ....:                 a = Zmod(n).random_element()
            ....:                 if a.is_square().__xor__(a.__pari__().issquare()):
            ....:                     print(a, n)

        ALGORITHM: Calculate the Jacobi symbol
        `(\\mathtt{self}/p)` at each prime `p`
        dividing `n`. It must be 1 or 0 for each prime, and if it
        is 0 mod `p`, where `p^k || n`, then
        `ord_p(\\mathtt{self})` must be even or greater than
        `k`.

        The case `p = 2` is handled separately.

        AUTHORS:

        - Robert Bradshaw"""
    def is_unit(self) -> bool:
        """IntegerMod_abstract.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1033)"""
    def lift_centered(self) -> Any:
        """IntegerMod_abstract.lift_centered(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 995)

        Lift ``self`` to a centered congruent integer.

        OUTPUT:

        The unique integer `i` such that `-n/2 < i \\leq n/2` and `i = self \\mod n`
        (where `n` denotes the modulus).

        EXAMPLES::

            sage: Mod(0,5).lift_centered()
            0
            sage: Mod(1,5).lift_centered()
            1
            sage: Mod(2,5).lift_centered()
            2
            sage: Mod(3,5).lift_centered()
            -2
            sage: Mod(4,5).lift_centered()
            -1
            sage: Mod(50,100).lift_centered()
            50
            sage: Mod(51,100).lift_centered()
            -49
            sage: Mod(-1,3^100).lift_centered()
            -1"""
    def log(self, b=..., order=..., check=...) -> Any:
        """IntegerMod_abstract.log(self, b=None, order=None, check=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 641)

        Compute the discrete logarithm of this element to base `b`,
        that is,
        return an integer `x` such that `b^x = a`, where
        `a` is ``self``.

        INPUT:

        - ``self`` -- unit modulo `n`

        - ``b`` -- a unit modulo `n`. If ``b`` is not given,
          ``R.multiplicative_generator()`` is used, where
          ``R`` is the parent of ``self``.

        - ``order`` -- integer (unused), the order of ``b``.
          This argument is normally unused, only there for
          coherence of apis with finite field elements.

        - ``check`` -- boolean (default: ``False``); if set,
          test whether the given ``order`` is correct

        OUTPUT:

        Integer `x` such that `b^x = a`, if this exists; a :exc:`ValueError`
        otherwise.

        .. NOTE::

           The algorithm first factors the modulus, then invokes Pari's :pari:`znlog`
           function for each odd prime power in the factorization of the modulus.
           This method can be quite slow for large moduli.

        EXAMPLES::

            sage: # needs sage.libs.pari sage.modules
            sage: r = Integers(125)
            sage: b = r.multiplicative_generator()^3
            sage: a = b^17
            sage: a.log(b)
            17
            sage: a.log()
            51

        A bigger example::

            sage: # needs sage.rings.finite_rings
            sage: FF = FiniteField(2^32 + 61)
            sage: c = FF(4294967356)
            sage: x = FF(2)
            sage: a = c.log(x)
            sage: a
            2147483678
            sage: x^a
            4294967356

        An example with a highly composite modulus::

            sage: m = 2^99 * 77^7 * 123456789 * 13712923537615486607^2
            sage: (Mod(5,m)^5735816763073854953388147237921).log(5)                     # needs sage.libs.pari
            5735816763073854953388147237921

        Errors are generated if the logarithm doesn't exist
        or the inputs are not units::

            sage: Mod(3, 7).log(Mod(2, 7))                                              # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ValueError: no logarithm of 3 found to base 2 modulo 7
            sage: a = Mod(16, 100); b = Mod(4, 100)
            sage: a.log(b)
            Traceback (most recent call last):
            ...
            ValueError: logarithm of 16 is not defined since it is not a unit modulo 100

        TESTS:

        We check that :issue:`9205` is fixed::

            sage: Mod(5, 9).log(Mod(2, 9))                                              # needs sage.libs.pari
            5

        We test against a bug (side effect on PARI) fixed in :issue:`9438`::

            sage: # needs sage.libs.pari
            sage: R.<a, b> = QQ[]
            sage: pari(b)
            b
            sage: GF(7)(5).log()
            5
            sage: pari(b)
            b

        We test that :issue:`23927` is fixed::

            sage: x = mod(48475563673907791151, 10^20 + 763)^2
            sage: e = 25248843418589594761
            sage: (x^e).log(x) == e                                                     # needs sage.libs.pari
            True

        Examples like this took extremely long before :issue:`32375`::

            sage: (Mod(5, 123337052926643**4) ^ (10^50-1)).log(5)                       # needs sage.libs.pari
            99999999999999999999999999999999999999999999999999

        We check that non-existence of solutions is detected:

        No local solutions::

            sage: Mod(1111, 1234567).log(1111**3)                                       # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ValueError: no logarithm of 1111 found to base 961261 modulo 1234567 (no solution modulo 9721)

        Incompatible local solutions::

            sage: Mod(230, 323).log(173)                                                # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ValueError: no logarithm of 230 found to base 173 modulo 323 (incompatible local solutions)

        We test that :issue:`12419` is fixed::

            sage: R.<x,y> = GF(2)[]
            sage: R(1).factor()
            1

        An example for ``check=True``::

            sage: F = GF(127, impl='modn')
            sage: t = F.primitive_element()
            sage: t.log(t, 57, check=True)
            Traceback (most recent call last):
            ...
            ValueError: base does not have the provided order

        AUTHORS:

        - David Joyner and William Stein (2005-11)

        - William Stein (2007-01-27): update to use PARI as requested
          by David Kohel.

        - Simon King (2010-07-07): fix a side effect on PARI

        - Lorenz Panny (2021): speedups for composite moduli"""
    @overload
    def minimal_polynomial(self, var=...) -> Any:
        """IntegerMod_abstract.minimal_polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 931)

        Return the minimal polynomial of this element.

        EXAMPLES::

            sage: GF(241, 'a')(1).minimal_polynomial(var = 'z')
            z + 240"""
    @overload
    def minimal_polynomial(self, var=...) -> Any:
        """IntegerMod_abstract.minimal_polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 931)

        Return the minimal polynomial of this element.

        EXAMPLES::

            sage: GF(241, 'a')(1).minimal_polynomial(var = 'z')
            z + 240"""
    @overload
    def minpoly(self, var=...) -> Any:
        """IntegerMod_abstract.minpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 920)

        Return the minimal polynomial of this element.

        EXAMPLES::

            sage: GF(241, 'a')(1).minpoly()
            x + 240"""
    @overload
    def minpoly(self) -> Any:
        """IntegerMod_abstract.minpoly(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 920)

        Return the minimal polynomial of this element.

        EXAMPLES::

            sage: GF(241, 'a')(1).minpoly()
            x + 240"""
    @overload
    def modulus(self) -> Any:
        """IntegerMod_abstract.modulus(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 891)

        EXAMPLES::

            sage: Mod(3,17).modulus()
            17"""
    @overload
    def modulus(self) -> Any:
        """IntegerMod_abstract.modulus(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 891)

        EXAMPLES::

            sage: Mod(3,17).modulus()
            17"""
    @overload
    def multiplicative_order(self) -> Any:
        """IntegerMod_abstract.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1878)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: Mod(-1, 5).multiplicative_order()                                     # needs sage.libs.pari
            2
            sage: Mod(1, 5).multiplicative_order()                                      # needs sage.libs.pari
            1
            sage: Mod(0, 5).multiplicative_order()                                      # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ArithmeticError: multiplicative order of 0 not defined
            since it is not a unit modulo 5"""
    @overload
    def multiplicative_order(self) -> Any:
        """IntegerMod_abstract.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1878)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: Mod(-1, 5).multiplicative_order()                                     # needs sage.libs.pari
            2
            sage: Mod(1, 5).multiplicative_order()                                      # needs sage.libs.pari
            1
            sage: Mod(0, 5).multiplicative_order()                                      # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ArithmeticError: multiplicative order of 0 not defined
            since it is not a unit modulo 5"""
    @overload
    def multiplicative_order(self) -> Any:
        """IntegerMod_abstract.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1878)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: Mod(-1, 5).multiplicative_order()                                     # needs sage.libs.pari
            2
            sage: Mod(1, 5).multiplicative_order()                                      # needs sage.libs.pari
            1
            sage: Mod(0, 5).multiplicative_order()                                      # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ArithmeticError: multiplicative order of 0 not defined
            since it is not a unit modulo 5"""
    @overload
    def multiplicative_order(self) -> Any:
        """IntegerMod_abstract.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1878)

        Return the multiplicative order of ``self``.

        EXAMPLES::

            sage: Mod(-1, 5).multiplicative_order()                                     # needs sage.libs.pari
            2
            sage: Mod(1, 5).multiplicative_order()                                      # needs sage.libs.pari
            1
            sage: Mod(0, 5).multiplicative_order()                                      # needs sage.libs.pari
            Traceback (most recent call last):
            ...
            ArithmeticError: multiplicative order of 0 not defined
            since it is not a unit modulo 5"""
    @overload
    def norm(self) -> Any:
        """IntegerMod_abstract.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 959)

        Return the norm of this element, which is itself. (This is here
        for compatibility with higher order finite fields.)

        EXAMPLES::

            sage: k = GF(691)
            sage: a = k(389)
            sage: a.norm()
            389

        AUTHORS:

        - Craig Citro"""
    @overload
    def norm(self) -> Any:
        """IntegerMod_abstract.norm(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 959)

        Return the norm of this element, which is itself. (This is here
        for compatibility with higher order finite fields.)

        EXAMPLES::

            sage: k = GF(691)
            sage: a = k(389)
            sage: a.norm()
            389

        AUTHORS:

        - Craig Citro"""
    def nth_root(self, n, extend=..., all=..., algorithm=..., cunningham=...) -> Any:
        """IntegerMod_abstract.nth_root(self, n, extend=False, all=False, algorithm=None, cunningham=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1367)

        Return an `n`-th root of ``self``.

        INPUT:

        - ``n`` -- integer `\\geq 1`

        - ``extend`` -- boolean (default: ``True``); if ``True``, return an
          `n`-th root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the root is not in the base ring.  Warning:
          this option is not implemented!

        - ``all`` -- boolean (default: ``False``); if ``True``, return all
          `n`-th roots of ``self``, instead of just one

        - ``algorithm`` -- string (default: ``None``); the algorithm for the
          prime modulus case. CRT and `p`-adic log techniques are used to reduce
          to this case. ``'Johnston'`` is the only currently supported option.

        - ``cunningham`` -- boolean (default: ``False``); in some cases,
          factorization of `n` is computed. If cunningham is set to ``True``,
          the factorization of `n` is computed using trial division for all
          primes in the so called Cunningham table. Refer to
          ``sage.rings.factorint.factor_cunningham`` for more information. You
          need to install an optional package to use this method, this can be
          done with the following command line: ``sage -i cunningham_tables``.

        OUTPUT:

        If ``self`` has an `n`-th root, returns one (if ``all`` is ``False``) or a
        list of all of them (if ``all`` is ``True``).  Otherwise, raises a
        :exc:`ValueError` (if ``extend`` is ``False``) or a
        :exc:`NotImplementedError` (if ``extend`` is ``True``).

        .. warning::

           The 'extend' option is not implemented (yet).

        NOTE:

        - If `n = 0`:

          - if ``all=True``:

            - if ``self=1``: all nonzero elements of the parent are returned in
              a list.  Note that this could be very expensive for large
              parents.

            - otherwise: an empty list is returned

          - if ``all=False``:

            - if ``self=1``: ``self`` is returned

            - otherwise; a :exc:`ValueError` is raised

        - If `n < 0`:

          - if ``self`` is invertible, the `(-n)`\\th root of the inverse of ``self`` is returned

          - otherwise a :exc:`ValueError` is raised or empty list returned.

        EXAMPLES::


            sage: K = GF(31)
            sage: a = K(22)
            sage: K(22).nth_root(7)
            13
            sage: K(25).nth_root(5)
            5
            sage: K(23).nth_root(3)
            29

            sage: # needs sage.rings.padics
            sage: mod(225, 2^5*3^2).nth_root(4, all=True)
            [225, 129, 33, 63, 255, 159, 9, 201, 105, 279, 183, 87, 81,
             273, 177, 207, 111, 15, 153, 57, 249, 135, 39, 231]
            sage: mod(275, 2^5*7^4).nth_root(7, all=True)
            [58235, 25307, 69211, 36283, 3355, 47259, 14331]
            sage: mod(1,8).nth_root(2, all=True)
            [1, 7, 5, 3]
            sage: mod(4,8).nth_root(2, all=True)
            [2, 6]
            sage: mod(1,16).nth_root(4, all=True)
            [1, 15, 13, 3, 9, 7, 5, 11]

            sage: (mod(22,31)^200).nth_root(200)
            5
            sage: mod(3,6).nth_root(0, all=True)
            []
            sage: mod(3,6).nth_root(0)
            Traceback (most recent call last):
            ...
            ValueError
            sage: mod(1,6).nth_root(0, all=True)
            [1, 2, 3, 4, 5]

        TESTS::

            sage: for p in [1009,2003,10007,100003]:                                    # needs sage.rings.finite_rings
            ....:     K = GF(p)
            ....:     for r in (p-1).divisors():
            ....:         if r == 1: continue
            ....:         x = K.random_element()
            ....:         y = x^r
            ....:         if y.nth_root(r)**r != y: raise RuntimeError
            ....:         if (y^41).nth_root(41*r)**(41*r) != y^41: raise RuntimeError
            ....:         if (y^307).nth_root(307*r)**(307*r) != y^307: raise RuntimeError

            sage: for t in range(200):                                                  # needs sage.libs.pari sage.rings.padics
            ....:     n = randint(1,2^63)
            ....:     K = Integers(n)
            ....:     b = K.random_element()
            ....:     e = randint(-2^62, 2^63)
            ....:     try:
            ....:         a = b.nth_root(e)
            ....:         if a^e != b:
            ....:             print(n, b, e, a)
            ....:             raise NotImplementedError
            ....:     except ValueError:
            ....:         pass

        We check that :issue:`13172` is resolved::

            sage: mod(-1, 4489).nth_root(2, all=True)                                   # needs sage.rings.padics
            []

        We check that :issue:`32084` is fixed::

            sage: mod(24, 25).nth_root(50)^50                                           # needs sage.rings.padics
            24

        Check that the code path cunningham might be used::

            sage: a = Mod(9,11)
            sage: a.nth_root(2, False, True, 'Johnston', cunningham=True)   # optional - cunningham_tables
            [3, 8]

        ALGORITHM:

        The default for prime modulus is currently an algorithm
        described in [Joh1999]_.

        AUTHORS:

        - David Roe (2010-02-13)"""
    @overload
    def polynomial(self, var=...) -> Any:
        """IntegerMod_abstract.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 942)

        Return a constant polynomial representing this value.

        EXAMPLES::

            sage: k = GF(7)
            sage: a = k.gen(); a
            1
            sage: a.polynomial()
            1
            sage: type(a.polynomial())                                                  # needs sage.libs.flint
            <class 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>"""
    @overload
    def polynomial(self) -> Any:
        """IntegerMod_abstract.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 942)

        Return a constant polynomial representing this value.

        EXAMPLES::

            sage: k = GF(7)
            sage: a = k.gen(); a
            1
            sage: a.polynomial()
            1
            sage: type(a.polynomial())                                                  # needs sage.libs.flint
            <class 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>"""
    @overload
    def polynomial(self) -> Any:
        """IntegerMod_abstract.polynomial(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 942)

        Return a constant polynomial representing this value.

        EXAMPLES::

            sage: k = GF(7)
            sage: a = k.gen(); a
            1
            sage: a.polynomial()
            1
            sage: type(a.polynomial())                                                  # needs sage.libs.flint
            <class 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>"""
    @overload
    def rational_reconstruction(self) -> Any:
        """IntegerMod_abstract.rational_reconstruction(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1670)

        Use rational reconstruction to try to find a lift of this element to
        the rational numbers.

        EXAMPLES::

            sage: R = IntegerModRing(97)
            sage: a = R(2) / R(3)
            sage: a
            33
            sage: a.rational_reconstruction()
            2/3

        This method is also inherited by prime finite fields elements::

            sage: k = GF(97)
            sage: a = k(RationalField()('2/3'))
            sage: a
            33
            sage: a.rational_reconstruction()
            2/3"""
    @overload
    def rational_reconstruction(self) -> Any:
        """IntegerMod_abstract.rational_reconstruction(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1670)

        Use rational reconstruction to try to find a lift of this element to
        the rational numbers.

        EXAMPLES::

            sage: R = IntegerModRing(97)
            sage: a = R(2) / R(3)
            sage: a
            33
            sage: a.rational_reconstruction()
            2/3

        This method is also inherited by prime finite fields elements::

            sage: k = GF(97)
            sage: a = k(RationalField()('2/3'))
            sage: a
            33
            sage: a.rational_reconstruction()
            2/3"""
    @overload
    def rational_reconstruction(self) -> Any:
        """IntegerMod_abstract.rational_reconstruction(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1670)

        Use rational reconstruction to try to find a lift of this element to
        the rational numbers.

        EXAMPLES::

            sage: R = IntegerModRing(97)
            sage: a = R(2) / R(3)
            sage: a
            33
            sage: a.rational_reconstruction()
            2/3

        This method is also inherited by prime finite fields elements::

            sage: k = GF(97)
            sage: a = k(RationalField()('2/3'))
            sage: a
            33
            sage: a.rational_reconstruction()
            2/3"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self, extend=...) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self, extend=...) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    def square_root(self, *args, **kwargs):
        """IntegerMod_abstract.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1134)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``); if ``True``, return a
          square root in an extension ring, if necessary. Otherwise, raise a
          :exc:`ValueError` if the square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if ``True``, return {all}
          square roots of self, instead of just one

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        Error message as requested in :issue:`38802`::

            sage: sqrt(Mod(2, 101010), all=True)
            Traceback (most recent call last):
            ...
            NotImplementedError: Finding all square roots in extensions is not implemented; try extend=False to find only roots in the base ring Zmod(n).

        Using the suggested ``extend=False`` works and returns an empty list
        as expected::

            sage: sqrt(Mod(2, 101010), all=True, extend=False)
            []

        ::

            sage: a = Mod(3, 5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359 over
             Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        ::

            sage: # needs sage.rings.finite_rings
            sage: t = FiniteField(next_prime(2^100))(4)
            sage: t.sqrt(extend=False, all=True)
            [2, 1267650600228229401496703205651]
            sage: t = FiniteField(next_prime(2^100))(2)
            sage: t.sqrt(extend=False, all=True)
            []

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]"""
    @overload
    def trace(self) -> Any:
        """IntegerMod_abstract.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 977)

        Return the trace of this element, which is itself. (This is here
        for compatibility with higher order finite fields.)

        EXAMPLES::

            sage: k = GF(691)
            sage: a = k(389)
            sage: a.trace()
            389

        AUTHORS:

        - Craig Citro"""
    @overload
    def trace(self) -> Any:
        """IntegerMod_abstract.trace(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 977)

        Return the trace of this element, which is itself. (This is here
        for compatibility with higher order finite fields.)

        EXAMPLES::

            sage: k = GF(691)
            sage: a = k(389)
            sage: a.trace()
            389

        AUTHORS:

        - Craig Citro"""
    def valuation(self, p) -> Any:
        """IntegerMod_abstract.valuation(self, p)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 1900)

        The largest power `r` such that `m` is in the ideal generated by `p^r` or infinity if there is not a largest such power.
        However it is an error to take the valuation with respect to a unit.

        .. NOTE::

            This is not a valuation in the mathematical sense. As shown with the examples below.

        EXAMPLES:

        This example shows that ``(a*b).valuation(n)`` is not always the same as ``a.valuation(n) + b.valuation(n)``

        ::

            sage: R = ZZ.quo(9)
            sage: a = R(3)
            sage: b = R(6)
            sage: a.valuation(3)
            1
            sage: a.valuation(3) + b.valuation(3)
            2
            sage: (a*b).valuation(3)
            +Infinity

        The valuation with respect to a unit is an error

        ::

            sage: a.valuation(4)
            Traceback (most recent call last):
            ...
            ValueError: Valuation with respect to a unit is not defined.

        TESTS::

            sage: R = ZZ.quo(12)
            sage: a = R(2)
            sage: b = R(4)
            sage: a.valuation(2)
            1
            sage: b.valuation(2)
            +Infinity
            sage: ZZ.quo(1024)(16).valuation(4)
            2"""
    def __abs__(self) -> Any:
        """IntegerMod_abstract.__abs__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 435)

        Raise an error message, since ``abs(x)`` makes no sense
        when ``x`` is an integer modulo `n`.

        EXAMPLES::

            sage: abs(Mod(2,3))
            Traceback (most recent call last):
            ...
            ArithmeticError: absolute value not defined on integers modulo n."""
    def __mod__(self, modulus) -> Any:
        """IntegerMod_abstract.__mod__(self, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 478)

        Coerce this element to the ring `Z/(modulus)`.

        If the new ``modulus`` does not divide the current modulus,
        an :exc:`ArithmeticError` is raised.

        EXAMPLES::

            sage: a = Mod(14, 35)
            sage: a % 5
            4
            sage: parent(a % 5)
            Ring of integers modulo 5
            sage: a % 350
            Traceback (most recent call last):
            ...
            ArithmeticError: reduction modulo 350 not defined
            sage: a % 35
            14
            sage: int(1) % a
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand type(s) for %: 'int' and 'sage.rings.finite_rings.integer_mod.IntegerMod_int'"""
    def __pari__(self) -> Any:
        """IntegerMod_abstract.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 551)"""
    def __reduce__(self) -> Any:
        """IntegerMod_abstract.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 449)

        EXAMPLES::

            sage: a = Mod(4,5); a
            4
            sage: loads(a.dumps()) == a
            True
            sage: a = Mod(-1,5^30)^25
            sage: loads(a.dumps()) == a
            True"""
    def __rmod__(self, other):
        """Return value%self."""

class IntegerMod_gmp(IntegerMod_abstract):
    """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2005)

        Elements of `\\ZZ/n\\ZZ` for n not small enough
        to be operated on in word size.

        AUTHORS:

        - Robert Bradshaw (2006-08-24)
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def gcd(self, IntegerMod_gmpother) -> Any:
        '''IntegerMod_gmp.gcd(self, IntegerMod_gmp other)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2414)

        Greatest common divisor.

        Returns the "smallest" generator in `\\ZZ / N\\ZZ` of the ideal
        generated by ``self`` and ``other``.

        INPUT:

        - ``other`` -- an element of the same ring as this one

        EXAMPLES::

            sage: mod(2^3*3^2*5, 3^3*2^2*17^8).gcd(mod(2^4*3*17, 3^3*2^2*17^8))
            12
            sage: mod(0,17^8).gcd(mod(0,17^8))
            0'''
    @overload
    def is_one(self) -> bool:
        """IntegerMod_gmp.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2138)

        Return ``True`` if this is `1`, otherwise ``False``.

        EXAMPLES::

            sage: mod(1,5^23).is_one()
            True
            sage: mod(0,5^23).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """IntegerMod_gmp.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2138)

        Return ``True`` if this is `1`, otherwise ``False``.

        EXAMPLES::

            sage: mod(1,5^23).is_one()
            True
            sage: mod(0,5^23).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """IntegerMod_gmp.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2138)

        Return ``True`` if this is `1`, otherwise ``False``.

        EXAMPLES::

            sage: mod(1,5^23).is_one()
            True
            sage: mod(0,5^23).is_one()
            False"""
    @overload
    def is_unit(self) -> bool:
        """IntegerMod_gmp.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2164)

        Return ``True`` iff this element is a unit.

        EXAMPLES::

            sage: mod(13, 5^23).is_unit()
            True
            sage: mod(25, 5^23).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """IntegerMod_gmp.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2164)

        Return ``True`` iff this element is a unit.

        EXAMPLES::

            sage: mod(13, 5^23).is_unit()
            True
            sage: mod(25, 5^23).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """IntegerMod_gmp.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2164)

        Return ``True`` iff this element is a unit.

        EXAMPLES::

            sage: mod(13, 5^23).is_unit()
            True
            sage: mod(25, 5^23).is_unit()
            False"""
    @overload
    def lift(self) -> Any:
        """IntegerMod_gmp.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2383)

        Lift an integer modulo `n` to the integers.

        EXAMPLES::

            sage: a = Mod(8943, 2^70); type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>
            sage: lift(a)
            8943
            sage: a.lift()
            8943"""
    @overload
    def lift(self, a) -> Any:
        """IntegerMod_gmp.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2383)

        Lift an integer modulo `n` to the integers.

        EXAMPLES::

            sage: a = Mod(8943, 2^70); type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>
            sage: lift(a)
            8943
            sage: a.lift()
            8943"""
    @overload
    def lift(self) -> Any:
        """IntegerMod_gmp.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2383)

        Lift an integer modulo `n` to the integers.

        EXAMPLES::

            sage: a = Mod(8943, 2^70); type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>
            sage: lift(a)
            8943
            sage: a.lift()
            8943"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """IntegerMod_gmp.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2198)

        EXAMPLES::

            sage: R = Integers(10^10)
            sage: R7 = R(7)
            sage: copy(R7) is R7
            True"""
    def __deepcopy__(self, memo) -> Any:
        """IntegerMod_gmp.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2210)

        EXAMPLES::

            sage: R = Integers(10^10)
            sage: R7 = R(7)
            sage: deepcopy(R7) is R7
            True"""
    def __float__(self) -> Any:
        """IntegerMod_gmp.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2401)"""
    def __hash__(self) -> Any:
        """IntegerMod_gmp.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2404)

        EXAMPLES::

            sage: a = Mod(8943, 2^100)
            sage: hash(a)
            8943"""
    def __index__(self) -> Any:
        """IntegerMod_gmp.__index__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2295)

        Needed so integers modulo `n` can be used as list indices.

        EXAMPLES::

            sage: v = [1,2,3,4,5]
            sage: v[Mod(3,10^20)]
            4"""
    def __int__(self) -> Any:
        """IntegerMod_gmp.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2292)"""
    def __invert__(self) -> Any:
        """IntegerMod_gmp.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2359)

        Return the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: a = mod(3,10^100); type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>
            sage: ~a
            6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666667
            sage: ~mod(2,10^100)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of Mod(2, 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000) does not exist"""
    def __lshift__(self, IntegerMod_gmpself, k) -> Any:
        """IntegerMod_gmp.__lshift__(IntegerMod_gmp self, k)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2047)

        Perform a left shift by ``k`` bits.

        For details, see :meth:`shift`.

        EXAMPLES::

            sage: e = Mod(19, 10^10)
            sage: e << 102
            9443608576
            sage: e << (2^200)
            Traceback (most recent call last):
            ...
            OverflowError: Python int too large to convert to C long"""
    def __pow__(self, IntegerMod_gmpself, exp, m) -> Any:
        """IntegerMod_gmp.__pow__(IntegerMod_gmp self, exp, m)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2307)

        EXAMPLES::

            sage: R = Integers(10^10)
            sage: R(2)^1000
            5668069376
            sage: p = next_prime(11^10)                                                 # needs sage.libs.pari
            sage: R = Integers(p)                                                       # needs sage.libs.pari
            sage: R(9876)^(p-1)                                                         # needs sage.libs.pari
            1
            sage: mod(3, 10^100)^-2
            8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888889
            sage: mod(2, 10^100)^-2
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Inverse does not exist.

        TESTS:

        We define ``0^0`` to be unity, :issue:`13894`::

            sage: p = next_prime(11^10)                                                 # needs sage.libs.pari
            sage: R = Integers(p)                                                       # needs sage.libs.pari
            sage: R(0)^0
            1

        The value returned from ``0^0`` should belong to our ring::

            sage: type(R(0)^0) == type(R(0))
            True

        When the modulus is ``1``, the only element in the ring is
        ``0`` (and it is equivalent to ``1``), so we return that
        instead::

            sage: from sage.rings.finite_rings.integer_mod             ....:     import IntegerMod_gmp
            sage: zero = IntegerMod_gmp(Integers(1),0)
            sage: type(zero)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>
            sage: zero^0
            0"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, IntegerMod_gmpself, k) -> Any:
        """IntegerMod_gmp.__rshift__(IntegerMod_gmp self, k)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2065)

        Perform a right shift by ``k`` bits.

        For details, see :meth:`shift`.

        EXAMPLES::

            sage: e = Mod(19, 10^10)
            sage: e >> 1
            9
            sage: e << (2^200)
            Traceback (most recent call last):
            ...
            OverflowError: Python int too large to convert to C long"""

class IntegerMod_hom(sage.categories.morphism.Morphism):
    """IntegerMod_hom(parent)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4300)"""

class IntegerMod_int(IntegerMod_abstract):
    """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2448)

        Elements of `\\ZZ/n\\ZZ` for n small enough to
        be operated on in 32 bits

        AUTHORS:

        - Robert Bradshaw (2006-08-24)

        EXAMPLES::

            sage: a = Mod(10,30); a
            10
            sage: loads(a.dumps()) == a
            True
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def gcd(self, IntegerMod_intother) -> Any:
        '''IntegerMod_int.gcd(self, IntegerMod_int other)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3092)

        Greatest common divisor.

        Returns the "smallest" generator in `\\ZZ / N\\ZZ` of the ideal
        generated by ``self`` and ``other``.

        INPUT:

        - ``other`` -- an element of the same ring as this one

        EXAMPLES::

            sage: R = Zmod(60); S = Zmod(72)
            sage: a = R(40).gcd(S(30)); a
            2
            sage: a.parent()
            Ring of integers modulo 12
            sage: b = R(17).gcd(60); b
            1
            sage: b.parent()
            Ring of integers modulo 60

            sage: mod(72*5, 3^3*2^2*17^2).gcd(mod(48*17, 3^3*2^2*17^2))
            12
            sage: mod(0,1).gcd(mod(0,1))
            0'''
    @overload
    def is_one(self) -> bool:
        """IntegerMod_int.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2518)

        Return ``True`` if this is `1`, otherwise ``False``.

        EXAMPLES::

            sage: mod(6,5).is_one()
            True
            sage: mod(0,5).is_one()
            False
            sage: mod(1, 1).is_one()
            True
            sage: Zmod(1).one().is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """IntegerMod_int.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2518)

        Return ``True`` if this is `1`, otherwise ``False``.

        EXAMPLES::

            sage: mod(6,5).is_one()
            True
            sage: mod(0,5).is_one()
            False
            sage: mod(1, 1).is_one()
            True
            sage: Zmod(1).one().is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """IntegerMod_int.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2518)

        Return ``True`` if this is `1`, otherwise ``False``.

        EXAMPLES::

            sage: mod(6,5).is_one()
            True
            sage: mod(0,5).is_one()
            False
            sage: mod(1, 1).is_one()
            True
            sage: Zmod(1).one().is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """IntegerMod_int.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2518)

        Return ``True`` if this is `1`, otherwise ``False``.

        EXAMPLES::

            sage: mod(6,5).is_one()
            True
            sage: mod(0,5).is_one()
            False
            sage: mod(1, 1).is_one()
            True
            sage: Zmod(1).one().is_one()
            True"""
    @overload
    def is_one(self) -> Any:
        """IntegerMod_int.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2518)

        Return ``True`` if this is `1`, otherwise ``False``.

        EXAMPLES::

            sage: mod(6,5).is_one()
            True
            sage: mod(0,5).is_one()
            False
            sage: mod(1, 1).is_one()
            True
            sage: Zmod(1).one().is_one()
            True"""
    @overload
    def is_unit(self) -> bool:
        """IntegerMod_int.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2548)

        Return ``True`` iff this element is a unit

        EXAMPLES::

            sage: a=Mod(23,100)
            sage: a.is_unit()
            True
            sage: a=Mod(24,100)
            sage: a.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """IntegerMod_int.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2548)

        Return ``True`` iff this element is a unit

        EXAMPLES::

            sage: a=Mod(23,100)
            sage: a.is_unit()
            True
            sage: a=Mod(24,100)
            sage: a.is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """IntegerMod_int.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2548)

        Return ``True`` iff this element is a unit

        EXAMPLES::

            sage: a=Mod(23,100)
            sage: a.is_unit()
            True
            sage: a=Mod(24,100)
            sage: a.is_unit()
            False"""
    @overload
    def lift(self) -> Any:
        """IntegerMod_int.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2881)

        Lift an integer modulo `n` to the integers.

        EXAMPLES::

            sage: a = Mod(8943, 2^10); type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: lift(a)
            751
            sage: a.lift()
            751"""
    @overload
    def lift(self, a) -> Any:
        """IntegerMod_int.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2881)

        Lift an integer modulo `n` to the integers.

        EXAMPLES::

            sage: a = Mod(8943, 2^10); type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: lift(a)
            751
            sage: a.lift()
            751"""
    @overload
    def lift(self) -> Any:
        """IntegerMod_int.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2881)

        Lift an integer modulo `n` to the integers.

        EXAMPLES::

            sage: a = Mod(8943, 2^10); type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>
            sage: lift(a)
            751
            sage: a.lift()
            751"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, extend=...) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, extend=...) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, all=...) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    @overload
    def sqrt(self, extend=..., all=...) -> Any:
        """IntegerMod_int.sqrt(self, extend=True, all=False)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2935)

        Return square root or square roots of ``self`` modulo `n`.

        INPUT:

        - ``extend`` -- boolean (default: ``True``);
          if ``True``, return a square root in an extension ring,
          if necessary. Otherwise, raise a :exc:`ValueError` if the
          square root is not in the base ring.

        - ``all`` -- boolean (default: ``False``); if
          ``True``, return {all} square roots of self, instead of
          just one.

        ALGORITHM: Calculates the square roots mod `p` for each of
        the primes `p` dividing the order of the ring, then lifts
        them `p`-adically and uses the CRT to find a square root
        mod `n`.

        See also :meth:`square_root_mod_prime_power` and
        :meth:`square_root_mod_prime` for more algorithmic details.

        EXAMPLES::

            sage: mod(-1, 17).sqrt()
            4
            sage: mod(5, 389).sqrt()
            86
            sage: mod(7, 18).sqrt()
            5

            sage: # needs sage.libs.pari
            sage: a = mod(14, 5^60).sqrt()
            sage: a*a
            14
            sage: mod(15, 389).sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: Mod(1/9, next_prime(2^40)).sqrt()^(-2)
            9
            sage: Mod(1/25, next_prime(2^90)).sqrt()^(-2)
            25

        ::

            sage: a = Mod(3,5); a
            3
            sage: x = Mod(-1, 360)
            sage: x.sqrt(extend=False)
            Traceback (most recent call last):
            ...
            ValueError: self must be a square
            sage: y = x.sqrt(); y
            sqrt359
            sage: y.parent()
            Univariate Quotient Polynomial Ring in sqrt359
             over Ring of integers modulo 360 with modulus x^2 + 1
            sage: y^2
            359

        We compute all square roots in several cases::

            sage: R = Integers(5*2^3*3^2); R
            Ring of integers modulo 360
            sage: R(40).sqrt(all=True)
            [20, 160, 200, 340]
            sage: [x for x in R if x^2 == 40]  # Brute force verification
            [20, 160, 200, 340]
            sage: R(1).sqrt(all=True)
            [1, 19, 71, 89, 91, 109, 161, 179, 181, 199, 251, 269, 271, 289, 341, 359]
            sage: R(0).sqrt(all=True)
            [0, 60, 120, 180, 240, 300]
            sage: GF(107)(0).sqrt(all=True)
            [0]

        ::

            sage: # needs sage.libs.pari
            sage: R = Integers(5*13^3*37); R
            Ring of integers modulo 406445
            sage: v = R(-1).sqrt(all=True); v
            [78853, 111808, 160142, 193097, 213348, 246303, 294637, 327592]
            sage: [x^2 for x in v]
            [406444, 406444, 406444, 406444, 406444, 406444, 406444, 406444]
            sage: v = R(169).sqrt(all=True); min(v), -max(v), len(v)
            (13, 13, 104)
            sage: all(x^2 == 169 for x in v)
            True

        Modulo a power of 2::

            sage: R = Integers(2^7); R
            Ring of integers modulo 128
            sage: a = R(17)
            sage: a.sqrt()
            23
            sage: a.sqrt(all=True)
            [23, 41, 87, 105]
            sage: [x for x in R if x^2==17]
            [23, 41, 87, 105]

        TESTS:

        Check for :issue:`30797`::

            sage: GF(103)(-1).sqrt(extend=False, all=True)
            []"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """IntegerMod_int.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2594)

        EXAMPLES::

            sage: R = Integers(10)
            sage: R7 = R(7)
            sage: copy(R7) is R7
            True"""
    def __deepcopy__(self, memo) -> Any:
        """IntegerMod_int.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2606)

        EXAMPLES::

            sage: R = Integers(10)
            sage: R7 = R(7)
            sage: deepcopy(R7) is R7
            True"""
    def __float__(self) -> Any:
        """IntegerMod_int.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2899)"""
    def __hash__(self) -> Any:
        """IntegerMod_int.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2902)

        EXAMPLES::

            sage: a = Mod(89, 2^10)
            sage: hash(a)
            89"""
    def __index__(self) -> Any:
        """IntegerMod_int.__index__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2698)

        Needed so integers modulo `n` can be used as list indices.

        EXAMPLES::

            sage: v = [1,2,3,4,5]
            sage: v[Mod(10,7)]
            4"""
    def __int__(self) -> Any:
        """IntegerMod_int.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2688)

        TESTS::

            sage: e = Mod(8, 31)
            sage: int(e)
            8"""
    def __invert__(self) -> Any:
        """IntegerMod_int.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2861)

        Return the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: ~mod(7,100)
            43
            sage: Mod(0,1)^-1
            0"""
    def __lshift__(self, IntegerMod_intself, k) -> Any:
        """IntegerMod_int.__lshift__(IntegerMod_int self, k)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2710)

        Perform a left shift by ``k`` bits.

        For details, see :meth:`shift`.

        EXAMPLES::

            sage: e = Mod(5, 2^10 - 1)
            sage: e << 5
            160
            sage: e * 2^5
            160"""
    def __pow__(self, IntegerMod_intself, exp, m) -> Any:
        """IntegerMod_int.__pow__(IntegerMod_int self, exp, m)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2783)

        EXAMPLES::

            sage: R = Integers(10)
            sage: R(2)^10
            4
            sage: R = Integers(389)
            sage: R(7)^388
            1

            sage: mod(3, 100)^-1
            67
            sage: mod(3, 100)^-100000000
            1

            sage: mod(2, 100)^-1
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of Mod(2, 100) does not exist
            sage: mod(2, 100)^-100000000
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Inverse does not exist.

        TESTS:

        We define ``0^0`` to be unity, :issue:`13894`::

            sage: R = Integers(100)
            sage: R(0)^0
            1

        The value returned from ``0^0`` should belong to our ring::

            sage: type(R(0)^0) == type(R(0))
            True

        When the modulus is ``1``, the only element in the ring is
        ``0`` (and it is equivalent to ``1``), so we return that
        instead::

            sage: R = Integers(1)
            sage: R(0)^0
            0"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, IntegerMod_intself, k) -> Any:
        """IntegerMod_int.__rshift__(IntegerMod_int self, k)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 2726)

        Perform a right shift by ``k`` bits.

        For details, see :meth:`shift`.

        EXAMPLES::

            sage: e = Mod(5, 2^10 - 1)
            sage: e << 5
            160
            sage: e * 2^5
            160"""

class IntegerMod_int64(IntegerMod_abstract):
    """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3273)

        Elements of `\\ZZ/n\\ZZ` for n small enough to
        be operated on in 64 bits

        EXAMPLES::

            sage: a = Mod(10,3^10); a
            10
            sage: type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int64'>
            sage: loads(a.dumps()) == a
            True
            sage: Mod(5, 2^31)
            5

        AUTHORS:

        - Robert Bradshaw (2006-09-14)
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    def gcd(self, IntegerMod_int64other) -> Any:
        '''IntegerMod_int64.gcd(self, IntegerMod_int64 other)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3754)

        Greatest common divisor.

        Returns the "smallest" generator in `\\ZZ / N\\ZZ` of the ideal
        generated by ``self`` and ``other``.

        INPUT:

        - ``other`` -- an element of the same ring as this one

        EXAMPLES::

            sage: mod(2^3*3^2*5, 3^3*2^2*17^5).gcd(mod(2^4*3*17, 3^3*2^2*17^5))
            12
            sage: mod(0,17^5).gcd(mod(0,17^5))
            0'''
    @overload
    def is_one(self) -> bool:
        """IntegerMod_int64.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3346)

        Return ``True`` if this is `1`, otherwise ``False``.

        EXAMPLES::

            sage: (mod(-1,5^10)^2).is_one()
            True
            sage: mod(0,5^10).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """IntegerMod_int64.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3346)

        Return ``True`` if this is `1`, otherwise ``False``.

        EXAMPLES::

            sage: (mod(-1,5^10)^2).is_one()
            True
            sage: mod(0,5^10).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """IntegerMod_int64.is_one(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3346)

        Return ``True`` if this is `1`, otherwise ``False``.

        EXAMPLES::

            sage: (mod(-1,5^10)^2).is_one()
            True
            sage: mod(0,5^10).is_one()
            False"""
    @overload
    def is_unit(self) -> bool:
        """IntegerMod_int64.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3372)

        Return ``True`` iff this element is a unit.

        EXAMPLES::

            sage: mod(13, 5^10).is_unit()
            True
            sage: mod(25, 5^10).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """IntegerMod_int64.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3372)

        Return ``True`` iff this element is a unit.

        EXAMPLES::

            sage: mod(13, 5^10).is_unit()
            True
            sage: mod(25, 5^10).is_unit()
            False"""
    @overload
    def is_unit(self) -> Any:
        """IntegerMod_int64.is_unit(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3372)

        Return ``True`` iff this element is a unit.

        EXAMPLES::

            sage: mod(13, 5^10).is_unit()
            True
            sage: mod(25, 5^10).is_unit()
            False"""
    @overload
    def lift(self) -> Any:
        """IntegerMod_int64.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3703)

        Lift an integer modulo `n` to the integers.

        EXAMPLES::

            sage: a = Mod(8943, 2^25); type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int64'>
            sage: lift(a)
            8943
            sage: a.lift()
            8943"""
    @overload
    def lift(self, a) -> Any:
        """IntegerMod_int64.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3703)

        Lift an integer modulo `n` to the integers.

        EXAMPLES::

            sage: a = Mod(8943, 2^25); type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int64'>
            sage: lift(a)
            8943
            sage: a.lift()
            8943"""
    @overload
    def lift(self) -> Any:
        """IntegerMod_int64.lift(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3703)

        Lift an integer modulo `n` to the integers.

        EXAMPLES::

            sage: a = Mod(8943, 2^25); type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int64'>
            sage: lift(a)
            8943
            sage: a.lift()
            8943"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """IntegerMod_int64.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3427)

        EXAMPLES::

            sage: R = Integers(10^5)
            sage: R7 = R(7)
            sage: copy(R7) is R7
            True"""
    def __deepcopy__(self, memo) -> Any:
        """IntegerMod_int64.__deepcopy__(self, memo)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3439)

        EXAMPLES::

            sage: R = Integers(10^5)
            sage: R7 = R(7)
            sage: deepcopy(R7) is R7
            True"""
    def __float__(self) -> Any:
        """IntegerMod_int64.__float__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3721)

        Coerce ``self`` to a float.

        EXAMPLES::

            sage: a = Mod(8943, 2^35)
            sage: float(a)
            8943.0"""
    def __hash__(self) -> Any:
        """IntegerMod_int64.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3733)

        Compute hash of ``self``.

        EXAMPLES::

            sage: a = Mod(8943, 2^35)
            sage: hash(a)
            8943"""
    def __index__(self) -> Any:
        """IntegerMod_int64.__index__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3516)

        Needed so integers modulo `n` can be used as list indices.

        EXAMPLES::

            sage: v = [1,2,3,4,5]
            sage: v[Mod(3, 2^20)]
            4"""
    def __int__(self) -> Any:
        """IntegerMod_int64.__int__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3513)"""
    def __invert__(self) -> Any:
        """IntegerMod_int64.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3688)

        Return the multiplicative inverse of ``self``.

        EXAMPLES::

            sage: a = mod(7,2^40); type(a)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>
            sage: ~a
            471219269047
            sage: a
            7"""
    def __lshift__(self, IntegerMod_int64self, k) -> Any:
        """IntegerMod_int64.__lshift__(IntegerMod_int64 self, k)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3528)

        Perform a left shift by ``k`` bits.

        For details, see :meth:`shift`.

        EXAMPLES::

            sage: e = Mod(5, 2^31 - 1)
            sage: e << 32
            10
            sage: e * 2^32
            10"""
    def __pow__(self, IntegerMod_int64self, exp, m) -> Any:
        """IntegerMod_int64.__pow__(IntegerMod_int64 self, exp, m)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3599)

        EXAMPLES::

            sage: R = Integers(10)
            sage: R(2)^10
            4
            sage: p = next_prime(10^5)                                                  # needs sage.libs.pari
            sage: R = Integers(p)                                                       # needs sage.libs.pari
            sage: R(1234)^(p - 1)                                                       # needs sage.libs.pari
            1
            sage: R = Integers(17^5)
            sage: R(17)^5
            0

            sage: R(2)^-1 * 2
            1
            sage: R(2)^-1000000 * 2^1000000
            1
            sage: R(17)^-1
            Traceback (most recent call last):
            ...
            ZeroDivisionError: inverse of Mod(17, 1419857) does not exist
            sage: R(17)^-100000000
            Traceback (most recent call last):
            ...
            ZeroDivisionError: Inverse does not exist.

        TESTS::

            sage: type(R(0))
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int64'>

        We define ``0^0`` to be unity, :issue:`13894`::

            sage: p = next_prime(10^5)                                                  # needs sage.libs.pari
            sage: R = Integers(p)                                                       # needs sage.libs.pari
            sage: R(0)^0
            1

        The value returned from ``0^0`` should belong to our ring::

            sage: type(R(0)^0) == type(R(0))
            True

        When the modulus is ``1``, the only element in the ring is
        ``0`` (and it is equivalent to ``1``), so we return that
        instead::

            sage: from sage.rings.finite_rings.integer_mod             ....:     import IntegerMod_int64
            sage: zero = IntegerMod_int64(Integers(1),0)
            sage: type(zero)
            <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int64'>
            sage: zero^0
            0"""
    def __rlshift__(self, other):
        """Return value<<self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __rrshift__(self, other):
        """Return value>>self."""
    def __rshift__(self, IntegerMod_int64self, k) -> Any:
        """IntegerMod_int64.__rshift__(IntegerMod_int64 self, k)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 3544)

        Perform a right shift by ``k`` bits.

        For details, see :meth:`shift`.

        EXAMPLES::

            sage: e = Mod(5, 2^31 - 1)
            sage: e >> 1
            2"""

class IntegerMod_to_Integer(sage.categories.map.Map):
    """IntegerMod_to_Integer(R)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4502)

    Map to lift elements to :class:`~sage.rings.integer.Integer`.

    EXAMPLES::

        sage: ZZ.convert_map_from(GF(2))
        Lifting map:
          From: Finite Field of size 2
          To:   Integer Ring"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4513)

                TESTS:

                Lifting maps are morphisms in the category of sets (see
                :issue:`15618`)::

                    sage: ZZ.convert_map_from(GF(2)).parent()
                    Set of Morphisms from Finite Field of size 2 to Integer Ring in Category of sets
        """

class IntegerMod_to_IntegerMod(IntegerMod_hom):
    """IntegerMod_to_IntegerMod(R, S)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4364)

    Very fast IntegerMod to IntegerMod homomorphism.

    EXAMPLES::

        sage: from sage.rings.finite_rings.integer_mod import IntegerMod_to_IntegerMod
        sage: Rs = [Integers(3**k) for k in range(1,30,5)]
        sage: [type(R(0)) for R in Rs]
        [<class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>,
         <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>,
         <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int64'>,
         <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int64'>,
         <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>,
         <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>]
        sage: fs = [IntegerMod_to_IntegerMod(S, R)
        ....:       for R in Rs for S in Rs if S is not R and S.order() > R.order()]
        sage: all(f(-1) == f.codomain()(-1) for f in fs)
        True
        sage: [f(-1) for f in fs]
        [2, 2, 2, 2, 2, 728, 728, 728, 728, 177146, 177146, 177146, 43046720, 43046720, 10460353202]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @overload
    def __init__(self, R, S) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4386)"""
    @overload
    def __init__(self, S, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4386)"""
    @overload
    def is_injective(self) -> Any:
        """IntegerMod_to_IntegerMod.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4422)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: Zmod(4).hom(Zmod(2)).is_injective()
            False"""
    @overload
    def is_injective(self) -> Any:
        """IntegerMod_to_IntegerMod.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4422)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: Zmod(4).hom(Zmod(2)).is_injective()
            False"""
    @overload
    def is_surjective(self) -> Any:
        """IntegerMod_to_IntegerMod.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4411)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: Zmod(4).hom(Zmod(2)).is_surjective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """IntegerMod_to_IntegerMod.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4411)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: Zmod(4).hom(Zmod(2)).is_surjective()
            True"""

class Integer_to_IntegerMod(IntegerMod_hom):
    """Integer_to_IntegerMod(R)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4433)

    Fast `\\ZZ \\rightarrow \\ZZ/n\\ZZ` morphism.

    EXAMPLES:

    We make sure it works for every type.

    ::

        sage: from sage.rings.finite_rings.integer_mod import Integer_to_IntegerMod
        sage: Rs = [Integers(10), Integers(10^5), Integers(10^10)]
        sage: [type(R(0)) for R in Rs]
        [<class 'sage.rings.finite_rings.integer_mod.IntegerMod_int'>,
         <class 'sage.rings.finite_rings.integer_mod.IntegerMod_int64'>,
         <class 'sage.rings.finite_rings.integer_mod.IntegerMod_gmp'>]
        sage: fs = [Integer_to_IntegerMod(R) for R in Rs]
        sage: [f(-1) for f in fs]
        [9, 99999, 9999999999]"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, R) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4453)"""
    @overload
    def is_injective(self) -> Any:
        """Integer_to_IntegerMod.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4490)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: ZZ.hom(Zmod(2)).is_injective()
            False"""
    @overload
    def is_injective(self) -> Any:
        """Integer_to_IntegerMod.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4490)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: ZZ.hom(Zmod(2)).is_injective()
            False"""
    @overload
    def is_surjective(self) -> Any:
        """Integer_to_IntegerMod.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4479)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: ZZ.hom(Zmod(2)).is_surjective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """Integer_to_IntegerMod.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4479)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: ZZ.hom(Zmod(2)).is_surjective()
            True"""
    def section(self) -> Any:
        """Integer_to_IntegerMod.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 4476)"""

class NativeIntStruct:
    """NativeIntStruct(m)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 239)

    We store the various forms of the modulus here rather than in the
    parent for efficiency reasons.

    We may also store a cached table of all elements of a given ring in
    this class."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    inverses: File
    table: File
    def __init__(self, m) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 251)"""
    @overload
    def precompute_table(self, parent) -> Any:
        """NativeIntStruct.precompute_table(self, parent)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 274)

        Function to compute and cache all elements of this class.

        If ``inverses == True``, also computes and caches the inverses
        of the invertible elements.

        EXAMPLES::

            sage: from sage.rings.finite_rings.integer_mod import NativeIntStruct
            sage: R = IntegerModRing(10)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            sage: M.table
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: M.inverses
            [None, 1, None, 7, None, None, None, 3, None, 9]

        This is used by the :class:`sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic` constructor::

            sage: from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
            sage: R = IntegerModRing_generic(39, cache=False)
            sage: R(5)^-1
            8
            sage: R(5)^-1 is R(8)
            False
            sage: R = IntegerModRing_generic(39, cache=True)  # indirect doctest
            sage: R(5)^-1 is R(8)
            True

        Check that the inverse of 0 modulo 1 works, see :issue:`13639`::

            sage: R = IntegerModRing_generic(1, cache=True)  # indirect doctest
            sage: R(0)^-1 is R(0)
            True

        TESTS::

            sage: R = IntegerModRing(10^50)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            Traceback (most recent call last):
            ...
            OverflowError: precompute_table() is only supported for small moduli"""
    @overload
    def precompute_table(self, R) -> Any:
        """NativeIntStruct.precompute_table(self, parent)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 274)

        Function to compute and cache all elements of this class.

        If ``inverses == True``, also computes and caches the inverses
        of the invertible elements.

        EXAMPLES::

            sage: from sage.rings.finite_rings.integer_mod import NativeIntStruct
            sage: R = IntegerModRing(10)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            sage: M.table
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: M.inverses
            [None, 1, None, 7, None, None, None, 3, None, 9]

        This is used by the :class:`sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic` constructor::

            sage: from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
            sage: R = IntegerModRing_generic(39, cache=False)
            sage: R(5)^-1
            8
            sage: R(5)^-1 is R(8)
            False
            sage: R = IntegerModRing_generic(39, cache=True)  # indirect doctest
            sage: R(5)^-1 is R(8)
            True

        Check that the inverse of 0 modulo 1 works, see :issue:`13639`::

            sage: R = IntegerModRing_generic(1, cache=True)  # indirect doctest
            sage: R(0)^-1 is R(0)
            True

        TESTS::

            sage: R = IntegerModRing(10^50)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            Traceback (most recent call last):
            ...
            OverflowError: precompute_table() is only supported for small moduli"""
    @overload
    def precompute_table(self, R) -> Any:
        """NativeIntStruct.precompute_table(self, parent)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 274)

        Function to compute and cache all elements of this class.

        If ``inverses == True``, also computes and caches the inverses
        of the invertible elements.

        EXAMPLES::

            sage: from sage.rings.finite_rings.integer_mod import NativeIntStruct
            sage: R = IntegerModRing(10)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            sage: M.table
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: M.inverses
            [None, 1, None, 7, None, None, None, 3, None, 9]

        This is used by the :class:`sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic` constructor::

            sage: from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
            sage: R = IntegerModRing_generic(39, cache=False)
            sage: R(5)^-1
            8
            sage: R(5)^-1 is R(8)
            False
            sage: R = IntegerModRing_generic(39, cache=True)  # indirect doctest
            sage: R(5)^-1 is R(8)
            True

        Check that the inverse of 0 modulo 1 works, see :issue:`13639`::

            sage: R = IntegerModRing_generic(1, cache=True)  # indirect doctest
            sage: R(0)^-1 is R(0)
            True

        TESTS::

            sage: R = IntegerModRing(10^50)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            Traceback (most recent call last):
            ...
            OverflowError: precompute_table() is only supported for small moduli"""
    @overload
    def precompute_table(self) -> Any:
        """NativeIntStruct.precompute_table(self, parent)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 274)

        Function to compute and cache all elements of this class.

        If ``inverses == True``, also computes and caches the inverses
        of the invertible elements.

        EXAMPLES::

            sage: from sage.rings.finite_rings.integer_mod import NativeIntStruct
            sage: R = IntegerModRing(10)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            sage: M.table
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: M.inverses
            [None, 1, None, 7, None, None, None, 3, None, 9]

        This is used by the :class:`sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic` constructor::

            sage: from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
            sage: R = IntegerModRing_generic(39, cache=False)
            sage: R(5)^-1
            8
            sage: R(5)^-1 is R(8)
            False
            sage: R = IntegerModRing_generic(39, cache=True)  # indirect doctest
            sage: R(5)^-1 is R(8)
            True

        Check that the inverse of 0 modulo 1 works, see :issue:`13639`::

            sage: R = IntegerModRing_generic(1, cache=True)  # indirect doctest
            sage: R(0)^-1 is R(0)
            True

        TESTS::

            sage: R = IntegerModRing(10^50)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            Traceback (most recent call last):
            ...
            OverflowError: precompute_table() is only supported for small moduli"""
    def __reduce__(self) -> Any:
        """NativeIntStruct.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 262)

        TESTS::

            sage: from sage.rings.finite_rings.integer_mod import NativeIntStruct
            sage: M = NativeIntStruct(12345); M
            NativeIntStruct(12345)
            sage: loads(dumps(M))
            NativeIntStruct(12345)"""

class makeNativeIntStruct:
    """NativeIntStruct(m)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 239)

    We store the various forms of the modulus here rather than in the
    parent for efficiency reasons.

    We may also store a cached table of all elements of a given ring in
    this class."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    inverses: File
    table: File
    def __init__(self, *args, **kwargs) -> None:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 251)"""
    @overload
    def precompute_table(self, parent) -> Any:
        """NativeIntStruct.precompute_table(self, parent)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 274)

        Function to compute and cache all elements of this class.

        If ``inverses == True``, also computes and caches the inverses
        of the invertible elements.

        EXAMPLES::

            sage: from sage.rings.finite_rings.integer_mod import NativeIntStruct
            sage: R = IntegerModRing(10)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            sage: M.table
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: M.inverses
            [None, 1, None, 7, None, None, None, 3, None, 9]

        This is used by the :class:`sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic` constructor::

            sage: from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
            sage: R = IntegerModRing_generic(39, cache=False)
            sage: R(5)^-1
            8
            sage: R(5)^-1 is R(8)
            False
            sage: R = IntegerModRing_generic(39, cache=True)  # indirect doctest
            sage: R(5)^-1 is R(8)
            True

        Check that the inverse of 0 modulo 1 works, see :issue:`13639`::

            sage: R = IntegerModRing_generic(1, cache=True)  # indirect doctest
            sage: R(0)^-1 is R(0)
            True

        TESTS::

            sage: R = IntegerModRing(10^50)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            Traceback (most recent call last):
            ...
            OverflowError: precompute_table() is only supported for small moduli"""
    @overload
    def precompute_table(self, R) -> Any:
        """NativeIntStruct.precompute_table(self, parent)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 274)

        Function to compute and cache all elements of this class.

        If ``inverses == True``, also computes and caches the inverses
        of the invertible elements.

        EXAMPLES::

            sage: from sage.rings.finite_rings.integer_mod import NativeIntStruct
            sage: R = IntegerModRing(10)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            sage: M.table
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: M.inverses
            [None, 1, None, 7, None, None, None, 3, None, 9]

        This is used by the :class:`sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic` constructor::

            sage: from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
            sage: R = IntegerModRing_generic(39, cache=False)
            sage: R(5)^-1
            8
            sage: R(5)^-1 is R(8)
            False
            sage: R = IntegerModRing_generic(39, cache=True)  # indirect doctest
            sage: R(5)^-1 is R(8)
            True

        Check that the inverse of 0 modulo 1 works, see :issue:`13639`::

            sage: R = IntegerModRing_generic(1, cache=True)  # indirect doctest
            sage: R(0)^-1 is R(0)
            True

        TESTS::

            sage: R = IntegerModRing(10^50)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            Traceback (most recent call last):
            ...
            OverflowError: precompute_table() is only supported for small moduli"""
    @overload
    def precompute_table(self, R) -> Any:
        """NativeIntStruct.precompute_table(self, parent)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 274)

        Function to compute and cache all elements of this class.

        If ``inverses == True``, also computes and caches the inverses
        of the invertible elements.

        EXAMPLES::

            sage: from sage.rings.finite_rings.integer_mod import NativeIntStruct
            sage: R = IntegerModRing(10)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            sage: M.table
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: M.inverses
            [None, 1, None, 7, None, None, None, 3, None, 9]

        This is used by the :class:`sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic` constructor::

            sage: from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
            sage: R = IntegerModRing_generic(39, cache=False)
            sage: R(5)^-1
            8
            sage: R(5)^-1 is R(8)
            False
            sage: R = IntegerModRing_generic(39, cache=True)  # indirect doctest
            sage: R(5)^-1 is R(8)
            True

        Check that the inverse of 0 modulo 1 works, see :issue:`13639`::

            sage: R = IntegerModRing_generic(1, cache=True)  # indirect doctest
            sage: R(0)^-1 is R(0)
            True

        TESTS::

            sage: R = IntegerModRing(10^50)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            Traceback (most recent call last):
            ...
            OverflowError: precompute_table() is only supported for small moduli"""
    @overload
    def precompute_table(self) -> Any:
        """NativeIntStruct.precompute_table(self, parent)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 274)

        Function to compute and cache all elements of this class.

        If ``inverses == True``, also computes and caches the inverses
        of the invertible elements.

        EXAMPLES::

            sage: from sage.rings.finite_rings.integer_mod import NativeIntStruct
            sage: R = IntegerModRing(10)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            sage: M.table
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            sage: M.inverses
            [None, 1, None, 7, None, None, None, 3, None, 9]

        This is used by the :class:`sage.rings.finite_rings.integer_mod_ring.IntegerModRing_generic` constructor::

            sage: from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
            sage: R = IntegerModRing_generic(39, cache=False)
            sage: R(5)^-1
            8
            sage: R(5)^-1 is R(8)
            False
            sage: R = IntegerModRing_generic(39, cache=True)  # indirect doctest
            sage: R(5)^-1 is R(8)
            True

        Check that the inverse of 0 modulo 1 works, see :issue:`13639`::

            sage: R = IntegerModRing_generic(1, cache=True)  # indirect doctest
            sage: R(0)^-1 is R(0)
            True

        TESTS::

            sage: R = IntegerModRing(10^50)
            sage: M = NativeIntStruct(R.order())
            sage: M.precompute_table(R)
            Traceback (most recent call last):
            ...
            OverflowError: precompute_table() is only supported for small moduli"""
    def __reduce__(self) -> Any:
        """NativeIntStruct.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/integer_mod.pyx (starting at line 262)

        TESTS::

            sage: from sage.rings.finite_rings.integer_mod import NativeIntStruct
            sage: M = NativeIntStruct(12345); M
            NativeIntStruct(12345)
            sage: loads(dumps(M))
            NativeIntStruct(12345)"""
