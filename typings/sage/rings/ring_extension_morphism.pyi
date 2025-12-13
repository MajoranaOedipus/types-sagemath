import sage.categories.map
import sage.rings.morphism
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

__pyx_capi__: dict
op_EQ: int
op_NE: int

class MapFreeModuleToRelativeRing(sage.categories.map.Map):
    """MapFreeModuleToRelativeRing(E, K)

    File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 707)

    Base class of the module isomorphism between a ring extension
    and a free module over one of its bases.

    TESTS::

        sage: K = GF(5^2).over()                                                        # needs sage.rings.finite_rings
        sage: V, i, j = K.free_module()                                                 # needs sage.rings.finite_rings
        sage: type(i)                                                                   # needs sage.rings.finite_rings
        <class 'sage.rings.ring_extension_morphism.MapFreeModuleToRelativeRing'>"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, E, K) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 719)

                Initialize this morphism.

                INPUT:

                - ``E`` -- a ring extension

                - ``K`` -- a commutative ring; one base of ``E``

                TESTS::

                    sage: K = GF(11^6).over(GF(11^3))                                           # needs sage.rings.finite_rings
                    sage: V, i, j = K.free_module()                                             # needs sage.rings.finite_rings
                    sage: i                                                                     # needs sage.rings.finite_rings
                    Generic map:
                      From: Vector space of dimension 2 over Finite Field in z3 of size 11^3
                      To:   Field in z6 with defining polynomial x^2 + (10*z3^2 + z3 + 6)*x + z3 over its base
        """
    @overload
    def is_injective(self) -> Any:
        """MapFreeModuleToRelativeRing.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 745)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: K = GF(11^6).over(GF(11^3))                                           # needs sage.rings.finite_rings
            sage: V, i, j = K.free_module()                                             # needs sage.rings.finite_rings
            sage: i.is_injective()                                                      # needs sage.rings.finite_rings
            True"""
    @overload
    def is_injective(self) -> Any:
        """MapFreeModuleToRelativeRing.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 745)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: K = GF(11^6).over(GF(11^3))                                           # needs sage.rings.finite_rings
            sage: V, i, j = K.free_module()                                             # needs sage.rings.finite_rings
            sage: i.is_injective()                                                      # needs sage.rings.finite_rings
            True"""
    @overload
    def is_surjective(self) -> Any:
        """MapFreeModuleToRelativeRing.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 758)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: K = GF(11^6).over(GF(11^3))                                           # needs sage.rings.finite_rings
            sage: V, i, j = K.free_module()                                             # needs sage.rings.finite_rings
            sage: i.is_surjective()                                                     # needs sage.rings.finite_rings
            True"""
    @overload
    def is_surjective(self) -> Any:
        """MapFreeModuleToRelativeRing.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 758)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: K = GF(11^6).over(GF(11^3))                                           # needs sage.rings.finite_rings
            sage: V, i, j = K.free_module()                                             # needs sage.rings.finite_rings
            sage: i.is_surjective()                                                     # needs sage.rings.finite_rings
            True"""

class MapRelativeRingToFreeModule(sage.categories.map.Map):
    """MapRelativeRingToFreeModule(E, K)

    File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 793)

    Base class of the module isomorphism between a ring extension
    and a free module over one of its bases.

    TESTS::

        sage: K = GF(5^2).over()                                                        # needs sage.rings.finite_rings
        sage: V, i, j = K.free_module()                                                 # needs sage.rings.finite_rings
        sage: type(j)                                                                   # needs sage.rings.finite_rings
        <class 'sage.rings.ring_extension_morphism.MapRelativeRingToFreeModule'>"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, E, K) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 805)

                Initialize this morphism.

                INPUT:

                - ``E`` -- a ring extension

                - ``K`` -- a commutative ring; one base of ``E``

                TESTS::

                    sage: K = GF(11^6).over(GF(11^3))                                           # needs sage.rings.finite_rings
                    sage: V, i, j = K.free_module()                                             # needs sage.rings.finite_rings
                    sage: j                                                                     # needs sage.rings.finite_rings
                    Generic map:
                      From: Field in z6 with defining polynomial x^2 + (10*z3^2 + z3 + 6)*x + z3 over its base
                      To:   Vector space of dimension 2 over Finite Field in z3 of size 11^3
        """
    @overload
    def is_injective(self) -> Any:
        """MapRelativeRingToFreeModule.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 853)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: K = GF(11^6).over(GF(11^3))                                           # needs sage.rings.finite_rings
            sage: V, i, j = K.free_module()                                             # needs sage.rings.finite_rings
            sage: j.is_injective()                                                      # needs sage.rings.finite_rings
            True"""
    @overload
    def is_injective(self) -> Any:
        """MapRelativeRingToFreeModule.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 853)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: K = GF(11^6).over(GF(11^3))                                           # needs sage.rings.finite_rings
            sage: V, i, j = K.free_module()                                             # needs sage.rings.finite_rings
            sage: j.is_injective()                                                      # needs sage.rings.finite_rings
            True"""
    @overload
    def is_surjective(self) -> Any:
        """MapRelativeRingToFreeModule.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 866)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: K = GF(11^6).over(GF(11^3))                                           # needs sage.rings.finite_rings
            sage: V, i, j = K.free_module()                                             # needs sage.rings.finite_rings
            sage: j.is_surjective()                                                     # needs sage.rings.finite_rings
            True"""
    @overload
    def is_surjective(self) -> Any:
        """MapRelativeRingToFreeModule.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 866)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: K = GF(11^6).over(GF(11^3))                                           # needs sage.rings.finite_rings
            sage: V, i, j = K.free_module()                                             # needs sage.rings.finite_rings
            sage: j.is_surjective()                                                     # needs sage.rings.finite_rings
            True"""

class RingExtensionBackendIsomorphism(RingExtensionHomomorphism):
    """RingExtensionBackendIsomorphism(parent)

    File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 530)

    A class for implementating isomorphisms taking an element of the
    backend to its ring extension.

    TESTS::

        sage: # needs sage.rings.finite_rings
        sage: K = GF(11^9).over(GF(11^3))
        sage: f = K.coerce_map_from(GF(11^9)); f
        Coercion morphism:
          From: Finite Field in z9 of size 11^9
          To:   Field in z9 with defining polynomial
                x^3 + (9*z3^2 + 5*z3 + 1)*x^2 + (4*z3 + 3)*x + 10*z3 over its base
        sage: type(f)
        <class 'sage.rings.ring_extension_morphism.RingExtensionBackendIsomorphism'>
        sage: TestSuite(f).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 548)

                Initialize this morphism.

                TESTS::

                    sage: x = polygen(ZZ, 'x')
                    sage: A.<a> = QQ.extension(x^2 - 5)                                         # needs sage.rings.number_field
                    sage: K = A.over()                                                          # needs sage.rings.number_field
                    sage: K.coerce_map_from(A)                                                  # needs sage.rings.number_field
                    Coercion morphism:
                      From: Number Field in a with defining polynomial x^2 - 5
                      To:   Field in a with defining polynomial x^2 - 5 over its base
        """

class RingExtensionBackendReverseIsomorphism(RingExtensionHomomorphism):
    """RingExtensionBackendReverseIsomorphism(parent)

    File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 619)

    A class for implementating isomorphisms from a ring extension to
    its backend.

    TESTS::

        sage: # needs sage.rings.finite_rings
        sage: K = GF(11^9).over(GF(11^3))
        sage: f = GF(11^9).convert_map_from(K); f
        Canonical morphism:
          From: Field in z9 with defining polynomial
                x^3 + (9*z3^2 + 5*z3 + 1)*x^2 + (4*z3 + 3)*x + 10*z3 over its base
          To:   Finite Field in z9 of size 11^9
        sage: type(f)
        <class 'sage.rings.ring_extension_morphism.RingExtensionBackendReverseIsomorphism'>
        sage: TestSuite(f).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 637)

                Initialize this morphism.

                TESTS::

                    sage: x = polygen(ZZ, 'x')
                    sage: A.<a> = QQ.extension(x^2 - 5)                                         # needs sage.rings.number_field
                    sage: K = A.over()                                                          # needs sage.rings.number_field
                    sage: A.convert_map_from(K)                                                 # needs sage.rings.number_field
                    Canonical morphism:
                      From: Field in a with defining polynomial x^2 - 5 over its base
                      To:   Number Field in a with defining polynomial x^2 - 5
        """

class RingExtensionHomomorphism(sage.rings.morphism.RingMap):
    """RingExtensionHomomorphism(parent, defn, base_map=None, check=True)

    File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 80)

    A class for ring homomorphisms between extensions.

    TESTS::

        sage: # needs sage.rings.finite_rings
        sage: K.<a> = GF(5^2).over()
        sage: L.<b> = GF(5^4).over(K)
        sage: phi = L.hom([b^5, a^5]); phi
        Ring endomorphism of Field in b
         with defining polynomial x^2 + (3 - a)*x + a over its base
          Defn: b |--> (2 + a) + 2*b
                with map on base ring:
                a |--> 1 - a
        sage: type(phi)
        <class 'sage.rings.ring_extension_morphism.RingExtensionHomomorphism'>
        sage: TestSuite(phi).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, defn, base_map=..., check=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 99)

                Initialize this morphism.

                INPUT:

                - ``defn`` -- the definition of the morphism (either a map or images of generators)

                - ``base_map`` -- a ring homomorphism or ``None`` (default: ``None``);
                  the action of this morphism on one of the bases of the domain;
                  if ``None``, a coercion map is used

                - ``check`` -- boolean (default: ``True``); whether to check if
                  the given data define a valid homomorphism

                TESTS::

                    sage: S.<x> = QQ[]
                    sage: T.<x,y> = QQ[]
                    sage: f = T.hom([x^2, y^2]); f
                    Ring endomorphism of Multivariate Polynomial Ring in x, y over Rational Field
                      Defn: x |--> x^2
                            y |--> y^2

                    sage: TT = T.over(QQ)
                    sage: End(TT)(f)
                    Ring endomorphism of Multivariate Polynomial Ring in x, y over Rational Field over its base
                      Defn: x |--> x^2
                            y |--> y^2

                    sage: TT = T.over(S)
                    sage: End(TT)(f)
                    Ring endomorphism of Multivariate Polynomial Ring in x, y over Rational Field over its base
                      Defn: y |--> y^2
                            with map on base ring:
                            x |--> x^2
        """
    @overload
    def base_map(self) -> Any:
        """RingExtensionHomomorphism.base_map(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 262)

        Return the base map of this morphism
        or just ``None`` if the base map is a coercion map.

        EXAMPLES::

            sage: F = GF(5)
            sage: K.<a> = GF(5^2).over(F)                                               # needs sage.rings.finite_rings
            sage: L.<b> = GF(5^6).over(K)                                               # needs sage.rings.finite_rings

        We define the absolute Frobenius of L::

            sage: FrobL = L.hom([b^5, a^5]); FrobL                                      # needs sage.rings.finite_rings
            Ring endomorphism of
             Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: b |--> (-1 + a) + (1 + 2*a)*b + a*b^2
                    with map on base ring:
                    a |--> 1 - a
            sage: FrobL.base_map()                                                      # needs sage.rings.finite_rings
            Ring morphism:
              From: Field in a with defining polynomial x^2 + 4*x + 2 over its base
              To:   Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: a |--> 1 - a

        The square of ``FrobL`` acts trivially on K; in other words, it has
        a trivial base map::

            sage: phi = FrobL^2; phi                                                    # needs sage.rings.finite_rings
            Ring endomorphism of
             Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: b |--> 2 + 2*a*b + (2 - a)*b^2
            sage: phi.base_map()                                                        # needs sage.rings.finite_rings"""
    @overload
    def base_map(self) -> Any:
        """RingExtensionHomomorphism.base_map(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 262)

        Return the base map of this morphism
        or just ``None`` if the base map is a coercion map.

        EXAMPLES::

            sage: F = GF(5)
            sage: K.<a> = GF(5^2).over(F)                                               # needs sage.rings.finite_rings
            sage: L.<b> = GF(5^6).over(K)                                               # needs sage.rings.finite_rings

        We define the absolute Frobenius of L::

            sage: FrobL = L.hom([b^5, a^5]); FrobL                                      # needs sage.rings.finite_rings
            Ring endomorphism of
             Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: b |--> (-1 + a) + (1 + 2*a)*b + a*b^2
                    with map on base ring:
                    a |--> 1 - a
            sage: FrobL.base_map()                                                      # needs sage.rings.finite_rings
            Ring morphism:
              From: Field in a with defining polynomial x^2 + 4*x + 2 over its base
              To:   Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: a |--> 1 - a

        The square of ``FrobL`` acts trivially on K; in other words, it has
        a trivial base map::

            sage: phi = FrobL^2; phi                                                    # needs sage.rings.finite_rings
            Ring endomorphism of
             Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: b |--> 2 + 2*a*b + (2 - a)*b^2
            sage: phi.base_map()                                                        # needs sage.rings.finite_rings"""
    @overload
    def base_map(self) -> Any:
        """RingExtensionHomomorphism.base_map(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 262)

        Return the base map of this morphism
        or just ``None`` if the base map is a coercion map.

        EXAMPLES::

            sage: F = GF(5)
            sage: K.<a> = GF(5^2).over(F)                                               # needs sage.rings.finite_rings
            sage: L.<b> = GF(5^6).over(K)                                               # needs sage.rings.finite_rings

        We define the absolute Frobenius of L::

            sage: FrobL = L.hom([b^5, a^5]); FrobL                                      # needs sage.rings.finite_rings
            Ring endomorphism of
             Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: b |--> (-1 + a) + (1 + 2*a)*b + a*b^2
                    with map on base ring:
                    a |--> 1 - a
            sage: FrobL.base_map()                                                      # needs sage.rings.finite_rings
            Ring morphism:
              From: Field in a with defining polynomial x^2 + 4*x + 2 over its base
              To:   Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: a |--> 1 - a

        The square of ``FrobL`` acts trivially on K; in other words, it has
        a trivial base map::

            sage: phi = FrobL^2; phi                                                    # needs sage.rings.finite_rings
            Ring endomorphism of
             Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: b |--> 2 + 2*a*b + (2 - a)*b^2
            sage: phi.base_map()                                                        # needs sage.rings.finite_rings"""
    @overload
    def is_identity(self) -> Any:
        """RingExtensionHomomorphism.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 350)

        Return whether this morphism is the identity.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()   # over GF(5)
            sage: FrobK = K.hom([a^5])
            sage: FrobK.is_identity()
            False
            sage: (FrobK^2).is_identity()
            True

        Coercion maps are not considered as identity morphisms::

            sage: # needs sage.rings.finite_rings
            sage: L.<b> = GF(5^6).over(K)
            sage: iota = L.defining_morphism(); iota
            Ring morphism:
              From: Field in a with defining polynomial x^2 + 4*x + 2 over its base
              To:   Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: a |--> a
            sage: iota.is_identity()
            False"""
    @overload
    def is_identity(self) -> Any:
        """RingExtensionHomomorphism.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 350)

        Return whether this morphism is the identity.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()   # over GF(5)
            sage: FrobK = K.hom([a^5])
            sage: FrobK.is_identity()
            False
            sage: (FrobK^2).is_identity()
            True

        Coercion maps are not considered as identity morphisms::

            sage: # needs sage.rings.finite_rings
            sage: L.<b> = GF(5^6).over(K)
            sage: iota = L.defining_morphism(); iota
            Ring morphism:
              From: Field in a with defining polynomial x^2 + 4*x + 2 over its base
              To:   Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: a |--> a
            sage: iota.is_identity()
            False"""
    @overload
    def is_identity(self) -> Any:
        """RingExtensionHomomorphism.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 350)

        Return whether this morphism is the identity.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()   # over GF(5)
            sage: FrobK = K.hom([a^5])
            sage: FrobK.is_identity()
            False
            sage: (FrobK^2).is_identity()
            True

        Coercion maps are not considered as identity morphisms::

            sage: # needs sage.rings.finite_rings
            sage: L.<b> = GF(5^6).over(K)
            sage: iota = L.defining_morphism(); iota
            Ring morphism:
              From: Field in a with defining polynomial x^2 + 4*x + 2 over its base
              To:   Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: a |--> a
            sage: iota.is_identity()
            False"""
    @overload
    def is_identity(self) -> Any:
        """RingExtensionHomomorphism.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 350)

        Return whether this morphism is the identity.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()   # over GF(5)
            sage: FrobK = K.hom([a^5])
            sage: FrobK.is_identity()
            False
            sage: (FrobK^2).is_identity()
            True

        Coercion maps are not considered as identity morphisms::

            sage: # needs sage.rings.finite_rings
            sage: L.<b> = GF(5^6).over(K)
            sage: iota = L.defining_morphism(); iota
            Ring morphism:
              From: Field in a with defining polynomial x^2 + 4*x + 2 over its base
              To:   Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: a |--> a
            sage: iota.is_identity()
            False"""
    @overload
    def is_injective(self) -> Any:
        """RingExtensionHomomorphism.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 380)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^10).over(GF(5^5))
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Finite Field in z5 of size 5^5
              To:   Field in z10 with defining polynomial
                    x^2 + (2*z5^3 + 2*z5^2 + 4*z5 + 4)*x + z5 over its base
              Defn: z5 |--> z5
            sage: iota.is_injective()
            True

            sage: K = GF(7).over(ZZ)
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Integer Ring
              To:   Finite Field of size 7 over its base
              Defn: 1 |--> 1
            sage: iota.is_injective()
            False"""
    @overload
    def is_injective(self) -> Any:
        """RingExtensionHomomorphism.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 380)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^10).over(GF(5^5))
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Finite Field in z5 of size 5^5
              To:   Field in z10 with defining polynomial
                    x^2 + (2*z5^3 + 2*z5^2 + 4*z5 + 4)*x + z5 over its base
              Defn: z5 |--> z5
            sage: iota.is_injective()
            True

            sage: K = GF(7).over(ZZ)
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Integer Ring
              To:   Finite Field of size 7 over its base
              Defn: 1 |--> 1
            sage: iota.is_injective()
            False"""
    @overload
    def is_injective(self) -> Any:
        """RingExtensionHomomorphism.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 380)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^10).over(GF(5^5))
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Finite Field in z5 of size 5^5
              To:   Field in z10 with defining polynomial
                    x^2 + (2*z5^3 + 2*z5^2 + 4*z5 + 4)*x + z5 over its base
              Defn: z5 |--> z5
            sage: iota.is_injective()
            True

            sage: K = GF(7).over(ZZ)
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Integer Ring
              To:   Finite Field of size 7 over its base
              Defn: 1 |--> 1
            sage: iota.is_injective()
            False"""
    @overload
    def is_surjective(self) -> Any:
        """RingExtensionHomomorphism.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 408)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^10).over(GF(5^5))
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Finite Field in z5 of size 5^5
              To:   Field in z10 with defining polynomial
                    x^2 + (2*z5^3 + 2*z5^2 + 4*z5 + 4)*x + z5 over its base
              Defn: z5 |--> z5
            sage: iota.is_surjective()
            False

            sage: K = GF(7).over(ZZ)
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Integer Ring
              To:   Finite Field of size 7 over its base
              Defn: 1 |--> 1
            sage: iota.is_surjective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """RingExtensionHomomorphism.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 408)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^10).over(GF(5^5))
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Finite Field in z5 of size 5^5
              To:   Field in z10 with defining polynomial
                    x^2 + (2*z5^3 + 2*z5^2 + 4*z5 + 4)*x + z5 over its base
              Defn: z5 |--> z5
            sage: iota.is_surjective()
            False

            sage: K = GF(7).over(ZZ)
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Integer Ring
              To:   Finite Field of size 7 over its base
              Defn: 1 |--> 1
            sage: iota.is_surjective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """RingExtensionHomomorphism.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension_morphism.pyx (starting at line 408)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^10).over(GF(5^5))
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Finite Field in z5 of size 5^5
              To:   Field in z10 with defining polynomial
                    x^2 + (2*z5^3 + 2*z5^2 + 4*z5 + 4)*x + z5 over its base
              Defn: z5 |--> z5
            sage: iota.is_surjective()
            False

            sage: K = GF(7).over(ZZ)
            sage: iota = K.defining_morphism(); iota
            Ring morphism:
              From: Integer Ring
              To:   Finite Field of size 7 over its base
              Defn: 1 |--> 1
            sage: iota.is_surjective()
            True"""
