from _typeshed import Incomplete
from sage.categories.homset import Hom as Hom
from sage.categories.map import Map as Map
from sage.categories.morphism import IdentityMorphism as IdentityMorphism

QQ: Incomplete
IdentityMap = IdentityMorphism

class NumberFieldIsomorphism(Map):
    """
    A base class for various isomorphisms between number fields and
    vector spaces.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^4 + 3*x + 1)
        sage: V, fr, to = K.vector_space()
        sage: isinstance(fr, sage.rings.number_field.maps.NumberFieldIsomorphism)
        True
    """
    def is_injective(self):
        """
        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^4 + 3*x + 1)
            sage: V, fr, to = K.vector_space()
            sage: fr.is_injective()
            True
        """
    def is_surjective(self):
        """
        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^4 + 3*x + 1)
            sage: V, fr, to = K.vector_space()
            sage: fr.is_surjective()
            True
        """

class MapVectorSpaceToNumberField(NumberFieldIsomorphism):
    """
    The map to an absolute number field from its underlying `\\QQ`-vector space.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^4 + 3*x + 1)
        sage: V, fr, to = K.vector_space()
        sage: V
        Vector space of dimension 4 over Rational Field
        sage: fr
        Isomorphism map:
          From: Vector space of dimension 4 over Rational Field
          To:   Number Field in a with defining polynomial x^4 + 3*x + 1
        sage: to
        Isomorphism map:
          From: Number Field in a with defining polynomial x^4 + 3*x + 1
          To:   Vector space of dimension 4 over Rational Field
        sage: type(fr), type(to)
        (<class 'sage.rings.number_field.maps.MapVectorSpaceToNumberField'>,
         <class 'sage.rings.number_field.maps.MapNumberFieldToVectorSpace'>)

        sage: fr.is_injective(), fr.is_surjective()
        (True, True)

        sage: fr.domain(), to.codomain()
        (Vector space of dimension 4 over Rational Field,
         Vector space of dimension 4 over Rational Field)
        sage: to.domain(), fr.codomain()
        (Number Field in a with defining polynomial x^4 + 3*x + 1,
         Number Field in a with defining polynomial x^4 + 3*x + 1)
        sage: fr * to
        Composite map:
          From: Number Field in a with defining polynomial x^4 + 3*x + 1
          To:   Number Field in a with defining polynomial x^4 + 3*x + 1
          Defn:   Isomorphism map:
                  From: Number Field in a with defining polynomial x^4 + 3*x + 1
                  To:   Vector space of dimension 4 over Rational Field
                then
                  Isomorphism map:
                  From: Vector space of dimension 4 over Rational Field
                  To:   Number Field in a with defining polynomial x^4 + 3*x + 1
        sage: to * fr
        Composite map:
          From: Vector space of dimension 4 over Rational Field
          To:   Vector space of dimension 4 over Rational Field
          Defn:   Isomorphism map:
                  From: Vector space of dimension 4 over Rational Field
                  To:   Number Field in a with defining polynomial x^4 + 3*x + 1
                then
                  Isomorphism map:
                  From: Number Field in a with defining polynomial x^4 + 3*x + 1
                  To:   Vector space of dimension 4 over Rational Field

        sage: to(a), to(a + 1)
        ((0, 1, 0, 0), (1, 1, 0, 0))
        sage: fr(to(a)), fr(V([0, 1, 2, 3]))
        (a, 3*a^3 + 2*a^2 + a)
    """
    def __init__(self, V, K) -> None:
        """
        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<c> = NumberField(x^9 + 3)
            sage: V, fr, to = K.vector_space(); fr # indirect doctest
            Isomorphism map:
              From: Vector space of dimension 9 over Rational Field
              To:   Number Field in c with defining polynomial x^9 + 3
            sage: type(fr)
            <class 'sage.rings.number_field.maps.MapVectorSpaceToNumberField'>
        """

class MapNumberFieldToVectorSpace(Map):
    """
    A class for the isomorphism from an absolute number field to its underlying
    `\\QQ`-vector space.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: L.<a> = NumberField(x^3 - x + 1)
        sage: V, fr, to = L.vector_space()
        sage: type(to)
        <class 'sage.rings.number_field.maps.MapNumberFieldToVectorSpace'>
    """
    def __init__(self, K, V) -> None:
        """
        Standard initialisation function.

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: L.<a> = NumberField(x^3 - x + 1)
            sage: L.vector_space()[2] # indirect doctest
            Isomorphism map:
              From: Number Field in a with defining polynomial x^3 - x + 1
              To:   Vector space of dimension 3 over Rational Field
        """

class MapRelativeVectorSpaceToRelativeNumberField(NumberFieldIsomorphism):
    """
    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: L.<b> = NumberField(x^4 + 3*x^2 + 1)
        sage: K = L.relativize(L.subfields(2)[0][1], 'a'); K
        Number Field in a with defining polynomial x^2 - b0*x + 1 over its base field
        sage: V, fr, to = K.relative_vector_space()
        sage: V
        Vector space of dimension 2 over Number Field in b0 with defining polynomial x^2 + 1
        sage: fr
        Isomorphism map:
          From: Vector space of dimension 2
                over Number Field in b0 with defining polynomial x^2 + 1
          To:   Number Field in a
                with defining polynomial x^2 - b0*x + 1 over its base field
        sage: type(fr)
        <class 'sage.rings.number_field.maps.MapRelativeVectorSpaceToRelativeNumberField'>

        sage: a0 = K.gen(); b0 = K.base_field().gen()
        sage: fr(to(a0 + 2*b0)), fr(V([0, 1])), fr(V([b0, 2*b0]))
        (a + 2*b0, a, 2*b0*a + b0)
        sage: (fr * to)(K.gen()) == K.gen()
        True
        sage: (to * fr)(V([1, 2])) == V([1, 2])
        True
    """
    def __init__(self, V, K) -> None:
        """

        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b> = NumberField([x^2 + 1, x^2 - 2])
            sage: V, _, to = K.relative_vector_space(); to # indirect doctest
            Isomorphism map:
              From: Number Field in a with defining polynomial x^2 + 1 over its base field
              To:   Vector space of dimension 2 over Number Field in b with defining polynomial x^2 - 2
        """

class MapRelativeNumberFieldToRelativeVectorSpace(NumberFieldIsomorphism):
    """
    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a, b> = NumberField([x^3 - x + 1, x^2 + 23])
        sage: V, fr, to = K.relative_vector_space()
        sage: type(to)
        <class 'sage.rings.number_field.maps.MapRelativeNumberFieldToRelativeVectorSpace'>
    """
    def __init__(self, K, V) -> None:
        """
        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: L.<b> = NumberField(x^4 + 3*x^2 + 1)
            sage: K = L.relativize(L.subfields(2)[0][1], 'a')
            sage: V, fr, to = K.relative_vector_space()
            sage: to
            Isomorphism map:
              From: Number Field in a with defining polynomial x^2 - b0*x + 1 over its base field
              To:   Vector space of dimension 2 over Number Field in b0 with defining polynomial x^2 + 1
        """

class NameChangeMap(NumberFieldIsomorphism):
    """
    A map between two isomorphic number fields with the same defining
    polynomial but different variable names.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^2 - 3)
        sage: L.<b> = K.change_names()
        sage: from_L, to_L = L.structure()
        sage: from_L
        Isomorphism given by variable name change map:
          From: Number Field in b with defining polynomial x^2 - 3
          To:   Number Field in a with defining polynomial x^2 - 3
        sage: to_L
        Isomorphism given by variable name change map:
          From: Number Field in a with defining polynomial x^2 - 3
          To:   Number Field in b with defining polynomial x^2 - 3
        sage: type(from_L), type(to_L)
        (<class 'sage.rings.number_field.maps.NameChangeMap'>,
         <class 'sage.rings.number_field.maps.NameChangeMap'>)
    """
    def __init__(self, K, L) -> None:
        """
        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: K.<a, b> = NumberField([x^2 - 3, x^2 + 7])
            sage: L.<c, d> = K.change_names()
            sage: L.structure()
            (Isomorphism given by variable name change map:
              From: Number Field in c with defining polynomial x^2 - 3 over its base field
              To:   Number Field in a with defining polynomial x^2 - 3 over its base field,
             Isomorphism given by variable name change map:
              From: Number Field in a with defining polynomial x^2 - 3 over its base field
              To:   Number Field in c with defining polynomial x^2 - 3 over its base field)
        """

class MapRelativeToAbsoluteNumberField(NumberFieldIsomorphism):
    """
    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^6 + 4*x^2 + 200)
        sage: L = K.relativize(K.subfields(3)[0][1], 'b'); L
        Number Field in b with defining polynomial x^2 + a0 over its base field
        sage: fr, to = L.structure()
        sage: fr
        Relative number field morphism:
          From: Number Field in b with defining polynomial x^2 + a0 over its base field
          To:   Number Field in a with defining polynomial x^6 + 4*x^2 + 200
          Defn: b |--> a
                a0 |--> -a^2
        sage: to
        Ring morphism:
          From: Number Field in a with defining polynomial x^6 + 4*x^2 + 200
          To:   Number Field in b with defining polynomial x^2 + a0 over its base field
          Defn: a |--> b
        sage: type(fr), type(to)
        (<class 'sage.rings.number_field.homset.RelativeNumberFieldHomset_with_category.element_class'>,
         <class 'sage.rings.number_field.homset.NumberFieldHomset_with_category.element_class'>)

        sage: M.<c> = L.absolute_field(); M
        Number Field in c with defining polynomial x^6 + 4*x^2 + 200
        sage: fr, to = M.structure()
        sage: fr
        Isomorphism map:
          From: Number Field in c with defining polynomial x^6 + 4*x^2 + 200
          To:   Number Field in b with defining polynomial x^2 + a0 over its base field
        sage: to
        Isomorphism map:
          From: Number Field in b with defining polynomial x^2 + a0 over its base field
          To:   Number Field in c with defining polynomial x^6 + 4*x^2 + 200
        sage: type(fr), type(to)
        (<class 'sage.rings.number_field.maps.MapAbsoluteToRelativeNumberField'>,
         <class 'sage.rings.number_field.maps.MapRelativeToAbsoluteNumberField'>)
        sage: fr(M.gen()), to(fr(M.gen())) == M.gen()
        (b, True)
        sage: to(L.gen()), fr(to(L.gen())) == L.gen()
        (c, True)
        sage: (to * fr)(M.gen()) == M.gen(), (fr * to)(L.gen()) == L.gen()
        (True, True)
    """
    def __init__(self, R, A) -> None:
        """
        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: L.<a, b> = NumberField([x^2 + 3, x^2 + 5])
            sage: K.<c> = L.absolute_field()
            sage: f = K.structure()[1]; f
            Isomorphism map:
              From: Number Field in a with defining polynomial x^2 + 3 over its base field
              To:   Number Field in c with defining polynomial x^4 + 16*x^2 + 4
            sage: type(f)
            <class 'sage.rings.number_field.maps.MapRelativeToAbsoluteNumberField'>
        """

class MapAbsoluteToRelativeNumberField(NumberFieldIsomorphism):
    """
    See :class:`~MapRelativeToAbsoluteNumberField` for examples.
    """
    def __init__(self, A, R) -> None:
        """
        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: L.<a, b> = NumberField([x^2 + 3, x^2 + 5])
            sage: K.<c> = L.absolute_field()
            sage: f = K.structure()[0] # indirect doctest
            sage: type(f)
            <class 'sage.rings.number_field.maps.MapAbsoluteToRelativeNumberField'>
        """

class MapVectorSpaceToRelativeNumberField(NumberFieldIsomorphism):
    """
    The isomorphism to a relative number field from its underlying `\\QQ`-vector
    space. Compare :class:`~MapRelativeVectorSpaceToRelativeNumberField`.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: L.<a, b> = NumberField([x^2 + 3, x^2 + 5])
        sage: V, fr, to = L.absolute_vector_space()
        sage: type(fr)
        <class 'sage.rings.number_field.maps.MapVectorSpaceToRelativeNumberField'>
    """
    def __init__(self, V, L, from_V, from_K) -> None:
        """
        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: L.<a, b> = NumberField([x^2 + 3, x^2 + 5])
            sage: V, fr, to = L.absolute_vector_space() # indirect doctest
            sage: fr
            Isomorphism map:
              From: Vector space of dimension 4 over Rational Field
              To:   Number Field in a with defining polynomial x^2 + 3 over its base field
        """

class MapRelativeNumberFieldToVectorSpace(NumberFieldIsomorphism):
    """
    The isomorphism from a relative number field to its underlying `\\QQ`-vector
    space. Compare :class:`~MapRelativeNumberFieldToRelativeVectorSpace`.

    EXAMPLES::

        sage: x = polygen(ZZ, 'x')
        sage: K.<a> = NumberField(x^8 + 100*x^6 + x^2 + 5)
        sage: L = K.relativize(K.subfields(4)[0][1], 'b'); L
        Number Field in b with defining polynomial x^2 + a0 over its base field
        sage: L_to_K, K_to_L = L.structure()

        sage: V, fr, to = L.absolute_vector_space()
        sage: V
        Vector space of dimension 8 over Rational Field
        sage: fr
        Isomorphism map:
          From: Vector space of dimension 8 over Rational Field
          To:   Number Field in b with defining polynomial x^2 + a0 over its base field
        sage: to
        Isomorphism map:
          From: Number Field in b with defining polynomial x^2 + a0 over its base field
          To:   Vector space of dimension 8 over Rational Field
        sage: type(fr), type(to)
        (<class 'sage.rings.number_field.maps.MapVectorSpaceToRelativeNumberField'>,
         <class 'sage.rings.number_field.maps.MapRelativeNumberFieldToVectorSpace'>)

        sage: v = V([1, 1, 1, 1, 0, 1, 1, 1])
        sage: fr(v), to(fr(v)) == v
        ((-a0^3 + a0^2 - a0 + 1)*b - a0^3 - a0 + 1, True)
        sage: to(L.gen()), fr(to(L.gen())) == L.gen()
        ((0, 1, 0, 0, 0, 0, 0, 0), True)
    """
    def __init__(self, L, V, to_K, to_V) -> None:
        """
        EXAMPLES::

            sage: x = polygen(ZZ, 'x')
            sage: L.<a, b> = NumberField([x^2 + 3, x^2 + 5])
            sage: V, fr, to = L.absolute_vector_space() # indirect doctest
            sage: to
            Isomorphism map:
              From: Number Field in a with defining polynomial x^2 + 3 over its base field
              To:   Vector space of dimension 4 over Rational Field
        """
