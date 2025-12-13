from . import ambient_space as ambient_space
from .cartan_type import CartanType_crystallographic as CartanType_crystallographic, CartanType_simple as CartanType_simple, CartanType_standard_finite as CartanType_standard_finite
from sage.combinat.root_system.root_lattice_realizations import RootLatticeRealizations as RootLatticeRealizations
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.sets.family import Family as Family

class AmbientSpace(ambient_space.AmbientSpace):
    '''
    EXAMPLES::

        sage: e = RootSystem([\'G\',2]).ambient_space(); e
        Ambient space of the Root system of type [\'G\', 2]

    One can not construct the ambient lattice because the simple
    coroots have rational coefficients::

        sage: e.simple_coroots()
        Finite family {1: (0, 1, -1), 2: (1/3, -2/3, 1/3)}
        sage: e.smallest_base_ring()
        Rational Field

    By default, this ambient space uses the barycentric projection for plotting::

        sage: # needs sage.symbolic
        sage: L = RootSystem(["G",2]).ambient_space()
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

    TESTS::

        sage: TestSuite(e).run()
        sage: [WeylDim([\'G\',2],[a,b]) for a,b in [[0,0], [1,0], [0,1], [1,1]]] # indirect doctest
        [1, 7, 14, 64]
    '''
    def dimension(self):
        """
        EXAMPLES::

            sage: e = RootSystem(['G',2]).ambient_space()
            sage: e.dimension()
            3
        """
    def simple_root(self, i):
        """
        EXAMPLES::

            sage: CartanType(['G',2]).root_system().ambient_space().simple_roots()
            Finite family {1: (0, 1, -1), 2: (1, -2, 1)}
        """
    def positive_roots(self):
        """
        EXAMPLES::

            sage: CartanType(['G',2]).root_system().ambient_space().positive_roots()
            [(0, 1, -1), (1, -2, 1), (1, -1, 0), (1, 0, -1), (1, 1, -2), (2, -1, -1)]
        """
    def negative_roots(self):
        """
        EXAMPLES::

            sage: CartanType(['G',2]).root_system().ambient_space().negative_roots()
            [(0, -1, 1), (-1, 2, -1), (-1, 1, 0), (-1, 0, 1), (-1, -1, 2), (-2, 1, 1)]
        """
    def fundamental_weights(self):
        """
        EXAMPLES::

            sage: CartanType(['G',2]).root_system().ambient_space().fundamental_weights()
            Finite family {1: (1, 0, -1), 2: (2, -1, -1)}
        """

class CartanType(CartanType_standard_finite, CartanType_simple, CartanType_crystallographic):
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['G',2])
            sage: ct
            ['G', 2]
            sage: ct._repr_(compact = True)
            'G2'

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            True
            sage: ct.is_crystallographic()
            True
            sage: ct.is_simply_laced()
            False
            sage: ct.dual()
            ['G', 2] relabelled by {1: 2, 2: 1}
            sage: ct.affine()
            ['G', 2, 1]

        TESTS::

            sage: TestSuite(ct).run()
        """
    AmbientSpace = AmbientSpace
    def coxeter_number(self):
        """
        Return the Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['G',2]).coxeter_number()
            6
        """
    def dual_coxeter_number(self):
        """
        Return the dual Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['G',2]).dual_coxeter_number()
            4
        """
    def dynkin_diagram(self):
        """
        Return a Dynkin diagram for type G.

        EXAMPLES::

            sage: g = CartanType(['G',2]).dynkin_diagram(); g                           # needs sage.graphs
              3
            O=<=O
            1   2
            G2
            sage: g.edges(sort=True)                                                    # needs sage.graphs
            [(1, 2, 1), (2, 1, 3)]
        """
    def ascii_art(self, label=None, node=None):
        """
        Return an ascii art representation of the Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['G',2]).ascii_art(label=lambda x: x+2))
              3
            O=<=O
            3   4
        """
    def dual(self):
        """
        Return the dual Cartan type.

        This uses that `G_2` is self-dual up to relabelling.

        EXAMPLES::

            sage: G2 = CartanType(['G',2])
            sage: G2.dual()
            ['G', 2] relabelled by {1: 2, 2: 1}

            sage: G2.dynkin_diagram()                                                   # needs sage.graphs
              3
            O=<=O
            1   2
            G2
            sage: G2.dual().dynkin_diagram()                                            # needs sage.graphs
              3
            O=<=O
            2   1
            G2 relabelled by {1: 2, 2: 1}
        """
