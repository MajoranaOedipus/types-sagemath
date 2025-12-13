from .cartan_type import CartanType_standard_affine as CartanType_standard_affine
from sage.rings.integer_ring import ZZ as ZZ

class CartanType(CartanType_standard_affine):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['BC',4,2])
            sage: ct
            ['BC', 4, 2]
            sage: ct._repr_(compact=True)
            'BC4~'
            sage: ct.dynkin_diagram()                                                   # needs sage.graphs
            O=<=O---O---O=<=O
            0   1   2   3   4
            BC4~

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            False
            sage: ct.is_affine()
            True
            sage: ct.is_crystallographic()
            True
            sage: ct.is_simply_laced()
            False
            sage: ct.classical()
            ['C', 4]

            sage: dual = ct.dual()
            sage: dual.dynkin_diagram()                                                 # needs sage.graphs
            O=>=O---O---O=>=O
            0   1   2   3   4
            BC4~*

            sage: dual.special_node()
            0
            sage: dual.classical().dynkin_diagram()                                     # needs sage.graphs
            O---O---O=>=O
            1   2   3   4
            B4

            sage: CartanType(['BC',1,2]).dynkin_diagram()                               # needs sage.graphs
              4
            O=<=O
            0   1
            BC1~

        TESTS::

            sage: TestSuite(ct).run()
        """
    def dynkin_diagram(self):
        '''
        Return the extended Dynkin diagram for affine type BC.

        EXAMPLES::

            sage: c = CartanType([\'BC\',3,2]).dynkin_diagram(); c                        # needs sage.graphs
            O=<=O---O=<=O
            0   1   2   3
            BC3~
            sage: c.edges(sort=True)                                                    # needs sage.graphs
            [(0, 1, 1), (1, 0, 2), (1, 2, 1), (2, 1, 1), (2, 3, 1), (3, 2, 2)]

            sage: c = CartanType(["A", 6, 2]).dynkin_diagram()  # should be the same as above; did fail at some point!  # needs sage.graphs
            sage: c                                                                     # needs sage.graphs
            O=<=O---O=<=O
            0   1   2   3
            BC3~
            sage: c.edges(sort=True)                                                    # needs sage.graphs
            [(0, 1, 1), (1, 0, 2), (1, 2, 1), (2, 1, 1), (2, 3, 1), (3, 2, 2)]

            sage: c = CartanType([\'BC\',2,2]).dynkin_diagram(); c                        # needs sage.graphs
            O=<=O=<=O
            0   1   2
            BC2~
            sage: c.edges(sort=True)                                                    # needs sage.graphs
            [(0, 1, 1), (1, 0, 2), (1, 2, 1), (2, 1, 2)]

            sage: c = CartanType([\'BC\',1,2]).dynkin_diagram(); c                        # needs sage.graphs
              4
            O=<=O
            0   1
            BC1~
            sage: c.edges(sort=True)                                                    # needs sage.graphs
            [(0, 1, 1), (1, 0, 4)]
        '''
    def ascii_art(self, label=None, node=None):
        """
        Return a ascii art representation of the extended Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['BC',2,2]).ascii_art())
            O=<=O=<=O
            0   1   2
            sage: print(CartanType(['BC',3,2]).ascii_art())
            O=<=O---O=<=O
            0   1   2   3
            sage: print(CartanType(['BC',5,2]).ascii_art(label = lambda x: x+2))
            O=<=O---O---O---O=<=O
            2   3   4   5   6   7

            sage: print(CartanType(['BC',1,2]).ascii_art(label = lambda x: x+2))
              4
            O=<=O
            2   3
        """
    def classical(self):
        '''
        Return the classical Cartan type associated with ``self``.

            sage: CartanType(["BC", 3, 2]).classical()
            [\'C\', 3]
        '''
    def basic_untwisted(self):
        """
        Return the basic untwisted Cartan type associated with this affine
        Cartan type.

        Given an affine type `X_n^{(r)}`, the basic untwisted type is `X_n`.
        In other words, it is the classical Cartan type that is twisted to
        obtain ``self``.

        EXAMPLES::

            sage: CartanType(['A', 2, 2]).basic_untwisted()
            ['A', 2]
            sage: CartanType(['A', 4, 2]).basic_untwisted()
            ['A', 4]
            sage: CartanType(['BC', 4, 2]).basic_untwisted()
            ['A', 8]
        """
