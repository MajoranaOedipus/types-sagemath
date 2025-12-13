import sage.rings.morphism
from sage.categories.homset import Hom as Hom
from sage.rings.infinity import Infinity as Infinity
from sage.rings.padics.padic_generic import pAdicGeneric as pAdicGeneric
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

class FrobeniusEndomorphism_padics(sage.rings.morphism.RingHomomorphism):
    """FrobeniusEndomorphism_padics(domain, n=1)

    File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 27)

    A class implementing Frobenius endomorphisms on `p`-adic fields."""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, domain, n=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 31)

                INPUT:

                - ``domain`` -- an unramified `p`-adic field

                - ``n`` -- integer (default: 1)

                .. NOTE::

                    `n` may be negative.

                OUTPUT:

                The `n`-th power of the absolute (arithmetic) Frobenius
                endomorphism on ``domain``

                TESTS::

                    sage: from sage.rings.padics.morphism import FrobeniusEndomorphism_padics
                    sage: K.<a> = Qq(5^3)
                    sage: FrobeniusEndomorphism_padics(K)
                    Frobenius endomorphism on 5-adic Unramified Extension ... lifting a |--> a^5 on the residue field
                    sage: FrobeniusEndomorphism_padics(K,2)
                    Frobenius endomorphism on 5-adic Unramified Extension ... lifting a |--> a^(5^2) on the residue field

                    sage: FrobeniusEndomorphism_padics(K,a)
                    Traceback (most recent call last):
                    ...
                    TypeError: n (=a + O(5^20)) is not an integer

                    sage: K = Qp(5)
                    sage: x = polygen(ZZ, 'x')
                    sage: L.<pi> = K.extension(x^2 - 5)
                    sage: FrobeniusEndomorphism_padics(L)
                    Traceback (most recent call last):
                    ...
                    TypeError: The domain must be unramified

                    sage: FrobeniusEndomorphism_padics(QQ)
                    Traceback (most recent call last):
                    ...
                    TypeError: The domain must be an instance of pAdicGeneric
        """
    @overload
    def is_identity(self) -> bool:
        """FrobeniusEndomorphism_padics.is_identity(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 294)

        Return ``True`` if this morphism is the identity morphism.

        EXAMPLES::

            sage: K.<a> = Qq(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.is_identity()
            False
            sage: (Frob^3).is_identity()
            True"""
    @overload
    def is_identity(self) -> Any:
        """FrobeniusEndomorphism_padics.is_identity(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 294)

        Return ``True`` if this morphism is the identity morphism.

        EXAMPLES::

            sage: K.<a> = Qq(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.is_identity()
            False
            sage: (Frob^3).is_identity()
            True"""
    @overload
    def is_identity(self) -> Any:
        """FrobeniusEndomorphism_padics.is_identity(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 294)

        Return ``True`` if this morphism is the identity morphism.

        EXAMPLES::

            sage: K.<a> = Qq(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.is_identity()
            False
            sage: (Frob^3).is_identity()
            True"""
    @overload
    def is_injective(self) -> bool:
        """FrobeniusEndomorphism_padics.is_injective(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 266)

        Return ``True`` since any power of the Frobenius endomorphism
        over an unramified `p`-adic field is always injective.

        EXAMPLES::

            sage: K.<a> = Qq(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.is_injective()
            True"""
    @overload
    def is_injective(self) -> Any:
        """FrobeniusEndomorphism_padics.is_injective(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 266)

        Return ``True`` since any power of the Frobenius endomorphism
        over an unramified `p`-adic field is always injective.

        EXAMPLES::

            sage: K.<a> = Qq(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.is_injective()
            True"""
    @overload
    def is_surjective(self) -> bool:
        """FrobeniusEndomorphism_padics.is_surjective(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 280)

        Return ``True`` since any power of the Frobenius endomorphism
        over an unramified `p`-adic field is always surjective.

        EXAMPLES::

            sage: K.<a> = Qq(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.is_surjective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """FrobeniusEndomorphism_padics.is_surjective(self) -> bool

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 280)

        Return ``True`` since any power of the Frobenius endomorphism
        over an unramified `p`-adic field is always surjective.

        EXAMPLES::

            sage: K.<a> = Qq(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.is_surjective()
            True"""
    @overload
    def order(self) -> Any:
        """FrobeniusEndomorphism_padics.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 183)

        Return the order of this endomorphism.

        EXAMPLES::

            sage: K.<a> = Qq(5^12)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.order()
            12
            sage: (Frob^2).order()
            6
            sage: (Frob^9).order()
            4"""
    @overload
    def order(self) -> Any:
        """FrobeniusEndomorphism_padics.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 183)

        Return the order of this endomorphism.

        EXAMPLES::

            sage: K.<a> = Qq(5^12)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.order()
            12
            sage: (Frob^2).order()
            6
            sage: (Frob^9).order()
            4"""
    @overload
    def order(self) -> Any:
        """FrobeniusEndomorphism_padics.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 183)

        Return the order of this endomorphism.

        EXAMPLES::

            sage: K.<a> = Qq(5^12)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.order()
            12
            sage: (Frob^2).order()
            6
            sage: (Frob^9).order()
            4"""
    @overload
    def order(self) -> Any:
        """FrobeniusEndomorphism_padics.order(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 183)

        Return the order of this endomorphism.

        EXAMPLES::

            sage: K.<a> = Qq(5^12)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.order()
            12
            sage: (Frob^2).order()
            6
            sage: (Frob^9).order()
            4"""
    @overload
    def power(self) -> Any:
        """FrobeniusEndomorphism_padics.power(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 203)

        Return the smallest integer `n` such that this endomorphism
        is the `n`-th power of the absolute (arithmetic) Frobenius.

        EXAMPLES::

            sage: K.<a> = Qq(5^12)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.power()
            1
            sage: (Frob^9).power()
            9
            sage: (Frob^13).power()
            1"""
    @overload
    def power(self) -> Any:
        """FrobeniusEndomorphism_padics.power(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 203)

        Return the smallest integer `n` such that this endomorphism
        is the `n`-th power of the absolute (arithmetic) Frobenius.

        EXAMPLES::

            sage: K.<a> = Qq(5^12)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.power()
            1
            sage: (Frob^9).power()
            9
            sage: (Frob^13).power()
            1"""
    @overload
    def power(self) -> Any:
        """FrobeniusEndomorphism_padics.power(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 203)

        Return the smallest integer `n` such that this endomorphism
        is the `n`-th power of the absolute (arithmetic) Frobenius.

        EXAMPLES::

            sage: K.<a> = Qq(5^12)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.power()
            1
            sage: (Frob^9).power()
            9
            sage: (Frob^13).power()
            1"""
    @overload
    def power(self) -> Any:
        """FrobeniusEndomorphism_padics.power(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 203)

        Return the smallest integer `n` such that this endomorphism
        is the `n`-th power of the absolute (arithmetic) Frobenius.

        EXAMPLES::

            sage: K.<a> = Qq(5^12)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob.power()
            1
            sage: (Frob^9).power()
            9
            sage: (Frob^13).power()
            1"""
    def __hash__(self) -> Any:
        """FrobeniusEndomorphism_padics.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 309)

        Return a hash of this morphism.

        It is the hash of ``(domain, codomain, ('Frob', power)``
        where ``power`` is the smallest integer `n` such that
        this morphism acts by `x \\mapsto x^(p^n)` on the residue field.

        EXAMPLES::

            sage: K.<a> = Qq(5^3)
            sage: Frob = K.frobenius_endomorphism()
            sage: hash(Frob)  # indirect doctest, random
            2818440606874670810"""
    def __pow__(self, n, modulus) -> Any:
        """FrobeniusEndomorphism_padics.__pow__(self, n, modulus)

        File: /build/sagemath/src/sage/src/sage/rings/padics/morphism.pyx (starting at line 221)

        Return the `n`-th iterate of this endomorphism.

        EXAMPLES::

            sage: K.<a> = Qq(5^12)
            sage: Frob = K.frobenius_endomorphism()
            sage: Frob^2
            Frobenius endomorphism on 5-adic Unramified Extension ... lifting a |--> a^(5^2) on the residue field

        The result is simplified if possible::

            sage: Frob^15
            Frobenius endomorphism on 5-adic Unramified Extension ... lifting a |--> a^(5^3) on the residue field
            sage: Frob^36
            Identity endomorphism of 5-adic Unramified Extension ..."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
