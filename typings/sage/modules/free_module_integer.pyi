from sage.matrix.constructor import matrix as matrix
from sage.misc.cachefunc import cached_method as cached_method
from sage.modules.free_module import FreeModule_ambient_pid as FreeModule_ambient_pid, FreeModule_submodule_with_basis_pid as FreeModule_submodule_with_basis_pid
from sage.modules.free_module_element import vector as vector
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.number_field.number_field_element import OrderElement_absolute as OrderElement_absolute
from sage.rings.rational_field import QQ as QQ

def IntegerLattice(basis, lll_reduce: bool = True):
    '''
    Construct a new integer lattice from ``basis``.

    INPUT:

    - ``basis`` -- can be one of the following:

      - a list of vectors

      - a matrix over the integers

      - an element of an absolute order

    - ``lll_reduce`` -- boolean (default: ``True``); run LLL reduction on the basis
      on construction

    EXAMPLES:

    We construct a lattice from a list of rows::

        sage: from sage.modules.free_module_integer import IntegerLattice
        sage: IntegerLattice([[1,0,3], [0,2,1], [0,2,7]])
        Free module of degree 3 and rank 3 over Integer Ring
        User basis matrix:
        [-2  0  0]
        [ 0  2  1]
        [ 1 -2  2]

    Sage includes a generator for hard lattices from cryptography::

        sage: from sage.modules.free_module_integer import IntegerLattice
        sage: A = sage.crypto.gen_lattice(type=\'modular\', m=10, seed=1337, dual=True)
        sage: IntegerLattice(A)
        Free module of degree 10 and rank 10 over Integer Ring
        User basis matrix:
        [-1  1  2 -2  0  1  0 -1  2  1]
        [ 1  0  0 -1 -2  1 -2  3 -1  0]
        [ 1  2  0  2 -1  1 -2  2  2  0]
        [ 1  0 -1  0  2  3  0  0 -1 -2]
        [ 1 -3  0  0  2  1 -2 -1  0  0]
        [-3  0 -1  0 -1  2 -2  0  0  2]
        [ 0  0  0  1  0  2 -3 -3 -2 -1]
        [ 0 -1 -4 -1 -1  1  2 -1  0  1]
        [ 1  1 -2  1  1  2  1  1 -2  3]
        [ 2 -1  1  2 -3  2  2  1  0  1]

    You can also construct the lattice directly::

        sage: from sage.modules.free_module_integer import IntegerLattice
        sage: sage.crypto.gen_lattice(type=\'modular\', m=10, seed=1337, dual=True, lattice=True)
        Free module of degree 10 and rank 10 over Integer Ring
        User basis matrix:
        [-1  1  2 -2  0  1  0 -1  2  1]
        [ 1  0  0 -1 -2  1 -2  3 -1  0]
        [ 1  2  0  2 -1  1 -2  2  2  0]
        [ 1  0 -1  0  2  3  0  0 -1 -2]
        [ 1 -3  0  0  2  1 -2 -1  0  0]
        [-3  0 -1  0 -1  2 -2  0  0  2]
        [ 0  0  0  1  0  2 -3 -3 -2 -1]
        [ 0 -1 -4 -1 -1  1  2 -1  0  1]
        [ 1  1 -2  1  1  2  1  1 -2  3]
        [ 2 -1  1  2 -3  2  2  1  0  1]

    We construct an ideal lattice from an element of an absolute order::

        sage: # needs sage.rings.number_field
        sage: K.<a>  = CyclotomicField(17)
        sage: O = K.ring_of_integers()
        sage: f = O(-a^15 + a^13 + 4*a^12 - 12*a^11 - 256*a^10 + a^9 - a^7
        ....:       - 4*a^6 + a^5 + 210*a^4 + 2*a^3 - 2*a^2 + 2*a - 2)
        sage: from sage.modules.free_module_integer import IntegerLattice
        sage: IntegerLattice(f)
        Free module of degree 16 and rank 16 over Integer Ring
        User basis matrix:
        [  -2    2   -2    2  210    1   -4   -1    0    1 -256  -12    4    1    0   -1]
        [  33   48   44   48  256 -209   28   51   45   49   -1   35   44   48   44   48]
        [   1   -1    3   -1    3  211    2   -3    0    1    2 -255  -11    5    2    1]
        [-223   34   50   47  258    0   29   45   46   47    2  -11   33   48   44   48]
        [ -13   31   46   42   46   -2 -225   32   48   45  256   -2   27   43   44   45]
        [ -16   33   42   46  254    1  -19   32   44   45    0  -13 -225   32   48   45]
        [ -15 -223   30   50  255    1  -20   32   42   47   -2  -11  -15   33   44   44]
        [ -11  -11   33   48  256    3  -17 -222   32   53    1   -9  -14   35   44   48]
        [ -12  -13   32   45  257    0  -16  -13   32   48   -1  -10  -14 -222   31   51]
        [  -9  -13 -221   32   52    1  -11  -12   33   46  258    1  -15  -12   33   49]
        [  -5   -2   -1    0 -257  -13    3    0   -1   -2   -1   -3    1   -3    1  209]
        [ -15  -11  -15   33  256   -1  -17  -14 -225   33    4  -12  -13  -14   31   44]
        [  11   11   11   11 -245   -3   17   10   13  220   12    5   12    9   14  -35]
        [ -18  -15  -20   29  250   -3  -23  -16  -19   30   -4  -17  -17  -17 -229   28]
        [ -15  -11  -15 -223  242    5  -18  -12  -16   34   -2  -11  -15  -11  -15   33]
        [ 378  120   92  147  152  462  136   96   99  144  -52  412  133   91 -107  138]

    We construct `\\ZZ^n`::

        sage: from sage.modules.free_module_integer import IntegerLattice
        sage: IntegerLattice(ZZ^10)
        Free module of degree 10 and rank 10 over Integer Ring
        User basis matrix:
        [1 0 0 0 0 0 0 0 0 0]
        [0 1 0 0 0 0 0 0 0 0]
        [0 0 1 0 0 0 0 0 0 0]
        [0 0 0 1 0 0 0 0 0 0]
        [0 0 0 0 1 0 0 0 0 0]
        [0 0 0 0 0 1 0 0 0 0]
        [0 0 0 0 0 0 1 0 0 0]
        [0 0 0 0 0 0 0 1 0 0]
        [0 0 0 0 0 0 0 0 1 0]
        [0 0 0 0 0 0 0 0 0 1]


    Sage also interfaces with fpylll\'s lattice generator::

        sage: # needs fpylll
        sage: from sage.modules.free_module_integer import IntegerLattice
        sage: from fpylll import IntegerMatrix
        sage: A = IntegerMatrix.random(8, "simdioph", bits=20, bits2=10)
        sage: A = A.to_matrix(matrix(ZZ, 8, 8))
        sage: IntegerLattice(A, lll_reduce=False)
        Free module of degree 8 and rank 8 over Integer Ring
        User basis matrix:
        [   1024  829556  161099   11567  521155  769480  639201  689979]
        [      0 1048576       0       0       0       0       0       0]
        [      0       0 1048576       0       0       0       0       0]
        [      0       0       0 1048576       0       0       0       0]
        [      0       0       0       0 1048576       0       0       0]
        [      0       0       0       0       0 1048576       0       0]
        [      0       0       0       0       0       0 1048576       0]
        [      0       0       0       0       0       0       0 1048576]
    '''

class FreeModule_submodule_with_basis_integer(FreeModule_submodule_with_basis_pid):
    """
    This class represents submodules of `\\ZZ^n` with a distinguished basis.

    However, most functionality in excess of standard submodules over PID
    is for these submodules considered as discrete subgroups of `\\ZZ^n`, i.e.
    as lattices. That is, this class provides functions for computing LLL
    and BKZ reduced bases for this free module with respect to the standard
    Euclidean norm.

    EXAMPLES::

        sage: from sage.modules.free_module_integer import IntegerLattice
        sage: L = IntegerLattice(sage.crypto.gen_lattice(type='modular', m=10,
        ....:                                            seed=1337, dual=True)); L
        Free module of degree 10 and rank 10 over Integer Ring
        User basis matrix:
        [-1  1  2 -2  0  1  0 -1  2  1]
        [ 1  0  0 -1 -2  1 -2  3 -1  0]
        [ 1  2  0  2 -1  1 -2  2  2  0]
        [ 1  0 -1  0  2  3  0  0 -1 -2]
        [ 1 -3  0  0  2  1 -2 -1  0  0]
        [-3  0 -1  0 -1  2 -2  0  0  2]
        [ 0  0  0  1  0  2 -3 -3 -2 -1]
        [ 0 -1 -4 -1 -1  1  2 -1  0  1]
        [ 1  1 -2  1  1  2  1  1 -2  3]
        [ 2 -1  1  2 -3  2  2  1  0  1]
        sage: L.shortest_vector()
        (-1, 1, 2, -2, 0, 1, 0, -1, 2, 1)
    """
    def __init__(self, ambient, basis, check: bool = True, echelonize: bool = False, echelonized_basis=None, already_echelonized: bool = False, lll_reduce: bool = True) -> None:
        """
        Construct a new submodule of `\\ZZ^n` with a distinguished basis.

        INPUT:

        - ``ambient`` -- ambient free module over a principal ideal domain
          `\\ZZ`, i.e. `\\ZZ^n`

        - ``basis`` -- either a list of vectors or a matrix over the integers

        - ``check`` -- boolean (default: ``True``); if ``False``, correctness
          of the input will not be checked and type conversion may be omitted,
          use with care

        - ``echelonize`` -- (default: ``False``) if ``True``, ``basis`` will be
          echelonized and the result will be used as the default basis of the
          constructed submodule

        - ``echelonized_basis`` -- (default: ``None``) if not ``None``, must
          be the echelonized basis spanning the same submodule as ``basis``

        - ``already_echelonized`` -- boolean (default: ``False``); if ``True``,
          ``basis`` must be already given in the echelonized form

        - ``lll_reduce`` -- boolean (default: ``True``); run LLL reduction on the basis
          on construction

        EXAMPLES::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: IntegerLattice([[1,0,-2], [0,2,5], [0,0,7]])
            Free module of degree 3 and rank 3 over Integer Ring
            User basis matrix:
            [ 1  0 -2]
            [ 1 -2  0]
            [ 2  2  1]

            sage: M = random_matrix(ZZ, 5, 5, x=-2^20, y=2^20)
            sage: L = IntegerLattice(M)
            sage: M.row_space() == L.matrix().row_space()
            True

            sage: # needs sage.rings.number_field
            sage: x = polygen(ZZ, 'x')
            sage: K.<a> = NumberField(x^8 + 1)
            sage: O = K.ring_of_integers()
            sage: f = O(a^7 - a^6 + 4*a^5 - a^4 + a^3 + 1)
            sage: IntegerLattice(f)
            Free module of degree 8 and rank 8 over Integer Ring
            User basis matrix:
            [ 0  1  0  1  0  3  3  0]
            [ 1  0  0  1 -1  4 -1  1]
            [ 0  0  1  0  1  0  3  3]
            [-4  1 -1  1  0  0  1 -1]
            [ 1 -3  0  0  0  3  0 -2]
            [ 0 -1  1 -4  1 -1  1  0]
            [ 2  0 -3 -1  0 -3  0  0]
            [-1  0 -1  0 -3 -3  0  0]
        """
    @property
    def reduced_basis(self):
        '''
        This attribute caches the currently best known reduced basis for
        ``self``, where "best" is defined by the Euclidean norm of the
        first row vector.

        EXAMPLES::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: M = random_matrix(ZZ, 10, 10)
            sage: while M.rank() < 10:
            ....:     M = random_matrix(ZZ, 10, 10)
            sage: L = IntegerLattice(M, lll_reduce=False)
            sage: L.reduced_basis == M
            True

            sage: LLL = L.LLL()
            sage: LLL == L.reduced_basis or bool(LLL[0].norm() >= M[0].norm())
            True
        '''
    def LLL(self, *args, **kwds):
        """
        Return an LLL reduced basis for ``self``.

        A lattice basis `(b_1, b_2, ..., b_d)` is `(\\delta, \\eta)`-LLL-reduced
        if the two following conditions hold:

        -  For any `i > j`, we have `\\lvert \\mu_{i, j} \\rvert \\leq \\eta`.

        -  For any `i < d`, we have
           `\\delta \\lvert b_i^* \\rvert^2 \\leq \\lvert b_{i+1}^* +
           \\mu_{i+1, i} b_i^* \\rvert^2`,

        where `\\mu_{i,j} = \\langle b_i, b_j^* \\rangle / \\langle b_j^*,b_j^*
        \\rangle` and `b_i^*` is the `i`-th vector of the Gram-Schmidt
        orthogonalisation of `(b_1, b_2, \\ldots, b_d)`.

        The default reduction parameters are `\\delta = 0.99` and
        `\\eta = 0.501`.

        The parameters `\\delta` and `\\eta` must satisfy:
        `0.25 < \\delta \\leq 1.0` and `0.5 \\leq \\eta < \\sqrt{\\delta}`.
        Polynomial time complexity is only guaranteed for `\\delta < 1`.
        Not every algorithm admits the case `\\delta = 1`.

        INPUT:

        - ``*args`` -- passed through to
          :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL`

        - ``**kwds`` -- passed through to
          :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.LLL`

        OUTPUT: integer matrix which is an LLL-reduced basis for this lattice

        EXAMPLES::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: A = random_matrix(ZZ, 10, 10, x=-2000, y=2000)
            sage: while A.rank() < 10:
            ....:     A = random_matrix(ZZ, 10, 10)
            sage: L = IntegerLattice(A, lll_reduce=False); L
            Free module of degree 10 and rank 10 over Integer Ring
            User basis matrix:
            ...
            sage: L.reduced_basis == A
            True
            sage: old = L.reduced_basis[0].norm().n()                                   # needs sage.symbolic
            sage: _ = L.LLL()
            sage: new = L.reduced_basis[0].norm().n()                                   # needs sage.symbolic
            sage: new <= old                                                            # needs sage.symbolic
            True
        """
    def BKZ(self, *args, **kwds):
        """
        Return a Block Korkine-Zolotareff reduced basis for ``self``.

        INPUT:

        - ``*args`` -- passed through to
          :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.BKZ`

        - ``*kwds`` -- passed through to
          :meth:`sage.matrix.matrix_integer_dense.Matrix_integer_dense.BKZ`

        OUTPUT: integer matrix which is a BKZ-reduced basis for this lattice

        EXAMPLES::

            sage: # needs sage.libs.linbox (o/w timeout)
            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: A = sage.crypto.gen_lattice(type='random', n=1, m=60, q=2^60, seed=42)
            sage: L = IntegerLattice(A, lll_reduce=False)
            sage: min(v.norm().n() for v in L.reduced_basis)
            4.17330740711759e15
            sage: L.LLL()
            60 x 60 dense matrix over Integer Ring (use the '.str()' method to see the entries)
            sage: min(v.norm().n() for v in L.reduced_basis)
            5.19615242270663
            sage: L.BKZ(block_size=10)
            60 x 60 dense matrix over Integer Ring (use the '.str()' method to see the entries)
            sage: min(v.norm().n() for v in L.reduced_basis)
            4.12310562561766

        .. NOTE::

            If ``block_size == L.rank()`` where ``L`` is this lattice, then
            this function performs Hermite-Korkine-Zolotareff (HKZ) reduction.
        """
    def HKZ(self, *args, **kwds):
        """
        Hermite-Korkine-Zolotarev (HKZ) reduce the basis.

        A basis `B` of a lattice `L`, with orthogonalized basis `B^*` such
        that `B = M \\cdot B^*` is HKZ reduced, if and only if, the following
        properties are satisfied:

        #. The basis `B` is size-reduced, i.e., all off-diagonal
           coefficients of `M` satisfy `|\\mu_{i,j}| \\leq 1/2`

        #. The vector `b_1` realizes the first minimum `\\lambda_1(L)`.

        #. The projection of the vectors `b_2, \\ldots,b_r` orthogonally to
           `b_1` form an HKZ reduced basis.

        .. NOTE::

            This is realized by calling
            :func:`sage.modules.free_module_integer.FreeModule_submodule_with_basis_integer.BKZ` with
            ``block_size == self.rank()``.

        INPUT:

        - ``*args`` -- passed through to :meth:`BKZ`

        - ``*kwds`` -- passed through to :meth:`BKZ`

        OUTPUT: integer matrix which is a HKZ-reduced basis for this lattice

        EXAMPLES::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: L = sage.crypto.gen_lattice(type='random', n=1, m=40, q=2^60, seed=1337, lattice=True)
            sage: L.HKZ()
            40 x 40 dense matrix over Integer Ring (use the '.str()' method to see the entries)

            sage: L.reduced_basis[0]
            (0, 0, -1, -1, 0, 0, -1, 1, 0, 0, -1, 1, 1, 0, 0, 1, 1, 1, -1, 0, 0, 1, -1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, 0, 1, 1, 0, 0, -2)
        """
    @cached_method
    def volume(self):
        """
        Return `vol(L)` which is `\\sqrt{\\det(B \\cdot B^T)}` for any basis `B`.

        OUTPUT: integer

        EXAMPLES::

            sage: L = sage.crypto.gen_lattice(m=10, seed=1337, lattice=True)
            sage: L.volume()
            14641
        """
    @cached_method
    def discriminant(self):
        """
        Return `|\\det(G)|`, i.e. the absolute value of the determinant of the
        Gram matrix `B \\cdot B^T` for any basis `B`.

        OUTPUT: integer

        EXAMPLES::

            sage: L = sage.crypto.gen_lattice(m=10, seed=1337, lattice=True)
            sage: L.discriminant()
            214358881
        """
    @cached_method
    def is_unimodular(self) -> bool:
        """
        Return ``True`` if this lattice is unimodular.

        OUTPUT: boolean

        EXAMPLES::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: L = IntegerLattice([[1, 0], [0, 1]])
            sage: L.is_unimodular()
            True
            sage: IntegerLattice([[2, 0], [0, 3]]).is_unimodular()
            False
        """
    @cached_method
    def shortest_vector(self, update_reduced_basis: bool = True, algorithm: str = 'fplll', *args, **kwds):
        """
        Return a shortest vector.

        INPUT:

        - ``update_reduced_basis`` -- boolean (default: ``True``); set this
          flag if the found vector should be used to improve the basis

        - ``algorithm`` -- (default: ``'fplll'``) either ``'fplll'`` or
          ``'pari'``

        - ``*args`` -- passed through to underlying implementation

        - ``**kwds`` -- passed through to underlying implementation

        OUTPUT: a shortest nonzero vector for this lattice

        EXAMPLES::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: A = sage.crypto.gen_lattice(type='random', n=1, m=30, q=2^40, seed=42)
            sage: L = IntegerLattice(A, lll_reduce=False)
            sage: min(v.norm().n() for v in L.reduced_basis)                            # needs sage.symbolic
            6.03890756700000e10

            sage: L.shortest_vector().norm().n()                                        # needs sage.symbolic
            3.74165738677394

            sage: L = IntegerLattice(A, lll_reduce=False)
            sage: min(v.norm().n() for v in L.reduced_basis)                            # needs sage.symbolic
            6.03890756700000e10

            sage: L.shortest_vector(algorithm='pari').norm().n()                        # needs sage.symbolic
            3.74165738677394

            sage: L = IntegerLattice(A, lll_reduce=True)
            sage: L.shortest_vector(algorithm='pari').norm().n()                        # needs sage.symbolic
            3.74165738677394
        """
    def update_reduced_basis(self, w) -> None:
        """
        Inject the vector ``w`` and run LLL to update the basis.

        INPUT:

        - ``w`` -- a vector

        OUTPUT: nothing is returned but the internal state is modified

        EXAMPLES::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: A = sage.crypto.gen_lattice(type='random', n=1, m=30, q=2^40, seed=42)
            sage: L = IntegerLattice(A)
            sage: B = L.reduced_basis
            sage: v = L.shortest_vector(update_reduced_basis=False)
            sage: L.update_reduced_basis(v)
            sage: bool(L.reduced_basis[0].norm() < B[0].norm())
            True
        """
    @cached_method
    def voronoi_cell(self, radius=None):
        """
        Compute the Voronoi cell of a lattice, returning a Polyhedron.

        INPUT:

        - ``radius`` -- (default: automatic determination) radius of ball
          containing considered vertices

        OUTPUT: the Voronoi cell as a Polyhedron instance

        The result is cached so that subsequent calls to this function
        return instantly.

        EXAMPLES::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: L = IntegerLattice([[1, 0], [0, 1]])
            sage: V = L.voronoi_cell()
            sage: V.Vrepresentation()
            (A vertex at (1/2, -1/2),
             A vertex at (1/2, 1/2),
             A vertex at (-1/2, 1/2),
             A vertex at (-1/2, -1/2))

        The volume of the Voronoi cell is the square root of the
        discriminant of the lattice::

            sage: L = IntegerLattice(Matrix(ZZ, 4, 4, [[0,0,1,-1], [1,-1,2,1],
            ....:                                      [-6,0,3,3,], [-6,-24,-6,-5]])); L
            Free module of degree 4 and rank 4 over Integer Ring
            User basis matrix:
            [  0   0   1  -1]
            [  1  -1   2   1]
            [ -6   0   3   3]
            [ -6 -24  -6  -5]
            sage: V = L.voronoi_cell()  # long time
            sage: V.volume()            # long time
            678
            sage: sqrt(L.discriminant())
            678

        Lattices not having full dimension are handled as well::

            sage: L = IntegerLattice([[2, 0, 0], [0, 2, 0]])
            sage: V = L.voronoi_cell()
            sage: V.Hrepresentation()
            (An inequality (-1, 0, 0) x + 1 >= 0,
             An inequality (0, -1, 0) x + 1 >= 0,
             An inequality (1, 0, 0) x + 1 >= 0,
             An inequality (0, 1, 0) x + 1 >= 0)

        ALGORITHM:

        Uses parts of the algorithm from [VB1996]_.
        """
    def voronoi_relevant_vectors(self):
        """
        Compute the embedded vectors inducing the Voronoi cell.

        OUTPUT: the list of Voronoi relevant vectors

        EXAMPLES::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: L = IntegerLattice([[3, 0], [4, 0]])
            sage: L.voronoi_relevant_vectors()
            [(-1, 0), (1, 0)]
        """
    def closest_vector(self, t):
        """
        Compute the closest vector in the embedded lattice to a given vector.

        INPUT:

        - ``t`` -- the target vector to compute the closest vector to

        OUTPUT: the vector in the lattice closest to ``t``

        EXAMPLES::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: L = IntegerLattice([[1, 0], [0, 1]])
            sage: L.closest_vector((-6, 5/3))
            (-6, 2)

        ALGORITHM:

        Uses the algorithm from [MV2010]_.

        TESTS:

        Check that the example from :issue:`29866` works::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: M = matrix(ZZ, [[20957228, -4966110], [9411844, 19625639]])
            sage: L = IntegerLattice(M)
            sage: u = vector([-423434678248195, -18882583298608161305227077482])
            sage: L.closest_vector(u) in L
            True

        Check that the example, of non-maximal rank, from :issue:`32486` works::

            from sage.modules.free_module_integer import IntegerLattice
            L = IntegerLattice([[-1,  0,  1],[1,0,2]])
            L.closest_vector((1,1,1))
            (2, 0, 1)
        """
    def approximate_closest_vector(self, t, delta=None, algorithm: str = 'embedding', *args, **kwargs):
        '''
        Compute a vector `w` in this lattice which is close to the target vector `t`.
        The ratio `\\frac{|t-w|}{|t-u|}`, where `u` is the closest lattice vector to `t`,
        is exponential in the dimension of the lattice.

        This will check whether the basis is already `\\delta`-LLL-reduced
        and otherwise it will run LLL to make sure that it is. For more
        information about ``delta`` see :meth:`LLL`.

        INPUT:

        - ``t`` -- the target vector to compute a close vector to

        - ``delta`` -- (default: ``0.99``) the LLL reduction parameter

        - ``algorithm`` -- string (default: \'embedding\'):

          - ``\'embedding\'`` -- embeds the lattice in a d+1 dimensional space
            and seeks short vectors using LLL. This calls LLL twice but is
            usually still quick.

          - ``\'nearest_plane\'`` -- uses the "NEAREST PLANE" algorithm from [Bab86]_

          - ``\'rounding_off\'`` -- uses the "ROUNDING OFF" algorithm from [Bab86]_.
            This yields slightly worse results than the other algorithms but is
            at least faster than ``\'nearest_plane\'``.

        - ``*args`` -- passed through to :meth:`LLL`

        - ``**kwds`` -- passed through to :meth:`LLL`

        OUTPUT: the vector `w` described above

        EXAMPLES::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: L = IntegerLattice([[1, 0], [0, 1]])
            sage: L.approximate_closest_vector((-6, 5/3))
            (-6, 2)

        The quality of the approximation depends on ``delta``::

            sage: from sage.modules.free_module_integer import IntegerLattice
            sage: L = IntegerLattice([[101, 0, 0, 0], [0, 101, 0, 0],
            ....:                     [0, 0, 101, 0], [-28, 39, 45, 1]], lll_reduce=False)
            sage: t = vector([1337]*4)
            sage: L.approximate_closest_vector(t, delta=0.26)
            (1331, 1324, 1349, 1334)
            sage: L.approximate_closest_vector(t, delta=0.99)
            (1326, 1349, 1339, 1345)
            sage: L.closest_vector(t)
            (1326, 1349, 1339, 1345)

            sage: # Checking that the other algorithms work
            sage: L.approximate_closest_vector(t, algorithm=\'nearest_plane\')
            (1326, 1349, 1339, 1345)
            sage: L.approximate_closest_vector(t, algorithm=\'rounding_off\')
            (1331, 1324, 1349, 1334)
        '''
    def babai(self, *args, **kwargs):
        """
        Alias for :meth:`approximate_closest_vector`.
        """
