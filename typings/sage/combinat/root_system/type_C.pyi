from . import ambient_space as ambient_space
from .cartan_type import CartanType_crystallographic as CartanType_crystallographic, CartanType_simple as CartanType_simple, CartanType_simply_laced as CartanType_simply_laced, CartanType_standard_finite as CartanType_standard_finite
from sage.misc.persist import register_unpickle_override as register_unpickle_override

class AmbientSpace(ambient_space.AmbientSpace):
    """
    EXAMPLES::

        sage: e = RootSystem(['C',2]).ambient_space(); e
        Ambient space of the Root system of type ['C', 2]

    One cannot construct the ambient lattice because the fundamental
    coweights have rational coefficients::

        sage: e.smallest_base_ring()
        Rational Field

        sage: RootSystem(['B',2]).ambient_space().fundamental_weights()
        Finite family {1: (1, 0), 2: (1/2, 1/2)}

    TESTS::

        sage: TestSuite(e).run()                                                        # needs sage.graphs
    """
    def dimension(self):
        """
        EXAMPLES::

            sage: e = RootSystem(['C',3]).ambient_space()
            sage: e.dimension()
            3
        """
    def root(self, i, j, p1, p2):
        """
        Note that indexing starts at 0.

        EXAMPLES::

            sage: e = RootSystem(['C',3]).ambient_space()
            sage: e.root(0, 1, 1, 1)
            (-1, -1, 0)
        """
    def simple_root(self, i):
        """
        EXAMPLES::

            sage: RootSystem(['C',3]).ambient_space().simple_roots()
            Finite family {1: (1, -1, 0), 2: (0, 1, -1), 3: (0, 0, 2)}
        """
    def positive_roots(self):
        """
        EXAMPLES::

            sage: RootSystem(['C',3]).ambient_space().positive_roots()
            [(1, 1, 0),
             (1, 0, 1),
             (0, 1, 1),
             (1, -1, 0),
             (1, 0, -1),
             (0, 1, -1),
             (2, 0, 0),
             (0, 2, 0),
             (0, 0, 2)]
        """
    def negative_roots(self):
        """
        EXAMPLES::

            sage: RootSystem(['C',3]).ambient_space().negative_roots()
            [(-1, 1, 0),
             (-1, 0, 1),
             (0, -1, 1),
             (-1, -1, 0),
             (-1, 0, -1),
             (0, -1, -1),
             (-2, 0, 0),
             (0, -2, 0),
             (0, 0, -2)]
        """
    def fundamental_weight(self, i):
        """
        EXAMPLES::

            sage: RootSystem(['C',3]).ambient_space().fundamental_weights()
            Finite family {1: (1, 0, 0), 2: (1, 1, 0), 3: (1, 1, 1)}
        """

class CartanType(CartanType_standard_finite, CartanType_simple, CartanType_crystallographic):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['C',4])
            sage: ct
            ['C', 4]
            sage: ct._repr_(compact = True)
            'C4'

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            True
            sage: ct.is_crystallographic()
            True
            sage: ct.is_simply_laced()
            False
            sage: ct.affine()
            ['C', 4, 1]
            sage: ct.dual()
            ['B', 4]

            sage: ct = CartanType(['C',1])
            sage: ct.is_simply_laced()
            True
            sage: ct.affine()
            ['C', 1, 1]

        TESTS::

            sage: TestSuite(ct).run()
        """
    AmbientSpace = AmbientSpace
    def coxeter_number(self):
        """
        Return the Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['C',4]).coxeter_number()
            8
        """
    def dual_coxeter_number(self):
        """
        Return the dual Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['C',4]).dual_coxeter_number()
            5
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
        Return a Dynkin diagram for type C.

        EXAMPLES::

            sage: c = CartanType(['C',3]).dynkin_diagram(); c                           # needs sage.graphs
            O---O=<=O
            1   2   3
            C3
            sage: c.edges(sort=True)                                                    # needs sage.graphs
            [(1, 2, 1), (2, 1, 1), (2, 3, 1), (3, 2, 2)]

             sage: b = CartanType(['C',1]).dynkin_diagram(); b                          # needs sage.graphs
             O
             1
             C1
             sage: b.edges(sort=True)                                                   # needs sage.graphs
             []
        """
    def ascii_art(self, label=None, node=None):
        """
        Return a ascii art representation of the extended Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['C',1]).ascii_art())
            O
            1
            sage: print(CartanType(['C',2]).ascii_art())
            O=<=O
            1   2
            sage: print(CartanType(['C',3]).ascii_art())
            O---O=<=O
            1   2   3
            sage: print(CartanType(['C',5]).ascii_art(label = lambda x: x+2))
            O---O---O---O=<=O
            3   4   5   6   7
        """
