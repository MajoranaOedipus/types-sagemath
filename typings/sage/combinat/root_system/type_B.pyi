from . import ambient_space as ambient_space
from .cartan_type import CartanType_crystallographic as CartanType_crystallographic, CartanType_simple as CartanType_simple, CartanType_simply_laced as CartanType_simply_laced, CartanType_standard_finite as CartanType_standard_finite
from sage.misc.persist import register_unpickle_override as register_unpickle_override

class AmbientSpace(ambient_space.AmbientSpace):
    def dimension(self):
        """
        EXAMPLES::

            sage: e = RootSystem(['B',3]).ambient_space()
            sage: e.dimension()
            3
        """
    def root(self, i, j):
        """
        Note that indexing starts at 0.

        EXAMPLES::

            sage: e = RootSystem(['B',3]).ambient_space()
            sage: e.root(0,1)
            (1, -1, 0)
        """
    def simple_root(self, i):
        """
        EXAMPLES::

            sage: e = RootSystem(['B',4]).ambient_space()
            sage: e.simple_roots()
            Finite family {1: (1, -1, 0, 0), 2: (0, 1, -1, 0), 3: (0, 0, 1, -1), 4: (0, 0, 0, 1)}
            sage: e.positive_roots()
            [(1, -1, 0, 0),
            (1, 1, 0, 0),
            (1, 0, -1, 0),
            (1, 0, 1, 0),
            (1, 0, 0, -1),
            (1, 0, 0, 1),
            (0, 1, -1, 0),
            (0, 1, 1, 0),
            (0, 1, 0, -1),
            (0, 1, 0, 1),
            (0, 0, 1, -1),
            (0, 0, 1, 1),
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1)]
            sage: e.fundamental_weights()
            Finite family {1: (1, 0, 0, 0), 2: (1, 1, 0, 0), 3: (1, 1, 1, 0), 4: (1/2, 1/2, 1/2, 1/2)}
        """
    def negative_roots(self):
        """
        EXAMPLES::

            sage: RootSystem(['B',3]).ambient_space().negative_roots()
            [(-1, 1, 0),
             (-1, -1, 0),
             (-1, 0, 1),
             (-1, 0, -1),
             (0, -1, 1),
             (0, -1, -1),
             (-1, 0, 0),
             (0, -1, 0),
             (0, 0, -1)]
        """
    def positive_roots(self):
        """
        EXAMPLES::

            sage: RootSystem(['B',3]).ambient_space().positive_roots()
            [(1, -1, 0),
             (1, 1, 0),
             (1, 0, -1),
             (1, 0, 1),
             (0, 1, -1),
             (0, 1, 1),
             (1, 0, 0),
             (0, 1, 0),
             (0, 0, 1)]
        """
    def fundamental_weight(self, i):
        """
        EXAMPLES::

            sage: RootSystem(['B',3]).ambient_space().fundamental_weights()
            Finite family {1: (1, 0, 0), 2: (1, 1, 0), 3: (1/2, 1/2, 1/2)}
        """

class CartanType(CartanType_standard_finite, CartanType_simple, CartanType_crystallographic):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['B',4])
            sage: ct
            ['B', 4]
            sage: ct._repr_(compact = True)
            'B4'

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            True
            sage: ct.is_affine()
            False
            sage: ct.is_crystallographic()
            True
            sage: ct.is_simply_laced()
            False
            sage: ct.affine()
            ['B', 4, 1]
            sage: ct.dual()
            ['C', 4]

            sage: ct = CartanType(['B',1])
            sage: ct.is_simply_laced()
            True
            sage: ct.affine()
            ['B', 1, 1]

        TESTS::

            sage: TestSuite(ct).run()
        """
    AmbientSpace = AmbientSpace
    def coxeter_number(self):
        """
        Return the Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['B',4]).coxeter_number()
            8
        """
    def dual_coxeter_number(self):
        """
        Return the dual Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['B',4]).dual_coxeter_number()
            7
        """
    def dual(self):
        '''
        Types B and C are in duality:

        EXAMPLES::

            sage: CartanType(["C", 3]).dual()
            [\'B\', 3]
        '''
    def dynkin_diagram(self):
        """
        Return a Dynkin diagram for type B.

        EXAMPLES::

             sage: b = CartanType(['B',3]).dynkin_diagram(); b                          # needs sage.graphs
             O---O=>=O
             1   2   3
             B3
             sage: b.edges(sort=True)                                                   # needs sage.graphs
             [(1, 2, 1), (2, 1, 1), (2, 3, 2), (3, 2, 1)]

             sage: b = CartanType(['B',1]).dynkin_diagram(); b                          # needs sage.graphs
             O
             1
             B1
             sage: b.edges(sort=True)                                                   # needs sage.graphs
             []
        """
    def ascii_art(self, label=None, node=None):
        """
        Return an ascii art representation of the Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['B',1]).ascii_art())
            O
            1
            sage: print(CartanType(['B',2]).ascii_art())
            O=>=O
            1   2
            sage: print(CartanType(['B',5]).ascii_art(label = lambda x: x+2))
            O---O---O---O=>=O
            3   4   5   6   7
        """
