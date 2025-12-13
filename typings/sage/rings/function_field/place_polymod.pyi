from .place import FunctionFieldPlace as FunctionFieldPlace
from sage.arith.functions import lcm as lcm
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field_base import NumberField as NumberField

class FunctionFieldPlace_polymod(FunctionFieldPlace):
    """
    Places of extensions of function fields.
    """
    def place_below(self):
        """
        Return the place lying below the place.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: OK = K.maximal_order()
            sage: OL = L.maximal_order()
            sage: p = OK.ideal(x^2 + x + 1)
            sage: dec = OL.decomposition(p)
            sage: q = dec[0][0].place()
            sage: q.place_below()
            Place (x^2 + x + 1)
        """
    def relative_degree(self):
        """
        Return the relative degree of the place.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: OK = K.maximal_order()
            sage: OL = L.maximal_order()
            sage: p = OK.ideal(x^2 + x + 1)
            sage: dec = OL.decomposition(p)
            sage: q = dec[0][0].place()
            sage: q.relative_degree()
            1
        """
    def degree(self):
        """
        Return the degree of the place.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: OK = K.maximal_order()
            sage: OL = L.maximal_order()
            sage: p = OK.ideal(x^2 + x + 1)
            sage: dec = OL.decomposition(p)
            sage: q = dec[0][0].place()
            sage: q.degree()
            2
        """
    def is_infinite_place(self):
        """
        Return ``True`` if the place is above the unique infinite place
        of the underlying rational function field.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: pls = L.places()
            sage: [p.is_infinite_place() for p in pls]
            [True, True, False]
            sage: [p.place_below() for p in pls]
            [Place (1/x), Place (1/x), Place (x)]
        """
    def local_uniformizer(self):
        """
        Return an element of the function field that has a simple zero
        at the place.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: pls = L.places()
            sage: [p.local_uniformizer().valuation(p) for p in pls]
            [1, 1, 1, 1, 1]
        """
    def gaps(self):
        """
        Return the gap sequence for the place.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(4)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^3 + x^3*Y + x)
            sage: O = L.maximal_order()
            sage: p = O.ideal(x,y).place()
            sage: p.gaps() # a Weierstrass place
            [1, 2, 4]

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]                             # needs sage.rings.finite_rings
            sage: L.<y> = K.extension(Y^3 + x^3 * Y + x)                                # needs sage.rings.finite_rings
            sage: [p.gaps() for p in L.places()]                                        # needs sage.rings.finite_rings
            [[1, 2, 4], [1, 2, 4], [1, 2, 4]]
        """
    def residue_field(self, name=None):
        """
        Return the residue field of the place.

        INPUT:

        - ``name`` -- string; name of the generator of the residue field

        OUTPUT:

        - a field isomorphic to the residue field

        - a ring homomorphism from the valuation ring to the field

        - a ring homomorphism from the field to the valuation ring

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p = L.places_finite()[0]
            sage: k, fr_k, to_k = p.residue_field()
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
            sage: to_k(y)
            Traceback (most recent call last):
            ...
            TypeError: y fails to convert into the map's domain
            Valuation ring at Place (x, x*y)...
            sage: to_k(1/y)
            0
            sage: to_k(y/(1+y))
            1
        """
    def valuation_ring(self):
        """
        Return the valuation ring at the place.

        EXAMPLES::

            sage: # needs sage.rings.finite_rings
            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)
            sage: p = L.places_finite()[0]
            sage: p.valuation_ring()
            Valuation ring at Place (x, x*y)
        """
