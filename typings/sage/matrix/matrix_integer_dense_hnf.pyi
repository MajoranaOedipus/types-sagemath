from sage.arith.misc import CRT_list as CRT_list, previous_prime as previous_prime
from sage.matrix.constructor import identity_matrix as identity_matrix, matrix as matrix, random_matrix as random_matrix
from sage.misc.timing import cputime as cputime
from sage.misc.verbose import verbose as verbose
from sage.rings.integer import Integer as Integer
from sage.rings.integer_ring import ZZ as ZZ
from sage.rings.real_mpfr import RR as RR

def max_det_prime(n):
    """
    Return the largest prime so that it is reasonably efficient to
    compute modulo that prime with n x n matrices in LinBox.

    INPUT:

    - ``n`` -- positive integer

    OUTPUT: a prime number

    EXAMPLES::

        sage: from sage.matrix.matrix_integer_dense_hnf import max_det_prime
        sage: max_det_prime(10000)
        8388593
        sage: max_det_prime(1000)
        8388593
        sage: max_det_prime(10)
        8388593
    """
def det_from_modp_and_divisor(A, d, p, z_mod, moduli, z_so_far=..., N_so_far=...):
    """
    This is used for internal purposes for computing determinants
    quickly (with the hybrid `p`-adic / multimodular algorithm).

    INPUT:

    - ``A`` -- a square matrix
    - ``d`` -- a divisor of the determinant of A
    - ``p`` -- a prime
    - ``z_mod`` -- values of det/d (mod ...)
    - ``moduli`` -- the moduli so far
    - ``z_so_far`` -- for a modulus p in the list moduli,
      (z_so_far mod p) is the determinant of A modulo p
    - ``N_so_far`` -- N_so_far is the product over the primes in the list moduli

    OUTPUT:

    - A triple (det bound, new z_so_far, new N_so_far).

    EXAMPLES::

        sage: a = matrix(ZZ, 3, [6, 1, 2, -56, -2, -1, -11, 2, -3])
        sage: factor(a.det())
        -1 * 13 * 29
        sage: d = 13
        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: matrix_integer_dense_hnf.det_from_modp_and_divisor(a, d, 97, [], [])
        (-377, -29, 97)
        sage: a.det()
        -377
    """
def det_given_divisor(A, d, proof: bool = True, stabilize: int = 2):
    """
    Given a divisor d of the determinant of A, compute the determinant of A.

    INPUT:

    - ``A`` -- square integer matrix
    - ``d`` -- nonzero integer that is assumed to divide the determinant of A
    - ``proof`` -- boolean (default: ``True``); compute det modulo enough primes
      so that the determinant is computed provably correctly (via the
      Hadamard bound).  It would be VERY hard for ``det()`` to fail even
      when ``proof`` is ``False``.
    - ``stabilize`` -- integer (default: 2); if proof = False, then compute
      the determinant modulo `p` until ``stabilize`` successive modulo
      determinant computations stabilize.

    OUTPUT: integer; determinant

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: a = matrix(ZZ,3,[-1, -1, -1, -20, 4, 1, -1, 1, 2])
        sage: matrix_integer_dense_hnf.det_given_divisor(a, 3)
        -30
        sage: matrix_integer_dense_hnf.det_given_divisor(a, 3, proof=False)
        -30
        sage: matrix_integer_dense_hnf.det_given_divisor(a, 3, proof=False, stabilize=1)
        -30
        sage: a.det()
        -30

    Here we illustrate proof=False giving a wrong answer::

        sage: p = matrix_integer_dense_hnf.max_det_prime(2)
        sage: q = previous_prime(p)
        sage: a = matrix(ZZ, 2, [p, 0, 0, q])
        sage: p * q
        70368442188091
        sage: matrix_integer_dense_hnf.det_given_divisor(a, 1, proof=False, stabilize=2)
        0

    This still works, because we do not work modulo primes that divide
    the determinant bound, which is found using a `p`-adic algorithm::

        sage: a.det(proof=False, stabilize=2)
        70368442188091

    3 primes is enough::

        sage: matrix_integer_dense_hnf.det_given_divisor(a, 1, proof=False, stabilize=3)
        70368442188091
        sage: matrix_integer_dense_hnf.det_given_divisor(a, 1, proof=False, stabilize=5)
        70368442188091
        sage: matrix_integer_dense_hnf.det_given_divisor(a, 1, proof=True)
        70368442188091

    TESTS::

        sage: m = diagonal_matrix(ZZ, 68, [2]*66 + [1,1])
        sage: m.det()
        73786976294838206464
    """
def det_padic(A, proof: bool = True, stabilize: int = 2):
    """
    Return the determinant of A, computed using a `p`-adic/multimodular
    algorithm.

    INPUT:

    - ``A`` -- a square matrix

    - ``proof`` -- boolean

    - ``stabilize`` -- (default: 2) if proof False, number of successive primes so that
      CRT det must stabilize

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as h
        sage: a = matrix(ZZ, 3, [1..9])
        sage: h.det_padic(a)
        0
        sage: a = matrix(ZZ, 3, [1,2,5,-7,8,10,192,5,18])
        sage: h.det_padic(a)
        -3669
        sage: a.determinant(algorithm='ntl')
        -3669
    """
def double_det(A, b, c, proof):
    """
    Compute the determinants of the stacked integer matrices
    A.stack(b) and A.stack(c).

    INPUT:

    - ``A`` -- an (n-1) x n matrix
    - ``b`` -- a 1 x n matrix
    - ``c`` -- a 1 x n matrix
    - ``proof`` -- whether or not to compute the det modulo enough times to
      provably compute the determinant

    OUTPUT: a pair of two integers

    EXAMPLES::

        sage: from sage.matrix.matrix_integer_dense_hnf import double_det
        sage: A = matrix(ZZ, 2, 3, [1,2,3, 4,-2,5])
        sage: b = matrix(ZZ, 1, 3, [1,-2,5])
        sage: c = matrix(ZZ, 1, 3, [8,2,10])
        sage: A.stack(b).det()
        -48
        sage: A.stack(c).det()
        42
        sage: double_det(A, b, c, False)
        (-48, 42)
    """
def add_column_fallback(B, a, proof):
    """
    Simplistic version of add_column, in case the powerful clever one
    fails (e.g., B is singular).

    INPUT:

    - ``B`` -- a square matrix (may be singular)
    - ``a`` -- an n x 1 matrix, where B has n rows
    - ``proof`` -- boolean; whether to prove result correct

    OUTPUT: x; a vector such that ``H' = H_B.augment(x)`` is the HNF of
    ``A = B.augment(a)``

    EXAMPLES::

        sage: B = matrix(ZZ,3, [-1, -1, 1, -3, 8, -2, -1, -1, -1])
        sage: a = matrix(ZZ,3,1, [1,2,3])
        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: matrix_integer_dense_hnf.add_column_fallback(B, a, True)
        [-3]
        [-7]
        [-2]
        sage: matrix_integer_dense_hnf.add_column_fallback(B, a, False)
        [-3]
        [-7]
        [-2]
        sage: B.augment(a).hermite_form()
        [ 1  1  1 -3]
        [ 0 11  1 -7]
        [ 0  0  2 -2]
    """
def solve_system_with_difficult_last_row(B, a):
    """
    Solve ``B*x = a`` when the last row of `B` contains huge entries using
    a clever trick that reduces the problem to solve ``C*x = a`` where `C`
    is `B` but with the last row replaced by something small, along
    with one easy null space computation.  The latter are both solved
    `p`-adically.

    INPUT:

    - ``B`` -- a square n x n nonsingular matrix with painful big bottom row
    - ``a`` -- an n x 1 column matrix

    OUTPUT: the unique solution to ``B*x = a``

    EXAMPLES::

        sage: from sage.matrix.matrix_integer_dense_hnf import solve_system_with_difficult_last_row
        sage: B = matrix(ZZ, 3, [1,2,4, 3,-4,7, 939082,2930982,132902384098234])
        sage: a = matrix(ZZ,3,1, [1,2,5])
        sage: z = solve_system_with_difficult_last_row(B, a)
        sage: z
        [ 106321906985474/132902379815497]
        [132902385037291/1329023798154970]
        [        -5221794/664511899077485]
        sage: B*z
        [1]
        [2]
        [5]
    """
def add_column(B, H_B, a, proof):
    """
    The add column procedure.

    INPUT:

    - ``B`` -- a square matrix (may be singular)
    - ``H_B`` -- the Hermite normal form of B
    - ``a`` -- an n x 1 matrix, where B has n rows
    - ``proof`` -- boolean; whether to prove result correct, in case we use fallback method

    OUTPUT:

    - x -- a vector such that H' = H_B.augment(x) is the HNF of A = B.augment(a)

    EXAMPLES::

        sage: B = matrix(ZZ, 3, 3, [1,2,5, 0,-5,3, 1,1,2])
        sage: H_B = B.echelon_form()
        sage: a = matrix(ZZ, 3, 1, [1,8,-2])
        sage: import sage.matrix.matrix_integer_dense_hnf as hnf
        sage: x = hnf.add_column(B, H_B, a, True); x
        [18]
        [ 3]
        [23]
        sage: H_B.augment(x)
        [ 1  0 17 18]
        [ 0  1  3  3]
        [ 0  0 18 23]
        sage: B.augment(a).echelon_form()
        [ 1  0 17 18]
        [ 0  1  3  3]
        [ 0  0 18 23]
    """
def add_row(A, b, pivots, include_zero_rows):
    """
    The add row procedure.

    INPUT:

    - ``A`` -- a matrix in Hermite normal form with n column
    - ``b`` -- an n x 1 row matrix
    - ``pivots`` -- sorted list of integers; the pivot positions of A

    OUTPUT:

    - ``H`` -- the Hermite normal form of A.stack(b)
    - ``new_pivots`` -- the pivot columns of H

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as hnf
        sage: A = matrix(ZZ, 2, 3, [-21, -7, 5, 1,20,-7])
        sage: b = matrix(ZZ, 1,3, [-1,1,-1])
        sage: hnf.add_row(A, b, A.pivots(), True)
        (
        [ 1  6 29]
        [ 0  7 28]
        [ 0  0 46], [0, 1, 2]
        )
        sage: A.stack(b).echelon_form()
        [ 1  6 29]
        [ 0  7 28]
        [ 0  0 46]
    """
def pivots_of_hnf_matrix(H):
    """
    Return the pivot columns of a matrix H assumed to be in HNF.

    INPUT:

    - ``H`` -- a matrix that must be HNF

    OUTPUT: list of pivots

    EXAMPLES::

        sage: H = matrix(ZZ, 3, 5, [1, 0, 0, 45, -36, 0, 1, 0, 131, -107, 0, 0, 0, 178, -145]); H
        [   1    0    0   45  -36]
        [   0    1    0  131 -107]
        [   0    0    0  178 -145]
        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: matrix_integer_dense_hnf.pivots_of_hnf_matrix(H)
        [0, 1, 3]
    """
def hnf_square(A, proof):
    """
    INPUT:

    - ``A`` -- a nonsingular n x n matrix over the integers

    OUTPUT: the Hermite normal form of A

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as hnf
        sage: A = matrix(ZZ, 3, [-21, -7, 5, 1,20,-7, -1,1,-1])
        sage: hnf.hnf_square(A, False)
        [ 1  6 29]
        [ 0  7 28]
        [ 0  0 46]
        sage: A.echelon_form()
        [ 1  6 29]
        [ 0  7 28]
        [ 0  0 46]
    """
def interleave_matrices(A, B, cols1, cols2):
    """
    INPUT:

    - A, B -- matrices with the same number of rows
    - cols1, cols2 -- disjoint lists of integers

    OUTPUT:

    construct a new matrix C by sticking the columns
    of A at the positions specified by cols1 and the
    columns of B at the positions specified by cols2.

    EXAMPLES::

        sage: A = matrix(ZZ, 2, [1,2,3,4]); B = matrix(ZZ, 2, [-1,5,2,3])
        sage: A
        [1 2]
        [3 4]
        sage: B
        [-1  5]
        [ 2  3]
        sage: import sage.matrix.matrix_integer_dense_hnf as hnf
        sage: hnf.interleave_matrices(A, B, [1,3], [0,2])
        [-1  1  5  2]
        [ 2  3  3  4]
    """
def probable_pivot_rows(A):
    """
    Return rows of A that are very likely to be pivots.

    This really finds the pivots of A modulo a random prime.

    INPUT:

    - ``A`` -- a matrix

    OUTPUT: a tuple of integers

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: a = matrix(ZZ,3,[0, -1, -1, 0, -20, 1, 0, 1, 2])
        sage: a
        [  0  -1  -1]
        [  0 -20   1]
        [  0   1   2]
        sage: matrix_integer_dense_hnf.probable_pivot_rows(a)
        (0, 1)
    """
def probable_pivot_columns(A):
    """
    INPUT:

    - ``A`` -- a matrix

    OUTPUT: a tuple of integers

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: a = matrix(ZZ,3,[0, -1, -1, 0, -20, 1, 0, 1, 2])
        sage: a
        [  0  -1  -1]
        [  0 -20   1]
        [  0   1   2]
        sage: matrix_integer_dense_hnf.probable_pivot_columns(a)
        (1, 2)
    """
def ones(H, pivots):
    """
    Find all 1 pivot columns of the matrix H in Hermite form, along
    with the corresponding rows, and also the non 1 pivot columns and
    non-pivot rows.  Here a 1 pivot column is a pivot column so that
    the leading bottom entry is 1.

    INPUT:

    - ``H`` -- matrix in Hermite form
    - ``pivots`` -- list of integers (all pivot positions of H)

    OUTPUT:

    4-tuple of integer lists: onecol, onerow, non_oneol, non_onerow

    EXAMPLES::

        sage: H = matrix(ZZ, 3, 5, [1, 0, 0, 45, -36, 0, 1, 0, 131, -107, 0, 0, 0, 178, -145]); H
        [   1    0    0   45  -36]
        [   0    1    0  131 -107]
        [   0    0    0  178 -145]
        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: matrix_integer_dense_hnf.ones(H, [0,1,3])
        ([0, 1], [0, 1], [2], [2])
    """
def extract_ones_data(H, pivots):
    """
    Compute ones data and corresponding submatrices of H.

    This is used to optimized the :func:`add_row` function.

    INPUT:

    - ``H`` -- a matrix in HNF
    - ``pivots`` -- list of all pivot column positions of H

    OUTPUT:

    C, D, E, onecol, onerow, non_onecol, non_onerow
    where onecol, onerow, non_onecol, non_onerow are as for
    the ones function, and C, D, E are matrices:

    - ``C`` -- submatrix of all non-onecol columns and onecol rows
    - ``D`` -- all non-onecol columns and other rows
    - ``E`` -- inverse of D

    If D is not invertible or there are 0 or more than 2 non onecols,
    then C, D, and E are set to None.

    EXAMPLES::

        sage: H = matrix(ZZ, 3, 4, [1, 0, 0, 7, 0, 1, 5, 2, 0, 0, 6, 6])
        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: matrix_integer_dense_hnf.extract_ones_data(H, [0,1,2])
        (
        [0]
        [5], [6], [1/6], [0, 1], [0, 1], [2], [2]
        )

    Here we get None's since the (2,2) position submatrix is not invertible.
        sage: H = matrix(ZZ, 3, 5, [1, 0, 0, 45, -36, 0, 1, 0, 131, -107, 0, 0, 0, 178, -145]); H
        [   1    0    0   45  -36]
        [   0    1    0  131 -107]
        [   0    0    0  178 -145]
        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: matrix_integer_dense_hnf.extract_ones_data(H, [0,1,3])
        (None, None, None, [0, 1], [0, 1], [2], [2])
    """
def is_in_hnf_form(H, pivots):
    """
    Return whether the matrix ``H`` is in Hermite normal form
    with given pivot columns.

    INPUT:

    - ``H`` -- matrix
    - ``pivots`` -- sorted list of integers

    OUTPUT: boolean

    EXAMPLES::

        sage: a = matrix(ZZ,3,5,[-2, -6, -3, -17, -1, 2, -1, -1, -2, -1, -2, -2, -6, 9, 2])
        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: matrix_integer_dense_hnf.is_in_hnf_form(a,range(3))
        False
        sage: e = a.hermite_form(); p = a.pivots()
        sage: matrix_integer_dense_hnf.is_in_hnf_form(e, p)
        True
    """
def probable_hnf(A, include_zero_rows, proof):
    """
    Return the HNF of A or raise an exception if something involving
    the randomized nature of the algorithm goes wrong along the way.

    Calling this function again a few times should result it in it
    working, at least if proof=True.

    INPUT:

    - ``A`` -- a matrix
    - ``include_zero_rows`` -- boolean
    - ``proof`` -- boolean

    OUTPUT:

    the Hermite normal form of A.
    cols -- pivot columns

    EXAMPLES::

        sage: a = matrix(ZZ,4,3,[-1, -1, -1, -20, 4, 1, -1, 1, 2,1,2,3])
        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: matrix_integer_dense_hnf.probable_hnf(a, True, True)
        (
        [1 0 0]
        [0 1 0]
        [0 0 1]
        [0 0 0], [0, 1, 2]
        )
        sage: matrix_integer_dense_hnf.probable_hnf(a, False, True)
        (
        [1 0 0]
        [0 1 0]
        [0 0 1], [0, 1, 2]
        )
        sage: matrix_integer_dense_hnf.probable_hnf(a, False, False)
        (
        [1 0 0]
        [0 1 0]
        [0 0 1], [0, 1, 2]
        )
    """
def pad_zeros(A, nrows):
    """
    Add zeros to the bottom of A so that the resulting matrix has nrows.

    INPUT:

    - ``A`` -- a matrix
    - ``nrows`` -- integer that is at least as big as the number of rows of A

    OUTPUT: a matrix with nrows rows

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: a = matrix(ZZ, 2, 4, [1, 0, 0, 7, 0, 1, 5, 2])
        sage: matrix_integer_dense_hnf.pad_zeros(a, 4)
        [1 0 0 7]
        [0 1 5 2]
        [0 0 0 0]
        [0 0 0 0]
        sage: matrix_integer_dense_hnf.pad_zeros(a, 2)
        [1 0 0 7]
        [0 1 5 2]
    """
def hnf(A, include_zero_rows: bool = True, proof: bool = True):
    """
    Return the Hermite Normal Form of a general integer matrix A,
    along with the pivot columns.

    INPUT:

    - ``A`` -- an n x m matrix A over the integers
    - ``include_zero_rows`` -- boolean (default: ``True``); whether or not to include zero
      rows in the output matrix
    - ``proof`` -- whether or not to prove the result correct

    OUTPUT: tuple of:

    - ``matrix`` -- the Hermite normal form of A
    - ``pivots`` -- the pivot column positions of A

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: a = matrix(ZZ,3,5,[-2, -6, -3, -17, -1, 2, -1, -1, -2, -1, -2, -2, -6, 9, 2])
        sage: matrix_integer_dense_hnf.hnf(a)
        (
        [   2    0   26  -75  -10]
        [   0    1   27  -73   -9]
        [   0    0   37 -106  -13], [0, 1, 2]
        )
        sage: matrix_integer_dense_hnf.hnf(a.transpose())
        (
        [1 0 0]
        [0 1 0]
        [0 0 1]
        [0 0 0]
        [0 0 0], [0, 1, 2]
        )
        sage: matrix_integer_dense_hnf.hnf(a.transpose(), include_zero_rows=False)
        (
        [1 0 0]
        [0 1 0]
        [0 0 1], [0, 1, 2]
        )
    """
def hnf_with_transformation(A, proof: bool = True):
    """
    Compute the HNF H of A along with a transformation matrix U
    such that U*A = H.

    INPUT:

    - ``A`` -- an n x m matrix A over the integers
    - ``proof`` -- whether or not to prove the result correct

    OUTPUT: tuple of:

    - ``matrix`` -- the Hermite normal form H of A
    - ``U`` -- a unimodular matrix such that U * A = H

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: A = matrix(ZZ, 2, [1, -5, -10, 1, 3, 197]); A
        [  1  -5 -10]
        [  1   3 197]
        sage: H, U = matrix_integer_dense_hnf.hnf_with_transformation(A)
        sage: H
        [  1   3 197]
        [  0   8 207]
        sage: U
        [ 0  1]
        [-1  1]
        sage: U*A
        [  1   3 197]
        [  0   8 207]
    """
def hnf_with_transformation_tests(n: int = 10, m: int = 5, trials: int = 10) -> None:
    """
    Use this to randomly test that hnf with transformation matrix
    is working.

    EXAMPLES::

        sage: from sage.matrix.matrix_integer_dense_hnf import hnf_with_transformation_tests
        sage: hnf_with_transformation_tests(n=15, m=10, trials=10)
        0 1 2 3 4 5 6 7 8 9
    """
def benchmark_hnf(nrange, bits: int = 4) -> None:
    """
    Run benchmark program.

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as hnf
        sage: hnf.benchmark_hnf([10,25],32)
        ('sage', 10, 32, ...),
        ('sage', 25, 32, ...),
    """
def benchmark_magma_hnf(nrange, bits: int = 4) -> None:
    """
    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as hnf
        sage: hnf.benchmark_magma_hnf([50,100],32)     # optional - magma
        ('magma', 50, 32, ...),
        ('magma', 100, 32, ...),
    """
def sanity_checks(times: int = 50, n: int = 8, m: int = 5, proof: bool = True, stabilize: int = 2, check_using_magma: bool = True) -> None:
    """
    Run random sanity checks on the modular `p`-adic HNF with tall and wide matrices
    both dense and sparse.

    INPUT:

    - ``times`` -- number of times to randomly try matrices with each shape
    - ``n`` -- number of rows
    - ``m`` -- number of columns
    - ``proof`` -- test with proof true
    - ``stabilize`` -- parameter to pass to hnf algorithm when proof is False
    - ``check_using_magma`` -- if ``True`` use Magma instead of PARI to check
      correctness of computed HNF's. Since PARI's HNF is buggy and slow (as of
      2008-02-16 non-pivot entries sometimes are not normalized to be
      nonnegative) the default is Magma.

    EXAMPLES::

        sage: import sage.matrix.matrix_integer_dense_hnf as matrix_integer_dense_hnf
        sage: matrix_integer_dense_hnf.sanity_checks(times=5, check_using_magma=False)
        small 8 x 5
        0 1 2 3 4  (done)
        big 8 x 5
        0 1 2 3 4  (done)
        small 5 x 8
        0 1 2 3 4  (done)
        big 5 x 8
        0 1 2 3 4  (done)
        sparse 8 x 5
        0 1 2 3 4  (done)
        sparse 5 x 8
        0 1 2 3 4  (done)
        ill conditioned -- 1000*A -- 8 x 5
        0 1 2 3 4  (done)
        ill conditioned -- 1000*A but one row -- 8 x 5
        0 1 2 3 4  (done)
    """
