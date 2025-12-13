from .cartan_type import CartanType_standard_untwisted_affine as CartanType_standard_untwisted_affine

class CartanType(CartanType_standard_untwisted_affine):
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['F',4,1])
            sage: ct
            ['F', 4, 1]
            sage: ct._repr_(compact = True)
            'F4~'

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
            ['F', 4]
            sage: ct.dual()
            ['F', 4, 1]^*
            sage: ct.dual().is_untwisted_affine()
            False

        TESTS::

            sage: TestSuite(ct).run()
        """
    def dynkin_diagram(self):
        """
        Return the extended Dynkin diagram for affine type F.

        EXAMPLES::

            sage: f = CartanType(['F', 4, 1]).dynkin_diagram(); f                       # needs sage.graphs
            O---O---O=>=O---O
            0   1   2   3   4
            F4~
            sage: f.edges(sort=True)                                                    # needs sage.graphs
            [(0, 1, 1), (1, 0, 1), (1, 2, 1), (2, 1, 1),
             (2, 3, 2), (3, 2, 1), (3, 4, 1), (4, 3, 1)]
        """
    def ascii_art(self, label=None, node=None):
        """
        Return a ascii art representation of the extended Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['F',4,1]).ascii_art(label = lambda x: x+2))
            O---O---O=>=O---O
            2   3   4   5   6
        """
