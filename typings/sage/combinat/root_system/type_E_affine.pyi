from .cartan_type import CartanType_simply_laced as CartanType_simply_laced, CartanType_standard_untwisted_affine as CartanType_standard_untwisted_affine

class CartanType(CartanType_standard_untwisted_affine, CartanType_simply_laced):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['E',6,1])
            sage: ct
            ['E', 6, 1]
            sage: ct._repr_(compact = True)
            'E6~'

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
            ['E', 6]
            sage: ct.dual()
            ['E', 6, 1]

        TESTS::

            sage: TestSuite(ct).run()
        """
    def dynkin_diagram(self):
        """
        Return the extended Dynkin diagram for affine type E.

        EXAMPLES::

            sage: e = CartanType(['E', 6, 1]).dynkin_diagram(); e                       # needs sage.graphs
                    O 0
                    |
                    |
                    O 2
                    |
                    |
            O---O---O---O---O
            1   3   4   5   6
            E6~
            sage: e.edges(sort=True)                                                    # needs sage.graphs
            [(0, 2, 1),
             (1, 3, 1),
             (2, 0, 1),
             (2, 4, 1),
             (3, 1, 1),
             (3, 4, 1),
             (4, 2, 1),
             (4, 3, 1),
             (4, 5, 1),
             (5, 4, 1),
             (5, 6, 1),
             (6, 5, 1)]

            sage: # needs sage.graphs
            sage: e = CartanType(['E', 7, 1]).dynkin_diagram(); e
                        O 2
                        |
                        |
            O---O---O---O---O---O---O
            0   1   3   4   5   6   7
            E7~
            sage: e.edges(sort=True)
            [(0, 1, 1), (1, 0, 1), (1, 3, 1), (2, 4, 1), (3, 1, 1), (3, 4, 1),
             (4, 2, 1), (4, 3, 1), (4, 5, 1), (5, 4, 1), (5, 6, 1),
             (6, 5, 1), (6, 7, 1), (7, 6, 1)]
            sage: e = CartanType(['E', 8, 1]).dynkin_diagram(); e
                    O 2
                    |
                    |
            O---O---O---O---O---O---O---O
            1   3   4   5   6   7   8   0
            E8~
            sage: e.edges(sort=True)
            [(0, 8, 1), (1, 3, 1), (2, 4, 1), (3, 1, 1), (3, 4, 1),
             (4, 2, 1), (4, 3, 1), (4, 5, 1), (5, 4, 1), (5, 6, 1),
             (6, 5, 1), (6, 7, 1), (7, 6, 1), (7, 8, 1), (8, 0, 1), (8, 7, 1)]
        """
    def ascii_art(self, label=None, node=None):
        """
        Return an ascii art representation of the extended Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['E',6,1]).ascii_art(label = lambda x: x+2))
                    O 2
                    |
                    |
                    O 4
                    |
                    |
            O---O---O---O---O
            3   5   6   7   8
            sage: print(CartanType(['E',7,1]).ascii_art(label = lambda x: x+2))
                        O 4
                        |
                        |
            O---O---O---O---O---O---O
            2   3   5   6   7   8   9
            sage: print(CartanType(['E',8,1]).ascii_art(label = lambda x: x-3))
                    O -1
                    |
                    |
            O---O---O---O---O---O---O---O
            -2  0   1   2   3   4   5   -3
        """
