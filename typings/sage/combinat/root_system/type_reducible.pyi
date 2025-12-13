from . import ambient_space as ambient_space
from _typeshed import Incomplete
from sage.combinat.root_system.cartan_type import CartanType_abstract as CartanType_abstract, CartanType_crystallographic as CartanType_crystallographic, CartanType_finite as CartanType_finite, CartanType_simple as CartanType_simple, CartanType_simply_laced as CartanType_simply_laced
from sage.matrix.constructor import block_diagonal_matrix as block_diagonal_matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.sets.family import Family as Family
from sage.structure.richcmp import rich_to_bool as rich_to_bool, richcmp as richcmp, richcmp_method as richcmp_method
from sage.structure.sage_object import SageObject as SageObject

class CartanType(SageObject, CartanType_abstract):
    '''
    A class for reducible Cartan types.

    Reducible root systems are ones that can be factored as direct
    products. Strictly speaking type `D_2` (corresponding to
    orthogonal groups of degree 4) is reducible since it is
    isomorphic to `A_1\\times A_1`. However type `D_2` is not built
    using this class for our purposes.

    INPUT:

    - ``types`` -- list of simple Cartan types

    EXAMPLES::

        sage: t1, t2 = [CartanType(x) for x in ([\'A\',1], [\'B\',2])]
        sage: CartanType([t1, t2])
        A1xB2
        sage: t = CartanType("A2xB2")

    A reducible Cartan type is finite (resp. crystallographic,
    simply laced) if all its components are::

        sage: t.is_finite()
        True
        sage: t.is_crystallographic()
        True
        sage: t.is_simply_laced()
        False

    This is implemented by inserting the appropriate abstract
    super classes (see :meth:`~sage.combinat.root_system.cartan_type.CartanType_abstract._add_abstract_superclass`)::

        sage: t.__class__.mro()
        [<class \'sage.combinat.root_system.type_reducible.CartanType_with_superclass\'>, <class \'sage.combinat.root_system.type_reducible.CartanType\'>, <class \'sage.structure.sage_object.SageObject\'>, <class \'sage.combinat.root_system.cartan_type.CartanType_finite\'>, <class \'sage.combinat.root_system.cartan_type.CartanType_crystallographic\'>, <class \'sage.combinat.root_system.cartan_type.CartanType_abstract\'>, <class \'object\'>]

    The index set of the reducible Cartan type is obtained by
    relabelling successively the nodes of the Dynkin diagrams of
    the components by 1,2,...::

        sage: t = CartanType(["A",4], ["BC",5,2], ["C",3])
        sage: t.index_set()
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

        sage: t.dynkin_diagram()                                                        # needs sage.graphs
        O---O---O---O
        1   2   3   4
        O=<=O---O---O---O=<=O
        5   6   7   8   9   10
        O---O=<=O
        11   12   13
        A4xBC5~xC3
    '''
    affine: bool
    tools: Incomplete
    def __init__(self, types) -> None:
        '''
        Initialize ``self``.

        TESTS:

        Internally, this relabelling is stored as a dictionary::

            sage: t = CartanType(["A",4], ["BC",5,2], ["C",3])
            sage: sorted(t._index_relabelling.items())
            [((0, 1), 1), ((0, 2), 2), ((0, 3), 3), ((0, 4), 4),
             ((1, 0), 5), ((1, 1), 6), ((1, 2), 7), ((1, 3), 8), ((1, 4), 9), ((1, 5), 10),
             ((2, 1), 11), ((2, 2), 12), ((2, 3), 13)]

        Similarly, the attribute ``_shifts`` specifies by how much the
        indices of the bases of the ambient spaces of the components
        are shifted in the ambient space of this Cartan type::

            sage: t = CartanType("A2xB2")
            sage: t._shifts
            [0, 3, 5]
            sage: A = t.root_system().ambient_space(); A
            Ambient space of the Root system of type A2xB2
            sage: A.ambient_spaces()
            [Ambient space of the Root system of type [\'A\', 2], Ambient space of the Root system of type [\'B\', 2]]
            sage: x = A.ambient_spaces()[0]([2,1,0]); x
            (2, 1, 0)
            sage: A.inject_weights(0,x)
            (2, 1, 0, 0, 0)
            sage: x = A.ambient_spaces()[1]([1,0]); x
            (1, 0)
            sage: A.inject_weights(1,x)
            (0, 0, 0, 1, 0)

        More tests::

            sage: TestSuite(t).run()
        '''
    def __hash__(self):
        """
        EXAMPLES::

            sage: ct0 = CartanType(['A',1],['B',2])
            sage: ct1 = CartanType(['A',2],['B',3])
            sage: hash(ct0) != hash(ct1)
            True
        """
    def __richcmp__(self, other, op):
        '''
        Rich comparison.

        EXAMPLES::

            sage: ct1 = CartanType([\'A\',1],[\'B\',2])
            sage: ct2 = CartanType([\'B\',2],[\'A\',1])
            sage: ct3 = CartanType([\'A\',4])
            sage: ct1 == ct1
            True
            sage: ct1 == ct2
            False
            sage: ct1 == ct3
            False

        TESTS:

        Check that :issue:`20418` is fixed::

            sage: ct = CartanType(["A2", "B2"])
            sage: ct == (1, 2, 1)
            False
        '''
    def component_types(self):
        """
        A list of Cartan types making up the reducible type.

        EXAMPLES::

            sage: CartanType(['A',2],['B',2]).component_types()
            [['A', 2], ['B', 2]]
        """
    def type(self):
        '''
        Return ``"reducible"`` since the type is reducible.

        EXAMPLES::

            sage: CartanType([\'A\',2],[\'B\',2]).type()
            \'reducible\'
        '''
    def rank(self):
        '''
        Return the rank of ``self``.

        EXAMPLES::

            sage: CartanType("A2","A1").rank()
            3
        '''
    @cached_method
    def index_set(self):
        '''
        Implement :meth:`CartanType_abstract.index_set`.

        For the moment, the index set is always of the form `\\{1, \\ldots, n\\}`.

        EXAMPLES::

            sage: CartanType("A2","A1").index_set()
            (1, 2, 3)
        '''
    def cartan_matrix(self, subdivide: bool = True):
        '''
        Return the Cartan matrix associated with ``self``. By default
        the Cartan matrix is a subdivided block matrix showing the
        reducibility but the subdivision can be suppressed with
        the option ``subdivide = False``.

        EXAMPLES::

            sage: ct = CartanType("A2","B2")
            sage: ct.cartan_matrix()                                                    # needs sage.graphs
            [ 2 -1| 0  0]
            [-1  2| 0  0]
            [-----+-----]
            [ 0  0| 2 -1]
            [ 0  0|-2  2]
            sage: ct.cartan_matrix(subdivide=False)                                     # needs sage.graphs
            [ 2 -1  0  0]
            [-1  2  0  0]
            [ 0  0  2 -1]
            [ 0  0 -2  2]
            sage: ct.index_set() == ct.cartan_matrix().index_set()                      # needs sage.graphs
            True
        '''
    def dynkin_diagram(self):
        '''
        Return a Dynkin diagram for type reducible.

        EXAMPLES::

            sage: dd = CartanType("A2xB2xF4").dynkin_diagram(); dd                      # needs sage.graphs
            O---O
            1   2
            O=>=O
            3   4
            O---O=>=O---O
            5   6   7   8
            A2xB2xF4
            sage: dd.edges(sort=True)                                                   # needs sage.graphs
            [(1, 2, 1), (2, 1, 1), (3, 4, 2), (4, 3, 1), (5, 6, 1),
             (6, 5, 1), (6, 7, 2), (7, 6, 1), (7, 8, 1), (8, 7, 1)]

            sage: CartanType("F4xA2").dynkin_diagram()                                  # needs sage.graphs
            O---O=>=O---O
            1   2   3   4
            O---O
            5   6
            F4xA2
        '''
    def ascii_art(self, label=None, node=None):
        '''
        Return an ascii art representation of this reducible Cartan type.

        EXAMPLES::

            sage: print(CartanType("F4xA2").ascii_art(label = lambda x: x+2))
            O---O=>=O---O
            3   4   5   6
            O---O
            7   8

            sage: print(CartanType(["BC",5,2], ["A",4]).ascii_art())
            O=<=O---O---O---O=<=O
            1   2   3   4   5   6
            O---O---O---O
            7   8   9   10

            sage: print(CartanType(["A",4], ["BC",5,2], ["C",3]).ascii_art())
            O---O---O---O
            1   2   3   4
            O=<=O---O---O---O=<=O
            5   6   7   8   9   10
            O---O=<=O
            11   12   13
        '''
    @cached_method
    def is_finite(self):
        """
        EXAMPLES::

            sage: ct1 = CartanType(['A',2],['B',2])
            sage: ct1.is_finite()
            True
            sage: ct2 = CartanType(['A',2],['B',2,1])
            sage: ct2.is_finite()
            False

        TESTS::

            sage: isinstance(ct1, sage.combinat.root_system.cartan_type.CartanType_finite)
            True
            sage: isinstance(ct2, sage.combinat.root_system.cartan_type.CartanType_finite)
            False
        """
    def is_irreducible(self):
        """
        Report that this Cartan type is not irreducible.

        EXAMPLES::

            sage: ct = CartanType(['A',2],['B',2])
            sage: ct.is_irreducible()
            False
        """
    def dual(self):
        '''
        EXAMPLES::

            sage: CartanType("A2xB2").dual()
            A2xC2
        '''
    def is_affine(self):
        """
        Report that this reducible Cartan type is not affine.

        EXAMPLES::

            sage: CartanType(['A',2],['B',2]).is_affine()
            False
        """
    @cached_method
    def coxeter_diagram(self):
        '''
        Return the Coxeter diagram for ``self``.

        EXAMPLES::

            sage: cd = CartanType("A2xB2xF4").coxeter_diagram(); cd                     # needs sage.graphs
            Graph on 8 vertices
            sage: cd.edges(sort=True)                                                   # needs sage.graphs
            [(1, 2, 3), (3, 4, 4), (5, 6, 3), (6, 7, 4), (7, 8, 3)]

            sage: CartanType("F4xA2").coxeter_diagram().edges(sort=True)                # needs sage.graphs
            [(1, 2, 3), (2, 3, 4), (3, 4, 3), (5, 6, 3)]

            sage: cd = CartanType("A1xH3").coxeter_diagram(); cd                        # needs sage.graphs
            Graph on 4 vertices
            sage: cd.edges(sort=True)                                                   # needs sage.graphs
            [(2, 3, 3), (3, 4, 5)]
        '''

class AmbientSpace(ambient_space.AmbientSpace):
    '''
    EXAMPLES::

        sage: RootSystem("A2xB2").ambient_space()
        Ambient space of the Root system of type A2xB2
    '''
    def cartan_type(self):
        '''
        EXAMPLES::

            sage: RootSystem("A2xB2").ambient_space().cartan_type()
            A2xB2
        '''
    def component_types(self):
        '''
        EXAMPLES::

            sage: RootSystem("A2xB2").ambient_space().component_types()
            [[\'A\', 2], [\'B\', 2]]
        '''
    def dimension(self):
        '''
        EXAMPLES::

            sage: RootSystem("A2xB2").ambient_space().dimension()
            5
        '''
    def ambient_spaces(self):
        '''
        Return a list of the irreducible Cartan types of which the
        given reducible Cartan type is a product.

        EXAMPLES::

            sage: RootSystem("A2xB2").ambient_space().ambient_spaces()
            [Ambient space of the Root system of type [\'A\', 2],
             Ambient space of the Root system of type [\'B\', 2]]
        '''
    def inject_weights(self, i, v):
        '''
        Produces the corresponding element of the lattice.

        INPUT:

        - ``i`` -- integer in ``range(self.components)``

        - ``v`` -- a vector in the `i`-th component weight lattice

        EXAMPLES::

            sage: V = RootSystem("A2xB2").ambient_space()
            sage: [V.inject_weights(i,V.ambient_spaces()[i].fundamental_weights()[1]) for i in range(2)]
            [(1, 0, 0, 0, 0), (0, 0, 0, 1, 0)]
            sage: [V.inject_weights(i,V.ambient_spaces()[i].fundamental_weights()[2]) for i in range(2)]
            [(1, 1, 0, 0, 0), (0, 0, 0, 1/2, 1/2)]
        '''
    @cached_method
    def simple_root(self, i):
        '''
        EXAMPLES::

            sage: A = RootSystem("A1xB2").ambient_space()
            sage: A.simple_root(2)
            (0, 0, 1, -1)
            sage: A.simple_roots()
            Finite family {1: (1, -1, 0, 0), 2: (0, 0, 1, -1), 3: (0, 0, 0, 1)}
        '''
    @cached_method
    def simple_coroot(self, i):
        '''
        EXAMPLES::

            sage: A = RootSystem("A1xB2").ambient_space()
            sage: A.simple_coroot(2)
            (0, 0, 1, -1)
            sage: A.simple_coroots()
            Finite family {1: (1, -1, 0, 0), 2: (0, 0, 1, -1), 3: (0, 0, 0, 2)}
        '''
    def positive_roots(self):
        '''
        EXAMPLES::

            sage: RootSystem("A1xA2").ambient_space().positive_roots()
            [(1, -1, 0, 0, 0), (0, 0, 1, -1, 0), (0, 0, 1, 0, -1), (0, 0, 0, 1, -1)]
        '''
    def negative_roots(self):
        '''
        EXAMPLES::

            sage: RootSystem("A1xA2").ambient_space().negative_roots()
            [(-1, 1, 0, 0, 0), (0, 0, -1, 1, 0), (0, 0, -1, 0, 1), (0, 0, 0, -1, 1)]
        '''
    def fundamental_weights(self):
        '''
        EXAMPLES::

            sage: RootSystem("A2xB2").ambient_space().fundamental_weights()
            Finite family {1: (1, 0, 0, 0, 0), 2: (1, 1, 0, 0, 0), 3: (0, 0, 0, 1, 0), 4: (0, 0, 0, 1/2, 1/2)}
        '''
