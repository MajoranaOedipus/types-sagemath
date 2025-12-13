from sage.categories.sets_cat import Sets as Sets
from sage.structure.element import Element as Element
from sage.structure.parent import Parent as Parent
from sage.structure.richcmp import richcmp as richcmp
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FunctionFieldPlace(Element):
    """
    Places of function fields.

    INPUT:

    - ``parent`` -- place set of a function field

    - ``prime`` -- prime ideal associated with the place

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
        sage: L.<y> = K.extension(Y^3 + x + x^3*Y)                                      # needs sage.rings.function_field
        sage: L.places_finite()[0]                                                      # needs sage.rings.function_field
        Place (x, y)
    """
    def __init__(self, parent, prime) -> None:
        """
        Initialize the place.

        TESTS::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)                                  # needs sage.rings.function_field
            sage: p = L.places_finite()[0]                                              # needs sage.rings.function_field
            sage: TestSuite(p).run()                                                    # needs sage.rings.function_field
        """
    def __hash__(self):
        """
        Return the hash of the place.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x + x^3*Y)                                  # needs sage.rings.function_field
            sage: p = L.places_finite()[0]                                              # needs sage.rings.function_field
            sage: {p: 1}                                                                # needs sage.rings.function_field
            {Place (x, y): 1}
        """
    def __radd__(self, other):
        """
        Return the prime divisor of the place if ``other`` is zero.

        This is only to support the ``sum`` function, that adds
        the argument to initial (int) zero.

        EXAMPLES::

            sage: k.<a> = GF(2)
            sage: K.<x> = FunctionField(k)
            sage: sum(K.places_finite())                                                # needs sage.libs.pari sage.modules
            Place (x) + Place (x + 1)

        Note that this does not work, as wanted::

            sage: 0 + K.place_infinite()
            Traceback (most recent call last):
            ...
            TypeError: unsupported operand parent(s) for +: ...

        The reason is that the ``0`` is a Sage integer, for which
        the coercion system applies.
        """
    def function_field(self):
        """
        Return the function field to which the place belongs.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)                                  # needs sage.rings.function_field
            sage: p = L.places()[0]                                                     # needs sage.rings.function_field
            sage: p.function_field() == L                                               # needs sage.rings.function_field
            True
        """
    def prime_ideal(self):
        """
        Return the prime ideal associated with the place.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)                                  # needs sage.rings.function_field
            sage: p = L.places()[0]                                                     # needs sage.rings.function_field
            sage: p.prime_ideal()                                                       # needs sage.rings.function_field
            Ideal (1/x^3*y^2 + 1/x) of Maximal infinite order of Function field
            in y defined by y^3 + x^3*y + x
        """
    def divisor(self, multiplicity: int = 1):
        """
        Return the prime divisor corresponding to the place.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(5)); R.<Y> = PolynomialRing(K)
            sage: F.<y> = K.extension(Y^2 - x^3 - 1)
            sage: O = F.maximal_order()
            sage: I = O.ideal(x + 1, y)
            sage: P = I.place()
            sage: P.divisor()
            Place (x + 1, y)
        """

class PlaceSet(UniqueRepresentation, Parent):
    """
    Sets of Places of function fields.

    INPUT:

    - ``field`` -- function field

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
        sage: L.<y> = K.extension(Y^3 + x^3*Y + x)                                      # needs sage.rings.function_field
        sage: L.place_set()                                                             # needs sage.rings.function_field
        Set of places of Function field in y defined by y^3 + x^3*y + x
    """
    Element = FunctionFieldPlace
    def __init__(self, field) -> None:
        """
        Initialize the set of places of the function ``field``.

        TESTS::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)                                  # needs sage.rings.function_field
            sage: places = L.place_set()                                                # needs sage.rings.function_field
            sage: TestSuite(places).run()                                               # needs sage.rings.function_field
        """
    def function_field(self):
        """
        Return the function field to which this place set belongs.

        EXAMPLES::

            sage: # needs sage.rings.function_field
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: PS = L.place_set()
            sage: PS.function_field() == L
            True
        """
