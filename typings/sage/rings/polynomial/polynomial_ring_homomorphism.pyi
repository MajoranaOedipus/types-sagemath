import sage.rings.morphism
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class PolynomialRingHomomorphism_from_base(sage.rings.morphism.RingHomomorphism_from_base):
    """File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_ring_homomorphism.pyx (starting at line 21)

        The canonical ring homomorphism from `R[x]` to `S[x]` induced by a
        ring homomorphism from `R` to `S`.

        EXAMPLES::

            sage: QQ['x'].coerce_map_from(ZZ['x'])
            Ring morphism:
              From: Univariate Polynomial Ring in x over Integer Ring
              To:   Univariate Polynomial Ring in x over Rational Field
              Defn: Induced from base ring by
                    Natural morphism:
                      From: Integer Ring
                      To:   Rational Field
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def is_injective(self) -> Any:
        """PolynomialRingHomomorphism_from_base.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_ring_homomorphism.pyx (starting at line 96)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: S.<x> = QQ[]
            sage: R.hom(S).is_injective()
            True"""
    @overload
    def is_injective(self) -> Any:
        """PolynomialRingHomomorphism_from_base.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_ring_homomorphism.pyx (starting at line 96)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: S.<x> = QQ[]
            sage: R.hom(S).is_injective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """PolynomialRingHomomorphism_from_base.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_ring_homomorphism.pyx (starting at line 109)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: S.<x> = Zmod(2)[]
            sage: R.hom(S).is_surjective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """PolynomialRingHomomorphism_from_base.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/polynomial/polynomial_ring_homomorphism.pyx (starting at line 109)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: R.<x> = ZZ[]
            sage: S.<x> = Zmod(2)[]
            sage: R.hom(S).is_surjective()
            True"""
