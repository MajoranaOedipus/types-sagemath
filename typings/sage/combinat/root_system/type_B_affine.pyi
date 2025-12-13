from .cartan_type import CartanType_standard_untwisted_affine as CartanType_standard_untwisted_affine

class CartanType(CartanType_standard_untwisted_affine):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['B',4,1])
            sage: ct
            ['B', 4, 1]
            sage: ct._repr_(compact = True)
            'B4~'

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
            ['B', 4]
            sage: ct.dual()
            ['B', 4, 1]^*
            sage: ct.dual().is_untwisted_affine()
            False

        TESTS::

            sage: TestSuite(ct).run()
        """
    def dynkin_diagram(self):
        """
        Return the extended Dynkin diagram for affine type `B`.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: b = CartanType(['B',3,1]).dynkin_diagram(); b
                O 0
                |
                |
            O---O=>=O
            1   2   3
            B3~
            sage: b.edges(sort=True)
            [(0, 2, 1), (1, 2, 1), (2, 0, 1), (2, 1, 1), (2, 3, 2), (3, 2, 1)]
            sage: b = CartanType(['B',2,1]).dynkin_diagram(); b
            O=>=O=<=O
            0   2   1
            B2~
            sage: b.edges(sort=True)
            [(0, 2, 2), (1, 2, 2), (2, 0, 1), (2, 1, 1)]
            sage: b = CartanType(['B',1,1]).dynkin_diagram(); b
            O<=>O
            0   1
            B1~
            sage: b.edges(sort=True)
            [(0, 1, 2), (1, 0, 2)]
        """
    def ascii_art(self, label=None, node=None):
        """
        Return an ascii art representation of the extended Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['B',3,1]).ascii_art())
                O 0
                |
                |
            O---O=>=O
            1   2   3

            sage: print(CartanType(['B',5,1]).ascii_art(label = lambda x: x+2))
                O 2
                |
                |
            O---O---O---O=>=O
            3   4   5   6   7

            sage: print(CartanType(['B',2,1]).ascii_art(label = lambda x: x+2))
            O=>=O=<=O
            2   4   3
            sage: print(CartanType(['B',1,1]).ascii_art(label = lambda x: x+2))
            O<=>O
            2   3
        """
