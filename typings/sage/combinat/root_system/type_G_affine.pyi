from .cartan_type import CartanType_standard_untwisted_affine as CartanType_standard_untwisted_affine

class CartanType(CartanType_standard_untwisted_affine):
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['G',2,1])
            sage: ct
            ['G', 2, 1]
            sage: ct._repr_(compact = True)
            'G2~'

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            False
            sage: ct.is_affine()
            True
            sage: ct.is_untwisted_affine()
            True
            sage: ct.is_crystallographic()
            True
            sage: ct.is_simply_laced()
            False
            sage: ct.classical()
            ['G', 2]
            sage: ct.dual()
            ['G', 2, 1]^*
            sage: ct.dual().is_untwisted_affine()
            False

        TESTS::

            sage: TestSuite(ct).run()
        """
    def dynkin_diagram(self):
        """
        Return the extended Dynkin diagram for type G.

        EXAMPLES::

            sage: g = CartanType(['G',2,1]).dynkin_diagram(); g                         # needs sage.graphs
              3
            O=<=O---O
            1   2   0
            G2~
            sage: g.edges(sort=True)                                                    # needs sage.graphs
            [(0, 2, 1), (1, 2, 1), (2, 0, 1), (2, 1, 3)]
        """
    def ascii_art(self, label=None, node=None):
        """
        Return an ascii art representation of the Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['G',2,1]).ascii_art(label = lambda x: x+2))
              3
            O=<=O---O
            3   4   2
        """
