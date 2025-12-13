from _typeshed import Incomplete
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class NumberFieldStructure(UniqueRepresentation):
    '''
    Abstract base class encapsulating information about a number fields
    relation to other number fields.

    TESTS::

        sage: from sage.rings.number_field.structure import NumberFieldStructure
        sage: NumberFieldStructure(QQ)
        <sage.rings.number_field.structure.NumberFieldStructure object at 0x...>

    Instances are cached through
    :class:`sage.structure.unique_representation.UniqueRepresentation`::

        sage: NumberFieldStructure(QQ) is NumberFieldStructure(QQ)
        True

        sage: R.<x> = QQ[]
        sage: x = polygen(ZZ, \'x\')
        sage: K.<i> = NumberField(x^2 + 1)
        sage: L = K.change_names(\'j\').change_names(\'i\')
        sage: K is L  # K and L differ in "structure", one is the "name-change" of the other
        False
        sage: NumberFieldStructure(L) is NumberFieldStructure(L)
        True
        sage: NumberFieldStructure(K) is NumberFieldStructure(L)
        False
        sage: from sage.rings.number_field.structure import NameChange
        sage: KK.<j> = NumberField(x^2 + 1, structure=NameChange(K))
        sage: LL.<j> = NumberField(x^2 + 1, structure=NameChange(L))
        sage: KK is LL
        False
    '''
    other: Incomplete
    def __init__(self, other) -> None:
        """
        Initialization.

        TESTS::

            sage: from sage.rings.number_field.structure import NumberFieldStructure
            sage: type(NumberFieldStructure(QQ))
            <class 'sage.rings.number_field.structure.NumberFieldStructure'>
        """
    def create_structure(self, field) -> None:
        """
        Return a tuple encoding structural information about ``field``.

        OUTPUT:

        Typically, the output is a pair of morphisms. The first one from
        ``field`` to a field from which ``field`` has been constructed and the
        second one its inverse. In this case, these morphisms are used as
        conversion maps between the two fields.

        TESTS::

            sage: from sage.rings.number_field.structure import NumberFieldStructure
            sage: NumberFieldStructure(QQ).create_structure(QQ)
            Traceback (most recent call last):
            ...
            NotImplementedError

        The morphisms created by this method are used as conversion maps::

            sage: K.<i> = QuadraticField(-1)
            sage: L.<j> = K.change_names()
            sage: isinstance(L._structure, NumberFieldStructure)
            True
            sage: from_L, to_L = L.structure()
            sage: L._convert_map_from_(K) is to_L
            True
            sage: L(i)
            j
            sage: K(j)
            i
        """

class NameChange(NumberFieldStructure):
    """
    Structure for a number field created by a change in variable name.

    INPUT:

    - ``other`` -- the number field from which this field has been created

    TESTS::

        sage: from sage.rings.number_field.structure import NameChange
        sage: K.<i> = QuadraticField(-1)
        sage: NameChange(K)
        <sage.rings.number_field.structure.NameChange object at 0x...>

    Check for memory leaks::

        sage: x = polygen(ZZ, 'x')
        sage: u = id(NumberField(x^2 - 5,'a').absolute_field('b'))
        sage: import gc
        sage: gc.collect() #random
        10
        sage: [id(v) for v in gc.get_objects() if id(v) == u]
        []
    """
    def create_structure(self, field):
        """
        Return a pair of isomorphisms which send the generator of ``field`` to
        the generator of ``other`` and vice versa.

        TESTS::

            sage: CyclotomicField(5).absolute_field('a').structure() # indirect doctest
            (Isomorphism given by variable name change map:
              From: Number Field in a with defining polynomial x^4 + x^3 + x^2 + x + 1
              To:   Cyclotomic Field of order 5 and degree 4,
             Isomorphism given by variable name change map:
              From: Cyclotomic Field of order 5 and degree 4
              To:   Number Field in a with defining polynomial x^4 + x^3 + x^2 + x + 1)
        """

class AbsoluteFromRelative(NumberFieldStructure):
    """
    Structure for an absolute number field created from a relative number
    field.

    INPUT:

    - ``other`` -- the number field from which this field has been created

    TESTS::

        sage: from sage.rings.number_field.structure import AbsoluteFromRelative
        sage: K.<a> = QuadraticField(2)
        sage: R.<x> = K[]
        sage: L.<b> = K.extension(x^2 - 3)
        sage: AbsoluteFromRelative(L)
        <sage.rings.number_field.structure.AbsoluteFromRelative object at 0x...>
    """
    def create_structure(self, field):
        """
        Return a pair of isomorphisms which go from ``field`` to ``other`` and
        vice versa.

        TESTS::

            sage: K.<a> = QuadraticField(2)
            sage: R.<x> = K[]
            sage: L.<b> = K.extension(x^2 - 3)
            sage: M.<c> = L.absolute_field()
            sage: M.structure() # indirect doctest
            (Isomorphism map:
              From: Number Field in c with defining polynomial x^4 - 10*x^2 + 1
              To:   Number Field in b with defining polynomial x^2 - 3 over its base field, Isomorphism map:
              From: Number Field in b with defining polynomial x^2 - 3 over its base field
              To:   Number Field in c with defining polynomial x^4 - 10*x^2 + 1)
        """

class RelativeFromAbsolute(NumberFieldStructure):
    """
    Structure for a relative number field created from an absolute number
    field.

    INPUT:

    - ``other`` -- the (absolute) number field from which this field has been
      created

    - ``gen`` -- the generator of the intermediate field

    TESTS::

        sage: from sage.rings.number_field.structure import RelativeFromAbsolute
        sage: RelativeFromAbsolute(QQ, 1/2)
        <sage.rings.number_field.structure.RelativeFromAbsolute object at 0x...>
    """
    gen: Incomplete
    def __init__(self, other, gen) -> None:
        """
        Initialization.

        TESTS::

            sage: from sage.rings.number_field.structure import RelativeFromAbsolute
            sage: type(RelativeFromAbsolute(QQ, 1/2))
            <class 'sage.rings.number_field.structure.RelativeFromAbsolute'>
        """
    def create_structure(self, field):
        """
        Return a pair of isomorphisms which go from ``field`` to ``other`` and
        vice versa.

        INPUT:

        - ``field`` -- a relative number field

        TESTS::

            sage: K.<a> = QuadraticField(2)
            sage: M.<b,a_> = K.relativize(-a)
            sage: M.structure() # indirect doctest
            (Relative number field morphism:
               From: Number Field in b with defining polynomial x + a_ over its base field
               To:   Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095?
               Defn: -a_ |--> a
                     a_ |--> -a, Ring morphism:
               From: Number Field in a with defining polynomial x^2 - 2 with a = 1.414213562373095?
               To:   Number Field in b with defining polynomial x + a_ over its base field
               Defn: a |--> -a_)
        """

class RelativeFromRelative(NumberFieldStructure):
    """
    Structure for a relative number field created from another relative number
    field.

    INPUT:

    - ``other`` -- the relative number field used in the construction, see
      :meth:`create_structure`; there this field will be called ``field_``

    TESTS::

        sage: from sage.rings.number_field.structure import RelativeFromRelative
        sage: K.<i> = QuadraticField(-1)
        sage: R.<x> = K[]
        sage: L.<a> = K.extension(x^2 - 2)
        sage: RelativeFromRelative(L)
        <sage.rings.number_field.structure.RelativeFromRelative object at 0x...>
    """
    def create_structure(self, field):
        """
        Return a pair of isomorphisms which go from ``field`` to the relative
        number field (called ``other`` below) from which ``field`` has been
        created and vice versa.

        The isomorphism is created via the relative number field ``field_``
        which is identical to ``field`` but is equipped with an isomorphism to
        an absolute field which was used in the construction of ``field``.

        INPUT:

        - ``field`` -- a relative number field

        TESTS::

            sage: K.<i> = QuadraticField(-1)
            sage: R.<x> = K[]
            sage: L.<a> = K.extension(x^2 - 2)
            sage: M.<b,a> = L.relativize(a)
            sage: M.structure() # indirect doctest
            (Relative number field morphism:
              From: Number Field in b with defining polynomial x^2 - 2*a*x + 3 over its base field
              To:   Number Field in a with defining polynomial x^2 - 2 over its base field
              Defn: b |--> a - i
                    a |--> a, Relative number field morphism:
              From: Number Field in a with defining polynomial x^2 - 2 over its base field
              To:   Number Field in b with defining polynomial x^2 - 2*a*x + 3 over its base field
              Defn: a |--> a
                    i |--> -b + a)
        """
