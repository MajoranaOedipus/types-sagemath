from . import ambient_space as ambient_space
from .cartan_type import SuperCartanType_standard as SuperCartanType_standard
from _typeshed import Incomplete
from sage.misc.cachefunc import cached_method as cached_method
from sage.rings.integer_ring import ZZ as ZZ

class AmbientSpace(ambient_space.AmbientSpace):
    """
    The ambient space for (super) type `A(m|n)`.

    EXAMPLES::

        sage: R = RootSystem(['A', [2,1]])
        sage: AL = R.ambient_space(); AL
        Ambient space of the Root system of type ['A', [2, 1]]
        sage: AL.basis()
        Finite family {-3: (1, 0, 0, 0, 0),
         -2: (0, 1, 0, 0, 0),
         -1: (0, 0, 1, 0, 0),
         1: (0, 0, 0, 1, 0),
         2: (0, 0, 0, 0, 1)}
    """
    def __init__(self, root_system, base_ring, index_set=None) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: R = RootSystem(['A', [4,2]])
            sage: AL = R.ambient_space(); AL
            Ambient space of the Root system of type ['A', [4, 2]]
            sage: TestSuite(AL).run(skip='_test_norm_of_simple_roots')
        """
    @classmethod
    def smallest_base_ring(cls, cartan_type=None):
        """
        Return the smallest base ring the ambient space can be defined upon.

        .. SEEALSO::

            :meth:`~sage.combinat.root_system.ambient_space.AmbientSpace.smallest_base_ring`

        EXAMPLES::

            sage: e = RootSystem(['A', [3,1]]).ambient_space()
            sage: e.smallest_base_ring()
            Integer Ring
        """
    def dimension(self):
        """
        Return the dimension of this ambient space.

        EXAMPLES::

            sage: e = RootSystem(['A', [4,2]]).ambient_space()
            sage: e.dimension()
            8
        """
    def simple_root(self, i):
        """
        Return the `i`-th simple root of ``self``.

        EXAMPLES::

            sage: e = RootSystem(['A', [2,1]]).ambient_lattice()
            sage: list(e.simple_roots())
            [(1, -1, 0, 0, 0), (0, 1, -1, 0, 0),
             (0, 0, 1, -1, 0), (0, 0, 0, 1, -1)]
        """
    def positive_roots(self):
        """
        Return the positive roots of ``self``.

        EXAMPLES::

            sage: e = RootSystem(['A', [2,1]]).ambient_lattice()
            sage: e.positive_roots()
            [(0, 1, -1, 0, 0),
             (1, 0, -1, 0, 0),
             (1, -1, 0, 0, 0),
             (0, 0, 0, 1, -1),
             (0, 0, 1, -1, 0),
             (0, 0, 1, 0, -1),
             (0, 1, 0, -1, 0),
             (0, 1, 0, 0, -1),
             (1, 0, 0, -1, 0),
             (1, 0, 0, 0, -1)]
        """
    def positive_even_roots(self):
        """
        Return the positive even roots of ``self``.

        EXAMPLES::

            sage: e = RootSystem(['A', [2,1]]).ambient_lattice()
            sage: e.positive_even_roots()
            [(0, 1, -1, 0, 0), (1, 0, -1, 0, 0),
             (1, -1, 0, 0, 0), (0, 0, 0, 1, -1)]
        """
    def positive_odd_roots(self):
        """
        Return the positive odd roots of ``self``.

        EXAMPLES::

            sage: e = RootSystem(['A', [2,1]]).ambient_lattice()
            sage: e.positive_odd_roots()
            [(0, 0, 1, -1, 0),
             (0, 0, 1, 0, -1),
             (0, 1, 0, -1, 0),
             (0, 1, 0, 0, -1),
             (1, 0, 0, -1, 0),
             (1, 0, 0, 0, -1)]
        """
    def highest_root(self):
        """
        Return the highest root of ``self``.

        EXAMPLES::

           sage: e = RootSystem(['A', [4,2]]).ambient_lattice()
           sage: e.highest_root()
           (1, 0, 0, 0, 0, 0, 0, -1)
        """
    def negative_roots(self):
        """
        Return the negative roots of ``self``.

        EXAMPLES::

            sage: e = RootSystem(['A', [2,1]]).ambient_lattice()
            sage: e.negative_roots()
            [(0, -1, 1, 0, 0),
             (-1, 0, 1, 0, 0),
             (-1, 1, 0, 0, 0),
             (0, 0, 0, -1, 1),
             (0, 0, -1, 1, 0),
             (0, 0, -1, 0, 1),
             (0, -1, 0, 1, 0),
             (0, -1, 0, 0, 1),
             (-1, 0, 0, 1, 0),
             (-1, 0, 0, 0, 1)]
        """
    def negative_even_roots(self):
        """
        Return the negative even roots of ``self``.

        EXAMPLES::

            sage: e = RootSystem(['A', [2,1]]).ambient_lattice()
            sage: e.negative_even_roots()
            [(0, -1, 1, 0, 0), (-1, 0, 1, 0, 0),
             (-1, 1, 0, 0, 0), (0, 0, 0, -1, 1)]
        """
    def negative_odd_roots(self):
        """
        Return the negative odd roots of ``self``.

        EXAMPLES::

            sage: e = RootSystem(['A', [2,1]]).ambient_lattice()
            sage: e.negative_odd_roots()
            [(0, 0, -1, 1, 0),
             (0, 0, -1, 0, 1),
             (0, -1, 0, 1, 0),
             (0, -1, 0, 0, 1),
             (-1, 0, 0, 1, 0),
             (-1, 0, 0, 0, 1)]
        """
    def fundamental_weight(self, i):
        """
        Return the fundamental weight `\\Lambda_i` of ``self``.

        EXAMPLES::

            sage: L = RootSystem(['A', [3,2]]).ambient_space()
            sage: L.fundamental_weight(-1)
            (1, 1, 1, 0, 0, 0, 0)
            sage: L.fundamental_weight(0)
            (1, 1, 1, 1, 0, 0, 0)
            sage: L.fundamental_weight(2)
            (1, 1, 1, 1, -1, -1, -2)
            sage: list(L.fundamental_weights())
            [(1, 0, 0, 0, 0, 0, 0),
             (1, 1, 0, 0, 0, 0, 0),
             (1, 1, 1, 0, 0, 0, 0),
             (1, 1, 1, 1, 0, 0, 0),
             (1, 1, 1, 1, -1, -2, -2),
             (1, 1, 1, 1, -1, -1, -2)]

        ::

            sage: L = RootSystem(['A', [2,3]]).ambient_space()
            sage: La = L.fundamental_weights()
            sage: al = L.simple_roots()
            sage: I = L.index_set()
            sage: matrix([[al[i].scalar(La[j]) for i in I] for j in I])
            [ 1  0  0  0  0  0]
            [ 0  1  0  0  0  0]
            [ 0  0  1  0  0  0]
            [ 0  0  0 -1  0  0]
            [ 0  0  0  0 -1  0]
            [ 0  0  0  0  0 -1]
        """
    def simple_coroot(self, i):
        """
        Return the simple coroot `h_i` of ``self``.

        EXAMPLES::

            sage: L = RootSystem(['A', [3,2]]).ambient_space()
            sage: L.simple_coroot(-2)
            (0, 1, -1, 0, 0, 0, 0)
            sage: L.simple_coroot(0)
            (0, 0, 0, 1, -1, 0, 0)
            sage: L.simple_coroot(2)
            (0, 0, 0, 0, 0, -1, 1)
            sage: list(L.simple_coroots())
            [(1, -1, 0, 0, 0, 0, 0),
             (0, 1, -1, 0, 0, 0, 0),
             (0, 0, 1, -1, 0, 0, 0),
             (0, 0, 0, 1, -1, 0, 0),
             (0, 0, 0, 0, -1, 1, 0),
             (0, 0, 0, 0, 0, -1, 1)]
        """
    class Element(ambient_space.AmbientSpaceElement):
        def inner_product(self, lambdacheck):
            """
            The scalar product with elements of the coroot lattice
            embedded in the ambient space.

            EXAMPLES::

                sage: L = RootSystem(['A', [2,1]]).ambient_space()
                sage: a = L.simple_roots()
                sage: matrix([[a[i].inner_product(a[j]) for j in L.index_set()] for i in L.index_set()])
                [ 2 -1  0  0]
                [-1  2 -1  0]
                [ 0 -1  0  1]
                [ 0  0  1 -2]
            """
        scalar = inner_product
        dot_product = inner_product
        def associated_coroot(self):
            """
            Return the coroot associated to ``self``.

            EXAMPLES::

                sage: L = RootSystem(['A', [3,2]]).ambient_space()
                sage: al = L.simple_roots()
                sage: al[-1].associated_coroot()
                (0, 0, 1, -1, 0, 0, 0)
                sage: al[0].associated_coroot()
                (0, 0, 0, 1, -1, 0, 0)
                sage: al[1].associated_coroot()
                (0, 0, 0, 0, -1, 1, 0)

                sage: a = al[-1] + al[0] + al[1]; a
                (0, 0, 1, 0, 0, -1, 0)
                sage: a.associated_coroot()
                (0, 0, 1, 0, -2, 1, 0)
                sage: h = L.simple_coroots()
                sage: h[-1] + h[0] + h[1]
                (0, 0, 1, 0, -2, 1, 0)

                sage: (al[-1] + al[0] + al[2]).associated_coroot()
                (0, 0, 1, 0, -1, -1, 1)
            """
        def has_descent(self, i, positive: bool = False) -> bool:
            """
            Test if ``self`` has a descent at position `i`, that is
            if ``self`` is on the strict negative side of the `i`-th
            simple reflection hyperplane.

            If ``positive`` is ``True``, tests if it is on the strict
            positive side instead.

            EXAMPLES::

                sage: L = RootSystem(['A', [2,1]]).ambient_space()
                sage: al = L.simple_roots()
                sage: [al[i].has_descent(1) for i in L.index_set()]
                [False, False, True, False]
                sage: [(-al[i]).has_descent(1) for i in L.index_set()]
                [False, False, False, True]
                sage: [al[i].has_descent(1, True) for i in L.index_set()]
                [False, False, False, True]
                sage: [(-al[i]).has_descent(1, True) for i in L.index_set()]
                [False, False, True, False]
                sage: (al[-2] + al[0] + al[1]).has_descent(-1)
                True
                sage: (al[-2] + al[0] + al[1]).has_descent(1)
                False
                sage: (al[-2] + al[0] + al[1]).has_descent(1, positive=True)
                True
                sage: all(all(not la.has_descent(i) for i in L.index_set())
                ....:     for la in L.fundamental_weights())
                True
            """
        def is_dominant_weight(self) -> bool:
            """
            Test whether ``self`` is a dominant element of the weight lattice.

            EXAMPLES::

                sage: L = RootSystem(['A',2]).ambient_lattice()
                sage: Lambda = L.fundamental_weights()
                sage: [x.is_dominant() for x in Lambda]
                [True, True]
                sage: (3*Lambda[1]+Lambda[2]).is_dominant()
                True
                sage: (Lambda[1]-Lambda[2]).is_dominant()
                False
                sage: (-Lambda[1]+Lambda[2]).is_dominant()
                False

            Tests that the scalar products with the coroots are all
            nonnegative integers. For example, if `x` is the sum of a
            dominant element of the weight lattice plus some other element
            orthogonal to all coroots, then the implementation correctly
            reports `x` to be a dominant weight::

               sage: x = Lambda[1] + L([-1,-1,-1])
               sage: x.is_dominant_weight()
               True
            """

class CartanType(SuperCartanType_standard):
    """
    Cartan Type `A(m|n)`.

    .. SEEALSO:: :func:`~sage.combinat.root_systems.cartan_type.CartanType`
    """
    m: Incomplete
    n: Incomplete
    letter: str
    def __init__(self, m, n) -> None:
        """
        EXAMPLES::

            sage: ct = CartanType(['A', [4,2]])
            sage: ct
            ['A', [4, 2]]
            sage: ct._repr_(compact=True)
            'A4|2'

            sage: ct.is_irreducible()
            True
            sage: ct.is_finite()
            True
            sage: ct.is_affine()
            False
            sage: ct.affine() # Not tested -- to be implemented
            ['A', [4, 2], 1]
            sage: ct.dual()
            ['A', [4, 2]]

        TESTS::

            sage: TestSuite(ct).run()
        """
    def index_set(self):
        """
        Return the index set of ``self``.

        EXAMPLES::

            sage: CartanType(['A', [2,3]]).index_set()
            (-2, -1, 0, 1, 2, 3)
        """
    AmbientSpace = AmbientSpace
    def is_irreducible(self):
        """
        Return whether ``self`` is irreducible, which is ``True``.

        EXAMPLES::

            sage: CartanType(['A', [3,4]]).is_irreducible()
            True
        """
    def is_affine(self):
        """
        Return whether ``self`` is affine or not.

        EXAMPLES::

            sage: CartanType(['A', [2,3]]).is_affine()
            False
        """
    def is_finite(self):
        """
        Return whether ``self`` is finite or not.

        EXAMPLES::

            sage: CartanType(['A', [2,3]]).is_finite()
            True
        """
    def dual(self):
        """
        Return dual of ``self``.

        EXAMPLES::

            sage: CartanType(['A', [2,3]]).dual()
            ['A', [2, 3]]
        """
    def type(self):
        """
        Return type of ``self``.

        EXAMPLES::

            sage: CartanType(['A', [2,3]]).type()
            'A'
        """
    def root_system(self):
        """
        Return root system of ``self``.

        EXAMPLES::

            sage: CartanType(['A', [2,3]]).root_system()
            Root system of type ['A', [2, 3]]
        """
    @cached_method
    def symmetrizer(self):
        """
        Return symmetrizing matrix for ``self``.

        EXAMPLES::

            sage: CartanType(['A', [2,3]]).symmetrizer()
            Finite family {-2: 1, -1: 1, 0: 1, 1: -1, 2: -1, 3: -1}
        """
    def dynkin_diagram(self):
        """
        Return the Dynkin diagram of super type A.

        EXAMPLES::

            sage: a = CartanType(['A', [4,2]]).dynkin_diagram(); a                      # needs sage.graphs
            O---O---O---O---X---O---O
            -4  -3  -2  -1  0   1   2
            A4|2
            sage: a.edges(sort=True)                                                    # needs sage.graphs
            [(-4, -3, 1), (-3, -4, 1), (-3, -2, 1), (-2, -3, 1),
             (-2, -1, 1), (-1, -2, 1), (-1, 0, 1), (0, -1, 1),
             (0, 1, 1), (1, 0, -1), (1, 2, 1), (2, 1, 1)]

        TESTS::

            sage: a = DynkinDiagram(['A', [0,0]]); a                                    # needs sage.graphs
            X
            0
            A0|0
            sage: a.vertices(sort=False), a.edges(sort=False)                           # needs sage.graphs
            ([0], [])

            sage: a = DynkinDiagram(['A', [1,0]]); a                                    # needs sage.graphs
            O---X
            -1  0
            A1|0
            sage: a.vertices(sort=True), a.edges(sort=True)                             # needs sage.graphs
            ([-1, 0], [(-1, 0, 1), (0, -1, 1)])

            sage: a = DynkinDiagram(['A', [0,1]]); a                                    # needs sage.graphs
            X---O
            0   1
            A0|1
            sage: a.vertices(sort=True), a.edges(sort=True)                             # needs sage.graphs
            ([0, 1], [(0, 1, 1), (1, 0, -1)])
        """
    def cartan_matrix(self):
        """
        Return the Cartan matrix associated to ``self``.

        EXAMPLES::

            sage: ct = CartanType(['A', [2,3]])
            sage: ct.cartan_matrix()                                                    # needs sage.graphs
            [ 2 -1  0  0  0  0]
            [-1  2 -1  0  0  0]
            [ 0 -1  0  1  0  0]
            [ 0  0 -1  2 -1  0]
            [ 0  0  0 -1  2 -1]
            [ 0  0  0  0 -1  2]

        TESTS::

            sage: ct = CartanType(['A', [0,0]])
            sage: ct.cartan_matrix()                                                    # needs sage.graphs
            [0]

            sage: ct = CartanType(['A', [1,0]])
            sage: ct.cartan_matrix()                                                    # needs sage.graphs
            [ 2 -1]
            [-1  0]

            sage: ct = CartanType(['A', [0,1]])
            sage: ct.cartan_matrix()                                                    # needs sage.graphs
            [ 0  1]
            [-1  2]
        """
    def relabel(self, relabelling):
        """
        Return a relabelled copy of this Cartan type.

        INPUT:

        - ``relabelling`` -- a function (or a list or dictionary)

        OUTPUT:

        an isomorphic Cartan type obtained by relabelling the nodes of
        the Dynkin diagram. Namely, the node with label ``i`` is
        relabelled ``f(i)`` (or, by ``f[i]`` if ``f`` is a list or
        dictionary).

        EXAMPLES::

            sage: ct = CartanType(['A', [1,2]])
            sage: ct.dynkin_diagram()                                                   # needs sage.graphs
            O---X---O---O
            -1  0   1   2
            A1|2
            sage: f = {1:2, 2:1, 0:0, -1:-1}
            sage: ct.relabel(f)
            ['A', [1, 2]] relabelled by {-1: -1, 0: 0, 1: 2, 2: 1}
            sage: ct.relabel(f).dynkin_diagram()                                        # needs sage.graphs
            O---X---O---O
            -1  0   2   1
            A1|2 relabelled by {-1: -1, 0: 0, 1: 2, 2: 1}
        """
    def ascii_art(self, label=None, node=None):
        """
        Return an ascii art representation of the Dynkin diagram.

        EXAMPLES::

            sage: t = CartanType(['A', [3,2]])
            sage: print(t.ascii_art())
            O---O---O---X---O---O
            -3  -2  -1  0   1   2
            sage: t = CartanType(['A', [3,7]])
            sage: print(t.ascii_art())
            O---O---O---X---O---O---O---O---O---O---O
            -3  -2  -1  0   1   2   3   4   5   6   7

            sage: t = CartanType(['A', [0,7]])
            sage: print(t.ascii_art())
            X---O---O---O---O---O---O---O
            0   1   2   3   4   5   6   7
            sage: t = CartanType(['A', [0,0]])
            sage: print(t.ascii_art())
            X
            0
            sage: t = CartanType(['A', [5,0]])
            sage: print(t.ascii_art())
            O---O---O---O---O---X
            -5  -4  -3  -2  -1  0
        """
