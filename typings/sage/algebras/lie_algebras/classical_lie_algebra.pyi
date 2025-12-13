from sage.algebras.lie_algebras.lie_algebra import FinitelyGeneratedLieAlgebra as FinitelyGeneratedLieAlgebra, MatrixLieAlgebraFromAssociative as MatrixLieAlgebraFromAssociative
from sage.algebras.lie_algebras.structure_coefficients import LieAlgebraWithStructureCoefficients as LieAlgebraWithStructureCoefficients
from sage.categories.lie_algebras import LieAlgebras as LieAlgebras
from sage.categories.triangular_kac_moody_algebras import TriangularKacMoodyAlgebras as TriangularKacMoodyAlgebras
from sage.combinat.root_system.cartan_matrix import CartanMatrix as CartanMatrix
from sage.combinat.root_system.cartan_type import CartanType as CartanType
from sage.combinat.root_system.dynkin_diagram import DynkinDiagram_class as DynkinDiagram_class
from sage.matrix.matrix_space import MatrixSpace as MatrixSpace
from sage.misc.abstract_method import abstract_method as abstract_method
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module import FreeModule as FreeModule
from sage.sets.family import Family as Family
from sage.structure.element import Element as Element
from sage.structure.indexed_generators import IndexedGenerators as IndexedGenerators
from sage.structure.richcmp import richcmp as richcmp

class ClassicalMatrixLieAlgebra(MatrixLieAlgebraFromAssociative):
    """
    A classical Lie algebra represented using matrices.

    This means a classical Lie algebra given as a Lie
    algebra of matrices, with commutator as Lie bracket.

    INPUT:

    - ``R`` -- the base ring
    - ``ct`` -- the finite Cartan type

    EXAMPLES::

        sage: lie_algebras.ClassicalMatrix(QQ, ['A', 4])
        Special linear Lie algebra of rank 5 over Rational Field
        sage: lie_algebras.ClassicalMatrix(QQ, CartanType(['B',4]))
        Special orthogonal Lie algebra of rank 9 over Rational Field
        sage: lie_algebras.ClassicalMatrix(QQ, 'C4')
        Symplectic Lie algebra of rank 8 over Rational Field
        sage: lie_algebras.ClassicalMatrix(QQ, cartan_type=['D',4])
        Special orthogonal Lie algebra of rank 8 over Rational Field
    """
    @staticmethod
    def __classcall_private__(cls, R, cartan_type):
        """
        Return the correct parent based on input.

        EXAMPLES::

            sage: lie_algebras.ClassicalMatrix(QQ, ['A', 4])
            Special linear Lie algebra of rank 5 over Rational Field
            sage: lie_algebras.ClassicalMatrix(QQ, CartanType(['B',4]))
            Special orthogonal Lie algebra of rank 9 over Rational Field
            sage: lie_algebras.ClassicalMatrix(QQ, 'C4')
            Symplectic Lie algebra of rank 8 over Rational Field
            sage: lie_algebras.ClassicalMatrix(QQ, cartan_type=['D',4])
            Special orthogonal Lie algebra of rank 8 over Rational Field
        """
    def __init__(self, R, ct, e, f, h, sparse: bool = True) -> None:
        """
        Initialize ``self``.

        INPUT:

        - ``R`` -- the base ring
        - ``ct`` -- the Cartan type
        - ``e`` -- the `e` generators
        - ``f`` -- the `f` generators
        - ``h`` -- the `h` generators
        - ``sparse`` -- boolean (default: ``True``); use the sparse vectors
          for the basis computation

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 3, representation='matrix')
            sage: TestSuite(g).run()

        TESTS:

        Check that :issue:`23266` is fixed::

            sage: sl2 = lie_algebras.sl(QQ, 2, 'matrix')
            sage: isinstance(sl2.indices(), FiniteEnumeratedSet)
            True

        Check that elements are hashable (see :issue:`28961`)::

            sage: sl2 = lie_algebras.sl(QQ, 2, 'matrix')
            sage: e,f,h = list(sl2.basis())
            sage: len(set([e, e+f]))
            2
        """
    def e(self, i):
        """
        Return the generator `e_i`.

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 3, representation='matrix')
            sage: g.e(2)
            [0 0 0]
            [0 0 1]
            [0 0 0]
        """
    def f(self, i):
        """
        Return the generator `f_i`.

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 3, representation='matrix')
            sage: g.f(2)
            [0 0 0]
            [0 0 0]
            [0 1 0]
        """
    def h(self, i):
        """
        Return the generator `h_i`.

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 3, representation='matrix')
            sage: g.h(2)
            [ 0  0  0]
            [ 0  1  0]
            [ 0  0 -1]
        """
    @cached_method
    def index_set(self):
        """
        Return the index_set of ``self``.

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 3, representation='matrix')
            sage: g.index_set()
            (1, 2)
        """
    def cartan_type(self):
        """
        Return the Cartan type of ``self``.

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 3, representation='matrix')
            sage: g.cartan_type()
            ['A', 2]
        """
    def epsilon(self, i, h):
        """
        Return the action of the functional
        `\\varepsilon_i \\colon \\mathfrak{h} \\to R`, where `R` is the base
        ring of ``self``, on the element ``h``.

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 3, representation='matrix')
            sage: g.epsilon(1, g.h(1))
            1
            sage: g.epsilon(2, g.h(1))
            -1
            sage: g.epsilon(3, g.h(1))
            0
        """
    def simple_root(self, i, h) -> None:
        """
        Return the action of the simple root
        `\\alpha_i \\colon \\mathfrak{h} \\to R`, where `R` is the base
        ring of ``self``, on the element ``h``.

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 3, representation='matrix')
            sage: g.simple_root(1, g.h(1))
            2
            sage: g.simple_root(1, g.h(2))
            -1
        """
    def highest_root_basis_elt(self, pos: bool = True):
        """
        Return the basis element corresponding to the highest root `\\theta`.
        If ``pos`` is ``True``, then returns `e_{\\theta}`, otherwise it
        returns `f_{\\theta}`.

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 3, representation='matrix')
            sage: g.highest_root_basis_elt()
            [0 0 1]
            [0 0 0]
            [0 0 0]
        """
    @cached_method
    def basis(self):
        """
        Return a basis of ``self``.

        EXAMPLES::

            sage: M = LieAlgebra(ZZ, cartan_type=['A',2], representation='matrix')
            sage: list(M.basis())
            [
            [ 1  0  0]  [0 1 0]  [0 0 1]  [0 0 0]  [ 0  0  0]  [0 0 0]  [0 0 0]
            [ 0  0  0]  [0 0 0]  [0 0 0]  [1 0 0]  [ 0  1  0]  [0 0 1]  [0 0 0]
            [ 0  0 -1], [0 0 0], [0 0 0], [0 0 0], [ 0  0 -1], [0 0 0], [1 0 0],
            <BLANKLINE>
            [0 0 0]
            [0 0 0]
            [0 1 0]
            ]

        Sparse version::

            sage: e6 = LieAlgebra(QQ, cartan_type=['E',6], representation='matrix')
            sage: len(e6.basis())  # long time
            78
        """
    def affine(self, kac_moody: bool = True):
        """
        Return the affine (Kac-Moody) Lie algebra of ``self``.

        EXAMPLES::

            sage: so5 = lie_algebras.so(QQ, 5, 'matrix')
            sage: so5
            Special orthogonal Lie algebra of rank 5 over Rational Field
            sage: so5.affine()
            Affine Special orthogonal Kac-Moody algebra of rank 5 over Rational Field
            sage: so5.affine(False)
            Affine Special orthogonal Lie algebra of rank 5 over Rational Field
        """

class gl(MatrixLieAlgebraFromAssociative):
    """
    The matrix Lie algebra `\\mathfrak{gl}_n`.

    The Lie algebra `\\mathfrak{gl}_n` which consists of all `n \\times n`
    matrices.

    INPUT:

    - ``R`` -- the base ring
    - ``n`` -- the size of the matrix
    """
    def __init__(self, R, n) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = lie_algebras.gl(QQ, 4)
            sage: TestSuite(g).run()

        TESTS:

        Check that :issue:`23266` is fixed::

            sage: gl2 = lie_algebras.gl(QQ, 2)
            sage: isinstance(gl2.basis().keys(), FiniteEnumeratedSet)
            True
            sage: Ugl2 = gl2.pbw_basis()
            sage: prod(Ugl2.gens())
            PBW['E_0_0']*PBW['E_0_1']*PBW['E_1_0']*PBW['E_1_1']
        """
    def killing_form(self, x, y):
        """
        Return the Killing form on ``x`` and ``y``.

        The Killing form on `\\mathfrak{gl}_n` is:

        .. MATH::

            \\langle x \\mid y \\rangle = 2n \\mathrm{tr}(xy) - 2 \\mathrm{tr}(x)
            \\mathrm{tr}(y).

        EXAMPLES::

            sage: g = lie_algebras.gl(QQ, 4)
            sage: x = g.an_element()
            sage: y = g.gens()[1]
            sage: g.killing_form(x, y)
            8
        """
    @cached_method
    def basis(self):
        """
        Return the basis of ``self``.

        EXAMPLES::

            sage: g = lie_algebras.gl(QQ, 2)
            sage: tuple(g.basis())
            (
            [1 0]  [0 1]  [0 0]  [0 0]
            [0 0], [0 0], [1 0], [0 1]
            )
        """
    def monomial(self, i):
        """
        Return the basis element indexed by ``i``.

        INPUT:

        - ``i`` -- an element of the index set

        EXAMPLES::

            sage: gl4 = lie_algebras.gl(QQ, 4)
            sage: gl4.monomial('E_2_1')
            [0 0 0 0]
            [0 0 0 0]
            [0 1 0 0]
            [0 0 0 0]
            sage: gl4.monomial((2,1))
            [0 0 0 0]
            [0 0 0 0]
            [0 1 0 0]
            [0 0 0 0]
        """
    class Element(MatrixLieAlgebraFromAssociative.Element):
        def monomial_coefficients(self, copy: bool = True):
            """
            Return the monomial coefficients of ``self``.

            EXAMPLES::

                sage: gl4 = lie_algebras.gl(QQ, 4)
                sage: x = gl4.monomial('E_2_1') + 3*gl4.monomial('E_0_3')
                sage: x.monomial_coefficients()
                {'E_0_3': 3, 'E_2_1': 1}
            """

class sl(ClassicalMatrixLieAlgebra):
    """
    The matrix Lie algebra `\\mathfrak{sl}_n`.

    The Lie algebra `\\mathfrak{sl}_n`, which consists of all `n \\times n`
    matrices with trace 0. This is the Lie algebra of type `A_{n-1}`.
    """
    def __init__(self, R, n) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 5, representation='matrix')
            sage: TestSuite(g).run()
        """
    def killing_form(self, x, y):
        """
        Return the Killing form on ``x`` and ``y``.

        The Killing form on `\\mathfrak{sl}_n` is:

        .. MATH::

            \\langle x \\mid y \\rangle = 2n \\mathrm{tr}(xy).

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 5, representation='matrix')
            sage: x = g.an_element()
            sage: y = g.lie_algebra_generators()['e1']
            sage: g.killing_form(x, y)
            10
        """
    def simple_root(self, i, h):
        """
        Return the action of the simple root
        `\\alpha_i \\colon \\mathfrak{h} \\to R`, where `R` is the base
        ring of ``self``, on the element ``j``.

        EXAMPLES::

            sage: g = lie_algebras.sl(QQ, 5, representation='matrix')
            sage: matrix([[g.simple_root(i, g.h(j)) for i in g.index_set()] for j in g.index_set()])
            [ 2 -1  0  0]
            [-1  2 -1  0]
            [ 0 -1  2 -1]
            [ 0  0 -1  2]
        """

class so(ClassicalMatrixLieAlgebra):
    """
    The matrix Lie algebra `\\mathfrak{so}_n`.

    The Lie algebra `\\mathfrak{so}_n`, which is isomorphic to the
    Lie algebra of all anti-symmetric `n \\times n` matrices.
    The implementation here uses a different bilinear form and follows
    the description in Chapter 8 of [HK2002]_. More precisely, this
    is the set of matrices:

    .. MATH::

        \\begin{pmatrix}
        A & B \\\\\n        C & D
        \\end{pmatrix}

    such that `A^t = -D`, `B^t = -B`, `C^t = -C` for `n` even and

    .. MATH::

        \\begin{pmatrix}
        A & B & a \\\\\n        C & D & b \\\\\n        c & d & 0
        \\end{pmatrix}

    such that `A^t = -D`, `B^t = -B`, `C^t = -C`, `a^t = -d`,
    and `b^t = -c` for `n` odd.

    This is the Lie algebra of type `B_{(n-1)/2}` or `D_{n/2}` if `n`
    is odd or even respectively.
    """
    def __init__(self, R, n) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = lie_algebras.so(QQ, 8, representation='matrix')
            sage: TestSuite(g).run()
            sage: g = lie_algebras.so(QQ, 9, representation='matrix')
            sage: TestSuite(g).run()
        """
    def killing_form(self, x, y):
        """
        Return the Killing form on ``x`` and ``y``.

        The Killing form on `\\mathfrak{so}_n` is:

        .. MATH::

            \\langle x \\mid y \\rangle = (n - 2) \\mathrm{tr}(xy).

        EXAMPLES::

            sage: g = lie_algebras.so(QQ, 8, representation='matrix')
            sage: x = g.an_element()
            sage: y = g.lie_algebra_generators()['e1']
            sage: g.killing_form(x, y)
            12
            sage: g = lie_algebras.so(QQ, 9, representation='matrix')
            sage: x = g.an_element()
            sage: y = g.lie_algebra_generators()['e1']
            sage: g.killing_form(x, y)
            14
        """
    def simple_root(self, i, h):
        """
        Return the action of the simple root
        `\\alpha_i \\colon \\mathfrak{h} \\to R`, where `R` is the base
        ring of ``self``, on the element ``j``.

        EXAMPLES:

        The even or type `D` case::

            sage: g = lie_algebras.so(QQ, 8, representation='matrix')
            sage: matrix([[g.simple_root(i, g.h(j)) for i in g.index_set()] for j in g.index_set()])
            [ 2 -1  0  0]
            [-1  2 -1 -1]
            [ 0 -1  2  0]
            [ 0 -1  0  2]

        The odd or type `B` case::

            sage: g = lie_algebras.so(QQ, 9, representation='matrix')
            sage: matrix([[g.simple_root(i, g.h(j)) for i in g.index_set()] for j in g.index_set()])
            [ 2 -1  0  0]
            [-1  2 -1  0]
            [ 0 -1  2 -1]
            [ 0  0 -2  2]
        """

class sp(ClassicalMatrixLieAlgebra):
    """
    The matrix Lie algebra `\\mathfrak{sp}_n`.

    The Lie algebra `\\mathfrak{sp}_{2k}`, which consists of all
    `2k \\times 2k` matrices `X` that satisfy the equation:

    .. MATH::

        X^T M - M X = 0

    where

    .. MATH::

        M = \\begin{pmatrix}
        0 & I_k \\\\\n        -I_k & 0
        \\end{pmatrix}.

    This is the Lie algebra of type `C_k`.
    """
    def __init__(self, R, n) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = lie_algebras.sp(QQ, 8, representation='matrix')
            sage: TestSuite(g).run()
        """
    def killing_form(self, x, y):
        """
        Return the Killing form on ``x`` and ``y``.

        The Killing form on `\\mathfrak{sp}_n` is:

        .. MATH::

            \\langle x \\mid y \\rangle = (2n + 2) \\mathrm{tr}(xy).

        EXAMPLES::

            sage: g = lie_algebras.sp(QQ, 8, representation='matrix')
            sage: x = g.an_element()
            sage: y = g.lie_algebra_generators()['e1']
            sage: g.killing_form(x, y)
            36
        """
    def simple_root(self, i, h):
        """
        Return the action of the simple root
        `\\alpha_i \\colon \\mathfrak{h} \\to R`, where `R` is the base
        ring of ``self``, on the element ``j``.

        EXAMPLES::

            sage: g = lie_algebras.sp(QQ, 8, representation='matrix')
            sage: matrix([[g.simple_root(i, g.h(j)) for i in g.index_set()] for j in g.index_set()])
            [ 2 -1  0  0]
            [-1  2 -1  0]
            [ 0 -1  2 -2]
            [ 0  0 -1  2]
        """

class ExceptionalMatrixLieAlgebra(ClassicalMatrixLieAlgebra):
    """
    A matrix Lie algebra of exceptional type.
    """
    def __init__(self, R, cartan_type, e, f, h=None, sparse: bool = False) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E',6], representation='matrix')
            sage: all(g.h(i) == g.e(i).bracket(g.f(i)) for i in range(1,7))
            True
        """

class e6(ExceptionalMatrixLieAlgebra):
    """
    The matrix Lie algebra `\\mathfrak{e}_6`.

    The simple Lie algebra `\\mathfrak{e}_6` of type `E_6`. The matrix
    representation is given following [HRT2000]_.
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E',6], representation='matrix')
            sage: TestSuite(g).run()  # long time
        """

class e7(ExceptionalMatrixLieAlgebra):
    """
    The matrix Lie algebra `\\mathfrak{e}_7`.

    The simple Lie algebra `\\mathfrak{e}_7` of type `E_7`. The matrix
    representation is given following [HRT2000]_.
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 7], representation='matrix')
            sage: g
            Simple matrix Lie algebra of type ['E', 7] over Rational Field

            sage: len(g.basis())  # long time
            133
            sage: TestSuite(g).run()  # long time
        """

class e8(ExceptionalMatrixLieAlgebra):
    """
    The matrix Lie algebra `\\mathfrak{e}_8`.

    The simple Lie algebra `\\mathfrak{e}_8` of type `E_8` built from the
    adjoint representation in the Chevalley basis.
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 8], representation='matrix')  # long time
            sage: g  # long time
            Simple matrix Lie algebra of type ['E', 8] over Rational Field

        We skip the not implemented methods test as it takes too much time::

            sage: TestSuite(g).run(skip='_test_not_implemented_methods')  # long time
        """
    @cached_method
    def basis(self):
        """
        Return a basis of ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['E', 8], representation='matrix')  # long time
            sage: len(g.basis())  # long time
            248
        """

class f4(ExceptionalMatrixLieAlgebra):
    """
    The matrix Lie algebra `\\mathfrak{f}_4`.

    The simple Lie algebra `\\mathfrak{f}_f` of type `F_4`. The matrix
    representation is given following [HRT2000]_ but indexed in the
    reversed order (i.e., interchange 1 with 4 and 2 with 3).
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['F',4], representation='matrix')
            sage: TestSuite(g).run()  # long time
        """

class g2(ExceptionalMatrixLieAlgebra):
    """
    The matrix Lie algebra `\\mathfrak{g}_2`.

    The simple Lie algebra `\\mathfrak{g}_2` of type `G_2`. The matrix
    representation is given following [HRT2000]_.
    """
    def __init__(self, R) -> None:
        """
        Initialize ``self``.

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['G',2], representation='matrix')
            sage: TestSuite(g).run()
        """

class MatrixCompactRealForm(FinitelyGeneratedLieAlgebra):
    '''
    The compact real form of a matrix Lie algebra.

    Let `L` be a classical (i.e., type `ABCD`) Lie algebra over `\\RR`
    given as matrices that is invariant under matrix transpose (i.e.,
    `X^T \\in L` for all `X \\in L`). Then we can perform the
    *Cartan decomposition* of `L` by `L = K \\oplus S`, where `K`
    (resp. `S`) is the set of skew-symmetric (resp. symmetric) matrices
    in `L`. Then the Lie algebra `U = K \\oplus i S` is an `\\RR`-subspace
    of the complexification of `L` that is closed under commutators and
    has skew-hermitian matrices. Hence, the Killing form is negative
    definitive (i.e., `U` is a compact Lie algebra), and thus `U` is
    the complex real form of the complexification of `L`.

    EXAMPLES::

        sage: U = LieAlgebra(QQ, cartan_type=[\'A\',1], representation="compact real")
        sage: list(U.basis())
        [
        [ 0  1]  [ i  0]  [0 i]
        [-1  0], [ 0 -i], [i 0]
        ]
        sage: U.killing_form_matrix()
        [-8  0  0]
        [ 0 -8  0]
        [ 0  0 -8]

    Computations are only (currently) possible if this is defined
    over a field::

        sage: U = LieAlgebra(ZZ, cartan_type=[\'A\',1], representation="compact real")
        sage: list(U.basis())
        Traceback (most recent call last):
        ...
        TypeError: no conversion of this rational to integer
    '''
    def __init__(self, R, cartan_type) -> None:
        '''
        Initialize ``self``.

        TESTS::

            sage: L = LieAlgebra(QQ, cartan_type=[\'A\',2], representation="compact real")
            sage: TestSuite(L).run()
        '''
    @cached_method
    def basis(self):
        '''
        Compute a basis of ``self``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=[\'B\',2], representation="compact real")
            sage: list(L.basis())
            [
            [ 0  1  0  0  0]  [ 0  0  0  1  0]  [ 0  0  0  0  1]  [ 0  0  0  0  0]
            [-1  0  0  0  0]  [ 0  0 -1  0  0]  [ 0  0  0  0  0]  [ 0  0  0  0  1]
            [ 0  0  0  1  0]  [ 0  1  0  0  0]  [ 0  0  0  0  1]  [ 0  0  0  0  0]
            [ 0  0 -1  0  0]  [-1  0  0  0  0]  [ 0  0  0  0  0]  [ 0  0  0  0  1]
            [ 0  0  0  0  0], [ 0  0  0  0  0], [-1  0 -1  0  0], [ 0 -1  0 -1  0],
            <BLANKLINE>
            [ i  0  0  0  0]  [ 0  i  0  0  0]  [ 0  0  0  i  0]  [ 0  0  0  0  i]
            [ 0  0  0  0  0]  [ i  0  0  0  0]  [ 0  0 -i  0  0]  [ 0  0  0  0  0]
            [ 0  0 -i  0  0]  [ 0  0  0 -i  0]  [ 0 -i  0  0  0]  [ 0  0  0  0 -i]
            [ 0  0  0  0  0]  [ 0  0 -i  0  0]  [ i  0  0  0  0]  [ 0  0  0  0  0]
            [ 0  0  0  0  0], [ 0  0  0  0  0], [ 0  0  0  0  0], [ i  0 -i  0  0],
            <BLANKLINE>
            [ 0  0  0  0  0]  [ 0  0  0  0  0]
            [ 0  i  0  0  0]  [ 0  0  0  0  i]
            [ 0  0  0  0  0]  [ 0  0  0  0  0]
            [ 0  0  0 -i  0]  [ 0  0  0  0 -i]
            [ 0  0  0  0  0], [ 0  i  0 -i  0]
            ]
        '''
    @cached_method
    def zero(self):
        '''
        Return the element `0`.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=[\'D\',4], representation="compact real")
            sage: L.zero()
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
            [0 0 0 0 0 0 0 0]
        '''
    def monomial(self, i):
        '''
        Return the monomial indexed by ``i``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=[\'A\',3], representation="compact real")
            sage: L.monomial(0)
            [ 0  1  0  0]
            [-1  0  0  0]
            [ 0  0  0  0]
            [ 0  0  0  0]
        '''
    def term(self, i, c=None):
        '''
        Return the term indexed by ``i`` with coefficient ``c``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=[\'C\',3], representation="compact real")
            sage: L.term(4, 7/2)
            [   0    0    0    0    0  7/2]
            [   0    0    0    0    0    0]
            [   0    0    0  7/2    0    0]
            [   0    0 -7/2    0    0    0]
            [   0    0    0    0    0    0]
            [-7/2    0    0    0    0    0]
        '''
    class Element(Element):
        """
        An element of a matrix Lie algebra in its compact real form.
        """
        def __init__(self, parent, real, imag) -> None:
            '''
            Initialize ``self``.

            EXAMPLES::

                sage: L = LieAlgebra(QQ, cartan_type=[\'D\',4], representation="compact real")
                sage: TestSuite(L.an_element()).run()
            '''
        def __bool__(self) -> bool:
            '''
            Return if ``self`` is nonzero.

            EXAMPLES::

                sage: L = LieAlgebra(QQ, cartan_type=[\'C\',3], representation="compact real")
                sage: all(b for b in L.basis() if b != 0)
                True
                sage: bool(L.zero())
                False
            '''
        def __hash__(self):
            '''
            Return the hash of ``self``.

            EXAMPLES::

                sage: L = LieAlgebra(QQ, cartan_type=[\'A\',2], representation="compact real")
                sage: x = L.an_element()
                sage: hash(x) == hash((x._real, x._imag))
                True
            '''
        def monomial_coefficients(self, copy: bool = False):
            '''
            Return the monomial coefficients of ``self``.

            EXAMPLES::

                sage: L = LieAlgebra(QQ, cartan_type=[\'C\',3], representation="compact real")
                sage: B = L.basis()
                sage: x = L.sum(i*B[i] for i in range(len(B)))
                sage: x.monomial_coefficients() == {i: i for i in range(1,len(B))}
                True
            '''

class LieAlgebraChevalleyBasis(LieAlgebraWithStructureCoefficients):
    """
    A simple finite dimensional Lie algebra in the Chevalley basis.

    Let `L` be a simple (complex) Lie algebra with roots `\\Phi`, then the
    Chevalley basis is given by `e_{\\alpha}` for all `\\alpha \\in \\Phi` and
    `h_{\\alpha_i} := h_i` where `\\alpha_i` is a simple root subject. These
    generators are subject to the relations:

    .. MATH::

        \\begin{aligned}
        [h_i, h_j] & = 0,
        \\\\ [h_i, e_{\\beta}] & = A_{\\alpha_i, \\beta} e_{\\beta},
        \\\\ [e_{\\beta}, e_{-\\beta}] & = \\sum_i A_{\\beta, \\alpha_i} h_i,
        \\\\ [e_{\\beta}, e_{\\gamma}] & = \\begin{cases}
        N_{\\beta,\\gamma} e_{\\beta + \\gamma} & \\beta + \\gamma \\in \\Phi, \\\\\n        0 & \\text{otherwise,} \\end{cases}
        \\end{aligned}

    where `A_{\\alpha, \\beta} = \\frac{2 (\\alpha, \\beta)}{(\\alpha, \\alpha)}`
    and `N_{\\alpha, \\beta}` is the maximum such that
    `\\alpha - N_{\\alpha, \\beta} \\beta \\in \\Phi`.

    For computing the signs of the coefficients, see Section 3 of [CMT2003]_.

    .. SEEALSO::

        For simply-laced types, an alternative construction using an asymmetry
        function is given by :class:`LieAlgebraChevalleyBasis_simply_laced`.
    """
    @staticmethod
    def __classcall_private__(cls, R, cartan_type, epsilon=None):
        """
        Normalize ``self`` to ensure a unique representation.

        TESTS::

            sage: L1 = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: L2 = LieAlgebra(QQ, cartan_type=CartanType(['A', 2]))
            sage: L3 = LieAlgebra(QQ, cartan_type=CartanMatrix(['A', 2]))
            sage: L1 is L2 and L2 is L3
            True


            sage: L = LieAlgebra(QQ, cartan_type=['A', 2], epsilon=[(1,2)])
            sage: type(L)
            <class '...LieAlgebraChevalleyBasis_simply_laced_with_category'>
            sage: L = LieAlgebra(QQ, cartan_type=['A', 1], epsilon=[])
            sage: type(L)
            <class '...LieAlgebraChevalleyBasis_simply_laced_with_category'>

            sage: L = LieAlgebra(QQ, cartan_type=['A', 2], epsilon=[(2,3)])
            Traceback (most recent call last):
            ...
            ValueError: not a valid Dynkin orientation
            sage: L = LieAlgebra(QQ, cartan_type=['A', 2], epsilon=[(1,2), (2,1)])
            Traceback (most recent call last):
            ...
            ValueError: not a valid Dynkin orientation
            sage: L = LieAlgebra(QQ, cartan_type=['A', 2], epsilon=[(1,2), (1,1)])
            Traceback (most recent call last):
            ...
            ValueError: not a valid Dynkin orientation
            sage: L = LieAlgebra(QQ, cartan_type=['A', 1], epsilon=[(1,1)])
            Traceback (most recent call last):
            ...
            ValueError: not a valid Dynkin orientation
        """
    def __init__(self, R, cartan_type) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: L = LieAlgebra(QQ, cartan_type=['A',2])
            sage: TestSuite(L).run()  # long time
        """
    def degree_on_basis(self, m):
        """
        Return the degree of the basis element indexed by ``m``.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=['G', 2])
            sage: [L.degree_on_basis(m) for m in L.basis().keys()]
            [alpha[2], alpha[1], alpha[1] + alpha[2],
             2*alpha[1] + alpha[2], 3*alpha[1] + alpha[2],
             3*alpha[1] + 2*alpha[2],
             0, 0,
             -alpha[2], -alpha[1], -alpha[1] - alpha[2],
             -2*alpha[1] - alpha[2], -3*alpha[1] - alpha[2],
             -3*alpha[1] - 2*alpha[2]]
        """
    def affine(self, kac_moody: bool = True):
        """
        Return the affine Lie algebra of ``self``.

        EXAMPLES::

            sage: sp6 = lie_algebras.sp(QQ, 6)
            sage: sp6
            Lie algebra of ['C', 3] in the Chevalley basis
            sage: sp6.affine()
            Affine Kac-Moody algebra of ['C', 3] in the Chevalley basis

            sage: L = LieAlgebra(QQ, cartan_type=['A',3], epsilon=[(1,2),(3,2)])
            sage: L.affine(False)
            Affine Lie algebra of ['A', 3] in the Chevalley basis
            sage: L.affine(True)
            Affine Kac-Moody algebra of ['A', 3] in the Chevalley basis
        """
    @cached_method
    def indices_to_positive_roots_map(self):
        """
        Return the map from indices to positive roots.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: L.indices_to_positive_roots_map()
            {1: alpha[1], 2: alpha[2], 3: alpha[1] + alpha[2]}
        """
    @cached_method
    def lie_algebra_generators(self, str_keys: bool = False):
        """
        Return the Chevalley Lie algebra generators of ``self``.

        INPUT:

        - ``str_keys`` -- boolean (default: ``False``); set to ``True`` to have
          the indices indexed by strings instead of simple (co)roots

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=['A', 1])
            sage: L.lie_algebra_generators()
            Finite family {alpha[1]: E[alpha[1]], -alpha[1]: E[-alpha[1]], alphacheck[1]: h1}
            sage: L.lie_algebra_generators(True)
            Finite family {'e1': E[alpha[1]], 'f1': E[-alpha[1]], 'h1': h1}
        """
    @cached_method
    def gens(self) -> tuple:
        """
        Return the generators of ``self`` in the order of `e_i`, `f_i`,
        and `h_i`.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: L.gens()
            (E[alpha[1]], E[alpha[2]], E[-alpha[1]], E[-alpha[2]], h1, h2)
        """
    def highest_root_basis_elt(self, pos: bool = True):
        """
        Return the basis element corresponding to the highest root `\\theta`.

        INPUT:

        - ``pos`` -- boolean (default: ``True``); if ``True``, then return
          `e_{\\theta}`, otherwise return `f_{\\theta}`

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: L.highest_root_basis_elt()
            E[alpha[1] + alpha[2]]
            sage: L.highest_root_basis_elt(False)
            E[-alpha[1] - alpha[2]]
        """
    @cached_method
    def killing_form_matrix(self):
        """
        Return the matrix of the Killing form of ``self``.

        The rows and the columns of this matrix are indexed by the
        elements of the basis of ``self`` (in the order provided by
        :meth:`basis`).

        EXAMPLES::

            sage: g = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: g.killing_form_matrix()
            [ 0  0  0  0  0  6  0  0]
            [ 0  0  0  0  0  0  6  0]
            [ 0  0  0  0  0  0  0  6]
            [ 0  0  0 12 -6  0  0  0]
            [ 0  0  0 -6 12  0  0  0]
            [ 6  0  0  0  0  0  0  0]
            [ 0  6  0  0  0  0  0  0]
            [ 0  0  6  0  0  0  0  0]
        """
    def killing_form(self, x, y):
        """
        Return the Killing form on ``x`` and ``y``, where ``x``
        and ``y`` are two elements of ``self``.

        The Killing form is defined as

        .. MATH::

            \\langle x \\mid y \\rangle
            = \\operatorname{tr}\\left( \\operatorname{ad}_x
            \\circ \\operatorname{ad}_y \\right).

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=['A', 2])
            sage: L.killing_form(L.an_element(), L.an_element())
            36
            sage: B = L.basis()
            sage: matrix([[L.killing_form(a, b) for a in B] for b in B])
            [ 0  0  0  0  0  6  0  0]
            [ 0  0  0  0  0  0  6  0]
            [ 0  0  0  0  0  0  0  6]
            [ 0  0  0 12 -6  0  0  0]
            [ 0  0  0 -6 12  0  0  0]
            [ 6  0  0  0  0  0  0  0]
            [ 0  6  0  0  0  0  0  0]
            [ 0  0  6  0  0  0  0  0]
        """

class LieAlgebraChevalleyBasis_simply_laced(LieAlgebraChevalleyBasis):
    """
    A finite dimensional simply-laced Lie algebra in the Chevalley basis
    with structure coefficients given by an orientation of the Dynkin
    diagram.

    We follow Chapter 7.7 of [Ka1990]_, where the structure coefficients
    are given by an :meth:`asymmetry function <asymmetry_function>` defined by
    `\\varepsilon(\\alpha_i, \\alpha_j) = -1` if there is an arrow `i \\to j` in
    the Dynkin quiver (an orientation of the Dynkin diagram). However we twist
    `E_{\\alpha}` by `\\mathrm{sign}(\\alpha)` so that `F_i = E_{-\\alpha_i}`
    rather than its negative.

    EXAMPLES::

        sage: L = LieAlgebra(QQ, cartan_type=['A', 2], epsilon=[(2, 1)])
        sage: L.e(1).bracket(L.e(2))
        E[alpha[1] + alpha[2]]

        sage: L = LieAlgebra(QQ, cartan_type=['A', 2], epsilon=[(1, 2)])
        sage: L.e(1).bracket(L.e(2))
        -E[alpha[1] + alpha[2]]
    """
    def __init__(self, R, cartan_type, epsilon) -> None:
        """
        Initialize ``self``.

        TESTS::

            sage: L = LieAlgebra(QQ, cartan_type=['A', 2], epsilon=[(2,1)])
            sage: TestSuite(L).run(elements=list(L.basis()))
            sage: L = LieAlgebra(QQ, cartan_type=['D', 4], epsilon=[(2,1), (3,2), (4,2)])
            sage: TestSuite(L).run(elements=list(L.basis()))  # long time
        """
    def asymmetry_function(self):
        """
        Return the asymmetry function of ``self``.

        An *asymmetry function* is a function `\\varepsilon : Q \\times Q
        \\to \\{1, -1\\}` that satisfies the following properties:

        1. `\\varepsilon(\\alpha, \\alpha) = (-1)^{(\\alpha|\\alpha)/2}`
        2. bimultiplicativity `\\varepsilon(alpha + \\alpha', \\beta) =
           \\varepsilon(\\alpha, \\beta) \\varepsilon(\\alpha', \\beta)` and
           `\\varepsilon(alpha, \\beta + \\beta') =
           \\varepsilon(\\alpha, \\beta) \\varepsilon(\\alpha', \\beta)`,

        where `(\\alpha | \\beta)` is the symmetric bilinear form on `Q` given
        by the Cartan matrix. Some consequences of these properties are that
        `\\varepsilon(\\alpha, 0) = \\varepsilon(0, \\beta) = 1` and
        `varepsilon(\\alpha, \\beta) \\varepsilon(\\beta, \\alpha) =
        (-1)^{(\\alpha|\\beta)}`.

        OUTPUT:

        The asymmetry function as a ``dict`` consisting of pairs of all of
        the roots of `Q` and `0`.

        EXAMPLES::

            sage: L = LieAlgebra(QQ, cartan_type=['A',2], epsilon=[(2,1)])
            sage: ep = L.asymmetry_function()
            sage: al = L.cartan_type().root_system().root_lattice().simple_roots()
            sage: ep[al[1], al[2]]
            1
            sage: ep[al[2],al[1]]
            -1

            sage: L = LieAlgebra(QQ, cartan_type=['A',2], epsilon=[(1,2)])
            sage: ep = L.asymmetry_function()
            sage: al = L.cartan_type().root_system().root_lattice().simple_roots()
            sage: ep[al[1], al[2]]
            -1
            sage: ep[al[2],al[1]]
            1
        """
