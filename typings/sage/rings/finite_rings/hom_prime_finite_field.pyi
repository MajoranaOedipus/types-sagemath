import sage.rings.finite_rings.hom_finite_field
from sage.categories.homset import Hom as Hom
from sage.rings.finite_rings.finite_field_base import FiniteField as FiniteField
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class FiniteFieldHomomorphism_prime(sage.rings.finite_rings.hom_finite_field.FiniteFieldHomomorphism_generic):
    """FiniteFieldHomomorphism_prime(parent, im_gens=None, base_map=None, check=False, section_class=None)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_prime_finite_field.pyx (starting at line 45)

    A class implementing embeddings of prime finite fields into
    general finite fields."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, im_gens=..., base_map=..., check=..., section_class=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_prime_finite_field.pyx (starting at line 50)

                TESTS::

                    sage: from sage.rings.finite_rings.hom_prime_finite_field import FiniteFieldHomomorphism_prime
                    sage: k = GF(3)
                    sage: K.<T> = GF(3^4)                                                       # needs sage.rings.finite_rings
                    sage: f = FiniteFieldHomomorphism_prime(Hom(k, K)); f                       # needs sage.rings.finite_rings
                    Ring morphism:
                      From: Finite Field of size 3
                      To:   Finite Field in T of size 3^4
                      Defn: 1 |--> 1

                    sage: k.<t> = GF(3^2)                                                       # needs sage.rings.finite_rings
                    sage: K.<T> = GF(3^4)                                                       # needs sage.rings.finite_rings
                    sage: f = FiniteFieldHomomorphism_prime(Hom(k, K)); f                       # needs sage.rings.finite_rings
                    Traceback (most recent call last):
                    ...
                    TypeError: The domain is not a finite prime field
        """

class FrobeniusEndomorphism_prime(sage.rings.finite_rings.hom_finite_field.FrobeniusEndomorphism_finite_field):
    """FrobeniusEndomorphism_prime(domain, power=1)

    File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_prime_finite_field.pyx (starting at line 95)

    A class implementing Frobenius endomorphism on prime finite
    fields (i.e. identity map :-)."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, domain, power=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_prime_finite_field.pyx (starting at line 100)"""
    @overload
    def fixed_field(self) -> Any:
        """FrobeniusEndomorphism_prime.fixed_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_prime_finite_field.pyx (starting at line 135)

        Return the fixed field of ``self``.

        OUTPUT:

        - a tuple `(K, e)`, where `K` is the subfield of the domain
          consisting of elements fixed by ``self`` and `e` is an
          embedding of `K` into the domain.

        .. NOTE::

            Since here the domain is a prime field, the subfield
            is the same prime field and the embedding is necessarily
            the identity map.

        EXAMPLES::

            sage: k.<t> = GF(5)
            sage: f = k.frobenius_endomorphism(2); f
            Identity endomorphism of Finite Field of size 5
            sage: kfixed, embed = f.fixed_field()

            sage: kfixed == k
            True
            sage: [ embed(x) == x for x in kfixed ]
            [True, True, True, True, True]"""
    @overload
    def fixed_field(self) -> Any:
        """FrobeniusEndomorphism_prime.fixed_field(self)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_prime_finite_field.pyx (starting at line 135)

        Return the fixed field of ``self``.

        OUTPUT:

        - a tuple `(K, e)`, where `K` is the subfield of the domain
          consisting of elements fixed by ``self`` and `e` is an
          embedding of `K` into the domain.

        .. NOTE::

            Since here the domain is a prime field, the subfield
            is the same prime field and the embedding is necessarily
            the identity map.

        EXAMPLES::

            sage: k.<t> = GF(5)
            sage: f = k.frobenius_endomorphism(2); f
            Identity endomorphism of Finite Field of size 5
            sage: kfixed, embed = f.fixed_field()

            sage: kfixed == k
            True
            sage: [ embed(x) == x for x in kfixed ]
            [True, True, True, True, True]"""
    def __pow__(self, n, modulus) -> Any:
        """FrobeniusEndomorphism_prime.__pow__(self, n, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/finite_rings/hom_prime_finite_field.pyx (starting at line 127)

        Return the `n`-th iterate of this endomorphism
        (that is the identity since the domain is a prime
        field)."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""

class SectionFiniteFieldHomomorphism_prime(sage.rings.finite_rings.hom_finite_field.SectionFiniteFieldHomomorphism_generic):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
