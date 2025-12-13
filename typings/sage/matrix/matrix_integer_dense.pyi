import cypari2.pari_instance
import sage.matrix.matrix_dense
import sage.matrix.matrix_space as matrix_space
from sage.arith.misc import previous_prime as previous_prime
from sage.categories.category import RDF as RDF, ZZ as ZZ
from sage.cpython.string import bytes_to_str as bytes_to_str, str_to_bytes as str_to_bytes
from sage.libs.pari.convert_sage_matrix import gen_to_sage_matrix as gen_to_sage_matrix
from sage.matrix.matrix2 import decomp_seq as decomp_seq
from sage.misc.superseded import deprecated_function_alias as deprecated_function_alias
from sage.misc.timing import cputime as cputime
from sage.misc.verbose import get_verbose as get_verbose, verbose as verbose
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing as PolynomialRing
from sage.rings.rational_field import QQ as QQ
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.proof.proof import get_proof_flag as get_proof_flag
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

__pyx_capi__: dict
fplll_fp_map: dict
pari: cypari2.pari_instance.Pari

class Matrix_integer_dense(sage.matrix.matrix_dense.Matrix_dense):
    """Matrix_integer_dense(parent, entries=None, copy=None, bool coerce=True)

    File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 172)

    Matrix over the integers, implemented using FLINT.

    On a 32-bit machine, they can have at most `2^{32}-1` rows or
    columns.  On a 64-bit machine, matrices can have at most
    `2^{64}-1` rows or columns.

    EXAMPLES::

        sage: a = MatrixSpace(ZZ,3)(2); a
        [2 0 0]
        [0 2 0]
        [0 0 2]
        sage: a = matrix(ZZ,1,3, [1,2,-3]); a
        [ 1  2 -3]
        sage: a = MatrixSpace(ZZ,2,4)(2); a
        Traceback (most recent call last):
        ...
        TypeError: nonzero scalar matrix must be square

    TESTS:

    Test hashing::

        sage: a = Matrix(ZZ, 2, [1,2,3,4])
        sage: hash(a)
        Traceback (most recent call last):
        ...
        TypeError: mutable matrices are unhashable
        sage: a.set_immutable()
        sage: hash(a)
        1846857684291126914  # 64-bit
        1591707266           # 32-bit"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 241)

                Initialize a dense matrix over the integers.

                INPUT:

                - ``parent`` -- a matrix space over ``ZZ``

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``False``, assume without checking that the
                  entries are of type :class:`Integer`

                EXAMPLES:

                The __init__ function is called implicitly in each of the
                examples below to actually fill in the values of the matrix.

                We create a `2 \\times 2` and a `1\\times 4` matrix::

                    sage: matrix(ZZ,2,2,range(4))
                    [0 1]
                    [2 3]
                    sage: Matrix(ZZ,1,4,range(4))
                    [0 1 2 3]

                If the number of columns isn't given, it is determined from the
                number of elements in the list.

                ::

                    sage: matrix(ZZ,2,range(4))
                    [0 1]
                    [2 3]
                    sage: matrix(ZZ,2,range(6))
                    [0 1 2]
                    [3 4 5]

                Another way to make a matrix is to create the space of matrices and
                coerce lists into it.

                ::

                    sage: A = Mat(ZZ,2); A
                    Full MatrixSpace of 2 by 2 dense matrices over Integer Ring
                    sage: A(range(4))
                    [0 1]
                    [2 3]

                Actually it is only necessary that the input can be coerced to a
                list, so the following also works::

                    sage: v = reversed(range(4))
                    sage: A(v)
                    [3 2]
                    [1 0]

                Matrices can have many rows or columns (in fact, on a 64-bit
                machine they could have up to `2^64-1` rows or columns)::

                    sage: v = matrix(ZZ,1,10^5, range(10^5))
                    sage: v.parent()
                    Full MatrixSpace of 1 by 100000 dense matrices over Integer Ring
        """
    def BKZ(self, delta=..., algorithm=..., fp=..., block_size=..., prune=..., use_givens=..., precision=..., proof=..., **kwds) -> Any:
        '''Matrix_integer_dense.BKZ(self, delta=None, algorithm=\'fpLLL\', fp=None, block_size=10, prune=0, use_givens=False, precision=0, proof=None, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2775)

        Return the result of running Block Korkin-Zolotarev reduction on
        ``self`` interpreted as a lattice.

        INPUT:

        - ``delta`` -- (default: ``0.99``) LLL parameter

        - ``algorithm`` -- (default: ``\'fpLLL\'``) ``\'fpLLL\'`` or ``"NTL"``

        - ``fp`` -- floating point number implementation

            - ``None`` -- NTL\'s exact reduction or fpLLL\'s wrapper (default)

            - ``\'fp\'`` -- double precision: NTL\'s FP or fpLLL\'s double

            - ``\'ld\'`` -- long doubles (fpLLL only)

            - ``\'qd\'`` -- NTL\'s QP

            - ``\'qd1\'`` -- quad doubles: Uses ``quad_float`` precision
              to compute Gram-Schmidt, but uses double precision in
              the search phase of the block reduction algorithm. This
              seems adequate for most purposes, and is faster than
              ``\'qd\'``, which uses quad_float precision uniformly
              throughout (NTL only).

            - ``\'xd\'`` -- extended exponent: NTL\'s XD or fpLLL\'s dpe

            - ``\'rr\'`` -- arbitrary precision: NTL\'RR or fpLLL\'s MPFR

        - ``block_size`` -- (default: ``10``) specifies the size
          of the blocks in the reduction.  High values yield
          shorter vectors, but the running time increases double
          exponentially with ``block_size``.  ``block_size``
          should be between 2 and the number of rows of ``self``.

        - ``proof`` -- (default: same as ``proof.linear_algebra()``)
          Insist on full BKZ reduction. If disabled and fplll is
          called, reduction is much faster but the result is not fully
          BKZ reduced.

        NTL SPECIFIC INPUT:

        - ``prune`` -- (default: ``0``) the optional parameter
          ``prune`` can be set to any positive number to invoke the
          Volume Heuristic from [SH1995]_. This can significantly reduce
          the running time, and hence allow much bigger block size,
          but the quality of the reduction is of course not as good in
          general. Higher values of ``prune`` mean better quality, and
          slower running time. When ``prune`` is ``0``, pruning is
          disabled. Recommended usage: for ``block_size==30``, set
          ``10 <= prune <=15``.

        - ``use_givens`` -- use Givens orthogonalization.  Only
          applies to approximate reduction using NTL.  This is a bit
          slower, but generally much more stable, and is really the
          preferred orthogonalization strategy.  For a nice
          description of this, see Chapter 5 of [GL1996]_.

        fpLLL SPECIFIC INPUT:

        - ``precision`` -- (default: ``0`` for automatic choice) bit
          precision to use if ``fp=\'rr\'`` is set

        - ``**kwds`` -- keywords to be passed to :mod:`fpylll`; see
          :class:`fpylll.BKZ.Param` for details

        Also, if the verbose level is at least `2`, some output
        is printed during the computation.

        EXAMPLES::

            sage: A = Matrix(ZZ,3,3,range(1,10))
            sage: A.BKZ()
            [ 0  0  0]
            [ 2  1  0]
            [-1  1  3]

            sage: A = Matrix(ZZ,3,3,range(1,10))
            sage: A.BKZ(use_givens=True)
            [ 0  0  0]
            [ 2  1  0]
            [-1  1  3]

            sage: A = Matrix(ZZ,3,3,range(1,10))
            sage: A.BKZ(fp=\'fp\')
            [ 0  0  0]
            [ 2  1  0]
            [-1  1  3]

        ALGORITHM:

        Calls either NTL or fpLLL.'''
    def LLL(self, delta=..., eta=..., algorithm=..., fp=..., prec=..., early_red=..., use_givens=..., use_siegel=..., transformation=..., **kwds) -> Any:
        '''Matrix_integer_dense.LLL(self, delta=None, eta=None, algorithm=\'fpLLL:wrapper\', fp=None, prec=0, early_red=False, use_givens=False, use_siegel=False, transformation=False, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2983)

        Return LLL-reduced or approximated LLL reduced matrix `R` of the lattice
        generated by the rows of ``self``.

        A set of vectors `(b_1, b_2, ..., b_d)` is `(\\delta, \\eta)`-LLL-reduced
        if the two following conditions hold:

        -  For any `i > j`, we have `\\lvert \\mu_{i,j} \\rvert \\leq \\eta`.

        -  For any `i < d`, we have `\\delta \\lvert b_i^* \\rvert^2 \\leq
           \\lvert b_{i + 1}^* + \\mu_{i+1, i} b_i^* \\rvert^2`,

        where `\\mu_{i,j} = \\langle b_i, b_j^* \\rangle / \\langle b_j^*, b_j^*
        \\rangle` and `b_i^*` is the `i`-th vector of the Gram-Schmidt
        orthogonalisation of `(b_1, b_2, ..., b_d)`.

        The default reduction parameters are `\\delta = 0.99` and `\\eta = 0.501`.
        The parameters `\\delta` and `\\eta` must satisfy `0.25 < \\delta
        \\leq 1.0` and `0.5 \\leq \\eta < \\sqrt{\\delta}`. Polynomial time
        complexity is only guaranteed for `\\delta < 1`. Not every algorithm
        admits the case `\\delta = 1`.

        If the matrix has a nonzero kernel, the LLL-reduced matrix will contain
        zero rows, so that the output has the same dimensions as the input. The
        transformation matrix is always invertible over the integers.

        Also the rank of ``self`` is cached if it is computed during the
        reduction. Note that in general this only happens when
        ``self.rank() == self.ncols()`` and the exact algorithm is used.

        INPUT:

        - ``delta`` -- (default: ``0.99``) `\\delta` parameter as described
          above, ignored by pari

        - ``eta`` -- (default: ``0.501``) `\\eta` parameter as described above,
          ignored by NTL and pari

        - ``algorithm`` -- string; one of the algorithms listed below
          (default: ``\'fpLLL:wrapper\'``)

        - ``fp`` -- floating point number implementation, ignored by pari:

          - ``None`` -- NTL\'s exact reduction or fpLLL\'s wrapper
          - ``\'fp\'`` -- double precision: NTL\'s FP or fpLLL\'s double
          - ``\'ld\'`` -- long doubles (fpLLL only)
          - ``\'qd\'`` -- NTL\'s QP
          - ``\'xd\'`` -- extended exponent: NTL\'s XD or fpLLL\'s dpe
          - ``\'rr\'`` -- arbitrary precision: NTL\'s RR or fpLLL\'s MPFR

        - ``prec`` -- (default: auto choose) precision, ignored by NTL and pari

        - ``early_red`` -- boolean (default: ``False``); perform early reduction,
          ignored by NTL and pari

        - ``use_givens`` -- boolean (default: ``False``); use Givens
          orthogonalization.  Only applies to approximate reduction
          using NTL.  This is slower but generally more stable.

        - ``use_siegel`` -- boolean (default: ``False``); use Siegel\'s condition
          instead of Lovász\'s condition, ignored by NTL and pari

        - ``transformation`` -- boolean (default: ``False``); also return transformation
          matrix

        - ``**kwds`` -- keywords to be passed to :mod:`fpylll`; see
          :meth:`fpylll.LLL.reduction` for details

        Also, if the verbose level is at least `2`, some output
        is printed during the computation.

        AVAILABLE ALGORITHMS:

        - ``\'NTL:LLL\'`` -- NTL\'s LLL + choice of ``fp``

        - ``\'fpLLL:heuristic\'`` -- fpLLL\'s heuristic + choice of ``fp``

        - ``\'fpLLL:fast\'`` -- fpLLL\'s fast + choice of ``fp``

        - ``\'fpLLL:proved\'`` -- fpLLL\'s proved + choice of ``fp``

        - ``\'fpLLL:wrapper\'`` -- fpLLL\'s automatic choice (default)

        - ``\'pari\'`` -- pari\'s qflll

        - ``\'flatter\'`` -- external executable ``flatter``, requires manual install (see caveats below).
          Note that sufficiently new version of ``pari`` also supports FLATTER algorithm, see
          https://pari.math.u-bordeaux.fr/dochtml/html/Vectors__matrices__linear_algebra_and_sets.html#qflll.

        OUTPUT: a matrix over the integers

        EXAMPLES::

            sage: A = Matrix(ZZ,3,3,range(1,10))
            sage: A.LLL()
            [ 0  0  0]
            [ 2  1  0]
            [-1  1  3]

        We compute the extended GCD of a list of integers using LLL, this
        example is from the Magma handbook::

            sage: Q = [ 67015143, 248934363018, 109210, 25590011055, 74631449,
            ....:       10230248, 709487, 68965012139, 972065, 864972271 ]
            sage: n = len(Q)
            sage: S = 100
            sage: X = Matrix(ZZ, n, n + 1)
            sage: for i in range(n):
            ....:     X[i, i + 1] = 1
            sage: for i in range(n):
            ....:     X[i, 0] = S * Q[i]
            sage: L = X.LLL()
            sage: M = L.row(n-1).list()[1:]
            sage: M
            [-3, -1, 13, -1, -4, 2, 3, 4, 5, -1]
            sage: add(Q[i]*M[i] for i in range(n))
            -1

        The case `\\delta = 1` is not always supported::

            sage: L = X.LLL(delta=2)
            Traceback (most recent call last):
            ...
            TypeError: delta must be <= 1
            sage: L = X.LLL(delta=1)    # not tested, will eat lots of ram
            Traceback (most recent call last):
            ...
            RuntimeError: infinite loop in LLL
            sage: L = X.LLL(delta=1, algorithm=\'NTL:LLL\')
            sage: L[-1]
            (-100, -3, -1, 13, -1, -4, 2, 3, 4, 5, -1)

        We return the transformation matrix::

            sage: A = random_matrix(ZZ, 10, 20)
            sage: R, U = A.LLL(transformation=True)
            sage: U * A == R
            True

            sage: R, U = A.LLL(algorithm=\'NTL:LLL\', transformation=True)
            sage: U * A == R
            True

            sage: R, U = A.LLL(algorithm=\'pari\', transformation=True)
            sage: U * A == R
            True

        Example with a nonzero kernel::

            sage: M = matrix(4,3,[1,2,3,2,4,6,7,0,1,-1,-2,-3])
            sage: M.LLL()[0:2]
            [0 0 0]
            [0 0 0]

            sage: M.LLL(algorithm="NTL:LLL")[0:2]
            [0 0 0]
            [0 0 0]

            sage: M.LLL(algorithm=\'pari\')[0:2]
            [0 0 0]
            [0 0 0]

        When ``algorithm=\'flatter\'``, some matrices are not supported depends
        on ``flatter``. For example::

            sage: # needs flatter
            sage: m = matrix.zero(3, 2)
            sage: m.LLL(algorithm=\'flatter\')
            Traceback (most recent call last):
            ...
            ValueError: ...

        TESTS::

            sage: matrix(ZZ, 0, 0).LLL()
            []
            sage: matrix(ZZ, 3, 0).LLL()
            []
            sage: matrix(ZZ, 0, 3).LLL()
            []

            sage: M = matrix(ZZ, [[1,2,3],[31,41,51],[101,201,301]])
            sage: A = M.LLL()
            sage: A
            [ 0  0  0]
            [-1  0  1]
            [ 1  1  1]
            sage: B = M.LLL(algorithm=\'NTL:LLL\')
            sage: C = M.LLL(algorithm=\'NTL:LLL\', fp=None)
            sage: D = M.LLL(algorithm=\'NTL:LLL\', fp=\'fp\')
            sage: F = M.LLL(algorithm=\'NTL:LLL\', fp=\'xd\')
            sage: G = M.LLL(algorithm=\'NTL:LLL\', fp=\'rr\')
            sage: A == B == C == D == F == G
            True
            sage: H = M.LLL(algorithm=\'NTL:LLL\', fp=\'qd\')
            Traceback (most recent call last):
            ...
            TypeError: algorithm NTL:LLL_QD not supported

            sage: A = random_matrix(ZZ, 0, 0)
            sage: R, U = A.LLL(transformation=True)

        Test rank caching::

            sage: M = matrix(4,3,[1,2,3,2,4,6,7,0,1,-1,-2,-3])
            sage: R = M.LLL(algorithm="NTL:LLL")
            sage: M._cache
            {\'rank\': 2}
            sage: M._clear_cache()
            sage: R = M.LLL(algorithm=\'pari\')
            sage: M._cache
            {\'rank\': 2}

        Check that :issue:`37236` is fixed::

            sage: M = matrix(ZZ, 2, 2, [-1,1,1,1])
            sage: L = M.LLL(algorithm="NTL:LLL")
            sage: M.det() == L.det()
            True

        .. NOTE::

            See :mod:`sage.libs.ntl.ntl_mat_ZZ.ntl_mat_ZZ.LLL` and
            :mod:`fpylll.fplll.lll` for details on the algorithms used.

            Although LLL is a deterministic algorithm, the output for
            different implementations and CPUs (32-bit vs. 64-bit) may
            vary, while still being correct.

        Check ``flatter``::

            sage: # needs flatter
            sage: M = matrix(ZZ, 2, 2, [-1,1,1,1])
            sage: L = M.LLL(algorithm="flatter")
            sage: abs(M.det()) == abs(L.det())
            True
            sage: L = M.LLL(algorithm="flatter", delta=0.99)
            sage: abs(M.det()) == abs(L.det())
            True'''
    @overload
    def antitranspose(self) -> Any:
        """Matrix_integer_dense.antitranspose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5779)

        Return the antitranspose of ``self``, without changing ``self``.

        EXAMPLES::

            sage: A = matrix(2,3,range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
            sage: A.antitranspose()
            [5 2]
            [4 1]
            [3 0]
            sage: A
            [0 1 2]
            [3 4 5]

            sage: A.subdivide(1,2); A
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: A.antitranspose()
            [5|2]
            [-+-]
            [4|1]
            [3|0]"""
    @overload
    def antitranspose(self) -> Any:
        """Matrix_integer_dense.antitranspose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5779)

        Return the antitranspose of ``self``, without changing ``self``.

        EXAMPLES::

            sage: A = matrix(2,3,range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
            sage: A.antitranspose()
            [5 2]
            [4 1]
            [3 0]
            sage: A
            [0 1 2]
            [3 4 5]

            sage: A.subdivide(1,2); A
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: A.antitranspose()
            [5|2]
            [-+-]
            [4|1]
            [3|0]"""
    @overload
    def antitranspose(self) -> Any:
        """Matrix_integer_dense.antitranspose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5779)

        Return the antitranspose of ``self``, without changing ``self``.

        EXAMPLES::

            sage: A = matrix(2,3,range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
            sage: A.antitranspose()
            [5 2]
            [4 1]
            [3 0]
            sage: A
            [0 1 2]
            [3 4 5]

            sage: A.subdivide(1,2); A
            [0 1|2]
            [---+-]
            [3 4|5]
            sage: A.antitranspose()
            [5|2]
            [-+-]
            [4|1]
            [3|0]"""
    @overload
    def augment(self, right, subdivide=...) -> Any:
        """Matrix_integer_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5397)

        Return a new matrix formed by appending the matrix
        (or vector) ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``right``

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side of ``self``.
        If ``right`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a column vector.  (The code first
        converts a vector to a 1-column matrix.)

        EXAMPLES::

            sage: A = matrix(ZZ, 4, 5, range(20))
            sage: B = matrix(ZZ, 4, 3, range(12))
            sage: A.augment(B)
            [ 0  1  2  3  4  0  1  2]
            [ 5  6  7  8  9  3  4  5]
            [10 11 12 13 14  6  7  8]
            [15 16 17 18 19  9 10 11]

        A vector may be augmented to a matrix. ::

            sage: A = matrix(ZZ, 3, 5, range(15))
            sage: v = vector(ZZ, 3, range(3))
            sage: A.augment(v)
            [ 0  1  2  3  4  0]
            [ 5  6  7  8  9  1]
            [10 11 12 13 14  2]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(ZZ, 3, 5, range(15))
            sage: B = matrix(ZZ, 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3  4| 0  1  2]
            [ 5  6  7  8  9| 3  4  5]
            [10 11 12 13 14| 6  7  8]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(ZZ, [[1, 2],[3, 4]])
            sage: B = matrix(ZZ, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, not 2 != 3"""
    @overload
    def augment(self, B) -> Any:
        """Matrix_integer_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5397)

        Return a new matrix formed by appending the matrix
        (or vector) ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``right``

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side of ``self``.
        If ``right`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a column vector.  (The code first
        converts a vector to a 1-column matrix.)

        EXAMPLES::

            sage: A = matrix(ZZ, 4, 5, range(20))
            sage: B = matrix(ZZ, 4, 3, range(12))
            sage: A.augment(B)
            [ 0  1  2  3  4  0  1  2]
            [ 5  6  7  8  9  3  4  5]
            [10 11 12 13 14  6  7  8]
            [15 16 17 18 19  9 10 11]

        A vector may be augmented to a matrix. ::

            sage: A = matrix(ZZ, 3, 5, range(15))
            sage: v = vector(ZZ, 3, range(3))
            sage: A.augment(v)
            [ 0  1  2  3  4  0]
            [ 5  6  7  8  9  1]
            [10 11 12 13 14  2]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(ZZ, 3, 5, range(15))
            sage: B = matrix(ZZ, 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3  4| 0  1  2]
            [ 5  6  7  8  9| 3  4  5]
            [10 11 12 13 14| 6  7  8]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(ZZ, [[1, 2],[3, 4]])
            sage: B = matrix(ZZ, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, not 2 != 3"""
    @overload
    def augment(self, v) -> Any:
        """Matrix_integer_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5397)

        Return a new matrix formed by appending the matrix
        (or vector) ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``right``

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side of ``self``.
        If ``right`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a column vector.  (The code first
        converts a vector to a 1-column matrix.)

        EXAMPLES::

            sage: A = matrix(ZZ, 4, 5, range(20))
            sage: B = matrix(ZZ, 4, 3, range(12))
            sage: A.augment(B)
            [ 0  1  2  3  4  0  1  2]
            [ 5  6  7  8  9  3  4  5]
            [10 11 12 13 14  6  7  8]
            [15 16 17 18 19  9 10 11]

        A vector may be augmented to a matrix. ::

            sage: A = matrix(ZZ, 3, 5, range(15))
            sage: v = vector(ZZ, 3, range(3))
            sage: A.augment(v)
            [ 0  1  2  3  4  0]
            [ 5  6  7  8  9  1]
            [10 11 12 13 14  2]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(ZZ, 3, 5, range(15))
            sage: B = matrix(ZZ, 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3  4| 0  1  2]
            [ 5  6  7  8  9| 3  4  5]
            [10 11 12 13 14| 6  7  8]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(ZZ, [[1, 2],[3, 4]])
            sage: B = matrix(ZZ, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, not 2 != 3"""
    @overload
    def augment(self, B, subdivide=...) -> Any:
        """Matrix_integer_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5397)

        Return a new matrix formed by appending the matrix
        (or vector) ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``right``

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side of ``self``.
        If ``right`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a column vector.  (The code first
        converts a vector to a 1-column matrix.)

        EXAMPLES::

            sage: A = matrix(ZZ, 4, 5, range(20))
            sage: B = matrix(ZZ, 4, 3, range(12))
            sage: A.augment(B)
            [ 0  1  2  3  4  0  1  2]
            [ 5  6  7  8  9  3  4  5]
            [10 11 12 13 14  6  7  8]
            [15 16 17 18 19  9 10 11]

        A vector may be augmented to a matrix. ::

            sage: A = matrix(ZZ, 3, 5, range(15))
            sage: v = vector(ZZ, 3, range(3))
            sage: A.augment(v)
            [ 0  1  2  3  4  0]
            [ 5  6  7  8  9  1]
            [10 11 12 13 14  2]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(ZZ, 3, 5, range(15))
            sage: B = matrix(ZZ, 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3  4| 0  1  2]
            [ 5  6  7  8  9| 3  4  5]
            [10 11 12 13 14| 6  7  8]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(ZZ, [[1, 2],[3, 4]])
            sage: B = matrix(ZZ, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, not 2 != 3"""
    @overload
    def augment(self, B) -> Any:
        """Matrix_integer_dense.augment(self, right, subdivide=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5397)

        Return a new matrix formed by appending the matrix
        (or vector) ``right`` on the right side of ``self``.

        INPUT:

        - ``right`` -- a matrix, vector or free module element, whose
          dimensions are compatible with ``self``

        - ``subdivide`` -- (default: ``False``) request the resulting
          matrix to have a new subdivision, separating ``self`` from ``right``

        OUTPUT:

        A new matrix formed by appending ``right`` onto the right side of ``self``.
        If ``right`` is a vector (or free module element) then in this context
        it is appropriate to consider it as a column vector.  (The code first
        converts a vector to a 1-column matrix.)

        EXAMPLES::

            sage: A = matrix(ZZ, 4, 5, range(20))
            sage: B = matrix(ZZ, 4, 3, range(12))
            sage: A.augment(B)
            [ 0  1  2  3  4  0  1  2]
            [ 5  6  7  8  9  3  4  5]
            [10 11 12 13 14  6  7  8]
            [15 16 17 18 19  9 10 11]

        A vector may be augmented to a matrix. ::

            sage: A = matrix(ZZ, 3, 5, range(15))
            sage: v = vector(ZZ, 3, range(3))
            sage: A.augment(v)
            [ 0  1  2  3  4  0]
            [ 5  6  7  8  9  1]
            [10 11 12 13 14  2]

        The ``subdivide`` option will add a natural subdivision between
        ``self`` and ``right``.  For more details about how subdivisions
        are managed when augmenting, see
        :meth:`sage.matrix.matrix1.Matrix.augment`.  ::

            sage: A = matrix(ZZ, 3, 5, range(15))
            sage: B = matrix(ZZ, 3, 3, range(9))
            sage: A.augment(B, subdivide=True)
            [ 0  1  2  3  4| 0  1  2]
            [ 5  6  7  8  9| 3  4  5]
            [10 11 12 13 14| 6  7  8]

        Errors are raised if the sizes are incompatible. ::

            sage: A = matrix(ZZ, [[1, 2],[3, 4]])
            sage: B = matrix(ZZ, [[10, 20], [30, 40], [50, 60]])
            sage: A.augment(B)
            Traceback (most recent call last):
            ...
            TypeError: number of rows must be the same, not 2 != 3"""
    def charpoly(self, var=..., algorithm=...) -> Any:
        '''Matrix_integer_dense.charpoly(self, var=\'x\', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1305)

        .. NOTE::

            The characteristic polynomial is defined as `\\det(xI-A)`.

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- (default: ``\'linbox\'``) either ``\'generic\'``,
          ``\'flint\'`` or ``\'linbox\'``

        EXAMPLES::

            sage: A = matrix(ZZ,6, range(36))
            sage: f = A.charpoly(); f
            x^6 - 105*x^5 - 630*x^4
            sage: f(A) == 0
            True
            sage: g = A.charpoly(algorithm=\'flint\')
            sage: f == g
            True
            sage: n=20; A = Mat(ZZ,n)(range(n^2))
            sage: A.charpoly()
            x^20 - 3990*x^19 - 266000*x^18
            sage: A.minpoly()
            x^3 - 3990*x^2 - 266000*x

        On non square matrices, this method raises an ArithmeticError::

            sage: matrix(ZZ, 2, 1).charpoly()
            Traceback (most recent call last):
            ...
            ArithmeticError: only valid for square matrix

        TESTS:

        The cached polynomial should be independent of the ``var``
        argument (:issue:`12292`). We check (indirectly) that the
        second call uses the cached value by noting that its result is
        not cached::

            sage: M = MatrixSpace(ZZ, 2)
            sage: A = M(range(0, 2^2))
            sage: type(A)
            <class \'sage.matrix.matrix_integer_dense.Matrix_integer_dense\'>
            sage: A.charpoly(\'x\')
            x^2 - 3*x - 2
            sage: A.charpoly(\'y\')
            y^2 - 3*y - 2
            sage: A._cache[\'charpoly_linbox\']
            x^2 - 3*x - 2

        Test corner cases::

            sage: matrix([5]).charpoly(\'z\', \'flint\')
            z - 5
            sage: matrix([5]).charpoly(\'z\', \'linbox\')
            z - 5
            sage: matrix([5]).charpoly(\'z\', \'generic\')
            z - 5


            sage: matrix([]).charpoly(\'y\', \'flint\')
            1
            sage: matrix([]).charpoly(\'y\', \'linbox\')
            1
            sage: matrix([]).charpoly(\'y\', \'generic\')
            1

            sage: matrix([0]).charpoly(\'x\', \'flint\')
            x
            sage: matrix([0]).charpoly(\'x\', \'linbox\')
            x
            sage: matrix([0]).charpoly(\'x\', \'generic\')
            x

        Consistency on random inputs::

            sage: for _ in range(100):
            ....:     dim = randint(1, 20)
            ....:     m  = random_matrix(ZZ, dim)
            ....:     m._clear_cache(); ans_flint = m.charpoly(algorithm=\'flint\')
            ....:     m._clear_cache(); ans_linbox = m.charpoly(algorithm=\'linbox\')
            ....:     m._clear_cache(); ans_generic = m.charpoly(algorithm=\'generic\')
            ....:     if ans_flint != ans_linbox or ans_flint != ans_generic:
            ....:         raise RuntimeError("ans_flint = {}, ans_linbox = {} and ans_generic = {} for\\n{}".format(
            ....:                            ans_flint, ans_linbox, ans_generic, m.str()))'''
    def column(self, Py_ssize_ti, from_list=...) -> Any:
        """Matrix_integer_dense.column(self, Py_ssize_t i, from_list=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5299)

        Return the `i`-th column of this matrix as a dense vector.

        INPUT:

        - ``i`` -- integer

        - ``from_list`` -- ignored

        EXAMPLES::

            sage: m = matrix(ZZ, 3, 2, [1, -2, 3, 4, -1, 0])
            sage: m.column(1)
            (-2, 4, 0)
            sage: m.column(1, from_list=True)
            (-2, 4, 0)
            sage: m.column(-1)
            (-2, 4, 0)
            sage: m.column(-2)
            (1, 3, -1)

            sage: m.column(2)
            Traceback (most recent call last):
            ...
            IndexError: column index out of range
            sage: m.column(-3)
            Traceback (most recent call last):
            ...
            IndexError: column index out of range"""
    @overload
    def decomposition(self, **kwds) -> Any:
        """Matrix_integer_dense.decomposition(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 4866)

        Return the decomposition of the free module on which this matrix A
        acts from the right (i.e., the action is x goes to x A), along with
        whether this matrix acts irreducibly on each factor. The factors
        are guaranteed to be sorted in the same way as the corresponding
        factors of the characteristic polynomial, and are saturated as ZZ
        modules.

        INPUT:

        - ``self`` -- a matrix over the integers

        - ``**kwds`` -- these are passed onto to the
          decomposition over QQ command

        EXAMPLES::

            sage: t = ModularSymbols(11,sign=1).hecke_matrix(2)
            sage: w = t.change_ring(ZZ)
            sage: w
            [ 3 -2]
            [ 0 -2]
            sage: w.charpoly().factor()
            (x - 3) * (x + 2)
            sage: w.decomposition()
            [(Free module of degree 2 and rank 1 over Integer Ring
              Echelon basis matrix:
              [ 5 -2],
              True),
             (Free module of degree 2 and rank 1 over Integer Ring
              Echelon basis matrix:
              [0 1],
              True)]"""
    @overload
    def decomposition(self) -> Any:
        """Matrix_integer_dense.decomposition(self, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 4866)

        Return the decomposition of the free module on which this matrix A
        acts from the right (i.e., the action is x goes to x A), along with
        whether this matrix acts irreducibly on each factor. The factors
        are guaranteed to be sorted in the same way as the corresponding
        factors of the characteristic polynomial, and are saturated as ZZ
        modules.

        INPUT:

        - ``self`` -- a matrix over the integers

        - ``**kwds`` -- these are passed onto to the
          decomposition over QQ command

        EXAMPLES::

            sage: t = ModularSymbols(11,sign=1).hecke_matrix(2)
            sage: w = t.change_ring(ZZ)
            sage: w
            [ 3 -2]
            [ 0 -2]
            sage: w.charpoly().factor()
            (x - 3) * (x + 2)
            sage: w.decomposition()
            [(Free module of degree 2 and rank 1 over Integer Ring
              Echelon basis matrix:
              [ 5 -2],
              True),
             (Free module of degree 2 and rank 1 over Integer Ring
              Echelon basis matrix:
              [0 1],
              True)]"""
    def determinant(self, algorithm=..., proof=..., stabilize=...) -> Any:
        '''Matrix_integer_dense.determinant(self, algorithm=\'default\', proof=None, stabilize=2)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 3749)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm``

          - ``\'default\'`` -- use ``flint``

          - ``\'flint\'`` -- let flint do the determinant

          - ``\'padic\'`` -- uses a `p`-adic / multimodular
            algorithm that relies on code in IML and linbox

          - ``\'linbox\'`` -- calls linbox det (you *must* set
            proof=False to use this!)

          - ``\'ntl\'`` -- calls NTL\'s det function

          - ``\'pari\'`` -- uses PARI

        - ``proof`` -- boolean or ``None``; if ``None`` use
          proof.linear_algebra(); only relevant for the padic algorithm

           .. NOTE::

              It would be *VERY VERY* hard for det to fail even with
              proof=False.

        - ``stabilize`` -- if proof is ``False``, require det to be the same
          for this many CRT primes in a row. Ignored if proof is ``True``.


        ALGORITHM: The `p`-adic algorithm works by first finding a random
        vector v, then solving `Ax = v` and taking the denominator
        `d`. This gives a divisor of the determinant. Then we
        compute `\\det(A)/d` using a multimodular algorithm and the
        Hadamard bound, skipping primes that divide `d`.

        EXAMPLES::

            sage: A = matrix(ZZ,8,8,[3..66])
            sage: A.determinant()
            0

        ::

            sage: A = random_matrix(ZZ,20,20)
            sage: D1 = A.determinant()
            sage: A._clear_cache()
            sage: D2 = A.determinant(algorithm=\'ntl\')
            sage: D1 == D2
            True

        We have a special-case algorithm for 4 x 4 determinants::

            sage: A = matrix(ZZ,4,[1,2,3,4,4,3,2,1,0,5,0,1,9,1,2,3])
            sage: A.determinant()
            270

        Next we try the Linbox det. Note that we must have proof=False.

        ::

            sage: A = matrix(ZZ,5,[1,2,3,4,5,4,6,3,2,1,7,9,7,5,2,1,4,6,7,8,3,2,4,6,7])
            sage: A.determinant(algorithm=\'linbox\')
            Traceback (most recent call last):
            ...
            RuntimeError: you must pass the proof=False option to the determinant command to use LinBox\'s det algorithm
            sage: A.determinant(algorithm=\'linbox\', proof=False)
            -21
            sage: A._clear_cache()
            sage: A.determinant()
            -21

        Try the other algorithms on the same example::

            sage: A._clear_cache(); A.determinant(algorithm=\'padic\')
            -21
            sage: A._clear_cache(); A.determinant(algorithm=\'pari\')
            -21
            sage: A._clear_cache(); A.determinant(algorithm=\'ntl\')
            -21
            sage: A._clear_cache(); A.determinant(algorithm=\'padic\')
            -21

        A bigger example::

            sage: A = random_matrix(ZZ,30)
            sage: d = A.determinant()
            sage: A._clear_cache()
            sage: A.determinant(algorithm=\'linbox\',proof=False) == d
            True

        TESTS:

        This shows that we can compute determinants for all sizes up to
        80. The check that the determinant of a squared matrix is a
        square is a sanity check that the result is probably correct::

            sage: for s in [1..80]:  # long time
            ....:     M = random_matrix(ZZ, s)
            ....:     d = (M*M).determinant()
            ....:     assert d.is_square()

        Check consistency::

            sage: all(matrix(ZZ, 0).det(algorithm=algo).is_one() for algo in [\'flint\', \'padic\', \'pari\', \'ntl\'])
            True
            sage: for _ in range(100):
            ....:     dim = randint(1, 10)
            ....:     m = random_matrix(ZZ, dim)
            ....:     det_flint = m.__copy__().det(algorithm=\'flint\')
            ....:     det_padic = m.__copy__().det(algorithm=\'padic\')
            ....:     det_pari = m.__copy__().det(algorithm=\'pari\')
            ....:     det_ntl = m.__copy__().det(algorithm=\'ntl\')
            ....:     if type(det_flint) is not Integer:
            ....:         raise RuntimeError("type(det_flint) = {}".format(type(det_flint)))
            ....:     if type(det_padic) is not Integer:
            ....:         raise RuntimeError("type(det_padic) = {}".format(type(det_padic)))
            ....:     if type(det_pari) is not Integer:
            ....:         raise RuntimeError("type(det_pari) = {}".format(type(det_pari)))
            ....:     if type(det_ntl) is not Integer:
            ....:         raise RuntimeError("type(det_ntl) = {}".format(type(det_ntl)))
            ....:     if det_flint != det_padic or det_flint != det_pari or det_flint != det_ntl:
            ....:         raise RuntimeError("ERROR\\ndet_flint = {}\\ndet_padic={}\\ndet_pari={}\\ndet_ntl={}\\n{}".format(
            ....:                           det_flint, det_padic, det_pari, det_ntl, self.str()))'''
    def echelon_form(self, algorithm=..., proof=..., include_zero_rows=..., transformation=..., D=...) -> Any:
        """Matrix_integer_dense.echelon_form(self, algorithm='default', proof=None, include_zero_rows=True, transformation=False, D=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1809)

        Return the echelon form of this matrix over the integers, also known
        as the hermite normal form (HNF).

        INPUT:

        - ``algorithm`` -- string; the algorithm to use. Valid options are:

          - ``'default'`` -- let Sage pick an algorithm (default).
            Up to 75 rows or columns with no transformation matrix,
            use pari with flag 0; otherwise, use flint.

          - ``'flint'`` -- use flint

          - ``'ntl'`` -- use NTL (only works for square matrices of
            full rank!)

          - ``'padic'`` -- an asymptotically fast `p`-adic modular
            algorithm, If your matrix has large coefficients and is
            small, you may also want to try this.

          - ``'pari'`` -- use PARI with flag 1

          - ``'pari0'`` -- use PARI with flag 0

          - ``'pari1'`` -- use PARI with flag 1

          - ``'pari4'`` -- use PARI with flag 4 (use heuristic LLL)

        - ``proof`` -- (default: ``True``) if proof=False certain
          determinants are computed using a randomized hybrid `p`-adic
          multimodular strategy until it stabilizes twice (instead of up to
          the Hadamard bound). It is *incredibly* unlikely that one would
          ever get an incorrect result with proof=False.

        - ``include_zero_rows`` -- boolean (default: ``True``); if ``False``,
          don't include zero rows

        - ``transformation`` -- if given, also compute
          transformation matrix; only valid for flint and padic algorithm

        - ``D`` -- (default: ``None``) if given and the algorithm
          is ``'ntl'``, then D must be a multiple of the determinant and this
          function will use that fact

        OUTPUT:

        The Hermite normal form (=echelon form over `\\ZZ`) of ``self`` as
        an immutable matrix.

        EXAMPLES::

            sage: A = MatrixSpace(ZZ,2)([1,2,3,4])
            sage: A.echelon_form()
            [1 0]
            [0 2]
            sage: A = MatrixSpace(ZZ,5)(range(25))
            sage: A.echelon_form()
            [  5   0  -5 -10 -15]
            [  0   1   2   3   4]
            [  0   0   0   0   0]
            [  0   0   0   0   0]
            [  0   0   0   0   0]

        Getting a transformation matrix in the nonsquare case::

            sage: A = matrix(ZZ,5,3,[1..15])
            sage: H, U = A.hermite_form(transformation=True, include_zero_rows=False)
            sage: H
            [1 2 3]
            [0 3 6]
            sage: U
            [  0   0   0   4  -3]
            [  0   0   0  13 -10]
            sage: U*A == H
            True

        TESTS:

        Make sure the zero matrices are handled correctly::

            sage: m = matrix(ZZ,3,3,[0]*9)
            sage: m.echelon_form()
            [0 0 0]
            [0 0 0]
            [0 0 0]
            sage: m = matrix(ZZ,3,1,[0]*3)
            sage: m.echelon_form()
            [0]
            [0]
            [0]
            sage: m = matrix(ZZ,1,3,[0]*3)
            sage: m.echelon_form()
            [0 0 0]

        The ultimate border case!

        ::

            sage: m = matrix(ZZ,0,0,[])
            sage: m.echelon_form()
            []

        .. NOTE::

           If 'ntl' is chosen for a non square matrix this function
           raises a :exc:`ValueError`.

        Special cases: 0 or 1 rows::

            sage: a = matrix(ZZ, 1,2,[0,-1])
            sage: a.hermite_form()
            [0 1]
            sage: a.pivots()
            (1,)
            sage: a = matrix(ZZ, 1,2,[0,0])
            sage: a.hermite_form()
            [0 0]
            sage: a.pivots()
            ()
            sage: a = matrix(ZZ,1,3); a
            [0 0 0]
            sage: a.echelon_form(include_zero_rows=False)
            []
            sage: a.echelon_form(include_zero_rows=True)
            [0 0 0]

        Illustrate using various algorithms.::

            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='pari')
            [1 2 3]
            [0 3 6]
            [0 0 0]
            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='pari0')
            [1 2 3]
            [0 3 6]
            [0 0 0]
            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='pari4')
            [1 2 3]
            [0 3 6]
            [0 0 0]
            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='padic')
            [1 2 3]
            [0 3 6]
            [0 0 0]
            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='default')
            [1 2 3]
            [0 3 6]
            [0 0 0]

        The 'ntl' algorithm doesn't work on matrices that do not have full rank.::

            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='ntl')
            Traceback (most recent call last):
            ...
            ValueError: ntl only computes HNF for square matrices of full rank.
            sage: matrix(ZZ,3,[0] +[2..9]).hermite_form(algorithm='ntl')
            [1 0 0]
            [0 1 0]
            [0 0 3]

        TESTS:

        This example illustrated :issue:`2398`::

            sage: a = matrix([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)])
            sage: a.hermite_form()
            [0 1 2]
            [0 0 3]
            [0 0 0]
            [0 0 0]

        Check that :issue:`12280` is fixed::

            sage: m = matrix([(-2, 1, 9, 2, -8, 1, -3, -1, -4, -1),
            ....:             (5, -2, 0, 1, 0, 4, -1, 1, -2, 0),
            ....:             (-11, 3, 1, 0, -3, -2, -1, -11, 2, -2),
            ....:             (-1, 1, -1, -2, 1, -1, -1, -1, -1, 7),
            ....:             (-2, -1, -1, 1, 1, -2, 1, 0, 2, -4)]).stack(
            ....:             200 * identity_matrix(ZZ, 10))
            sage: matrix(ZZ,m).hermite_form(algorithm='pari', include_zero_rows=False)
            [  1   0   2   0  13   5   1 166  72  69]
            [  0   1   1   0  20   4  15 195  65 190]
            [  0   0   4   0  24   5  23  22  51 123]
            [  0   0   0   1  23   7  20 105  60 151]
            [  0   0   0   0  40   4   0  80  36  68]
            [  0   0   0   0   0  10   0 100 190 170]
            [  0   0   0   0   0   0  25   0 100 150]
            [  0   0   0   0   0   0   0 200   0   0]
            [  0   0   0   0   0   0   0   0 200   0]
            [  0   0   0   0   0   0   0   0   0 200]
            sage: matrix(ZZ,m).hermite_form(algorithm='padic', include_zero_rows=False)
            [  1   0   2   0  13   5   1 166  72  69]
            [  0   1   1   0  20   4  15 195  65 190]
            [  0   0   4   0  24   5  23  22  51 123]
            [  0   0   0   1  23   7  20 105  60 151]
            [  0   0   0   0  40   4   0  80  36  68]
            [  0   0   0   0   0  10   0 100 190 170]
            [  0   0   0   0   0   0  25   0 100 150]
            [  0   0   0   0   0   0   0 200   0   0]
            [  0   0   0   0   0   0   0   0 200   0]
            [  0   0   0   0   0   0   0   0   0 200]

        Check that the output is correct in corner cases, see :issue:`18613`::

            sage: m = matrix(2, 0)
            sage: m.parent()
            Full MatrixSpace of 2 by 0 dense matrices over Integer Ring
            sage: H, U = m.echelon_form(transformation=True)
            sage: H.parent()
            Full MatrixSpace of 2 by 0 dense matrices over Integer Ring
            sage: H.is_immutable()
            True
            sage: U
            [1 0]
            [0 1]
            sage: H == U * m
            True
            sage: H, U = m.echelon_form(transformation=True,
            ....:                       include_zero_rows=False)
            sage: H.parent()
            Full MatrixSpace of 0 by 0 dense matrices over Integer Ring
            sage: U.parent()
            Full MatrixSpace of 0 by 2 dense matrices over Integer Ring
            sage: H == U * m
            True
            sage: m = random_matrix(ZZ, 15, 15, x=-1000, y=1000, density=0.1)
            sage: m.parent()
            Full MatrixSpace of 15 by 15 dense matrices over Integer Ring
            sage: H, U = m.hermite_form(algorithm='flint',
            ....:                       transformation=True)
            sage: H == U*m
            True"""
    @overload
    def elementary_divisors(self, algorithm=...) -> Any:
        """Matrix_integer_dense.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2316)

        Return the elementary divisors of self, in order.

        .. WARNING::

           This is MUCH faster than the :meth:`smith_form` function.

        The elementary divisors are the invariants of the finite abelian
        group that is the cokernel of *left* multiplication of this matrix.
        They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix

        - ``algorithm`` -- (default: ``'pari'``)

           - ``'pari'`` -- works robustly, but is slower.

           - ``'linbox'`` -- use linbox (currently off, broken)

        OUTPUT: list of integers


        .. NOTE::

           These are the invariants of the cokernel of *left* multiplication::

               sage: M = Matrix([[3,0,1],[0,1,0]])
               sage: M
               [3 0 1]
               [0 1 0]
               sage: M.elementary_divisors()
               [1, 1]
               sage: M.transpose().elementary_divisors()
               [1, 1, 0]

        EXAMPLES::

            sage: matrix(3, range(9)).elementary_divisors()
            [1, 3, 0]
            sage: matrix(3, range(9)).elementary_divisors(algorithm='pari')
            [1, 3, 0]
            sage: C = MatrixSpace(ZZ,4)([3,4,5,6,7,3,8,10,14,5,6,7,2,2,10,9])
            sage: C.elementary_divisors()
            [1, 1, 1, 687]

        ::

            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2])
            sage: M.elementary_divisors()
            [1, 1, 6]

        This returns a copy, which is safe to change::

            sage: edivs = M.elementary_divisors()
            sage: edivs.pop()
            6
            sage: M.elementary_divisors()
            [1, 1, 6]

        .. SEEALSO::

           :meth:`smith_form`"""
    @overload
    def elementary_divisors(self) -> Any:
        """Matrix_integer_dense.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2316)

        Return the elementary divisors of self, in order.

        .. WARNING::

           This is MUCH faster than the :meth:`smith_form` function.

        The elementary divisors are the invariants of the finite abelian
        group that is the cokernel of *left* multiplication of this matrix.
        They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix

        - ``algorithm`` -- (default: ``'pari'``)

           - ``'pari'`` -- works robustly, but is slower.

           - ``'linbox'`` -- use linbox (currently off, broken)

        OUTPUT: list of integers


        .. NOTE::

           These are the invariants of the cokernel of *left* multiplication::

               sage: M = Matrix([[3,0,1],[0,1,0]])
               sage: M
               [3 0 1]
               [0 1 0]
               sage: M.elementary_divisors()
               [1, 1]
               sage: M.transpose().elementary_divisors()
               [1, 1, 0]

        EXAMPLES::

            sage: matrix(3, range(9)).elementary_divisors()
            [1, 3, 0]
            sage: matrix(3, range(9)).elementary_divisors(algorithm='pari')
            [1, 3, 0]
            sage: C = MatrixSpace(ZZ,4)([3,4,5,6,7,3,8,10,14,5,6,7,2,2,10,9])
            sage: C.elementary_divisors()
            [1, 1, 1, 687]

        ::

            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2])
            sage: M.elementary_divisors()
            [1, 1, 6]

        This returns a copy, which is safe to change::

            sage: edivs = M.elementary_divisors()
            sage: edivs.pop()
            6
            sage: M.elementary_divisors()
            [1, 1, 6]

        .. SEEALSO::

           :meth:`smith_form`"""
    @overload
    def elementary_divisors(self) -> Any:
        """Matrix_integer_dense.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2316)

        Return the elementary divisors of self, in order.

        .. WARNING::

           This is MUCH faster than the :meth:`smith_form` function.

        The elementary divisors are the invariants of the finite abelian
        group that is the cokernel of *left* multiplication of this matrix.
        They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix

        - ``algorithm`` -- (default: ``'pari'``)

           - ``'pari'`` -- works robustly, but is slower.

           - ``'linbox'`` -- use linbox (currently off, broken)

        OUTPUT: list of integers


        .. NOTE::

           These are the invariants of the cokernel of *left* multiplication::

               sage: M = Matrix([[3,0,1],[0,1,0]])
               sage: M
               [3 0 1]
               [0 1 0]
               sage: M.elementary_divisors()
               [1, 1]
               sage: M.transpose().elementary_divisors()
               [1, 1, 0]

        EXAMPLES::

            sage: matrix(3, range(9)).elementary_divisors()
            [1, 3, 0]
            sage: matrix(3, range(9)).elementary_divisors(algorithm='pari')
            [1, 3, 0]
            sage: C = MatrixSpace(ZZ,4)([3,4,5,6,7,3,8,10,14,5,6,7,2,2,10,9])
            sage: C.elementary_divisors()
            [1, 1, 1, 687]

        ::

            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2])
            sage: M.elementary_divisors()
            [1, 1, 6]

        This returns a copy, which is safe to change::

            sage: edivs = M.elementary_divisors()
            sage: edivs.pop()
            6
            sage: M.elementary_divisors()
            [1, 1, 6]

        .. SEEALSO::

           :meth:`smith_form`"""
    @overload
    def elementary_divisors(self) -> Any:
        """Matrix_integer_dense.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2316)

        Return the elementary divisors of self, in order.

        .. WARNING::

           This is MUCH faster than the :meth:`smith_form` function.

        The elementary divisors are the invariants of the finite abelian
        group that is the cokernel of *left* multiplication of this matrix.
        They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix

        - ``algorithm`` -- (default: ``'pari'``)

           - ``'pari'`` -- works robustly, but is slower.

           - ``'linbox'`` -- use linbox (currently off, broken)

        OUTPUT: list of integers


        .. NOTE::

           These are the invariants of the cokernel of *left* multiplication::

               sage: M = Matrix([[3,0,1],[0,1,0]])
               sage: M
               [3 0 1]
               [0 1 0]
               sage: M.elementary_divisors()
               [1, 1]
               sage: M.transpose().elementary_divisors()
               [1, 1, 0]

        EXAMPLES::

            sage: matrix(3, range(9)).elementary_divisors()
            [1, 3, 0]
            sage: matrix(3, range(9)).elementary_divisors(algorithm='pari')
            [1, 3, 0]
            sage: C = MatrixSpace(ZZ,4)([3,4,5,6,7,3,8,10,14,5,6,7,2,2,10,9])
            sage: C.elementary_divisors()
            [1, 1, 1, 687]

        ::

            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2])
            sage: M.elementary_divisors()
            [1, 1, 6]

        This returns a copy, which is safe to change::

            sage: edivs = M.elementary_divisors()
            sage: edivs.pop()
            6
            sage: M.elementary_divisors()
            [1, 1, 6]

        .. SEEALSO::

           :meth:`smith_form`"""
    @overload
    def elementary_divisors(self, algorithm=...) -> Any:
        """Matrix_integer_dense.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2316)

        Return the elementary divisors of self, in order.

        .. WARNING::

           This is MUCH faster than the :meth:`smith_form` function.

        The elementary divisors are the invariants of the finite abelian
        group that is the cokernel of *left* multiplication of this matrix.
        They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix

        - ``algorithm`` -- (default: ``'pari'``)

           - ``'pari'`` -- works robustly, but is slower.

           - ``'linbox'`` -- use linbox (currently off, broken)

        OUTPUT: list of integers


        .. NOTE::

           These are the invariants of the cokernel of *left* multiplication::

               sage: M = Matrix([[3,0,1],[0,1,0]])
               sage: M
               [3 0 1]
               [0 1 0]
               sage: M.elementary_divisors()
               [1, 1]
               sage: M.transpose().elementary_divisors()
               [1, 1, 0]

        EXAMPLES::

            sage: matrix(3, range(9)).elementary_divisors()
            [1, 3, 0]
            sage: matrix(3, range(9)).elementary_divisors(algorithm='pari')
            [1, 3, 0]
            sage: C = MatrixSpace(ZZ,4)([3,4,5,6,7,3,8,10,14,5,6,7,2,2,10,9])
            sage: C.elementary_divisors()
            [1, 1, 1, 687]

        ::

            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2])
            sage: M.elementary_divisors()
            [1, 1, 6]

        This returns a copy, which is safe to change::

            sage: edivs = M.elementary_divisors()
            sage: edivs.pop()
            6
            sage: M.elementary_divisors()
            [1, 1, 6]

        .. SEEALSO::

           :meth:`smith_form`"""
    @overload
    def elementary_divisors(self) -> Any:
        """Matrix_integer_dense.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2316)

        Return the elementary divisors of self, in order.

        .. WARNING::

           This is MUCH faster than the :meth:`smith_form` function.

        The elementary divisors are the invariants of the finite abelian
        group that is the cokernel of *left* multiplication of this matrix.
        They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix

        - ``algorithm`` -- (default: ``'pari'``)

           - ``'pari'`` -- works robustly, but is slower.

           - ``'linbox'`` -- use linbox (currently off, broken)

        OUTPUT: list of integers


        .. NOTE::

           These are the invariants of the cokernel of *left* multiplication::

               sage: M = Matrix([[3,0,1],[0,1,0]])
               sage: M
               [3 0 1]
               [0 1 0]
               sage: M.elementary_divisors()
               [1, 1]
               sage: M.transpose().elementary_divisors()
               [1, 1, 0]

        EXAMPLES::

            sage: matrix(3, range(9)).elementary_divisors()
            [1, 3, 0]
            sage: matrix(3, range(9)).elementary_divisors(algorithm='pari')
            [1, 3, 0]
            sage: C = MatrixSpace(ZZ,4)([3,4,5,6,7,3,8,10,14,5,6,7,2,2,10,9])
            sage: C.elementary_divisors()
            [1, 1, 1, 687]

        ::

            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2])
            sage: M.elementary_divisors()
            [1, 1, 6]

        This returns a copy, which is safe to change::

            sage: edivs = M.elementary_divisors()
            sage: edivs.pop()
            6
            sage: M.elementary_divisors()
            [1, 1, 6]

        .. SEEALSO::

           :meth:`smith_form`"""
    @overload
    def elementary_divisors(self) -> Any:
        """Matrix_integer_dense.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2316)

        Return the elementary divisors of self, in order.

        .. WARNING::

           This is MUCH faster than the :meth:`smith_form` function.

        The elementary divisors are the invariants of the finite abelian
        group that is the cokernel of *left* multiplication of this matrix.
        They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix

        - ``algorithm`` -- (default: ``'pari'``)

           - ``'pari'`` -- works robustly, but is slower.

           - ``'linbox'`` -- use linbox (currently off, broken)

        OUTPUT: list of integers


        .. NOTE::

           These are the invariants of the cokernel of *left* multiplication::

               sage: M = Matrix([[3,0,1],[0,1,0]])
               sage: M
               [3 0 1]
               [0 1 0]
               sage: M.elementary_divisors()
               [1, 1]
               sage: M.transpose().elementary_divisors()
               [1, 1, 0]

        EXAMPLES::

            sage: matrix(3, range(9)).elementary_divisors()
            [1, 3, 0]
            sage: matrix(3, range(9)).elementary_divisors(algorithm='pari')
            [1, 3, 0]
            sage: C = MatrixSpace(ZZ,4)([3,4,5,6,7,3,8,10,14,5,6,7,2,2,10,9])
            sage: C.elementary_divisors()
            [1, 1, 1, 687]

        ::

            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2])
            sage: M.elementary_divisors()
            [1, 1, 6]

        This returns a copy, which is safe to change::

            sage: edivs = M.elementary_divisors()
            sage: edivs.pop()
            6
            sage: M.elementary_divisors()
            [1, 1, 6]

        .. SEEALSO::

           :meth:`smith_form`"""
    @overload
    def elementary_divisors(self) -> Any:
        """Matrix_integer_dense.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2316)

        Return the elementary divisors of self, in order.

        .. WARNING::

           This is MUCH faster than the :meth:`smith_form` function.

        The elementary divisors are the invariants of the finite abelian
        group that is the cokernel of *left* multiplication of this matrix.
        They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix

        - ``algorithm`` -- (default: ``'pari'``)

           - ``'pari'`` -- works robustly, but is slower.

           - ``'linbox'`` -- use linbox (currently off, broken)

        OUTPUT: list of integers


        .. NOTE::

           These are the invariants of the cokernel of *left* multiplication::

               sage: M = Matrix([[3,0,1],[0,1,0]])
               sage: M
               [3 0 1]
               [0 1 0]
               sage: M.elementary_divisors()
               [1, 1]
               sage: M.transpose().elementary_divisors()
               [1, 1, 0]

        EXAMPLES::

            sage: matrix(3, range(9)).elementary_divisors()
            [1, 3, 0]
            sage: matrix(3, range(9)).elementary_divisors(algorithm='pari')
            [1, 3, 0]
            sage: C = MatrixSpace(ZZ,4)([3,4,5,6,7,3,8,10,14,5,6,7,2,2,10,9])
            sage: C.elementary_divisors()
            [1, 1, 1, 687]

        ::

            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2])
            sage: M.elementary_divisors()
            [1, 1, 6]

        This returns a copy, which is safe to change::

            sage: edivs = M.elementary_divisors()
            sage: edivs.pop()
            6
            sage: M.elementary_divisors()
            [1, 1, 6]

        .. SEEALSO::

           :meth:`smith_form`"""
    @overload
    def elementary_divisors(self) -> Any:
        """Matrix_integer_dense.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2316)

        Return the elementary divisors of self, in order.

        .. WARNING::

           This is MUCH faster than the :meth:`smith_form` function.

        The elementary divisors are the invariants of the finite abelian
        group that is the cokernel of *left* multiplication of this matrix.
        They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix

        - ``algorithm`` -- (default: ``'pari'``)

           - ``'pari'`` -- works robustly, but is slower.

           - ``'linbox'`` -- use linbox (currently off, broken)

        OUTPUT: list of integers


        .. NOTE::

           These are the invariants of the cokernel of *left* multiplication::

               sage: M = Matrix([[3,0,1],[0,1,0]])
               sage: M
               [3 0 1]
               [0 1 0]
               sage: M.elementary_divisors()
               [1, 1]
               sage: M.transpose().elementary_divisors()
               [1, 1, 0]

        EXAMPLES::

            sage: matrix(3, range(9)).elementary_divisors()
            [1, 3, 0]
            sage: matrix(3, range(9)).elementary_divisors(algorithm='pari')
            [1, 3, 0]
            sage: C = MatrixSpace(ZZ,4)([3,4,5,6,7,3,8,10,14,5,6,7,2,2,10,9])
            sage: C.elementary_divisors()
            [1, 1, 1, 687]

        ::

            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2])
            sage: M.elementary_divisors()
            [1, 1, 6]

        This returns a copy, which is safe to change::

            sage: edivs = M.elementary_divisors()
            sage: edivs.pop()
            6
            sage: M.elementary_divisors()
            [1, 1, 6]

        .. SEEALSO::

           :meth:`smith_form`"""
    def frobenius(self, *args, **kwargs):
        """Deprecated: Use :meth:`frobenius_form` instead.
        See :issue:`36396` for details.

        """
    def frobenius_form(self, flag=..., var=...) -> Any:
        """Matrix_integer_dense.frobenius_form(self, flag=0, var='x')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2506)

        Return the Frobenius form (rational canonical form) of this
        matrix.

        INPUT:

        - ``flag`` -- 0 (default), 1 or 2 as follows:

            - ``0`` -- (default) return the Frobenius form of this
               matrix

            - ``1`` -- return only the elementary divisor
               polynomials, as polynomials in var

            - ``2`` -- return a two-components vector [F,B] where F
               is the Frobenius form and B is the basis change so that
               `M=B^{-1}FB`

        - ``var`` -- string (default: ``'x'``)

        ALGORITHM: uses PARI's :pari:`matfrobenius`

        EXAMPLES::

            sage: A = MatrixSpace(ZZ, 3)(range(9))
            sage: A.frobenius_form(0)
            [ 0  0  0]
            [ 1  0 18]
            [ 0  1 12]
            sage: A.frobenius_form(1)
            [x^3 - 12*x^2 - 18*x]
            sage: A.frobenius_form(1, var='y')
            [y^3 - 12*y^2 - 18*y]
            sage: F, B = A.frobenius_form(2)
            sage: A == B^(-1)*F*B
            True
            sage: a=matrix([])
            sage: a.frobenius_form(2)
            ([], [])
            sage: a.frobenius_form(0)
            []
            sage: a.frobenius_form(1)
            []
            sage: B = random_matrix(ZZ,2,3)
            sage: B.frobenius_form()
            Traceback (most recent call last):
            ...
            ArithmeticError: frobenius matrix of non-square matrix not defined.

        AUTHORS:

        - Martin Albrecht (2006-04-02)

        TODO: - move this to work for more general matrices than just over
        Z. This will require fixing how PARI polynomials are coerced to
        Sage polynomials."""
    @overload
    def gcd(self) -> Any:
        """Matrix_integer_dense.gcd(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5655)

        Return the gcd of all entries of self; very fast.

        EXAMPLES::

            sage: a = matrix(ZZ,2, [6,15,-6,150])
            sage: a.gcd()
            3"""
    @overload
    def gcd(self) -> Any:
        """Matrix_integer_dense.gcd(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5655)

        Return the gcd of all entries of self; very fast.

        EXAMPLES::

            sage: a = matrix(ZZ,2, [6,15,-6,150])
            sage: a.gcd()
            3"""
    @overload
    def height(self) -> Any:
        """Matrix_integer_dense.height(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1509)

        Return the height of this matrix, i.e., the max absolute value of
        the entries of the matrix.

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: a = Mat(ZZ,3)(range(9))
            sage: a.height()
            8
            sage: a = Mat(ZZ,2,3)([-17,3,-389,15,-1,0]); a
            [ -17    3 -389]
            [  15   -1    0]
            sage: a.height()
            389"""
    @overload
    def height(self) -> Any:
        """Matrix_integer_dense.height(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1509)

        Return the height of this matrix, i.e., the max absolute value of
        the entries of the matrix.

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: a = Mat(ZZ,3)(range(9))
            sage: a.height()
            8
            sage: a = Mat(ZZ,2,3)([-17,3,-389,15,-1,0]); a
            [ -17    3 -389]
            [  15   -1    0]
            sage: a.height()
            389"""
    @overload
    def height(self) -> Any:
        """Matrix_integer_dense.height(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1509)

        Return the height of this matrix, i.e., the max absolute value of
        the entries of the matrix.

        OUTPUT: nonnegative integer

        EXAMPLES::

            sage: a = Mat(ZZ,3)(range(9))
            sage: a.height()
            8
            sage: a = Mat(ZZ,2,3)([-17,3,-389,15,-1,0]); a
            [ -17    3 -389]
            [  15   -1    0]
            sage: a.height()
            389"""
    def hermite_form(self, *args, **kwargs):
        """Matrix_integer_dense.echelon_form(self, algorithm='default', proof=None, include_zero_rows=True, transformation=False, D=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1809)

        Return the echelon form of this matrix over the integers, also known
        as the hermite normal form (HNF).

        INPUT:

        - ``algorithm`` -- string; the algorithm to use. Valid options are:

          - ``'default'`` -- let Sage pick an algorithm (default).
            Up to 75 rows or columns with no transformation matrix,
            use pari with flag 0; otherwise, use flint.

          - ``'flint'`` -- use flint

          - ``'ntl'`` -- use NTL (only works for square matrices of
            full rank!)

          - ``'padic'`` -- an asymptotically fast `p`-adic modular
            algorithm, If your matrix has large coefficients and is
            small, you may also want to try this.

          - ``'pari'`` -- use PARI with flag 1

          - ``'pari0'`` -- use PARI with flag 0

          - ``'pari1'`` -- use PARI with flag 1

          - ``'pari4'`` -- use PARI with flag 4 (use heuristic LLL)

        - ``proof`` -- (default: ``True``) if proof=False certain
          determinants are computed using a randomized hybrid `p`-adic
          multimodular strategy until it stabilizes twice (instead of up to
          the Hadamard bound). It is *incredibly* unlikely that one would
          ever get an incorrect result with proof=False.

        - ``include_zero_rows`` -- boolean (default: ``True``); if ``False``,
          don't include zero rows

        - ``transformation`` -- if given, also compute
          transformation matrix; only valid for flint and padic algorithm

        - ``D`` -- (default: ``None``) if given and the algorithm
          is ``'ntl'``, then D must be a multiple of the determinant and this
          function will use that fact

        OUTPUT:

        The Hermite normal form (=echelon form over `\\ZZ`) of ``self`` as
        an immutable matrix.

        EXAMPLES::

            sage: A = MatrixSpace(ZZ,2)([1,2,3,4])
            sage: A.echelon_form()
            [1 0]
            [0 2]
            sage: A = MatrixSpace(ZZ,5)(range(25))
            sage: A.echelon_form()
            [  5   0  -5 -10 -15]
            [  0   1   2   3   4]
            [  0   0   0   0   0]
            [  0   0   0   0   0]
            [  0   0   0   0   0]

        Getting a transformation matrix in the nonsquare case::

            sage: A = matrix(ZZ,5,3,[1..15])
            sage: H, U = A.hermite_form(transformation=True, include_zero_rows=False)
            sage: H
            [1 2 3]
            [0 3 6]
            sage: U
            [  0   0   0   4  -3]
            [  0   0   0  13 -10]
            sage: U*A == H
            True

        TESTS:

        Make sure the zero matrices are handled correctly::

            sage: m = matrix(ZZ,3,3,[0]*9)
            sage: m.echelon_form()
            [0 0 0]
            [0 0 0]
            [0 0 0]
            sage: m = matrix(ZZ,3,1,[0]*3)
            sage: m.echelon_form()
            [0]
            [0]
            [0]
            sage: m = matrix(ZZ,1,3,[0]*3)
            sage: m.echelon_form()
            [0 0 0]

        The ultimate border case!

        ::

            sage: m = matrix(ZZ,0,0,[])
            sage: m.echelon_form()
            []

        .. NOTE::

           If 'ntl' is chosen for a non square matrix this function
           raises a :exc:`ValueError`.

        Special cases: 0 or 1 rows::

            sage: a = matrix(ZZ, 1,2,[0,-1])
            sage: a.hermite_form()
            [0 1]
            sage: a.pivots()
            (1,)
            sage: a = matrix(ZZ, 1,2,[0,0])
            sage: a.hermite_form()
            [0 0]
            sage: a.pivots()
            ()
            sage: a = matrix(ZZ,1,3); a
            [0 0 0]
            sage: a.echelon_form(include_zero_rows=False)
            []
            sage: a.echelon_form(include_zero_rows=True)
            [0 0 0]

        Illustrate using various algorithms.::

            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='pari')
            [1 2 3]
            [0 3 6]
            [0 0 0]
            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='pari0')
            [1 2 3]
            [0 3 6]
            [0 0 0]
            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='pari4')
            [1 2 3]
            [0 3 6]
            [0 0 0]
            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='padic')
            [1 2 3]
            [0 3 6]
            [0 0 0]
            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='default')
            [1 2 3]
            [0 3 6]
            [0 0 0]

        The 'ntl' algorithm doesn't work on matrices that do not have full rank.::

            sage: matrix(ZZ,3,[1..9]).hermite_form(algorithm='ntl')
            Traceback (most recent call last):
            ...
            ValueError: ntl only computes HNF for square matrices of full rank.
            sage: matrix(ZZ,3,[0] +[2..9]).hermite_form(algorithm='ntl')
            [1 0 0]
            [0 1 0]
            [0 0 3]

        TESTS:

        This example illustrated :issue:`2398`::

            sage: a = matrix([(0, 0, 3), (0, -2, 2), (0, 1, 2), (0, -2, 5)])
            sage: a.hermite_form()
            [0 1 2]
            [0 0 3]
            [0 0 0]
            [0 0 0]

        Check that :issue:`12280` is fixed::

            sage: m = matrix([(-2, 1, 9, 2, -8, 1, -3, -1, -4, -1),
            ....:             (5, -2, 0, 1, 0, 4, -1, 1, -2, 0),
            ....:             (-11, 3, 1, 0, -3, -2, -1, -11, 2, -2),
            ....:             (-1, 1, -1, -2, 1, -1, -1, -1, -1, 7),
            ....:             (-2, -1, -1, 1, 1, -2, 1, 0, 2, -4)]).stack(
            ....:             200 * identity_matrix(ZZ, 10))
            sage: matrix(ZZ,m).hermite_form(algorithm='pari', include_zero_rows=False)
            [  1   0   2   0  13   5   1 166  72  69]
            [  0   1   1   0  20   4  15 195  65 190]
            [  0   0   4   0  24   5  23  22  51 123]
            [  0   0   0   1  23   7  20 105  60 151]
            [  0   0   0   0  40   4   0  80  36  68]
            [  0   0   0   0   0  10   0 100 190 170]
            [  0   0   0   0   0   0  25   0 100 150]
            [  0   0   0   0   0   0   0 200   0   0]
            [  0   0   0   0   0   0   0   0 200   0]
            [  0   0   0   0   0   0   0   0   0 200]
            sage: matrix(ZZ,m).hermite_form(algorithm='padic', include_zero_rows=False)
            [  1   0   2   0  13   5   1 166  72  69]
            [  0   1   1   0  20   4  15 195  65 190]
            [  0   0   4   0  24   5  23  22  51 123]
            [  0   0   0   1  23   7  20 105  60 151]
            [  0   0   0   0  40   4   0  80  36  68]
            [  0   0   0   0   0  10   0 100 190 170]
            [  0   0   0   0   0   0  25   0 100 150]
            [  0   0   0   0   0   0   0 200   0   0]
            [  0   0   0   0   0   0   0   0 200   0]
            [  0   0   0   0   0   0   0   0   0 200]

        Check that the output is correct in corner cases, see :issue:`18613`::

            sage: m = matrix(2, 0)
            sage: m.parent()
            Full MatrixSpace of 2 by 0 dense matrices over Integer Ring
            sage: H, U = m.echelon_form(transformation=True)
            sage: H.parent()
            Full MatrixSpace of 2 by 0 dense matrices over Integer Ring
            sage: H.is_immutable()
            True
            sage: U
            [1 0]
            [0 1]
            sage: H == U * m
            True
            sage: H, U = m.echelon_form(transformation=True,
            ....:                       include_zero_rows=False)
            sage: H.parent()
            Full MatrixSpace of 0 by 0 dense matrices over Integer Ring
            sage: U.parent()
            Full MatrixSpace of 0 by 2 dense matrices over Integer Ring
            sage: H == U * m
            True
            sage: m = random_matrix(ZZ, 15, 15, x=-1000, y=1000, density=0.1)
            sage: m.parent()
            Full MatrixSpace of 15 by 15 dense matrices over Integer Ring
            sage: H, U = m.hermite_form(algorithm='flint',
            ....:                       transformation=True)
            sage: H == U*m
            True"""
    @overload
    def index_in_saturation(self, proof=...) -> Any:
        """Matrix_integer_dense.index_in_saturation(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2237)

        Return the index of ``self`` in its saturation.

        INPUT:

        - ``proof`` -- (default: use proof.linear_algebra());
          if ``False``, the determinant calculations are done with
          ``proof=False``

        OUTPUT: positive integer; the index of the row span of
        this matrix in its saturation


        ALGORITHM:

        Use Hermite normal form twice to find an invertible matrix whose
        inverse transforms a matrix with the same row span as ``self`` to its
        saturation, then compute the determinant of that matrix.

        EXAMPLES::

            sage: A = matrix(ZZ, 2,3, [1..6]); A
            [1 2 3]
            [4 5 6]
            sage: A.index_in_saturation()
            3
            sage: A.saturation()
            [1 2 3]
            [1 1 1]"""
    @overload
    def index_in_saturation(self) -> Any:
        """Matrix_integer_dense.index_in_saturation(self, proof=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2237)

        Return the index of ``self`` in its saturation.

        INPUT:

        - ``proof`` -- (default: use proof.linear_algebra());
          if ``False``, the determinant calculations are done with
          ``proof=False``

        OUTPUT: positive integer; the index of the row span of
        this matrix in its saturation


        ALGORITHM:

        Use Hermite normal form twice to find an invertible matrix whose
        inverse transforms a matrix with the same row span as ``self`` to its
        saturation, then compute the determinant of that matrix.

        EXAMPLES::

            sage: A = matrix(ZZ, 2,3, [1..6]); A
            [1 2 3]
            [4 5 6]
            sage: A.index_in_saturation()
            3
            sage: A.saturation()
            [1 2 3]
            [1 1 1]"""
    def insert_row(self, Py_ssize_tindex, row) -> Any:
        """Matrix_integer_dense.insert_row(self, Py_ssize_t index, row)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5483)

        Create a new matrix from ``self`` with.

        INPUT:

        - ``index`` -- integer

        - ``row`` -- a vector

        EXAMPLES::

            sage: X = matrix(ZZ,3,range(9)); X
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: X.insert_row(1, [1,5,-10])
            [  0   1   2]
            [  1   5 -10]
            [  3   4   5]
            [  6   7   8]
            sage: X.insert_row(0, [1,5,-10])
            [  1   5 -10]
            [  0   1   2]
            [  3   4   5]
            [  6   7   8]
            sage: X.insert_row(3, [1,5,-10])
            [  0   1   2]
            [  3   4   5]
            [  6   7   8]
            [  1   5 -10]

        TESTS:

        Ensure that :issue:`11328` is fixed::

            sage: m = matrix([[int(1),int(1)],[int(1),int(1)]])
            sage: m.insert_row(1,[int(2),int(3)])
            [1 1]
            [2 3]
            [1 1]"""
    def integer_valued_polynomials_generators(self) -> Any:
        """Matrix_integer_dense.integer_valued_polynomials_generators(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 6017)

        Determine the generators of the ring of integer valued polynomials on this
        matrix.

        OUTPUT:

        A pair ``(mu_B, P)`` where ``P`` is a list of polynomials in `\\QQ[X]`
        such that

        .. MATH::

           \\{f \\in \\QQ[X] \\mid f(B) \\in M_n(\\ZZ)\\}
               = \\mu_B \\QQ[X] + \\sum_{g\\in P} g \\ZZ[X]

        where `B` is this matrix.

        EXAMPLES::

            sage: B = matrix(ZZ, [[1, 0, 1], [1, -2, -1], [10, 0, 0]])
            sage: B.integer_valued_polynomials_generators()
            (x^3 + x^2 - 12*x - 20, [1, 1/4*x^2 + 3/4*x + 1/2])

        .. SEEALSO::

            :mod:`~sage.matrix.compute_J_ideal`,
            :meth:`~sage.matrix.compute_J_ideal.ComputeMinimalPolynomials.integer_valued_polynomials_generators`"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Matrix_integer_dense.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 4229)

        If ``self`` is a matrix with determinant `1` or `-1` return the inverse of
        ``self`` as a matrix over `ZZ`.

        EXAMPLES::

            sage: m = matrix(ZZ, 2, [2,1,1,1]).inverse_of_unit()
            sage: m
            [ 1 -1]
            [-1  2]
            sage: parent(m)
            Full MatrixSpace of 2 by 2 dense matrices over Integer Ring

            sage: matrix(2, [2,1,0,1]).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: non-invertible matrix"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Matrix_integer_dense.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 4229)

        If ``self`` is a matrix with determinant `1` or `-1` return the inverse of
        ``self`` as a matrix over `ZZ`.

        EXAMPLES::

            sage: m = matrix(ZZ, 2, [2,1,1,1]).inverse_of_unit()
            sage: m
            [ 1 -1]
            [-1  2]
            sage: parent(m)
            Full MatrixSpace of 2 by 2 dense matrices over Integer Ring

            sage: matrix(2, [2,1,0,1]).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: non-invertible matrix"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Matrix_integer_dense.inverse_of_unit(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 4229)

        If ``self`` is a matrix with determinant `1` or `-1` return the inverse of
        ``self`` as a matrix over `ZZ`.

        EXAMPLES::

            sage: m = matrix(ZZ, 2, [2,1,1,1]).inverse_of_unit()
            sage: m
            [ 1 -1]
            [-1  2]
            sage: parent(m)
            Full MatrixSpace of 2 by 2 dense matrices over Integer Ring

            sage: matrix(2, [2,1,0,1]).inverse_of_unit()
            Traceback (most recent call last):
            ...
            ArithmeticError: non-invertible matrix"""
    def is_LLL_reduced(self, delta=..., eta=..., algorithm=...) -> Any:
        """Matrix_integer_dense.is_LLL_reduced(self, delta=None, eta=None, algorithm='fpLLL')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 3386)

        Return ``True`` if this lattice is `(\\delta, \\eta)`-LLL reduced.
        See ``self.LLL`` for a definition of LLL reduction.

        INPUT:

        - ``delta`` -- (default: `0.99`) parameter `\\delta` as described above

        - ``eta`` -- (default: `0.501`) parameter `\\eta` as described above

        - ``algorithm`` -- either ``'fpLLL'`` (default) or ``'sage'``

        EXAMPLES::

            sage: A = random_matrix(ZZ, 10, 10)
            sage: L = A.LLL()
            sage: A.is_LLL_reduced()
            False
            sage: L.is_LLL_reduced()
            True

        The ``'sage'`` algorithm currently does not work for matrices with
        linearly dependent rows::

            sage: A = matrix(ZZ, [[1, 2, 3], [2, 4, 6]])
            sage: A.is_LLL_reduced(algorithm='sage')
            Traceback (most recent call last):
            ...
            ValueError: linearly dependent input for module version of Gram-Schmidt"""
    @overload
    def is_one(self) -> Any:
        """Matrix_integer_dense.is_one(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 742)

        Test whether ``self`` is the identity matrix.

        EXAMPLES::

            sage: matrix(2, [1,0,0,1]).is_one()
            True
            sage: matrix(2, [1,1,0,1]).is_one()
            False
            sage: matrix(2, 3, [1,0,0,0,1,0]).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """Matrix_integer_dense.is_one(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 742)

        Test whether ``self`` is the identity matrix.

        EXAMPLES::

            sage: matrix(2, [1,0,0,1]).is_one()
            True
            sage: matrix(2, [1,1,0,1]).is_one()
            False
            sage: matrix(2, 3, [1,0,0,0,1,0]).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """Matrix_integer_dense.is_one(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 742)

        Test whether ``self`` is the identity matrix.

        EXAMPLES::

            sage: matrix(2, [1,0,0,1]).is_one()
            True
            sage: matrix(2, [1,1,0,1]).is_one()
            False
            sage: matrix(2, 3, [1,0,0,0,1,0]).is_one()
            False"""
    @overload
    def is_one(self) -> Any:
        """Matrix_integer_dense.is_one(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 742)

        Test whether ``self`` is the identity matrix.

        EXAMPLES::

            sage: matrix(2, [1,0,0,1]).is_one()
            True
            sage: matrix(2, [1,1,0,1]).is_one()
            False
            sage: matrix(2, 3, [1,0,0,0,1,0]).is_one()
            False"""
    @overload
    def is_primitive(self) -> Any:
        """Matrix_integer_dense.is_primitive(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1145)

        Test whether the matrix is primitive.

        An integral matrix `A` is primitive if all its entries are nonnegative
        and for some positive integer `n` the matrix `A^n` has all its
        entries positive.

        EXAMPLES::

            sage: m = matrix(3, [1,1,0,0,0,1,1,0,0])
            sage: m.is_primitive()
            True
            sage: m**4
            [3 2 1]
            [1 1 1]
            [2 1 1]

            sage: m = matrix(4, [[1,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
            sage: m.is_primitive()
            True
            sage: m**6
            [4 3 2 1]
            [1 1 1 1]
            [2 1 1 1]
            [3 2 1 1]

            sage: m = matrix(4, [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
            sage: m.is_primitive()
            False

        Testing extremal matrices::

            sage: def matrix1(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = m[i+1,i] = 1
            ....:     return m
            sage: all(matrix1(d).is_primitive() for d in range(2,20))
            True

            sage: def matrix2(d):
            ....:     m = matrix(d)
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     m[d-1,0] = m[d-1,1] = 1
            ....:     return m
            sage: all(matrix2(d).is_primitive() for d in range(2,20))
            True

        Non-primitive families::

            sage: def matrix3(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     return m
            sage: any(matrix3(d).is_primitive() for d in range(2,20))
            False

        TESTS::

            sage: matrix(1, 2, [1,3]).is_primitive()
            Traceback (most recent call last):
            ...
            ValueError: not a square matrix"""
    @overload
    def is_primitive(self) -> Any:
        """Matrix_integer_dense.is_primitive(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1145)

        Test whether the matrix is primitive.

        An integral matrix `A` is primitive if all its entries are nonnegative
        and for some positive integer `n` the matrix `A^n` has all its
        entries positive.

        EXAMPLES::

            sage: m = matrix(3, [1,1,0,0,0,1,1,0,0])
            sage: m.is_primitive()
            True
            sage: m**4
            [3 2 1]
            [1 1 1]
            [2 1 1]

            sage: m = matrix(4, [[1,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
            sage: m.is_primitive()
            True
            sage: m**6
            [4 3 2 1]
            [1 1 1 1]
            [2 1 1 1]
            [3 2 1 1]

            sage: m = matrix(4, [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
            sage: m.is_primitive()
            False

        Testing extremal matrices::

            sage: def matrix1(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = m[i+1,i] = 1
            ....:     return m
            sage: all(matrix1(d).is_primitive() for d in range(2,20))
            True

            sage: def matrix2(d):
            ....:     m = matrix(d)
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     m[d-1,0] = m[d-1,1] = 1
            ....:     return m
            sage: all(matrix2(d).is_primitive() for d in range(2,20))
            True

        Non-primitive families::

            sage: def matrix3(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     return m
            sage: any(matrix3(d).is_primitive() for d in range(2,20))
            False

        TESTS::

            sage: matrix(1, 2, [1,3]).is_primitive()
            Traceback (most recent call last):
            ...
            ValueError: not a square matrix"""
    @overload
    def is_primitive(self) -> Any:
        """Matrix_integer_dense.is_primitive(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1145)

        Test whether the matrix is primitive.

        An integral matrix `A` is primitive if all its entries are nonnegative
        and for some positive integer `n` the matrix `A^n` has all its
        entries positive.

        EXAMPLES::

            sage: m = matrix(3, [1,1,0,0,0,1,1,0,0])
            sage: m.is_primitive()
            True
            sage: m**4
            [3 2 1]
            [1 1 1]
            [2 1 1]

            sage: m = matrix(4, [[1,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
            sage: m.is_primitive()
            True
            sage: m**6
            [4 3 2 1]
            [1 1 1 1]
            [2 1 1 1]
            [3 2 1 1]

            sage: m = matrix(4, [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
            sage: m.is_primitive()
            False

        Testing extremal matrices::

            sage: def matrix1(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = m[i+1,i] = 1
            ....:     return m
            sage: all(matrix1(d).is_primitive() for d in range(2,20))
            True

            sage: def matrix2(d):
            ....:     m = matrix(d)
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     m[d-1,0] = m[d-1,1] = 1
            ....:     return m
            sage: all(matrix2(d).is_primitive() for d in range(2,20))
            True

        Non-primitive families::

            sage: def matrix3(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     return m
            sage: any(matrix3(d).is_primitive() for d in range(2,20))
            False

        TESTS::

            sage: matrix(1, 2, [1,3]).is_primitive()
            Traceback (most recent call last):
            ...
            ValueError: not a square matrix"""
    @overload
    def is_primitive(self) -> Any:
        """Matrix_integer_dense.is_primitive(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1145)

        Test whether the matrix is primitive.

        An integral matrix `A` is primitive if all its entries are nonnegative
        and for some positive integer `n` the matrix `A^n` has all its
        entries positive.

        EXAMPLES::

            sage: m = matrix(3, [1,1,0,0,0,1,1,0,0])
            sage: m.is_primitive()
            True
            sage: m**4
            [3 2 1]
            [1 1 1]
            [2 1 1]

            sage: m = matrix(4, [[1,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
            sage: m.is_primitive()
            True
            sage: m**6
            [4 3 2 1]
            [1 1 1 1]
            [2 1 1 1]
            [3 2 1 1]

            sage: m = matrix(4, [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
            sage: m.is_primitive()
            False

        Testing extremal matrices::

            sage: def matrix1(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = m[i+1,i] = 1
            ....:     return m
            sage: all(matrix1(d).is_primitive() for d in range(2,20))
            True

            sage: def matrix2(d):
            ....:     m = matrix(d)
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     m[d-1,0] = m[d-1,1] = 1
            ....:     return m
            sage: all(matrix2(d).is_primitive() for d in range(2,20))
            True

        Non-primitive families::

            sage: def matrix3(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     return m
            sage: any(matrix3(d).is_primitive() for d in range(2,20))
            False

        TESTS::

            sage: matrix(1, 2, [1,3]).is_primitive()
            Traceback (most recent call last):
            ...
            ValueError: not a square matrix"""
    @overload
    def is_primitive(self) -> Any:
        """Matrix_integer_dense.is_primitive(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1145)

        Test whether the matrix is primitive.

        An integral matrix `A` is primitive if all its entries are nonnegative
        and for some positive integer `n` the matrix `A^n` has all its
        entries positive.

        EXAMPLES::

            sage: m = matrix(3, [1,1,0,0,0,1,1,0,0])
            sage: m.is_primitive()
            True
            sage: m**4
            [3 2 1]
            [1 1 1]
            [2 1 1]

            sage: m = matrix(4, [[1,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
            sage: m.is_primitive()
            True
            sage: m**6
            [4 3 2 1]
            [1 1 1 1]
            [2 1 1 1]
            [3 2 1 1]

            sage: m = matrix(4, [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
            sage: m.is_primitive()
            False

        Testing extremal matrices::

            sage: def matrix1(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = m[i+1,i] = 1
            ....:     return m
            sage: all(matrix1(d).is_primitive() for d in range(2,20))
            True

            sage: def matrix2(d):
            ....:     m = matrix(d)
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     m[d-1,0] = m[d-1,1] = 1
            ....:     return m
            sage: all(matrix2(d).is_primitive() for d in range(2,20))
            True

        Non-primitive families::

            sage: def matrix3(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     return m
            sage: any(matrix3(d).is_primitive() for d in range(2,20))
            False

        TESTS::

            sage: matrix(1, 2, [1,3]).is_primitive()
            Traceback (most recent call last):
            ...
            ValueError: not a square matrix"""
    @overload
    def is_primitive(self) -> Any:
        """Matrix_integer_dense.is_primitive(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1145)

        Test whether the matrix is primitive.

        An integral matrix `A` is primitive if all its entries are nonnegative
        and for some positive integer `n` the matrix `A^n` has all its
        entries positive.

        EXAMPLES::

            sage: m = matrix(3, [1,1,0,0,0,1,1,0,0])
            sage: m.is_primitive()
            True
            sage: m**4
            [3 2 1]
            [1 1 1]
            [2 1 1]

            sage: m = matrix(4, [[1,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
            sage: m.is_primitive()
            True
            sage: m**6
            [4 3 2 1]
            [1 1 1 1]
            [2 1 1 1]
            [3 2 1 1]

            sage: m = matrix(4, [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
            sage: m.is_primitive()
            False

        Testing extremal matrices::

            sage: def matrix1(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = m[i+1,i] = 1
            ....:     return m
            sage: all(matrix1(d).is_primitive() for d in range(2,20))
            True

            sage: def matrix2(d):
            ....:     m = matrix(d)
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     m[d-1,0] = m[d-1,1] = 1
            ....:     return m
            sage: all(matrix2(d).is_primitive() for d in range(2,20))
            True

        Non-primitive families::

            sage: def matrix3(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     return m
            sage: any(matrix3(d).is_primitive() for d in range(2,20))
            False

        TESTS::

            sage: matrix(1, 2, [1,3]).is_primitive()
            Traceback (most recent call last):
            ...
            ValueError: not a square matrix"""
    @overload
    def is_primitive(self) -> Any:
        """Matrix_integer_dense.is_primitive(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1145)

        Test whether the matrix is primitive.

        An integral matrix `A` is primitive if all its entries are nonnegative
        and for some positive integer `n` the matrix `A^n` has all its
        entries positive.

        EXAMPLES::

            sage: m = matrix(3, [1,1,0,0,0,1,1,0,0])
            sage: m.is_primitive()
            True
            sage: m**4
            [3 2 1]
            [1 1 1]
            [2 1 1]

            sage: m = matrix(4, [[1,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
            sage: m.is_primitive()
            True
            sage: m**6
            [4 3 2 1]
            [1 1 1 1]
            [2 1 1 1]
            [3 2 1 1]

            sage: m = matrix(4, [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
            sage: m.is_primitive()
            False

        Testing extremal matrices::

            sage: def matrix1(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = m[i+1,i] = 1
            ....:     return m
            sage: all(matrix1(d).is_primitive() for d in range(2,20))
            True

            sage: def matrix2(d):
            ....:     m = matrix(d)
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     m[d-1,0] = m[d-1,1] = 1
            ....:     return m
            sage: all(matrix2(d).is_primitive() for d in range(2,20))
            True

        Non-primitive families::

            sage: def matrix3(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     return m
            sage: any(matrix3(d).is_primitive() for d in range(2,20))
            False

        TESTS::

            sage: matrix(1, 2, [1,3]).is_primitive()
            Traceback (most recent call last):
            ...
            ValueError: not a square matrix"""
    @overload
    def is_primitive(self) -> Any:
        """Matrix_integer_dense.is_primitive(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1145)

        Test whether the matrix is primitive.

        An integral matrix `A` is primitive if all its entries are nonnegative
        and for some positive integer `n` the matrix `A^n` has all its
        entries positive.

        EXAMPLES::

            sage: m = matrix(3, [1,1,0,0,0,1,1,0,0])
            sage: m.is_primitive()
            True
            sage: m**4
            [3 2 1]
            [1 1 1]
            [2 1 1]

            sage: m = matrix(4, [[1,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
            sage: m.is_primitive()
            True
            sage: m**6
            [4 3 2 1]
            [1 1 1 1]
            [2 1 1 1]
            [3 2 1 1]

            sage: m = matrix(4, [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
            sage: m.is_primitive()
            False

        Testing extremal matrices::

            sage: def matrix1(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = m[i+1,i] = 1
            ....:     return m
            sage: all(matrix1(d).is_primitive() for d in range(2,20))
            True

            sage: def matrix2(d):
            ....:     m = matrix(d)
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     m[d-1,0] = m[d-1,1] = 1
            ....:     return m
            sage: all(matrix2(d).is_primitive() for d in range(2,20))
            True

        Non-primitive families::

            sage: def matrix3(d):
            ....:     m = matrix(d)
            ....:     m[0,0] = 1
            ....:     for i in range(d-1):
            ....:         m[i,i+1] = 1
            ....:     return m
            sage: any(matrix3(d).is_primitive() for d in range(2,20))
            False

        TESTS::

            sage: matrix(1, 2, [1,3]).is_primitive()
            Traceback (most recent call last):
            ...
            ValueError: not a square matrix"""
    @overload
    def minpoly(self, var=..., algorithm=...) -> Any:
        '''Matrix_integer_dense.minpoly(self, var=\'x\', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1426)

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- either ``\'linbox\'`` (default) or ``\'generic\'``

        EXAMPLES::

            sage: A = matrix(ZZ, 6, range(36))
            sage: A.minpoly()
            x^3 - 105*x^2 - 630*x

            sage: A = Mat(ZZ, 6)([k^2 for k in range(36)])
            sage: A.minpoly(algorithm=\'linbox\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x
            sage: A.minpoly(algorithm=\'generic\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x

        On non square matrices, this method raises an ArithmeticError::

            sage: matrix(ZZ, 2, 1).minpoly()
            Traceback (most recent call last):
            ...
            ArithmeticError: only valid for square matrix

        TESTS:

        Corner cases::

            sage: matrix([5]).minpoly(\'z\', \'linbox\')
            z - 5
            sage: matrix([5]).minpoly(\'z\', \'generic\')
            z - 5

            sage: matrix([]).minpoly(\'y\', \'linbox\')
            1
            sage: matrix([]).minpoly(\'y\', \'generic\')
            1

            sage: matrix(ZZ, 2).minpoly(\'x\', \'linbox\')
            x
            sage: matrix(ZZ, 2).minpoly(\'x\', \'generic\')
            x

        Consistency on random inputs::

            sage: for _ in range(100):
            ....:     dim = randint(1, 20)
            ....:     m  = random_matrix(ZZ, dim)
            ....:     m._clear_cache(); ans_generic = m.minpoly(algorithm=\'generic\')
            ....:     m._clear_cache(); ans_linbox = m.minpoly(algorithm=\'linbox\')
            ....:     if ans_generic != ans_linbox:
            ....:         raise RuntimeError("ans_generic = {} and ans_linbox = {} for\\n{}".format(
            ....:                            ans_generic, ans_linbox, m.str()))'''
    @overload
    def minpoly(self) -> Any:
        '''Matrix_integer_dense.minpoly(self, var=\'x\', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1426)

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- either ``\'linbox\'`` (default) or ``\'generic\'``

        EXAMPLES::

            sage: A = matrix(ZZ, 6, range(36))
            sage: A.minpoly()
            x^3 - 105*x^2 - 630*x

            sage: A = Mat(ZZ, 6)([k^2 for k in range(36)])
            sage: A.minpoly(algorithm=\'linbox\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x
            sage: A.minpoly(algorithm=\'generic\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x

        On non square matrices, this method raises an ArithmeticError::

            sage: matrix(ZZ, 2, 1).minpoly()
            Traceback (most recent call last):
            ...
            ArithmeticError: only valid for square matrix

        TESTS:

        Corner cases::

            sage: matrix([5]).minpoly(\'z\', \'linbox\')
            z - 5
            sage: matrix([5]).minpoly(\'z\', \'generic\')
            z - 5

            sage: matrix([]).minpoly(\'y\', \'linbox\')
            1
            sage: matrix([]).minpoly(\'y\', \'generic\')
            1

            sage: matrix(ZZ, 2).minpoly(\'x\', \'linbox\')
            x
            sage: matrix(ZZ, 2).minpoly(\'x\', \'generic\')
            x

        Consistency on random inputs::

            sage: for _ in range(100):
            ....:     dim = randint(1, 20)
            ....:     m  = random_matrix(ZZ, dim)
            ....:     m._clear_cache(); ans_generic = m.minpoly(algorithm=\'generic\')
            ....:     m._clear_cache(); ans_linbox = m.minpoly(algorithm=\'linbox\')
            ....:     if ans_generic != ans_linbox:
            ....:         raise RuntimeError("ans_generic = {} and ans_linbox = {} for\\n{}".format(
            ....:                            ans_generic, ans_linbox, m.str()))'''
    @overload
    def minpoly(self, algorithm=...) -> Any:
        '''Matrix_integer_dense.minpoly(self, var=\'x\', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1426)

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- either ``\'linbox\'`` (default) or ``\'generic\'``

        EXAMPLES::

            sage: A = matrix(ZZ, 6, range(36))
            sage: A.minpoly()
            x^3 - 105*x^2 - 630*x

            sage: A = Mat(ZZ, 6)([k^2 for k in range(36)])
            sage: A.minpoly(algorithm=\'linbox\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x
            sage: A.minpoly(algorithm=\'generic\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x

        On non square matrices, this method raises an ArithmeticError::

            sage: matrix(ZZ, 2, 1).minpoly()
            Traceback (most recent call last):
            ...
            ArithmeticError: only valid for square matrix

        TESTS:

        Corner cases::

            sage: matrix([5]).minpoly(\'z\', \'linbox\')
            z - 5
            sage: matrix([5]).minpoly(\'z\', \'generic\')
            z - 5

            sage: matrix([]).minpoly(\'y\', \'linbox\')
            1
            sage: matrix([]).minpoly(\'y\', \'generic\')
            1

            sage: matrix(ZZ, 2).minpoly(\'x\', \'linbox\')
            x
            sage: matrix(ZZ, 2).minpoly(\'x\', \'generic\')
            x

        Consistency on random inputs::

            sage: for _ in range(100):
            ....:     dim = randint(1, 20)
            ....:     m  = random_matrix(ZZ, dim)
            ....:     m._clear_cache(); ans_generic = m.minpoly(algorithm=\'generic\')
            ....:     m._clear_cache(); ans_linbox = m.minpoly(algorithm=\'linbox\')
            ....:     if ans_generic != ans_linbox:
            ....:         raise RuntimeError("ans_generic = {} and ans_linbox = {} for\\n{}".format(
            ....:                            ans_generic, ans_linbox, m.str()))'''
    @overload
    def minpoly(self, algorithm=...) -> Any:
        '''Matrix_integer_dense.minpoly(self, var=\'x\', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1426)

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- either ``\'linbox\'`` (default) or ``\'generic\'``

        EXAMPLES::

            sage: A = matrix(ZZ, 6, range(36))
            sage: A.minpoly()
            x^3 - 105*x^2 - 630*x

            sage: A = Mat(ZZ, 6)([k^2 for k in range(36)])
            sage: A.minpoly(algorithm=\'linbox\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x
            sage: A.minpoly(algorithm=\'generic\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x

        On non square matrices, this method raises an ArithmeticError::

            sage: matrix(ZZ, 2, 1).minpoly()
            Traceback (most recent call last):
            ...
            ArithmeticError: only valid for square matrix

        TESTS:

        Corner cases::

            sage: matrix([5]).minpoly(\'z\', \'linbox\')
            z - 5
            sage: matrix([5]).minpoly(\'z\', \'generic\')
            z - 5

            sage: matrix([]).minpoly(\'y\', \'linbox\')
            1
            sage: matrix([]).minpoly(\'y\', \'generic\')
            1

            sage: matrix(ZZ, 2).minpoly(\'x\', \'linbox\')
            x
            sage: matrix(ZZ, 2).minpoly(\'x\', \'generic\')
            x

        Consistency on random inputs::

            sage: for _ in range(100):
            ....:     dim = randint(1, 20)
            ....:     m  = random_matrix(ZZ, dim)
            ....:     m._clear_cache(); ans_generic = m.minpoly(algorithm=\'generic\')
            ....:     m._clear_cache(); ans_linbox = m.minpoly(algorithm=\'linbox\')
            ....:     if ans_generic != ans_linbox:
            ....:         raise RuntimeError("ans_generic = {} and ans_linbox = {} for\\n{}".format(
            ....:                            ans_generic, ans_linbox, m.str()))'''
    @overload
    def minpoly(self) -> Any:
        '''Matrix_integer_dense.minpoly(self, var=\'x\', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1426)

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- either ``\'linbox\'`` (default) or ``\'generic\'``

        EXAMPLES::

            sage: A = matrix(ZZ, 6, range(36))
            sage: A.minpoly()
            x^3 - 105*x^2 - 630*x

            sage: A = Mat(ZZ, 6)([k^2 for k in range(36)])
            sage: A.minpoly(algorithm=\'linbox\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x
            sage: A.minpoly(algorithm=\'generic\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x

        On non square matrices, this method raises an ArithmeticError::

            sage: matrix(ZZ, 2, 1).minpoly()
            Traceback (most recent call last):
            ...
            ArithmeticError: only valid for square matrix

        TESTS:

        Corner cases::

            sage: matrix([5]).minpoly(\'z\', \'linbox\')
            z - 5
            sage: matrix([5]).minpoly(\'z\', \'generic\')
            z - 5

            sage: matrix([]).minpoly(\'y\', \'linbox\')
            1
            sage: matrix([]).minpoly(\'y\', \'generic\')
            1

            sage: matrix(ZZ, 2).minpoly(\'x\', \'linbox\')
            x
            sage: matrix(ZZ, 2).minpoly(\'x\', \'generic\')
            x

        Consistency on random inputs::

            sage: for _ in range(100):
            ....:     dim = randint(1, 20)
            ....:     m  = random_matrix(ZZ, dim)
            ....:     m._clear_cache(); ans_generic = m.minpoly(algorithm=\'generic\')
            ....:     m._clear_cache(); ans_linbox = m.minpoly(algorithm=\'linbox\')
            ....:     if ans_generic != ans_linbox:
            ....:         raise RuntimeError("ans_generic = {} and ans_linbox = {} for\\n{}".format(
            ....:                            ans_generic, ans_linbox, m.str()))'''
    @overload
    def minpoly(self, algorithm=...) -> Any:
        '''Matrix_integer_dense.minpoly(self, var=\'x\', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1426)

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- either ``\'linbox\'`` (default) or ``\'generic\'``

        EXAMPLES::

            sage: A = matrix(ZZ, 6, range(36))
            sage: A.minpoly()
            x^3 - 105*x^2 - 630*x

            sage: A = Mat(ZZ, 6)([k^2 for k in range(36)])
            sage: A.minpoly(algorithm=\'linbox\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x
            sage: A.minpoly(algorithm=\'generic\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x

        On non square matrices, this method raises an ArithmeticError::

            sage: matrix(ZZ, 2, 1).minpoly()
            Traceback (most recent call last):
            ...
            ArithmeticError: only valid for square matrix

        TESTS:

        Corner cases::

            sage: matrix([5]).minpoly(\'z\', \'linbox\')
            z - 5
            sage: matrix([5]).minpoly(\'z\', \'generic\')
            z - 5

            sage: matrix([]).minpoly(\'y\', \'linbox\')
            1
            sage: matrix([]).minpoly(\'y\', \'generic\')
            1

            sage: matrix(ZZ, 2).minpoly(\'x\', \'linbox\')
            x
            sage: matrix(ZZ, 2).minpoly(\'x\', \'generic\')
            x

        Consistency on random inputs::

            sage: for _ in range(100):
            ....:     dim = randint(1, 20)
            ....:     m  = random_matrix(ZZ, dim)
            ....:     m._clear_cache(); ans_generic = m.minpoly(algorithm=\'generic\')
            ....:     m._clear_cache(); ans_linbox = m.minpoly(algorithm=\'linbox\')
            ....:     if ans_generic != ans_linbox:
            ....:         raise RuntimeError("ans_generic = {} and ans_linbox = {} for\\n{}".format(
            ....:                            ans_generic, ans_linbox, m.str()))'''
    @overload
    def minpoly(self, algorithm=...) -> Any:
        '''Matrix_integer_dense.minpoly(self, var=\'x\', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1426)

        INPUT:

        - ``var`` -- a variable name

        - ``algorithm`` -- either ``\'linbox\'`` (default) or ``\'generic\'``

        EXAMPLES::

            sage: A = matrix(ZZ, 6, range(36))
            sage: A.minpoly()
            x^3 - 105*x^2 - 630*x

            sage: A = Mat(ZZ, 6)([k^2 for k in range(36)])
            sage: A.minpoly(algorithm=\'linbox\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x
            sage: A.minpoly(algorithm=\'generic\')
            x^4 - 2695*x^3 - 257964*x^2 + 1693440*x

        On non square matrices, this method raises an ArithmeticError::

            sage: matrix(ZZ, 2, 1).minpoly()
            Traceback (most recent call last):
            ...
            ArithmeticError: only valid for square matrix

        TESTS:

        Corner cases::

            sage: matrix([5]).minpoly(\'z\', \'linbox\')
            z - 5
            sage: matrix([5]).minpoly(\'z\', \'generic\')
            z - 5

            sage: matrix([]).minpoly(\'y\', \'linbox\')
            1
            sage: matrix([]).minpoly(\'y\', \'generic\')
            1

            sage: matrix(ZZ, 2).minpoly(\'x\', \'linbox\')
            x
            sage: matrix(ZZ, 2).minpoly(\'x\', \'generic\')
            x

        Consistency on random inputs::

            sage: for _ in range(100):
            ....:     dim = randint(1, 20)
            ....:     m  = random_matrix(ZZ, dim)
            ....:     m._clear_cache(); ans_generic = m.minpoly(algorithm=\'generic\')
            ....:     m._clear_cache(); ans_linbox = m.minpoly(algorithm=\'linbox\')
            ....:     if ans_generic != ans_linbox:
            ....:         raise RuntimeError("ans_generic = {} and ans_linbox = {} for\\n{}".format(
            ....:                            ans_generic, ans_linbox, m.str()))'''
    def null_ideal(self, b=...) -> Any:
        """Matrix_integer_dense.null_ideal(self, b=0)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5979)

        Return the `(b)`-ideal of this matrix.

        Let `B` be a `n \\times n` matrix. The *null ideal* modulo `b`,
        or `(b)`-ideal, is

        .. MATH::

            N_{(b)}(B) = \\{f \\in \\ZZ[X] \\mid f(B) \\in M_n(b\\ZZ)\\}.

        INPUT:

        - ``b`` -- an element of `\\ZZ` (default: 0)

        OUTPUT: an ideal in `\\ZZ[X]`

        EXAMPLES::

            sage: B = matrix(ZZ, [[1, 0, 1], [1, -2, -1], [10, 0, 0]])
            sage: B.null_ideal()
            Principal ideal (x^3 + x^2 - 12*x - 20) of
                Univariate Polynomial Ring in x over Integer Ring
            sage: B.null_ideal(8)
            Ideal (8, x^3 + x^2 - 12*x - 20, 2*x^2 + 6*x + 4) of
                Univariate Polynomial Ring in x over Integer Ring
            sage: B.null_ideal(6)
            Ideal (6, 2*x^3 + 2*x^2 - 24*x - 40, 3*x^2 + 3*x) of
                Univariate Polynomial Ring in x over Integer Ring

        .. SEEALSO::

            :mod:`~sage.matrix.compute_J_ideal`,
            :meth:`~sage.matrix.compute_J_ideal.ComputeMinimalPolynomials.null_ideal`"""
    def p_minimal_polynomials(self, p, s_max=...) -> Any:
        """Matrix_integer_dense.p_minimal_polynomials(self, p, s_max=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5926)

        Compute `(p^s)`-minimal polynomials `\\nu_s` of this matrix.

        For `s  \\ge 0`, a `(p^s)`-minimal polynomial of
        a matrix `B` is a monic polynomial `f \\in \\ZZ[X]` of
        minimal degree such that all entries of `f(B)` are divisible
        by `p^s`.

        Compute a finite subset `\\mathcal{S}` of the positive
        integers and `(p^s)`-minimal polynomials
        `\\nu_s` for `s \\in \\mathcal{S}`.

        For `0 < t \\le \\max \\mathcal{S}`, a `(p^t)`-minimal polynomial is
        given by `\\nu_s` where
        `s = \\min\\{ r \\in \\mathcal{S} \\mid r\\ge t \\}`.
        For `t > \\max\\mathcal{S}`, the minimal polynomial of `B` is
        also a `(p^t)`-minimal polynomial.

        INPUT:

        - ``p`` -- a prime in `\\ZZ`

        - ``s_max`` -- positive integer (default: ``None``); if set, only
          `(p^s)`-minimal polynomials for ``s <= s_max`` are computed
          (see below for details)

        OUTPUT:

        A dictionary. Keys are the finite set `\\mathcal{S}`, the
        values are the associated `(p^s)`-minimal polynomials `\\nu_s`,
        `s\\in\\mathcal{S}`.

        Setting ``s_max`` only affects the output if ``s_max`` is at
        most `\\max\\mathcal{S}` where `\\mathcal{S}` denotes the full
        set. In that case, only those `\\nu_s` with ``s <= s_max`` are
        returned where ``s_max`` is always included even if it is not
        included in the full set `\\mathcal{S}`.

        EXAMPLES::

            sage: B = matrix(ZZ, [[1, 0, 1], [1, -2, -1], [10, 0, 0]])
            sage: B.p_minimal_polynomials(2)
            {2: x^2 + 3*x + 2}

        .. SEEALSO::

            :mod:`~sage.matrix.compute_J_ideal`,
            :meth:`~sage.matrix.compute_J_ideal.ComputeMinimalPolynomials.p_minimal_polynomials`"""
    @overload
    def pivots(self) -> Any:
        """Matrix_integer_dense.pivots(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2272)

        Return the pivot column positions of this matrix.

        OUTPUT: a tuple of Python integers: the position of the
        first nonzero entry in each row of the echelon form.

        EXAMPLES::

            sage: n = 3; A = matrix(ZZ,n,range(n^2)); A
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: A.pivots()
            (0, 1)
            sage: A.echelon_form()
            [ 3  0 -3]
            [ 0  1  2]
            [ 0  0  0]"""
    @overload
    def pivots(self) -> Any:
        """Matrix_integer_dense.pivots(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2272)

        Return the pivot column positions of this matrix.

        OUTPUT: a tuple of Python integers: the position of the
        first nonzero entry in each row of the echelon form.

        EXAMPLES::

            sage: n = 3; A = matrix(ZZ,n,range(n^2)); A
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: A.pivots()
            (0, 1)
            sage: A.echelon_form()
            [ 3  0 -3]
            [ 0  1  2]
            [ 0  0  0]"""
    def prod_of_row_sums(self, cols) -> Any:
        """Matrix_integer_dense.prod_of_row_sums(self, cols)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 3452)

        Return the product of the sums of the entries in the submatrix of
        ``self`` with given columns.

        INPUT:

        - ``cols`` -- list (or set) of integers representing columns
          of ``self``

        OUTPUT: integer

        EXAMPLES::

            sage: a = matrix(ZZ,2,3,[1..6]); a
            [1 2 3]
            [4 5 6]
            sage: a.prod_of_row_sums([0,2])
            40
            sage: (1+3)*(4+6)
            40
            sage: a.prod_of_row_sums(set([0,2]))
            40"""
    def randomize(self, density=..., x=..., y=..., distribution=..., nonzero=...) -> Any:
        """Matrix_integer_dense.randomize(self, density=1, x=None, y=None, distribution=None, nonzero=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 3543)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        The parameters are the same as the ones for the integer ring's
        ``random_element`` function.

        If ``x`` and ``y`` are given, randomized entries of this matrix have
        to be between ``x`` and ``y`` and have density 1.

        INPUT:

        - ``self`` -- a mutable matrix over ZZ

        - ``density`` -- a float between 0 and 1

        - ``x``, ``y`` -- if not ``None``, these are passed to the
           ``ZZ.random_element`` function as the upper and lower endpoints in
           the  uniform distribution

        - ``distribution`` -- would also be passed into ``ZZ.random_element``
          if given

        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are guaranteed to be zero

        OUTPUT: None, the matrix is modified in-place

        EXAMPLES::

            sage: A = matrix(ZZ, 2,3, [1..6])
            sage: ranks = [True, True, True]
            sage: while any(ranks):
            ....:    A.randomize()
            ....:    ranks[A.rank()] = False

            sage: mini = 0
            sage: maxi = 0
            sage: while mini != -30 and maxi != 30:
            ....:     A.randomize(x=-30, y=30)
            ....:     mini = min(min(A.list()), mini)
            ....:     maxi = min(min(A.list()), maxi)"""
    def rank(self, algorithm=...) -> Any:
        """Matrix_integer_dense.rank(self, algorithm='modp')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 3653)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- either ``'modp'`` (default) or ``'flint'``
          or ``'linbox'``

        OUTPUT: nonnegative integer -- the rank

        .. NOTE::

            The rank is cached.

        ALGORITHM:

        If set to ``'modp'``, first check if the matrix has maximum
        possible rank by working modulo one random prime. If not, call
        LinBox's rank function.

        EXAMPLES::

            sage: a = matrix(ZZ,2,3,[1..6]); a
            [1 2 3]
            [4 5 6]
            sage: a.rank()
            2
            sage: a = matrix(ZZ,3,3,[1..9]); a
            [1 2 3]
            [4 5 6]
            [7 8 9]
            sage: a.rank()
            2

        Here is a bigger example - the rank is of course still 2::

            sage: a = matrix(ZZ,100,[1..100^2]); a.rank()
            2

        TESTS::

            sage: a.rank(algorithm='funky')
            Traceback (most recent call last):
            ...
            ValueError: algorithm must be one of 'modp', 'flint' or 'linbox'"""
    def rational_reconstruction(self, N) -> Any:
        """Matrix_integer_dense.rational_reconstruction(self, N)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 3496)

        Use rational reconstruction to lift ``self`` to a matrix over the
        rational numbers (if possible), where we view ``self`` as a matrix
        modulo N.

        INPUT:

        - ``N`` -- integer

        OUTPUT: matrix over `\\QQ` or raise a :exc:`ValueError`

        EXAMPLES: We create a random 4x4 matrix over ZZ.

        ::

            sage: A = matrix(ZZ, 4, [4, -4, 7, 1, -1, 1, -1, -12, -1, -1, 1, -1, -3, 1, 5, -1])

        There isn't a unique rational reconstruction of it::

            sage: A.rational_reconstruction(11)
            Traceback (most recent call last):
            ...
            ValueError: rational reconstruction does not exist

        We throw in a denominator and reduce the matrix modulo 389 - it
        does rationally reconstruct.

        ::

            sage: B = (A/3 % 389).change_ring(ZZ)
            sage: B.rational_reconstruction(389) == A/3
            True

        TESTS:

        Check that :issue:`9345` is fixed::

            sage: A = random_matrix(ZZ, 3, 3)
            sage: A.rational_reconstruction(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: The modulus cannot be zero"""
    def row(self, Py_ssize_ti, from_list=...) -> Any:
        """Matrix_integer_dense.row(self, Py_ssize_t i, from_list=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5256)

        Return the `i`-th row of this matrix as a dense vector.

        INPUT:

        - ``i`` -- integer

        - ``from_list`` -- ignored

        EXAMPLES::

            sage: m = matrix(ZZ, 2, [1, -2, 3, 4])
            sage: m.row(0)
            (1, -2)
            sage: m.row(1)
            (3, 4)
            sage: m.row(1, from_list=True)
            (3, 4)
            sage: m.row(-2)
            (1, -2)

            sage: m.row(2)
            Traceback (most recent call last):
            ...
            IndexError: row index out of range
            sage: m.row(-3)
            Traceback (most recent call last):
            ...
            IndexError: row index out of range"""
    def saturation(self, p=..., proof=..., max_dets=...) -> Any:
        """Matrix_integer_dense.saturation(self, p=0, proof=None, max_dets=5)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2157)

        Return a saturation matrix of self, which is a matrix whose rows
        span the saturation of the row span of ``self``. This is not unique.

        The saturation of a `\\ZZ` module `M`
        embedded in `\\ZZ^n` is a module `S` that
        contains `M` with finite index such that
        `\\ZZ^n/S` is torsion free. This function takes the
        row span `M` of self, and finds another matrix of full rank
        with row span the saturation of `M`.

        INPUT:

        - ``p`` -- (default: 0) if nonzero given, saturate
          only at the prime `p`, i.e., return a matrix whose row span
          is a `\\ZZ`-module `S` that contains ``self`` and
          such that the index of `S` in its saturation is coprime to
          `p`. If `p` is None, return full saturation of ``self``.

        - ``proof`` -- (default: use proof.linear_algebra());
          if ``False``, the determinant calculations are done with
          ``proof=False``

        - ``max_dets`` -- (default: 5) technical parameter -
          max number of determinant to compute when bounding prime divisor of
          ``self`` in its saturation.

        OUTPUT: matrix over ZZ


        .. NOTE::

           The result is *not* cached.

        ALGORITHM: 1. Replace input by a matrix of full rank got from a
        subset of the rows. 2. Divide out any common factors from rows. 3.
        Check max_dets random dets of submatrices to see if their GCD
        (with p) is 1 - if so matrix is saturated and we're done. 4.
        Finally, use that if A is a matrix of full rank, then
        `hnf(transpose(A))^{-1}*A` is a saturation of A.

        EXAMPLES::

            sage: A = matrix(ZZ, 3, 5, [-51, -1509, -71, -109, -593, -19, -341, 4, 86, 98, 0, -246, -11, 65, 217])
            sage: A.echelon_form()
            [      1       5    2262   20364   56576]
            [      0       6   35653  320873  891313]
            [      0       0   42993  386937 1074825]
            sage: S = A.saturation(); S
            [  -51 -1509   -71  -109  -593]
            [  -19  -341     4    86    98]
            [   35   994    43    51   347]

        Notice that the saturation spans a different module than A.

        ::

            sage: S.echelon_form()
            [ 1  2  0  8 32]
            [ 0  3  0 -2 -6]
            [ 0  0  1  9 25]
            sage: V = A.row_space(); W = S.row_space()
            sage: V.is_submodule(W)
            True
            sage: V.index_in(W)
            85986
            sage: V.index_in_saturation()
            85986

        We illustrate each option::

            sage: S = A.saturation(p=2)
            sage: S = A.saturation(proof=False)
            sage: S = A.saturation(max_dets=2)"""
    def smith_form(self, transformation=..., integral=...) -> Any:
        """Matrix_integer_dense.smith_form(self, transformation=True, integral=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 2401)

        Return the smith normal form of this matrix, that is the diagonal
        matrix `S` with diagonal entries the ordered elementary divisors of
        this matrix.

        INPUT:

        - ``transformation`` -- boolean (default: ``True``); whether to
          return the transformation matrices `U` and `V` such that `S=U\\cdot
          self\\cdot V`

        - ``integral`` -- a subring of the base ring or ``True`` (default:
          ``None``); ignored for matrices with integer entries

        .. NOTE::

           The :meth:`elementary_divisors` function, which returns the diagonal
           entries of `S`, is VASTLY faster than this function.

        The elementary divisors are the invariants of the finite abelian
        group that is the cokernel of this matrix. They are ordered in
        reverse by divisibility.

        EXAMPLES::

            sage: A = MatrixSpace(IntegerRing(), 3)(range(9))
            sage: D, U, V = A.smith_form()
            sage: D
            [1 0 0]
            [0 3 0]
            [0 0 0]
            sage: U
            [ 0  2 -1]
            [ 0 -1  1]
            [ 1 -2  1]
            sage: V
            [ 0  0  1]
            [-1  2 -2]
            [ 1 -1  1]
            sage: U*A*V
            [1 0 0]
            [0 3 0]
            [0 0 0]

        It also makes sense for nonsquare matrices::

            sage: A = Matrix(ZZ,3,2,range(6))
            sage: D, U, V = A.smith_form()
            sage: D
            [1 0]
            [0 2]
            [0 0]
            sage: U
            [ 0  2 -1]
            [ 0 -1  1]
            [ 1 -2  1]
            sage: V
            [-1  1]
            [ 1  0]
            sage: U * A * V
            [1 0]
            [0 2]
            [0 0]

        Empty matrices are handled sensibly (see :issue:`3068`)::

            sage: m = MatrixSpace(ZZ, 2,0)(0); d,u,v = m.smith_form(); u*m*v == d
            True
            sage: m = MatrixSpace(ZZ, 0,2)(0); d,u,v = m.smith_form(); u*m*v == d
            True
            sage: m = MatrixSpace(ZZ, 0,0)(0); d,u,v = m.smith_form(); u*m*v == d
            True

        .. SEEALSO::

           :meth:`elementary_divisors`"""
    def symplectic_form(self) -> Any:
        """Matrix_integer_dense.symplectic_form(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1745)

        Find a symplectic basis for ``self`` if ``self`` is an anti-symmetric,
        alternating matrix.

        Return a pair (F, C) such that the rows of C form a symplectic
        basis for ``self`` and ``F = C * self * C.transpose()``.

        Raise a :exc:`ValueError` if ``self`` is not anti-symmetric,
        or ``self`` is not alternating.

        Anti-symmetric means that `M = -M^t`. Alternating means
        that the diagonal of `M` is identically zero.

        A symplectic basis is a basis of the form
        `e_1, \\ldots, e_j, f_1, \\ldots f_j, z_1, \\dots, z_k`
        such that

        -  `z_i M v^t = 0` for all vectors `v`

        -  `e_i M {e_j}^t = 0` for all `i, j`

        -  `f_i M {f_j}^t = 0` for all `i, j`

        -  `e_i M {f_i}^t = 1` for all `i`

        -  `e_i M {f_j}^t = 0` for all `i` not equal
            `j`.

        The ordering for the factors `d_{i} | d_{i+1}` and for
        the placement of zeroes was chosen to agree with the output of
        :meth:`smith_form`.

        See the example for a pictorial description of such a basis.

        EXAMPLES::

            sage: E = matrix(ZZ, 5, 5, [0, 14, 0, -8, -2, -14, 0, -3, -11, 4, 0, 3, 0, 0, 0, 8, 11, 0, 0, 8, 2, -4, 0, -8, 0]); E
            [  0  14   0  -8  -2]
            [-14   0  -3 -11   4]
            [  0   3   0   0   0]
            [  8  11   0   0   8]
            [  2  -4   0  -8   0]
            sage: F, C = E.symplectic_form()
            sage: F
            [ 0  0  1  0  0]
            [ 0  0  0  2  0]
            [-1  0  0  0  0]
            [ 0 -2  0  0  0]
            [ 0  0  0  0  0]
            sage: F == C * E * C.transpose()
            True
            sage: E.smith_form()[0]
            [1 0 0 0 0]
            [0 1 0 0 0]
            [0 0 2 0 0]
            [0 0 0 2 0]
            [0 0 0 0 0]"""
    @overload
    def transpose(self) -> Any:
        """Matrix_integer_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5728)

        Return the transpose of self, without changing ``self``.

        EXAMPLES:

        We create a matrix, compute its transpose, and note that the
        original matrix is not changed.

        ::

            sage: A = matrix(ZZ, 2, 3, range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
            sage: B = A.transpose()
            sage: print(B)
            [0 3]
            [1 4]
            [2 5]
            sage: print(A)
            [0 1 2]
            [3 4 5]

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [0 3]
            [1 4]
            [2 5]

        ::

            sage: A.subdivide(None, 1); A
            [0|1 2]
            [3|4 5]
            sage: A.transpose()
            [0 3]
            [---]
            [1 4]
            [2 5]"""
    @overload
    def transpose(self) -> Any:
        """Matrix_integer_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5728)

        Return the transpose of self, without changing ``self``.

        EXAMPLES:

        We create a matrix, compute its transpose, and note that the
        original matrix is not changed.

        ::

            sage: A = matrix(ZZ, 2, 3, range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
            sage: B = A.transpose()
            sage: print(B)
            [0 3]
            [1 4]
            [2 5]
            sage: print(A)
            [0 1 2]
            [3 4 5]

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [0 3]
            [1 4]
            [2 5]

        ::

            sage: A.subdivide(None, 1); A
            [0|1 2]
            [3|4 5]
            sage: A.transpose()
            [0 3]
            [---]
            [1 4]
            [2 5]"""
    @overload
    def transpose(self) -> Any:
        """Matrix_integer_dense.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5728)

        Return the transpose of self, without changing ``self``.

        EXAMPLES:

        We create a matrix, compute its transpose, and note that the
        original matrix is not changed.

        ::

            sage: A = matrix(ZZ, 2, 3, range(6))
            sage: type(A)
            <class 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
            sage: B = A.transpose()
            sage: print(B)
            [0 3]
            [1 4]
            [2 5]
            sage: print(A)
            [0 1 2]
            [3 4 5]

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [0 3]
            [1 4]
            [2 5]

        ::

            sage: A.subdivide(None, 1); A
            [0|1 2]
            [3|4 5]
            sage: A.transpose()
            [0 3]
            [---]
            [1 4]
            [2 5]"""
    def __bool__(self) -> bool:
        """True if self else False"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_integer_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 683)

        Return a new copy of this matrix.

        EXAMPLES::

            sage: a = matrix(ZZ,1,3, [1,2,-3]); a
            [ 1  2 -3]
            sage: b = a.__copy__(); b
            [ 1  2 -3]
            sage: b is a
            False
            sage: b == a
            True

            sage: M = MatrixSpace(ZZ,2,3)
            sage: m = M([1,2,3,3,2,1])
            sage: mc = m.__copy__()
            sage: mc == m and mc is not m
            True"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_integer_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 683)

        Return a new copy of this matrix.

        EXAMPLES::

            sage: a = matrix(ZZ,1,3, [1,2,-3]); a
            [ 1  2 -3]
            sage: b = a.__copy__(); b
            [ 1  2 -3]
            sage: b is a
            False
            sage: b == a
            True

            sage: M = MatrixSpace(ZZ,2,3)
            sage: m = M([1,2,3,3,2,1])
            sage: mc = m.__copy__()
            sage: mc == m and mc is not m
            True"""
    @overload
    def __copy__(self) -> Any:
        """Matrix_integer_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 683)

        Return a new copy of this matrix.

        EXAMPLES::

            sage: a = matrix(ZZ,1,3, [1,2,-3]); a
            [ 1  2 -3]
            sage: b = a.__copy__(); b
            [ 1  2 -3]
            sage: b is a
            False
            sage: b == a
            True

            sage: M = MatrixSpace(ZZ,2,3)
            sage: m = M([1,2,3,3,2,1])
            sage: mc = m.__copy__()
            sage: mc == m and mc is not m
            True"""
    def __invert__(self) -> Any:
        """Matrix_integer_dense.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 4193)

        Return the inverse of ``self``.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ,3)
            sage: m = M([1,2,3,3,4,5,1,2,-3])
            sage: ~m
            [-11/6     1  -1/6]
            [  7/6  -1/2   1/3]
            [  1/6     0  -1/6]
            sage: ~m * m == m * ~m == M.identity_matrix()
            True

        Note that inverse of determinant one integer matrices do not belong to
        the same parent::

            sage: (~M.identity_matrix()).parent()
            Full MatrixSpace of 3 by 3 dense matrices over Rational Field

        This is consistent with::

            sage: (~1).parent()
            Rational Field

        TESTS::

            sage: ~M.zero_matrix()
            Traceback (most recent call last):
            ...
            ZeroDivisionError: matrix must be nonsingular"""
    @overload
    def __neg__(self) -> Any:
        """Matrix_integer_dense.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1041)

        Return the negative of this matrix.

        TESTS::

            sage: a = matrix(ZZ,2,range(4))
            sage: a.__neg__()
            [ 0 -1]
            [-2 -3]
            sage: -a
            [ 0 -1]
            [-2 -3]"""
    @overload
    def __neg__(self) -> Any:
        """Matrix_integer_dense.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 1041)

        Return the negative of this matrix.

        TESTS::

            sage: a = matrix(ZZ,2,range(4))
            sage: a.__neg__()
            [ 0 -1]
            [-2 -3]
            sage: -a
            [ 0 -1]
            [-2 -3]"""
    @overload
    def __pari__(self) -> Any:
        """Matrix_integer_dense.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5829)

        Return PARI C-library version of this matrix.

        EXAMPLES::

            sage: a = matrix(ZZ,2,2,[1,2,3,4])
            sage: a.__pari__()
            [1, 2; 3, 4]
            sage: pari(a)
            [1, 2; 3, 4]
            sage: type(pari(a))
            <class 'cypari2.gen.Gen'>"""
    @overload
    def __pari__(self) -> Any:
        """Matrix_integer_dense.__pari__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 5829)

        Return PARI C-library version of this matrix.

        EXAMPLES::

            sage: a = matrix(ZZ,2,2,[1,2,3,4])
            sage: a.__pari__()
            [1, 2; 3, 4]
            sage: pari(a)
            [1, 2; 3, 4]
            sage: type(pari(a))
            <class 'cypari2.gen.Gen'>"""
    def __pow__(self, sself, n, dummy) -> Any:
        """Matrix_integer_dense.__pow__(sself, n, dummy)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_dense.pyx (starting at line 941)

        Return the ``n``-th power of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(ZZ,3)
            sage: m = M([1, 1, 1, 2, 1, 1, -3, -2, -1])
            sage: m ** 3
            [-3 -2 -1]
            [-3 -2  0]
            [ 2  1 -3]
            sage: m ** -2
            [ 2 -3 -1]
            [-4  4  1]
            [ 1  0  0]
            sage: M(range(9)) ** -1
            Traceback (most recent call last):
            ...
            ZeroDivisionError: matrix must be nonsingular

        TESTS::

            sage: m ** 3 == m ** 3r == (~m) ** (-3) == (~m) ** (-3r)
            True

        The following exponents do not fit in an unsigned long and the
        multiplication method fall back to the generic power implementation in
        :mod:`sage.structure.element`::

            sage: m = M.identity_matrix()
            sage: m ** (2**256)
            [1 0 0]
            [0 1 0]
            [0 0 1]
            sage: m ** (2r**256r)
            [1 0 0]
            [0 1 0]
            [0 0 1]

        In this case, the second argument to ``__pow__`` is a matrix,
        which should raise the correct error::

            sage: M = Matrix(2, 2, range(4))
            sage: None^M
            Traceback (most recent call last):
            ...
            TypeError: Cannot convert NoneType to sage.matrix.matrix_integer_dense.Matrix_integer_dense
            sage: M^M
            Traceback (most recent call last):
            ...
            NotImplementedError: the given exponent is not supported"""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
