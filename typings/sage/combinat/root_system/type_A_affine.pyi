from .cartan_type import CartanType_simply_laced as CartanType_simply_laced, CartanType_standard_untwisted_affine as CartanType_standard_untwisted_affine

class CartanType(CartanType_standard_untwisted_affine):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['A',4,1])
            sage: ct
            ['A', 4, 1]
            sage: ct._repr_(compact = True)
            'A4~'

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
            True
            sage: ct.classical()
            ['A', 4]
            sage: ct.dual()
            ['A', 4, 1]

            sage: ct = CartanType(['A', 1, 1])
            sage: ct.is_simply_laced()
            False
            sage: ct.dual()
            ['A', 1, 1]

        TESTS::

            sage: TestSuite(ct).run()
        """
    def dynkin_diagram(self):
        """
        Return the extended Dynkin diagram for affine type A.

        EXAMPLES::

            sage: a = CartanType(['A',3,1]).dynkin_diagram(); a                         # needs sage.graphs
             0
             O-------+
             |       |
             |       |
             O---O---O
             1   2   3
             A3~
            sage: a.edges(sort=True)                                                    # needs sage.graphs
            [(0, 1, 1),
             (0, 3, 1),
             (1, 0, 1),
             (1, 2, 1),
             (2, 1, 1),
             (2, 3, 1),
             (3, 0, 1),
             (3, 2, 1)]

            sage: a = DynkinDiagram(['A',1,1]); a                                       # needs sage.graphs
            O<=>O
            0   1
            A1~
            sage: a.edges(sort=True)                                                    # needs sage.graphs
            [(0, 1, 2), (1, 0, 2)]
        """
    def ascii_art(self, label=None, node=None):
        """
        Return an ascii art representation of the extended Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['A',3,1]).ascii_art())
            0
            O-------+
            |       |
            |       |
            O---O---O
            1   2   3

            sage: print(CartanType(['A',5,1]).ascii_art(label = lambda x: x+2))
            2
            O---------------+
            |               |
            |               |
            O---O---O---O---O
            3   4   5   6   7

            sage: print(CartanType(['A',1,1]).ascii_art())
            O<=>O
            0   1

            sage: print(CartanType(['A',1,1]).ascii_art(label = lambda x: x+2))
            O<=>O
            2   3
        """
    def dual(self):
        """
        Type `A_1^1` is self dual despite not being simply laced.

        EXAMPLES::

            sage: CartanType(['A',1,1]).dual()
            ['A', 1, 1]
        """
