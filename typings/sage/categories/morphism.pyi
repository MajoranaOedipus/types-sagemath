import _cython_3_2_1
import sage.categories.map
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

is_Morphism: _cython_3_2_1.cython_function_or_method

class CallMorphism(Morphism):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class FormalCoercionMorphism(Morphism):
    """FormalCoercionMorphism(parent)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 452)"""

class IdentityMorphism(Morphism):
    """IdentityMorphism(parent)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 473)"""
    @overload
    def is_identity(self) -> Any:
        """IdentityMorphism.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 512)

        Return ``True`` if this morphism is the identity morphism.

        EXAMPLES::

            sage: E = End(Partitions(5))                                                # needs sage.combinat
            sage: E.identity().is_identity()                                            # needs sage.combinat
            True

        Check that :issue:`15478` is fixed::

            sage: # needs sage.rings.finite_rings
            sage: K.<z> = GF(4)
            sage: phi = End(K)([z^2])
            sage: R.<t> = K[]
            sage: psi = End(R)(phi)
            sage: psi.is_identity()
            False"""
    @overload
    def is_identity(self) -> Any:
        """IdentityMorphism.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 512)

        Return ``True`` if this morphism is the identity morphism.

        EXAMPLES::

            sage: E = End(Partitions(5))                                                # needs sage.combinat
            sage: E.identity().is_identity()                                            # needs sage.combinat
            True

        Check that :issue:`15478` is fixed::

            sage: # needs sage.rings.finite_rings
            sage: K.<z> = GF(4)
            sage: phi = End(K)([z^2])
            sage: R.<t> = K[]
            sage: psi = End(R)(phi)
            sage: psi.is_identity()
            False"""
    @overload
    def is_identity(self) -> Any:
        """IdentityMorphism.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 512)

        Return ``True`` if this morphism is the identity morphism.

        EXAMPLES::

            sage: E = End(Partitions(5))                                                # needs sage.combinat
            sage: E.identity().is_identity()                                            # needs sage.combinat
            True

        Check that :issue:`15478` is fixed::

            sage: # needs sage.rings.finite_rings
            sage: K.<z> = GF(4)
            sage: phi = End(K)([z^2])
            sage: R.<t> = K[]
            sage: psi = End(R)(phi)
            sage: psi.is_identity()
            False"""
    @overload
    def is_injective(self) -> Any:
        """IdentityMorphism.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 557)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: Hom(ZZ, ZZ).identity().is_injective()
            True"""
    @overload
    def is_injective(self) -> Any:
        """IdentityMorphism.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 557)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: Hom(ZZ, ZZ).identity().is_injective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """IdentityMorphism.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 546)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: Hom(ZZ, ZZ).identity().is_surjective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """IdentityMorphism.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 546)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: Hom(ZZ, ZZ).identity().is_surjective()
            True"""
    @overload
    def section(self) -> Any:
        """IdentityMorphism.section(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 534)

        Return a section of this morphism.

        EXAMPLES::

            sage: T = Hom(ZZ, ZZ).identity()
            sage: T.section() is T
            True"""
    @overload
    def section(self) -> Any:
        """IdentityMorphism.section(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 534)

        Return a section of this morphism.

        EXAMPLES::

            sage: T = Hom(ZZ, ZZ).identity()
            sage: T.section() is T
            True"""
    def __invert__(self) -> Any:
        """IdentityMorphism.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 509)"""
    def __mul__(self, left, right) -> Any:
        """IdentityMorphism.__mul__(left, right)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 491)"""
    def __rmul__(self, other):
        """Return value*self."""

class Morphism(sage.categories.map.Map):
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def category(self) -> Any:
        """Morphism.category(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 173)

        Return the category of the parent of this morphism.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: f = R.hom([t**2])
            sage: f.category()
            Category of endsets of unital magmas and right modules over
             (Dedekind domains and euclidean domains
              and noetherian rings
              and infinite enumerated sets and metric spaces)
             and left modules over
             (Dedekind domains and euclidean domains
              and noetherian rings
              and infinite enumerated sets and metric spaces)

            sage: # needs sage.rings.number_field
            sage: K = CyclotomicField(12)
            sage: L = CyclotomicField(132)
            sage: phi = L._internal_coerce_map_from(K)
            sage: phi.category()
            Category of homsets of number fields"""
    @overload
    def category(self) -> Any:
        """Morphism.category(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 173)

        Return the category of the parent of this morphism.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: f = R.hom([t**2])
            sage: f.category()
            Category of endsets of unital magmas and right modules over
             (Dedekind domains and euclidean domains
              and noetherian rings
              and infinite enumerated sets and metric spaces)
             and left modules over
             (Dedekind domains and euclidean domains
              and noetherian rings
              and infinite enumerated sets and metric spaces)

            sage: # needs sage.rings.number_field
            sage: K = CyclotomicField(12)
            sage: L = CyclotomicField(132)
            sage: phi = L._internal_coerce_map_from(K)
            sage: phi.category()
            Category of homsets of number fields"""
    @overload
    def category(self) -> Any:
        """Morphism.category(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 173)

        Return the category of the parent of this morphism.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: f = R.hom([t**2])
            sage: f.category()
            Category of endsets of unital magmas and right modules over
             (Dedekind domains and euclidean domains
              and noetherian rings
              and infinite enumerated sets and metric spaces)
             and left modules over
             (Dedekind domains and euclidean domains
              and noetherian rings
              and infinite enumerated sets and metric spaces)

            sage: # needs sage.rings.number_field
            sage: K = CyclotomicField(12)
            sage: L = CyclotomicField(132)
            sage: phi = L._internal_coerce_map_from(K)
            sage: phi.category()
            Category of homsets of number fields"""
    @overload
    def is_endomorphism(self) -> Any:
        """Morphism.is_endomorphism(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 201)

        Return ``True`` if this morphism is an endomorphism.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: f = R.hom([t])
            sage: f.is_endomorphism()
            True

            sage: # needs sage.rings.number_field
            sage: K = CyclotomicField(12)
            sage: L = CyclotomicField(132)
            sage: phi = L._internal_coerce_map_from(K)
            sage: phi.is_endomorphism()
            False"""
    @overload
    def is_endomorphism(self) -> Any:
        """Morphism.is_endomorphism(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 201)

        Return ``True`` if this morphism is an endomorphism.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: f = R.hom([t])
            sage: f.is_endomorphism()
            True

            sage: # needs sage.rings.number_field
            sage: K = CyclotomicField(12)
            sage: L = CyclotomicField(132)
            sage: phi = L._internal_coerce_map_from(K)
            sage: phi.is_endomorphism()
            False"""
    @overload
    def is_endomorphism(self) -> Any:
        """Morphism.is_endomorphism(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 201)

        Return ``True`` if this morphism is an endomorphism.

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: f = R.hom([t])
            sage: f.is_endomorphism()
            True

            sage: # needs sage.rings.number_field
            sage: K = CyclotomicField(12)
            sage: L = CyclotomicField(132)
            sage: phi = L._internal_coerce_map_from(K)
            sage: phi.is_endomorphism()
            False"""
    @overload
    def is_identity(self) -> Any:
        """Morphism.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 221)

        Return ``True`` if this morphism is the identity morphism.

        .. NOTE::

            Implemented only when the domain has a method gens()

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: f = R.hom([t])
            sage: f.is_identity()
            True
            sage: g = R.hom([t + 1])
            sage: g.is_identity()
            False

        A morphism between two different spaces cannot be the identity::

            sage: R2.<t2> = QQ[]
            sage: h = R.hom([t2])
            sage: h.is_identity()
            False"""
    @overload
    def is_identity(self) -> Any:
        """Morphism.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 221)

        Return ``True`` if this morphism is the identity morphism.

        .. NOTE::

            Implemented only when the domain has a method gens()

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: f = R.hom([t])
            sage: f.is_identity()
            True
            sage: g = R.hom([t + 1])
            sage: g.is_identity()
            False

        A morphism between two different spaces cannot be the identity::

            sage: R2.<t2> = QQ[]
            sage: h = R.hom([t2])
            sage: h.is_identity()
            False"""
    @overload
    def is_identity(self) -> Any:
        """Morphism.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 221)

        Return ``True`` if this morphism is the identity morphism.

        .. NOTE::

            Implemented only when the domain has a method gens()

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: f = R.hom([t])
            sage: f.is_identity()
            True
            sage: g = R.hom([t + 1])
            sage: g.is_identity()
            False

        A morphism between two different spaces cannot be the identity::

            sage: R2.<t2> = QQ[]
            sage: h = R.hom([t2])
            sage: h.is_identity()
            False"""
    @overload
    def is_identity(self) -> Any:
        """Morphism.is_identity(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 221)

        Return ``True`` if this morphism is the identity morphism.

        .. NOTE::

            Implemented only when the domain has a method gens()

        EXAMPLES::

            sage: R.<t> = ZZ[]
            sage: f = R.hom([t])
            sage: f.is_identity()
            True
            sage: g = R.hom([t + 1])
            sage: g.is_identity()
            False

        A morphism between two different spaces cannot be the identity::

            sage: R2.<t2> = QQ[]
            sage: h = R.hom([t2])
            sage: h.is_identity()
            False"""
    def pushforward(self, I) -> Any:
        """Morphism.pushforward(self, I)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 254)"""
    def register_as_coercion(self) -> Any:
        """Morphism.register_as_coercion(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 257)

        Register this morphism as a coercion to Sage's coercion model
        (see :mod:`sage.structure.coerce`).

        EXAMPLES:

        By default, adding polynomials over different variables triggers an error::

            sage: X.<x> = ZZ[]
            sage: Y.<y> = ZZ[]
            sage: x^2 + y
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +:
            'Univariate Polynomial Ring in x over Integer Ring' and
            'Univariate Polynomial Ring in y over Integer Ring'

        Let us declare a coercion from `\\ZZ[x]` to `\\ZZ[z]`::

            sage: Z.<z> = ZZ[]
            sage: phi = Hom(X, Z)(z)
            sage: phi(x^2+1)
            z^2 + 1
            sage: phi.register_as_coercion()

        Now we can add elements from `\\ZZ[x]` and `\\ZZ[z]`, because
        the elements of the former are allowed to be implicitly
        coerced into the later::

            sage: x^2 + z
            z^2 + z

        Caveat: the registration of the coercion must be done before any
        other coercion is registered or discovered::

            sage: phi = Hom(X, Z)(z^2)
            sage: phi.register_as_coercion()
            Traceback (most recent call last):
            ...
            AssertionError: coercion from Univariate Polynomial Ring in x over Integer Ring
            to Univariate Polynomial Ring in z over Integer Ring
            already registered or discovered"""
    def register_as_conversion(self) -> Any:
        """Morphism.register_as_conversion(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 303)

        Register this morphism as a conversion to Sage's coercion model.

        (see :mod:`sage.structure.coerce`).

        EXAMPLES:

        Let us declare a conversion from the symmetric group to `\\ZZ`
        through the sign map::

            sage: # needs sage.groups
            sage: S = SymmetricGroup(4)
            sage: phi = Hom(S, ZZ)(lambda x: ZZ(x.sign()))
            sage: x = S.an_element(); x
            (2,3,4)
            sage: phi(x)
            1
            sage: phi.register_as_conversion()
            sage: ZZ(x)
            1"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __hash__(self) -> Any:
        """Morphism.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 327)

        Return a hash of this morphism.

        It is the hash of the triple (domain, codomain, definition)
        where ``definition`` is:

        - a tuple consisting of the images of the generators
          of the domain if domain has generators

        - the string representation of this morphism otherwise

        AUTHOR:

        - Xavier Caruso (2012-07-09)"""

class SetIsomorphism(SetMorphism):
    """File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 742)

        An isomorphism of sets.

        INPUT:

        - ``parent`` -- a Homset
        - ``function`` -- a Python function that takes elements
          of the domain as input and returns elements of the codomain

        EXAMPLES::

            sage: f = sage.categories.morphism.SetIsomorphism(Hom(ZZ, ZZ, Sets()),
            ....:                                             operator.__neg__); f
            Generic endomorphism of Integer Ring
            sage: f._set_inverse(f)
            sage: ~f is f
            True
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def is_injective(self) -> Any:
        """SetIsomorphism.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 884)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: f = sage.categories.morphism.SetIsomorphism(Hom(ZZ, ZZ, Sets()),
            ....:                                             operator.__neg__)
            sage: f.is_injective()
            True"""
    @overload
    def is_injective(self) -> Any:
        """SetIsomorphism.is_injective(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 884)

        Return whether this morphism is injective.

        EXAMPLES::

            sage: f = sage.categories.morphism.SetIsomorphism(Hom(ZZ, ZZ, Sets()),
            ....:                                             operator.__neg__)
            sage: f.is_injective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """SetIsomorphism.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 871)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: f = sage.categories.morphism.SetIsomorphism(Hom(ZZ, ZZ, Sets()),
            ....:                                             operator.__neg__)
            sage: f.is_surjective()
            True"""
    @overload
    def is_surjective(self) -> Any:
        """SetIsomorphism.is_surjective(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 871)

        Return whether this morphism is surjective.

        EXAMPLES::

            sage: f = sage.categories.morphism.SetIsomorphism(Hom(ZZ, ZZ, Sets()),
            ....:                                             operator.__neg__)
            sage: f.is_surjective()
            True"""
    @overload
    def section(self) -> Any:
        """SetIsomorphism.section(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 857)

        Return a section of this morphism.

        EXAMPLES::

            sage: f = sage.categories.morphism.SetIsomorphism(Hom(ZZ, ZZ, Sets()),
            ....:                                             operator.__neg__)
            sage: f._set_inverse(f)
            sage: f.section() is f
            True"""
    @overload
    def section(self) -> Any:
        """SetIsomorphism.section(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 857)

        Return a section of this morphism.

        EXAMPLES::

            sage: f = sage.categories.morphism.SetIsomorphism(Hom(ZZ, ZZ, Sets()),
            ....:                                             operator.__neg__)
            sage: f._set_inverse(f)
            sage: f.section() is f
            True"""
    def __invert__(self) -> Any:
        """SetIsomorphism.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 779)

        Return the inverse morphism of ``self``.

        If :meth:`_set_inverse` has not been called yet, an error is raised.

        EXAMPLES::

            sage: f = sage.categories.morphism.SetIsomorphism(Hom(ZZ, ZZ, Sets()),
            ....:                                             operator.__neg__)
            sage: ~f
            Traceback (most recent call last):
            ...
            RuntimeError: inverse morphism has not been set
            sage: f._set_inverse(f)
            sage: ~f
            Generic endomorphism of Integer Ring"""

class SetMorphism(Morphism):
    """SetMorphism(parent, function)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, function) -> Any:
        """File: /build/sagemath/src/sage/src/sage/categories/morphism.pyx (starting at line 570)

                INPUT:

                - ``parent`` -- a Homset
                - ``function`` -- a Python function that takes elements
                  of the domain as input and returns elements of the codomain

                EXAMPLES::

                    sage: from sage.categories.morphism import SetMorphism
                    sage: f = SetMorphism(Hom(QQ, ZZ, Sets()), numerator)
                    sage: f.parent()
                    Set of Morphisms from Rational Field to Integer Ring in Category of sets
                    sage: f.domain()
                    Rational Field
                    sage: f.codomain()
                    Integer Ring
                    sage: TestSuite(f).run()
        """
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""
