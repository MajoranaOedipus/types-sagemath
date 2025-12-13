import sage.matrix.matrix_space as matrix_space
import sage.matrix.matrix_sparse
from sage.categories.category import ZZ as ZZ
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing as IntegerModRing
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from typing import Any, ClassVar, overload

class Matrix_integer_sparse(sage.matrix.matrix_sparse.Matrix_sparse):
    """Matrix_integer_sparse(parent, entries=None, copy=None, bool coerce=True)"""
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    def __init__(self, parent, entries=..., copy=..., boolcoerce=...) -> Any:
        """File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 89)

                Create a sparse matrix over the integers.

                INPUT:

                - ``parent`` -- a matrix space over ``ZZ``

                - ``entries`` -- see :func:`matrix`

                - ``copy`` -- ignored (for backwards compatibility)

                - ``coerce`` -- if ``False``, assume without checking that the
                  entries are of type :class:`Integer`
        """
    @overload
    def charpoly(self, var=..., algorithm=...) -> Any:
        """Matrix_integer_sparse.charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 816)

        Return the characteristic polynomial of this matrix.

        INPUT:

        - ``var`` -- (default: ``'x'``) the name of the variable
          of the polynomial

        - ``algorithm`` -- (default: ``None``) one of ``None``,
          ``'linbox'``, or an algorithm accepted by
          :meth:`sage.matrix.matrix_sparse.Matrix_sparse.charpoly`

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 4, sparse=True)
            sage: m = M()
            sage: m[0,0] = m[1,2] = m[2,3] = m[3,3] = 1
            sage: m[0,2] = m[1,3] = m[2,0] = m[3,0] = -3
            sage: m[1,1] = 2
            sage: m
            [ 1  0 -3  0]
            [ 0  2  1 -3]
            [-3  0  0  1]
            [-3  0  0  1]
            sage: m.charpoly()
            x^4 - 4*x^3 - 4*x^2 + 16*x

        TESTS::

            sage: matrix(ZZ, 0, 0, sparse=True).charpoly(algorithm='linbox')
            1
            sage: matrix(ZZ, 0, 0, sparse=True).charpoly(algorithm='generic')
            1"""
    @overload
    def charpoly(self) -> Any:
        """Matrix_integer_sparse.charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 816)

        Return the characteristic polynomial of this matrix.

        INPUT:

        - ``var`` -- (default: ``'x'``) the name of the variable
          of the polynomial

        - ``algorithm`` -- (default: ``None``) one of ``None``,
          ``'linbox'``, or an algorithm accepted by
          :meth:`sage.matrix.matrix_sparse.Matrix_sparse.charpoly`

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 4, sparse=True)
            sage: m = M()
            sage: m[0,0] = m[1,2] = m[2,3] = m[3,3] = 1
            sage: m[0,2] = m[1,3] = m[2,0] = m[3,0] = -3
            sage: m[1,1] = 2
            sage: m
            [ 1  0 -3  0]
            [ 0  2  1 -3]
            [-3  0  0  1]
            [-3  0  0  1]
            sage: m.charpoly()
            x^4 - 4*x^3 - 4*x^2 + 16*x

        TESTS::

            sage: matrix(ZZ, 0, 0, sparse=True).charpoly(algorithm='linbox')
            1
            sage: matrix(ZZ, 0, 0, sparse=True).charpoly(algorithm='generic')
            1"""
    @overload
    def charpoly(self, algorithm=...) -> Any:
        """Matrix_integer_sparse.charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 816)

        Return the characteristic polynomial of this matrix.

        INPUT:

        - ``var`` -- (default: ``'x'``) the name of the variable
          of the polynomial

        - ``algorithm`` -- (default: ``None``) one of ``None``,
          ``'linbox'``, or an algorithm accepted by
          :meth:`sage.matrix.matrix_sparse.Matrix_sparse.charpoly`

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 4, sparse=True)
            sage: m = M()
            sage: m[0,0] = m[1,2] = m[2,3] = m[3,3] = 1
            sage: m[0,2] = m[1,3] = m[2,0] = m[3,0] = -3
            sage: m[1,1] = 2
            sage: m
            [ 1  0 -3  0]
            [ 0  2  1 -3]
            [-3  0  0  1]
            [-3  0  0  1]
            sage: m.charpoly()
            x^4 - 4*x^3 - 4*x^2 + 16*x

        TESTS::

            sage: matrix(ZZ, 0, 0, sparse=True).charpoly(algorithm='linbox')
            1
            sage: matrix(ZZ, 0, 0, sparse=True).charpoly(algorithm='generic')
            1"""
    @overload
    def charpoly(self, algorithm=...) -> Any:
        """Matrix_integer_sparse.charpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 816)

        Return the characteristic polynomial of this matrix.

        INPUT:

        - ``var`` -- (default: ``'x'``) the name of the variable
          of the polynomial

        - ``algorithm`` -- (default: ``None``) one of ``None``,
          ``'linbox'``, or an algorithm accepted by
          :meth:`sage.matrix.matrix_sparse.Matrix_sparse.charpoly`

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 4, sparse=True)
            sage: m = M()
            sage: m[0,0] = m[1,2] = m[2,3] = m[3,3] = 1
            sage: m[0,2] = m[1,3] = m[2,0] = m[3,0] = -3
            sage: m[1,1] = 2
            sage: m
            [ 1  0 -3  0]
            [ 0  2  1 -3]
            [-3  0  0  1]
            [-3  0  0  1]
            sage: m.charpoly()
            x^4 - 4*x^3 - 4*x^2 + 16*x

        TESTS::

            sage: matrix(ZZ, 0, 0, sparse=True).charpoly(algorithm='linbox')
            1
            sage: matrix(ZZ, 0, 0, sparse=True).charpoly(algorithm='generic')
            1"""
    @overload
    def elementary_divisors(self, algorithm=...) -> Any:
        """Matrix_integer_sparse.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 574)

        Return the elementary divisors of self, in order.

        The elementary divisors are the invariants of the finite
        abelian group that is the cokernel of *left* multiplication by
        this matrix.  They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix
        - ``algorithm`` -- (default: ``'pari'``)

          * 'pari': works robustly, but is slower
          * 'linbox' -- use linbox (currently off, broken)

        OUTPUT: list of integers

        EXAMPLES::

            sage: matrix(3, range(9),sparse=True).elementary_divisors()
            [1, 3, 0]
            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2], sparse=True)
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
        """Matrix_integer_sparse.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 574)

        Return the elementary divisors of self, in order.

        The elementary divisors are the invariants of the finite
        abelian group that is the cokernel of *left* multiplication by
        this matrix.  They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix
        - ``algorithm`` -- (default: ``'pari'``)

          * 'pari': works robustly, but is slower
          * 'linbox' -- use linbox (currently off, broken)

        OUTPUT: list of integers

        EXAMPLES::

            sage: matrix(3, range(9),sparse=True).elementary_divisors()
            [1, 3, 0]
            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2], sparse=True)
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
        """Matrix_integer_sparse.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 574)

        Return the elementary divisors of self, in order.

        The elementary divisors are the invariants of the finite
        abelian group that is the cokernel of *left* multiplication by
        this matrix.  They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix
        - ``algorithm`` -- (default: ``'pari'``)

          * 'pari': works robustly, but is slower
          * 'linbox' -- use linbox (currently off, broken)

        OUTPUT: list of integers

        EXAMPLES::

            sage: matrix(3, range(9),sparse=True).elementary_divisors()
            [1, 3, 0]
            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2], sparse=True)
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
        """Matrix_integer_sparse.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 574)

        Return the elementary divisors of self, in order.

        The elementary divisors are the invariants of the finite
        abelian group that is the cokernel of *left* multiplication by
        this matrix.  They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix
        - ``algorithm`` -- (default: ``'pari'``)

          * 'pari': works robustly, but is slower
          * 'linbox' -- use linbox (currently off, broken)

        OUTPUT: list of integers

        EXAMPLES::

            sage: matrix(3, range(9),sparse=True).elementary_divisors()
            [1, 3, 0]
            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2], sparse=True)
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
        """Matrix_integer_sparse.elementary_divisors(self, algorithm='pari')

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 574)

        Return the elementary divisors of self, in order.

        The elementary divisors are the invariants of the finite
        abelian group that is the cokernel of *left* multiplication by
        this matrix.  They are ordered in reverse by divisibility.

        INPUT:

        - ``self`` -- matrix
        - ``algorithm`` -- (default: ``'pari'``)

          * 'pari': works robustly, but is slower
          * 'linbox' -- use linbox (currently off, broken)

        OUTPUT: list of integers

        EXAMPLES::

            sage: matrix(3, range(9),sparse=True).elementary_divisors()
            [1, 3, 0]
            sage: M = matrix(ZZ, 3, [1,5,7, 3,6,9, 0,1,2], sparse=True)
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
    def hermite_form(self, *args, **kwargs):
        """Matrix.echelon_form(self, algorithm='default', cutoff=0, **kwds)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix2.pyx (starting at line 8553)

        Return the echelon form of ``self``.

        .. NOTE::

            This row reduction does not use division if the
            matrix is not over a field (e.g., if the matrix is over
            the integers).  If you want to calculate the echelon form
            using division, then use :meth:`rref`, which assumes that
            the matrix entries are in a field (specifically, the field
            of fractions of the base ring of the matrix).

        INPUT:

        - ``algorithm`` -- string. Which algorithm to use. Choices are

          - ``'default'``: Let Sage choose an algorithm (default).

          - ``'classical'``: Gauss elimination.

          - ``'partial_pivoting'``: Gauss elimination, using partial pivoting
            (if base ring has absolute value)

          - ``'scaled_partial_pivoting'`` -- Gauss elimination, using scaled
            partial pivoting (if base ring has absolute value)

          - ``'scaled_partial_pivoting_valuation'``: Gauss elimination, using
            scaled partial pivoting (if base ring has valuation)

          - ``'strassen'``: use a Strassen divide and conquer
            algorithm (if available)

        - ``cutoff`` -- integer; only used if the Strassen algorithm is selected

        - ``transformation`` -- boolean; whether to also return the
          transformation matrix. Some matrix backends do not provide
          this information, in which case this option is ignored.

        OUTPUT:

        The reduced row echelon form of ``self``, as an immutable
        matrix. Note that ``self`` is *not* changed by this command. Use
        :meth:`echelonize` to change ``self`` in place.

        If the optional parameter ``transformation=True`` is
        specified, the output consists of a pair `(E,T)` of matrices
        where `E` is the echelon form of ``self`` and `T` is the
        transformation matrix.

        EXAMPLES::

            sage: MS = MatrixSpace(GF(19), 2, 3)
            sage: C = MS.matrix([1,2,3,4,5,6])
            sage: C.rank()
            2
            sage: C.nullity()
            0
            sage: C.echelon_form()
            [ 1  0 18]
            [ 0  1  2]

        The matrix library used for `\\ZZ/p`-matrices does not return
        the transformation matrix, so the ``transformation`` option is
        ignored::

            sage: C.echelon_form(transformation=True)
            [ 1  0 18]
            [ 0  1  2]

            sage: D = matrix(ZZ, 2, 3, [1,2,3,4,5,6])
            sage: D.echelon_form(transformation=True)
            (
            [1 2 3]  [ 1  0]
            [0 3 6], [ 4 -1]
            )
            sage: E, T = D.echelon_form(transformation=True)
            sage: T*D == E
            True"""
    @overload
    def minpoly(self, var=..., algorithm=...) -> Any:
        """Matrix_integer_sparse.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 920)

        Return the minimal polynomial of this matrix.

        INPUT:

        - ``var`` -- (default: ``'x'``) the name of the variable
          of the polynomial

        - ``algorithm`` -- (default: ``None``) one of ``None``,
          ``'linbox'``, or an algorithm accepted by
          :meth:`sage.matrix.matrix_sparse.Matrix_sparse.minpoly`

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 4, sparse=True)
            sage: m = M({(0, 0):2, (1, 1):1, (2, 1):-8, (2, 2):2, (2, 3):-1, (3, 3):1})
            sage: m
            [ 2  0  0  0]
            [ 0  1  0  0]
            [ 0 -8  2 -1]
            [ 0  0  0  1]
            sage: m.minpoly()
            x^2 - 3*x + 2

        TESTS::

            sage: matrix(ZZ, 0, 0, sparse=True).minpoly(algorithm='linbox')
            1
            sage: matrix(ZZ, 0, 0, sparse=True).minpoly(algorithm='generic')
            1"""
    @overload
    def minpoly(self) -> Any:
        """Matrix_integer_sparse.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 920)

        Return the minimal polynomial of this matrix.

        INPUT:

        - ``var`` -- (default: ``'x'``) the name of the variable
          of the polynomial

        - ``algorithm`` -- (default: ``None``) one of ``None``,
          ``'linbox'``, or an algorithm accepted by
          :meth:`sage.matrix.matrix_sparse.Matrix_sparse.minpoly`

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 4, sparse=True)
            sage: m = M({(0, 0):2, (1, 1):1, (2, 1):-8, (2, 2):2, (2, 3):-1, (3, 3):1})
            sage: m
            [ 2  0  0  0]
            [ 0  1  0  0]
            [ 0 -8  2 -1]
            [ 0  0  0  1]
            sage: m.minpoly()
            x^2 - 3*x + 2

        TESTS::

            sage: matrix(ZZ, 0, 0, sparse=True).minpoly(algorithm='linbox')
            1
            sage: matrix(ZZ, 0, 0, sparse=True).minpoly(algorithm='generic')
            1"""
    @overload
    def minpoly(self, algorithm=...) -> Any:
        """Matrix_integer_sparse.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 920)

        Return the minimal polynomial of this matrix.

        INPUT:

        - ``var`` -- (default: ``'x'``) the name of the variable
          of the polynomial

        - ``algorithm`` -- (default: ``None``) one of ``None``,
          ``'linbox'``, or an algorithm accepted by
          :meth:`sage.matrix.matrix_sparse.Matrix_sparse.minpoly`

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 4, sparse=True)
            sage: m = M({(0, 0):2, (1, 1):1, (2, 1):-8, (2, 2):2, (2, 3):-1, (3, 3):1})
            sage: m
            [ 2  0  0  0]
            [ 0  1  0  0]
            [ 0 -8  2 -1]
            [ 0  0  0  1]
            sage: m.minpoly()
            x^2 - 3*x + 2

        TESTS::

            sage: matrix(ZZ, 0, 0, sparse=True).minpoly(algorithm='linbox')
            1
            sage: matrix(ZZ, 0, 0, sparse=True).minpoly(algorithm='generic')
            1"""
    @overload
    def minpoly(self, algorithm=...) -> Any:
        """Matrix_integer_sparse.minpoly(self, var='x', algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 920)

        Return the minimal polynomial of this matrix.

        INPUT:

        - ``var`` -- (default: ``'x'``) the name of the variable
          of the polynomial

        - ``algorithm`` -- (default: ``None``) one of ``None``,
          ``'linbox'``, or an algorithm accepted by
          :meth:`sage.matrix.matrix_sparse.Matrix_sparse.minpoly`

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 4, sparse=True)
            sage: m = M({(0, 0):2, (1, 1):1, (2, 1):-8, (2, 2):2, (2, 3):-1, (3, 3):1})
            sage: m
            [ 2  0  0  0]
            [ 0  1  0  0]
            [ 0 -8  2 -1]
            [ 0  0  0  1]
            sage: m.minpoly()
            x^2 - 3*x + 2

        TESTS::

            sage: matrix(ZZ, 0, 0, sparse=True).minpoly(algorithm='linbox')
            1
            sage: matrix(ZZ, 0, 0, sparse=True).minpoly(algorithm='generic')
            1"""
    @overload
    def rank(self, algorithm=...) -> Any:
        """Matrix_integer_sparse.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 691)

        Compute the rank of this matrix.

        INPUT:

        - ``algorithm`` -- (optional) one of ``None``, ``'linbox'`` or
          ``'generic'``

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 3, 2, sparse=True)
            sage: m = M([1, 0, 2, 3, -1, 0])
            sage: m.rank()
            2"""
    @overload
    def rank(self) -> Any:
        """Matrix_integer_sparse.rank(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 691)

        Compute the rank of this matrix.

        INPUT:

        - ``algorithm`` -- (optional) one of ``None``, ``'linbox'`` or
          ``'generic'``

        EXAMPLES::

            sage: M = MatrixSpace(ZZ, 3, 2, sparse=True)
            sage: m = M([1, 0, 2, 3, -1, 0])
            sage: m.rank()
            2"""
    def rational_reconstruction(self, N) -> Any:
        """Matrix_integer_sparse.rational_reconstruction(self, N)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 438)

        Use rational reconstruction to lift ``self`` to a matrix over the
        rational numbers (if possible), where we view ``self`` as a matrix
        modulo `N`.

        EXAMPLES::

            sage: A = matrix(ZZ, 3, 4, [(1/3)%500, 2, 3, (-4)%500,
            ....:                       7, 2, 2, 3,
            ....:                       4, 3, 4, (5/7)%500], sparse=True)
            sage: A.rational_reconstruction(500)
            [1/3   2   3  -4]
            [  7   2   2   3]
            [  4   3   4 5/7]

        TESTS:

        Check that :issue:`9345` is fixed::

            sage: A = random_matrix(ZZ, 3, 3, sparse=True)
            sage: A.rational_reconstruction(0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: The modulus cannot be zero"""
    def smith_form(self, transformation=..., integral=...) -> Any:
        """Matrix_integer_sparse.smith_form(self, transformation=True, integral=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix_integer_sparse.pyx (starting at line 614)

        Return the smith normal form of this matrix, that is the diagonal
        matrix `S` with diagonal entries the ordered elementary divisors of
        this matrix.

        INPUT:

        - ``transformation`` -- boolean (default: ``True``); whether to
          return the transformation matrices `U` and `V` such that `S = U\\cdot
          self\\cdot V`

        - ``integral`` -- a subring of the base ring or ``True`` (default:
          ``None``); ignored for matrices with integer entries

        This version is for sparse matrices and simply makes the matrix
        dense and calls the version for dense integer matrices.

        .. NOTE::

           The :meth:`elementary_divisors` function, which returns the diagonal
           entries of S, is VASTLY faster than this function.

        The elementary divisors are the invariants of the finite abelian
        group that is the cokernel of this matrix. They are ordered in
        reverse by divisibility.

        EXAMPLES::

            sage: A = MatrixSpace(IntegerRing(), 3, sparse=True)(range(9))
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

            sage: A = Matrix(ZZ,3,2,range(6), sparse=True)
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

        The examples above show that :issue:`10626` has been implemented.


        .. SEEALSO::

           :meth:`elementary_divisors`"""
