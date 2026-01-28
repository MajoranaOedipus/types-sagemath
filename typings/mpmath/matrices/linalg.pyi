"""

Linear algebra
--------------

Linear equations
................

Basic linear algebra is implemented; you can for example solve the linear
equation system::

      x + 2*y = -10
    3*x + 4*y =  10

using ``lu_solve``::

    >>> from mpmath import *
    >>> mp.pretty = False
    >>> A = matrix([[1, 2], [3, 4]])
    >>> b = matrix([-10, 10])
    >>> x = lu_solve(A, b)
    >>> x
    matrix(
    [['30.0'],
     ['-20.0']])

If you don't trust the result, use ``residual`` to calculate the residual ||A*x-b||::

    >>> residual(A, x, b)
    matrix(
    [['3.46944695195361e-18'],
     ['3.46944695195361e-18']])
    >>> str(eps)
    '2.22044604925031e-16'

As you can see, the solution is quite accurate. The error is caused by the
inaccuracy of the internal floating point arithmetic. Though, it's even smaller
than the current machine epsilon, which basically means you can trust the
result.

If you need more speed, use NumPy, or ``fp.lu_solve`` for a floating-point computation.

    >>> fp.lu_solve(A, b)   # doctest: +ELLIPSIS
    matrix(...)

``lu_solve`` accepts overdetermined systems. It is usually not possible to solve
such systems, so the residual is minimized instead. Internally this is done
using Cholesky decomposition to compute a least squares approximation. This means
that that ``lu_solve`` will square the errors. If you can't afford this, use
``qr_solve`` instead. It is twice as slow but more accurate, and it calculates
the residual automatically.


Matrix factorization
....................

The function ``lu`` computes an explicit LU factorization of a matrix::

    >>> P, L, U = lu(matrix([[0,2,3],[4,5,6],[7,8,9]]))
    >>> print(P)
    [0.0  0.0  1.0]
    [1.0  0.0  0.0]
    [0.0  1.0  0.0]
    >>> print(L)
    [              1.0                0.0  0.0]
    [              0.0                1.0  0.0]
    [0.571428571428571  0.214285714285714  1.0]
    >>> print(U)
    [7.0  8.0                9.0]
    [0.0  2.0                3.0]
    [0.0  0.0  0.214285714285714]
    >>> print(P.T*L*U)
    [0.0  2.0  3.0]
    [4.0  5.0  6.0]
    [7.0  8.0  9.0]

Interval matrices
-----------------

Matrices may contain interval elements. This allows one to perform
basic linear algebra operations such as matrix multiplication
and equation solving with rigorous error bounds::

    >>> a = iv.matrix([['0.1','0.3','1.0'],
    ...             ['7.1','5.5','4.8'],
    ...             ['3.2','4.4','5.6']])
    >>>
    >>> b = iv.matrix(['4','0.6','0.5'])
    >>> c = iv.lu_solve(a, b)
    >>> print(c)
    [   [5.2582327113062568605927528666, 5.25823271130625686059275702219]]
    [[-13.1550493962678375411635581388, -13.1550493962678375411635540152]]
    [  [7.42069154774972557628979076189, 7.42069154774972557628979190734]]
    >>> print(a*c)
    [  [3.99999999999999999999999844904, 4.00000000000000000000000155096]]
    [[0.599999999999999999999968898009, 0.600000000000000000000031763736]]
    [[0.499999999999999999999979320485, 0.500000000000000000000020679515]]
"""
from __future__ import annotations
from builtins import range as xrange
from copy import copy
__all__: list[str] = ['LinearAlgebraMethods', 'copy', 'xrange']
class LinearAlgebraMethods:
    @staticmethod
    def LU_decomp(ctx, A, overwrite = False, use_cache = True):
        """
        
        LU-factorization of a n*n matrix using the Gauss algorithm.
        Returns L and U in one matrix and the pivot indices.
        
        Use overwrite to specify whether A will be overwritten with L and U.
        """
    @staticmethod
    def L_solve(ctx, L, b, p = None):
        """
        
        Solve the lower part of a LU factorized matrix for y.
        """
    @staticmethod
    def U_solve(ctx, U, y):
        """
        
        Solve the upper part of a LU factorized matrix for x.
        """
    @staticmethod
    def cholesky(ctx, A, tol = None):
        """
        
        Cholesky decomposition of a symmetric positive-definite matrix `A`.
        Returns a lower triangular matrix `L` such that `A = L \\times L^T`.
        More generally, for a complex Hermitian positive-definite matrix,
        a Cholesky decomposition satisfying `A = L \\times L^H` is returned.
        
        The Cholesky decomposition can be used to solve linear equation
        systems twice as efficiently as LU decomposition, or to
        test whether `A` is positive-definite.
        
        The optional parameter ``tol`` determines the tolerance for
        verifying positive-definiteness.
        
        **Examples**
        
        Cholesky decomposition of a positive-definite symmetric matrix::
        
            >>> from mpmath import *
            >>> mp.dps = 25; mp.pretty = True
            >>> A = eye(3) + hilbert(3)
            >>> nprint(A)
            [     2.0      0.5  0.333333]
            [     0.5  1.33333      0.25]
            [0.333333     0.25       1.2]
            >>> L = cholesky(A)
            >>> nprint(L)
            [ 1.41421      0.0      0.0]
            [0.353553  1.09924      0.0]
            [0.235702  0.15162  1.05899]
            >>> chop(A - L*L.T)
            [0.0  0.0  0.0]
            [0.0  0.0  0.0]
            [0.0  0.0  0.0]
        
        Cholesky decomposition of a Hermitian matrix::
        
            >>> A = eye(3) + matrix([[0,0.25j,-0.5j],[-0.25j,0,0],[0.5j,0,0]])
            >>> L = cholesky(A)
            >>> nprint(L)
            [          1.0                0.0                0.0]
            [(0.0 - 0.25j)  (0.968246 + 0.0j)                0.0]
            [ (0.0 + 0.5j)  (0.129099 + 0.0j)  (0.856349 + 0.0j)]
            >>> chop(A - L*L.H)
            [0.0  0.0  0.0]
            [0.0  0.0  0.0]
            [0.0  0.0  0.0]
        
        Attempted Cholesky decomposition of a matrix that is not positive
        definite::
        
            >>> A = -eye(3) + hilbert(3)
            >>> L = cholesky(A)
            Traceback (most recent call last):
              ...
            ValueError: matrix is not positive-definite
        
        **References**
        
        1. [Wikipedia]_ http://en.wikipedia.org/wiki/Cholesky_decomposition
        
        """
    @staticmethod
    def cholesky_solve(ctx, A, b, **kwargs):
        """
        
        Ax = b => x
        
        Solve a symmetric positive-definite linear equation system.
        This is twice as efficient as lu_solve.
        
        Typical use cases:
        * A.T*A
        * Hessian matrix
        * differential equations
        """
    @staticmethod
    def cond(ctx, A, norm = None):
        """
        
        Calculate the condition number of a matrix using a specified matrix norm.
        
        The condition number estimates the sensitivity of a matrix to errors.
        Example: small input errors for ill-conditioned coefficient matrices
        alter the solution of the system dramatically.
        
        For ill-conditioned matrices it's recommended to use qr_solve() instead
        of lu_solve(). This does not help with input errors however, it just avoids
        to add additional errors.
        
        Definition:    cond(A) = ||A|| * ||A**-1||
        """
    @staticmethod
    def det(ctx, A):
        """
        
        Calculate the determinant of a matrix.
        """
    @staticmethod
    def householder(ctx, A):
        """
        
        (A|b) -> H, p, x, res
        
        (A|b) is the coefficient matrix with left hand side of an optionally
        overdetermined linear equation system.
        H and p contain all information about the transformation matrices.
        x is the solution, res the residual.
        """
    @staticmethod
    def improve_solution(ctx, A, x, b, maxsteps = 1):
        """
        
        Improve a solution to a linear equation system iteratively.
        
        This re-uses the LU decomposition and is thus cheap.
        Usually 3 up to 4 iterations are giving the maximal improvement.
        """
    @staticmethod
    def inverse(ctx, A, **kwargs):
        """
        
        Calculate the inverse of a matrix.
        
        If you want to solve an equation system Ax = b, it's recommended to use
        solve(A, b) instead, it's about 3 times more efficient.
        """
    @staticmethod
    def lu(ctx, A):
        """
        
        A -> P, L, U
        
        LU factorisation of a square matrix A. L is the lower, U the upper part.
        P is the permutation matrix indicating the row swaps.
        
        P*A = L*U
        
        If you need efficiency, use the low-level method LU_decomp instead, it's
        much more memory efficient.
        """
    @staticmethod
    def lu_solve(ctx, A, b, **kwargs):
        """
        
        Ax = b => x
        
        Solve a determined or overdetermined linear equations system.
        Fast LU decomposition is used, which is less accurate than QR decomposition
        (especially for overdetermined systems), but it's twice as efficient.
        Use qr_solve if you want more precision or have to solve a very ill-
        conditioned system.
        
        If you specify real=True, it does not check for overdeterminded complex
        systems.
        """
    @staticmethod
    def lu_solve_mat(ctx, a, b):
        """
        Solve a * x = b  where a and b are matrices.
        """
    @staticmethod
    def qr(ctx, A, mode = 'full', edps = 10):
        """
        
        Compute a QR factorization $A = QR$ where
        A is an m x n matrix of real or complex numbers where m >= n
        
        mode has following meanings:
        (1) mode = 'raw' returns two matrixes (A, tau) in the
            internal format used by LAPACK
        (2) mode = 'skinny' returns the leading n columns of Q
            and n rows of R
        (3) Any other value returns the leading m columns of Q
            and m rows of R
        
        edps is the increase in mp precision used for calculations
        
        **Examples**
        
            >>> from mpmath import *
            >>> mp.dps = 15
            >>> mp.pretty = True
            >>> A = matrix([[1, 2], [3, 4], [1, 1]])
            >>> Q, R = qr(A)
            >>> Q
            [-0.301511344577764   0.861640436855329   0.408248290463863]
            [-0.904534033733291  -0.123091490979333  -0.408248290463863]
            [-0.301511344577764  -0.492365963917331   0.816496580927726]
            >>> R
            [-3.3166247903554  -4.52267016866645]
            [             0.0  0.738548945875996]
            [             0.0                0.0]
            >>> Q * R
            [1.0  2.0]
            [3.0  4.0]
            [1.0  1.0]
            >>> chop(Q.T * Q)
            [1.0  0.0  0.0]
            [0.0  1.0  0.0]
            [0.0  0.0  1.0]
            >>> B = matrix([[1+0j, 2-3j], [3+j, 4+5j]])
            >>> Q, R = qr(B)
            >>> nprint(Q)
            [     (-0.301511 + 0.0j)   (0.0695795 - 0.95092j)]
            [(-0.904534 - 0.301511j)  (-0.115966 + 0.278318j)]
            >>> nprint(R)
            [(-3.31662 + 0.0j)  (-5.72872 - 2.41209j)]
            [              0.0       (3.91965 + 0.0j)]
            >>> Q * R
            [(1.0 + 0.0j)  (2.0 - 3.0j)]
            [(3.0 + 1.0j)  (4.0 + 5.0j)]
            >>> chop(Q.T * Q.conjugate())
            [1.0  0.0]
            [0.0  1.0]
        
        """
    @staticmethod
    def qr_solve(ctx, A, b, norm = None, **kwargs):
        """
        
        Ax = b => x, ||Ax - b||
        
        Solve a determined or overdetermined linear equations system and
        calculate the norm of the residual (error).
        QR decomposition using Householder factorization is applied, which gives very
        accurate results even for ill-conditioned matrices. qr_solve is twice as
        efficient.
        """
    @staticmethod
    def residual(ctx, A, x, b, **kwargs):
        """
        
        Calculate the residual of a solution to a linear equation system.
        
        r = A*x - b for A*x = b
        """
    @staticmethod
    def unitvector(ctx, n, i):
        """
        
        Return the i-th n-dimensional unit vector.
        """
