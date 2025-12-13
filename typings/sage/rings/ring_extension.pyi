import _cython_3_2_1
import sage.rings.ring_extension_element
import sage.structure.factory
import sage.structure.parent
from sage.categories.category import ZZ as ZZ
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.fields import Fields as Fields
from sage.cpython.getattr import dir_with_other_class as dir_with_other_class
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.latex import latex as latex, latex_variable_name as latex_variable_name
from sage.rings.infinity import Infinity as Infinity
from sage.structure.category_object import normalize_names as normalize_names
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.factory import UniqueFactory as UniqueFactory
from typing import Any, ClassVar, overload

RingExtension: RingExtensionFactory
common_base: _cython_3_2_1.cython_function_or_method
generators: _cython_3_2_1.cython_function_or_method
tower_bases: _cython_3_2_1.cython_function_or_method
variable_names: _cython_3_2_1.cython_function_or_method

class RingExtensionFactory(sage.structure.factory.UniqueFactory):
    """File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 329)

        Factory for ring extensions.

        TESTS::

            sage: E = QQ.over(ZZ)
            sage: QQ.over(ZZ) is E
            True

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = QQ.extension(x^2 - 2)                                             # needs sage.rings.number_field
            sage: E = K.over(QQ); E                                                         # needs sage.rings.number_field
            Field in a with defining polynomial x^2 - 2 over its base

            sage: E2.<b> = K.over(QQ)                                                       # needs sage.rings.number_field
            sage: E2 is E                                                                   # needs sage.rings.number_field
            False
    """
    @overload
    def create_key_and_extra_args(self, ring, defining_morphism=..., gens=..., names=..., constructors=...) -> Any:
        """RingExtensionFactory.create_key_and_extra_args(self, ring, defining_morphism=None, gens=None, names=None, constructors=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 348)

        Create a key and return it together with a list of constructors
        of the object.

        INPUT:

        - ``ring`` -- a commutative ring

        - ``defining_morphism`` -- a ring homomorphism or a commutative
          ring or ``None`` (default: ``None``); the defining morphism of
          this extension or its base (if it coerces to ``ring``)

        - ``gens`` -- list of generators of this extension (over its base)
          or ``None`` (default: ``None``)

        - ``names`` -- list or a tuple of variable names or ``None``
          (default: ``None``)

        - ``constructors`` -- list of constructors; each constructor
          is a pair `(class, arguments)` where `class` is the class
          implementing the extension and `arguments` is the dictionary
          of arguments to pass in to init function

        TESTS::

            sage: from sage.rings.ring_extension import RingExtension
            sage: RingExtension.create_key_and_extra_args(QQ, ZZ)
            ((Ring morphism:
                From: Integer Ring
                To:   Rational Field
                Defn: 1 |--> 1, (), ()),
             {'constructors': [(<class 'sage.rings.ring_extension.RingExtension_generic'>,
                               {'is_backend_exposed': True,
                                'print_options': {'print_elements_as': None,
                                                  'print_parent_as': None}})]})

            sage: RingExtension.create_key_and_extra_args(GF(5^4), GF(5^2),             # needs sage.rings.finite_rings
            ....:                                         names=('a',))
            ((Ring morphism:
                From: Finite Field in z2 of size 5^2
                To:   Finite Field in z4 of size 5^4
                Defn: z2 |--> z4^3 + z4^2 + z4 + 3, (z4,), ('a',)),
             {'constructors': [(<class 'sage.rings.ring_extension.RingExtensionWithGen'>,
                               {'gen': z4, 'is_backend_exposed': True, 'names': ('a',)})]})"""
    @overload
    def create_key_and_extra_args(self, QQ, ZZ) -> Any:
        """RingExtensionFactory.create_key_and_extra_args(self, ring, defining_morphism=None, gens=None, names=None, constructors=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 348)

        Create a key and return it together with a list of constructors
        of the object.

        INPUT:

        - ``ring`` -- a commutative ring

        - ``defining_morphism`` -- a ring homomorphism or a commutative
          ring or ``None`` (default: ``None``); the defining morphism of
          this extension or its base (if it coerces to ``ring``)

        - ``gens`` -- list of generators of this extension (over its base)
          or ``None`` (default: ``None``)

        - ``names`` -- list or a tuple of variable names or ``None``
          (default: ``None``)

        - ``constructors`` -- list of constructors; each constructor
          is a pair `(class, arguments)` where `class` is the class
          implementing the extension and `arguments` is the dictionary
          of arguments to pass in to init function

        TESTS::

            sage: from sage.rings.ring_extension import RingExtension
            sage: RingExtension.create_key_and_extra_args(QQ, ZZ)
            ((Ring morphism:
                From: Integer Ring
                To:   Rational Field
                Defn: 1 |--> 1, (), ()),
             {'constructors': [(<class 'sage.rings.ring_extension.RingExtension_generic'>,
                               {'is_backend_exposed': True,
                                'print_options': {'print_elements_as': None,
                                                  'print_parent_as': None}})]})

            sage: RingExtension.create_key_and_extra_args(GF(5^4), GF(5^2),             # needs sage.rings.finite_rings
            ....:                                         names=('a',))
            ((Ring morphism:
                From: Finite Field in z2 of size 5^2
                To:   Finite Field in z4 of size 5^4
                Defn: z2 |--> z4^3 + z4^2 + z4 + 3, (z4,), ('a',)),
             {'constructors': [(<class 'sage.rings.ring_extension.RingExtensionWithGen'>,
                               {'gen': z4, 'is_backend_exposed': True, 'names': ('a',)})]})"""
    def create_object(self, version, key, **extra_args) -> Any:
        """RingExtensionFactory.create_object(self, version, key, **extra_args)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 471)

        Return the object associated to a given key.

        TESTS::

            sage: from sage.rings.ring_extension import RingExtension
            sage: key, extra_args = RingExtension.create_key_and_extra_args(QQ, ZZ)
            sage: RingExtension.create_object((8,9,0), key, **extra_args)
            Rational Field over its base"""

class RingExtensionFractionField(RingExtension_generic):
    """RingExtensionFractionField(defining_morphism, ring=None, **kwargs)

    File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1974)

    A class for ring extensions of the form `   extrm{Frac}(A)/A`.

    TESTS::

        sage: Z = ZZ.over()   # over ZZ itself
        sage: Q = Z.fraction_field()
        sage: Q
        Fraction Field of Integer Ring over its base

        sage: type(Q)
        <class 'sage.rings.ring_extension.RingExtensionFractionField'>

        sage: TestSuite(Q).run()"""
    Element: ClassVar[type[sage.rings.ring_extension_element.RingExtensionFractionFieldElement]] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, defining_morphism, ring=..., **kwargs) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1992)

                Initialize this ring extension.

                INPUT:

                - ``defining_morphism`` -- a ring homomorphism

                - ``ring`` -- the commutative ring whose fraction field is this
                  extension

                TESTS::

                    sage: # needs sage.rings.number_field
                    sage: x = polygen(ZZ, 'x')
                    sage: A.<a> = ZZ.extension(x^2 - 2)
                    sage: OK = A.over()
                    sage: K = OK.fraction_field(); K
                    Fraction Field of
                     Maximal Order generated by a in Number Field in a
                     with defining polynomial x^2 - 2 over its base
                    sage: TestSuite(K).run()
        """
    @overload
    def ring(self) -> Any:
        """RingExtensionFractionField.ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2021)

        Return the ring whose fraction field is this extension.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: A.<a> = ZZ.extension(x^2 - 2)
            sage: OK = A.over()
            sage: K = OK.fraction_field(); K
            Fraction Field of
             Maximal Order generated by a in Number Field in a with defining polynomial x^2 - 2 over its base
            sage: K.ring()
            Maximal Order generated by a in Number Field in a with defining polynomial x^2 - 2 over its base
            sage: K.ring() is OK
            True"""
    @overload
    def ring(self) -> Any:
        """RingExtensionFractionField.ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2021)

        Return the ring whose fraction field is this extension.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: A.<a> = ZZ.extension(x^2 - 2)
            sage: OK = A.over()
            sage: K = OK.fraction_field(); K
            Fraction Field of
             Maximal Order generated by a in Number Field in a with defining polynomial x^2 - 2 over its base
            sage: K.ring()
            Maximal Order generated by a in Number Field in a with defining polynomial x^2 - 2 over its base
            sage: K.ring() is OK
            True"""
    @overload
    def ring(self) -> Any:
        """RingExtensionFractionField.ring(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2021)

        Return the ring whose fraction field is this extension.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: A.<a> = ZZ.extension(x^2 - 2)
            sage: OK = A.over()
            sage: K = OK.fraction_field(); K
            Fraction Field of
             Maximal Order generated by a in Number Field in a with defining polynomial x^2 - 2 over its base
            sage: K.ring()
            Maximal Order generated by a in Number Field in a with defining polynomial x^2 - 2 over its base
            sage: K.ring() is OK
            True"""

class RingExtensionWithBasis(RingExtension_generic):
    """RingExtensionWithBasis(defining_morphism, basis, names=None, check=True, **kwargs)

    File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2085)

    A class for finite free ring extensions equipped
    with a basis.

    TESTS::

        sage: E = GF(5^4).over(GF(5^2)); E                                              # needs sage.rings.finite_rings
        Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base

        sage: TestSuite(E).run()                                                        # needs sage.rings.finite_rings"""
    Element: ClassVar[type[sage.rings.ring_extension_element.RingExtensionWithBasisElement]] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, defining_morphism, basis, names=..., check=..., **kwargs) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2099)

                Initialize this ring extension.

                INPUT:

                - ``defining_morphism`` -- a ring homomorphism

                - ``basis`` -- tuple of elements in this extension

                - ``names`` -- tuple of strings or ``None`` (default: ``None``);
                  the way the elements of the basis are printed

                - ``check`` -- boolean (default: ``True``); whether to check if
                  ``basis`` is indeed a basis

                TESTS::

                    sage: x = polygen(ZZ, 'x')
                    sage: K.<a> = QQ.extension(x^3 - 2)                                         # needs sage.rings.number_field
                    sage: E = K.over(); E                                                       # needs sage.rings.number_field
                    Field in a with defining polynomial x^3 - 2 over its base

                    sage: TestSuite(E).run()                                                    # needs sage.rings.number_field
        """
    @overload
    def basis_over(self, base=...) -> Any:
        """RingExtensionWithBasis.basis_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2261)

        Return a basis of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2).over()  # over GF(5)
            sage: K.<b> = GF(5^4).over(F)
            sage: L.<c> = GF(5^12).over(K)
            sage: L.basis_over(K)
            [1, c, c^2]
            sage: L.basis_over(F)
            [1, b, c, b*c, c^2, b*c^2]
            sage: L.basis_over(GF(5))
            [1, a, b, a*b, c, a*c, b*c, a*b*c, c^2, a*c^2, b*c^2, a*b*c^2]

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: L.basis_over()                                                        # needs sage.rings.finite_rings
            [1, c, c^2]

            sage: K.basis_over()                                                        # needs sage.rings.finite_rings
            [1, b]

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: L.degree_over(GF(5^6))                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z6 of size 5^6"""
    @overload
    def basis_over(self, K) -> Any:
        """RingExtensionWithBasis.basis_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2261)

        Return a basis of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2).over()  # over GF(5)
            sage: K.<b> = GF(5^4).over(F)
            sage: L.<c> = GF(5^12).over(K)
            sage: L.basis_over(K)
            [1, c, c^2]
            sage: L.basis_over(F)
            [1, b, c, b*c, c^2, b*c^2]
            sage: L.basis_over(GF(5))
            [1, a, b, a*b, c, a*c, b*c, a*b*c, c^2, a*c^2, b*c^2, a*b*c^2]

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: L.basis_over()                                                        # needs sage.rings.finite_rings
            [1, c, c^2]

            sage: K.basis_over()                                                        # needs sage.rings.finite_rings
            [1, b]

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: L.degree_over(GF(5^6))                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z6 of size 5^6"""
    @overload
    def basis_over(self, F) -> Any:
        """RingExtensionWithBasis.basis_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2261)

        Return a basis of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2).over()  # over GF(5)
            sage: K.<b> = GF(5^4).over(F)
            sage: L.<c> = GF(5^12).over(K)
            sage: L.basis_over(K)
            [1, c, c^2]
            sage: L.basis_over(F)
            [1, b, c, b*c, c^2, b*c^2]
            sage: L.basis_over(GF(5))
            [1, a, b, a*b, c, a*c, b*c, a*b*c, c^2, a*c^2, b*c^2, a*b*c^2]

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: L.basis_over()                                                        # needs sage.rings.finite_rings
            [1, c, c^2]

            sage: K.basis_over()                                                        # needs sage.rings.finite_rings
            [1, b]

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: L.degree_over(GF(5^6))                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z6 of size 5^6"""
    @overload
    def basis_over(self) -> Any:
        """RingExtensionWithBasis.basis_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2261)

        Return a basis of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2).over()  # over GF(5)
            sage: K.<b> = GF(5^4).over(F)
            sage: L.<c> = GF(5^12).over(K)
            sage: L.basis_over(K)
            [1, c, c^2]
            sage: L.basis_over(F)
            [1, b, c, b*c, c^2, b*c^2]
            sage: L.basis_over(GF(5))
            [1, a, b, a*b, c, a*c, b*c, a*b*c, c^2, a*c^2, b*c^2, a*b*c^2]

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: L.basis_over()                                                        # needs sage.rings.finite_rings
            [1, c, c^2]

            sage: K.basis_over()                                                        # needs sage.rings.finite_rings
            [1, b]

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: L.degree_over(GF(5^6))                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z6 of size 5^6"""
    @overload
    def basis_over(self) -> Any:
        """RingExtensionWithBasis.basis_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2261)

        Return a basis of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F.<a> = GF(5^2).over()  # over GF(5)
            sage: K.<b> = GF(5^4).over(F)
            sage: L.<c> = GF(5^12).over(K)
            sage: L.basis_over(K)
            [1, c, c^2]
            sage: L.basis_over(F)
            [1, b, c, b*c, c^2, b*c^2]
            sage: L.basis_over(GF(5))
            [1, a, b, a*b, c, a*c, b*c, a*b*c, c^2, a*c^2, b*c^2, a*b*c^2]

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: L.basis_over()                                                        # needs sage.rings.finite_rings
            [1, c, c^2]

            sage: K.basis_over()                                                        # needs sage.rings.finite_rings
            [1, b]

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: L.degree_over(GF(5^6))                                                # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z6 of size 5^6"""
    def fraction_field(self, extend_base=...) -> Any:
        """RingExtensionWithBasis.fraction_field(self, extend_base=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2454)

        Return the fraction field of this extension.

        INPUT:

        - ``extend_base`` -- boolean (default: ``False``)

        If ``extend_base`` is ``False``, the fraction field of the
        extension `L/K` is defined as `\\textrm{Frac}(L)/L/K`, except
        is `L` is already a field in which base the fraction field
        of `L/K` is `L/K` itself.

        If ``extend_base`` is ``True``, the fraction field of the
        extension `L/K` is defined as `\\textrm{Frac}(L)/\\textrm{Frac}(K)`
        (provided that the defining morphism extends to the fraction
        fields, i.e. is injective).

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: A.<a> = ZZ.extension(x^2 - 5)
            sage: OK = A.over()   # over ZZ
            sage: OK
            Order of conductor 2 generated by a in Number Field in a with defining polynomial x^2 - 5 over its base
            sage: K1 = OK.fraction_field(); K1
            Fraction Field of Order of conductor 2 generated by a in Number Field in a
             with defining polynomial x^2 - 5 over its base
            sage: K1.bases()
            [Fraction Field of Order of conductor 2 generated by a in Number Field in a
              with defining polynomial x^2 - 5 over its base,
             Order of conductor 2 generated by a in Number Field in a
              with defining polynomial x^2 - 5 over its base,
             Integer Ring]
            sage: K2 = OK.fraction_field(extend_base=True); K2
            Fraction Field of Order of conductor 2 generated by a
              in Number Field in a with defining polynomial x^2 - 5 over its base
            sage: K2.bases()
            [Fraction Field of Order of conductor 2 generated by a
              in Number Field in a with defining polynomial x^2 - 5 over its base,
             Rational Field]

        Note that there is no coercion map between `K_1` and `K_2`::

            sage: K1.has_coerce_map_from(K2)                                            # needs sage.rings.number_field
            False
            sage: K2.has_coerce_map_from(K1)                                            # needs sage.rings.number_field
            False

        We check that when the extension is a field, its fraction field does not change::

            sage: K1.fraction_field() is K1                                             # needs sage.rings.number_field
            True
            sage: K2.fraction_field() is K2                                             # needs sage.rings.number_field
            True

        TESTS::

            sage: A = GF(5).over(ZZ)
            sage: A.fraction_field(extend_base=True)
            Traceback (most recent call last):
            ...
            ValueError: the morphism is not injective"""
    @overload
    def free_module(self, base=..., map=...) -> Any:
        """RingExtensionWithBasis.free_module(self, base=None, map=True)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2327)

        Return a free module V over ``base`` which is isomorphic to
        this ring

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        - ``map`` -- boolean (default: ``True``); whether to return
          isomorphisms between this ring and V

        OUTPUT:

        - A finite-rank free module V over ``base``

        - The isomorphism from V to this ring corresponding to the
          basis output by the method :meth:`basis_over`
          (only included if ``map`` is ``True``)

        - The reverse isomorphism of the isomorphism above
          (only included if ``map`` is ``True``)

        EXAMPLES::

            sage: F = GF(11)
            sage: K.<a> = GF(11^2).over()                                               # needs sage.rings.finite_rings
            sage: L.<b> = GF(11^6).over(K)                                              # needs sage.rings.finite_rings

        Forgetting a part of the multiplicative structure, the field L
        can be viewed as a vector space of dimension 3 over K, equipped
        with a distinguished basis, namely `(1, b, b^2)`::

            sage: # needs sage.rings.finite_rings
            sage: V, i, j = L.free_module(K)
            sage: V
            Vector space of dimension 3 over
             Field in a with defining polynomial x^2 + 7*x + 2 over its base
            sage: i
            Generic map:
              From: Vector space of dimension 3 over
                    Field in a with defining polynomial x^2 + 7*x + 2 over its base
              To:   Field in b with defining polynomial
                    x^3 + (7 + 2*a)*x^2 + (2 - a)*x - a over its base
            sage: j
            Generic map:
              From: Field in b with defining polynomial
                    x^3 + (7 + 2*a)*x^2 + (2 - a)*x - a over its base
              To:   Vector space of dimension 3 over
                    Field in a with defining polynomial x^2 + 7*x + 2 over its base
            sage: j(b)
            (0, 1, 0)
            sage: i((1, a, a+1))
            1 + a*b + (1 + a)*b^2

        Similarly, one can view L as a F-vector space of dimension 6::

            sage: V, i, j, = L.free_module(F)                                           # needs sage.rings.finite_rings
            sage: V                                                                     # needs sage.rings.finite_rings
            Vector space of dimension 6 over Finite Field of size 11

        In this case, the isomorphisms between `V` and `L` are given by the
        basis `(1, a, b, ab, b^2, ab^2)`:

            sage: j(a*b)                                                                # needs sage.rings.finite_rings
            (0, 0, 0, 1, 0, 0)
            sage: i((1,2,3,4,5,6))                                                      # needs sage.rings.finite_rings
            (1 + 2*a) + (3 + 4*a)*b + (5 + 6*a)*b^2

        When ``base`` is omitted, the default is the base of this extension::

            sage: L.free_module(map=False)                                              # needs sage.rings.finite_rings
            Vector space of dimension 3 over
             Field in a with defining polynomial x^2 + 7*x + 2 over its base

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: L.degree(GF(11^3))                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 11^3"""
    @overload
    def free_module(self, K) -> Any:
        """RingExtensionWithBasis.free_module(self, base=None, map=True)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2327)

        Return a free module V over ``base`` which is isomorphic to
        this ring

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        - ``map`` -- boolean (default: ``True``); whether to return
          isomorphisms between this ring and V

        OUTPUT:

        - A finite-rank free module V over ``base``

        - The isomorphism from V to this ring corresponding to the
          basis output by the method :meth:`basis_over`
          (only included if ``map`` is ``True``)

        - The reverse isomorphism of the isomorphism above
          (only included if ``map`` is ``True``)

        EXAMPLES::

            sage: F = GF(11)
            sage: K.<a> = GF(11^2).over()                                               # needs sage.rings.finite_rings
            sage: L.<b> = GF(11^6).over(K)                                              # needs sage.rings.finite_rings

        Forgetting a part of the multiplicative structure, the field L
        can be viewed as a vector space of dimension 3 over K, equipped
        with a distinguished basis, namely `(1, b, b^2)`::

            sage: # needs sage.rings.finite_rings
            sage: V, i, j = L.free_module(K)
            sage: V
            Vector space of dimension 3 over
             Field in a with defining polynomial x^2 + 7*x + 2 over its base
            sage: i
            Generic map:
              From: Vector space of dimension 3 over
                    Field in a with defining polynomial x^2 + 7*x + 2 over its base
              To:   Field in b with defining polynomial
                    x^3 + (7 + 2*a)*x^2 + (2 - a)*x - a over its base
            sage: j
            Generic map:
              From: Field in b with defining polynomial
                    x^3 + (7 + 2*a)*x^2 + (2 - a)*x - a over its base
              To:   Vector space of dimension 3 over
                    Field in a with defining polynomial x^2 + 7*x + 2 over its base
            sage: j(b)
            (0, 1, 0)
            sage: i((1, a, a+1))
            1 + a*b + (1 + a)*b^2

        Similarly, one can view L as a F-vector space of dimension 6::

            sage: V, i, j, = L.free_module(F)                                           # needs sage.rings.finite_rings
            sage: V                                                                     # needs sage.rings.finite_rings
            Vector space of dimension 6 over Finite Field of size 11

        In this case, the isomorphisms between `V` and `L` are given by the
        basis `(1, a, b, ab, b^2, ab^2)`:

            sage: j(a*b)                                                                # needs sage.rings.finite_rings
            (0, 0, 0, 1, 0, 0)
            sage: i((1,2,3,4,5,6))                                                      # needs sage.rings.finite_rings
            (1 + 2*a) + (3 + 4*a)*b + (5 + 6*a)*b^2

        When ``base`` is omitted, the default is the base of this extension::

            sage: L.free_module(map=False)                                              # needs sage.rings.finite_rings
            Vector space of dimension 3 over
             Field in a with defining polynomial x^2 + 7*x + 2 over its base

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: L.degree(GF(11^3))                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 11^3"""
    @overload
    def free_module(self, F) -> Any:
        """RingExtensionWithBasis.free_module(self, base=None, map=True)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2327)

        Return a free module V over ``base`` which is isomorphic to
        this ring

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        - ``map`` -- boolean (default: ``True``); whether to return
          isomorphisms between this ring and V

        OUTPUT:

        - A finite-rank free module V over ``base``

        - The isomorphism from V to this ring corresponding to the
          basis output by the method :meth:`basis_over`
          (only included if ``map`` is ``True``)

        - The reverse isomorphism of the isomorphism above
          (only included if ``map`` is ``True``)

        EXAMPLES::

            sage: F = GF(11)
            sage: K.<a> = GF(11^2).over()                                               # needs sage.rings.finite_rings
            sage: L.<b> = GF(11^6).over(K)                                              # needs sage.rings.finite_rings

        Forgetting a part of the multiplicative structure, the field L
        can be viewed as a vector space of dimension 3 over K, equipped
        with a distinguished basis, namely `(1, b, b^2)`::

            sage: # needs sage.rings.finite_rings
            sage: V, i, j = L.free_module(K)
            sage: V
            Vector space of dimension 3 over
             Field in a with defining polynomial x^2 + 7*x + 2 over its base
            sage: i
            Generic map:
              From: Vector space of dimension 3 over
                    Field in a with defining polynomial x^2 + 7*x + 2 over its base
              To:   Field in b with defining polynomial
                    x^3 + (7 + 2*a)*x^2 + (2 - a)*x - a over its base
            sage: j
            Generic map:
              From: Field in b with defining polynomial
                    x^3 + (7 + 2*a)*x^2 + (2 - a)*x - a over its base
              To:   Vector space of dimension 3 over
                    Field in a with defining polynomial x^2 + 7*x + 2 over its base
            sage: j(b)
            (0, 1, 0)
            sage: i((1, a, a+1))
            1 + a*b + (1 + a)*b^2

        Similarly, one can view L as a F-vector space of dimension 6::

            sage: V, i, j, = L.free_module(F)                                           # needs sage.rings.finite_rings
            sage: V                                                                     # needs sage.rings.finite_rings
            Vector space of dimension 6 over Finite Field of size 11

        In this case, the isomorphisms between `V` and `L` are given by the
        basis `(1, a, b, ab, b^2, ab^2)`:

            sage: j(a*b)                                                                # needs sage.rings.finite_rings
            (0, 0, 0, 1, 0, 0)
            sage: i((1,2,3,4,5,6))                                                      # needs sage.rings.finite_rings
            (1 + 2*a) + (3 + 4*a)*b + (5 + 6*a)*b^2

        When ``base`` is omitted, the default is the base of this extension::

            sage: L.free_module(map=False)                                              # needs sage.rings.finite_rings
            Vector space of dimension 3 over
             Field in a with defining polynomial x^2 + 7*x + 2 over its base

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: L.degree(GF(11^3))                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 11^3"""
    @overload
    def free_module(self, map=...) -> Any:
        """RingExtensionWithBasis.free_module(self, base=None, map=True)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2327)

        Return a free module V over ``base`` which is isomorphic to
        this ring

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        - ``map`` -- boolean (default: ``True``); whether to return
          isomorphisms between this ring and V

        OUTPUT:

        - A finite-rank free module V over ``base``

        - The isomorphism from V to this ring corresponding to the
          basis output by the method :meth:`basis_over`
          (only included if ``map`` is ``True``)

        - The reverse isomorphism of the isomorphism above
          (only included if ``map`` is ``True``)

        EXAMPLES::

            sage: F = GF(11)
            sage: K.<a> = GF(11^2).over()                                               # needs sage.rings.finite_rings
            sage: L.<b> = GF(11^6).over(K)                                              # needs sage.rings.finite_rings

        Forgetting a part of the multiplicative structure, the field L
        can be viewed as a vector space of dimension 3 over K, equipped
        with a distinguished basis, namely `(1, b, b^2)`::

            sage: # needs sage.rings.finite_rings
            sage: V, i, j = L.free_module(K)
            sage: V
            Vector space of dimension 3 over
             Field in a with defining polynomial x^2 + 7*x + 2 over its base
            sage: i
            Generic map:
              From: Vector space of dimension 3 over
                    Field in a with defining polynomial x^2 + 7*x + 2 over its base
              To:   Field in b with defining polynomial
                    x^3 + (7 + 2*a)*x^2 + (2 - a)*x - a over its base
            sage: j
            Generic map:
              From: Field in b with defining polynomial
                    x^3 + (7 + 2*a)*x^2 + (2 - a)*x - a over its base
              To:   Vector space of dimension 3 over
                    Field in a with defining polynomial x^2 + 7*x + 2 over its base
            sage: j(b)
            (0, 1, 0)
            sage: i((1, a, a+1))
            1 + a*b + (1 + a)*b^2

        Similarly, one can view L as a F-vector space of dimension 6::

            sage: V, i, j, = L.free_module(F)                                           # needs sage.rings.finite_rings
            sage: V                                                                     # needs sage.rings.finite_rings
            Vector space of dimension 6 over Finite Field of size 11

        In this case, the isomorphisms between `V` and `L` are given by the
        basis `(1, a, b, ab, b^2, ab^2)`:

            sage: j(a*b)                                                                # needs sage.rings.finite_rings
            (0, 0, 0, 1, 0, 0)
            sage: i((1,2,3,4,5,6))                                                      # needs sage.rings.finite_rings
            (1 + 2*a) + (3 + 4*a)*b + (5 + 6*a)*b^2

        When ``base`` is omitted, the default is the base of this extension::

            sage: L.free_module(map=False)                                              # needs sage.rings.finite_rings
            Vector space of dimension 3 over
             Field in a with defining polynomial x^2 + 7*x + 2 over its base

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: L.degree(GF(11^3))                                                    # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field in z3 of size 11^3"""

class RingExtensionWithGen(RingExtensionWithBasis):
    """RingExtensionWithGen(defining_morphism, gen, names, check=True, **kwargs)

    File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2537)

    A class for finite free ring extensions generated by
    a single element

    TESTS::

        sage: # needs sage.rings.number_field
        sage: x = polygen(ZZ, 'x')
        sage: A.<a> = QQ.extension(x^3 - 7)
        sage: K = A.over()
        sage: type(K)
        <class 'sage.rings.ring_extension.RingExtensionWithGen'>
        sage: TestSuite(K).run()"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, defining_morphism, gen, names, check=..., **kwargs) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2552)

                Initialize this ring extension.

                INPUT:

                - ``defining_morphism`` -- a ring homomorphism

                - ``gen`` -- a generator of this extension

                - ``names`` -- tuple of strings or ``None`` (default: ``None``);
                  the way the elements of the basis are printed

                - ``check`` -- boolean (default: ``True``); whether to check if
                  ``gen`` is indeed a generator

                TESTS::

                    sage: x = polygen(ZZ, 'x')
                    sage: K.<a> = QQ.extension(x^3 + 3*x + 1)                                   # needs sage.rings.number_field
                    sage: E = K.over(); E                                                       # needs sage.rings.number_field
                    Field in a with defining polynomial x^3 + 3*x + 1 over its base

                    sage: TestSuite(E).run()                                                    # needs sage.rings.number_field
        """
    def fraction_field(self, extend_base=...) -> Any:
        """RingExtensionWithGen.fraction_field(self, extend_base=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2697)

        Return the fraction field of this extension.

        INPUT:

        - ``extend_base`` -- boolean (default: ``False``)

        If ``extend_base`` is ``False``, the fraction field of the
        extension `L/K` is defined as `\\textrm{Frac}(L)/L/K`, except
        is `L` is already a field in which base the fraction field
        of `L/K` is `L/K` itself.

        If ``extend_base`` is ``True``, the fraction field of the
        extension `L/K` is defined as `\\textrm{Frac}(L)/\\textrm{Frac}(K)`
        (provided that the defining morphism extends to the fraction
        fields, i.e. is injective).

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: A.<a> = ZZ.extension(x^2 - 5)
            sage: OK = A.over()   # over ZZ
            sage: OK
            Order of conductor 2 generated by a in Number Field in a
             with defining polynomial x^2 - 5 over its base
            sage: K1 = OK.fraction_field(); K1
            Fraction Field of Order of conductor 2 generated by a
             in Number Field in a with defining polynomial x^2 - 5 over its base
            sage: K1.bases()
            [Fraction Field of Order of conductor 2 generated by a
              in Number Field in a with defining polynomial x^2 - 5 over its base,
             Order of conductor 2 generated by a in Number Field in a
              with defining polynomial x^2 - 5 over its base,
             Integer Ring]
            sage: K2 = OK.fraction_field(extend_base=True); K2
            Fraction Field of Order of conductor 2 generated by a
             in Number Field in a with defining polynomial x^2 - 5 over its base
            sage: K2.bases()
            [Fraction Field of Order of conductor 2 generated by a
              in Number Field in a with defining polynomial x^2 - 5 over its base,
             Rational Field]

        Note that there is no coercion map between `K_1` and `K_2`::

            sage: K1.has_coerce_map_from(K2)                                            # needs sage.rings.number_field
            False
            sage: K2.has_coerce_map_from(K1)                                            # needs sage.rings.number_field
            False

        We check that when the extension is a field, its fraction field does not change::

            sage: K1.fraction_field() is K1                                             # needs sage.rings.number_field
            True
            sage: K2.fraction_field() is K2                                             # needs sage.rings.number_field
            True

        TESTS::

            sage: A = GF(5).over(ZZ)
            sage: A.fraction_field(extend_base=True)
            Traceback (most recent call last):
            ...
            ValueError: the morphism is not injective"""
    @overload
    def gens(self, base=...) -> tuple:
        """RingExtensionWithGen.gens(self, base=None) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2666)

        Return the generators of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()  # over GF(5)
            sage: K.gens()
            (a,)
            sage: L.<b> = GF(5^4).over(K)
            sage: L.gens()
            (b,)
            sage: L.gens(GF(5))
            (b, a)"""
    @overload
    def gens(self) -> Any:
        """RingExtensionWithGen.gens(self, base=None) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2666)

        Return the generators of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()  # over GF(5)
            sage: K.gens()
            (a,)
            sage: L.<b> = GF(5^4).over(K)
            sage: L.gens()
            (b,)
            sage: L.gens(GF(5))
            (b, a)"""
    @overload
    def gens(self) -> Any:
        """RingExtensionWithGen.gens(self, base=None) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2666)

        Return the generators of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()  # over GF(5)
            sage: K.gens()
            (a,)
            sage: L.<b> = GF(5^4).over(K)
            sage: L.gens()
            (b,)
            sage: L.gens(GF(5))
            (b, a)"""
    @overload
    def modulus(self, var=...) -> Any:
        """RingExtensionWithGen.modulus(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2634)

        Return the defining polynomial of this extension, that is the
        minimal polynomial of the given generator of this extension.

        INPUT:

        - ``var`` -- a variable name (default: ``x``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<u> = GF(7^10).over(GF(7^2)); K
            Field in u with defining polynomial x^5 + (6*z2 + 4)*x^4
             + (3*z2 + 5)*x^3 + (2*z2 + 2)*x^2 + 4*x + 6*z2 over its base
            sage: P = K.modulus(); P
            x^5 + (6*z2 + 4)*x^4 + (3*z2 + 5)*x^3 + (2*z2 + 2)*x^2 + 4*x + 6*z2
            sage: P(u)
            0

        We can use a different variable name::

            sage: K.modulus('y')                                                        # needs sage.rings.finite_rings
            y^5 + (6*z2 + 4)*y^4 + (3*z2 + 5)*y^3 + (2*z2 + 2)*y^2 + 4*y + 6*z2"""
    @overload
    def modulus(self) -> Any:
        """RingExtensionWithGen.modulus(self, var='x')

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 2634)

        Return the defining polynomial of this extension, that is the
        minimal polynomial of the given generator of this extension.

        INPUT:

        - ``var`` -- a variable name (default: ``x``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<u> = GF(7^10).over(GF(7^2)); K
            Field in u with defining polynomial x^5 + (6*z2 + 4)*x^4
             + (3*z2 + 5)*x^3 + (2*z2 + 2)*x^2 + 4*x + 6*z2 over its base
            sage: P = K.modulus(); P
            x^5 + (6*z2 + 4)*x^4 + (3*z2 + 5)*x^3 + (2*z2 + 2)*x^2 + 4*x + 6*z2
            sage: P(u)
            0

        We can use a different variable name::

            sage: K.modulus('y')                                                        # needs sage.rings.finite_rings
            y^5 + (6*z2 + 4)*y^4 + (3*z2 + 5)*y^3 + (2*z2 + 2)*y^2 + 4*y + 6*z2"""

class RingExtension_generic(sage.structure.parent.Parent):
    """RingExtension_generic(defining_morphism, print_options={}, import_methods=True, is_backend_exposed=False, category=None)

    File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 501)

    A generic class for all ring extensions.

    TESTS::

        sage: Q = QQ.over(ZZ)  # indirect doctest
        sage: Q
        Rational Field over its base

        sage: type(Q)
        <class 'sage.rings.ring_extension.RingExtension_generic'>

        sage: TestSuite(Q).run()"""
    Element: ClassVar[type[sage.rings.ring_extension_element.RingExtensionElement]] = ...
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, defining_morphism, print_options=..., import_methods=..., is_backend_exposed=..., category=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 518)

                Initialize this ring extension.

                INPUT:

                - ``defining_morphism`` -- a ring homomorphism

                - ``print_options`` -- dictionary

                - ``import_methods`` -- boolean (default: ``True``); whether this
                  parent (resp. its elements) import the methods of the backend
                  parent class (resp. element class)

                - ``is_backend_exposed`` -- boolean (default: ``False``); whether
                  the backend ring can be exposed to the user

                - ``category`` -- the category for the resulting parent
                  (default: ``CommutativeRings()``)

                .. NOTE::

                    The attribute ``is_backend_exposed`` is only used for printing;
                    when it is ``False``, printing an element like its backend is
                    disabled (and a :exc:`RuntimeError` is raised when it would occur).

                OUTPUT: the extension defined by ``defining_morphism``

                EXAMPLES::

                    sage: QQ.over(ZZ)
                    Rational Field over its base

                    sage: S.<x> = QQ[]
                    sage: S.over()  # over QQ
                    Univariate Polynomial Ring in x over Rational Field over its base

                TESTS::

                    sage: ZZ.over(NN)
                    Traceback (most recent call last):
                    ...
                    TypeError: only commutative rings are accepted

                    sage: K = GF(5^3)                                                           # needs sage.rings.finite_rings
                    sage: K.over(K.frobenius_endomorphism())                                    # needs sage.rings.finite_rings
                    Traceback (most recent call last):
                    ...
                    ValueError: exotic defining morphism between two rings in the tower; consider using another variable name
        """
    def absolute_base(self) -> Any:
        """RingExtension_generic.absolute_base(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1135)

        Return the absolute base of this extension.

        By definition, the absolute base of an iterated extension
        `K_n/\\cdots K_2/K_1` is the ring `K_1`.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()   # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.absolute_base()
            Finite Field of size 5
            sage: K.absolute_base()
            Finite Field of size 5
            sage: L.absolute_base()
            Finite Field of size 5

        .. SEEALSO::

            :meth:`base`, :meth:`bases`, :meth:`is_defined_over`"""
    @overload
    def absolute_degree(self) -> Any:
        """RingExtension_generic.absolute_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1532)

        Return the degree of this extension over its absolute base.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A = GF(5^4).over(GF(5^2))
            sage: B = GF(5^12).over(A)
            sage: A.absolute_degree()
            2
            sage: B.absolute_degree()
            6

        .. SEEALSO::

            :meth:`degree`, :meth:`relative_degree`"""
    @overload
    def absolute_degree(self) -> Any:
        """RingExtension_generic.absolute_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1532)

        Return the degree of this extension over its absolute base.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A = GF(5^4).over(GF(5^2))
            sage: B = GF(5^12).over(A)
            sage: A.absolute_degree()
            2
            sage: B.absolute_degree()
            6

        .. SEEALSO::

            :meth:`degree`, :meth:`relative_degree`"""
    @overload
    def absolute_degree(self) -> Any:
        """RingExtension_generic.absolute_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1532)

        Return the degree of this extension over its absolute base.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A = GF(5^4).over(GF(5^2))
            sage: B = GF(5^12).over(A)
            sage: A.absolute_degree()
            2
            sage: B.absolute_degree()
            6

        .. SEEALSO::

            :meth:`degree`, :meth:`relative_degree`"""
    @overload
    def backend(self, force=...) -> Any:
        """RingExtension_generic.backend(self, force=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 730)

        Return the backend of this extension.

        INPUT:

        - ``force`` -- boolean (default: ``False``); if ``False``,
          raise an error if the backend is not exposed

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^3)
            sage: E = K.over()
            sage: E
            Field in z3 with defining polynomial x^3 + 3*x + 3 over its base
            sage: E.backend()
            Finite Field in z3 of size 5^3
            sage: E.backend() is K
            True"""
    @overload
    def backend(self) -> Any:
        """RingExtension_generic.backend(self, force=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 730)

        Return the backend of this extension.

        INPUT:

        - ``force`` -- boolean (default: ``False``); if ``False``,
          raise an error if the backend is not exposed

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^3)
            sage: E = K.over()
            sage: E
            Field in z3 with defining polynomial x^3 + 3*x + 3 over its base
            sage: E.backend()
            Finite Field in z3 of size 5^3
            sage: E.backend() is K
            True"""
    @overload
    def backend(self) -> Any:
        """RingExtension_generic.backend(self, force=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 730)

        Return the backend of this extension.

        INPUT:

        - ``force`` -- boolean (default: ``False``); if ``False``,
          raise an error if the backend is not exposed

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^3)
            sage: E = K.over()
            sage: E
            Field in z3 with defining polynomial x^3 + 3*x + 3 over its base
            sage: E.backend()
            Finite Field in z3 of size 5^3
            sage: E.backend() is K
            True"""
    @overload
    def base(self) -> Any:
        """RingExtension_generic.base(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1074)

        Return the base of this extension.

        EXAMPLES::

            sage: F = GF(5^2)                                                           # needs sage.rings.finite_rings
            sage: K = GF(5^4).over(F)                                                   # needs sage.rings.finite_rings
            sage: K.base()                                                              # needs sage.rings.finite_rings
            Finite Field in z2 of size 5^2

        In case of iterated extensions, the base is itself an extension::

            sage: L = GF(5^8).over(K)                                                   # needs sage.rings.finite_rings
            sage: L.base()                                                              # needs sage.rings.finite_rings
            Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
            sage: L.base() is K                                                         # needs sage.rings.finite_rings
            True

        .. SEEALSO::

            :meth:`bases`, :meth:`absolute_base`, :meth:`is_defined_over`"""
    @overload
    def base(self) -> Any:
        """RingExtension_generic.base(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1074)

        Return the base of this extension.

        EXAMPLES::

            sage: F = GF(5^2)                                                           # needs sage.rings.finite_rings
            sage: K = GF(5^4).over(F)                                                   # needs sage.rings.finite_rings
            sage: K.base()                                                              # needs sage.rings.finite_rings
            Finite Field in z2 of size 5^2

        In case of iterated extensions, the base is itself an extension::

            sage: L = GF(5^8).over(K)                                                   # needs sage.rings.finite_rings
            sage: L.base()                                                              # needs sage.rings.finite_rings
            Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
            sage: L.base() is K                                                         # needs sage.rings.finite_rings
            True

        .. SEEALSO::

            :meth:`bases`, :meth:`absolute_base`, :meth:`is_defined_over`"""
    @overload
    def base(self) -> Any:
        """RingExtension_generic.base(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1074)

        Return the base of this extension.

        EXAMPLES::

            sage: F = GF(5^2)                                                           # needs sage.rings.finite_rings
            sage: K = GF(5^4).over(F)                                                   # needs sage.rings.finite_rings
            sage: K.base()                                                              # needs sage.rings.finite_rings
            Finite Field in z2 of size 5^2

        In case of iterated extensions, the base is itself an extension::

            sage: L = GF(5^8).over(K)                                                   # needs sage.rings.finite_rings
            sage: L.base()                                                              # needs sage.rings.finite_rings
            Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
            sage: L.base() is K                                                         # needs sage.rings.finite_rings
            True

        .. SEEALSO::

            :meth:`bases`, :meth:`absolute_base`, :meth:`is_defined_over`"""
    @overload
    def base(self) -> Any:
        """RingExtension_generic.base(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1074)

        Return the base of this extension.

        EXAMPLES::

            sage: F = GF(5^2)                                                           # needs sage.rings.finite_rings
            sage: K = GF(5^4).over(F)                                                   # needs sage.rings.finite_rings
            sage: K.base()                                                              # needs sage.rings.finite_rings
            Finite Field in z2 of size 5^2

        In case of iterated extensions, the base is itself an extension::

            sage: L = GF(5^8).over(K)                                                   # needs sage.rings.finite_rings
            sage: L.base()                                                              # needs sage.rings.finite_rings
            Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
            sage: L.base() is K                                                         # needs sage.rings.finite_rings
            True

        .. SEEALSO::

            :meth:`bases`, :meth:`absolute_base`, :meth:`is_defined_over`"""
    @overload
    def bases(self) -> Any:
        """RingExtension_generic.bases(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1099)

        Return the list of successive bases of this extension
        (including itself).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()  # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.bases()
            [Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]
            sage: K.bases()
            [Field in z4 with defining polynomial x^2 + (3 - z2)*x + z2 over its base,
             Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]
            sage: L.bases()
            [Field in z12 with defining polynomial
              x^3 + (1 + (2 - z2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base,
             Field in z4 with defining polynomial x^2 + (3 - z2)*x + z2 over its base,
             Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]

        .. SEEALSO::

            :meth:`base`, :meth:`absolute_base`, :meth:`is_defined_over`"""
    @overload
    def bases(self) -> Any:
        """RingExtension_generic.bases(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1099)

        Return the list of successive bases of this extension
        (including itself).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()  # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.bases()
            [Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]
            sage: K.bases()
            [Field in z4 with defining polynomial x^2 + (3 - z2)*x + z2 over its base,
             Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]
            sage: L.bases()
            [Field in z12 with defining polynomial
              x^3 + (1 + (2 - z2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base,
             Field in z4 with defining polynomial x^2 + (3 - z2)*x + z2 over its base,
             Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]

        .. SEEALSO::

            :meth:`base`, :meth:`absolute_base`, :meth:`is_defined_over`"""
    @overload
    def bases(self) -> Any:
        """RingExtension_generic.bases(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1099)

        Return the list of successive bases of this extension
        (including itself).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()  # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.bases()
            [Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]
            sage: K.bases()
            [Field in z4 with defining polynomial x^2 + (3 - z2)*x + z2 over its base,
             Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]
            sage: L.bases()
            [Field in z12 with defining polynomial
              x^3 + (1 + (2 - z2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base,
             Field in z4 with defining polynomial x^2 + (3 - z2)*x + z2 over its base,
             Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]

        .. SEEALSO::

            :meth:`base`, :meth:`absolute_base`, :meth:`is_defined_over`"""
    @overload
    def bases(self) -> Any:
        """RingExtension_generic.bases(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1099)

        Return the list of successive bases of this extension
        (including itself).

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()  # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.bases()
            [Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]
            sage: K.bases()
            [Field in z4 with defining polynomial x^2 + (3 - z2)*x + z2 over its base,
             Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]
            sage: L.bases()
            [Field in z12 with defining polynomial
              x^3 + (1 + (2 - z2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base,
             Field in z4 with defining polynomial x^2 + (3 - z2)*x + z2 over its base,
             Field in z2 with defining polynomial x^2 + 4*x + 2 over its base,
             Finite Field of size 5]

        .. SEEALSO::

            :meth:`base`, :meth:`absolute_base`, :meth:`is_defined_over`"""
    @overload
    def characteristic(self) -> Any:
        """RingExtension_generic.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1916)

        Return the characteristic of the extension as a ring.

        OUTPUT: a prime number or zero

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()   # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.characteristic()
            5
            sage: K.characteristic()
            5
            sage: L.characteristic()
            5

        ::

            sage: F = RR.over(ZZ)
            sage: F.characteristic()
            0

        ::

            sage: F = GF(11)
            sage: A.<x> = F[]
            sage: K = Frac(F).over(F)
            sage: K.characteristic()
            11

        ::

            sage: E = GF(7).over(ZZ)
            sage: E.characteristic()
            7

        TESTS:

        Ensure issue :issue:`34692` is fixed::

            sage: Fq = GF(11)
            sage: FqX.<X> = Fq[]
            sage: k = Frac(FqX)
            sage: K = k.over(FqX)
            sage: K.frobenius_endomorphism()
            Frobenius endomorphism x |--> x^11 of
             Fraction Field of Univariate Polynomial Ring in X over
              Finite Field of size 11 over its base"""
    @overload
    def characteristic(self) -> Any:
        """RingExtension_generic.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1916)

        Return the characteristic of the extension as a ring.

        OUTPUT: a prime number or zero

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()   # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.characteristic()
            5
            sage: K.characteristic()
            5
            sage: L.characteristic()
            5

        ::

            sage: F = RR.over(ZZ)
            sage: F.characteristic()
            0

        ::

            sage: F = GF(11)
            sage: A.<x> = F[]
            sage: K = Frac(F).over(F)
            sage: K.characteristic()
            11

        ::

            sage: E = GF(7).over(ZZ)
            sage: E.characteristic()
            7

        TESTS:

        Ensure issue :issue:`34692` is fixed::

            sage: Fq = GF(11)
            sage: FqX.<X> = Fq[]
            sage: k = Frac(FqX)
            sage: K = k.over(FqX)
            sage: K.frobenius_endomorphism()
            Frobenius endomorphism x |--> x^11 of
             Fraction Field of Univariate Polynomial Ring in X over
              Finite Field of size 11 over its base"""
    @overload
    def characteristic(self) -> Any:
        """RingExtension_generic.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1916)

        Return the characteristic of the extension as a ring.

        OUTPUT: a prime number or zero

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()   # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.characteristic()
            5
            sage: K.characteristic()
            5
            sage: L.characteristic()
            5

        ::

            sage: F = RR.over(ZZ)
            sage: F.characteristic()
            0

        ::

            sage: F = GF(11)
            sage: A.<x> = F[]
            sage: K = Frac(F).over(F)
            sage: K.characteristic()
            11

        ::

            sage: E = GF(7).over(ZZ)
            sage: E.characteristic()
            7

        TESTS:

        Ensure issue :issue:`34692` is fixed::

            sage: Fq = GF(11)
            sage: FqX.<X> = Fq[]
            sage: k = Frac(FqX)
            sage: K = k.over(FqX)
            sage: K.frobenius_endomorphism()
            Frobenius endomorphism x |--> x^11 of
             Fraction Field of Univariate Polynomial Ring in X over
              Finite Field of size 11 over its base"""
    @overload
    def characteristic(self) -> Any:
        """RingExtension_generic.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1916)

        Return the characteristic of the extension as a ring.

        OUTPUT: a prime number or zero

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()   # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.characteristic()
            5
            sage: K.characteristic()
            5
            sage: L.characteristic()
            5

        ::

            sage: F = RR.over(ZZ)
            sage: F.characteristic()
            0

        ::

            sage: F = GF(11)
            sage: A.<x> = F[]
            sage: K = Frac(F).over(F)
            sage: K.characteristic()
            11

        ::

            sage: E = GF(7).over(ZZ)
            sage: E.characteristic()
            7

        TESTS:

        Ensure issue :issue:`34692` is fixed::

            sage: Fq = GF(11)
            sage: FqX.<X> = Fq[]
            sage: k = Frac(FqX)
            sage: K = k.over(FqX)
            sage: K.frobenius_endomorphism()
            Frobenius endomorphism x |--> x^11 of
             Fraction Field of Univariate Polynomial Ring in X over
              Finite Field of size 11 over its base"""
    @overload
    def characteristic(self) -> Any:
        """RingExtension_generic.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1916)

        Return the characteristic of the extension as a ring.

        OUTPUT: a prime number or zero

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()   # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.characteristic()
            5
            sage: K.characteristic()
            5
            sage: L.characteristic()
            5

        ::

            sage: F = RR.over(ZZ)
            sage: F.characteristic()
            0

        ::

            sage: F = GF(11)
            sage: A.<x> = F[]
            sage: K = Frac(F).over(F)
            sage: K.characteristic()
            11

        ::

            sage: E = GF(7).over(ZZ)
            sage: E.characteristic()
            7

        TESTS:

        Ensure issue :issue:`34692` is fixed::

            sage: Fq = GF(11)
            sage: FqX.<X> = Fq[]
            sage: k = Frac(FqX)
            sage: K = k.over(FqX)
            sage: K.frobenius_endomorphism()
            Frobenius endomorphism x |--> x^11 of
             Fraction Field of Univariate Polynomial Ring in X over
              Finite Field of size 11 over its base"""
    @overload
    def characteristic(self) -> Any:
        """RingExtension_generic.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1916)

        Return the characteristic of the extension as a ring.

        OUTPUT: a prime number or zero

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()   # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.characteristic()
            5
            sage: K.characteristic()
            5
            sage: L.characteristic()
            5

        ::

            sage: F = RR.over(ZZ)
            sage: F.characteristic()
            0

        ::

            sage: F = GF(11)
            sage: A.<x> = F[]
            sage: K = Frac(F).over(F)
            sage: K.characteristic()
            11

        ::

            sage: E = GF(7).over(ZZ)
            sage: E.characteristic()
            7

        TESTS:

        Ensure issue :issue:`34692` is fixed::

            sage: Fq = GF(11)
            sage: FqX.<X> = Fq[]
            sage: k = Frac(FqX)
            sage: K = k.over(FqX)
            sage: K.frobenius_endomorphism()
            Frobenius endomorphism x |--> x^11 of
             Fraction Field of Univariate Polynomial Ring in X over
              Finite Field of size 11 over its base"""
    @overload
    def characteristic(self) -> Any:
        """RingExtension_generic.characteristic(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1916)

        Return the characteristic of the extension as a ring.

        OUTPUT: a prime number or zero

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2).over()   # over GF(5)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: F.characteristic()
            5
            sage: K.characteristic()
            5
            sage: L.characteristic()
            5

        ::

            sage: F = RR.over(ZZ)
            sage: F.characteristic()
            0

        ::

            sage: F = GF(11)
            sage: A.<x> = F[]
            sage: K = Frac(F).over(F)
            sage: K.characteristic()
            11

        ::

            sage: E = GF(7).over(ZZ)
            sage: E.characteristic()
            7

        TESTS:

        Ensure issue :issue:`34692` is fixed::

            sage: Fq = GF(11)
            sage: FqX.<X> = Fq[]
            sage: k = Frac(FqX)
            sage: K = k.over(FqX)
            sage: K.frobenius_endomorphism()
            Frobenius endomorphism x |--> x^11 of
             Fraction Field of Univariate Polynomial Ring in X over
              Finite Field of size 11 over its base"""
    @overload
    def construction(self) -> Any:
        """RingExtension_generic.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 718)

        Return the functorial construction of this extension, if defined.

        EXAMPLES::

             sage: E = GF(5^3).over()                                                   # needs sage.rings.finite_rings
             sage: E.construction()                                                     # needs sage.rings.finite_rings"""
    @overload
    def construction(self) -> Any:
        """RingExtension_generic.construction(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 718)

        Return the functorial construction of this extension, if defined.

        EXAMPLES::

             sage: E = GF(5^3).over()                                                   # needs sage.rings.finite_rings
             sage: E.construction()                                                     # needs sage.rings.finite_rings"""
    @overload
    def defining_morphism(self, base=...) -> Any:
        """RingExtension_generic.defining_morphism(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1259)

        Return the defining morphism of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: K.defining_morphism()
            Ring morphism:
              From: Finite Field in z2 of size 5^2
              To:   Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
              Defn: z2 |--> z2
            sage: L.defining_morphism()
            Ring morphism:
              From: Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
              To:   Field in z12 with defining polynomial
                    x^3 + (1 + (4*z2 + 2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base
              Defn: z4 |--> z4

        One can also pass in a base over which the extension is explicitly
        defined (see also :meth:`is_defined_over`)::

            sage: L.defining_morphism(F)                                                # needs sage.rings.finite_rings
            Ring morphism:
              From: Finite Field in z2 of size 5^2
              To:   Field in z12 with defining polynomial
                    x^3 + (1 + (4*z2 + 2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base
              Defn: z2 |--> z2
            sage: L.defining_morphism(GF(5))                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5"""
    @overload
    def defining_morphism(self) -> Any:
        """RingExtension_generic.defining_morphism(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1259)

        Return the defining morphism of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: K.defining_morphism()
            Ring morphism:
              From: Finite Field in z2 of size 5^2
              To:   Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
              Defn: z2 |--> z2
            sage: L.defining_morphism()
            Ring morphism:
              From: Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
              To:   Field in z12 with defining polynomial
                    x^3 + (1 + (4*z2 + 2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base
              Defn: z4 |--> z4

        One can also pass in a base over which the extension is explicitly
        defined (see also :meth:`is_defined_over`)::

            sage: L.defining_morphism(F)                                                # needs sage.rings.finite_rings
            Ring morphism:
              From: Finite Field in z2 of size 5^2
              To:   Field in z12 with defining polynomial
                    x^3 + (1 + (4*z2 + 2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base
              Defn: z2 |--> z2
            sage: L.defining_morphism(GF(5))                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5"""
    @overload
    def defining_morphism(self) -> Any:
        """RingExtension_generic.defining_morphism(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1259)

        Return the defining morphism of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: K.defining_morphism()
            Ring morphism:
              From: Finite Field in z2 of size 5^2
              To:   Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
              Defn: z2 |--> z2
            sage: L.defining_morphism()
            Ring morphism:
              From: Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
              To:   Field in z12 with defining polynomial
                    x^3 + (1 + (4*z2 + 2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base
              Defn: z4 |--> z4

        One can also pass in a base over which the extension is explicitly
        defined (see also :meth:`is_defined_over`)::

            sage: L.defining_morphism(F)                                                # needs sage.rings.finite_rings
            Ring morphism:
              From: Finite Field in z2 of size 5^2
              To:   Field in z12 with defining polynomial
                    x^3 + (1 + (4*z2 + 2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base
              Defn: z2 |--> z2
            sage: L.defining_morphism(GF(5))                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5"""
    @overload
    def defining_morphism(self, F) -> Any:
        """RingExtension_generic.defining_morphism(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1259)

        Return the defining morphism of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: K.defining_morphism()
            Ring morphism:
              From: Finite Field in z2 of size 5^2
              To:   Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
              Defn: z2 |--> z2
            sage: L.defining_morphism()
            Ring morphism:
              From: Field in z4 with defining polynomial x^2 + (4*z2 + 3)*x + z2 over its base
              To:   Field in z12 with defining polynomial
                    x^3 + (1 + (4*z2 + 2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base
              Defn: z4 |--> z4

        One can also pass in a base over which the extension is explicitly
        defined (see also :meth:`is_defined_over`)::

            sage: L.defining_morphism(F)                                                # needs sage.rings.finite_rings
            Ring morphism:
              From: Finite Field in z2 of size 5^2
              To:   Field in z12 with defining polynomial
                    x^3 + (1 + (4*z2 + 2)*z4)*x^2 + (2 + 2*z4)*x - z4 over its base
              Defn: z2 |--> z2
            sage: L.defining_morphism(GF(5))                                            # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5"""
    @overload
    def degree(self, base) -> Any:
        """RingExtension_generic.degree(self, base)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1481)

        Return the degree of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A = GF(5^4).over(GF(5^2))
            sage: B = GF(5^12).over(A)
            sage: A.degree(GF(5^2))
            2
            sage: B.degree(A)
            3
            sage: B.degree(GF(5^2))
            6

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: A.degree(GF(5))                                                       # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5

        .. SEEALSO::

            :meth:`relative_degree`, :meth:`absolute_degree`"""
    @overload
    def degree(self, A) -> Any:
        """RingExtension_generic.degree(self, base)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1481)

        Return the degree of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A = GF(5^4).over(GF(5^2))
            sage: B = GF(5^12).over(A)
            sage: A.degree(GF(5^2))
            2
            sage: B.degree(A)
            3
            sage: B.degree(GF(5^2))
            6

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: A.degree(GF(5))                                                       # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5

        .. SEEALSO::

            :meth:`relative_degree`, :meth:`absolute_degree`"""
    @overload
    def degree_over(self, base=...) -> Any:
        """RingExtension_generic.degree_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1414)

        Return the degree of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: K.degree_over(F)
            2
            sage: L.degree_over(K)
            3
            sage: L.degree_over(F)
            6

        If ``base`` is omitted, the degree is computed over the base
        of the extension::

            sage: K.degree_over()                                                       # needs sage.rings.finite_rings
            2
            sage: L.degree_over()                                                       # needs sage.rings.finite_rings
            3

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: K.degree_over(GF(5))                                                  # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5"""
    @overload
    def degree_over(self, F) -> Any:
        """RingExtension_generic.degree_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1414)

        Return the degree of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: K.degree_over(F)
            2
            sage: L.degree_over(K)
            3
            sage: L.degree_over(F)
            6

        If ``base`` is omitted, the degree is computed over the base
        of the extension::

            sage: K.degree_over()                                                       # needs sage.rings.finite_rings
            2
            sage: L.degree_over()                                                       # needs sage.rings.finite_rings
            3

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: K.degree_over(GF(5))                                                  # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5"""
    @overload
    def degree_over(self, K) -> Any:
        """RingExtension_generic.degree_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1414)

        Return the degree of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: K.degree_over(F)
            2
            sage: L.degree_over(K)
            3
            sage: L.degree_over(F)
            6

        If ``base`` is omitted, the degree is computed over the base
        of the extension::

            sage: K.degree_over()                                                       # needs sage.rings.finite_rings
            2
            sage: L.degree_over()                                                       # needs sage.rings.finite_rings
            3

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: K.degree_over(GF(5))                                                  # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5"""
    @overload
    def degree_over(self, F) -> Any:
        """RingExtension_generic.degree_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1414)

        Return the degree of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: K.degree_over(F)
            2
            sage: L.degree_over(K)
            3
            sage: L.degree_over(F)
            6

        If ``base`` is omitted, the degree is computed over the base
        of the extension::

            sage: K.degree_over()                                                       # needs sage.rings.finite_rings
            2
            sage: L.degree_over()                                                       # needs sage.rings.finite_rings
            3

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: K.degree_over(GF(5))                                                  # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5"""
    @overload
    def degree_over(self) -> Any:
        """RingExtension_generic.degree_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1414)

        Return the degree of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: K.degree_over(F)
            2
            sage: L.degree_over(K)
            3
            sage: L.degree_over(F)
            6

        If ``base`` is omitted, the degree is computed over the base
        of the extension::

            sage: K.degree_over()                                                       # needs sage.rings.finite_rings
            2
            sage: L.degree_over()                                                       # needs sage.rings.finite_rings
            3

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: K.degree_over(GF(5))                                                  # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5"""
    @overload
    def degree_over(self) -> Any:
        """RingExtension_generic.degree_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1414)

        Return the degree of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: F = GF(5^2)
            sage: K = GF(5^4).over(F)
            sage: L = GF(5^12).over(K)
            sage: K.degree_over(F)
            2
            sage: L.degree_over(K)
            3
            sage: L.degree_over(F)
            6

        If ``base`` is omitted, the degree is computed over the base
        of the extension::

            sage: K.degree_over()                                                       # needs sage.rings.finite_rings
            2
            sage: L.degree_over()                                                       # needs sage.rings.finite_rings
            3

        Note that ``base`` must be an explicit base over which the
        extension has been defined (as listed by the method :meth:`bases`)::

            sage: K.degree_over(GF(5))                                                  # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: not (explicitly) defined over Finite Field of size 5"""
    def fraction_field(self, extend_base=...) -> Any:
        """RingExtension_generic.fraction_field(self, extend_base=False)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1702)

        Return the fraction field of this extension.

        INPUT:

        - ``extend_base`` -- boolean (default: ``False``)

        If ``extend_base`` is ``False``, the fraction field of the
        extension `L/K` is defined as `\\textrm{Frac}(L)/L/K`, except
        if `L` is already a field in which base the fraction field
        of `L/K` is `L/K` itself.

        If ``extend_base`` is ``True``, the fraction field of the
        extension `L/K` is defined as `\\textrm{Frac}(L)/\\textrm{Frac}(K)`
        (provided that the defining morphism extends to the fraction
        fields, i.e. is injective).

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: A.<a> = ZZ.extension(x^2 - 5)
            sage: OK = A.over()   # over ZZ
            sage: OK
            Order of conductor 2 generated by a in Number Field in a
             with defining polynomial x^2 - 5 over its base
            sage: K1 = OK.fraction_field(); K1
            Fraction Field of Order of conductor 2 generated by a
             in Number Field in a with defining polynomial x^2 - 5 over its base
            sage: K1.bases()
            [Fraction Field of Order of conductor 2 generated by a
             in Number Field in a with defining polynomial x^2 - 5 over its base,
             Order of conductor 2 generated by a in Number Field in a
             with defining polynomial x^2 - 5 over its base,
             Integer Ring]
            sage: K2 = OK.fraction_field(extend_base=True); K2
            Fraction Field of Order of conductor 2 generated by a
             in Number Field in a with defining polynomial x^2 - 5 over its base
            sage: K2.bases()
            [Fraction Field of Order of conductor 2 generated by a
             in Number Field in a with defining polynomial x^2 - 5 over its base,
             Rational Field]

        Note that there is no coercion between `K_1` and `K_2`::

            sage: K1.has_coerce_map_from(K2)                                            # needs sage.rings.number_field
            False
            sage: K2.has_coerce_map_from(K1)                                            # needs sage.rings.number_field
            False

        We check that when the extension is a field, its fraction field does not change::

            sage: K1.fraction_field() is K1                                             # needs sage.rings.number_field
            True
            sage: K2.fraction_field() is K2                                             # needs sage.rings.number_field
            True

        TESTS::

            sage: A = GF(5).over(ZZ)
            sage: A.fraction_field(extend_base=True)
            Traceback (most recent call last):
            ...
            ValueError: the morphism is not injective"""
    @overload
    def from_base_ring(self, r) -> Any:
        """RingExtension_generic.from_base_ring(self, r)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 755)

        Return the canonical embedding of ``r`` into this extension.

        INPUT:

        - ``r`` -- an element of the base of the ring of this extension

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k = GF(5)
            sage: K.<u> = GF(5^2).over(k)
            sage: L.<v> = GF(5^4).over(K)
            sage: x = L.from_base_ring(k(2)); x
            2
            sage: x.parent()
            Field in v with defining polynomial x^2 + (3 - u)*x + u over its base
            sage: x = L.from_base_ring(u); x
            u
            sage: x.parent()
            Field in v with defining polynomial x^2 + (3 - u)*x + u over its base"""
    @overload
    def from_base_ring(self, u) -> Any:
        """RingExtension_generic.from_base_ring(self, r)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 755)

        Return the canonical embedding of ``r`` into this extension.

        INPUT:

        - ``r`` -- an element of the base of the ring of this extension

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: k = GF(5)
            sage: K.<u> = GF(5^2).over(k)
            sage: L.<v> = GF(5^4).over(K)
            sage: x = L.from_base_ring(k(2)); x
            2
            sage: x.parent()
            Field in v with defining polynomial x^2 + (3 - u)*x + u over its base
            sage: x = L.from_base_ring(u); x
            u
            sage: x.parent()
            Field in v with defining polynomial x^2 + (3 - u)*x + u over its base"""
    @overload
    def gen(self) -> Any:
        """RingExtension_generic.gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1377)

        Return the first generator of this extension.

        EXAMPLES::

            sage: K = GF(5^2).over()   # over GF(5)                                     # needs sage.rings.finite_rings
            sage: x = K.gen(); x                                                        # needs sage.rings.finite_rings
            z2

        Observe that the generator lives in the extension::

            sage: x.parent()                                                            # needs sage.rings.finite_rings
            Field in z2 with defining polynomial x^2 + 4*x + 2 over its base
            sage: x.parent() is K                                                       # needs sage.rings.finite_rings
            True"""
    @overload
    def gen(self) -> Any:
        """RingExtension_generic.gen(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1377)

        Return the first generator of this extension.

        EXAMPLES::

            sage: K = GF(5^2).over()   # over GF(5)                                     # needs sage.rings.finite_rings
            sage: x = K.gen(); x                                                        # needs sage.rings.finite_rings
            z2

        Observe that the generator lives in the extension::

            sage: x.parent()                                                            # needs sage.rings.finite_rings
            Field in z2 with defining polynomial x^2 + 4*x + 2 over its base
            sage: x.parent() is K                                                       # needs sage.rings.finite_rings
            True"""
    @overload
    def gens(self, base=...) -> tuple:
        """RingExtension_generic.gens(self, base=None) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1319)

        Return the generators of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``); if omitted,
          use the base of this extension

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()  # over GF(5)
            sage: K.gens()
            (a,)
            sage: L.<b> = GF(5^4).over(K)
            sage: L.gens()
            (b,)
            sage: L.gens(GF(5))
            (b, a)

            sage: S.<x> = QQ[]
            sage: T.<y> = S[]
            sage: T.over(S).gens()
            (y,)
            sage: T.over(QQ).gens()
            (y, x)"""
    @overload
    def gens(self) -> Any:
        """RingExtension_generic.gens(self, base=None) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1319)

        Return the generators of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``); if omitted,
          use the base of this extension

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()  # over GF(5)
            sage: K.gens()
            (a,)
            sage: L.<b> = GF(5^4).over(K)
            sage: L.gens()
            (b,)
            sage: L.gens(GF(5))
            (b, a)

            sage: S.<x> = QQ[]
            sage: T.<y> = S[]
            sage: T.over(S).gens()
            (y,)
            sage: T.over(QQ).gens()
            (y, x)"""
    @overload
    def gens(self) -> Any:
        """RingExtension_generic.gens(self, base=None) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1319)

        Return the generators of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``); if omitted,
          use the base of this extension

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()  # over GF(5)
            sage: K.gens()
            (a,)
            sage: L.<b> = GF(5^4).over(K)
            sage: L.gens()
            (b,)
            sage: L.gens(GF(5))
            (b, a)

            sage: S.<x> = QQ[]
            sage: T.<y> = S[]
            sage: T.over(S).gens()
            (y,)
            sage: T.over(QQ).gens()
            (y, x)"""
    @overload
    def gens(self) -> Any:
        """RingExtension_generic.gens(self, base=None) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1319)

        Return the generators of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``); if omitted,
          use the base of this extension

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()  # over GF(5)
            sage: K.gens()
            (a,)
            sage: L.<b> = GF(5^4).over(K)
            sage: L.gens()
            (b,)
            sage: L.gens(GF(5))
            (b, a)

            sage: S.<x> = QQ[]
            sage: T.<y> = S[]
            sage: T.over(S).gens()
            (y,)
            sage: T.over(QQ).gens()
            (y, x)"""
    @overload
    def gens(self) -> Any:
        """RingExtension_generic.gens(self, base=None) -> tuple

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1319)

        Return the generators of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``); if omitted,
          use the base of this extension

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<a> = GF(5^2).over()  # over GF(5)
            sage: K.gens()
            (a,)
            sage: L.<b> = GF(5^4).over(K)
            sage: L.gens()
            (b,)
            sage: L.gens(GF(5))
            (b, a)

            sage: S.<x> = QQ[]
            sage: T.<y> = S[]
            sage: T.over(S).gens()
            (y,)
            sage: T.over(QQ).gens()
            (y, x)"""
    def hom(self, im_gens, codomain=..., base_map=..., category=..., check=...) -> Any:
        """RingExtension_generic.hom(self, im_gens, codomain=None, base_map=None, category=None, check=True)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1845)

        Return the unique homomorphism from this extension to
        ``codomain`` that sends ``self.gens()`` to the entries
        of ``im_gens`` and induces the map ``base_map`` on the
        base ring.

        INPUT:

        - ``im_gens`` -- the images of the generators of this extension

        - ``codomain`` -- the codomain of the homomorphism; if omitted, it
          is set to the smallest parent containing all the entries of ``im_gens``

        - ``base_map`` -- a map from one of the bases of this extension into
          something that coerces into the codomain; if omitted, coercion maps
          are used

        - ``category`` -- the category of the resulting morphism

        - ``check`` -- boolean (default: ``True``); whether to verify that the
          images of generators extend to define a map (using only canonical coercions)

        EXAMPLES::

            sage: K.<a> = GF(5^2).over()    # over GF(5)                                # needs sage.rings.finite_rings
            sage: L.<b> = GF(5^6).over(K)                                               # needs sage.rings.finite_rings

        We define (by hand) the relative Frobenius endomorphism of the extension `L/K`::

            sage: L.hom([b^25])                                                         # needs sage.rings.finite_rings
            Ring endomorphism of
             Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: b |--> 2 + 2*a*b + (2 - a)*b^2

        Defining the absolute Frobenius of `L` is a bit more complicated
        because it is not a homomorphism of `K`-algebras.
        For this reason, the construction ``L.hom([b^5])`` fails::

            sage: L.hom([b^5])                                                          # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ValueError: images do not define a valid homomorphism

        What we need is to specify a base map::

            sage: FrobK = K.hom([a^5])                                                  # needs sage.rings.finite_rings
            sage: FrobL = L.hom([b^5], base_map=FrobK); FrobL                           # needs sage.rings.finite_rings
            Ring endomorphism of
             Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: b |--> (-1 + a) + (1 + 2*a)*b + a*b^2
                    with map on base ring:
                    a |--> 1 - a

        As a shortcut, we may use the following construction::

            sage: phi = L.hom([b^5, a^5]); phi                                          # needs sage.rings.finite_rings
            Ring endomorphism of
             Field in b with defining polynomial x^3 + (2 + 2*a)*x - a over its base
              Defn: b |--> (-1 + a) + (1 + 2*a)*b + a*b^2
                    with map on base ring:
                    a |--> 1 - a
            sage: phi == FrobL                                                          # needs sage.rings.finite_rings
            True"""
    @overload
    def is_defined_over(self, base) -> Any:
        """RingExtension_generic.is_defined_over(self, base)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1161)

        Return whether or not ``base`` is one of the bases of this
        extension.

        INPUT:

        - ``base`` -- a commutative ring, which might be itself an
          extension

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A = GF(5^4).over(GF(5^2))
            sage: B = GF(5^12).over(A)
            sage: A.is_defined_over(GF(5^2))
            True
            sage: A.is_defined_over(GF(5))
            False

            sage: # needs sage.rings.finite_rings
            sage: B.is_defined_over(A)
            True
            sage: B.is_defined_over(GF(5^4))
            True
            sage: B.is_defined_over(GF(5^2))
            True
            sage: B.is_defined_over(GF(5))
            False

        Note that an extension is defined over itself::

            sage: A.is_defined_over(A)                                                  # needs sage.rings.finite_rings
            True
            sage: A.is_defined_over(GF(5^4))                                            # needs sage.rings.finite_rings
            True

        .. SEEALSO::

            :meth:`base`, :meth:`bases`, :meth:`absolute_base`"""
    @overload
    def is_defined_over(self, A) -> Any:
        """RingExtension_generic.is_defined_over(self, base)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1161)

        Return whether or not ``base`` is one of the bases of this
        extension.

        INPUT:

        - ``base`` -- a commutative ring, which might be itself an
          extension

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A = GF(5^4).over(GF(5^2))
            sage: B = GF(5^12).over(A)
            sage: A.is_defined_over(GF(5^2))
            True
            sage: A.is_defined_over(GF(5))
            False

            sage: # needs sage.rings.finite_rings
            sage: B.is_defined_over(A)
            True
            sage: B.is_defined_over(GF(5^4))
            True
            sage: B.is_defined_over(GF(5^2))
            True
            sage: B.is_defined_over(GF(5))
            False

        Note that an extension is defined over itself::

            sage: A.is_defined_over(A)                                                  # needs sage.rings.finite_rings
            True
            sage: A.is_defined_over(GF(5^4))                                            # needs sage.rings.finite_rings
            True

        .. SEEALSO::

            :meth:`base`, :meth:`bases`, :meth:`absolute_base`"""
    @overload
    def is_defined_over(self, A) -> Any:
        """RingExtension_generic.is_defined_over(self, base)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1161)

        Return whether or not ``base`` is one of the bases of this
        extension.

        INPUT:

        - ``base`` -- a commutative ring, which might be itself an
          extension

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A = GF(5^4).over(GF(5^2))
            sage: B = GF(5^12).over(A)
            sage: A.is_defined_over(GF(5^2))
            True
            sage: A.is_defined_over(GF(5))
            False

            sage: # needs sage.rings.finite_rings
            sage: B.is_defined_over(A)
            True
            sage: B.is_defined_over(GF(5^4))
            True
            sage: B.is_defined_over(GF(5^2))
            True
            sage: B.is_defined_over(GF(5))
            False

        Note that an extension is defined over itself::

            sage: A.is_defined_over(A)                                                  # needs sage.rings.finite_rings
            True
            sage: A.is_defined_over(GF(5^4))                                            # needs sage.rings.finite_rings
            True

        .. SEEALSO::

            :meth:`base`, :meth:`bases`, :meth:`absolute_base`"""
    @overload
    def is_field(self, proof=...) -> Any:
        """RingExtension_generic.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1677)

        Return whether or not this extension is a field.

        INPUT:

        - ``proof`` -- boolean (default: ``False``)

        EXAMPLES::

            sage: K = GF(5^5).over()  # over GF(5)                                      # needs sage.rings.finite_rings
            sage: K.is_field()                                                          # needs sage.rings.finite_rings
            True

            sage: S.<x> = QQ[]
            sage: A = S.over(QQ)
            sage: A.is_field()
            False

            sage: B = A.fraction_field()
            sage: B.is_field()
            True"""
    @overload
    def is_field(self) -> Any:
        """RingExtension_generic.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1677)

        Return whether or not this extension is a field.

        INPUT:

        - ``proof`` -- boolean (default: ``False``)

        EXAMPLES::

            sage: K = GF(5^5).over()  # over GF(5)                                      # needs sage.rings.finite_rings
            sage: K.is_field()                                                          # needs sage.rings.finite_rings
            True

            sage: S.<x> = QQ[]
            sage: A = S.over(QQ)
            sage: A.is_field()
            False

            sage: B = A.fraction_field()
            sage: B.is_field()
            True"""
    @overload
    def is_field(self) -> Any:
        """RingExtension_generic.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1677)

        Return whether or not this extension is a field.

        INPUT:

        - ``proof`` -- boolean (default: ``False``)

        EXAMPLES::

            sage: K = GF(5^5).over()  # over GF(5)                                      # needs sage.rings.finite_rings
            sage: K.is_field()                                                          # needs sage.rings.finite_rings
            True

            sage: S.<x> = QQ[]
            sage: A = S.over(QQ)
            sage: A.is_field()
            False

            sage: B = A.fraction_field()
            sage: B.is_field()
            True"""
    @overload
    def is_field(self) -> Any:
        """RingExtension_generic.is_field(self, proof=True)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1677)

        Return whether or not this extension is a field.

        INPUT:

        - ``proof`` -- boolean (default: ``False``)

        EXAMPLES::

            sage: K = GF(5^5).over()  # over GF(5)                                      # needs sage.rings.finite_rings
            sage: K.is_field()                                                          # needs sage.rings.finite_rings
            True

            sage: S.<x> = QQ[]
            sage: A = S.over(QQ)
            sage: A.is_field()
            False

            sage: B = A.fraction_field()
            sage: B.is_field()
            True"""
    @overload
    def is_finite_over(self, base=...) -> Any:
        """RingExtension_generic.is_finite_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1552)

        Return whether or not this extension is finite over ``base`` (as a module).

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^2).over()  # over GF(5)
            sage: L = GF(5^4).over(K)
            sage: L.is_finite_over(K)
            True
            sage: L.is_finite_over(GF(5))
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: L.is_finite_over()                                                    # needs sage.rings.finite_rings
            True"""
    @overload
    def is_finite_over(self, K) -> Any:
        """RingExtension_generic.is_finite_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1552)

        Return whether or not this extension is finite over ``base`` (as a module).

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^2).over()  # over GF(5)
            sage: L = GF(5^4).over(K)
            sage: L.is_finite_over(K)
            True
            sage: L.is_finite_over(GF(5))
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: L.is_finite_over()                                                    # needs sage.rings.finite_rings
            True"""
    @overload
    def is_finite_over(self) -> Any:
        """RingExtension_generic.is_finite_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1552)

        Return whether or not this extension is finite over ``base`` (as a module).

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^2).over()  # over GF(5)
            sage: L = GF(5^4).over(K)
            sage: L.is_finite_over(K)
            True
            sage: L.is_finite_over(GF(5))
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: L.is_finite_over()                                                    # needs sage.rings.finite_rings
            True"""
    @overload
    def is_free_over(self, base=...) -> Any:
        """RingExtension_generic.is_free_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1614)

        Return ``True`` if this extension is free (as a module)
        over ``base``

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^2).over()  # over GF(5)
            sage: L = GF(5^4).over(K)
            sage: L.is_free_over(K)
            True
            sage: L.is_free_over(GF(5))
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: L.is_free_over()                                                      # needs sage.rings.finite_rings
            True"""
    @overload
    def is_free_over(self, K) -> Any:
        """RingExtension_generic.is_free_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1614)

        Return ``True`` if this extension is free (as a module)
        over ``base``

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^2).over()  # over GF(5)
            sage: L = GF(5^4).over(K)
            sage: L.is_free_over(K)
            True
            sage: L.is_free_over(GF(5))
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: L.is_free_over()                                                      # needs sage.rings.finite_rings
            True"""
    @overload
    def is_free_over(self) -> Any:
        """RingExtension_generic.is_free_over(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1614)

        Return ``True`` if this extension is free (as a module)
        over ``base``

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^2).over()  # over GF(5)
            sage: L = GF(5^4).over(K)
            sage: L.is_free_over(K)
            True
            sage: L.is_free_over(GF(5))
            True

        If ``base`` is omitted, it is set to its default which is the
        base of the extension::

            sage: L.is_free_over()                                                      # needs sage.rings.finite_rings
            True"""
    @overload
    def ngens(self, base=...) -> Any:
        """RingExtension_generic.ngens(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1352)

        Return the number of generators of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^2).over()   # over GF(5)
            sage: K.gens()
            (z2,)
            sage: K.ngens()
            1
            sage: L = GF(5^4).over(K)
            sage: L.gens(GF(5))
            (z4, z2)
            sage: L.ngens(GF(5))
            2"""
    @overload
    def ngens(self) -> Any:
        """RingExtension_generic.ngens(self, base=None)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1352)

        Return the number of generators of this extension over ``base``.

        INPUT:

        - ``base`` -- a commutative ring (which might be itself an
          extension) or ``None`` (default: ``None``)

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^2).over()   # over GF(5)
            sage: K.gens()
            (z2,)
            sage: K.ngens()
            1
            sage: L = GF(5^4).over(K)
            sage: L.gens(GF(5))
            (z4, z2)
            sage: L.ngens(GF(5))
            2"""
    @overload
    def print_options(self, **options) -> Any:
        """RingExtension_generic.print_options(self, **options)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 782)

        Update the printing options of this extension.

        INPUT:

        - ``over`` -- integer or ``Infinity`` (default: ``0``); the maximum
          number of bases included in the printing of this extension

        - ``base`` -- a base over which this extension is finite free;
          elements in this extension will be printed as a linear
          combinaison of a basis of this extension over the given base

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<a> = GF(5^2).over()   # over GF(5)
            sage: B.<b> = GF(5^4).over(A)
            sage: C.<c> = GF(5^12).over(B)
            sage: D.<d> = GF(5^24).over(C)

        Observe what happens when we modify the option ``over``::

            sage: # needs sage.rings.finite_rings
            sage: D
            Field in d with defining polynomial
             x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over its base
            sage: D.print_options(over=2)
            sage: D
            Field in d with defining polynomial x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over
            Field in c with defining polynomial x^3 + (1 + (2 - a)*b)*x^2 + (2 + 2*b)*x - b over
            Field in b with defining polynomial x^2 + (3 - a)*x + a over its base
            sage: D.print_options(over=Infinity)
            sage: D
            Field in d with defining polynomial x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over
            Field in c with defining polynomial x^3 + (1 + (2 - a)*b)*x^2 + (2 + 2*b)*x - b over
            Field in b with defining polynomial x^2 + (3 - a)*x + a over
            Field in a with defining polynomial x^2 + 4*x + 2 over
            Finite Field of size 5

        Now the option ``base``::

            sage: # needs sage.rings.finite_rings
            sage: d^2
            -c + ((-1 + a) + ((-1 + 3*a) + b)*c + ((3 - a) + (-1 + a)*b)*c^2)*d
            sage: D.basis_over(B)
            [1, c, c^2, d, c*d, c^2*d]
            sage: D.print_options(base=B)
            sage: d^2
            -c + (-1 + a)*d + ((-1 + 3*a) + b)*c*d + ((3 - a) + (-1 + a)*b)*c^2*d
            sage: D.basis_over(A)
            [1, b, c, b*c, c^2, b*c^2, d, b*d, c*d, b*c*d, c^2*d, b*c^2*d]
            sage: D.print_options(base=A)
            sage: d^2
            -c + (-1 + a)*d + (-1 + 3*a)*c*d + b*c*d + (3 - a)*c^2*d + (-1 + a)*b*c^2*d"""
    @overload
    def print_options(self, over=...) -> Any:
        """RingExtension_generic.print_options(self, **options)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 782)

        Update the printing options of this extension.

        INPUT:

        - ``over`` -- integer or ``Infinity`` (default: ``0``); the maximum
          number of bases included in the printing of this extension

        - ``base`` -- a base over which this extension is finite free;
          elements in this extension will be printed as a linear
          combinaison of a basis of this extension over the given base

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<a> = GF(5^2).over()   # over GF(5)
            sage: B.<b> = GF(5^4).over(A)
            sage: C.<c> = GF(5^12).over(B)
            sage: D.<d> = GF(5^24).over(C)

        Observe what happens when we modify the option ``over``::

            sage: # needs sage.rings.finite_rings
            sage: D
            Field in d with defining polynomial
             x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over its base
            sage: D.print_options(over=2)
            sage: D
            Field in d with defining polynomial x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over
            Field in c with defining polynomial x^3 + (1 + (2 - a)*b)*x^2 + (2 + 2*b)*x - b over
            Field in b with defining polynomial x^2 + (3 - a)*x + a over its base
            sage: D.print_options(over=Infinity)
            sage: D
            Field in d with defining polynomial x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over
            Field in c with defining polynomial x^3 + (1 + (2 - a)*b)*x^2 + (2 + 2*b)*x - b over
            Field in b with defining polynomial x^2 + (3 - a)*x + a over
            Field in a with defining polynomial x^2 + 4*x + 2 over
            Finite Field of size 5

        Now the option ``base``::

            sage: # needs sage.rings.finite_rings
            sage: d^2
            -c + ((-1 + a) + ((-1 + 3*a) + b)*c + ((3 - a) + (-1 + a)*b)*c^2)*d
            sage: D.basis_over(B)
            [1, c, c^2, d, c*d, c^2*d]
            sage: D.print_options(base=B)
            sage: d^2
            -c + (-1 + a)*d + ((-1 + 3*a) + b)*c*d + ((3 - a) + (-1 + a)*b)*c^2*d
            sage: D.basis_over(A)
            [1, b, c, b*c, c^2, b*c^2, d, b*d, c*d, b*c*d, c^2*d, b*c^2*d]
            sage: D.print_options(base=A)
            sage: d^2
            -c + (-1 + a)*d + (-1 + 3*a)*c*d + b*c*d + (3 - a)*c^2*d + (-1 + a)*b*c^2*d"""
    @overload
    def print_options(self, over=...) -> Any:
        """RingExtension_generic.print_options(self, **options)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 782)

        Update the printing options of this extension.

        INPUT:

        - ``over`` -- integer or ``Infinity`` (default: ``0``); the maximum
          number of bases included in the printing of this extension

        - ``base`` -- a base over which this extension is finite free;
          elements in this extension will be printed as a linear
          combinaison of a basis of this extension over the given base

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<a> = GF(5^2).over()   # over GF(5)
            sage: B.<b> = GF(5^4).over(A)
            sage: C.<c> = GF(5^12).over(B)
            sage: D.<d> = GF(5^24).over(C)

        Observe what happens when we modify the option ``over``::

            sage: # needs sage.rings.finite_rings
            sage: D
            Field in d with defining polynomial
             x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over its base
            sage: D.print_options(over=2)
            sage: D
            Field in d with defining polynomial x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over
            Field in c with defining polynomial x^3 + (1 + (2 - a)*b)*x^2 + (2 + 2*b)*x - b over
            Field in b with defining polynomial x^2 + (3 - a)*x + a over its base
            sage: D.print_options(over=Infinity)
            sage: D
            Field in d with defining polynomial x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over
            Field in c with defining polynomial x^3 + (1 + (2 - a)*b)*x^2 + (2 + 2*b)*x - b over
            Field in b with defining polynomial x^2 + (3 - a)*x + a over
            Field in a with defining polynomial x^2 + 4*x + 2 over
            Finite Field of size 5

        Now the option ``base``::

            sage: # needs sage.rings.finite_rings
            sage: d^2
            -c + ((-1 + a) + ((-1 + 3*a) + b)*c + ((3 - a) + (-1 + a)*b)*c^2)*d
            sage: D.basis_over(B)
            [1, c, c^2, d, c*d, c^2*d]
            sage: D.print_options(base=B)
            sage: d^2
            -c + (-1 + a)*d + ((-1 + 3*a) + b)*c*d + ((3 - a) + (-1 + a)*b)*c^2*d
            sage: D.basis_over(A)
            [1, b, c, b*c, c^2, b*c^2, d, b*d, c*d, b*c*d, c^2*d, b*c^2*d]
            sage: D.print_options(base=A)
            sage: d^2
            -c + (-1 + a)*d + (-1 + 3*a)*c*d + b*c*d + (3 - a)*c^2*d + (-1 + a)*b*c^2*d"""
    @overload
    def print_options(self, base=...) -> Any:
        """RingExtension_generic.print_options(self, **options)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 782)

        Update the printing options of this extension.

        INPUT:

        - ``over`` -- integer or ``Infinity`` (default: ``0``); the maximum
          number of bases included in the printing of this extension

        - ``base`` -- a base over which this extension is finite free;
          elements in this extension will be printed as a linear
          combinaison of a basis of this extension over the given base

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<a> = GF(5^2).over()   # over GF(5)
            sage: B.<b> = GF(5^4).over(A)
            sage: C.<c> = GF(5^12).over(B)
            sage: D.<d> = GF(5^24).over(C)

        Observe what happens when we modify the option ``over``::

            sage: # needs sage.rings.finite_rings
            sage: D
            Field in d with defining polynomial
             x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over its base
            sage: D.print_options(over=2)
            sage: D
            Field in d with defining polynomial x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over
            Field in c with defining polynomial x^3 + (1 + (2 - a)*b)*x^2 + (2 + 2*b)*x - b over
            Field in b with defining polynomial x^2 + (3 - a)*x + a over its base
            sage: D.print_options(over=Infinity)
            sage: D
            Field in d with defining polynomial x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over
            Field in c with defining polynomial x^3 + (1 + (2 - a)*b)*x^2 + (2 + 2*b)*x - b over
            Field in b with defining polynomial x^2 + (3 - a)*x + a over
            Field in a with defining polynomial x^2 + 4*x + 2 over
            Finite Field of size 5

        Now the option ``base``::

            sage: # needs sage.rings.finite_rings
            sage: d^2
            -c + ((-1 + a) + ((-1 + 3*a) + b)*c + ((3 - a) + (-1 + a)*b)*c^2)*d
            sage: D.basis_over(B)
            [1, c, c^2, d, c*d, c^2*d]
            sage: D.print_options(base=B)
            sage: d^2
            -c + (-1 + a)*d + ((-1 + 3*a) + b)*c*d + ((3 - a) + (-1 + a)*b)*c^2*d
            sage: D.basis_over(A)
            [1, b, c, b*c, c^2, b*c^2, d, b*d, c*d, b*c*d, c^2*d, b*c^2*d]
            sage: D.print_options(base=A)
            sage: d^2
            -c + (-1 + a)*d + (-1 + 3*a)*c*d + b*c*d + (3 - a)*c^2*d + (-1 + a)*b*c^2*d"""
    @overload
    def print_options(self, base=...) -> Any:
        """RingExtension_generic.print_options(self, **options)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 782)

        Update the printing options of this extension.

        INPUT:

        - ``over`` -- integer or ``Infinity`` (default: ``0``); the maximum
          number of bases included in the printing of this extension

        - ``base`` -- a base over which this extension is finite free;
          elements in this extension will be printed as a linear
          combinaison of a basis of this extension over the given base

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: A.<a> = GF(5^2).over()   # over GF(5)
            sage: B.<b> = GF(5^4).over(A)
            sage: C.<c> = GF(5^12).over(B)
            sage: D.<d> = GF(5^24).over(C)

        Observe what happens when we modify the option ``over``::

            sage: # needs sage.rings.finite_rings
            sage: D
            Field in d with defining polynomial
             x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over its base
            sage: D.print_options(over=2)
            sage: D
            Field in d with defining polynomial x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over
            Field in c with defining polynomial x^3 + (1 + (2 - a)*b)*x^2 + (2 + 2*b)*x - b over
            Field in b with defining polynomial x^2 + (3 - a)*x + a over its base
            sage: D.print_options(over=Infinity)
            sage: D
            Field in d with defining polynomial x^2 + ((1 - a) + ((1 + 2*a) - b)*c + ((2 + a) + (1 - a)*b)*c^2)*x + c over
            Field in c with defining polynomial x^3 + (1 + (2 - a)*b)*x^2 + (2 + 2*b)*x - b over
            Field in b with defining polynomial x^2 + (3 - a)*x + a over
            Field in a with defining polynomial x^2 + 4*x + 2 over
            Finite Field of size 5

        Now the option ``base``::

            sage: # needs sage.rings.finite_rings
            sage: d^2
            -c + ((-1 + a) + ((-1 + 3*a) + b)*c + ((3 - a) + (-1 + a)*b)*c^2)*d
            sage: D.basis_over(B)
            [1, c, c^2, d, c*d, c^2*d]
            sage: D.print_options(base=B)
            sage: d^2
            -c + (-1 + a)*d + ((-1 + 3*a) + b)*c*d + ((3 - a) + (-1 + a)*b)*c^2*d
            sage: D.basis_over(A)
            [1, b, c, b*c, c^2, b*c^2, d, b*d, c*d, b*c*d, c^2*d, b*c^2*d]
            sage: D.print_options(base=A)
            sage: d^2
            -c + (-1 + a)*d + (-1 + 3*a)*c*d + b*c*d + (3 - a)*c^2*d + (-1 + a)*b*c^2*d"""
    @overload
    def random_element(self) -> Any:
        """RingExtension_generic.random_element(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1396)

        Return a random element in this extension.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^2).over()   # over GF(5)
            sage: x = K.random_element(); x   # random
            3 + z2
            sage: x.parent()
            Field in z2 with defining polynomial x^2 + 4*x + 2 over its base
            sage: x.parent() is K
            True"""
    @overload
    def random_element(self) -> Any:
        """RingExtension_generic.random_element(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1396)

        Return a random element in this extension.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K = GF(5^2).over()   # over GF(5)
            sage: x = K.random_element(); x   # random
            3 + z2
            sage: x.parent()
            Field in z2 with defining polynomial x^2 + 4*x + 2 over its base
            sage: x.parent() is K
            True"""
    @overload
    def relative_degree(self) -> Any:
        """RingExtension_generic.relative_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1516)

        Return the degree of this extension over its base.

        EXAMPLES::

            sage: A = GF(5^4).over(GF(5^2))                                             # needs sage.rings.finite_rings
            sage: A.relative_degree()                                                   # needs sage.rings.finite_rings
            2

        .. SEEALSO::

            :meth:`degree`, :meth:`absolute_degree`"""
    @overload
    def relative_degree(self) -> Any:
        """RingExtension_generic.relative_degree(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 1516)

        Return the degree of this extension over its base.

        EXAMPLES::

            sage: A = GF(5^4).over(GF(5^2))                                             # needs sage.rings.finite_rings
            sage: A.relative_degree()                                                   # needs sage.rings.finite_rings
            2

        .. SEEALSO::

            :meth:`degree`, :meth:`absolute_degree`"""
    def __dir__(self) -> Any:
        """RingExtension_generic.__dir__(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 653)

        Return the list of all the attributes of this extension;
        if the extension was created with ``import_methods = True``,
        concatenate this list with the list of all the methods of
        the backend parent.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: A.<a> = QQ.extension(x^2 - 2)                                         # needs sage.rings.number_field
            sage: K.<a> = A.over()                                                      # needs sage.rings.number_field

            sage: dir(K)                                                                # needs sage.rings.number_field
            ['CartesianProduct',
             'Element',
             'Hom',
             ...
             'zeta',
             'zeta_coefficients',
             'zeta_function',
             'zeta_order']"""
    def __hash__(self) -> Any:
        """RingExtension_generic.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 689)

        Return a hash of this extension.

        EXAMPLES:

            sage: E = GF(5^3).over()                                                    # needs sage.rings.finite_rings
            sage: hash(E)   # random                                                    # needs sage.rings.finite_rings
            140257667982632"""
    def __reduce__(self) -> Any:
        """RingExtension_generic.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/rings/ring_extension.pyx (starting at line 701)

        Return a tuple of a function and data that can be used to unpickle this
        extension.

        TESTS::

            sage: K = GF(7^3).over()                                                    # needs sage.rings.finite_rings
            sage: type(K)                                                               # needs sage.rings.finite_rings
            <class 'sage.rings.ring_extension.RingExtensionWithGen'>
            sage: loads(dumps(K)) is K                                                  # needs sage.rings.finite_rings
            True"""
