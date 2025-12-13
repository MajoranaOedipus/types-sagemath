from . import ambient_space as ambient_space
from .cartan_type import CartanType_simple as CartanType_simple, CartanType_simply_laced as CartanType_simply_laced, CartanType_standard_finite as CartanType_standard_finite
from sage.combinat.root_system.root_lattice_realizations import RootLatticeRealizations as RootLatticeRealizations
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer_ring import ZZ as ZZ

class AmbientSpace(ambient_space.AmbientSpace):
    '''
    EXAMPLES::

        sage: R = RootSystem(["A",3])
        sage: e = R.ambient_space(); e
        Ambient space of the Root system of type [\'A\', 3]
        sage: TestSuite(e).run()                                                        # needs sage.graphs

    By default, this ambient space uses the barycentric projection for plotting::

        sage: # needs sage.symbolic
        sage: L = RootSystem(["A",2]).ambient_space()
        sage: e = L.basis()
        sage: L._plot_projection(e[0])
        (1/2, 989/1142)
        sage: L._plot_projection(e[1])
        (-1, 0)
        sage: L._plot_projection(e[2])
        (1/2, -989/1142)
        sage: L = RootSystem(["A",3]).ambient_space()
        sage: l = L.an_element(); l
        (2, 2, 3, 0)
        sage: L._plot_projection(l)
        (0, -1121/1189, 7/3)

    .. SEEALSO::

        - :meth:`sage.combinat.root_system.root_lattice_realizations.RootLatticeRealizations.ParentMethods._plot_projection`
    '''
    @classmethod
    def smallest_base_ring(cls, cartan_type=None):
        '''
        Return the smallest base ring the ambient space can be defined upon.

        .. SEEALSO:: :meth:`~sage.combinat.root_system.ambient_space.AmbientSpace.smallest_base_ring`

        EXAMPLES::

            sage: e = RootSystem(["A",3]).ambient_space()
            sage: e.smallest_base_ring()
            Integer Ring
        '''
    def dimension(self):
        '''
        EXAMPLES::

            sage: e = RootSystem(["A",3]).ambient_space()
            sage: e.dimension()
            4
        '''
    def root(self, i, j):
        """
        Note that indexing starts at 0.

        EXAMPLES::

            sage: e = RootSystem(['A',3]).ambient_lattice()
            sage: e.root(0,1)
            (1, -1, 0, 0)
        """
    def simple_root(self, i):
        """
        EXAMPLES::

            sage: e = RootSystem(['A',3]).ambient_lattice()
            sage: e.simple_roots()
            Finite family {1: (1, -1, 0, 0), 2: (0, 1, -1, 0), 3: (0, 0, 1, -1)}
        """
    def negative_roots(self):
        """
        EXAMPLES::

            sage: e = RootSystem(['A',3]).ambient_lattice()
            sage: e.negative_roots()
            [(-1, 1, 0, 0),
             (-1, 0, 1, 0),
             (-1, 0, 0, 1),
             (0, -1, 1, 0),
             (0, -1, 0, 1),
             (0, 0, -1, 1)]
        """
    def positive_roots(self):
        """
        EXAMPLES::

            sage: e = RootSystem(['A',3]).ambient_lattice()
            sage: e.positive_roots()
            [(1, -1, 0, 0),
             (1, 0, -1, 0),
             (0, 1, -1, 0),
             (1, 0, 0, -1),
             (0, 1, 0, -1),
             (0, 0, 1, -1)]
        """
    def highest_root(self):
        """
        EXAMPLES::

           sage: e = RootSystem(['A',3]).ambient_lattice()
           sage: e.highest_root()
           (1, 0, 0, -1)
        """
    def fundamental_weight(self, i):
        """
        EXAMPLES::

            sage: e = RootSystem(['A',3]).ambient_lattice()
            sage: e.fundamental_weights()
            Finite family {1: (1, 0, 0, 0), 2: (1, 1, 0, 0), 3: (1, 1, 1, 0)}
        """
    def det(self, k: int = 1):
        """
        Return the vector (1, ... ,1) which in the ['A',r]
        weight lattice, interpreted as a weight of GL(r+1,CC)
        is the determinant. If the optional parameter k is
        given, returns (k, ... ,k), the `k`-th power of the
        determinant.

        EXAMPLES::

            sage: e = RootSystem(['A',3]).ambient_space()
            sage: e.det(1/2)
            (1/2, 1/2, 1/2, 1/2)
        """

class CartanType(CartanType_standard_finite, CartanType_simply_laced, CartanType_simple):
    """
    Cartan Type `A_n`.

    .. SEEALSO:: :func:`~sage.combinat.root_systems.cartan_type.CartanType`
    """
    def __init__(self, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['A',4])
            sage: ct
            ['A', 4]
            sage: ct._repr_(compact = True)
            'A4'

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            True
            sage: ct.is_affine()
            False
            sage: ct.is_crystallographic()
            True
            sage: ct.is_simply_laced()
            True
            sage: ct.affine()
            ['A', 4, 1]
            sage: ct.dual()
            ['A', 4]

        TESTS::

            sage: TestSuite(ct).run()
        """
    AmbientSpace = AmbientSpace
    def coxeter_number(self):
        """
        Return the Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['A',4]).coxeter_number()
            5
        """
    def dual_coxeter_number(self):
        """
        Return the dual Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['A',4]).dual_coxeter_number()
            5
        """
    def dynkin_diagram(self):
        """
        Return the Dynkin diagram of type A.

        EXAMPLES::

            sage: a = CartanType(['A',3]).dynkin_diagram(); a                           # needs sage.graphs
            O---O---O
            1   2   3
            A3
            sage: a.edges(sort=True)                                                    # needs sage.graphs
            [(1, 2, 1), (2, 1, 1), (2, 3, 1), (3, 2, 1)]

        TESTS::

            sage: a = DynkinDiagram(['A',1]); a                                         # needs sage.graphs
            O
            1
            A1
            sage: a.vertices(sort=False), a.edges(sort=False)                           # needs sage.graphs
            ([1], [])
        """
    def ascii_art(self, label=None, node=None):
        """
        Return an ascii art representation of the Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['A',0]).ascii_art())
            sage: print(CartanType(['A',1]).ascii_art())
            O
            1
            sage: print(CartanType(['A',3]).ascii_art())
            O---O---O
            1   2   3
            sage: print(CartanType(['A',12]).ascii_art())
            O---O---O---O---O---O---O---O---O---O---O---O
            1   2   3   4   5   6   7   8   9   10  11  12
            sage: print(CartanType(['A',5]).ascii_art(label = lambda x: x+2))
            O---O---O---O---O
            3   4   5   6   7
            sage: print(CartanType(['A',5]).ascii_art(label = lambda x: x-2))
            O---O---O---O---O
            -1  0   1   2   3
        """
