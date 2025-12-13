import sage.categories.map
import sage.rings.morphism
from sage.categories.homset import Hom as Hom
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.finite_rings.finite_field_base import FiniteField_base as FiniteField_base
from sage.rings.finite_rings.finite_field_constructor import FiniteField as FiniteField
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class FiniteFieldHomomorphism_generic(sage.rings.morphism.RingHomomorphism_im_gens):
    """FiniteFieldHomomorphism_generic(parent, im_gens=None, base_map=None, check=True, section_class=None)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 186)

    A class implementing embeddings between finite fields.

    TESTS::

        sage: from sage.rings.finite_rings.hom_finite_field import FiniteFieldHomomorphism_generic
        sage: k.<t> = GF(3^7)
        sage: K.<T> = GF(3^21)
        sage: f = FiniteFieldHomomorphism_generic(Hom(k, K))
        sage: TestSuite(f).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, im_gens=..., base_map=..., check=..., section_class=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 198)

                TESTS::

                    sage: from sage.rings.finite_rings.hom_finite_field import FiniteFieldHomomorphism_generic
                    sage: k.<t> = GF(3^7)
                    sage: K.<T> = GF(3^21)
                    sage: f = FiniteFieldHomomorphism_generic(Hom(k, K)); f # random
                    Ring morphism:
                      From: Finite Field in t of size 3^7
                      To:   Finite Field in T of size 3^21
                      Defn: t |--> T^20 + 2*T^18 + T^16 + 2*T^13 + T^9 + 2*T^8 + T^7 + T^6 + T^5 + T^3 + 2*T^2 + T
                    sage: a = k.random_element()
                    sage: b = k.random_element()
                    sage: f(a) + f(b) == f(a + b)
                    True

                    sage: k.<t> = GF(3^6)
                    sage: K.<t> = GF(3^9)
                    sage: FiniteFieldHomomorphism_generic(Hom(k, K))
                    Traceback (most recent call last):
                    ...
                    ValueError: No embedding of Finite Field in t of size 3^6 into Finite Field in t of size 3^9

                    sage: FiniteFieldHomomorphism_generic(Hom(ZZ, QQ))
                    Traceback (most recent call last):
                    ...
                    TypeError: The domain is not a finite field or does not provide the required interface for finite fields

                    sage: R.<x> = k[]
                    sage: FiniteFieldHomomorphism_generic(Hom(k, R))
                    Traceback (most recent call last):
                    ...
                    TypeError: The codomain is not a finite field or does not provide the required interface for finite fields
        """
    @overload
    def is_injective(self) -> Any:
        """FiniteFieldHomomorphism_generic.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 322)

        Return ``True`` since a embedding between finite fields is
        always injective.

        EXAMPLES::

            sage: from sage.rings.finite_rings.hom_finite_field import FiniteFieldHomomorphism_generic
            sage: k.<t> = GF(3^3)
            sage: K.<T> = GF(3^9)
            sage: f = FiniteFieldHomomorphism_generic(Hom(k, K))
            sage: f.is_injective()
            True"""
    @overload
    def is_injective(self) -> Any:
        """FiniteFieldHomomorphism_generic.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 322)

        Return ``True`` since a embedding between finite fields is
        always injective.

        EXAMPLES::

            sage: from sage.rings.finite_rings.hom_finite_field import FiniteFieldHomomorphism_generic
            sage: k.<t> = GF(3^3)
            sage: K.<T> = GF(3^9)
            sage: f = FiniteFieldHomomorphism_generic(Hom(k, K))
            sage: f.is_injective()
            True"""
    def is_surjective(self) -> Any:
        """FiniteFieldHomomorphism_generic.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 338)

        Return ``True`` if this embedding is surjective (and hence an
        isomorphism.

        EXAMPLES::

            sage: from sage.rings.finite_rings.hom_finite_field import FiniteFieldHomomorphism_generic
            sage: k.<t> = GF(3^3)
            sage: K.<T> = GF(3^9)
            sage: f = FiniteFieldHomomorphism_generic(Hom(k, K))
            sage: f.is_surjective()
            False
            sage: g = FiniteFieldHomomorphism_generic(Hom(k, k))
            sage: g.is_surjective()
            True"""
    @overload
    def section(self) -> Any:
        """FiniteFieldHomomorphism_generic.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 357)

        Return the ``inverse`` of this embedding.

        It is a partially defined map whose domain is the codomain
        of the embedding, but which is only defined on the image of
        the embedding.

        EXAMPLES::

            sage: from sage.rings.finite_rings.hom_finite_field import FiniteFieldHomomorphism_generic
            sage: k.<t> = GF(3^7)
            sage: K.<T> = GF(3^21)
            sage: f = FiniteFieldHomomorphism_generic(Hom(k, K))
            sage: g = f.section(); g # random
            Section of Ring morphism:
              From: Finite Field in t of size 3^7
              To:   Finite Field in T of size 3^21
              Defn: t |--> T^20 + 2*T^18 + T^16 + 2*T^13 + T^9 + 2*T^8 + T^7 + T^6 + T^5 + T^3 + 2*T^2 + T
            sage: a = k.random_element()
            sage: b = k.random_element()
            sage: g(f(a) + f(b)) == a + b
            True
            sage: g(T)
            Traceback (most recent call last):
            ...
            ValueError: T is not in the image of Ring morphism:
              From: Finite Field in t of size 3^7
              To:   Finite Field in T of size 3^21
              Defn: ..."""
    @overload
    def section(self) -> Any:
        """FiniteFieldHomomorphism_generic.section(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 357)

        Return the ``inverse`` of this embedding.

        It is a partially defined map whose domain is the codomain
        of the embedding, but which is only defined on the image of
        the embedding.

        EXAMPLES::

            sage: from sage.rings.finite_rings.hom_finite_field import FiniteFieldHomomorphism_generic
            sage: k.<t> = GF(3^7)
            sage: K.<T> = GF(3^21)
            sage: f = FiniteFieldHomomorphism_generic(Hom(k, K))
            sage: g = f.section(); g # random
            Section of Ring morphism:
              From: Finite Field in t of size 3^7
              To:   Finite Field in T of size 3^21
              Defn: t |--> T^20 + 2*T^18 + T^16 + 2*T^13 + T^9 + 2*T^8 + T^7 + T^6 + T^5 + T^3 + 2*T^2 + T
            sage: a = k.random_element()
            sage: b = k.random_element()
            sage: g(f(a) + f(b)) == a + b
            True
            sage: g(T)
            Traceback (most recent call last):
            ...
            ValueError: T is not in the image of Ring morphism:
              From: Finite Field in t of size 3^7
              To:   Finite Field in T of size 3^21
              Defn: ..."""
    def __copy__(self) -> Any:
        """FiniteFieldHomomorphism_generic.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 250)

        Return a copy of this map.

        TESTS::

            sage: from sage.rings.finite_rings.hom_finite_field import FiniteFieldHomomorphism_generic
            sage: k.<t> = GF(3^7)
            sage: K.<T> = GF(3^21)
            sage: f = FiniteFieldHomomorphism_generic(Hom(k, K))
            sage: g = copy(f)
            sage: g.section()(g(t)) == f.section()(f(t))
            True

        ::

            sage: F = GF(2)
            sage: E = GF(4)
            sage: phi = E.coerce_map_from(F); phi
            Ring morphism:
              From: Finite Field of size 2
              To:   Finite Field in z2 of size 2^2
              Defn: 1 |--> 1
            sage: phi.section()
            Section of Ring morphism:
              From: Finite Field of size 2
              To:   Finite Field in z2 of size 2^2
              Defn: 1 |--> 1"""
    def __hash__(self) -> Any:
        """FiniteFieldHomomorphism_generic.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 418)

        Return a hash of this morphism.

        TESTS::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: embed = Frob.fixed_field()[1]
            sage: hash(embed) # random
            -2441354824160407762"""

class FrobeniusEndomorphism_finite_field(sage.rings.morphism.FrobeniusEndomorphism_generic):
    """FrobeniusEndomorphism_finite_field(domain, n=1)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 482)

    A class implementing Frobenius endomorphisms on finite fields.

    TESTS::

        sage: k.<a> = GF(7^11)
        sage: Frob = k.frobenius_endomorphism(5)
        sage: TestSuite(Frob).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, domain, n=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 492)

                INPUT:

                - ``domain`` -- a finite field

                - ``n`` -- integer (default: 1)

                .. NOTE::

                    `n` may be negative.

                OUTPUT:

                The `n`-th power of the absolute (arithmetic) Frobenius
                endomorphism on ``domain``

                TESTS::

                    sage: from sage.rings.finite_rings.hom_finite_field import FrobeniusEndomorphism_finite_field
                    sage: k.<t> = GF(5^3)
                    sage: FrobeniusEndomorphism_finite_field(k)
                    Frobenius endomorphism t |--> t^5 on Finite Field in t of size 5^3
                    sage: FrobeniusEndomorphism_finite_field(k, 2)
                    Frobenius endomorphism t |--> t^(5^2) on Finite Field in t of size 5^3

                    sage: FrobeniusEndomorphism_finite_field(k, t)
                    Traceback (most recent call last):
                    ...
                    TypeError: n (=t) is not an integer

                    sage: FrobeniusEndomorphism_finite_field(k['x'])
                    Traceback (most recent call last):
                    ...
                    TypeError: The domain is not a finite field or does not provide the required interface for finite fields
        """
    @overload
    def fixed_field(self) -> Any:
        """FrobeniusEndomorphism_finite_field.fixed_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 727)

        Return the fixed field of ``self``.

        OUTPUT:

        - a tuple `(K, e)`, where `K` is the subfield of the domain
          consisting of elements fixed by ``self`` and `e` is an
          embedding of `K` into the domain.

        .. NOTE::

            The name of the variable used for the subfield (if it
            is not a prime subfield) is suffixed by ``_fixed``.

        EXAMPLES::

            sage: k.<t> = GF(5^6)
            sage: f = k.frobenius_endomorphism(2)
            sage: kfixed, embed = f.fixed_field()
            sage: kfixed
            Finite Field in t_fixed of size 5^2
            sage: embed # random
            Ring morphism:
              From: Finite Field in t_fixed of size 5^2
              To:   Finite Field in t of size 5^6
              Defn: t_fixed |--> 4*t^5 + 2*t^4 + 4*t^2 + t

            sage: tfixed = kfixed.gen()
            sage: embed(tfixed) # random
            4*t^5 + 2*t^4 + 4*t^2 + t
            sage: embed(tfixed) == embed.im_gens()[0]
            True"""
    @overload
    def fixed_field(self) -> Any:
        """FrobeniusEndomorphism_finite_field.fixed_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 727)

        Return the fixed field of ``self``.

        OUTPUT:

        - a tuple `(K, e)`, where `K` is the subfield of the domain
          consisting of elements fixed by ``self`` and `e` is an
          embedding of `K` into the domain.

        .. NOTE::

            The name of the variable used for the subfield (if it
            is not a prime subfield) is suffixed by ``_fixed``.

        EXAMPLES::

            sage: k.<t> = GF(5^6)
            sage: f = k.frobenius_endomorphism(2)
            sage: kfixed, embed = f.fixed_field()
            sage: kfixed
            Finite Field in t_fixed of size 5^2
            sage: embed # random
            Ring morphism:
              From: Finite Field in t_fixed of size 5^2
              To:   Finite Field in t of size 5^6
              Defn: t_fixed |--> 4*t^5 + 2*t^4 + 4*t^2 + t

            sage: tfixed = kfixed.gen()
            sage: embed(tfixed) # random
            4*t^5 + 2*t^4 + 4*t^2 + t
            sage: embed(tfixed) == embed.im_gens()[0]
            True"""
    @overload
    def inverse(self) -> Any:
        """FrobeniusEndomorphism_finite_field.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 687)

        Return the inverse of this Frobenius endomorphism.

        EXAMPLES::

            sage: k.<a> = GF(7^11)
            sage: f = k.frobenius_endomorphism(5)
            sage: (f.inverse() * f).is_identity()
            True"""
    @overload
    def inverse(self) -> Any:
        """FrobeniusEndomorphism_finite_field.inverse(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 687)

        Return the inverse of this Frobenius endomorphism.

        EXAMPLES::

            sage: k.<a> = GF(7^11)
            sage: f = k.frobenius_endomorphism(5)
            sage: (f.inverse() * f).is_identity()
            True"""
    @overload
    def is_identity(self) -> Any:
        """FrobeniusEndomorphism_finite_field.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 799)

        Return ``True`` if this morphism is the identity morphism.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.is_identity()
            False
            sage: (Frob^3).is_identity()
            True"""
    @overload
    def is_identity(self) -> Any:
        """FrobeniusEndomorphism_finite_field.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 799)

        Return ``True`` if this morphism is the identity morphism.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.is_identity()
            False
            sage: (Frob^3).is_identity()
            True"""
    @overload
    def is_identity(self) -> Any:
        """FrobeniusEndomorphism_finite_field.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 799)

        Return ``True`` if this morphism is the identity morphism.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.is_identity()
            False
            sage: (Frob^3).is_identity()
            True"""
    @overload
    def is_injective(self) -> Any:
        """FrobeniusEndomorphism_finite_field.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 771)

        Return ``True`` since any power of the Frobenius endomorphism
        over a finite field is always injective.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.is_injective()
            True"""
    @overload
    def is_injective(self) -> Any:
        """FrobeniusEndomorphism_finite_field.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 771)

        Return ``True`` since any power of the Frobenius endomorphism
        over a finite field is always injective.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.is_injective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """FrobeniusEndomorphism_finite_field.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 785)

        Return ``True`` since any power of the Frobenius endomorphism
        over a finite field is always surjective.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.is_surjective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """FrobeniusEndomorphism_finite_field.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 785)

        Return ``True`` since any power of the Frobenius endomorphism
        over a finite field is always surjective.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.is_surjective()
            True"""
    @overload
    def order(self) -> Any:
        """FrobeniusEndomorphism_finite_field.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 626)

        Return the order of this endomorphism.

        EXAMPLES::

            sage: k.<t> = GF(5^12)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.order()
            12
            sage: (Frob^2).order()
            6
            sage: (Frob^9).order()
            4"""
    @overload
    def order(self) -> Any:
        """FrobeniusEndomorphism_finite_field.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 626)

        Return the order of this endomorphism.

        EXAMPLES::

            sage: k.<t> = GF(5^12)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.order()
            12
            sage: (Frob^2).order()
            6
            sage: (Frob^9).order()
            4"""
    @overload
    def order(self) -> Any:
        """FrobeniusEndomorphism_finite_field.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 626)

        Return the order of this endomorphism.

        EXAMPLES::

            sage: k.<t> = GF(5^12)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.order()
            12
            sage: (Frob^2).order()
            6
            sage: (Frob^9).order()
            4"""
    @overload
    def order(self) -> Any:
        """FrobeniusEndomorphism_finite_field.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 626)

        Return the order of this endomorphism.

        EXAMPLES::

            sage: k.<t> = GF(5^12)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.order()
            12
            sage: (Frob^2).order()
            6
            sage: (Frob^9).order()
            4"""
    @overload
    def power(self) -> Any:
        """FrobeniusEndomorphism_finite_field.power(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 647)

        Return an integer `n` such that this endomorphism
        is the `n`-th power of the absolute (arithmetic)
        Frobenius.

        EXAMPLES::

            sage: k.<t> = GF(5^12)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.power()
            1
            sage: (Frob^9).power()
            9
            sage: (Frob^13).power()
            1"""
    @overload
    def power(self) -> Any:
        """FrobeniusEndomorphism_finite_field.power(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 647)

        Return an integer `n` such that this endomorphism
        is the `n`-th power of the absolute (arithmetic)
        Frobenius.

        EXAMPLES::

            sage: k.<t> = GF(5^12)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.power()
            1
            sage: (Frob^9).power()
            9
            sage: (Frob^13).power()
            1"""
    @overload
    def power(self) -> Any:
        """FrobeniusEndomorphism_finite_field.power(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 647)

        Return an integer `n` such that this endomorphism
        is the `n`-th power of the absolute (arithmetic)
        Frobenius.

        EXAMPLES::

            sage: k.<t> = GF(5^12)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.power()
            1
            sage: (Frob^9).power()
            9
            sage: (Frob^13).power()
            1"""
    @overload
    def power(self) -> Any:
        """FrobeniusEndomorphism_finite_field.power(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 647)

        Return an integer `n` such that this endomorphism
        is the `n`-th power of the absolute (arithmetic)
        Frobenius.

        EXAMPLES::

            sage: k.<t> = GF(5^12)
            sage: Frob = k.frobenius_endomorphism()
            sage: Frob.power()
            1
            sage: (Frob^9).power()
            9
            sage: (Frob^13).power()
            1"""
    def __hash__(self) -> Any:
        """FrobeniusEndomorphism_finite_field.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 814)

        Return a hash of this morphism.

        EXAMPLES::

            sage: k.<t> = GF(5^3)
            sage: Frob = k.frobenius_endomorphism()
            sage: hash(Frob)  # random
            383183030479672104"""
    def __pow__(self, n, modulus) -> Any:
        """FrobeniusEndomorphism_finite_field.__pow__(self, n, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 666)

        Return the `n`-th iterate of this endomorphism.

        EXAMPLES::

            sage: k.<t> = GF(5^12)
            sage: Frob = k.frobenius_endomorphism(); Frob
            Frobenius endomorphism t |--> t^5 on Finite Field in t of size 5^12
            sage: Frob^2
            Frobenius endomorphism t |--> t^(5^2) on Finite Field in t of size 5^12

        The result is simplified if possible::

            sage: Frob^15
            Frobenius endomorphism t |--> t^(5^3) on Finite Field in t of size 5^12
            sage: Frob^36
            Identity endomorphism of Finite Field in t of size 5^12"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class SectionFiniteFieldHomomorphism_generic(sage.categories.map.Section):
    """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_finite_field.pyx (starting at line 123)

        A class implementing sections of embeddings between finite fields.
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
