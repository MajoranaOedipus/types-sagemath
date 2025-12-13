from sage.combinat.root_system.cartan_type import CartanType as CartanType, CartanType_abstract as CartanType_abstract
from sage.combinat.root_system.root_system import RootSystem as RootSystem
from sage.combinat.subset import powerset as powerset
from sage.matrix.constructor import matrix as matrix
from sage.matrix.matrix_generic_sparse import Matrix_generic_sparse as Base
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.cachefunc import cached_method as cached_method
from sage.misc.classcall_metaclass import typecall as typecall
from sage.misc.inherit_comparison import InheritComparisonClasscallMetaclass as InheritComparisonClasscallMetaclass
from sage.misc.lazy_import import lazy_import as lazy_import
from sage.rings.integer_ring import ZZ as ZZ
from sage.sets.family import Family as Family
from sage.structure.element import Matrix as Matrix

class CartanMatrix(Base, CartanType_abstract, metaclass=InheritComparisonClasscallMetaclass):
    """
    A (generalized) Cartan matrix.

    A matrix `A = (a_{ij})_{i,j \\in I}` for some index set `I` is a
    generalized Cartan matrix if it satisfies the following properties:

    - `a_{ii} = 2` for all `i`,
    - `a_{ij} \\leq 0` for all `i \\neq j`,
    - `a_{ij} = 0` if and only if `a_{ji} = 0` for all `i \\neq j`.

    Additionally some reference assume that a Cartan matrix is
    *symmetrizable* (see :meth:`is_symmetrizable`). However following Kac, we
    do not make that assumption here.

    An even, integral Borcherds--Cartan matrix is an integral matrix
    `A = (a_{ij})_{i,j \\in I}` for some countable index set `I` which satisfies
    the following properties:

    - `a_{ii} \\in \\{2\\} \\cup 2\\ZZ_{<0}` for all `i`,
    - `a_{ij} \\leq 0` for all `i \\neq j`,
    - `a_{ij} = 0` if and only if `a_{ji} = 0` for all `i \\neq j`.

    INPUT:

    Can be anything which is accepted by ``CartanType`` or a matrix.

    If given a matrix, one can also use the keyword ``cartan_type`` when giving
    a matrix to explicitly state the type. Otherwise this will try to check the
    input matrix against possible standard types of Cartan matrices. To disable
    this check, use the keyword ``cartan_type_check = False``.

    If one wants to initialize a Borcherds-Cartan matrix using matrix data,
    use the keyword ``borcherds=True``. To specify the diagonal entries of
    corresponding to a Cartan type (a Cartan matrix is treated as matrix data),
    use ``borcherds`` with a list of the diagonal entries.

    EXAMPLES::

        sage: # needs sage.graphs
        sage: CartanMatrix(['A', 4])
        [ 2 -1  0  0]
        [-1  2 -1  0]
        [ 0 -1  2 -1]
        [ 0  0 -1  2]
        sage: CartanMatrix(['B', 6])
        [ 2 -1  0  0  0  0]
        [-1  2 -1  0  0  0]
        [ 0 -1  2 -1  0  0]
        [ 0  0 -1  2 -1  0]
        [ 0  0  0 -1  2 -1]
        [ 0  0  0  0 -2  2]
        sage: CartanMatrix(['C', 4])
        [ 2 -1  0  0]
        [-1  2 -1  0]
        [ 0 -1  2 -2]
        [ 0  0 -1  2]
        sage: CartanMatrix(['D', 6])
        [ 2 -1  0  0  0  0]
        [-1  2 -1  0  0  0]
        [ 0 -1  2 -1  0  0]
        [ 0  0 -1  2 -1 -1]
        [ 0  0  0 -1  2  0]
        [ 0  0  0 -1  0  2]
        sage: CartanMatrix(['E',6])
        [ 2  0 -1  0  0  0]
        [ 0  2  0 -1  0  0]
        [-1  0  2 -1  0  0]
        [ 0 -1 -1  2 -1  0]
        [ 0  0  0 -1  2 -1]
        [ 0  0  0  0 -1  2]
        sage: CartanMatrix(['E',7])
        [ 2  0 -1  0  0  0  0]
        [ 0  2  0 -1  0  0  0]
        [-1  0  2 -1  0  0  0]
        [ 0 -1 -1  2 -1  0  0]
        [ 0  0  0 -1  2 -1  0]
        [ 0  0  0  0 -1  2 -1]
        [ 0  0  0  0  0 -1  2]
        sage: CartanMatrix(['E', 8])
        [ 2  0 -1  0  0  0  0  0]
        [ 0  2  0 -1  0  0  0  0]
        [-1  0  2 -1  0  0  0  0]
        [ 0 -1 -1  2 -1  0  0  0]
        [ 0  0  0 -1  2 -1  0  0]
        [ 0  0  0  0 -1  2 -1  0]
        [ 0  0  0  0  0 -1  2 -1]
        [ 0  0  0  0  0  0 -1  2]
        sage: CartanMatrix(['F', 4])
        [ 2 -1  0  0]
        [-1  2 -1  0]
        [ 0 -2  2 -1]
        [ 0  0 -1  2]

    This is different from MuPAD-Combinat, due to different node
    convention?

    ::

        sage: # needs sage.graphs
        sage: CartanMatrix(['G', 2])
        [ 2 -3]
        [-1  2]
        sage: CartanMatrix(['A',1,1])
        [ 2 -2]
        [-2  2]
        sage: CartanMatrix(['A', 3, 1])
        [ 2 -1  0 -1]
        [-1  2 -1  0]
        [ 0 -1  2 -1]
        [-1  0 -1  2]
        sage: CartanMatrix(['B', 3, 1])
        [ 2  0 -1  0]
        [ 0  2 -1  0]
        [-1 -1  2 -1]
        [ 0  0 -2  2]
        sage: CartanMatrix(['C', 3, 1])
        [ 2 -1  0  0]
        [-2  2 -1  0]
        [ 0 -1  2 -2]
        [ 0  0 -1  2]
        sage: CartanMatrix(['D', 4, 1])
        [ 2  0 -1  0  0]
        [ 0  2 -1  0  0]
        [-1 -1  2 -1 -1]
        [ 0  0 -1  2  0]
        [ 0  0 -1  0  2]
        sage: CartanMatrix(['E', 6, 1])
        [ 2  0 -1  0  0  0  0]
        [ 0  2  0 -1  0  0  0]
        [-1  0  2  0 -1  0  0]
        [ 0 -1  0  2 -1  0  0]
        [ 0  0 -1 -1  2 -1  0]
        [ 0  0  0  0 -1  2 -1]
        [ 0  0  0  0  0 -1  2]
        sage: CartanMatrix(['E', 7, 1])
        [ 2 -1  0  0  0  0  0  0]
        [-1  2  0 -1  0  0  0  0]
        [ 0  0  2  0 -1  0  0  0]
        [ 0 -1  0  2 -1  0  0  0]
        [ 0  0 -1 -1  2 -1  0  0]
        [ 0  0  0  0 -1  2 -1  0]
        [ 0  0  0  0  0 -1  2 -1]
        [ 0  0  0  0  0  0 -1  2]
        sage: CartanMatrix(['E', 8, 1])
        [ 2  0  0  0  0  0  0  0 -1]
        [ 0  2  0 -1  0  0  0  0  0]
        [ 0  0  2  0 -1  0  0  0  0]
        [ 0 -1  0  2 -1  0  0  0  0]
        [ 0  0 -1 -1  2 -1  0  0  0]
        [ 0  0  0  0 -1  2 -1  0  0]
        [ 0  0  0  0  0 -1  2 -1  0]
        [ 0  0  0  0  0  0 -1  2 -1]
        [-1  0  0  0  0  0  0 -1  2]
        sage: CartanMatrix(['F', 4, 1])
        [ 2 -1  0  0  0]
        [-1  2 -1  0  0]
        [ 0 -1  2 -1  0]
        [ 0  0 -2  2 -1]
        [ 0  0  0 -1  2]
        sage: CartanMatrix(['G', 2, 1])
        [ 2  0 -1]
        [ 0  2 -3]
        [-1 -1  2]

    Examples of Borcherds-Cartan matrices::

        sage: CartanMatrix([[2,-1],[-1,-2]], borcherds=True)                            # needs sage.graphs
        [ 2 -1]
        [-1 -2]
        sage: CartanMatrix('B3', borcherds=[-4,-6,2])                                   # needs sage.graphs
        [-4 -1  0]
        [-1 -6 -1]
        [ 0 -2  2]

    .. NOTE::

        Since this is a matrix, :meth:`row()` and :meth:`column()` will return
        the standard row and column respectively. To get the row with the
        indices as in Dynkin diagrams/Cartan types, use
        :meth:`row_with_indices()` and :meth:`column_with_indices()`
        respectively.
    """
    @staticmethod
    def __classcall_private__(cls, data=None, index_set=None, cartan_type=None, cartan_type_check: bool = True, borcherds=None):
        """
        Normalize input so we can inherit from sparse integer matrix.

        .. NOTE::

            To disable the Cartan type check, use the optional argument
            ``cartan_type_check = False``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: C = CartanMatrix(['A',1,1])
            sage: C2 = CartanMatrix([[2, -2], [-2, 2]])
            sage: C3 = CartanMatrix(matrix([[2, -2], [-2, 2]]), [0, 1])
            sage: C == C2 and C == C3
            True

        TESTS:

        Check that :issue:`15740` is fixed::

            sage: # needs sage.graphs
            sage: d = DynkinDiagram()
            sage: d.add_edge('a', 'b', 2)
            sage: d.index_set()
            ('a', 'b')
            sage: cm = CartanMatrix(d)
            sage: cm.index_set()
            ('a', 'b')
        """
    def matrix_space(self, nrows=None, ncols=None, sparse=None):
        """
        Return a matrix space over the integers.

        INPUT:

        - ``nrows`` -- number of rows

        - ``ncols`` -- number of columns

        - ``sparse`` -- boolean

        EXAMPLES::

            sage: # needs sage.graphs
            sage: cm = CartanMatrix(['A', 3])
            sage: cm.matrix_space()
            Full MatrixSpace of 3 by 3 sparse matrices over Integer Ring
            sage: cm.matrix_space(2, 2)
            Full MatrixSpace of 2 by 2 sparse matrices over Integer Ring
            sage: cm[:2,1:]   # indirect doctest
            [-1  0]
            [ 2 -1]
        """
    def __reduce__(self):
        """
        Used for pickling.

        TESTS::

            sage: CM = CartanMatrix(['A',4])                                            # needs sage.graphs
            sage: x = loads(dumps(CM))                                                  # needs sage.graphs
            sage: x._index_set                                                          # needs sage.graphs
            (1, 2, 3, 4)
        """
    def root_system(self):
        """
        Return the root system corresponding to ``self``.

        EXAMPLES::

            sage: C = CartanMatrix(['A',3])                                             # needs sage.graphs
            sage: C.root_system()                                                       # needs sage.graphs
            Root system of type ['A', 3]
        """
    def root_space(self):
        """
        Return the root space corresponding to ``self``.

        EXAMPLES::

            sage: C = CartanMatrix(['A',3])                                             # needs sage.graphs
            sage: C.root_space()                                                        # needs sage.graphs
            Root space over the Rational Field of the Root system of type ['A', 3]
        """
    def reflection_group(self, type: str = 'matrix'):
        """
        Return the reflection group corresponding to ``self``.

        EXAMPLES::

            sage: C = CartanMatrix(['A',3])                                             # needs sage.graphs
            sage: C.reflection_group()                                                  # needs sage.graphs sage.libs.gap
            Weyl Group of type ['A', 3] (as a matrix group acting on the root space)
        """
    def symmetrizer(self):
        """
        Return the symmetrizer of ``self``.

        EXAMPLES::

            sage: cm = CartanMatrix([[2,-5],[-2,2]])                                    # needs sage.graphs
            sage: cm.symmetrizer()                                                      # needs sage.graphs
            Finite family {0: 2, 1: 5}

        TESTS:

        Check that the symmetrizer computed from the Cartan matrix agrees
        with the values given by the Cartan type::

            sage: ct = CartanType(['B',4,1])
            sage: ct.symmetrizer()                                                      # needs sage.graphs
            Finite family {0: 2, 1: 2, 2: 2, 3: 2, 4: 1}
            sage: ct.cartan_matrix().symmetrizer()                                      # needs sage.graphs
            Finite family {0: 2, 1: 2, 2: 2, 3: 2, 4: 1}
        """
    @cached_method
    def symmetrized_matrix(self):
        """
        Return the symmetrized matrix of ``self`` if symmetrizable.

        EXAMPLES::

            sage: cm = CartanMatrix(['B',4,1])                                          # needs sage.graphs
            sage: cm.symmetrized_matrix()                                               # needs sage.graphs
            [ 4  0 -2  0  0]
            [ 0  4 -2  0  0]
            [-2 -2  4 -2  0]
            [ 0  0 -2  4 -2]
            [ 0  0  0 -2  2]
        """
    def index_set(self):
        """
        Return the index set of ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: C = CartanMatrix(['A',1,1])
            sage: C.index_set()
            (0, 1)
            sage: C = CartanMatrix(['E',6])
            sage: C.index_set()
            (1, 2, 3, 4, 5, 6)
        """
    def cartan_type(self):
        """
        Return the Cartan type of ``self`` or ``self`` if unknown.

        EXAMPLES::

            sage: C = CartanMatrix(['A',4,1])                                           # needs sage.graphs
            sage: C.cartan_type()                                                       # needs sage.graphs
            ['A', 4, 1]

        If the Cartan type is unknown::

            sage: C = CartanMatrix([[2,-1,-2], [-1,2,-1], [-2,-1,2]])                   # needs sage.graphs
            sage: C.cartan_type()                                                       # needs sage.graphs
            [ 2 -1 -2]
            [-1  2 -1]
            [-2 -1  2]
        """
    def subtype(self, index_set):
        """
        Return a subtype of ``self`` given by ``index_set``.

        A subtype can be considered the Dynkin diagram induced from
        the Dynkin diagram of ``self`` by ``index_set``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: C = CartanMatrix(['F',4])
            sage: S = C.subtype([1,2,3])
            sage: S
            [ 2 -1  0]
            [-1  2 -1]
            [ 0 -2  2]
            sage: S.index_set()
            (1, 2, 3)
        """
    def rank(self):
        '''
        Return the rank of ``self``.

        EXAMPLES::

            sage: CartanMatrix([\'C\',3]).rank()                                          # needs sage.graphs
            3
            sage: CartanMatrix(["A2","B2","F4"]).rank()                                 # needs sage.graphs
            8
        '''
    def relabel(self, relabelling):
        """
        Return the relabelled Cartan matrix.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: CM = CartanMatrix(['C',3])
            sage: R = CM.relabel({1:0, 2:4, 3:1}); R
            [ 2  0 -1]
            [ 0  2 -1]
            [-1 -2  2]
            sage: R.index_set()
            (0, 1, 4)
            sage: CM
            [ 2 -1  0]
            [-1  2 -2]
            [ 0 -1  2]
        """
    @cached_method
    def dynkin_diagram(self):
        """
        Return the Dynkin diagram corresponding to ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: C = CartanMatrix(['A',2])
            sage: C.dynkin_diagram()
            O---O
            1   2
            A2
            sage: C = CartanMatrix(['F',4,1])
            sage: C.dynkin_diagram()
            O---O---O=>=O---O
            0   1   2   3   4
            F4~
            sage: C = CartanMatrix([[2,-4],[-4,2]])
            sage: C.dynkin_diagram()
            Dynkin diagram of rank 2
        """
    def cartan_matrix(self):
        """
        Return the Cartan matrix of ``self``.

        EXAMPLES::

            sage: CartanMatrix(['C',3]).cartan_matrix()                                 # needs sage.graphs
            [ 2 -1  0]
            [-1  2 -2]
            [ 0 -1  2]
        """
    def dual(self):
        """
        Return the dual Cartan matrix of ``self``, which is obtained by taking
        the transpose.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: ct = CartanType(['C',3])
            sage: M = CartanMatrix(ct); M
            [ 2 -1  0]
            [-1  2 -2]
            [ 0 -1  2]
            sage: M.dual()
            [ 2 -1  0]
            [-1  2 -1]
            [ 0 -2  2]
            sage: M.dual() == CartanMatrix(ct.dual())
            True
            sage: M.dual().cartan_type() == ct.dual()
            True

        An example with arbitrary Cartan matrices::

            sage: # needs sage.graphs
            sage: cm = CartanMatrix([[2,-5], [-2, 2]]); cm
            [ 2 -5]
            [-2  2]
            sage: cm.dual()
            [ 2 -2]
            [-5  2]
            sage: cm.dual() == CartanMatrix(cm.transpose())
            True
            sage: cm.dual().dual() == cm
            True
        """
    def is_simply_laced(self):
        """
        Implement :meth:`CartanType_abstract.is_simply_laced()`.

        A Cartan matrix is simply-laced if all non diagonal entries are `0`
        or `-1`.

        EXAMPLES::

            sage: cm = CartanMatrix([[2, -1, -1, -1], [-1, 2, -1, -1],                  # needs sage.graphs
            ....:                    [-1, -1, 2, -1], [-1, -1, -1, 2]])
            sage: cm.is_simply_laced()                                                  # needs sage.graphs
            True
        """
    def is_crystallographic(self):
        """
        Implement :meth:`CartanType_abstract.is_crystallographic`.

        A Cartan matrix is crystallographic if it is symmetrizable.

        EXAMPLES::

            sage: CartanMatrix(['F',4]).is_crystallographic()                           # needs sage.graphs
            True
        """
    def column_with_indices(self, j):
        """
        Return the `j`-th column `(a_{i,j})_i` of ``self`` as a container
        (or iterator) of tuples `(i, a_{i,j})`

        EXAMPLES::

            sage: M = CartanMatrix(['B',4])                                             # needs sage.graphs
            sage: [ (i,a) for (i,a) in M.column_with_indices(3) ]                       # needs sage.graphs
            [(3, 2), (2, -1), (4, -2)]
        """
    def row_with_indices(self, i):
        """
        Return the `i`-th row `(a_{i,j})_j` of ``self`` as a container
        (or iterator) of tuples `(j, a_{i,j})`

        EXAMPLES::

            sage: M = CartanMatrix(['C',4])                                             # needs sage.graphs
            sage: [ (i,a) for (i,a) in M.row_with_indices(3) ]                          # needs sage.graphs
            [(3, 2), (2, -1), (4, -2)]
        """
    @cached_method
    def is_finite(self):
        """
        Return ``True`` if ``self`` is a finite type or ``False`` otherwise.

        A generalized Cartan matrix is finite if the determinant of all its
        principal submatrices (see :meth:`principal_submatrices`) is positive.
        Such matrices have a positive definite symmetrized matrix. Note that a
        finite matrix may consist of multiple blocks of Cartan matrices each
        having finite Cartan type.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: M = CartanMatrix(['C',4])
            sage: M.is_finite()
            True
            sage: M = CartanMatrix(['D',4,1])
            sage: M.is_finite()
            False
            sage: M = CartanMatrix([[2, -4], [-3, 2]])
            sage: M.is_finite()
            False
        """
    @cached_method
    def is_affine(self):
        """
        Return ``True`` if ``self`` is an affine type or ``False`` otherwise.

        A generalized Cartan matrix is affine if all of its indecomposable
        blocks are either finite (see :meth:`is_finite`) or have zero
        determinant with all proper principal minors positive.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: M = CartanMatrix(['C',4])
            sage: M.is_affine()
            False
            sage: M = CartanMatrix(['D',4,1])
            sage: M.is_affine()
            True
            sage: M = CartanMatrix([[2, -4], [-3, 2]])
            sage: M.is_affine()
            False
        """
    @cached_method
    def is_hyperbolic(self, compact: bool = False):
        """
        Return if ``True`` if ``self`` is a (compact) hyperbolic type
        or ``False`` otherwise.

        An indecomposable generalized Cartan matrix is hyperbolic if it has
        negative determinant and if any proper connected subdiagram of its
        Dynkin diagram is of finite or affine type. It is compact hyperbolic
        if any proper connected subdiagram has finite type.

        INPUT:

        - ``compact`` -- if ``True``, check if matrix is compact hyperbolic

        EXAMPLES::

            sage: # needs sage.graphs
            sage: M = CartanMatrix([[2,-2,0],[-2,2,-1],[0,-1,2]])
            sage: M.is_hyperbolic()
            True
            sage: M.is_hyperbolic(compact=True)
            False
            sage: M = CartanMatrix([[2,-3],[-3,2]])
            sage: M.is_hyperbolic()
            True
            sage: M = CartanMatrix(['C',4])
            sage: M.is_hyperbolic()
            False
        """
    @cached_method
    def is_lorentzian(self):
        """
        Return ``True`` if ``self`` is a Lorentzian type or ``False`` otherwise.

        A generalized Cartan matrix is Lorentzian if it has negative determinant
        and exactly one negative eigenvalue.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: M = CartanMatrix([[2,-3],[-3,2]])
            sage: M.is_lorentzian()
            True
            sage: M = CartanMatrix([[2,-1],[-1,2]])
            sage: M.is_lorentzian()
            False
        """
    @cached_method
    def is_indefinite(self):
        '''
        Return if ``self`` is an indefinite type or ``False`` otherwise.

        EXAMPLES::

           sage: # needs sage.graphs
           sage: M = CartanMatrix([[2,-3],[-3,2]])
           sage: M.is_indefinite()
           True
           sage: M = CartanMatrix("A2")
           sage: M.is_indefinite()
           False
        '''
    @cached_method
    def is_indecomposable(self):
        """
        Return if ``self`` is an indecomposable matrix or ``False`` otherwise.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: M = CartanMatrix(['A',5])
            sage: M.is_indecomposable()
            True
            sage: M = CartanMatrix([[2,-1,0],[-1,2,0],[0,0,2]])
            sage: M.is_indecomposable()
            False
        """
    @cached_method
    def coxeter_matrix(self):
        """
        Return the Coxeter matrix for ``self``.

        .. SEEALSO:: :meth:`CartanType_abstract.coxeter_matrix`

        EXAMPLES::

            sage: # needs sage.graphs
            sage: cm = CartanMatrix([[2,-5,0],[-2,2,-1],[0,-1,2]])
            sage: cm.coxeter_matrix()
            [ 1 -1  2]
            [-1  1  3]
            [ 2  3  1]
            sage: ct = CartanType([['A',2,2], ['B',3]])
            sage: ct.coxeter_matrix()
            [ 1 -1  2  2  2]
            [-1  1  2  2  2]
            [ 2  2  1  3  2]
            [ 2  2  3  1  4]
            [ 2  2  2  4  1]
            sage: ct.cartan_matrix().coxeter_matrix() == ct.coxeter_matrix()
            True
        """
    @cached_method
    def coxeter_diagram(self):
        """
        Construct the Coxeter diagram of ``self``.

        .. SEEALSO:: :meth:`CartanType_abstract.coxeter_diagram`

        EXAMPLES::

            sage: # needs sage.graphs
            sage: cm = CartanMatrix([[2,-5,0],[-2,2,-1],[0,-1,2]])
            sage: G = cm.coxeter_diagram(); G
            Graph on 3 vertices
            sage: G.edges(sort=True)
            [(0, 1, +Infinity), (1, 2, 3)]
            sage: ct = CartanType([['A',2,2], ['B',3]])
            sage: ct.coxeter_diagram()
            Graph on 5 vertices
            sage: ct.cartan_matrix().coxeter_diagram() == ct.coxeter_diagram()
            True
        """
    def principal_submatrices(self, proper: bool = False):
        """
        Return a list of all principal submatrices of ``self``.

        INPUT:

        - ``proper`` -- if ``True``, return only proper submatrices

        EXAMPLES::

            sage: M = CartanMatrix(['A',2])                                             # needs sage.graphs
            sage: M.principal_submatrices()                                             # needs sage.graphs
            [
                          [ 2 -1]
            [], [2], [2], [-1  2]
            ]
            sage: M.principal_submatrices(proper=True)                                  # needs sage.graphs
            [[], [2], [2]]
        """
    @cached_method
    def indecomposable_blocks(self):
        """
        Return a tuple of all indecomposable blocks of ``self``.

        EXAMPLES::

            sage: # needs sage.graphs
            sage: M = CartanMatrix(['A',2])
            sage: M.indecomposable_blocks()
            (
            [ 2 -1]
            [-1  2]
            )
            sage: M = CartanMatrix([['A',2,1],['A',3,1]])
            sage: M.indecomposable_blocks()
            (
            [ 2 -1  0 -1]
            [-1  2 -1  0]  [ 2 -1 -1]
            [ 0 -1  2 -1]  [-1  2 -1]
            [-1  0 -1  2], [-1 -1  2]
            )
        """

def is_borcherds_cartan_matrix(M):
    """
    Return ``True`` if ``M`` is an even, integral Borcherds-Cartan matrix.
    For a definition of such a matrix, see :class:`CartanMatrix`.

    EXAMPLES::

        sage: from sage.combinat.root_system.cartan_matrix import is_borcherds_cartan_matrix
        sage: M = Matrix([[2,-1],[-1,2]])
        sage: is_borcherds_cartan_matrix(M)
        True
        sage: N = Matrix([[2,-1],[-1,0]])
        sage: is_borcherds_cartan_matrix(N)
        False
        sage: O = Matrix([[2,-1],[-1,-2]])
        sage: is_borcherds_cartan_matrix(O)
        True
        sage: O = Matrix([[2,-1],[-1,-3]])
        sage: is_borcherds_cartan_matrix(O)
        False
    """
def is_generalized_cartan_matrix(M):
    """
    Return ``True`` if ``M`` is a generalized Cartan matrix. For a definition
    of a generalized Cartan matrix, see :class:`CartanMatrix`.

    EXAMPLES::

        sage: from sage.combinat.root_system.cartan_matrix import is_generalized_cartan_matrix
        sage: M = matrix([[2,-1,-2], [-1,2,-1], [-2,-1,2]])
        sage: is_generalized_cartan_matrix(M)
        True
        sage: M = matrix([[2,-1,-2], [-1,2,-1], [0,-1,2]])
        sage: is_generalized_cartan_matrix(M)
        False
        sage: M = matrix([[1,-1,-2], [-1,2,-1], [-2,-1,2]])
        sage: is_generalized_cartan_matrix(M)
        False

    A non-symmetrizable example::

        sage: M = matrix([[2,-1,-2], [-1,2,-1], [-1,-1,2]])
        sage: is_generalized_cartan_matrix(M)
        True
    """
def find_cartan_type_from_matrix(CM):
    """
    Find a Cartan type by direct comparison of Dynkin diagrams given from
    the generalized Cartan matrix ``CM`` and return ``None`` if not found.

    INPUT:

    - ``CM`` -- a generalized Cartan matrix

    EXAMPLES::

        sage: # needs sage.graphs
        sage: from sage.combinat.root_system.cartan_matrix import find_cartan_type_from_matrix
        sage: CM = CartanMatrix([[2,-1,-1], [-1,2,-1], [-1,-1,2]])
        sage: find_cartan_type_from_matrix(CM)
        ['A', 2, 1]
        sage: CM = CartanMatrix([[2,-1,0], [-1,2,-2], [0,-1,2]])
        sage: find_cartan_type_from_matrix(CM)
        ['C', 3] relabelled by {1: 0, 2: 1, 3: 2}
        sage: CM = CartanMatrix([[2,-1,-2], [-1,2,-1], [-2,-1,2]])
        sage: find_cartan_type_from_matrix(CM)

    TESTS:

    Check that :issue:`35987` is fixed::

        sage: from sage.combinat.root_system.cartan_matrix import find_cartan_type_from_matrix
        sage: cm = CartanMatrix(['A',7]).subtype([2,3,5])
        sage: find_cartan_type_from_matrix(cm)
        A2xA1 relabelled by {1: 2, 2: 3, 3: 5}

        sage: cm = CartanMatrix(['B',10,1]).subtype([0,1,2,3,5,6,8,9,10])
        sage: ct = find_cartan_type_from_matrix(cm); ct
        D4xB3xA2 relabelled by {1: 0, 2: 2, 3: 1, 4: 3, 5: 8, 6: 9, 7: 10, 8: 5, 9: 6}
        sage: ct.dynkin_diagram()
            O 3
            |
            |
        O---O---O
        0   2   1
        O---O=>=O
        8   9   10
        O---O
        5   6
        D4xB3xA2 relabelled by {1: 0, 2: 2, 3: 1, 4: 3, 5: 8, 6: 9, 7: 10, 8: 5, 9: 6}
    """
