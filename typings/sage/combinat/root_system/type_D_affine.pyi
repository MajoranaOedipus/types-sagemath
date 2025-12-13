from .cartan_type import CartanType_simply_laced as CartanType_simply_laced, CartanType_standard_untwisted_affine as CartanType_standard_untwisted_affine

class CartanType(CartanType_standard_untwisted_affine, CartanType_simply_laced):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['D',4,1])
            sage: ct
            ['D', 4, 1]
            sage: ct._repr_(compact = True)
            'D4~'

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
            ['D', 4]
            sage: ct.dual()
            ['D', 4, 1]

        TESTS::

            sage: TestSuite(ct).run()
        """
    def dynkin_diagram(self):
        """
        Return the extended Dynkin diagram for affine type D.

        EXAMPLES::

           sage: d = CartanType(['D', 6, 1]).dynkin_diagram(); d                        # needs sage.graphs
              0 O       O 6
                |       |
                |       |
            O---O---O---O---O
            1   2   3   4   5
            D6~
           sage: d.edges(sort=True)                                                     # needs sage.graphs
           [(0, 2, 1), (1, 2, 1), (2, 0, 1), (2, 1, 1), (2, 3, 1),
            (3, 2, 1), (3, 4, 1), (4, 3, 1), (4, 5, 1), (4, 6, 1), (5, 4, 1), (6, 4, 1)]

           sage: d = CartanType(['D', 4, 1]).dynkin_diagram(); d                        # needs sage.graphs
               O 4
               |
               |
           O---O---O
           1   |2  3
               |
               O 0
           D4~
           sage: d.edges(sort=True)                                                     # needs sage.graphs
           [(0, 2, 1),
            (1, 2, 1),
            (2, 0, 1),
            (2, 1, 1),
            (2, 3, 1),
            (2, 4, 1),
            (3, 2, 1),
            (4, 2, 1)]

           sage: d = CartanType(['D', 3, 1]).dynkin_diagram(); d                        # needs sage.graphs
           0
           O-------+
           |       |
           |       |
           O---O---O
           3   1   2
           D3~
           sage: d.edges(sort=True)                                                     # needs sage.graphs
           [(0, 2, 1), (0, 3, 1), (1, 2, 1), (1, 3, 1),
            (2, 0, 1), (2, 1, 1), (3, 0, 1), (3, 1, 1)]
        """
    def ascii_art(self, label=None, node=None):
        """
        Return an ascii art representation of the extended Dynkin diagram.

        TESTS::

            sage: print(CartanType(['D',6,1]).ascii_art(label = lambda x: x+2))
              2 O       O 8
                |       |
                |       |
            O---O---O---O---O
            3   4   5   6   7

            sage: print(CartanType(['D',4,1]).ascii_art(label = lambda x: x+2))
                O 6
                |
                |
            O---O---O
            3   |4  5
                |
                O 2

            sage: print(CartanType(['D',3,1]).ascii_art(label = lambda x: x+2))
            2
            O-------+
            |       |
            |       |
            O---O---O
            5   3   4
        """
