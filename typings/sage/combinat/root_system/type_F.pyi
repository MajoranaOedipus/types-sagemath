from . import ambient_space as ambient_space
from .cartan_type import CartanType_crystallographic as CartanType_crystallographic, CartanType_simple as CartanType_simple, CartanType_standard_finite as CartanType_standard_finite
from _typeshed import Incomplete
from sage.misc.persist import register_unpickle_override as register_unpickle_override
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family

class AmbientSpace(ambient_space.AmbientSpace):
    """
    The lattice behind `F_4`.  The computations are based on Bourbaki,
    Groupes et Algèbres de Lie, Ch. 4,5,6 (planche VIII).
    """
    Base: Incomplete
    def __init__(self, root_system, base_ring) -> None:
        """
        Initialize the ambient lattice for the root system of type `F_4`.

        This essentially initializes ``Base`` with the coordinates of
        the simple roots in the canonical basis for `\\RR^4`.

        EXAMPLES::

            sage: e = RootSystem(['F',4]).ambient_space()

        TESTS::

            sage: TestSuite(e).run()                                                    # needs sage.graphs
        """
    def dimension(self):
        """
        Return the dimension of ``self``.

        EXAMPLES::

            sage: e = RootSystem(['F',4]).ambient_space()
            sage: e.dimension()
            4
        """
    def root(self, i, j=None, k=None, l=None, p1: int = 0, p2: int = 0, p3: int = 0, p4: int = 0):
        """
        Compute a root from base elements of the underlying lattice.
        The arguments specify the basis elements and the signs.
        Sadly, the base elements are indexed zero-based.
        We assume that if one of the indices is not given, the rest are not as well.

        EXAMPLES::

            sage: e = RootSystem(['F',4]).ambient_space()
            sage: [ e.root(i,j,p2=1) for i in range(e.n) for j in range(i+1,e.n) ]
            [(1, -1, 0, 0), (1, 0, -1, 0), (1, 0, 0, -1), (0, 1, -1, 0), (0, 1, 0, -1), (0, 0, 1, -1)]
        """
    def simple_root(self, i):
        """
        Return the `i`-th simple root.

        It is computed according to what Bourbaki calls the Base:

        .. MATH::

            \\alpha_1 = \\epsilon_2-\\epsilon_3,
            \\alpha_2 = \\epsilon_3-\\epsilon_4,
            \\alpha_3 = \\epsilon_4,
            \\alpha_4 = \\frac{1}{2} \\left( \\epsilon_1-\\epsilon_2-\\epsilon_3-\\epsilon_4 \\right).

        EXAMPLES::

            sage: e = RootSystem(['F',4]).ambient_space()
            sage: e.simple_roots()
            Finite family {1: (0, 1, -1, 0), 2: (0, 0, 1, -1), 3: (0, 0, 0, 1), 4: (1/2, -1/2, -1/2, -1/2)}
        """
    def negative_roots(self):
        """
        Return the negative roots.

        EXAMPLES::

            sage: e = RootSystem(['F',4]).ambient_space()
            sage: e.negative_roots()
            [(-1, 0, 0, 0),
            (0, -1, 0, 0),
            (0, 0, -1, 0),
            (0, 0, 0, -1),
            (-1, -1, 0, 0),
            (-1, 0, -1, 0),
            (-1, 0, 0, -1),
            (0, -1, -1, 0),
            (0, -1, 0, -1),
            (0, 0, -1, -1),
            (-1, 1, 0, 0),
            (-1, 0, 1, 0),
            (-1, 0, 0, 1),
            (0, -1, 1, 0),
            (0, -1, 0, 1),
            (0, 0, -1, 1),
            (-1/2, -1/2, -1/2, -1/2),
            (-1/2, -1/2, -1/2, 1/2),
            (-1/2, -1/2, 1/2, -1/2),
            (-1/2, -1/2, 1/2, 1/2),
            (-1/2, 1/2, -1/2, -1/2),
            (-1/2, 1/2, -1/2, 1/2),
            (-1/2, 1/2, 1/2, -1/2),
            (-1/2, 1/2, 1/2, 1/2)]
        """
    PosRoots: Incomplete
    def positive_roots(self):
        """
        Return the positive roots.

        These are the roots which are positive with respect to the
        lexicographic ordering of the basis elements
        (`\\epsilon_1<\\epsilon_2<\\epsilon_3<\\epsilon_4`).

        EXAMPLES::

            sage: e = RootSystem(['F',4]).ambient_space()
            sage: e.positive_roots()
            [(1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1),
            (1, 1, 0, 0),
            (1, 0, 1, 0),
            (1, 0, 0, 1),
            (0, 1, 1, 0),
            (0, 1, 0, 1),
            (0, 0, 1, 1),
            (1, -1, 0, 0),
            (1, 0, -1, 0),
            (1, 0, 0, -1),
            (0, 1, -1, 0),
            (0, 1, 0, -1),
            (0, 0, 1, -1),
            (1/2, 1/2, 1/2, 1/2),
            (1/2, 1/2, 1/2, -1/2),
            (1/2, 1/2, -1/2, 1/2),
            (1/2, 1/2, -1/2, -1/2),
            (1/2, -1/2, 1/2, 1/2),
            (1/2, -1/2, 1/2, -1/2),
            (1/2, -1/2, -1/2, 1/2),
            (1/2, -1/2, -1/2, -1/2)]
            sage: e.rho()
            (11/2, 5/2, 3/2, 1/2)
        """
    def fundamental_weights(self):
        """
        Return the fundamental weights of ``self``.

        EXAMPLES::

            sage: e =  RootSystem(['F',4]).ambient_space()
            sage: e.fundamental_weights()
            Finite family {1: (1, 1, 0, 0), 2: (2, 1, 1, 0), 3: (3/2, 1/2, 1/2, 1/2), 4: (1, 0, 0, 0)}
        """

class CartanType(CartanType_standard_finite, CartanType_simple, CartanType_crystallographic):
    def __init__(self) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['F',4])
            sage: ct
            ['F', 4]
            sage: ct._repr_(compact = True)
            'F4'

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            True
            sage: ct.is_crystallographic()
            True
            sage: ct.is_simply_laced()
            False
            sage: ct.dual()
            ['F', 4] relabelled by {1: 4, 2: 3, 3: 2, 4: 1}
            sage: ct.affine()
            ['F', 4, 1]

        TESTS::

            sage: TestSuite(ct).run()
        """
    AmbientSpace = AmbientSpace
    def coxeter_number(self):
        """
        Return the Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['F',4]).coxeter_number()
            12
        """
    def dual_coxeter_number(self):
        """
        Return the dual Coxeter number associated with ``self``.

        EXAMPLES::

            sage: CartanType(['F',4]).dual_coxeter_number()
            9
        """
    def dynkin_diagram(self):
        """
        Return a Dynkin diagram for type F.

        EXAMPLES::

            sage: f = CartanType(['F',4]).dynkin_diagram(); f                           # needs sage.graphs
            O---O=>=O---O
            1   2   3   4
            F4
            sage: f.edges(sort=True)                                                    # needs sage.graphs
            [(1, 2, 1), (2, 1, 1), (2, 3, 2), (3, 2, 1), (3, 4, 1), (4, 3, 1)]
        """
    def ascii_art(self, label=None, node=None):
        """
        Return an ascii art representation of the extended Dynkin diagram.

        EXAMPLES::

            sage: print(CartanType(['F',4]).ascii_art(label = lambda x: x+2))
            O---O=>=O---O
            3   4   5   6
            sage: print(CartanType(['F',4]).ascii_art(label = lambda x: x-2))
            O---O=>=O---O
            -1  0   1   2
        """
    def dual(self):
        """
        Return the dual Cartan type.

        This uses that `F_4` is self-dual up to relabelling.

        EXAMPLES::

            sage: F4 = CartanType(['F',4])
            sage: F4.dual()
            ['F', 4] relabelled by {1: 4, 2: 3, 3: 2, 4: 1}

            sage: F4.dynkin_diagram()                                                   # needs sage.graphs
            O---O=>=O---O
            1   2   3   4
            F4
            sage: F4.dual().dynkin_diagram()                                            # needs sage.graphs
            O---O=>=O---O
            4   3   2   1
            F4 relabelled by {1: 4, 2: 3, 3: 2, 4: 1}
        """
