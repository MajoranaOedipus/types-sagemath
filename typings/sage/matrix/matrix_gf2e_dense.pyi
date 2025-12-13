import _cython_3_2_1
import sage.matrix.matrix_dense
from sage.rings.finite_rings.finite_field_constructor import GF as GF
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.richcmp import revop as revop, rich_to_bool as rich_to_bool, rich_to_bool_sgn as rich_to_bool_sgn, richcmp as richcmp, richcmp_not_equal as richcmp_not_equal
from typing import Any, ClassVar, overload

unpickle_matrix_gf2e_dense_v0: _cython_3_2_1.cython_function_or_method

class M4RIE_finite_field:
    """File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 109)

        A thin wrapper around the M4RIE finite field class such that we
        can put it in a hash table. This class is not meant for public
        consumption.
    """
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""

class Matrix_gf2e_dense(sage.matrix.matrix_dense.Matrix_dense):
    """Matrix_gf2e_dense(parent, entries=None, copy=None, bool coerce=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 196)

                Create new matrix over `GF(2^e)` for `2 \\leq e \\leq 16`.

                INPUT:

                - ``parent`` -- a matrix space over ``GF(2^e)``

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``False``, assume without checking that the
                  entries lie in the base ring

                EXAMPLES::

                    sage: K.<a> = GF(2^4)
                    sage: l = [K.random_element() for _ in range(3*4)]

                    sage: A = Matrix(K, 3, 4, l)
                    sage: l == A.list()
                    True

                    sage: l[0] == A[0,0]
                    True

                    sage: A = Matrix(K, 3, 3, a); A
                    [a 0 0]
                    [0 a 0]
                    [0 0 a]
        """
    @overload
    def augment(self, right) -> Any:
        """Matrix_gf2e_dense.augment(self, right)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1173)

        Augments ``self`` with ``right``.

        INPUT:

        - ``right`` -- a matrix

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: MS = MatrixSpace(K,3,3)
            sage: A = random_matrix(K,3,3)
            sage: B = A.augment(MS(1))
            sage: B.echelonize()
            sage: C = B.matrix_from_columns([3,4,5])
            sage: A.rank() < 3 or C == ~A
            True
            sage: A.rank() < 3 or C*A == MS(1)
            True

        TESTS::

            sage: K.<a> = GF(2^4)
            sage: A = random_matrix(K,2,3)
            sage: B = random_matrix(K,2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(K, 0, 0, 0)
            sage: N = Matrix(K, 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19

            sage: M = Matrix(K, 0, 1, 0)
            sage: N = Matrix(K, 0, 1, 0)
            sage: M.augment(N)
            []

            sage: A = matrix(K, 3, range(12))
            sage: B = vector(QQ, [2,5/7,1.2]) # see issue: 38448
            sage: A.augment(B).ncols()
            5

            sage: B = vector([])
            sage: A.augment(B) == A
            True"""
    @overload
    def augment(self, B) -> Any:
        """Matrix_gf2e_dense.augment(self, right)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1173)

        Augments ``self`` with ``right``.

        INPUT:

        - ``right`` -- a matrix

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: MS = MatrixSpace(K,3,3)
            sage: A = random_matrix(K,3,3)
            sage: B = A.augment(MS(1))
            sage: B.echelonize()
            sage: C = B.matrix_from_columns([3,4,5])
            sage: A.rank() < 3 or C == ~A
            True
            sage: A.rank() < 3 or C*A == MS(1)
            True

        TESTS::

            sage: K.<a> = GF(2^4)
            sage: A = random_matrix(K,2,3)
            sage: B = random_matrix(K,2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(K, 0, 0, 0)
            sage: N = Matrix(K, 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19

            sage: M = Matrix(K, 0, 1, 0)
            sage: N = Matrix(K, 0, 1, 0)
            sage: M.augment(N)
            []

            sage: A = matrix(K, 3, range(12))
            sage: B = vector(QQ, [2,5/7,1.2]) # see issue: 38448
            sage: A.augment(B).ncols()
            5

            sage: B = vector([])
            sage: A.augment(B) == A
            True"""
    @overload
    def augment(self, A) -> Any:
        """Matrix_gf2e_dense.augment(self, right)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1173)

        Augments ``self`` with ``right``.

        INPUT:

        - ``right`` -- a matrix

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: MS = MatrixSpace(K,3,3)
            sage: A = random_matrix(K,3,3)
            sage: B = A.augment(MS(1))
            sage: B.echelonize()
            sage: C = B.matrix_from_columns([3,4,5])
            sage: A.rank() < 3 or C == ~A
            True
            sage: A.rank() < 3 or C*A == MS(1)
            True

        TESTS::

            sage: K.<a> = GF(2^4)
            sage: A = random_matrix(K,2,3)
            sage: B = random_matrix(K,2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(K, 0, 0, 0)
            sage: N = Matrix(K, 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19

            sage: M = Matrix(K, 0, 1, 0)
            sage: N = Matrix(K, 0, 1, 0)
            sage: M.augment(N)
            []

            sage: A = matrix(K, 3, range(12))
            sage: B = vector(QQ, [2,5/7,1.2]) # see issue: 38448
            sage: A.augment(B).ncols()
            5

            sage: B = vector([])
            sage: A.augment(B) == A
            True"""
    @overload
    def augment(self, N) -> Any:
        """Matrix_gf2e_dense.augment(self, right)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1173)

        Augments ``self`` with ``right``.

        INPUT:

        - ``right`` -- a matrix

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: MS = MatrixSpace(K,3,3)
            sage: A = random_matrix(K,3,3)
            sage: B = A.augment(MS(1))
            sage: B.echelonize()
            sage: C = B.matrix_from_columns([3,4,5])
            sage: A.rank() < 3 or C == ~A
            True
            sage: A.rank() < 3 or C*A == MS(1)
            True

        TESTS::

            sage: K.<a> = GF(2^4)
            sage: A = random_matrix(K,2,3)
            sage: B = random_matrix(K,2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(K, 0, 0, 0)
            sage: N = Matrix(K, 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19

            sage: M = Matrix(K, 0, 1, 0)
            sage: N = Matrix(K, 0, 1, 0)
            sage: M.augment(N)
            []

            sage: A = matrix(K, 3, range(12))
            sage: B = vector(QQ, [2,5/7,1.2]) # see issue: 38448
            sage: A.augment(B).ncols()
            5

            sage: B = vector([])
            sage: A.augment(B) == A
            True"""
    @overload
    def augment(self, N) -> Any:
        """Matrix_gf2e_dense.augment(self, right)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1173)

        Augments ``self`` with ``right``.

        INPUT:

        - ``right`` -- a matrix

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: MS = MatrixSpace(K,3,3)
            sage: A = random_matrix(K,3,3)
            sage: B = A.augment(MS(1))
            sage: B.echelonize()
            sage: C = B.matrix_from_columns([3,4,5])
            sage: A.rank() < 3 or C == ~A
            True
            sage: A.rank() < 3 or C*A == MS(1)
            True

        TESTS::

            sage: K.<a> = GF(2^4)
            sage: A = random_matrix(K,2,3)
            sage: B = random_matrix(K,2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(K, 0, 0, 0)
            sage: N = Matrix(K, 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19

            sage: M = Matrix(K, 0, 1, 0)
            sage: N = Matrix(K, 0, 1, 0)
            sage: M.augment(N)
            []

            sage: A = matrix(K, 3, range(12))
            sage: B = vector(QQ, [2,5/7,1.2]) # see issue: 38448
            sage: A.augment(B).ncols()
            5

            sage: B = vector([])
            sage: A.augment(B) == A
            True"""
    @overload
    def augment(self, B) -> Any:
        """Matrix_gf2e_dense.augment(self, right)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1173)

        Augments ``self`` with ``right``.

        INPUT:

        - ``right`` -- a matrix

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: MS = MatrixSpace(K,3,3)
            sage: A = random_matrix(K,3,3)
            sage: B = A.augment(MS(1))
            sage: B.echelonize()
            sage: C = B.matrix_from_columns([3,4,5])
            sage: A.rank() < 3 or C == ~A
            True
            sage: A.rank() < 3 or C*A == MS(1)
            True

        TESTS::

            sage: K.<a> = GF(2^4)
            sage: A = random_matrix(K,2,3)
            sage: B = random_matrix(K,2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(K, 0, 0, 0)
            sage: N = Matrix(K, 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19

            sage: M = Matrix(K, 0, 1, 0)
            sage: N = Matrix(K, 0, 1, 0)
            sage: M.augment(N)
            []

            sage: A = matrix(K, 3, range(12))
            sage: B = vector(QQ, [2,5/7,1.2]) # see issue: 38448
            sage: A.augment(B).ncols()
            5

            sage: B = vector([])
            sage: A.augment(B) == A
            True"""
    @overload
    def augment(self, B) -> Any:
        """Matrix_gf2e_dense.augment(self, right)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1173)

        Augments ``self`` with ``right``.

        INPUT:

        - ``right`` -- a matrix

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: MS = MatrixSpace(K,3,3)
            sage: A = random_matrix(K,3,3)
            sage: B = A.augment(MS(1))
            sage: B.echelonize()
            sage: C = B.matrix_from_columns([3,4,5])
            sage: A.rank() < 3 or C == ~A
            True
            sage: A.rank() < 3 or C*A == MS(1)
            True

        TESTS::

            sage: K.<a> = GF(2^4)
            sage: A = random_matrix(K,2,3)
            sage: B = random_matrix(K,2,0)
            sage: A.augment(B) == A
            True

            sage: B.augment(A) == A
            True

            sage: M = Matrix(K, 0, 0, 0)
            sage: N = Matrix(K, 0, 19, 0)
            sage: W = M.augment(N)
            sage: W.ncols()
            19

            sage: M = Matrix(K, 0, 1, 0)
            sage: N = Matrix(K, 0, 1, 0)
            sage: M.augment(N)
            []

            sage: A = matrix(K, 3, range(12))
            sage: B = vector(QQ, [2,5/7,1.2]) # see issue: 38448
            sage: A.augment(B).ncols()
            5

            sage: B = vector([])
            sage: A.augment(B) == A
            True"""
    def cling(self, *C) -> Any:
        """Matrix_gf2e_dense.cling(self, *C)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1510)

        Pack the matrices over `\\GF{2}` into this matrix over `\\GF{2^e}`.

        Elements in `\\GF{2^e}` can be represented as `\\sum c_i a^i` where
        `a` is a root the minimal polynomial. If this matrix is `A`
        then this function writes `c_i a^i` to the entry `A[x,y]`
        where `c_i` is the entry `C_i[x,y]`.

        INPUT:

        - ``C`` -- list of matrices over GF(2)

        EXAMPLES::

            sage: K.<a> = GF(2^2)
            sage: A = matrix(K, 5, 5)
            sage: A0 = random_matrix(GF(2), 5, 5)
            sage: A1 = random_matrix(GF(2), 5, 5)
            sage: A.cling(A0, A1)
            sage: all(A.list()[i] == A0.list()[i] + a*A1.list()[i] for i in range(25))
            True

        Slicing and clinging are inverse operations::

            sage: B0, B1 = A.slice()
            sage: B0 == A0 and B1 == A1
            True

        TESTS::

            sage: K.<a> = GF(2^2)
            sage: A = matrix(K, 5, 5)
            sage: A0 = random_matrix(GF(2), 5, 5)
            sage: A1 = random_matrix(GF(2), 5, 5)
            sage: A.cling(A0, A1)
            sage: B = copy(A)
            sage: A.cling(A0, A1)
            sage: A == B
            True

            sage: A.cling(A0)
            Traceback (most recent call last):
            ...
            ValueError: The number of input matrices must be equal to the degree of the base field.

            sage: K.<a> = GF(2^5)
            sage: A = matrix(K, 5, 5)
            sage: A0 = random_matrix(GF(2), 5, 5)
            sage: A1 = random_matrix(GF(2), 5, 5)
            sage: A2 = random_matrix(GF(2), 5, 5)
            sage: A3 = random_matrix(GF(2), 5, 5)
            sage: A4 = random_matrix(GF(2), 5, 5)
            sage: A.cling(A0, A1, A2, A3, A4)
            Traceback (most recent call last):
            ...
            NotImplementedError: Cling is only implemented for degree <= 4."""
    @overload
    def echelonize(self, algorithm=..., reduced=..., **kwds) -> Any:
        """Matrix_gf2e_dense.echelonize(self, algorithm='heuristic', reduced=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 893)

        Compute the row echelon form of ``self`` in place.

        INPUT:

        - ``algorithm`` -- one of the following
          - ``heuristic`` -- let M4RIE decide (default)
          - ``newton_john`` -- use newton_john table based algorithm
          - ``ple`` -- use PLE decomposition
          - ``naive`` -- use naive cubic Gaussian elimination (M4RIE implementation)
          - ``builtin`` -- use naive cubic Gaussian elimination (Sage implementation)
        - ``reduced`` -- if ``True`` return reduced echelon form. No
          guarantee is given that the matrix is *not* reduced if
          ``False`` (default: ``True``)

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: m,n  = 3, 5
            sage: A = random_matrix(K, 3, 5)
            sage: R = A.row_space()
            sage: A.echelonize()
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in A.rows() if r)
            True
            sage: A.row_space() == R
            True

            sage: K.<a> = GF(2^3)
            sage: m,n  = 3, 5
            sage: MS = MatrixSpace(K,m,n)
            sage: A = random_matrix(K, 3, 5)
            sage: B = copy(A).echelon_form('newton_john')
            sage: C = copy(A).echelon_form('naive')
            sage: D = copy(A).echelon_form('builtin')
            sage: B == C == D
            True
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in B.rows() if r)
            True"""
    @overload
    def echelonize(self) -> Any:
        """Matrix_gf2e_dense.echelonize(self, algorithm='heuristic', reduced=True, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 893)

        Compute the row echelon form of ``self`` in place.

        INPUT:

        - ``algorithm`` -- one of the following
          - ``heuristic`` -- let M4RIE decide (default)
          - ``newton_john`` -- use newton_john table based algorithm
          - ``ple`` -- use PLE decomposition
          - ``naive`` -- use naive cubic Gaussian elimination (M4RIE implementation)
          - ``builtin`` -- use naive cubic Gaussian elimination (Sage implementation)
        - ``reduced`` -- if ``True`` return reduced echelon form. No
          guarantee is given that the matrix is *not* reduced if
          ``False`` (default: ``True``)

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: m,n  = 3, 5
            sage: A = random_matrix(K, 3, 5)
            sage: R = A.row_space()
            sage: A.echelonize()
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in A.rows() if r)
            True
            sage: A.row_space() == R
            True

            sage: K.<a> = GF(2^3)
            sage: m,n  = 3, 5
            sage: MS = MatrixSpace(K,m,n)
            sage: A = random_matrix(K, 3, 5)
            sage: B = copy(A).echelon_form('newton_john')
            sage: C = copy(A).echelon_form('naive')
            sage: D = copy(A).echelon_form('builtin')
            sage: B == C == D
            True
            sage: all(r[r.nonzero_positions()[0]] == 1 for r in B.rows() if r)
            True"""
    @overload
    def randomize(self, density=..., nonzero=..., *args, **kwds) -> Any:
        """Matrix_gf2e_dense.randomize(self, density=1, nonzero=False, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 746)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        INPUT:

        - ``density`` -- float; proportion (roughly) to be considered for
          changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are forced to be nonzero

        OUTPUT: none, the matrix is modified in-place

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: total_count = 0
            sage: from collections import defaultdict
            sage: dic = defaultdict(Integer)
            sage: def add_samples():
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(K,3,3)
            ....:         A.randomize()
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0
            sage: add_samples()
            sage: while not all(abs(dic[a]/total_count - 1/16) < 0.01 for a in dic):
            ....:     add_samples()

            sage: def add_sample(density):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     density_sum += random_matrix(K, 1000, 1000, density=density).density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1)
            sage: while abs(density_sum/total_count - 0.1) > 0.001:
            ....:     add_sample(0.1)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(1.0)
            sage: while abs(density_sum/total_count - 1.0) > 0.001:
            ....:     add_sample(1.0)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5)
            sage: while abs(density_sum/total_count - 0.5) > 0.001:
            ....:     add_sample(0.5)

        Note, that the matrix is updated and not zero-ed out before
        being randomized::

            sage: def add_sample(density, nonzero):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = matrix(K, 1000, 1000)
            ....:     A.randomize(nonzero=nonzero, density=density)
            ....:     A.randomize(nonzero=nonzero, density=density)
            ....:     density_sum += A.density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1, True)
            sage: while abs(density_sum/total_count - (1 - 0.9^2)) > 0.001:
            ....:     add_sample(0.1, True)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1, False)
            sage: while abs(density_sum/total_count - (1 - 0.9^2)*15/16) > 0.001:
            ....:     add_sample(0.1, False)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.05, True)
            sage: while abs(density_sum/total_count - (1 - 0.95^2)) > 0.001:
            ....:     add_sample(0.05, True)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5, True)
            sage: while abs(density_sum/total_count - (1 - 0.5^2)) > 0.001:
            ....:     add_sample(0.5, True)"""
    @overload
    def randomize(self) -> Any:
        """Matrix_gf2e_dense.randomize(self, density=1, nonzero=False, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 746)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        INPUT:

        - ``density`` -- float; proportion (roughly) to be considered for
          changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are forced to be nonzero

        OUTPUT: none, the matrix is modified in-place

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: total_count = 0
            sage: from collections import defaultdict
            sage: dic = defaultdict(Integer)
            sage: def add_samples():
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(K,3,3)
            ....:         A.randomize()
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0
            sage: add_samples()
            sage: while not all(abs(dic[a]/total_count - 1/16) < 0.01 for a in dic):
            ....:     add_samples()

            sage: def add_sample(density):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     density_sum += random_matrix(K, 1000, 1000, density=density).density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1)
            sage: while abs(density_sum/total_count - 0.1) > 0.001:
            ....:     add_sample(0.1)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(1.0)
            sage: while abs(density_sum/total_count - 1.0) > 0.001:
            ....:     add_sample(1.0)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5)
            sage: while abs(density_sum/total_count - 0.5) > 0.001:
            ....:     add_sample(0.5)

        Note, that the matrix is updated and not zero-ed out before
        being randomized::

            sage: def add_sample(density, nonzero):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = matrix(K, 1000, 1000)
            ....:     A.randomize(nonzero=nonzero, density=density)
            ....:     A.randomize(nonzero=nonzero, density=density)
            ....:     density_sum += A.density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1, True)
            sage: while abs(density_sum/total_count - (1 - 0.9^2)) > 0.001:
            ....:     add_sample(0.1, True)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1, False)
            sage: while abs(density_sum/total_count - (1 - 0.9^2)*15/16) > 0.001:
            ....:     add_sample(0.1, False)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.05, True)
            sage: while abs(density_sum/total_count - (1 - 0.95^2)) > 0.001:
            ....:     add_sample(0.05, True)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5, True)
            sage: while abs(density_sum/total_count - (1 - 0.5^2)) > 0.001:
            ....:     add_sample(0.5, True)"""
    @overload
    def randomize(self, nonzero=..., density=...) -> Any:
        """Matrix_gf2e_dense.randomize(self, density=1, nonzero=False, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 746)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        INPUT:

        - ``density`` -- float; proportion (roughly) to be considered for
          changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are forced to be nonzero

        OUTPUT: none, the matrix is modified in-place

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: total_count = 0
            sage: from collections import defaultdict
            sage: dic = defaultdict(Integer)
            sage: def add_samples():
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(K,3,3)
            ....:         A.randomize()
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0
            sage: add_samples()
            sage: while not all(abs(dic[a]/total_count - 1/16) < 0.01 for a in dic):
            ....:     add_samples()

            sage: def add_sample(density):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     density_sum += random_matrix(K, 1000, 1000, density=density).density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1)
            sage: while abs(density_sum/total_count - 0.1) > 0.001:
            ....:     add_sample(0.1)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(1.0)
            sage: while abs(density_sum/total_count - 1.0) > 0.001:
            ....:     add_sample(1.0)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5)
            sage: while abs(density_sum/total_count - 0.5) > 0.001:
            ....:     add_sample(0.5)

        Note, that the matrix is updated and not zero-ed out before
        being randomized::

            sage: def add_sample(density, nonzero):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = matrix(K, 1000, 1000)
            ....:     A.randomize(nonzero=nonzero, density=density)
            ....:     A.randomize(nonzero=nonzero, density=density)
            ....:     density_sum += A.density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1, True)
            sage: while abs(density_sum/total_count - (1 - 0.9^2)) > 0.001:
            ....:     add_sample(0.1, True)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1, False)
            sage: while abs(density_sum/total_count - (1 - 0.9^2)*15/16) > 0.001:
            ....:     add_sample(0.1, False)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.05, True)
            sage: while abs(density_sum/total_count - (1 - 0.95^2)) > 0.001:
            ....:     add_sample(0.05, True)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5, True)
            sage: while abs(density_sum/total_count - (1 - 0.5^2)) > 0.001:
            ....:     add_sample(0.5, True)"""
    @overload
    def randomize(self, nonzero=..., density=...) -> Any:
        """Matrix_gf2e_dense.randomize(self, density=1, nonzero=False, *args, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 746)

        Randomize ``density`` proportion of the entries of this matrix,
        leaving the rest unchanged.

        INPUT:

        - ``density`` -- float; proportion (roughly) to be considered for
          changes
        - ``nonzero`` -- boolean (default: ``False``); whether the new entries
          are forced to be nonzero

        OUTPUT: none, the matrix is modified in-place

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: total_count = 0
            sage: from collections import defaultdict
            sage: dic = defaultdict(Integer)
            sage: def add_samples():
            ....:     global dic, total_count
            ....:     for _ in range(100):
            ....:         A = Matrix(K,3,3)
            ....:         A.randomize()
            ....:         for a in A.list():
            ....:             dic[a] += 1
            ....:             total_count += 1.0
            sage: add_samples()
            sage: while not all(abs(dic[a]/total_count - 1/16) < 0.01 for a in dic):
            ....:     add_samples()

            sage: def add_sample(density):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     density_sum += random_matrix(K, 1000, 1000, density=density).density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1)
            sage: while abs(density_sum/total_count - 0.1) > 0.001:
            ....:     add_sample(0.1)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(1.0)
            sage: while abs(density_sum/total_count - 1.0) > 0.001:
            ....:     add_sample(1.0)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5)
            sage: while abs(density_sum/total_count - 0.5) > 0.001:
            ....:     add_sample(0.5)

        Note, that the matrix is updated and not zero-ed out before
        being randomized::

            sage: def add_sample(density, nonzero):
            ....:     global density_sum, total_count
            ....:     total_count += 1.0
            ....:     A = matrix(K, 1000, 1000)
            ....:     A.randomize(nonzero=nonzero, density=density)
            ....:     A.randomize(nonzero=nonzero, density=density)
            ....:     density_sum += A.density()

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1, True)
            sage: while abs(density_sum/total_count - (1 - 0.9^2)) > 0.001:
            ....:     add_sample(0.1, True)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.1, False)
            sage: while abs(density_sum/total_count - (1 - 0.9^2)*15/16) > 0.001:
            ....:     add_sample(0.1, False)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.05, True)
            sage: while abs(density_sum/total_count - (1 - 0.95^2)) > 0.001:
            ....:     add_sample(0.05, True)

            sage: density_sum = 0.0
            sage: total_count = 0.0
            sage: add_sample(0.5, True)
            sage: while abs(density_sum/total_count - (1 - 0.5^2)) > 0.001:
            ....:     add_sample(0.5, True)"""
    @overload
    def rank(self) -> Any:
        """Matrix_gf2e_dense.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1392)

        Return the rank of this matrix (cached).

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: A = random_matrix(K, 10, 10, algorithm='unimodular')
            sage: A.rank()
            10
            sage: A = matrix(K, 10, 0)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_gf2e_dense.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1392)

        Return the rank of this matrix (cached).

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: A = random_matrix(K, 10, 10, algorithm='unimodular')
            sage: A.rank()
            10
            sage: A = matrix(K, 10, 0)
            sage: A.rank()
            0"""
    @overload
    def rank(self) -> Any:
        """Matrix_gf2e_dense.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1392)

        Return the rank of this matrix (cached).

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: A = random_matrix(K, 10, 10, algorithm='unimodular')
            sage: A.rank()
            10
            sage: A = matrix(K, 10, 0)
            sage: A.rank()
            0"""
    def slice(self) -> Any:
        """Matrix_gf2e_dense.slice(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1452)

        Unpack this matrix into matrices over `\\GF{2}`.

        Elements in `\\GF{2^e}` can be represented as `\\sum c_i a^i`
        where `a` is a root the minimal polynomial. This function
        returns a tuple of matrices `C` whose entry `C_i[x,y]` is the
        coefficient of `c_i` in `A[x,y]` if this matrix is `A`.

        EXAMPLES::

            sage: K.<a> = GF(2^2)
            sage: A = random_matrix(K, 5, 5)
            sage: A0, A1 = A.slice()
            sage: all(A.list()[i] == A0.list()[i] + a*A1.list()[i] for i in range(25))
            True

            sage: K.<a> = GF(2^3)
            sage: A = random_matrix(K, 5, 5)
            sage: A0, A1, A2 = A.slice()
            sage: all(A.list()[i] == A0.list()[i] + a*A1.list()[i] + a^2*A2.list()[i] for i in range(25))
            True

        Slicing and clinging are inverse operations::

            sage: B = matrix(K, 5, 5)
            sage: B.cling(A0, A1, A2)
            sage: B == A
            True"""
    def submatrix(self, Py_ssize_trow=..., Py_ssize_tcol=..., Py_ssize_tnrows=..., Py_ssize_tncols=...) -> Any:
        """Matrix_gf2e_dense.submatrix(self, Py_ssize_t row=0, Py_ssize_t col=0, Py_ssize_t nrows=-1, Py_ssize_t ncols=-1)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1327)

        Return submatrix from the index ``row,col`` (inclusive) with
        dimension ``nrows x ncols``.

        INPUT:

        - ``row`` -- index of start row
        - ``col`` -- index of start column
        - ``nrows`` -- number of rows of submatrix
        - ``ncols`` -- number of columns of submatrix

        EXAMPLES::

             sage: K.<a> = GF(2^10)
             sage: A = random_matrix(K,200,200)
             sage: A[0:2,0:2] == A.submatrix(0,0,2,2)
             True
             sage: A[0:100,0:100] == A.submatrix(0,0,100,100)
             True
             sage: A == A.submatrix(0,0,200,200)
             True

             sage: A[1:3,1:3] == A.submatrix(1,1,2,2)
             True
             sage: A[1:100,1:100] == A.submatrix(1,1,99,99)
             True
             sage: A[1:200,1:200] == A.submatrix(1,1,199,199)
             True

        TESTS for handling of default arguments (:issue:`18761`)::

             sage: A.submatrix(17,15) == A.submatrix(17,15,183,185)
             True
             sage: A.submatrix(row=100,col=37,nrows=1,ncols=3) == A.submatrix(100,37,1,3)
             True"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __copy__(self) -> Any:
        """Matrix_gf2e_dense.__copy__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 688)

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: m,n  = 3, 4
            sage: A = random_matrix(K,3,4)
            sage: A2 = copy(A)
            sage: A2.list() == A.list()
            True

            sage: A[0,0] = 1 if A[0,0] != 1 else 0
            sage: A2[0,0] == A[0,0]
            False"""
    def __invert__(self) -> Any:
        """Matrix_gf2e_dense.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1007)

        EXAMPLES::

            sage: K.<a> = GF(2^3)
            sage: A = random_matrix(K, 3, 3)
            sage: while A.rank() != 3:
            ....:     A = random_matrix(K, 3, 3)
            sage: B = ~A
            sage: A*B
            [1 0 0]
            [0 1 0]
            [0 0 1]"""
    def __neg__(self) -> Any:
        """Matrix_gf2e_dense.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 657)

        EXAMPLES::

            sage: K.<a> = GF(2^4)
            sage: A = random_matrix(K, 3, 4)
            sage: B = -A
            sage: all(B.list()[i] == -A.list()[i] for i in range(12))
            True"""
    @overload
    def __reduce__(self) -> Any:
        """Matrix_gf2e_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1418)

        EXAMPLES::

            sage: K.<a> = GF(2^8)
            sage: A = random_matrix(K,70,70)
            sage: f, s= A.__reduce__()
            sage: from sage.matrix.matrix_gf2e_dense import unpickle_matrix_gf2e_dense_v0
            sage: f == unpickle_matrix_gf2e_dense_v0
            True
            sage: f(*s) == A
            True

        See :issue:`21669`::

            sage: all(f(*s) == B
            ....:     for r,c in [(0,0),(0,1),(1,0)]
            ....:     for B in [Matrix(GF(4, 'a'), r,c)]
            ....:     for f,s in [B.__reduce__()])
            True"""
    @overload
    def __reduce__(self) -> Any:
        """Matrix_gf2e_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1418)

        EXAMPLES::

            sage: K.<a> = GF(2^8)
            sage: A = random_matrix(K,70,70)
            sage: f, s= A.__reduce__()
            sage: from sage.matrix.matrix_gf2e_dense import unpickle_matrix_gf2e_dense_v0
            sage: f == unpickle_matrix_gf2e_dense_v0
            True
            sage: f(*s) == A
            True

        See :issue:`21669`::

            sage: all(f(*s) == B
            ....:     for r,c in [(0,0),(0,1),(1,0)]
            ....:     for B in [Matrix(GF(4, 'a'), r,c)]
            ....:     for f,s in [B.__reduce__()])
            True"""
    @overload
    def __reduce__(self) -> Any:
        """Matrix_gf2e_dense.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_gf2e_dense.pyx (starting at line 1418)

        EXAMPLES::

            sage: K.<a> = GF(2^8)
            sage: A = random_matrix(K,70,70)
            sage: f, s= A.__reduce__()
            sage: from sage.matrix.matrix_gf2e_dense import unpickle_matrix_gf2e_dense_v0
            sage: f == unpickle_matrix_gf2e_dense_v0
            True
            sage: f(*s) == A
            True

        See :issue:`21669`::

            sage: all(f(*s) == B
            ....:     for r,c in [(0,0),(0,1),(1,0)]
            ....:     for B in [Matrix(GF(4, 'a'), r,c)]
            ....:     for f,s in [B.__reduce__()])
            True"""
