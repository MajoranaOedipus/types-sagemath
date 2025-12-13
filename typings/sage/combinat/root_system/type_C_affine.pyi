from .cartan_type import CartanType_standard_untwisted_affine as CartanType_standard_untwisted_affine

class CartanType(CartanType_standard_untwisted_affine):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['C',4,1])
            sage: ct
            ['C', 4, 1]
            sage: ct._repr_(compact = True)
            'C4~'

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
            ['C', 4]
            sage: ct.dual()
            ['C', 4, 1]^*
            sage: ct.dual().is_untwisted_affine()
            False

        TESTS::

            sage: TestSuite(ct).run()
        """
    def dynkin_diagram(self):
        """
        Return the extended Dynkin diagram for affine type C.

        EXAMPLES::

            sage: c = CartanType(['C',3,1]).dynkin_diagram(); c                         # needs sage.graphs
             O=>=O---O=<=O
             0   1   2   3
             C3~
            sage: c.edges(sort=True)                                                    # needs sage.graphs
            [(0, 1, 2), (1, 0, 1), (1, 2, 1), (2, 1, 1), (2, 3, 1), (3, 2, 2)]
        """
    def ascii_art(self, label=None, node=None):
        """
        Return a ascii art representation of the extended Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['C',5,1]).ascii_art(label = lambda x: x+2))
            O=>=O---O---O---O=<=O
            2   3   4   5   6   7

            sage: print(CartanType(['C',3,1]).ascii_art())
            O=>=O---O=<=O
            0   1   2   3

            sage: print(CartanType(['C',2,1]).ascii_art())
            O=>=O=<=O
            0   1   2

            sage: print(CartanType(['C',1,1]).ascii_art())
            O<=>O
            0   1
        """
