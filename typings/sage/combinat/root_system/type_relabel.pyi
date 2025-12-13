from _typeshed import Incomplete
from sage.combinat.root_system import ambient_space as ambient_space, cartan_type as cartan_type
from sage.combinat.root_system.root_lattice_realizations import RootLatticeRealizations as RootLatticeRealizations
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_attribute import lazy_attribute as lazy_attribute
from sage.sets.family import Family as Family, FiniteFamily as FiniteFamily

class CartanType(cartan_type.CartanType_decorator):
    """
    A class for relabelled Cartan types.
    """
    @staticmethod
    def __classcall__(cls, type, relabelling):
        """
        This standardizes the input of the constructor to ensure
        unique representation.

        EXAMPLES::

            sage: ct1 = CartanType(['B',2]).relabel({1:2, 2:1})    # indirect doctest
            sage: ct2 = CartanType(['B',2]).relabel(lambda x: 3-x)
            sage: ct3 = CartanType(['B',2]).relabel({1:3, 2: 4})
            sage: ct4 = CartanType(['D',4]).relabel(lambda x: 3-x)
            sage: ct1 == ct2
            True
            sage: ct1 == ct3
            False
            sage: ct1 == ct4
            False
        """
    __class__: Incomplete
    def __init__(self, type, relabelling) -> None:
        '''
        INPUT:

        - ``type`` -- a Cartan type

        - ``relabelling`` -- a function (or a list, or a dictionary)

        Returns an isomorphic Cartan type obtained by relabelling the
        nodes of the Dynkin diagram. Namely the node with label ``i``
        is relabelled ``f(i)`` (or, by ``f[i]`` if ``f`` is a list or
        dictionary).

        EXAMPLES:

        We take the Cartan type `B_4`::

            sage: T = CartanType([\'B\',4])
            sage: T.dynkin_diagram()                                                    # needs sage.graphs
            O---O---O=>=O
            1   2   3   4
            B4

        And relabel its nodes::

            sage: cycle = {1:2, 2:3, 3:4, 4:1}

            sage: T = T.relabel(cycle)
            sage: T.dynkin_diagram()                                                    # needs sage.graphs
            O---O---O=>=O
            2   3   4   1
            B4 relabelled by {1: 2, 2: 3, 3: 4, 4: 1}
            sage: T.dynkin_diagram().edges(sort=True)                                   # needs sage.graphs
            [(1, 4, 1), (2, 3, 1), (3, 2, 1), (3, 4, 1), (4, 1, 2), (4, 3, 1)]

        Multiple relabelling are recomposed into a single one::

            sage: T = T.relabel(cycle)
            sage: T.dynkin_diagram()                                                    # needs sage.graphs
            O---O---O=>=O
            3   4   1   2
            B4 relabelled by {1: 3, 2: 4, 3: 1, 4: 2}

            sage: T = T.relabel(cycle)
            sage: T.dynkin_diagram()                                                    # needs sage.graphs
            O---O---O=>=O
            4   1   2   3
            B4 relabelled by {1: 4, 2: 1, 3: 2, 4: 3}

        And trivial relabelling are honoured nicely::

            sage: T = T.relabel(cycle)
            sage: T.dynkin_diagram()                                                    # needs sage.graphs
            O---O---O=>=O
            1   2   3   4
            B4

        TESTS:

        Test that the produced Cartan type is in the appropriate
        abstract classes (see :issue:`13724`)::

            sage: ct = CartanType([\'B\',4]).relabel(cycle)
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

            sage: ct = CartanType([\'A\',3,1]).relabel({0:3,1:2, 2:1,3:0})
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

        Check for the original issues of :issue:`13724`::

            sage: A3 = CartanType("A3")
            sage: A3.cartan_matrix()                                                    # needs sage.graphs
            [ 2 -1  0]
            [-1  2 -1]
            [ 0 -1  2]
            sage: A3r = A3.relabel({1:2,2:3,3:1})
            sage: A3r.cartan_matrix()                                                   # needs sage.graphs
            [ 2  0 -1]
            [ 0  2 -1]
            [-1 -1  2]

            sage: ct = CartanType(["D",4,3]).classical(); ct
            [\'G\', 2]
            sage: ct.symmetrizer()                                                      # needs sage.graphs
            Finite family {1: 1, 2: 3}

        Check the underlying issue of :issue:`24892`, that the root system
        of a relabelled non-crystallographic Cartan type has an
        ``ambient_space()`` that does not result in an error (note that
        this should actually return a valid ambient space, which requires
        the non-crystallographic finite types to have them implemented)::

            sage: rI5 = CartanType([\'I\',5]).relabel({1:0,2:1})
            sage: rI5.root_system().ambient_space()
        '''
    def ascii_art(self, label=None, node=None):
        '''
        Return an ascii art representation of this Cartan type.

        EXAMPLES::

            sage: print(CartanType(["G", 2]).relabel({1:2,2:1}).ascii_art())
              3
            O=<=O
            2   1
            sage: print(CartanType(["B", 3, 1]).relabel([1,3,2,0]).ascii_art())
                O 1
                |
                |
            O---O=>=O
            3   2   0
            sage: print(CartanType(["F", 4, 1]).relabel(lambda n: 4-n).ascii_art())
            O---O---O=>=O---O
            4   3   2   1   0
        '''
    def dynkin_diagram(self):
        '''
        Return the Dynkin diagram for this Cartan type.

        EXAMPLES::

            sage: CartanType(["G", 2]).relabel({1:2,2:1}).dynkin_diagram()              # needs sage.graphs
              3
            O=<=O
            2   1
            G2 relabelled by {1: 2, 2: 1}

        TESTS:

        To be compared with the examples in :meth:`ascii_art`::

            sage: CartanType(["G", 2]).relabel({1:2,2:1}).dynkin_diagram().edges(sort=True)         # needs sage.graphs
            [(1, 2, 3), (2, 1, 1)]
            sage: CartanType(["B", 3, 1]).relabel([1,3,2,0]).dynkin_diagram().edges(sort=True)      # needs sage.graphs
            [(0, 2, 1), (1, 2, 1), (2, 0, 2), (2, 1, 1), (2, 3, 1), (3, 2, 1)]
            sage: CartanType(["F", 4, 1]).relabel(lambda n: 4-n).dynkin_diagram().edges(sort=True)  # needs sage.graphs
            [(0, 1, 1), (1, 0, 1), (1, 2, 1), (2, 1, 2), (2, 3, 1), (3, 2, 1), (3, 4, 1), (4, 3, 1)]
        '''
    def index_set(self):
        """
        EXAMPLES::

            sage: ct = CartanType(['G', 2]).relabel({1:2,2:1})
            sage: ct.index_set()
            (1, 2)
        """
    def dual(self):
        '''
        Implement :meth:`sage.combinat.root_system.cartan_type.CartanType_abstract.dual`,
        using that taking the dual and relabelling are commuting operations.

        EXAMPLES::

            sage: T = CartanType(["BC",3, 2])
            sage: cycle = {1:2, 2:3, 3:0, 0:1}
            sage: T.relabel(cycle).dual().dynkin_diagram()                              # needs sage.graphs
            O=>=O---O=>=O
            1   2   3   0
            BC3~* relabelled by {0: 1, 1: 2, 2: 3, 3: 0}
            sage: T.dual().relabel(cycle).dynkin_diagram()                              # needs sage.graphs
            O=>=O---O=>=O
            1   2   3   0
            BC3~* relabelled by {0: 1, 1: 2, 2: 3, 3: 0}
        '''
    def type(self):
        """
        Return the type of ``self`` or ``None`` if unknown.

        EXAMPLES::

            sage: ct = CartanType(['G', 2]).relabel({1:2,2:1})
            sage: ct.type()
            'G'
        """
    @cached_method
    def coxeter_diagram(self):
        """
        Return the Coxeter diagram for ``self``.

        EXAMPLES::

            sage: ct = CartanType(['H', 3]).relabel({1:3,2:2,3:1})
            sage: G = ct.coxeter_diagram(); G                                           # needs sage.graphs
            Graph on 3 vertices
            sage: G.edges(sort=True)                                                    # needs sage.graphs
            [(1, 2, 5), (2, 3, 3)]
        """

class AmbientSpace(ambient_space.AmbientSpace):
    '''
    Ambient space for a relabelled finite Cartan type.

    It is constructed in the canonical way from the ambient space of
    the original Cartan type, by relabelling the simple roots,
    fundamental weights, etc.

    EXAMPLES::

        sage: cycle = {1:2, 2:3, 3:4, 4:1}
        sage: L = CartanType(["F",4]).relabel(cycle).root_system().ambient_space(); L
        Ambient space of the Root system of type [\'F\', 4] relabelled by {1: 2, 2: 3, 3: 4, 4: 1}
        sage: TestSuite(L).run()                                                        # needs sage.graphs
    '''
    def dimension(self):
        '''
        Return the dimension of this ambient space.

        .. SEEALSO:: :meth:`sage.combinat.root_system.ambient_space.AmbientSpace.dimension`

        EXAMPLES::

            sage: cycle = {1:2, 2:3, 3:4, 4:1}
            sage: L = CartanType(["F",4]).relabel(cycle).root_system().ambient_space()
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

            sage: cycle = {1:2, 2:3, 3:4, 4:1}
            sage: L = CartanType(["F",4]).relabel(cycle).root_system().ambient_space()
            sage: K = CartanType(["F",4]).root_system().ambient_space()
            sage: K.simple_roots()
            Finite family {1: (0, 1, -1, 0), 2: (0, 0, 1, -1), 3: (0, 0, 0, 1), 4: (1/2, -1/2, -1/2, -1/2)}
            sage: K.simple_coroots()
            Finite family {1: (0, 1, -1, 0), 2: (0, 0, 1, -1), 3: (0, 0, 0, 2), 4: (1, -1, -1, -1)}
            sage: L.simple_root(1)
            (1/2, -1/2, -1/2, -1/2)

            sage: L.simple_roots()
            Finite family {1: (1/2, -1/2, -1/2, -1/2), 2: (0, 1, -1, 0), 3: (0, 0, 1, -1), 4: (0, 0, 0, 1)}

            sage: L.simple_coroots()
            Finite family {1: (1, -1, -1, -1), 2: (0, 1, -1, 0), 3: (0, 0, 1, -1), 4: (0, 0, 0, 2)}
        '''
    @cached_method
    def fundamental_weight(self, i):
        '''
        Return the ``i``-th fundamental weight.

        It is constructed by looking up the corresponding simple
        coroot in the ambient space for the original Cartan type.

        EXAMPLES::

            sage: cycle = {1:2, 2:3, 3:4, 4:1}
            sage: L = CartanType(["F",4]).relabel(cycle).root_system().ambient_space()
            sage: K = CartanType(["F",4]).root_system().ambient_space()
            sage: K.fundamental_weights()
            Finite family {1: (1, 1, 0, 0), 2: (2, 1, 1, 0), 3: (3/2, 1/2, 1/2, 1/2), 4: (1, 0, 0, 0)}
            sage: L.fundamental_weight(1)
            (1, 0, 0, 0)
            sage: L.fundamental_weights()
            Finite family {1: (1, 0, 0, 0), 2: (1, 1, 0, 0), 3: (2, 1, 1, 0), 4: (3/2, 1/2, 1/2, 1/2)}
        '''

class CartanType_finite(CartanType, cartan_type.CartanType_finite):
    AmbientSpace = AmbientSpace
    def affine(self):
        '''
        Return the affine Cartan type associated with ``self``.

        EXAMPLES::

            sage: B4 = CartanType([\'B\',4])
            sage: B4.dynkin_diagram()                                                   # needs sage.graphs
            O---O---O=>=O
            1   2   3   4
            B4
            sage: B4.affine().dynkin_diagram()                                          # needs sage.graphs
                O 0
                |
                |
            O---O---O=>=O
            1   2   3   4
            B4~

        If possible, this reuses the original label for the special node::

            sage: T = B4.relabel({1:2, 2:3, 3:4, 4:1}); T.dynkin_diagram()              # needs sage.graphs
            O---O---O=>=O
            2   3   4   1
            B4 relabelled by {1: 2, 2: 3, 3: 4, 4: 1}
            sage: T.affine().dynkin_diagram()                                           # needs sage.graphs
                O 0
                |
                |
            O---O---O=>=O
            2   3   4   1
            B4~ relabelled by {0: 0, 1: 2, 2: 3, 3: 4, 4: 1}

        Otherwise, it chooses a label for the special_node in `0,1,...`::

            sage: T = B4.relabel({1:0, 2:1, 3:2, 4:3}); T.dynkin_diagram()              # needs sage.graphs
            O---O---O=>=O
            0   1   2   3
            B4 relabelled by {1: 0, 2: 1, 3: 2, 4: 3}
            sage: T.affine().dynkin_diagram()                                           # needs sage.graphs
                O 4
                |
                |
            O---O---O=>=O
            0   1   2   3
            B4~ relabelled by {0: 4, 1: 0, 2: 1, 3: 2, 4: 3}

        This failed before :issue:`13724`::

            sage: ct = CartanType(["G",2]).dual(); ct
            [\'G\', 2] relabelled by {1: 2, 2: 1}
            sage: ct.affine()
            [\'G\', 2, 1] relabelled by {0: 0, 1: 2, 2: 1}

            sage: ct = CartanType(["F",4]).dual(); ct
            [\'F\', 4] relabelled by {1: 4, 2: 3, 3: 2, 4: 1}
            sage: ct.affine()
            [\'F\', 4, 1] relabelled by {0: 0, 1: 4, 2: 3, 3: 2, 4: 1}

        Check that we don\'t inadvertently change the internal
        relabelling of ``ct``::

            sage: ct
            [\'F\', 4] relabelled by {1: 4, 2: 3, 3: 2, 4: 1}
        '''

class CartanType_affine(CartanType, cartan_type.CartanType_affine):
    """
    TESTS::

        sage: ct = CartanType(['D',4,3]); ct
        ['G', 2, 1]^* relabelled by {0: 0, 1: 2, 2: 1}

        sage: L = ct.root_system().ambient_space(); L
        Ambient space of the Root system of type ['G', 2, 1]^* relabelled by {0: 0, 1: 2, 2: 1}
        sage: L.classical()
        Ambient space of the Root system of type ['G', 2]
        sage: TestSuite(L).run()
    """
    def classical(self):
        """
        Return the classical Cartan type associated with ``self``.

        EXAMPLES::

            sage: A41 = CartanType(['A',4,1])
            sage: A41.dynkin_diagram()                                                  # needs sage.graphs
            0
            O-----------+
            |           |
            |           |
            O---O---O---O
            1   2   3   4
            A4~

            sage: T = A41.relabel({0:1, 1:2, 2:3, 3:4, 4:0})
            sage: T
            ['A', 4, 1] relabelled by {0: 1, 1: 2, 2: 3, 3: 4, 4: 0}
            sage: T.dynkin_diagram()                                                    # needs sage.graphs
            1
            O-----------+
            |           |
            |           |
            O---O---O---O
            2   3   4   0
            A4~ relabelled by {0: 1, 1: 2, 2: 3, 3: 4, 4: 0}

            sage: T0 = T.classical()
            sage: T0
            ['A', 4] relabelled by {1: 2, 2: 3, 3: 4, 4: 0}
            sage: T0.dynkin_diagram()                                                   # needs sage.graphs
            O---O---O---O
            2   3   4   0
            A4 relabelled by {1: 2, 2: 3, 3: 4, 4: 0}
        """
    def basic_untwisted(self):
        """
        Return the basic untwisted Cartan type associated with this affine
        Cartan type.

        Given an affine type `X_n^{(r)}`, the basic untwisted type is `X_n`.
        In other words, it is the classical Cartan type that is twisted to
        obtain ``self``.

        EXAMPLES::

            sage: ct = CartanType(['A', 5, 2]).relabel({0:1, 1:0, 2:2, 3:3})
            sage: ct.basic_untwisted()
            ['A', 5]
        """
    def special_node(self):
        """
        Return a special node of the Dynkin diagram.

        .. SEEALSO:: :meth:`~sage.combinat.root_system.CartanType_affine.special_node`

        It is obtained by relabelling of the special node of the non
        relabelled Dynkin diagram.

        EXAMPLES::

            sage: CartanType(['B', 3, 1]).special_node()
            0
            sage: CartanType(['B', 3, 1]).relabel({1:2, 2:3, 3:0, 0:1}).special_node()
            1
        """
    def is_untwisted_affine(self):
        """
        Implement :meth:`CartanType_affine.is_untwisted_affine`.

        A relabelled Cartan type is untwisted affine if the original is.

        EXAMPLES::

            sage: CartanType(['B', 3, 1]).relabel({1:2, 2:3, 3:0, 0:1}).is_untwisted_affine()
            True
        """
