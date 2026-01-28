"""

The eigenvalue problem
----------------------

This file contains routines for the eigenvalue problem.

high level routines:

  hessenberg : reduction of a real or complex square matrix to upper Hessenberg form
  schur : reduction of a real or complex square matrix to upper Schur form
  eig : eigenvalues and eigenvectors of a real or complex square matrix

low level routines:

  hessenberg_reduce_0 : reduction of a real or complex square matrix to upper Hessenberg form
  hessenberg_reduce_1 : auxiliary routine to hessenberg_reduce_0
  qr_step : a single implicitly shifted QR step for an upper Hessenberg matrix
  hessenberg_qr : Schur decomposition of an upper Hessenberg matrix
  eig_tr_r : right eigenvectors of an upper triangular matrix
  eig_tr_l : left  eigenvectors of an upper triangular matrix
"""
from __future__ import annotations
from builtins import range as xrange
__all__: list[str] = ['Eigen', 'defun', 'eig', 'eig_sort', 'eig_tr_l', 'eig_tr_r', 'hessenberg', 'hessenberg_qr', 'hessenberg_reduce_0', 'hessenberg_reduce_1', 'qr_step', 'schur', 'xrange']
class Eigen:
    @staticmethod
    def eig(ctx, A, left = False, right = True, overwrite_a = False):
        """
        
        This routine computes the eigenvalues and optionally the left and right
        eigenvectors of a square matrix A. Given A, a vector E and matrices ER
        and EL are calculated such that
        
                            A ER[:,i] =         E[i] ER[:,i]
                    EL[i,:] A         = EL[i,:] E[i]
        
        E contains the eigenvalues of A. The columns of ER contain the right eigenvectors
        of A whereas the rows of EL contain the left eigenvectors.
        
        
        input:
          A           : a real or complex square matrix of shape (n, n)
          left        : if true, the left eigenvectors are calculated.
          right       : if true, the right eigenvectors are calculated.
          overwrite_a : if true, allows modification of A which may improve
                        performance. if false, A is not modified.
        
        output:
          E    : a list of length n containing the eigenvalues of A.
          ER   : a matrix whose columns contain the right eigenvectors of A.
          EL   : a matrix whose rows contain the left eigenvectors of A.
        
        return values:
           E            if left and right are both false.
          (E, ER)       if right is true and left is false.
          (E, EL)       if left is true and right is false.
          (E, EL, ER)   if left and right are true.
        
        
        examples:
          >>> from mpmath import mp
          >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
          >>> E, ER = mp.eig(A)
          >>> print(mp.chop(A * ER[:,0] - E[0] * ER[:,0]))
          [0.0]
          [0.0]
          [0.0]
        
          >>> E, EL, ER = mp.eig(A,left = True, right = True)
          >>> E, EL, ER = mp.eig_sort(E, EL, ER)
          >>> mp.nprint(E)
          [2.0, 4.0, 9.0]
          >>> print(mp.chop(A * ER[:,0] - E[0] * ER[:,0]))
          [0.0]
          [0.0]
          [0.0]
          >>> print(mp.chop( EL[0,:] * A - EL[0,:] * E[0]))
          [0.0  0.0  0.0]
        
        warning:
         - If there are multiple eigenvalues, the eigenvectors do not necessarily
           span the whole vectorspace, i.e. ER and EL may have not full rank.
           Furthermore in that case the eigenvectors are numerical ill-conditioned.
         - In the general case the eigenvalues have no natural order.
        
        see also:
          - eigh (or eigsy, eighe) for the symmetric eigenvalue problem.
          - eig_sort for sorting of eigenvalues and eigenvectors
        """
    @staticmethod
    def eig_sort(ctx, E, EL = False, ER = False, f = 'real'):
        """
        
        This routine sorts the eigenvalues and eigenvectors delivered by ``eig``.
        
        parameters:
          E  : the eigenvalues as delivered by eig
          EL : the left  eigenvectors as delivered by eig, or false
          ER : the right eigenvectors as delivered by eig, or false
          f  : either a string ("real" sort by increasing real part, "imag" sort by
               increasing imag part, "abs" sort by absolute value) or a function
               mapping complexs to the reals, i.e. ``f = lambda x: -mp.re(x) ``
               would sort the eigenvalues by decreasing real part.
        
        return values:
           E            if EL and ER are both false.
          (E, ER)       if ER is not false and left is false.
          (E, EL)       if EL is not false and right is false.
          (E, EL, ER)   if EL and ER are not false.
        
        example:
          >>> from mpmath import mp
          >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
          >>> E, EL, ER = mp.eig(A,left = True, right = True)
          >>> E, EL, ER = mp.eig_sort(E, EL, ER)
          >>> mp.nprint(E)
          [2.0, 4.0, 9.0]
          >>> E, EL, ER = mp.eig_sort(E, EL, ER,f = lambda x: -mp.re(x))
          >>> mp.nprint(E)
          [9.0, 4.0, 2.0]
          >>> print(mp.chop(A * ER[:,0] - E[0] * ER[:,0]))
          [0.0]
          [0.0]
          [0.0]
          >>> print(mp.chop( EL[0,:] * A - EL[0,:] * E[0]))
          [0.0  0.0  0.0]
        """
    @staticmethod
    def eigh(ctx, A, eigvals_only = False, overwrite_a = False):
        """
        
        "eigh" is a unified interface for "eigsy" and "eighe". Depending on
        whether A is real or complex the appropriate function is called.
        
        This routine solves the (ordinary) eigenvalue problem for a real symmetric
        or complex hermitian square matrix A. Given A, an orthogonal (A real) or
        unitary (A complex) matrix Q is calculated which diagonalizes A:
        
            Q' A Q = diag(E)               and                Q Q' = Q' Q = 1
        
        Here diag(E) a is diagonal matrix whose diagonal is E.
        ' denotes the hermitian transpose (i.e. ordinary transposition and
        complex conjugation).
        
        The columns of Q are the eigenvectors of A and E contains the eigenvalues:
        
            A Q[:,i] = E[i] Q[:,i]
        
        input:
        
          A: a real or complex square matrix of format (n,n) which is symmetric
             (i.e. A[i,j]=A[j,i]) or hermitian (i.e. A[i,j]=conj(A[j,i])).
        
          eigvals_only: if true, calculates only the eigenvalues E.
                        if false, calculates both eigenvectors and eigenvalues.
        
          overwrite_a: if true, allows modification of A which may improve
                       performance. if false, A is not modified.
        
        output:
        
          E: vector of format (n). contains the eigenvalues of A in ascending order.
        
          Q: an orthogonal or unitary matrix of format (n,n). contains the
             eigenvectors of A as columns.
        
        return value:
        
              E         if eigvals_only is true
             (E, Q)     if eigvals_only is false
        
        example:
          >>> from mpmath import mp
          >>> A = mp.matrix([[3, 2], [2, 0]])
          >>> E = mp.eigh(A, eigvals_only = True)
          >>> print(E)
          [-1.0]
          [ 4.0]
        
          >>> A = mp.matrix([[1, 2], [2, 3]])
          >>> E, Q = mp.eigh(A)
          >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
          [0.0]
          [0.0]
        
          >>> A = mp.matrix([[1, 2 + 5j], [2 - 5j, 3]])
          >>> E, Q = mp.eigh(A)
          >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
          [0.0]
          [0.0]
        
        see also: eigsy, eighe, eig
        """
    @staticmethod
    def eighe(ctx, A, eigvals_only = False, overwrite_a = False):
        """
        
        This routine solves the (ordinary) eigenvalue problem for a complex
        hermitian square matrix A. Given A, an unitary matrix Q is calculated which
        diagonalizes A:
        
            Q' A Q = diag(E)               and                Q Q' = Q' Q = 1
        
        Here diag(E) a is diagonal matrix whose diagonal is E.
        ' denotes the hermitian transpose (i.e. ordinary transposition and
        complex conjugation).
        
        The columns of Q are the eigenvectors of A and E contains the eigenvalues:
        
            A Q[:,i] = E[i] Q[:,i]
        
        
        input:
        
          A: complex matrix of format (n,n) which is hermitian
             (i.e. A=A' or A[i,j]=conj(A[j,i]))
        
          eigvals_only: if true, calculates only the eigenvalues E.
                        if false, calculates both eigenvectors and eigenvalues.
        
          overwrite_a: if true, allows modification of A which may improve
                       performance. if false, A is not modified.
        
        output:
        
          E: vector of format (n). contains the eigenvalues of A in ascending order.
        
          Q: unitary matrix of format (n,n). contains the eigenvectors
             of A as columns.
        
        return value:
        
               E         if eigvals_only is true
              (E, Q)     if eigvals_only is false
        
        example:
          >>> from mpmath import mp
          >>> A = mp.matrix([[1, -3 - 1j], [-3 + 1j, -2]])
          >>> E = mp.eighe(A, eigvals_only = True)
          >>> print(E)
          [-4.0]
          [ 3.0]
        
          >>> A = mp.matrix([[1, 2 + 5j], [2 - 5j, 3]])
          >>> E, Q = mp.eighe(A)
          >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
          [0.0]
          [0.0]
        
        see also: eigsy, eigh, eig
        """
    @staticmethod
    def eigsy(ctx, A, eigvals_only = False, overwrite_a = False):
        """
        
        This routine solves the (ordinary) eigenvalue problem for a real symmetric
        square matrix A. Given A, an orthogonal matrix Q is calculated which
        diagonalizes A:
        
              Q' A Q = diag(E)               and                Q Q' = Q' Q = 1
        
        Here diag(E) is a diagonal matrix whose diagonal is E.
        ' denotes the transpose.
        
        The columns of Q are the eigenvectors of A and E contains the eigenvalues:
        
              A Q[:,i] = E[i] Q[:,i]
        
        
        input:
        
          A: real matrix of format (n,n) which is symmetric
             (i.e. A=A' or A[i,j]=A[j,i])
        
          eigvals_only: if true, calculates only the eigenvalues E.
                        if false, calculates both eigenvectors and eigenvalues.
        
          overwrite_a: if true, allows modification of A which may improve
                       performance. if false, A is not modified.
        
        output:
        
          E: vector of format (n). contains the eigenvalues of A in ascending order.
        
          Q: orthogonal matrix of format (n,n). contains the eigenvectors
             of A as columns.
        
        return value:
        
              E          if eigvals_only is true
             (E, Q)      if eigvals_only is false
        
        example:
          >>> from mpmath import mp
          >>> A = mp.matrix([[3, 2], [2, 0]])
          >>> E = mp.eigsy(A, eigvals_only = True)
          >>> print(E)
          [-1.0]
          [ 4.0]
        
          >>> A = mp.matrix([[1, 2], [2, 3]])
          >>> E, Q = mp.eigsy(A)
          >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
          [0.0]
          [0.0]
        
        see also: eighe, eigh, eig
        """
    @staticmethod
    def gauss_quadrature(ctx, n, qtype = 'legendre', alpha = 0, beta = 0):
        """
        
        This routine calulates gaussian quadrature rules for different
        families of orthogonal polynomials. Let (a, b) be an interval,
        W(x) a positive weight function and n a positive integer.
        Then the purpose of this routine is to calculate pairs (x_k, w_k)
        for k=0, 1, 2, ... (n-1) which give
        
          int(W(x) * F(x), x = a..b) = sum(w_k * F(x_k),k = 0..(n-1))
        
        exact for all polynomials F(x) of degree (strictly) less than 2*n. For all
        integrable functions F(x) the sum is a (more or less) good approximation to
        the integral. The x_k are called nodes (which are the zeros of the
        related orthogonal polynomials) and the w_k are called the weights.
        
        parameters
           n        (input) The degree of the quadrature rule, i.e. its number of
                    nodes.
        
           qtype    (input) The family of orthogonal polynmomials for which to
                    compute the quadrature rule. See the list below.
        
           alpha    (input) real number, used as parameter for some orthogonal
                    polynomials
        
           beta     (input) real number, used as parameter for some orthogonal
                    polynomials.
        
        return value
        
          (X, W)    a pair of two real arrays where x_k = X[k] and w_k = W[k].
        
        
        orthogonal polynomials:
        
          qtype           polynomial
          -----           ----------
        
          "legendre"      Legendre polynomials, W(x)=1 on the interval (-1, +1)
          "legendre01"    shifted Legendre polynomials, W(x)=1 on the interval (0, +1)
          "hermite"       Hermite polynomials, W(x)=exp(-x*x) on (-infinity,+infinity)
          "laguerre"      Laguerre polynomials, W(x)=exp(-x) on (0,+infinity)
          "glaguerre"     generalized Laguerre polynomials, W(x)=exp(-x)*x**alpha
                          on (0, +infinity)
          "chebyshev1"    Chebyshev polynomials of the first kind, W(x)=1/sqrt(1-x*x)
                          on (-1, +1)
          "chebyshev2"    Chebyshev polynomials of the second kind, W(x)=sqrt(1-x*x)
                          on (-1, +1)
          "jacobi"        Jacobi polynomials, W(x)=(1-x)**alpha * (1+x)**beta on (-1, +1)
                          with alpha>-1 and beta>-1
        
        examples:
          >>> from mpmath import mp
          >>> f = lambda x: x**8 + 2 * x**6 - 3 * x**4 + 5 * x**2 - 7
          >>> X, W = mp.gauss_quadrature(5, "hermite")
          >>> A = mp.fdot([(f(x), w) for x, w in zip(X, W)])
          >>> B = mp.sqrt(mp.pi) * 57 / 16
          >>> C = mp.quad(lambda x: mp.exp(- x * x) * f(x), [-mp.inf, +mp.inf])
          >>> mp.nprint((mp.chop(A-B, tol = 1e-10), mp.chop(A-C, tol = 1e-10)))
          (0.0, 0.0)
        
          >>> f = lambda x: x**5 - 2 * x**4 + 3 * x**3 - 5 * x**2 + 7 * x - 11
          >>> X, W = mp.gauss_quadrature(3, "laguerre")
          >>> A = mp.fdot([(f(x), w) for x, w in zip(X, W)])
          >>> B = 76
          >>> C = mp.quad(lambda x: mp.exp(-x) * f(x), [0, +mp.inf])
          >>> mp.nprint(mp.chop(A-B, tol = 1e-10), mp.chop(A-C, tol = 1e-10))
          .0
        
          # orthogonality of the chebyshev polynomials:
          >>> f = lambda x: mp.chebyt(3, x) * mp.chebyt(2, x)
          >>> X, W = mp.gauss_quadrature(3, "chebyshev1")
          >>> A = mp.fdot([(f(x), w) for x, w in zip(X, W)])
          >>> print(mp.chop(A, tol = 1e-10))
          0.0
        
        references:
          - golub and welsch, "calculations of gaussian quadrature rules", mathematics of
            computation 23, p. 221-230 (1969)
          - golub, "some modified matrix eigenvalue problems", siam review 15, p. 318-334 (1973)
          - stroud and secrest, "gaussian quadrature formulas", prentice-hall (1966)
        
        See also the routine gaussq.f in netlog.org or ACM Transactions on
        Mathematical Software algorithm 726.
        """
    @staticmethod
    def hessenberg(ctx, A, overwrite_a = False):
        """
        
        This routine computes the Hessenberg decomposition of a square matrix A.
        Given A, an unitary matrix Q is determined such that
        
              Q' A Q = H                and               Q' Q = Q Q' = 1
        
        where H is an upper right Hessenberg matrix. Here ' denotes the hermitian
        transpose (i.e. transposition and conjugation).
        
        input:
          A            : a real or complex square matrix
          overwrite_a  : if true, allows modification of A which may improve
                         performance. if false, A is not modified.
        
        output:
          Q : an unitary matrix
          H : an upper right Hessenberg matrix
        
        example:
          >>> from mpmath import mp
          >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
          >>> Q, H = mp.hessenberg(A)
          >>> mp.nprint(H, 3) # doctest:+SKIP
          [  3.15  2.23  4.44]
          [-0.769  4.85  3.05]
          [   0.0  3.61   7.0]
          >>> print(mp.chop(A - Q * H * Q.transpose_conj()))
          [0.0  0.0  0.0]
          [0.0  0.0  0.0]
          [0.0  0.0  0.0]
        
        return value:   (Q, H)
        """
    @staticmethod
    def schur(ctx, A, overwrite_a = False):
        """
        
        This routine computes the Schur decomposition of a square matrix A.
        Given A, an unitary matrix Q is determined such that
        
              Q' A Q = R                and               Q' Q = Q Q' = 1
        
        where R is an upper right triangular matrix. Here ' denotes the
        hermitian transpose (i.e. transposition and conjugation).
        
        input:
          A            : a real or complex square matrix
          overwrite_a  : if true, allows modification of A which may improve
                         performance. if false, A is not modified.
        
        output:
          Q : an unitary matrix
          R : an upper right triangular matrix
        
        return value:   (Q, R)
        
        example:
          >>> from mpmath import mp
          >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
          >>> Q, R = mp.schur(A)
          >>> mp.nprint(R, 3) # doctest:+SKIP
          [2.0  0.417  -2.53]
          [0.0    4.0  -4.74]
          [0.0    0.0    9.0]
          >>> print(mp.chop(A - Q * R * Q.transpose_conj()))
          [0.0  0.0  0.0]
          [0.0  0.0  0.0]
          [0.0  0.0  0.0]
        
        warning: The Schur decomposition is not unique.
        """
    @staticmethod
    def svd(ctx, A, full_matrices = False, compute_uv = True, overwrite_a = False):
        """
        
        "svd" is a unified interface for "svd_r" and "svd_c". Depending on
        whether A is real or complex the appropriate function is called.
        
        This routine computes the singular value decomposition of a matrix A.
        Given A, two orthogonal (A real) or unitary (A complex) matrices U and V
        are calculated such that
        
               A = U S V        and        U' U = 1         and         V V' = 1
        
        where S is a suitable shaped matrix whose off-diagonal elements are zero.
        Here ' denotes the hermitian transpose (i.e. transposition and complex
        conjugation). The diagonal elements of S are the singular values of A,
        i.e. the squareroots of the eigenvalues of A' A or A A'.
        
        input:
          A             : a real or complex matrix of shape (m, n)
          full_matrices : if true, U and V are of shape (m, m) and (n, n).
                          if false, U and V are of shape (m, min(m, n)) and (min(m, n), n).
          compute_uv    : if true, U and V are calculated. if false, only S is calculated.
          overwrite_a   : if true, allows modification of A which may improve
                          performance. if false, A is not modified.
        
        output:
          U : an orthogonal or unitary matrix: U' U = 1. if full_matrices is true, U is of
              shape (m, m). ortherwise it is of shape (m, min(m, n)).
        
          S : an array of length min(m, n) containing the singular values of A sorted by
              decreasing magnitude.
        
          V : an orthogonal or unitary matrix: V V' = 1. if full_matrices is true, V is of
              shape (n, n). ortherwise it is of shape (min(m, n), n).
        
        return value:
        
               S          if compute_uv is false
           (U, S, V)      if compute_uv is true
        
        overview of the matrices:
        
          full_matrices true:
            A           : m*n
            U           : m*m     U' U  = 1
            S as matrix : m*n
            V           : n*n     V  V' = 1
        
         full_matrices false:
            A           : m*n
            U           : m*min(n,m)             U' U  = 1
            S as matrix : min(m,n)*min(m,n)
            V           : min(m,n)*n             V  V' = 1
        
        examples:
        
           >>> from mpmath import mp
           >>> A = mp.matrix([[2, -2, -1], [3, 4, -2], [-2, -2, 0]])
           >>> S = mp.svd(A, compute_uv = False)
           >>> print(S)
           [6.0]
           [3.0]
           [1.0]
        
           >>> U, S, V = mp.svd(A)
           >>> print(mp.chop(A - U * mp.diag(S) * V))
           [0.0  0.0  0.0]
           [0.0  0.0  0.0]
           [0.0  0.0  0.0]
        
        see also: svd_r, svd_c
        """
    @staticmethod
    def svd_c(ctx, A, full_matrices = False, compute_uv = True, overwrite_a = False):
        """
        
        This routine computes the singular value decomposition of a matrix A.
        Given A, two unitary matrices U and V are calculated such that
        
               A = U S V        and        U' U = 1         and         V V' = 1
        
        where S is a suitable shaped matrix whose off-diagonal elements are zero.
        Here ' denotes the hermitian transpose (i.e. transposition and complex
        conjugation). The diagonal elements of S are the singular values of A,
        i.e. the squareroots of the eigenvalues of A' A or A A'.
        
        input:
          A             : a complex matrix of shape (m, n)
          full_matrices : if true, U and V are of shape (m, m) and (n, n).
                          if false, U and V are of shape (m, min(m, n)) and (min(m, n), n).
          compute_uv    : if true, U and V are calculated. if false, only S is calculated.
          overwrite_a   : if true, allows modification of A which may improve
                          performance. if false, A is not modified.
        
        output:
          U : an unitary matrix: U' U = 1. if full_matrices is true, U is of
              shape (m, m). ortherwise it is of shape (m, min(m, n)).
        
          S : an array of length min(m, n) containing the singular values of A sorted by
              decreasing magnitude.
        
          V : an unitary matrix: V V' = 1. if full_matrices is true, V is of
              shape (n, n). ortherwise it is of shape (min(m, n), n).
        
        return value:
        
               S          if compute_uv is false
           (U, S, V)      if compute_uv is true
        
        overview of the matrices:
        
          full_matrices true:
            A           : m*n
            U           : m*m     U' U  = 1
            S as matrix : m*n
            V           : n*n     V  V' = 1
        
         full_matrices false:
            A           : m*n
            U           : m*min(n,m)             U' U  = 1
            S as matrix : min(m,n)*min(m,n)
            V           : min(m,n)*n             V  V' = 1
        
        example:
          >>> from mpmath import mp
          >>> A = mp.matrix([[-2j, -1-3j, -2+2j], [2-2j, -1-3j, 1], [-3+1j,-2j,0]])
          >>> S = mp.svd_c(A, compute_uv = False)
          >>> print(mp.chop(S - mp.matrix([mp.sqrt(34), mp.sqrt(15), mp.sqrt(6)])))
          [0.0]
          [0.0]
          [0.0]
        
          >>> U, S, V = mp.svd_c(A)
          >>> print(mp.chop(A - U * mp.diag(S) * V))
          [0.0  0.0  0.0]
          [0.0  0.0  0.0]
          [0.0  0.0  0.0]
        
        see also: svd, svd_r
        """
    @staticmethod
    def svd_r(ctx, A, full_matrices = False, compute_uv = True, overwrite_a = False):
        """
        
        This routine computes the singular value decomposition of a matrix A.
        Given A, two orthogonal matrices U and V are calculated such that
        
               A = U S V        and        U' U = 1         and         V V' = 1
        
        where S is a suitable shaped matrix whose off-diagonal elements are zero.
        Here ' denotes the transpose. The diagonal elements of S are the singular
        values of A, i.e. the squareroots of the eigenvalues of A' A or A A'.
        
        input:
          A             : a real matrix of shape (m, n)
          full_matrices : if true, U and V are of shape (m, m) and (n, n).
                          if false, U and V are of shape (m, min(m, n)) and (min(m, n), n).
          compute_uv    : if true, U and V are calculated. if false, only S is calculated.
          overwrite_a   : if true, allows modification of A which may improve
                          performance. if false, A is not modified.
        
        output:
          U : an orthogonal matrix: U' U = 1. if full_matrices is true, U is of
              shape (m, m). ortherwise it is of shape (m, min(m, n)).
        
          S : an array of length min(m, n) containing the singular values of A sorted by
              decreasing magnitude.
        
          V : an orthogonal matrix: V V' = 1. if full_matrices is true, V is of
              shape (n, n). ortherwise it is of shape (min(m, n), n).
        
        return value:
        
               S          if compute_uv is false
           (U, S, V)      if compute_uv is true
        
        overview of the matrices:
        
          full_matrices true:
            A           : m*n
            U           : m*m     U' U  = 1
            S as matrix : m*n
            V           : n*n     V  V' = 1
        
         full_matrices false:
            A           : m*n
            U           : m*min(n,m)             U' U  = 1
            S as matrix : min(m,n)*min(m,n)
            V           : min(m,n)*n             V  V' = 1
        
        examples:
        
           >>> from mpmath import mp
           >>> A = mp.matrix([[2, -2, -1], [3, 4, -2], [-2, -2, 0]])
           >>> S = mp.svd_r(A, compute_uv = False)
           >>> print(S)
           [6.0]
           [3.0]
           [1.0]
        
           >>> U, S, V = mp.svd_r(A)
           >>> print(mp.chop(A - U * mp.diag(S) * V))
           [0.0  0.0  0.0]
           [0.0  0.0  0.0]
           [0.0  0.0  0.0]
        
        
        see also: svd, svd_c
        """
def defun(f):
    ...
def eig(ctx, A, left = False, right = True, overwrite_a = False):
    """
    
    This routine computes the eigenvalues and optionally the left and right
    eigenvectors of a square matrix A. Given A, a vector E and matrices ER
    and EL are calculated such that
    
                        A ER[:,i] =         E[i] ER[:,i]
                EL[i,:] A         = EL[i,:] E[i]
    
    E contains the eigenvalues of A. The columns of ER contain the right eigenvectors
    of A whereas the rows of EL contain the left eigenvectors.
    
    
    input:
      A           : a real or complex square matrix of shape (n, n)
      left        : if true, the left eigenvectors are calculated.
      right       : if true, the right eigenvectors are calculated.
      overwrite_a : if true, allows modification of A which may improve
                    performance. if false, A is not modified.
    
    output:
      E    : a list of length n containing the eigenvalues of A.
      ER   : a matrix whose columns contain the right eigenvectors of A.
      EL   : a matrix whose rows contain the left eigenvectors of A.
    
    return values:
       E            if left and right are both false.
      (E, ER)       if right is true and left is false.
      (E, EL)       if left is true and right is false.
      (E, EL, ER)   if left and right are true.
    
    
    examples:
      >>> from mpmath import mp
      >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
      >>> E, ER = mp.eig(A)
      >>> print(mp.chop(A * ER[:,0] - E[0] * ER[:,0]))
      [0.0]
      [0.0]
      [0.0]
    
      >>> E, EL, ER = mp.eig(A,left = True, right = True)
      >>> E, EL, ER = mp.eig_sort(E, EL, ER)
      >>> mp.nprint(E)
      [2.0, 4.0, 9.0]
      >>> print(mp.chop(A * ER[:,0] - E[0] * ER[:,0]))
      [0.0]
      [0.0]
      [0.0]
      >>> print(mp.chop( EL[0,:] * A - EL[0,:] * E[0]))
      [0.0  0.0  0.0]
    
    warning:
     - If there are multiple eigenvalues, the eigenvectors do not necessarily
       span the whole vectorspace, i.e. ER and EL may have not full rank.
       Furthermore in that case the eigenvectors are numerical ill-conditioned.
     - In the general case the eigenvalues have no natural order.
    
    see also:
      - eigh (or eigsy, eighe) for the symmetric eigenvalue problem.
      - eig_sort for sorting of eigenvalues and eigenvectors
    """
def eig_sort(ctx, E, EL = False, ER = False, f = 'real'):
    """
    
    This routine sorts the eigenvalues and eigenvectors delivered by ``eig``.
    
    parameters:
      E  : the eigenvalues as delivered by eig
      EL : the left  eigenvectors as delivered by eig, or false
      ER : the right eigenvectors as delivered by eig, or false
      f  : either a string ("real" sort by increasing real part, "imag" sort by
           increasing imag part, "abs" sort by absolute value) or a function
           mapping complexs to the reals, i.e. ``f = lambda x: -mp.re(x) ``
           would sort the eigenvalues by decreasing real part.
    
    return values:
       E            if EL and ER are both false.
      (E, ER)       if ER is not false and left is false.
      (E, EL)       if EL is not false and right is false.
      (E, EL, ER)   if EL and ER are not false.
    
    example:
      >>> from mpmath import mp
      >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
      >>> E, EL, ER = mp.eig(A,left = True, right = True)
      >>> E, EL, ER = mp.eig_sort(E, EL, ER)
      >>> mp.nprint(E)
      [2.0, 4.0, 9.0]
      >>> E, EL, ER = mp.eig_sort(E, EL, ER,f = lambda x: -mp.re(x))
      >>> mp.nprint(E)
      [9.0, 4.0, 2.0]
      >>> print(mp.chop(A * ER[:,0] - E[0] * ER[:,0]))
      [0.0]
      [0.0]
      [0.0]
      >>> print(mp.chop( EL[0,:] * A - EL[0,:] * E[0]))
      [0.0  0.0  0.0]
    """
def eig_tr_l(ctx, A):
    """
    
    This routine calculates the left eigenvectors of an upper right triangular matrix.
    
    input:
      A      an upper right triangular matrix
    
    output:
      EL     a matrix whose rows form the left eigenvectors of A
    
    return value:  EL
    """
def eig_tr_r(ctx, A):
    """
    
    This routine calculates the right eigenvectors of an upper right triangular matrix.
    
    input:
      A      an upper right triangular matrix
    
    output:
      ER     a matrix whose columns form the right eigenvectors of A
    
    return value: ER
    """
def hessenberg(ctx, A, overwrite_a = False):
    """
    
    This routine computes the Hessenberg decomposition of a square matrix A.
    Given A, an unitary matrix Q is determined such that
    
          Q' A Q = H                and               Q' Q = Q Q' = 1
    
    where H is an upper right Hessenberg matrix. Here ' denotes the hermitian
    transpose (i.e. transposition and conjugation).
    
    input:
      A            : a real or complex square matrix
      overwrite_a  : if true, allows modification of A which may improve
                     performance. if false, A is not modified.
    
    output:
      Q : an unitary matrix
      H : an upper right Hessenberg matrix
    
    example:
      >>> from mpmath import mp
      >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
      >>> Q, H = mp.hessenberg(A)
      >>> mp.nprint(H, 3) # doctest:+SKIP
      [  3.15  2.23  4.44]
      [-0.769  4.85  3.05]
      [   0.0  3.61   7.0]
      >>> print(mp.chop(A - Q * H * Q.transpose_conj()))
      [0.0  0.0  0.0]
      [0.0  0.0  0.0]
      [0.0  0.0  0.0]
    
    return value:   (Q, H)
    """
def hessenberg_qr(ctx, A, Q):
    """
    
    This routine computes the Schur decomposition of an upper Hessenberg matrix A.
    Given A, an unitary matrix Q is determined such that
    
          Q' A Q = R                   and                  Q' Q = Q Q' = 1
    
    where R is an upper right triangular matrix. Here ' denotes the hermitian
    transpose (i.e. transposition and conjugation).
    
    parameters:
      A         (input/output) On input, A contains an upper Hessenberg matrix.
                On output, A is replace by the upper right triangluar matrix R.
    
      Q         (input/output) The parameter Q is multiplied by the unitary
                matrix Q arising from the Schur decomposition. Q can also be
                false, in which case the unitary matrix Q is not computated.
    """
def hessenberg_reduce_0(ctx, A, T):
    """
    
    This routine computes the (upper) Hessenberg decomposition of a square matrix A.
    Given A, an unitary matrix Q is calculated such that
    
               Q' A Q = H              and             Q' Q = Q Q' = 1
    
    where H is an upper Hessenberg matrix, meaning that it only contains zeros
    below the first subdiagonal. Here ' denotes the hermitian transpose (i.e.
    transposition and conjugation).
    
    parameters:
      A         (input/output) On input, A contains the square matrix A of
                dimension (n,n). On output, A contains a compressed representation
                of Q and H.
      T         (output) An array of length n containing the first elements of
                the Householder reflectors.
    """
def hessenberg_reduce_1(ctx, A, T):
    """
    
    This routine forms the unitary matrix Q described in hessenberg_reduce_0.
    
    parameters:
      A    (input/output) On input, A is the same matrix as delivered by
           hessenberg_reduce_0. On output, A is set to Q.
    
      T    (input) On input, T is the same array as delivered by hessenberg_reduce_0.
    """
def qr_step(ctx, n0, n1, A, Q, shift):
    """
    
    This subroutine executes a single implicitly shifted QR step applied to an
    upper Hessenberg matrix A. Given A and shift as input, first an QR
    decomposition is calculated:
    
      Q R = A - shift * 1 .
    
    The output is then following matrix:
    
      R Q + shift * 1
    
    parameters:
      n0, n1    (input) Two integers which specify the submatrix A[n0:n1,n0:n1]
                on which this subroutine operators. The subdiagonal elements
                to the left and below this submatrix must be deflated (i.e. zero).
                following restriction is imposed: n1>=n0+2
      A         (input/output) On input, A is an upper Hessenberg matrix.
                On output, A is replaced by "R Q + shift * 1"
      Q         (input/output) The parameter Q is multiplied by the unitary matrix
                Q arising from the QR decomposition. Q can also be false, in which
                case the unitary matrix Q is not computated.
      shift     (input) a complex number specifying the shift. idealy close to an
                eigenvalue of the bottemmost part of the submatrix A[n0:n1,n0:n1].
    
    references:
      Stoer, Bulirsch - Introduction to Numerical Analysis.
      Kresser : Numerical Methods for General and Structured Eigenvalue Problems
    """
def schur(ctx, A, overwrite_a = False):
    """
    
    This routine computes the Schur decomposition of a square matrix A.
    Given A, an unitary matrix Q is determined such that
    
          Q' A Q = R                and               Q' Q = Q Q' = 1
    
    where R is an upper right triangular matrix. Here ' denotes the
    hermitian transpose (i.e. transposition and conjugation).
    
    input:
      A            : a real or complex square matrix
      overwrite_a  : if true, allows modification of A which may improve
                     performance. if false, A is not modified.
    
    output:
      Q : an unitary matrix
      R : an upper right triangular matrix
    
    return value:   (Q, R)
    
    example:
      >>> from mpmath import mp
      >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
      >>> Q, R = mp.schur(A)
      >>> mp.nprint(R, 3) # doctest:+SKIP
      [2.0  0.417  -2.53]
      [0.0    4.0  -4.74]
      [0.0    0.0    9.0]
      >>> print(mp.chop(A - Q * R * Q.transpose_conj()))
      [0.0  0.0  0.0]
      [0.0  0.0  0.0]
      [0.0  0.0  0.0]
    
    warning: The Schur decomposition is not unique.
    """
