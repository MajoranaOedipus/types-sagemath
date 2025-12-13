from .place import FunctionFieldPlace as FunctionFieldPlace

class FunctionFieldPlace_rational(FunctionFieldPlace):
    """
    Places of rational function fields.
    """
    def degree(self):
        """
        Return the degree of the place.

        EXAMPLES::

            sage: F.<x> = FunctionField(GF(2))
            sage: O = F.maximal_order()
            sage: i = O.ideal(x^2 + x + 1)
            sage: p = i.place()
            sage: p.degree()
            2
        """
    def is_infinite_place(self):
        """
        Return ``True`` if the place is at infinite.

        EXAMPLES::

            sage: F.<x> = FunctionField(GF(2))
            sage: F.places()
            [Place (1/x), Place (x), Place (x + 1)]
            sage: [p.is_infinite_place() for p in F.places()]
            [True, False, False]
        """
    def local_uniformizer(self):
        """
        Return a local uniformizer of the place.

        EXAMPLES::

            sage: F.<x> = FunctionField(GF(2))
            sage: F.places()
            [Place (1/x), Place (x), Place (x + 1)]
            sage: [p.local_uniformizer() for p in F.places()]
            [1/x, x, x + 1]
        """
    def residue_field(self, name=None):
        """
        Return the residue field of the place.

        EXAMPLES::

            sage: F.<x> = FunctionField(GF(2))
            sage: O = F.maximal_order()
            sage: p = O.ideal(x^2 + x + 1).place()
            sage: k, fr_k, to_k = p.residue_field()                                     # needs sage.rings.function_field
            sage: k                                                                     # needs sage.rings.function_field
            Finite Field in z2 of size 2^2
            sage: fr_k                                                                  # needs sage.rings.function_field
            Ring morphism:
              From: Finite Field in z2 of size 2^2
              To:   Valuation ring at Place (x^2 + x + 1)
            sage: to_k                                                                  # needs sage.rings.function_field
            Ring morphism:
              From: Valuation ring at Place (x^2 + x + 1)
              To:   Finite Field in z2 of size 2^2
        """
    def valuation_ring(self):
        """
        Return the valuation ring at the place.

        EXAMPLES::

            sage: K.<x> = FunctionField(GF(2)); _.<Y> = K[]
            sage: L.<y> = K.extension(Y^2 + Y + x + 1/x)                                # needs sage.rings.function_field
            sage: p = L.places_finite()[0]                                              # needs sage.rings.function_field
            sage: p.valuation_ring()                                                    # needs sage.rings.function_field
            Valuation ring at Place (x, x*y)
        """
