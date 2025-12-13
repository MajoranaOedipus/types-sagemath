import _cython_3_2_1
import sage as sage
import sage.structure.element
from sage.categories.commutative_rings import CommutativeRings as CommutativeRings
from sage.categories.fields import Fields as Fields
from sage.categories.integral_domains import IntegralDomains as IntegralDomains
from sage.categories.rings import Rings as Rings
from sage.matrix.matrix_misc import row_iterator as row_iterator
from sage.rings.integer_ring import IntegerRing_class as IntegerRing_class
from sage.structure.element import have_same_parent as have_same_parent, parent as parent
from sage.structure.sequence import Sequence as Sequence
from typing import Any, ClassVar, overload

set_max_cols: _cython_3_2_1.cython_function_or_method
set_max_rows: _cython_3_2_1.cython_function_or_method
unpickle: _cython_3_2_1.cython_function_or_method

class Matrix(sage.structure.element.Matrix):
    """File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 54)

        A generic matrix.

        The ``Matrix`` class is the base class for all matrix
        classes. To create a ``Matrix``, first create a
        ``MatrixSpace``, then coerce a list of elements into
        the ``MatrixSpace``. See the documentation of
        ``MatrixSpace`` for more details.

        EXAMPLES:

        We illustrate matrices and matrix spaces. Note that no actual
        matrix that you make should have class Matrix; the class should
        always be derived from Matrix.

        ::

            sage: M = MatrixSpace(CDF,2,3); M
            Full MatrixSpace of 2 by 3 dense matrices over Complex Double Field
            sage: a = M([1,2,3,  4,5,6]); a
            [1.0 2.0 3.0]
            [4.0 5.0 6.0]
            sage: type(a)
            <class 'sage.matrix.matrix_complex_double_dense.Matrix_complex_double_dense'>
            sage: parent(a)
            Full MatrixSpace of 2 by 3 dense matrices over Complex Double Field

        ::

            sage: matrix(CDF, 2,3, [1,2,3, 4,5,6])
            [1.0 2.0 3.0]
            [4.0 5.0 6.0]
            sage: Mat(CDF,2,3)(range(1,7))
            [1.0 2.0 3.0]
            [4.0 5.0 6.0]

        ::

            sage: Q.<i,j,k> = QuaternionAlgebra(QQ, -1,-1)
            sage: matrix(Q,2,1,[1,2])
            [1]
            [2]
    """
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None:
        """Create and return a new object.  See help(type) for accurate signature."""
    @overload
    def act_on_polynomial(self, f) -> Any:
        """Matrix.act_on_polynomial(self, f)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2460)

        Return the polynomial ``f(self*x)``.

        INPUT:

        - ``self`` -- an nxn matrix

        - ``f`` -- a polynomial in n variables x=(x1,...,xn)

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: x, y = R.gens()
            sage: f = x**2 - y**2
            sage: M = MatrixSpace(QQ, 2)
            sage: A = M([1,2,3,4])
            sage: A.act_on_polynomial(f)
            -8*x^2 - 20*x*y - 12*y^2"""
    @overload
    def act_on_polynomial(self, f) -> Any:
        """Matrix.act_on_polynomial(self, f)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2460)

        Return the polynomial ``f(self*x)``.

        INPUT:

        - ``self`` -- an nxn matrix

        - ``f`` -- a polynomial in n variables x=(x1,...,xn)

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: x, y = R.gens()
            sage: f = x**2 - y**2
            sage: M = MatrixSpace(QQ, 2)
            sage: A = M([1,2,3,4])
            sage: A.act_on_polynomial(f)
            -8*x^2 - 20*x*y - 12*y^2"""
    def add_multiple_of_column(self, Py_ssize_ti, Py_ssize_tj, s, Py_ssize_tstart_row=...) -> Any:
        """Matrix.add_multiple_of_column(self, Py_ssize_t i, Py_ssize_t j, s, Py_ssize_t start_row=0)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3129)

        Add s times column j to column i.

        EXAMPLES: We add -1 times the third column to the second column of
        an integer matrix, remembering to start numbering cols at zero::

            sage: a = matrix(ZZ,2,3,range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.add_multiple_of_column(1,2,-1)
            sage: a
            [ 0 -1  2]
            [ 3 -1  5]

        To add a rational multiple, we first need to change the base ring::

            sage: a = a.change_ring(QQ)
            sage: a.add_multiple_of_column(1,0,1/3)
            sage: a
            [ 0 -1  2]
            [ 3  0  5]

        If not, we get an error message::

            sage: a.add_multiple_of_column(1, 0, SR.I())                                # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: Multiplying column by Symbolic Ring element cannot be done over
            Rational Field, use change_ring or with_added_multiple_of_column instead."""
    def add_multiple_of_row(self, Py_ssize_ti, Py_ssize_tj, s, Py_ssize_tstart_col=...) -> Any:
        """Matrix.add_multiple_of_row(self, Py_ssize_t i, Py_ssize_t j, s, Py_ssize_t start_col=0)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3044)

        Add s times row j to row i.

        EXAMPLES: We add -3 times the first row to the second row of an
        integer matrix, remembering to start numbering rows at zero::

            sage: a = matrix(ZZ,2,3,range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.add_multiple_of_row(1,0,-3)
            sage: a
            [ 0  1  2]
            [ 3  1 -1]

        To add a rational multiple, we first need to change the base ring::

            sage: a = a.change_ring(QQ)
            sage: a.add_multiple_of_row(1,0,1/3)
            sage: a
            [   0    1    2]
            [   3  4/3 -1/3]

        If not, we get an error message::

            sage: a.add_multiple_of_row(1, 0, SR.I())                                   # needs sage.symbolic
            Traceback (most recent call last):
            ...
            TypeError: Multiplying row by Symbolic Ring element cannot be done over
            Rational Field, use change_ring or with_added_multiple_of_row instead."""
    def add_to_entry(self, Py_ssize_ti, Py_ssize_tj, elt) -> Any:
        """Matrix.add_to_entry(self, Py_ssize_t i, Py_ssize_t j, elt)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 603)

        Add ``elt`` to the entry at position ``(i, j)``.

        EXAMPLES::

            sage: m = matrix(QQ['x,y'], 2, 2)
            sage: m.add_to_entry(0, 1, 2)
            sage: m
            [0 2]
            [0 0]"""
    def anticommutator(self, other) -> Any:
        """Matrix.anticommutator(self, other)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2538)

        Return the anticommutator ``self`` and ``other``.

        The *anticommutator* of two `n \\times n` matrices `A` and `B`
        is defined as `\\{A, B\\} := AB + BA` (sometimes this is written as
        `[A, B]_+`).

        EXAMPLES::

            sage: A = Matrix(ZZ, 2, 2, range(4))
            sage: B = Matrix(ZZ, 2, 2, [0, 1, 0, 0])
            sage: A.anticommutator(B)
            [2 3]
            [0 2]
            sage: A.anticommutator(B) == B.anticommutator(A)
            True
            sage: A.commutator(B) + B.anticommutator(A) == 2*A*B
            True"""
    @overload
    def base_ring(self) -> Any:
        """Matrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 1654)

        Return the base ring of the matrix.

        EXAMPLES::

            sage: m = matrix(QQ, 2, [1,2,3,4])
            sage: m.base_ring()
            Rational Field"""
    @overload
    def base_ring(self) -> Any:
        """Matrix.base_ring(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 1654)

        Return the base ring of the matrix.

        EXAMPLES::

            sage: m = matrix(QQ, 2, [1,2,3,4])
            sage: m.base_ring()
            Rational Field"""
    @overload
    def change_ring(self, ring) -> Any:
        """Matrix.change_ring(self, ring)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 1666)

        Return the matrix obtained by coercing the entries of this matrix
        into the given ring.

        Always returns a copy (unless ``self`` is immutable, in which case
        returns ``self``).

        EXAMPLES::

            sage: A = Matrix(QQ, 2, 2, [1/2, 1/3, 1/3, 1/4])
            sage: A.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: A.change_ring(GF(25,'a'))                                             # needs sage.rings.finite_rings
            [3 2]
            [2 4]
            sage: A.change_ring(GF(25,'a')).parent()                                    # needs sage.rings.finite_rings
            Full MatrixSpace of 2 by 2 dense matrices
             over Finite Field in a of size 5^2
            sage: A.change_ring(ZZ)                                                     # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: matrix has denominators so can...t change to ZZ

        Changing rings preserves subdivisions::

            sage: A.subdivide([1], []); A
            [1/2 1/3]
            [-------]
            [1/3 1/4]
            sage: A.change_ring(GF(25,'a'))                                             # needs sage.rings.finite_rings
            [3 2]
            [---]
            [2 4]"""
    @overload
    def change_ring(self, ZZ) -> Any:
        """Matrix.change_ring(self, ring)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 1666)

        Return the matrix obtained by coercing the entries of this matrix
        into the given ring.

        Always returns a copy (unless ``self`` is immutable, in which case
        returns ``self``).

        EXAMPLES::

            sage: A = Matrix(QQ, 2, 2, [1/2, 1/3, 1/3, 1/4])
            sage: A.parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field
            sage: A.change_ring(GF(25,'a'))                                             # needs sage.rings.finite_rings
            [3 2]
            [2 4]
            sage: A.change_ring(GF(25,'a')).parent()                                    # needs sage.rings.finite_rings
            Full MatrixSpace of 2 by 2 dense matrices
             over Finite Field in a of size 5^2
            sage: A.change_ring(ZZ)                                                     # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            TypeError: matrix has denominators so can...t change to ZZ

        Changing rings preserves subdivisions::

            sage: A.subdivide([1], []); A
            [1/2 1/3]
            [-------]
            [1/3 1/4]
            sage: A.change_ring(GF(25,'a'))                                             # needs sage.rings.finite_rings
            [3 2]
            [---]
            [2 4]"""
    def commutator(self, other) -> Any:
        """Matrix.commutator(self, other)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2522)

        Return the commutator self\\*other - other\\*self.

        EXAMPLES::

            sage: A = Matrix(ZZ, 2, 2, range(4))
            sage: B = Matrix(ZZ, 2, 2, [0, 1, 0, 0])
            sage: A.commutator(B)
            [-2 -3]
            [ 0  2]
            sage: A.commutator(B) == -B.commutator(A)
            True"""
    @overload
    def dense_coefficient_list(self, order=...) -> list:
        """Matrix.dense_coefficient_list(self, order=None) -> list

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 159)

        Return a list of *all* coefficients of ``self``.

        By default, this is the same as :meth:`list`.

        INPUT:

        - ``order`` -- (optional) an ordering of the basis indexing set

        EXAMPLES::

            sage: A = matrix([[1,2,3], [4,5,6]])
            sage: A.dense_coefficient_list()
            [1, 2, 3, 4, 5, 6]
            sage: A.dense_coefficient_list([(1,2), (1,0), (0,1), (0,2), (0,0), (1,1)])
            [6, 4, 2, 3, 1, 5]"""
    @overload
    def dense_coefficient_list(self) -> Any:
        """Matrix.dense_coefficient_list(self, order=None) -> list

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 159)

        Return a list of *all* coefficients of ``self``.

        By default, this is the same as :meth:`list`.

        INPUT:

        - ``order`` -- (optional) an ordering of the basis indexing set

        EXAMPLES::

            sage: A = matrix([[1,2,3], [4,5,6]])
            sage: A.dense_coefficient_list()
            [1, 2, 3, 4, 5, 6]
            sage: A.dense_coefficient_list([(1,2), (1,0), (0,1), (0,2), (0,0), (1,1)])
            [6, 4, 2, 3, 1, 5]"""
    @overload
    def dict(self, copy=...) -> Any:
        """Matrix.dict(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 234)

        Dictionary of the elements of ``self`` with keys pairs ``(i,j)``
        and values the nonzero entries of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); make a copy of the ``dict``
          corresponding to ``self``

        If ``copy=True``, then is safe to change the returned dictionary.
        Otherwise, this can cause undesired behavior by mutating the ``dict``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: a = matrix(R,2,[x,y,0, 0,0,2*x+y]); a
            [      x       y       0]
            [      0       0 2*x + y]
            sage: d = a.dict(); d
            {(0, 0): x, (0, 1): y, (1, 2): 2*x + y}

        Notice that changing the returned list does not change a (the list
        is a copy)::

            sage: d[0,0] = 25
            sage: a
            [      x       y       0]
            [      0       0 2*x + y]"""
    @overload
    def dict(self) -> Any:
        """Matrix.dict(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 234)

        Dictionary of the elements of ``self`` with keys pairs ``(i,j)``
        and values the nonzero entries of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); make a copy of the ``dict``
          corresponding to ``self``

        If ``copy=True``, then is safe to change the returned dictionary.
        Otherwise, this can cause undesired behavior by mutating the ``dict``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: a = matrix(R,2,[x,y,0, 0,0,2*x+y]); a
            [      x       y       0]
            [      0       0 2*x + y]
            sage: d = a.dict(); d
            {(0, 0): x, (0, 1): y, (1, 2): 2*x + y}

        Notice that changing the returned list does not change a (the list
        is a copy)::

            sage: d[0,0] = 25
            sage: a
            [      x       y       0]
            [      0       0 2*x + y]"""
    @overload
    def dimensions(self) -> Any:
        """Matrix.dimensions(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2437)

        Return the dimensions of this matrix as the tuple (nrows, ncols).

        EXAMPLES::

            sage: M = matrix([[1,2,3],[4,5,6]])
            sage: N = M.transpose()
            sage: M.dimensions()
            (2, 3)
            sage: N.dimensions()
            (3, 2)

        AUTHORS:

        - Benjamin Lundell (2012-02-09): examples"""
    @overload
    def dimensions(self) -> Any:
        """Matrix.dimensions(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2437)

        Return the dimensions of this matrix as the tuple (nrows, ncols).

        EXAMPLES::

            sage: M = matrix([[1,2,3],[4,5,6]])
            sage: N = M.transpose()
            sage: M.dimensions()
            (2, 3)
            sage: N.dimensions()
            (3, 2)

        AUTHORS:

        - Benjamin Lundell (2012-02-09): examples"""
    @overload
    def dimensions(self) -> Any:
        """Matrix.dimensions(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2437)

        Return the dimensions of this matrix as the tuple (nrows, ncols).

        EXAMPLES::

            sage: M = matrix([[1,2,3],[4,5,6]])
            sage: N = M.transpose()
            sage: M.dimensions()
            (2, 3)
            sage: N.dimensions()
            (3, 2)

        AUTHORS:

        - Benjamin Lundell (2012-02-09): examples"""
    @overload
    def inverse_of_unit(self, algorithm=...) -> Any:
        """Matrix.inverse_of_unit(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5928)

        Return the inverse of this matrix in the same matrix space.

        The matrix must be invertible on the base ring. Otherwise, an
        :exc:`ArithmeticError` is raised.

        The computation goes through the matrix of cofactors and avoids
        division. In particular the base ring does not need to have a
        fraction field.

        INPUT:

        - ``algorithm`` -- (default: ``None``) either ``None`` or ``'df'`` (for
          division free)

        EXAMPLES::

            sage: R.<a,b,c,d> = ZZ[]
            sage: RR = R.quotient(a*d - b*c - 1)
            sage: a,b,c,d = RR.gens()                                                   # needs sage.libs.singular
            sage: m = matrix(2, [a,b, c,d])
            sage: n = m.inverse_of_unit()                                               # needs sage.libs.singular
            sage: m * n                                                                 # needs sage.libs.singular
            [1 0]
            [0 1]

            sage: matrix(RR, 2, 1, [a,b]).inverse_of_unit()                             # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be a square matrix

            sage: matrix(RR, 1, 1, [2]).inverse_of_unit()                               # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: non-invertible matrix

            sage: R = ZZ.cartesian_product(ZZ)
            sage: m = matrix(R, 2, [R((2,1)), R((1,1)), R((1,1)), R((1,2))])
            sage: m * m.inverse_of_unit()
            [(1, 1) (0, 0)]
            [(0, 0) (1, 1)]

        Tests for :issue:`28570`::

            sage: P = posets.TamariLattice(7)                                           # needs sage.graphs
            sage: M = P._hasse_diagram._leq_matrix                                      # needs sage.graphs
            sage: M.inverse_of_unit()   # this was very slow, now 1s                    # needs sage.graphs
            429 x 429 sparse matrix over Integer Ring...

            sage: m = matrix(Zmod(2**2), 1, 1, [1], sparse=True)
            sage: mi = ~m; mi
            [1]
            sage: mi.parent()
            Full MatrixSpace of 1 by 1 sparse matrices over Ring of integers modulo 4"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Matrix.inverse_of_unit(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5928)

        Return the inverse of this matrix in the same matrix space.

        The matrix must be invertible on the base ring. Otherwise, an
        :exc:`ArithmeticError` is raised.

        The computation goes through the matrix of cofactors and avoids
        division. In particular the base ring does not need to have a
        fraction field.

        INPUT:

        - ``algorithm`` -- (default: ``None``) either ``None`` or ``'df'`` (for
          division free)

        EXAMPLES::

            sage: R.<a,b,c,d> = ZZ[]
            sage: RR = R.quotient(a*d - b*c - 1)
            sage: a,b,c,d = RR.gens()                                                   # needs sage.libs.singular
            sage: m = matrix(2, [a,b, c,d])
            sage: n = m.inverse_of_unit()                                               # needs sage.libs.singular
            sage: m * n                                                                 # needs sage.libs.singular
            [1 0]
            [0 1]

            sage: matrix(RR, 2, 1, [a,b]).inverse_of_unit()                             # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be a square matrix

            sage: matrix(RR, 1, 1, [2]).inverse_of_unit()                               # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: non-invertible matrix

            sage: R = ZZ.cartesian_product(ZZ)
            sage: m = matrix(R, 2, [R((2,1)), R((1,1)), R((1,1)), R((1,2))])
            sage: m * m.inverse_of_unit()
            [(1, 1) (0, 0)]
            [(0, 0) (1, 1)]

        Tests for :issue:`28570`::

            sage: P = posets.TamariLattice(7)                                           # needs sage.graphs
            sage: M = P._hasse_diagram._leq_matrix                                      # needs sage.graphs
            sage: M.inverse_of_unit()   # this was very slow, now 1s                    # needs sage.graphs
            429 x 429 sparse matrix over Integer Ring...

            sage: m = matrix(Zmod(2**2), 1, 1, [1], sparse=True)
            sage: mi = ~m; mi
            [1]
            sage: mi.parent()
            Full MatrixSpace of 1 by 1 sparse matrices over Ring of integers modulo 4"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Matrix.inverse_of_unit(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5928)

        Return the inverse of this matrix in the same matrix space.

        The matrix must be invertible on the base ring. Otherwise, an
        :exc:`ArithmeticError` is raised.

        The computation goes through the matrix of cofactors and avoids
        division. In particular the base ring does not need to have a
        fraction field.

        INPUT:

        - ``algorithm`` -- (default: ``None``) either ``None`` or ``'df'`` (for
          division free)

        EXAMPLES::

            sage: R.<a,b,c,d> = ZZ[]
            sage: RR = R.quotient(a*d - b*c - 1)
            sage: a,b,c,d = RR.gens()                                                   # needs sage.libs.singular
            sage: m = matrix(2, [a,b, c,d])
            sage: n = m.inverse_of_unit()                                               # needs sage.libs.singular
            sage: m * n                                                                 # needs sage.libs.singular
            [1 0]
            [0 1]

            sage: matrix(RR, 2, 1, [a,b]).inverse_of_unit()                             # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be a square matrix

            sage: matrix(RR, 1, 1, [2]).inverse_of_unit()                               # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: non-invertible matrix

            sage: R = ZZ.cartesian_product(ZZ)
            sage: m = matrix(R, 2, [R((2,1)), R((1,1)), R((1,1)), R((1,2))])
            sage: m * m.inverse_of_unit()
            [(1, 1) (0, 0)]
            [(0, 0) (1, 1)]

        Tests for :issue:`28570`::

            sage: P = posets.TamariLattice(7)                                           # needs sage.graphs
            sage: M = P._hasse_diagram._leq_matrix                                      # needs sage.graphs
            sage: M.inverse_of_unit()   # this was very slow, now 1s                    # needs sage.graphs
            429 x 429 sparse matrix over Integer Ring...

            sage: m = matrix(Zmod(2**2), 1, 1, [1], sparse=True)
            sage: mi = ~m; mi
            [1]
            sage: mi.parent()
            Full MatrixSpace of 1 by 1 sparse matrices over Ring of integers modulo 4"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Matrix.inverse_of_unit(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5928)

        Return the inverse of this matrix in the same matrix space.

        The matrix must be invertible on the base ring. Otherwise, an
        :exc:`ArithmeticError` is raised.

        The computation goes through the matrix of cofactors and avoids
        division. In particular the base ring does not need to have a
        fraction field.

        INPUT:

        - ``algorithm`` -- (default: ``None``) either ``None`` or ``'df'`` (for
          division free)

        EXAMPLES::

            sage: R.<a,b,c,d> = ZZ[]
            sage: RR = R.quotient(a*d - b*c - 1)
            sage: a,b,c,d = RR.gens()                                                   # needs sage.libs.singular
            sage: m = matrix(2, [a,b, c,d])
            sage: n = m.inverse_of_unit()                                               # needs sage.libs.singular
            sage: m * n                                                                 # needs sage.libs.singular
            [1 0]
            [0 1]

            sage: matrix(RR, 2, 1, [a,b]).inverse_of_unit()                             # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be a square matrix

            sage: matrix(RR, 1, 1, [2]).inverse_of_unit()                               # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: non-invertible matrix

            sage: R = ZZ.cartesian_product(ZZ)
            sage: m = matrix(R, 2, [R((2,1)), R((1,1)), R((1,1)), R((1,2))])
            sage: m * m.inverse_of_unit()
            [(1, 1) (0, 0)]
            [(0, 0) (1, 1)]

        Tests for :issue:`28570`::

            sage: P = posets.TamariLattice(7)                                           # needs sage.graphs
            sage: M = P._hasse_diagram._leq_matrix                                      # needs sage.graphs
            sage: M.inverse_of_unit()   # this was very slow, now 1s                    # needs sage.graphs
            429 x 429 sparse matrix over Integer Ring...

            sage: m = matrix(Zmod(2**2), 1, 1, [1], sparse=True)
            sage: mi = ~m; mi
            [1]
            sage: mi.parent()
            Full MatrixSpace of 1 by 1 sparse matrices over Ring of integers modulo 4"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Matrix.inverse_of_unit(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5928)

        Return the inverse of this matrix in the same matrix space.

        The matrix must be invertible on the base ring. Otherwise, an
        :exc:`ArithmeticError` is raised.

        The computation goes through the matrix of cofactors and avoids
        division. In particular the base ring does not need to have a
        fraction field.

        INPUT:

        - ``algorithm`` -- (default: ``None``) either ``None`` or ``'df'`` (for
          division free)

        EXAMPLES::

            sage: R.<a,b,c,d> = ZZ[]
            sage: RR = R.quotient(a*d - b*c - 1)
            sage: a,b,c,d = RR.gens()                                                   # needs sage.libs.singular
            sage: m = matrix(2, [a,b, c,d])
            sage: n = m.inverse_of_unit()                                               # needs sage.libs.singular
            sage: m * n                                                                 # needs sage.libs.singular
            [1 0]
            [0 1]

            sage: matrix(RR, 2, 1, [a,b]).inverse_of_unit()                             # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be a square matrix

            sage: matrix(RR, 1, 1, [2]).inverse_of_unit()                               # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: non-invertible matrix

            sage: R = ZZ.cartesian_product(ZZ)
            sage: m = matrix(R, 2, [R((2,1)), R((1,1)), R((1,1)), R((1,2))])
            sage: m * m.inverse_of_unit()
            [(1, 1) (0, 0)]
            [(0, 0) (1, 1)]

        Tests for :issue:`28570`::

            sage: P = posets.TamariLattice(7)                                           # needs sage.graphs
            sage: M = P._hasse_diagram._leq_matrix                                      # needs sage.graphs
            sage: M.inverse_of_unit()   # this was very slow, now 1s                    # needs sage.graphs
            429 x 429 sparse matrix over Integer Ring...

            sage: m = matrix(Zmod(2**2), 1, 1, [1], sparse=True)
            sage: mi = ~m; mi
            [1]
            sage: mi.parent()
            Full MatrixSpace of 1 by 1 sparse matrices over Ring of integers modulo 4"""
    @overload
    def inverse_of_unit(self) -> Any:
        """Matrix.inverse_of_unit(self, algorithm=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5928)

        Return the inverse of this matrix in the same matrix space.

        The matrix must be invertible on the base ring. Otherwise, an
        :exc:`ArithmeticError` is raised.

        The computation goes through the matrix of cofactors and avoids
        division. In particular the base ring does not need to have a
        fraction field.

        INPUT:

        - ``algorithm`` -- (default: ``None``) either ``None`` or ``'df'`` (for
          division free)

        EXAMPLES::

            sage: R.<a,b,c,d> = ZZ[]
            sage: RR = R.quotient(a*d - b*c - 1)
            sage: a,b,c,d = RR.gens()                                                   # needs sage.libs.singular
            sage: m = matrix(2, [a,b, c,d])
            sage: n = m.inverse_of_unit()                                               # needs sage.libs.singular
            sage: m * n                                                                 # needs sage.libs.singular
            [1 0]
            [0 1]

            sage: matrix(RR, 2, 1, [a,b]).inverse_of_unit()                             # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be a square matrix

            sage: matrix(RR, 1, 1, [2]).inverse_of_unit()                               # needs sage.libs.singular
            Traceback (most recent call last):
            ...
            ArithmeticError: non-invertible matrix

            sage: R = ZZ.cartesian_product(ZZ)
            sage: m = matrix(R, 2, [R((2,1)), R((1,1)), R((1,1)), R((1,2))])
            sage: m * m.inverse_of_unit()
            [(1, 1) (0, 0)]
            [(0, 0) (1, 1)]

        Tests for :issue:`28570`::

            sage: P = posets.TamariLattice(7)                                           # needs sage.graphs
            sage: M = P._hasse_diagram._leq_matrix                                      # needs sage.graphs
            sage: M.inverse_of_unit()   # this was very slow, now 1s                    # needs sage.graphs
            429 x 429 sparse matrix over Integer Ring...

            sage: m = matrix(Zmod(2**2), 1, 1, [1], sparse=True)
            sage: mi = ~m; mi
            [1]
            sage: mi.parent()
            Full MatrixSpace of 1 by 1 sparse matrices over Ring of integers modulo 4"""
    @overload
    def is_alternating(self) -> Any:
        '''Matrix.is_alternating(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4435)

        Return ``True`` if ``self`` is an alternating matrix.

        Here, "alternating matrix" means a square matrix `A`
        satisfying `A^T = -A` and such that the diagonal entries
        of `A` are `0`. Notice that the condition that the
        diagonal entries be `0` is not redundant for matrices over
        arbitrary ground rings (but it is redundant when `2` is
        invertible in the ground ring). A square matrix `A` only
        required to satisfy `A^T = -A` is said to be
        "skew-symmetric", and this property is checked by the
        :meth:`is_skew_symmetric` method.

        EXAMPLES::

            sage: m = matrix(QQ, [[0,2], [-2,0]])
            sage: m.is_alternating()
            True
            sage: m = matrix(QQ, [[1,2], [2,1]])
            sage: m.is_alternating()
            False

        In contrast to the property of being skew-symmetric, the
        property of being alternating does not tolerate nonzero
        entries on the diagonal even if they are their own
        negatives::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 2]])
            sage: n.is_alternating()
            False'''
    @overload
    def is_alternating(self) -> Any:
        '''Matrix.is_alternating(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4435)

        Return ``True`` if ``self`` is an alternating matrix.

        Here, "alternating matrix" means a square matrix `A`
        satisfying `A^T = -A` and such that the diagonal entries
        of `A` are `0`. Notice that the condition that the
        diagonal entries be `0` is not redundant for matrices over
        arbitrary ground rings (but it is redundant when `2` is
        invertible in the ground ring). A square matrix `A` only
        required to satisfy `A^T = -A` is said to be
        "skew-symmetric", and this property is checked by the
        :meth:`is_skew_symmetric` method.

        EXAMPLES::

            sage: m = matrix(QQ, [[0,2], [-2,0]])
            sage: m.is_alternating()
            True
            sage: m = matrix(QQ, [[1,2], [2,1]])
            sage: m.is_alternating()
            False

        In contrast to the property of being skew-symmetric, the
        property of being alternating does not tolerate nonzero
        entries on the diagonal even if they are their own
        negatives::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 2]])
            sage: n.is_alternating()
            False'''
    @overload
    def is_alternating(self) -> Any:
        '''Matrix.is_alternating(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4435)

        Return ``True`` if ``self`` is an alternating matrix.

        Here, "alternating matrix" means a square matrix `A`
        satisfying `A^T = -A` and such that the diagonal entries
        of `A` are `0`. Notice that the condition that the
        diagonal entries be `0` is not redundant for matrices over
        arbitrary ground rings (but it is redundant when `2` is
        invertible in the ground ring). A square matrix `A` only
        required to satisfy `A^T = -A` is said to be
        "skew-symmetric", and this property is checked by the
        :meth:`is_skew_symmetric` method.

        EXAMPLES::

            sage: m = matrix(QQ, [[0,2], [-2,0]])
            sage: m.is_alternating()
            True
            sage: m = matrix(QQ, [[1,2], [2,1]])
            sage: m.is_alternating()
            False

        In contrast to the property of being skew-symmetric, the
        property of being alternating does not tolerate nonzero
        entries on the diagonal even if they are their own
        negatives::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 2]])
            sage: n.is_alternating()
            False'''
    @overload
    def is_alternating(self) -> Any:
        '''Matrix.is_alternating(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4435)

        Return ``True`` if ``self`` is an alternating matrix.

        Here, "alternating matrix" means a square matrix `A`
        satisfying `A^T = -A` and such that the diagonal entries
        of `A` are `0`. Notice that the condition that the
        diagonal entries be `0` is not redundant for matrices over
        arbitrary ground rings (but it is redundant when `2` is
        invertible in the ground ring). A square matrix `A` only
        required to satisfy `A^T = -A` is said to be
        "skew-symmetric", and this property is checked by the
        :meth:`is_skew_symmetric` method.

        EXAMPLES::

            sage: m = matrix(QQ, [[0,2], [-2,0]])
            sage: m.is_alternating()
            True
            sage: m = matrix(QQ, [[1,2], [2,1]])
            sage: m.is_alternating()
            False

        In contrast to the property of being skew-symmetric, the
        property of being alternating does not tolerate nonzero
        entries on the diagonal even if they are their own
        negatives::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 2]])
            sage: n.is_alternating()
            False'''
    @overload
    def is_dense(self) -> Any:
        """Matrix.is_dense(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4591)

        Return ``True`` if this is a dense matrix.

        In Sage, being dense is a property of the underlying
        representation, not the number of nonzero entries.

        EXAMPLES::

            sage: matrix(QQ, 2, 2, range(4)).is_dense()
            True
            sage: matrix(QQ, 2, 2, range(4), sparse=True).is_dense()
            False"""
    @overload
    def is_dense(self) -> Any:
        """Matrix.is_dense(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4591)

        Return ``True`` if this is a dense matrix.

        In Sage, being dense is a property of the underlying
        representation, not the number of nonzero entries.

        EXAMPLES::

            sage: matrix(QQ, 2, 2, range(4)).is_dense()
            True
            sage: matrix(QQ, 2, 2, range(4), sparse=True).is_dense()
            False"""
    @overload
    def is_dense(self) -> Any:
        """Matrix.is_dense(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4591)

        Return ``True`` if this is a dense matrix.

        In Sage, being dense is a property of the underlying
        representation, not the number of nonzero entries.

        EXAMPLES::

            sage: matrix(QQ, 2, 2, range(4)).is_dense()
            True
            sage: matrix(QQ, 2, 2, range(4), sparse=True).is_dense()
            False"""
    @overload
    def is_hermitian(self) -> Any:
        """Matrix.is_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4251)

        Return ``True`` if the matrix is equal to its conjugate-transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the transpose with
        every entry conjugated, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[ 1 + I,  1 - 6*I, -1 - I],
            ....:                    [-3 - I,     -4*I,     -2],
            ....:                    [-1 + I, -2 - 8*I,  2 + I]])
            sage: A.is_hermitian()
            False
            sage: B = A * A.conjugate_transpose()
            sage: B.is_hermitian()
            True

        Sage has several fields besides the entire complex numbers
        where conjugation is non-trivial. ::

            sage: # needs sage.rings.number_field
            sage: F.<b> = QuadraticField(-7)
            sage: C = matrix(F, [[-2*b - 3,  7*b - 6, -b + 3],
            ....:                [-2*b - 3, -3*b + 2,   -2*b],
            ....:                [   b + 1,        0,     -2]])
            sage: C.is_hermitian()
            False
            sage: C = C*C.conjugate_transpose()
            sage: C.is_hermitian()
            True

        A matrix that is nearly Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[    2,   2-I, 1+4*I],
            ....:                    [  2+I,   3+I, 2-6*I],
            ....:                    [1-4*I, 2+6*I,     5]])
            sage: A.is_hermitian()
            False
            sage: A[1, 1] = 132
            sage: A.is_hermitian()
            True

        Rectangular matrices are never Hermitian.  ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_hermitian()                                                      # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian.  ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_hermitian()
            True"""
    @overload
    def is_hermitian(self) -> Any:
        """Matrix.is_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4251)

        Return ``True`` if the matrix is equal to its conjugate-transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the transpose with
        every entry conjugated, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[ 1 + I,  1 - 6*I, -1 - I],
            ....:                    [-3 - I,     -4*I,     -2],
            ....:                    [-1 + I, -2 - 8*I,  2 + I]])
            sage: A.is_hermitian()
            False
            sage: B = A * A.conjugate_transpose()
            sage: B.is_hermitian()
            True

        Sage has several fields besides the entire complex numbers
        where conjugation is non-trivial. ::

            sage: # needs sage.rings.number_field
            sage: F.<b> = QuadraticField(-7)
            sage: C = matrix(F, [[-2*b - 3,  7*b - 6, -b + 3],
            ....:                [-2*b - 3, -3*b + 2,   -2*b],
            ....:                [   b + 1,        0,     -2]])
            sage: C.is_hermitian()
            False
            sage: C = C*C.conjugate_transpose()
            sage: C.is_hermitian()
            True

        A matrix that is nearly Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[    2,   2-I, 1+4*I],
            ....:                    [  2+I,   3+I, 2-6*I],
            ....:                    [1-4*I, 2+6*I,     5]])
            sage: A.is_hermitian()
            False
            sage: A[1, 1] = 132
            sage: A.is_hermitian()
            True

        Rectangular matrices are never Hermitian.  ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_hermitian()                                                      # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian.  ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_hermitian()
            True"""
    @overload
    def is_hermitian(self) -> Any:
        """Matrix.is_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4251)

        Return ``True`` if the matrix is equal to its conjugate-transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the transpose with
        every entry conjugated, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[ 1 + I,  1 - 6*I, -1 - I],
            ....:                    [-3 - I,     -4*I,     -2],
            ....:                    [-1 + I, -2 - 8*I,  2 + I]])
            sage: A.is_hermitian()
            False
            sage: B = A * A.conjugate_transpose()
            sage: B.is_hermitian()
            True

        Sage has several fields besides the entire complex numbers
        where conjugation is non-trivial. ::

            sage: # needs sage.rings.number_field
            sage: F.<b> = QuadraticField(-7)
            sage: C = matrix(F, [[-2*b - 3,  7*b - 6, -b + 3],
            ....:                [-2*b - 3, -3*b + 2,   -2*b],
            ....:                [   b + 1,        0,     -2]])
            sage: C.is_hermitian()
            False
            sage: C = C*C.conjugate_transpose()
            sage: C.is_hermitian()
            True

        A matrix that is nearly Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[    2,   2-I, 1+4*I],
            ....:                    [  2+I,   3+I, 2-6*I],
            ....:                    [1-4*I, 2+6*I,     5]])
            sage: A.is_hermitian()
            False
            sage: A[1, 1] = 132
            sage: A.is_hermitian()
            True

        Rectangular matrices are never Hermitian.  ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_hermitian()                                                      # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian.  ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_hermitian()
            True"""
    @overload
    def is_hermitian(self) -> Any:
        """Matrix.is_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4251)

        Return ``True`` if the matrix is equal to its conjugate-transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the transpose with
        every entry conjugated, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[ 1 + I,  1 - 6*I, -1 - I],
            ....:                    [-3 - I,     -4*I,     -2],
            ....:                    [-1 + I, -2 - 8*I,  2 + I]])
            sage: A.is_hermitian()
            False
            sage: B = A * A.conjugate_transpose()
            sage: B.is_hermitian()
            True

        Sage has several fields besides the entire complex numbers
        where conjugation is non-trivial. ::

            sage: # needs sage.rings.number_field
            sage: F.<b> = QuadraticField(-7)
            sage: C = matrix(F, [[-2*b - 3,  7*b - 6, -b + 3],
            ....:                [-2*b - 3, -3*b + 2,   -2*b],
            ....:                [   b + 1,        0,     -2]])
            sage: C.is_hermitian()
            False
            sage: C = C*C.conjugate_transpose()
            sage: C.is_hermitian()
            True

        A matrix that is nearly Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[    2,   2-I, 1+4*I],
            ....:                    [  2+I,   3+I, 2-6*I],
            ....:                    [1-4*I, 2+6*I,     5]])
            sage: A.is_hermitian()
            False
            sage: A[1, 1] = 132
            sage: A.is_hermitian()
            True

        Rectangular matrices are never Hermitian.  ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_hermitian()                                                      # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian.  ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_hermitian()
            True"""
    @overload
    def is_hermitian(self) -> Any:
        """Matrix.is_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4251)

        Return ``True`` if the matrix is equal to its conjugate-transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the transpose with
        every entry conjugated, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[ 1 + I,  1 - 6*I, -1 - I],
            ....:                    [-3 - I,     -4*I,     -2],
            ....:                    [-1 + I, -2 - 8*I,  2 + I]])
            sage: A.is_hermitian()
            False
            sage: B = A * A.conjugate_transpose()
            sage: B.is_hermitian()
            True

        Sage has several fields besides the entire complex numbers
        where conjugation is non-trivial. ::

            sage: # needs sage.rings.number_field
            sage: F.<b> = QuadraticField(-7)
            sage: C = matrix(F, [[-2*b - 3,  7*b - 6, -b + 3],
            ....:                [-2*b - 3, -3*b + 2,   -2*b],
            ....:                [   b + 1,        0,     -2]])
            sage: C.is_hermitian()
            False
            sage: C = C*C.conjugate_transpose()
            sage: C.is_hermitian()
            True

        A matrix that is nearly Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[    2,   2-I, 1+4*I],
            ....:                    [  2+I,   3+I, 2-6*I],
            ....:                    [1-4*I, 2+6*I,     5]])
            sage: A.is_hermitian()
            False
            sage: A[1, 1] = 132
            sage: A.is_hermitian()
            True

        Rectangular matrices are never Hermitian.  ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_hermitian()                                                      # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian.  ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_hermitian()
            True"""
    @overload
    def is_hermitian(self) -> Any:
        """Matrix.is_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4251)

        Return ``True`` if the matrix is equal to its conjugate-transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the transpose with
        every entry conjugated, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[ 1 + I,  1 - 6*I, -1 - I],
            ....:                    [-3 - I,     -4*I,     -2],
            ....:                    [-1 + I, -2 - 8*I,  2 + I]])
            sage: A.is_hermitian()
            False
            sage: B = A * A.conjugate_transpose()
            sage: B.is_hermitian()
            True

        Sage has several fields besides the entire complex numbers
        where conjugation is non-trivial. ::

            sage: # needs sage.rings.number_field
            sage: F.<b> = QuadraticField(-7)
            sage: C = matrix(F, [[-2*b - 3,  7*b - 6, -b + 3],
            ....:                [-2*b - 3, -3*b + 2,   -2*b],
            ....:                [   b + 1,        0,     -2]])
            sage: C.is_hermitian()
            False
            sage: C = C*C.conjugate_transpose()
            sage: C.is_hermitian()
            True

        A matrix that is nearly Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[    2,   2-I, 1+4*I],
            ....:                    [  2+I,   3+I, 2-6*I],
            ....:                    [1-4*I, 2+6*I,     5]])
            sage: A.is_hermitian()
            False
            sage: A[1, 1] = 132
            sage: A.is_hermitian()
            True

        Rectangular matrices are never Hermitian.  ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_hermitian()                                                      # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian.  ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_hermitian()
            True"""
    @overload
    def is_hermitian(self) -> Any:
        """Matrix.is_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4251)

        Return ``True`` if the matrix is equal to its conjugate-transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the transpose with
        every entry conjugated, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[ 1 + I,  1 - 6*I, -1 - I],
            ....:                    [-3 - I,     -4*I,     -2],
            ....:                    [-1 + I, -2 - 8*I,  2 + I]])
            sage: A.is_hermitian()
            False
            sage: B = A * A.conjugate_transpose()
            sage: B.is_hermitian()
            True

        Sage has several fields besides the entire complex numbers
        where conjugation is non-trivial. ::

            sage: # needs sage.rings.number_field
            sage: F.<b> = QuadraticField(-7)
            sage: C = matrix(F, [[-2*b - 3,  7*b - 6, -b + 3],
            ....:                [-2*b - 3, -3*b + 2,   -2*b],
            ....:                [   b + 1,        0,     -2]])
            sage: C.is_hermitian()
            False
            sage: C = C*C.conjugate_transpose()
            sage: C.is_hermitian()
            True

        A matrix that is nearly Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[    2,   2-I, 1+4*I],
            ....:                    [  2+I,   3+I, 2-6*I],
            ....:                    [1-4*I, 2+6*I,     5]])
            sage: A.is_hermitian()
            False
            sage: A[1, 1] = 132
            sage: A.is_hermitian()
            True

        Rectangular matrices are never Hermitian.  ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_hermitian()                                                      # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian.  ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_hermitian()
            True"""
    @overload
    def is_hermitian(self) -> Any:
        """Matrix.is_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4251)

        Return ``True`` if the matrix is equal to its conjugate-transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the transpose with
        every entry conjugated, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[ 1 + I,  1 - 6*I, -1 - I],
            ....:                    [-3 - I,     -4*I,     -2],
            ....:                    [-1 + I, -2 - 8*I,  2 + I]])
            sage: A.is_hermitian()
            False
            sage: B = A * A.conjugate_transpose()
            sage: B.is_hermitian()
            True

        Sage has several fields besides the entire complex numbers
        where conjugation is non-trivial. ::

            sage: # needs sage.rings.number_field
            sage: F.<b> = QuadraticField(-7)
            sage: C = matrix(F, [[-2*b - 3,  7*b - 6, -b + 3],
            ....:                [-2*b - 3, -3*b + 2,   -2*b],
            ....:                [   b + 1,        0,     -2]])
            sage: C.is_hermitian()
            False
            sage: C = C*C.conjugate_transpose()
            sage: C.is_hermitian()
            True

        A matrix that is nearly Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[    2,   2-I, 1+4*I],
            ....:                    [  2+I,   3+I, 2-6*I],
            ....:                    [1-4*I, 2+6*I,     5]])
            sage: A.is_hermitian()
            False
            sage: A[1, 1] = 132
            sage: A.is_hermitian()
            True

        Rectangular matrices are never Hermitian.  ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_hermitian()                                                      # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian.  ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_hermitian()
            True"""
    @overload
    def is_hermitian(self) -> Any:
        """Matrix.is_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4251)

        Return ``True`` if the matrix is equal to its conjugate-transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the transpose with
        every entry conjugated, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[ 1 + I,  1 - 6*I, -1 - I],
            ....:                    [-3 - I,     -4*I,     -2],
            ....:                    [-1 + I, -2 - 8*I,  2 + I]])
            sage: A.is_hermitian()
            False
            sage: B = A * A.conjugate_transpose()
            sage: B.is_hermitian()
            True

        Sage has several fields besides the entire complex numbers
        where conjugation is non-trivial. ::

            sage: # needs sage.rings.number_field
            sage: F.<b> = QuadraticField(-7)
            sage: C = matrix(F, [[-2*b - 3,  7*b - 6, -b + 3],
            ....:                [-2*b - 3, -3*b + 2,   -2*b],
            ....:                [   b + 1,        0,     -2]])
            sage: C.is_hermitian()
            False
            sage: C = C*C.conjugate_transpose()
            sage: C.is_hermitian()
            True

        A matrix that is nearly Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[    2,   2-I, 1+4*I],
            ....:                    [  2+I,   3+I, 2-6*I],
            ....:                    [1-4*I, 2+6*I,     5]])
            sage: A.is_hermitian()
            False
            sage: A[1, 1] = 132
            sage: A.is_hermitian()
            True

        Rectangular matrices are never Hermitian.  ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_hermitian()                                                      # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian.  ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_hermitian()
            True"""
    @overload
    def is_immutable(self) -> Any:
        """Matrix.is_immutable(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 500)

        Return ``True`` if this matrix is immutable.

        See the documentation for self.set_immutable for more details
        about mutability.

        EXAMPLES::

            sage: A = Matrix(QQ['t','s'], 2, 2, range(4))
            sage: A.is_immutable()
            False
            sage: A.set_immutable()
            sage: A.is_immutable()
            True"""
    @overload
    def is_immutable(self) -> Any:
        """Matrix.is_immutable(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 500)

        Return ``True`` if this matrix is immutable.

        See the documentation for self.set_immutable for more details
        about mutability.

        EXAMPLES::

            sage: A = Matrix(QQ['t','s'], 2, 2, range(4))
            sage: A.is_immutable()
            False
            sage: A.set_immutable()
            sage: A.is_immutable()
            True"""
    @overload
    def is_immutable(self) -> Any:
        """Matrix.is_immutable(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 500)

        Return ``True`` if this matrix is immutable.

        See the documentation for self.set_immutable for more details
        about mutability.

        EXAMPLES::

            sage: A = Matrix(QQ['t','s'], 2, 2, range(4))
            sage: A.is_immutable()
            False
            sage: A.set_immutable()
            sage: A.is_immutable()
            True"""
    def is_invertible(self) -> Any:
        """Matrix.is_invertible(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4637)

        Return ``True`` if this matrix is invertible.

        EXAMPLES: The following matrix is invertible over
        `\\QQ` but not over `\\ZZ`.

        ::

            sage: A = MatrixSpace(ZZ, 2)(range(4))
            sage: A.is_invertible()
            False
            sage: A.matrix_over_field().is_invertible()
            True

        The inverse function is a constructor for matrices over the
        fraction field, so it can work even if A is not invertible.

        ::

            sage: ~A   # inverse of A
            [-3/2  1/2]
            [   1    0]

        The next matrix is invertible over `\\ZZ`.

        ::

            sage: A = MatrixSpace(IntegerRing(), 2)([1,10,0,-1])
            sage: A.is_invertible()
            True
            sage: ~A                # compute the inverse
            [ 1 10]
            [ 0 -1]

        The following nontrivial matrix is invertible over
        `\\ZZ[x]`.

        ::

            sage: R.<x> = PolynomialRing(IntegerRing())
            sage: A = MatrixSpace(R, 2)([1,x,0,-1])
            sage: A.is_invertible()
            True
            sage: ~A
            [ 1  x]
            [ 0 -1]"""
    @overload
    def is_mutable(self) -> Any:
        """Matrix.is_mutable(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 518)

        Return ``True`` if this matrix is mutable.

        See the documentation for self.set_immutable for more details
        about mutability.

        EXAMPLES::

            sage: A = Matrix(QQ['t','s'], 2, 2, range(4))
            sage: A.is_mutable()
            True
            sage: A.set_immutable()
            sage: A.is_mutable()
            False"""
    @overload
    def is_mutable(self) -> Any:
        """Matrix.is_mutable(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 518)

        Return ``True`` if this matrix is mutable.

        See the documentation for self.set_immutable for more details
        about mutability.

        EXAMPLES::

            sage: A = Matrix(QQ['t','s'], 2, 2, range(4))
            sage: A.is_mutable()
            True
            sage: A.set_immutable()
            sage: A.is_mutable()
            False"""
    @overload
    def is_mutable(self) -> Any:
        """Matrix.is_mutable(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 518)

        Return ``True`` if this matrix is mutable.

        See the documentation for self.set_immutable for more details
        about mutability.

        EXAMPLES::

            sage: A = Matrix(QQ['t','s'], 2, 2, range(4))
            sage: A.is_mutable()
            True
            sage: A.set_immutable()
            sage: A.is_mutable()
            False"""
    @overload
    def is_singular(self) -> Any:
        """Matrix.is_singular(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4689)

        Return ``True`` if ``self`` is singular.

        OUTPUT:

        A square matrix is singular if it has a zero
        determinant and this method will return ``True``
        in exactly this case. When the entries of the
        matrix come from a field, this is equivalent
        to having a nontrivial kernel, or lacking an
        inverse, or having linearly dependent rows,
        or having linearly dependent columns.

        For square matrices over a field the methods
        :meth:`is_invertible` and :meth:`is_singular`
        are logical opposites.  However, it is an error
        to apply :meth:`is_singular` to a matrix that
        is not square, while :meth:`is_invertible` will
        always return ``False`` for a matrix that is not
        square.

        EXAMPLES:

        A singular matrix over the field ``QQ``. ::

            sage: A = matrix(QQ, 4, [-1,2,-3,6, 0,-1,-1,0, -1,1,-5,7, -1,6,5,2])
            sage: A.is_singular()
            True
            sage: A.right_kernel().dimension()
            1

        A matrix that is not singular, i.e. nonsingular, over a field. ::

            sage: B = matrix(QQ, 4, [1,-3,-1,-5, 2,-5,-2,-7, -2,5,3,4, -1,4,2,6])
            sage: B.is_singular()
            False
            sage: B.left_kernel().dimension()
            0

        For *rectangular* matrices, invertibility is always
        ``False``, but asking about singularity will give an error. ::

            sage: C = matrix(QQ, 5, range(30))
            sage: C.is_invertible()
            False
            sage: C.is_singular()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

        When the base ring is not a field, then a matrix
        may be both not invertible and not singular. ::

            sage: D = matrix(ZZ, 4, [2,0,-4,8, 2,1,-2,7, 2,5,7,0, 0,1,4,-6])
            sage: D.is_invertible()
            False
            sage: D.is_singular()
            False
            sage: d = D.determinant(); d
            2
            sage: d.is_unit()
            False"""
    @overload
    def is_singular(self) -> Any:
        """Matrix.is_singular(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4689)

        Return ``True`` if ``self`` is singular.

        OUTPUT:

        A square matrix is singular if it has a zero
        determinant and this method will return ``True``
        in exactly this case. When the entries of the
        matrix come from a field, this is equivalent
        to having a nontrivial kernel, or lacking an
        inverse, or having linearly dependent rows,
        or having linearly dependent columns.

        For square matrices over a field the methods
        :meth:`is_invertible` and :meth:`is_singular`
        are logical opposites.  However, it is an error
        to apply :meth:`is_singular` to a matrix that
        is not square, while :meth:`is_invertible` will
        always return ``False`` for a matrix that is not
        square.

        EXAMPLES:

        A singular matrix over the field ``QQ``. ::

            sage: A = matrix(QQ, 4, [-1,2,-3,6, 0,-1,-1,0, -1,1,-5,7, -1,6,5,2])
            sage: A.is_singular()
            True
            sage: A.right_kernel().dimension()
            1

        A matrix that is not singular, i.e. nonsingular, over a field. ::

            sage: B = matrix(QQ, 4, [1,-3,-1,-5, 2,-5,-2,-7, -2,5,3,4, -1,4,2,6])
            sage: B.is_singular()
            False
            sage: B.left_kernel().dimension()
            0

        For *rectangular* matrices, invertibility is always
        ``False``, but asking about singularity will give an error. ::

            sage: C = matrix(QQ, 5, range(30))
            sage: C.is_invertible()
            False
            sage: C.is_singular()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

        When the base ring is not a field, then a matrix
        may be both not invertible and not singular. ::

            sage: D = matrix(ZZ, 4, [2,0,-4,8, 2,1,-2,7, 2,5,7,0, 0,1,4,-6])
            sage: D.is_invertible()
            False
            sage: D.is_singular()
            False
            sage: d = D.determinant(); d
            2
            sage: d.is_unit()
            False"""
    @overload
    def is_singular(self) -> Any:
        """Matrix.is_singular(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4689)

        Return ``True`` if ``self`` is singular.

        OUTPUT:

        A square matrix is singular if it has a zero
        determinant and this method will return ``True``
        in exactly this case. When the entries of the
        matrix come from a field, this is equivalent
        to having a nontrivial kernel, or lacking an
        inverse, or having linearly dependent rows,
        or having linearly dependent columns.

        For square matrices over a field the methods
        :meth:`is_invertible` and :meth:`is_singular`
        are logical opposites.  However, it is an error
        to apply :meth:`is_singular` to a matrix that
        is not square, while :meth:`is_invertible` will
        always return ``False`` for a matrix that is not
        square.

        EXAMPLES:

        A singular matrix over the field ``QQ``. ::

            sage: A = matrix(QQ, 4, [-1,2,-3,6, 0,-1,-1,0, -1,1,-5,7, -1,6,5,2])
            sage: A.is_singular()
            True
            sage: A.right_kernel().dimension()
            1

        A matrix that is not singular, i.e. nonsingular, over a field. ::

            sage: B = matrix(QQ, 4, [1,-3,-1,-5, 2,-5,-2,-7, -2,5,3,4, -1,4,2,6])
            sage: B.is_singular()
            False
            sage: B.left_kernel().dimension()
            0

        For *rectangular* matrices, invertibility is always
        ``False``, but asking about singularity will give an error. ::

            sage: C = matrix(QQ, 5, range(30))
            sage: C.is_invertible()
            False
            sage: C.is_singular()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

        When the base ring is not a field, then a matrix
        may be both not invertible and not singular. ::

            sage: D = matrix(ZZ, 4, [2,0,-4,8, 2,1,-2,7, 2,5,7,0, 0,1,4,-6])
            sage: D.is_invertible()
            False
            sage: D.is_singular()
            False
            sage: d = D.determinant(); d
            2
            sage: d.is_unit()
            False"""
    @overload
    def is_singular(self) -> Any:
        """Matrix.is_singular(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4689)

        Return ``True`` if ``self`` is singular.

        OUTPUT:

        A square matrix is singular if it has a zero
        determinant and this method will return ``True``
        in exactly this case. When the entries of the
        matrix come from a field, this is equivalent
        to having a nontrivial kernel, or lacking an
        inverse, or having linearly dependent rows,
        or having linearly dependent columns.

        For square matrices over a field the methods
        :meth:`is_invertible` and :meth:`is_singular`
        are logical opposites.  However, it is an error
        to apply :meth:`is_singular` to a matrix that
        is not square, while :meth:`is_invertible` will
        always return ``False`` for a matrix that is not
        square.

        EXAMPLES:

        A singular matrix over the field ``QQ``. ::

            sage: A = matrix(QQ, 4, [-1,2,-3,6, 0,-1,-1,0, -1,1,-5,7, -1,6,5,2])
            sage: A.is_singular()
            True
            sage: A.right_kernel().dimension()
            1

        A matrix that is not singular, i.e. nonsingular, over a field. ::

            sage: B = matrix(QQ, 4, [1,-3,-1,-5, 2,-5,-2,-7, -2,5,3,4, -1,4,2,6])
            sage: B.is_singular()
            False
            sage: B.left_kernel().dimension()
            0

        For *rectangular* matrices, invertibility is always
        ``False``, but asking about singularity will give an error. ::

            sage: C = matrix(QQ, 5, range(30))
            sage: C.is_invertible()
            False
            sage: C.is_singular()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

        When the base ring is not a field, then a matrix
        may be both not invertible and not singular. ::

            sage: D = matrix(ZZ, 4, [2,0,-4,8, 2,1,-2,7, 2,5,7,0, 0,1,4,-6])
            sage: D.is_invertible()
            False
            sage: D.is_singular()
            False
            sage: d = D.determinant(); d
            2
            sage: d.is_unit()
            False"""
    @overload
    def is_singular(self) -> Any:
        """Matrix.is_singular(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4689)

        Return ``True`` if ``self`` is singular.

        OUTPUT:

        A square matrix is singular if it has a zero
        determinant and this method will return ``True``
        in exactly this case. When the entries of the
        matrix come from a field, this is equivalent
        to having a nontrivial kernel, or lacking an
        inverse, or having linearly dependent rows,
        or having linearly dependent columns.

        For square matrices over a field the methods
        :meth:`is_invertible` and :meth:`is_singular`
        are logical opposites.  However, it is an error
        to apply :meth:`is_singular` to a matrix that
        is not square, while :meth:`is_invertible` will
        always return ``False`` for a matrix that is not
        square.

        EXAMPLES:

        A singular matrix over the field ``QQ``. ::

            sage: A = matrix(QQ, 4, [-1,2,-3,6, 0,-1,-1,0, -1,1,-5,7, -1,6,5,2])
            sage: A.is_singular()
            True
            sage: A.right_kernel().dimension()
            1

        A matrix that is not singular, i.e. nonsingular, over a field. ::

            sage: B = matrix(QQ, 4, [1,-3,-1,-5, 2,-5,-2,-7, -2,5,3,4, -1,4,2,6])
            sage: B.is_singular()
            False
            sage: B.left_kernel().dimension()
            0

        For *rectangular* matrices, invertibility is always
        ``False``, but asking about singularity will give an error. ::

            sage: C = matrix(QQ, 5, range(30))
            sage: C.is_invertible()
            False
            sage: C.is_singular()
            Traceback (most recent call last):
            ...
            ValueError: self must be a square matrix

        When the base ring is not a field, then a matrix
        may be both not invertible and not singular. ::

            sage: D = matrix(ZZ, 4, [2,0,-4,8, 2,1,-2,7, 2,5,7,0, 0,1,4,-6])
            sage: D.is_invertible()
            False
            sage: D.is_singular()
            False
            sage: d = D.determinant(); d
            2
            sage: d.is_unit()
            False"""
    @overload
    def is_skew_hermitian(self) -> Any:
        """Matrix.is_skew_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4328)

        Return ``True`` if the matrix is equal to the negative of its
        conjugate transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the negative of
        its conjugate transpose, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_skew_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_skew_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: A = matrix(QQbar, [[0, -1],                                           # needs sage.rings.number_field
            ....:                    [1,  0]])
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            True

        A matrix that is nearly skew-Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[  -I, -1, 1-I],
            ....:                    [   1,  1,  -1],
            ....:                    [-1-I,  1,  -I]])
            sage: A.is_skew_hermitian()
            False
            sage: A[1, 1] = -I
            sage: A.is_skew_hermitian()
            True

        Rectangular matrices are never skew-Hermitian. ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian. ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_skew_hermitian()
            True"""
    @overload
    def is_skew_hermitian(self) -> Any:
        """Matrix.is_skew_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4328)

        Return ``True`` if the matrix is equal to the negative of its
        conjugate transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the negative of
        its conjugate transpose, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_skew_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_skew_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: A = matrix(QQbar, [[0, -1],                                           # needs sage.rings.number_field
            ....:                    [1,  0]])
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            True

        A matrix that is nearly skew-Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[  -I, -1, 1-I],
            ....:                    [   1,  1,  -1],
            ....:                    [-1-I,  1,  -I]])
            sage: A.is_skew_hermitian()
            False
            sage: A[1, 1] = -I
            sage: A.is_skew_hermitian()
            True

        Rectangular matrices are never skew-Hermitian. ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian. ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_skew_hermitian()
            True"""
    @overload
    def is_skew_hermitian(self) -> Any:
        """Matrix.is_skew_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4328)

        Return ``True`` if the matrix is equal to the negative of its
        conjugate transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the negative of
        its conjugate transpose, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_skew_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_skew_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: A = matrix(QQbar, [[0, -1],                                           # needs sage.rings.number_field
            ....:                    [1,  0]])
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            True

        A matrix that is nearly skew-Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[  -I, -1, 1-I],
            ....:                    [   1,  1,  -1],
            ....:                    [-1-I,  1,  -I]])
            sage: A.is_skew_hermitian()
            False
            sage: A[1, 1] = -I
            sage: A.is_skew_hermitian()
            True

        Rectangular matrices are never skew-Hermitian. ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian. ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_skew_hermitian()
            True"""
    @overload
    def is_skew_hermitian(self) -> Any:
        """Matrix.is_skew_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4328)

        Return ``True`` if the matrix is equal to the negative of its
        conjugate transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the negative of
        its conjugate transpose, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_skew_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_skew_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: A = matrix(QQbar, [[0, -1],                                           # needs sage.rings.number_field
            ....:                    [1,  0]])
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            True

        A matrix that is nearly skew-Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[  -I, -1, 1-I],
            ....:                    [   1,  1,  -1],
            ....:                    [-1-I,  1,  -I]])
            sage: A.is_skew_hermitian()
            False
            sage: A[1, 1] = -I
            sage: A.is_skew_hermitian()
            True

        Rectangular matrices are never skew-Hermitian. ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian. ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_skew_hermitian()
            True"""
    @overload
    def is_skew_hermitian(self) -> Any:
        """Matrix.is_skew_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4328)

        Return ``True`` if the matrix is equal to the negative of its
        conjugate transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the negative of
        its conjugate transpose, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_skew_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_skew_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: A = matrix(QQbar, [[0, -1],                                           # needs sage.rings.number_field
            ....:                    [1,  0]])
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            True

        A matrix that is nearly skew-Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[  -I, -1, 1-I],
            ....:                    [   1,  1,  -1],
            ....:                    [-1-I,  1,  -I]])
            sage: A.is_skew_hermitian()
            False
            sage: A[1, 1] = -I
            sage: A.is_skew_hermitian()
            True

        Rectangular matrices are never skew-Hermitian. ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian. ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_skew_hermitian()
            True"""
    @overload
    def is_skew_hermitian(self) -> Any:
        """Matrix.is_skew_hermitian(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4328)

        Return ``True`` if the matrix is equal to the negative of its
        conjugate transpose.

        OUTPUT:

        ``True`` if the matrix is square and equal to the negative of
        its conjugate transpose, and ``False`` otherwise.

        Note that if conjugation has no effect on elements of the base
        ring (such as for integers), then the :meth:`is_skew_symmetric`
        method is equivalent and faster.

        This routine is for matrices over exact rings and so may not
        work properly for matrices over ``RR`` or ``CC``.  For matrices with
        approximate entries, the rings of double-precision floating-point
        numbers, ``RDF`` and ``CDF``, are a better choice since the
        :meth:`sage.matrix.matrix_double_dense.Matrix_double_dense.is_skew_hermitian`
        method has a tolerance parameter.  This provides control over
        allowing for minor discrepancies between entries when checking
        equality.

        The result is cached.

        EXAMPLES::

            sage: A = matrix(QQbar, [[0, -1],                                           # needs sage.rings.number_field
            ....:                    [1,  0]])
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            True

        A matrix that is nearly skew-Hermitian, but for a non-real
        diagonal entry. ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQbar, [[  -I, -1, 1-I],
            ....:                    [   1,  1,  -1],
            ....:                    [-1-I,  1,  -I]])
            sage: A.is_skew_hermitian()
            False
            sage: A[1, 1] = -I
            sage: A.is_skew_hermitian()
            True

        Rectangular matrices are never skew-Hermitian. ::

            sage: A = matrix(QQbar, 3, 4)                                               # needs sage.rings.number_field
            sage: A.is_skew_hermitian()                                                 # needs sage.rings.number_field
            False

        A square, empty matrix is trivially Hermitian. ::

            sage: A = matrix(QQ, 0, 0)
            sage: A.is_skew_hermitian()
            True"""
    @overload
    def is_skew_symmetric(self) -> Any:
        '''Matrix.is_skew_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4387)

        Return ``True`` if ``self`` is a skew-symmetric matrix.

        Here, "skew-symmetric matrix" means a square matrix `A`
        satisfying `A^T = -A`. It does not require that the
        diagonal entries of `A` are `0` (although this
        automatically follows from `A^T = -A` when `2` is
        invertible in the ground ring over which the matrix is
        considered). Skew-symmetric matrices `A` whose diagonal
        entries are `0` are said to be "alternating", and this
        property is checked by the :meth:`is_alternating`
        method.

        EXAMPLES::

            sage: m = matrix(QQ, [[0,2], [-2,0]])
            sage: m.is_skew_symmetric()
            True
            sage: m = matrix(QQ, [[1,2], [2,1]])
            sage: m.is_skew_symmetric()
            False

        Skew-symmetric is not the same as alternating when
        `2` is a zero-divisor in the ground ring::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 2]])
            sage: n.is_skew_symmetric()
            True

        but yet the diagonal cannot be completely
        arbitrary in this case::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 3]])
            sage: n.is_skew_symmetric()
            False'''
    @overload
    def is_skew_symmetric(self) -> Any:
        '''Matrix.is_skew_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4387)

        Return ``True`` if ``self`` is a skew-symmetric matrix.

        Here, "skew-symmetric matrix" means a square matrix `A`
        satisfying `A^T = -A`. It does not require that the
        diagonal entries of `A` are `0` (although this
        automatically follows from `A^T = -A` when `2` is
        invertible in the ground ring over which the matrix is
        considered). Skew-symmetric matrices `A` whose diagonal
        entries are `0` are said to be "alternating", and this
        property is checked by the :meth:`is_alternating`
        method.

        EXAMPLES::

            sage: m = matrix(QQ, [[0,2], [-2,0]])
            sage: m.is_skew_symmetric()
            True
            sage: m = matrix(QQ, [[1,2], [2,1]])
            sage: m.is_skew_symmetric()
            False

        Skew-symmetric is not the same as alternating when
        `2` is a zero-divisor in the ground ring::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 2]])
            sage: n.is_skew_symmetric()
            True

        but yet the diagonal cannot be completely
        arbitrary in this case::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 3]])
            sage: n.is_skew_symmetric()
            False'''
    @overload
    def is_skew_symmetric(self) -> Any:
        '''Matrix.is_skew_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4387)

        Return ``True`` if ``self`` is a skew-symmetric matrix.

        Here, "skew-symmetric matrix" means a square matrix `A`
        satisfying `A^T = -A`. It does not require that the
        diagonal entries of `A` are `0` (although this
        automatically follows from `A^T = -A` when `2` is
        invertible in the ground ring over which the matrix is
        considered). Skew-symmetric matrices `A` whose diagonal
        entries are `0` are said to be "alternating", and this
        property is checked by the :meth:`is_alternating`
        method.

        EXAMPLES::

            sage: m = matrix(QQ, [[0,2], [-2,0]])
            sage: m.is_skew_symmetric()
            True
            sage: m = matrix(QQ, [[1,2], [2,1]])
            sage: m.is_skew_symmetric()
            False

        Skew-symmetric is not the same as alternating when
        `2` is a zero-divisor in the ground ring::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 2]])
            sage: n.is_skew_symmetric()
            True

        but yet the diagonal cannot be completely
        arbitrary in this case::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 3]])
            sage: n.is_skew_symmetric()
            False'''
    @overload
    def is_skew_symmetric(self) -> Any:
        '''Matrix.is_skew_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4387)

        Return ``True`` if ``self`` is a skew-symmetric matrix.

        Here, "skew-symmetric matrix" means a square matrix `A`
        satisfying `A^T = -A`. It does not require that the
        diagonal entries of `A` are `0` (although this
        automatically follows from `A^T = -A` when `2` is
        invertible in the ground ring over which the matrix is
        considered). Skew-symmetric matrices `A` whose diagonal
        entries are `0` are said to be "alternating", and this
        property is checked by the :meth:`is_alternating`
        method.

        EXAMPLES::

            sage: m = matrix(QQ, [[0,2], [-2,0]])
            sage: m.is_skew_symmetric()
            True
            sage: m = matrix(QQ, [[1,2], [2,1]])
            sage: m.is_skew_symmetric()
            False

        Skew-symmetric is not the same as alternating when
        `2` is a zero-divisor in the ground ring::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 2]])
            sage: n.is_skew_symmetric()
            True

        but yet the diagonal cannot be completely
        arbitrary in this case::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 3]])
            sage: n.is_skew_symmetric()
            False'''
    @overload
    def is_skew_symmetric(self) -> Any:
        '''Matrix.is_skew_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4387)

        Return ``True`` if ``self`` is a skew-symmetric matrix.

        Here, "skew-symmetric matrix" means a square matrix `A`
        satisfying `A^T = -A`. It does not require that the
        diagonal entries of `A` are `0` (although this
        automatically follows from `A^T = -A` when `2` is
        invertible in the ground ring over which the matrix is
        considered). Skew-symmetric matrices `A` whose diagonal
        entries are `0` are said to be "alternating", and this
        property is checked by the :meth:`is_alternating`
        method.

        EXAMPLES::

            sage: m = matrix(QQ, [[0,2], [-2,0]])
            sage: m.is_skew_symmetric()
            True
            sage: m = matrix(QQ, [[1,2], [2,1]])
            sage: m.is_skew_symmetric()
            False

        Skew-symmetric is not the same as alternating when
        `2` is a zero-divisor in the ground ring::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 2]])
            sage: n.is_skew_symmetric()
            True

        but yet the diagonal cannot be completely
        arbitrary in this case::

            sage: n = matrix(Zmod(4), [[0, 1], [-1, 3]])
            sage: n.is_skew_symmetric()
            False'''
    @overload
    def is_skew_symmetrizable(self, return_diag=..., positive=...) -> Any:
        """Matrix.is_skew_symmetrizable(self, return_diag=False, positive=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4532)

        This function takes a square matrix over an *ordered integral domain*
        and checks if it is skew-symmetrizable.
        A matrix `B` is skew-symmetrizable iff there exists an invertible
        diagonal matrix `D` such that `DB` is skew-symmetric.

        .. warning:: Expects ``self`` to be a matrix over an *ordered integral domain*.

        INPUT:

        - ``return_diag`` -- boolean (default: ``False``); if ``True`` and
          ``self`` is skew-symmetrizable the diagonal entries of the matrix `D`
          are returned
        - ``positive`` -- boolean (default: ``True``); if ``True``, the
          condition that `D` has positive entries is added

        OUTPUT:

        - ``True`` -- if ``self`` is skew-symmetrizable and ``return_diag`` is
          ``False``
        - the diagonal entries of a matrix `D` such that `DB` is
          skew-symmetric -- iff ``self`` is skew-symmetrizable and ``return_diag``
          is ``True``
        - ``False`` -- iff ``self`` is not skew-symmetrizable

        EXAMPLES::

            sage: matrix([[0,6],[3,0]]).is_skew_symmetrizable(positive=False)
            True
            sage: matrix([[0,6],[3,0]]).is_skew_symmetrizable(positive=True)
            False

            sage: M = matrix(4, [0,1,0,0, -1,0,-1,0, 0,2,0,1, 0,0,-1,0]); M
            [ 0  1  0  0]
            [-1  0 -1  0]
            [ 0  2  0  1]
            [ 0  0 -1  0]

            sage: M.is_skew_symmetrizable(return_diag=True)
            [1, 1, 1/2, 1/2]

            sage: M2 = diagonal_matrix([1,1,1/2,1/2]) * M; M2
            [   0    1    0    0]
            [  -1    0   -1    0]
            [   0    1    0  1/2]
            [   0    0 -1/2    0]

            sage: M2.is_skew_symmetric()
            True

        REFERENCES:

        - [FZ2001]_"""
    @overload
    def is_skew_symmetrizable(self, positive=...) -> Any:
        """Matrix.is_skew_symmetrizable(self, return_diag=False, positive=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4532)

        This function takes a square matrix over an *ordered integral domain*
        and checks if it is skew-symmetrizable.
        A matrix `B` is skew-symmetrizable iff there exists an invertible
        diagonal matrix `D` such that `DB` is skew-symmetric.

        .. warning:: Expects ``self`` to be a matrix over an *ordered integral domain*.

        INPUT:

        - ``return_diag`` -- boolean (default: ``False``); if ``True`` and
          ``self`` is skew-symmetrizable the diagonal entries of the matrix `D`
          are returned
        - ``positive`` -- boolean (default: ``True``); if ``True``, the
          condition that `D` has positive entries is added

        OUTPUT:

        - ``True`` -- if ``self`` is skew-symmetrizable and ``return_diag`` is
          ``False``
        - the diagonal entries of a matrix `D` such that `DB` is
          skew-symmetric -- iff ``self`` is skew-symmetrizable and ``return_diag``
          is ``True``
        - ``False`` -- iff ``self`` is not skew-symmetrizable

        EXAMPLES::

            sage: matrix([[0,6],[3,0]]).is_skew_symmetrizable(positive=False)
            True
            sage: matrix([[0,6],[3,0]]).is_skew_symmetrizable(positive=True)
            False

            sage: M = matrix(4, [0,1,0,0, -1,0,-1,0, 0,2,0,1, 0,0,-1,0]); M
            [ 0  1  0  0]
            [-1  0 -1  0]
            [ 0  2  0  1]
            [ 0  0 -1  0]

            sage: M.is_skew_symmetrizable(return_diag=True)
            [1, 1, 1/2, 1/2]

            sage: M2 = diagonal_matrix([1,1,1/2,1/2]) * M; M2
            [   0    1    0    0]
            [  -1    0   -1    0]
            [   0    1    0  1/2]
            [   0    0 -1/2    0]

            sage: M2.is_skew_symmetric()
            True

        REFERENCES:

        - [FZ2001]_"""
    @overload
    def is_skew_symmetrizable(self, positive=...) -> Any:
        """Matrix.is_skew_symmetrizable(self, return_diag=False, positive=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4532)

        This function takes a square matrix over an *ordered integral domain*
        and checks if it is skew-symmetrizable.
        A matrix `B` is skew-symmetrizable iff there exists an invertible
        diagonal matrix `D` such that `DB` is skew-symmetric.

        .. warning:: Expects ``self`` to be a matrix over an *ordered integral domain*.

        INPUT:

        - ``return_diag`` -- boolean (default: ``False``); if ``True`` and
          ``self`` is skew-symmetrizable the diagonal entries of the matrix `D`
          are returned
        - ``positive`` -- boolean (default: ``True``); if ``True``, the
          condition that `D` has positive entries is added

        OUTPUT:

        - ``True`` -- if ``self`` is skew-symmetrizable and ``return_diag`` is
          ``False``
        - the diagonal entries of a matrix `D` such that `DB` is
          skew-symmetric -- iff ``self`` is skew-symmetrizable and ``return_diag``
          is ``True``
        - ``False`` -- iff ``self`` is not skew-symmetrizable

        EXAMPLES::

            sage: matrix([[0,6],[3,0]]).is_skew_symmetrizable(positive=False)
            True
            sage: matrix([[0,6],[3,0]]).is_skew_symmetrizable(positive=True)
            False

            sage: M = matrix(4, [0,1,0,0, -1,0,-1,0, 0,2,0,1, 0,0,-1,0]); M
            [ 0  1  0  0]
            [-1  0 -1  0]
            [ 0  2  0  1]
            [ 0  0 -1  0]

            sage: M.is_skew_symmetrizable(return_diag=True)
            [1, 1, 1/2, 1/2]

            sage: M2 = diagonal_matrix([1,1,1/2,1/2]) * M; M2
            [   0    1    0    0]
            [  -1    0   -1    0]
            [   0    1    0  1/2]
            [   0    0 -1/2    0]

            sage: M2.is_skew_symmetric()
            True

        REFERENCES:

        - [FZ2001]_"""
    @overload
    def is_skew_symmetrizable(self, return_diag=...) -> Any:
        """Matrix.is_skew_symmetrizable(self, return_diag=False, positive=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4532)

        This function takes a square matrix over an *ordered integral domain*
        and checks if it is skew-symmetrizable.
        A matrix `B` is skew-symmetrizable iff there exists an invertible
        diagonal matrix `D` such that `DB` is skew-symmetric.

        .. warning:: Expects ``self`` to be a matrix over an *ordered integral domain*.

        INPUT:

        - ``return_diag`` -- boolean (default: ``False``); if ``True`` and
          ``self`` is skew-symmetrizable the diagonal entries of the matrix `D`
          are returned
        - ``positive`` -- boolean (default: ``True``); if ``True``, the
          condition that `D` has positive entries is added

        OUTPUT:

        - ``True`` -- if ``self`` is skew-symmetrizable and ``return_diag`` is
          ``False``
        - the diagonal entries of a matrix `D` such that `DB` is
          skew-symmetric -- iff ``self`` is skew-symmetrizable and ``return_diag``
          is ``True``
        - ``False`` -- iff ``self`` is not skew-symmetrizable

        EXAMPLES::

            sage: matrix([[0,6],[3,0]]).is_skew_symmetrizable(positive=False)
            True
            sage: matrix([[0,6],[3,0]]).is_skew_symmetrizable(positive=True)
            False

            sage: M = matrix(4, [0,1,0,0, -1,0,-1,0, 0,2,0,1, 0,0,-1,0]); M
            [ 0  1  0  0]
            [-1  0 -1  0]
            [ 0  2  0  1]
            [ 0  0 -1  0]

            sage: M.is_skew_symmetrizable(return_diag=True)
            [1, 1, 1/2, 1/2]

            sage: M2 = diagonal_matrix([1,1,1/2,1/2]) * M; M2
            [   0    1    0    0]
            [  -1    0   -1    0]
            [   0    1    0  1/2]
            [   0    0 -1/2    0]

            sage: M2.is_skew_symmetric()
            True

        REFERENCES:

        - [FZ2001]_"""
    @overload
    def is_sparse(self) -> Any:
        """Matrix.is_sparse(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4607)

        Return ``True`` if this is a sparse matrix.

        In Sage, being sparse is a property of the underlying
        representation, not the number of nonzero entries.

        EXAMPLES::

            sage: matrix(QQ, 2, 2, range(4)).is_sparse()
            False
            sage: matrix(QQ, 2, 2, range(4), sparse=True).is_sparse()
            True"""
    @overload
    def is_sparse(self) -> Any:
        """Matrix.is_sparse(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4607)

        Return ``True`` if this is a sparse matrix.

        In Sage, being sparse is a property of the underlying
        representation, not the number of nonzero entries.

        EXAMPLES::

            sage: matrix(QQ, 2, 2, range(4)).is_sparse()
            False
            sage: matrix(QQ, 2, 2, range(4), sparse=True).is_sparse()
            True"""
    @overload
    def is_sparse(self) -> Any:
        """Matrix.is_sparse(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4607)

        Return ``True`` if this is a sparse matrix.

        In Sage, being sparse is a property of the underlying
        representation, not the number of nonzero entries.

        EXAMPLES::

            sage: matrix(QQ, 2, 2, range(4)).is_sparse()
            False
            sage: matrix(QQ, 2, 2, range(4), sparse=True).is_sparse()
            True"""
    @overload
    def is_square(self) -> Any:
        """Matrix.is_square(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4623)

        Return ``True`` precisely if this matrix is square, i.e., has the same
        number of rows and columns.

        EXAMPLES::

            sage: matrix(QQ, 2, 2, range(4)).is_square()
            True
            sage: matrix(QQ, 2, 3, range(6)).is_square()
            False"""
    @overload
    def is_square(self) -> Any:
        """Matrix.is_square(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4623)

        Return ``True`` precisely if this matrix is square, i.e., has the same
        number of rows and columns.

        EXAMPLES::

            sage: matrix(QQ, 2, 2, range(4)).is_square()
            True
            sage: matrix(QQ, 2, 3, range(6)).is_square()
            False"""
    @overload
    def is_square(self) -> Any:
        """Matrix.is_square(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4623)

        Return ``True`` precisely if this matrix is square, i.e., has the same
        number of rows and columns.

        EXAMPLES::

            sage: matrix(QQ, 2, 2, range(4)).is_square()
            True
            sage: matrix(QQ, 2, 3, range(6)).is_square()
            False"""
    @overload
    def is_symmetric(self) -> Any:
        """Matrix.is_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4071)

        Return ``True`` if this is a symmetric matrix.

        A symmetric matrix is necessarily square.

        EXAMPLES::

            sage: m = Matrix(QQ, 2, range(0,4))
            sage: m.is_symmetric()
            False

            sage: m = Matrix(QQ, 2, (1,1,1,1,1,1))
            sage: m.is_symmetric()
            False

            sage: m = Matrix(QQ, 1, (2,))
            sage: m.is_symmetric()
            True"""
    @overload
    def is_symmetric(self) -> Any:
        """Matrix.is_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4071)

        Return ``True`` if this is a symmetric matrix.

        A symmetric matrix is necessarily square.

        EXAMPLES::

            sage: m = Matrix(QQ, 2, range(0,4))
            sage: m.is_symmetric()
            False

            sage: m = Matrix(QQ, 2, (1,1,1,1,1,1))
            sage: m.is_symmetric()
            False

            sage: m = Matrix(QQ, 1, (2,))
            sage: m.is_symmetric()
            True"""
    @overload
    def is_symmetric(self) -> Any:
        """Matrix.is_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4071)

        Return ``True`` if this is a symmetric matrix.

        A symmetric matrix is necessarily square.

        EXAMPLES::

            sage: m = Matrix(QQ, 2, range(0,4))
            sage: m.is_symmetric()
            False

            sage: m = Matrix(QQ, 2, (1,1,1,1,1,1))
            sage: m.is_symmetric()
            False

            sage: m = Matrix(QQ, 1, (2,))
            sage: m.is_symmetric()
            True"""
    @overload
    def is_symmetric(self) -> Any:
        """Matrix.is_symmetric(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4071)

        Return ``True`` if this is a symmetric matrix.

        A symmetric matrix is necessarily square.

        EXAMPLES::

            sage: m = Matrix(QQ, 2, range(0,4))
            sage: m.is_symmetric()
            False

            sage: m = Matrix(QQ, 2, (1,1,1,1,1,1))
            sage: m.is_symmetric()
            False

            sage: m = Matrix(QQ, 1, (2,))
            sage: m.is_symmetric()
            True"""
    @overload
    def is_symmetrizable(self, return_diag=..., positive=...) -> Any:
        """Matrix.is_symmetrizable(self, return_diag=False, positive=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4481)

        This function takes a square matrix over an *ordered integral domain*
        and checks if it is symmetrizable.

        A matrix `B` is symmetrizable iff there exists an invertible diagonal
        matrix `D` such that `DB` is symmetric.

        .. warning:: Expects ``self`` to be a matrix over an *ordered integral domain*.

        INPUT:

        - ``return_diag`` -- boolean (default: ``False``); if ``True`` and
          ``self`` is symmetrizable the diagonal entries of the matrix `D` are
          returned
        - ``positive`` -- boolean (default: ``True``); if ``True``, the
          condition that `D` has positive entries is added

        OUTPUT:

        - ``True`` -- if ``self`` is symmetrizable and ``return_diag`` is
          ``False``
        - the diagonal entries of a matrix `D` such that `DB` is symmetric --
          iff ``self`` is symmetrizable and ``return_diag`` is ``True``
        - ``False`` -- iff ``self`` is not symmetrizable

        EXAMPLES::

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=False)
            True

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=True)
            True

            sage: matrix([[0,6],[0,0]]).is_symmetrizable(return_diag=True)
            False

            sage: matrix([2]).is_symmetrizable(positive=True)
            True

            sage: matrix([[1,2],[3,4]]).is_symmetrizable(return_diag=true)
            [1, 2/3]

        REFERENCES:

        - [FZ2001]_"""
    @overload
    def is_symmetrizable(self, positive=...) -> Any:
        """Matrix.is_symmetrizable(self, return_diag=False, positive=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4481)

        This function takes a square matrix over an *ordered integral domain*
        and checks if it is symmetrizable.

        A matrix `B` is symmetrizable iff there exists an invertible diagonal
        matrix `D` such that `DB` is symmetric.

        .. warning:: Expects ``self`` to be a matrix over an *ordered integral domain*.

        INPUT:

        - ``return_diag`` -- boolean (default: ``False``); if ``True`` and
          ``self`` is symmetrizable the diagonal entries of the matrix `D` are
          returned
        - ``positive`` -- boolean (default: ``True``); if ``True``, the
          condition that `D` has positive entries is added

        OUTPUT:

        - ``True`` -- if ``self`` is symmetrizable and ``return_diag`` is
          ``False``
        - the diagonal entries of a matrix `D` such that `DB` is symmetric --
          iff ``self`` is symmetrizable and ``return_diag`` is ``True``
        - ``False`` -- iff ``self`` is not symmetrizable

        EXAMPLES::

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=False)
            True

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=True)
            True

            sage: matrix([[0,6],[0,0]]).is_symmetrizable(return_diag=True)
            False

            sage: matrix([2]).is_symmetrizable(positive=True)
            True

            sage: matrix([[1,2],[3,4]]).is_symmetrizable(return_diag=true)
            [1, 2/3]

        REFERENCES:

        - [FZ2001]_"""
    @overload
    def is_symmetrizable(self, positive=...) -> Any:
        """Matrix.is_symmetrizable(self, return_diag=False, positive=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4481)

        This function takes a square matrix over an *ordered integral domain*
        and checks if it is symmetrizable.

        A matrix `B` is symmetrizable iff there exists an invertible diagonal
        matrix `D` such that `DB` is symmetric.

        .. warning:: Expects ``self`` to be a matrix over an *ordered integral domain*.

        INPUT:

        - ``return_diag`` -- boolean (default: ``False``); if ``True`` and
          ``self`` is symmetrizable the diagonal entries of the matrix `D` are
          returned
        - ``positive`` -- boolean (default: ``True``); if ``True``, the
          condition that `D` has positive entries is added

        OUTPUT:

        - ``True`` -- if ``self`` is symmetrizable and ``return_diag`` is
          ``False``
        - the diagonal entries of a matrix `D` such that `DB` is symmetric --
          iff ``self`` is symmetrizable and ``return_diag`` is ``True``
        - ``False`` -- iff ``self`` is not symmetrizable

        EXAMPLES::

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=False)
            True

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=True)
            True

            sage: matrix([[0,6],[0,0]]).is_symmetrizable(return_diag=True)
            False

            sage: matrix([2]).is_symmetrizable(positive=True)
            True

            sage: matrix([[1,2],[3,4]]).is_symmetrizable(return_diag=true)
            [1, 2/3]

        REFERENCES:

        - [FZ2001]_"""
    @overload
    def is_symmetrizable(self, return_diag=...) -> Any:
        """Matrix.is_symmetrizable(self, return_diag=False, positive=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4481)

        This function takes a square matrix over an *ordered integral domain*
        and checks if it is symmetrizable.

        A matrix `B` is symmetrizable iff there exists an invertible diagonal
        matrix `D` such that `DB` is symmetric.

        .. warning:: Expects ``self`` to be a matrix over an *ordered integral domain*.

        INPUT:

        - ``return_diag`` -- boolean (default: ``False``); if ``True`` and
          ``self`` is symmetrizable the diagonal entries of the matrix `D` are
          returned
        - ``positive`` -- boolean (default: ``True``); if ``True``, the
          condition that `D` has positive entries is added

        OUTPUT:

        - ``True`` -- if ``self`` is symmetrizable and ``return_diag`` is
          ``False``
        - the diagonal entries of a matrix `D` such that `DB` is symmetric --
          iff ``self`` is symmetrizable and ``return_diag`` is ``True``
        - ``False`` -- iff ``self`` is not symmetrizable

        EXAMPLES::

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=False)
            True

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=True)
            True

            sage: matrix([[0,6],[0,0]]).is_symmetrizable(return_diag=True)
            False

            sage: matrix([2]).is_symmetrizable(positive=True)
            True

            sage: matrix([[1,2],[3,4]]).is_symmetrizable(return_diag=true)
            [1, 2/3]

        REFERENCES:

        - [FZ2001]_"""
    @overload
    def is_symmetrizable(self, positive=...) -> Any:
        """Matrix.is_symmetrizable(self, return_diag=False, positive=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4481)

        This function takes a square matrix over an *ordered integral domain*
        and checks if it is symmetrizable.

        A matrix `B` is symmetrizable iff there exists an invertible diagonal
        matrix `D` such that `DB` is symmetric.

        .. warning:: Expects ``self`` to be a matrix over an *ordered integral domain*.

        INPUT:

        - ``return_diag`` -- boolean (default: ``False``); if ``True`` and
          ``self`` is symmetrizable the diagonal entries of the matrix `D` are
          returned
        - ``positive`` -- boolean (default: ``True``); if ``True``, the
          condition that `D` has positive entries is added

        OUTPUT:

        - ``True`` -- if ``self`` is symmetrizable and ``return_diag`` is
          ``False``
        - the diagonal entries of a matrix `D` such that `DB` is symmetric --
          iff ``self`` is symmetrizable and ``return_diag`` is ``True``
        - ``False`` -- iff ``self`` is not symmetrizable

        EXAMPLES::

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=False)
            True

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=True)
            True

            sage: matrix([[0,6],[0,0]]).is_symmetrizable(return_diag=True)
            False

            sage: matrix([2]).is_symmetrizable(positive=True)
            True

            sage: matrix([[1,2],[3,4]]).is_symmetrizable(return_diag=true)
            [1, 2/3]

        REFERENCES:

        - [FZ2001]_"""
    @overload
    def is_symmetrizable(self, return_diag=...) -> Any:
        """Matrix.is_symmetrizable(self, return_diag=False, positive=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4481)

        This function takes a square matrix over an *ordered integral domain*
        and checks if it is symmetrizable.

        A matrix `B` is symmetrizable iff there exists an invertible diagonal
        matrix `D` such that `DB` is symmetric.

        .. warning:: Expects ``self`` to be a matrix over an *ordered integral domain*.

        INPUT:

        - ``return_diag`` -- boolean (default: ``False``); if ``True`` and
          ``self`` is symmetrizable the diagonal entries of the matrix `D` are
          returned
        - ``positive`` -- boolean (default: ``True``); if ``True``, the
          condition that `D` has positive entries is added

        OUTPUT:

        - ``True`` -- if ``self`` is symmetrizable and ``return_diag`` is
          ``False``
        - the diagonal entries of a matrix `D` such that `DB` is symmetric --
          iff ``self`` is symmetrizable and ``return_diag`` is ``True``
        - ``False`` -- iff ``self`` is not symmetrizable

        EXAMPLES::

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=False)
            True

            sage: matrix([[0,6],[3,0]]).is_symmetrizable(positive=True)
            True

            sage: matrix([[0,6],[0,0]]).is_symmetrizable(return_diag=True)
            False

            sage: matrix([2]).is_symmetrizable(positive=True)
            True

            sage: matrix([[1,2],[3,4]]).is_symmetrizable(return_diag=true)
            [1, 2/3]

        REFERENCES:

        - [FZ2001]_"""
    def is_unit(self, *args, **kwargs):
        """Matrix.is_invertible(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4637)

        Return ``True`` if this matrix is invertible.

        EXAMPLES: The following matrix is invertible over
        `\\QQ` but not over `\\ZZ`.

        ::

            sage: A = MatrixSpace(ZZ, 2)(range(4))
            sage: A.is_invertible()
            False
            sage: A.matrix_over_field().is_invertible()
            True

        The inverse function is a constructor for matrices over the
        fraction field, so it can work even if A is not invertible.

        ::

            sage: ~A   # inverse of A
            [-3/2  1/2]
            [   1    0]

        The next matrix is invertible over `\\ZZ`.

        ::

            sage: A = MatrixSpace(IntegerRing(), 2)([1,10,0,-1])
            sage: A.is_invertible()
            True
            sage: ~A                # compute the inverse
            [ 1 10]
            [ 0 -1]

        The following nontrivial matrix is invertible over
        `\\ZZ[x]`.

        ::

            sage: R.<x> = PolynomialRing(IntegerRing())
            sage: A = MatrixSpace(R, 2)([1,x,0,-1])
            sage: A.is_invertible()
            True
            sage: ~A
            [ 1  x]
            [ 0 -1]"""
    @overload
    def items(self) -> Any:
        """Matrix.items(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 270)

        Return an iterable of ``((i,j), value)`` elements.

        This may (but is not guaranteed to) suppress zero values.

        EXAMPLES::

            sage: a = matrix(QQ['x,y'], 2, range(6), sparse=True); a
            [0 1 2]
            [3 4 5]
            sage: list(a.items())
            [((0, 1), 1), ((0, 2), 2), ((1, 0), 3), ((1, 1), 4), ((1, 2), 5)]"""
    @overload
    def items(self) -> Any:
        """Matrix.items(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 270)

        Return an iterable of ``((i,j), value)`` elements.

        This may (but is not guaranteed to) suppress zero values.

        EXAMPLES::

            sage: a = matrix(QQ['x,y'], 2, range(6), sparse=True); a
            [0 1 2]
            [3 4 5]
            sage: list(a.items())
            [((0, 1), 1), ((0, 2), 2), ((1, 0), 3), ((1, 1), 4), ((1, 2), 5)]"""
    def iterates(self, v, n, rows=...) -> Any:
        """Matrix.iterates(self, v, n, rows=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5278)

        Let `A` be this matrix and `v` be a free module
        element. If rows is True, return a matrix whose rows are the
        entries of the following vectors:

        .. MATH::

                       v, v A, v A^2, \\dots, v A^{n-1}.

        If rows is False, return a matrix whose columns are the entries of
        the following vectors:

        .. MATH::

                       v, Av, A^2 v, \\dots, A^{n-1} v.

        INPUT:

        - ``v`` -- free module element

        - ``n`` -- nonnegative integer

        EXAMPLES::

            sage: A = matrix(ZZ, 2, [1,1,3,5]); A
            [1 1]
            [3 5]
            sage: v = vector([1,0])
            sage: A.iterates(v, 0)
            []
            sage: A.iterates(v, 5)
            [  1   0]
            [  1   1]
            [  4   6]
            [ 22  34]
            [124 192]

        Another example::

            sage: a = matrix(ZZ, 3, range(9)); a
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: v = vector([1,0,0])
            sage: a.iterates(v, 4)
            [  1   0   0]
            [  0   1   2]
            [ 15  18  21]
            [180 234 288]
            sage: a.iterates(v, 4, rows=False)
            [  1   0  15 180]
            [  0   3  42 558]
            [  0   6  69 936]"""
    @overload
    def linear_combination_of_columns(self, v) -> Any:
        """Matrix.linear_combination_of_columns(self, v)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3990)

        Return the linear combination of the columns of ``self`` given by the
        coefficients in the list ``v``.

        INPUT:

        - ``v`` -- a list of scalars.  The length can be less than
          the number of columns of ``self`` but not greater.

        OUTPUT:

        The vector (or free module element) that is a linear
        combination of the columns of ``self``. If the list of
        scalars has fewer entries than the number of columns,
        additional zeros are appended to the list until it
        has as many entries as the number of columns.

        EXAMPLES::

            sage: a = matrix(ZZ, 2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.linear_combination_of_columns([1,1,1])
            (3, 12)

            sage: a.linear_combination_of_columns([0,0,0])
            (0, 0)

            sage: a.linear_combination_of_columns([1/2,2/3,3/4])
            (13/6, 95/12)

        The list ``v`` can be anything that is iterable.  Perhaps most
        naturally, a vector may be used. ::

            sage: v = vector(ZZ, [1,2,3])
            sage: a.linear_combination_of_columns(v)
            (8, 26)

        We check that a matrix with no columns behaves properly. ::

            sage: matrix(QQ, 2, 0).linear_combination_of_columns([])
            (0, 0)

        The object returned is a vector, or a free module element. ::

            sage: B = matrix(ZZ, 4, 3, range(12))
            sage: w = B.linear_combination_of_columns([-1,2,-3])
            sage: w
            (-4, -10, -16, -22)
            sage: w.parent()
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
            sage: x = B.linear_combination_of_columns([1/2,1/3,1/4])
            sage: x
            (5/6, 49/12, 22/3, 127/12)
            sage: x.parent()
            Vector space of dimension 4 over Rational Field

        The length of v can be less than the number of columns, but not
        greater. ::

            sage: A = matrix(QQ, 3, 5, range(15))
            sage: A.linear_combination_of_columns([1,-2,3,-4])
            (-8, -18, -28)
            sage: A.linear_combination_of_columns([1,2,3,4,5,6])
            Traceback (most recent call last):
            ...
            ValueError: length of v must be at most the number of columns of self"""
    @overload
    def linear_combination_of_columns(self, v) -> Any:
        """Matrix.linear_combination_of_columns(self, v)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3990)

        Return the linear combination of the columns of ``self`` given by the
        coefficients in the list ``v``.

        INPUT:

        - ``v`` -- a list of scalars.  The length can be less than
          the number of columns of ``self`` but not greater.

        OUTPUT:

        The vector (or free module element) that is a linear
        combination of the columns of ``self``. If the list of
        scalars has fewer entries than the number of columns,
        additional zeros are appended to the list until it
        has as many entries as the number of columns.

        EXAMPLES::

            sage: a = matrix(ZZ, 2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.linear_combination_of_columns([1,1,1])
            (3, 12)

            sage: a.linear_combination_of_columns([0,0,0])
            (0, 0)

            sage: a.linear_combination_of_columns([1/2,2/3,3/4])
            (13/6, 95/12)

        The list ``v`` can be anything that is iterable.  Perhaps most
        naturally, a vector may be used. ::

            sage: v = vector(ZZ, [1,2,3])
            sage: a.linear_combination_of_columns(v)
            (8, 26)

        We check that a matrix with no columns behaves properly. ::

            sage: matrix(QQ, 2, 0).linear_combination_of_columns([])
            (0, 0)

        The object returned is a vector, or a free module element. ::

            sage: B = matrix(ZZ, 4, 3, range(12))
            sage: w = B.linear_combination_of_columns([-1,2,-3])
            sage: w
            (-4, -10, -16, -22)
            sage: w.parent()
            Ambient free module of rank 4 over the principal ideal domain Integer Ring
            sage: x = B.linear_combination_of_columns([1/2,1/3,1/4])
            sage: x
            (5/6, 49/12, 22/3, 127/12)
            sage: x.parent()
            Vector space of dimension 4 over Rational Field

        The length of v can be less than the number of columns, but not
        greater. ::

            sage: A = matrix(QQ, 3, 5, range(15))
            sage: A.linear_combination_of_columns([1,-2,3,-4])
            (-8, -18, -28)
            sage: A.linear_combination_of_columns([1,2,3,4,5,6])
            Traceback (most recent call last):
            ...
            ValueError: length of v must be at most the number of columns of self"""
    @overload
    def linear_combination_of_rows(self, v) -> Any:
        """Matrix.linear_combination_of_rows(self, v)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3913)

        Return the linear combination of the rows of ``self`` given by the
        coefficients in the list ``v``.

        INPUT:

        - ``v`` -- a list of scalars.  The length can be less than
          the number of rows of ``self`` but not greater.

        OUTPUT:

        The vector (or free module element) that is a linear
        combination of the rows of ``self``. If the list of
        scalars has fewer entries than the number of rows,
        additional zeros are appended to the list until it
        has as many entries as the number of rows.

        EXAMPLES::

            sage: a = matrix(ZZ, 2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.linear_combination_of_rows([1,2])
            (6, 9, 12)

            sage: a.linear_combination_of_rows([0,0])
            (0, 0, 0)

            sage: a.linear_combination_of_rows([1/2,2/3])
            (2, 19/6, 13/3)

        The list ``v`` can be anything that is iterable.  Perhaps most
        naturally, a vector may be used. ::

            sage: v = vector(ZZ, [1,2])
            sage: a.linear_combination_of_rows(v)
            (6, 9, 12)

        We check that a matrix with no rows behaves properly. ::

            sage: matrix(QQ, 0, 2).linear_combination_of_rows([])
            (0, 0)

        The object returned is a vector, or a free module element. ::

            sage: B = matrix(ZZ, 4, 3, range(12))
            sage: w = B.linear_combination_of_rows([-1,2,-3,4])
            sage: w
            (24, 26, 28)
            sage: w.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: x = B.linear_combination_of_rows([1/2,1/3,1/4,1/5])
            sage: x
            (43/10, 67/12, 103/15)
            sage: x.parent()
            Vector space of dimension 3 over Rational Field

        The length of v can be less than the number of rows, but not
        greater. ::

            sage: A = matrix(QQ, 3, 4, range(12))
            sage: A.linear_combination_of_rows([2,3])
            (12, 17, 22, 27)
            sage: A.linear_combination_of_rows([1,2,3,4])
            Traceback (most recent call last):
            ...
            ValueError: length of v must be at most the number of rows of self"""
    @overload
    def linear_combination_of_rows(self, v) -> Any:
        """Matrix.linear_combination_of_rows(self, v)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3913)

        Return the linear combination of the rows of ``self`` given by the
        coefficients in the list ``v``.

        INPUT:

        - ``v`` -- a list of scalars.  The length can be less than
          the number of rows of ``self`` but not greater.

        OUTPUT:

        The vector (or free module element) that is a linear
        combination of the rows of ``self``. If the list of
        scalars has fewer entries than the number of rows,
        additional zeros are appended to the list until it
        has as many entries as the number of rows.

        EXAMPLES::

            sage: a = matrix(ZZ, 2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.linear_combination_of_rows([1,2])
            (6, 9, 12)

            sage: a.linear_combination_of_rows([0,0])
            (0, 0, 0)

            sage: a.linear_combination_of_rows([1/2,2/3])
            (2, 19/6, 13/3)

        The list ``v`` can be anything that is iterable.  Perhaps most
        naturally, a vector may be used. ::

            sage: v = vector(ZZ, [1,2])
            sage: a.linear_combination_of_rows(v)
            (6, 9, 12)

        We check that a matrix with no rows behaves properly. ::

            sage: matrix(QQ, 0, 2).linear_combination_of_rows([])
            (0, 0)

        The object returned is a vector, or a free module element. ::

            sage: B = matrix(ZZ, 4, 3, range(12))
            sage: w = B.linear_combination_of_rows([-1,2,-3,4])
            sage: w
            (24, 26, 28)
            sage: w.parent()
            Ambient free module of rank 3 over the principal ideal domain Integer Ring
            sage: x = B.linear_combination_of_rows([1/2,1/3,1/4,1/5])
            sage: x
            (43/10, 67/12, 103/15)
            sage: x.parent()
            Vector space of dimension 3 over Rational Field

        The length of v can be less than the number of rows, but not
        greater. ::

            sage: A = matrix(QQ, 3, 4, range(12))
            sage: A.linear_combination_of_rows([2,3])
            (12, 17, 22, 27)
            sage: A.linear_combination_of_rows([1,2,3,4])
            Traceback (most recent call last):
            ...
            ValueError: length of v must be at most the number of rows of self"""
    @overload
    def list(self) -> Any:
        """Matrix.list(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 121)

        List of the elements of ``self`` ordered by elements in each
        row. It is safe to change the returned list.

        .. warning::

           This function returns a list of the entries in the matrix
           ``self``.  It does not return a list of the rows of ``self``,
           so it is different than the output of ``list(self)``, which
           returns ``[self[0],self[1],...]``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: a = matrix(R,2,[x,y,x*y, y,x,2*x+y]); a
            [      x       y     x*y]
            [      y       x 2*x + y]
            sage: v = a.list(); v
            [x, y, x*y, y, x, 2*x + y]

        Note that list(a) is different than a.list()::

            sage: a.list()
            [x, y, x*y, y, x, 2*x + y]
            sage: list(a)
            [(x, y, x*y), (y, x, 2*x + y)]

        Notice that changing the returned list does not change a (the list
        is a copy)::

            sage: v[0] = 25
            sage: a
            [      x       y     x*y]
            [      y       x 2*x + y]"""
    @overload
    def list(self) -> Any:
        """Matrix.list(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 121)

        List of the elements of ``self`` ordered by elements in each
        row. It is safe to change the returned list.

        .. warning::

           This function returns a list of the entries in the matrix
           ``self``.  It does not return a list of the rows of ``self``,
           so it is different than the output of ``list(self)``, which
           returns ``[self[0],self[1],...]``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: a = matrix(R,2,[x,y,x*y, y,x,2*x+y]); a
            [      x       y     x*y]
            [      y       x 2*x + y]
            sage: v = a.list(); v
            [x, y, x*y, y, x, 2*x + y]

        Note that list(a) is different than a.list()::

            sage: a.list()
            [x, y, x*y, y, x, 2*x + y]
            sage: list(a)
            [(x, y, x*y), (y, x, 2*x + y)]

        Notice that changing the returned list does not change a (the list
        is a copy)::

            sage: v[0] = 25
            sage: a
            [      x       y     x*y]
            [      y       x 2*x + y]"""
    @overload
    def list(self) -> Any:
        """Matrix.list(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 121)

        List of the elements of ``self`` ordered by elements in each
        row. It is safe to change the returned list.

        .. warning::

           This function returns a list of the entries in the matrix
           ``self``.  It does not return a list of the rows of ``self``,
           so it is different than the output of ``list(self)``, which
           returns ``[self[0],self[1],...]``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: a = matrix(R,2,[x,y,x*y, y,x,2*x+y]); a
            [      x       y     x*y]
            [      y       x 2*x + y]
            sage: v = a.list(); v
            [x, y, x*y, y, x, 2*x + y]

        Note that list(a) is different than a.list()::

            sage: a.list()
            [x, y, x*y, y, x, 2*x + y]
            sage: list(a)
            [(x, y, x*y), (y, x, 2*x + y)]

        Notice that changing the returned list does not change a (the list
        is a copy)::

            sage: v[0] = 25
            sage: a
            [      x       y     x*y]
            [      y       x 2*x + y]"""
    @overload
    def list(self, a) -> Any:
        """Matrix.list(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 121)

        List of the elements of ``self`` ordered by elements in each
        row. It is safe to change the returned list.

        .. warning::

           This function returns a list of the entries in the matrix
           ``self``.  It does not return a list of the rows of ``self``,
           so it is different than the output of ``list(self)``, which
           returns ``[self[0],self[1],...]``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: a = matrix(R,2,[x,y,x*y, y,x,2*x+y]); a
            [      x       y     x*y]
            [      y       x 2*x + y]
            sage: v = a.list(); v
            [x, y, x*y, y, x, 2*x + y]

        Note that list(a) is different than a.list()::

            sage: a.list()
            [x, y, x*y, y, x, 2*x + y]
            sage: list(a)
            [(x, y, x*y), (y, x, 2*x + y)]

        Notice that changing the returned list does not change a (the list
        is a copy)::

            sage: v[0] = 25
            sage: a
            [      x       y     x*y]
            [      y       x 2*x + y]"""
    @overload
    def list(self) -> Any:
        """Matrix.list(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 121)

        List of the elements of ``self`` ordered by elements in each
        row. It is safe to change the returned list.

        .. warning::

           This function returns a list of the entries in the matrix
           ``self``.  It does not return a list of the rows of ``self``,
           so it is different than the output of ``list(self)``, which
           returns ``[self[0],self[1],...]``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: a = matrix(R,2,[x,y,x*y, y,x,2*x+y]); a
            [      x       y     x*y]
            [      y       x 2*x + y]
            sage: v = a.list(); v
            [x, y, x*y, y, x, 2*x + y]

        Note that list(a) is different than a.list()::

            sage: a.list()
            [x, y, x*y, y, x, 2*x + y]
            sage: list(a)
            [(x, y, x*y), (y, x, 2*x + y)]

        Notice that changing the returned list does not change a (the list
        is a copy)::

            sage: v[0] = 25
            sage: a
            [      x       y     x*y]
            [      y       x 2*x + y]"""
    @overload
    def list(self, a) -> Any:
        """Matrix.list(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 121)

        List of the elements of ``self`` ordered by elements in each
        row. It is safe to change the returned list.

        .. warning::

           This function returns a list of the entries in the matrix
           ``self``.  It does not return a list of the rows of ``self``,
           so it is different than the output of ``list(self)``, which
           returns ``[self[0],self[1],...]``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: a = matrix(R,2,[x,y,x*y, y,x,2*x+y]); a
            [      x       y     x*y]
            [      y       x 2*x + y]
            sage: v = a.list(); v
            [x, y, x*y, y, x, 2*x + y]

        Note that list(a) is different than a.list()::

            sage: a.list()
            [x, y, x*y, y, x, 2*x + y]
            sage: list(a)
            [(x, y, x*y), (y, x, 2*x + y)]

        Notice that changing the returned list does not change a (the list
        is a copy)::

            sage: v[0] = 25
            sage: a
            [      x       y     x*y]
            [      y       x 2*x + y]"""
    def mod(self, p) -> Any:
        """Matrix.mod(self, p)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5427)

        Return matrix mod `p`, over the reduced ring.

        EXAMPLES::

            sage: M = matrix(ZZ, 2, 2, [5, 9, 13, 15])
            sage: M.mod(7)
            [5 2]
            [6 1]
            sage: parent(M.mod(7))
            Full MatrixSpace of 2 by 2 dense matrices over Ring of integers modulo 7"""
    def monomial_coefficients(self, *args, **kwargs):
        """Matrix.dict(self, copy=True)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 234)

        Dictionary of the elements of ``self`` with keys pairs ``(i,j)``
        and values the nonzero entries of ``self``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); make a copy of the ``dict``
          corresponding to ``self``

        If ``copy=True``, then is safe to change the returned dictionary.
        Otherwise, this can cause undesired behavior by mutating the ``dict``.

        EXAMPLES::

            sage: R.<x,y> = QQ[]
            sage: a = matrix(R,2,[x,y,0, 0,0,2*x+y]); a
            [      x       y       0]
            [      0       0 2*x + y]
            sage: d = a.dict(); d
            {(0, 0): x, (0, 1): y, (1, 2): 2*x + y}

        Notice that changing the returned list does not change a (the list
        is a copy)::

            sage: d[0,0] = 25
            sage: a
            [      x       y       0]
            [      0       0 2*x + y]"""
    def multiplicative_order(self) -> Any:
        """Matrix.multiplicative_order(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5036)

        Return the multiplicative order of this matrix, which must
        therefore be invertible.

        Only implemented over finite fields and over `\\ZZ`.

        EXAMPLES:

        Over finite fields::

            sage: A = matrix(GF(59), 3, [10,56,39,53,56,33,58,24,55])
            sage: A.multiplicative_order()                                              # needs sage.libs.pari
            580
            sage: (A^580).is_one()
            True

            sage: B = matrix(GF(10007^3, 'b'), 0)                                       # needs sage.rings.finite_rings
            sage: B.multiplicative_order()                                              # needs sage.rings.finite_rings
            1

            sage: # needs sage.rings.finite_rings
            sage: M = MatrixSpace(GF(11^2, 'e'), 5)
            sage: E = M.random_element()
            sage: while E.det() == 0:
            ....:     E = M.random_element()
            sage: (E^E.multiplicative_order()).is_one()
            True

        Over `\\ZZ`::

            sage: m = matrix(ZZ, 2, 2, [-1,1,-1,0])
            sage: m.multiplicative_order()                                              # needs sage.libs.pari
            3

            sage: m = posets.ChainPoset(6).coxeter_transformation()                     # needs sage.combinat sage.graphs
            sage: m.multiplicative_order()                                              # needs sage.combinat sage.graphs sage.groups
            7

            sage: P = posets.TamariLattice(4).coxeter_transformation()                  # needs sage.combinat sage.graphs
            sage: P.multiplicative_order()                                              # needs sage.combinat sage.graphs sage.groups
            10

            sage: M = matrix(ZZ, 2, 2, [1, 1, 0, 1])
            sage: M.multiplicative_order()                                              # needs sage.libs.pari
            +Infinity

            sage: for k in range(600):                                                  # needs sage.groups sage.modular
            ....:     m = SL2Z.random_element()
            ....:     o = m.multiplicative_order()
            ....:     if o != Infinity and m**o != SL2Z.one():
            ....:         raise RuntimeError

            sage: m24 = matrix.companion(cyclotomic_polynomial(24))
            sage: def val(i, j):
            ....:     if i < j:
            ....:         return 0
            ....:     elif i == j:
            ....:         return 1
            ....:     else:
            ....:         return ZZ.random_element(-100,100)
            sage: rnd = matrix(ZZ, 8, 8, val)
            sage: (rnd * m24 * rnd.inverse_of_unit()).multiplicative_order()            # needs sage.libs.pari
            24

        TESTS::

            sage: C = matrix(GF(2^10, 'c'), 2, 3, [1]*6)                                # needs sage.rings.finite_rings
            sage: C.multiplicative_order()                                              # needs sage.rings.finite_rings
            Traceback (most recent call last):
            ...
            ArithmeticError: self must be invertible ...

            sage: D = matrix(IntegerModRing(6), 3, [5,5,3,0,2,5,5,4,0])
            sage: D.multiplicative_order()
            Traceback (most recent call last):
            ...
            NotImplementedError: ... only ... over finite fields or ZZ

        REFERENCES:

        - [CLG1997]_

        - [KP2002b]_"""
    def mutate(self, Py_ssize_tk) -> Any:
        """Matrix.mutate(self, Py_ssize_t k)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3713)

        Mutates ``self`` at row and column index ``k``.

        .. warning:: Only makes sense if ``self`` is skew-symmetrizable.

        INPUT:

        - ``k`` -- integer at which row/column ``self`` is mutated

        EXAMPLES:

        Mutation of the B-matrix of the quiver of type `A_3`::

            sage: M = matrix(ZZ, 3, [0,1,0,-1,0,-1,0,1,0]); M
            [ 0  1  0]
            [-1  0 -1]
            [ 0  1  0]

            sage: M.mutate(0); M
            [ 0 -1  0]
            [ 1  0 -1]
            [ 0  1  0]

            sage: M.mutate(1); M
            [ 0  1 -1]
            [-1  0  1]
            [ 1 -1  0]

            sage: M = matrix(ZZ, 6, [0,1,0,-1,0,-1,0,1,0,1,0,0,0,1,0,0,0,1]); M
            [ 0  1  0]
            [-1  0 -1]
            [ 0  1  0]
            [ 1  0  0]
            [ 0  1  0]
            [ 0  0  1]

            sage: M.mutate(0); M
            [ 0 -1  0]
            [ 1  0 -1]
            [ 0  1  0]
            [-1  1  0]
            [ 0  1  0]
            [ 0  0  1]

        REFERENCES:

        - [FZ2001]_"""
    @overload
    def ncols(self) -> Any:
        """Matrix.ncols(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2389)

        Return the number of columns of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, 3)
            sage: A = M([1,2,3, 4,5,6])
            sage: A
            [1 2 3]
            [4 5 6]
            sage: A.ncols()
            3
            sage: A.nrows()
            2

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples"""
    @overload
    def ncols(self) -> Any:
        """Matrix.ncols(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2389)

        Return the number of columns of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(QQ, 2, 3)
            sage: A = M([1,2,3, 4,5,6])
            sage: A
            [1 2 3]
            [4 5 6]
            sage: A.ncols()
            3
            sage: A.nrows()
            2

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples"""
    @overload
    def nonpivots(self) -> Any:
        """Matrix.nonpivots(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4827)

        Return the list of `i` such that the `i`-th column of ``self`` is NOT a
        pivot column of the reduced row echelon form of ``self``.

        OUTPUT: sorted tuple of (Python) integers

        EXAMPLES::

            sage: a = matrix(QQ, 3, 3, range(9)); a
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: a.echelon_form()
            [ 1  0 -1]
            [ 0  1  2]
            [ 0  0  0]
            sage: a.nonpivots()
            (2,)"""
    @overload
    def nonpivots(self) -> Any:
        """Matrix.nonpivots(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4827)

        Return the list of `i` such that the `i`-th column of ``self`` is NOT a
        pivot column of the reduced row echelon form of ``self``.

        OUTPUT: sorted tuple of (Python) integers

        EXAMPLES::

            sage: a = matrix(QQ, 3, 3, range(9)); a
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: a.echelon_form()
            [ 1  0 -1]
            [ 0  1  2]
            [ 0  0  0]
            sage: a.nonpivots()
            (2,)"""
    @overload
    def nonzero_positions(self, copy=..., column_order=...) -> Any:
        """Matrix.nonzero_positions(self, copy=True, column_order=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4860)

        Return the sorted list of pairs ``(i,j)`` such that ``self[i,j] != 0``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); it is safe to change the
          resulting list (unless you give the option ``copy=False``)

        - ``column_order`` -- boolean (default: ``False``); if ``True``,
          returns the list of pairs ``(i,j)`` such that ``self[i,j] != 0``, but
          sorted by columns, i.e., column ``j=0`` entries occur first, then
          column ``j=1`` entries, etc.

        EXAMPLES::

            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0]); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]
            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0], sparse=True); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]"""
    @overload
    def nonzero_positions(self) -> Any:
        """Matrix.nonzero_positions(self, copy=True, column_order=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4860)

        Return the sorted list of pairs ``(i,j)`` such that ``self[i,j] != 0``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); it is safe to change the
          resulting list (unless you give the option ``copy=False``)

        - ``column_order`` -- boolean (default: ``False``); if ``True``,
          returns the list of pairs ``(i,j)`` such that ``self[i,j] != 0``, but
          sorted by columns, i.e., column ``j=0`` entries occur first, then
          column ``j=1`` entries, etc.

        EXAMPLES::

            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0]); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]
            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0], sparse=True); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]"""
    @overload
    def nonzero_positions(self, copy=...) -> Any:
        """Matrix.nonzero_positions(self, copy=True, column_order=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4860)

        Return the sorted list of pairs ``(i,j)`` such that ``self[i,j] != 0``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); it is safe to change the
          resulting list (unless you give the option ``copy=False``)

        - ``column_order`` -- boolean (default: ``False``); if ``True``,
          returns the list of pairs ``(i,j)`` such that ``self[i,j] != 0``, but
          sorted by columns, i.e., column ``j=0`` entries occur first, then
          column ``j=1`` entries, etc.

        EXAMPLES::

            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0]); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]
            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0], sparse=True); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]"""
    @overload
    def nonzero_positions(self, column_order=...) -> Any:
        """Matrix.nonzero_positions(self, copy=True, column_order=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4860)

        Return the sorted list of pairs ``(i,j)`` such that ``self[i,j] != 0``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); it is safe to change the
          resulting list (unless you give the option ``copy=False``)

        - ``column_order`` -- boolean (default: ``False``); if ``True``,
          returns the list of pairs ``(i,j)`` such that ``self[i,j] != 0``, but
          sorted by columns, i.e., column ``j=0`` entries occur first, then
          column ``j=1`` entries, etc.

        EXAMPLES::

            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0]); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]
            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0], sparse=True); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]"""
    @overload
    def nonzero_positions(self) -> Any:
        """Matrix.nonzero_positions(self, copy=True, column_order=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4860)

        Return the sorted list of pairs ``(i,j)`` such that ``self[i,j] != 0``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); it is safe to change the
          resulting list (unless you give the option ``copy=False``)

        - ``column_order`` -- boolean (default: ``False``); if ``True``,
          returns the list of pairs ``(i,j)`` such that ``self[i,j] != 0``, but
          sorted by columns, i.e., column ``j=0`` entries occur first, then
          column ``j=1`` entries, etc.

        EXAMPLES::

            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0]); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]
            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0], sparse=True); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]"""
    @overload
    def nonzero_positions(self, copy=...) -> Any:
        """Matrix.nonzero_positions(self, copy=True, column_order=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4860)

        Return the sorted list of pairs ``(i,j)`` such that ``self[i,j] != 0``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); it is safe to change the
          resulting list (unless you give the option ``copy=False``)

        - ``column_order`` -- boolean (default: ``False``); if ``True``,
          returns the list of pairs ``(i,j)`` such that ``self[i,j] != 0``, but
          sorted by columns, i.e., column ``j=0`` entries occur first, then
          column ``j=1`` entries, etc.

        EXAMPLES::

            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0]); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]
            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0], sparse=True); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]"""
    @overload
    def nonzero_positions(self, column_order=...) -> Any:
        """Matrix.nonzero_positions(self, copy=True, column_order=False)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4860)

        Return the sorted list of pairs ``(i,j)`` such that ``self[i,j] != 0``.

        INPUT:

        - ``copy`` -- boolean (default: ``True``); it is safe to change the
          resulting list (unless you give the option ``copy=False``)

        - ``column_order`` -- boolean (default: ``False``); if ``True``,
          returns the list of pairs ``(i,j)`` such that ``self[i,j] != 0``, but
          sorted by columns, i.e., column ``j=0`` entries occur first, then
          column ``j=1`` entries, etc.

        EXAMPLES::

            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0]); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]
            sage: a = matrix(QQ, 2,3, [1,2,0,2,0,0], sparse=True); a
            [1 2 0]
            [2 0 0]
            sage: a.nonzero_positions()
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(copy=False)
            [(0, 0), (0, 1), (1, 0)]
            sage: a.nonzero_positions(column_order=True)
            [(0, 0), (1, 0), (0, 1)]"""
    def nonzero_positions_in_column(self, Py_ssize_ti) -> Any:
        """Matrix.nonzero_positions_in_column(self, Py_ssize_t i)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4960)

        Return a sorted list of the integers ``j`` such that ``self[j,i]`` is
        nonzero, i.e., such that the ``j``-th position of the ``i``-th column
        is nonzero.

        INPUT:

        - ``i`` -- integer

        OUTPUT: list

        EXAMPLES::

            sage: a = matrix(QQ, 3,2, [1,2,0,2,0,0]); a
            [1 2]
            [0 2]
            [0 0]
            sage: a.nonzero_positions_in_column(0)
            [0]
            sage: a.nonzero_positions_in_column(1)
            [0, 1]

        You will get an :exc:`IndexError` if you select an invalid column::

            sage: a.nonzero_positions_in_column(2)
            Traceback (most recent call last):
            ...
            IndexError: matrix column index out of range"""
    def nonzero_positions_in_row(self, Py_ssize_ti) -> Any:
        """Matrix.nonzero_positions_in_row(self, Py_ssize_t i)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5000)

        Return the integers ``j`` such that ``self[i,j]`` is nonzero, i.e.,
        such that the ``j``-th position of the ``i``-th row is nonzero.

        INPUT:

        - ``i`` -- integer

        OUTPUT: list

        EXAMPLES::

            sage: a = matrix(QQ, 3,2, [1,2,0,2,0,0]); a
            [1 2]
            [0 2]
            [0 0]
            sage: a.nonzero_positions_in_row(0)
            [0, 1]
            sage: a.nonzero_positions_in_row(1)
            [1]
            sage: a.nonzero_positions_in_row(2)
            []"""
    @overload
    def nrows(self) -> Any:
        """Matrix.nrows(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2411)

        Return the number of rows of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(QQ,6,7)
            sage: A = M([1,2,3,4,5,6,7, 22,3/4,34,11,7,5,3, 99,65,1/2,2/3,3/5,4/5,5/6, 9,8/9, 9/8,7/6,6/7,76,4, 0,9,8,7,6,5,4, 123,99,91,28,6,1024,1])
            sage: A
            [   1    2    3    4    5    6    7]
            [  22  3/4   34   11    7    5    3]
            [  99   65  1/2  2/3  3/5  4/5  5/6]
            [   9  8/9  9/8  7/6  6/7   76    4]
            [   0    9    8    7    6    5    4]
            [ 123   99   91   28    6 1024    1]
            sage: A.ncols()
            7
            sage: A.nrows()
            6

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples"""
    @overload
    def nrows(self) -> Any:
        """Matrix.nrows(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2411)

        Return the number of rows of this matrix.

        EXAMPLES::

            sage: M = MatrixSpace(QQ,6,7)
            sage: A = M([1,2,3,4,5,6,7, 22,3/4,34,11,7,5,3, 99,65,1/2,2/3,3/5,4/5,5/6, 9,8/9, 9/8,7/6,6/7,76,4, 0,9,8,7,6,5,4, 123,99,91,28,6,1024,1])
            sage: A
            [   1    2    3    4    5    6    7]
            [  22  3/4   34   11    7    5    3]
            [  99   65  1/2  2/3  3/5  4/5  5/6]
            [   9  8/9  9/8  7/6  6/7   76    4]
            [   0    9    8    7    6    5    4]
            [ 123   99   91   28    6 1024    1]
            sage: A.ncols()
            7
            sage: A.nrows()
            6

        AUTHORS:

        - Naqi Jaffery (2006-01-24): examples"""
    def permute_columns(self, permutation) -> Any:
        """Matrix.permute_columns(self, permutation)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2675)

        Permute the columns of ``self`` by applying the permutation
        group element ``permutation``.

        As permutation group elements act on integers `\\{1,\\dots,n\\}`,
        columns are considered numbered from 1 for this operation.

        INPUT:

        - ``permutation`` -- a ``PermutationGroupElement``

        EXAMPLES: We create a matrix::

            sage: M = matrix(ZZ, [[1,0,0,0,0],[0,2,0,0,0],[0,0,3,0,0],[0,0,0,4,0],[0,0,0,0,5]])
            sage: M
            [1 0 0 0 0]
            [0 2 0 0 0]
            [0 0 3 0 0]
            [0 0 0 4 0]
            [0 0 0 0 5]

        Next of all, create a permutation group element and act
        on ``M`` with it::

            sage: # needs sage.groups
            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: sigma, tau = G.gens()
            sage: sigma
            (1,2,3)(4,5)
            sage: M.permute_columns(sigma)
            sage: M
            [0 0 1 0 0]
            [2 0 0 0 0]
            [0 3 0 0 0]
            [0 0 0 0 4]
            [0 0 0 5 0]"""
    def permute_rows(self, permutation) -> Any:
        """Matrix.permute_rows(self, permutation)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2857)

        Permute the rows of ``self`` by applying the permutation
        group element ``permutation``.

        As permutation group elements act on integers `\\{1,\\dots,n\\}`,
        rows are considered numbered from 1 for this operation.

        INPUT:

        - ``permutation`` -- a ``PermutationGroupElement``

        EXAMPLES: We create a matrix::

            sage: M = matrix(ZZ, [[1,0,0,0,0],[0,2,0,0,0],[0,0,3,0,0],[0,0,0,4,0],[0,0,0,0,5]])
            sage: M
            [1 0 0 0 0]
            [0 2 0 0 0]
            [0 0 3 0 0]
            [0 0 0 4 0]
            [0 0 0 0 5]

        Next of all, create a permutation group element and act on ``M``::

            sage: # needs sage.groups
            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: sigma, tau = G.gens()
            sage: sigma
            (1,2,3)(4,5)
            sage: M.permute_rows(sigma)
            sage: M
            [0 2 0 0 0]
            [0 0 3 0 0]
            [1 0 0 0 0]
            [0 0 0 0 5]
            [0 0 0 4 0]"""
    def permute_rows_and_columns(self, row_permutation, column_permutation) -> Any:
        """Matrix.permute_rows_and_columns(self, row_permutation, column_permutation)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2958)

        Permute the rows and columns of ``self`` by applying the permutation
        group elements ``row_permutation`` and ``column_permutation``
        respectively.

        As permutation group elements act on integers `\\{1,\\dots,n\\}`,
        rows and columns are considered numbered from 1 for this operation.

        INPUT:

        - ``row_permutation`` -- a ``PermutationGroupElement``
        - ``column_permutation`` -- a ``PermutationGroupElement``

        OUTPUT: a matrix

        EXAMPLES: We create a matrix::

            sage: M = matrix(ZZ, [[1,0,0,0,0],[0,2,0,0,0],[0,0,3,0,0],[0,0,0,4,0],[0,0,0,0,5]])
            sage: M
            [1 0 0 0 0]
            [0 2 0 0 0]
            [0 0 3 0 0]
            [0 0 0 4 0]
            [0 0 0 0 5]

        Next of all, create a permutation group element and act on ``M``::

            sage: # needs sage.groups
            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: sigma, tau = G.gens()
            sage: sigma
            (1,2,3)(4,5)
            sage: M.permute_rows_and_columns(sigma,tau)
            sage: M
            [2 0 0 0 0]
            [0 3 0 0 0]
            [0 0 0 0 1]
            [0 0 0 5 0]
            [0 0 4 0 0]"""
    @overload
    def pivots(self) -> Any:
        """Matrix.pivots(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4762)

        Return the pivot column positions of this matrix.

        OUTPUT: a tuple of Python integers: the position of the
        first nonzero entry in each row of the echelon form.

        This returns a tuple so it is immutable; see :issue:`10752`.

        EXAMPLES::

            sage: A = matrix(QQ, 2, 2, range(4))
            sage: A.pivots()
            (0, 1)"""
    @overload
    def pivots(self) -> Any:
        """Matrix.pivots(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4762)

        Return the pivot column positions of this matrix.

        OUTPUT: a tuple of Python integers: the position of the
        first nonzero entry in each row of the echelon form.

        This returns a tuple so it is immutable; see :issue:`10752`.

        EXAMPLES::

            sage: A = matrix(QQ, 2, 2, range(4))
            sage: A.pivots()
            (0, 1)"""
    @overload
    def rank(self) -> Any:
        """Matrix.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4789)

        Return the rank of this matrix.

        EXAMPLES::

            sage: m = matrix(GF(7), 5, range(25))
            sage: m.rank()
            2

        Rank is not implemented over the integers modulo a composite yet.::

            sage: m = matrix(Integers(4), 2, [2,2,2,2])
            sage: m.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        TESTS:

        We should be able to compute the rank of a matrix whose
        entries are polynomials over a finite field (:issue:`5014`)::

            sage: P.<x> = PolynomialRing(GF(17))
            sage: m = matrix(P, [[ 6*x^2 + 8*x + 12, 10*x^2 + 4*x + 11],
            ....:                [8*x^2 + 12*x + 15,  8*x^2 + 9*x + 16]])
            sage: m.rank()
            2"""
    @overload
    def rank(self) -> Any:
        """Matrix.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4789)

        Return the rank of this matrix.

        EXAMPLES::

            sage: m = matrix(GF(7), 5, range(25))
            sage: m.rank()
            2

        Rank is not implemented over the integers modulo a composite yet.::

            sage: m = matrix(Integers(4), 2, [2,2,2,2])
            sage: m.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        TESTS:

        We should be able to compute the rank of a matrix whose
        entries are polynomials over a finite field (:issue:`5014`)::

            sage: P.<x> = PolynomialRing(GF(17))
            sage: m = matrix(P, [[ 6*x^2 + 8*x + 12, 10*x^2 + 4*x + 11],
            ....:                [8*x^2 + 12*x + 15,  8*x^2 + 9*x + 16]])
            sage: m.rank()
            2"""
    @overload
    def rank(self) -> Any:
        """Matrix.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4789)

        Return the rank of this matrix.

        EXAMPLES::

            sage: m = matrix(GF(7), 5, range(25))
            sage: m.rank()
            2

        Rank is not implemented over the integers modulo a composite yet.::

            sage: m = matrix(Integers(4), 2, [2,2,2,2])
            sage: m.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        TESTS:

        We should be able to compute the rank of a matrix whose
        entries are polynomials over a finite field (:issue:`5014`)::

            sage: P.<x> = PolynomialRing(GF(17))
            sage: m = matrix(P, [[ 6*x^2 + 8*x + 12, 10*x^2 + 4*x + 11],
            ....:                [8*x^2 + 12*x + 15,  8*x^2 + 9*x + 16]])
            sage: m.rank()
            2"""
    @overload
    def rank(self) -> Any:
        """Matrix.rank(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 4789)

        Return the rank of this matrix.

        EXAMPLES::

            sage: m = matrix(GF(7), 5, range(25))
            sage: m.rank()
            2

        Rank is not implemented over the integers modulo a composite yet.::

            sage: m = matrix(Integers(4), 2, [2,2,2,2])
            sage: m.rank()
            Traceback (most recent call last):
            ...
            NotImplementedError: Echelon form not implemented over 'Ring of integers modulo 4'.

        TESTS:

        We should be able to compute the rank of a matrix whose
        entries are polynomials over a finite field (:issue:`5014`)::

            sage: P.<x> = PolynomialRing(GF(17))
            sage: m = matrix(P, [[ 6*x^2 + 8*x + 12, 10*x^2 + 4*x + 11],
            ....:                [8*x^2 + 12*x + 15,  8*x^2 + 9*x + 16]])
            sage: m.rank()
            2"""
    def rescale_col(self, Py_ssize_ti, s, Py_ssize_tstart_row=...) -> Any:
        """Matrix.rescale_col(self, Py_ssize_t i, s, Py_ssize_t start_row=0)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3331)

        Replace `i`-th col of ``self`` by `s` times `i`-th col of ``self``.

        INPUT:

        - ``i`` -- `i`-th column

        - ``s`` -- scalar

        - ``start_row`` -- only rescale entries at this row
          and lower

        EXAMPLES: We rescale the last column of a matrix over the rational
        numbers::

            sage: a = matrix(QQ, 2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.rescale_col(2, 1/2); a
            [  0   1   1]
            [  3   4 5/2]
            sage: R.<x> = QQ[]

        We rescale the last column of a matrix over a polynomial ring::

            sage: a = matrix(R, 2, 3, [1,x,x^2,x^3,x^4,x^5]); a
            [  1   x x^2]
            [x^3 x^4 x^5]
            sage: a.rescale_col(2, 1/2); a
            [      1       x 1/2*x^2]
            [    x^3     x^4 1/2*x^5]

        We try and fail to rescale a matrix over the integers by a
        non-integer::

            sage: a = matrix(ZZ, 2, 3, [0,1,2, 3,4,4]); a
            [0 1 2]
            [3 4 4]
            sage: a.rescale_col(2, 1/2)
            Traceback (most recent call last):
            ...
            TypeError: Rescaling column by Rational Field element cannot be done
            over Integer Ring, use change_ring or with_rescaled_col instead.

        To rescale the matrix by 1/2, you must change the base ring to the
        rationals::

            sage: a = a.change_ring(QQ); a
            [0 1 2]
            [3 4 4]
            sage: a.rescale_col(2,1/2); a
            [0 1 1]
            [3 4 2]"""
    def rescale_row(self, Py_ssize_ti, s, Py_ssize_tstart_col=...) -> Any:
        """Matrix.rescale_row(self, Py_ssize_t i, s, Py_ssize_t start_col=0)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3214)

        Replace `i`-th row of ``self`` by `s` times `i`-th row of ``self``.

        INPUT:

        - ``i`` -- `i`-th row

        - ``s`` -- scalar

        - ``start_col`` -- only rescale entries at this column
          and to the right

        EXAMPLES: We rescale the second row of a matrix over the rational
        numbers::

            sage: a = matrix(QQ, 3, range(6)); a
            [0 1]
            [2 3]
            [4 5]
            sage: a.rescale_row(1, 1/2); a
            [ 0   1]
            [ 1 3/2]
            [ 4   5]

        We rescale the second row of a matrix over a polynomial ring::

            sage: R.<x> = QQ[]
            sage: a = matrix(R, 3, [1,x,x^2,x^3,x^4,x^5]); a
            [  1   x]
            [x^2 x^3]
            [x^4 x^5]
            sage: a.rescale_row(1, 1/2); a
            [      1       x]
            [1/2*x^2 1/2*x^3]
            [    x^4     x^5]

        We try and fail to rescale a matrix over the integers by a
        non-integer::

            sage: a = matrix(ZZ, 2, 3, [0,1,2, 3,4,4]); a
            [0 1 2]
            [3 4 4]
            sage: a.rescale_row(1, 1/2)
            Traceback (most recent call last):
            ...
            TypeError: Rescaling row by Rational Field element cannot be done
            over Integer Ring, use change_ring or with_rescaled_row instead.

        To rescale the matrix by 1/2, you must change the base ring to the
        rationals::

            sage: a = a.change_ring(QQ); a
            [0 1 2]
            [3 4 4]
            sage: a.rescale_col(1, 1/2); a
            [  0 1/2   2]
            [  3   2   4]"""
    def reverse_rows_and_columns(self) -> Any:
        """Matrix.reverse_rows_and_columns(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3640)

        Reverse the row order and column order of this matrix.

        This method transforms a matrix `m_{i,j}` with `0 \\leq i < nrows` and
        `0 \\leq j < ncols` into `m_{nrows - i - 1, ncols - j - 1}`.

        EXAMPLES::

            sage: m = matrix(ZZ, 2, 2, range(4))
            sage: m.reverse_rows_and_columns()
            sage: m
            [3 2]
            [1 0]

            sage: m = matrix(ZZ, 2, 3, range(6), sparse=True)
            sage: m.reverse_rows_and_columns()
            sage: m
            [5 4 3]
            [2 1 0]
            sage: m = matrix(ZZ, 3, 2, range(6), sparse=True)
            sage: m.reverse_rows_and_columns()
            sage: m
            [5 4]
            [3 2]
            [1 0]
            sage: m.reverse_rows_and_columns()
            sage: m
            [0 1]
            [2 3]
            [4 5]

            sage: m = matrix(QQ, 3, 2, [1/i for i in range(1,7)])
            sage: m.reverse_rows_and_columns()
            sage: m
            [1/6 1/5]
            [1/4 1/3]
            [1/2   1]

            sage: R.<x,y> = ZZ['x,y']
            sage: m = matrix(R, 3, 3, lambda i,j: x**i*y**j, sparse=True)
            sage: m.reverse_rows_and_columns()
            sage: m
            [x^2*y^2   x^2*y     x^2]
            [  x*y^2     x*y       x]
            [    y^2       y       1]

        If the matrix is immutable, the method raises an error::

            sage: m = matrix(ZZ, 2, [1, 3, -2, 4])
            sage: m.set_immutable()
            sage: m.reverse_rows_and_columns()
            Traceback (most recent call last):
            ...
            ValueError: matrix is immutable; please change a copy
            instead (i.e., use copy(M) to change a copy of M)."""
    def set_col_to_multiple_of_col(self, Py_ssize_ti, Py_ssize_tj, s) -> Any:
        """Matrix.set_col_to_multiple_of_col(self, Py_ssize_t i, Py_ssize_t j, s)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3517)

        Set column i equal to s times column j.

        EXAMPLES: We change the second column to -3 times the first
        column.

        ::

            sage: a = matrix(ZZ, 2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.set_col_to_multiple_of_col(1, 0, -3)
            sage: a
            [ 0  0  2]
            [ 3 -9  5]

        If we try to multiply a column by a rational number, we get an
        error message::

            sage: a.set_col_to_multiple_of_col(1, 0, 1/2)
            Traceback (most recent call last):
            ...
            TypeError: Multiplying column by Rational Field element cannot be done over Integer Ring, use change_ring or with_col_set_to_multiple_of_col instead."""
    def set_immutable(self) -> Any:
        """Matrix.set_immutable(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 445)

        Call this function to set the matrix as immutable.

        Matrices are always mutable by default, i.e., you can change their
        entries using ``A[i,j] = x``. However, mutable matrices
        aren't hashable, so can't be used as keys in dictionaries, etc.
        Also, often when implementing a class, you might compute a matrix
        associated to it, e.g., the matrix of a Hecke operator. If you
        return this matrix to the user you're really returning a reference
        and the user could then change an entry; this could be confusing.
        Thus you should set such a matrix immutable.

        EXAMPLES::

            sage: A = Matrix(QQ, 2, 2, range(4))
            sage: A.is_mutable()
            True
            sage: A[0,0] = 10
            sage: A
            [10   1]
            [ 2   3]

        Mutable matrices are not hashable, so can't be used as keys for
        dictionaries::

            sage: hash(A)
            Traceback (most recent call last):
            ...
            TypeError: mutable matrices are unhashable
            sage: v = {A:1}
            Traceback (most recent call last):
            ...
            TypeError: mutable matrices are unhashable

        If we make A immutable it suddenly is hashable.

        ::

            sage: A.set_immutable()
            sage: A.is_mutable()
            False
            sage: A[0,0] = 10
            Traceback (most recent call last):
            ...
            ValueError: matrix is immutable; please change a copy instead
            (i.e., use copy(M) to change a copy of M).
            sage: hash(A) #random
            12
            sage: v = {A:1}; v
            {[10  1]
             [ 2  3]: 1}"""
    def set_row_to_multiple_of_row(self, Py_ssize_ti, Py_ssize_tj, s) -> Any:
        """Matrix.set_row_to_multiple_of_row(self, Py_ssize_t i, Py_ssize_t j, s)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3441)

        Set row i equal to s times row j.

        EXAMPLES: We change the second row to -3 times the first row::

            sage: a = matrix(ZZ, 2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: a.set_row_to_multiple_of_row(1, 0, -3)
            sage: a
            [ 0  1  2]
            [ 0 -3 -6]

        If we try to multiply a row by a rational number, we get an error
        message::

            sage: a.set_row_to_multiple_of_row(1, 0, 1/2)
            Traceback (most recent call last):
            ...
            TypeError: Multiplying row by Rational Field element cannot be done over
            Integer Ring, use change_ring or with_row_set_to_multiple_of_row instead."""
    def str(self, *args, **kwargs):
        '''Matrix.str(self, rep_mapping=None, zero=None, plus_one=None, minus_one=None, *, unicode=False, shape=None, character_art=False, left_border=None, right_border=None, top_border=None, bottom_border=None)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 1834)

        Return a nice string representation of the matrix.

        INPUT:

        - ``rep_mapping`` -- dictionary or callable used to override
          the usual representation of elements

          If ``rep_mapping`` is a dictionary then keys should be
          elements of the base ring and values the desired string
          representation.  Values sent in via the other keyword
          arguments will override values in the dictionary.
          Use of a dictionary can potentially take a very long time
          due to the need to hash entries of the matrix.  Matrices
          with entries from ``QQbar`` are one example.

          If ``rep_mapping`` is callable then it will be called with
          elements of the matrix and must return a string.  Simply
          call :func:`repr` on elements which should have the default
          representation.

        - ``zero`` -- string (default: ``None``); if not ``None`` use
          the value of ``zero`` as the representation of the zero
          element.

        - ``plus_one`` -- string (default: ``None``); if not ``None``
          use the value of ``plus_one`` as the representation of the
          one element.

        - ``minus_one`` -- string (default: ``None``); if not ``None``
          use the value of ``minus_one`` as the representation of the
          negative of the one element.

        - ``unicode`` -- boolean (default: ``False``);
          whether to use Unicode symbols instead of ASCII symbols
          for brackets and subdivision lines

        - ``shape`` -- one of ``\'square\'`` or ``\'round\'`` (default: ``None``).
          Switches between round and square brackets.
          The default depends on the setting of the ``unicode`` keyword
          argument. For Unicode symbols, the default is round brackets
          in accordance with the TeX rendering,
          while the ASCII rendering defaults to square brackets.

        - ``character_art`` -- boolean (default: ``False``); if ``True``, the
          result will be of type :class:`~sage.typeset.ascii_art.AsciiArt` or
          :class:`~sage.typeset.unicode_art.UnicodeArt` which support line
          breaking of wide matrices that exceed the window width

        - ``left_border``, ``right_border`` -- sequence (default: ``None``);
          if not ``None``, call :func:`str` on the elements and use the
          results as labels for the rows of the matrix. The labels appear
          outside of the parentheses.

        - ``top_border``, ``bottom_border`` -- sequence (default: ``None``);
          if not ``None``, call :func:`str` on the elements and use the
          results as labels for the columns of the matrix. The labels appear
          outside of the parentheses.

        EXAMPLES::

            sage: R = PolynomialRing(QQ,6,\'z\')
            sage: a = matrix(2,3, R.gens())
            sage: a.__repr__()
            \'[z0 z1 z2]\\n[z3 z4 z5]\'

            sage: M = matrix([[1,0],[2,-1]])
            sage: M.str()
            \'[ 1  0]\\n[ 2 -1]\'
            sage: M.str(plus_one=\'+\',minus_one=\'-\',zero=\'.\')
            \'[+ .]\\n[2 -]\'
            sage: M.str({1:"not this one",2:"II"},minus_one=\'*\',plus_one=\'I\')
            \'[ I  0]\\n[II  *]\'

            sage: def print_entry(x):
            ....:   if x>0:
            ....:       return \'+\'
            ....:   elif x<0:
            ....:       return \'-\'
            ....:   else: return \'.\'
            ...
            sage: M.str(print_entry)
            \'[+ .]\\n[+ -]\'
            sage: M.str(repr)
            \'[ 1  0]\\n[ 2 -1]\'

            sage: M = matrix([[1,2,3],[4,5,6],[7,8,9]])
            sage: M.subdivide(None, 2)
            sage: print(M.str(unicode=True))
            ⎛1 2│3⎞
            ⎜4 5│6⎟
            ⎝7 8│9⎠
            sage: M.subdivide([0,1,1,3], [0,2,3,3])
            sage: print(M.str(unicode=True, shape=\'square\'))
            ⎡┼───┼─┼┼⎤
            ⎢│1 2│3││⎥
            ⎢┼───┼─┼┼⎥
            ⎢┼───┼─┼┼⎥
            ⎢│4 5│6││⎥
            ⎢│7 8│9││⎥
            ⎣┼───┼─┼┼⎦

        If ``character_art`` is set, the lines of large matrices are wrapped in
        a readable way::

            sage: set_random_seed(0)
            sage: matrix.random(RDF, 3, 5).str(unicode=True, character_art=True)
            ⎛ -0.27440062056807446    0.5031965950979831 -0.001975438590219314
            ⎜ -0.05461130074681608 -0.033673314214051286   -0.9401270875197381
            ⎝  0.19906256610645512    0.3242250183948632    0.6026443545751128
            <BLANKLINE>
               -0.9467802263760512    0.5056889961514748⎞
              -0.35104242112828943    0.5084492941557279⎟
               -0.9541798283979341   -0.8948790563276592⎠

        The number of floating point digits to display is controlled by
        :obj:`matrix.options.precision <.constructor.options>` and can also be
        set by the `IPython magic
        <https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-precision>`_
        ``%precision``. This does not affect the internal precision of the
        represented data, but only the textual display of matrices::

            sage: matrix.options.precision = 4
            sage: A = matrix(RR, [[1/3, 200/3], [-3, 1e6]]); A
            [  0.3333    66.67]
            [  -3.000 1.000E+6]
            sage: unicode_art(A)
            ⎛  0.3333    66.67⎞
            ⎝  -3.000 1.000E+6⎠
            sage: matrix.options.precision = None
            sage: A
            [ 0.333333333333333   66.6666666666667]
            [ -3.00000000000000 1.00000000000000e6]

        Matrices with borders::

            sage: M = matrix([[1,2,3], [4,5,6], [7,8,9]])
            sage: M.subdivide(None, 2)
            sage: print(M.str(unicode=True,
            ....:             top_border=[\'ab\', \'cde\', \'f\'],
            ....:             bottom_border=[\'*\', \'\', \'\'],
            ....:             left_border=[1, 10, 100],
            ....:             right_border=[\'\', \' <\', \'\']))
                 ab cde   f
              1⎛  1   2│  3⎞
             10⎜  4   5│  6⎟ <
            100⎝  7   8│  9⎠
                  *

        TESTS:

        Prior to :issue:`11544` this could take a full minute to run (2011). ::

            sage: # needs sage.rings.number_field
            sage: A = matrix(QQ, 4, 4, [1, 2, -2, 2, 1, 0, -1, -1, 0, -1, 1, 1, -1, 2, 1/2, 0])
            sage: e = A.eigenvalues()[3]
            sage: K = (A - e).kernel()
            sage: P = K.basis_matrix()
            sage: P.str()
            \'[              1.000000000000000? + 0.?e-17*I  -2.116651487479748? + 0.0255565807096352?*I -0.2585224251020429? + 0.2886023409047535?*I  -0.4847545623533090? - 1.871890760086142?*I]\'

        Use single-row delimiters where appropriate::

            sage: print(matrix([[1]]).str(unicode=True))
            (1)
            sage: print(matrix([[],[]]).str(unicode=True))
            ()
            sage: M = matrix([[1]])
            sage: M.subdivide([0,1], [])
            sage: print(M.str(unicode=True))
            ⎛─⎞
            ⎜1⎟
            ⎝─⎠

        Check that exact number types are not affected by the precision
        option::

            sage: matrix.options.precision = 4
            sage: matrix(ZZ, [[10^10]])
            [10000000000]
            sage: matrix(QQ, [[2/3, 10^6]])
            [    2/3 1000000]
            sage: R.<x,y> = QQ[[]]
            sage: matrix(R, [[2/3 - 10^6 * x^3 + 3 * y + O(x, y)^4]])
            [2/3 + 3*y - 1000000*x^3 + O(x, y)^4]
            sage: matrix.options._reset()

        Edge cases of matrices with borders::

            sage: print(matrix(ZZ, 0, 0).str(
            ....:     top_border=[], bottom_border=[], left_border=[], right_border=[]))
            []
            sage: print(matrix(ZZ, 0, 4).str(
            ....:     unicode=True,
            ....:     top_border=\'abcd\', bottom_border=range(4)))
            ()
            sage: print(matrix(ZZ, 1, 4).str(
            ....:     unicode=True,
            ....:     top_border=\'abcd\', bottom_border=range(4)))
             a b c d
            (0 0 0 0)
             0 1 2 3
            sage: print(matrix(ZZ, 2, 4).str(
            ....:     unicode=True,
            ....:     top_border=\'abcd\', bottom_border=range(4), left_border=\'uv\'))
              a b c d
            u⎛0 0 0 0⎞
            v⎝0 0 0 0⎠
              0 1 2 3
            sage: print(matrix(ZZ, 2, 0).str(
            ....:     top_border=\'\', left_border=\'uv\', right_border=[\'*\', \'\']))
              []'''
    def swap_columns(self, Py_ssize_tc1, Py_ssize_tc2) -> Any:
        """Matrix.swap_columns(self, Py_ssize_t c1, Py_ssize_t c2)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2596)

        Swap columns c1 and c2 of ``self``.

        EXAMPLES: We create a rational matrix::

            sage: M = MatrixSpace(QQ,3,3)
            sage: A = M([1,9,-7,4/5,4,3,6,4,3])
            sage: A
            [  1   9  -7]
            [4/5   4   3]
            [  6   4   3]

        Since the first column is numbered zero, this swaps the second and
        third columns::

            sage: A.swap_columns(1,2); A
            [  1  -7   9]
            [4/5   3   4]
            [  6   3   4]"""
    def swap_rows(self, r1, r2) -> Any:
        """Matrix.swap_rows(self, r1, r2)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2778)

        Swap rows r1 and r2 of ``self``.

        EXAMPLES: We create a rational matrix::

            sage: M = MatrixSpace(QQ, 3, 3)
            sage: A = M([1,9,-7, 4/5,4,3, 6,4,3])
            sage: A
            [  1   9  -7]
            [4/5   4   3]
            [  6   4   3]

        Since the first row is numbered zero, this swaps the first and
        third rows::

            sage: A.swap_rows(0, 2); A
            [  6   4   3]
            [4/5   4   3]
            [  1   9  -7]"""
    def with_added_multiple_of_column(self, Py_ssize_ti, Py_ssize_tj, s, Py_ssize_tstart_row=...) -> Any:
        """Matrix.with_added_multiple_of_column(self, Py_ssize_t i, Py_ssize_t j, s, Py_ssize_t start_row=0)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3172)

        Add s times column j to column i, returning new matrix.

        EXAMPLES: We add -1 times the third column to the second column of
        an integer matrix, remembering to start numbering cols at zero::

            sage: a = matrix(ZZ, 2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: b = a.with_added_multiple_of_column(1, 2, -1); b
            [ 0 -1  2]
            [ 3 -1  5]

        The original matrix is unchanged::

            sage: a
            [0 1 2]
            [3 4 5]

        Adding a rational multiple is okay, and reassigning a variable is
        okay::

            sage: a = a.with_added_multiple_of_column(0, 1, 1/3); a
            [ 1/3    1    2]
            [13/3    4    5]"""
    def with_added_multiple_of_row(self, Py_ssize_ti, Py_ssize_tj, s, Py_ssize_tstart_col=...) -> Any:
        """Matrix.with_added_multiple_of_row(self, Py_ssize_t i, Py_ssize_t j, s, Py_ssize_t start_col=0)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3087)

        Add s times row j to row i, returning new matrix.

        EXAMPLES: We add -3 times the first row to the second row of an
        integer matrix, remembering to start numbering rows at zero::

            sage: a = matrix(ZZ,2,3,range(6)); a
            [0 1 2]
            [3 4 5]
            sage: b = a.with_added_multiple_of_row(1,0,-3); b
            [ 0  1  2]
            [ 3  1 -1]

        The original matrix is unchanged::

            sage: a
            [0 1 2]
            [3 4 5]

        Adding a rational multiple is okay, and reassigning a variable is
        okay::

            sage: a = a.with_added_multiple_of_row(0,1,1/3); a
            [   1  7/3 11/3]
            [   3    4    5]"""
    def with_col_set_to_multiple_of_col(self, Py_ssize_ti, Py_ssize_tj, s) -> Any:
        """Matrix.with_col_set_to_multiple_of_col(self, Py_ssize_t i, Py_ssize_t j, s)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3553)

        Set column i equal to s times column j, returning a new matrix.

        EXAMPLES: We change the second column to -3 times the first
        column.

        ::

            sage: a = matrix(ZZ, 2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: b = a.with_col_set_to_multiple_of_col(1, 0, -3); b
            [ 0  0  2]
            [ 3 -9  5]

        Note that the original matrix is unchanged::

            sage: a
            [0 1 2]
            [3 4 5]

        Adding a rational multiple is okay, and reassigning a variable is
        okay::

            sage: a = a.with_col_set_to_multiple_of_col(1, 0, 1/2); a
            [  0   0   2]
            [  3 3/2   5]"""
    def with_permuted_columns(self, permutation) -> Any:
        """Matrix.with_permuted_columns(self, permutation)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2721)

        Return the matrix obtained from permuting the columns
        of ``self`` by applying the permutation group element
        ``permutation``.

        As permutation group elements act on integers `\\{1,\\dots,n\\}`,
        columns are considered numbered from 1 for this operation.

        INPUT:

        - ``permutation`` -- a ``PermutationGroupElement``

        OUTPUT: a matrix

        EXAMPLES: We create some matrix::

            sage: M = matrix(ZZ, [[1,0,0,0,0],[0,2,0,0,0],[0,0,3,0,0],[0,0,0,4,0],[0,0,0,0,5]])
            sage: M
            [1 0 0 0 0]
            [0 2 0 0 0]
            [0 0 3 0 0]
            [0 0 0 4 0]
            [0 0 0 0 5]

        Next of all, create a permutation group element and
        act on ``M``::

            sage: # needs sage.groups
            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: sigma, tau = G.gens()
            sage: sigma
            (1,2,3)(4,5)
            sage: M.with_permuted_columns(sigma)
            [0 0 1 0 0]
            [2 0 0 0 0]
            [0 3 0 0 0]
            [0 0 0 0 4]
            [0 0 0 5 0]"""
    def with_permuted_rows(self, permutation) -> Any:
        """Matrix.with_permuted_rows(self, permutation)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2902)

        Return the matrix obtained from permuting the rows
        of ``self`` by applying the permutation group element
        ``permutation``.

        As permutation group elements act on integers `\\{1,\\dots,n\\}`,
        rows are considered numbered from 1 for this operation.

        INPUT:

        - ``permutation`` -- a ``PermutationGroupElement``

        OUTPUT: a matrix

        EXAMPLES: We create a matrix::

            sage: M = matrix(ZZ, [[1,0,0,0,0],[0,2,0,0,0],[0,0,3,0,0],[0,0,0,4,0],[0,0,0,0,5]])
            sage: M
            [1 0 0 0 0]
            [0 2 0 0 0]
            [0 0 3 0 0]
            [0 0 0 4 0]
            [0 0 0 0 5]

        Next of all, create a permutation group element and act on ``M``::

            sage: # needs sage.groups
            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: sigma, tau = G.gens()
            sage: sigma
            (1,2,3)(4,5)
            sage: M.with_permuted_rows(sigma)
            [0 2 0 0 0]
            [0 0 3 0 0]
            [1 0 0 0 0]
            [0 0 0 0 5]
            [0 0 0 4 0]"""
    def with_permuted_rows_and_columns(self, row_permutation, column_permutation) -> Any:
        """Matrix.with_permuted_rows_and_columns(self, row_permutation, column_permutation)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3002)

        Return the matrix obtained from permuting the rows and
        columns of ``self`` by applying the permutation group
        elements ``row_permutation`` and ``column_permutation``.

        As permutation group elements act on integers `\\{1,\\dots,n\\}`,
        rows and columns are considered numbered from 1 for this operation.

        INPUT:

        - ``row_permutation`` -- a ``PermutationGroupElement``
        - ``column_permutation`` -- a ``PermutationGroupElement``

        OUTPUT: a matrix

        EXAMPLES: We create a matrix::

            sage: M = matrix(ZZ, [[1,0,0,0,0],[0,2,0,0,0],[0,0,3,0,0],[0,0,0,4,0],[0,0,0,0,5]])
            sage: M
            [1 0 0 0 0]
            [0 2 0 0 0]
            [0 0 3 0 0]
            [0 0 0 4 0]
            [0 0 0 0 5]

        Next of all, create a permutation group element and act on ``M``::

            sage: # needs sage.groups
            sage: G = PermutationGroup(['(1,2,3)(4,5)', '(1,2,3,4,5)'])
            sage: sigma, tau = G.gens()
            sage: sigma
            (1,2,3)(4,5)
            sage: M.with_permuted_rows_and_columns(sigma,tau)
            [2 0 0 0 0]
            [0 3 0 0 0]
            [0 0 0 0 1]
            [0 0 0 5 0]
            [0 0 4 0 0]"""
    def with_rescaled_col(self, Py_ssize_ti, s, Py_ssize_tstart_row=...) -> Any:
        """Matrix.with_rescaled_col(self, Py_ssize_t i, s, Py_ssize_t start_row=0)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3398)

        Replaces `i`-th col of ``self`` by `s` times `i`-th col of self, returning
        new matrix.

        EXAMPLES: We rescale the last column of a matrix over the
        integers::

            sage: a = matrix(ZZ, 2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: b = a.with_rescaled_col(2, -2); b
            [  0   1  -4]
            [  3   4 -10]

        The original matrix is unchanged::

            sage: a
            [0 1 2]
            [3 4 5]

        Adding a rational multiple is okay, and reassigning a variable is
        okay::

            sage: a = a.with_rescaled_col(1, 1/3); a
            [  0 1/3   2]
            [  3 4/3   5]"""
    def with_rescaled_row(self, Py_ssize_ti, s, Py_ssize_tstart_col=...) -> Any:
        """Matrix.with_rescaled_row(self, Py_ssize_t i, s, Py_ssize_t start_col=0)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3285)

        Replace `i`-th row of ``self`` by s times `i`-th row of self, returning
        new matrix.

        EXAMPLES: We rescale the second row of a matrix over the integers::

            sage: a = matrix(ZZ, 3, 2, range(6)); a
            [0 1]
            [2 3]
            [4 5]
            sage: b = a.with_rescaled_row(1, -2); b
            [ 0  1]
            [-4 -6]
            [ 4  5]

        The original matrix is unchanged::

            sage: a
            [0 1]
            [2 3]
            [4 5]

        Adding a rational multiple is okay, and reassigning a variable is
        okay::

            sage: a = a.with_rescaled_row(2, 1/3); a
            [  0   1]
            [  2   3]
            [4/3 5/3]"""
    def with_row_set_to_multiple_of_row(self, Py_ssize_ti, Py_ssize_tj, s) -> Any:
        """Matrix.with_row_set_to_multiple_of_row(self, Py_ssize_t i, Py_ssize_t j, s)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 3473)

        Set row i equal to s times row j, returning a new matrix.

        EXAMPLES: We change the second row to -3 times the first row::

            sage: a = matrix(ZZ, 2, 3, range(6)); a
            [0 1 2]
            [3 4 5]
            sage: b = a.with_row_set_to_multiple_of_row(1, 0, -3); b
            [ 0  1  2]
            [ 0 -3 -6]

        Note that the original matrix is unchanged::

            sage: a
            [0 1 2]
            [3 4 5]

        Adding a rational multiple is okay, and reassigning a variable is
        okay::

            sage: a = a.with_row_set_to_multiple_of_row(1, 0, 1/2); a
            [  0   1   2]
            [  0 1/2   1]"""
    def with_swapped_columns(self, c1, c2) -> Any:
        """Matrix.with_swapped_columns(self, c1, c2)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2621)

        Swap columns ``c1`` and ``c2`` of ``self`` and return a new matrix.

        INPUT:

        - ``c1``, ``c2`` -- integers specifying columns of ``self`` to interchange

        OUTPUT:

        A new matrix, identical to ``self`` except that columns ``c1`` and ``c2``
        are swapped.

        EXAMPLES:

        Remember that columns are numbered starting from zero. ::

            sage: A = matrix(QQ, 4, range(20))
            sage: A.with_swapped_columns(1, 2)
            [ 0  2  1  3  4]
            [ 5  7  6  8  9]
            [10 12 11 13 14]
            [15 17 16 18 19]

        Trying to swap a column with itself will succeed, but still return
        a new matrix. ::

            sage: A = matrix(QQ, 4, range(20))
            sage: B = A.with_swapped_columns(2, 2)
            sage: A == B
            True
            sage: A is B
            False

        The column specifications are checked. ::

            sage: A = matrix(4, range(20))
            sage: A.with_swapped_columns(-1, 2)
            Traceback (most recent call last):
            ...
            IndexError: matrix column index out of range

            sage: A.with_swapped_columns(2, 5)
            Traceback (most recent call last):
            ...
            IndexError: matrix column index out of range"""
    def with_swapped_rows(self, r1, r2) -> Any:
        """Matrix.with_swapped_rows(self, r1, r2)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2803)

        Swap rows ``r1`` and ``r2`` of ``self`` and return a new matrix.

        INPUT:

        - ``r1``, ``r2`` -- integers specifying rows of ``self`` to interchange

        OUTPUT:

        A new matrix, identical to ``self`` except that rows ``r1`` and ``r2``
        are swapped.

        EXAMPLES:

        Remember that rows are numbered starting from zero. ::

            sage: A = matrix(QQ, 4, range(20))
            sage: A.with_swapped_rows(1, 2)
            [ 0  1  2  3  4]
            [10 11 12 13 14]
            [ 5  6  7  8  9]
            [15 16 17 18 19]

        Trying to swap a row with itself will succeed, but still return
        a new matrix. ::

            sage: A = matrix(QQ, 4, range(20))
            sage: B = A.with_swapped_rows(2, 2)
            sage: A == B
            True
            sage: A is B
            False

        The row specifications are checked. ::

            sage: A = matrix(4, range(20))
            sage: A.with_swapped_rows(-1, 2)
            Traceback (most recent call last):
            ...
            IndexError: matrix row index out of range

            sage: A.with_swapped_rows(2, 5)
            Traceback (most recent call last):
            ...
            IndexError: matrix row index out of range"""
    def __bool__(self) -> bool:
        """True if self else False"""
    def __call__(self, *args, **kwargs) -> Any:
        """Matrix.__call__(self, *args, **kwargs)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 2495)

        Calling a matrix returns the result of calling each component.

        EXAMPLES::

            sage: # needs sage.symbolic
            sage: f(x,y) = x^2 + y
            sage: m = matrix([[f, f*f], [f^3, f^4]]); m
            [    (x, y) |--> x^2 + y (x, y) |--> (x^2 + y)^2]
            [(x, y) |--> (x^2 + y)^3 (x, y) |--> (x^2 + y)^4]
            sage: m(1, 2)
            [ 3  9]
            [27 81]
            sage: m(y=2, x=1)
            [ 3  9]
            [27 81]
            sage: m(2, 1)
            [  5  25]
            [125 625]"""
    def __delitem__(self, other) -> None:
        """Delete self[key]."""
    def __getitem__(self, key) -> Any:
        """Matrix.__getitem__(self, key)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 659)

        Return element, row, or slice of ``self``.

        INPUT:

        - ``key``- tuple (i,j) where i, j can be integers, slices or lists

        USAGE:

        - ``A[i, j]`` -- the i,j element (or elements, if i or j are
          slices or lists) of A, or

        - ``A[i:j]`` -- rows of A, according to slice notation

        EXAMPLES::

            sage: A = Matrix(Integers(2006),2,2,[-1,2,3,4])
            sage: A[0,0]
            2005
            sage: A[0]
            (2005, 2)

        The returned row is immutable (mainly to avoid confusion)::

            sage: A[0][0] = 123
            Traceback (most recent call last):
            ...
            ValueError: vector is immutable; please change a copy instead (use copy())
            sage: A[0].is_immutable()
            True
            sage: a = matrix(ZZ,3,range(9)); a
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: a[1,2]
            5
            sage: a[0]
            (0, 1, 2)
            sage: a[4,7]
            Traceback (most recent call last):
            ...
            IndexError: matrix index out of range
            sage: a[-1,0]
            6

        ::

            sage: a[2.7]
            Traceback (most recent call last):
            ...
            TypeError: index must be an integer
            sage: a[1, 2.7]
            Traceback (most recent call last):
            ...
            TypeError: index must be an integer
            sage: a[2.7, 1]
            Traceback (most recent call last):
            ...
            TypeError: index must be an integer

            sage: m = [(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)]; M = matrix(m)
            sage: M
            [ 1 -2 -1 -1  9]
            [ 1  8  6  2  2]
            [ 1  1 -1  1  4]
            [-1  2 -2 -1  4]

        Get the 2 x 2 submatrix of M, starting at row index and column
        index 1

        ::

            sage: M[1:3,1:3]
            [ 8  6]
            [ 1 -1]

        Get the 2 x 3 submatrix of M starting at row index and column index
        1::

            sage: M[1:3,[1..3]]
            [ 8  6  2]
            [ 1 -1  1]

        Get the second column of M::

            sage: M[:,1]
            [-2]
            [ 8]
            [ 1]
            [ 2]

        Get the first row of M::

            sage: M[0,:]
            [ 1 -2 -1 -1  9]

        More examples::

            sage: M[range(2),:]
            [ 1 -2 -1 -1  9]
            [ 1  8  6  2  2]
            sage: M[range(2),4]
            [9]
            [2]
            sage: M[range(3),range(5)]
            [ 1 -2 -1 -1  9]
            [ 1  8  6  2  2]
            [ 1  1 -1  1  4]

        ::

            sage: M[3,range(5)]
            [-1  2 -2 -1  4]
            sage: M[3,:]
            [-1  2 -2 -1  4]
            sage: M[3,4]
            4

            sage: M[-1,:]
            [-1  2 -2 -1  4]

            sage: A = matrix(ZZ,3,4, [3, 2, -5, 0, 1, -1, 1, -4, 1, 0, 1, -3]); A
            [ 3  2 -5  0]
            [ 1 -1  1 -4]
            [ 1  0  1 -3]

        ::

            sage: A[:,0:4:2]
            [ 3 -5]
            [ 1  1]
            [ 1  1]

        ::

            sage: A[1:,0:4:2]
            [1 1]
            [1 1]

            sage: A[2::-1,:]
            [ 1  0  1 -3]
            [ 1 -1  1 -4]
            [ 3  2 -5  0]

            sage: A[1:,3::-1]
            [-4  1 -1  1]
            [-3  1  0  1]

            sage: A[1:,3::-2]
            [-4 -1]
            [-3  0]

            sage: A[2::-1,3:1:-1]
            [-3  1]
            [-4  1]
            [ 0 -5]

        ::

            sage: A= matrix(3,4,[1, 0, -3, -1, 3, 0, -2, 1, -3, -5, -1, -5])
            sage: A[range(2,-1,-1),:]
            [-3 -5 -1 -5]
            [ 3  0 -2  1]
            [ 1  0 -3 -1]

        ::

            sage: A[range(2,-1,-1),range(3,-1,-1)]
            [-5 -1 -5 -3]
            [ 1 -2  0  3]
            [-1 -3  0  1]

        ::

            sage: A = matrix(2, [1, 2, 3, 4])
            sage: A[[0,0],[0,0]]
            [1 1]
            [1 1]

        ::

            sage: M = matrix(3, 4, range(12))
            sage: M[0:0, 0:0]
            []
            sage: M[0:0, 1:4]
            []
            sage: M[2:3, 3:3]
            []
            sage: M[range(2,2), :3]
            []
            sage: M[(1,2), 3]
            [ 7]
            [11]
            sage: M[(1,2),(0,1,1)]
            [4 5 5]
            [8 9 9]
            sage: m=[(1, -2, -1, -1), (1, 8, 6, 2), (1, 1, -1, 1), (-1, 2, -2, -1)]
            sage: M= matrix(m);M
            [ 1 -2 -1 -1]
            [ 1  8  6  2]
            [ 1  1 -1  1]
            [-1  2 -2 -1]

            sage: M[:2]
            [ 1 -2 -1 -1]
            [ 1  8  6  2]
            sage: M[:]
            [ 1 -2 -1 -1]
            [ 1  8  6  2]
            [ 1  1 -1  1]
            [-1  2 -2 -1]
            sage: M[1:3]
            [ 1  8  6  2]
            [ 1  1 -1  1]

            sage: A=matrix(QQ,10,range(100))
            sage: A[0:3]
            [ 0  1  2  3  4  5  6  7  8  9]
            [10 11 12 13 14 15 16 17 18 19]
            [20 21 22 23 24 25 26 27 28 29]
            sage: A[:2]
            [ 0  1  2  3  4  5  6  7  8  9]
            [10 11 12 13 14 15 16 17 18 19]
            sage: A[8:]
            [80 81 82 83 84 85 86 87 88 89]
            [90 91 92 93 94 95 96 97 98 99]
            sage: A[1:10:3]
            [10 11 12 13 14 15 16 17 18 19]
            [40 41 42 43 44 45 46 47 48 49]
            [70 71 72 73 74 75 76 77 78 79]
            sage: A[-1]
            (90, 91, 92, 93, 94, 95, 96, 97, 98, 99)
            sage: A[-1:-6:-2]
            [90 91 92 93 94 95 96 97 98 99]
            [70 71 72 73 74 75 76 77 78 79]
            [50 51 52 53 54 55 56 57 58 59]

            sage: A[3].is_immutable()
            True
            sage: A[1:3].is_immutable()
            True

        Slices that result in zero rows or zero columns are supported too::

            sage: m = identity_matrix(QQ, 4)[4:,:]
            sage: m.nrows(), m.ncols()
            (0, 4)
            sage: m * vector(QQ, 4)
            ()

        TESTS:

        If we're given lists as arguments, we should throw an
        appropriate error when those lists do not contain valid
        indices (:issue:`6569`)::

            sage: A = matrix(4, range(1,17))
            sage: A[[1.5], [1]]
            Traceback (most recent call last):
            ...
            IndexError: row indices must be integers
            sage: A[[1], [1.5]]
            Traceback (most recent call last):
            ...
            IndexError: column indices must be integers
            sage: A[[1.5]]
            Traceback (most recent call last):
            ...
            IndexError: row indices must be integers

        Before :issue:`6569` was fixed, sparse/dense matrices behaved
        differently due to implementation details. Given invalid
        indices, they should fail in the same manner. These tests
        just repeat the previous set with a sparse matrix::

            sage: A = matrix(4, range(1,17), sparse=True)
            sage: A[[1.5], [1]]
            Traceback (most recent call last):
            ...
            IndexError: row indices must be integers
            sage: A[[1], [1.5]]
            Traceback (most recent call last):
            ...
            IndexError: column indices must be integers
            sage: A[[1.5]]
            Traceback (most recent call last):
            ...
            IndexError: row indices must be integers

        Check that submatrices with a specified implementation have the
        same implementation::

            sage: # needs sage.libs.pari
            sage: M = MatrixSpace(GF(2), 3, 3, implementation='generic')
            sage: m = M(range(9))
            sage: type(m)
            <class 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>
            sage: parent(m)
            Full MatrixSpace of 3 by 3 dense matrices
             over Finite Field of size 2 (using Matrix_generic_dense)
            sage: type(m[:2,:2])
            <class 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>
            sage: parent(m[:2,:2])
            Full MatrixSpace of 2 by 2 dense matrices
             over Finite Field of size 2 (using Matrix_generic_dense)"""
    def __hash__(self) -> Any:
        """Matrix.__hash__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 6088)

        Return the hash of this matrix.

        Equal matrices should have equal hashes, even if one is sparse
        and the other is dense. We also ensure that zero matrices hash
        to zero and that scalar matrices have the same hash as the
        scalar.

        EXAMPLES::

            sage: m = matrix(2, range(24), sparse=True)
            sage: m.set_immutable()
            sage: hash(m)
            3327233128576517516  # 64-bit
            -373881460           # 32-bit

        ::

            sage: d = m.dense_matrix()
            sage: d.set_immutable()
            sage: hash(m) == hash(d)
            True

        ::

            sage: R.<x> = ZZ[]
            sage: M = matrix(R, 10, 20); M.set_immutable()
            sage: hash(M)
            0
            sage: M = matrix(R, 10, 10, x); M.set_immutable()
            sage: hash(M) == hash(x)
            True"""
    def __invert__(self) -> Any:
        """Matrix.__invert__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5748)

        Return the inverse of this matrix, as a matrix over the fraction
        field.

        Raises a :exc:`ZeroDivisionError` if the matrix has zero
        determinant, and raises an :exc:`ArithmeticError`, if the
        inverse doesn't exist because the matrix is nonsquare. Also, note,
        e.g., that the inverse of a matrix over `\\ZZ` is
        always a matrix defined over `\\QQ` (even if the
        entries are integers).

        EXAMPLES::

            sage: A = MatrixSpace(ZZ, 2)([1,1,3,5])
            sage: ~A
            [ 5/2 -1/2]
            [-3/2  1/2]
            sage: A.__invert__()
            [ 5/2 -1/2]
            [-3/2  1/2]

        Even if the inverse lies in the base field, the result is still a
        matrix over the fraction field.

        ::

            sage: I = MatrixSpace(ZZ, 2)(1)  # identity matrix
            sage: ~I
            [1 0]
            [0 1]
            sage: (~I).parent()
            Full MatrixSpace of 2 by 2 dense matrices over Rational Field

        This is analogous to the situation for ring elements, e.g., for
        `\\ZZ` we have::

            sage: parent(~1)
            Rational Field

        A matrix with 0 rows and 0 columns is invertible (see :issue:`3734`)::

            sage: M = MatrixSpace(RR, 0, 0)(0); M
            []
            sage: M.determinant()
            1.00000000000000
            sage: M.is_invertible()
            True
            sage: M.inverse() == M
            True

        Matrices over the integers modulo a composite modulus::

            sage: m = matrix(Zmod(49), 2, [2,1,3,3])
            sage: type(m)
            <class 'sage.matrix.matrix_modn_dense_float.Matrix_modn_dense_float'>
            sage: ~m
            [ 1 16]
            [48 17]
            sage: m = matrix(Zmod(2^100), 2, [2,1,3,3])
            sage: type(m)
            <class 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>
            sage: (~m)*m                                                                # needs sage.libs.pari
            [1 0]
            [0 1]
            sage: ~m                                                                    # needs sage.libs.pari
            [                              1  422550200076076467165567735125]
            [1267650600228229401496703205375  422550200076076467165567735126]

        Matrices over `p`-adics. See :issue:`17272` ::

            sage: # needs sage.rings.padics
            sage: R = ZpCA(5, 5, print_mode='val-unit')
            sage: A = matrix(R, 3, 3, [250,2369,1147,106,927,362,90,398,2483])
            sage: A
            [5^3 * 2 + O(5^5)    2369 + O(5^5)    1147 + O(5^5)]
            [    106 + O(5^5)     927 + O(5^5)     362 + O(5^5)]
            [ 5 * 18 + O(5^5)     398 + O(5^5)    2483 + O(5^5)]
            sage: ~A
            [5 * 212 + O(5^5)    3031 + O(5^5)    2201 + O(5^5)]
            [   1348 + O(5^5) 5 * 306 + O(5^5)    2648 + O(5^5)]
            [   1987 + O(5^5) 5 * 263 + O(5^5)     154 + O(5^5)]

        This matrix is not invertible::

            sage: m = matrix(Zmod(9), 2, [2,1,3,3])
            sage: ~m
            Traceback (most recent call last):
            ...
            ZeroDivisionError: input matrix must be nonsingular

        Check to make sure that :issue:`2256` is still fixed::

            sage: M = MatrixSpace(CC, 2)(-1.10220440881763)
            sage: N = ~M
            sage: (N*M).norm()
            0.9999999999999999

        Check that :issue:`28402` is fixed::

            sage: B = matrix(RR, [[1/6, -1/24, -1/30, 1/120,1/12, 0, 0, 0, 0],
            ....:                 [-1/24,1/60,1/60, 1/420, -1/24, 0, 0, 0, 0],
            ....:                 [-1/30,1/60, 2/105, 1/140, -1/20, 0, 0, 0, 0],
            ....:                 [1/120, 1/420, 1/140, 13/1260, -1/40, 0, 0, 0, 0],
            ....:                 [1/12, -1/24, -1/20, -1/40, 1/3, -1/24, -1/30, 1/120,1/12],
            ....:                 [0, 0, 0, 0, -1/24,1/60,1/60, 1/420, -1/24],
            ....:                 [0, 0, 0, 0, -1/30,1/60, 2/105, 1/140, -1/20],
            ....:                 [0, 0, 0, 0, 1/120, 1/420, 1/140, 13/1260, -1/40],
            ....:                 [0, 0, 0, 0,1/12, -1/24, -1/20, -1/40, 1/6]],
            ....:           sparse=True)
            sage: (B.inverse()*B).norm(1)  # rel tol 2e-12
            1.0
            sage: B = matrix(QQ, [[1/6, -1/24, -1/30, 1/120,1/12, 0, 0, 0, 0],
            ....:                 [-1/24,1/60,1/60, 1/420, -1/24, 0, 0, 0, 0],
            ....:                 [-1/30,1/60, 2/105, 1/140, -1/20, 0, 0, 0, 0],
            ....:                 [1/120, 1/420, 1/140, 13/1260, -1/40, 0, 0, 0, 0],
            ....:                 [1/12, -1/24, -1/20, -1/40, 1/3, -1/24, -1/30, 1/120,1/12],
            ....:                 [0, 0, 0, 0, -1/24,1/60,1/60, 1/420, -1/24],
            ....:                 [0, 0, 0, 0, -1/30,1/60, 2/105, 1/140, -1/20],
            ....:                 [0, 0, 0, 0, 1/120, 1/420, 1/140, 13/1260, -1/40],
            ....:                 [0, 0, 0, 0,1/12, -1/24, -1/20, -1/40, 1/6]],
            ....:           sparse=True)
            sage: (B.inverse()*B).norm(1)
            1.0"""
    @overload
    def __iter__(self) -> Any:
        """Matrix.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 647)

        Return an iterator for the rows of ``self``.

        EXAMPLES::

            sage: m = matrix(2,[1,2,3,4])
            sage: next(m.__iter__())
            (1, 2)"""
    @overload
    def __iter__(self) -> Any:
        """Matrix.__iter__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 647)

        Return an iterator for the rows of ``self``.

        EXAMPLES::

            sage: m = matrix(2,[1,2,3,4])
            sage: next(m.__iter__())
            (1, 2)"""
    def __mod__(self, p) -> Any:
        """Matrix.__mod__(self, p)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5400)

        Return matrix mod `p`, returning again a matrix over the
        same base ring.

        .. NOTE::

           Use :meth:`mod` to obtain a matrix over the residue class ring
           modulo `p`.

        EXAMPLES::

            sage: M = Matrix(ZZ, 2, 2, [5, 9, 13, 15])
            sage: M % 7
            [5 2]
            [6 1]
            sage: parent(M % 7)
            Full MatrixSpace of 2 by 2 dense matrices over Integer Ring"""
    @overload
    def __neg__(self) -> Any:
        """Matrix.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5732)

        Return the negative of ``self``.

        EXAMPLES::

            sage: a = matrix(ZZ,2,range(4))
            sage: a.__neg__()
            [ 0 -1]
            [-2 -3]
            sage: -a
            [ 0 -1]
            [-2 -3]"""
    @overload
    def __neg__(self) -> Any:
        """Matrix.__neg__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 5732)

        Return the negative of ``self``.

        EXAMPLES::

            sage: a = matrix(ZZ,2,range(4))
            sage: a.__neg__()
            [ 0 -1]
            [-2 -3]
            sage: -a
            [ 0 -1]
            [-2 -3]"""
    @overload
    def __pos__(self) -> Any:
        """Matrix.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 6019)

        Return +self, which is just self, of course.

        EXAMPLES::

            sage: a = matrix(ZZ,2,range(4))
            sage: +a
            [0 1]
            [2 3]
            sage: a.__pos__()
            [0 1]
            [2 3]"""
    @overload
    def __pos__(self) -> Any:
        """Matrix.__pos__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 6019)

        Return +self, which is just self, of course.

        EXAMPLES::

            sage: a = matrix(ZZ,2,range(4))
            sage: +a
            [0 1]
            [2 3]
            sage: a.__pos__()
            [0 1]
            [2 3]"""
    def __pow__(self, n, ignored) -> Any:
        """Matrix.__pow__(self, n, ignored)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 6035)

        EXAMPLES::

            sage: MS = MatrixSpace(QQ, 3, 3)
            sage: A = MS([0, 0, 1, 1, 0, '-2/11', 0, 1, '-3/11'])
            sage: A * A^(-1) == 1
            True
            sage: A^4
            [      -3/11     -13/121   1436/1331]
            [    127/121   -337/1331 -4445/14641]
            [    -13/121   1436/1331 -8015/14641]
            sage: A.__pow__(4)
            [      -3/11     -13/121   1436/1331]
            [    127/121   -337/1331 -4445/14641]
            [    -13/121   1436/1331 -8015/14641]

        Sage follows Python's convention 0^0 = 1, as each of the following
        examples show::

            sage: a = Matrix([[1,0],[0,0]]); a
            [1 0]
            [0 0]
            sage: a^0 # lower right entry is 0^0
            [1 0]
            [0 1]
            sage: Matrix([[0]])^0
            [1]
            sage: 0^0
            1

        Non-integer (symbolic) exponents are also supported::

            sage: k = var('k')                                                          # needs sage.symbolic
            sage: A = matrix([[2, -1], [1,  0]])
            sage: A^(2*k+1)                                                             # needs sage.symbolic
            [ 2*k + 2 -2*k - 1]
            [ 2*k + 1     -2*k]"""
    def __reduce__(self) -> Any:
        """Matrix.__reduce__(self)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 1615)

        EXAMPLES::

            sage: a = matrix(Integers(8),3,range(9))
            sage: a == loads(dumps(a))
            True"""
    def __rmod__(self, other):
        """Return value%self."""
    def __rpow__(self, other):
        """Return pow(value, self, mod)."""
    def __setitem__(self, key, value) -> Any:
        """Matrix.__setitem__(self, key, value)

        File: /build/sagemath/src/sage/src/sage/matrix/matrix0.pyx (starting at line 1110)

        Set elements of this matrix to values given in value.

        INPUT:

        - ``key`` -- any legal indexing (i.e., such that self[key] works)

        - ``value`` -- values that are used to set the elements indicated by key

        EXAMPLES::

            sage: A = Matrix(Integers(2006),2,2,[-1,2,3,4])
            sage: A[0,0]=43; A
            [43  2]
            [ 3  4]

            sage: A[0]=[10,20]; A
            [10 20]
            [ 3  4]

            sage: M=matrix([(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)]); M
            [ 1 -2 -1 -1  9]
            [ 1  8  6  2  2]
            [ 1  1 -1  1  4]
            [-1  2 -2 -1  4]

        Set the 2 x 2 submatrix of M, starting at row index and column
        index 1::

            sage: M[1:3,1:3] = [[1,0],[0,1]]; M
            [ 1 -2 -1 -1  9]
            [ 1  1  0  2  2]
            [ 1  0  1  1  4]
            [-1  2 -2 -1  4]

        Set the 2 x 3 submatrix of M starting at row index and column
        index 1::

            sage: M[1:3,[1..3]] = M[2:4,0:3]; M
            [ 1 -2 -1 -1  9]
            [ 1  1  0  1  2]
            [ 1 -1  2 -2  4]
            [-1  2 -2 -1  4]

        Set part of the first column of M::

            sage: M[1:,0]=[[2],[3],[4]]; M
            [ 1 -2 -1 -1  9]
            [ 2  1  0  1  2]
            [ 3 -1  2 -2  4]
            [ 4  2 -2 -1  4]

        Or do a similar thing with a vector::

            sage: M[1:,0]=vector([-2,-3,-4]); M
            [ 1 -2 -1 -1  9]
            [-2  1  0  1  2]
            [-3 -1  2 -2  4]
            [-4  2 -2 -1  4]

        Or a constant::

            sage: M[1:,0]=30; M
            [ 1 -2 -1 -1  9]
            [30  1  0  1  2]
            [30 -1  2 -2  4]
            [30  2 -2 -1  4]


        Set the first row of M::

            sage: M[0,:]=[[20,21,22,23,24]]; M
            [20 21 22 23 24]
            [30  1  0  1  2]
            [30 -1  2 -2  4]
            [30  2 -2 -1  4]
            sage: M[0,:]=vector([0,1,2,3,4]); M
            [ 0  1  2  3  4]
            [30  1  0  1  2]
            [30 -1  2 -2  4]
            [30  2 -2 -1  4]
            sage: M[0,:]=-3; M
            [-3 -3 -3 -3 -3]
            [30  1  0  1  2]
            [30 -1  2 -2  4]
            [30  2 -2 -1  4]


            sage: A = matrix(ZZ,3,4, [3, 2, -5, 0, 1, -1, 1, -4, 1, 0, 1, -3]); A
            [ 3  2 -5  0]
            [ 1 -1  1 -4]
            [ 1  0  1 -3]

        We can use the step feature of slices to set every other column::

            sage: A[:,0:3:2] = 5; A
            [ 5  2  5  0]
            [ 5 -1  5 -4]
            [ 5  0  5 -3]

            sage: A[1:,0:4:2] = [[100,200],[300,400]]; A
            [  5   2   5   0]
            [100  -1 200  -4]
            [300   0 400  -3]

        We can also count backwards to flip the matrix upside down.

        ::

            sage: A[::-1,:]=A; A
            [300   0 400  -3]
            [100  -1 200  -4]
            [  5   2   5   0]


            sage: A[1:,3::-1]=[[2,3,0,1],[9,8,7,6]]; A
            [300   0 400  -3]
            [  1   0   3   2]
            [  6   7   8   9]

            sage: A[1:,::-2] = A[1:,::2]; A
            [300   0 400  -3]
            [  1   3   3   1]
            [  6   8   8   6]

            sage: A[::-1,3:1:-1] = [[4,3],[1,2],[-1,-2]]; A
            [300   0  -2  -1]
            [  1   3   2   1]
            [  6   8   3   4]


        TESTS::

            sage: A = MatrixSpace(ZZ,3)(range(9)); A
            [0 1 2]
            [3 4 5]
            [6 7 8]
            sage: A[1,2]=100; A
            [  0   1   2]
            [  3   4 100]
            [  6   7   8]
            sage: A[0]=(10,20,30); A
            [ 10  20  30]
            [  3   4 100]
            [  6   7   8]
            sage: A[4,7]=45
            Traceback (most recent call last):
            ...
            IndexError: index out of range
            sage: A[-1,0]=63; A[-1,0]
            63
            sage: A[2.7]=3
            Traceback (most recent call last):
            ...
            TypeError: index must be an integer or slice or a tuple/list of integers and slices
            sage: A[1, 2.7]=3
            Traceback (most recent call last):
            ...
            TypeError: index must be an integer or slice or a tuple/list of integers and slices
            sage: A[2.7, 1]=3
            Traceback (most recent call last):
            ...
            TypeError: index must be an integer or slice or a tuple/list of integers and slices
            sage: A.set_immutable()
            sage: A[0,0] = 7
            Traceback (most recent call last):
            ...
            ValueError: matrix is immutable; please change a copy instead (i.e., use copy(M) to change a copy of M).
            sage: A=matrix([[1,2],[3,4]]); B=matrix([[1,3],[5,7]])
            sage: A[1:2,1:2]=B[1:2,1:2]
            sage: A
            [1 2]
            [3 7]
            sage: A=matrix([[1,2],[3,4]]); B=matrix([[1,3],[5,7]])
            sage: A[1,0:1]=B[1,1:2]
            sage: A
            [1 2]
            [7 4]


        More examples::

            sage: M[range(2),:]=[[1..5], [6..10]]; M
            [ 1  2  3  4  5]
            [ 6  7  8  9 10]
            [30 -1  2 -2  4]
            [30  2 -2 -1  4]

            sage: M[range(2),4]=0; M
            [ 1  2  3  4  0]
            [ 6  7  8  9  0]
            [30 -1  2 -2  4]
            [30  2 -2 -1  4]

            sage: M[range(3),range(5)]=M[range(1,4), :]; M
            [ 6  7  8  9  0]
            [30 -1  2 -2  4]
            [30  2 -2 -1  4]
            [30  2 -2 -1  4]


            sage: M[3,range(5)]=vector([-2,3,4,-5,4]); M
            [ 6  7  8  9  0]
            [30 -1  2 -2  4]
            [30  2 -2 -1  4]
            [-2  3  4 -5  4]
            sage: M[3,:]=2*M[2,:]; M
            [ 6  7  8  9  0]
            [30 -1  2 -2  4]
            [30  2 -2 -1  4]
            [60  4 -4 -2  8]
            sage: M[3,4]=M[3,2]; M
            [ 6  7  8  9  0]
            [30 -1  2 -2  4]
            [30  2 -2 -1  4]
            [60  4 -4 -2 -4]

            sage: M[-1,:]=M[-3,:]; M
            [ 6  7  8  9  0]
            [30 -1  2 -2  4]
            [30  2 -2 -1  4]
            [30 -1  2 -2  4]


            sage: A= matrix(3,4,[1, 0, -3, -1, 3, 0, -2, 1, -3, -5, -1, -5]); A
            [ 1  0 -3 -1]
            [ 3  0 -2  1]
            [-3 -5 -1 -5]

            sage: A[range(2,-1,-1),:]=A; A
            [-3 -5 -1 -5]
            [ 3  0 -2  1]
            [ 1  0 -3 -1]

            sage: A[range(2,-1,-1),range(3,-1,-1)]=A; A
            [-1 -3  0  1]
            [ 1 -2  0  3]
            [-5 -1 -5 -3]

            sage: A = matrix(2, [1, 2, 3, 4])
            sage: A[[0,0],[0,0]]=10; A
            [10  2]
            [ 3  4]

            sage: M = matrix(3, 4, range(12))
            sage: M[0:0, 0:0]=20; M
            [ 0  1  2  3]
            [ 4  5  6  7]
            [ 8  9 10 11]
            sage: M[0:0, 1:4]=20; M
            [ 0  1  2  3]
            [ 4  5  6  7]
            [ 8  9 10 11]
            sage: M[2:3, 3:3]=20; M
            [ 0  1  2  3]
            [ 4  5  6  7]
            [ 8  9 10 11]
            sage: M[range(2,2), :3]=20; M
            [ 0  1  2  3]
            [ 4  5  6  7]
            [ 8  9 10 11]
            sage: M[(1,2), 3]=vector([-1,-2]); M
            [ 0  1  2  3]
            [ 4  5  6 -1]
            [ 8  9 10 -2]
            sage: M[(1,2),(0,1,1)]=[[-1,-2,-3],[-4,-5,-6]]; M
            [ 0  1  2  3]
            [-1 -3  6 -1]
            [-4 -6 10 -2]
            sage: M=matrix([(1, -2, -1, -1), (1, 8, 6, 2), (1, 1, -1, 1), (-1, 2, -2, -1)]); M
            [ 1 -2 -1 -1]
            [ 1  8  6  2]
            [ 1  1 -1  1]
            [-1  2 -2 -1]

            sage: M[:2]=M[2:]; M
            [ 1  1 -1  1]
            [-1  2 -2 -1]
            [ 1  1 -1  1]
            [-1  2 -2 -1]

            sage: M[:] = M.transpose(); M
            [ 1 -1  1 -1]
            [ 1  2  1  2]
            [-1 -2 -1 -2]
            [ 1 -1  1 -1]
            sage: M = matrix(ZZ,4,range(16)); M
            [ 0  1  2  3]
            [ 4  5  6  7]
            [ 8  9 10 11]
            [12 13 14 15]
            sage: M[::2]=M[::-2]; M
            [12 13 14 15]
            [ 4  5  6  7]
            [ 4  5  6  7]
            [12 13 14 15]
            sage: M[::2]=2; M
            [ 2  2  2  2]
            [ 4  5  6  7]
            [ 2  2  2  2]
            [12 13 14 15]

            sage: M[2:]=10; M
            [ 2  2  2  2]
            [ 4  5  6  7]
            [10 10 10 10]
            [10 10 10 10]

            sage: M=matrix(3,1,[1,2,3]); M
            [1]
            [2]
            [3]
            sage: M[1] = vector([20]); M
            [ 1]
            [20]
            [ 3]
            sage: M = matrix(3, 2, srange(6)); M[1] = 15; M
            [ 0  1]
            [15 15]
            [ 4  5]
            sage: M = matrix(3, 1, srange(3)); M[1] = 15; M
            [ 0]
            [15]
            [ 2]
            sage: M = matrix(3, 1, srange(3)); M[1] = [15]; M
            [ 0]
            [15]
            [ 2]"""
