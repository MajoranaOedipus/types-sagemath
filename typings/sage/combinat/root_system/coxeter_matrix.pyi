from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.coxeter_type import CoxeterType as CoxeterType
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_generic_dense import Matrix_generic_dense as Matrix_generic_dense
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.classcall_metaclass import ClasscallMetaclass as ClasscallMetaclass, typecall as typecall
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.infinity import infinity as infinity
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.rational_field import QQ as QQ
from sage.rings.real_mpfr import RR as RR

class CoxeterMatrix(CoxeterType, metaclass=ClasscallMetaclass):
    """
    A Coxeter matrix.

    A Coxeter matrix `M = (m_{ij})_{i,j \\in I}` is a matrix encoding
    a Coxeter system `(W, S)`, where the relations are given by
    `(s_i s_j)^{m_{ij}}`. Thus `M` is symmetric and has entries
    in `\\{1, 2, 3, \\ldots, \\infty\\}` with `m_{ij} = 1` if and only
    if `i = j`.

    We represent `m_{ij} = \\infty` by any number `m_{ij} \\leq -1`. In
    particular, we can construct a bilinear form `B = (b_{ij})_{i,j \\in I}`
    from `M` by

    .. MATH::

        b_{ij} = \\begin{cases}
        m_{ij} & m_{ij} < 0\\ (\\text{i.e., } m_{ij} = \\infty), \\\\\n        -\\cos\\left( \\frac{\\pi}{m_{ij}} \\right) & \\text{otherwise}.
        \\end{cases}

    EXAMPLES::

        sage: CoxeterMatrix(['A', 4])
        [1 3 2 2]
        [3 1 3 2]
        [2 3 1 3]
        [2 2 3 1]
        sage: CoxeterMatrix(['B', 4])
        [1 3 2 2]
        [3 1 3 2]
        [2 3 1 4]
        [2 2 4 1]
        sage: CoxeterMatrix(['C', 4])
        [1 3 2 2]
        [3 1 3 2]
        [2 3 1 4]
        [2 2 4 1]
        sage: CoxeterMatrix(['D', 4])
        [1 3 2 2]
        [3 1 3 3]
        [2 3 1 2]
        [2 3 2 1]

        sage: CoxeterMatrix(['E', 6])
        [1 2 3 2 2 2]
        [2 1 2 3 2 2]
        [3 2 1 3 2 2]
        [2 3 3 1 3 2]
        [2 2 2 3 1 3]
        [2 2 2 2 3 1]

        sage: CoxeterMatrix(['F', 4])
        [1 3 2 2]
        [3 1 4 2]
        [2 4 1 3]
        [2 2 3 1]

        sage: CoxeterMatrix(['G', 2])
        [1 6]
        [6 1]

    By default, entries representing `\\infty` are given by `-1`
    in the Coxeter matrix::

        sage: G = Graph([(0,1,None), (1,2,4), (0,2,oo)])
        sage: CoxeterMatrix(G)
        [ 1  3 -1]
        [ 3  1  4]
        [-1  4  1]

    It is possible to give a number `\\leq -1` to represent an infinite label::

        sage: CoxeterMatrix([[1,-1],[-1,1]])
        [ 1 -1]
        [-1  1]
        sage: CoxeterMatrix([[1,-3/2],[-3/2,1]])
        [   1 -3/2]
        [-3/2    1]
    """
    @staticmethod
    def __classcall_private__(cls, data=None, index_set=None, coxeter_type=None, cartan_type=None, coxeter_type_check: bool = True):
        """
        A Coxeter matrix can we created via a graph, a Coxeter type, or
        a matrix.

        .. NOTE::

            To disable the Coxeter type check, use the optional argument
            ``coxeter_type_check = False``.

        EXAMPLES::

            sage: C = CoxeterMatrix(['A',1,1],['a','b'])
            sage: C2 = CoxeterMatrix([[1, -1], [-1, 1]])
            sage: C3 = CoxeterMatrix(matrix([[1, -1], [-1, 1]]), [0, 1])
            sage: C == C2 and C == C3
            True

        Check with `\\infty` because of the hack of using `-1` to represent
        `\\infty` in the Coxeter matrix::

            sage: G = Graph([(0, 1, 3), (1, 2, oo)])
            sage: W1 = CoxeterMatrix([[1, 3, 2], [3, 1, -1], [2, -1, 1]])
            sage: W2 = CoxeterMatrix(G)
            sage: W1 == W2
            True
            sage: CoxeterMatrix(W1.coxeter_graph()) == W1
            True

        The base ring of the matrix depends on the entries given::

            sage: CoxeterMatrix([[1,-1],[-1,1]])._matrix.base_ring()
            Integer Ring
            sage: CoxeterMatrix([[1,-3/2],[-3/2,1]])._matrix.base_ring()
            Rational Field
            sage: CoxeterMatrix([[1,-1.5],[-1.5,1]])._matrix.base_ring()
            Real Field with 53 bits of precision
        """
    def __init__(self, parent, data, coxeter_type, index_set) -> None:
        '''
        Initialize ``self``.

        TESTS::

            sage: C = CoxeterMatrix([\'A\', 2, 1])
            sage: TestSuite(C).run(skip=["_test_category", "_test_change_ring"])
        '''
    @classmethod
    def samples(self, finite=None, affine=None, crystallographic=None, higher_rank=None):
        """
        Return a sample of the available Coxeter types.

        INPUT:

        - ``finite`` -- (default: ``None``) a boolean or ``None``

        - ``affine`` -- (default: ``None``) a boolean or ``None``

        - ``crystallographic`` -- (default: ``None``) a boolean or ``None``

        - ``higher_rank`` -- (default: ``None``) a boolean or ``None``

        The sample contains all the exceptional finite and affine
        Coxeter types, as well as typical representatives of the
        infinite families.

        Here the ``higher_rank`` term denotes non-finite, non-affine,
        Coxeter groups (including hyperbolic types).

        .. TODO:: Implement the hyperbolic and compact hyperbolic in the samples.

        EXAMPLES::

            sage: [CM.coxeter_type() for CM in CoxeterMatrix.samples()]
            [
            Coxeter type of ['A', 1], Coxeter type of ['A', 5],
            <BLANKLINE>
            Coxeter type of ['B', 5], Coxeter type of ['D', 4],
            <BLANKLINE>
            Coxeter type of ['D', 5], Coxeter type of ['E', 6],
            <BLANKLINE>
            Coxeter type of ['E', 7], Coxeter type of ['E', 8],
            <BLANKLINE>
            Coxeter type of ['F', 4], Coxeter type of ['H', 3],
            <BLANKLINE>
            Coxeter type of ['H', 4], Coxeter type of ['I', 10],
            <BLANKLINE>
            Coxeter type of ['A', 2, 1], Coxeter type of ['B', 5, 1],
            <BLANKLINE>
            Coxeter type of ['C', 5, 1], Coxeter type of ['D', 5, 1],
            <BLANKLINE>
            Coxeter type of ['E', 6, 1], Coxeter type of ['E', 7, 1],
            <BLANKLINE>
            Coxeter type of ['E', 8, 1], Coxeter type of ['F', 4, 1],
            <BLANKLINE>
                                                                      [ 1 -1 -1]
                                                                      [-1  1 -1]
            Coxeter type of ['G', 2, 1], Coxeter type of ['A', 1, 1], [-1 -1  1],
            <BLANKLINE>
                     [ 1 -2  3  2]
            [1 2 3]  [-2  1  2  3]
            [2 1 7]  [ 3  2  1 -8]
            [3 7 1], [ 2  3 -8  1]
            ]

        The finite, affine and crystallographic options allow
        respectively for restricting to (non) finite, (non) affine,
        and (non) crystallographic Cartan types::

            sage: [CM.coxeter_type() for CM in CoxeterMatrix.samples(finite=True)]
            [Coxeter type of ['A', 1], Coxeter type of ['A', 5],
             Coxeter type of ['B', 5], Coxeter type of ['D', 4],
             Coxeter type of ['D', 5], Coxeter type of ['E', 6],
             Coxeter type of ['E', 7], Coxeter type of ['E', 8],
             Coxeter type of ['F', 4], Coxeter type of ['H', 3],
             Coxeter type of ['H', 4], Coxeter type of ['I', 10]]

            sage: [CM.coxeter_type() for CM in CoxeterMatrix.samples(affine=True)]
            [Coxeter type of ['A', 2, 1], Coxeter type of ['B', 5, 1],
             Coxeter type of ['C', 5, 1], Coxeter type of ['D', 5, 1],
             Coxeter type of ['E', 6, 1], Coxeter type of ['E', 7, 1],
             Coxeter type of ['E', 8, 1], Coxeter type of ['F', 4, 1],
             Coxeter type of ['G', 2, 1], Coxeter type of ['A', 1, 1]]

            sage: [CM.coxeter_type() for CM in CoxeterMatrix.samples(crystallographic=True)]
            [Coxeter type of ['A', 1], Coxeter type of ['A', 5],
             Coxeter type of ['B', 5], Coxeter type of ['D', 4],
             Coxeter type of ['D', 5], Coxeter type of ['E', 6],
             Coxeter type of ['E', 7], Coxeter type of ['E', 8],
             Coxeter type of ['F', 4], Coxeter type of ['A', 2, 1],
             Coxeter type of ['B', 5, 1], Coxeter type of ['C', 5, 1],
             Coxeter type of ['D', 5, 1], Coxeter type of ['E', 6, 1],
             Coxeter type of ['E', 7, 1], Coxeter type of ['E', 8, 1],
             Coxeter type of ['F', 4, 1], Coxeter type of ['G', 2, 1]]

            sage: CoxeterMatrix.samples(crystallographic=False)
            [
                     [1 3 2 2]
            [1 3 2]  [3 1 3 2]                    [ 1 -1 -1]  [1 2 3]
            [3 1 5]  [2 3 1 5]  [ 1 10]  [ 1 -1]  [-1  1 -1]  [2 1 7]
            [2 5 1], [2 2 5 1], [10  1], [-1  1], [-1 -1  1], [3 7 1],
            <BLANKLINE>
            [ 1 -2  3  2]
            [-2  1  2  3]
            [ 3  2  1 -8]
            [ 2  3 -8  1]
            ]

        .. TODO:: add some reducible Coxeter types (suggestions?)

        TESTS::

            sage: for ct in CoxeterMatrix.samples(): TestSuite(ct).run()
        """
    def relabel(self, relabelling):
        """
        Return a relabelled copy of this Coxeter matrix.

        INPUT:

        - ``relabelling`` -- a function (or dictionary)

        OUTPUT:

        an isomorphic Coxeter type obtained by relabelling the nodes of
        the Coxeter graph. Namely, the node with label ``i`` is
        relabelled ``f(i)`` (or, by ``f[i]`` if ``f`` is a dictionary).

        EXAMPLES::

            sage: CoxeterMatrix(['F',4]).relabel({ 1:2, 2:3, 3:4, 4:1})
            [1 4 2 3]
            [4 1 3 2]
            [2 3 1 2]
            [3 2 2 1]
            sage: CoxeterMatrix(['F',4]).relabel(lambda x: x+1 if x<4 else 1)
            [1 4 2 3]
            [4 1 3 2]
            [2 3 1 2]
            [3 2 2 1]
        """
    def __reduce__(self):
        """
        Used for pickling.

        TESTS::

            sage: C = CoxeterMatrix(['A',4])
            sage: M = loads(dumps(C))
            sage: M._index_set
            (1, 2, 3, 4)
        """
    def __iter__(self):
        """
        Return an iterator for the rows of the Coxeter matrix.

        EXAMPLES::

            sage: CM = CoxeterMatrix([[1,8],[8,1]])
            sage: next(CM.__iter__())
            (1, 8)
        """
    def __getitem__(self, key):
        """
        Return a dictionary of labels adjacent to a node or
        the label of an edge in the Coxeter graph.

        EXAMPLES::

            sage: CM = CoxeterMatrix([[1,-2],[-2,1]])
            sage: CM = CoxeterMatrix([[1,-2],[-2,1]], ['a','b'])
            sage: CM['a']
            {'a': 1, 'b': -2}
            sage: CM['b']
            {'a': -2, 'b': 1}
            sage: CM['a','b']
            -2
            sage: CM['a','a']
            1
        """
    def __hash__(self):
        """
        Return hash of the Coxeter matrix.

        EXAMPLES::

            sage: CM = CoxeterMatrix([[1, -2], [-2, 1]], ['a', 'b'])
            sage: CM.__hash__()
            -337812865737895661  # 64-bit
            153276691            # 32-bit
            sage: CM = CoxeterMatrix([[1, -3], [-3, 1]], ['1', '2'])
            sage: CM.__hash__()
            -506719298606843492  # 64-bit
            -1917568612          # 32-bit
        """
    def __eq__(self, other):
        """
        Return if ``self`` and ``other`` are equal.

        EXAMPLES::

            sage: CM = CoxeterMatrix([[1,-2],[-2,1]],['a','b'])
            sage: CM2 = CoxeterMatrix([[1,-2],[-2,1]],['1','2'])
            sage: CM == CM2
            True
            sage: CM == matrix(CM)
            False
            sage: CM3 = CoxeterMatrix([[1,-3],[-3,1]],['1','2'])
            sage: CM == CM3
            False
        """
    def __ne__(self, other):
        """
        Return if ``self`` and ``other`` are not equal.

        EXAMPLES::

            sage: CM = CoxeterMatrix([[1,-2],[-2,1]],['a','b'])
            sage: CM2 = CoxeterMatrix([[1,-2],[-2,1]],['1','2'])
            sage: CM != CM2
            False
            sage: matrix(CM) != CM
            True
            sage: CM3 = CoxeterMatrix([[1,-3],[-3,1]],['1','2'])
            sage: CM != CM3
            True
        """
    def index_set(self):
        """
        Return the index set of ``self``.

        EXAMPLES::

            sage: C = CoxeterMatrix(['A',1,1])
            sage: C.index_set()
            (0, 1)
            sage: C = CoxeterMatrix(['E',6])
            sage: C.index_set()
            (1, 2, 3, 4, 5, 6)
        """
    def coxeter_type(self):
        """
        Return the Coxeter type of ``self`` or ``self`` if unknown.

        EXAMPLES::

            sage: C = CoxeterMatrix(['A',4,1])
            sage: C.coxeter_type()
            Coxeter type of ['A', 4, 1]

        If the Coxeter type is unknown::

            sage: C = CoxeterMatrix([[1,3,4], [3,1,-1], [4,-1,1]])
            sage: C.coxeter_type()
            [ 1  3  4]
            [ 3  1 -1]
            [ 4 -1  1]
        """
    def rank(self):
        '''
        Return the rank of ``self``.

        EXAMPLES::

            sage: CoxeterMatrix([\'C\',3]).rank()
            3
            sage: CoxeterMatrix(["A2","B2","F4"]).rank()
            8
        '''
    def coxeter_matrix(self):
        """
        Return the Coxeter matrix of ``self``.

        EXAMPLES::

            sage: CoxeterMatrix(['C',3]).coxeter_matrix()
            [1 3 2]
            [3 1 4]
            [2 4 1]
        """
    def bilinear_form(self, R=None):
        """
        Return the bilinear form of ``self``.

        EXAMPLES::

            sage: # needs sage.libs.gap
            sage: CoxeterType(['A', 2, 1]).bilinear_form()
            [   1 -1/2 -1/2]
            [-1/2    1 -1/2]
            [-1/2 -1/2    1]
            sage: CoxeterType(['H', 3]).bilinear_form()
            [                      1                    -1/2                       0]
            [                   -1/2                       1 1/2*E(5)^2 + 1/2*E(5)^3]
            [                      0 1/2*E(5)^2 + 1/2*E(5)^3                       1]
            sage: C = CoxeterMatrix([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
            sage: C.bilinear_form()
            [ 1 -1 -1]
            [-1  1 -1]
            [-1 -1  1]
        """
    @cached_method
    def coxeter_graph(self):
        """
        Return the Coxeter graph of ``self``.

        EXAMPLES::

            sage: C = CoxeterMatrix(['A',3])
            sage: C.coxeter_graph()
            Graph on 3 vertices

            sage: C = CoxeterMatrix([['A',3],['A',1]])
            sage: C.coxeter_graph()
            Graph on 4 vertices
        """
    def is_simply_laced(self):
        """
        Return if ``self`` is simply-laced.

        A Coxeter matrix is simply-laced if all non-diagonal entries are
        either 2 or 3.

        EXAMPLES::

            sage: cm = CoxeterMatrix([[1,3,3,3], [3,1,3,3], [3,3,1,3], [3,3,3,1]])
            sage: cm.is_simply_laced()
            True
        """
    def is_crystallographic(self):
        """
        Return whether ``self`` is crystallographic.

        A Coxeter matrix is crystallographic if all non-diagonal entries
        are either 2, 3, 4, or 6.

        EXAMPLES::

            sage: CoxeterMatrix(['F',4]).is_crystallographic()
            True
            sage: CoxeterMatrix(['H',3]).is_crystallographic()
            False
        """
    def is_irreducible(self):
        """
        Return whether ``self`` is irreducible.

        A Coxeter matrix is irreducible if the Coxeter graph is connected.

        EXAMPLES::

            sage: CoxeterMatrix([['F',4],['A',1]]).is_irreducible()
            False
            sage: CoxeterMatrix(['H',3]).is_irreducible()
            True
        """
    def is_finite(self):
        """
        Return if ``self`` is a finite type or ``False`` if unknown.

        EXAMPLES::

            sage: M = CoxeterMatrix(['C',4])
            sage: M.is_finite()
            True
            sage: M = CoxeterMatrix(['D',4,1])
            sage: M.is_finite()
            False
            sage: M = CoxeterMatrix([[1, -1], [-1, 1]])
            sage: M.is_finite()
            False
        """
    def is_affine(self):
        """
        Return if ``self`` is an affine type or ``False`` if unknown.

        EXAMPLES::

            sage: M = CoxeterMatrix(['C',4])
            sage: M.is_affine()
            False
            sage: M = CoxeterMatrix(['D',4,1])
            sage: M.is_affine()
            True
            sage: M = CoxeterMatrix([[1, 3],[3,1]])
            sage: M.is_affine()
            False
            sage: M = CoxeterMatrix([[1, -1, 7], [-1, 1, 3], [7, 3, 1]])
            sage: M.is_affine()
            False
        """

def recognize_coxeter_type_from_matrix(coxeter_matrix, index_set):
    """
    Return the Coxeter type of ``coxeter_matrix`` if known,
    otherwise return ``None``.

    EXAMPLES:

    Some infinite ones::

        sage: C = CoxeterMatrix([[1,3,2],[3,1,-1],[2,-1,1]])
        sage: C.is_finite()  # indirect doctest
        False
        sage: C = CoxeterMatrix([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
        sage: C.is_finite()  # indirect doctest
        False

    Some finite ones::

        sage: m = matrix(CoxeterMatrix(['D', 4]))
        sage: CoxeterMatrix(m).is_finite()  # indirect doctest
        True
        sage: m = matrix(CoxeterMatrix(['H', 4]))
        sage: CoxeterMatrix(m).is_finite()  # indirect doctest
        True

        sage: CoxeterMatrix(CoxeterType(['A',10]).coxeter_graph()).coxeter_type()
        Coxeter type of ['A', 10]
        sage: CoxeterMatrix(CoxeterType(['B',10]).coxeter_graph()).coxeter_type()
        Coxeter type of ['B', 10]
        sage: CoxeterMatrix(CoxeterType(['C',10]).coxeter_graph()).coxeter_type()
        Coxeter type of ['B', 10]
        sage: CoxeterMatrix(CoxeterType(['D',10]).coxeter_graph()).coxeter_type()
        Coxeter type of ['D', 10]
        sage: CoxeterMatrix(CoxeterType(['E',6]).coxeter_graph()).coxeter_type()
        Coxeter type of ['E', 6]
        sage: CoxeterMatrix(CoxeterType(['E',7]).coxeter_graph()).coxeter_type()
        Coxeter type of ['E', 7]
        sage: CoxeterMatrix(CoxeterType(['E',8]).coxeter_graph()).coxeter_type()
        Coxeter type of ['E', 8]
        sage: CoxeterMatrix(CoxeterType(['F',4]).coxeter_graph()).coxeter_type()
        Coxeter type of ['F', 4]
        sage: CoxeterMatrix(CoxeterType(['G',2]).coxeter_graph()).coxeter_type()
        Coxeter type of ['G', 2]
        sage: CoxeterMatrix(CoxeterType(['H',3]).coxeter_graph()).coxeter_type()
        Coxeter type of ['H', 3]
        sage: CoxeterMatrix(CoxeterType(['H',4]).coxeter_graph()).coxeter_type()
        Coxeter type of ['H', 4]
        sage: CoxeterMatrix(CoxeterType(['I',100]).coxeter_graph()).coxeter_type()
        Coxeter type of ['I', 100]

    Some affine graphs::

        sage: CoxeterMatrix(CoxeterType(['A',1,1]).coxeter_graph()).coxeter_type()
        Coxeter type of ['A', 1, 1]
        sage: CoxeterMatrix(CoxeterType(['A',10,1]).coxeter_graph()).coxeter_type()
        Coxeter type of ['A', 10, 1]
        sage: CoxeterMatrix(CoxeterType(['B',10,1]).coxeter_graph()).coxeter_type()
        Coxeter type of ['B', 10, 1]
        sage: CoxeterMatrix(CoxeterType(['C',10,1]).coxeter_graph()).coxeter_type()
        Coxeter type of ['C', 10, 1]
        sage: CoxeterMatrix(CoxeterType(['D',10,1]).coxeter_graph()).coxeter_type()
        Coxeter type of ['D', 10, 1]
        sage: CoxeterMatrix(CoxeterType(['E',6,1]).coxeter_graph()).coxeter_type()
        Coxeter type of ['E', 6, 1]
        sage: CoxeterMatrix(CoxeterType(['E',7,1]).coxeter_graph()).coxeter_type()
        Coxeter type of ['E', 7, 1]
        sage: CoxeterMatrix(CoxeterType(['E',8,1]).coxeter_graph()).coxeter_type()
        Coxeter type of ['E', 8, 1]
        sage: CoxeterMatrix(CoxeterType(['F',4,1]).coxeter_graph()).coxeter_type()
        Coxeter type of ['F', 4, 1]
        sage: CoxeterMatrix(CoxeterType(['G',2,1]).coxeter_graph()).coxeter_type()
        Coxeter type of ['G', 2, 1]

    TESTS:

    Check that we detect relabellings::

        sage: M = CoxeterMatrix([[1,2,3],[2,1,6],[3,6,1]], index_set=['a', 'b', 'c'])
        sage: M.coxeter_type()
        Coxeter type of ['G', 2, 1] relabelled by {0: 'a', 1: 'b', 2: 'c'}

        sage: from sage.combinat.root_system.coxeter_matrix import recognize_coxeter_type_from_matrix
        sage: for C in CoxeterMatrix.samples():
        ....:     relabelling_perm = Permutations(C.index_set()).random_element()
        ....:     relabelling_dict = {C.index_set()[i]: relabelling_perm[i] for i in range(C.rank())}
        ....:     relabeled_matrix = C.relabel(relabelling_dict)._matrix
        ....:     recognized_type = recognize_coxeter_type_from_matrix(relabeled_matrix, relabelling_perm)
        ....:     if C.is_finite() or C.is_affine():
        ....:         assert recognized_type == C.coxeter_type()

    We check the rank 2 cases (:issue:`20419`)::

        sage: for i in range(2, 10):
        ....:     M = matrix([[1,i],[i,1]])
        ....:     CoxeterMatrix(M).coxeter_type()
        Coxeter type of A1xA1 relabelled by {1: 2}
        Coxeter type of ['A', 2]
        Coxeter type of ['B', 2]
        Coxeter type of ['I', 5]
        Coxeter type of ['G', 2]
        Coxeter type of ['I', 7]
        Coxeter type of ['I', 8]
        Coxeter type of ['I', 9]
        sage: CoxeterMatrix(matrix([[1,-1],[-1,1]]), index_set=[0,1]).coxeter_type()
        Coxeter type of ['A', 1, 1]

    Check that this works for reducible types with relabellings
    (:issue:`24892`)::

        sage: CM = CoxeterMatrix([[1,2,5],[2,1,2],[5,2,1]]); CM
        [1 2 5]
        [2 1 2]
        [5 2 1]
        sage: CM.coxeter_type()
        Coxeter type of I5 relabelled by {1: 1, 2: 3}xA1 relabelled by {1: 2}
    """
def check_coxeter_matrix(m) -> None:
    """
    Check if ``m`` represents a generalized Coxeter matrix and raise
    and error if not.

    EXAMPLES::

        sage: from sage.combinat.root_system.coxeter_matrix import check_coxeter_matrix
        sage: m = matrix([[1,3,2],[3,1,-1],[2,-1,1]])
        sage: check_coxeter_matrix(m)

        sage: m = matrix([[1,3],[3,1],[2,-1]])
        sage: check_coxeter_matrix(m)
        Traceback (most recent call last):
        ...
        ValueError: not a square matrix

        sage: m = matrix([[1,3,2],[3,1,-1],[2,-1,2]])
        sage: check_coxeter_matrix(m)
        Traceback (most recent call last):
        ...
        ValueError: the matrix diagonal is not all 1

        sage: m = matrix([[1,3,3],[3,1,-1],[2,-1,1]])
        sage: check_coxeter_matrix(m)
        Traceback (most recent call last):
        ...
        ValueError: the matrix is not symmetric

        sage: m = matrix([[1,3,1/2],[3,1,-1],[1/2,-1,1]])
        sage: check_coxeter_matrix(m)
        Traceback (most recent call last):
        ...
        ValueError: invalid Coxeter label 1/2

        sage: m = matrix([[1,3,1],[3,1,-1],[1,-1,1]])
        sage: check_coxeter_matrix(m)
        Traceback (most recent call last):
        ...
        ValueError: invalid Coxeter label 1
    """
def coxeter_matrix_as_function(t):
    """
    Return the Coxeter matrix, as a function.

    INPUT:

    - ``t`` -- a Cartan type

    EXAMPLES::

        sage: from sage.combinat.root_system.coxeter_matrix import coxeter_matrix_as_function
        sage: f = coxeter_matrix_as_function(['A',4])
        sage: matrix([[f(i,j) for j in range(1,5)] for i in range(1,5)])
        [1 3 2 2]
        [3 1 3 2]
        [2 3 1 3]
        [2 2 3 1]
    """
