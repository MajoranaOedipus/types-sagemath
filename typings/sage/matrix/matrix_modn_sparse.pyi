import sage.matrix.matrix_sparse
from sage.arith.misc import is_prime as is_prime
from sage.categories.category import ZZ as ZZ
from sage.matrix.matrix2 import Matrix2 as Matrix2
from sage.misc.verbose import get_verbose as get_verbose, verbose as verbose
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

MAX_MODULUS: int

class Matrix_modn_sparse(sage.matrix.matrix_sparse.Matrix_sparse):
    """Matrix_modn_sparse(parent, entries=None, copy=None, bool coerce=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    p: p
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 153)

                Create a sparse matrix over the integers modulo ``n``.

                INPUT:

                - ``parent`` -- a matrix space over the integers modulo ``n``

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``False``, assume without checking that the
                  entries lie in the base ring
        """
    @overload
    def density(self) -> Any:
        """Matrix_modn_sparse.density(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 544)

        Return the density of ``self``, i.e., the ratio of the number of
        nonzero entries of ``self`` to the total size of ``self``.

        EXAMPLES::

            sage: A = matrix(QQ,3,3,[0,1,2,3,0,0,6,7,8],sparse=True)
            sage: A.density()
            2/3

        Notice that the density parameter does not ensure the density
        of a matrix; it is only an upper bound.

        ::

            sage: A = random_matrix(GF(127), 200, 200, density=0.3, sparse=True)
            sage: density_sum = float(A.density())
            sage: total = 1
            sage: expected_density = 1.0 - (199/200)^60
            sage: expected_density
            0.2597...
            sage: while abs(density_sum/total - expected_density) > 0.001:
            ....:     A = random_matrix(GF(127), 200, 200, density=0.3, sparse=True)
            ....:     density_sum += float(A.density())
            ....:     total += 1"""
    @overload
    def density(self) -> Any:
        """Matrix_modn_sparse.density(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 544)

        Return the density of ``self``, i.e., the ratio of the number of
        nonzero entries of ``self`` to the total size of ``self``.

        EXAMPLES::

            sage: A = matrix(QQ,3,3,[0,1,2,3,0,0,6,7,8],sparse=True)
            sage: A.density()
            2/3

        Notice that the density parameter does not ensure the density
        of a matrix; it is only an upper bound.

        ::

            sage: A = random_matrix(GF(127), 200, 200, density=0.3, sparse=True)
            sage: density_sum = float(A.density())
            sage: total = 1
            sage: expected_density = 1.0 - (199/200)^60
            sage: expected_density
            0.2597...
            sage: while abs(density_sum/total - expected_density) > 0.001:
            ....:     A = random_matrix(GF(127), 200, 200, density=0.3, sparse=True)
            ....:     density_sum += float(A.density())
            ....:     total += 1"""
    @overload
    def density(self) -> Any:
        """Matrix_modn_sparse.density(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 544)

        Return the density of ``self``, i.e., the ratio of the number of
        nonzero entries of ``self`` to the total size of ``self``.

        EXAMPLES::

            sage: A = matrix(QQ,3,3,[0,1,2,3,0,0,6,7,8],sparse=True)
            sage: A.density()
            2/3

        Notice that the density parameter does not ensure the density
        of a matrix; it is only an upper bound.

        ::

            sage: A = random_matrix(GF(127), 200, 200, density=0.3, sparse=True)
            sage: density_sum = float(A.density())
            sage: total = 1
            sage: expected_density = 1.0 - (199/200)^60
            sage: expected_density
            0.2597...
            sage: while abs(density_sum/total - expected_density) > 0.001:
            ....:     A = random_matrix(GF(127), 200, 200, density=0.3, sparse=True)
            ....:     density_sum += float(A.density())
            ....:     total += 1"""
    @overload
    def density(self) -> Any:
        """Matrix_modn_sparse.density(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 544)

        Return the density of ``self``, i.e., the ratio of the number of
        nonzero entries of ``self`` to the total size of ``self``.

        EXAMPLES::

            sage: A = matrix(QQ,3,3,[0,1,2,3,0,0,6,7,8],sparse=True)
            sage: A.density()
            2/3

        Notice that the density parameter does not ensure the density
        of a matrix; it is only an upper bound.

        ::

            sage: A = random_matrix(GF(127), 200, 200, density=0.3, sparse=True)
            sage: density_sum = float(A.density())
            sage: total = 1
            sage: expected_density = 1.0 - (199/200)^60
            sage: expected_density
            0.2597...
            sage: while abs(density_sum/total - expected_density) > 0.001:
            ....:     A = random_matrix(GF(127), 200, 200, density=0.3, sparse=True)
            ....:     density_sum += float(A.density())
            ....:     total += 1"""
    def determinant(self, algorithm=...) -> Any:
        """Matrix_modn_sparse.determinant(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 839)

        Return the determinant of this matrix.

        INPUT:

        - ``algorithm`` -- either ``'linbox'`` (default) or ``'generic'``

        EXAMPLES::

            sage: A = matrix(GF(3), 4, range(16), sparse=True)
            sage: B = identity_matrix(GF(3), 4, sparse=True)
            sage: (A + B).det()
            2
            sage: (A + B).det(algorithm='linbox')
            2
            sage: (A + B).det(algorithm='generic')
            2
            sage: (A + B).det(algorithm='hey')
            Traceback (most recent call last):
            ...
            ValueError: no algorithm 'hey'

            sage: matrix(GF(11), 1, 2, sparse=True).det()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

        TESTS::

            sage: matrix(GF(3), 0, sparse=True).det(algorithm='generic')
            1
            sage: matrix(GF(3), 0, sparse=True).det(algorithm='linbox')
            1

            sage: for _ in range(100):
            ....:     dim = randint(0, 50)
            ....:     p = random_prime(10000)
            ....:     M = MatrixSpace(GF(p), dim, sparse=True)
            ....:     m = M.random_element()
            ....:     det_linbox = m.det(algorithm='linbox')
            ....:     det_generic = m.det(algorithm='generic')
            ....:     assert parent(det_linbox) == m.base_ring()
            ....:     assert parent(det_generic) == m.base_ring()
            ....:     if det_linbox != det_generic:
            ....:         print(m)
            ....:         raise RuntimeError"""
    def matrix_from_columns(self, cols) -> Any:
        """Matrix_modn_sparse.matrix_from_columns(self, cols)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 657)

        Return the matrix constructed from ``self`` using columns with indices
        in the columns list.

        EXAMPLES::

            sage: M = MatrixSpace(GF(127),3,3,sparse=True)
            sage: A = M(range(9)); A
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: A.matrix_from_columns([2,1])
            [2 1]
            [5 4]
            [8 7]"""
    def matrix_from_rows(self, rows) -> Any:
        """Matrix_modn_sparse.matrix_from_rows(self, rows)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 616)

        Return the matrix constructed from ``self`` using rows with indices in
        the rows list.

        INPUT:

        - ``rows`` -- list or tuple of row indices

        EXAMPLES::

            sage: M = MatrixSpace(GF(127),3,3,sparse=True)
            sage: A = M(range(9)); A
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: A.matrix_from_rows([2,1])
            [6 7 8]
            [3 4 5]"""
    @overload
    def rank(self, algorithm=...) -> Any:
        """Matrix_modn_sparse.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 755)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- either ``'linbox'`` (only available for
          matrices over prime fields) or ``'generic'``

        EXAMPLES::

            sage: A = matrix(GF(127), 2, 2, sparse=True)
            sage: A[0,0] = 34
            sage: A[0,1] = 102
            sage: A[1,0] = 55
            sage: A[1,1] = 74
            sage: A.rank()
            2

            sage: A._clear_cache()
            sage: A.rank(algorithm='generic')
            2
            sage: A._clear_cache()
            sage: A.rank(algorithm='hey')
            Traceback (most recent call last):
            ...
            ValueError: no algorithm 'hey'

        TESTS::

            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='generic')
            0
            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='linbox')
            0

            sage: for _ in range(50):
            ....:     nrows = randint(0, 100)
            ....:     ncols = randint(0, 100)
            ....:     p = random_prime(10000)
            ....:     M = MatrixSpace(GF(p), nrows, ncols, sparse=True)
            ....:     m = M.random_element()
            ....:     rank_linbox = m.rank(algorithm='linbox')
            ....:     rank_generic = m.rank(algorithm='generic')
            ....:     if rank_linbox != rank_generic:
            ....:         print(m)
            ....:         raise RuntimeError

        REFERENCES:

        - Jean-Guillaume Dumas and Gilles Villars. 'Computing the Rank
          of Large Sparse Matrices over Finite
          Fields'. Proc. CASC'2002, The Fifth International Workshop
          on Computer Algebra in Scientific Computing, Big Yalta,
          Crimea, Ukraine, 22-27 sept. 2002, Springer-Verlag,
          http://perso.ens-lyon.fr/gilles.villard/BIBLIOGRAPHIE/POSTSCRIPT/rankjgd.ps

        .. NOTE::

           For very sparse matrices Gaussian elimination is faster
           because it barely has anything to do. If the fill in needs to
           be considered, 'Symbolic Reordering' is usually much faster."""
    @overload
    def rank(self) -> Any:
        """Matrix_modn_sparse.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 755)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- either ``'linbox'`` (only available for
          matrices over prime fields) or ``'generic'``

        EXAMPLES::

            sage: A = matrix(GF(127), 2, 2, sparse=True)
            sage: A[0,0] = 34
            sage: A[0,1] = 102
            sage: A[1,0] = 55
            sage: A[1,1] = 74
            sage: A.rank()
            2

            sage: A._clear_cache()
            sage: A.rank(algorithm='generic')
            2
            sage: A._clear_cache()
            sage: A.rank(algorithm='hey')
            Traceback (most recent call last):
            ...
            ValueError: no algorithm 'hey'

        TESTS::

            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='generic')
            0
            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='linbox')
            0

            sage: for _ in range(50):
            ....:     nrows = randint(0, 100)
            ....:     ncols = randint(0, 100)
            ....:     p = random_prime(10000)
            ....:     M = MatrixSpace(GF(p), nrows, ncols, sparse=True)
            ....:     m = M.random_element()
            ....:     rank_linbox = m.rank(algorithm='linbox')
            ....:     rank_generic = m.rank(algorithm='generic')
            ....:     if rank_linbox != rank_generic:
            ....:         print(m)
            ....:         raise RuntimeError

        REFERENCES:

        - Jean-Guillaume Dumas and Gilles Villars. 'Computing the Rank
          of Large Sparse Matrices over Finite
          Fields'. Proc. CASC'2002, The Fifth International Workshop
          on Computer Algebra in Scientific Computing, Big Yalta,
          Crimea, Ukraine, 22-27 sept. 2002, Springer-Verlag,
          http://perso.ens-lyon.fr/gilles.villard/BIBLIOGRAPHIE/POSTSCRIPT/rankjgd.ps

        .. NOTE::

           For very sparse matrices Gaussian elimination is faster
           because it barely has anything to do. If the fill in needs to
           be considered, 'Symbolic Reordering' is usually much faster."""
    @overload
    def rank(self, algorithm=...) -> Any:
        """Matrix_modn_sparse.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 755)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- either ``'linbox'`` (only available for
          matrices over prime fields) or ``'generic'``

        EXAMPLES::

            sage: A = matrix(GF(127), 2, 2, sparse=True)
            sage: A[0,0] = 34
            sage: A[0,1] = 102
            sage: A[1,0] = 55
            sage: A[1,1] = 74
            sage: A.rank()
            2

            sage: A._clear_cache()
            sage: A.rank(algorithm='generic')
            2
            sage: A._clear_cache()
            sage: A.rank(algorithm='hey')
            Traceback (most recent call last):
            ...
            ValueError: no algorithm 'hey'

        TESTS::

            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='generic')
            0
            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='linbox')
            0

            sage: for _ in range(50):
            ....:     nrows = randint(0, 100)
            ....:     ncols = randint(0, 100)
            ....:     p = random_prime(10000)
            ....:     M = MatrixSpace(GF(p), nrows, ncols, sparse=True)
            ....:     m = M.random_element()
            ....:     rank_linbox = m.rank(algorithm='linbox')
            ....:     rank_generic = m.rank(algorithm='generic')
            ....:     if rank_linbox != rank_generic:
            ....:         print(m)
            ....:         raise RuntimeError

        REFERENCES:

        - Jean-Guillaume Dumas and Gilles Villars. 'Computing the Rank
          of Large Sparse Matrices over Finite
          Fields'. Proc. CASC'2002, The Fifth International Workshop
          on Computer Algebra in Scientific Computing, Big Yalta,
          Crimea, Ukraine, 22-27 sept. 2002, Springer-Verlag,
          http://perso.ens-lyon.fr/gilles.villard/BIBLIOGRAPHIE/POSTSCRIPT/rankjgd.ps

        .. NOTE::

           For very sparse matrices Gaussian elimination is faster
           because it barely has anything to do. If the fill in needs to
           be considered, 'Symbolic Reordering' is usually much faster."""
    @overload
    def rank(self, algorithm=...) -> Any:
        """Matrix_modn_sparse.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 755)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- either ``'linbox'`` (only available for
          matrices over prime fields) or ``'generic'``

        EXAMPLES::

            sage: A = matrix(GF(127), 2, 2, sparse=True)
            sage: A[0,0] = 34
            sage: A[0,1] = 102
            sage: A[1,0] = 55
            sage: A[1,1] = 74
            sage: A.rank()
            2

            sage: A._clear_cache()
            sage: A.rank(algorithm='generic')
            2
            sage: A._clear_cache()
            sage: A.rank(algorithm='hey')
            Traceback (most recent call last):
            ...
            ValueError: no algorithm 'hey'

        TESTS::

            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='generic')
            0
            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='linbox')
            0

            sage: for _ in range(50):
            ....:     nrows = randint(0, 100)
            ....:     ncols = randint(0, 100)
            ....:     p = random_prime(10000)
            ....:     M = MatrixSpace(GF(p), nrows, ncols, sparse=True)
            ....:     m = M.random_element()
            ....:     rank_linbox = m.rank(algorithm='linbox')
            ....:     rank_generic = m.rank(algorithm='generic')
            ....:     if rank_linbox != rank_generic:
            ....:         print(m)
            ....:         raise RuntimeError

        REFERENCES:

        - Jean-Guillaume Dumas and Gilles Villars. 'Computing the Rank
          of Large Sparse Matrices over Finite
          Fields'. Proc. CASC'2002, The Fifth International Workshop
          on Computer Algebra in Scientific Computing, Big Yalta,
          Crimea, Ukraine, 22-27 sept. 2002, Springer-Verlag,
          http://perso.ens-lyon.fr/gilles.villard/BIBLIOGRAPHIE/POSTSCRIPT/rankjgd.ps

        .. NOTE::

           For very sparse matrices Gaussian elimination is faster
           because it barely has anything to do. If the fill in needs to
           be considered, 'Symbolic Reordering' is usually much faster."""
    @overload
    def rank(self, algorithm=...) -> Any:
        """Matrix_modn_sparse.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 755)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- either ``'linbox'`` (only available for
          matrices over prime fields) or ``'generic'``

        EXAMPLES::

            sage: A = matrix(GF(127), 2, 2, sparse=True)
            sage: A[0,0] = 34
            sage: A[0,1] = 102
            sage: A[1,0] = 55
            sage: A[1,1] = 74
            sage: A.rank()
            2

            sage: A._clear_cache()
            sage: A.rank(algorithm='generic')
            2
            sage: A._clear_cache()
            sage: A.rank(algorithm='hey')
            Traceback (most recent call last):
            ...
            ValueError: no algorithm 'hey'

        TESTS::

            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='generic')
            0
            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='linbox')
            0

            sage: for _ in range(50):
            ....:     nrows = randint(0, 100)
            ....:     ncols = randint(0, 100)
            ....:     p = random_prime(10000)
            ....:     M = MatrixSpace(GF(p), nrows, ncols, sparse=True)
            ....:     m = M.random_element()
            ....:     rank_linbox = m.rank(algorithm='linbox')
            ....:     rank_generic = m.rank(algorithm='generic')
            ....:     if rank_linbox != rank_generic:
            ....:         print(m)
            ....:         raise RuntimeError

        REFERENCES:

        - Jean-Guillaume Dumas and Gilles Villars. 'Computing the Rank
          of Large Sparse Matrices over Finite
          Fields'. Proc. CASC'2002, The Fifth International Workshop
          on Computer Algebra in Scientific Computing, Big Yalta,
          Crimea, Ukraine, 22-27 sept. 2002, Springer-Verlag,
          http://perso.ens-lyon.fr/gilles.villard/BIBLIOGRAPHIE/POSTSCRIPT/rankjgd.ps

        .. NOTE::

           For very sparse matrices Gaussian elimination is faster
           because it barely has anything to do. If the fill in needs to
           be considered, 'Symbolic Reordering' is usually much faster."""
    @overload
    def rank(self, algorithm=...) -> Any:
        """Matrix_modn_sparse.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 755)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- either ``'linbox'`` (only available for
          matrices over prime fields) or ``'generic'``

        EXAMPLES::

            sage: A = matrix(GF(127), 2, 2, sparse=True)
            sage: A[0,0] = 34
            sage: A[0,1] = 102
            sage: A[1,0] = 55
            sage: A[1,1] = 74
            sage: A.rank()
            2

            sage: A._clear_cache()
            sage: A.rank(algorithm='generic')
            2
            sage: A._clear_cache()
            sage: A.rank(algorithm='hey')
            Traceback (most recent call last):
            ...
            ValueError: no algorithm 'hey'

        TESTS::

            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='generic')
            0
            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='linbox')
            0

            sage: for _ in range(50):
            ....:     nrows = randint(0, 100)
            ....:     ncols = randint(0, 100)
            ....:     p = random_prime(10000)
            ....:     M = MatrixSpace(GF(p), nrows, ncols, sparse=True)
            ....:     m = M.random_element()
            ....:     rank_linbox = m.rank(algorithm='linbox')
            ....:     rank_generic = m.rank(algorithm='generic')
            ....:     if rank_linbox != rank_generic:
            ....:         print(m)
            ....:         raise RuntimeError

        REFERENCES:

        - Jean-Guillaume Dumas and Gilles Villars. 'Computing the Rank
          of Large Sparse Matrices over Finite
          Fields'. Proc. CASC'2002, The Fifth International Workshop
          on Computer Algebra in Scientific Computing, Big Yalta,
          Crimea, Ukraine, 22-27 sept. 2002, Springer-Verlag,
          http://perso.ens-lyon.fr/gilles.villard/BIBLIOGRAPHIE/POSTSCRIPT/rankjgd.ps

        .. NOTE::

           For very sparse matrices Gaussian elimination is faster
           because it barely has anything to do. If the fill in needs to
           be considered, 'Symbolic Reordering' is usually much faster."""
    @overload
    def rank(self, algorithm=...) -> Any:
        """Matrix_modn_sparse.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 755)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- either ``'linbox'`` (only available for
          matrices over prime fields) or ``'generic'``

        EXAMPLES::

            sage: A = matrix(GF(127), 2, 2, sparse=True)
            sage: A[0,0] = 34
            sage: A[0,1] = 102
            sage: A[1,0] = 55
            sage: A[1,1] = 74
            sage: A.rank()
            2

            sage: A._clear_cache()
            sage: A.rank(algorithm='generic')
            2
            sage: A._clear_cache()
            sage: A.rank(algorithm='hey')
            Traceback (most recent call last):
            ...
            ValueError: no algorithm 'hey'

        TESTS::

            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='generic')
            0
            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='linbox')
            0

            sage: for _ in range(50):
            ....:     nrows = randint(0, 100)
            ....:     ncols = randint(0, 100)
            ....:     p = random_prime(10000)
            ....:     M = MatrixSpace(GF(p), nrows, ncols, sparse=True)
            ....:     m = M.random_element()
            ....:     rank_linbox = m.rank(algorithm='linbox')
            ....:     rank_generic = m.rank(algorithm='generic')
            ....:     if rank_linbox != rank_generic:
            ....:         print(m)
            ....:         raise RuntimeError

        REFERENCES:

        - Jean-Guillaume Dumas and Gilles Villars. 'Computing the Rank
          of Large Sparse Matrices over Finite
          Fields'. Proc. CASC'2002, The Fifth International Workshop
          on Computer Algebra in Scientific Computing, Big Yalta,
          Crimea, Ukraine, 22-27 sept. 2002, Springer-Verlag,
          http://perso.ens-lyon.fr/gilles.villard/BIBLIOGRAPHIE/POSTSCRIPT/rankjgd.ps

        .. NOTE::

           For very sparse matrices Gaussian elimination is faster
           because it barely has anything to do. If the fill in needs to
           be considered, 'Symbolic Reordering' is usually much faster."""
    @overload
    def rank(self, algorithm=...) -> Any:
        """Matrix_modn_sparse.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 755)

        Return the rank of this matrix.

        INPUT:

        - ``algorithm`` -- either ``'linbox'`` (only available for
          matrices over prime fields) or ``'generic'``

        EXAMPLES::

            sage: A = matrix(GF(127), 2, 2, sparse=True)
            sage: A[0,0] = 34
            sage: A[0,1] = 102
            sage: A[1,0] = 55
            sage: A[1,1] = 74
            sage: A.rank()
            2

            sage: A._clear_cache()
            sage: A.rank(algorithm='generic')
            2
            sage: A._clear_cache()
            sage: A.rank(algorithm='hey')
            Traceback (most recent call last):
            ...
            ValueError: no algorithm 'hey'

        TESTS::

            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='generic')
            0
            sage: matrix(GF(3), 0, sparse=True).rank(algorithm='linbox')
            0

            sage: for _ in range(50):
            ....:     nrows = randint(0, 100)
            ....:     ncols = randint(0, 100)
            ....:     p = random_prime(10000)
            ....:     M = MatrixSpace(GF(p), nrows, ncols, sparse=True)
            ....:     m = M.random_element()
            ....:     rank_linbox = m.rank(algorithm='linbox')
            ....:     rank_generic = m.rank(algorithm='generic')
            ....:     if rank_linbox != rank_generic:
            ....:         print(m)
            ....:         raise RuntimeError

        REFERENCES:

        - Jean-Guillaume Dumas and Gilles Villars. 'Computing the Rank
          of Large Sparse Matrices over Finite
          Fields'. Proc. CASC'2002, The Fifth International Workshop
          on Computer Algebra in Scientific Computing, Big Yalta,
          Crimea, Ukraine, 22-27 sept. 2002, Springer-Verlag,
          http://perso.ens-lyon.fr/gilles.villard/BIBLIOGRAPHIE/POSTSCRIPT/rankjgd.ps

        .. NOTE::

           For very sparse matrices Gaussian elimination is faster
           because it barely has anything to do. If the fill in needs to
           be considered, 'Symbolic Reordering' is usually much faster."""
    def swap_rows(self, r1, r2) -> Any:
        """Matrix_modn_sparse.swap_rows(self, r1, r2)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 429)"""
    @overload
    def transpose(self) -> Any:
        """Matrix_modn_sparse.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 579)

        Return the transpose of ``self``.

        EXAMPLES::

            sage: A = matrix(GF(127),3,3,[0,1,0,2,0,0,3,0,0],sparse=True)
            sage: A
            [0 1 0]
            [2 0 0]
            [3 0 0]
            sage: A.transpose()
            [0 2 3]
            [1 0 0]
            [0 0 0]

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [0 2 3]
            [1 0 0]
            [0 0 0]"""
    @overload
    def transpose(self) -> Any:
        """Matrix_modn_sparse.transpose(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_modn_sparse.pyx (starting at line 579)

        Return the transpose of ``self``.

        EXAMPLES::

            sage: A = matrix(GF(127),3,3,[0,1,0,2,0,0,3,0,0],sparse=True)
            sage: A
            [0 1 0]
            [2 0 0]
            [3 0 0]
            sage: A.transpose()
            [0 2 3]
            [1 0 0]
            [0 0 0]

        ``.T`` is a convenient shortcut for the transpose::

            sage: A.T
            [0 2 3]
            [1 0 0]
            [0 0 0]"""
