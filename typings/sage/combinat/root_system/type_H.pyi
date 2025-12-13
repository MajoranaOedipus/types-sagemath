from .cartan_type import CartanType_simple as CartanType_simple, CartanType_standard_finite as CartanType_standard_finite

class CartanType(CartanType_standard_finite, CartanType_simple):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['H',3])
            sage: ct
            ['H', 3]
            sage: ct._repr_(compact = True)
            'H3'
            sage: ct.rank()
            3

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            True
            sage: ct.is_affine()
            False
            sage: ct.is_crystallographic()
            False
            sage: ct.is_simply_laced()
            False

        TESTS::

            sage: TestSuite(ct).run()
        """
    def coxeter_diagram(self):
        """
        Return a Coxeter diagram for type H.

        EXAMPLES::

             sage: ct = CartanType(['H',3])
             sage: ct.coxeter_diagram()                                                 # needs sage.graphs
             Graph on 3 vertices
             sage: ct.coxeter_diagram().edges(sort=True)                                # needs sage.graphs
             [(1, 2, 3), (2, 3, 5)]
             sage: ct.coxeter_matrix()                                                  # needs sage.graphs
             [1 3 2]
             [3 1 5]
             [2 5 1]

             sage: ct = CartanType(['H',4])
             sage: ct.coxeter_diagram()                                                 # needs sage.graphs
             Graph on 4 vertices
             sage: ct.coxeter_diagram().edges(sort=True)                                # needs sage.graphs
             [(1, 2, 3), (2, 3, 3), (3, 4, 5)]
             sage: ct.coxeter_matrix()                                                  # needs sage.graphs
             [1 3 2 2]
             [3 1 3 2]
             [2 3 1 5]
             [2 2 5 1]
        """
    def coxeter_number(self):
        """
        Return the Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['H',3]).coxeter_number()
            10
            sage: CartanType(['H',4]).coxeter_number()
            30
        """
