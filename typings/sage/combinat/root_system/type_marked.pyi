from _typeshed import Incomplete
from sage.combinat.root_system import ambient_space as ambient_space, cartan_type as cartan_type
from sage.combinat.root_system.root_lattice_realizations import RootLatticeRealizations as RootLatticeRealizations
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute

class CartanType(cartan_type.CartanType_decorator):
    """
    A class for Cartan types with marked nodes.

    INPUT:

    - ``ct`` -- a Cartan type

    - ``marked_nodes`` -- list of marked nodes

    EXAMPLES:

    We take the Cartan type `B_4`::

        sage: T = CartanType(['B',4])
        sage: T.dynkin_diagram()                                                        # needs sage.graphs
        O---O---O=>=O
        1   2   3   4
        B4

    And mark some of its nodes::

        sage: T = T.marked_nodes([2,3])
        sage: T.dynkin_diagram()                                                        # needs sage.graphs
        O---X---X=>=O
        1   2   3   4
        B4 with nodes (2, 3) marked

    Markings are not additive::

        sage: T.marked_nodes([1,4]).dynkin_diagram()                                    # needs sage.graphs
        X---O---O=>=X
        1   2   3   4
        B4 with nodes (1, 4) marked

    And trivial relabelling are honoured nicely::

        sage: T = T.marked_nodes([])
        sage: T.dynkin_diagram()                                                        # needs sage.graphs
        O---O---O=>=O
        1   2   3   4
        B4
    """
    @staticmethod
    def __classcall__(cls, ct, marked_nodes):
        """
        This standardizes the input of the constructor to ensure
        unique representation.

        EXAMPLES::

            sage: ct1 = CartanType(['B',2]).marked_nodes([1,2])
            sage: ct2 = CartanType(['B',2]).marked_nodes([2,1])
            sage: ct3 = CartanType(['B',2]).marked_nodes((1,2))
            sage: ct4 = CartanType(['D',4]).marked_nodes([1,2])
            sage: ct1 is ct2
            True
            sage: ct1 is ct3
            True
            sage: ct1 == ct4
            False
        """
    __class__: Incomplete
    def __init__(self, ct, marked_nodes) -> None:
        """
        Return an isomorphic Cartan type obtained by marking the
        nodes of the Dynkin diagram.

        TESTS:

        Test that the produced Cartan type is in the appropriate
        abstract classes::

            sage: ct = CartanType(['B',4]).marked_nodes([1,2])
            sage: TestSuite(ct).run()
            sage: from sage.combinat.root_system import cartan_type
            sage: isinstance(ct, cartan_type.CartanType_finite)
            True
            sage: isinstance(ct, cartan_type.CartanType_simple)
            True
            sage: isinstance(ct, cartan_type.CartanType_affine)
            False
            sage: isinstance(ct, cartan_type.CartanType_crystallographic)
            True
            sage: isinstance(ct, cartan_type.CartanType_simply_laced)
            False

            sage: ct = CartanType(['A',3,1]).marked_nodes([1,2])
            sage: TestSuite(ct).run()
            sage: isinstance(ct, cartan_type.CartanType_simple)
            True
            sage: isinstance(ct, cartan_type.CartanType_finite)
            False
            sage: isinstance(ct, cartan_type.CartanType_affine)
            True
            sage: isinstance(ct, cartan_type.CartanType_crystallographic)
            True
            sage: isinstance(ct, cartan_type.CartanType_simply_laced)
            True
        """
    def ascii_art(self, label=None, node=None):
        '''
        Return an ascii art representation of this Cartan type.

        EXAMPLES::

            sage: print(CartanType(["G", 2]).marked_nodes([2]).ascii_art())
              3
            O=<=X
            1   2
            sage: print(CartanType(["B", 3, 1]).marked_nodes([0, 3]).ascii_art())
                X 0
                |
                |
            O---O=>=X
            1   2   3
            sage: print(CartanType(["F", 4, 1]).marked_nodes([0, 2]).ascii_art())
            X---O---X=>=O---O
            0   1   2   3   4
        '''
    def dynkin_diagram(self):
        '''
        Return the Dynkin diagram for this Cartan type.

        EXAMPLES::

            sage: CartanType(["G", 2]).marked_nodes([2]).dynkin_diagram()               # needs sage.graphs
              3
            O=<=X
            1   2
            G2 with node 2 marked

        TESTS:

        To be compared with the examples in :meth:`ascii_art`::

            sage: CartanType(["G", 2]).relabel({1:2,2:1}).dynkin_diagram().edges(sort=True)         # needs sage.graphs
            [(1, 2, 3), (2, 1, 1)]
            sage: CartanType(["B", 3, 1]).relabel([1,3,2,0]).dynkin_diagram().edges(sort=True)      # needs sage.graphs
            [(0, 2, 1), (1, 2, 1), (2, 0, 2), (2, 1, 1), (2, 3, 1), (3, 2, 1)]
            sage: CartanType(["F", 4, 1]).relabel(lambda n: 4-n).dynkin_diagram().edges(sort=True)  # needs sage.graphs
            [(0, 1, 1), (1, 0, 1), (1, 2, 1), (2, 1, 2), (2, 3, 1), (3, 2, 1), (3, 4, 1), (4, 3, 1)]
        '''
    def dual(self):
        '''
        Implement
        :meth:`sage.combinat.root_system.cartan_type.CartanType_abstract.dual`,
        using that taking the dual and marking nodes are commuting operations.

        EXAMPLES::

            sage: T = CartanType(["BC",3, 2])
            sage: T.marked_nodes([1,3]).dual().dynkin_diagram()                         # needs sage.graphs
            O=>=X---O=>=X
            0   1   2   3
            BC3~* with nodes (1, 3) marked
            sage: T.dual().marked_nodes([1,3]).dynkin_diagram()                         # needs sage.graphs
            O=>=X---O=>=X
            0   1   2   3
            BC3~* with nodes (1, 3) marked
        '''
    def relabel(self, relabelling):
        '''
        Return the relabelling of ``self``.

        EXAMPLES::

            sage: T = CartanType(["BC",3, 2])
            sage: T.marked_nodes([1,3]).relabel(lambda x: x+2).dynkin_diagram()         # needs sage.graphs
            O=<=X---O=<=X
            2   3   4   5
            BC3~ relabelled by {0: 2, 1: 3, 2: 4, 3: 5} with nodes (3, 5) marked
            sage: T.relabel(lambda x: x+2).marked_nodes([3,5]).dynkin_diagram()         # needs sage.graphs
            O=<=X---O=<=X
            2   3   4   5
            BC3~ relabelled by {0: 2, 1: 3, 2: 4, 3: 5} with nodes (3, 5) marked
        '''
    def marked_nodes(self, marked_nodes):
        """
        Return ``self`` with nodes ``marked_nodes`` marked.

        EXAMPLES::

            sage: ct = CartanType(['A',12])
            sage: m = ct.marked_nodes([1,4,6,7,8,12]); m
            ['A', 12] with nodes (1, 4, 6, 7, 8, 12) marked
            sage: m.marked_nodes([2])
            ['A', 12] with node 2 marked
            sage: m.marked_nodes([]) is ct
            True
        """
    def type(self):
        """
        Return the type of ``self`` or ``None`` if unknown.

        EXAMPLES::

            sage: ct = CartanType(['F', 4]).marked_nodes([1,3])
            sage: ct.type()
            'F'
        """

class AmbientSpace(ambient_space.AmbientSpace):
    '''
    Ambient space for a marked finite Cartan type.

    It is constructed in the canonical way from the ambient space of
    the original Cartan type.

    EXAMPLES::

        sage: L = CartanType(["F",4]).marked_nodes([1,3]).root_system().ambient_space(); L
        Ambient space of the Root system of type [\'F\', 4] with nodes (1, 3) marked
        sage: TestSuite(L).run()                                                        # needs sage.graphs
    '''
    def dimension(self):
        '''
        Return the dimension of this ambient space.

        .. SEEALSO:: :meth:`sage.combinat.root_system.ambient_space.AmbientSpace.dimension`

        EXAMPLES::

            sage: L = CartanType(["F",4]).marked_nodes([1,3]).root_system().ambient_space()
            sage: L.dimension()
            4
        '''
    @cached_method
    def simple_root(self, i):
        '''
        Return the ``i``-th simple root.

        It is constructed by looking up the corresponding simple
        coroot in the ambient space for the original Cartan type.

        EXAMPLES::

            sage: L = CartanType(["F",4]).marked_nodes([1,3]).root_system().ambient_space()
            sage: L.simple_root(1)
            (0, 1, -1, 0)
            sage: L.simple_roots()
            Finite family {1: (0, 1, -1, 0), 2: (0, 0, 1, -1),
                           3: (0, 0, 0, 1), 4: (1/2, -1/2, -1/2, -1/2)}
            sage: L.simple_coroots()
            Finite family {1: (0, 1, -1, 0), 2: (0, 0, 1, -1),
                           3: (0, 0, 0, 2), 4: (1, -1, -1, -1)}
        '''
    @cached_method
    def fundamental_weight(self, i):
        '''
        Return the ``i``-th fundamental weight.

        It is constructed by looking up the corresponding simple
        coroot in the ambient space for the original Cartan type.

        EXAMPLES::

            sage: L = CartanType(["F",4]).marked_nodes([1,3]).root_system().ambient_space()
            sage: L.fundamental_weight(1)
            (1, 1, 0, 0)
            sage: L.fundamental_weights()
            Finite family {1: (1, 1, 0, 0), 2: (2, 1, 1, 0),
                           3: (3/2, 1/2, 1/2, 1/2), 4: (1, 0, 0, 0)}
        '''

class CartanType_finite(CartanType, cartan_type.CartanType_finite):
    AmbientSpace = AmbientSpace
    def affine(self):
        """
        Return the affine Cartan type associated with ``self``.

        EXAMPLES::

            sage: B4 = CartanType(['B',4]).marked_nodes([1,3])
            sage: B4.dynkin_diagram()                                                   # needs sage.graphs
            X---O---X=>=O
            1   2   3   4
            B4 with nodes (1, 3) marked
            sage: B4.affine().dynkin_diagram()                                          # needs sage.graphs
                O 0
                |
                |
            X---O---X=>=O
            1   2   3   4
            B4~ with nodes (1, 3) marked

        TESTS:

        Check that we don't inadvertently change the internal
        marking of ``ct``::

            sage: ct = CartanType(['F', 4]).marked_nodes([1,3])
            sage: ct.affine()
            ['F', 4, 1] with nodes (1, 3) marked
            sage: ct
            ['F', 4] with nodes (1, 3) marked
        """

class CartanType_affine(CartanType, cartan_type.CartanType_affine):
    """
    TESTS::

        sage: ct = CartanType(['B',3,1]).marked_nodes([1,3])
        sage: ct
        ['B', 3, 1] with nodes (1, 3) marked

        sage: L = ct.root_system().ambient_space(); L
        Ambient space of the Root system of type ['B', 3, 1] with nodes (1, 3) marked
        sage: L.classical()
        Ambient space of the Root system of type ['B', 3] with nodes (1, 3) marked
        sage: TestSuite(L).run()
    """
    def classical(self):
        """
        Return the classical Cartan type associated with ``self``.

        EXAMPLES::

            sage: T = CartanType(['A',4,1]).marked_nodes([0,2,4])
            sage: T.dynkin_diagram()                                                    # needs sage.graphs
            0
            X-----------+
            |           |
            |           |
            O---X---O---X
            1   2   3   4
            A4~ with nodes (0, 2, 4) marked

            sage: T0 = T.classical(); T0
            ['A', 4] with nodes (2, 4) marked
            sage: T0.dynkin_diagram()                                                   # needs sage.graphs
            O---X---O---X
            1   2   3   4
            A4 with nodes (2, 4) marked
        """
    def basic_untwisted(self):
        """
        Return the basic untwisted Cartan type associated with this affine
        Cartan type.

        Given an affine type `X_n^{(r)}`, the basic untwisted type is `X_n`.
        In other words, it is the classical Cartan type that is twisted to
        obtain ``self``.

        EXAMPLES::

            sage: CartanType(['A', 7, 2]).marked_nodes([1,3]).basic_untwisted()
            ['A', 7] with nodes (1, 3) marked
            sage: CartanType(['D', 4, 3]).marked_nodes([0,2]).basic_untwisted()
            ['D', 4] with node 2 marked
        """
    def special_node(self):
        """
        Return the special node of the Cartan type.

        .. SEEALSO:: :meth:`~sage.combinat.root_system.CartanType_affine.special_node`

        It is the special node of the non-marked Cartan type..

        EXAMPLES::

            sage: CartanType(['B', 3, 1]).marked_nodes([1,3]).special_node()
            0
        """
    def is_untwisted_affine(self):
        """
        Implement :meth:`CartanType_affine.is_untwisted_affine`.

        A marked Cartan type is untwisted affine if the original is.

        EXAMPLES::

            sage: CartanType(['B', 3, 1]).marked_nodes([1,3]).is_untwisted_affine()
            True
        """
