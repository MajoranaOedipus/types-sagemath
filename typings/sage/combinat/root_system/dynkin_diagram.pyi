from sage.combinat.root_system.cartan_type import CartanType as CartanType, CartanType_abstract as CartanType_abstract
from sage.graphs.digraph import DiGraph as DiGraph
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.structure.element import Matrix as Matrix

def DynkinDiagram(*args, **kwds):
    '''
    Return the Dynkin diagram corresponding to the input.

    INPUT:

    The input can be one of the following:

    - empty to obtain an empty Dynkin diagram
    - a Cartan type
    - a Cartan matrix
    - a Cartan matrix and an indexing set

    One can also input an indexing set by passing a tuple using the optional
    argument ``index_set``.

    The edge multiplicities are encoded as edge labels. For the corresponding
    Cartan matrices, this uses the convention in Hong and Kang, Kac,
    Fulton and Harris, and crystals. This is the **opposite** convention
    in Bourbaki and Wikipedia\'s Dynkin diagram (:wikipedia:`Dynkin_diagram`).
    That is for `i \\neq j`::

        i <--k-- j <==> a_ij = -k
                   <==> -scalar(coroot[i], root[j]) = k
                   <==> multiple arrows point from the longer root
                        to the shorter one

    For example, in type `C_2`, we have::

        sage: C2 = DynkinDiagram([\'C\',2]); C2
        O=<=O
        1   2
        C2
        sage: C2.cartan_matrix()
        [ 2 -2]
        [-1  2]

    However Bourbaki would have the Cartan matrix as:

    .. MATH::

        \\begin{bmatrix}
        2 & -1 \\\\\n        -2 & 2
        \\end{bmatrix}.

    EXAMPLES::

        sage: DynkinDiagram([\'A\', 4])
        O---O---O---O
        1   2   3   4
        A4

        sage: DynkinDiagram([\'A\',1],[\'A\',1])
        O
        1
        O
        2
        A1xA1

        sage: R = RootSystem("A2xB2xF4")
        sage: DynkinDiagram(R)
        O---O
        1   2
        O=>=O
        3   4
        O---O=>=O---O
        5   6   7   8
        A2xB2xF4

        sage: R = RootSystem("A2xB2xF4")
        sage: CM = R.cartan_matrix(); CM
        [ 2 -1| 0  0| 0  0  0  0]
        [-1  2| 0  0| 0  0  0  0]
        [-----+-----+-----------]
        [ 0  0| 2 -1| 0  0  0  0]
        [ 0  0|-2  2| 0  0  0  0]
        [-----+-----+-----------]
        [ 0  0| 0  0| 2 -1  0  0]
        [ 0  0| 0  0|-1  2 -1  0]
        [ 0  0| 0  0| 0 -2  2 -1]
        [ 0  0| 0  0| 0  0 -1  2]
        sage: DD = DynkinDiagram(CM); DD
        O---O
        1   2
        O=>=O
        3   4
        O---O=>=O---O
        5   6   7   8
        A2xB2xF4
        sage: DD.cartan_matrix()
        [ 2 -1  0  0  0  0  0  0]
        [-1  2  0  0  0  0  0  0]
        [ 0  0  2 -1  0  0  0  0]
        [ 0  0 -2  2  0  0  0  0]
        [ 0  0  0  0  2 -1  0  0]
        [ 0  0  0  0 -1  2 -1  0]
        [ 0  0  0  0  0 -2  2 -1]
        [ 0  0  0  0  0  0 -1  2]

    We can also create Dynkin diagrams from arbitrary Cartan matrices::

        sage: C = CartanMatrix([[2, -3], [-4, 2]])
        sage: DynkinDiagram(C)
        Dynkin diagram of rank 2
        sage: C.index_set()
        (0, 1)
        sage: CI = CartanMatrix([[2, -3], [-4, 2]], [3, 5])
        sage: DI = DynkinDiagram(CI)
        sage: DI.index_set()
        (3, 5)
        sage: CII = CartanMatrix([[2, -3], [-4, 2]])
        sage: DII = DynkinDiagram(CII, (\'y\', \'x\'))
        sage: DII.index_set()
        (\'x\', \'y\')

    .. SEEALSO::

        :func:`CartanType` for a general discussion on Cartan
        types and in particular node labeling conventions.

    TESTS:

    Check that :issue:`15277` is fixed by not having edges from 0s::

        sage: CM = CartanMatrix([[2,-1,0,0],[-3,2,-2,-2],[0,-1,2,-1],[0,-1,-1,2]])
        sage: CM
        [ 2 -1  0  0]
        [-3  2 -2 -2]
        [ 0 -1  2 -1]
        [ 0 -1 -1  2]
        sage: CM.dynkin_diagram().edges(sort=True)
        [(0, 1, 3),
         (1, 0, 1),
         (1, 2, 1),
         (1, 3, 1),
         (2, 1, 2),
         (2, 3, 1),
         (3, 1, 2),
         (3, 2, 1)]
    '''

class DynkinDiagram_class(DiGraph, CartanType_abstract):
    """
    A Dynkin diagram.

    .. SEEALSO::

        :func:`DynkinDiagram()`

    INPUT:

    - ``t`` -- a Cartan type, Cartan matrix, or ``None``

    EXAMPLES::

        sage: DynkinDiagram(['A', 3])
        O---O---O
        1   2   3
        A3
        sage: C = CartanMatrix([[2, -3], [-4, 2]])
        sage: DynkinDiagram(C)
        Dynkin diagram of rank 2
        sage: C.dynkin_diagram().cartan_matrix() == C
        True

    TESTS:

    Check that the correct type is returned when copied::

        sage: d = DynkinDiagram(['A', 3])
        sage: type(copy(d))
        <class 'sage.combinat.root_system.dynkin_diagram.DynkinDiagram_class'>

    We check that :issue:`14655` is fixed::

        sage: cd = copy(d)
        sage: cd.add_vertex(4)
        sage: d.vertices(sort=True) != cd.vertices(sort=True)
        True

    Implementation note: if a Cartan type is given, then the nodes
    are initialized from the index set of this Cartan type.
    """
    def __init__(self, t=None, index_set=None, odd_isotropic_roots=[], **options) -> None:
        '''
        Initialize ``self``.

        EXAMPLES::

            sage: d = DynkinDiagram(["A", 3])
            sage: TestSuite(d).run()
        '''
    def add_edge(self, i, j, label: int = 1) -> None:
        """
        EXAMPLES::

            sage: from sage.combinat.root_system.dynkin_diagram import DynkinDiagram_class
            sage: d = DynkinDiagram_class(CartanType(['A',3]))
            sage: sorted(d.edges(sort=True))
            []
            sage: d.add_edge(2, 3)
            sage: sorted(d.edges(sort=True))
            [(2, 3, 1), (3, 2, 1)]
        """
    def __hash__(self):
        """
        EXAMPLES::

            sage: d = CartanType(['A',3]).dynkin_diagram()
            sage: dv = d.vertices(sort=True)
            sage: hash(d) == hash((d.cartan_type(), tuple(dv), tuple(d.edge_iterator(dv))))
            True
        """
    @staticmethod
    def an_instance():
        """
        Return an example of Dynkin diagram.

        EXAMPLES::

            sage: from sage.combinat.root_system.dynkin_diagram import DynkinDiagram_class
            sage: g = DynkinDiagram_class.an_instance()
            sage: g
            Dynkin diagram of rank 3
            sage: g.cartan_matrix()
            [ 2 -1 -1]
            [-2  2 -1]
            [-1 -1  2]
        """
    @cached_method
    def index_set(self):
        '''
        EXAMPLES::

            sage: DynkinDiagram([\'C\',3]).index_set()
            (1, 2, 3)
            sage: DynkinDiagram("A2","B2","F4").index_set()
            (1, 2, 3, 4, 5, 6, 7, 8)
        '''
    def cartan_type(self):
        '''
        EXAMPLES::

            sage: DynkinDiagram("A2","B2","F4").cartan_type()
            A2xB2xF4
        '''
    def rank(self):
        '''
        Return the index set for this Dynkin diagram.

        EXAMPLES::

            sage: DynkinDiagram([\'C\',3]).rank()
            3
            sage: DynkinDiagram("A2","B2","F4").rank()
            8
        '''
    def dynkin_diagram(self):
        """
        EXAMPLES::

            sage: DynkinDiagram(['C',3]).dynkin_diagram()
            O---O=<=O
            1   2   3
            C3
        """
    @cached_method
    def cartan_matrix(self):
        """
        Return the Cartan matrix for this Dynkin diagram.

        EXAMPLES::

            sage: DynkinDiagram(['C',3]).cartan_matrix()
            [ 2 -1  0]
            [-1  2 -2]
            [ 0 -1  2]
        """
    def dual(self):
        """
        Return the dual Dynkin diagram, obtained by reversing all edges.

        EXAMPLES::

            sage: D = DynkinDiagram(['C',3])
            sage: D.edges(sort=True)
            [(1, 2, 1), (2, 1, 1), (2, 3, 1), (3, 2, 2)]
            sage: D.dual()
            O---O=>=O
            1   2   3
            B3
            sage: D.dual().edges(sort=True)
            [(1, 2, 1), (2, 1, 1), (2, 3, 2), (3, 2, 1)]
            sage: D.dual() == DynkinDiagram(['B',3])
            True

        TESTS::

            sage: D = DynkinDiagram(['A',0]); D
            A0
            sage: D.edges(sort=True)
            []
            sage: D.dual()
            A0
            sage: D.dual().edges(sort=True)
            []
            sage: D = DynkinDiagram(['A',1])
            sage: D.edges(sort=True)
            []
            sage: D.dual()
            O
            1
            A1
            sage: D.dual().edges(sort=True)
            []
        """
    def relabel(self, *args, **kwds):
        """
        Return the relabelled Dynkin diagram of ``self``.

        INPUT: see :meth:`~sage.graphs.generic_graph.GenericGraph.relabel`

        There is one difference: the default value for ``inplace`` is
        ``False`` instead of ``True``.

        EXAMPLES::

            sage: D = DynkinDiagram(['C',3])
            sage: D.relabel({1:0, 2:4, 3:1})
            O---O=<=O
            0   4   1
            C3 relabelled by {1: 0, 2: 4, 3: 1}
            sage: D
            O---O=<=O
            1   2   3
            C3

            sage: _ = D.relabel({1:0, 2:4, 3:1}, inplace=True)
            sage: D
            O---O=<=O
            0   4   1
            C3 relabelled by {1: 0, 2: 4, 3: 1}

            sage: D = DynkinDiagram(['A', [1,2]])
            sage: Dp = D.relabel({-1:4, 0:-3, 1:3, 2:2})
            sage: Dp
            O---X---O---O
            4   -3  3   2
            A1|2 relabelled by {-1: 4, 0: -3, 1: 3, 2: 2}
            sage: Dp.odd_isotropic_roots()
            (-3,)

            sage: D = DynkinDiagram(['D', 5])
            sage: G, perm = D.relabel(range(5), return_map=True)
            sage: G
                    O 4
                    |
                    |
            O---O---O---O
            0   1   2   3
            D5 relabelled by {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
            sage: perm
            {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}

            sage: perm = D.relabel(range(5), return_map=True, inplace=True)
            sage: D
                    O 4
                    |
                    |
            O---O---O---O
            0   1   2   3
            D5 relabelled by {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
            sage: perm
            {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
        """
    def subtype(self, index_set):
        """
        Return a subtype of ``self`` given by ``index_set``.

        A subtype can be considered the Dynkin diagram induced from
        the Dynkin diagram of ``self`` by ``index_set``.

        EXAMPLES::

            sage: D = DynkinDiagram(['A',6,2]); D
            O=<=O---O=<=O
            0   1   2   3
            BC3~
            sage: D.subtype([1,2,3])
            Dynkin diagram of rank 3
        """
    def is_finite(self):
        """
        Check if ``self`` corresponds to a finite root system.

        EXAMPLES::

            sage: CartanType(['F',4]).dynkin_diagram().is_finite()
            True
            sage: D = DynkinDiagram(CartanMatrix([[2, -4], [-3, 2]]))
            sage: D.is_finite()
            False
        """
    def is_affine(self):
        """
        Check if ``self`` corresponds to an affine root system.

        EXAMPLES::

            sage: CartanType(['F',4]).dynkin_diagram().is_affine()
            False
            sage: D = DynkinDiagram(CartanMatrix([[2, -4], [-3, 2]]))
            sage: D.is_affine()
            False
        """
    def is_irreducible(self):
        '''
        Check if ``self`` corresponds to an irreducible root system.

        EXAMPLES::

            sage: CartanType([\'F\',4]).dynkin_diagram().is_irreducible()
            True
            sage: CM = CartanMatrix([[2,-6],[-4,2]])
            sage: CM.dynkin_diagram().is_irreducible()
            True
            sage: CartanType("A2xB3").dynkin_diagram().is_irreducible()
            False
            sage: CM = CartanMatrix([[2,-6,0],[-4,2,0],[0,0,2]])
            sage: CM.dynkin_diagram().is_irreducible()
            False
        '''
    def is_crystallographic(self):
        """
        Implement :meth:`CartanType_abstract.is_crystallographic`.

        A Dynkin diagram always corresponds to a crystallographic root system.

        EXAMPLES::

            sage: CartanType(['F',4]).dynkin_diagram().is_crystallographic()
            True

        TESTS::

            sage: CartanType(['G',2]).dynkin_diagram().is_crystallographic()
            True
        """
    def symmetrizer(self):
        """
        Return the symmetrizer of the corresponding Cartan matrix.

        EXAMPLES::

            sage: d = DynkinDiagram()
            sage: d.add_edge(1,2,3)
            sage: d.add_edge(2,3)
            sage: d.add_edge(3,4,3)
            sage: d.symmetrizer()
            Finite family {1: 9, 2: 3, 3: 3, 4: 1}

        TESTS:

        We check that :issue:`15740` is fixed::

            sage: d = DynkinDiagram()
            sage: d.add_edge(1,2,3)
            sage: d.add_edge(2,3)
            sage: d.add_edge(3,4,3)
            sage: L = d.root_system().root_lattice()
            sage: al = L.simple_roots()
            sage: al[1].associated_coroot()
            alphacheck[1]
            sage: al[1].reflection(al[2])
            alpha[1] + 3*alpha[2]
        """
    def odd_isotropic_roots(self):
        """
        Return the odd isotropic roots of ``self``.

        EXAMPLES::

            sage: g = DynkinDiagram(['A',4])
            sage: g.odd_isotropic_roots()
            ()
            sage: g = DynkinDiagram(['A',[4,3]])
            sage: g.odd_isotropic_roots()
            (0,)
        """
    def __getitem__(self, i):
        """
        With a tuple (i,j) as argument, returns the scalar product
        `\\langle \\alpha^\\vee_i, \\alpha_j\\rangle`.

        Otherwise, behaves as the usual ``DiGraph.__getitem__``

        EXAMPLES:

        We use the `C_4` Dynkin diagram as a Cartan matrix::

            sage: g = DynkinDiagram(['C',4])
            sage: matrix([[g[i,j] for j in range(1,5)] for i in range(1,5)])
            [ 2 -1  0  0]
            [-1  2 -1  0]
            [ 0 -1  2 -2]
            [ 0  0 -1  2]

        The neighbors of a node can still be obtained in the usual way::

            sage: [g[i] for i in range(1,5)]
            [[2], [1, 3], [2, 4], [3]]
        """
    def column(self, j):
        '''
        Return the `j`-th column `(a_{i,j})_i` of the
        Cartan matrix corresponding to this Dynkin diagram, as a container
        (or iterator) of tuples `(i, a_{i,j})`.

        EXAMPLES::

            sage: g = DynkinDiagram(["B",4])
            sage: [ (i,a) for (i,a) in g.column(3) ]
            [(3, 2), (2, -1), (4, -2)]
        '''
    def row(self, i):
        '''
        Return the `i`-th row `(a_{i,j})_j` of the
        Cartan matrix corresponding to this Dynkin diagram, as a container
        (or iterator) of tuples `(j, a_{i,j})`.

        EXAMPLES::

            sage: g = DynkinDiagram(["C",4])
            sage: [ (i,a) for (i,a) in g.row(3) ]
            [(3, 2), (2, -1), (4, -2)]
        '''
    @cached_method
    def coxeter_diagram(self):
        """
        Construct the Coxeter diagram of ``self``.

        .. SEEALSO:: :meth:`CartanType_abstract.coxeter_diagram`

        EXAMPLES::

            sage: cm = CartanMatrix([[2,-5,0],[-2,2,-1],[0,-1,2]])
            sage: D = cm.dynkin_diagram()
            sage: G = D.coxeter_diagram(); G
            Graph on 3 vertices
            sage: G.edges(sort=True)
            [(0, 1, +Infinity), (1, 2, 3)]

            sage: ct = CartanType([['A',2,2], ['B',3]])
            sage: ct.coxeter_diagram()
            Graph on 5 vertices
            sage: ct.dynkin_diagram().coxeter_diagram() == ct.coxeter_diagram()
            True
        """

def precheck(t, letter=None, length=None, affine=None, n_ge=None, n=None) -> None:
    """
    EXAMPLES::

        sage: from sage.combinat.root_system.dynkin_diagram import precheck
        sage: ct = CartanType(['A',4])
        sage: precheck(ct, letter='C')
        Traceback (most recent call last):
        ...
        ValueError: t[0] must be = 'C'
        sage: precheck(ct, affine=1)
        Traceback (most recent call last):
        ...
        ValueError: t[2] must be = 1
        sage: precheck(ct, length=3)
        Traceback (most recent call last):
        ...
        ValueError: len(t) must be = 3
        sage: precheck(ct, n=3)
        Traceback (most recent call last):
        ...
        ValueError: t[1] must be = 3
        sage: precheck(ct, n_ge=5)
        Traceback (most recent call last):
        ...
        ValueError: t[1] must be >= 5
    """
