from . import ambient_space as ambient_space
from .cartan_type import CartanType_simple as CartanType_simple, CartanType_simply_laced as CartanType_simply_laced, CartanType_standard_finite as CartanType_standard_finite
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.persist import register_unpickle_override as register_unpickle_override

class AmbientSpace(ambient_space.AmbientSpace):
    def dimension(self):
        """
        EXAMPLES::

            sage: e = RootSystem(['D',3]).ambient_space()
            sage: e.dimension()
            3
        """
    def root(self, i, j, p1, p2):
        """
        Note that indexing starts at 0.

        EXAMPLES::

            sage: e = RootSystem(['D',3]).ambient_space()
            sage: e.root(0, 1, 1, 1)
            (-1, -1, 0)
            sage: e.root(0, 0, 1, 1)
            (-1, 0, 0)
        """
    def simple_root(self, i):
        """
        EXAMPLES::

            sage: RootSystem(['D',4]).ambient_space().simple_roots()
            Finite family {1: (1, -1, 0, 0), 2: (0, 1, -1, 0), 3: (0, 0, 1, -1), 4: (0, 0, 1, 1)}
        """
    def positive_roots(self):
        """
        EXAMPLES::

            sage: RootSystem(['D',4]).ambient_space().positive_roots()
            [(1, 1, 0, 0),
             (1, 0, 1, 0),
             (0, 1, 1, 0),
             (1, 0, 0, 1),
             (0, 1, 0, 1),
             (0, 0, 1, 1),
             (1, -1, 0, 0),
             (1, 0, -1, 0),
             (0, 1, -1, 0),
             (1, 0, 0, -1),
             (0, 1, 0, -1),
             (0, 0, 1, -1)]
        """
    def negative_roots(self):
        """
        EXAMPLES::

            sage: RootSystem(['D',4]).ambient_space().negative_roots()
            [(-1, 1, 0, 0),
             (-1, 0, 1, 0),
             (0, -1, 1, 0),
             (-1, 0, 0, 1),
             (0, -1, 0, 1),
             (0, 0, -1, 1),
             (-1, -1, 0, 0),
             (-1, 0, -1, 0),
             (0, -1, -1, 0),
             (-1, 0, 0, -1),
             (0, -1, 0, -1),
             (0, 0, -1, -1)]
        """
    def fundamental_weight(self, i):
        """
        EXAMPLES::

            sage: RootSystem(['D',4]).ambient_space().fundamental_weights()
            Finite family {1: (1, 0, 0, 0), 2: (1, 1, 0, 0), 3: (1/2, 1/2, 1/2, -1/2), 4: (1/2, 1/2, 1/2, 1/2)}
        """

class CartanType(CartanType_standard_finite, CartanType_simply_laced):
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['D',4])
            sage: ct
            ['D', 4]
            sage: ct._repr_(compact = True)
            'D4'

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            True
            sage: ct.is_crystallographic()
            True
            sage: ct.is_simply_laced()
            True
            sage: ct.dual()
            ['D', 4]
            sage: ct.affine()
            ['D', 4, 1]

            sage: ct = CartanType(['D',2])
            sage: ct.is_irreducible()
            False
            sage: ct.dual()
            ['D', 2]
            sage: ct.affine()
            Traceback (most recent call last):
            ...
            ValueError: ['D', 2, 1] is not a valid Cartan type


        TESTS::

            sage: TestSuite(ct).run()
        """
    AmbientSpace = AmbientSpace
    def is_atomic(self):
        '''
        Implement :meth:`CartanType_abstract.is_atomic`.

        `D_2` is atomic, like all `D_n`, despite being non irreducible.

        EXAMPLES::

            sage: CartanType(["D",2]).is_atomic()
            True
            sage: CartanType(["D",2]).is_irreducible()
            False
        '''
    def coxeter_number(self):
        """
        Return the Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['D',4]).coxeter_number()
            6
        """
    def dual_coxeter_number(self):
        """
        Return the dual Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['D',4]).dual_coxeter_number()
            6
        """
    @cached_method
    def dynkin_diagram(self):
        """
        Return a Dynkin diagram for type D.

        EXAMPLES::

            sage: d = CartanType(['D',5]).dynkin_diagram(); d                           # needs sage.graphs
                    O 5
                    |
                    |
            O---O---O---O
            1   2   3   4
            D5
            sage: d.edges(sort=True)                                                    # needs sage.graphs
            [(1, 2, 1), (2, 1, 1), (2, 3, 1), (3, 2, 1),
             (3, 4, 1), (3, 5, 1), (4, 3, 1), (5, 3, 1)]

            sage: d = CartanType(['D',4]).dynkin_diagram(); d                           # needs sage.graphs
                O 4
                |
                |
            O---O---O
            1   2   3
            D4
            sage: d.edges(sort=True)                                                    # needs sage.graphs
            [(1, 2, 1), (2, 1, 1), (2, 3, 1), (2, 4, 1), (3, 2, 1), (4, 2, 1)]

            sage: d = CartanType(['D',3]).dynkin_diagram(); d                           # needs sage.graphs
            O 3
            |
            |
            O---O
            1   2
            D3
            sage: d.edges(sort=True)                                                    # needs sage.graphs
            [(1, 2, 1), (1, 3, 1), (2, 1, 1), (3, 1, 1)]


            sage: d = CartanType(['D',2]).dynkin_diagram(); d                           # needs sage.graphs
            O   O
            1   2
            D2
            sage: d.edges(sort=True)                                                    # needs sage.graphs
            []
        """
    def ascii_art(self, label=None, node=None):
        """
        Return a ascii art representation of the extended Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['D',3]).ascii_art())
            O 3
            |
            |
            O---O
            1   2
            sage: print(CartanType(['D',4]).ascii_art())
                O 4
                |
                |
            O---O---O
            1   2   3
            sage: print(CartanType(['D',4]).ascii_art(label = lambda x: x+2))
                O 6
                |
                |
            O---O---O
            3   4   5
            sage: print(CartanType(['D',6]).ascii_art(label = lambda x: x+2))
                        O 8
                        |
                        |
            O---O---O---O---O
            3   4   5   6   7
        """
