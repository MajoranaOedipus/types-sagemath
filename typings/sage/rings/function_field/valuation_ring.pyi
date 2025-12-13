from sage.categories.homset import Hom as Hom
from sage.categories.rings import Rings as Rings
from sage.misc.cachefunc import cached_method as cached_method
from sage.structure.parent import Parent as Parent
from sage.structure.unique_representation import UniqueRepresentation as UniqueRepresentation

class FunctionFieldValuationRing(UniqueRepresentation, Parent):
    """
    Base class for valuation rings of function fields.

    INPUT:

    - ``field`` -- function field

    - ``place`` -- place of the function field

    EXAMPLES::

        sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
        sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
        sage: p = L.places_finite()[0]
        sage: p.valuation_ring()
        Valuation ring at Place (x, x*y)
    """
    def __init__(self, field, place, category=None) -> None:
        """
        Initialize.

        TESTS::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p = L.places_finite()[0]
            sage: R = p.valuation_ring()
            sage: TestSuite(R).run()
        """
    def place(self):
        """
        Return the place associated with the valuation ring.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p = L.places_finite()[0]
            sage: R = p.valuation_ring()
            sage: p == R.place()
            True
        """
    @cached_method
    def residue_field(self, name=None):
        """
        Return the residue field of the valuation ring together with
        the maps from and to it.

        INPUT:

        - ``name`` -- string; name of the generator of the field

        OUTPUT:

        - a field isomorphic to the residue field

        - a ring homomorphism from the valuation ring to the field

        - a ring homomorphism from the field to the valuation ring

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p = L.places_finite()[0]
            sage: R = p.valuation_ring()
            sage: k, fr_k, to_k = R.residue_field()
            sage: k
            Finite Field of size 2
            sage: fr_k
            Ring morphism:
              From: Finite Field of size 2
              To:   Valuation ring at Place (x, x*y)
            sage: to_k
            Ring morphism:
              From: Valuation ring at Place (x, x*y)
              To:   Finite Field of size 2
            sage: to_k(1/y)
            0
            sage: to_k(y/(1+y))
            1
        """
